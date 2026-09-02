---
name: session-audit
description: Audit Claude transcript history for repeated corrections, recurring workflows, and model-specific failures using a deterministic local extraction before judgment.
---

# Session audit

Use this skill only when invoked. Transcript history is private evidence, not content to publish or quote at length.

## Extract deterministically

Inspect one recent transcript to confirm the current schema, then use [scripts/extract_transcripts.py](scripts/extract_transcripts.py) to produce a bounded local corpus:

```bash
python3 scripts/extract_transcripts.py --limit 25 > /tmp/session-audit.jsonl
```

The extractor reads only, hashes source paths, and keeps messages in chronological order. Store its output in a temporary or user-approved local location. Never commit it.

## Review three lenses

1. **Corrections:** repeated complaints, redirects, reversals, and instructions the user had to restate.
2. **Workflows:** multi-step work repeatedly explained from scratch; candidates for a skill or project instruction.
3. **Failure patterns:** the user's next message signals overbuilding, verbosity, wrong interpretation, breakage, premature stopping, missing verification, or invention. Preserve model/version and date when present.

Use independent review lanes only when delegation is available and authorized; otherwise review the lenses sequentially. Short snippets may support a finding, but do not reproduce private conversations in the report.

## Turn evidence into proposals

Rank findings by frequency, pain, and recency. Counts inform judgment rather than imposing an automatic threshold. Route each proposed change:

- always-relevant working contract → CLAUDE.md;
- project-specific convention → project instructions;
- on-demand repeated workflow → skill;
- failure isolated to one model generation → temporary routing or model note, not a permanent universal rule.

Run the reverse pass too: standing instructions that never affect behavior, duplicate stronger rules, or patch an obsolete model are deletion candidates.

Do not edit configuration during the audit. Present the evidence, proposed destination, and expected behavioral change; apply only after approval.
