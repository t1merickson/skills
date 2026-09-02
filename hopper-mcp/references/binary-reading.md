# Reading macOS binaries

## Objective-C noise

- Treat retain/release/autorelease as ownership bookkeeping unless lifetime is the question.
- Read `objc_msgSend(obj, selector, args...)` through the selector name.
- Recognize expanded fast-enumeration loops and mutation guards as collection iteration.
- Map ivar offsets through Objective-C metadata before naming fields.
- Follow a block's invoke pointer to its closure body.

## Swift

Swift/mixed binaries expose runtime retains, metadata accessors, witness tables, and mangled symbols. Demangle with `xcrun swift-demangle`. Search `__swift5_*` metadata and strings for types/fields. Value-witness and bridging calls add noise; focus on recovered named calls and corroborated data flow.

## Mach-O and static data

Use `list_segments` for the actual layout. Common evidence lives in `__cstring`, `__cfstring`, Objective-C method/class/const/reference sections, Swift type/protocol/field metadata, and `__DATA_CONST`.

ARM64 `adrp` plus `add` often forms a pointer; `adrp` plus `ldr` loads through one. Chained fixups encode rebase/bind metadata in on-disk pointer words, so raw 8-byte values may be meaningless as addresses. Use `xcrun dyld_info -fixups` for resolved targets and `otool -s` for section bytes.

## Terminal context

Useful read-only commands include:

```bash
codesign -d --entitlements :- <app>
otool -L <binary>
plutil -p <app>/Contents/Info.plist
xcrun dyld_info -exports <binary>
xcrun dyld_info -fixups <binary>
otool -s <segment> <section> <binary>
xcrun swift-demangle '<symbol>'
```

Confirm the selected architecture in universal binaries. Entitlements and linked libraries bound capability; they do not prove execution. Hash target artifacts and record the slice/build identity when findings must be reproducible.
