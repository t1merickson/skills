---
name: kit
description: Operate Kit, the font-project toolkit (`kit` CLI) that holds all of a type-design workspace's tooling: audits and rule plugins, measuring, parts, coverage and fill, curve repair, plans applied safely to Glyphs packages, kerning and spacing, sheets and specimens, tracing, Bench views. Use for any measuring, checking, editing or reporting on fonts in a workspace that has Kit, before writing a new script.
---

# Kit

Kit is one CLI and Python library for a type-design workspace (`Developer/Fonts`): every font project reads fonts,
measures, checks, edits and reports through it. The projects hold data, sources and pages; the tools live in Kit.
Its docs live with it: `Kit/README.md`, `Kit/docs/cookbook.md` (which command answers which question), `Kit/docs/commands.md`, `Kit/docs/library.md`, and `Kit/DESIGN.md` (the contract). Read the
cookbook first; read DESIGN.md before changing Kit.

## Run it

From inside a project (Kit finds the nearest `kit.toml`): `.venv/bin/kit <command>`. The project's `kit.toml` supplies
the font, the reference, the output folder and the rules, so most commands need no arguments.

| Need | Command |
|---|---|
| check drawing against the project's rules (plus rule plugins: health, components, kinks, joints, wobble...) | `kit audit` (prints new / fixed / same) |
| numbers: levels, stems, weight, curves, terminals, serifs, spacing, sides, body, nib... | `kit measure FONT TOPIC` (`--list` shows topics) |
| stroke weight and contrast at chosen spots | `kit weigh` |
| shared drawings, components, ligature parts, marks | `kit parts` |
| what's built, waiting, left to draw; language support | `kit coverage`, `kit languages` |
| fill a glyph set from a reference out of your own parts | `kit fill --plan`, then `--apply --glyphs-closed` |
| curve repair: fair, fillets, rounds, snap, smooth, refit | `kit curves ...` (a plan + Bench overlays) |
| apply any plan to a package safely; preview it | `kit apply PLAN --glyphs-closed`, `kit preview PLAN` |
| a bold from the regular; serif corners as components; stems on a reference's hints | `kit embolden`, `kit corners`, `kit align` |
| kerning and spacing | `kit kern ...`, `kit space ...` |
| pictures and pages | `kit sheet`, `kit overlay`, `kit specimen`, `kit proof` |
| pictures to outlines; pen centerlines | `kit trace`, `kit skeleton` |
| what changed between two versions | `kit diff BEFORE AFTER` |
| one glyph's points, a font's tables | `kit inspect FONT GLYPH`, `kit info FONT` |
| fonts by name | `kit fonts` |
| Bench views, measurement marks, review lists | `kit view`, `kit marks`, `kit review`, `kit retire` |

Each report writes `report.html` for the user and `report.json` for you, side by side in `<out>/<command>/`. Read the
JSON; send the user the HTML. `--json` prints the result instead of the summary.

## Rules Kit enforces, and you keep

- **Glyphs packages**: close the font in Glyphs first (through the Glyphs MCP, refusing if it has unsaved edits; ask the
  user to save), `kit snapshot --reason R`, write, then `kit diff` against the snapshot. Never delete glyphs. Never
  discard the user's unsaved edits.
- Read-only sources (archives, font libraries, installed fonts, Downloads) are never written to.
- A reference font is a witness, not a target: report a difference as a question, lead with the glyph's own family.

## When Kit can't answer it yet

Use the library in a few lines of Python (`from kit import font, geom, report`; see `Kit/docs/library.md`) rather than
a standalone script in a project. If the question comes back, add a command: module plus `kit/commands/<group>.py`
with `register(subparsers)`, a golden test against any script it replaces, a line in docs/commands.md and the cookbook.
Ideas already harvested from retired scripts, by module: the workspace's `.toolkit-survey/harvest/ideas-by-module.md`.

## Verify

`PYTHONPATH=Kit .venv/bin/python -m unittest discover -s Kit/tests` from the workspace root. Tests read a frozen
fixture (`tests/make_fixtures.py`), never the live package.
