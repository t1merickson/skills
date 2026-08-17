---
name: synthetic-fixtures
description: Recipes for generating good synthetic test media — images, audio, video, data — instead of using timmy's personal files. Use when a task needs test material: sample images, audio clips, datasets, placeholder video, or fixtures for an image/audio/data pipeline.
---

# synthetic-fixtures

timmy's files are never test material. synthetic is the first choice, and it's usually the better one: you control every property, it reproduces exactly, and nothing private can leak into a commit or screenshot.

## rules

- **seed everything.** a fixture that renders differently on the next run is a bug. pass explicit seeds to noise, random layouts, and generated data.
- fixtures live in a `fixtures/` directory in the project, named by what they test: `gradient-16bit.png`, `speech-like-3s.wav`, not `test1.png`.
- generate the properties the code under test actually exercises. testing color handling needs strong casts and wide gamuts, not pretty photos. testing edge cases needs the edges: 1px images, zero-length audio, empty arrays, huge files.
- when synthetic genuinely can't do it (you need real-world messiness, real photography, real speech), escalate: ask timmy for reference material, or pull open-access (Unsplash, Wikimedia Commons, freesound.org) into the project with the source noted in the repo.

## image recipes

- test cards: PIL or ImageMagick. grids, color bars, resolution wedges. `magick -size 512x512 gradient:red-blue out.png` for casts.
- seeded noise and procedural texture: numpy + PIL, always with `np.random.default_rng(seed)`.
- shapes and layouts: SVG written by hand then rasterized. exact, tiny, versionable.
- text rendering: system fonts via PIL's ImageFont. for macOS UI work, SF Symbols rendered from SwiftUI previews are legitimate fixtures.
- alpha and masks: generate the PNG with explicit alpha ramps; don't hand-edit.

## audio recipes (Owavo work lands here)

- tones, sweeps, and noise: `sox -n out.wav synth 3 sine 440`, `synth 3 sine 20-20000` for sweeps, `synth 3 whitenoise` / `pinknoise`.
- ffmpeg equivalents when sox is missing: `ffmpeg -f lavfi -i "sine=frequency=440:duration=3"`.
- speech-like without speech: amplitude-modulated noise bursts approximate the envelope; real speech comes from open-access (freesound, LibriVox) with source noted.
- edge cases: silence, clipped full-scale, 1-sample files, mismatched sample rates, mono vs stereo pairs.

## video and data

- video: `ffmpeg -f lavfi -i testsrc=duration=5:size=1280x720:rate=30` and the `smptebars` source. burn frame numbers in with `drawtext` when testing sync.
- structured data: small generators in the test file itself, seeded. realistic shapes (names, dates, unicode including NFD filenames, emoji, empty strings) matter more than realistic content.
- filenames as fixtures: when testing file handling, include the macOS traps on purpose — decomposed unicode names, case-collision pairs, spaces, very long names. see `file-batch-safety` for why.
