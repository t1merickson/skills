---
name: paper-mcp
description: Drive the Paper (paper.design) app over its local MCP server: layers, masks, blends, exports.
---

# paper-mcp

Paper Desktop serves an MCP endpoint at `http://127.0.0.1:29979/mcp` whenever
the app is running with a file open. Everything below was verified hands-on
against Paper Desktop 0.5.3 (2026-08-10) from this machine.

## Talking to it

The endpoint speaks MCP over HTTP with SSE responses. `windowid`-style
plumbing is already wrapped in [paper-mcp.sh](paper-mcp.sh) next to this file:

```bash
SID=$("$CLAUDE_SKILL_DIR/paper-mcp.sh" init)          # new session, prints id
"$CLAUDE_SKILL_DIR/paper-mcp.sh" call "$SID" get_basic_info '{}'
"$CLAUDE_SKILL_DIR/paper-mcp.sh" raw  "$SID" '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
```

Responses come back as `data:` SSE lines; the helper strips them to plain
JSON. Tool results wrap their payload as a JSON *string* in
`.result.content[0].text` — pipe through `jq -r ... | jq` to unwrap.
Screenshots/exports put images in `.result.content[] | select(.type=="image")`.

Session rules the server enforces:

- Call `get_guide {"topic":"paper-mcp-instructions"}` once per session before
  other tools — the server tells you to, and the guide carries real workflow
  rules (write HTML in small pieces, screenshot after changes, call
  `finish_working_on_nodes` when done).
- Call `get_font_family_info {"familyNames":[...]}` before first text styling.
- The first file touched becomes sticky for the session; pass `fileId`
  explicitly only when juggling several files.

## What works (verified)

- **Raster images via data URI.** `write_html` with
  `<img src="data:image/jpeg;base64,...">` creates a Rectangle with an image
  fill. Payloads ≥190 KB base64 went through fine.
- **PNG alpha masks.** `mask-image: url(data:image/png;base64,...)` +
  `mask-size` (include `-webkit-` twins) clips correctly — torn-paper edges
  render exactly as the alpha says.
- **Blend modes.** `mix-blend-mode: multiply` composites for real (verified
  against underlying photo). Standard CSS blend modes are the vocabulary.
- **Per-node PNG export with alpha.** `export` with
  `{"nodes":{"<id>":[{"format":"png","scale":"1x"}]}}` writes the file and
  keeps transparency (masked-out corners have alpha 0). Formats: png, jpg,
  webp, avif, svg, pdf, mp4. Scale grammar: `2x`, `512w`, `720p`, `512h`.
- **SVG inline in write_html** — paths, ellipses, transforms, opacity all
  render; each SVG element becomes its own node.
- **Text** — real text nodes; crop giant type with a parent div +
  `overflow:hidden`.
- `duplicate_nodes`, `move_nodes`, `update_styles`, `delete_nodes`,
  `create_page`, `create_artboard` all behave as documented in `tools/list`.

## Traps (each cost a debugging round)

1. **`height: auto` collapses to 0.** Images get created with height 0 and
   silently vanish. Always give explicit `width` AND `height` px.
2. **Screenshots can be stale.** `get_screenshot` right after a burst of
   `write_html` calls returned a frame missing the last two writes. Nodes
   were fine (`get_node_info` proved it). `sleep 2` before screenshotting
   after writes; trust node info over a suspicious screenshot.
3. **Schema drift vs docs.** `create_artboard` wants
   `{"name","styles":{"width":"800px","height":"600px",...}}` (styles object,
   not top-level w/h). `update_styles` wants
   `{"updates":[{"nodeIds":["..."],"styles":{...}}]}` (array `nodeIds`, not
   `nodeId`). `get_font_family_info` wants `familyNames` (array). When a call
   fails with "Invalid arguments", run `tools/list` and read the real schema
   instead of guessing twice.
4. **Exports land in `~/Downloads/<NodeName>.<ext>`** — the tool result gives
   the path. There is no way to choose the destination; copy the file out.
   (`~/Downloads` is the user's personal folder: touch only the file you just
   exported.)
5. **`overflow:hidden` on a plain div did not clip a child image** in one
   test. Don't rely on it for cropping; bake crops into the asset, use
   `object-fit:cover` with exact dimensions, or use a real mask.
6. **z-order = document order.** `write_html` with `insert-children` appends
   on top. Use `move_nodes` to restack. (`mode:"replace"` keeps the replaced
   node's slot in the z-order — safe for swapping assets.)
7. **Don't judge alignment from a downscaled screenshot.** A 1x screenshot
   viewed scaled-down produces moiré that makes perfectly grid-snapped edges
   look off by half a cell. Verify alignment by measuring pixels in the
   screenshot PNG (find line positions / element bounding boxes with PIL),
   not by eye.

## Working style that fits Paper's guide

- One visual group per `write_html` call — the user watches the canvas build
  live.
- `mode:"replace"` with a `targetNodeId` swaps a bad node for corrected HTML
  in place — the cheap fix loop.
- Screenshot (`get_screenshot {"nodeId":...}`) → judge → targeted fix. Don't
  delete-and-restart a composition; Paper's guide explicitly calls that out
  as hostile to the user.
- Never put node IDs in user-facing text.

## Composition pattern that worked (collage)

Bake raster scraps locally (grayscale/duotone/dither/grid via Python or the
PaperStack pipeline), push each as a data-URI layer bottom-to-top onto one
artboard, use SVG for line work (pencil arcs, blueprint strokes), HTML text
for type fragments, plain divs for accent blocks. Local baking beats trying
to do image processing in CSS — Paper is the compositor, not the darkroom.

## Limits

- MCP works only while Paper Desktop is running with the file open — no
  headless mode.
- Free tier: 100 MCP tool calls/week (Pro raises it to 1M). A single collage
  build + fix loop here took ~35 calls.
- No custom shaders/plugins via MCP; the built-in shader library is
  editor-side only.
