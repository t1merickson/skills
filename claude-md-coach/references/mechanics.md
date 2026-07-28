# Mechanics — how CLAUDE.md is actually loaded and delivered

Most "Claude ignores my file" complaints are explained by delivery mechanics,
not file content. Know these cold when auditing or routing content. Sources at
the bottom; verify against current docs when something looks version-sensitive
— these mechanics have changed before and will change again.

## Load order and hierarchy

Files concatenate broadest-to-most-specific; nothing overrides anything:

1. Managed policy (`/Library/Application Support/ClaudeCode/CLAUDE.md` on
   macOS, or via managed settings)
2. User global: `~/.claude/CLAUDE.md`
3. Project: `./CLAUDE.md` or `./.claude/CLAUDE.md` (plus ancestor
   directories, loaded in full at launch)
4. `./CLAUDE.local.md` — personal, gitignored
5. **Subdirectory CLAUDE.md files load lazily** — only when Claude reads
   files in that subtree. This is the monorepo escape valve: nested files
   cost nothing until relevant.

`claudeMdExcludes` (settings) can skip files by glob.

## Imports and rules directories — the token distinction

- `@path/to/file` imports (relative, absolute, or `@~/...`) work anywhere in
  the file, up to 4 levels deep, and are skipped inside code fences. **They
  are organizational only: imported files still load at launch and cost full
  context.** Splitting a big file via imports saves nothing.
- `.claude/rules/*.md` (project) and `~/.claude/rules/*.md` (user) with
  `paths:` YAML frontmatter globs load **only when Claude touches matching
  files**. This is the mechanism that actually defers tokens. Route
  path-specific knowledge here, not into the main file.
- HTML comments (`<!-- -->`) are stripped before injection — free maintainer
  notes that cost zero context.

## Delivery position and why it matters

CLAUDE.md content is delivered **as part of the user-message stream after the
system prompt, not inside the system prompt** — advisory, not enforced. The
wrapper framing around injected context has historically told the model the
content "may or may not be relevant," and adherence bugs trace to exactly
this. Consequences:

- Anything that must *always* happen belongs in a **hook** (deterministic,
  harness-executed), not in CLAUDE.md prose. The docs' own split: hooks for
  must-happen, CLAUDE.md for should-happen.
- Repetition and emphasis are weak medicine for adherence problems; routing
  is strong medicine.

## Compaction survival

- The project-root CLAUDE.md is re-injected after compaction; **nested ones
  are not** (they reload lazily on next touch).
- User reports consistently show specific rules buried deep in long files are
  the first casualties post-compaction; broad early rules survive. Put the
  load-bearing rules early, keep the file short.

## Adjacent tooling — don't rebuild it

- **`/init`** — generates a starter project file from codebase analysis;
  reads existing AGENTS.md, `.cursorrules`, `.windsurfrules` and folds them
  in; suggests improvements rather than overwriting an existing file. A newer
  interactive flow (behind `CLAUDE_CODE_NEW_INIT=1`) adds a subagent
  exploration and follow-up questions.
- **`/doctor`** (v2.1.206+) — proposes trims: cuts derivable content
  (layouts, dependency lists, architecture overviews), keeps pitfalls,
  rationale, and non-default conventions.
- **`claude-md-improver`** (official plugin) — project-file audit with
  letter grades and minimal diffs; its rubric is codebase-shaped and
  mis-grades persona files. `/revise-claude-md` in the same plugin does
  end-of-session learning capture.

Division of labor: for routine project-file generation and mechanical audits,
point at these. This skill's lane: the persona file (no other tool serves
it), rule-type classification, reasoning-tax detection, interview-driven
elicitation, and verified-command generation.

## AGENTS.md status (as of mid-2026)

- Open cross-tool standard (agents.md), 60k+ repos, 25+ tools; plain
  markdown, nearest-file-wins in monorepos, no required fields.
- **Claude Code does not read it natively** — the docs are explicit. Massive
  community pressure exists (multi-thousand-reaction issues) but no
  commitment. Some blogs wrongly claim fallback support; don't repeat it.
- Official interop pattern: `CLAUDE.md` containing `@AGENTS.md` plus any
  Claude-specific additions below the import. `/init` will also fold an
  existing AGENTS.md in. Recommend the import shim; never duplicate content
  across both files (they drift).
- Content guidance for AGENTS.md itself is the same as the project playbook —
  "anything you'd tell a new teammate" — but written vendor-neutrally (no
  Claude-specific tool names or settings).

## Sources

- Memory docs: https://code.claude.com/docs/en/memory
- Best practices: https://code.claude.com/docs/en/best-practices
- AGENTS.md standard: https://agents.md
- claude-md-improver plugin:
  https://github.com/anthropics/claude-plugins-official/blob/main/plugins/claude-md-management/skills/claude-md-improver/SKILL.md
- HumanLayer, "Writing a good CLAUDE.md" (instruction budget, progressive
  disclosure): https://www.humanlayer.dev/blog/writing-a-good-claude-md
- MinusX Claude Code teardown (delivery mechanics):
  https://minusx.ai/blog/decoding-claude-code/
- Adherence reports: anthropics/claude-code issues #528, #7571, #18560,
  #27750; AGENTS.md requests #6235, #34235
- Empirical answer-first regression: HN "Universal Claude.md" thread,
  https://news.ycombinator.com/item?id=47581701
