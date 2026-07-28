# Second-loop scaffold — file templates

Instantiate per-domain during the interview. Rename freely; keep the contracts. Run everything offline with sample data first — the loop proves itself on local files before it touches anything real.

## Repo tree

```
<name>-second-loop/
  AGENTS.md               # the law — read by the improver before anything else
  config/
    scoring.yaml          # targeting judgment, externalized
    plays.yaml            # message judgment, externalized
  plays/
    <play_name>.md        # one file per play: the actual template/instructions
  memory/
    outcomes.jsonl        # the ledger — append-only, validator-guarded
  evals/
    fixtures.yaml         # frozen human judgment: cases + expected routing
    gate.py               # one command → one number; exit 0 only on pass
    checks/               # cheap tier: pre-send automatic checks (domain-specific)
  scripts/
    log_outcome.py        # the capture habit — one command, validates, appends
    weekly_tune.sh        # the cadence
  outputs/                # improver summaries land here
```

## AGENTS.md — the law

```markdown
# <Name> Second Loop — Rules

You improve a <domain> playbook from logged outcomes. You do not run it.

Hard rules (never editable by you):
- Never send, submit, or publish anything.
- Never fabricate: no invented experience, credentials, metrics, or personalization.
- Never edit this file, evals/fixtures.yaml, or anything outside this repo.
- The user's voice is not a tunable. Emphasis, structure, targeting — yes. Identity — no.
- One concept per proposal. One weight, or one play edit, or one banned line. Never mixed.
- Every proposal cites specific rows from memory/outcomes.jsonl.
- Cite no rate from a base under 20 without stating the base.
- Under ~30 outcomes for the thing you're changing: justify by reasons (the text), not rates.
- Run evals/gate.py before and after. Flat or worse → revert and stop.
- "No change this week" is a valid result. Thin data → say so, propose nothing.

Allowed edits:
- config/scoring.yaml
- config/plays.yaml
- plays/*.md

Required output (outputs/proposal.md):
- the exact change (diff)
- the outcome rows that motivated it
- gate score before / after
- risk, and what the human reviewer should check
- do not claim the change is live
```

## config/scoring.yaml

```yaml
signals:
  <signal_key>:            # e.g. reposted_role / engaged_with_content
    weight: 6
    reason: "<one line: why this predicts worth-the-effort>"
  # ~5 signals total. Small enough to argue with.

negative_signals:
  <bad_fit_key>: -8        # e.g. ghost_job_tells / freebie_seeker

thresholds:
  full_effort: 10          # top lane: custom artifact, real time
  standard: 6              # normal play
  # below standard → skip (and see exploration lane)

exploration:
  rate: 0.2                # ~1 in 5 sends deliberately breaks these rules
  log_as: "exploration"    # logged identically — the ledger must know
```

## config/plays.yaml

```yaml
plays:
  <play_name>:
    file: plays/<play_name>.md
    use_when: [<signal_key>, ...]
    banned_lines:
      - "<phrase the user already knows is dead>"
      - "<fake-personalization pattern>"
```

## memory/outcomes.jsonl — the ledger

One line per send, written when the outcome is known. `reason` is mandatory and is the whole point.

```json
{"date":"YYYY-MM-DD","target":"<who/what>","signals":["<key>"],"play":"<play_name>","score":8,"lane":"standard|exploration","outcome":"<stage>","reason":"<why, while it's fresh>"}
```

Outcome vocab is domain-specific but closed (validator rejects unknowns). Job hunt: `screen | interview | offer | rejection | ghost`. Outreach: `reply | call_booked | client | no_reply | bad_fit | bounced`. Staged outcomes get one line per stage transition — "rejected post-screen: wanted agency experience" is a targeting datum, not a failure.

`scripts/log_outcome.py`: accepts the fields as args, rejects missing fields / unknown outcomes / empty reason / future dates, appends, echoes the row. Make it one command with no ceremony — a ledger that needs Friday memory is a ledger of fiction.

## evals/ — the gate, two tiers

**Cheap tier (`evals/checks/`)** — automatic, pre-send, per-artifact. Find these in the interview; every domain hides some:
- job hunt: parses cleanly as plain text (ATS), covers the posting's required keywords, one page, no fabricated claims vs. a canonical facts file
- outreach: names something real about the recipient, under N words, contains no banned_lines, has exactly one ask

**Judgment tier (`evals/fixtures.yaml` + `gate.py`)** — frozen human routing decisions:

```yaml
cases:
  - target: "<real-ish example>"
    signals: [<key>, <key>]
    expected: full_effort | standard | skip
    note: "<why the human says so>"
  # Include ugly cases: weak signals, bad fits, the ones you wish you'd skipped.
  # A fixture file of obvious wins lets every reckless change pass.
```

`gate.py`: sum weights + negatives, route by thresholds, compare to expected, print each case, print `score=0.00–1.00`, exit 0 only at 1.00. Small enough to read; sharp enough to catch a real miss.

## The improver prompt

```markdown
Read AGENTS.md and obey it. Read config/, memory/outcomes.jsonl, evals/fixtures.yaml.

Find the ONE change most supported by the ledger — a weight, a threshold,
a play edit, or a banned line. Prefer the smallest edit that fixes a known miss
over the biggest story. Reasons outrank rates at this N.

Make the edit. Run evals/gate.py before and after.
Improved → write outputs/proposal.md per the law's required output.
Flat or worse → revert, and write outputs/proposal.md explaining what you
tried, why the gate rejected it, and what data would settle it.
```

## scripts/weekly_tune.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 evals/gate.py || true          # baseline, may be failing — that's information
<agent> exec "$(cat prompts/improve.md)"   # codex exec / claude -p / any capable agent
python3 evals/gate.py
cat outputs/proposal.md                 # human reads THIS, then merges or rejects
```

Cadence: weekly. Run the first two cycles by hand and read everything the improver attempts — schedule it only once the proposals are boring. If using git: improver commits to a branch, human merges; the merge IS the approval. No git? The human applies the diff from proposal.md by hand — slower, same control point.

## Failure modes to warn the user about at setup

- **Backfilled outcomes.** Logged Friday-from-memory → the system learns fiction. The capture habit is load-bearing.
- **Fixture rot.** The gate encodes last month's judgment; when the user's judgment moves, the fixtures must move with it — reviewing them monthly is part of the cadence.
- **Junk-drawer config.** Twenty signals and exception rules → the improver overfits. Start at five; let outcomes argue for the sixth.
- **The skipped review.** One un-reviewed merge "because it's boring now" is how drift starts. Boring proposals are the system working.
- **Shadow blindness.** No exploration lane → the loop can only reweight choices it already makes, and never learns what the skipped targets would have said.
