---
name: standup
description: Reconstruct project status and next actions from checkpoints, Git, and durable project instructions within an explicitly chosen scope.
---

# Standup

Use this skill only when invoked. The working directory supplies the first scope candidate; do not turn a status request into an unbounded scan of the machine.

## Choose scope

- **Project root:** report that project in depth.
- **Container with several projects:** inventory one level down, report the count, and cover each discovered project unless the user narrows it.
- **Generic directory:** ask which project root or configured project registry to use. Do not guess personal development roots.

If discovery produces an unexpectedly large set, show the count and roots before a deep read. Recency orders the report; it does not silently exclude quiet projects.

## Gather read-only evidence

For each project:

1. Relevant unarchived `.checkpoints/` files and a legacy `CHECKPOINT.md`, if present.
2. Current branch, last meaningful commit and date, ahead/behind state, and `git status --porcelain`.
3. AGENTS.md, CLAUDE.md, or the opening of README when nothing else explains the project.

Do not fix, clean, commit, or invent a next step during gathering.

## Report

For a container, give one entry per project: name, last activity, plain-language state, recorded next step, and a visible dirty-worktree marker. For one project, include current phase, recent changes, live plates, contradictions between checkpoint and repository, and the best-supported next action.

Payload first. “No recorded next step” is valid. Recommend the hottest supported thread when one is obvious, then let the user choose what to resume.
