# Hero vault contract

Copy the selected contract into the vault's `SHAPE.md`.

## Admission

1. Every captured artifact is inside one `sources/<slug>/` with `SOURCE.md` containing original URL/citation, retrieval date, creator, kind, capture method, transformations/stripping, integrity hash, and owning wiki slug.
2. Every source directory has exactly one wiki page whose `local_path` points to it. A page may cite many sources, but one source directory has one catalog owner.
3. Loose source files and miscellaneous holding directories are illegal. Unacquired or unclassified material belongs in the frontier/open-questions files.

## Types

Every page requires `type` and `sources`.

| Type | Required fields | Boundary |
|---|---|---|
| Person | none | relationship materially explains the hero/work |
| Work | `authored_by`, `kind`, `status` | made by the hero or their organization |
| Source | `citation`, `author`, `retrieved`, `liveness` | external interview, criticism, profile, reference |
| Idea | `advanced_by` | concept the person originated or materially advanced |
| Position | `kind`, `evidence`, `stated_in` | sourced belief, practice, or preference |
| Event | `date` | occurrence rather than durable synthesis |
| Place | none | stable location |
| Organization | none | company, school, label, publisher, studio, band |
| Note | none | research synthesis such as an arc or comparison |
| Topic | none | field/lens with no owner |

Position `kind` is `belief`, `practice`, or `preference`. A Position without specific evidence is not admitted. A hero-created interview may require explicit local policy; by default the interviewer-made artifact is a Source containing the hero's evidence.

## Relationships

- `belongs_to` (one, any)
- `related_to` (many, any)
- `authored_by` (many, Person or Organization)
- `influenced_by` (many, Person, Work, or Idea)
- `advanced_by` (many, Person)
- `stated_in` (one, Work or Source)
- `cites` (many, Work or Source)
- `member_of` (many, Organization)
- `located_at` (one, Place)

Record only the direction evidence supports. Do not infer reciprocal influence.

## Source mapping

On multi-source pages, mark which source supports each material claim with 1-based footnotes matching the `sources` list. Quotes must appear verbatim in an inspected source. Paraphrases remain attributable.

## Work status

- `held`: a verified file is present;
- `captured`: permitted web archive is present;
- `depicted`: photographs/documentation of an unheld physical work are present;
- `wanted`: existence verified but no legitimate copy held;
- `scan-only`: only an unsuitable or disallowed scan was found;
- `unreachable`: cited, but no accessible copy found within the search budget.

Offers, prices, and listings are dated observations, not valuations or instructions to buy. Catalog numbers belong on Work pages when an authoritative catalog exists.

## Furniture

- `INDEX.md`: every page grouped by type; optional hook must be verbatim body text.
- `LEDGER.md`: generated inventory of Works, status, year, kind, catalog number, local path, and slug.
- `FRONTIER.md`: lead, source, expected value, estimated next-pull tokens/subagents/requests/storage, followed status, and stop reason.
- `OPEN-QUESTIONS.md`: contradictions, uncertainty, missing evidence, and scope exclusions.
- Hero page: the sole long narrative synthesis; other pages remain atomic.

Lifecycle is none. Use `review: needs-human` for import uncertainty.
