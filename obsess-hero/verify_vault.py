#!/usr/bin/env python3
"""Layout verifier for an obsess-hero vault. Asserts and exits non-zero.

Usage: verify_vault.py /Users/Commons/Heroes/<person-slug>

Checks: the two admission rules, SHAPE.md conformance (types, required fields, enums,
declared relationships, link resolution), footnote/source consistency, and ledger agreement.
Read-only.
"""
import os, re, sys, glob, json

if len(sys.argv) < 2:
    sys.exit("usage: verify_vault.py /Users/Commons/Heroes/<person-slug>")
VAULT = sys.argv[1].rstrip("/")
WIKI = os.path.join(VAULT, "sources"), os.path.join(VAULT, "wiki")
SRC_DIR, WIKI_DIR = WIKI

FURNITURE = {"INDEX.md", "LEDGER.md", "FRONTIER.md", "OPEN-QUESTIONS.md", "SHAPE.md",
             "00-braindump.md", "NOTES.md"}

fail, warn = [], []
def bad(m): fail.append(m)
def note(m): warn.append(m)

# ── shape contract (mirrors SHAPE.md frontmatter)
TYPES = {
    "Person": [], "Work": ["authored_by", "kind", "status"],
    "Source": ["citation", "author", "retrieved", "liveness"],
    "Idea": ["advanced_by"], "Position": ["kind", "evidence", "stated_in"],
    "Event": ["date"], "Place": [], "Organization": [], "Note": [], "Topic": [],
}
RELS = {"belongs_to": None, "related_to": None, "authored_by": ["Person", "Organization"],
        "influenced_by": ["Person", "Work", "Idea"], "advanced_by": ["Person"],
        "stated_in": ["Work", "Source"], "cites": ["Work", "Source"],
        "member_of": ["Organization"], "located_at": ["Place"]}
ONE = {"belongs_to", "stated_in", "located_at"}
ENUMS = {"liveness": {"live", "moved", "dead", "paywalled", "unchecked"},
         "status": {"held", "captured", "depicted", "wanted", "scan-only", "unreachable"},
         "kind": None}  # kind is free on Work, constrained on Position
POSITION_KIND = {"belief", "practice", "preference"}
NON_REL_FIELDS = {"type", "title", "sources", "kind", "evidence", "status", "citation", "author",
                  "retrieved", "liveness", "local_path", "year", "edition", "format", "born",
                  "died", "date", "review", "also_known_as", "offered_at", "seller", "listing", "catalog_no"}

# ── rule 1: sources/ layout
if os.path.isdir(SRC_DIR):
    for entry in os.listdir(SRC_DIR):
        if entry.startswith("."):
            continue
        p = os.path.join(SRC_DIR, entry)
        if os.path.isfile(p):
            bad(f"RULE 1: loose file at sources/ root: {entry}")
        elif not os.path.exists(os.path.join(p, "SOURCE.md")):
            bad(f"RULE 1: sources/{entry}/ has no SOURCE.md")

# ── parse wiki
def parse(path):
    txt = open(path).read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", txt, re.S)
    if not m:
        bad(f"{os.path.basename(path)}: no frontmatter"); return None, None, txt
    fm, body, key = {}, m.group(2), None
    for line in m.group(1).split("\n"):
        if line.startswith("  - "):
            fm.setdefault(key, [])
            if not isinstance(fm[key], list): fm[key] = []
            fm[key].append(line[4:].strip().strip('"'))
        elif ":" in line:
            key, _, val = line.partition(":")
            key, val = key.strip(), val.strip()
            if val.startswith("[") and val.endswith("]"):
                fm[key] = [x.strip().strip('"') for x in val[1:-1].split(",") if x.strip()]
            else:
                fm[key] = val.strip('"') if val else None
    return fm, body, txt

pages = {}
for f in sorted(glob.glob(os.path.join(WIKI_DIR, "*.md"))):
    slug = os.path.basename(f)[:-3]
    fm, body, txt = parse(f)
    if fm is not None:
        pages[slug] = (fm, body, txt)

if not pages:
    bad("no wiki pages found")

# ── rule 2: every sources/<slug>/ has exactly one page pointing at it
local_paths = {}
for slug, (fm, _, _) in pages.items():
    lp = fm.get("local_path")
    if lp:
        local_paths.setdefault(lp.rstrip("/"), []).append(slug)
if os.path.isdir(SRC_DIR):
    for entry in sorted(os.listdir(SRC_DIR)):
        if entry.startswith(".") or not os.path.isdir(os.path.join(SRC_DIR, entry)):
            continue
        key = f"sources/{entry}"
        owners = local_paths.get(key, [])
        if len(owners) == 0:
            bad(f"RULE 2: sources/{entry}/ has no wiki page claiming it")
        elif len(owners) > 1:
            bad(f"RULE 2: sources/{entry}/ claimed by {len(owners)} pages: {owners}")
for key, owners in local_paths.items():
    if not os.path.isdir(os.path.join(VAULT, key)):
        bad(f"RULE 2: {owners[0]} points at missing {key}")

# ── page contract
for slug, (fm, body, txt) in sorted(pages.items()):
    t = fm.get("type")
    if t not in TYPES:
        bad(f"{slug}: type '{t}' not in SHAPE"); continue
    for req in ["type", "sources"] + TYPES[t]:
        if not fm.get(req):
            bad(f"{slug}: missing required field '{req}' for type {t}")
    if t == "Position" and fm.get("kind") not in POSITION_KIND:
        bad(f"{slug}: Position kind '{fm.get('kind')}' not in {sorted(POSITION_KIND)}")
    if t == "Source" and fm.get("liveness") not in ENUMS["liveness"]:
        bad(f"{slug}: liveness '{fm.get('liveness')}' not a legal value")
    if t == "Work" and fm.get("status") not in ENUMS["status"]:
        bad(f"{slug}: status '{fm.get('status')}' not a legal value")
    # relationships declared + range + cardinality
    for k, v in fm.items():
        if k in NON_REL_FIELDS:
            continue
        if k not in RELS:
            bad(f"{slug}: undeclared relationship '{k}'"); continue
        vals = v if isinstance(v, list) else [v]
        if k in ONE and len(vals) > 1:
            bad(f"{slug}: '{k}' is cardinality one, got {len(vals)}")
        for target in vals:
            m = re.fullmatch(r"\[\[([a-z0-9\-]+)\]\]", str(target))
            if not m:
                bad(f"{slug}: '{k}' value is not a wikilink: {target!r}"); continue
            tgt = m.group(1)
            if tgt not in pages:
                bad(f"{slug}: '{k}' points at missing page [[{tgt}]]"); continue
            rng = RELS[k]
            if rng and pages[tgt][0].get("type") not in rng:
                bad(f"{slug}: '{k}' → [[{tgt}]] is {pages[tgt][0].get('type')}, range is {rng}")
    # footnotes: every [^n] has an entry at index n in sources
    n_src = len(fm.get("sources") or [])
    used = {int(x) for x in re.findall(r"\[\^(\d+)\](?!:)", body)}
    for n in sorted(used):
        if n < 1 or n > n_src:
            bad(f"{slug}: footnote [^{n}] but sources has {n_src} entries")
    if n_src > 1 and not used:
        bad(f"{slug}: {n_src} sources but no inline [^n] markers")
    defined = {int(x) for x in re.findall(r"^\[\^(\d+)\]:", body, re.M)}
    if defined != set(range(1, n_src + 1)):
        bad(f"{slug}: footnote definitions {sorted(defined)} != sources 1..{n_src}")
    # body wikilinks resolve
    for tgt in set(re.findall(r"\[\[([a-z0-9\-]+)\]\]", body)):
        if tgt not in pages and tgt.upper() not in {"FRONTIER", "OPEN-QUESTIONS", "INDEX", "LEDGER"}:
            bad(f"{slug}: body link [[{tgt}]] does not resolve")

# ── furniture links resolve
for fn in ["INDEX.md", "LEDGER.md", "FRONTIER.md", "OPEN-QUESTIONS.md", "SHAPE.md"]:
    p = os.path.join(VAULT, fn)
    if not os.path.exists(p):
        bad(f"missing furniture: {fn}"); continue
    for tgt in set(re.findall(r"\[\[([a-z0-9\-]+)\]\]", open(p).read())):
        if tgt not in pages and tgt.upper() not in {"FRONTIER", "OPEN-QUESTIONS", "INDEX", "LEDGER"}:
            bad(f"{fn}: link [[{tgt}]] does not resolve")

# ── index completeness + hooks verbatim
idx = open(os.path.join(VAULT, "INDEX.md")).read()
listed = set(re.findall(r"^- \[\[([a-z0-9\-]+)\]\]", idx, re.M))
for slug in pages:
    if slug not in listed:
        bad(f"INDEX.md: {slug} is unreachable from the index")
for line in idx.split("\n"):
    m = re.match(r"^- \[\[([a-z0-9\-]+)\]\] — \*\*.*?\*\*(?: \(.*?\))? — (.+)$", line)
    if m:
        slug, hook = m.group(1), m.group(2)
        flat = " ".join(pages[slug][1].split())
        if " ".join(hook.split()) not in flat:
            bad(f"INDEX.md: hook for {slug} is not verbatim in the page")

# ── ledger agreement
led = open(os.path.join(VAULT, "LEDGER.md")).read()
led_slugs = set(re.findall(r"\| \[\[([a-z0-9\-]+)\]\] \|", led))
works = {s for s, (fm, _, _) in pages.items() if fm.get("type") == "Work"}
for s in works - led_slugs:
    bad(f"LEDGER.md: Work {s} has no row")
for s in led_slugs - works:
    bad(f"LEDGER.md: row for {s}, which is not a Work page")

# ── report
print(f"vault: {VAULT}")
print(f"pages: {len(pages)}   sources dirs: "
      f"{len([d for d in os.listdir(SRC_DIR) if os.path.isdir(os.path.join(SRC_DIR, d))])}")
for w in warn:
    print(f"  warn  {w}")
if fail:
    print(f"\nFAILED — {len(fail)} problems")
    for m in fail:
        print(f"  FAIL  {m}")
    sys.exit(1)
print("\nAll checks passed.")
