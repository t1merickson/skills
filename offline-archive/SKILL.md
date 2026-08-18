---
name: offline-archive
description: Scrape a page or web tool into a self-contained offline copy that still works.
---

# offline-archive

the user archives web tools and pages they want to keep or reuse. history shows the same two-step shape every time: a broad "archive this URL", then a scoping correction stripping something unwanted (a paywall, crypto junk, DRM, a watermark). so ask the scoping question UP FRONT, once: "keep it whole, or strip anything — paywalls, tracking, promo chrome?" then work.

## the archive

1. fetch the page. inspect what it actually is: static page, JS app, canvas/shader toy. the strategy follows from that.
2. pull every asset the page needs: styles, scripts, fonts, images, fetched data. inline small things, download the rest into an `assets/` directory, rewrite paths to relative.
3. preserve the LOGIC, not just the look. an archived shader toy has to render; an archived tool has to work. if logic loads from an API that won't exist offline, capture a snapshot of the data and stub the fetch.
4. strip what the user asked to strip: remove the code, not just hide the element. tracking scripts and analytics go by default.
5. output: one self-contained directory, `index.html` at the root, opens from `file://` with no network. put a `SOURCE.md` beside it: original URL, archive date, what was stripped.

## verify

done means it runs offline: open the local copy, confirm the core interaction works with the network off (or at least with devtools offline). a directory of files that 404s locally is not an archive.

## rules

- these live in the Archival project (`/Users/Commons/Developer/Archival/`) unless the user names a different home. one directory per archive, named after the thing.
- personal-use archival only. if the user asks to republish one, that leaves this machine and needs the usual ask-first.
- expect the second pass anyway. even with the upfront question, they often see the archive and wants one more thing removed or kept. that's the workflow, not a failure.
