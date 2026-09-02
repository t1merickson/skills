---
name: brain-wiki
description: Turn an existing document corpus into a new typed Markdown vault by surveying objects, agreeing on a machine-checkable shape, preserving source provenance, and verifying every page.
---

# Brain wiki

Take a pile of documents and give it an order: every durable object gets a type, links to what explains it, and a page that says where it came from. This is an additive bulk import, not a note-taking ritual. Originals remain read-only. The output is plain Markdown with YAML frontmatter and wikilinks for Tolaria or Obsidian.

The important move is from **files** to **objects**. A folder tree tells you where material happened to land; a typed vault tells you what is actually there. Do not mistake one for the other.

## 1. Survey before writing

Resolve input and output roots. Exclude code, generated build trees, VCS metadata, credentials, application state, and unrelated operating material. Apply `file-batch-safety` when the corpus is large or heterogeneous.

Inventory files, formats, bytes, unreadable/placeheld items, duplicates, and conversion needs. Then propose actual vault objects—not just source-file clusters:

- one source may yield zero, one, or several pages;
- several sources may converge on one page;
- an entity mentioned once does not automatically earn a page;
- a document about a project may still be a Note, while a page whose subject is the project is a Project.

This classification work is the survey. If it is deferred until writing, the shape merely blesses accidental output after the fact.

Report the corpus map, proposed objects, type candidates, uncertainty, and page estimate.

## 2. Compile the shape

Write `SHAPE.md` as the self-contained contract: allowed types, required fields, enums, relationships with range/cardinality, lifecycle policy, provenance root, slug/collision rules, attachment policy, and exempt vault furniture. Start from [references/shape-contract.md](references/shape-contract.md), include only the vocabulary this vault needs, and get one user approval before bulk writing.

Add a root type only when it has a distinct invariant, template, view, or lifecycle. Counts are evidence, never the rule: forty essays do not require an Essay type if `Note` plus `kind: essay` behaves identically. Prefer `kind`, then Topic, then a relationship, before inventing another type. Lifecycle defaults to none unless the target system or corpus carries meaningful state; the import pipeline finishing is not an object's lifecycle.

`SHAPE.md` must stand alone. A writer or verifier should be able to classify and serialize a page from that file without this skill, conversation history, or a guess about which optional vocabulary was enabled.

## 3. Distill

Type the subject named by the page title, not every role or format mentioned by its source. “Design meeting, 4 March” is an Event; its attendees and room are relationships, and arriving as a Markdown file does not make it a Note. This single rule eliminates much false precision.

Every page:

- validates against `SHAPE.md`;
- records source paths relative to the declared input root;
- links only to real objects or records an unresolved question;
- distinguishes extracted facts, quotations, and synthesis;
- marks claim-to-source correspondence when multiple sources support one page;
- uses `review: needs-human` for unresolved classification, never invented connective prose.

Work may be divided by content area only when parallel writers are authorized and each file has one owner. Otherwise write sequentially. The primary task owns shape amendments and `INDEX.md`; writers do not quietly evolve the ontology to accommodate a difficult page.

## 4. Verify adversarially

Use a deterministic validator where possible. Check frontmatter, type membership, required fields, enums, cardinality, relationship ranges, source paths, footnote/source indices, wikilink resolution, slug collisions, index completeness, and extracted hooks. Then sample claims against originals, with special attention to dates, quotations, decisions, and merged pages.

Run a second, adversarial pass after writing, even when no independent reviewer is available. Re-read from the verifier's side rather than continuing the writer's momentum. The first real use of this workflow produced plausible fabrications; this pass is the scar that caught them. Findings are fixed or surfaced as open questions—they are not waved through with a note.

## 5. Augment without drift

New corpora enter under the existing shape. Extend existing objects when evidence adds to them; create new pages only for new objects. Preserve contradictions explicitly. Amend `SHAPE.md` before using a new invariant, type, relationship, or enum.

Vault furniture is `SHAPE.md`, `INDEX.md`, and `OPEN-QUESTIONS.md`, plus target-specific type documents. `INDEX.md` reaches every page and may use only verbatim extracted hooks: composed summaries at bulk scale become one more surface that drifts from the pages. A page nobody can reach from the index effectively does not exist.

Report source counts, page counts by type, review queue, unresolved contradictions, verifier result, and untouched originals. Lead phase updates with the payload: “Survey done: 340 files, 96 proposed objects, work pack off. Next: SHAPE.md for approval.”
