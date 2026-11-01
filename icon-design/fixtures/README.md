# Synthetic fixture contract

These are original deterministic diagnostic assets. They are not course derivatives or production artwork. Generate with `python scripts/make_fixtures.py NEW_DIRECTORY`; verify with `python scripts/test_iconkit.py`. No stochastic generator is used, so the seed is null. The generated manifest records Python/Pillow versions, dimensions/mode, expected property, and SHA-256. PNG byte identity is version-scoped; assert decoded properties as well as hashes.

| Fixture | Property | Failure exposed |
|---|---|---|
| alpha-ramp | Alpha 0..255; 224 partial pixels | Inverted or dropped alpha; false opaque acceptance |
| empty | Fully transparent 16×16 | Saving invisible icon as valid |
| one-pixel | 1×1 opaque | Zero-area arithmetic or invalid minimum handling |
| nonsquare | 16×8 source | Silent aspect distortion |
| full-bleed | Opaque and edge-touching | Treating every edge warning as clipping |
| transparent-border | Exact [3,3,13,13] bounds | Crop/coverage errors |
| renderer-probe | Soft blur plus hard clip | Unsupported filter or leaking clip |
| malformed | Invalid XML | Accepting unreadable source |

Tests also construct duplicate slots, mismatched scale metadata, out-of-range output dimensions, external SVG references, stale source/output receipts, and occupied output directories. Test fixtures are generated in disposable directories and removed by the test harness; existing user files are never fixture inputs.

`generated/` is the checked diagnostic corpus. The generator refuses an existing output directory. To compare regeneration, create a sibling or temporary directory, verify its manifest and pixels, then decide whether a source-controlled replacement is warranted. Do not overwrite reference fixtures before investigating drift.

A native ICNS decoder discrepancy was found during qualification. It is recorded in the tooling reference and research verification notes; do not convert that discrepancy into an expected artistic alteration. The direct PNG resources and independent decoder remain the source of truth for authored pixels.
