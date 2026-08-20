---
name: brain-wiki
description: Distill an exported corpus (Notion, Slack, GitHub) into a source-grounded wiki.
---

# brain-wiki

Turn a raw export into a wiki future sessions can actually use. The phases below matched across two independent corpus builds, months apart; keep the order, it's critical.

## Phases

1. **Survey and sort.** Walk the export. Separate CONTENT (docs, decisions, knowledge) from OPERATING MATERIAL (scripts, configs, templates). Map what's there before distilling anything; report the map to the user with a page-count estimate before phase 2.
2. **Distill with subagents.** Fan out Sonnet subagents, each owning one content area, each producing wiki pages. Every claim on a page cites its source file. Pages are dense and factual: what is true, who decided, when, where it's written down. No filler, no invented connective tissue.
3. **Adversarial fact-check.** A second wave of subagents, each checking a different area than the one that wrote it: verify every claim against the cited source. This pass is MANDATORY — the first real run produced actual fabrications, and this pass is what caught them. Findings get fixed, not footnoted.
4. **Augment source by source.** Next corpus (Slack after Notion, GitHub after Slack, codebase last) folds into the same wiki: new pages where new topics appear, edits where a source contradicts or extends an existing page. Contradictions between sources get surfaced to the user, not silently resolved.

## Structure

- One directory per wiki, an `INDEX.md` at the root listing every page with a one-line hook. The index is the entry point for future sessions; keep it current as pages land.
- Pages link to each other and to sources. A page nobody can reach from the index doesn't exist.
- Keep an `OPEN-QUESTIONS.md`: what the corpus doesn't answer, what contradicts, what looks stale. Empty is a valid state; invented entries are not.

## Rules

- Subagents distill and check; only you merge. One writer per file, always.
- Never quote private content into commit messages or anything that could leave the repo.
- Report per phase, payload first: "Phase 2 done: 34 pages from Notion, 3 areas thin on sources. Next: fact-check wave." Wait for the user's go between phases on the first corpus; later corpora can run heads-down if they say so.
