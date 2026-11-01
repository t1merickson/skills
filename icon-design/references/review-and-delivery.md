# Review and delivery

## Five separate gates

1. **Source integrity:** editable masters remain; IDs and geometry are understandable; external dependencies are intentional; optical overrides are explicit.
2. **Raster behavior:** correct dimensions, color interpretation, alpha, filtering, and crop. Inspect the actual output, not only SVG syntax.
3. **Package behavior:** the container decodes, required slots exist, hashes match the selected sources, and the intended target includes it.
4. **Context behavior:** icon appears correctly in the actual app/OS surface and required appearances. Native UI evidence is distinct from a browser gallery.
5. **Human acceptance:** identity, personality, and relative visual quality meet the brief. Automated checks do not make this decision.

Report each gate accurately. A successful `iconutil` command does not prove a beautiful Dock icon. A visually pleasing mockup does not prove a valid archive.

## Minimum inspection sequence

Start at intended size, without zooming. Identify the hero and the first three things your eye notices. Then compare adjacent sizes and appearances. Look for accidental visual jumps, ambiguous overlaps, and details that become noise. Next enlarge with nearest-neighbor sampling to investigate the cause of any defects. Return to intended size before accepting a correction.

Inspect white, dark, middle gray, saturated magenta, and a representative busy background where transparency is relevant. Look for halos, clipped blur, dirty semitransparent edges, invisible white content, and unintended holes. Alpha-only view should show the intended coverage; remember that alpha is visibility, not luminance.

Compare against neighboring icons in the target context. Use fresh screenshots or user-provided references when that comparison is authorized; do not distribute copied app icons in the reusable skill. Equal bounding boxes do not ensure equal optical weight. Large filled shapes can need a different inset from narrow or diagonal objects.

For dimensional art, follow every contact: Does each prop sit on the support? Does its shadow meet it? Do shared light directions agree? Does a bright reflection cross a boundary where the material changes? Does texture leak outside a mask? Could one effect be removed without losing any information?

For modern material icons, inspect default, dark, clear, and tinted behavior at supported OS versions. A local static layer recomposition can check registration but cannot validate refraction or system highlights. Use the official preview and built application.

## Defect-to-action guide

| Defect | Investigate | Correct at |
|---|---|---|
| Blurry large export | Renderer rasterized small before enlargement | Render at output resolution |
| Halo on dark background | Matte contamination or alpha resampling | Export/compositing pipeline |
| Shadow cut off in a rectangle | Filter region or canvas clipping | Source/filter bounds |
| Unexpected outline in tiny icon | Border occupies too much of silhouette | Optical master |
| Icon looks off-center despite equal margins | Asymmetric perceived mass | Composition |
| Variant loses recognition | Tone collapse or altered silhouette | Appearance source/settings |
| Missing family badge | Wrong source selected or automatic downscale | Manifest/optical master |
| Tool says valid but deployed icon differs | Wrong target, stale build, system material | Integration/context |
| Rich illustration feels plasticky | Same highlight/edge on every material | Material hierarchy |
| Everything attracts attention equally | No dominant value or shape group | Concept/composition |

## Handoff structure

Deliver a directory containing the brief, source masters, manifest, fresh render outputs, receipt, and review notes. Include package or layer exports when requested. Explain which source controls each resource and where authored exceptions live. Include one concise rationale for the selected design and a small list of known limits.

A useful review note says: “The 16-point master removes the lake line, enlarges the lens rim, and keeps the mountain silhouette. The 32-point master restores the water band. Both were rendered at 1x and 2x and inspected on light/dark backgrounds.” It does not say only “optimized for all sizes.”

Do not copy this skill's example directly into a production identity without a design decision. It is original instructional art, not a user-approved brand.
