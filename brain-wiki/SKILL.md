---
name: brain-wiki
description: Distill an exported corpus (Notion, Slack, GitHub) into a source-grounded wiki.
---

# brain-wiki

turn a raw export into a wiki future sessions can actually use. the phases below matched across shay-brain and roots-brain, months apart; keep the order, it's load-bearing.

## phases

1. **survey and sort.** walk the export. separate CONTENT (docs, decisions, knowledge) from OPERATING MATERIAL (scripts, configs, templates). map what's there before distilling anything; report the map to timmy with a page-count estimate before phase 2.
2. **distill with subagents.** fan out sonnet subagents, each owning one content area, each producing wiki pages. every claim on a page cites its source file. pages are dense and factual: what is true, who decided, when, where it's written down. no filler, no invented connective tissue.
3. **adversarial fact-check.** a second wave of subagents, each checking a different area than the one that wrote it: verify every claim against the cited source. this pass is MANDATORY — the first shay-brain run produced real fabrications, and this pass is what caught them. findings get fixed, not footnoted.
4. **augment source by source.** next corpus (Slack after Notion, GitHub after Slack, codebase last) folds into the same wiki: new pages where new topics appear, edits where a source contradicts or extends an existing page. contradictions between sources get surfaced to timmy, not silently resolved.

## structure

- one directory per wiki, an `INDEX.md` at the root listing every page with a one-line hook. the index is the entry point for future sessions; keep it current as pages land.
- pages link to each other and to sources. a page nobody can reach from the index doesn't exist.
- keep an `OPEN-QUESTIONS.md`: what the corpus doesn't answer, what contradicts, what looks stale. empty is a valid state; invented entries are not.

## rules

- subagents distill and check; only you merge. one writer per file, always.
- never quote private content into commit messages or anything that could leave the repo.
- report per phase, payload first: "phase 2 done: 34 pages from Notion, 3 areas thin on sources. next: fact-check wave." wait for timmy's go between phases on the first corpus; later corpora can run heads-down if he says so.
