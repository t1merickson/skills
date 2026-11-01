# N0 — Intake, Interview & Canonicalization

<!-- Instantiate this template as ~/.claude/obsessions/<yyyy-mm-dd>-prediction-<slug>/00-INTAKE.md.
     Guidance appears in blockquotes (>) — replace it with content; do not leave guidance text in the finished file.
     This file is also the run's living index: the fact register at the bottom is APPENDED TO by later nodes. -->

**Run:** `{{slug}}` · **Date:** {{YYYY-MM-DD}} · **Analyst mode:** {{reasoning-first | research}} · **Depth:** {{full | compact}}
**Attended:** {{yes/no — if no, note that defaults were chosen and stated rather than asked}}

## 1. Verbatim capture

> Paste the prediction exactly as the user gave it — the whole message, thread, or transcript excerpt. Resist cleaning it up: the original wording is evidence (N9 will need it to check for definitional drift, N11 to verify the verdict answers what was actually asked). If the prediction arrived across multiple messages, capture all of them with attribution.

{{verbatim text}}

## 2. Canonical claim register

> One row per distinct claim, including implicit claims that do argumentative work (universal "laws," offered mechanisms, evidence-claims). Splitting generously is better than lumping: N2 can merge, but a claim never registered is never scored. The resolution criterion must be FUNCTIONAL (observable behavior, shares, mechanisms-in-use) — never names or vibes. If you had to invent the criterion, that's normal; flag it and defend the choice in §4. Finalize this register only AFTER the interview in §3.

| ID | Claim (canonical restatement) | Horizon | Resolution criterion (functional) | Shape(s) | Origin |
|----|-------------------------------|---------|------------------------------------|----------|--------|
| C1 | {{...}} | {{year/range}} | {{observable that settles it}} | {{shape(s) from SKILL.md table}} | {{explicit / implicit}} |
| C2 | {{...}} | | | | |

## 3. Pre-tree interview record

> The questions put to the user BEFORE the tree took shape, and their answers, verbatim — plus one line per answer on how it changed the canonicalization, definitions, or node plan. Ask only tree-changing questions (horizons, intended meanings, scope priority, stipulate-vs-verify, depth, purpose/stakes, optionally the user's own stance and preferred outcome). Binding rules apply: meanings/horizons/scope answers BIND; asserted facts → register rows marked assumed-from-user; stated preferences bind NOTHING and are recorded here for N10's residue disclosure. If unattended: record each default chosen in place of an answer, and why it was the reasonable reading.

| # | Question asked | Answer (verbatim) | What it changed |
|---|----------------|-------------------|-----------------|
| Q1 | {{...}} | {{...}} | {{claim register / definition / node plan / nothing}} |

**User's stated stance / preferred outcome (binds nothing; for N10 §5):** {{... or "not asked / not given"}}

## 3b. Braindump (before any research)

> Written BEFORE any web search or fetch, in either analysis mode. Everything already known that bears on the claim — fast, dense, unpolished. Mark each claim inline: ✓ know it cold · ? verify this · ✗ known blank spot. Suspicious fluency gets a ?. The marks seed the fact register in §7, and in research mode the ?s and ✗s are the search agenda.

{{braindump}}

## 4. Definitional work

> For every vague predicate in the original: the definition fixed (the user's choice where they made one, marked as such), the plausible alternatives rejected, and one sentence defending the choice. Do this BEFORE forming any view of the verdict — a definition chosen after you know which answer you like is anti-pattern #13's seed. If a definition choice by itself predetermines a verdict, say so here in bold: that is a finding.

- **"{{predicate}}"** fixed as: {{definition}} ({{user-chosen / analyst-chosen}}). Rejected: {{alt}} because {{reason}}.

## 5. Shape diagnosis & node plan

> Diagnose each claim's shape(s) against SKILL.md's adaptation table, then commit the node plan: which nodes run expanded and why, plus anything consciously de-emphasized. This section is the written answer to "how many nodes does this question require" — N11's node accounting will grade it against what actually happened.

| Node | Runs as | Why |
|------|---------|-----|
| N0–N11 | {{standard / expanded / compact-section}} | {{one line each; expansions justified by claim shape}} |

## 6. Mode & scoping decisions

> Everything settled with (or on behalf of) the user beyond the interview table: modes, depth, deadline, any constraint on scope. If unattended: each default chosen and why.

## 7. Fact register (living — appended by all nodes)

> Every factual claim the analysis leans on, from any node, gets a row AT THE TIME IT IS FIRST RELIED ON. Status values: `verified` (checked against a source this run — research mode), `assumed-from-user` (user supplied or stipulated), `model-recall-unverified` (from internal knowledge, unchecked). "Assume the facts are correct" means marking rows assumed-from-user — it does not mean skipping rows. The Used-by column is what lets N10 and N11 trace which verdicts inherit which assumptions.

| # | Fact | Status | Confidence | Used by | Notes |
|---|------|--------|------------|---------|-------|
| F1 | {{...}} | {{status}} | {{low/med/high}} | {{node(s)}} | {{...}} |

## 8. Open questions carried forward

> Anything unresolved at intake that a later node must settle, each tagged with the node expected to settle it.

<!-- REVISED blocks: if any later node forces a change to this file (a claim re-canonicalized,
     a definition re-fixed, a promoted implicit claim), append below — never edit silently:

## REVISED — {{date, forcing node}}
What changed: ... · What forced it: ... · Downstream effects: ...
-->
