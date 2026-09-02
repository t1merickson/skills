---
name: brain-wiki
description: Turn an existing document corpus into a new typed Markdown vault by surveying objects, agreeing on a machine-checkable shape, preserving source provenance, and verifying every page.
---

# Brain wiki

This is an additive bulk import, not a note-taking ritual. Originals remain read-only. The output is plain Markdown with YAML frontmatter and wikilinks for Tolaria or Obsidian.

## 1. Survey before writing

Resolve input and output roots. Exclude code, generated build trees, VCS metadata, credentials, application state, and unrelated operating material. Apply `file-batch-safety` when the corpus is large or heterogeneous.

Inventory files, formats, bytes, unreadable/placeheld items, duplicates, and conversion needs. Propose actual vault objects—not just source-file clusters. One source may yield zero, one, or several pages; an entity mentioned once does not automatically earn a page.

Report the corpus map, proposed objects, type candidates, uncertainty, and page estimate.

## 2. Compile the shape

Write `SHAPE.md` as the self-contained contract: allowed types, required fields, enums, relationships with range/cardinality, lifecycle policy, provenance root, slug/collision rules, attachment policy, and exempt vault furniture. Start from [references/shape-contract.md](references/shape-contract.md), include only the vocabulary this vault needs, and get one user approval before bulk writing.

Add a root type only when it has a distinct invariant, template, view, or lifecycle. Prefer `kind`, then Topic, then a relationship, before inventing another type. Lifecycle defaults to none unless the target system or corpus carries meaningful state.

## 3. Distill

Type the subject named by the page title. Every page:

- validates against `SHAPE.md`;
- records source paths relative to the declared input root;
- links only to real objects or records an unresolved question;
- distinguishes extracted facts, quotations, and synthesis;
- marks claim-to-source correspondence when multiple sources support one page;
- uses `review: needs-human` for unresolved classification, never invented connective prose.

Work may be divided by content area only when parallel writers are authorized and each file has one owner. Otherwise write sequentially. The primary task owns shape amendments and `INDEX.md`.

## 4. Verify adversarially

Use a deterministic validator where possible. Check frontmatter, type membership, required fields, enums, cardinality, relationship ranges, source paths, footnote/source indices, wikilink resolution, slug collisions, index completeness, and extracted hooks. Then sample claims against originals, with special attention to dates, quotations, decisions, and merged pages.

Independent review is useful when available, not mandatory. Findings are fixed or surfaced as open questions; they are not waved through with a note.

## 5. Augment without drift

New corpora enter under the existing shape. Extend existing objects when evidence adds to them; create new pages only for new objects. Preserve contradictions explicitly. Amend `SHAPE.md` before using a new invariant, type, relationship, or enum.

Vault furniture is `SHAPE.md`, `INDEX.md`, and `OPEN-QUESTIONS.md`, plus target-specific type documents. `INDEX.md` reaches every page and may use only verbatim extracted hooks. Report source counts, page counts by type, review queue, unresolved contradictions, verifier result, and untouched originals.
