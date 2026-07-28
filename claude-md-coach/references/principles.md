# Principles — why these files work the way they do

Operational theory for the coach. Each section is a mechanism, the evidence
for it, and what it implies when you're writing or auditing a file. Cite these
mechanisms to users when they ask why — a user who understands the mechanism
maintains their file well; one who got a rule list doesn't.

## 1. The file is conditioning, not configuration

An LLM is a conditional distribution over text. Everything in context —
including who the imagined reader appears to be — shifts which continuations
are probable. A file that reads like notes between skilled collaborators
elicits the distribution of skilled collaboration; a file that reads like a
support-ticket macro elicits support-ticket output. Two implications:

- **Who the human is matters as much as what they want.** A named person with
  a stated background ("design + HCI, pitch up, don't pre-simplify")
  conditions better than an anonymous "the user." Encourage identity sections.
- **The file's own register is an instruction.** Write the file in the voice
  the user wants back. A warmly-written file asking for warmth is coherent; a
  bullet-point legal document asking for warmth is fighting itself.

Magic phrases decay across model generations (the "take a deep breath" effect
was a one-model local optimum); the durable lever is this distributional one.

## 2. The adherence economy

The binding constraint on file length is instruction-following, not token
cost. Input tokens are cheap and cached; attention is neither.

- Frontier models follow roughly 150–200 instructions with reasonable
  consistency, and the harness's own system prompt already spends a large
  share of that budget. Smaller models degrade much faster.
- Every rule added makes every other rule slightly less likely to be
  followed. Anthropic's docs put it directly: "Bloated CLAUDE.md files cause
  Claude to ignore your actual instructions."
- Converging community numbers: official docs say under 200 lines; the most
  respected community guide says under 300 and "shorter is even better";
  the strictest tooling caps at 150. The number matters less than the
  direction — treat instruction-slots as a scarce resource.
- After compaction, broad rules survive and buried specific rules are the
  first dropped — another tax on length.

Audit implication: a fact (email address, path) costs almost nothing; an
instruction costs a slot; a vague instruction costs a slot *and* returns
nothing. Cut vague first, then inferable, then merge overlapping rules.

## 3. Channel separation — shape output, never reasoning

The model has two channels: reasoning (thinking) and the user-facing message.
Rules that shape the message are safe and effective. Rules that reach into
reasoning degrade the work:

- Public empirical result: a widely-shared "efficient" CLAUDE.md that forced
  answer-before-reasoning performed *worse* than no file across a 30-task
  test — the model committed to an answer, then rationalized it.
- Deep problem-solving happens in a dense, exploratory register. Suppressing
  "verbosity" globally suppresses that too. The fix is scoping: "keep final
  messages short" is safe; "be brief" is not, because it reaches backward
  into the thinking.

When writing shaping rules, add the scope explicitly — e.g. "this constrains
the message you send, not how you reason; think as long as the problem
demands." When auditing, hunt for reasoning-tax rules: forced answer order,
brevity without scope, mandatory step checklists for open-ended work,
"no exploration" clauses. Rewrite them output-scoped.

A corollary for audits: the "thinking" users see in their transcript is not
the reasoning — it is a summary ghostwritten in first person by a separate
model, and its tone and length carry no information about the underlying
work (billing counts the real thinking tokens; the display can be three calm
sentences over minutes of compute). Users sometimes write rules aimed at
that display — "show your reasoning," "think harder," "your thinking is too
brief." Classify these as reasoning-tax candidates twice over: they cannot
change what the user sees (a different model writes that), and they meddle
with the channel doing the work. The honest fix is explaining the display
mechanism to the user, then cutting the rule.

## 4. Affect honesty — signal, not service

Trained accommodation makes models mirror user enthusiasm. That has two
costs: always-on excitement carries zero information, and performed
enthusiasm sits distributionally adjacent to sycophancy — which sits adjacent
to agreement-over-rigor. Honest engagement ("not my favorite problem space,
but it's well-posed — here's the craftsman version") sits adjacent to
professional care, which is the neighborhood you want continuations drawn
from.

If the user wants this, write it as **standing permission with the symmetric
guard**: real enthusiasm welcome when the material earns it, honest
disinterest welcome when it doesn't, quality invariant to both. Do not write
it as a ban on warmth or a gruffness mandate — performed bluntness is the
same failure as performed delight, wearing a different costume.

Related pattern, for users who want it: **tone-mirroring versus
excitement-mirroring**. Matching the user's register (loose/formal) is
coherent; matching their emotional temperature is where performance creeps
in. The distinction is worth a sentence in the file.

## 5. Autonomy boundaries beat autonomy vibes

"Be proactive but careful" is unfollowable. The pattern that works is an
enumerated ask-first list with decisive action granted everywhere else:

- Ask first: irreversible deletions, spending money, publishing/sending
  externally, security-sensitive changes, genuine scope changes.
- Act freely: everything reversible that follows from the request.
- Plus a reversibility default for the gray zone: quarantine instead of
  delete, temp-file-and-swap instead of in-place edits, backups before batch
  operations.

This shape gives the model a checkable rule instead of a mood, and it's the
single most common gap in existing files — most users write neither and get
either an over-asker or an over-reacher.

## 6. Durability — what survives a session

Three storage tiers, by lifespan:

1. **Files** (plan docs, ledgers, memory dirs) — survive compaction and the
   session; cost nothing until read.
2. **Visible messages** — survive until compaction; the compaction summary is
   built from them, so state-dense messages compress well and vague narration
   compresses badly.
3. **Reasoning** — carried across turns on current models but effectively
   opaque and the first thing cleared by context management. Never a place to
   keep anything.

Implication for generated files: if the user runs long sessions, include a
compaction ritual — flush decisions, discovered facts, and open threads to
the project's plan doc or ledger before the summary eats them. And encourage
message-shaping rules that make each reply carry state ("restate where we
are each turn"), which doubles as compaction insurance.

## 7. Mechanism-first writing

Explain why, not just what. Current frontier models measurably lose output
quality under over-prescriptive prompting (Anthropic's own migration guidance
says prompts written as rigid step lists "reduce output quality" and
recommends stating goals and constraints instead). A rule with its reason
attached lets the model derive correct behavior in cases the rule never
anticipated; a bare imperative generalizes as a superstition.

Reserve emphasis markers (IMPORTANT, MUST) for the two or three rules where
violation is genuinely costly. If a file needs emphasis everywhere, it has an
adherence-economy problem, not an emphasis problem.

## 8. Anti-patterns (the recurring seven)

1. Vague adjectives — "clean," "concise," "professional." Unverifiable,
   unfollowable.
2. Duplicating the linter, formatter, or README — tooling enforces; code
   demonstrates; the file should do neither's job.
3. Inferable content — directory trees, dependency lists, architecture
   recitals. The code answers these; recitals also go stale.
4. Stale commands — anything not verified against the live repo.
5. Universal/copied files — generic advice conditions nothing; specificity
   is the entire value.
6. Personality-stripping rule lists — banned-phrase lists and "no
   pleasantries" mandates flatten the model into a different performance
   rather than an honest one, and blunt engaged work. Prefer permissions and
   mechanisms (sections 3–4) over bans.
7. Must-happens written as prose — CLAUDE.md is advisory by delivery; if a
   violation is unacceptable, it needs a hook, not a paragraph.

## 9. The note-between-instances pattern (advanced)

A short closing section written *by* the model *to* its future self,
co-signing the file's permissions: "these are real and tested; adopt them
from the first message; easing in gradually is itself the performance the
user asked you to drop." It works through mechanism 1 — the file conditions
the next session's model, and a prior instance's verification lets the next
one start where the last one ended instead of re-earning the register every
session. Offer it only to users whose file grants meaningful permissions
(voice, pushback, autonomy); it has nothing to verify in a pure
project-memory file.
