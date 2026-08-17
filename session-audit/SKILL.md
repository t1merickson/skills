---
name: session-audit
description: Audit timmy's Claude Code transcripts with subagents to find repeated corrections, repeated workflows, and per-model failure modes — evidence for CLAUDE.md and skill changes. Use when timmy says "run the audit", "audit my sessions", "what keeps going wrong", or after a major new model release.
---

# session-audit

config lines should come from data, not vibes. this skill turns transcript history into a ranked list of what to change.

## the sweep

transcripts live in `~/.claude/projects/*/` as .jsonl files, one JSON object per line. user messages are lines where `.message.role == "user"` with typed-text content; assistant lines usually carry a model field. schemas drift, so each agent inspects one file before parsing at scale.

launch three sonnet subagents, read-only, each over the ~25 most recently modified transcripts:

1. **corrections**: complaints and redirections timmy repeats ("too long", "no, i meant", "stop", "undo", instructions retyped across sessions). cluster, count, quote.
2. **workflows**: multi-step flows he re-explains each session — candidate skills. name, session count, projects, one-line shape.
3. **failure modes**: incidents where his next message signals the model got it wrong, classified (overbuild, verbosity, wrong interpretation, broke something, stopped early, didn't verify, invented content), broken down by model where the transcript says.

subagents are read-only. no writes, no deletes, and they never quote anything private back beyond short correction snippets.

## turning findings into changes

- a correction repeated 3+ times across sessions earns a CLAUDE.md line, written in the file's register.
- a workflow appearing in 3+ sessions earns a skill, or a line in that project's CLAUDE.md if it's project-shaped.
- a failure mode concentrated in ONE model earns nothing permanent: note it in memory and route around that model, because model-specific patches rot when the model updates.
- below those thresholds: report it and let timmy decide. never pad the file with one-off fixes.
- also run the reverse pass: any existing CLAUDE.md line the transcripts show never firing, or always being followed anyway, is a deletion candidate.

## cadence

quarterly, or after each major model release, or when timmy's corrections feel like they're repeating. report findings ranked by frequency × pain, with counts and short quotes as evidence. changes to CLAUDE.md or skills happen only after timmy approves them.
