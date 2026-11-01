# Materials, light, and depth

This chapter applies primarily to authored static illustration. For dynamic Apple app icons, transfer the object structure and hierarchy while leaving the system-owned material effects to Icon Composer. The two routes can share geometry without sharing every highlight.

## Establish a lighting contract

Write down the main light direction, softness, ambient fill, viewing angle, and approximate support plane. Upper-left light is a useful convention, not a law. Check every facet, reflection, and shadow against the chosen setup. Objects can have different reflectance; they should still appear to occupy the same scene.

Distinguish three mechanisms:

- Form shading describes how a surface turns relative to light.
- A specular reflection describes the light environment reflected by a material.
- A cast shadow describes one object blocking light from reaching another.

Painting all three as the same diagonal black-to-white gradient produces unclear material. A highlight need not sit at an object's geometric center, and a cast shadow need not be a scaled duplicate of the front silhouette.

## Metal

A compact sequence of bright and dark bands can convey a smooth metallic ferrule. The adjacency and width of the bands matter more than their number. Keep transitions along the curvature rather than randomly across the surface. A soft bright band suggests a broad light source; a narrow bright edge next to a darker band can suggest polished metal. Flat gray alone generally reads as gray paint.

Metal should connect plausibly to adjacent materials. Add a restrained contact shadow where a ferrule grips wood or bristles. Avoid giving every boundary the same heavy outline. At small sizes, simplify the multistop gradient to two or three value zones; a large-scale realistic reflection can collapse into striped noise.

## Painted wood and exposed wood

Painted facets are a strong starting exercise: build the polygonal body, assign related values to adjacent faces, and keep the light-facing plane coherent with the tip and fittings. Saturated paint can become unpleasantly neon under aggressive additive or dodge blending. Prefer a controlled highlight color and opacity when the blend operation changes hue unexpectedly.

Exposed wood needs directional texture aligned with its structure. Clip fibers to the tip, adapt their direction to the shape, and keep their contrast subordinate to the overall form. The boundary where paint meets sharpened wood can be scalloped, but the tip mask, paint mask, and texture masks must agree. A tiny texture leak can look like a damaged edge.

Do not apply the same grain amplitude to bare wood and a painted shaft. The finish changes what texture is visible. Seed procedural grain and retain its generator. Randomly regenerating grain on every export makes comparison harder and hides unrelated changes.

## Paper and curled surfaces

A page is not simply a white rectangle with a universal drop shadow. First define the contour and thickness. For a curl, distinguish front face, reverse face, crease or bend, and the shadow on the receiving sheet. Build the fold's contour from observation or a clear spatial model; a sharp accidental cusp can read as torn paper.

Use a shaped shadow beneath the curl, clipped to the page where appropriate. Its darkest part is usually near contact; its spread and softness change as the curl lifts away. A generic offset duplicate can be a useful rough, but inspect the far end and the attachment point. If the curl seems detached, fix geometry and contact before darkening the whole shadow.

Nearly white paper can retain enough shading to express form while remaining white perceptually. Check it on white, gray, dark, and saturated backgrounds. If its silhouette disappears, decide whether a subtle edge is part of the illustration or whether contrast must come from the surrounding icon composition. Don't solve every background with an indiscriminate thick stroke.

## Fibers, hair, and bristles

Texture direction must reinforce the object's growth or construction. A brush spreads toward its tip; straight parallel stripes over a fan-shaped outline contradict that form. Warp or generate the fiber directions to match the spread. Distinct tips and dark grooves should correspond; decorative scallops unrelated to the texture look stamped.

Material porosity affects shadows. A solid black slab beneath a brush tip makes soft bristles look like a rigid block. Thin or interrupt the shadow locally while keeping the attachment point grounded. Use irregularity in bounded amounts: too uniform looks manufactured, too random loses the brush's large silhouette.

At tiny sizes, describe bristles as a shaped mass with one or two directional breaks. Individual hairs are rarely the identity-bearing detail.

## Erasers, rubber, and matte materials

Use broad, quiet tonal transitions. A small edge light can describe a rounded eraser without turning it into polished candy. Saturation should remain consistent with the material. A bevel is one possible construction aid, not the material itself. Compare a matte surface with its neighboring metal: if both share identical highlights, the material distinction has failed.

## Contact and cast shadows

Separate a compact, relatively dark contact shadow from a broader, softer ambient or cast shadow. This often offers better control than one enormous blur. Shift and shape the shadow according to the object's height and receiving plane. Distance from the surface generally increases softness for an extended light source, but the exact shape depends on geometry and lighting; avoid prescribing a single blur formula as physics.

A shadow near a page fold belongs on that page. A ground shadow belongs on the support plane. A cast shadow crossing different surfaces may need separate clipped pieces. Taper or fade an illustrative cast shadow when that improves the intended reading, while preserving convincing contact.

The course's advice favoring black shadows is contextual: neutral translucent shadows are convenient over arbitrary backgrounds. It is not a universal prohibition on colored shadows or reflected color. Use the actual compositing context. For Apple material rendering, use and inspect the available system shadow treatments instead of duplicating them in source layers.

## Material review

Temporarily hide texture. Does the object still have volume? Hide highlights. Are the silhouette and overlaps coherent? Hide shadows. Is the scene's arrangement still understandable? Restore each layer and ask what it contributes. Remove effects that cannot justify themselves.

The aim is not exhaustive simulation. It is a small, coherent set of cues that stays convincing under reduction. Large-preview realism that destroys small-preview recognition is a failed tradeoff for an icon.
