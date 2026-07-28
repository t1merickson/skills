---
name: second-loop
description: Interview-driven setup of a human-gated improvement loop for any repeated "send things into the world" task — job applications, client outreach, pitches, proposals, grant submissions. The agent interviews the user to externalize their judgment into versioned config, sets up an outcomes ledger with reasons, an eval gate, and a weekly cadence where the agent proposes ONE evidenced change and the human approves it. Use when the user wants to "systematize my job hunt", "make my outreach improve from outcomes", "set up a self-improving loop for X", "build a second loop", "Karpathy-loop my applications/pipeline", or describes repeatedly sending similar things (applications, DMs, pitches) and wanting to get better at it deliberately. Not for domains with cheap automatic ground truth (benchmarks, test suites) — those can run true volume search and barely need this.
---

# Second loop: a human-gated improvement loop for outbound-shaped work

The name is the design: the *first* loop is the user doing the work — pick a target, write the thing, send it, observe what happens. The *second* loop is the one that edits the first: read the outcomes, propose a change to the playbook, prove or argue for it, and let the human merge. This skill sets up the second loop. It never runs the first — **sending always stays human.**

## The regime triage (do this first)

One question decides the architecture: **is the ground truth cheap, fast, and safe to evaluate — or scarce, slow, and expensive?**

- *Cheap* (a benchmark, a test suite, a simulator): you don't need this skill's shape. That's true volume search — hundreds of mutations against an automatic gate, keep what wins. Rare in personal work. Point it out and offer the simple version.
- *Scarce* (replies, interviews, clients, acceptances — anything where each data point costs a real message to a real person and days of latency): this skill. The gate is a proxy for the user's judgment plus hard constraints, the cadence is slow, evidence is cited not proven, and a human merges every change.

Almost everything a person calls "outbound" is the second regime. Don't let the Karpathy framing seduce anyone into pretending otherwise.

## The honest premise at personal N

At 10 applications a week or 30 outreach touches a month, response-*rate* optimization is statistically meaningless — no change will reach significance before the world shifts under it. Say this to the user plainly. What the loop actually buys at this scale:

- **Anti-superstition.** Humans at N=8 overfit harder than any agent: one reply after mentioning X becomes "always mention X." A ledger with reasons, reviewed on a cadence, replaces vibes with evidence — even when the evidence is "we don't have enough yet."
- **Anti-fiction.** Outcomes backfilled on Friday from memory are fiction — wins survive, reasons blur. Logged at outcome-time with a mandatory reason, they're data.
- **Legibility.** Judgment in a file can be argued with, versioned, and improved. Judgment in a head can only be second-guessed.
- **The reasons carry the signal, not the rates.** A rejection that says why, an interview question that kept coming up, a discovery call that stalled at price — one of those is worth twenty bare `no_reply` rows. The improver conditions on the *text*, and cites rates only with the base size attached.

## The five components

Every second loop has the same skeleton (templates in [references/scaffold.md](references/scaffold.md)):

1. **The law** — a short rules file the improver reads first. Scope: which files it may edit, what it must cite, what it must never do. If it needs a table of contents, it's too long.
2. **The ledger** — `memory/outcomes.jsonl`, one line per send, written when the outcome lands, `reason` field mandatory. Built with a validator so junk can't get in.
3. **The gate** — fixtures encoding the user's judgment ("this target deserved effort; this one didn't") plus every *cheap* check the domain hides (see below). One command, one number, failures inspectable.
4. **The lane** — one concept per proposal. Never scoring and copy in the same change; never three weights at once. If two things changed, nobody knows which one worked.
5. **The merge** — the human reads the diff and the cited rows, then approves, edits, or rejects. The minute this gets skipped because review "feels like friction" is the minute the system stops improving and starts drifting.

## The interview (this is the product)

The scaffold is generic; the interview makes it theirs. Work through, conversationally, one at a time — the answers become the config files:

1. **Targeting judgment → `scoring.yaml`.** "When you decide something is worth real effort, what are you actually looking at?" Extract ~5 signals with weights and a one-line reason each. Five is a feature: small enough to argue with. Also extract negative signals — the things that make them walk away. Push past platitudes to the real tells ("reposted twice in a month" beats "seems like a good fit").
2. **Message judgment → `plays.yaml`.** What do they say, keyed to which signal? Which openers/framings do they already believe are dead? Those become `banned_lines` on day one.
3. **The never-do list → the law.** Ethics and identity constraints, non-negotiable and never editable by the improver (see rails below).
4. **The cheap sub-evals hunt.** Inside every scarce-metric domain hide checks that ARE cheap: does the artifact parse, does it cover the posting's required keywords, is it under the length that gets read, does it name the recipient's actual work. These gate automatically, pre-send, for free — find them and wire them into the gate.
5. **The exploration lane.** The ledger only ever contains the policy's own choices — you never observe the interview you'd have gotten from the role you skipped. Reserve ~1 in 5 sends for deliberate rule-breakers, logged identically. Without it the loop can only reweight inside its own shadow.
6. **The capture habit.** Design the lowest-friction way to log an outcome the moment it lands (one command, one line). A ledger that requires opening a laptop on Friday is a ledger of fiction.

## The cadence

Weekly, not per-outcome — per-outcome tuning overfits to one loud data point.

1. Improver reads the law, the ledger, the config. Proposes **one** change, citing specific rows.
2. Gate runs. Improves → the change plus evidence goes to the human as a small diff with a plain-language summary (what changed, why, which rows, what to check). Flat or worse → revert and stop; "no change this week" is a valid and common result.
3. Human merges, edits, or rejects.
4. First two cycles by hand, reading everything the improver tries — put it on a schedule only once the proposals are boring.

N-honesty rules, written into the improver's prompt: cite no rate off a base under 20 without flagging the base; below ~30 outcomes per play, justify changes by *reasons*, not rates; when the data is thin, say so and propose nothing.

## The rails (load-bearing, not boilerplate)

These go in the law verbatim, and the improver may never edit them:

- **Never fabricate.** No invented experience, credentials, or metrics on an application; no fake personalization ("loved your post" unread) in outreach. The loop tunes emphasis, structure, and targeting — never truth.
- **The voice stays theirs.** Tune which things get said, not who is saying them. If a proposed edit would make the user sound like someone else, it fails review regardless of any metric.
- **Sending stays human.** The system drafts and scores; a person sends every artifact. This is also what keeps it out of spam-cannon territory — volume automation is both counterproductive (the metric turns adversarial: optimize reply rate at scale and you train the ecosystem to filter you) and corrosive to the very signal the loop learns from.
- **One concept at a time.** Structural, not stylistic: it's what keeps every merge attributable.

## Worked shapes

**Job hunt.** Scoring signals: posting age, repost count, referral path available, keyword overlap with her actual experience, seniority match; negatives: ghost-job tells, 4th-round-take-home cultures. Plays: referral-first, cold-apply-with-artifact, hiring-manager-note. Two-tier gate: cheap tier = ATS parseability, required-keyword coverage, one-page check, runs pre-send on every artifact; scarce tier = staged outcomes (`screen`, `interview`, `offer`, `rejection`, `ghost`) each with a reason — "rejected post-screen, they wanted agency experience" is a targeting signal, not a failure. Exploration lane: one application a week that breaks her own scoring rules.

**Client acquisition (coaching).** Signals: engaged with her content, life-event markers she ethically can act on, referral source, expressed-problem match to her actual offer; negatives: freebie-seekers, peer-coaches window-shopping. Plays keyed to signals, `banned_lines` seeded with fake-personalization patterns and whatever "would love to pick your brain" energy she already hates. The gold ledger entries are discovery calls that *didn't* convert, with reasons — that text is where the improver finds which play or which audience is mismatched, at an N where rates say nothing.

## Composition

Agent-agnostic on purpose: the law is `AGENTS.md`-shaped, so Codex, Claude, or any capable agent can run the weekly tune. A nice division of labor where both are available: one agent proposes the weekly diff, a different one judges it before the human ever looks — cheap adversarial review on top of the human merge, never instead of it.
