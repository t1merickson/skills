# Apple delivery — verified 2026-10-03

This file records a dated production boundary, not a permanently correct SDK table. Refresh the linked primary documents and inspect the project's actual Xcode/OS targets before shipping. The documentation retrieved for this skill includes 2026 and OS 27 material; do not silently apply every control to OS 26.

## Route decision

| Task | Authoring and delivery route | Required proof |
|---|---|---|
| Layered macOS/iOS app icon | Clean registered layers → Icon Composer → `.icon` in Xcode | Composer appearance checks plus built app on supported OS |
| Static illustrative app icon / existing catalog workflow | SVG or raster optical masters → target's asset catalog | Xcode compilation and installed context |
| Traditional macOS ICNS/customization study | Explicit optical resources → `.iconset` → `iconutil` | Container decode and actual consumer |
| Document/file-type icon | Shared base and badges, target's document-icon mechanism | Registered file type in disposable test app/context |
| Toolbar/menu/sidebar symbol | Match system symbol semantics and weight; use appropriate symbol/template pipeline | Actual control, selected/disabled states, accessibility label |

The supplied CLI implements raster study, a layer handoff, and traditional ICNS packaging. It is **not** an Icon Composer compiler, Xcode asset-catalog compiler, or native symbol authoring tool.

## Current layered app-icon design

Apple's current HIG describes a 1024×1024 square canvas for iOS, iPadOS, and macOS. Supply unmasked layers and let the system form the outer shape. Keep a clear central identity, defined foreground edges, and a full-bleed opaque background when importing one. Current appearances include default, dark, clear light/dark, and tinted light/dark. Maintain recognizable features across them. Supported color spaces include sRGB, Gray Gamma 2.2, and Display P3. The included kit intentionally outputs sRGB only. [Apple HIG: App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons)

These constraints are compatible with rich identity. The design question is which complexity belongs in the artwork and which belongs in the system's rendering. For a static illustrated lens, painted metal may be part of the identity. For a simple overlapping lens emblem, system material may express depth more coherently. Test the actual result before deciding.

## Composer workflow and version boundary

Create clean SVG/PNG foreground assets with matching canvases and meaningful ordered names. Import them into Composer, organize up to four groups, configure background and appearances, and save the `.icon` file. Add it to the app target and match the App Icon setting to its filename without the extension. Composer owns the material preview; a browser is insufficient. Current docs say adding this file supersedes the old app-icon catalog and generates backward-compatible images. Retain the catalog route if preserving an existing older-OS icon is required. The retrieved documentation also distinguishes OS 27 refraction/specular controls from earlier behavior. Verify the installed tool and target OS before using them. [Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer)

Record the tool build, target OS, appearance, settings, and screenshot for each material decision. “Looks good in Composer” and “looks good on the supported OS” are separate facts. For lower-version rendering, check the appropriate preview mode and still inspect an installed build.

Apple's WWDC25 demonstration recommends preserving canvas registration, outlining text, and leaving dynamic material decisions for Composer. Its examples show that local optical tuning remains necessary even when export is automated. It also describes a flattened-art route for complex illustration. Do not confuse the old pre-Liquid-Glass utility named Icon Composer in the course with this newer tool. [Create icons with Icon Composer, WWDC25](https://developer.apple.com/videos/play/wwdc2025/361/)

## Static asset catalogs

Xcode's catalog workflow can generate iOS/iPadOS variations from one high-resolution image or accept individually supplied variants. Its current documentation specifies individual macOS sizes. It describes iOS dark and tinted assets separately: tinted is grayscale; dark may use transparency to reveal the system background. Therefore “all iOS icon inputs must be opaque” is an unsafe blanket rule. Apply the exact contract of the slot being supplied. The default/App Store image and a foreground layer are not interchangeable. [Configuring your app icon using an asset catalog](https://developer.apple.com/documentation/xcode/configuring-your-app-icon)

Use the project's actual generated catalog schema and image wells. Do not paste a decade-old `Contents.json` size table into a current project and call it complete. Check compiled warnings and archived output. A source filename looking right does not prove that the correct target includes it.

## Traditional macOS ICNS

The kit supports the familiar `.iconset` resource family of 16, 32, 128, 256, and 512 logical points at 1x and 2x. It stores explicit PNG resources by default, checks them with an independent decoder, and uses the host's `iconutil` for a separate native decode check. Native differences are reported; see the tooling reference. This is an explicit legacy/static packaging capability, not a replacement for the modern layered app-icon route. The output still requires a consumer-specific test.

Do not bake assumptions about Finder caching into destructive troubleshooting. Use a new disposable test bundle or file, confirm its identifier and resource references, and inspect it. Avoid altering an installed third-party app merely to view an icon.

## Interface symbols and document icons

Do not apply the app-icon rounded container and material vocabulary automatically to every small UI glyph. Symbols need meaningful action/state semantics, matching weight and scale, and accessible text supplied by the application. Prefer established platform symbols when they express the intended action. Custom symbols require their own template and rendering checks; this skill's SVG renderer alone does not establish SF Symbols compatibility.

Document icons need a clear family relationship and actual file-type integration. The course's normal/open/drop resource examples are historical. Verify the current application/document mechanism instead of promising support for those states.

## Release record

Record: source hashes; route; tool versions; target/minimum OS; platform and appearance coverage; decoded output dimensions; compiled target association; real-context screenshots; and remaining human preference decisions. If the task stops at artwork, say “artwork and layer handoff complete.” Do not call it an integrated or shipped app icon.
