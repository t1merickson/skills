---
name: synthetic-fixtures
description: Recipes for synthetic test media — images, audio, video, data — instead of the user's personal files.
---

# synthetic-fixtures

The user's files are never test material. Synthetic is the first choice, and it's usually the better one: you control every property, it reproduces exactly, and nothing private can leak into a commit or screenshot.

## Rules

- **Seed everything.** A fixture that renders differently on the next run is a bug. Pass explicit seeds to noise, random layouts, and generated data.
- Fixtures live in a `fixtures/` directory in the project, named by what they test: `gradient-16bit.png`, `speech-like-3s.wav`, not `test1.png`.
- Generate the properties the code under test actually exercises. Testing color handling needs strong casts and wide gamuts, not pretty photos. Testing edge cases needs the edges: 1px images, zero-length audio, empty arrays, huge files.
- When synthetic genuinely can't do it (you need real-world messiness, real photography, real speech), escalate: ask the user for reference material, or pull open-access (Unsplash, Wikimedia Commons, freesound.org) into the project with the source noted in the repo.

## Image recipes

- Test cards: PIL or ImageMagick. Grids, color bars, resolution wedges. `magick -size 512x512 gradient:red-blue out.png` for casts.
- Seeded noise and procedural texture: numpy + PIL, always with `np.random.default_rng(seed)`.
- Shapes and layouts: SVG written by hand then rasterized. Exact, tiny, versionable.
- Text rendering: system fonts via PIL's ImageFont. For macOS UI work, SF Symbols rendered from SwiftUI previews are legitimate fixtures.
- Alpha and masks: generate the PNG with explicit alpha ramps; don't hand-edit.

## Audio recipes (Owavo work lands here)

- Tones, sweeps, and noise: `sox -n out.wav synth 3 sine 440`, `synth 3 sine 20-20000` for sweeps, `synth 3 whitenoise` / `pinknoise`.
- ffmpeg equivalents when sox is missing: `ffmpeg -f lavfi -i "sine=frequency=440:duration=3"`.
- Speech-like without speech: amplitude-modulated noise bursts approximate the envelope; real speech comes from open-access (freesound, LibriVox) with source noted.
- Edge cases: silence, clipped full-scale, 1-sample files, mismatched sample rates, mono vs stereo pairs.

## Video and data

- Video: `ffmpeg -f lavfi -i testsrc=duration=5:size=1280x720:rate=30` and the `smptebars` source. Burn frame numbers in with `drawtext` when testing sync.
- Structured data: small generators in the test file itself, seeded. Realistic shapes (names, dates, unicode including NFD filenames, emoji, empty strings) matter more than realistic content.
- Filenames as fixtures: when testing file handling, include the macOS traps on purpose — decomposed unicode names, case-collision pairs, spaces, very long names. See `file-batch-safety` for why.
