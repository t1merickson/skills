---
name: file-batch-safety
description: Read before any batch file operation — moving, deleting, renaming, or deduping many files. Real file loss lives here.
---

# file-batch-safety

These rules were learned through actual lost files. Read them before the first batch operation of a session, not after something goes wrong.

## Policies (non-negotiable)

- **Duplicates don't mean delete.** Identical bytes don't mean the user wanted the copy gone — where a file sits carries intent. Report duplicates (paths, sizes, hashes); delete only with their explicit OK for that specific operation.
- **Quarantine instead of `rm`.** Move to a clearly-named quarantine directory; tell the user where it is and how to restore.
- **No recursive delete for cleanup.** Never `shutil.rmtree` a directory you only assume is empty. Use `os.rmdir` — it fails loudly if you're wrong.
- **Adversarial pass before running.** Before a script touches many real files, trace 2–3 input shapes that could break the logic — not just the case that motivated the script. Ask the user about worst-case inputs when unsure.
- **Backup before batch.** A reversible action taken and reported beats a question asked and waited on.
- **Read-only volumes.** When the user names a disk or directory as a backup, an archive, or "real data" (their backup drives, Patreon archive content), treat it as read-only: no moves, no renames, no cleanup, no "helpful" reorganization. Reading is fine; extracting is done to a temp location outside it. This has come up on real backup disks where loss would be unrecoverable — when in doubt about a volume's status, ask before the first write, not after.

## macOS traps

- **NFD filenames.** APFS/HFS+ returns decomposed Unicode (`ç` = `c` + combining cedilla); Python string literals are NFC. They print identically but compare unequal, so a naive `.replace()` or `==` silently misses. Normalize with `unicodedata.normalize("NFD", name)` (and strip combining marks if matching loosely) before comparing.
- **Case-insensitive paths.** Default APFS/HFS+ is case-insensitive: `Foo/` and `foo/` can be the *same* file. Before renaming onto an existing name or deduping, confirm they're actually different files with `os.path.samefile` — an md5 match between two spellings of one file proves nothing.
- **Don't walk a tree you're moving into.** `os.walk` over a destination re-finds just-moved files and flags them as duplicates of themselves — a file gets deleted as its own copy. Collect all sources first, then move. Guard `realpath(src) == realpath(dst)`. Never auto-delete on an md5 match between what might be the same inode.

## Preflight and reconciliation

Before a real batch, record a manifest: source roots, target roots, item count, total bytes, free space, symlinks, and whether the move crosses filesystems. A cross-filesystem move is copy-then-delete rather than an atomic rename; verify the copy before removing the source. Cloud placeholders and offline files are not fully present merely because a directory entry exists.

Afterward, reconcile against that manifest: every source accounted for, expected target count and bytes, quarantine present, and no unexpected paths. Report counts and the undo location. A command exiting zero is not the reconciliation.
