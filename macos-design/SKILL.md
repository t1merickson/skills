---
name: macos-design
description: Design direction and HIG grounding for native macOS app UI.
---

# macos-design

the user builds Mac apps that should feel like Mac apps. the direction: quiet, dense but cohesive, standard controls doing standard things, with a few precise custom moments where the app's identity lives. when a specific control's rules matter, check the current Human Interface Guidelines (developer.apple.com/design/human-interface-guidelines) instead of trusting recall — the HIG moves.

## what makes an app feel properly Mac

- **a real menu bar.** every action in the app exists in the menus with a keyboard shortcut. the menu bar is the app's index; power users live there.
- **undo everywhere.** every destructive or mutating action is undoable via cmd-Z. this is the single strongest native signal and the most commonly skipped.
- **standard controls first.** the stock toolbar, sidebar, popover, sheet, and inspector behave in ways users' hands already know. a custom control has to beat the standard one, not just differ from it.
- **windows behave.** resizable with sensible minimums, content that stretches the right way, state restored on relaunch, full keyboard navigation. settings live in a Settings window (cmd-comma), not an in-window tab.
- **drag and drop** where content moves, and dropped things go where they landed.

## visual defaults

- type: the system font through semantic text styles, not hardcoded sizes. macOS body is 13pt; respect the smaller-than-iOS scale. hierarchy from weight and spacing before size.
- color: semantic colors only (`labelColor`, `separatorColor`, accent) so dark mode is free and correct. near-monochrome base; the accent color and content supply the color.
- SF Symbols at text-matching weights for iconography. no emoji in UI, ever.
- materials and vibrancy: sparingly and semantically — sidebars and overlays where the system uses them, not as decoration.
- density: macOS tolerates real density, and the user likes information-dense. cohesion is the constraint — one idea per region, aligned to a consistent grid, not many ideas crammed together.
- spacing: standard control spacing comes from the system; custom layouts use one spacing scale, 4 or 8pt base.

## motion

small, physical, interruptible. read the `apple-design` skill for the actual physics; `find-animation-opportunities` decides what earns motion. on the Mac, less than iOS: windows and panels mostly appear; springs belong to content, not chrome.

## when judging existing UI

capture the single window with the `window-capture` skill and look for the usual native-feel failures, in order of damage: missing menu items and shortcuts, non-standard control behavior, hardcoded colors breaking dark mode, off-grid spacing, density without cohesion, animation where the system would have none. report per `explaining-problems`; propose direction changes as mocks per `mock-and-pick`, not silent edits.
