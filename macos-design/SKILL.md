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
- Ship a placeholder icon and label it one. Don't invent a logo, a wordmark, or a mascot — do generate something neutral (an SF Symbol on a flat gradient), check the generator in beside it, and record that real art is still owed. An empty icon slot means the app wears Apple's blank page in the Dock for months. Ship the full ten-size iconset: a single 1024 asset does not resolve at all, and the app falls back to the blank icon with no icon key in its Info.plist. Draw it full-bleed, not pre-rounded — macOS masks and shades the icon itself, so a rounded rect gets rounded twice.
- Verify against the built `.app`, never `swift run` or the test binary. The bundle is the only artifact that exercises signing, entitlements, and the dylib loader, and it is the only one whose window size and menus match what the user gets. `open` returns before a crash-on-launch happens: wait five seconds, then confirm the process is still alive.
- Check it headlessly, since you cannot see the screen. `lsappinfo info -only ApplicationType $(pgrep -x App)` should report `Foreground`; `osascript -e 'tell application "System Events" to tell process "App" to get name of menu bar items of menu bar 1'` should list the real menus. The app menu takes its name from `CFBundleName` — setting only `CFBundleDisplayName` leaves the lowercase build-artifact name in the menu bar.

## Populate the menu bar

An empty template menu bar is an unfinished app. Every action the app offers belongs in the menus, with a keyboard shortcut where one is conventional:

- Provide the standard menus — the app menu, File, Edit, View, Window, Help — and populate them with the app's real commands. In SwiftUI, use the `Commands` API; remove default groups that don't apply rather than shipping dead items.
- Keep the Edit menu even in simple apps: it's what makes system text behaviors (copy, paste, undo, dictation) work in every text field.
- Settings opens with Cmd-Comma from the app menu, in its own window — never as an in-window tab.
- Undo everywhere it can work. Register in-app edits with the window's `UndoManager`, capturing the previous value rather than re-toggling, and coalesce a drag or a slider sweep into a single step. Actions that leave the app — a file moved to the Trash, a request sent — cannot come back with Cmd-Z: give those a restore path instead (a removal manifest plus a "Restore…" menu item), and write the reason at the call site for the ones that get neither. An Edit menu whose Undo item is permanently disabled is the tell.

## Choose deployment targets before writing code

The minimum macOS version determines the Xcode version, SDK, and which APIs and design elements are available at all. Decide it early, deliberately:

1. Ask what Macs the app must run on, and check current adoption if the answer is "most people's."
2. List the APIs the app's core features need, and verify their availability against current documentation — API availability moves too fast to answer from memory.
3. Record the decision and its reasoning in the project's CLAUDE.md so later sessions don't relitigate it.

Decide the sandbox in the same breath. It is not a packaging detail — it decides the architecture.

- A sandboxed app cannot shell out to helper tools. If the app needs `yt-dlp`, `ffmpeg`, or a Python worker, the sandbox is off and you build around that from day one.
- `com.apple.security.app-sandbox` on its own buys restrictions and nothing else. An app that reads or writes user files also needs `files.user-selected.read-write` and `files.bookmarks.app-scope`, or `NSOpenPanel` hands back a path the app is not allowed to touch and the buttons do nothing, with no error.
- Linking any non-Apple dylib with the hardened runtime on requires `com.apple.security.cs.disable-library-validation`, or the app dies before `main()`. Add it when you add the first dylib, not during packaging.
- Read entitlements off the built app (`codesign -d --entitlements - <App>.app`), never off the source file. Under XcodeGen an `entitlements:` block with `path:` and no `properties:` rewrites that file to an empty dict on every generate.

## AppKit or SwiftUI

Prefer SwiftUI for new work; it is the current default and where the platform is headed. Drop to AppKit deliberately, not accidentally:

- Use AppKit when the work needs mature, high-performance table and text machinery (`NSTableView`, `NSTextView`), fine-grained window management, or controls SwiftUI hasn't matched yet on the Mac.
- Mix the two with `NSViewRepresentable` rather than rebuilding a mature AppKit control in SwiftUI for purity's sake.

## Design language

- Type: the system font through semantic text styles, not hardcoded sizes. macOS body text is 13 points; respect the smaller-than-iOS scale. Build hierarchy from weight and spacing before size.
- Color: semantic colors only (`labelColor`, `separatorColor`, the accent) so Dark Mode is correct for free. Keep the base near-monochrome; let content and the accent supply color.
- Iconography: SF Symbols at text-matching weights. No emoji in UI.
- Materials and vibrancy: sparingly and semantically — sidebars and overlays where the system uses them, not as decoration.
- Density: macOS tolerates real density, and this user prefers information-dense interfaces. Cohesion is the constraint: one idea per region, aligned to a consistent grid.
- Windows behave: resizable with sensible minimums and maximums, content that stretches correctly, state restored on relaunch, full keyboard navigation.
- With `NavigationSplitView`, columns lay out at the sum of their ideal widths and will not compress below it. Make the window's minimum wider than that sum, or the sidebar clips off the left edge and the inspector off the right. `.frame(minWidth:)` and `.contentMinSize` only stop the user's drag — a frame restored from an earlier build can still come back narrower, so set `NSWindow.minSize` and grow a restored frame that sits under it.
- Size windows to their content. A window's default size should fit what it presents — sized by its ideal content dimensions, not an arbitrary 800×600. A settings window hugs its controls; a document window opens at a size that shows a useful amount of document. The wrong default size is one of the most common tells of a generated app.
- Drag and drop wherever content moves.
- Motion: small, physical, interruptible, and rarer than on iOS — windows and panels mostly appear. See the `apple-design` skill for the physics and `apple-native-motion` for the SwiftUI code; `find-animation-opportunities` decides what earns motion.
- VoiceOver: every control needs a label and a sane reading order.
- Contrast passes in both Light and Dark Mode, not just one.

## Interface copy

Write interface text the way the HIG does: say what a thing does in a few plain words, and stop. Do not narrate — a toggle labeled "Show grid" needs no sentence beneath it explaining why grids are useful or when someone might want one. People learn an interface by using it, not by reading about it.

- Labels are short verb or noun phrases: "Show grid," "Export…," "Auto-save." If a label needs a paragraph, the design is unclear, not under-explained.
- Reserve helper text for genuine consequences people can't see ("Deletes originals after import"), not for restating the label.
- Match the platform's capitalization: title case for menu items and buttons, sentence case for descriptive text.
- Every ellipsis means "asks for more input before acting" — use it exactly that way, nowhere else.

## Bug ownership

When behavior is wrong and the minimal repro shows the framework at fault, tag the workaround per the `os-workarounds` skill — bug id, observed OS version, removal condition. Fault attribution stays greppable; retest tags on every OS update.

Before debugging a strange layout or launch failure, grep `/Users/Commons/Developer/Wizard/wizard-wiki` — a hundred-odd notes with provenance, and the same bugs keep coming back. One to know cold: `.fixedSize(horizontal: false, vertical: true)` on a Text inside a NavigationSplitView scrolls every scroll view in the window to its bottom on mount. If two unrelated scroll containers move in lockstep, the cause is AppKit, not your view body.

## Before calling it done

Launch the built app and confirm: Dock and Cmd-Tab presence; menus populated and shortcuts firing; Cmd-Comma opens Settings; Cmd-Z undoes; Dark Mode holds up; the default window size fits the content, and the window resizes to its minimum without breaking. Then: navigate the whole app by keyboard alone; run VoiceOver through the core flow once; turn on Reduce Motion and confirm nothing relies on motion to communicate state; scroll the longest list or table and watch for dropped frames; if multi-window or multi-display is supported, confirm state restores. Capture the window for review per `window-capture`. For visual direction decisions, propose options per `mock-and-pick` rather than deciding silently.

Then give the user a build they can keep. A path deep in DerivedData goes stale the moment the session ends. Copy the built .app to a stable, project-local location (such as `<project>/build/<App>.app` — record the convention in the project's CLAUDE.md) and report that path, so the app stays usable between sessions. Replace it on each new build rather than accumulating stale copies.
