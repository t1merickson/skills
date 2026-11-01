# Tooling: an explicit icon workbench

## Capabilities and boundaries

`iconkit.py` replaces the useful **resource manifest → build → inspect → verify** loop from the old tools. It renders local SVG/PNG sources, preserves explicit optical overrides, records hashes, generates an offline HTML inspector, exports named SVG layers, and packages traditional ICNS resources. It does not infer good taste, create arbitrary Apple's `.icon` internals, install app icons, or control Photoshop.

Dependencies: Python 3.11+ and Pillow; Node.js and sharp; macOS `iconutil` for native container decode. Qualification run used Python 3.13.15, Pillow 12.3.0, sharp 0.35.4, librsvg 2.62.91, and libvips 8.18.6. Use your host's supplied runtime when available. Otherwise install dependencies in a project-local environment and retain its lockfile. Do not assume this run's temporary environment exists on another machine.

A typical local setup is:

```sh
python3 -m venv .icon-venv
.icon-venv/bin/pip install Pillow==12.3.0
npm install --prefix .icon-node sharp@0.35.4
export ICON_SHARP_MODULE="$PWD/.icon-node/node_modules/sharp"
export ICON_NODE=node
```

Use the resulting Python executable for all commands. `ICON_NODE` can be an absolute runtime executable; `ICON_SHARP_MODULE` can be an absolute module path. The script's other paths are relative to the command invocation or manifest, never a hardcoded personal directory.

## Manifest

Copy `examples/` into the project's icon workspace before editing. All source paths must resolve beneath the manifest directory. Each resource explicitly selects its source.

```json
{
  "schema": 1,
  "resources": [
    {
      "id": "mac-16pt-2x",
      "platform": "macos",
      "appearance": "default",
      "points": 16,
      "scale": 2,
      "pixels": 32,
      "source": "tiny.svg",
      "alpha": "allowed",
      "reason": "Enlarged recognition cue; removed secondary lines."
    }
  ]
}
```

Required: schema, nonempty resources, unique filename-safe IDs, source, integer pixel dimension 1..4096. If logical dimensions are supplied, points × scale must equal pixels and scale is 1, 2, or 3. Duplicate platform/appearance/logical-size/scale/pixel slots fail. `alpha` is `allowed` or `opaque`; omission means allowed. Sources must be square SVG with a finite square viewBox, or square PNG. Maximum 100 resources per manifest is a deliberate bounded-work constraint.

The tool does not automatically fall back to the largest master when an override is missing. This makes authorship visible and protects small-size decisions from a “regenerate everything” operation. The manifest may include intent/reason fields for human-readable provenance.

## Build and inspect

```sh
python scripts/iconkit.py build examples/manifest.json /tmp/icon-study-001
python scripts/iconkit.py verify examples/manifest.json /tmp/icon-study-001/receipt.json
python scripts/iconkit.py inspect /tmp/icon-study-001/mac-16pt-2x.png
```

The output directory must not exist. Each output is sRGB-tagged RGBA PNG. SVG root dimensions are set on a temporary copy before rendering so a small intrinsic canvas is not rasterized first and then enlarged. The original SVG remains untouched. The receipt records renderer versions, source/output hashes, dimensions, alpha bounds, coverage, centroid, partial-alpha count, and edge contact. Open `review.html` in a browser for intended CSS-size previews, magnified pixels, alpha views, and adjustable backgrounds. It has no network dependencies.

An edge-contact warning is not automatically an error: full-bleed backgrounds should reach the edge. Empty alpha is an error. The opaque contract fails if any pixel is translucent. The verification command detects changed manifests, sources, or outputs. It does not certify that a maliciously edited receipt is authentic; receipts are local reproducibility records, not signatures.

On a failed build, completed derivatives and `FAILED.json` stay in the new output directory. Read the error, fix the source or manifest, and build to another directory. Do not merge old and new partial output sets. No command overwrites an existing output directory or deletes sources.

## Registered layer export

```sh
python scripts/iconkit.py layers examples/composer-layers.svg /tmp/icon-layers-001
```

Top-level groups require safe unique IDs. The export retains the full canvas and shared definitions in each SVG and writes `layers.json`. Keep shared geometry in `<defs>` rather than referencing omitted sibling groups. The tool does not flatten effects, assign material settings, or create a `.icon` package. Inspect every export and import into Icon Composer through its supported workflow. Simple background color is configured there.

## Traditional ICNS packaging

```sh
python scripts/iconkit.py icns examples/manifest.json /tmp/icon-study-001/receipt.json /tmp/icon-package-001
```

Requires ten `macos/default` slots: 16, 32, 128, 256, 512 points, each 1x and 2x. The default encoding stores PNG resources with separate logical-slot codes. It verifies them with Pillow's ICNS decoder and also invokes Apple's `iconutil` to decode all ten slots. `--encoding native` delegates encoding to `iconutil` instead. Packaging writes its source `.iconset`, decoded native `.iconset`, container, and receipt in a new directory.

The codes and independent decoder follow [Pillow's ICNS implementation](https://pillow.readthedocs.io/en/stable/_modules/PIL/IcnsImagePlugin.html). Traditional filenames are documented in Apple's [archived Icon Set Type reference](https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/IconSetType.html). This packaging path is not a current layered-app-icon specification.

**Qualification caveat:** On this host, `iconutil` decoded the two smallest 1x resources with changed partial-alpha RGB values, even when the container retained exact PNG bytes. The independent decoder preserved every RGBA value for the default PNG encoding. The package receipt therefore records native differences instead of silently tolerating or “correcting” the source art. A package with such differences requires actual-consumer inspection; do not claim universal visual fidelity. Native decode discrepancies are not automatically proof that Finder renders incorrectly.

Sandboxed `iconutil` also reported “Invalid Iconset” here despite valid files; the same native command succeeded outside the sandbox. Diagnose dimensions and files first, then use the host's normal approval mechanism if native services are unavailable. Do not keep changing artwork to fix an environment failure.

## Qualification and regression

```sh
python scripts/test_iconkit.py
python scripts/make_fixtures.py /tmp/icon-fixtures-001
```

See [fixture contract](../fixtures/README.md). Tests cover source/slot failures, alpha semantics, stale and changed outputs, renderer blur/clipping, layers, and fixture hashes. The actual example also exercises 10 resources and packaging. When adding a new filter, gradient mode, raster profile, or external renderer, add a small targeted probe before relying on it. Do not use CairoSVG as a drop-in replacement without qualifying filters: renderer feature support differs.

Unsupported production needs should get an explicit adapter and tests, not a broadening claim: Display P3, SF Symbols validation, Windows ICO packaging, arbitrary SVG/CSS, `.icon` compilation, or automated app integration are outside this version.
