---
name: hopper-discovery
description: >
  Reference for the Hopper MCP tools, which read a program the user already has open in the
  Hopper app. Use when the user wants to explore a program's symbols, procedures, strings,
  call graph, or annotations through those tools. Triggers on: Hopper, the Hopper MCP,
  reading a Mach-O binary's structure, listing or searching procedures/strings/names,
  navigating by address, or annotating a document.
---

# Hopper MCP tools

The tools read and annotate a document the user has open in Hopper. You drive, they watch.
Report findings in plain terms; keep "the code contains X" separate from "X runs in normal
use," and back a claim with two or three agreeing signals before stating it.

## Orient first

- `current_document` — the active document (empty/error → nothing open).
- `list_documents` / `set_current_document` — pick or switch when several are open. Work one
  at a time; re-check `current_document` if results look off.
- `list_segments` — read once; small, and shows the real section layout so you aren't guessing.

## Cursor model

Hopper tracks a current document, procedure, and address. Most tools default to it when the
argument is omitted (`procedure_pseudo_code`, `procedure_info`, `procedure_assembly`, `xrefs`,
the comment/name setters). Park the cursor once with `goto_address`, then call a cluster of
tools with no arguments. `current_address` / `next_address` / `prev_address` move it.

## Search, don't dump

`list_procedures`, `list_strings`, `list_names` return the whole table — often tens of
thousands of rows. Prefer the targeted forms; fall back to a full list only if a search is
empty.

- `search_strings(pattern=…)` — regex, case-insensitive by default. Best starting point:
  surfaces UI text, selectors, class names, paths, URLs, error messages. Each result address
  is a thread for `xrefs`.
- `search_procedures(pattern=…)` — name → address.
- `search_name(pattern=…)` — any named symbol.
- `procedure_address(procedure="name or 0x…")` — resolve a name or interior address to an entry.

## Map the call graph

- `procedure_callers(procedure=…)` — who reaches this, i.e. entry points.
- `procedure_callees(procedure=…)` — what it uses (network, filesystem, crypto, spawn APIs).
- `xrefs(address="0x…")` — every instruction referencing an address.

Callers/callees usually reveal a feature's shape before you read a single body.

## Read a procedure

- `procedure_info` — `basicblock_count`, `length`, `signature`, stack locals. Check first:
  keep `procedure_pseudo_code` under ~50 blocks (time scales badly). Most methods are 6–30.
- `procedure_pseudo_code(procedure=…)` — C-like output; lossy, needs interpretation.
- `procedure_assembly(procedure="name or 0x…")` — when pseudo-code hides constant loads,
  `+initialize`/`+load`, tail calls, or inline data.
- `list_procedure_info` / `list_procedure_size` / `current_procedure` — bulk/context helpers.

## Annotate as you go

Annotations persist for the session and show in the user's window. Record confirmed facts.

- `set_address_name(address, name)` / `set_addresses_names({address: name})` — rename
  `sub_…`; propagates to every reference. Empty string clears.
- `set_comment` / `set_inline_comment` — full-line or end-of-line notes.
- `set_bookmark(address, name)` / `unset_bookmark` / `list_bookmarks` — mark landmarks.
- `address_name` / `comment` / `inline_comment` — read existing annotations so a resumed
  document shows prior work instead of being relabeled over.

## Reading pseudo-code

- Objective-C renders manual-retain-release; `retain`/`release`/`autorelease` are bookkeeping.
  `objc_msgSend(obj, sel, …)` is a method call — read the selector as `[obj sel:…]`. Ivars
  appear as `*(self + 0x…)`.
- Swift shows `swift_retain`, witness/metadata calls, and mangled `$s…` names. Focus on the
  named calls. String and type names still show up in `search_strings`.

## Terminal context (often answers "why" fast)

```bash
codesign -d --entitlements :- /path/App.app   # sandbox / network / hardware access
otool -L /path/binary                          # linked libraries
plutil -p /path/App.app/Contents/Info.plist    # URL schemes, XPC names, min OS
xcrun swift-demangle '$s…'                      # decode a Swift symbol
```

On Apple Silicon most binaries are universal; pass `-arch arm64` (or `arm64e`) to
`otool`/`strings` for the native slice.
