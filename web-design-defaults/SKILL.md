---
name: web-design-defaults
description: "Apply the user's baseline web visual direction—Base UI, system fonts, no Tailwind, and black-and-white minimalism—when creating a new web interface or when the user explicitly asks for these defaults. Do not use when an existing product has its own established design system, for backend-only work, native apps, or fixes that require no visual decision."
---

# web-design-defaults

The baseline for the user's web projects. A project's own design system or an explicit direction from the user overrides all of it.

## The direction

Minimal, quiet, information-dense. The shadcn-adjacent aesthetic without the framework baggage: hairline borders, subtle radii, generous whitespace, type doing the work. The interface should look like it was designed by someone who kept deleting things until it was done.

Quiet is not empty. Remove what is unnecessary so the primary task is obvious, then add the labels, boundaries, and density that make it understandable. A page that is calm and also vague is a worse page.

## Hard rules

- **No Tailwind for new systems.** Prefer plain CSS or CSS modules. If an existing product already uses Tailwind or another component system, work within it unless the user approves a migration; do not turn a scoped design change into a framework rewrite.
- **System fonts.** `font-family: system-ui, -apple-system, sans-serif` for UI, `ui-monospace` for code. No webfont downloads unless the user asks.
- **Base UI for new components** (base-ui.com): unstyled, accessible primitives (popovers, menus, dialogs, selects). Style them ourselves. Preserve a project's established accessible component library rather than introducing a second one for preference alone.
- **Black and white first.** Near-black text on white, or the inverse in dark mode. Color enters only with a job: state, warning, a single accent earning its place. No decorative gradients.

## Neutrals are alpha black, not gray

Build intermediate tones as black over white rather than picking gray hex values — hex grays drift warm or cool and the drift compounds across a page.

| Role | Light |
| --- | --- |
| Canvas / surface | `#ffffff` |
| Primary ink | `#000000` (or `#111` if pure black feels harsh) |
| Secondary ink | `rgb(0 0 0 / 64%)` |
| Tertiary ink | `rgb(0 0 0 / 44%)` |
| Border | `rgb(0 0 0 / 10%)` |
| Strong border | `rgb(0 0 0 / 18%)` |
| Hover fill | `rgb(0 0 0 / 5%)` |
| Pressed fill | `rgb(0 0 0 / 9%)` |

Two rules that go with it:

- **Set ink with alpha colors, never the `opacity` property.** On a container it fades every descendant; on a leaf it multiplies against the rung already there and quietly pushes text under readable contrast.
- **The tertiary rung fails 4.5:1 on white.** It is for glyphs and genuinely optional text. When real reading lives there — a timestamp someone needs, a struck-through price — lift it to about 56% instead of accepting the failure. Validate contrast rather than trusting the table.
- No beige, cream, blue-gray, or green-gray in interface chrome. A neutral derived from the project's own brand color and used consistently is brand, not drift.

## Defaults

- Radii: small and consistent, 4 to 8px. One radius scale per project.
- Spacing: a 4px base scale. Whitespace is the main grouping tool, boxes are the fallback.
- Type: few sizes, real hierarchy from weight and spacing rather than size explosions. Body around 14 to 15px in dense UI.
- Left-align text by default, headings and labels and footers included. Centered text is a deliberate exception, never a leftover, and never mixed with left-aligned siblings in the same group.
- One icon family, one stroke weight, monochrome on the same ink ladder as text. Emoji are not an icon family and no filter brings them onto the ladder — remove them and let labels carry the meaning. Emoji inside content (a screenshot, a post, someone's display name) are content; leave them alone.
- Borders over shadows; shadows only for true elevation like menus and dialogs, and subtle there.
- Dark mode: respected from the start via `prefers-color-scheme`, same structure, inverted neutrals.
- Motion: minimal and physical. Small distances, quick springs, nothing looping. Motion must carry meaning or improve continuity; omit it when it only decorates a frequent action.
- Prefer container queries to viewport breakpoints where a component can appear in more than one width. A component should respond to the space it is in, not to the window.
- Empty states, focus rings, and hover states are part of the design, not afterthoughts. Visible focus always survives.

## Judge clutter by weights, not elements

Count visual weights in a region, not things. Decide which elements are peers and render peers identically — one size, one rung, one baseline. A control's weight should track how often it is used, so the least-used control in a region must never be its heaviest element.

Long pages are a sequence of distinct, spacious chapters, not a stack of similar cards. A mixed composition of large and small containers each holding real product media is a deliberate layout, not a card grid to flatten.

## Order of operations

When improving an existing interface, prefer earlier moves to later ones. Most "it looks off" problems are the first two, and restyling before fixing them just makes the wrong hierarchy prettier.

1. Page flow, hierarchy, wayfinding, grouping.
2. Layout, when the current composition blocks those.
3. Remove ornament, redundant surfaces, duplicated labels.
4. Normalize spacing, alignment, density.
5. Normalize type, measure, tracking, line height.
6. Consolidate color, borders, radii into tokens.
7. Refine control states: focus, hover, pressed, disabled, loading, empty, error.
8. Motion, only once the static hierarchy works.

## What must survive a cleanup

Restraint applied without looking is just deletion. Before a pass lands, check:

Visual restraint is subordinate to interface integrity. Do not hide frequent actions, erase signs of scrollability, weaken state, shorten labels into ambiguity, or move recovery into an overflow menu merely to make a still image cleaner. If the work reveals a flow-level problem involving prediction, feedback, interruption, authority, or recovery, use `interface-integrity`; do not load it for purely visual token or spacing work.

- **Brand marks stay.** A product's one recognizable color is not a tint to neutralize.
- **Semantic color stays.** Status, focus, warning, error, success, selected, active, destructive. It is usually lost by accident: a rule about label size that also sets `color` will take the state with it, because a flag and an ordinary label are often the same element reading a different token.
- **State survives as more than hue.** If a fill goes neutral and a tab is now distinguished from its neighbors by one hairline, the distinction technically exists and the affordance is gone. Re-encode it.
- **Check what a token is used *for* before changing it.** The value that quiets a fill will shout as a border — an accent taken to black calms every button and turns a soft hairline into a hard box. Where one token serves two jobs, splitting it is the fix, not a compromise value.
- **Some surfaces are correctly loud.** If quieting one would improve its structure and damage its voice, say which was chosen and why instead of reporting the whole thing as an improvement.

## When unsure

Two or three static mocks per the `mock-and-pick` skill beat guessing. The user picks fast.
