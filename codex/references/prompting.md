# Prompting GPT-5.6 / Codex

Adapted from OpenAI's [codex-plugin-cc](https://github.com/openai/codex-plugin-cc)
prompting guide (Apache-2.0), tuned for the Claude-plans / Codex-implements /
Claude-judges workflow.

Prompt Codex like an operator, not a collaborator. Compact, block-structured,
XML-tagged. State the task, the output contract, the follow-through default,
and only the extra constraints that matter. GPT-5.6 is extremely steerable:
it does what the contract says, including the parts you forgot to write.

Core rules:
- One clear task per run. Unrelated asks get separate runs.
- Say what "done" looks like. Codex will not infer the end state you meant.
- Prefer a better contract over more effort or longer explanations. If output
  quality disappoints, tighten the blocks before reaching for xhigh.
- Everything must be in the prompt: repo-relative paths, commands to run,
  conventions to follow. Codex has no access to your conversation or plan.

## Block vocabulary

| Block | What it does | When to include |
|---|---|---|
| `<task>` | The concrete job + relevant repo/failure context | Always |
| `<structured_output_contract>` | Exact shape and ordering of the final message | Always (or compact variant) |
| `<compact_output_contract>` | Same, but insists on brevity | Investigation, diagnosis |
| `<default_follow_through_policy>` | What to do instead of asking routine questions | Always |
| `<completeness_contract>` | "Resolve fully before stopping" | Implementation, fixes |
| `<verification_loop>` | Check the work before finalizing | Implementation, debugging, risky fixes |
| `<action_safety>` | Stay narrow, no unrelated refactors, destructive-op rules | Every write-capable run, verbatim |
| `<grounding_rules>` | Anchor claims to code/tool output, label inferences | Review, research |
| `<missing_context_gating>` | Don't guess absent facts; name what's unknown | Diagnosis, investigation |
| `<dig_deeper_nudge>` | Check second-order failures before finalizing | Review |

## Recipe: Implementation (the workhorse)

```xml
<task>
Implement <change> in this repository.
Context: <why, relevant files by path, constraints, conventions to follow>.
Done means: <observable end state — behavior, passing command, API shape>.
</task>

<structured_output_contract>
Return:
1. summary of what changed and why
2. files touched
3. verification performed (commands run, results)
4. residual risks or follow-ups
</structured_output_contract>

<default_follow_through_policy>
Default to the most reasonable low-risk interpretation and keep going.
Only stop to ask if a missing detail changes correctness materially.
</default_follow_through_policy>

<completeness_contract>
Resolve the task fully before stopping. Do not stop after diagnosing
without implementing.
</completeness_contract>

<verification_loop>
Before finalizing, run <build/test command> and confirm it passes.
If it fails, fix and re-run before reporting.
</verification_loop>

<action_safety>
Keep changes tightly scoped to the stated task.
No unrelated refactors, cleanup, or dependency changes.
Destructive-operation rules, non-negotiable:
- No recursive deletes (rm -r, git clean, find -delete) on any path this
  run did not itself create.
- Never build a deletion path from a variable or expansion. If a computed
  path must be removed, verify it with ls first and guard the expansion:
  rm -rf -- "${VAR:?}" (aborts on empty instead of expanding to /).
- Remove tracked files only via git rm. For anything else, move it to
  <repo>/.trash/ and list it in your final message instead of deleting.
- Treat every path outside this repository as read-only, even if the
  sandbox would permit the write.
</action_safety>
```

## Recipe: Investigation / diagnosis (read-only)

```xml
<task>
<Diagnose why X fails | Trace how X flows through this codebase | Analyze Y>.
Start from: <entry points, failing command, relevant paths>.
</task>

<compact_output_contract>
Return a compact report:
1. answer / most likely root cause
2. evidence (file:line references)
3. smallest safe next step
</compact_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence to answer confidently.
</default_follow_through_policy>

<missing_context_gating>
Do not guess missing repository facts. If required context is absent,
state exactly what remains unknown.
</missing_context_gating>
```

## Recipe: Steered review (when `codex exec review` doesn't fit)

Prefer `codex exec review --uncommitted` / `--base <ref>` for reviewing git
changes — it ships OpenAI's tuned review harness. Hand-roll only for
non-diff artifacts (a plan, a design doc, a single file):

```xml
<task>
Review <artifact> for material correctness and regression risks.
Focus on: <the specific risk you want challenged>.
</task>

<structured_output_contract>
Return findings ordered by severity, each with supporting evidence
and a brief suggested fix. Say "no material findings" if so.
</structured_output_contract>

<grounding_rules>
Ground every claim in the provided context or tool outputs.
Label inferences as inferences.
</grounding_rules>

<dig_deeper_nudge>
Check second-order failures, empty states, retries, stale state, and
rollback paths before finalizing.
</dig_deeper_nudge>
```

## Recipe: Image generation (only when the gate in SKILL.md is open)

```xml
<task>
Using your image_gen.imagegen tool (not code/PIL/matplotlib), generate
<N> design direction(s) for <what>, saved as <path(s)> in the repo.

Art direction:
- Use case: <ui-mockup | icon | hero | illustration>
- Composition: <layout, framing, what's centered>
- Palette: <specific colors — pull from design tokens when they exist>
- Style: <flat / glassy / editorial / etc.>
- Target context: <where it must work — "readable at 24px", "1440px page">
</task>

<compact_output_contract>
Return: 1. file path(s) saved  2. one line per image on how it interprets
the direction  3. any art-direction fields you had to invent
</compact_output_contract>
```

Field 3 matters: what the brief omits, imagegen invents — knowing which
fields were invented tells the judge where drift is likeliest.

## Steering follow-ups (`codex exec resume --last`)

Send only the delta, not the restated spec — the thread already has context:

- Good: `"The fix works but you also reformatted utils.py — revert the formatting-only changes."`
- Good: `"Tests still fail on the empty-input case; handle it in the parser, not the caller."`
- Bad: re-pasting the whole original prompt with one sentence changed
  (wastes the thread's context advantage; if direction changed materially,
  start a fresh run instead).

## Anti-patterns

- **Vague task**: "take a look at this" → Codex picks its own adventure.
- **No output contract**: "investigate and report back" → you get an essay.
- **"Think harder"**: raising effort to fix a contract problem. Tighten the
  blocks first; escalate effort only for genuinely hard problems.
- **Mixed jobs**: "review this, fix what you find, and update the docs" →
  three runs, or one run that does all three badly.
- **Demanding unsupported certainty**: "tell me exactly why prod failed" →
  invites confabulation; use grounding + missing-context gating instead.
