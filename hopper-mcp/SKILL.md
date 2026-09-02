---
name: hopper-mcp
description: Operate Hopper Disassembler through its MCP server only when the user explicitly asks to inspect a binary in Hopper or invokes this skill. Do not trigger merely because a task mentions reverse engineering.
---

# Hopper MCP

Use only for an explicit Hopper/binary-inspection request. Generic words such as reverse engineering, decompilation, interoperability, app behavior, or binary format are not enough to activate this skill.

Hopper's tools navigate an analysis database the user has open. The job is to locate relevant code quickly, interpret lossy output without being seduced by plausible pseudo-code, and separate confirmed behavior from attractive guesses.

## Establish the target

1. Confirm the binary/bundle, architecture, provenance, and question.
2. Use `current_document` and `list_documents` to prove which Hopper document is active.
3. Wait for Hopper's initial analysis to finish; partial analysis produces false absences.
4. For an app bundle, determine whether the behavior lives in the main executable, XPC service, login item, helper, framework, or extension before interpreting a missing result. The main executable is often only the UI shell.

Work one document at a time and recheck it whenever results appear inconsistent.

## Search broad, trace narrow

Read [references/tool-workflow.md](references/tool-workflow.md).

- Start with targeted strings, names, selectors, classes, URLs, paths, and error text. Avoid dumping global procedure/string tables.
- Follow cross-references to candidate functions, then use callers to find how a feature is reached and callees to find what it can affect. A feature's shape is often visible in the call graph before its pseudo-code is readable.
- Inspect function size/blocks before decompiling. Use assembly when pseudo-code loses control flow, constants, dispatch, or pointer indirection.
- Read bundle metadata, entitlements, linked libraries, and exports as capability context—not proof that a path executes.
- For static pointer tables and chained fixups, use platform tooling that resolves encoded on-disk pointers; raw bytes may not be addresses.

Annotate or rename inside Hopper only when useful and within the user's request. Prefer comments that state evidence and uncertainty. Do not turn a tentative hypothesis into a persistent symbol name.

## Evidence discipline

Separate:

- **present:** code/data exists in this binary;
- **reachable:** a known entry path can call it;
- **observed:** runtime evidence shows it executed;
- **inferred:** the best explanation, not yet corroborated.

Corroborate material findings with independent signals such as string + xref + caller/callee, metadata + implementation, or static path + runtime observation. One suggestive name is a lead, not a finding. Hopper pseudo-code and symbol recovery are lossy.

Read [references/binary-reading.md](references/binary-reading.md) for Objective-C, Swift, Mach-O, and terminal details. Read [references/scenarios.md](references/scenarios.md) for common investigations.

## Report behavior first

Lead with behavior in plain language, then supply mechanism where it explains the result. “It scans this directory on launch” is usually more useful than opening with an `objc_msgSend` signature. State target binary/architecture, evidence grade, path to the relevant code, corroborating signals, uncertainty, and the next check that would upgrade confidence. Distinguish what the app can do from what it does in normal use—the classic overclaim is finding an upload path and reporting that normal use uploads data without proving reachability or observation.

When documenting a format or interface for interoperability, separate observed bytes/calls from proposed semantics and preserve representative hashes/offsets so another analyst can reproduce the claim.
