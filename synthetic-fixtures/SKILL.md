---
name: synthetic-fixtures
description: Create deterministic synthetic media and data fixtures instead of using private user files, with property verification and provenance.
---

# Synthetic fixtures

Synthetic is the first choice: it controls the property under test, reproduces exactly, and keeps private material out of commits and screenshots.

## Contract

- Name the property and failure the fixture is meant to exercise before generating it.
- Seed every stochastic generator and pin material tool versions when output bytes matter.
- Store the generator beside the fixture or generate during tests. Record the command, seed, dimensions/duration/schema, SHA-256, and expected assertions.
- Verify properties programmatically: image mode/profile/EXIF/orientation, audio codec/rate/channels/loudness, video codec/rate/timestamps, or data encoding/schema. A file that merely opens is not a valid fixture.
- Include edge fixtures deliberately: empty, one-unit, maximum practical size, malformed, unusual Unicode, mismatched metadata, and boundary values relevant to the code.
- Strip accidental metadata and inspect generated files before committing them.

Use a project `fixtures/` directory and descriptive names such as `gradient-p3-16bit.png` or `silence-mono-48k-3s.wav`.

## Recipes

- Images: Pillow, ImageMagick, or SVG for exact test cards, alpha ramps, color casts, masks, resolution wedges, and seeded noise.
- Audio: SoX or FFmpeg for tones, sweeps, silence, clipped samples, seeded noise, channel layouts, and sample-rate mismatches.
- Video: FFmpeg test sources with burned-in frame numbers for sync, rate, color, and timestamp tests.
- Structured data: small seeded generators covering empty values, normalization forms, emoji, long names, case collisions, and invalid records.

When synthetic media cannot represent the required real-world messiness, ask for approved material or use clearly licensed public material. Store source URL, author, license, retrieval date, and any transformations. Do not assume that visible-on-the-web means reusable.

Pair every durable fixture with a verifier that fails when the property drifts. See `file-batch-safety` before generating or renaming a large fixture corpus.
