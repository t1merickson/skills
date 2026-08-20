---
name: crash-debugging
description: Diagnose macOS and iOS crash reports: read the log, symbolicate, name the root cause.
---

# crash-debugging

The user pastes a crash log and wants the root cause, not a tour of the file. Read the log, name the cause in plain words, point at the code.

## Read it in this order

1. **Exception type and signal.** This alone narrows most crashes:
   - `EXC_BREAKPOINT` in a Swift frame: a Swift runtime trap — force-unwrapped nil, array out of bounds, a failed `precondition`. The message line often says which.
   - `EXC_BAD_ACCESS` / `SIGSEGV`: touched bad memory — use-after-free, dangling pointer, threading race. The hardest class; note the address (near-zero means nil deref).
   - `SIGABRT` with an ObjC exception: read the "Last Exception Backtrace" and the termination reason — "unrecognized selector" and "index beyond bounds" name themselves.
   - termination reason `0x8badf00d`: the watchdog killed it for blocking the main thread too long — the bug is whatever synchronous work is in the backtrace, not a crash at all.
   - jetsam / `EXC_RESOURCE`: killed for memory or CPU. Profile, don't debug frame-by-frame.
2. **The crashed thread, bottom up.** Walk to the first frame in OUR code and start there. Frames in Apple frameworks below it are usually the symptom, not the cause.
3. **Main-thread check.** UI touched off the main thread crashes in strange places. If the crashed thread isn't thread 0 but does UI work, that's likely the whole story.
4. **Recent history.** `git log` the files in the faulting path. A crash that started this week usually has a commit from this week.

## Symbolication

Unsymbolicated frames (raw addresses) need the matching dSYM:

- Find it: for local builds it's in DerivedData next to the .app; archived builds keep it in the .xcarchive.
- Verify it matches: the UUIDs must agree — `dwarfdump --uuid <dSYM>` vs the binary UUID listed in the crash log's Binary Images section.
- Resolve frames: `atos -o <dSYM path to DWARF binary> -arch arm64 -l <load address from Binary Images> <frame address>`.
- Flags and tooling drift between Xcode versions; check `man atos` on first use rather than trusting memory.

## Report shape

Follow the `explaining-problems` skill: what the crashing component is, what triggers it, the mechanism in plain words, the smallest fix, one check after. Include a reproduction if the log gives enough to construct one; say so plainly when it doesn't ("this needs the dSYM from build 214" or "this one needs a repro — the log alone can't distinguish X from Y").

When the root cause turns out to be Apple's — a framework defect, not our code — prove it and tag the workaround per the `os-workarounds` skill, so the verdict survives in the codebase.

Never present a plausible-sounding cause as confirmed. "the crash is in the thumbnail cache eviction, and the two likely causes are A and B — here's the log line that would settle it" beats a confident guess.
