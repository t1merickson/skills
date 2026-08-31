---
name: brain-wiki
description: Sort a pile of documents into an ordered, typed vault for Tolaria or Obsidian. Defaults to the PORTENT shape, and the typing flexes.
---

# brain-wiki

Take loose material and give it an order: every piece gets a type, a place, links to what explains it, and a state. The output is a plain markdown vault — YAML frontmatter, wikilinks, one file per thing — which is exactly what [Tolaria](https://tolaria.md) and Obsidian both read, so one build serves either.

The order of the phases below matched across two independent corpus builds months apart. Keep it.

## 0 · Inputs

**What goes in.** If the user names the material, use that. If they don't, it means every document in the cwd: `**/*.md` plus `.txt`, `.pdf`, `.docx`, `.rtf`, and exports. Skip `node_modules`, `.git`, `build`/`dist`, `.claude`, and anything that is obviously code or config rather than content. Say what you found before touching anything — file count, rough page count, top-level areas.

**What comes out.** A new vault directory. Ask for the path if it isn't obvious; `./vault` is a fine default. Never move, rewrite, or delete the originals — the vault is new files that point back at them. If deduping comes up, report duplicates, don't resolve them.

**Which app.** Tolaria and Obsidian both take flat markdown with typed frontmatter, so build for that and it works in both. Only ask if the answer would change the layout (someone with an existing Obsidian vault built on folders-as-categories, say).

## 1 · Define the shape first

The **shape** is the contract for the vault: what kinds of thing exist, how they connect, what states they pass through, and where files land. Write it to `SHAPE.md` at the vault root **before any page gets written**, and get the user's yes on it. It is the thing the distilling pass writes against and the checking pass checks against, and it's what a future session reads to extend the vault without inventing a second system inside the first.

A shape has four parts, and this is the format:

- **Types** — for each: a name, a group, one `use_when` line, the frontmatter fields it requires, and a "pick the neighbor instead when…" note. Sorting mistakes are almost always between two adjacent types, so write the boundary down.
- **Relationships** — for each: a name, what it means, and whether it takes one value or many.
- **Lifecycle** — the states an object can be in, and the single frontmatter field that carries them.
- **Filing** — file naming, folder layout, and which files are the entry points.

Frontmatter in `SHAPE.md` is the machine-readable half; the body is the half a writer reads while deciding. Both halves, always.

### The default shape: PORTENT

[PORTENT](https://portent.md) is an open spec for knowledge bases: eight types, two relationships, three lifecycle states. Use it unless the material argues otherwise. Written in the format above, it is:

````markdown
---
shape: portent-0.1
spec: https://portent.md
lifecycle_field: state
states: [captured, organized, archived]
relationships:
  - name: belongs_to
    means: primary context, ownership, or composition
    cardinality: one
  - name: related_to
    means: secondary usefulness, association without ownership
    cardinality: many
types:
  - {name: Project,        group: PORT, requires: [belongs_to]}
  - {name: Operation,      group: PORT, requires: [belongs_to]}
  - {name: Responsibility, group: PORT, requires: []}
  - {name: Task,           group: PORT, requires: [belongs_to]}
  - {name: Event,          group: ENTP, requires: [belongs_to]}
  - {name: Note,           group: ENTP, requires: []}
  - {name: Topic,          group: ENTP, requires: []}
  - {name: Person,         group: ENTP, requires: []}
extensions:
  - {property: source, on: all, means: file paths this object was distilled from}
---

# Shape

PORT types are things to do or operate. ENTP types record what happened, what is
known, what is interesting, and who was involved. Ask "is there work in it?" first;
that one question sorts most of the pile.

## Project — PORT
Use when: a bounded effort that produces an output, has a definition of done, and
can't be finished in one sitting.
Not this when: there's no end date and no output, only an outcome to maintain →
Responsibility. It repeats on a schedule → Operation.

## Operation — PORT
Use when: recurring work that fits in one sitting — a review, a check, a publishing
or maintenance routine.
Not this when: it happens once → Task. It runs to a finish and stops → Project.

## Responsibility — PORT
Use when: a long-running area of accountability, measured by standards or metrics
rather than completion. Projects and operations hang off it.
Not this when: it can be finished → Project. Nobody is accountable for it and it's
just an area of interest → Topic.

## Task — PORT
Use when: one-off work that fits in one sitting.
Note: tasks are part of the worldview but don't have to live in the vault. If they
live in Linear, Todoist, or GitHub Issues, link back instead of copying.

## Event — ENTP
Use when: something happened and is worth keeping — a meeting, a decision, an
incident, a launch, a conversation. Events carry a date.
Not this when: it's the durable knowledge that came out of the meeting rather than
the fact of the meeting → Note.

## Note — ENTP
Use when: a durable knowledge artifact — a document, reference, research summary,
decision record, checklist, or tool.
Not this when: it's a lens you'd file other things under → Topic. Reach for a
`kind` property before inventing Article, Video, or Essay as types.

## Topic — ENTP
Use when: an area of interest or a conceptual lens that collects notes and events
across projects, with no ownership and no expectation of completion.
Not this when: someone is accountable for outcomes in it → Responsibility.

## Person — ENTP
Use when: a real person, or an AI agent treated as an actor — collaborators,
customers, authors, attendees, decision makers.

## Filing

- One file per object, flat at the vault root. Type lives in frontmatter, not in
  the folder path. Attachments in `attachments/`.
- Filename is the kebab-case slug of the title: `launch-the-new-website.md`.
  The H1 repeats the title in prose form. Wikilinks target the slug:
  `[[launch-the-new-website]]`.
- Entry points: `INDEX.md`, `OPEN-QUESTIONS.md`, `SHAPE.md`.
````

And a page written against that shape:

```markdown
---
type: Event
state: organized
belongs_to: "[[launch-the-new-website]]"
related_to:
  - "[[sergio-panagia]]"
  - "[[design-systems]]"
source:
  - exports/notion/Design meeting 2026-03-04.md
---

# Design meeting for the new website

Workshop to settle the design language. Sergio owns the type scale;
the palette decision was deferred to the next session.
```

Two things to check against reality rather than assume:

- **The lifecycle field.** PORTENT lets an implementation name it. `state: organized` is the portable form. The Tolaria vault template writes `_organized: true` instead, and underscore-prefixed keys there (`_icon`, `_order`, `_sidebar_label`) are Tolaria's own. Writing into a vault that already exists? Open a real note and copy whatever field it uses. Starting fresh? Use `state`.
- **`source` is an extension**, not part of the spec. It's the field that makes the fact-check pass possible, so it stays — but say so when you present the shape, and keep any extension separated out like that.

### Flexing the shape

Eight types is a starting point, not a floor or a ceiling. Adjust it in the survey phase, before writing, with the counts in hand:

- **Contract** when a type would hold nothing. A type with zero or one member isn't a type. A vault of research papers may need only Note, Topic, Person.
- **Expand** when the material has a kind with its own fields, its own template, or its own relationships. Recipes, incidents, customer accounts, podcast interviews, calendar periods.
- **Properties before types.** Article, video, and checklist are all `Note` with a `kind` property. Split into a real type only when the behavior differs, not just the label.
- **Two relationships before three.** Add one only when `belongs_to` or `related_to` is hiding something a reader needs. `authored_by` earns its place; `associated_with` doesn't.
- **A different shape entirely is fine.** Zettelkasten, PARA, or one the user describes in the session. Write it into `SHAPE.md` in the same four-part format and everything downstream still works.

Whatever you land on, `SHAPE.md` says what was decided. A shape held only in your head lasts until the context window ends.

## 2 · Survey and sort

Walk the input. Separate CONTENT (documents, decisions, knowledge) from OPERATING MATERIAL (scripts, configs, templates, boilerplate). Cluster the content and count the clusters — those counts are what tell you whether to contract or expand the shape.

Report the map, the proposed shape, and a page estimate. Wait for the go.

## 3 · Distill

Fan out subagents, one per content area, each writing pages for its own area. Rules for them:

- Every claim on a page cites a source file in `source:`. No claim without one.
- Pages are dense and factual: what is true, who decided, when, where it's written down. No connective tissue you made up to make a page feel finished.
- Every page validates against `SHAPE.md`: a type from the list, the fields that type requires, a lifecycle state, wikilinks that resolve.
- `state: organized` only when the page has a clear title, a type, and enough relationships to explain why anyone would open it again. Otherwise `captured`, and it goes to the inbox for a human. Capture optimistically, organize pessimistically.

Subagents write pages; only you merge and only you touch `INDEX.md`. One writer per file, always.

## 4 · Fact-check, adversarially

A second wave, each subagent checking an area it did not write. Two jobs: verify every claim against its cited source, and validate every page against `SHAPE.md` — type exists, required fields present, wikilinks resolve to real files, `belongs_to` is single-valued.

**This pass is not optional.** The first real run of this skill produced actual fabrications, and this is what caught them. Findings get fixed, not footnoted.

## 5 · Augment, source by source

The next corpus folds into the same vault under the same shape — Slack after Notion, GitHub after Slack, codebase last. New pages where new topics appear; edits where a source extends an existing page. Where two sources contradict, surface it to the user and log it in `OPEN-QUESTIONS.md`. Never resolve a contradiction silently.

If the new corpus needs a type the shape doesn't have, amend `SHAPE.md` first and say so — then write.

## Vault furniture

- **`INDEX.md`** — every page, one line of hook each, grouped by type. The entry point for future sessions. A page nobody can reach from the index doesn't exist.
- **`OPEN-QUESTIONS.md`** — what the corpus doesn't answer, what contradicts, what looks stale. Empty is a valid state. Invented entries are not.
- **`SHAPE.md`** — the contract from phase 1.
- **Tolaria type documents** (only when the target is Tolaria) — one file per type, `type: Type` in frontmatter, and the app picks up display settings: `color`, `_icon`, `_sidebar_label`, `_order`, `_list_properties_display`. Generate them from `SHAPE.md` so the two can't drift.

## Rules

- Never quote private content into commit messages, or anywhere else that could leave the repo.
- Originals are read-only. The vault is additive.
- Report per phase, payload first: "Phase 3 done: 34 pages, 6 types used, Operation empty so I dropped it. Next: fact-check wave." Wait for the go between phases on the first corpus; later corpora can run heads-down if the user says so.
