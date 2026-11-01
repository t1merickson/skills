---
name: offline-archive
description: Preserve a legitimately accessible web page, tool, or bounded site as a self-contained personal-use archive with polite acquisition, provenance, and network-blocked replay. Also use when hunting for more pages or sources to archive and judging whether the supply is exhausted.
---

# Offline archive

Web archives usually begin with a broad “keep this URL” and then reveal a second question: what should survive besides the core experience? If the user says nothing about cleanup, use the defaults below rather than asking again. Confirm the URL, output location, breadth, and fidelity needs. Do not assume archives belong inside the current project; resolve the user’s configured archival root first. Treat authenticated or blocked material as a stop, not an invitation to invent a bypass.

## Default cleanup

Unless told otherwise:

- Strip: tracking and analytics, ad containers, share widgets, cookie banners, newsletter and promo popups, site chrome noise unrelated to the content.
- Keep: all graphs, charts, images, video, and their data.
- Put image and video caption text into the page as visible text next to the media.

## Finding sources

When asked for more sources or whether the supply is exhausted, report a table before saying "exhausted": each source tried, items found per source, and sources not tried yet. "Exhausted" means the untried list is empty or every item on it is ruled out with a reason.

## Plan before fetching

Identify the site architecture first; strategy follows from what the site is. Prefer an available source repository over scraping deployed bundles, then compare source commit and built asset hashes when possible. A static mirror, an ES-module toy, a Vite SPA, and a Next.js application fail offline for different reasons.

For a bounded crawl, inspect sitemaps and `robots.txt` as planning evidence. Stop on access denial, sustained throttling, or a scope that expands materially beyond the approved request.

Create a request plan and manifest before a whole-site crawl:

- allowed origins and paths;
- sitemap or known inventory;
- estimated pages/assets/bytes;
- concurrency, delay, retry/backoff, and maximum request budget;
- resume state and deduplication key;
- user agent/contact convention where appropriate;
- capture date and tool versions.

The fetch loop is mechanical and already written. Use it rather than writing a crawler:

```bash
<skill-directory>/scripts/mirror.py --out <docroot> --host <host> [--prefix /path] [--exclude REGEX] <seed-urls...>
<skill-directory>/scripts/verify.sh <docroot>            # serve locally, counts, failed URLs
<skill-directory>/scripts/source.sh <docroot> <url> [scope]   # SOURCE.md skeleton from the manifest
```

`mirror.py` is stdlib only and does: same-origin transitive discovery through HTML, CSS, `srcset`, and quoted asset strings in JS; retry with capped backoff, jitter, and `Retry-After`; resume state and a sha256 manifest under `.mirror/`. `--exclude` skips URLs matching a regex, which is how you defer a bulk asset class (thumbnail sets, media libraries) to a later pass or out of scope entirely. It does not render JavaScript, follow cross-origin assets unless listed with `--host`, or rewrite paths; serve per-host docroots instead. When a site needs a headless browser or source rebuild, that is a judgment call recorded in `SOURCE.md`, and the recipe goes in `references/site-recipes.md`. Extend the script for a general gap; do not fork it per site.

Use low concurrency, server-directed retry delays, capped exponential backoff, and resumability. Add jitter: a perfectly regular request cadence is conspicuously automated even when slow. Build resume state before the long run; a crawl that dies at 80% and refetches everything is the impolite outcome. Avoid refetching unchanged assets. For evidentiary or long-lived captures, consider WARC alongside the browsable derivative.

## Preserve behavior deliberately

Capture HTML, styles, fonts, media, modules, JSON payloads, service-worker references, and runtime-generated assets within scope. URLs hide inside CSS, serialized hydration data, template literals, and copied public assets—not only in HTML attributes. Rewrite them to relative paths or data URLs.

Preserve the logic, not only the first paint. Live API behavior becomes an explicit captured snapshot or a clearly disabled feature; install a deny-by-default network shim before application chunks run. A page that quietly falls back to production is not an offline archive.

Prefer rebuilding from source when available and record the relationship between source commit, production asset hashes, and archive build. Do not patch opaque minified code unless a smaller, testable seam is unavailable.

Architecture-specific traps belong in [references/site-recipes.md](references/site-recipes.md). Verify them against the current site rather than assuming a framework from old filenames. When a new architecture costs real debugging, add the smallest reusable recipe so the trap is not paid for twice.

## Provenance

Place `SOURCE.md` beside the archive with original URL, retrieval date, scope, request policy, capture tool/version, source commit when known, transformations, omitted features/content, licenses, integrity hashes, known failures, and replay instructions. Preserve superseded captures by project policy; do not accumulate them blindly.

## Verify offline

Do not call the archive done until this checklist passes. A pass from `verify.sh` alone is not enough; it has missed failed graphs and cross-domain media before.

1. Scroll the full page in the live site and in the archive so lazy content loads.
2. Every chart and graph renders with data in the archive, not an empty frame.
3. Images, video, and fonts served from other domains (CDNs, media hosts) were captured with `--host` and load offline.
4. Replay with the network blocked and look at it. Compare against the live page, section by section.

Report any item that failed instead of rounding it to done.

Serve or open the archive through its supported local route with all HTTP, HTTPS, and WebSocket traffic blocked. Clear or isolate browser caches first; otherwise a broken archive can look complete because the live site's service worker is helping. The verifier exits non-zero for any attempted network access, missing asset, broken image/font, console error that affects function, failed route, or required interaction/export that no longer works.

Exercise lazy content after scrolling through its loading boundary, navigation, keyboard paths, forms that are meant to remain local, downloads/exports, canvas/WebGL rendering through compositor screenshots, and refresh/deep-link behavior. Do not trust a pleasant screenshot: placeholder images, dead export buttons, and live dependencies can all look fine. Record what was not reproducible.

If the user later wants to extend the archived tool, look for the narrowest dependency-free seam in the original engine before patching opaque minified application code. A small verbatim engine behind a fresh local front end is usually easier to verify and keep offline.
