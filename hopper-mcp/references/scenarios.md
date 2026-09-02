# Investigation scenarios

## How is a feature implemented?

Search its UI/error vocabulary, identify classes/functions through xrefs, trace callers to entry and callees to effects, then read the smallest function that answers the question.

## What data can leave the app?

Search hosts, URL paths, HTTP verbs, serialization, telemetry SDKs, and session APIs. Trace payload construction and call reachability. Distinguish a linked SDK, dormant code path, reachable path, and runtime-observed request.

## What files or processes does it touch?

Search path fragments, extensions, bundle IDs, launch-service names, command strings, and filesystem/process APIs. Cross-check sandbox entitlements, XPC boundaries, and helpers.

## Why does condition Y change behavior?

Find the entry point, then inspect branches around condition/error strings. Compare constants and preferences to runtime/bundle context. Do not infer user-visible causality from a nearby branch without reachability evidence.

## Undocumented format for interoperability

Collect multiple legitimate samples, hashes, file sizes, headers, offsets, and version context. Trace parse/write routines in both directions. Record confirmed fields separately from hypotheses and create a minimal parser fixture that rejects unsupported variants honestly.
