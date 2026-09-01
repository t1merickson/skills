---
name: obsess-hero
description: Study one person completely — braindump what you already know, archive everything they made, then build a typed wiki about their work and how they think. Use when the user names a person to go deep on.
---

# obsess-hero

`/obsess-hero <name>`, or "go deep on X", "I want to know everything about X".

One person per run. The output is a durable vault at `/Users/Commons/Heroes/<person-slug>/`: their work, their ideas, and how they see and act in the world, built from sources you read yourself and files you actually hold.

No name given → ask. It's the one thing you can't infer.

This composes three skills. Read each when you reach its phase; don't reimplement them here.

| Skill | Used for | Changed here |
|---|---|---|
| `obsess` | phases 1–3, the braindump-first ritual | different index home; the vault below replaces `~/.agents/obsessions/` |
| `offline-archive` | every web capture | archives land in `sources/<slug>/`, one per capture |
| `brain-wiki` | the typed vault | the vocabulary is fixed in advance, so its phase-2 negotiation is skipped |

The anchor is a person, not a topic and not a pile of files. Their life and their work are one subject — a hero's habits, refusals, and daily routine explain the work, and the work explains the habits. Don't split the vault into a "life" half and a "work" half.

## Levers

Two, both read off the invocation.

**Depth** — `brief` unless told otherwise.

| | brief (default) | deep |
|---|---|---|
| Triggered by | anything not listed opposite | "go deep", "know everything", "exhaustive", "all of it", "follow every thread" |
| Frontier | one round; the rest is listed, not followed | rounds until the frontier is empty |
| People | the hero, plus first-degree names that explain the work | second-degree — their influences' influences, students, rivals |
| Web | their main home, plus anything short | every site they own, every long-form interview |
| Works | the ones that matter, roughly 15–30 pages | every work that exists, however minor |
| Budget | an hour of reading, one pass | report per round and check in |

**Angle** — an optional direction ("Eno, the music side"). It orders the frontier. It never lowers the depth of what it does cover.

Neither lever licenses guessing. A brief run holds fewer facts, not softer ones.

## The layout

```
/Users/Commons/Heroes/<person-slug>/
  00-braindump.md      phase 1. Dated, written once, never revised.
  NOTES.md             your running research trace. For you, not the user.
  SHAPE.md             the contract. Standard vocabulary unless this hero forced a change.
  INDEX.md             every wiki page, grouped by type.
  LEDGER.md            every known work, and whether we hold it.
  FRONTIER.md          threads known and not yet followed.
  OPEN-QUESTIONS.md    what the sources don't answer, and where they contradict.
  wiki/                one flat markdown file per object.
  sources/<slug>/      one directory per captured thing. SOURCE.md required.
```

Two admission rules, both mechanically checkable. They are the whole defence against a junk drawer:

1. Every captured file sits in exactly one `sources/<slug>/`, and that directory contains a `SOURCE.md`. No loose files at `sources/` root, no second level of grouping.
2. Every `sources/<slug>/` has exactly one page in `wiki/` whose `local_path` points back at it.

Nothing else is a legal location. Something that fits nowhere becomes a line in `OPEN-QUESTIONS.md`. When you want to create `misc/`, `other/`, `assets/`, `raw/`, or `to-sort/`, the thing either earns a `sources/<slug>/` with real provenance or it doesn't come in at all.

`SOURCE.md` carries: original URL, retrieval date, kind, who made it, how it was captured, what was stripped, and the wiki slug it maps to.

**Slugs are global.** Each hero folder is its own vault, but the slug namespace spans all of `/Users/Commons/Heroes/`. `[[christopher-alexander]]` means the same object in every vault, so opening the parent directory as one vault resolves cross-hero links for free, and the per-hero `INDEX.md` stays local. Never slug one object two ways in two heroes.

## 0 · Resolve and set up

- **Which person.** Disambiguate before creating anything. The slug is the kebab-case of the name on the work, not the legal name. Add a birth year only to break a real collision: `john-wilson-1953`.
- **Existing folder means augment, not restart.** Read `00-braindump.md`, `INDEX.md`, and `FRONTIER.md`, then work as a delta. Never overwrite the braindump; write a dated second one if today's recall differs.
- **When augmenting or migrating, re-read the holdings, not just the notes.** Notes are a map; `sources/` is the territory. Every capture already in `sources/` gets re-mined before any new fetching — prior-round notes summarize what that round found interesting, not what the sources contain.
- **Park in-flight work first.** Half-attention immersion produces half-dense notes.
- **Living people.** These are public figures, and their published life is fair material. The line: anything they published, said on the record, or that a good biography would carry is in. Anything that only exists by aggregating records — home address, family who aren't public, current movements — stays out, at any depth.

## 1 · Braindump, before any tool call

`00-braindump.md`: everything you already believe about this person, fast and dense, zero searches. The order matters — after you've read sources you can no longer tell recall from what you just saw.

Mark inline: `✓` know it cold, `?` verify, `✗` known blank. For a person, four things reliably come out fluent and wrong, so pre-mark them `?` on sight: **dates**, **titles of works**, **who influenced whom**, and **quotes**. Attributed quotes are the single most fabricated object in this whole skill. A quote you cannot later pin to a source you read is deleted, not softened.

## 2 · Agenda

Open `NOTES.md` with the research agenda built from those marks: what to verify, what to fill, what moved since your cutoff (people keep publishing, and some have died — check).

Then draft the works list: everything you think they made. This is a hypothesis, not the ledger. Every line arrives at `status: unverified` and either gets confirmed against a source or is struck. It never graduates on confidence alone.

## 3 · Immersion and capture

Read in this context. Delegate finding, never reading — a source a subagent read did not happen to you, and the teaching at the end runs on what you actually hold.

Priority order for sources: their own words first (their books, their site, their talks, their code), then long-form interviews where they talk at length, then serious criticism, then reference material. A single-author profile beats a crowd-edited page: one author builds an arc.

Capture as you go, don't batch it at the end. Every capture follows `offline-archive`, including the load discipline for whole sites (roughly 1 request/second with jitter, resumable before you start) and the network-blocked replay to verify. A blog with 400 posts is **one** `sources/<slug>/`, not 400.

Keep `NOTES.md` running as a verdict log against your own braindump: "had the date wrong, it's 1977", "confirmed, and the primary source adds…". A note that restates a source is wasted.

### The frontier

Every thread you learn about and don't follow goes to `FRONTIER.md` immediately, with three fields: the thread, where you found it, and why it might matter. In deep mode you drain this list in rounds, and dead ends stay listed as followed-and-empty so an augment doesn't re-walk them. In brief mode you stop after one round and **report the frontier to the user** — that's what makes a brief run honest rather than merely short.

## 4 · Acquiring files

The rule the library paid for: **read-only finders, one central filer.** Nothing that searches also writes. Path decisions are yours alone and made by rule, so no subagent ever invents a folder.

Every candidate file clears the same gate before it lands:

1. **It is what it claims.** `%PDF` header, and a real text layer via `pdftotext`.
2. **Born-digital, not a photographed book.** Import the gate; don't shell out:

   ```python
   sys.path.insert(0, scan_dir)      # dir containing scan_detect.py
   from scan_detect import score_pdf
   result = score_pdf(path)          # reject when result.unwanted_scan
   ```

   Look for `scan_detect.py` in `/Users/Commons/Developer/Projects/library-tools/tools/`, then wherever the user names. If it's absent, say so and record `gate: ungated` on the page rather than implying a check that didn't run.

   **Never run `scan_detect.py <folder>` as a bare script** — plain invocation *moves* files into Scanned/Digital/Uncertain siblings. The read-only entry points are `--score <file>` and `--report <folder>`.

   1-bit scans are acceptable. Reject when most pages are full-page raster above 1-bit. Born-digital producer metadata (InDesign, LaTeX, Illustrator) passes even when the file is image-heavy — that's the glossy-monograph case, and it's common for exactly the kind of person this skill is pointed at.
3. **Dedup by normalized title, not path.** "Vaswani et al." and "Ashish Vaswani" are one work.
4. **Never overwrite.** Collisions take a ` (2)` suffix. Nothing is ever deleted.

**No substitutions to hit a count.** A bibliography padded with plausible-sounding titles is the failure this whole skill exists to prevent. A work you can't verify exists gets no page at all. A work you verified and can't obtain gets a page and `status: wanted`.

Paywalled and in-print works get stubbed. Never pirate, and never buy — spending is always the user's call.

## 5 · The shape

Write `SHAPE.md` from the vocabulary below, then write pages. Only stop for approval if this hero forced a deviation — a type you need that isn't here, or one you're dropping. Otherwise the shape is settled and the yes isn't worth the interruption.

**Required on every page:** `type`, `sources`.

`sources` is a list mixing repo-relative paths (`sources/a-pattern-language/`) and URLs you read but didn't capture. Pages built from more than one entry mark inline which one backs which claim, with a footnote whose number is the 1-based index: `He disowned the method by 1993.[^2]`. The verify pass can't check what isn't marked.

### Types

| Type | Use when | Pick the neighbor when |
|---|---|---|
| **Person** | the hero, or anyone whose relationship to them explains something | they're mentioned once and explain nothing — then it's a mention, not a page |
| **Work** | something the hero made. Requires `authored_by`, `year`, `kind`, `status` | someone else made it → Source |
| **Source** | an external work you cite: criticism, an interview, a profile, a reference. Requires `citation`, `author`, `retrieved`, `liveness` | the hero made it → Work |
| **Idea** | a concept they originated or advanced. Requires `advanced_by` | nobody owns it, it's just a field → Topic |
| **Position** | a stated belief, practice, or preference. Requires `evidence` and `stated_in` | it's a concept rather than a stance → Idea |
| **Event** | something that happened, with a `date` | you mean the durable knowledge from it → Note |
| **Place** | a location with stable identity | you mean what happened there → Event |
| **Organization** | a company, school, publisher, label, studio, band | it's a field of study → Topic |
| **Note** | synthesis you wrote: a career arc, a comparison, a reading order | it's a lens that collects other pages → Topic |
| **Topic** | a field or lens with no owner | someone advanced it → Idea |

**Acquisition fields.** A hero whose work is out of print generates live purchase data — a
seller, a price, a listing. Record it on the Work page rather than losing it, and surface it in
the ledger:

```yaml
offered_at: "GBP 152"
seller: "Wittenborn Art Books (via AbeBooks)"
listing: "https://…"
```

These record an offer seen on a date, not a valuation, and never an instruction to buy.

**Catalog numbers.** Most archival subjects have an external catalog — a catalogue raisonné, a standard checklist, a discography. When one exists, every Work page carries `catalog_no` (`catalog_no: "Bradbury RB #21"`), the ledger gets a column for it, and the catalog itself gets a Source page. Dealers key their listings to these numbers; a vault without them cannot be checked against the trade.

Three types carry the weight and are easy to get wrong:

- **Work vs Source** turns on who made it. An interview is a **Source** (the interviewer made it) that is `about` the hero — and the hero's sentences inside it are the evidence for **Position** pages. This is the ambiguous case; decide it this way every time.
- **Position** is where "how they see and act in the world" lives. `kind:` is `belief`, `practice`, or `preference` — what they think, what they do, what they like. The required `evidence` field holds a verbatim quote or a specific observed behavior, and `stated_in` points at the Work or Source it came from. **A Position without evidence is deleted, not flagged.** That required field is the entire defence against a vault of invented opinions, which is what a person-shaped wiki degrades into when it degrades.
- **Idea vs Topic** turns on ownership. "Pattern language" is an Idea advanced by a person. "Architecture" is a Topic.

Do not switch on brain-wiki's PORT work pack. This vault is studied, not operated. Lifecycle is `none`; use `review: needs-human` for import uncertainty.

### Relationships

| Name | Cardinality | Range |
|---|---|---|
| `belongs_to` | one | any |
| `related_to` | many | any |
| `authored_by` | many | Person, Organization |
| `influenced_by` | many | Person, Work, Idea |
| `advanced_by` | many | Person |
| `stated_in` | one | Work, Source |
| `cites` | many | Work, Source |
| `member_of` | many | Organization |
| `located_at` | one | Place |

`influenced_by` is the one that earns the vault its shape — it's what turns a pile of pages into a lineage you can read backwards. Record the direction you have evidence for and no more.

### The hero page

`wiki/<person-slug>.md` is the entry point and the only page allowed to be long and narrative. It carries the synthesis: how the life and the work explain each other, what changed across the career, what they'd say about their own late work. Every other page stays atomic.

## 6 · Write

In brief mode, write the pages yourself. In deep mode, fan out one writer per area — writers only serialize what you already read, and one writer per file, always. You alone touch `INDEX.md`, `LEDGER.md`, and the hero page.

`LEDGER.md` is generated from the wiki at the end of every round so the two can't drift. Columns: title, kind, year, catalog number when one exists, status, local path, wiki slug. The first time you generate it, write the generator into the vault as `tools/regen_ledger.py` and name it in the ledger header. "Do not hand-edit; regenerate" is not an instruction unless there is something concrete to run.

| Status | Means |
|---|---|
| `held` | the file is in `sources/`, gated and verified |
| `captured` | archived from the web as a site or page rather than a file |
| `depicted` | the object is physical and unheld, but photographs of it are in `sources/` |
| `wanted` | verified to exist; paywalled, in print, or otherwise unobtainable |
| `scan-only` | exists only as a scan, and the gate rejected it |
| `unreachable` | cited somewhere, but every copy is dead |

For a hero whose work is physical — books in small editions, paintings, instruments — `depicted` is the honest common case. A ledger reading `held: 0` above a source tree full of photographs is technically true and practically misleading. Say what you hold.

`INDEX.md` lists every page grouped by type. A hook per line is allowed but must be **extracted, never composed** — the page's first sentence of body prose, copied verbatim, or nothing. Body prose skips headings, blank lines, and footnote-definition lines; strip inline footnote markers from the hook. A page nobody can reach from the index doesn't exist.

## 7 · Verify

Three passes. None optional.

1. **Claims** — a subagent checking an area it did not write. Every claim resolves against the source marked for it. Every quote appears verbatim in a source you hold. This pass exists because the first run of brain-wiki produced fabrications and this is what caught them; on a person-shaped vault the exposure is quotes and dates.
2. **Archive** — `offline-archive`'s network-blocked replay. An archive that looks perfect while silently depending on the live site is the normal failure, so assert and exit non-zero rather than eyeballing.
3. **Layout** — run `verify_vault.py` from this skill's directory:

   ```
   python3 verify_vault.py /Users/Commons/Heroes/<person-slug>
   ```

   It asserts and exits non-zero: both admission rules hold, every `sources/<slug>/` has a `SOURCE.md` and exactly one wiki page, every `[^n]` has an entry at index *n*, every wikilink resolves, every INDEX hook is verbatim, and every LEDGER row matches a Work page.

Findings get fixed, not footnoted.

## 8 · Return, then teach

Report payload-first: who, how deep, what you read, the two or three most interesting things, what you changed your mind about, what's still on the frontier. Then teach — pitch up, first principles, real opinions, motivation before mechanism. The immersion earned the confidence; spend it.

Never recommend one of their works from memory alone. Titles and links are exactly where recall fabricates. It's in the ledger or you don't cite it.

When a question lands on `OPEN-QUESTIONS.md`, say so and go check.

## Housekeeping

- Post-compaction, read the hero page and `INDEX.md` before answering anything about them. The vault survives compaction; your reasoning doesn't.
- Hero folders are not scratch. Never sweep `/Users/Commons/Heroes/`. The vault is the durable output.
- This vault is separate from the Books library by design. A work can exist in both; note it, don't cross-file.
- **Non-hero material gets evicted, not stored.** Research turns up useful tangents that are not about the hero. Move them to a home the user names, or ask once, and leave a one-line housekeeping pointer in `OPEN-QUESTIONS.md` until they are gone.
- Personal-use archival only. Republishing leaves the machine and needs the usual ask-first.
