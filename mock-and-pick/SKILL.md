---
name: mock-and-pick
description: The a/b/c static-mock workflow for UI or copy changes with no stated direction. Use before editing real components on taste.
---

# mock-and-pick

When the user hands you a direction (a mock, tokens, reference shots, a described look), build exactly that. This skill is for the other case: a non-trivial UI, layout, or copy change with NO direction yet. Don't edit real components on your own taste. Mock first, let them pick.

## When it applies

- Non-trivial visual or copy changes without a stated direction.
- It does NOT apply to trivial changes (a spacing fix, a typo, an obvious bug). Just do those.
- It does NOT apply when direction exists. Design intent is law; mocks would second-guess them.

## Making the mocks

- **2 to 4 mocks, distinct directions, not variations.** Each mock is a different bet, not the same bet in three fonts. If you can't articulate what each one bets on, you have variations, and you should collapse them.
- **Static only.** A self-contained HTML file, a SwiftUI preview, or a rendered image. Never edits to real components. Mocks live in a `mocks/` directory in the project until the winner ships.
- **Label A, B, C** and give each one line of rationale: "A bets on density. B bets on calm. C bets on the sidebar doing the work."
- Copy changes: mock as before/after text blocks, same labels.
- Motion: static mocks lie about how motion feels. Describe the choreography in a line each, and when the decision IS the motion, build tiny isolated runnable prototypes instead of stills. For native prototypes, use `apple-native-motion`.
- Match each mock's fidelity to the decision. Picking a layout needs boxes; picking a type treatment needs real type.

## Showing them

- Web: render the HTML inline or send the file so the user sees it immediately.
- Native: build the preview and capture it with the `window-capture` skill.
- Show all options in one message, side by side where possible. Then STOP. No implementing, no "meanwhile I went ahead".

## After the pick

- Picks compose. "C plus A's header" is a normal answer; build the composite.
- Implement exactly what was picked. The losing mocks go in the discard pile with the reason each lost, because the user sometimes rescues one later.
- If they pick nothing and redirects, that redirect is the new direction. Follow it, don't defend the mocks.
