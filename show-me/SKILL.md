---
name: show-me
description: Show work, a decision, a state, a comparison, or an idea visually instead of in prose. Use when invoked as /show-me, and offer it unprompted when the user must judge or pick something that is easier to see than read (glyphs, layouts, options, file sets, data, before/after). Not for picking a new UI direction with no design yet (use mock-and-pick), and not for short answers that read fine as text.
---

# show-me

The user judges by looking. Markdown tables, file trees, and lists of dial values are not legible to them. When something needs their eyes or their pick, put the real thing in front of them.

## When to use

- `/show-me`, with or without a topic. No topic means: show whatever is open right now (the current decision, the work just done, the state of the thing).
- Unprompted: offer it in one line when a decision or comparison is about to go out as a wall of text. If the user already asked for visuals in this session, skip the offer and just do it.
- Not for: a new UI direction with no design yet (that is `mock-and-pick`), yes/no questions, or answers that fit in two sentences.

## Where to show it

Use the first that fits. Native beats new.

1. **The thing itself.** If the work is an app or page, build it and open it. Native apps: `make run`. Web: the project's existing dev server, opened in Chrome.
2. **The project's own viewer.** Font projects: Bench, through the `kit` skill. Design work on a Paper canvas: the canvas, through `paper-mcp`. Any existing viz page, preview, or viewer already in the repo.
3. **One HTML file in the project.** Save it at `<project>/show-me/<topic>.html`. Not `/tmp`, not a chat artifact, not markdown. Open it yourself:
   `open -a "Google Chrome" /absolute/path/to/show-me/<topic>.html`

Open it yourself every time. Never hand the user a path or a command to open it.

## What goes on the page

- **Real content.** Actual glyphs in the actual font, real window captures (via `window-capture`), real data, real file thumbnails. Never a description of the thing in place of the thing.
- **Decisions:** options side by side. Each gets a label and one plain line on what picking it means. Add a way to pick: checkboxes or radio buttons plus a "Copy picks" button that copies a short text line the user can paste back.
- **State or progress:** what is done, what is not, what is broken, as a grid or list of the real items, not a summary.
- **Comparisons:** same scale, same order, aligned so differences jump out.
- Style per `web-design-defaults`: black and white, system font, no decoration.

## Keep it small

- One page. The smallest thing that makes it legible.
- No dashboards, nav, theming, or build step. A single self-contained HTML file is the default.
- Reuse and update the same file for the same topic instead of making new ones.

## After showing

- Say in one line what is on screen and what you need from the user. Then stop and wait if it is a decision.
- When they paste picks back, act on them.
- Files in `show-me/` are scratch. Once the decision lands, move them to quarantine (never `rm`) unless the user wants to keep them. Ask before committing them.
