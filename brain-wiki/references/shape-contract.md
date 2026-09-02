# Shape contract vocabulary

Use only the pieces the surveyed corpus needs. Copy their complete definitions into the vault's `SHAPE.md`; writers and validators should not need this skill installed later.

## Core types

| Type | Use when | Required distinction |
|---|---|---|
| Note | durable knowledge artifact, summary, decision, checklist | not merely a collecting lens |
| Topic | field or lens with no owner | not an organization or accountable responsibility |
| Person | a real actor worth a page | more than a passing mention |
| Organization | company, team, institution, publication, label | a body with identity or members |
| Place | stable location | not the event that occurred there |
| Event | something that happened | requires a date or calibrated date range |

Optional work types: Project (bounded effort and done condition), Operation (recurring one-sitting work), Responsibility (ongoing accountability), and Task (one-off work). Enable them when the corpus contains actionable subjects, not merely documents discussing work.

Optional Source represents an external paper, article, book, talk, repository, or video that receives citations. Require `citation`, `author`, `retrieved`, and `liveness`. A local input file distilled into a page remains `source_files` provenance, not automatically a Source object.

## Relationships

Start with `belongs_to` (one primary context) and `related_to` (many secondary associations). Add specific relationships such as `authored_by`, `attended_by`, or `located_at` only when a view, template, query, or verifier depends on the role. Declare cardinality and target ranges.

Do not duplicate the same fact into both links and parallel who/where fields.

## Lifecycle and review

Default lifecycle is `none`. Enable one only when the target vault already uses it, the application depends on it, the user intends active operation, or the corpus has reliable state worth preserving. Directory names such as `old` or `archive` are not sufficient evidence.

Use `review: needs-human` only on uncertain pages. Import processing state is not object lifecycle.

## Filing

- One file per object; type lives in frontmatter rather than a category folder.
- Attachments live under the declared attachment directory.
- Filenames are stable kebab-case slugs; H1 contains the title.
- Never overwrite or silently merge collisions. Disambiguate with an intrinsic date, organization, place, or other stable property and record ambiguous cases.
- Every page records `source_files` relative to one `input_root` declared in `SHAPE.md`.
- Multi-source pages map claims to the 1-based source list with footnotes or another validator-readable scheme.

## Minimal machine-readable frontmatter

```yaml
---
shape: brain-wiki-import-1
lifecycle: none
required_on_all: [type, source_files]
types:
  - {name: Note, requires: []}
  - {name: Event, requires: [date]}
relationships:
  - {name: belongs_to, cardinality: one, range: any}
source_files:
  input_root: ../exports
  shape: list of paths relative to input_root
---
```

The body of `SHAPE.md` defines each included type's boundary and the filing rules. Types and relationships absent from the contract are illegal until the shape is amended.
