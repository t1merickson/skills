# Dated Paper observations

Recheck `tools/list` and `get_guide` before relying on any field. Remove or revise an entry when current Paper behavior contradicts it.

## Paper Desktop 0.5.15, `paper` CLI 0.0.1 — 2026-10-08

Observed while building a 45-artboard wireframe board:

- `create_artboard` ignored `left`/`top` passed in `styles` and placed the artboard in the next free spot. Setting `left`/`top` afterwards with `update_styles` moved it.
- `duplicate_nodes` returns a `descendantIdMap` for every copied descendant. It placed copies in free space, sometimes on top of planned grid slots.
- A free-plan account hit "Weekly MCP limit reached. It resets tomorrow." mid-build. After that every call failed, reads included. Upgrading lifted the limit immediately, with no restart.
- `find_nodes` by a literal hex searched the whole file. It returned `matched[].styleName` (`backgroundColor`, `color`, `borderColor`), and one color matched 146 nodes.
- `update_styles` reported `whiteSpace` under `ignoredStyles` on frames; it applied on text nodes.
- `create_tokens` accepted `var(--other)` as an alias value and changed the file's token `contentHash`.
- No component or instance tool appeared in the tool list.
- Superellipse corners work through CSS `corner-shape`. `corner-shape: squircle` and `superellipse(2)` were both stored per corner as `cornerTopLeftShape` etc., and rendered visibly smoother than circular arcs at the same `border-radius`. A Figma-style `cornerSmoothing` style was silently dropped: it didn't appear in computed styles or in `ignoredStyles`. No token type exists for corner shape.
- How the corner curve was measured, to repeat for other platforms:
  1. Render the reference with Core Animation in a Swift script: a 400×400 CALayer with `cornerRadius 100` and `cornerCurve .continuous`, drawn at 2× with `layer.render(in:)`, black on white. Render a `.circular` copy as the control.
  2. Render a grid of CSS candidates in headless Chrome at device scale 2: `superellipse(k)` for several k, with radius × s.
  3. Diff the top-left corners with numpy (mean absolute difference, plus pixels off by more than 128).
  4. Sanity check: Chrome's plain round matched Apple's circular control at 0.06.
  5. Best fit was k=1.45, s=1.3. Paper's own 2× screenshot of that setting scored 0.35, against 0.28 for its round-vs-circular noise floor.
- Several general-purpose subagents edited different artboards in the same file at once without conflicts.

## Paper Desktop 0.5.14, `paper` CLI 0.0.1 — 2026-09-30

Setup:

- Paper Desktop installs `~/.paper/bin/paper`. `paper mcp` is a stdio relay (server name `paper-desktop`, protocol `2025-06-18`). Paper's docs say it lets agents start even when Desktop is closed, instead of failing to connect.
- The HTTP endpoint `http://127.0.0.1:29979/mcp` still answered and served the same 35 tools. Paper's docs call it legacy.
- The `paper-design/agent-plugins` repository holds MCP configs and the `.mcpb` extension only. It ships no skill.
- The server's `initialize` instructions require loading `get_guide({ topic: "paper-mcp-instructions" })` once per session.

Tools: files and pages (`open_file`, `list_files`, `create_file`, `create_page`, `rename_pages`); reading (`get_basic_info`, `get_selection`, `get_node_info`, `get_children`, `get_tree_summary`, `get_jsx`, `get_computed_styles`, `get_fill_image`, `find_nodes`, `get_screenshot`); editing (`write_html`, `create_artboard`, `update_styles`, `set_text_content`, `rename_nodes`, `duplicate_nodes`, `move_nodes`, `delete_nodes`); tokens (`get_tokens`, `create_tokens`, `set_tokens`); comments (`list_comment_threads`, `get_comment_thread`, `list_comment_thread_authors`, `set_comment_thread_status`); output (`export`, `export_combined_pdf`); plus `get_font_family_info`, `get_guide`, `finish_working_on_nodes`.

Observed:

- `get_guide` with no arguments failed validation. Topics: `paper-mcp-instructions`, `mobile-status-bar`, `figma-import`, `image-generation`.
- With no file open in Desktop, `get_basic_info` without `fileId` returned "Open a Paper file to use this tool."
- `create_file` returned a file ID and an `app.paper.design` URL. The file appeared in the team's file list.
- After `create_file` and `open_file`, `get_font_family_info` still returned "Open a Paper file", in the same session and in a fresh one. Passing an extra `fileId` returned `{}`. `system-ui` rendered correctly without a check.
- `create_artboard` placed the first artboard centered on the origin and took dimensions in `styles`.
- A `<span style="color:…">` inside a text `<div>` was flattened: the text survived, the span's color did not. Two sibling text nodes in a flex row kept separate styles.
- `write_html` in `replace` mode swapped a node in place.
- `get_screenshot` returned JPEG data at 1x.
- `get_jsx` returned Tailwind-style class names, useful for checking what styles actually landed.
- Not retested in this build: exports, masks, blends, raster data URIs.

## Paper Desktop 0.5.3 — 2026-08-10

Capabilities confirmed then:

- `write_html` accepted raster data URIs and inline SVG.
- PNG alpha masks and standard CSS blend modes rendered.
- Per-node export supported PNG/JPEG/WebP/AVIF/SVG/PDF/MP4 and scale strings such as `2x` or dimension-constrained forms.

Debugging clues from that build:

- Images with `height:auto` could collapse; explicit pixel width and height were safer.
- Screenshots immediately after several writes could omit the newest nodes even when node inspection showed them.
- Style updates used an updates array and a node ID array; font lookup took a family-name array.
- Exports landed in Downloads and returned the actual path.
- Plain-container overflow clipping was unreliable in one test; explicit masks or pre-cropped assets were safer.
- Appended children appeared above earlier document siblings.
- Downscaled previews created moiré and alignment illusions; pixel or node-bound measurement settled them.
