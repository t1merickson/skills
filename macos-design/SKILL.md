---
name: macos-design
description: Best practices for building native macOS apps — read early in any macOS app session. Real-app behavior, the menu bar, deployment targets, AppKit vs SwiftUI, and HIG-grounded design.
---

# macOS App Essentials

People expect a Mac app to behave like a Mac app from its first launch. Read this before writing code in a new macOS app session; most of the failures it prevents are cheap to avoid and expensive to retrofit. When a specific control or component's rules matter, consult the current Human Interface Guidelines (developer.apple.com/design/human-interface-guidelines) rather than trusting recall.

## Be a real app

The most common failure is producing a detached, ownerless floating window — a process with no Dock presence, no menu bar, and no identity. Avoid it from the start:

- Build a proper app bundle with an Info.plist, not a bare executable. A binary launched with `swift run` is not an app; people (and the system) can't treat it like one.
- The app must appear in the Dock and the app switcher. Confirm the activation policy is `.regular` — an `LSUIElement` entry or an `.accessory` policy silently removes the app from the Dock, and is only correct for true background utilities.
- Use the real application lifecycle: a SwiftUI `App` with a `WindowGroup` or `Window` scene, or `NSApplicationMain` with an app delegate. This is what gives the app an owned menu bar, correct activation, and windows that minimize to the Dock.
- If the project has no app icon yet, say so and ask — never invent placeholder branding. A missing icon is a flag to raise, not a gap to fill creatively.
- Verify by launching: Dock icon present, Cmd-Tab entry present, menu bar shows the app's name, the window minimizes and restores.

## Populate the menu bar

An empty template menu bar is an unfinished app. Every action the app offers belongs in the menus, with a keyboard shortcut where one is conventional:

- Provide the standard menus — the app menu, File, Edit, View, Window, Help — and populate them with the app's real commands. In SwiftUI, use the `Commands` API; remove default groups that don't apply rather than shipping dead items.
- Keep the Edit menu even in simple apps: it's what makes system text behaviors (copy, paste, undo, dictation) work in every text field.
- Settings opens with Cmd-Comma from the app menu, in its own window — never as an in-window tab.
- Undo everywhere. Every destructive or mutating action should be undoable with Cmd-Z. This is the strongest single native signal and the most commonly skipped.

## Choose deployment targets before writing code

The minimum macOS version determines the Xcode version, SDK, and which APIs and design elements are available at all. Decide it early, deliberately:

1. Ask what Macs the app must run on, and check current adoption if the answer is "most people's."
2. List the APIs the app's core features need, and verify their availability against current documentation — API availability moves too fast to answer from memory.
3. Record the decision and its reasoning in the project's CLAUDE.md so later sessions don't relitigate it.

## AppKit or SwiftUI

Prefer SwiftUI for new work; it is the current default and where the platform is headed. Drop to AppKit deliberately, not accidentally:

- Use AppKit when the work needs mature, high-performance table and text machinery (`NSTableView`, `NSTextView`), fine-grained window management, or controls SwiftUI hasn't matched yet on the Mac.
- Mix the two with `NSViewRepresentable` rather than rebuilding a mature AppKit control in SwiftUI for purity's sake.
- The gaps between the frameworks shift with every release; when a capability is in question, verify against the deployment target's SDK rather than assuming.

## Design language

- Type: the system font through semantic text styles, not hardcoded sizes. macOS body text is 13 points; respect the smaller-than-iOS scale. Build hierarchy from weight and spacing before size.
- Color: semantic colors only (`labelColor`, `separatorColor`, the accent) so Dark Mode is correct for free. Keep the base near-monochrome; let content and the accent supply color.
- Iconography: SF Symbols at text-matching weights. No emoji in UI.
- Materials and vibrancy: sparingly and semantically — sidebars and overlays where the system uses them, not as decoration.
- Density: macOS tolerates real density, and this user prefers information-dense interfaces. Cohesion is the constraint: one idea per region, aligned to a consistent grid.
- Windows behave: resizable with sensible minimums, content that stretches correctly, state restored on relaunch, full keyboard navigation.
- Drag and drop wherever content moves.
- Motion: small, physical, interruptible, and rarer than on iOS — windows and panels mostly appear. See the `apple-design` skill for the physics; `find-animation-opportunities` decides what earns motion.

## Bug ownership

When behavior is wrong and the minimal repro shows the framework at fault, tag the workaround per the `os-workarounds` skill — bug id, observed OS version, removal condition. Fault attribution stays greppable; retest tags on every OS update.

## Before calling it done

Launch the built app and confirm: Dock and Cmd-Tab presence; menus populated and shortcuts firing; Cmd-Comma opens Settings; Cmd-Z undoes; Dark Mode holds up; the window resizes to its minimum without breaking. Capture the window for review per `window-capture`. For visual direction decisions, propose options per `mock-and-pick` rather than deciding silently.
