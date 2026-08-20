---
name: offline-archive
description: Scrape a page or web tool into a self-contained offline copy that still works.
---

# offline-archive

the user archives web tools and pages they want to keep or reuse. history shows the same two-step shape every time: a broad "archive this URL", then a scoping correction stripping something unwanted (a paywall, crypto junk, DRM, a watermark). so ask the scoping question UP FRONT, once: "keep it whole, or strip anything — paywalls, tracking, promo chrome?" then work.

## identify the site type first

the strategy follows from what the site is, and several types have known recipes. check the archive project's session memory for a recipe matching the type before starting — solved traps shouldn't be re-lost. known types so far:

- **static page, no modules**: classic asset pull works.
- **plain ES modules, no bundler**: still can't be double-clicked — browsers block module *fetches* from `file://`. inline the modules (wrap each in an IIFE returning its exports; rewrite imports to destructuring).
- **Vite/React SPA**: a wget mirror is dead on arrival (HTML shell + hashed bundles, CORS-blocked from `file://`). rebuild single-file: inline everything, one chunk, CSS folded in.
- **Next.js App Router**: chunks are plain `<script src>` (no CORS problem), but asset paths are ALSO baked into the RSC payload and React re-injects them at hydration — replace every occurrence of each asset path across the whole document, scripts included, with `data:` URIs. neutralize root-relative nav links or `file://` navigates off the archive.
- **Cargo Collective**: the entire site inventory lives in `window.__PRELOADED_STATE__` — extract it, no crawling needed. originals at `/t/original/`; freight 403s without a browser user-agent; flip `domain_active` to false or the boot code redirects off localhost.

**prefer building from source whenever the repo exists** — then check built asset hashes against the deployed ones, which proves byte-identity to production for free.

## the archive

1. pull every asset the page needs and rewrite to relative or `data:` URIs. assets hide beyond the HTML: `public/`-copied files that bypass inline limits, template-literal URLs in minified JS (backticks, not quotes), paths inside JSON payloads.
2. preserve the LOGIC, not just the look. for live APIs, install a `fetch` shim in `<head>` before any chunk runs: serve captured snapshots, and **reject everything else** so the archive can never quietly depend on the live site. shimming beats string-patching minified code.
3. one string-replacement trap that corrupts silently: `String.replace(pattern, bigString)` interprets `$&` and friends in the replacement — minified JS is full of `$`. always use a function replacer.
4. strip what the user asked to strip: remove the code, not just hide the element. tracking and analytics go by default.
5. output: one self-contained directory, `index.html` at the root, opens from `file://` with no network. `SOURCE.md` beside it: original URL, archive date, what was stripped. superseded captures move to `previous/`, never deleted.

## verify — assert, don't eyeball

a page can look perfect while being wrong (placeholder images, dead exports, live-site dependencies). the verifier must assert and exit non-zero, not print:

- **kill the network and replay**: drive headless Chrome over CDP with `Network.setBlockedURLs: ['http://*','https://*','ws://*','wss://*']`. that turns "self-contained" into an assertion instead of a hope.
- never `--virtual-time-budget` — it hangs forever on any continuous rAF loop. use `--remote-debugging-port` with per-command timeouts, or a dropped reply wedges the run silently.
- check `document.images` for `naturalWidth === 0`; scroll to the true bottom first — lazy loaders revert offscreen images to placeholders.
- WebGL canvases can't be sampled with `drawImage` (buffer clears after compositing — reads solid black). screenshot through the compositor (`Page.captureScreenshot` with a clip) and diff only the pixels that changed; whole-image averages can't see a brushstroke.
- exercise the interactions: click the export buttons with `URL.createObjectURL` hooked, fire the keyboard shortcuts.

## when the ask becomes "now make it do more"

it usually does. patching minified React is the wrong move — instead, look for the interesting engine as a **dependency-free webpack module** (exports only, no cross-module calls), lift its body out verbatim behind a five-line shim, and write a fresh front end around it. the engine stays byte-identical to production, which the build can assert. find the narrowest seam into the renderer before assuming a rewrite.

## rules

- archives live in the user's designated archive project, one directory per archive, named after the thing.
- personal-use archival only. republishing leaves this machine and needs the usual ask-first.
- expect the second scoping pass anyway; that's the workflow, not a failure.
- **when a new site type costs real debugging, write the recipe into the archive project's memory** — that's how this section grows instead of the traps being re-paid.
