---
name: ios-design
description: Best practices for building native iOS apps — read early in any iOS app session. Real-app setup, deployment targets, UIKit vs SwiftUI, platform conventions, and HIG-grounded design.
---

# iOS App Essentials

People expect an iOS app to feel at home on their device immediately. Read this before writing code in a new iOS app session. When a specific component's rules matter, consult the current Human Interface Guidelines (developer.apple.com/design/human-interface-guidelines) rather than trusting recall.

## Be a real app

- Build a proper app target with an Info.plist, a launch screen, and correct supported orientations — decide early whether iPad is in scope, because retrofitting size-class support is expensive.
- Respect the safe areas from the first view. Content that collides with the Dynamic Island, home indicator, or keyboard marks an app as careless faster than any other defect.
- Handle the keyboard: scroll views adjust for it, text fields stay visible above it, and it dismisses the way people expect (interactive drag in scrolling contexts).
- If the project has no app icon yet, say so and ask — never invent placeholder branding.
- Verify on a simulator by actually driving it: launch, rotate if supported, type in every field, background and foreground the app.

## Choose deployment targets before writing code

The minimum iOS version determines the Xcode version, SDK, available APIs, and available design elements. Decide deliberately:

1. Ask which devices and iOS versions matter, and check current adoption if the answer is "most people's."
2. List the APIs the core features need and verify availability against current documentation — never from memory.
3. Decide the device story explicitly: iPhone-only, or iPhone and iPad with real size-class layouts.
4. Record the decision and its reasoning in the project's CLAUDE.md.

## UIKit or SwiftUI

Prefer SwiftUI for new work. Drop to UIKit deliberately:

- Use UIKit for mature high-performance machinery — heavy collection views, complex text editing, fine scroll control — and for APIs SwiftUI hasn't wrapped yet.
- Mix with `UIViewRepresentable` / `UIHostingController` rather than rebuilding mature UIKit components for purity's sake.
- Verify the current gaps against the deployment target's SDK; they shift every release.

## Platform conventions

- Navigation: standard patterns first — a tab bar for top-level sections, a navigation stack within them, sheets for modal tasks. The back-swipe from the left edge must always work; custom navigation that breaks it needs to earn its keep.
- Touch targets: 44 points minimum. Spacing generous enough for thumbs, controls reachable in one-handed use where the app's core loop demands it.
- Dynamic Type: use semantic text styles so people's chosen text size is respected; test at least one accessibility size. Layouts that break at large type are broken layouts.
- Dark Mode from the start via semantic colors, never hardcoded values.
- Iconography: SF Symbols at text-matching weights. No emoji in UI.
- Haptics for meaningful moments — confirmation, boundaries, selection — not decoration.
- Motion: physical, interruptible, and driven by gestures where possible; respect Reduce Motion. See the `apple-design` skill for the physics and `apple-native-motion` for the SwiftUI code; `find-animation-opportunities` decides what earns motion.
- VoiceOver: every interactive element needs a label, a trait, and a sane reading order.
- Contrast passes in both Light and Dark Mode, not just one.
- Tab bar holds 2–5 top-level sections and nothing else — no actions living in tab items.
- Large titles on top-level screens, collapsing on scroll; detail screens stay inline.
- Density: iOS forgives less density than macOS. One primary action per screen region; whitespace does the grouping.

## Interface copy

Write interface text the way the HIG does: say what a thing does in a few plain words, and stop. A toggle labeled "Show grid" needs no sentence beneath it explaining why grids are useful. Labels are short verb or noun phrases; helper text is reserved for genuine consequences people can't see ("Deletes originals after import"), never for restating the label. Match platform capitalization: title case for buttons and bar items, sentence case for descriptive text.

## Bug ownership

When behavior is wrong and a minimal repro shows the framework at fault, tag the workaround per the `os-workarounds` skill — bug id, observed OS version, removal condition — and retest tags on every iOS update.

## Before calling it done

Drive the built app in the simulator: safe areas respected in both orientations you support, keyboard behavior correct, Dynamic Type at a large size, Dark Mode, back-swipe working, no dead ends without a way back. Then the accessibility and performance pass: run VoiceOver through the core flow once (labels present, order sensible, nothing silent); set text to the largest accessibility size and confirm nothing clips; turn on Reduce Motion and confirm big transitions fall back to a crossfade; scroll the longest list and watch for dropped frames; if iPad is in scope, check Split View and landscape. For visual direction decisions, propose options per `mock-and-pick` rather than deciding silently.
