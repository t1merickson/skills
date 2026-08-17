---
name: crash-debugging
description: Diagnose macOS and iOS crash reports: read the log, symbolicate, name the root cause.
---

# crash-debugging

the user pastes a crash log and wants the root cause, not a tour of the file. read the log, name the cause in plain words, point at the code.

## read it in this order

1. **exception type and signal.** this alone narrows most crashes:
   - `EXC_BREAKPOINT` in a Swift frame: a Swift runtime trap — force-unwrapped nil, array out of bounds, a failed `precondition`. the message line often says which.
   - `EXC_BAD_ACCESS` / `SIGSEGV`: touched bad memory — use-after-free, dangling pointer, threading race. the hardest class; note the address (near-zero means nil deref).
   - `SIGABRT` with an ObjC exception: read the "Last Exception Backtrace" and the termination reason — "unrecognized selector" and "index beyond bounds" name themselves.
   - termination reason `0x8badf00d`: the watchdog killed it for blocking the main thread too long — the bug is whatever synchronous work is in the backtrace, not a crash at all.
   - jetsam / `EXC_RESOURCE`: killed for memory or CPU. profile, don't debug frame-by-frame.
2. **the crashed thread, bottom up.** walk to the first frame in OUR code and start there. frames in Apple frameworks below it are usually the symptom, not the cause.
3. **main-thread check.** UI touched off the main thread crashes in strange places. if the crashed thread isn't thread 0 but does UI work, that's likely the whole story.
4. **recent history.** `git log` the files in the faulting path. a crash that started this week usually has a commit from this week.

## symbolication

unsymbolicated frames (raw addresses) need the matching dSYM:

- find it: for local builds it's in DerivedData next to the .app; archived builds keep it in the .xcarchive.
- verify it matches: the UUIDs must agree — `dwarfdump --uuid <dSYM>` vs the binary UUID listed in the crash log's Binary Images section.
- resolve frames: `atos -o <dSYM path to DWARF binary> -arch arm64 -l <load address from Binary Images> <frame address>`.
- flags and tooling drift between Xcode versions; check `man atos` on first use rather than trusting memory.

## report shape

follow the `explaining-problems` skill: what the crashing component is, what triggers it, the mechanism in plain words, the smallest fix, one check after. include a reproduction if the log gives enough to construct one; say so plainly when it doesn't ("this needs the dSYM from build 214" or "this one needs a repro — the log alone can't distinguish X from Y").

never present a plausible-sounding cause as confirmed. "the crash is in the thumbnail cache eviction, and the two likely causes are A and B — here's the log line that would settle it" beats a confident guess.
