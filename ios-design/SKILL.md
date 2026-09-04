---
name: ios-design
description: "Use when building or reviewing actual native iOS app behavior: app structure, deployment targets, UIKit/SwiftUI choices, platform conventions, accessibility, or HIG-grounded interface decisions. Do not use for general Swift questions, macOS/server/CLI work, cross-platform code without an iOS-specific decision, or a passing mention of iPhone or iPad."
---

# iOS App Essentials

People expect an iOS app to feel at home on their device immediately. Read this before writing code in a new iOS app session. When a specific component's rules matter, consult the current Human Interface Guidelines (developer.apple.com/design/human-interface-guidelines) rather than trusting recall.

## Be a real app

- Build a proper app target with an Info.plist, a launch screen, and correct supported orientations — decide early whether iPad is in scope, because retrofitting size-class support is expensive.
- Respect the safe areas from the first view. Content that collides with the Dynamic Island, home indicator, or keyboard marks an app as careless faster than any other defect.
- Handle the keyboard: scroll views adjust for it, text fields stay visible above it, and it dismisses the way people expect (interactive drag in scrolling contexts). When you test this on the simulator, turn off Connect Hardware Keyboard first — with it on, the software keyboard never appears and a keyboard check is vacuously true. Assert on field focus, which is honest either way, and treat keyboard visibility as the secondary check.
- If the project has no app icon yet, say so and ask — never invent placeholder branding.
- Never pass `CODE_SIGNING_ALLOWED=NO` to a simulator build or test run. Simulator builds sign to run locally by default and need no team id; turning signing off produces a binary whose entitlements cannot be validated, so every Keychain call fails with `errSecMissingEntitlement` (-34018) and saved sessions silently vanish. It presents as a flaky login, not as a signing error.
- Every protected resource the app requests needs the matching `Info.plist` purpose string before first access. A missing required string can terminate the app. Verify the exact key in current Apple documentation, then test the permission path on a fresh install; capabilities and entitlements that do not use a purpose string should not get invented ones.
- Verify on a simulator by actually driving it: launch, rotate if supported, type in every field, background and foreground the app. Then say out loud what the simulator did not prove. It cannot fire a haptic, mint a push token, mint a Sign in with Apple identity token, or tell you anything about audio latency, speaker character, or the silent switch. A green simulator run on a haptic- or audio-heavy app says the structure works and nothing about whether the app is good to hold. Ask for a device pass, and keep one list of every path that is waiting on a device or a credential rather than letting them scatter.
- Prefer an isolated simulator when tests reset data, change accounts, alter permissions, or need a controlled OS/device profile. Reuse a project-owned test device when one exists; create and delete a temporary device only when isolation is actually needed. Do not mutate a user's reference simulator without permission.

## Choose deployment targets before writing code

The minimum iOS version determines the Xcode version, SDK, available APIs, and available design elements. Decide deliberately:

1. Ask which devices and iOS versions matter, and check current adoption if the answer is "most people's."
2. List the APIs the core features need and verify availability against current documentation — never from memory.
3. Decide the device story explicitly: iPhone-only, or iPhone and iPad with real size-class layouts.
4. Record the decision and its reasoning in the project's AGENTS.md or other standing project documentation.

The decision is not permanent. A design decision can demand a newer API, and raising the floor is the right answer more often than reimplementing what the OS now gives you — record the raise and its reason alongside the original. If the project is split into packages, only raise the floors that actually need it.

## UIKit or SwiftUI

Prefer SwiftUI for new work. Drop to UIKit deliberately:

- Use UIKit for mature high-performance machinery — heavy collection views, complex text editing, fine scroll control — and for APIs SwiftUI hasn't wrapped yet.
- Mix with `UIViewRepresentable` / `UIHostingController` rather than rebuilding mature UIKit components for purity's sake.
- Verify the current gaps against the deployment target's SDK; they shift every release.

## Platform conventions

- Navigation: chrome is native, content is yours. Tab bar, navigation stack, toolbar, sheets, `Form`, `List`, system button styles, `.redacted` for loading — take all of it stock. Personality goes into the content: type, color, cards, illustration. Custom chrome forfeits every system behavior you would otherwise get free (Dynamic Type, VoiceOver, scroll behaviors, new system styling on the next OS) and buys a maintenance surface you will iterate away. The back-swipe from the left edge must always work.
- Touch targets: 44 points minimum. Spacing generous enough for thumbs, controls reachable in one-handed use where the app's core loop demands it.
- Dynamic Type: use semantic text styles so people's chosen text size is respected; test at least one accessibility size. Layouts that break at large type are broken layouts.
- Dark Mode from the start via semantic colors, never hardcoded values. Split the palette explicitly: brand colors are fixed, every surface and text color is adaptive. Two failures show up late and cost a full sweep to undo — forcing `.colorScheme(.dark)` on a screen while system chrome still follows the OS, and using a surface token as text ink (invisible in one appearance, fine in the other). Every `#Preview` renders in both appearances, and the UI tests run in both.
- Iconography: SF Symbols at text-matching weights. No emoji in UI.
- Haptics for meaningful moments — confirmation, boundaries, selection — not decoration.
- Motion: physical, interruptible, and driven by gestures where possible. Reduce Motion means a designed gentler equivalent — a crossfade, a static summary — never a removal or a broken state. See `apple-native-motion` for the SwiftUI and UIKit implementation guidance.
- VoiceOver: every interactive element needs a label, a trait, and a sane reading order.
- Contrast passes in both Light and Dark Mode, not just one.
- Tab bar holds 2–5 top-level sections and nothing else — no actions living in tab items.
- Large titles on top-level screens, collapsing on scroll; detail screens stay inline.
- Density: iOS forgives less density than macOS. One primary action per screen region; whitespace does the grouping.

## Interface copy

Write interface text the way the HIG does: say what a thing does in a few plain words, and stop. A toggle labeled "Show grid" needs no sentence beneath it explaining why grids are useful. Labels are short verb or noun phrases; helper text is reserved for genuine consequences people can't see ("Deletes originals after import"), never for restating the label. Match platform capitalization: title case for buttons and bar items, sentence case for descriptive text. Every ellipsis means "asks for more input before acting" — use it exactly that way, nowhere else.

## Bug ownership

When a minimal repro shows the framework at fault, tag the compatibility code through `os-workarounds` with evidence, owner, and removal test. Retest when a relevant iOS, SDK, or deployment-target change could invalidate it.

## Before calling it done

Drive the built app in the simulator: safe areas respected in both orientations you support, keyboard behavior correct, Dynamic Type at a large size, Dark Mode, back-swipe working, no dead ends without a way back. Then the accessibility and performance pass: run VoiceOver through the core flow once (labels present, order sensible, nothing silent); set text to the largest accessibility size and confirm nothing clips; turn on Reduce Motion and confirm big transitions fall back to a crossfade; scroll the longest list and watch for dropped frames; if iPad is in scope, check Split View and landscape. For visual direction decisions, propose options per `mock-and-pick` rather than deciding silently.

For substantial or repeatedly reviewed apps, leave a documented command that builds, installs, and launches on the project-owned simulator, plus a deterministic screenshot command. For a small existing project, use its established build and test entry points instead of adding harness infrastructure solely to satisfy this skill. Report device-only gaps either way.
