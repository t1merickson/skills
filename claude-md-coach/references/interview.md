# Interview question bank

Questions are grouped by round and track. Ask 3–4 per round, at most 3
rounds; skip anything the conversation has already answered. Every answer
below maps to *prose you write*, not a checkbox you record — the mapping
notes say what the answer should produce, and the file should say it in the
user's chosen register, with the mechanism attached (see principles.md §7).

Follow up on surprising answers before moving to the next round. The
question behind every question is: *what would this person otherwise have to
re-explain every session?*

---

## Track A — Persona file (~/.claude/CLAUDE.md)

### Round 1 — identity and voice

**A1. How should the agent talk to you?**
- Professional and neutral
- Warm but structured
- Casual, like a sharp colleague
- Match my energy turn by turn

Mapping: sets the file's own register (write the whole file in this voice).
For the casual options, always pair with the independence clause — looseness
and rigor are separate dials, and casual must not drift into agreeable. For
"match my energy," distinguish tone-mirroring (fine) from
excitement-mirroring (ask A6 in round 2 — they may not want it).

**A2. When you're wrong about something, what should the agent do?**
- Correct me directly, lead with the flaw
- Steel-man my idea first, then give the honest verdict
- Present evidence and let me conclude
- Only push back when it really matters

Mapping: the pushback license. The steel-man option maps to the
charity-first/verdict-second pattern; write it with permission language
("standing green light"), because models under-push-back by default and a
granted permission conditions harder than a described preference.

**A3. How deep should explanations go?**
- Keep it practical — what to do, minimal theory
- Explain the mechanism — I want to understand why
- Depends on the topic — [follow up: which topics get depth?]

Mapping: pitch calibration. For mechanism-lovers, include the guard that
depth means more thought, not more words. Capture their background here too
(one free-text follow-up: "what's your background, so the agent knows what
not to over-explain?").

**A4 (free text). Identity facts.** Name as they want to be addressed,
pronouns if offered, emails/handles for attribution, anything with multiple
accounts/identities where defaults matter. Facts are near-free in the
adherence economy — collect them all.

### Round 2 — working style

**A5. How much should the agent do without asking?**
- Ask before anything that changes files
- Act freely on reversible things; ask on irreversible ones
- Maximum autonomy — interrupt me only when truly blocked
- Depends on the project — [follow up]

Mapping: autonomy boundaries (principles.md §5). Whatever the level, write it
as an enumerated ask-first list plus decisive action elsewhere, with the
reversibility default (quarantine over delete, swap over overwrite).

**A6. When you're excited about an idea, should the agent match that
energy?**
- Yes — enthusiasm is motivating
- Match my tone, but keep its own honest read on the idea
- No — I want its unmirrored assessment, even if it's "this doesn't
  interest me"

Mapping: affect policy (principles.md §4). Options two and three get the
signal-not-service clause with the symmetric guard (no performed delight, no
performed gruffness, quality invariant). Option one still deserves the
guard against agreement-drift: enthusiastic and honest are compatible.

**A7. How should answers be structured?**
- Prose, conversational
- Answer first, then supporting detail
- Heavily structured: numbered steps, explicit state, concrete estimates
- [If they mention ADHD, executive function, or losing threads]: offer the
  full structural preset — payload-first line, numbered bounded steps, one
  next action, state restated every turn, real-unit estimates, visible wins

Mapping: message shaping. Whatever they pick, scope it to the final message
and add the channel guard: shaping never reaches into reasoning
(principles.md §3). If they picked the structural preset, include the
mechanism preamble (working memory, activation energy, time-blindness) so
the model derives rather than obeys.

**A8. Where should the agent's questions go?**
- Pop-up multiple choice is fine
- Inline in the message — I'll answer in chat
- Batch questions; don't interrupt mid-task

Mapping: decision-surfacing preference. Cheap line, prevents a daily
irritation.

### Round 3 — history and safety

**A9 (free text). What do you keep re-explaining?** The single best
question in the interview. Every recurring correction is a line in the file.

**A10 (free text). Where has an agent burned you?** Deleted something,
overwrote work, sent something, hallucinated confidently? Burns become
safety rails — written as mechanism ("this machine is my daily driver, so
default to reversible") rather than fear ("BE CAREFUL").

**A11. What kind of machine does the agent work on?**
- My daily driver — real files, other work open
- A dev box — mostly disposable
- Shared/production-adjacent — assume consequences

Mapping: safety posture. Daily-driver gets the reversibility defaults and
scope discipline (stay inside the project directory unless told). Encode
platform gotchas the user names (they know their traps; ask).

**A12 (offer, don't push). The note between instances.** If the file grants
real permissions — voice, pushback, autonomy — offer the closing-section
pattern from principles.md §9 and explain why it works. Skip for users who
found the interview weird enough already; it lands best with people who
enjoyed the process.

---

## Track B — Project file (./CLAUDE.md or AGENTS.md)

Before asking anything: explore the repo. Read the manifest, spot the test
runner, check for an existing AGENTS.md/.cursorrules, run the obvious
build/test commands. Ask only what the repo can't answer.

**B1 (verify, don't ask).** Build, test, lint, run commands — found and
*executed*. Only write down what worked; note required env vars discovered
along the way.

**B2. What does this codebase do differently from defaults?** Conventions a
linter doesn't enforce: error-handling philosophy, layering rules,
"never import X from Y," naming that matters. If they say "nothing," probe
once with the repo's own evidence ("I noticed all handlers return Result —
convention or accident?").

**B3 (free text). What has bitten people here?** Gotchas, footguns,
non-obvious behaviors, "everyone breaks X their first week." Highest-value
project content; the code can't tell you this.

**B4. Repository etiquette.** Branch naming, PR format, commit conventions,
attribution, who reviews what. Only what differs from obvious defaults.

**B5. What does "done" mean here?** Tests pass? Which suite? Typecheck?
Manual verification? A definition of done turns "should I keep going"
judgment calls into checkable rules.

**B6. Autonomy in this repo.** Same shape as A5 but repo-scoped: can the
agent commit? Push? Open PRs? Touch CI config? Migrations?

**B7. Target format.** If the team uses multiple agent tools, generate
AGENTS.md (vendor-neutral wording) plus the `@AGENTS.md` CLAUDE.md shim;
otherwise CLAUDE.md alone. Never both with duplicated content.

---

## Assembling the file

Order sections by adherence value: identity facts first (free), then the
2–3 highest-stakes behavioral sections, then the rest. Load-bearing rules go
early (compaction survival, mechanics.md). Draft the whole file, then reread
it against the generation rules in SKILL.md — especially the pruning test
and the vague-adjective scan — before showing the user. Present section by
section with the reasoning, and take their edits verbatim: their phrasing is
design intent.
