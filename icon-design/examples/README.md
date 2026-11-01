# Field Lens — original demonstration

This example is an original icon study produced for the skill, not copied from the paid course. It depicts a lens containing a mountain, with a deep teal support, brass rim, and walnut handle. It is intentionally frontal. It demonstrates that selective material rendering does not require a diagonal overall composition.

- `field-lens.svg`: static material illustration at a 512-unit canvas; named shapes, gradients, clip, and soft shadow.
- `field-lens-small.svg`: 32-point optical master; less material detail, enlarged lens, one mountain and a broad foreground.
- `field-lens-tiny.svg`: 16-point optical master; removes the landscape shading and secondary peak, simplifies the case and rim.
- `composer-layers.svg`: distinct clean foreground geometry on a 1024 canvas for layer handoff. No outer mask, painted ground shadow, or glass reflection. Configure the background and material in Composer.
- `manifest.json`: ten explicit macOS/static logical resources. @2x versions use the appropriate logical master, not whichever source happens to have matching pixel dimensions.

The rounded green support in the static example is an illustrated object in a legacy/static study. Do not mistake it for the exact current Apple system mask. The Composer example deliberately omits that support so the platform route controls the background and boundary.

Build from the commands in `references/tooling.md`. Inspect the actual output at intended size. The example is a renderer/workflow demonstration, not a claim of production brand approval or a rendered Liquid Glass preview. New product work should begin with its own brief and concepts.

Revision after visual critique: the first study had an off-axis attachment and weak material development. The revised masters construct every handle in the lens-centered coordinate frame. The large version adds a physically joined collar, curved walnut grip, machined rim, restrained glass reflections, and more deliberate tonal separation. Geometric correctness is necessary; visual acceptance remains a separate judgment.
