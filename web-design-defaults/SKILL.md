---
name: web-design-defaults
description: timmy's base web design direction: Base UI, system fonts, no Tailwind, black-and-white minimalism.
---

# web-design-defaults

the baseline for timmy's web projects. a project's own design system or an explicit direction from timmy overrides all of it.

## the direction

minimal, quiet, information-dense. the shadcn-adjacent aesthetic without the framework baggage: hairline borders, subtle radii, generous whitespace, type doing the work. the interface should look like it was designed by someone who kept deleting things until it was done.

## hard rules

- **no Tailwind.** plain CSS or CSS modules. utility-class soup is off the table even if a template arrives with it.
- **system fonts.** `font-family: system-ui, -apple-system, sans-serif` for UI, `ui-monospace` for code. no webfont downloads unless timmy asks.
- **Base UI for components** (base-ui.com): unstyled, accessible primitives (popovers, menus, dialogs, selects). style them ourselves. don't hand-roll a11y-heavy components Base UI already provides, and don't pull in styled kits on top of it.
- **black and white first.** near-black text on white, or the inverse in dark mode. color enters only with a job: state, warning, a single accent earning its place. no decorative gradients.

## defaults

- borders: 1px, low-contrast (`#e5e5e5`-ish light, `#262626`-ish dark). borders over shadows; shadows only for true elevation like menus and dialogs, and subtle there.
- radii: small and consistent, 4 to 8px. one radius scale per project.
- spacing: a 4px base scale. whitespace is the main grouping tool, boxes are the fallback.
- type: few sizes, real hierarchy from weight and spacing rather than size explosions. body around 14 to 15px in dense UI.
- dark mode: respected from the start via `prefers-color-scheme`, same structure, inverted neutrals.
- motion: minimal and physical. small distances, quick springs, nothing looping. the `apple-design` skill has the physics; `find-animation-opportunities` decides what earns motion at all.
- empty states, focus rings, and hover states are part of the design, not afterthoughts. visible focus always survives.

## when unsure

two or three static mocks per the `mock-and-pick` skill beat guessing. timmy picks fast.
