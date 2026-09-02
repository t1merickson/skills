---
name: obsess-hero
description: Build a bounded, source-accounted vault about one named person's published work and documented thinking. Use only when explicitly invoked.
---

# Obsess hero

Invoke with `/obsess-hero <name>` or an equally explicit request to go deep on one person. The output is a durable person-shaped vault: their work, their ideas, and the documented relationship between how they lived, thought, and made things.

If no person is named, ask. Disambiguate them before creating files.

This composes three skills. Read each when its phase begins; do not replace their distinctive work with a summary here.

| Skill | Used for | Changed here |
|---|---|---|
| `obsess` | the braindump-first immersion and mile markers | the hero vault replaces the ordinary obsession index |
| `offline-archive` | substantial web capture | archives land in `sources/<slug>/` |
| `brain-wiki` | the typed vault | the vocabulary is already governed by this skill's contract |

The anchor is a person, not a topic or a pile of files. Their life and work are one subject when sources connect them. Do not split the vault into unrelated “life” and “work” halves, and do not infer a connection merely because it would make a good story.

## Levers

Read two levers from the invocation.

**Depth** defaults to brief.

| | Brief | Deep |
|---|---|---|
| Research | one user-selected, high-yield pull | several proposed paths, selected one pull at a time |
| People | the hero and first-degree relationships that explain the work | wider lineage, students, rivals, or influences only on selected paths |
| Works | the works needed to establish the shape | a route toward a fuller verified census |
| Frontier | report the rest after the first mile marker | redraw and ask which branch to fund next |

**Angle** is an optional direction such as “the music side” or “their teaching practice.” It orders the frontier; it does not soften the evidence standard inside that angle.

Neither lever licenses guessing. A brief run holds fewer facts, not softer ones. “Deep,” “everything,” and “exhaustive” expand the route map; they do not waive mile markers or promise completeness.

## Vault layout

Use an existing configured hero root when the user has one; otherwise prefer a project-local `heroes/<person-slug>/` or ask. Do not hard-code a machine-specific library.

```text
<vault>/
  00-braindump.md
  00-braindump-<date>.md   optional blind delta on later runs
  NOTES.md
  SHAPE.md
  INDEX.md
  LEDGER.md
  FRONTIER.md
  OPEN-QUESTIONS.md
  wiki/<object-slug>.md
  sources/<capture-slug>/SOURCE.md
  tools/regen_ledger.py
```

Read [references/vault-contract.md](references/vault-contract.md) when shaping the vault and copy the selected contract into `SHAPE.md` so the vault remains self-describing.

Two admission rules defend against a junk drawer:

1. Every captured artifact belongs to exactly one `sources/<slug>/` with `SOURCE.md`; no loose files or miscellaneous holding directories.
2. Every `sources/<slug>/` has exactly one owning wiki page whose `local_path` points back to it.

Slugs are local to the vault unless the selected root is intentionally governed as one cross-person library. Do not silently impose a global namespace on unrelated vaults.

## The ritual

### 0 · Resolve and set the contract

- Name the person, angle, breadth, vault root, recency risk, time/request/token/storage budget, and stopping condition.
- If work is already in flight, park its non-reconstructable state before switching.
- An existing vault means augment, not restart. Locate it, but preserve the blind phase: write a dated braindump before rereading its index, notes, frontier, ledger, or holdings. Never overwrite an earlier braindump.

### 1 · Braindump, before research

Write `00-braindump.md`, or a dated sibling on an augment, before searching, opening sources, rereading the vault, or asking an agent to investigate. Put down everything you already believe about the person, fast and dense. Mark it using `obsess`'s `✓`, `?`, and `✗` notation.

For a person, pre-mark four fluent failure modes as `?`: dates, titles of works, influence claims, and quotations. A quote that cannot later be pinned to a source actually inspected does not graduate into the vault. Do not revise the blind dump after research.

### 2 · Re-enter, build the agenda, and map routes

After the blind dump, reread an existing vault's hero page, index, frontier, ledger, relevant notes, and actual holdings. Notes are a map; `sources/` is the territory. Re-mine relevant holdings before fetching replacements, then treat this run as a dated delta.

Open `NOTES.md` with the agenda built from the braindump: what to verify, fill, or update. Draft a works list as a hypothesis. Every entry begins unverified and either graduates against evidence or is struck; confidence alone never promotes it into the ledger.

Follow `obsess`'s mile-marker protocol. Make the route chart person-specific and keep it to a few high-yield alternatives. Relevant paths may include:

- works census and catalog identity;
- direct study of primary works;
- interviews and documented positions;
- biography or working practice that explains the work;
- reception, influence, students, and rivals;
- recent work or changed status.

For each path show where it leads, the bounded pull, main-task token range, subagent roles and delegated-token range, requests or access dependencies, expected capture/storage growth, vault-writing cost, and stop point. Ask which path or paths to fund. Do not begin an unchosen branch or spawn its agents.

### 3 · Immerse and capture, one selected pull at a time

Read in the primary task. A selected subagent may find candidates or map a bibliography, but a source read only by an agent cannot support the hero synthesis.

Prioritize the person's own work and words, then long-form interviews, serious criticism or biography, and reference sources. A coherent author can reveal an arc that a crowd-edited page cannot. Use the latter for orientation, not as a substitute for the best available evidence.

Capture substantial public pages through `offline-archive` as you go rather than batching provenance at the end. A site or coherent corpus may be one source directory rather than hundreds of arbitrary fragments. `SOURCE.md` records what the capture is, where it came from, when and how it was captured, what changed in capture, and which page owns it.

Keep `NOTES.md` as a verdict log against the braindump: “had the date wrong,” “confirmed, and the primary work adds…,” “these accounts conflict because….” A note that merely restates a source is wasted.

Every lead not followed goes to `FRONTIER.md` immediately with its origin, expected value, estimated next-pull cost, status, and stop reason. Dead ends remain marked followed-and-empty so an augment does not walk them again.

At each mile marker, report what the selected path changed, coverage gained, actual observable spend, held versus merely identified works, corrections, and the redrawn frontier. Say `not metered` rather than inventing token usage. Then pause unless the user explicitly authorized an uninterrupted run bounded by paths, total budget, and stopping condition.

### 4 · Acquire files without losing their identity

Use read-only finders and one central filer. Searchers do not invent destination paths or write into the vault; the primary task applies the vault's admission rules.

Every candidate clears the same gate:

1. It is what it claims: check format identity and, for text-bearing documents, confirm a usable text layer.
2. If a configured born-digital/scan gate exists, use only its read-only scoring or report entry point. Never invoke a batch mode known to move files. If no gate is available, record `gate: ungated` rather than implying a check ran.
3. Deduplicate by work identity and normalized title, not merely by path or filename.
4. Never overwrite. Preserve collisions under distinct names until identity is resolved.

Do not substitute plausible works to hit a count. A work verified to exist but not held still earns a Work page with the appropriate contract status. Any actual purchase remains a separate user decision. Read `file-batch-safety` before a large acquisition or reorganization.

### 5 · Shape the vault

Read the vault contract, copy it into `SHAPE.md`, then apply `brain-wiki`. Only stop for shape approval when this hero genuinely requires a new type, relationship, or admission rule.

Three boundaries carry unusual weight:

- Work versus Source turns on who made the artifact. An interviewer-made interview is normally a Source containing evidence from the hero.
- Position pages require a specific statement or observed practice and a `stated_in` source. Unsupported psychological portraiture does not become a Position.
- Idea versus Topic turns on evidenced ownership or advancement. Record only the influence direction the evidence supports.

The hero page is the entry point and the only page allowed to carry the long narrative synthesis. Other pages stay atomic. Do not enable an operational work-management pack; this vault is studied, not operated.

### 6 · Write

Serialize only claims supported by material this task inspected. In a brief run, write the pages directly. In a deeper run, optional writers must appear in a user-selected route; one writer owns each file, and writers only serialize the inspected evidence assigned to them. The primary task owns the hero synthesis, shape, index, ledger, and final evidence judgment.

Generate `LEDGER.md` from Work pages at the end of every pull. The first time, put the generator at `tools/regen_ledger.py` and name it in the ledger header; “do not hand-edit” is not a useful rule without something concrete to run.

`INDEX.md` lists every page grouped by type. Any hook is extracted verbatim from the page's body rather than composed afresh. A page unreachable from the index does not exist operationally.

### 7 · Verify

Run three passes:

1. **Claims:** every material claim resolves to its marked source and every quotation appears in an inspected source. If an independent reviewer was funded in the selected route, give it an area it did not write; otherwise perform the mapping directly.
2. **Archive:** replay web captures with the network blocked using `offline-archive`'s verifier.
3. **Layout:** run this skill's read-only verifier:

   ```bash
   python3 <skill-directory>/verify_vault.py <vault>
   ```

Fix findings where evidence permits; otherwise keep them visibly unresolved. A clean layout does not prove claim truth.

### 8 · Return, then teach

At the final return, report the person, angle, selected paths, pulls completed, coverage by source/work type, held versus identified works, major corrections, frontier, open questions, verifier result, observable spend, storage consumed, and stopping reason.

Then teach from the sourced pages: first principles, motivation before mechanism, real synthesis, and visible uncertainty. Never recommend one of the person's works from recall alone. When a question lands on `OPEN-QUESTIONS.md`, say so and offer the next bounded pull.

## Housekeeping

- After context loss, read the hero page and `INDEX.md` before answering and reverify volatile claims.
- Hero vaults are durable outputs, not scratch. Never sweep or merge roots casually.
- Non-hero material does not belong in the vault. Park it in `OPEN-QUESTIONS.md` until the user names a home; do not grow a miscellaneous branch.
