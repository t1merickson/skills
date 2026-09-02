# Dated Paper Desktop observations

Observed against Paper Desktop 0.5.3 on 2026-08-10. Recheck `tools/list` before relying on any field.

## Confirmed capabilities in that build

- `write_html` accepted raster data URIs and inline SVG.
- PNG alpha masks and standard CSS blend modes rendered.
- per-node export supported PNG/JPEG/WebP/AVIF/SVG/PDF/MP4 and scale strings such as `2x` or dimension-constrained forms.
- text nodes, node duplication/movement/style updates/deletion, page creation, and artboard creation were exposed.

## Debugging clues from that build

- Images with `height:auto` could collapse; explicit pixel width/height was safer.
- Screenshots immediately after several writes could omit the newest nodes even when node inspection showed them.
- Argument shapes differed from prose examples: artboard dimensions lived in `styles`, style updates used an updates array and node ID array, and font lookup accepted a family-name array.
- Exports landed in Downloads and returned the actual path.
- Plain-container overflow clipping was unreliable in one test; explicit masks or pre-cropped assets were safer.
- Appended children appeared above earlier document siblings; replacing a node tended to preserve its slot.
- Downscaled previews created moire/alignment illusions; pixel or node-bound measurement settled them.

These are leads for diagnosis, not permanent workarounds. Remove or revise this snapshot when current Paper behavior contradicts it.
