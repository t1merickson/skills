---
name: ship-macos
description: Release a macOS app through Developer ID or TestFlight with explicit credential gates, artifact verification, release provenance, and rollback information.
---

# Ship macOS

## Gates

Confirm the intended channel, version, supported architectures, and destination. Never invent a bundle ID. Before touching signing identities, keychains, provisioning profiles, notarization credentials, App Store Connect, or an upload, confirm that the requested release authorizes that exact step.

Read [references/distribution.md](references/distribution.md) for channel mechanics, then verify command syntax against the installed Xcode tools and current Apple documentation. Those details are volatile.

## Release record

Before distribution, write or update a project-local release record containing:

- source commit and dirty-state result;
- marketing version, build number, bundle ID, and architectures;
- Xcode/SDK version and release scheme;
- entitlements and signing identity/team;
- artifact names plus SHA-256 hashes;
- notarization submission ID or TestFlight build link/status;
- smoke-test results, known limitations, and the prior releasable artifact or rollback route.

Do not place secrets, profile contents, or private keys in the record.

## Verify the artifact people receive

Verification happens on the packaged output, not only the archive:

1. confirm signature, entitlements, architectures, version, and bundle ID;
2. verify notarization/Gatekeeper status for Developer ID distribution;
3. mount or install through the real delivery container;
4. launch and exercise the shortest critical flow on a clean-enough account or machine;
5. preserve the exact artifact and hash referenced by the release record.

If notarization fails, fetch and inspect the notary log before changing signing settings. Do not weaken hardened runtime or entitlements merely to make a submission pass.

Uploading or publishing leaves the machine and requires explicit scope. A locally verified artifact is not a shipped release; report the last completed gate precisely.
