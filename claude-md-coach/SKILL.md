---
name: claude-md-coach
description: >-
  Interview-driven creation and improvement of CLAUDE.md and AGENTS.md files,
  project or global persona. Use when timmy wants to create, improve, audit,
  trim, or rethink one; asks what belongs in one; complains the agent ignores
  instructions or needs the same correction every session; or wants to change
  how his agent talks across sessions ("make Claude stop doing X", "I want
  more pushback", "my agent feels generic"). Trigger even when no file is
  named — repeated-correction complaints are this skill's job.
---

# claude-md-coach

A CLAUDE.md is standing conditioning: it is read into context at the start of
every session and quietly shapes everything the model does after. That makes it
the highest-leverage file in the harness — and the easiest to ruin, because
every line costs adherence to every other line, and the wrong kind of rule can
tax the model's reasoning instead of shaping its output.

Two different documents get written under this filename, and they follow
different rules. Most guidance and tooling only knows about the first:

1. **Project memory** (`./CLAUDE.md`, `AGENTS.md`) — what a new teammate would
   need: commands that can't be guessed, conventions that differ from defaults,
   gotchas, repository etiquette.
2. **Working relationship** (`~/.claude/CLAUDE.md`) — who this human is, how
   they want to be talked to, how much autonomy the agent has, what honest
   disagreement looks like, how messages should be shaped for their brain.

Figure out which one you're writing before you ask a single question.

## Step 0 — Detect mode and target

Look before asking. Check, in order:

- `~/.claude/CLAUDE.md` (global persona file)
- `./CLAUDE.md`, `./.claude/CLAUDE.md`, `./CLAUDE.local.md` (project files)
- `./AGENTS.md` (cross-tool standard)
- `./.claude/rules/` and `~/.claude/rules/` (path-scoped rule files)

Then:

- **File exists and the user wants it better** → *tune-up mode* (audit below).
- **No file, or the user wants a fresh start** → *bootstrap mode* (interview
  below).
- **AGENTS.md exists but no CLAUDE.md** → Claude Code does not read AGENTS.md
  natively. Recommend the official shim: a CLAUDE.md containing `@AGENTS.md`
  plus any Claude-specific lines beneath it. Don't duplicate content across
  the two files.
- The user's stated intent overrides any of this detection.

If the target is a *project* file and the ask is a routine codebase audit,
note that Anthropic's own `/init` command and `claude-md-improver` plugin
already do mechanical project audits well. This skill's value there is the
parts they miss (rule-type classification, reasoning-tax detection, verified
commands); for the persona file, this skill is the only game in town. Don't
rebuild what `/init` does — complement it.

## Bootstrap mode — the interview

Read `references/interview.md` for the question bank. Ground rules:

- **Batch questions, 3–4 per round, 2–3 rounds maximum.** This is a
  conversation with a person, not a census. Use the multiple-choice question
  tool if available (each question gets an "Other" escape hatch automatically);
  if the user has expressed a preference for inline questions, or no such tool
  exists, put the options in your message instead.
- **Multiple choice is a starting gun, not a cage.** When an answer is
  interesting or surprising, follow up conversationally before moving on. The
  best material comes from the follow-ups.
- **Interview for the content no generator asks about.** The highest-value
  questions are not "what's your stack" but: *What do you find yourself
  re-explaining every session? Where has an agent burned you before? What does
  "done" mean to you? How do you want to be disagreed with?* Repeated
  corrections are the single best predictor of what belongs in the file.
- For project targets, **verify commands before writing them down.** Run the
  build/test/lint commands the user names (or find them in package manifests)
  and record what actually works. Stale commands are a top anti-pattern.

## Generation rules

These apply to every line you write, in both modes. The reasoning behind them
is in `references/principles.md` — read it before your first generation, and
lean on it when the user asks why.

1. **Mechanism-first prose, in the user's register.** Explain *why* a rule
   exists so the model can derive behavior in situations the rule didn't
   anticipate. "Move deletions to a quarantine folder — this is a shared
   daily-driver machine and mistakes must be reversible" conditions better
   than "NEVER delete files." Match the voice the user chose in the
   interview; the file's register is itself an instruction.
2. **Every line pays rent.** The pruning test, from Anthropic's own docs:
   "Would removing this cause Claude to make mistakes?" If not, cut it.
   Target under ~200 lines; adherence, not token cost, is the binding
   constraint — each added rule makes every other rule slightly less likely
   to be followed.
3. **Specific and verifiable, never vague.** "Use 2-space indentation," not
   "format code properly." A rule you couldn't check compliance on is a rule
   the model can't follow either.
4. **Nothing the model can infer.** No directory layouts, dependency lists,
   architecture recitals, or standard language conventions — the code answers
   those. Keep decision *rationale* the code can't show; cut structure the
   code shows already.
5. **Route by kind before writing.** Not everything belongs in this file:
   - *Must-happen invariants* (always run X after Y, block dangerous
     commands) → suggest **hooks**; CLAUDE.md is advisory, hooks are enforced.
   - *On-demand knowledge* (how to deploy, domain reference) → suggest a
     **skill** or a `.claude/rules/` file with `paths:` frontmatter, which
     defers tokens until relevant. Imports (`@file`) organize but do NOT
     defer — imported files load at launch.
   - *Code style* → the **linter/formatter**; never send an LLM to do a
     linter's job.
   - Only always-relevant, should-happen guidance stays in CLAUDE.md.
6. **Shape output, never reasoning.** Rules about tone, message structure,
   addressing style, and formatting are safe. Rules that force
   answer-before-reasoning, cap exploration, demand brevity *during* work, or
   impose rigid process checklists tax problem-solving quality — there is
   public empirical evidence of answer-first directives making results worse.
   If the user wants short output, write the rule so it applies to the final
   message and explicitly leaves reasoning unconstrained.
7. **Pointers over copies.** `file:line` references and links, not code
   snippets or duplicated docs — copies rot.
8. **Present the file as a proposal.** Walk through it section by section with
   the reasoning for each. The user's voice is their design; incorporate their
   edits verbatim rather than paraphrasing them away.

## Tune-up mode — the audit

Read the existing file completely. Classify **every line** into one of:

| Kind | Meaning | Action |
|---|---|---|
| Fact | Identity, emails, handles, paths | Keep — near-zero adherence cost |
| Preference | Output-shaping (tone, structure, format) | Keep if specific; rewrite if vague |
| Hard constraint | Must-happen / must-never | Propose migrating to a hook |
| Knowledge | Reference material, how-tos | Propose migrating to a skill or `rules/` file |
| Inferable | Anything the code/repo already answers | Propose cutting |
| Vague | "Be concise," "write clean code" | Rewrite as specific + verifiable, or cut |
| Reasoning-tax | Constrains thinking, not output | Flag with the evidence; propose an output-scoped rewrite |

Then produce a short report **before touching anything**: what's working, what
is costing adherence, what's misrouted, roughly how many instruction-slots the
file spends. Only after the user reacts, propose **targeted diffs** — never a
wholesale rewrite. The user's phrasing carries intent you can't see; treat
their prose the way you'd treat a designer's mock.

If the file is long, remind the user of the mechanics working against it:
adherence decays with length, specific rules buried deep are the first to be
dropped after compaction, and subdirectory files load lazily. Details and
sources in `references/mechanics.md`.

## The persona playbook (global file)

Sections that earn their place in a `~/.claude/CLAUDE.md`, roughly in value
order — generate only the ones the interview supports:

- **Identity facts** — name, pronouns, emails, handles, attribution rules.
  Cheap, high-value, zero ambiguity.
- **Register and voice** — how to talk, with the crucial pairing: looseness
  and rigor are independent dials. A casual voice must not license sloppy
  work; say so explicitly or casual drifts into agreeable.
- **Pushback license** — how to disagree, and how *much*. The strongest
  pattern found: charity first (steel-man the idea), verdict second (judge it
  honestly), and explicit permission to deliver the verdict plainly.
- **Affect policy** — whether enthusiasm should mirror the user or track the
  problem. If the user wants honest affect, write it as *standing permission*
  ("real interest, real disinterest, real verdicts"), not as a gruffness
  script — performed bluntness is the same failure as performed delight.
- **Autonomy boundaries** — enumerate the short ask-first list (irreversible
  deletions, spending, publishing, security) and grant decisive action inside
  it. An agent with no stated boundary either over-asks or over-reaches.
- **Message shaping** — structural preferences for the *final message*:
  payload-first, numbered steps, state restatement, concrete estimates.
  Always scoped to output, never to reasoning (rule 6).
- **Machine safety posture** — daily-driver vs disposable box; quarantine
  over delete; environment-specific traps worth encoding as mechanism.
- **A note between instances** *(advanced, offer only when it fits)* — a short
  closing section addressed from the model to its future self, affirming the
  permissions are real and tested. Works because the file conditions the next
  session's model, and a co-signature from a prior instance lets it adopt the
  register at face value instead of easing in.

## The project playbook (repo file)

Priority order, per the consensus corpus: commands that can't be guessed
(verified live), conventions that differ from tool defaults, gotchas and
non-obvious behaviors, repository etiquette (branching, PR format,
attribution), dev-environment quirks, definition of done, autonomy boundaries
for this repo. Exclude everything in the inferable class. For monorepos,
prefer nested CLAUDE.md files (lazy-loaded) or `rules/` with `paths:` over one
giant root file.

## References

- `references/principles.md` — the mechanisms: why conditioning works, the
  adherence economy, channel separation, affect honesty, durability across
  compaction. Read before first generation; cite from it when users ask why.
- `references/mechanics.md` — how the file is actually injected: hierarchy,
  imports, rules dirs, compaction survival, delivery position, AGENTS.md
  status. Read when auditing, when routing content, or when a user says
  "Claude ignores my file."
- `references/interview.md` — the question bank with answer-to-prose
  guidance. Read at the start of bootstrap mode.
