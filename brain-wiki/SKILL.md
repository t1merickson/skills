---
name: brain-wiki
description: Sort a pile of documents into an ordered, typed vault for Tolaria or Obsidian. Survey first, compile a shape, then write.
---

# brain-wiki

Take a pile of documents and give it an order: every object gets a type, links to what explains it, and a page that says where it came from. Output is plain markdown — one file per object, YAML frontmatter, wikilinks — which is what [Tolaria](https://tolaria.md) and Obsidian both read, so one build serves either.

This is a bulk import of material that already exists, not a note-taking practice. That difference decides most of what follows.

## 0 · Inputs

**What goes in.** If the user names the material, use that. Otherwise it means every document in the cwd: `**/*.md` plus `.txt`, `.pdf`, `.docx`, `.rtf`, and exports. Skip `node_modules`, `.git`, `build`/`dist`, `.claude`, and anything that is code or config rather than content.

**What comes out.** A new vault directory; `./vault` is a fine default. Never move, rewrite, or delete the originals — the vault is new files that point back at them. If duplicates turn up, report them; don't resolve them.

**Which app.** Both read flat markdown with typed frontmatter, so build for that. Only ask if the answer changes the layout — someone with an existing Obsidian vault built on folders-as-categories, say.

## 1 · Survey

Walk the input. Separate CONTENT (documents, decisions, knowledge) from OPERATING MATERIAL (scripts, configs, templates, boilerplate).

Then do the part that matters: **propose the output objects**. Not clusters of files — the actual things the vault will contain, and what each one *is*. Files and objects don't map one to one:

- One source can produce zero pages, one page, or several.
- Several sources can merge into one page.
- An entity merely mentioned in a document does not earn a stub page. A person named once in a meeting note is a mention, not a Person page.

Report the map, the proposed objects, and a page estimate. This is where the shape comes from, so do it before writing the shape, not after.

## 2 · Compile the shape

The **shape** is the contract for the vault: what types exist, how objects connect, and what a verifier can check. Write it to `SHAPE.md` at the vault root, get one yes from the user, then write pages. Nothing gets written before this.

`SHAPE.md` is **flat and self-contained**. It lists the types this vault actually uses, with their fields and boundaries — the vocabulary below is how you assemble it, not something the file refers back to. The subagents that write and verify pages read only `SHAPE.md`, and should never need to reason about which optional piece was switched on.

### The vocabulary

**Core — always in the shape:**

| Type | Use when | Pick the neighbor when |
|---|---|---|
| **Note** | a durable knowledge artifact: document, reference, research summary, decision record, checklist | it's a lens you'd file other things under → Topic |
| **Topic** | an area of interest or conceptual lens that collects other objects, with no ownership | it's a real body with members → Organization; someone is accountable for outcomes in it → Responsibility |
| **Person** | a real person, or an AI agent treated as an actor | it's a company, team, or institution → Organization |
| **Organization** | a company, team, institution, publication, label, or band | it's a field of study rather than a body → Topic |
| **Place** | a location with stable identity: venue, city, site, region, building | you mean what happened there → Event |
| **Event** | something that happened, with a date: meeting, decision, incident, launch, release | you mean the durable knowledge that came out of it → Note |

**Work pack — the four PORT types from [PORTENT](https://portent.md):**

| Type | Use when | Pick the neighbor when |
|---|---|---|
| **Project** | a bounded effort producing an output, more than one sitting, with a definition of done | no end and no output, only an outcome to maintain → Responsibility; it repeats on a schedule → Operation |
| **Operation** | recurring work that fits in one sitting: a review, a check, a publishing or maintenance routine | it happened once → Task; it runs to a finish and stops → Project |
| **Responsibility** | long-running accountability, measured by standards or metrics rather than completion | it can be finished → Project |
| **Task** | one-off work that fits in one sitting | — |

*Activation:* turn the pack on when the survey proposes at least one page whose **subject** is an actionable object — an effort, a routine, an area of accountability. A document that merely discusses work is a Note. Once on, all four types are available whether or not each has members; a shipped project is still a Project. Do not count objects to decide this.

**Source — a conditional single type, not a pack:**

| Type | Use when | Pick the neighbor when |
|---|---|---|
| **Source** | an external work that pages cite: paper, article, book, talk, repo, video. Requires `url` or citation, `author`, `retrieved`, and a liveness state | it's your own writing *about* the source → Note |

*Activation:* turn it on when pages will carry that bibliographic metadata and receive inbound `cites` edges. A file path you distilled a page from is `source_files:` provenance, not a Source page — those are different things and both can be present.

### Adding anything else

Add a root type only when it has an **invariant its nearest neighbor lacks**: a required field, a constrained relationship, a distinct template, a distinct view, or its own state machine. Counts are evidence, never the rule — forty sources justify a Source type only if sources behave differently, and they do; forty essays do not justify an Essay type, because an essay is a Note with `kind: essay`.

Reach in this order: a `kind:` property, then a Topic, then a relationship, then a new type.

### Relationships

Two defaults carry most of it:

| Name | Cardinality | Means |
|---|---|---|
| `belongs_to` | one | primary context, ownership, or composition |
| `related_to` | many | secondary usefulness, association without ownership |

Add a specific relationship only when the role drives a view, a query, a template, or a verifier rule — never because it's more precise English. `authored_by` earns its place; `associated_with` doesn't. Declare each with a range so the verifier can check it:

```yaml
- name: attended_by
  cardinality: many
  range: [Person, Organization]
- name: located_at
  cardinality: one
  range: [Place]
```

Once Person, Organization, Place, and Event are all real objects, who/where/when are answerable by asking what type a link points at. Don't add parallel `who:`/`where:` fields — one fact stored twice drifts.

### Lifecycle

Default is **none**. PORTENT's captured→organized→archived describes attention over time in a vault someone operates; on a bulk import every object arrives at once and the field carries almost nothing. The pipeline's own progression (surveyed → distilled → verified) is processing state, not object state, and conflating them makes `organized` mean "the importer finished."

Turn lifecycle on when one of these is true, and say which in `SHAPE.md`:

- the target vault already uses a lifecycle field (open a real note and copy whatever it uses — Tolaria's own template writes `_organized: true`),
- the app needs it to drive inbox or archive visibility,
- the user wants this vault to become an actively maintained system,
- the corpus itself carries reliable active/archive distinctions worth preserving.

Never infer `archived` from a directory called `old`, `archive`, or `dead-project`. Archive state is about desired visibility, not the age of the file.

For import uncertainty use a separate field, written only on pages that need it:

```yaml
review: needs-human
```

### Filing

Vault-format policy, not ontology. Keep it at the bottom of `SHAPE.md`:

- One file per object, flat at the vault root; type lives in frontmatter, not the folder path. Attachments in `attachments/`.
- Filename is the kebab-case slug of the title. The H1 repeats the title in prose. Wikilinks target the slug: `[[launch-the-new-website]]`.
- Entry points: `INDEX.md`, `OPEN-QUESTIONS.md`, `SHAPE.md`.

### A compiled SHAPE.md

```yaml
---
shape: brain-wiki-import-1
extends: portent-0.1
lifecycle: none
types:
  - {name: Note,         requires: []}
  - {name: Topic,        requires: []}
  - {name: Person,       requires: []}
  - {name: Organization, requires: []}
  - {name: Place,        requires: []}
  - {name: Event,        requires: [date]}
  - {name: Source,       requires: [author, retrieved, liveness]}
relationships:
  - {name: belongs_to, cardinality: one,  range: any}
  - {name: related_to, cardinality: many, range: any}
  - {name: cites,      cardinality: many, range: [Source]}
provenance: source_files
---
```

Types and relationships listed there are the whole allowed set. A page using anything else fails verification.

## 3 · Distill

Fan out subagents, one per content area, each writing pages for its own area.

**Type the subject the page title names** — not every role, format, or entity its source mentions. A page titled "Design meeting, 4 March" is an Event; the three attendees and the room are relationships, and the fact that it arrived as a markdown file makes it no less an Event. This one rule replaces most agonizing over which type fits.

The rest:

- Every page validates against `SHAPE.md`: a type from the list, that type's required fields, declared relationships only, wikilinks that resolve.
- Every page records `source_files:` — repo-relative paths it was distilled from.
- **On a page built from more than one source, mark inline which source backs which claim.** A three-item list in the frontmatter does not say which file supports which sentence, and the verify pass can't check what isn't marked.
- Dense and factual: what is true, who decided, when, where it's written down. No connective tissue invented to make a page feel finished.
- Anything you couldn't confidently type or connect gets `review: needs-human` and stays on the list you report.

Subagents write pages; only you merge, and only you touch `INDEX.md`. One writer per file, always.

## 4 · Verify, adversarially

A second wave, each subagent checking an area it did not write. Two jobs:

1. **Claims** — every claim resolves against its cited source. This is why sources are marked inline.
2. **Shape** — type is in `SHAPE.md`, required fields present, relationships declared, cardinality respected, link targets exist and have the right type for the relationship's range.

**This pass is not optional.** The first real run of this skill produced fabrications and this is what caught them. Findings get fixed, not footnoted.

## 5 · Augment

The next corpus folds into the same vault under the same shape — Slack after Notion, GitHub after Slack, codebase last. New pages for new objects, edits where a source extends an existing page. Where two sources contradict, surface it and log it in `OPEN-QUESTIONS.md`. Never resolve a contradiction silently.

If the new corpus needs something the shape lacks, amend `SHAPE.md` against the invariant test first, and say so, then write.

## Vault furniture

- **`INDEX.md`** — every page, grouped by type. A hook per line is allowed but must be **extracted, never composed**: the page's first substantive sentence, verbatim, or nothing. Skip the hook if that sentence is boilerplate or too long. Written summaries at bulk scale are one more surface that drifts from the page, and an extracted hook is checkable — it's a substring of the file. A page nobody can reach from the index doesn't exist.
- **`OPEN-QUESTIONS.md`** — what the corpus doesn't answer, what contradicts, what looks stale. Empty is valid. Invented entries are not.
- **`SHAPE.md`** — the contract from phase 2.
- **Tolaria type documents**, when the target is Tolaria — one file per type *actually used*, `type: Type` in frontmatter, carrying display settings the app reads: `color`, `_icon`, `_sidebar_label`, `_order`, `_list_properties_display`. Generate from `SHAPE.md` so the two can't drift.

## Rules

- Never quote private content into commit messages, or anywhere else that could leave the repo.
- Originals are read-only. The vault is additive.
- Report per phase, payload first: "Survey done: 340 files, 96 proposed objects, work pack off — nothing actionable in the pile. Next: SHAPE.md for your yes." One approval, after the survey and the proposed shape. Later corpora can run heads-down if the user says so.
