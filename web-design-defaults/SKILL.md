---
name: web-design-defaults
description: the user's base web design direction: Base UI, system fonts, no Tailwind, black-and-white minimalism.
---

# web-design-defaults

The baseline for the user's web projects. A project's own design system or an explicit direction from the user overrides all of it.

## The direction

Minimal, quiet, information-dense. The shadcn-adjacent aesthetic without the framework baggage: hairline borders, subtle radii, generous whitespace, type doing the work. The interface should look like it was designed by someone who kept deleting things until it was done.

## Hard rules

- **No Tailwind.** Plain CSS or CSS modules. Utility-class soup is off the table even if a template arrives with it.
- **System fonts.** `font-family: system-ui, -apple-system, sans-serif` for UI, `ui-monospace` for code. No webfont downloads unless the user asks.
- **Base UI for components** (base-ui.com): unstyled, accessible primitives (popovers, menus, dialogs, selects). Style them ourselves. Don't hand-roll a11y-heavy components Base UI already provides, and don't pull in styled kits on top of it.
- **Black and white first.** Near-black text on white, or the inverse in dark mode. Color enters only with a job: state, warning, a single accent earning its place. No decorative gradients.

## Defaults

- Borders: 1px, low-contrast (`#e5e5e5`-ish light, `#262626`-ish dark). Borders over shadows; shadows only for true elevation like menus and dialogs, and subtle there.
- Radii: small and consistent, 4 to 8px. One radius scale per project.
- Spacing: a 4px base scale. Whitespace is the main grouping tool, boxes are the fallback.
- Type: few sizes, real hierarchy from weight and spacing rather than size explosions. Body around 14 to 15px in dense UI.
- Dark mode: respected from the start via `prefers-color-scheme`, same structure, inverted neutrals.
- Motion: minimal and physical. Small distances, quick springs, nothing looping. The `apple-design` skill has the physics; `find-animation-opportunities` decides what earns motion at all.
- Empty states, focus rings, and hover states are part of the design, not afterthoughts. Visible focus always survives.

## When unsure

Two or three static mocks per the `mock-and-pick` skill beat guessing. The user picks fast.
