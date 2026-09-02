---
name: paper-mcp
description: Operate an open Paper.design canvas through Paper Desktop's local MCP server for layer editing, masks, blends, screenshots, and exports.
---

# Paper MCP

Use when the user asks to work in Paper and Paper Desktop is running with the intended file open. Canvas edits and exports change user state; stay within the named file/artboard and preserve existing work.

## Initialize and inspect

Resolve this installed skill directory from the host; do not assume a Claude-specific environment variable.

```bash
sid="$(<skill-directory>/paper-mcp.sh init)"
<skill-directory>/paper-mcp.sh raw "$sid" '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
<skill-directory>/paper-mcp.sh call "$sid" get_basic_info '{}'
```

The helper accepts `PAPER_MCP_ENDPOINT` and `PAPER_MCP_PROTOCOL_VERSION` overrides for a changed local server. It unwraps SSE framing but leaves MCP result content intact.

Before editing:

1. inspect `tools/list` and use its current schemas rather than memorized arguments;
2. call the server's Paper instructions/guide tool when advertised;
3. inspect basic file/page/artboard/node state;
4. confirm the intended target when more than one file or artboard is open;
5. inspect font availability before applying a family.

The first file may become session-sticky on some builds. Pass file IDs explicitly when supported and re-read state after switching.

## Edit in reviewable groups

- Make one coherent visual group per write rather than replacing a whole composition.
- Preserve z-order, grouping, masks, and existing node identity where practical.
- Prefer targeted replace/style/move operations over delete-and-rebuild.
- Use raster assets as data URIs only when size and current schema permit; keep local source assets and transformations reproducible.
- Treat Paper as a compositor. Perform heavy image processing in a suitable local tool, then bring the resulting layer in.
- Never expose internal node IDs as user-facing labels or prose.

After a burst of edits, verify node state first, then request a screenshot once rendering has settled. A screenshot can lag document state. Measure alignment from node bounds or full-resolution pixels, not a downscaled preview.

## Export and finish

Probe the current export schema and supported formats/scales. Export only named nodes/artboards. The server may choose a user Downloads location; touch only the returned artifact, then copy it to the approved project/output location if needed.

Inspect transparency, dimensions, color, and the actual exported file—not just the canvas preview. Call the server's finish/cleanup tool when its guide requires one.

Read [references/verified-snapshot.md](references/verified-snapshot.md) only for debugging clues. It is a dated observation, not the live schema or service policy.
