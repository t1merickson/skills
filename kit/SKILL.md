---
name: kit
description: Operate Kit, the font-project toolkit (`kit` CLI): audit drawn glyphs, weigh strokes against a reference, check glyph-set and language coverage, diff packages, inspect glyphs, write Bench views. Use for any measuring, checking or reporting on fonts in a workspace that has Kit, before writing a new script.
---

# Kit

Kit is one CLI and Python library for a type-design workspace (`Developer/Fonts`): every font project reads fonts,
measures, checks and reports through it. Its docs live with it: `Kit/README.md`, `Kit/docs/cookbook.md` (which command
answers which question), `Kit/docs/commands.md`, `Kit/docs/library.md`, and `Kit/DESIGN.md` (the contract). Read the
cookbook first; read DESIGN.md before changing Kit.

## Run it

From inside a project (Kit finds the nearest `kit.toml`): `.venv/bin/kit <command>`. The project's `kit.toml` supplies
the font, the reference, the output folder and the rules, so most commands need no arguments.

| Need | Command |
|---|---|
| check drawing against the project's rules | `kit audit` (prints new / fixed / same since the last run) |
| stroke weight and contrast at chosen spots | `kit weigh` |
| what's built, waiting, left to draw; what to draw first | `kit coverage` |
| language support today and once drawn | `kit languages` |
| what changed between two versions | `kit diff BEFORE AFTER` |
| one glyph's points, components, hints | `kit inspect FONT GLYPH` |
| fonts by name, with license | `kit fonts` |
| a comparison in the Bench app | `kit view NAME --title T --src id=font ...`, then `kit retire NAME` once settled |

Each report writes `report.html` for the user and `report.json` for you, side by side in `<out>/<command>/`. Read the
JSON; send the user the HTML. `--json` prints the result instead of the summary.

## Rules Kit enforces, and you keep

- **License rules live in `Kit/fonts.toml`.** A `measure-only` font may be measured in memory for numbers. Never cache,
  export, draw, trace or build from its outlines, by Kit or by hand.
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
