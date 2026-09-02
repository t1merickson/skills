# Hopper MCP workflow

## Cursor and search

Hopper tracks a current document, procedure, and address. Park it with `set_current_document` or `goto_address`, then call related info, pseudo-code, assembly, and xref tools without repeatedly resolving the same address.

Prefer `search_strings`, `search_procedures`, and targeted names. `list_segments` is small and useful early; full lists of strings/procedures/names can be enormous and should be fallback evidence.

Typical sequence:

1. `search_strings` for user-visible text, selectors, paths, URLs, format strings, and errors.
2. `xrefs` from a promising address.
3. `procedure_address` and `procedure_info` for the owning function.
4. `procedure_callers` to locate entry paths and `procedure_callees` to identify filesystem, network, crypto, process, or preferences effects.
5. `procedure_pseudo_code` for manageable functions; `procedure_assembly` for hidden details.

Decompilation cost rises quickly with control-flow complexity. For very large functions, inspect key blocks and named callees instead of requesting one giant pseudo-code result.

## Bundle triage

Check common locations:

- `Contents/MacOS/` main and auxiliary executables;
- `Contents/XPCServices/`;
- `Contents/Library/LoginItems/`;
- `Contents/Helpers/`;
- `Contents/Frameworks/`;
- `Contents/PlugIns/` and extensions.

Use targeted `strings` searches across candidate binaries to locate the component before loading more documents.

## Persistent annotations

`set_address_name`, `set_comment`, `set_inline_comment`, and `set_bookmark` modify the Hopper analysis document. Read existing annotations first on resumed work. Use a batch rename only for confirmed mappings. Clear names/comments through their documented empty value and bookmarks through `unset_bookmark`.
