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

## Verify

After a burst of edits, check node state (`get_jsx`, `get_computed_styles`) first, then take one screenshot once rendering settles. Screenshots are JPEG and can lag document state. Measure alignment from node bounds or full-resolution pixels, not a downscaled preview. Treat calls as a budget: inspect once, write coherent groups, screenshot at review points.

## Export

Read the current `export` schema for formats and scales. Export only named nodes or artboards. The server chooses the output location, often Downloads, and returns the path. Touch only that file, copy it to the project if needed, and inspect the actual file for dimensions, transparency, and color.

Read [references/verified-snapshot.md](references/verified-snapshot.md) only for debugging clues. It records dated observations, not the live schema.
