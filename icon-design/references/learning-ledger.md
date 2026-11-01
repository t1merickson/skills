# Learning ledger and source boundaries

## Corpus and method

Primary historical source: **Icon Resource**, by **Sebastiaan de With**, plus bundled Iconfactory IconBuilder/IconExaminer material. Studied locally on 2026-10-03. The supplied collection contains 138 file entries, including 15 MOV lessons totaling 9,512.85 seconds (about 2h 38m 33s), five PDFs totaling 70 pages, 17 PSDs, palettes, final icon resources, scripts/actions, documentation, UI resources, and legacy binaries.

All video audio was extracted and transcribed locally with MLX Whisper large-v3-turbo. A second pass reduced repetitive hallucinations. All 950 still frames sampled across the videos at roughly ten-second intervals were visually reviewed, alongside complete transcripts. This is **full-duration audio processing plus sampled visual review**, not native continuous watching or frame-by-frame inspection. Transcripts are machine evidence, not authoritative quotations. Proper names were checked against visible/textual sources. Silent sequences were interpreted from frames, not hallucinated speech.

All PDF pages were read as text and rendered images. PSD layer inventories and embedded merged previews were inspected. Scripts, presets, localized copy, and configuration were read. Small raster assets and palettes were previewed. Legacy executable/resource binaries were identified and inspected structurally/through strings; they were not run or exhaustively reverse engineered. The bundled short sound effect received audio extraction and ASR inspection, but its ASR output is not reliable speech evidence. Eight `Icon` carriage-return entries are symlinks to an unrelated empty file, not recovered resource-fork artwork; no unrelated content was pursued.

The detailed file IDs, hashes, derivatives, and coverage record belong to the local research directory, not the portable skill. None of the course media or source illustrations is redistributed here. This ledger is an original synthesis and index of decisions.

## Lesson-to-practice map

Times are approximate locations in the reviewed media. They are navigation aids, not exact quotations.

| Local ID / lesson | Key observation | Durable practice / update |
|---|---|---|
| F135 Theory 1 Introduction | Design knowledge and technique are both needed | Explain why a shape works before teaching the command |
| F136 Theory 2 About Icons | Identity, function, and context define different icon jobs | Separate app identities, documents, and interface symbols |
| F137 Theory 3 History | Aesthetic and hardware constraints evolve | Preserve principles without making period style universal; historical firsts are not relied on |
| F138 Theory 4 Standards, ~2:36–3:26 | Optical occupancy relative to neighboring icons | Compare mass and context, not only numeric bounds |
| F138, ~3:39–4:00 | Repeated angled compositions in period Apple examples | Treat tilt as a contextual convention, not a law |
| F124 Technique 1 Introduction | Scope is the author's 2D illustration workflow | Translate mechanisms to SVG; do not require Photoshop or ban 3D |
| F127 Technique 2 Sketching, ~0:12–1:32 | Associations → sketches → two or three digital roughs | Compare distinct metaphors at equal finish |
| F128 Technique 3 Illustration, ~1:40–3:35 | Editable shape geometry and fill/mask separation | Named SVG shapes, gradients, clips; scalable geometry still needs optical review |
| F129 Technique 4 Pencil, ~5–10m | Metal banding and shared object geometry | Material-specific light response with reusable contours |
| F129, ~12–15m | Nonrectangular gradient treatment; grayscale exposes tonal errors | Shape-following highlights and value checks before texture |
| F129, ~18–29m | Rounded eraser, restrained grain, bare wood versus paint | Distinguish finishes and texture amplitude; scale effects consciously |
| F129, ~30–34m | Scalloped sharpened boundary and related masks | Update fill/clip/texture together; inspect leaks |
| F130 Technique 5 Document, ~0–7m | Curl contour, smooth handles, shaped fold shadow | Geometry before effects; cast shadow belongs on receiving surface |
| F130, ~10–14m | Background stress and early small preview | Validate contrast and scale before finishing |
| F131 Technique 6 Pieces | Reusable source with disposable merged composition | Preserve editable originals; distinguish source from outputs |
| F131 | Layered shadows and height cues | Separate contact and broad cast/ambient components |
| F132 Technique 7 Shading, ~0–12m | Brush silhouette, metal, directional fibers, curved reflection | Material and geometry must agree |
| F132, ~12–20m | Grooves/tips correspond; local attachment shadow | Structured irregularity and coherent material contacts |
| F132, ~20–27m | Texture cleanup, porous bristle shadow, fade with distance | Inspect alpha; tailor shadow to the object, not just bounding box |
| F133 Technique 8 Composition | Correct perspective in context; reduce competing rainbow | Revisit source proportion; subordinate support to hero |
| F133 | Paper thickness, fold alignment, optional second sheet | Detail hierarchy and coordinated layers |
| F134 Technique 9 Resizing | Rebuild 32/16, simplify perspective, remove sheet, strengthen cues | Explicit optical sources; regenerate without overwriting them |
| F125 Technique 10 Creating the Icon | Package resources and inspect real system surfaces | Separate render, package, and native-context checks; old Icon Composer is a different tool |
| F126 Technique 11 Postscript | Accelerated alternate artwork reuses document structure | Build families from reusable bases; inspect silent work visually |

## Documents, tools, and assets

- **F100 course Documentation.pdf (10 pages):** compact theory and reference context. Author spelling comes from this document, not the ASR rendering “DeWitt.” Its illustration/history examples are study sources, not reusable skill assets.
- **F095 New Features (3 pages), F096 QuickStart (1), F097 Tutorial (29), F098 User's Guide (27):** separate capture, preview, and verification; explicit resource families; alpha/background views; stable state anchors; badges and base reuse. These motivated the manifest and inspector.
- **F099 What's New / licensing text:** version history includes fixes involving malformed resource metadata and compression. Validate resources instead of trusting container existence. Third-party license text is not a license for copying the entire course.
- **F021–F025 Fireworks scripts:** automate grid placement and resampling, sometimes with approximate ratios and destructive merging. Replace coordinate-driven output with explicit resource slots and exact dimensions. Do not inherit global-editor-state changes.
- **F027 Photoshop actions:** action names and opcode/string structure expose similar build/resize/merge/color-depth automation. Not executed or fully reconstructed. Their useful intent is implemented independently.
- **F029/F031–F033 grids and F111–F123 PSDs:** inspect layer types, masks, hidden alternatives, and merged previews. The pencil/brush masters retain shape construction; the composition contains disposable pixel layers. Their practical lesson is reversibility and component reuse, not dependence on PSD.
- **F015–F019 palettes:** period compatibility targets, not a modern color identity system. Full-color rendering and appearance-specific values supersede automatic commitment to 16/256-color tables.
- **F103–F110 finished resources:** compare representations and authored small sizes. They are evidence of the final artifact, not a guarantee that every bundled format is visually identical.
- **Legacy apps/plugins/nibs/resources:** application architecture and UI copy reveal explicit size/state/depth checks, alpha inspection, and preview controls. The new tool implements a bounded subset from those concepts. It does not claim feature parity or revive obsolete binary compatibility.

## Corrections to the blind braindump

Confirmed: silhouette, material coherence, optical centering, actual-size inspection, editable geometry, and separate export verification. Strengthened: size-specific composition is a primary design activity, not just sharpening after export.

Updated: app-icon masking and current material ownership must be route-specific. Old free silhouettes and baked shadows cannot be treated as the modern Composer contract. Current dark/mono/clear behavior requires more than a single default image. A blanket iOS-opacity rule is too broad once foreground layers and dark variants are considered.

Rejected as universal rules: negative-nine-degree tilt; one perspective for all app classes; black-only shadows; 72/96 DPI as a screen-quality control; fixed low-color palettes; always rasterizing transformed vector art; automatic large-to-small scaling as sufficient; old favicon troubleshooting that clears unrelated browser data.

Historical interpretation rather than established fact: the course's compressed pictogram/writing/GUI origin story. It is unnecessary for the skill's production claims and should not be repeated as a definitive history.

## Modern sources

The dated primary-source guidance and links are in [Apple delivery](apple-delivery.md) and [Evolution and future](evolution-and-future.md). These include Apple's current HIG and Xcode documentation, the 2025 icon design and Composer talks, and contemporaneous 2013/2020 redesign announcements. The local research captures include current 2026 documentation. A documented UI control is not proof that the installed tool or an older deployment OS supports it.

## Teaching order and limits

Teach recognition → silhouette → editable geometry → values → material → composition → optical variants → packaging → real-context review. Introduce gradients only after surfaces exist; texture only after form reads; automation only after the manifest preserves authored choices. Then show where the simplified model breaks: appearance changes, system materials, renderer variation, and physical display scale.

Open limits: no continuous frame-by-frame video review; no execution of legacy binaries; no subjective production approval for the original example; no integrated `.icon`/Xcode app delivered by this skill-building task; native ICNS decode discrepancy remains documented; Windows-specific shipping guidance not refreshed. These are explicit boundaries, not hidden passing gates.
