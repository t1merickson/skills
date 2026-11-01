# macOS visual language

Read this when defining or auditing the app's visual system. It is a decision guide, not a frozen specification. Apple revises the HIG and system appearance; check the linked pages and the deployed macOS SDK when an exact size, API, or availability boundary matters. Last reviewed 2026-09-03.

## Typography

- SF Pro is the macOS system typeface. Use semantic SwiftUI text styles or AppKit's role-specific system fonts so interface text matches standard controls.
- macOS does not support Dynamic Type. Do not copy an iOS Dynamic Type claim into a Mac acceptance checklist. If people need larger document or content text, provide an explicit scale or font preference and make the layout tolerate it.
- Body text is commonly 13 points in the current HIG, but the role is the durable decision and the number is a reference value. Avoid scattering literal point sizes through views.
- Establish hierarchy with semantic role, grouping, alignment, space, and weight before size. Too many sizes make a dense Mac interface noisy; very light weights make small text fragile.
- UI chrome normally uses the system font. A document editor or creative tool can let people choose fonts for their content without turning the app's controls into branded typography.
- Test long and localized labels, truncation, wrapping, editable fields, menus, and the smallest supported window. A type scale that works only in the ideal screenshot is not a system.

Current source: [Typography — Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/typography).

## Color and appearance

- Start with semantic system roles such as label, secondary label, separator, control background, selected content, and keyboard focus indicator. Use the role's API rather than copying its current numeric value.
- Let the person's system accent color appear where AppKit and SwiftUI expect it. Avoid tinting every sidebar or toolbar glyph with a fixed brand color; color stops communicating when it is everywhere.
- A custom color set needs deliberate variants for Light, Dark, and Increase Contrast. Test it over the actual material or background where it appears, including key and inactive windows.
- Keep one meaning per color. Do not reuse the same treatment for interactive text, decoration, selection, warning, and success.
- Pair color with text, shape, position, or a symbol when it communicates status. Color alone is not enough for selection, errors, or destructive consequences.
- Prefer system-drawn window and control surfaces. Custom chrome inherits responsibility for key-window, inactive-window, focus, vibrancy, contrast, and future appearance changes.

Current sources: [Color](https://developer.apple.com/design/human-interface-guidelines/color), [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode), and [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).

## SF Symbols

Use SF Symbols aggressively for interface iconography because they share the system font's optical alignment, weights, scales, localization behavior, and appearance adaptation.

- Search the current SF Symbols catalog before drawing a custom glyph. Prefer the symbol whose established meaning matches the command, not the one whose silhouette merely fits the space.
- Match weight and scale to adjacent text and the containing control. Inspect the result at its rendered size; a detailed symbol that looks good enlarged may close up in a compact toolbar.
- Use outline, fill, slash, badge, and enclosed variants to communicate state or emphasis consistently. Do not mix variants arbitrarily across sibling controls.
- Monochrome is the dependable default. Use hierarchical, palette, multicolor, variable-color, gradient, or animated effects when layers encode real hierarchy, status, or change—not to make every control lively.
- Prefer automatic/system colors so symbols adapt to appearance and accessibility settings. Sidebar icons should generally honor the person's accent color.
- Pair unfamiliar or consequential symbols with text, a tooltip, or both. Give every symbol-only control an accessibility label that names the action, not the artwork.
- If no system symbol fits, begin from the closest custom-symbol template so baseline, cap height, margins, weights, and rendering layers behave like the rest of the interface.

Current sources: [SF Symbols HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) and [SF Symbols resources](https://developer.apple.com/sf-symbols/).

## Toolbars, sidebars, and hierarchy

- A toolbar holds frequent commands, navigation, search, and the current-view title. Group items by purpose and keep enough room to distinguish and activate them.
- Every toolbar command also needs a menu-bar home because toolbars can be hidden, customized, or collapsed into overflow. The inverse is not true: rare menu commands do not all deserve toolbar space.
- Use the leading toolbar region for navigation/sidebar controls and identity, the central region for common work, and the trailing region for secondary actions when that arrangement fits the app.
- A sidebar presents a broad, fairly flat information hierarchy. Keep it to roughly two visible hierarchy levels; add a content column when the data is deeper.
- Let people show and hide the sidebar through familiar controls and View-menu commands. Consider automatic collapse at narrow widths, but do not hide the app's primary map by default.
- Use an inspector for substantial properties related to a selection. A bottom status bar is for a small amount of status, not critical controls or a second inspector; the bottom edge of a Mac window may sit offscreen.
- Professional and frequently used apps should consider customizable toolbars, persistent window arrangements, and user choices for useful density, fonts, or colors where those choices affect the work rather than merely exposing implementation knobs.

Current sources: [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos/), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), [Windows](https://developer.apple.com/design/human-interface-guidelines/windows), and [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).

## Review questions

- Does a grayscale screenshot still reveal hierarchy and state?
- Does every toolbar action remain reachable after hiding the toolbar?
- Does the interface respect the person's accent color and remain clear in Light, Dark, and Increase Contrast?
- Do text and symbols share a deliberate role, weight, scale, and baseline?
- Can the smallest supported window still expose the primary content, navigation, and recovery paths?
- Does a keyboard-only pass show visible focus and reach the whole core workflow?
- Does the app remain recognizably itself when materials, symbol effects, and animation are reduced?
