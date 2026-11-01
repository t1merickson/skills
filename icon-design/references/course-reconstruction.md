# Direct course reconstruction

## Purpose and attribution

This is a study of the **same icon taught in Sebastiaan de With's Icon Resource course**: a blue curled document, a beige rear sheet, a long red paintbrush, and a yellow pencil with a pink eraser. The composition is attributed to the course. The SVG paths, gradients, procedural fibers, and source generator were independently authored from scratch; no course pixels, PSD paths, or extracted shapes were imported. This exercise is not an original app identity or a pixel-identical reproduction.

The user explicitly requested source-native tooling. The visible paintbrush object is reconstructed; this does not claim use of the identical Photoshop brush preset or Photoshop brush engine. Fibers that the lesson paints are expressed here as deterministic clipped curves. Preserve the lesson's design operation and explain this implementation substitution.

## Read and build progressively

Start with `examples/course-study/build_source.py`. It writes named SVG geometry, optical sources, components, and a manifest beside itself. Run it only in the study directory or a working copy; it intentionally regenerates its own authored outputs. Rendering uses the general icon toolkit:

```sh
python examples/course-study/build_source.py
python scripts/iconkit.py build examples/course-study/manifest.json /tmp/course-study-render-NEW
python scripts/iconkit.py verify examples/course-study/manifest.json /tmp/course-study-render-NEW/receipt.json
```

Use the dependency/environment setup in Tooling. Choose a new render destination. The resulting inspector displays the actual raster sizes and backgrounds. The full composition is rendered at 512, 256, and 128 pixels. Separate optical sources render at 32 and 16 pixels. Three component studies isolate paper, brush, and pencil.

## Construction order

1. **Pencil silhouette.** Build along a local horizontal axis: graphite point, exposed wood, yellow painted barrel, metal ferrule, pink eraser. The wood/paint boundary uses a scalloped cut rather than a straight transverse join. All these parts share coordinates before one group transform places the pencil in the composition.
2. **Pencil material.** Use separate profiles for graphite, wood, painted facets, silver, and rubber. Facet highlights are broad flat bands; the ferrule changes more abruptly between dark and bright. Fine wood fibers run from the cut toward the point. Clip them to the wood so no stroke floats beyond the silhouette.
3. **Document.** Author the outer page, inset blue field, flowing blue artwork, white paper edge, fold shadow, and curled face separately. The fold is a change of surface orientation, not a white triangle with an arbitrary drop shadow. Use a softer broad shadow beneath the page and a tighter dark region under the fold.
4. **Brush silhouette.** Work on one local axis: fanned bristles, silver ferrule, tapered red handle. Check that the ferrule receives both bristles and handle without a step or accidental bend. The handle's asymmetrical taper is intentional; its long highlight follows the curved body.
5. **Bristles.** Seeded curves fan between narrow roots and a broader end. Mix a bounded set of warm light and dark strands; vary their width and bend slightly. Clip to a shaped tip and darken the root. The seed is fixed so a geometry change does not also randomize texture.
6. **Compose.** Place paper first, then brush, then pencil. Apply rotations to entire assembled tools, not independently to highlights or ferrules. Preserve the reference's relative tool directions and its red/yellow/blue color structure. Inspect the negative spaces around the tips and between the tools.
7. **Optical redesign.** For 32 and 16, remove the rear sheet, straighten the page, enlarge the fold, simplify the blue sweep, replace dense bristles with a few marks, and strengthen essential edges. The tiny version increases structural stroke widths. These are separate drawings, not just different PNG export settings.

## What the exercise tests

The exercise makes material transitions inspectable: paper versus paint, lacquer versus fiber, graphite versus sharpened wood, metal versus rubber. It also tests geometry ownership: local-axis parts must remain mechanically connected after rotation. A mathematically valid SVG is insufficient; inspect the resulting joins and silhouettes.

The current reconstruction follows the course composition closely but differs in the exact blue sweep contours, tonal transitions, individual fibers, and some tool thicknesses. Those differences are visible in the local comparison sheet. The small drawings apply the taught optical strategy; they are not traced copies of the course's final small bitmap resources. Do not report pixel fidelity or human acceptance.

## Evergreen versus contemporary use

Keep editable shapes, value-first construction, directional texture, plausible junctions, and optical redraws. The old uncontained desktop icon, tilted paper, and baked shadows belong to this faithful historical exercise. For a current app, make a separate adaptation after selecting the delivery route. A modern frontal version might keep the same tool materials while simplifying paper and changing the container. Icon Composer requires clean layers and explicit decisions about system-owned effects; do not import this fully shaded composition and call the result a complete modern delivery.

A faithful exercise and a modern reinterpretation answer different questions. Preserve both sources if both are requested, and label them so later agents cannot silently replace the historical construction with their preferred style.
