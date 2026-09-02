---
name: macos-design
description: Best practices for building native macOS apps, including app identity, menu commands, sandbox and signing boundaries, AppKit/SwiftUI choices, accessibility, and artifact verification.
---

# macOS app essentials

Read this early in a macOS app session. People expect a Mac app to behave like a Mac app from first launch; the failures here are cheap to avoid and expensive to retrofit. Use the current Human Interface Guidelines and platform documentation for component- or release-specific facts; do not treat this file as a frozen SDK reference.

## Establish the app type

Decide whether the product is a regular foreground app, menu-bar utility, background agent, document app, or mixed design. The recurring generated-app failure is a detached, ownerless window: a process with no real Dock presence, menu architecture, restoration, or identity. Make identity and activation policy agree:

- Regular apps use a real `.app` bundle, normal lifecycle, menu bar, Dock/App Switcher presence, and owned windows.
- Menu-bar utilities and agents may intentionally use `LSUIElement` or accessory activation. Their discoverability, settings, quit path, and relaunch behavior need explicit design because the Dock will not provide them.
- Verify the built bundle, not `swift run`: bundle metadata, signing, entitlements, loader behavior, menus, restoration, and launch crashes only exist in the shipped shape.
- Use a real icon before release. During development, either retain the project's existing mark or label a neutral placeholder clearly; do not invent permanent branding. Supply the complete asset catalog and let macOS apply its mask.

## Menus are command architecture

Expose user-visible commands through conventional menus and shortcuts. Keep system text editing, undo, Settings at Command-Comma, Window management, and Help behavior intact. Remove irrelevant template commands rather than shipping dead items.

Register reversible in-app edits with `UndoManager` using the prior value and sensible coalescing. For external effects that cannot be undone, design a restore or recovery route and communicate the boundary before the action.

## Decide runtime boundaries early

Choose the deployment target from supported hardware, required APIs, and current adoption evidence. Record the rationale in durable project instructions.

Treat sandbox and hardened runtime as architecture:

- A sandboxed app can use approved system services and properly embedded/signed helpers, but cannot assume it may execute arbitrary user- or package-manager-installed tools. Decide whether helpers are bundled, connected through XPC, user-selected, or incompatible with sandbox distribution.
- User-selected file access and persistent bookmarks require the corresponding entitlements and security-scoped lifecycle; an open-panel URL is not universal continuing authority.
- Hardened runtime library validation permits Apple libraries and appropriately signed same-team code. Arbitrary third-party or unsigned dynamic libraries may require a different packaging/signing plan or, as a security tradeoff of last resort, disabling library validation. Do not add that entitlement automatically for every non-Apple dylib.
- Inspect entitlements and nested signatures from the built app. Source plist files prove intent, not the emitted artifact.

## SwiftUI and AppKit

Prefer SwiftUI for new interface structure where it meets the target's needs. Use AppKit for mature text systems, complex tables/outlines, fine window and responder control, drag-and-drop, or framework gaps. Bridge deliberately rather than rebuilding a proven native component for purity.

Preserve platform behavior: real windows with sensible minimum/default sizes, keyboard navigation and focus, system toolbars/sidebar patterns where appropriate, Dynamic Type/legible text, semantic colors, VoiceOver labels and order, Reduce Motion, and multi-window/restoration behavior when supported.

Size windows to their contents, not to a habitual 800×600. Settings should hug their controls; document windows should reveal a useful amount of document. With split views, validate the sum of column minimums against both the window minimum and restored frames—a stale narrow frame can bypass the assumptions visible in SwiftUI layout code.

Mac interfaces can carry real density. Build hierarchy from alignment, spacing, weight, and semantic color before reaching for larger type, decorative materials, or extra panels. Use SF Symbols at compatible weights and reserve motion for small, physical, interruptible state changes.

Interface copy is short and operational because people learn the interface by using it, not by reading a narration beside every control. Ellipses mean more input is required before the command executes. Helper text explains hidden consequences, not the label again.

When a minimal reproduction proves a framework defect, use `os-workarounds` with a repro, upstream issue, owner, and removal test. Do not hard-code a private wiki path into a portable skill.

## Verification

Launch the built `.app` and verify the behavior appropriate to its app type: activation, menus, Settings, undo/recovery, Dark Mode, smallest supported window, keyboard-only navigation, VoiceOver core flow, Reduce Motion, representative performance, and state restoration. Confirm the process remains alive after launch rather than trusting `open` to report it.

For visual work, capture only the app window through `window-capture`. For ongoing local use, provide a documented stable build output or install command rather than pointing at ephemeral DerivedData.
