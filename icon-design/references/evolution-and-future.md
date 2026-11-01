# Twenty years of change: preserve the craft, choose the era deliberately

Coverage: roughly the mid-2000s through October 2026. This is a practical design history, not a claim that every icon or designer followed the same sequence. Platform changes, production changes, and judgments are distinguished below. The supplied course bundle is mixed: some manuals carry 2005-era copyright, course slides show 2008, and the included IconBuilder 8.5.2 files reach 2009. Its original release year has not been established from those facts alone.

## Separate the axes before naming the style

An icon can be frontal and dimensional. It can be tilted and flat. It can be rendered in 3D and look graphic. It can be drawn in SVG and convincingly describe volume. These are independent choices:

| Axis | Choices | What the choice controls |
|---|---|---|
| Representation | abstract mark, familiar object, scene | Recognition and association |
| Projection | frontal, orthographic oblique, perspective | Visible surfaces and foreshortening |
| In-plane orientation | upright, diagonal, arbitrary rotation | Rhythm and occupied space |
| Depth | flat, shallow relief, volumetric | Overlap and surface relationships |
| Material | matte, paper, metal, wood, glass | Light response and personality |
| Detail | symbolic, selective illustration, dense realism | Information surviving reduction |
| Rendering ownership | painted/static, system material, hybrid | Who controls light and appearance |
| Container | free silhouette, authored tile, system mask | Boundary and platform integration |

Never use “3D” as a complete art direction. Specify these axes. The historical negative-nine-degree tilt is a composition convention observed in the course, not a prerequisite for depth. A modern upright lens can retain metal, glass, contact, and thickness without recreating a tilted stack of documents.

## A bounded chronology

### Mid-2000s: the icon as a small illustrated object

In the supplied course, the Mac application icon is developed through metaphor, object illustration, material rendering, composition, and bespoke small versions. Shadows and highlights live in the artwork. A document, pencil, and brush form an explanatory scene; desk-like perspective and diagonals contribute to the period's visual language. The tiny versions are actively redesigned.

The surrounding tools expose multiple size, depth, mask, and state resources. Fixed grids and Photoshop/Fireworks automation make those resources manageable. The constraints include lower-resolution viewing and compatibility with older display palettes. These constraints explain some techniques, but not all their value. Deliberate silhouettes, coherent lighting, and optical correction remain useful when indexed palettes disappear.

**Keep:** a distinctive physical or conceptual identity; knowledge of how materials behave; attention to every delivered size. **Contextualize:** desk perspective, angled paper, tool-over-document formulas, low-color resources, resource-fork customization, and exact size tables. A formula that once communicated category can become a cliché or obscure a different product.

### 2013: simplification becomes a dominant platform direction

Apple's iOS 7 announcement dates the redesign to June 10, 2013 and emphasizes simpler typography, translucency, motion, and functional layers. It is evidence of a changed platform language, not proof that dimensional thinking vanished. [Apple's iOS 7 announcement](https://www.apple.com/newsroom/2013/06/10Apple-Unveils-iOS-7/)

**Interpretation:** the useful lesson from the flatter period is reduction: clearer grouping, fewer incidental textures, and a stronger graphic core. The failure mode is to confuse reduction with sameness. Removing all material cues can remove character without improving the silhouette. A generic glyph on a gradient may be technically simple while remaining difficult to remember.

Do not retrospectively call all realistic imagery “skeuomorphism.” A depiction of a physical object, a retained obsolete affordance, and an ornamental texture are different design decisions. Explain which one is being retained or removed and why.

### Higher density and larger source art: more samples, the same small attention window

The course's hand-tuned 16-pixel work and today's large app-icon canvases solve related but different problems. More display pixels permit smoother contours and subtler tonal transitions. They do not increase the amount of attention someone gives a small icon, or guarantee that fine structure can be recognized.

**Synthesis:** higher resolution should first buy cleaner edges and more controlled material transitions. Spend it on additional detail only after the hierarchy survives. “High definition” can mean a beautifully resolved simple object rather than a crowded miniature scene. The logical-size distinction remains important even as automatic rendering becomes more capable.

### 2020: Mac identity within a more consistent family

Apple's June 22, 2020 Big Sur announcement explicitly describes Dock icons becoming more consistent across its ecosystem while retaining Mac personality. [Apple's Big Sur announcement](https://www.apple.com/newsroom/2020/06/apple-introduces-macos-big-sur-with-a-beautiful-new-design/)

**Interpretation:** a stronger shared container and family language shifts differentiation inward. Character increasingly depends on the foreground relationship, color, proportion, and material rather than only a free outer silhouette. The design challenge is to preserve distinctiveness within that common frame. Uniform containers are not a sufficient reason to give every product the same rendering recipe.

### 2025–2026: some dimensional rendering moves into the platform

Apple's 2025 design talk presents layered material effects and contrasts the old perspective Chess artwork with a flatter frontal treatment that works with those effects. It does not equate richer rendering with more elaborate perspective. [Say hello to the new look of app icons](https://developer.apple.com/videos/play/wwdc2025/220/)

Current production details are in [Apple delivery](apple-delivery.md). The material system can supply depth and changing light; the source can therefore be graphically simpler while the displayed result is richer. This changes the ownership of effects. An author still controls identity, geometry, layering, and material choices, but no longer necessarily paints the final appearance of every edge.

**Synthesis:** this is not merely a pendulum from “3D” to “flat” and back. It is also a movement from authored static shading toward a negotiated result between artwork, renderer, OS version, user appearance, and background. Keep the source capable of supporting that negotiation without losing the product's visual anchor.

## Things that remain, and things worth recovering

The following are editorial judgments for this skill, not claims that all historical designs possessed them or all modern designs lost them.

| Principle | Why it should survive | How to practice it now |
|---|---|---|
| Specific identity | People remember particular forms and relationships | Establish an unmistakable anchor before effects |
| Material literacy | Light can explain structure and personality | Study real surfaces; simplify their strongest cues |
| Optical authorship | Numerical scale does not guarantee perceptual equivalence | Review intended sizes; author exceptions where supported |
| Honest contact and depth | Contradictory shadows weaken even playful art | Make contacts and occlusion coherent |
| Product personality | Consistency alone does not create attachment | Let color, proportion, motif, or material carry a distinctive choice |
| Restraint through understanding | Removing detail thoughtfully is different from never learning it | Understand the object, then omit what is unnecessary |
| Editable construction | Iteration should improve the design without rebuilding it | Preserve geometry, materials, and generated outputs separately |
| Contextual judgment | An isolated hero render can mislead | Compare peers, appearances, backgrounds, and real deployment |

Worth recovering is the care devoted to the tiny final object: the sense that someone chose the contour, not merely selected an effect. That care can appear in a one-color symbol, a frontal relief, or a richly illustrated instrument. It is not tied to an old gloss treatment.

## A possible return to richer rendered icons

**Hypothesis, not forecast:** richer 3D or selectively realistic app icons may gain renewed interest. Dimensional system materials already provide one form of richness, but that does not prove a broad return to elaborate object illustration. The future could contain both carefully modeled product icons and simpler shapes whose rendering is largely system-owned.

Prepare for this possibility without choosing it for every task:

1. Keep geometry and material decisions separable from the current platform finish.
2. Explore frontal or shallow-relief compositions before reaching for theatrical perspective.
3. If using a 3D tool, specify camera, lighting, material roughness, silhouette, and output passes. Preserve the scene or generator, not only its beauty render.
4. Render at delivery resolution and inspect small; high sample count does not rescue weak shape hierarchy.
5. Separate the object from its ground and cast shadow where the destination owns those effects.
6. Keep a graphic recognition anchor that survives dark, clear, or tinted appearances.
7. Compare a rich and a reduced version of the same concept at equal intended size. Choose from evidence, not nostalgia or fashion.

A useful experiment is an upright enamel badge, instrument, or shallow sculpted emblem: controlled thickness, a small number of material boundaries, one lighting logic, and a strong frontal silhouette. That can feel tactile and highly resolved without importing the old angled document composition.

## Agent decision record

For each new icon, state: which historical principles are being retained; which period conventions are being omitted; who owns the final effects; and which future change the editable source can accommodate. A concise example:

“Retain selective material realism and small-size authorship. Use an upright, near-frontal composition. Keep system-owned shadows out of the Composer layers. Preserve a separate static illustration master for contexts that require a painted render. The lens/mountain relationship is invariant across treatments.”

Do not call this direction universally modern. It is a deliberate, revisable design choice supported by the target context.
