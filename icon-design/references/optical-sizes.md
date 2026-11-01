# Optical sizes, appearances, and families

## Scaling is a starting hypothesis

Geometric scaling preserves ratios. Perception does not. Reduction averages high-frequency features, narrows gaps, changes apparent weight, and can erase the single cue that identifies an object. A perfect vector contour can rasterize into an indecipherable miniature.

Start a size study as soon as the silhouette and composition exist. Show the smallest expected context next to a generous preview. If the small icon is unclear, change its large relationships before spending hours on texture. Do not postpone small sizes until final packaging.

For a static desktop illustration, useful study sizes include 16, 32, 64, 128, 256, and 512 pixels, plus actual high-density resources. These are investigation sizes, not a universal shipping table. Current Composer output and Xcode asset catalogs have their own delivery rules. For those routes, still inspect small renders and simplify the shared artwork when necessary; do not assume there is a supported per-size override inside every modern pipeline.

## Logical size matters

Pixels = points × scale for a specified resource. A 16-point @2x resource has 32 pixels. So does a 32-point @1x resource. They occupy different logical sizes and can benefit from different compositions. The manifest retains platform, appearance, points, scale, pixel dimensions, and explicit source. Do not deduplicate resources by pixel dimensions alone.

Display context matters too. A screenshot viewed at arbitrary browser zoom is not an exact physical-size test. Record display scale, screenshot scale, application context, and whether the proof is a native render or only a raster study.

## How to make an optical master

Preserve the identity-bearing relationships. Then consider, in order:

1. Remove secondary props and background patterns that do not survive.
2. Widen narrow negative spaces or separate adjoining objects.
3. Enlarge the identifying cue: fold, handle, aperture, notch, badge.
4. Reduce perspective if it compresses important surfaces into slivers.
5. Straighten an object if angled raster edges overwhelm its information.
6. Adjust weight of outlines and highlights independently.
7. Reduce texture and gradient complexity.
8. Shift the whole composition optically after local edits change its mass.

The course's 32-pixel paper is a redrawn composition, and its 16-pixel version receives further individual-pixel corrections. This is an argument for authored optical decisions, not a command to hand-paint every modern high-density asset.

For SVG masters, use coordinates suited to the target logical grid. A one-pixel centered stroke at integer coordinates may straddle pixels; a half-unit adjustment can help for that exact raster scale. Filled rectangles aligned with pixel boundaries behave differently from centered strokes. Do not mechanically snap every curve or diagonal. Compare rendered alternatives at actual size.

Raster touch-up can be appropriate for final tiny art. Store the authored raster as a source referenced by the manifest, with a clear name and rationale. Do not place it in a build directory that a future export assumes disposable. Keep the larger editable source and the small raster both.

## Maintain identity across the family

Choose invariants: silhouette, dominant shape relationship, location of the recognition anchor, and a small set of proportions. Allow variables: detail density, line weight, local spacing, perspective compression, and material complexity. Record intentional differences. Otherwise one size becomes an unrelated logo by gradual correction.

For document families, share the base and vary a strong badge or content motif. Tiny sizes may emphasize the badge when the base consumes too much space. Keep badge placement and scale consistent enough to preserve recognition. State changes should have a stable visual anchor so the object does not jump. Do not infer that an old Finder resource state is supported by a current app simply because an old manual describes it.

## Appearances are authored relationships

Dark appearance is not a mechanical inversion. A color that distinguishes the hero in light appearance can disappear on a dark ground. Mono or tinted appearance can collapse two different hues into one tone. Preserve the visual anchor using value, spacing, or controlled outlines; do not silently substitute a different metaphor.

Review appearance variants as a matrix across intended sizes and backgrounds. A variant that works on its own can have a mismatched apparent size beside another. Avoid changing the silhouette, crop, and material simultaneously unless there is a deliberate product reason. Separate alternate identities chosen by the user from appearances chosen by the system.

## Failure diagnosis

| Observation | Likely cause | First experiment |
|---|---|---|
| Big render beautiful, small one muddy | Too many comparable details | Remove detail before sharpening |
| Thin halo around every object | Resampling or flattened matte | Inspect RGBA and compositing pipeline |
| Small icon feels too heavy | Border/highlight dominates area | Reduce edge opacity or simplify border |
| Icon jumps between sizes | Changed visual center | Compare anchor and mass, then shift |
| Two objects merge in mono | Hue carried all separation | Change values or the gap |
| Pixel zoom looks good, actual size fails | Local edits lost global hierarchy | Return to silhouette/value view |
| Regeneration loses small-size fixes | Override was stored as output | Promote it to explicit source |

Sharpening cannot reconstruct a concept that has disappeared. Use it sparingly after the composition works, and inspect halos and saturation changes.
