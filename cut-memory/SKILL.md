---
name: cut-memory
description: Audit the session's memory files and cut everything the codebase or CLAUDE.md already records. Assumes memory is mostly bloat.
---

# cut-memory

A pass over the auto-memory directory that defaults to **cutting**, not tidying. Derived from a consolidation workflow that assumed stored memories were valuable and needed merging; the assumption here is inverted, because in practice most of them restate something the agent can already read.

**The premise: the codebase is the memory.** Code, structure, git history, README, the skills repo, agent definitions — all of it is on disk and re-reads in seconds. CLAUDE.md is a deliberately designed file that already carries the user's preferences, rules, and identity, and it loads in every session. A memory file duplicating any of that is pure overhead: it costs context on every recall and drifts out of sync with the thing it describes.

Start from "this is bloat" and make each file earn its place.

## Know the scope first

Auto-memory is **per working directory** — `~/.claude/projects/<encoded-cwd>/memory/`. There is no account-wide memory directory. A session in a different folder reads a different set and never sees this one.

That matters for the most common bad entry: notes about global config, the user's working style, or agent behavior, filed in a directory scoped to one folder. Those either belong in CLAUDE.md (which is the account-wide layer) or nowhere. Cut them from memory; if a rule genuinely needs to be global, say so and let the user decide whether it goes in CLAUDE.md.

## Phase 1 — Take stock

List the directory, read `MEMORY.md`, read every file. Note overlaps and anything that looks dated.

## Phase 2 — Apply the test

For each file, one question: **does CLAUDE.md, the codebase, or any other file on disk already carry this?** If yes, cut it. Verify rather than assume — grep CLAUDE.md, check whether the referenced skill/agent/config still exists, confirm the fact is still true. Stale memories are common and a corrected one is often better cut than fixed.

A file survives only if all three hold:

1. **It changes behavior.** Interesting context that alters nothing is not a memory.
2. **It is recorded nowhere else.** Not in CLAUDE.md, not in a repo, not in an agent definition, not re-derivable with one command.
3. **The default would be wrong without it.** The strongest keeps are silent traps and facts about the agent's own runtime — things that would be confidently gotten wrong, not just unknown.

Cut regardless of the three: reports and one-off task output, motives behind rules that CLAUDE.md already states, notes explaining an artifact that sits next to that artifact, and lists that re-derive from a single command.

Cutting to zero files is a valid outcome. Say so plainly rather than keeping a token few.

## Phase 3 — Tidy the index

Rewrite `MEMORY.md`: one line per surviving file, `- [Title](file.md) — one-line hook`. Remove pointers to cut files. Do not summarize cut content into the index — that reintroduces the bloat one level up.

## Rules

- **Quarantine, never delete.** Move cut files to a dated sibling directory and report the one-line undo. The user may disagree with a call.
- **Verify before cutting for staleness.** "This is out of date" is a claim; check it.
- **Do not merge to look tidy.** Two files that sound like one topic but carry different rules stay separate. Losing precision for a smaller file count is a bad trade.
- **Do not mirror memory into other agents' config.** Another agent's instruction file is not a backup location, and content ported there becomes noise nobody maintains. Report that a mirror exists or has gone stale; leave the decision to the user.
- **No invented findings.** If nothing overlapped, say nothing overlapped. Do not manufacture a merge or a stale fact to make the pass look productive.
- **Report per-file reasoning.** For each cut, name what already records it. That is what lets the user overrule a bad call, and it is the only way the pass is auditable.
