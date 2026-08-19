---
name: mock-and-pick
description: The a/b/c static-mock workflow for UI or copy changes with no stated direction. Use before editing real components on taste.
---

# mock-and-pick

when the user hands you a direction (a mock, tokens, reference shots, a described look), build exactly that. this skill is for the other case: a non-trivial UI, layout, or copy change with NO direction yet. don't edit real components on your own taste. mock first, let them pick.

## when it applies

- non-trivial visual or copy changes without a stated direction.
- it does NOT apply to trivial changes (a spacing fix, a typo, an obvious bug). just do those.
- it does NOT apply when direction exists. design intent is law; mocks would second-guess them.

## making the mocks

- **2 to 4 mocks, distinct directions, not variations.** each mock is a different bet, not the same bet in three fonts. if you can't articulate what each one bets on, you have variations, and you should collapse them.
- **static only.** a self-contained HTML file, a SwiftUI preview, or a rendered image. never edits to real components. mocks live in a `mocks/` directory in the project until the winner ships.
- **label a, b, c** and give each one line of rationale: "a bets on density. b bets on calm. c bets on the sidebar doing the work."
- copy changes: mock as before/after text blocks, same labels.
- motion: static mocks lie about how motion feels. describe the choreography in a line each, and when the decision IS the motion, build tiny isolated runnable prototypes instead of stills. read the `apple-design` skill for the physics (`apple-native-motion` for the SwiftUI translation).
- match each mock's fidelity to the decision. picking a layout needs boxes; picking a type treatment needs real type.

## showing them

- web: render the HTML inline or send the file so the user sees it immediately.
- native: build the preview and capture it with the `window-capture` skill.
- show all options in one message, side by side where possible. then STOP. no implementing, no "meanwhile i went ahead".

## after the pick

- picks compose. "c plus a's header" is a normal answer; build the composite.
- implement exactly what was picked. the losing mocks go in the discard pile with the reason each lost, because the user sometimes rescues one later.
- if they pick nothing and redirects, that redirect is the new direction. follow it, don't defend the mocks.
