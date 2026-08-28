---
name: offline-archive
description: Scrape a page or web tool into a self-contained offline copy that still works, or crawl a whole site politely.
---

# offline-archive

The user archives web tools and pages they want to keep or reuse. History shows the same two-step shape every time: a broad "archive this URL", then a scoping correction stripping something unwanted (a paywall, crypto junk, DRM, a watermark). So ask the scoping question UP FRONT, once: "keep it whole, or strip anything — paywalls, tracking, promo chrome?" Then work.

## Identify the site type first

The strategy follows from what the site is, and several types have known recipes. Check the archive project's session memory for a recipe matching the type before starting — solved traps shouldn't be re-lost. Known types so far:

- **Static page, no modules**: classic asset pull works.
- **Plain ES modules, no bundler**: still can't be double-clicked — browsers block module *fetches* from `file://`. Inline the modules (wrap each in an IIFE returning its exports; rewrite imports to destructuring).
- **Vite/React SPA**: a wget mirror is dead on arrival (HTML shell + hashed bundles, CORS-blocked from `file://`). Rebuild single-file: inline everything, one chunk, CSS folded in.
- **Next.js App Router**: chunks are plain `<script src>` (no CORS problem), but asset paths are ALSO baked into the RSC payload and React re-injects them at hydration — replace every occurrence of each asset path across the whole document, scripts included, with `data:` URIs. Neutralize root-relative nav links or `file://` navigates off the archive.
- **WordPress**: check `wp-sitemap.xml` before writing a parser — the REST API at `/wp-json/` is commonly locked (`{"code":"rest_login_required"}`) while the sitemaps are left wide open, and their children give the full item list plus taxonomy and author indexes. Media sits at predictable paths (`/wp-content/uploads/<year>/<month>/`, or `/wp-content/themes/<theme>/...` for theme-bundled assets); if directory listing returns 200, enumerate it instead of parsing pages.
- **Cargo Collective**: the entire site inventory lives in `window.__PRELOADED_STATE__` — extract it, no crawling needed. Originals at `/t/original/`; freight 403s without a browser user-agent; flip `domain_active` to false or the boot code redirects off localhost.

**Prefer building from source whenever the repo exists** — then check built asset hashes against the deployed ones, which proves byte-identity to production for free.

## Whole-site crawls

Different job from a single-artifact archive: hundreds or thousands of fetches against someone else's host. The goal is that the host stays unbothered. Parameters below come from a 2,484-fetch run over 2h 45m with zero 429s, zero 5xx, and zero backoffs.

**Read robots.txt and take the answer.** Sites increasingly enumerate AI-affiliated agents by name under `Disallow: /` — `anthropic-ai`, `Claude-User`, `Claude-Web`, `ClaudeBot`, `Claude-SearchBot`, `GPTBot`, `Bytespider`, `Scrapy` — while leaving generic crawlers like Googlebot allowed. That is a legible position: automated traffic is fine, AI-affiliated scrapers are refused. Two consequences, neither negotiable:

- **Never impersonate an allowed crawler.** Claiming to be Googlebot to get past a rule aimed at you is the line.
- **Identify honestly** — a user agent naming what the archive is for, plus a contact address that actually receives mail. A bouncing contact address is worse than none, since the entire purpose is that a sysadmin can reach someone. If a later pass finds the site has gotten stricter, stop.

**When the API is locked, try the sitemaps.** Access control gets applied to the API and forgotten on the sitemaps — see the WordPress recipe above for the common case. A sitemap is usually enough to plan the whole crawl before fetching a single page. Expect it to be slightly wrong: dedupe and filter out non-item URLs (redirect endpoints, `/random/`) before counting anything.

**Rate:** 1 request/second with **±40% jitter**. The jitter matters more than the rate — a metronome reads as a bot even at a polite interval. Exponential backoff on 429/5xx (2s, 4s, 8s, capped at 60s). **Bail on 403** — a 403 is an answer, not an obstacle. Keep the crawl resumable; dying at minute 140 of a 165-minute run is expensive.

**Look for the direct asset path, then look for the exception.** Once a predictable media path is found, enumerate it rather than parsing pages — but assume at least one item breaks the pattern — in that run, one was synthesized in-browser and had no assets at all. Any asset-path assumption has an exception; find it before trusting the count.

**A published total that disagrees with yours is usually a definition mismatch, not a crawl error.** Work out which noun each side counts — that run's "7,560 patterns" turned out to be sequences, where each upload held 1 to 16 of them. Reconcile definitions before assuming either number is wrong.

**Toolchain trap:** Python 3.14+ raises `socket.TimeoutError` directly out of `urllib.request` instead of wrapping it in `URLError`. A scraper catching only `URLError`/`HTTPError` dies mid-run; catch `(TimeoutError, ConnectionError, OSError)` too.

## The archive

1. Pull every asset the page needs and rewrite to relative or `data:` URIs. Assets hide beyond the HTML: `public/`-copied files that bypass inline limits, template-literal URLs in minified JS (backticks, not quotes), paths inside JSON payloads.
2. Preserve the LOGIC, not just the look. For live APIs, install a `fetch` shim in `<head>` before any chunk runs: serve captured snapshots, and **reject everything else** so the archive can never quietly depend on the live site. Shimming beats string-patching minified code.
3. One string-replacement trap that corrupts silently: `String.replace(pattern, bigString)` interprets `$&` and friends in the replacement — minified JS is full of `$`. Always use a function replacer.
4. Strip what the user asked to strip: remove the code, not just hide the element. Tracking and analytics go by default.
5. Output: one self-contained directory, `index.html` at the root, opens from `file://` with no network. `SOURCE.md` beside it: original URL, archive date, what was stripped. Superseded captures move to `previous/`, never deleted.

## Verify — assert, don't eyeball

A page can look perfect while being wrong (placeholder images, dead exports, live-site dependencies). The verifier must assert and exit non-zero, not print:

- **Kill the network and replay**: drive headless Chrome over CDP with `Network.setBlockedURLs: ['http://*','https://*','ws://*','wss://*']`. That turns "self-contained" into an assertion instead of a hope.
- Never `--virtual-time-budget` — it hangs forever on any continuous rAF loop. Use `--remote-debugging-port` with per-command timeouts, or a dropped reply wedges the run silently.
- Check `document.images` for `naturalWidth === 0`; scroll to the true bottom first — lazy loaders revert offscreen images to placeholders.
- WebGL canvases can't be sampled with `drawImage` (buffer clears after compositing — reads solid black). Screenshot through the compositor (`Page.captureScreenshot` with a clip) and diff only the pixels that changed; whole-image averages can't see a brushstroke.
- Exercise the interactions: click the export buttons with `URL.createObjectURL` hooked, fire the keyboard shortcuts.

## When the ask becomes "now make it do more"

It usually does. Patching minified React is the wrong move — instead, look for the interesting engine as a **dependency-free webpack module** (exports only, no cross-module calls), lift its body out verbatim behind a five-line shim, and write a fresh front end around it. The engine stays byte-identical to production, which the build can assert. Find the narrowest seam into the renderer before assuming a rewrite.

## Rules

- Archives live in the user's designated archive project, one directory per archive, named after the thing.
- Personal-use archival only. Republishing leaves this machine and needs the usual ask-first.
- Expect the second scoping pass anyway; that's the workflow, not a failure.
- **When a new site type costs real debugging, write the recipe into the archive project's memory** — that's how this section grows instead of the traps being re-paid.
