---
name: crash-debugging
description: Diagnose macOS and iOS crash reports by establishing build identity, symbolication quality, faulting path, and confidence before naming a root cause.
---

# Crash debugging

Diagnose first. Do not change code unless the user also asked for a fix.

## Establish evidence quality

1. Identify app version, build number, OS, architecture, timestamp, incident ID, and whether the report belongs to the build under discussion.
2. Read `Application Specific Information`, exception notes, termination reason, and any Last Exception Backtrace before interpreting ordinary frames.
3. Grade symbolication: **complete**, **partial**, or **absent**. Confirm that the binary and dSYM UUIDs match before trusting resolved names.
4. State what evidence is missing and what it prevents you from distinguishing.

## Follow the fault

- `EXC_BREAKPOINT` in Swift often indicates a runtime trap; use the runtime message to distinguish nil unwrap, bounds, and explicit precondition failures.
- `EXC_BAD_ACCESS` / `SIGSEGV` means invalid memory access; a near-zero address suggests nil, while other addresses may indicate lifetime or race failures.
- `SIGABRT` with an Objective-C exception is usually named in the exception reason and Last Exception Backtrace.
- `0x8badf00d` is a watchdog termination; find synchronous work blocking the watched process or extension.
- jetsam and `EXC_RESOURCE` are resource terminations; use memory, CPU, or I/O evidence rather than guessing from one frame.

Read the crashed thread bottom-up to the first relevant project frame. Check whether UI was touched off the main thread. Inspect recent history only after establishing the faulting files; recency is a lead, not proof.

## Symbolicate when needed

For local builds, find the matching dSYM beside the built product or in the archive. Compare UUIDs with `dwarfdump --uuid`. Use the current Xcode toolchain's documented symbolication route; if using `atos`, verify its local syntax and the image load address first.

## Report

Lead with one of: **confirmed root cause**, **best-supported diagnosis**, or **insufficient evidence**. Then name the trigger, mechanism, faulting component, supporting lines/frames, smallest plausible fix, and one verification. Separate alternative hypotheses and state the observation that would settle them.

If the minimal reproduction proves an Apple or framework defect, route the compatibility code through `os-workarounds`.
