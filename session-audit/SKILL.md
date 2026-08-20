---
name: session-audit
description: Audit transcripts with subagents for repeated corrections, workflows, and per-model failures.
---

# session-audit

Config lines should come from data, not vibes. This skill turns transcript history into a ranked list of what to change.

## The sweep

Transcripts live in `~/.claude/projects/*/` as .jsonl files, one JSON object per line. User messages are lines where `.message.role == "user"` with typed-text content; assistant lines usually carry a model field. Schemas drift, so each agent inspects one file before parsing at scale.

Launch three sonnet subagents, read-only, each over the ~25 most recently modified transcripts:

1. **Corrections**: complaints and redirections the user repeats ("too long", "no, i meant", "stop", "undo", instructions retyped across sessions). Cluster, count, quote.
2. **Workflows**: multi-step flows they re-explain each session — candidate skills. Name, session count, projects, one-line shape.
3. **Failure modes**: incidents where their next message signals the model got it wrong, classified (overbuild, verbosity, wrong interpretation, broke something, stopped early, didn't verify, invented content), broken down by model where the transcript says.

Subagents are read-only. No writes, no deletes, and they never quote anything private back beyond short correction snippets.

## Turning findings into changes

- A correction repeated 3+ times across sessions earns a CLAUDE.md line, written in the file's register.
- A workflow appearing in 3+ sessions earns a skill, or a line in that project's CLAUDE.md if it's project-shaped.
- A failure mode concentrated in ONE model earns nothing permanent: note it in memory and route around that model, because model-specific patches rot when the model updates.
- Below those thresholds: report it and let the user decide. Never pad the file with one-off fixes.
- Also run the reverse pass: any existing CLAUDE.md line the transcripts show never firing, or always being followed anyway, is a deletion candidate.

## Cadence

Quarterly, or after each major model release, or when the user's corrections feel like they're repeating. Report findings ranked by frequency × pain, with counts and short quotes as evidence. Changes to CLAUDE.md or skills happen only after the user approves them.
