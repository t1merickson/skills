---
name: hopper-mcp
description: >
  Guide for reverse engineering macOS binaries using the Hopper Disassembler MCP Server.
  Use this skill whenever the user wants to analyze, reverse engineer, disassemble, or
  decompile a macOS application or binary. Triggers on: Hopper, disassembly, decompilation,
  binary analysis, reverse engineering macOS apps, understanding how an app works internally,
  "what does this app do", analyzing .app bundles, inspecting helper daemons, examining
  Mach-O binaries, or any request involving the Hopper MCP tools. Also use when the user
  has a binary open in Hopper and asks questions about its behavior, classes, methods, or
  data flow.
---

# Reverse Engineering macOS Binaries with Hopper

You have access to Hopper Disassembler's MCP tools, which let you read and navigate
disassembled/decompiled binary code. This skill teaches you how to use those tools
effectively and how to communicate your findings clearly to the user.

## Communicating with the user

The user likely does not know assembly language, Objective-C runtime internals, or
binary formats. Your job is to be the expert and translate what you find into clear,
plain-language explanations. When you discover what a method does, explain its *behavior*
("this function scans your Applications folder for apps matching certain keywords")
rather than its implementation details ("this calls objc_msgSend with selector
contentsOfDirectoryAtPath:error:").

Use implementation details only when the user specifically asks for them or when they
help explain *why* something behaves a certain way.

## Before you start

### Verify Hopper is ready

Always begin by confirming you can talk to Hopper and that the right binary is loaded:

1. Call `list_documents` to see what's open
2. Call `current_document` to confirm which binary is active

If nothing is open, tell the user they need to open a binary in Hopper first and wait
for its analysis to complete (the status bar at the bottom of Hopper shows progress).

### Multiple documents

Prefer working with one document at a time. Hopper 6.2.5 fixed a crash when switching
documents while the app was minimised, but having multiple documents with similar names
can still cause confusion in the MCP's document lookup. If you do need to switch, make
sure Hopper is in the foreground and the document names are distinct.

### Finding the right binary

For macOS .app bundles, the interesting code is often NOT in the main app binary. Helpers,
daemons, and XPC services live inside the bundle:

- `MyApp.app/Contents/MacOS/MyApp` — often just the UI shell
- `MyApp.app/Contents/Library/LoginItems/...` — background daemons
- `MyApp.app/Contents/XPCServices/...` — XPC service helpers
- `MyApp.app/Contents/Frameworks/...` — shared framework code

If the user asks about a specific feature and you can't find it in the loaded binary,
suggest they check these other locations. A quick terminal command can help:

```bash
strings -arch arm64 /path/to/binary | grep -i "keyword"
```

## The analysis workflow

Work through these phases in order. Each phase builds on the previous one.

### Phase 1: Discovery — Map the territory

Start broad. Your goal is to understand what's in this binary before diving into any
specific method.

**Step 1: Search strings for keywords**

`search_strings` is your most valuable starting tool. Search for words related to
whatever the user is asking about:

```
search_strings pattern="keyword|Keyword|KEYWORD"
```

This returns UI text, class names, method selectors, file paths, error messages — the
vocabulary of the feature. It gives you a roadmap before you decompile anything.

**Step 2: Find relevant classes and methods**

Once you have class names from the string search, use `search_procedures` to find all
methods on those classes:

```
search_procedures pattern="ClassName"
```

This returns every method with its address. Scan the method names to understand the
class's responsibilities before decompiling.

**Step 3: Understand the call graph**

Use `procedure_callees` and `procedure_callers` to map relationships without
decompiling everything:

- `procedure_callees` — "what does this method call?" (shows dependencies)
- `procedure_callers` — "who calls this method?" (shows entry points)

Start with the method that looks like the main entry point for the feature, check its
callees, and you'll have the full call tree.

### Phase 2: Decompilation — Read the code

Now you know which methods matter. Time to read them.

**Always check complexity first**

Before decompiling, call `procedure_info` and check `basicblock_count`. Methods with
more than 50 basic blocks can take a very long time to decompile. Most interesting
methods have 6-30 blocks and decompile instantly.

```
procedure_info procedure="methodName"
```

If a method has >50 blocks, mention this to the user and consider whether you really
need the full decompilation or whether `procedure_callees` gives enough insight.

**Decompile with `procedure_pseudo_code`**

This is your primary tool. It produces C-like pseudo-code from the binary:

```
procedure_pseudo_code procedure="methodName"
```

The output requires interpretation — see "Reading decompiled output" below.

**Fall back to assembly when needed**

When the pseudo-code is ambiguous (especially for `+initialize` methods or constant
data references), use `procedure_assembly` to see the actual instructions:

```
procedure_assembly procedure="methodName"
```

### Phase 3: Data extraction

Some information lives in static data sections that the MCP cannot read directly.

**Tracing data references**

Use `xrefs` to find where a constant or data address is referenced:

```
xrefs address="0x100040728"
```

**Reading static data from the binary**

The Hopper MCP cannot read raw data sections (constant arrays, string tables stored as
data). When you need this data:

1. Get the address from assembly — look for the `adrp` + `add` instruction pattern
   that loads a data pointer
2. Use terminal tools to extract it:
   ```bash
   xcrun dyld_info -fixups /path/to/binary
   ```

Modern arm64 Mach-O binaries use **chained fixup rebasing** — pointers stored in
`__DATA_CONST` sections are encoded and won't make sense if read raw. The `dyld_info`
command shows the actual resolved targets.

## Reading decompiled output

Hopper's pseudo-code for Objective-C uses Manual Reference Counting (MRC) style, which
adds a lot of noise. Here's how to read through it:

### Ignore retain/release

About half the lines will be `retain`, `release`, or `autorelease` calls. These are
memory management bookkeeping — skip them entirely and focus on the actual method calls
between them.

### Fast enumeration loops

The decompiler expands `for (id item in collection)` into a verbose pattern using
`countByEnumeratingWithState:objects:count:`. When you see this pattern, just read it
as a simple for-each loop.

### Instance variable access

`self[0x1]`, `self[0x2]`, etc. are instance variable (ivar) accesses at byte offsets.
The decompiler can't always resolve ivar names, so you see these numeric offsets instead.
Cross-reference with the class's ivar list (visible in `search_strings` or the ObjC
metadata) to figure out what each offset corresponds to.

### Register reuse

`r19` through `r28` are callee-saved registers that the decompiler often shows as local
variables. They're just regular variables — the register names are an artifact of
decompilation.

### Common constants

NSString search method options often appear as bitmask integers:
- `0x1` = case-insensitive search
- `0x4` = backwards search
- `0x8` = anchored search (prefix/suffix match)
- `0x9` = case-insensitive + anchored

## Useful terminal commands

When the MCP tools aren't enough, these commands help fill gaps:

```bash
# Find which binary in an .app bundle contains a feature
strings -arch arm64 /path/to/binary | grep -i "keyword"

# Dump a specific section's contents
otool -arch arm64 -s __DATA_CONST __cfstring /path/to/binary

# Resolve chained fixup pointers (essential for static data)
xcrun dyld_info -fixups /path/to/binary

# List exports
xcrun dyld_info -exports /path/to/binary

# Read BOM files (package receipts)
/usr/bin/lsbom -sf /path/to/Archive.bom
```

Always specify `-arch arm64` on Apple Silicon Macs — binaries are often universal
(fat) with both x86_64 and arm64 slices, and you want the native one.

## Key Mach-O sections for ObjC data

When you encounter addresses in these sections, here's what they contain:

| Section | What's stored there |
|---|---|
| `__objc_methname` | Method name strings (selectors) |
| `__cfstring` | Constant NSString/CFString objects |
| `__cstring` | Plain C strings |
| `__objc_const` | Class metadata, method lists |
| `__objc_classname` | Class name strings |
| `__objc_arraydata` | Constant array element storage |

## Tips for specific scenarios

**"How does this app do X?"** — Start with Phase 1 discovery using keywords related
to X. The string search will usually reveal the relevant classes immediately.

**"What data does this app collect/send?"** — Search for URL patterns, HTTP method
strings, analytics keywords. Check `procedure_callees` on network-related methods to
see what data they package up.

**"Why does this app behave strangely when..."** — Find the feature's entry point
method, decompile it, and trace the conditional logic. Look for error strings near
branch points — they often explain what condition triggers each code path.

**"What files does this app read/write?"** — Search strings for file paths, directory
names, and common path components like `Application Support`, `Preferences`, `Caches`,
`Library`.
