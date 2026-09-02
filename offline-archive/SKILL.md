---
name: offline-archive
description: Preserve a legitimately accessible web page, tool, or bounded site as a self-contained personal-use archive with polite acquisition, provenance, and network-blocked replay.
---

# Offline archive

Confirm the URL, intended personal-use scope, output location, breadth, fidelity needs, and anything to omit. Omission may remove tracking or promotional chrome from content the user can legitimately access; it does not authorize bypassing paywalls, authentication, DRM, robots restrictions, or technical access controls.

## Plan before fetching

Identify the site architecture and prefer an available source repository over scraping deployed bundles. Read the site's terms and `robots.txt`; respect explicit restrictions. Stop on access denial, sustained throttling, or a scope that expands materially beyond the approved request.

Create a request plan and manifest before a whole-site crawl:

- allowed origins and paths;
- sitemap or known inventory;
- estimated pages/assets/bytes;
- concurrency, delay, retry/backoff, and maximum request budget;
- resume state and deduplication key;
- user agent/contact convention where appropriate;
- capture date and tool versions.

Use low concurrency, server-directed retry delays, capped exponential backoff, and resumability. Avoid refetching unchanged assets. For evidentiary or long-lived captures, consider WARC alongside the browsable derivative.

## Preserve behavior deliberately

Capture HTML, styles, fonts, media, modules, JSON payloads, and other runtime assets within scope. Rewrite them to relative paths or data URLs. Live API behavior becomes an explicit captured snapshot or a clearly disabled feature; install a deny-by-default network shim rather than letting missed requests silently escape to production.

Prefer rebuilding from source when available and record the relationship between source commit, production asset hashes, and archive build. Do not patch opaque minified code unless a smaller, testable seam is unavailable.

Architecture-specific traps belong in [references/site-recipes.md](references/site-recipes.md). Verify them against the current site rather than assuming a framework from old filenames.

## Provenance

Place `SOURCE.md` beside the archive with original URL, retrieval date, scope, request policy, capture tool/version, source commit when known, transformations, omitted features/content, licenses, integrity hashes, known failures, and replay instructions. Preserve superseded captures by project policy; do not accumulate them blindly.

## Verify offline

Serve or open the archive through its supported local route with all HTTP, HTTPS, and WebSocket traffic blocked. The verifier exits non-zero for any attempted network access, missing asset, broken image/font, console error that affects function, failed route, or required interaction/export that no longer works.

Exercise lazy content, navigation, keyboard paths, forms that are meant to remain local, downloads/exports, canvas/WebGL rendering through compositor screenshots, and refresh/deep-link behavior. Record what was not reproducible.

Republishing or hosting is a separate rights and deployment decision. A personal archive does not imply permission to distribute it.
