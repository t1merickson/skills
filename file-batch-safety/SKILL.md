---
name: file-batch-safety
description: Guardrails for scripts and commands that move, delete, rename, copy, or dedupe many real files on Tim's Mac. Use BEFORE writing or running any batch file operation, cleanup script, dedupe pass, or bulk reorganization — the traps here have caused real file loss on this machine.
---

# file-batch-safety

These rules were learned through actual lost files. Read them before the first batch operation of a session, not after something goes wrong.

## Policies (non-negotiable)

- **Duplicates don't mean delete.** Identical bytes don't mean Tim wanted the copy gone — where a file sits carries intent. Report duplicates (paths, sizes, hashes); delete only with his explicit OK for that specific operation.
- **Quarantine instead of `rm`.** Move to a clearly-named quarantine directory; tell Tim where it is and how to restore.
- **No recursive delete for cleanup.** Never `shutil.rmtree` a directory you only assume is empty. Use `os.rmdir` — it fails loudly if you're wrong.
- **Adversarial pass before running.** Before a script touches many real files, trace 2–3 input shapes that could break the logic — not just the case that motivated the script. Ask Tim about worst-case inputs when unsure.
- **Backup before batch.** A reversible action taken and reported beats a question asked and waited on.

## macOS traps

- **NFD filenames.** APFS/HFS+ returns decomposed Unicode (`ç` = `c` + combining cedilla); Python string literals are NFC. They print identically but compare unequal, so a naive `.replace()` or `==` silently misses. Normalize with `unicodedata.normalize("NFD", name)` (and strip combining marks if matching loosely) before comparing.
- **Case-insensitive paths.** Default APFS/HFS+ is case-insensitive: `Foo/` and `foo/` can be the *same* file. Before renaming onto an existing name or deduping, confirm they're actually different files with `os.path.samefile` — an md5 match between two spellings of one file proves nothing.
- **Don't walk a tree you're moving into.** `os.walk` over a destination re-finds just-moved files and flags them as duplicates of themselves — a file gets deleted as its own copy. Collect all sources first, then move. Guard `realpath(src) == realpath(dst)`. Never auto-delete on an md5 match between what might be the same inode.
