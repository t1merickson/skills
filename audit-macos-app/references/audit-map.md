# Where a Mac app rots

Twelve dimensions. Each has what to look for, why it matters, and checks that find it. Not every dimension applies to every app — a single-window utility has no window-restoration story worth auditing. Say which you skipped and why.

Grep patterns assume the source root. Adjust for the project's layout.

## 1. Identity, lifecycle, and entitlements

**Info.plist**
- `LSApplicationCategoryType` — required for App Store, and wrong-or-missing is a rejection.
- `LSMinimumSystemVersion` agrees with the deployment target actually built.
- `CFBundleDisplayName` present when the product name differs from what users should read.
- `LSUIElement` / `LSBackgroundOnly` — deliberate or accidental. An app with `LSUIElement` true has no Dock icon and no menu bar; if the app has windows and menus, this is a bug.
- `NSSupportsAutomaticTermination` / `NSSupportsSuddenTermination` — claiming either while holding unsaved state in memory loses data.
- `ITSAppUsesNonExemptEncryption` set, or export compliance answered per build.

**Entitlements** — read them from the built product, not the source, because the spec and the signature drift:
```bash
codesign -d --entitlements - --xml "<App>.app" | plutil -p -
```
- **`com.apple.security.get-task-allow` in a release build.** Notarization rejects it, and it means the shipped binary is debuggable. A real finding every time.
- **Entitlement creep.** Every entitlement present but unused is attack surface and an App Store review question. Cross-check each against actual API use.
- `com.apple.security.temporary-exception.*` — these draw review scrutiny and usually mean a design problem upstream.
- Sandbox on for App Store; Hardened Runtime on for Developer ID. Both, if shipping both ways.
- File access: `files.user-selected.read-write` with no security-scoped bookmark handling (see dimension 9) means access dies at quit.

**Lifecycle**
- `applicationShouldTerminateAfterLastWindowClosed` — answered deliberately. A document app returning true loses the user's place; a single-window utility returning false leaves a dead Dock icon.
- `applicationShouldHandleReopen(_:hasVisibleWindows:)` — clicking the Dock icon with no windows open should reopen one. Commonly missing, and the app looks frozen.
- Login items and helpers via `SMAppService` (macOS 13+). `SMLoginItemSetEnabled` is deprecated; grep it.
- Termination while work is in flight: an in-progress write, upload, or export cancelled by quit with no warning.

```bash
grep -rn "SMLoginItemSetEnabled\|NSUserNotification\b\|NavigationView\|ObservableObject" --include='*.swift' .
grep -rn "applicationShouldTerminate\|applicationShouldHandleReopen" --include='*.swift' .
```

## 2. Windows and state restoration

The most common macOS disappointment: the app forgets everything on quit.

- **Size and position survive relaunch.** SwiftUI: a `WindowGroup` restores by default only if the scene is restorable and `@SceneStorage` carries the rest. AppKit: `NSWindow.isRestorable` plus a restoration class, or `setFrameAutosaveName`.
- **In-window state survives.** Sidebar width, selected tab, scroll position, selection, inspector open/closed, sort order. `@SceneStorage` for per-window, `@AppStorage`/`UserDefaults` for app-wide — and never `@AppStorage` outside a `View`.
- **Sizing is sane.** `defaultSize`, `windowResizability`, and a minimum that doesn't clip content. Test at the smallest size the window allows.
- **⌘N** does something correct: a new window for a `WindowGroup`, nothing for a single `Window`, a new document for a document app.
- **Full screen, Split View, and window tiling** (macOS 15+) don't break the layout. A fixed-width sidebar plus a tiled half-screen window is where this shows up.
- **Display changes**: unplugging an external display shouldn't leave the window off screen. Reconnecting shouldn't lose it.
- **Panels and sheets**: an inspector is a panel or an `.inspector`, not a floating always-on-top window. A sheet is window-attached, not a centered card.
- Multiple windows on the same document don't fight over state.

```bash
grep -rn "SceneStorage\|setFrameAutosaveName\|isRestorable\|windowResizability\|defaultSize" --include='*.swift' .
grep -rn "AppStorage" --include='*.swift' . | grep -v "struct.*View\|: View"
```

## 3. Menu bar and commands

The dimension most often half-built, and the one users read as "is this a real Mac app."

A complete menu bar has, at minimum:

| Menu | Required items |
| --- | --- |
| App | About <App>, Settings… (⌘,), Services, Hide, Hide Others, Show All, Quit (⌘Q) |
| File | New (⌘N) / Open (⌘O) / Close (⌘W) / Save (⌘S) as the app's model warrants; Print (⌘P) if printable |
| Edit | Undo (⌘Z), Redo (⇧⌘Z), Cut (⌘X), Copy (⌘C), Paste (⌘V), Delete, Select All (⌘A) |
| View | Toolbar and sidebar visibility, Enter Full Screen |
| Window | Minimize (⌘M), Zoom, Bring All to Front, the window list |
| Help | <App> Help, or a link that resolves |

Findings to look for:
- **A missing Edit menu, or one with no Undo.** Even an app with no document model usually has text fields, and those need the Edit menu to work. Undo/Redo present but not wired to anything is worse than absent.
- **Settings missing or not on ⌘,.** In SwiftUI this is the `Settings` scene; anything else is wrong.
- **Menu items that are always enabled.** Validation matters: Copy with no selection, Save with no changes, Undo with an empty stack should all be disabled. Always-enabled items that no-op read as broken.
- **Orphan items** that do nothing, or duplicate a toolbar button that is itself the only way to reach the feature.
- **Every feature reachable from the menu bar.** A capability available only from a toolbar button or a right-click is unreachable by keyboard and invisible to Help search.
- **Key equivalents follow convention.** Don't rebind ⌘W, ⌘Q, ⌘,. Don't invent a shortcut that collides with a system one.
- **Title Case** for menu items, per the HIG. Route capitalization to `apple-ui-copy`.

Dimension 3 is mostly a dynamic check — see [inspecting-a-running-app.md](inspecting-a-running-app.md) for the mechanical sweep.

```bash
grep -rn "CommandGroup\|CommandMenu\|keyboardShortcut\|Settings {" --include='*.swift' .
grep -rn "NSMenu\|NSMenuItem\|validateMenuItem" --include='*.swift' .
```

## 4. Keyboard and focus

- **Tab reaches every control.** macOS gates this behind System Settings → Keyboard → Keyboard navigation; turn it on and try. Custom views are where the chain breaks.
- **Escape cancels, Return commits** in every sheet, dialog, and alert. SwiftUI: `.keyboardShortcut(.cancelAction)` and `.defaultAction`.
- **A default button exists** in every dialog, and it's the safe one.
- **Arrow keys** move selection in lists, tables, and outlines. Free from `List` and `Table`; absent from a hand-rolled `VStack` of rows.
- **Focus is visible.** A focus ring that's been styled away leaves keyboard users blind.
- **No focus trap.** A custom view that swallows Tab without forwarding it strands the user.
- `@FocusState` / `focusedValue` used for real focus management rather than as a hack to dismiss a keyboard.
- Text fields: `onSubmit`, `submitLabel`, and a sensible tab order between them.

```bash
grep -rn "keyboardShortcut\|FocusState\|focusedValue\|onSubmit\|onKeyPress" --include='*.swift' .
grep -rn "focusable(false)\|\.focusEffectDisabled" --include='*.swift' .
```

## 5. Accessibility

**This skill owns this dimension — no specialist skill covers macOS accessibility.** Say that in the report.

- **Every control has a label.** An icon-only button with no `accessibilityLabel` reads as "button". Use `Label`, or pass title and image and hide the text with `.labelStyle(.iconOnly)` — which keeps the label available — rather than dropping the text.
- **Custom views are accessibility elements.** A `Canvas`, a custom chart, or a drawn control with no `accessibilityElement`, role, value, and actions is invisible to VoiceOver. An interactive canvas needs `accessibilityAction`s as an alternative to its gestures.
- **Values and state are exposed.** A custom toggle needs its on/off state, a slider its value, a progress view its progress — not just a label.
- **Grouping.** A row of related labels should be one element with a combined label, not five separate stops.
- **Reduce Motion, Reduce Transparency, Increase Contrast, Differentiate Without Color** are all real system settings on macOS, and all four are commonly ignored. Check each is honored.
- **Color is never the only signal.** Status shown by color alone fails Differentiate Without Color.
- **Text sizing.** macOS has no system-wide Dynamic Type, so the concern is different from iOS: use `NSFont.preferredFont(forTextStyle:)` or SwiftUI's semantic text styles rather than hardcoded point sizes, and let the layout reflow. Hardcoded `.font(.system(size: 13))` throughout is a finding.
- **Contrast.** Check custom foreground-on-background pairs in both appearances.

```bash
grep -rn "accessibilityLabel\|accessibilityElement\|accessibilityValue\|accessibilityAction\|accessibilityHidden" --include='*.swift' .
grep -rn "reduceMotion\|reduceTransparency\|differentiateWithoutColor\|increaseContrast\|accessibilityReduceMotion" --include='*.swift' .
grep -rn "font(.system(size:" --include='*.swift' . | head -20
grep -rn "Image(systemName:" --include='*.swift' . | wc -l   # compare against accessibilityLabel count
```

Verify with Accessibility Inspector (Xcode → Open Developer Tool), which audits a running app and lists unlabeled elements directly.

## 6. Appearance and materials

- **Semantic colors, not literals.** `NSColor.labelColor`, `.secondaryLabelColor`, `.controlBackgroundColor`, or SwiftUI's `.primary`/`.secondary` — hardcoded hex breaks dark mode and Increase Contrast at once.
- **Custom colors live in the asset catalog with both appearance variants.** A single-appearance custom color is a dark-mode bug waiting.
- **The user's accent color is respected.** `NSColor.controlAccentColor` / SwiftUI `.tint`. An app that hardcodes blue ignores a setting the user deliberately changed.
- **Materials match the surface.** `NSVisualEffectView` blending mode `.behindWindow` for window-background vibrancy, `.withinWindow` for a panel over content — swapped, it looks wrong and nobody can say why. In SwiftUI, one `Material`, not a material plus a tint fill on top.
- **Both appearances actually checked.** Switch and look, don't assume.
- Selection and highlight use system colors so they follow the accent.

```bash
grep -rnE "Color\(red:|#[0-9A-Fa-f]{6}|NSColor\(calibrated|\.init\(srgbRed" --include='*.swift' .
grep -rn "controlAccentColor\|\.tint\|NSVisualEffectView\|blendingMode" --include='*.swift' .
```

## 7. Code health

- **Deprecated API.** `NavigationView`, `ObservableObject` where `@Observable` fits, `NSUserNotification`, `SMLoginItemSetEnabled`, `NSUnarchiver`, `String(contentsOfFile:)` without encoding.
- **Work in `body`.** Date formatting, sorting, filtering, or file reads inside a view's `body` re-run on every invalidation. A `DateFormatter` constructed in `body` is the classic one.
- **Over-invalidation.** One large `@Observable` model that every view reads redraws the whole tree on any change. Look for a single god-object store.
- **Retain cycles.** Closures capturing `self` strongly in AppKit delegates, `NotificationCenter` observers never removed, Combine sinks without `[weak self]`.
- **`onAppear` fetches** that re-fire on every appearance, including when a window is reordered.
- **`Task` without cancellation.** A `.task` tied to view lifetime is fine; a detached `Task` that outlives its view and writes to it is a bug.
- **Force unwraps and `try!`** on anything derived from user input, the filesystem, or the network. `fatalError` in a shipping path.
- **`NSViewRepresentable`/`NSViewControllerRepresentable` lifecycle.** `updateNSView` rebuilding the view or re-registering observers on every update; a coordinator that leaks.
- **Naming collisions with framework types.** A local `Button`, `ProgressView`, or `Label` is a trap for everyone who reads the file later.
- Route API-choice findings to `swiftui-defaults`.

```bash
grep -rnE "DateFormatter\(\)|NumberFormatter\(\)" --include='*.swift' .
grep -rn "try!\|fatalError(\|\!\s*$" --include='*.swift' . | head -30
grep -rn "NotificationCenter.default.addObserver" --include='*.swift' .
grep -rn "\.sink\|\.assign" --include='*.swift' . | grep -v "weak self"
```

## 8. Concurrency and main-thread discipline

- **File I/O, network, and heavy compute on the main thread.** On macOS this shows up as a beachball, and users blame the whole app. Anything synchronous in a `body`, an `@IBAction`, or a `@MainActor` function without an `await` boundary.
- **`DispatchQueue.main.async` used to paper over a data race** rather than to hop to the main actor deliberately.
- **`@MainActor` discipline.** UI types annotated; model types not annotated purely to silence a warning.
- **Swift 6 readiness.** Check the language mode. In Swift 5 with strict concurrency off, data races are invisible; `swiftSettings` with `SwiftConcurrency` or `-strict-concurrency=complete` reveals them. A project still in Swift 5 mode with heavy concurrency is a migration finding, not a bug list.
- `@unchecked Sendable` — every instance is a claim someone has to justify. Ask what protects it.
- Actor reentrancy: state assumptions across an `await` inside an actor.

```bash
grep -rn "DispatchQueue.main\|@unchecked Sendable\|nonisolated(unsafe)" --include='*.swift' .
grep -rn "Data(contentsOf:\|String(contentsOf:\|FileManager.default.contentsOf" --include='*.swift' .
grep -rn "swiftLanguageMode\|SWIFT_VERSION\|strict-concurrency" --include='*.swift' --include='*.yml' --include='*.json' --include='*.pbxproj' .
```

## 9. Data safety and persistence

- **Where user data lives.** `~/Library/Application Support/<bundle-id>/` for app data, `~/Library/Caches/` for regenerable, `~/Documents` only for documents the user created and can see. `UserDefaults` holding megabytes of app data is a finding.
- **Writes are atomic.** `Data.write(to:options: .atomic)`, or a write-temp-then-rename. A non-atomic write interrupted by a crash or a quit leaves a truncated file, and the app opens empty next launch.
- **A migration path exists** for any persisted format. What happens when this version reads last version's file, and what happens when last version reads this one's.
- **Security-scoped bookmarks** for sandboxed apps that remember a user-chosen folder. Without `bookmarkData(options: .withSecurityScope)` and `startAccessingSecurityScopedResource()`, access is lost at quit and the app silently can't read the folder it had permission for yesterday. Then check the matching `stopAccessing` — leaking scopes exhausts a real limit.
- **Keychain** for credentials, never `UserDefaults` or a plist. Check the access group and `kSecAttrAccessible` level.
- **Unsaved state at quit.** Either autosave, or ask. Silently discarding is the worst option and the most common.
- iCloud or CloudKit present → route to `cloudkit`.

```bash
grep -rn "applicationSupportDirectory\|documentDirectory\|cachesDirectory\|NSHomeDirectory" --include='*.swift' .
grep -rn "withSecurityScope\|startAccessingSecurityScopedResource\|stopAccessingSecurityScopedResource" --include='*.swift' .
grep -rn "write(to:" --include='*.swift' . | grep -v atomic
grep -rniE "UserDefaults.*(password|token|secret|key)" --include='*.swift' .
```

## 10. Performance and energy

Energy is a Mac-specific concern users feel directly, as fan noise and battery drain.

- **Launch time.** Time it. Work in `applicationDidFinishLaunching` or a root view's `init` that could be deferred.
- **Main-thread hangs.** Instruments' Hangs / Time Profiler:
  ```bash
  xcrun xctrace record --template 'Time Profiler' --attach "<App>" --output trace.trace
  ```
- **Timers.** A repeating `Timer` at 60 Hz, or any polling loop, prevents App Nap and costs battery. Ask what it's polling and whether a notification would do.
- **Unnecessary wake-ups.** `beginActivity` held longer than the work, background `URLSession` misuse.
- **Memory growth** over a long session — leaks, and caches with no eviction. All four
  tools ship with macOS, no Xcode project needed:
  ```bash
  footprint "<App>"                      # current and peak memory, one line
  leaks "<App>" --outputGraph=before.memgraph
  # exercise the suspect flow twenty times, then:
  leaks "<App>" --diffFrom=before.memgraph    # only what leaked since
  vmmap -summary "<App>"                 # where the memory actually went
  heap "<App>" | head -40                # object counts by class, largest first
  ```
  `--diffFrom` is the finding: a leak count that grows with repetitions is evidence,
  a single non-zero count often isn't. Repeat the flow, diff, and report the delta
  per repetition rather than the absolute number.
- **List and table performance** at realistic data volume. `List` with 10,000 rows and no lazy loading, or a `ForEach` over a computed-every-time array.
- **Image handling.** Full-resolution images decoded for thumbnails; no downsampling.

```bash
grep -rn "Timer.scheduledTimer\|Timer.publish\|DispatchSourceTimer" --include='*.swift' .
grep -rn "beginActivity\|ProcessInfo.processInfo.beginActivity" --include='*.swift' .
```

## 11. Text, localization, and copy

- **Hardcoded user-facing strings** that should be localized. Even an English-only app benefits — it's the difference between localizable later and a rewrite later.
- `Formatter` / `FormatStyle` for dates, numbers, and measurements, not string interpolation. A hand-built `"\(count) items"` breaks pluralization in every language including English at 1.
- **Real ellipsis `…`, real quotes, real dashes.** Three periods in a menu item is a HIG violation you can grep for.
- **Title Case for menu items, buttons, and labels** on macOS; route to `apple-ui-copy` for the rules, and to `clean-copy` for text that shouldn't exist at all.
- **Error messages say what to do next.** "An error occurred" is a finding.
- Right-to-left: leading/trailing rather than left/right, and let native controls mirror.

```bash
grep -rn '\.\.\.' --include='*.swift' . | grep -iE 'Text\(|Button\(|title|label'
grep -rn 'String(localized\|NSLocalizedString\|LocalizedStringKey\|String(format:' --include='*.swift' .
```

## 12. Tooling, tests, and distribution readiness

- **A reproducible build from the CLI.** `make build`, `make test`, `make run`. No Makefile → `xcode-makefiles`.
- **Tests exist and pass.** What they cover, and whether the critical paths from dimension 9 are among them. No test suite is finding #1 in disguise: it blocks every risky fix behind "we can't tell if this broke anything."
- **A clean build from scratch** works — not just an incremental one with a warm derived-data.
- **Warnings.** Count them. A build with 200 warnings has no working warning signal.
- **Version and build numbers** increment, and agree between the spec and the built product.
- **Crash reporting** wired, or a deliberate decision not to. Route existing reports to `crash-debugging`.
- **Updates**: Sparkle or equivalent for Developer ID, or App Store. An app with no update path is a finding on its own.
- Signing and notarization → `ship-macos`. Don't re-derive that pipeline here.

```bash
ls Makefile 2>/dev/null || echo "no Makefile"
grep -rn "MARKETING_VERSION\|CURRENT_PROJECT_VERSION\|CFBundleShortVersionString" --include='*.yml' --include='*.json' --include='*.pbxproj' .
find . -name '*Tests*' -maxdepth 3 -type d
```
