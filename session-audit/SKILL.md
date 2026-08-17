---
name: session-audit
description: Audit transcripts with subagents for repeated corrections, workflows, and per-model failures.
---

# session-audit

config lines should come from data, not vibes. this skill turns transcript history into a ranked list of what to change.

## the sweep

transcripts live in `~/.claude/projects/*/` as .jsonl files, one JSON object per line. user messages are lines where `.message.role == "user"` with typed-text content; assistant lines usually carry a model field. schemas drift, so each agent inspects one file before parsing at scale.

launch three sonnet subagents, read-only, each over the ~25 most recently modified transcripts:

1. **corrections**: complaints and redirections the user repeats ("too long", "no, i meant", "stop", "undo", instructions retyped across sessions). cluster, count, quote.
2. **workflows**: multi-step flows they re-explains each session — candidate skills. name, session count, projects, one-line shape.
3. **failure modes**: incidents where their next message signals the model got it wrong, classified (overbuild, verbosity, wrong interpretation, broke something, stopped early, didn't verify, invented content), broken down by model where the transcript says.

subagents are read-only. no writes, no deletes, and they never quote anything private back beyond short correction snippets.

## turning findings into changes

- a correction repeated 3+ times across sessions earns a CLAUDE.md line, written in the file's register.
- a workflow appearing in 3+ sessions earns a skill, or a line in that project's CLAUDE.md if it's project-shaped.
- a failure mode concentrated in ONE model earns nothing permanent: note it in memory and route around that model, because model-specific patches rot when the model updates.
- below those thresholds: report it and let the user decide. never pad the file with one-off fixes.
- also run the reverse pass: any existing CLAUDE.md line the transcripts show never firing, or always being followed anyway, is a deletion candidate.

## cadence

quarterly, or after each major model release, or when the user's corrections feel like they're repeating. report findings ranked by frequency × pain, with counts and short quotes as evidence. changes to CLAUDE.md or skills happen only after the user approves them.
