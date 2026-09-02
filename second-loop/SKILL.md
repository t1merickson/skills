---
name: second-loop
description: Set up a human-gated improvement loop for repeated outbound work where outcomes are sparse and sending remains human.
---

# Second loop

The first loop chooses, drafts, sends, and observes. This skill builds a second loop that edits the first: it reads outcomes, proposes one change to the playbook, and lets the human judge the evidence and merge. It never runs the first loop; sending stays human.

## Confirm the regime

Use this shape when outcomes are slow, scarce, socially costly, or confounded: applications, pitches, client outreach, and similar work. If ground truth is cheap and safely automated, use ordinary tests or optimization instead.

At personal sample sizes, response-rate optimization is mostly theater because the world shifts before significance arrives. The loop buys something more useful:

- **anti-superstition:** one lucky reply does not become a permanent rule;
- **anti-fiction:** outcomes and reasons are captured when they happen, not reconstructed from Friday's memory;
- **legibility:** judgment in a file can be argued with and versioned;
- **reason-rich evidence:** one rejection explaining why can teach more than twenty bare `no_reply` rows.

Always report denominators and allow “insufficient evidence; no change” as the expected result.

## Establish governance first

The interview is the product; the scaffold is generic until it captures the user's real tells. Work conversationally through target-selection judgment, message strategy, non-negotiable identity constraints, cheap pre-send checks, outcome capture, review cadence, and an exploration policy the user is comfortable with. Push past platitudes: “reposted twice this month” is a usable signal; “seems like a fit” is not.

Then define:

- what the ledger actually needs to retain and for how long;
- a stable baseline and frozen evaluation fixtures;
- likely confounders such as season, channel, audience, offer, sender reputation, and market changes;
- a kill switch for harmful, embarrassing, high-volume, or identity-drifting proposals;
- one human approval point before any playbook change becomes live.

Use [references/scaffold.md](references/scaffold.md) as a starting contract, not a mandatory directory tree.

## Five pieces

1. **Law:** scope, editable files, evidence requirements, ledger retention/readership, never-do rules, and the kill switch.
2. **Ledger:** append-only outcomes captured promptly, with event time, play/version, target pseudonym or minimal identifier, outcome, and reason. Validate entries.
3. **Gate:** cheap deterministic checks plus frozen examples of the user's routing judgment. Preserve a baseline result before tuning.
4. **Lane:** one attributable concept per proposal. Record contextual changes that could confound it.
5. **Merge:** a human reviews the diff, cited ledger rows, baseline/gate result, voice/identity impact, and rollback before approving or rejecting. The minute review is skipped because it feels like friction, the loop stops improving and starts drifting.

Exploration reduces policy blindness: the ledger contains only outcomes from targets the current policy selected, so without deliberate exceptions the loop can only reweight inside its own shadow. There is no universal percentage. Choose a small, explicit budget with the user; never turn it into unsolicited volume.

## Cadence

On each review cycle:

1. read the law, retained ledger, current configuration, baseline, and recent confounder log;
2. propose at most one change supported by specific evidence;
3. run cheap checks and frozen fixtures before and after;
4. reject or roll back flat, harmful, data-expanding, or voice-changing proposals;
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
