# Editable construction in SVG

## Build a scene, not an undifferentiated picture

Use named groups for physical objects and meaningful surfaces. Keep geometry, fill, texture, highlights, contact shadows, and cast shadows distinguishable. A reasonable order is: background/support, cast shadows, rear objects, front objects, material details, restrained reflections. A shadow belongs to a relationship between two objects; do not leave it behind when moving one of them.

SVG is especially useful when the icon is a controlled assembly of paths, shapes, gradients, and masks. It allows precise edits, reusable geometry, named parameters, and inexpensive optical variants. Raster painting remains appropriate for intricate organic detail; 3D rendering can be appropriate for complex perspective and controlled lighting. Pick a route based on controllability, not a blanket claim that one medium is colder or more artistic.

The included renderer supports a deliberately small SVG subset. Use `<path>`, primitive shapes, gradients, groups, local `<use>`, clipping, masks, and supported filter primitives. Outline text. External assets, scripts, embedded HTML, live fonts, and broad CSS are rejected to make local rendering reproducible. This is a portability constraint of the kit, not a claim that SVG itself cannot express them.

## Geometry first

Start with a handful of shapes at a consistent coordinate scale. Establish the main axis, focal point, and object-to-object proportions before rounding every corner. For smooth Bézier curves, prefer a few intentional points with tangential handles over many little corrections. A curled page needs a convincing folded contour before it needs a gradient. A tapered handle needs believable thickness before it needs a highlight.

Use shared geometry rather than almost-matching copies. Define a shape once and reuse it for fill, clip, and edge where possible. If the underlying contour changes, texture and shading should follow. When separate paths represent adjoining surfaces, inspect seams after rasterization. Perfectly adjacent vector edges can reveal antialiasing cracks; a slight concealed overlap is often more reliable.

Boolean operations are an authoring technique. SVG fill rules can express holes, but overlapping paths do not automatically behave like an editor's union. Use `fill-rule="evenodd"` intentionally, or resolve the path operation in the generator. Inspect the result at corners and intersections. Keep symmetrical construction when it helps, then merge or overlap the center seam and introduce asymmetry only where it explains the object.

## Shared axes and mechanical attachments

Construct attached parts in a common coordinate frame. For a magnifier, define the lens center `(cx, cy)` once. Put the handle on the local vertical axis, centered at `x=0`, and apply `translate(cx cy) rotate(angle)` to its entire group. The collar, grip, end cap, highlights, and shadows derive from that same frame. A handle can be parallel to a radius while still missing the center; checking its angle alone is insufficient.

For an independently constructed straight attachment with centerline point `P` and unit direction `u`, its perpendicular offset from circular center `C` is `abs((C.x-P.x)*u.y - (C.y-P.y)*u.x)`. A radial handle should have zero intentional offset. More importantly, extend the centerline visibly through the object in a temporary diagnostic overlay and inspect the join at actual size. Do not hide a misaligned connection under a shiny collar.

Also distinguish geometric center from perceived balance. Shared-axis construction fixes a mechanical attachment; optical placement fixes the assembled icon's mass within its container. Neither substitutes for the other. Move the whole assembled object when correcting overall balance so the attachment remains coherent.

## Gradients and highlights

Choose gradient coordinates explicitly. With `gradientUnits="objectBoundingBox"`, a reused gradient stretches with its shape; this is convenient for normalized objects but may distort the lighting. With `userSpaceOnUse`, the light field is anchored to the scene's coordinate space; this can help adjacent surfaces share a coherent direction. Neither setting automatically produces physically correct shading.

Describe curved highlights with paths when a generic gradient does not follow the contour. A long highlight on a brush handle should taper and bend with the handle. A duplicated silhouette filled with a gradient and clipped to itself is safer than destructively erasing a highlight. Use a small number of purposeful gradient stops. Many arbitrary stops can produce banding or an unintended chrome effect.

Keep broad tonal modeling independent from high-frequency texture. Test values in grayscale. If the object already fails to read without texture, adding texture makes the failure more expensive to repair.

## Clip paths, masks, and alpha

Use a clip path for a hard geometric boundary. Use a mask for varying visibility. Set mask semantics explicitly when crossing renderers: luminance and alpha masks are not interchangeable. In the ordinary PNG alpha channel, 0 is transparent and 255 is opaque. A legacy UI showing “black mask = opaque” is a display convention, not a reason to invert PNG alpha.

After blur, inspect the filter region and the canvas boundary. A filter's default region may crop the very shadow it produces. Expand it enough for the effect, while keeping the canvas extent intentional. Clipping a blurred shadow to the receiving page can be correct; clipping the entire object's ground shadow to its silhouette cannot produce a cast shadow outside it.

Black or white halos usually indicate a compositing or export problem, not a need for a thicker border. Inspect partial-alpha pixels on contrasting backgrounds. Avoid flattening onto a temporary background before exporting transparency. When resizing raster art, use a pipeline that handles premultiplied alpha correctly, then inspect the result. The kit's renderer probe checks selected behavior; it does not qualify every possible filter combination.

## Transform safely

Use transforms for composition while the geometry remains editable. Determine whether strokes, gradients, patterns, and filters should transform with the object. A Photoshop layer-style artifact during rotation is not a universal reason to flatten every SVG. Render a proof of the transformed object and compare its lighting with its neighbors.

Separate the source object from disposable composition renders. For complex raster layers, copy or render into a derived file before perspective distortion. Never let that copy become the only surviving source. Record corrections that happen only in an optical variant so a future regeneration does not remove them.

## Layer preparation for Icon Composer

Use a second source intended for material rendering. Reuse the identity and geometry, but remove painted inter-layer shadows and glass reflections that the system will own. Separate independently colored or adjustable elements. Preserve the full canvas on every export; cropping every layer to its own bounds loses registration. The `layers` command exports named top-level groups and shared definitions, preserving coordinates. It does not infer which layers should be glass or remove effects automatically.

Avoid cross-layer `<use>` dependencies outside shared `<defs>`: a layer exported alone cannot reference a sibling omitted from its file. Put shared paths in definitions. Check every exported layer independently and recomposed before import. Group related pieces in Icon Composer according to intended material and depth, not merely the number of SVG files.
