# macOS distribution mechanics

Verify these routes against the installed Xcode version and current Apple documentation before use.

## Developer ID

1. Archive the release scheme with `xcodebuild archive`.
2. Export using a Developer ID export options plist.
3. Submit the app or containing archive with `xcrun notarytool submit ... --wait` using an approved credential source.
4. If rejected or invalid, retrieve the notary log with the submission ID and diagnose it.
5. Staple the accepted ticket with `xcrun stapler staple`.
6. Verify with `codesign --verify --deep --strict`, inspect entitlements, and assess with `spctl -a -vv`.
7. Package the verified app in the project's established DMG or archive format, then mount and launch that package.

## TestFlight / App Store Connect

Archive and export for App Store distribution. Use Xcode Organizer or the current supported App Store Connect upload tool; do not preserve an obsolete uploader in project automation merely because it appears in an old note. Confirm version/build-number rules and existing uploaded builds before incrementing.

Processing, export compliance, tester groups, phased release, and review are separate gates. Record which one has actually completed.
