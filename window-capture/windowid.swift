// Lists CoreGraphics window ids for on-screen app windows.
//
// Usage:  swift windowid.swift [owner-substring] [--titles]
//         swift windowid.swift --id <CGWindowID>
//
// Prints id / size / owner, one per line. Window titles are OFF by default —
// on a shared daily-driver machine a title is often a document or folder name,
// and the id plus owner is enough to pick a window. Pass --titles only when an
// app has several windows and you need to disambiguate.
//
// The id printed here is the CGWindowID that `screencapture -l` expects. It is
// NOT the same number AppleScript/Accessibility reports as `id of window 1`;
// passing that one makes screencapture silently capture the whole screen.

import CoreGraphics
import Foundation

let args = Array(CommandLine.arguments.dropFirst())
let showTitles = args.contains("--titles")
let idIndex = args.firstIndex(of: "--id")
let requestedID: Int? = idIndex.flatMap { index in
    let valueIndex = args.index(after: index)
    guard valueIndex < args.endIndex else { return nil }
    return Int(args[valueIndex])
}
if idIndex != nil && requestedID == nil {
    FileHandle.standardError.write(Data("--id requires a numeric CoreGraphics window id\n".utf8))
    exit(64)
}
let filter = idIndex == nil
    ? args.first(where: { !$0.hasPrefix("--") })?.lowercased()
    : nil

guard let list = CGWindowListCopyWindowInfo(
    [.optionOnScreenOnly, .excludeDesktopElements], kCGNullWindowID
) as? [[String: Any]] else {
    FileHandle.standardError.write(Data("could not read the window list\n".utf8))
    exit(1)
}

var rows: [String] = []

for w in list {
    guard let owner = w[kCGWindowOwnerName as String] as? String,
          let id = w[kCGWindowNumber as String] as? Int else { continue }

    if let requestedID, id != requestedID { continue }
    if let filter, !owner.lowercased().contains(filter) { continue }

    // Layer 0 is a normal application window; menus, shadows, and status
    // overlays live on other layers and are never what we want to capture.
    guard (w[kCGWindowLayer as String] as? Int ?? -1) == 0 else { continue }

    var width = 0, height = 0
    if let b = w[kCGWindowBounds as String] as? [String: Any] {
        width  = Int(b["Width"]  as? Double ?? 0)
        height = Int(b["Height"] as? Double ?? 0)
    }
    // Drop tooltips, popovers, and 1x1 helper windows.
    guard width > 120, height > 120 else { continue }

    var row = "\(id)\t\(width)x\(height)\t\(owner)"
    if showTitles, let name = w[kCGWindowName as String] as? String, !name.isEmpty {
        row += "\t\(name)"
    }
    rows.append(row)
}

guard !rows.isEmpty else {
    let detail = requestedID.map { " for id \($0)" }
        ?? filter.map { " for \"\($0)\"" }
        ?? ""
    print("no matching on-screen windows" + detail)
    exit(2)
}

print("id\tsize\towner" + (showTitles ? "\ttitle" : ""))
rows.forEach { print($0) }
