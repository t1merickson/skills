---
name: icon-design
description: "Design, refine, inspect, and package macOS or iOS icons using editable SVG, optical size variants, and explicit Apple delivery routes. Use for app identities, document icons, icon families, or icon craft reviews; distinguish these from interface symbols. Includes material illustration, small-size correction, Icon Composer layer preparation, and reproducible raster/ICNS tools."
---

# Icon design

Make a recognizable object at its actual viewing size. Preserve the editable design decisions and prove the delivered resource matches them.

## Start here

1. Identify the role: **app identity**, **document/file type**, **interface symbol**, or **customization artwork**. Record the app's human purpose, audience, recognizable anchor, platform, minimum OS, current Xcode, appearances, and exact deliverables. Infer routine choices; ask only for missing decisions that affect direction.
2. Read [Concept and judgment](references/concept-and-judgment.md). For premium craft or reference-led work, read [Premium reference review](references/premium-reference-review.md). Produce two or three materially different silhouettes when the direction is open. Use SVG roughs; do not perfect three cosmetic variations of one idea.
3. For style direction, modernization, or dimensional artwork, read [Evolution and future](references/evolution-and-future.md). Separate depth, perspective, tilt, and rendering ownership. Select the delivery route before adding effects. Read [Apple delivery](references/apple-delivery.md): clean layered art for Icon Composer; painted masters for static illustration/asset catalogs; separate symbol conventions for UI. OS-dependent facts are dated and must be refreshed when shipping.
4. Build named geometry, then value hierarchy, material, and restrained detail. Read [Construction](references/construction.md) and, for dimensional illustration, [Materials and light](references/materials-and-light.md).
5. Review early at intended size. Read [Optical sizes and families](references/optical-sizes.md). Author smaller compositions when scaling loses identity. A 16-point @2x resource and a 32-point @1x resource can need different artwork despite both being 32 pixels.
6. Render and inspect using [Tooling](references/tooling.md). Use a new output directory each build. Exporting must never replace an authored optical source. Verify receipts after edits.
7. Read [Review and delivery](references/review-and-delivery.md). Inspect actual renders, alpha, light/dark/busy backgrounds, peers, and target application. Record source, raster, package, OS-context, and human acceptance separately.

## Non-negotiable craft

- One recognizable idea leads. Detail earns its place by improving identity, depth, or material.
- Optical balance wins over numeric symmetry. Metrics identify questions; they do not grade beauty.
- Preserve identity across sizes and appearances; simplify geometry and redistribute contrast.
- Keep authored surface shading distinct from system-owned effects. Avoid double shadows and baked glass in Composer inputs.
- Preview every new rendering technique before scaling up its use. An SVG that parses can still render differently across engines.
- Treat current Apple masking as a delivery contract. Do not bake today's app-icon outer mask into Composer layers.
- Do not extrapolate 2000s desk perspective, tilt, color-depth tables, or mask conventions into current requirements.
- Never declare a static browser preview equivalent to Icon Composer or a shipped-device render.

## Progressive disclosure map

| Need | Read |
|---|---|
| Metaphor, style, critiques, avoiding generic polish | [Concept and judgment](references/concept-and-judgment.md) |
| Bézier shapes, layer structure, SVG primitives, masks | [Construction](references/construction.md) |
| Paper, metal, wood, paint, fiber, highlights, shadows | [Materials and light](references/materials-and-light.md) |
| Pixel decisions, logical size, appearance consistency | [Optical sizes and families](references/optical-sizes.md) |
| Current macOS/iOS integration and version caveats | [Apple delivery](references/apple-delivery.md) |
| CLI, inspector, schemas, dependencies, failure recovery | [Tooling](references/tooling.md) |
| Concrete acceptance and defect diagnosis | [Review and delivery](references/review-and-delivery.md) |
| Twenty-year evolution, retained craft, future dimensional styles | [Evolution and future](references/evolution-and-future.md) |
| Curated examples, material standards, junction audits | [Premium reference review](references/premium-reference-review.md) |
| Faithful from-scratch course exercise | [Course reconstruction](references/course-reconstruction.md) |
| What came from the course; what changed | [Learning ledger](references/learning-ledger.md) |
| Synthetic assertions and renderer qualification | [Fixtures](fixtures/README.md) |

## Working outputs

Keep a brief, concept sheet, editable masters, explicit resource manifest, render receipt, inspection sheet, and delivery notes. Add `.icon` or compiled packages only when that route has actually been executed. Start from the original [example](examples/README.md) when a deterministic tool smoke test is useful; do not turn its identity into the user's design by default.

The skill is an original operational synthesis of the locally studied Icon Resource course, associated Iconfactory manuals, and dated Apple documentation. It contains no course videos, transcripts, PSDs, or extracted course artwork. The separately attributed course study is independently redrawn. See the learning ledger for provenance and coverage limits.
