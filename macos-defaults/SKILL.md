---
name: macos-defaults
description: "Use when building or reviewing actual native macOS app behavior: identity and lifecycle, commands and menus, SwiftUI/AppKit choices, HIG-grounded interface decisions, accessibility, runtime boundaries, or stable app delivery. Do not use for general Swift questions, shell tools that merely run on macOS, cross-platform code without a Mac-specific decision, or passing mentions of .app files."
---

# macOS app essentials

Read this early in a macOS app session. People expect a Mac app to behave like a Mac app from first launch; the failures here are cheap to avoid and expensive to retrofit. Use the current Human Interface Guidelines (the local `apple-hig` mirror when installed) and platform documentation for component- or release-specific facts; do not treat this file as a frozen SDK reference. Deeper topics have their own skills; see [Where to go deeper](#where-to-go-deeper).

## Establish the app type

Decide whether the product is a regular foreground app, menu-bar utility, background agent, document app, or mixed design. The recurring generated-app failure is a detached, ownerless window: a process with no real Dock presence, menu architecture, restoration, or identity. Make identity and activation policy agree:

- Regular apps use a real `.app` bundle, normal lifecycle, menu bar, Dock/App Switcher presence, and owned windows. The app menu takes its title from `CFBundleName`; setting only `CFBundleDisplayName` leaves the raw build-artifact name sitting in the menu bar.
- Menu-bar utilities and agents may intentionally use `LSUIElement` or accessory activation. Their discoverability, settings, quit path, and relaunch behavior need explicit design because the Dock will not provide them.
- Verify the built bundle, not `swift run`: bundle metadata, signing, entitlements, loader behavior, menus, restoration, and launch crashes only exist in the shipped shape.
- Use a real icon before release. During development, either retain the project's existing mark or label a neutral placeholder clearly; do not invent permanent branding. Use the current asset-catalog or Icon Composer pipeline, provide full-bleed source artwork where required, and inspect the built icon at Dock, Finder, and small-list sizes rather than judging only the 1024-pixel source. Supply every size the pipeline asks for: an incomplete set can fail to resolve entirely, leaving the built app with no icon key in its `Info.plist` and the system's blank page in the Dock — a different failure from an icon that merely reads poorly when small.

## Menus are command architecture

Expose the app's complete command set through conventional menus and shortcuts. A toolbar is a convenient subset, not the only home for a command: people can hide or customize it, and keyboard-first users work through menus. Keep system text editing, undo/redo, Settings at Command-Comma, Window management, and Help behavior intact. Remove irrelevant template commands rather than shipping dead items.

Put frequent, context-relevant actions in the toolbar, group them by purpose, and let overflow work when the window narrows. Keep Settings in the app menu and open a dedicated settings window; do not spend primary toolbar space on it. Context menus supplement the menu bar for the current selection—they do not hide otherwise undiscoverable capabilities.

Register reversible in-app edits with `UndoManager` using the prior value and sensible coalescing. For external effects that cannot be undone, design a restore or recovery route and communicate the boundary before the action. An Edit menu whose Undo item is permanently disabled is the fastest tell that nothing was registered at all.

## Decide runtime boundaries early

Choose the deployment target from supported hardware, required APIs, and current adoption evidence. Record the rationale in durable project instructions.

Treat sandbox and hardened runtime as architecture:

- A sandboxed app can use approved system services and properly embedded/signed helpers, but cannot assume it may execute arbitrary user- or package-manager-installed tools. Decide whether helpers are bundled, connected through XPC, user-selected, or incompatible with sandbox distribution.
- User-selected file access and persistent bookmarks require the corresponding entitlements and security-scoped lifecycle; an open-panel URL is not universal continuing authority.
- Hardened runtime library validation permits Apple libraries and appropriately signed same-team code. Arbitrary third-party or unsigned dynamic libraries may require a different packaging/signing plan or, as a security tradeoff of last resort, disabling library validation. Do not add that entitlement automatically for every non-Apple dylib.
- Inspect entitlements and nested signatures from the built app — `codesign -d --entitlements - <App>.app`. Source plist files prove intent, not the emitted artifact, and a project generator can silently disagree with them: in XcodeGen an `entitlements:` block that names a `path:` without `properties:` rewrites that file to an empty dictionary on every generate, so the app ships sandboxed with no permissions and file access fails with no error.

## Choose interface technology deliberately

Prefer SwiftUI for new interface structure where it meets the target's needs. Use AppKit for mature text systems, complex tables/outlines, fine window and responder control, drag-and-drop, or framework gaps. Bridge deliberately rather than rebuilding a proven native component for purity; `appkit-interop` covers picking the narrowest bridge.

Preserve platform behavior: real windows with sensible minimum/default sizes, keyboard navigation and focus, system toolbars/sidebar patterns where appropriate, semantic fonts and colors, VoiceOver labels and order, Reduce Motion, and multi-window/restoration behavior when supported.

Size windows to their contents, not to a habitual 800×600. Settings should hug their controls; document windows should reveal a useful amount of document. With `NavigationSplitView`, columns lay out at the sum of their *ideal* widths and will not compress below it, so the window minimum must exceed that sum or the sidebar clips off one edge and the inspector off the other. Validate it against restored frames too—`.frame(minWidth:)` only constrains the user's drag, and a stale narrow frame saved by an earlier build can bypass the assumptions visible in SwiftUI layout code.

## Use the Mac's space and input model

Mac interfaces can carry real density. Use the large display to show more of the working set in fewer nested levels and with less modality, while keeping the primary content visually dominant. Prefer a sidebar for broad, relatively flat navigation, a content column for a deeper hierarchy, and an inspector for secondary properties. Do not put critical actions or state at the bottom edge, which may sit offscreen when a window is moved or resized.

Assume precision pointer input and a keyboard workflow. Support selection, multiple selection where the content calls for it, contextual actions, drag and drop, conventional modifier keys, meaningful focus order, and keyboard-only access to the core workflow. If the app is used repeatedly or professionally, consider toolbar customization, remembered window arrangements, and user-controlled presentation density.

## Establish a visual system

Read [references/visual-language.md](references/visual-language.md) when choosing or reviewing typography, color, symbols, toolbars, sidebars, or materials.

- **Typography:** use SF Pro through semantic SwiftUI text styles or AppKit font roles. macOS does **not** support Dynamic Type. Build hierarchy from role, spacing, and weight before introducing custom sizes; offer explicit content scaling when the product needs it.
- **Color:** use semantic, dynamic system colors for interface roles. Custom colors need light, dark, and increased-contrast behavior. Respect the person's accent color, keep meanings consistent, and never make color the only carrier of state.
- **SF Symbols:** make them the default source for interface glyphs in toolbars, sidebars, menus, buttons, status, and inline controls. Choose by meaning, match symbol weight and scale to adjacent text, prefer familiar variants, and use rendering modes or effects only when they clarify hierarchy or state. A custom glyph should be a deliberate exception, ideally built as a custom symbol so it inherits the same alignment and scaling behavior.
- **Materials:** use system surfaces and vibrancy where the platform gives them structural meaning—toolbars, sidebars, inspectors, overlays—not as decorative frosting.

Use labels or tooltips when a symbol's meaning is not immediately conventional, and always provide an accessibility label. Reserve motion for small, physical, interruptible state changes and keep a legible resting state under Reduce Motion.

Interface copy is short and operational because people learn the interface by using it, not by reading a narration beside every control. Helper text explains hidden consequences, not the label again. Capitalization, ellipses, and alerts have mechanical rules: use `apple-ui-copy`.

When a minimal reproduction proves a framework defect, use `os-workarounds` with a repro, upstream issue, owner, and removal test. Do not hard-code a private wiki path into a portable skill.

## Keep the experience continuous

Read [references/interaction-baseline.md](references/interaction-baseline.md) when implementing launch, asynchronous work, errors, localization, onboarding, or help. These concerns are easy to postpone because each can look secondary in a happy-path demo; together they determine whether the app feels dependable in ordinary use.

- **Launch and restoration:** become useful immediately; macOS does not need a launch screen. Restore the last meaningful working state—including windows, selection, sidebar or inspector visibility, and scroll position—when that state remains valid. Fall back to a useful default when it does not.
- **Responsiveness and progress:** never let long work read as a hang. Show content or a useful placeholder quickly, keep unrelated work available, use accurate determinate progress when work is measurable, and offer cancellation or pause when it is safe.
- **Feedback and recovery:** put status near the content or action it describes. Errors name what happened, preserve the person's work, and offer a concrete recovery step. Reserve alerts for rare, important, actionable interruptions; routine or undoable actions should not demand confirmation.
- **Localization and layout direction:** localize visible strings and locale-sensitive values, use leading and trailing rather than hard-coded left and right layout, and test long strings, right-to-left direction, mixed-script content, and the smallest supported window.
- **Discoverability and help:** prefer familiar controls, menu commands, labels, tooltips, and contextual tips. Onboarding starts after launch, remains brief and skippable, and teaches only what ordinary use cannot reveal. Explain the app-specific action, not how standard Mac controls work.

## Verification

Launch the built `.app` and verify the behavior appropriate to its app type: activation, menus and shortcuts, Settings, undo/recovery, toolbar overflow/customization where supported, Light and Dark appearances, Increase Contrast, smallest supported and restored window sizes, keyboard-only navigation, VoiceOver core flow, Reduce Motion, representative performance, and state restoration. Test a cold first launch and a relaunch with meaningful working state; confirm the process remains alive after launch rather than trusting `open` to report it, which returns before a crash-on-launch happens.

When you cannot see the screen, verify identity and menus mechanically rather than assuming: `lsappinfo info -only ApplicationType $(pgrep -x <App>)` should report `Foreground` for a regular app, and `osascript -e 'tell application "System Events" to tell process "<App>" to get name of menu bar items of menu bar 1'` should list the real menus rather than a bare template. A cold first launch also needs the accumulated state of previous runs cleared—saved window frames, defaults, and support directories—or first-run behavior is untestable on any machine that has already run the app.

Inspect typography and symbols at their real control sizes, not only in a zoomed canvas. Check the key and inactive window states, long or pseudolocalized labels, right-to-left layout, empty and error states, focus rings, disabled controls, and the longest realistic sidebar or table content. Deliberately slow and fail a representative operation; verify progress remains truthful, unrelated work remains usable, cancellation behaves safely, and recovery preserves the person's work. If onboarding exists, skip it and confirm the core workflow is still discoverable and help can be found again. Use Accessibility Inspector when available; a visual pass alone cannot verify the accessibility tree.

## Deliver a build the user can keep

DerivedData is an implementation cache, not a handoff location. Its paths are opaque, configuration-specific, and disposable. Never give the user a DerivedData path as the durable result, and never create a “stable” symlink whose target still lives there.

After the build passes verification:

1. copy the actual `.app` bundle to the project's documented stable location, such as `<project>/build/<App>.app`, or use the project's established install command;
2. when replacing an existing build, stop the old instance and copy to a temporary sibling before swapping it into the stable path, so interruption cannot leave a half-copied bundle; replace the prior build instead of accumulating indistinguishable copies;
3. launch and smoke-test **that copied artifact**, because a successful product in DerivedData does not prove the delivered copy is intact;
4. report the absolute path, build configuration, architecture, source revision and dirty state, signing/notarization state, and any environment it still depends on;
5. for distribution beyond the local development machine, produce the appropriate archived, exported, signed, and notarized artifact instead of relabeling a Debug build as distributable.

For visual work, capture only the app window through `window-capture`. Keep the stable-build convention in durable project instructions so later sessions replace the same artifact and the user always knows which app is current.

## Where to go deeper

Use these when installed. Each owns its topic; don't restate them here.

| Topic | Skill |
|---|---|
| Component and platform rules | `apple-hig`, `native-app-design` |
| SwiftUI API choices and code style | `swiftui-defaults` |
| AppKit bridges, windows, panels, responder chain | `appkit-interop` |
| Liquid Glass and system materials | `macos-liquid-glass` |
| Accessibility, VoiceOver, keyboard access | `apple-accessibility` |
| UI text and capitalization | `apple-ui-copy` |
| Animation and Reduce Motion | `apple-native-motion` |
| Concurrency and main-thread work | `swift-concurrency` |
| Apps built on TCA | `composable-architecture` |
| Project targets and entitlements | `xcodegen-targets` |
| App icon | `icon-design` |
| Crash reports | `crash-debugging` |
| Full audit of an existing app | `audit-macos-app` |
| Developer ID or TestFlight release | `ship-macos` |
| Window screenshots | `window-capture` |
