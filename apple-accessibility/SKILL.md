---
name: apple-accessibility
description: "Native accessibility for SwiftUI, UIKit, and AppKit apps: VoiceOver labels, traits, grouping, and reading order; custom actions and rotors; Dynamic Type and text scaling; Reduce Motion, Reduce Transparency, Increase Contrast, and Differentiate Without Color; keyboard and Full Keyboard Access; Voice Control; and how to test all of it. Use when building or reviewing accessibility in an Apple-platform app. Do not use for web accessibility (ARIA, HTML, WCAG markup)."
---

# Apple accessibility

Accessibility on Apple platforms is mostly free if you use system controls and mostly lost the moment you draw your own. The work is in three places: custom views, layouts that assume a text size, and anything that only works with a pointer or only shows state with color.

The component rules live in the Human Interface Guidelines: the `Accessibility`, `VoiceOver`, `Typography`, `Motion`, and `Color` pages (in the local `apple-hig` mirror when installed). This skill covers the implementation and the testing.

## Start from the system

- A `Button`, `Toggle`, `Picker`, `Slider`, `List`, or `Form` already has a role, a value, and actions. Style it rather than replacing it. A tap gesture on a `Text` or a shape has no role, no keyboard access, and no VoiceOver action until you add each one.
- Give every icon-only control a label. In SwiftUI, use `Button("Delete", systemImage: "trash")` or a `Label` with `.labelStyle(.iconOnly)`. The text stays available to VoiceOver and Voice Control.
- Mark decorative images as decorative: `Image(decorative:)` or `.accessibilityHidden(true)`. An image read aloud as its file name is worse than silence.

## VoiceOver: what an element is, says, and does

| Need | SwiftUI | UIKit / AppKit |
|---|---|---|
| Name | `.accessibilityLabel` | `accessibilityLabel` |
| Current value | `.accessibilityValue` | `accessibilityValue` |
| Role and state | `.accessibilityAddTraits(.isHeader)` / `.isSelected` / `.isButton` | `accessibilityTraits` (UIKit), `accessibilityRole` (AppKit) |
| What happens on activate, when not obvious | `.accessibilityHint` | `accessibilityHint` |
| One element from several views | `.accessibilityElement(children: .combine)` | a container with `isAccessibilityElement = true` |
| Secondary actions without hidden gestures | `.accessibilityAction(named:)` | `accessibilityCustomActions` |
| Increment and decrement a custom control | `.accessibilityAdjustableAction` | `.adjustable` trait plus `accessibilityIncrement()` |
| Replace a custom control's accessibility with a standard one | `.accessibilityRepresentation { Slider(...) }` | — |
| Reading order | `.accessibilitySortPriority` | element order in `accessibilityElements` |
| Jump between items of one kind | `.accessibilityRotor` | `accessibilityCustomRotors` |
| Announce something that changed off-focus | `AccessibilityNotification.Announcement("…").post()` | `UIAccessibility.post(notification: .announcement, …)` / `NSAccessibility.post` |
| Charts | `.accessibilityChartDescriptor` | `accessibilityChartDescriptor` |

Rules that come up in every review:

- **The label is a noun, not an instruction.** "Delete", not "Tap to delete" and not "Delete button". VoiceOver already speaks the role and how to activate it.
- **A list row reads as one thing.** Combine the title, subtitle, and status into one element so VoiceOver doesn't stop on each fragment. Put row actions such as delete, flag, and share into custom actions; swipe actions and context menus alone are hard to find.
- **State is spoken, not just shown.** Selected, on, unread, and error states need a trait or a value as well as a color or a badge.
- **Labels change with the UI.** A play/pause button whose label still says "Play" while playing is a bug.
- **Headers are marked.** VoiceOver users move by heading; a screen with none forces them to swipe through every element.

## Text size

On iOS, iPadOS, watchOS, and visionOS, people pick a text size and Dynamic Type applies it. **macOS has no system-wide Dynamic Type.** There the concern is using text styles instead of fixed point sizes, and offering an in-app size setting when the content is text-heavy.

- Use text styles (`.body`, `.headline`, `.caption`) or `Font.custom(_:size:relativeTo:)`. A fixed `.system(size: 15)` does not scale.
- Scale the spacing and icon sizes that sit next to text with `@ScaledMetric`.
- At accessibility sizes, a row that was side by side usually has to stack. Check `dynamicTypeSize.isAccessibilitySize` and switch layout with `AnyLayout` or `ViewThatFits`; don't truncate.
- Let text wrap. `lineLimit(1)` on content text is a decision to hide words from people who need them most.
- Cap the range with `.dynamicTypeSize(...)` only for chrome that physically cannot grow, never for content.

## Display settings

Read each through the environment and design a real alternative, not an absence.

| Setting | SwiftUI environment | What to do |
|---|---|---|
| Reduce Motion | `accessibilityReduceMotion` | Replace movement and scale with a crossfade; keep the state change. See `apple-native-motion`. |
| Reduce Transparency | `accessibilityReduceTransparency` | Put an opaque background behind text on custom materials. System materials already adapt. |
| Increase Contrast | `colorSchemeContrast == .increased` | Give custom colors a high-contrast variant in the asset catalog; strengthen borders. |
| Differentiate Without Color | `accessibilityDifferentiateWithoutColor` | Add a shape, symbol, or label wherever color alone carries meaning. Better: do it always. |
| Bold Text | `legibilityWeight == .bold` | Custom fonts need a heavier weight; text styles handle it. |

## Keyboard, switch, and voice

- **iPad and Mac:** everything the pointer can do, the keyboard can do. Use `.focusable()`, `@FocusState`, and `.onKeyPress` for custom controls; give commands shortcuts through the menu bar or `.keyboardShortcut`.
- **Mac:** test with keyboard navigation turned on (System Settings > Keyboard > Keyboard navigation). Without it, Tab skips most controls, so a test with it off proves nothing.
- **Voice Control:** people say what they see. When the visible text differs from the label, or the label is long, add the short spoken forms with `.accessibilityInputLabels`.
- **Hit areas:** the HIG's default control size is 44 × 44 points on iOS and iPadOS and 28 × 28 on macOS, with floors of 28 × 28 and 20 × 20. Aim for the default. Grow the hit area with `.contentShape`, not the visible control.

## Testing

Reading the code is not enough. Test the built app.

1. **Automated audit.** In a UI test, `try XCUIApplication().performAccessibilityAudit()` (Xcode 15+, iOS 17+ and macOS 14+) fails on missing labels, clipped text, low contrast, small hit areas, and more. Run it through the project's test entry point on each main screen. It catches the mechanical half.
2. **Accessibility Inspector** (Xcode > Open Developer Tool). Point it at the simulator or the Mac app, hover elements to read label, value, and traits, and run its audit.
3. **VoiceOver for real.** Turn it on (Command-F5 on Mac; Settings > Accessibility on a device or simulator) and complete the core task without looking. Listen for unlabeled buttons, fragments that should be one element, and focus that jumps after an update.
4. **Largest text size.** On iOS, the largest accessibility size; in the simulator, `xcrun simctl ui booted content_size accessibility-extra-extra-extra-large`. Look for clipping, overlap, and content you can no longer scroll to.
5. **Each display setting** from the table above, once, on the screens that use custom drawing, materials, or motion.

For the simulator mechanics see `simulator-driving`. For a running Mac app, `audit-macos-app` reads the accessibility tree through System Events.

## Reporting

For each finding: the screen and element, which setting or assistive technology exposes it, what a person experiences ("VoiceOver reads 'button' with no name"), and the fix. Rank by how far it blocks the core task, not by how many there are. A missing label on the primary action outranks fifty decorative images read aloud.
