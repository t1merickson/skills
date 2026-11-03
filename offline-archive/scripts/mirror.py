#!/usr/bin/env python3
"""Mirror a bounded set of same-origin pages and their assets to a docroot.

This is the mechanical part of an offline archive: polite fetch loop, retry with
backoff and jitter, URL to local path mapping, transitive asset discovery in
HTML, CSS, and JS, resume state, and a manifest with sha256 per file. It does
not decide scope: pass seeds, allowed hosts, and an optional path prefix.

    mirror.py --out DOCROOT --host example.com [--host cdn.example.com]
              [--prefix /docs] [--exclude REGEX] [--max-requests 2000] [--delay 0.5]
              https://example.com/ https://example.com/about

Output layout: DOCROOT/<host>/<path>, so a static server per host serves the
original absolute paths without rewriting. State lives in DOCROOT/.mirror/.
Re-running resumes: fetched URLs are skipped unless --refetch is given.

Stdlib only. Exit 0 when every queued URL was fetched or recorded as failed;
exit 2 when the request budget stopped the crawl early.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

TEXT_TYPES = ("text/", "application/javascript", "application/json",
              "application/xml", "application/x-javascript", "image/svg")

ASSET_EXT = (r"js|mjs|css|json|map|png|jpe?g|gif|svg|webp|avif|ico|woff2?|ttf|otf|eot|"
             r"mp4|webm|mp3|wav|ogg|csv|tsv|txt|xml|pdf|glsl|frag|vert|wasm|geojson|md")

HTML_ATTR_RE = re.compile(
    r"""\b(?:src|href|poster|data-src)\s*=\s*["']([^"'#>\s]+)["']""", re.I)
SRCSET_RE = re.compile(r"""srcset\s*=\s*["']([^"']+)["']""", re.I)
CSS_URL_RE = re.compile(r"""url\(\s*["']?([^"')\s]+)["']?\s*\)""", re.I)
CSS_IMPORT_RE = re.compile(r"""@import\s+["']([^"']+)["']""", re.I)
QUOTED_ASSET_RE = re.compile(
    r"""["'`(]([^"'`()\s{}<>]+?\.(?:%s))(?:\?[^"'`()\s]*)?["'`)]""" % ASSET_EXT, re.I)
JS_IMPORT_RE = re.compile(r"""(?:from|import)\s*\(?\s*["']([./][^"']+)["']""")


class Mirror:
    def __init__(self, out, hosts, prefix, delay, max_requests, refetch, retries,
                 exclude=None):
        self.out = os.path.abspath(out)
        self.hosts = set(hosts)
        self.prefix = prefix or ""
        self.exclude = [re.compile(p) for p in (exclude or [])]
        self.delay = delay
        self.max_requests = max_requests
        self.refetch = refetch
        self.retries = retries
        self.state_dir = os.path.join(self.out, ".mirror")
        os.makedirs(self.state_dir, exist_ok=True)
        self.manifest_path = os.path.join(self.state_dir, "manifest.json")
        self.manifest = self._load(self.manifest_path, {})
        self.failed_path = os.path.join(self.state_dir, "failed.json")
        self.failed = self._load(self.failed_path, {})
        self.seen = set(self.manifest) | set(self.failed)
        self.queue = []
        self.requests = 0
        self.user_agent = UA

    @staticmethod
    def _load(path, default):
        if os.path.exists(path):
            with open(path) as fh:
                return json.load(fh)
        return default

    def _save(self):
        for path, data in ((self.manifest_path, self.manifest), (self.failed_path, self.failed)):
            tmp = path + ".tmp"
            with open(tmp, "w") as fh:
                json.dump(data, fh, indent=1, sort_keys=True)
            os.replace(tmp, path)

    # ---- URL handling -------------------------------------------------
    def norm(self, url):
        url, _ = urllib.parse.urldefrag(url)
        return url

    def in_scope(self, url):
        p = urllib.parse.urlsplit(url)
        if p.scheme not in ("http", "https") or p.hostname not in self.hosts:
            return False
        if any(rx.search(url) for rx in self.exclude):
            return False
        return p.path.startswith(self.prefix) or not self.prefix

    def local_path(self, url):
        p = urllib.parse.urlsplit(url)
        path = urllib.parse.unquote(p.path) or "/"
        if path.endswith("/"):
            path += "index.html"
        elif "." not in os.path.basename(path):
            path += "/index.html"
        rel = path.lstrip("/")
        if p.query:
            stem, ext = os.path.splitext(rel)
            q = re.sub(r"[^A-Za-z0-9._-]", "_", p.query)
            if len(q) > 120:  # filesystems cap names at 255 bytes; keep it unique, not readable
                q = q[:60] + "_" + hashlib.sha1(p.query.encode()).hexdigest()[:16]
            rel = stem + "__q" + q + ext
        return os.path.join(self.out, p.hostname, rel)

    def enqueue(self, url, referer=None):
        url = self.norm(url.strip())
        if not url or url.startswith(("data:", "mailto:", "javascript:", "tel:", "blob:")):
            return
        if any(ch in url for ch in " \t\n\r{}<>"):
            return
        if referer:
            url = urllib.parse.urljoin(referer, url)
        if not self.in_scope(url):
            return
        if url in self.seen and not self.refetch:
            return
        self.seen.add(url)
        self.queue.append((url, referer))

    # ---- discovery ----------------------------------------------------
    def discover(self, text, url, ctype):
        if "html" in ctype:
            for m in HTML_ATTR_RE.finditer(text):
                self.enqueue(m.group(1), url)
            for m in SRCSET_RE.finditer(text):
                for cand in m.group(1).split(","):
                    self.enqueue(cand.strip().split(" ")[0], url)
            for m in CSS_URL_RE.finditer(text):
                self.enqueue(m.group(1), url)
        if "css" in ctype or "html" in ctype:
            for m in CSS_URL_RE.finditer(text):
                self.enqueue(m.group(1), url)
            for m in CSS_IMPORT_RE.finditer(text):
                self.enqueue(m.group(1), url)
        if "javascript" in ctype or "html" in ctype:
            for m in QUOTED_ASSET_RE.finditer(text):
                self.enqueue(m.group(1), url)
            for m in JS_IMPORT_RE.finditer(text):
                self.enqueue(m.group(1), url)

    # ---- fetch --------------------------------------------------------
    def fetch(self, url, referer):
        headers = {"User-Agent": self.user_agent, "Accept": "*/*"}
        if referer:
            headers["Referer"] = referer
        backoff = 1.0
        for attempt in range(self.retries + 1):
            self.requests += 1
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=30) as resp:
                    body = resp.read()
                    return body, resp.headers.get("Content-Type", ""), resp.geturl()
            except urllib.error.HTTPError as e:
                if e.code in (429, 500, 502, 503, 504) and attempt < self.retries:
                    retry_after = e.headers.get("Retry-After") if e.headers else None
                    wait = float(retry_after) if retry_after and retry_after.isdigit() else backoff
                    time.sleep(min(wait, 60) + random.uniform(0, 0.5))
                    backoff = min(backoff * 2, 60)
                    continue
                raise
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                if attempt < self.retries:
                    time.sleep(backoff + random.uniform(0, 0.5))
                    backoff = min(backoff * 2, 60)
                    continue
                raise

    def run(self, seeds):
        for s in seeds:
            self.enqueue(s)
        budget_hit = False
        try:
            while self.queue:
                if self.requests >= self.max_requests:
                    budget_hit = True
                    break
                url, referer = self.queue.pop(0)
                try:
                    body, ctype, final = self.fetch(url, referer)
                except Exception as e:  # noqa: BLE001
                    self.failed[url] = str(e)
                    print(f"FAIL {url} ({e})", file=sys.stderr)
                    continue
                path = self.local_path(url)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "wb") as fh:
                    fh.write(body)
                self.manifest[url] = {
                    "path": os.path.relpath(path, self.out),
                    "bytes": len(body),
                    "sha256": hashlib.sha256(body).hexdigest(),
                    "content_type": ctype,
                    "final_url": final,
                    "fetched": time.strftime("%Y-%m-%dT%H:%M:%S"),
                }
                self.failed.pop(url, None)
                print(f"ok   {len(body):>9}  {url}")
                if any(ctype.startswith(t) for t in TEXT_TYPES):
                    try:
                        self.discover(body.decode("utf-8", "replace"), final, ctype)
                    except Exception as e:  # noqa: BLE001
                        print(f"warn discovery failed for {url}: {e}", file=sys.stderr)
                if len(self.manifest) % 25 == 0:
                    self._save()
                time.sleep(self.delay + random.uniform(0, self.delay))
        finally:
            self._save()
        print(f"\nfetched {len(self.manifest)} files, {len(self.failed)} failed, "
              f"{self.requests} requests, queue left {len(self.queue)}")
        return 2 if budget_hit else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("seeds", nargs="+")
    ap.add_argument("--out", required=True, help="docroot directory")
    ap.add_argument("--host", action="append", required=True, help="allowed host (repeatable)")
    ap.add_argument("--prefix", default="", help="only paths under this prefix")
    ap.add_argument("--exclude", action="append", default=[],
                    help="skip URLs matching this regex (repeatable); use to defer "
                         "a bulk asset class to a later pass")
    ap.add_argument("--delay", type=float, default=0.5, help="base delay between requests, seconds")
    ap.add_argument("--max-requests", type=int, default=2000)
    ap.add_argument("--retries", type=int, default=3)
    ap.add_argument("--refetch", action="store_true", help="ignore resume state")
    ap.add_argument("--user-agent", default=UA,
                    help="User-Agent header; media hosts like Wikimedia ask for a descriptive one with contact info")
    a = ap.parse_args()
    m = Mirror(a.out, a.host, a.prefix, a.delay, a.max_requests, a.refetch, a.retries,
               a.exclude)
    m.user_agent = a.user_agent
    sys.exit(m.run(a.seeds))


if __name__ == "__main__":
    main()
