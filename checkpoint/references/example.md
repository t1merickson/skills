# Example checkpoint

A synthetic one, shown mid-project so the register is visible. The thing to copy is not the shape — it's how much unearned, uncertain, and half-formed material makes it in. A checkpoint that reads as tidy is a checkpoint that lost the payload.

---

# Checkpoint — Tessera

Last written: 2026-07-24, mid-way through the sync rewrite. Branch `sync-rewrite`, 6 commits in, not merged.

## Now

Replacing the naive last-write-wins sync with a CRDT-backed store so offline edits on two devices stop clobbering each other. Model layer is converted and tested; the SwiftUI views still bind to the old `Document` type through a shim. Next concrete step: delete the shim and update `LibraryView` to bind to `CRDTDocument` directly.

## Plates

- **The shim** (`Sync/LegacyDocumentBridge.swift`) — deliberately temporary, exists only so the views compile mid-migration. Three view files still depend on it. Delete it last, not first; it's load-bearing until they're all converted.
- **Waiting on timmy** — asked whether merge conflicts should surface in the UI at all or resolve silently. Blocks the conflict-banner work entirely; everything else can proceed.
- **Known-necessary, unstarted** — the migration path for existing users' local stores. Nobody has written a line of it. It is not hard, but it is not free, and it's the kind of thing that gets discovered the day before shipping.
- **Promised** — said I'd check whether the CRDT library's `merge` is actually O(n log n) as documented before we commit to it at library scale. Haven't.

## Terrain

- Tests: `xcodebuild test -scheme Tessera -destination 'platform=iOS Simulator,name=iPhone 16'`. The `-quiet` flag swallows the failure summary; don't use it.
- `SyncEngineTests` needs the fixture generator to run first (`swift run fixtures`) or 4 tests fail with an empty-store error that looks like a real bug and isn't. Cost me 40 minutes.
- The CRDT library vendors its own `Clock` type that shadows Foundation's in any file importing both. Fully-qualify.
- Simulator sync tests are flaky above ~200 documents — appears to be simulator disk throughput, not our code. Unconfirmed.

## Decided

- **CRDT over operational transform** — OT needs a central server to order operations; the whole point is offline-first peer sync. Not close.
- **Vendored the CRDT library rather than SPM** — needed two patches for the `Sendable` conformances and upstream is quiet. Revisit if upstream wakes up; the patches are in `Vendor/PATCHES.md`.
- **Document IDs stay UUIDs, not content hashes** — content hashes would dedupe identical documents, which sounds good and is actually wrong: two users independently writing the same note is two notes.

## Discards

- **Actor-per-document isolation** — killed. Elegant on paper, but every view read became async and the SwiftUI binding story fell apart. Would un-kill if we move off `@Observable`.
- **Syncing through CloudKit's record change tokens** — killed on the conflict model, not the transport. CloudKit resolves conflicts server-side with its own policy, which fights the CRDT rather than carrying it. Transport is still reusable if we want it.
- **Writing our own minimal CRDT** — killed for scope, reluctantly. Two days minimum and the merge semantics are exactly where subtle bugs hide. Reconsider only if the vendored library becomes a real liability.

## Live wires

- **The migration is going to be the hard part, not the CRDT.** No evidence, just pattern-matching — the data model translation is mechanical, but the "user has 800 documents in the old store and a half-synced iPad" case has nowhere good to fail. Worth thinking about before more feature work.
- ~60% sure the flaky sync tests are simulator disk throughput. Would settle it by running the same test on device and watching whether the failure count tracks document count the same way.
- **Almost said and cut:** the conflict-banner question I asked timmy may be the wrong question. Silent-resolve vs. surface-conflict is framed as binary, but the interesting version is surfacing only *semantic* conflicts (two different edits to the same paragraph) and silently merging structural ones. That's more work and might be the actually-correct design. Raise it before he answers the easier question.
- Nagging: `LibraryView` has grown to 400 lines and every migration step makes it worse. Not this PR's job. But it's the file that will make the next three tasks unpleasant.
- The vendored patches are undocumented in the commit history — only in `Vendor/PATCHES.md`. If someone re-vendors from upstream they'll silently lose them. Cheap to fix, keeps not getting fixed.
