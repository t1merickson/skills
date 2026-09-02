---
name: obsess-hero
description: Build a bounded, source-accounted vault about one public person's work and documented thinking. Use only when explicitly invoked with a named person.
---

# Obsess hero

One person per run. This composes `obsess` for recall/research, `offline-archive` for permitted capture, and `brain-wiki` for typed pages. Read those skills when their phase begins. Follow `obsess`'s mile-marker protocol throughout the run, including its default pause between bounded research pulls.

## Resolve scope and root

Disambiguate the person before creating files. Agree on angle, breadth, time/request/storage budget, stopping condition, and vault root. Use an existing configured hero root when the user has one; otherwise prefer a project-local `heroes/<person-slug>/` or ask. Do not hard-code a machine-specific library.

“Brief” means one prioritized research pull and an explicit frontier. “Deep” means offering additional bounded paths toward the agreed coverage target; it does not authorize them or waive the pause between pulls. It never promises completeness.

For living people, include published work, on-record statements, and reputable biographical context relevant to the work. Exclude private addresses, family details without public relevance, current movements, private records, rumor, and sensitive aggregation. Public availability alone does not make invasive synthesis appropriate.

## Vault layout

```text
<vault>/
  00-braindump.md
  NOTES.md
  SHAPE.md
  INDEX.md
  LEDGER.md
  FRONTIER.md
  OPEN-QUESTIONS.md
  wiki/<object-slug>.md
  sources/<capture-slug>/SOURCE.md
```

Read [references/vault-contract.md](references/vault-contract.md) for types, fields, relationships, source admission, and ledger states. Copy the actual contract into `SHAPE.md` so the vault remains self-describing.

Every captured source directory has provenance and exactly one owning wiki page with `local_path`. Slugs are shared across vaults only when the selected root is intentionally opened and governed as one cross-person library; otherwise keep the namespace local.

## Research

Write a dated braindump before searching, marking dates, titles, influence claims, and quotations for verification. Existing vaults are augmented, not restarted: reread their index, frontier, ledger, and relevant holdings before fetching more.

Make the initial route chart person-specific: distinguish paths such as works census, primary works, interviews and documented thinking, biography/context, reception/influence, and recent delta only when they are relevant. Alongside `obsess`'s fields, estimate capture/storage work and vault-writing cost. Prefer a few high-yield alternatives over an exhaustive tree.

Build a works hypothesis, then verify each entry. Prioritize the person's own work and words, followed by long-form interviews, serious criticism/biography, and reference sources. A title, quote, attribution, life date, price, current status, or influence claim never graduates on confidence alone.

Record each unfollowed lead in `FRONTIER.md` with origin, importance, estimated next-pull cost, status, and reason stopped. Record contradictions and missing evidence in `OPEN-QUESTIONS.md`. Notes say what evidence changed, not merely what a source contains.

Acquire only legitimate, useful copies within scope. Never bypass paywalls/DRM, pirate, purchase without approval, or treat a photograph of a work as the work itself. Capture public pages through `offline-archive`; store source URL, author/creator, retrieval date, license/rights note, transformations, and integrity hash. Apply `file-batch-safety` to large acquisitions.

## Write and verify

Serialize only claims the task inspected. Additional writers or reviewers are optional and require available, authorized parallel work; one writer owns each file. The primary task owns the hero synthesis, shape, index, ledger, and final evidence judgment.

Regenerate the ledger from Work pages using a vault-local script. Run this skill's read-only verifier:

```bash
python3 <skill-directory>/verify_vault.py <vault>
```

Also verify quotations/dates against sources and replay web captures with the network blocked. A layout pass cannot prove claim truth. Fix findings or keep them visibly unresolved.

## Return and maintain

At every mile marker, report the person, selected path, coverage gained, actual observable spend, held versus merely identified works, major corrections, changed frontier, and the next route choices; then pause unless the user authorized an uninterrupted bounded run. At the final return, also report the full scope, pulls completed, coverage by source/work type, open questions, verifier result, stopping reason, and storage consumed. Then teach from sourced pages, distinguishing evidence from synthesis.

The vault is durable, not scratch. Never sweep or merge hero roots casually. Republishing, sharing, or hosting is a separate rights decision.
