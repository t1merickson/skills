---
name: paper-mcp
description: Work in Paper (paper.design) canvases through Paper's MCP tools — reading and editing layers, text, tokens, comments, screenshots, and exports.
---

# Paper MCP

Use when the user asks to read, build, or change something in Paper. Canvas edits change the user's real files, which sync to their Paper team. Stay within the named file, page, and artboard, and preserve existing work.

## Connect

Paper ships its own MCP server. Paper Desktop's MCP panel installs it for each host:

- **Claude Code:** a `paper` stdio server that runs `~/.paper/bin/paper mcp`, added directly or through the `paper-desktop@paper` plugin from the `paper-design/agent-plugins` marketplace.
- **Claude Desktop:** the Paper `.mcpb` extension.
- **Codex, Cursor:** the same plugin repository ships configs for both.

Prefer the native tools when the host lists them (in Claude Code they appear as `mcp__paper__<tool>`). A server added mid-session loads only in a new session.

When no native tools are loaded, use the bundled helper. It speaks to Paper Desktop's local HTTP endpoint, which Paper now calls legacy but still serves while Desktop runs:

```bash
sid="$(<skill-directory>/paper-mcp.sh init)"
<skill-directory>/paper-mcp.sh call "$sid" get_guide '{"topic":"paper-mcp-instructions"}'
<skill-directory>/paper-mcp.sh call "$sid" get_basic_info '{"fileId":"<id>"}'
```

The helper strips SSE `data:` framing and leaves MCP content intact. Tool payloads are usually JSON strings inside `.result.content[].text`; screenshots arrive as image blocks. `PAPER_MCP_ENDPOINT` and `PAPER_MCP_PROTOCOL_VERSION` override the defaults. If the HTTP endpoint stops answering, check whether Paper removed it before debugging the helper.

## Start of session

1. Call `get_guide` with `topic: "paper-mcp-instructions"` once per session. The server requires it, and it documents current behavior better than any snapshot.
2. Read the live tool schemas instead of trusting memorized arguments.
3. Call `get_basic_info`. With no `fileId` it reads the file the user is viewing, and fails with "Open a Paper file" when there is none. Then use `list_files` and `open_file`, or `create_file` when the user asked for a new file. A new file lands in the user's Paper team, so don't create one as scratch space unasked.
4. Pass `fileId` and `pageId` explicitly from then on. The viewed page can change between calls, and tool results echo the file ID so a wrong target is visible.
5. Use `get_selection` to see what the user is focused on. Confirm the target when several files or artboards could match.
6. Check fonts with `get_font_family_info` before choosing a family. It has no `fileId` argument and may report no open file even after `open_file`. When it does, prefer families already in the file or `system-ui`, and say that the check was skipped.

## Whose taste wins

Paper's guide has two kinds of content. Follow its mechanics: incremental writes, design tokens as CSS variables, cloning with `<x-paper-clone>`, screenshot review, and `finish_working_on_nodes`. Its taste rules (a design brief before any mutation, mood words, palettes, making a vague prompt impressive) are Paper's defaults. The user's own design instructions, the project's design system, and any mock-first workflow come first. For a technical test or a narrow edit, skip the brief.

## Edit in reviewable groups

- One visual group per `write_html` call: a header, a row, a button bar. The user watches the canvas fill in real time.
- Prefer targeted `update_styles`, `set_text_content`, `move_nodes`, and `duplicate_nodes` over delete-and-rebuild. `move_nodes` keeps node identity; `write_html` in `replace` mode keeps the node's slot.
- Inline `<span>` styling inside a text node is flattened. For mixed styles, write separate text nodes in a flex row.
- Treat Paper as a compositor, not a darkroom. Do heavy image processing locally, bring rasters in as data-URI layers, use inline SVG for line work, and keep live text as text.
- Never show internal node IDs to the user. Refer to layers by name.
- Call `finish_working_on_nodes` with the artboard IDs when done. It clears the working indicator.

## Build with a system, not copies

Anything past a single screen needs a design system before the second screen exists. Copying earlier screens and patching them makes the copies drift apart, multiplies edits, and invites wrong-node mistakes.

1. **Tokens first.** Before building screens, create design tokens with `create_tokens`. If the project has code tokens (a theme file, CSS variables), mirror their names so the canvas and the code share one vocabulary. Write every color, radius, spacing and type size as `var(--token)`. Where the canvas and the code need different values, keep the code's name and put the difference in the value and description.
2. **A Kit artboard of masters.** Draw one master of each repeated part: buttons, fields, chips, tags, cards, nav bars, list rows, and a blank screen template. Name each one `Kit/<Part>`. Build new screens from Kit masters with `<x-paper-clone node-id="…">` or `duplicate_nodes`, never by copying another screen. Change a part in the Kit, then re-clone it.
3. **Clones don't stay linked.** The MCP tool list has no component or instance tool, so assume a clone is an independent copy. Tokens are the only live link between copies. That makes tokens important and the Kit a convenience.
4. **Migrating an existing board.** `find_nodes` with `filters: [{styleValue: "<hex>"}]` returns every node using that literal, with the property in `matched[].styleName`. Group the results by property and target token, then apply each group with one `update_styles` call. The results get large (one color can match more than 100 nodes), so hand migrations to a subagent to keep the main context clean. `find_nodes` caps at 200 results and counts nodes already converted to `var()`, so a big migration can stall. A trailing wildcard (`"#151515*"`) matches only the literal string. Nodes with a single-side border need the side property (`borderTopColor`), not `borderColor`.

## Match the target platform

Mobile mocks should get the platform's basics right from the first screen, since fixing 40 screens later is a migration.

- **Device size:** use the project's actual target device in points. Check the simulator or the project config rather than defaulting to Paper's suggested 390×844.
- **Status bar:** use Paper's official markup from `get_guide({ topic: "mobile-status-bar" })`, changing only its color. On iPhones with a Dynamic Island, add the island (about 126×37, 11px from the top, centered) and a home indicator (134×5, 8px from the bottom).
- **Continuous corners:** CSS `corner-shape: squircle` and `superellipse()` are not Apple's continuous corner, which is a different curve. Don't approximate it by eye. Measured against Core Animation's own render, Apple's corner leaves the straight edge further out than a circular arc, then rejoins the arc. The measured match (2026-10-08, Paper 0.5.15 and Chrome 154, against a Core Animation render) is `corner-shape: superellipse(1.45)` with the radius ×1.3. Example: an iOS radius of 16 becomes `border-radius: 20.8px; corner-shape: superellipse(1.45)`. Error was at the measurement's noise floor. CSS `squircle` was 27× worse than that. Bake the ×1.3 into the radius tokens and note the corner-shape pairing in their descriptions. In the app itself, use the native curve (`cornerCurve = .continuous`, or React Native's `borderCurve: 'continuous'`). Paper has no token type for corner shape and no components yet, so any corner change touches every node.
- **System metrics:** a 44pt nav bar, a 34pt bold large title, 17pt body, 44pt minimum touch targets, a 51×31 switch, and 270pt alerts.

## Boards of many screens

- **Show one version of each screen.** Don't place an as-built screen next to its planned replacement in the same row; reading left to right, it looks like a step forward into nearly the same screen. Pick the version the board is about (usually the target design) and tag each screen's status: built, change, new, later.
- **One flow per row, left to right.** Branches and variants (an error state, an alternate path, a sub-state) go in their own labeled row under the screen they come from. A variant should never look like the next step.
- **Position explicitly.** `create_artboard` and `duplicate_nodes` pick their own spot, so set `left`/`top` with `update_styles` right after. Keep a grid (column step = artboard width + 80) and reserve a column for row labels.
- **Brief subagents with the system.** Parallel subagents can each own a row, as long as each gets: the token names, the Kit node IDs, the exact copy, the board's positions, and any banned patterns. Without these, every agent invents its own card or button and the board drifts.
- **Budget for limits.** Paper plans can cap MCP calls; when a limit is hit, reads fail too. Stop, report what's half-built with node IDs, and leave the decision about upgrading to the user, since it costs money.

## Verify

After a burst of edits, check node state (`get_jsx`, `get_computed_styles`) first, then take one screenshot once rendering settles. Screenshots are JPEG and can lag document state. Measure alignment from node bounds or full-resolution pixels, not a downscaled preview. Treat calls as a budget: inspect once, write coherent groups, screenshot at review points.

## Export

Read the current `export` schema for formats and scales. Export only named nodes or artboards. The server chooses the output location, often Downloads, and returns the path. Touch only that file, copy it to the project if needed, and inspect the actual file for dimensions, transparency, and color.

Read [references/verified-snapshot.md](references/verified-snapshot.md) only for debugging clues. It records dated observations, not the live schema.
