---
name: ship-macos
description: Release flow for timmy's macOS apps — archive, Developer ID export, notarize, staple, package as DMG or push to TestFlight. Use when timmy says "ship it" about a macOS app, "notarize", "release build", "make a DMG", "put it on TestFlight", or asks to distribute an app outside Xcode.
---

# ship-macos

two gates before anything else:

1. **signing is security-shaped.** touching signing identities, keychains, provisioning profiles, or App Store Connect credentials falls under the ask-first list in CLAUDE.md. confirm with timmy before the first signing step of a session. after that, the session's approval holds.
2. **bundle ID.** never invent one. ask which domain: `com.timerickson.*` (personal), `cool.wizard.*` (Wizard apps), `xyz.fourthplaces.*` (fourth places). if the project already has one, use it.

## the flow (Developer ID, outside the App Store)

the stable skeleton. flags drift between Xcode versions, so on first use in a session, verify the exact syntax against `man` pages or Apple's current docs rather than trusting this file or memory:

1. archive: `xcodebuild archive` with the release scheme.
2. export with the Developer ID method: `xcodebuild -exportArchive` and an export options plist.
3. notarize: `xcrun notarytool submit <artifact> --wait` (needs an App Store Connect API key or keychain profile — credentials, so gate 1 applies).
4. staple: `xcrun stapler staple <app>`.
5. verify: `spctl -a -vv <app>` should say accepted, source Notarized Developer ID.

package: `hdiutil` for a plain DMG, or `create-dmg` if it's installed for a nicer one. name it `<App>-<version>.dmg`.

## TestFlight instead

archive the same way, export with the app-store method, upload via `xcrun altool` or Xcode's organizer, then processing happens on App Store Connect. TestFlight builds need the version and build number bumped; check the current values before bumping, and bump build number only unless timmy says otherwise.

## rules

- every shipped artifact gets verified: open the DMG, launch the app on this machine, confirm no Gatekeeper complaint. "notarytool said accepted" is not the finish line; the launch is.
- distribution is "leaves this machine": uploading to TestFlight or anywhere public needs timmy's go-ahead per the ask-first list. building and notarizing locally does not.
- record the flow's project-specific quirks (scheme names, plist paths, version conventions) in that project's CLAUDE.md the first time you learn them.
