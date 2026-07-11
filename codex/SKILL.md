---
name: codex
description: Delegate coding work to Codex (GPT-5.6) agents via the codex CLI, with Claude as planner and judge. Use whenever the user says "codex", "send this to codex", "switch to codex agents", "have GPT do it", "prep for codex", "hand this off to codex/GPT", asks for a GPT-5.6 second opinion, or signals Claude usage pressure in any phrasing — "I'm hitting usage credits", "running low on limits", "almost at my cap", "avoid overage" — even when it sounds like an aside rather than a request. Also for well-specified implementation, bulk/mechanical work, independent code review, or verification that would burn a lot of Claude tokens for little judgment. Use proactively when orchestrating: plan in Claude, implement in Codex, judge in Claude — and mid-epic, when work started with Claude agents should continue on Codex.
---

# Codex delegation

Codex agents (GPT-5.6) are collaborators, not competitors. They are fast, cheap
(they run on a ChatGPT subscription, not API pricing), extremely steerable,
and very good at executing well-specified work. You are the architect and the
judge: you decide what gets built, write the spec, and verify the result. Codex
does the labor in between. The division that works: **judgment stays here,
execution goes there.**

## When to delegate (and when not to)

Delegate to Codex:
- Well-specified implementation — you know exactly what change is needed and
  could describe "done" in a paragraph.
- Bulk/mechanical work — migrations, repetitive refactors, test scaffolding,
  data analysis scripts.
- Independent review — a second opinion on a plan or diff from a model family
  with different blind spots than yours.
- Investigation you'd rather not spend your own context on — "trace how X
  flows through this codebase and report back."

Keep for yourself:
- Anything where the spec is still forming — if you can't write the "done"
  criteria yet, delegating just outsources the confusion.
- Taste-heavy work (API design, UX copy, architecture) unless the user asks for a
  Codex take explicitly.
- Small edits where writing the handoff prompt costs more than doing the work.

## Sol: peer consultation

Sol is the one tier at your level — a peer to think with, not a bigger
subcontractor. The trigger for bringing it in is *your own uncertainty*, not
task size: a design that won't settle after two passes, a diagnosis that
keeps slipping, orchestration you can't get clean, research-heavy questions
where a second frontier take would change what you commit to. Run it
read-only at `high` and hand it your actual position with the weak points
named — "here's my plan and where it creaks; find the flaw" — not a neutral
summary that hides what you're unsure about.

This is consultation, not delegation, so the "keep taste-heavy work for
yourself" rule above doesn't apply: judgment never leaves here — you're
stress-testing yours. Sol's take enters the same judge loop as any other run;
when you and Sol disagree, that's signal — resolve it on the merits and
surface it to the user when it matters.

Never send Sol menial work. Chat-grade asks and small mechanical actions go
to luna, context-gathering to terra; sol does real coding but at `medium` —
its high efforts are for judgment, not labor. If a prompt could be executed
well without hard thinking, it's mis-tiered.

## Running Codex

Codex installs a few ways, so don't assume `codex` is on PATH. Resolve
whichever exists — prefer the user's own CLI, fall back to the ChatGPT.app
bundle (which auto-updates with the app):

```bash
CODEX=$(command -v codex \
  || ls /Applications/ChatGPT.app/Contents/Resources/codex \
        "$HOME/Applications/ChatGPT.app/Contents/Resources/codex" \
        /Applications/Codex.app/Contents/Resources/codex \
        "$HOME/Applications/Codex.app/Contents/Resources/codex" 2>/dev/null \
     | head -1)
[ -x "$CODEX" ] || echo "Codex not found — install the CLI (npm i -g @openai/codex, or brew install codex) or the ChatGPT desktop app, then re-resolve"
```

Covers the usual cases:
- **CLI on PATH** — npm, Homebrew, or a manual install; `command -v` finds it.
- **ChatGPT.app** — Codex.app merged into the unified ChatGPT desktop app
  (July 2026: Chat + Work + Codex in one bundle); the binary lives at
  `Contents/Resources/codex`, in `/Applications` or `~/Applications`. The old
  Codex.app paths are kept as a fallback for machines that haven't
  auto-updated yet.
- **Neither** — surface the install options instead of failing mid-run.

Core invocations — pick by job:

| Job | Command |
|---|---|
| Implement / fix | `"$CODEX" exec -s workspace-write -C <repo> -o <out.md> "<prompt>"` |
| Investigate / analyze (no writes) | `"$CODEX" exec -s read-only -C <repo> -o <out.md> "<prompt>"` |
| Review working tree | `"$CODEX" exec review --uncommitted -C <repo> -o <out.md> ["<focus>"]` |
| Review branch vs base | `"$CODEX" exec review --base main -C <repo> -o <out.md>` |
| Follow-up on same thread | `"$CODEX" exec resume --last "<delta instruction only>"` |

Mechanics that matter:
- **`-o <file>` (output-last-message)** — always use it, pointed at the
  scratchpad. Codex's stdout is a progress stream; the file is the actual
  answer. Read the file, not the scroll.
- **Long prompts via stdin** — for multi-paragraph specs, write the prompt to
  a file and pipe it: `"$CODEX" exec -s workspace-write ... - < prompt.md`.
  Avoids shell-quoting hell.
- **Redirect stdin when the prompt is an argument** — append `< /dev/null`.
  In non-TTY contexts (agent Bash, scripts, cron) `codex exec` otherwise
  blocks forever on "Reading additional input from stdin..." and looks like a
  slow model. Only omit this when you're piping the prompt in via `-`.
- **Background for anything nontrivial** — implementation runs take minutes.
  Use Bash `run_in_background` and keep planning while Codex works. The `-o`
  file makes results easy to collect when it finishes.
- **Model × effort — pick from this matrix.** Always pass both `-m` and
  `-c model_reasoning_effort=...` explicitly: a `model` pin in
  `~/.codex/config.toml` silently overrides the CLI default. Requires codex
  CLI ≥ 0.143.

  | Job | Model / effort |
  |---|---|
  | Judgment work — planning, architecture, peer consultation, review and diagnosis second opinions | `gpt-5.6-sol` / `high` |
  | Implementing a written plan; general coding | `gpt-5.6-sol` / `medium` |
  | Context subagents — read, search, trace the codebase | `gpt-5.6-terra` / `high` |
  | Chat-grade asks; small mechanical actions (moving files, organizing) | `gpt-5.6-luna` / any |

  Sol/medium for coding is deliberate: once the plan is written, a frontier
  model at moderate effort beats a mid-tier model at high effort. Don't
  escalate effort to fix output that a tighter prompt would fix.
- **Effort values** (verified 2026-07, codex 0.144, OpenAI provider): every
  tier accepts none, minimal, low, medium, high, xhigh; `max` is
  Bedrock-only. An invalid value fails fast with the supported list in the
  error, so probing is cheap if this drifts.
- **Never pass `ultra`.** Sol accepts it as an effort string, but it isn't a
  deeper thinking level — it's GPT's internal agent fan-out (their Workflow
  equivalent: the run decomposes into parallel subagents, multiplying token
  burn). In this skill's division of labor, orchestration stays on the
  Claude side; a delegated Codex run should be one agent doing one job.
- **Git requirement** — `codex exec` refuses to run outside a git repo unless
  you pass `--skip-git-repo-check`. Prefer running in the repo; the sandbox
  scopes writes to it.
- **Structured output** — when you want a machine-checkable verdict (review
  findings, pass/fail), pass `--output-schema <schema.json>` with a JSON
  Schema for the final message.
- **Sandbox discipline** — `read-only` for investigation/review,
  `workspace-write` for implementation. Never
  `--dangerously-bypass-approvals-and-sandbox`. Full rules in
  "Blast radius" below.

## Blast radius

Prompt contracts lower the *odds* of a destructive command; the sandbox
decides whether it *executes*. The known incident shape (July 2026, public):
a review subagent improvised "cleanup", a variable expanded wrong, and
`rm -rf` hit the user's home directory. Every layer below independently
stops that — run all of them:

- **Read-only unless the task writes.** Review, investigation, diagnosis:
  `-s read-only`, no exceptions. A non-write task that improvises cleanup
  then hits the sandbox instead of the filesystem.
- **`-C` is the blast radius.** `workspace-write` scopes writes to the `-C`
  directory, so the sandbox is exactly as wide as the workspace you hand it.
  Point it at the repo root — never $HOME, never a broad parent directory.
  A recursive delete *inside* the workspace is sandbox-legal by definition.
- **Commit before write runs.** Committed files are the recoverable class;
  untracked scratch and ignored files (.env) are what a bad command destroys
  permanently. `git status` before dispatch — anything precious gets
  committed (or copied out) or the run doesn't go.
- **Deletion is never delegated as a side effect.** If removal is the task,
  it's `git rm` of named tracked files. Cleanup sweeps, cache pruning,
  "remove build artifacts" — do those yourself, or have Codex *report*
  candidates and delete after judging. The `<action_safety>` block in
  [references/prompting.md](references/prompting.md) carries the matching
  contract language; include it in every write-capable run.
- **Judge for destruction, not just correctness.** After any write run, scan
  the progress stream for `rm -rf`, `git clean`, `git reset --hard`,
  `find ... -delete` before trusting the diff — the summary won't confess
  what a subshell did. Pair with `git status`: files that *vanished* are as
  much a finding as files that changed.

## Writing the handoff prompt

Codex sees none of your conversation, none of your plan, none of the user's
context. The prompt must be self-contained: repo-relative file paths, the
change wanted, the "done" criteria, and how to verify. A GPT-5.6 agent with a
tight contract will run a long way without asking questions — that's the
feature you're buying, so give it the contract.

Structure prompts as XML-tagged blocks — task, output contract, follow-through
policy, verification loop, action safety. Read
[references/prompting.md](references/prompting.md) before writing your first
handoff prompt of the session; it has the block vocabulary and full recipes
for implementation, diagnosis, and review runs.

The two failure modes that actually happen: a vague task ("clean this up")
that Codex interprets creatively, and a missing output contract so the final
message is an essay instead of the summary/files/verification list you needed.
Both are prompt bugs, not model bugs — fix the prompt before escalating effort
or taking the work back.

## The judge loop

Delegation without judgment is just hoping. After every Codex run:

1. **Collect** — read the `-o` output file; for write runs, `git diff` (and
   `git status` for new files) in the repo.
2. **Judge the diff on the merits** — as if reviewing a PR from a strong
   contributor: correctness, scope creep, style fit with the surrounding code,
   edge cases. Spot-read the actual changed files, not just the diff hunks,
   when the change touches logic you care about.
3. **Verify independently** — run the build/tests yourself. Codex reporting
   "tests pass" is a claim, not evidence.
4. **Verdict:**
   - *Accept* — report to the user what Codex did and your assessment.
   - *Steer* — small gaps: send only the delta via
     `codex exec resume --last "<what to change>"`. Don't restate the whole
     spec; the thread has context. One or two steering rounds is normal.
   - *Take over* — if two steers haven't converged, the spec was probably the
     problem. Either rewrite the spec fresh (new run) or finish it yourself.
     Tell the user which and why.

Never relay Codex's self-reported success as your own conclusion. You are the
last line before the user sees it.

## Parallel work

Multiple Codex agents can run concurrently (background Bash calls). If two
write-runs would touch the same repo, give each its own git worktree and merge
after judging — same rule as any two agents sharing a checkout. Read-only
runs can share freely.

## Workspace geography (mixed Claude + Codex fleets)

When Claude and Codex agents share a repo, the failure mode is durable work
stranded in a throwaway worktree while the canonical checkout rots — no deps,
wrong branch, one `git clean -fd` from gone. Rules that prevent it:

- **One canonical checkout; the branch is the product.** Durable work lands on
  a real branch in the primary checkout. Worktrees — Claude's EnterWorktree,
  `isolation: "worktree"`, or hand-made ones for Codex — are *agent scratch*:
  spawn for parallel/expendable work, merge or discard by slice end. A
  worktree that outlives its session is debt; the next session's first job is
  landing it.
- **Never grow a project inside `.claude/worktrees/`.** Those are
  harness-managed and sit untracked inside the main checkout — cleanup
  tooling, `git clean`, or a future session can vaporize them. If work
  unexpectedly matures there, promote it: merge to the canonical checkout and
  remove the worktree at the next commit boundary.
- **Same geography for every agent.** Each brief — Claude subagent prompt or
  `codex exec -C` — names the same repo root explicitly. Never let an agent
  infer cwd, and never mix "some agents in the worktree, some in the main
  checkout" within a slice.
- **Two write-agents never share a tree** (any vendor combination). One
  writer per worktree; readers share freely. Judge and merge in one place.
- **Un-tracked state lives in the canonical checkout.** `.env` files, local
  service associations, symlinks: keep the originals canonical and
  copy/symlink *into* worktrees, so tearing a worktree down loses nothing.
- **Remote before fleet.** Before fanning agents out on a repo, make sure a
  remote exists and the branch is pushed. Agent-heavy workflows multiply the
  ways a local tree gets clobbered; a push is the cheapest insurance there is.
- **Session-end sweep:** no stray worktrees, no uncommitted agent output, no
  test data left in shared services (DBs, mail catchers), and the canonical
  checkout truthfully reflects project state. If a handoff doc has to explain
  the geography, the geography is wrong — fix it instead of documenting it.

## Mid-epic handoff (Claude → Codex)

When an epic starts on Claude agents and the labor swaps to Codex mid-stream
(judgment stays here; execution moves), two facts shape the protocol:

- There is **no cross-vendor resume**. `codex exec resume` only continues
  Codex-started threads. A Claude→Codex handoff is always a cold start, and
  the only memory both vendors share is the filesystem.
- Therefore **the repo must hold the epic's state, not the conversation**.
  If the next task can only be explained by someone who was in the chat, the
  handoff isn't ready.

Before dispatching Codex mid-epic, run the checkpoint — full checklist and
brief template in [references/handoff.md](references/handoff.md):

1. **Land the state** — commit WIP on a real branch in the canonical checkout
   (never a stash, never loose in a worktree); push if a remote exists.
2. **Fix geography first** — per the workspace-geography rules: no paths into
   `.claude/worktrees/`, no tree only you can find. If the brief would need a
   map, fix the terrain instead.
3. **Crystallize the plan into the repo** — a plan file recording goal, done
   criteria, decisions already made (with the why, so Codex doesn't
   relitigate them), tasks completed, tasks remaining as self-contained
   items, verification commands, and discovered gotchas.
4. **Note untracked state** — env files, running services, test data: what
   git doesn't carry, the plan file must mention.

Then each Codex brief goes thin: point at the plan file, name one task, state
done-criteria and verification. The judge loop is unchanged — you still
review every diff. This checkpoint is vendor-neutral on purpose: it's the
same artifact a future Claude session resumes from, so it's never wasted work
even if Codex ends up not being used.

## Browser / UI verification

Codex's browser runtime loads under `codex exec` but needs a paired backend
(the OpenAI Codex Chrome extension, connected via
`~/.codex/chrome-native-hosts-v2.json`); unpaired, browser tasks fail with
"No browser is available." When it's unpaired, do UI verification yourself via
claude-in-chrome, or ask the user for a visual review. If a Codex run needs to
check a page, have it report what it needs rather than shell out via curl.

Codex agents testing web work will often spin up their own sandboxed
Chromium (usually via Playwright) — that's acceptable and safer than touching
real browsers, but sprawl isn't. `~/.codex/AGENTS.md` carries the hygiene
rules (shared cache, headless, kill on exit); when briefing Codex on web-UI
work, reinforce them in the prompt: reuse the shared Playwright cache, run
headless, terminate every browser you started, and report any new browser
binary you had to download.

## Image generation (gated subroutine)

Codex has a native `image_gen.imagegen` tool — text-to-image on the ChatGPT
subscription, no plugin, works in `codex exec` (verified 2026-07). It can
generate UI mockups, icons, and design directions that you then view and
judge (Read renders PNGs). Anthropic models can't generate images; this is
the bridge's imagegen arm.

**Off by default.** Only invoke when the user explicitly asks for generative
or exploratory UI direction ("use imagegen", "generate some mockups", "give me
a first pass", "not sure what I want here"). If they've already given visual
direction — mocks, tokens, reference screenshots — implement that; don't
generate alternatives. When the signal is ambiguous, ask in one line first.

**The subroutine, when on:**
1. **Generate** — brief Codex with real art direction, not vibes: use case,
   asset type, composition, palette (pull from existing design tokens if any
   exist), style, and target context ("must read at 24px" / "1440px marketing
   hero"). Codex structures the imagegen prompt from these fields — what you
   specify passes through; what you omit gets invented.
2. **Judge visually** — Read every generated image yourself and check it
   against the brief the way you'd check a diff; drift from the spec (an
   illustration when you asked for an icon) is common. Steer via
   `resume --last` with concrete visual deltas.
3. **User verdict before implementation** — present the direction(s) to the user.
   A generated mock is a proposal, never an approved target. Only after their
   yes does it become a spec to implement toward.

Housekeeping: each generation also leaves a ~1MB original in
`~/.codex/generated_images/<uuid>/` regardless of where the agent saves the
copy — a slow-growing cache; mention it if it gets large.

## Review second opinions

For "what does GPT think of this?" on a diff, prefer `codex exec review` over
a hand-rolled prompt — it carries OpenAI's own tuned review harness. Pass
focus text for a steered review ("focus on concurrency in the cache layer").
Then triage its findings yourself: confirm each one against the code before
presenting it to the user as real. Findings from Codex are leads, not verdicts.
