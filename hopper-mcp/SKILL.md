---
name: hopper-mcp
description: >
  Guide for reverse-engineering compiled macOS binaries using the Hopper Disassembler MCP
  Server. Use this skill whenever the user wants to inspect, analyze, decompile, or reverse
  engineer a macOS application or binary at the machine-code level. Triggers on: Hopper,
  disassembly, decompilation, reverse engineering, binary analysis, static analysis,
  understanding how an app works internally, "what does this app do", analyzing .app
  bundles, inspecting helper daemons and XPC services, examining Mach-O binaries, or any
  request involving the Hopper MCP tools. Also use when the user has a binary open in Hopper
  and asks questions about its behavior, classes, methods, or data flow.
---

# Reverse Engineering macOS Binaries with Hopper

Hopper's MCP tools read and navigate a binary the user has open in the Hopper app. You
drive; the user watches. Priorities: locate relevant code fast, interpret Hopper's output
without being misled by it, and separate confirmed findings from guesses.

Typical tasks: understanding what a background daemon does, auditing what data an app
collects or transmits, verifying a security or privacy claim, learning how a feature is
implemented, recovering an undocumented file format for interoperability. Scope is analysis
and documentation of behavior. If a request shifts to modifying software the user doesn't
own — bypassing licensing, defeating copy protection, patching out authentication — pause
and confirm intent first.

## Reporting to the user

Assume the user doesn't read assembly or know Objective-C runtime internals. Report
*behavior* ("on launch it scans /Applications for names matching a hardcoded keyword list")
over *mechanism* ("calls `objc_msgSend` with `contentsOfDirectoryAtPath:error:`"). Give
mechanism only when asked, or when it's the actual explanation for something they care about.

Two honesty rules:

- **"Can" vs "does."** A code path that uploads a file proves the binary *contains* the
  capability, not that it runs in normal use. State which you've established. Overclaiming
  from one decompiled function is the classic error, and it alarms the user when wrong.
- **Corroborate before asserting.** Pseudo-code is lossy and Hopper guesses. Before stating
  a conclusion, line up two or three agreeing signals — a string, its `xrefs`, and the
  `callees` of the function using it. One suggestive name is a lead, not a finding.

## Before you start

Confirm the target:

1. `current_document` — the active binary. Errors or empty → no document open.
2. `list_documents` — all open documents, if you need to choose.

If nothing's loaded, have the user open a binary and let Hopper finish analyzing (progress
bar at the bottom of its window). The MCP reads Hopper's analysis database; mid-analysis
results are partial and misleading.

### The cursor model

Hopper tracks a *current* document, procedure, and address, and most tools default to it
when the argument is omitted: `procedure_pseudo_code`, `procedure_info`, `procedure_assembly`,
`xrefs`, and the comment/name setters all fall back to current. Efficient loop: `goto_address`
(or `set_current_document`) once to park the cursor, then call a cluster of tools with no
arguments. `current_address`/`next_address`/`prev_address` move the cursor.

### Search, don't dump

`list_procedures`, `list_strings`, and `list_names` return the entire table — often tens of
thousands of entries; Hopper's docs advise against them. Use the `search_*` tools; fall back
to a full list only if a targeted search comes up empty. `list_segments` is the exception:
small, and worth reading early.

### Find the right binary in the bundle

In a `.app`, the interesting code is often not the main executable (frequently just the UI
shell):

- `Contents/MacOS/AppName` — main binary
- `Contents/Library/LoginItems/*` — background/login helpers
- `Contents/XPCServices/*.xpc` — privilege-separated services
- `Contents/Helpers/*`, `Contents/MacOS/*Helper` — auxiliary tools
- `Contents/Frameworks/*.framework` — shared logic, often the bulk of it
- `Contents/PlugIns/*` — extensions

If a feature isn't in the loaded binary, check these. Locate it before opening in Hopper:

```bash
grep -rl "keyword" /path/to/App.app/Contents 2>/dev/null   # which binary mentions it
strings -a /path/to/binary | grep -i "keyword"             # one binary's strings (see arch note)
```

## Analysis workflow

Broad to narrow. Establish vocabulary and structure before reading any single function.

### Phase 1 — Map the territory

**Strings first.** `search_strings` is the best starting point.

```
search_strings(pattern="keyword|Keyword|KEYWORD")   # regex; case_sensitive defaults false
```

Returns `{address: string}` and surfaces a feature's whole vocabulary: UI text, selector
names, class names, file paths, URLs, error messages, format strings. Each address is a
thread to pull with `xrefs`.

**Classes/methods.** Turn class names from the strings into procedures:

```
search_procedures(pattern="ClassName")   # returns {address: procedureName}
```

Scan method names to infer the class's responsibilities before reading one. `procedure_address(procedure="name or 0xADDR")`
resolves a name — or any interior address — to the entrypoint.

**Call graph without reading bodies:**

- `procedure_callers(procedure=…)` — callers → entry points, how a feature is reached
- `procedure_callees(procedure=…)` — callees → what it does (network, filesystem, crypto,
  `NSTask`/`posix_spawn`, `defaults`/preferences APIs)

Start at the plausible entry point, expand callees one level, and the feature's shape is
usually clear before reading pseudo-code.

**`list_segments` once.** Gives this binary's real section layout (names, address ranges,
writable/executable flags) so you're not guessing which section an address is in.

### Phase 2 — Read the code

**Gate on complexity.** `procedure_info` reports `basicblock_count`, `length`, the `signature`
(if recovered), and stack locals. Decompilation time scales badly with block count — Hopper
warns to keep `procedure_pseudo_code` under ~50 blocks. Most interesting methods are 6–30 and
process instantly. If it's large, use callees plus assembly of the key blocks instead of the
full run.

**Decompile.**

```
procedure_pseudo_code(procedure="name")   # or omit for the current procedure
```

C-like pseudo-code; needs interpretation (see "Reading the output").

**Assembly when pseudo-code hides or misleads** — `+initialize`/`+load`, constant-data loads,
tail calls, inline data:

```
procedure_assembly(procedure="name or 0xADDR")   # accepts an address, not just a name
```

### Phase 3 — Annotate as you go

Annotations persist for the session and are visible in the user's Hopper window. Record
confirmed facts to avoid re-deriving them.

- `set_address_name(address, name)` — rename `sub_100abcd` → `scanApplicationsForKeywords`;
  propagates everywhere it's referenced. Clear with an empty string. `set_addresses_names`
  takes an `{address: name}` map — the intended way to rename many at once.
- `set_comment(address, comment)` — full-line note above an address.
- `set_inline_comment(address, comment)` — short note at the end of an instruction's line.
- `set_bookmark(address, name)` — mark entry points and landmarks. `list_bookmarks` recalls
  them; `unset_bookmark(address)` removes one.

Read-side mirrors — `address_name`, `comment`, `inline_comment`, `list_bookmarks` — report
existing annotations, so a resumed document shows prior work instead of being relabeled over.

Clearing differs by tool: empty (or omitted) argument for the name/comment setters;
`unset_bookmark` for bookmarks.

### Phase 4 — Static data pseudo-code won't inline

Constant arrays, string tables, and lookup tables in `__DATA_CONST` don't appear in
pseudo-code.

1. `xrefs(address="0x…")` returns every instruction referencing the address.
2. In assembly, `adrp` + `add` forms a data pointer (page + offset); `adrp` + `ldr` loads
   *through* it. That's where a constant address is formed.
3. Pull the bytes from the terminal:

```bash
xcrun dyld_info -fixups /path/to/binary                    # resolved pointer targets
otool -s __DATA_CONST __objc_arraydata /path/to/binary     # dump a section
```

**Chained fixups:** arm64 Mach-O rebases pointers in `__DATA*` using chained fixups — the raw
8-byte on-disk value is *encoded* (packed with rebase/bind metadata), not a usable address.
Read raw, it's garbage. `xcrun dyld_info -fixups` prints the resolved targets.

## Reading the output

### Objective-C (MRC-style noise)

Hopper renders Objective-C in manual-retain-release style; roughly half the lines are
bookkeeping.

- **`retain`/`release`/`autorelease`** — memory management. Ignore; the logic is the calls
  between them.
- **`objc_msgSend(obj, sel, args…)`** — a method call. The selector is the payload, shown as
  `@selector(foo:bar:)` or a `sel_` symbol. Read as `[obj foo:… bar:…]`.
- **Fast enumeration** — `for (x in collection)` expands into a
  `countByEnumeratingWithState:objects:count:` loop with a mutation guard. Read as for-each.
- **Ivar access** — `*(self + 0x20)`, `self->field`, `self[0x…]` are ivar reads at byte
  offsets. Map offset → field via the ivar list (`__objc_const` metadata, or ivar name strings
  via `search_strings`). Offset `0x0` is `isa`; real ivars follow.
- **Callee-saved registers** — `r19`–`r28` / `x19`–`x28` shown as locals are just variables;
  the register names are a decompilation artifact.
- **Blocks** — a struct whose `invoke` field is a function pointer; follow it for the closure
  body. Captured variables sit in the struct's later fields.

### Swift (the modern default — don't assume ObjC)

Most current apps are Swift or mixed. Tells: `swift_retain`/`swift_release`/`swift_bridgeObject*`,
witness-table and metadata-accessor calls, symbol names starting `$s`/`_$s` (or older `_T`).

- **Demangle:** `swift demangle '$s…'` or pipe assembly through `xcrun swift-demangle`.
  `_$s4MyApp10NetworkKitC4sendyyF` → `MyApp.NetworkKit.send()`.
- Swift string literals and type/field names still appear in `search_strings` and the
  `__swift5_*` sections; only the function names are mangled until demangled.
- Value types are passed in registers and copied by value-witness functions, so pseudo-code
  looks busier than the ObjC equivalent. Focus on the named calls.

### Common constants

`NSString` search/compare options are bitmask ints:

| Value | Meaning |
|---|---|
| `0x1` | case-insensitive (`NSCaseInsensitiveSearch`) |
| `0x2` | literal, no Unicode normalization (`NSLiteralSearch`) |
| `0x4` | backwards (`NSBackwardsSearch`) |
| `0x8` | anchored — prefix/suffix match (`NSAnchoredSearch`) |
| `0x9` | case-insensitive + anchored |

For an unfamiliar magic constant, check whether it's a known option-set or errno before
treating it as data.

## Mach-O sections

`list_segments` gives this binary's real layout; this table is what common ObjC/Swift sections
hold when an address lands in one:

| Section | Contents |
|---|---|
| `__cstring` | plain C strings |
| `__cfstring` | constant `NSString`/`CFString` objects (pointer + length, not the bytes) |
| `__objc_methname` | selector strings |
| `__objc_classname` | class name strings |
| `__objc_const` | class metadata: method lists, ivar lists, protocol lists |
| `__objc_selrefs` / `__objc_classrefs` | selector/class reference pointers (indirection) |
| `__objc_arraydata` | constant array element storage |
| `__swift5_types` / `__swift5_proto` / `__swift5_fieldmd` | Swift type, protocol-conformance, field metadata |
| `__DATA_CONST` | const pointers subject to chained fixups (Phase 4) |

## Terminal commands

```bash
# Locate a feature in a bundle
grep -rl "keyword" /path/to/App.app/Contents
strings -a /path/to/binary | grep -i "keyword"

# Bundle / entitlement / signing context (often answers "why" faster than code)
codesign -d --entitlements :- /path/to/App.app       # sandbox, network, hardware access
otool -L /path/to/binary                             # linked libraries → capabilities
plutil -p /path/to/App.app/Contents/Info.plist       # URL schemes, XPC names, min OS

# Symbols and data
xcrun dyld_info -exports /path/to/binary             # exported symbols
xcrun dyld_info -fixups  /path/to/binary             # resolved chained-fixup pointers
otool -s __SEG __sect    /path/to/binary             # raw section dump
xcrun swift-demangle '$s…'                           # decode Swift symbol names

# Package receipts
/usr/bin/lsbom -sf /path/to/Archive.bom
```

**Architecture:** on Apple Silicon most binaries are universal (fat) with `x86_64` and
`arm64`/`arm64e` slices. Pass `-arch arm64` (or `arm64e`) to `otool`/`strings`/`dyld_info` to
work the native slice.

## Scenario playbook

- **How does the app do X?** — Phase 1 keyword search; the strings usually name the class.
  Confirm with `callers`/`callees`, then read the entry point.
- **What data does it collect or transmit?** — search URL patterns (`https?://`), HTTP verbs,
  analytics/telemetry SDK names, `JSONSerialization`, `URLSession`. Trace `callees` on the
  network methods to see the payload. State whether the path is reachable in normal use or
  only present in the binary.
- **Why does it behave unexpectedly under condition Y?** — find the entry point and trace the
  conditional logic. Error/log strings sit near branch points and usually name the condition.
- **What files does it touch?** — search strings for path fragments: `Application Support`,
  `Preferences`, `Caches`, `Library`, `~/`, `.plist`, bundle IDs. Cross-check the filesystem
  APIs in the relevant callees.
- **Auditing capabilities and data handling** — start with `codesign --entitlements` and
  `otool -L` (they bound what the app *can* do), then confirm the relevant capabilities in
  code. Report capability and evidence separately.

## Multiple documents

Work one document at a time. `set_current_document` switches the active one; keep Hopper in
the foreground when switching and prefer distinct document names, since similar names confuse
the MCP's lookup. If results look like they're from the wrong binary, re-check
`current_document` before trusting anything downstream.
