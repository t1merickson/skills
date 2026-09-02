---
name: second-loop
description: Set up a privacy-aware, human-gated improvement loop for repeated outbound work where outcomes are sparse and sending remains human.
---

# Second loop

The first loop chooses, drafts, sends, and observes. This skill builds a second loop that proposes small changes to the first. It never sends, submits, publishes, buys, or contacts anyone.

## Confirm the regime

Use this shape when outcomes are slow, scarce, socially costly, or confounded: applications, pitches, client outreach, and similar work. If ground truth is cheap and safely automated, use ordinary tests or optimization instead.

At small sample sizes, reasons and qualitative failures usually carry more signal than response-rate movement. Always report denominators, avoid significance theater, and allow “insufficient evidence; no change” as the expected result.

## Establish governance first

Interview for target-selection judgment, message strategy, non-negotiable ethics/identity constraints, cheap pre-send checks, outcome capture, review cadence, and an exploration policy the user is comfortable with. Then define:

- data minimization, redaction, local storage, retention/deletion, and who may read the ledger;
- a stable baseline and frozen evaluation fixtures;
- likely confounders such as season, channel, audience, offer, sender reputation, and market changes;
- a kill switch for harmful, embarrassing, high-volume, or identity-drifting proposals;
- one human approval point before any playbook change becomes live.

Use [references/scaffold.md](references/scaffold.md) as a starting contract, not a mandatory directory tree.

## Five pieces

1. **Law:** scope, editable files, evidence requirements, privacy/retention, never-do rules, and the kill switch.
2. **Ledger:** append-only outcomes captured promptly, with event time, play/version, target pseudonym or minimal identifier, outcome, and reason. Validate entries.
3. **Gate:** cheap deterministic checks plus frozen examples of the user's routing judgment. Preserve a baseline result before tuning.
4. **Lane:** one attributable concept per proposal. Record contextual changes that could confound it.
5. **Merge:** a human reviews the diff, cited ledger rows, privacy impact, baseline/gate result, and rollback before approving or rejecting.

Exploration can reduce policy blindness, but there is no universal percentage. Choose a small, ethical budget with the user; never turn it into unsolicited volume.

## Cadence

On each review cycle:

1. read the law, retained ledger, current configuration, baseline, and recent confounder log;
2. propose at most one change supported by specific evidence;
3. run cheap checks and frozen fixtures before and after;
4. reject or roll back flat, harmful, privacy-expanding, or voice-changing proposals;
5. present the diff and evidence for human decision;
6. record approval/rejection and the version used by later sends.

Run initial cycles manually. Automation may prepare a proposal only after the loop is predictable; it never removes human review or human sending.

## Load-bearing rails

- Never fabricate experience, credentials, metrics, relationships, or personalization.
- The user's voice and ethical boundaries are not tunable variables.
- Sending stays human and volume remains explicitly bounded.
- One concept changes at a time; preserve a direct rollback.
- Do not retain full message bodies or recipient identity when derived features and pseudonyms are enough.
- Stop when evidence is thin, drift is detected, or the user cannot comfortably inspect what the loop is learning.
