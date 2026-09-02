#!/usr/bin/env python3
"""Extract a bounded, path-anonymized Claude transcript corpus as JSONL."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


def text_content(content: object) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts: list[str] = []
    for item in content:
        if isinstance(item, str):
            parts.append(item)
        elif isinstance(item, dict) and item.get("type") in {"text", "input_text", "output_text"}:
            value = item.get("text")
            if isinstance(value, str):
                parts.append(value)
    return "\n".join(parts)


def transcript_id(path: Path) -> str:
    return hashlib.sha256(str(path.resolve()).encode()).hexdigest()[:12]


def extract(path: Path, max_chars: int) -> tuple[list[dict[str, object]], int]:
    records: list[dict[str, object]] = []
    malformed = 0
    for line_number, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
        try:
            raw = json.loads(line)
        except json.JSONDecodeError:
            malformed += 1
            continue
        message = raw.get("message") if isinstance(raw, dict) else None
        if not isinstance(message, dict):
            continue
        role = message.get("role")
        if role not in {"user", "assistant"}:
            continue
        text = text_content(message.get("content"))
        if not text:
            continue
        records.append(
            {
                "transcript": transcript_id(path),
                "line": line_number,
                "timestamp": raw.get("timestamp"),
                "role": role,
                "model": raw.get("model") or message.get("model"),
                "text": text[:max_chars],
                "truncated": len(text) > max_chars,
            }
        )
    return records, malformed


def modified_time(path: Path) -> float:
    try:
        return path.stat().st_mtime
    except OSError:
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("~/.claude/projects").expanduser())
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--max-chars", type=int, default=4000)
    args = parser.parse_args()
    if args.limit < 1 or args.max_chars < 1:
        parser.error("--limit and --max-chars must be positive")
    if not args.root.is_dir():
        parser.error(f"transcript root does not exist: {args.root}")

    paths = sorted(args.root.rglob("*.jsonl"), key=modified_time, reverse=True)
    malformed = 0
    unreadable = 0
    emitted = 0
    for path in paths[: args.limit]:
        try:
            records, skipped = extract(path, args.max_chars)
        except OSError as error:
            unreadable += 1
            print(f"skipped unreadable transcript {transcript_id(path)}: {error}", file=sys.stderr)
            continue
        malformed += skipped
        for record in records:
            print(json.dumps(record, ensure_ascii=False))
            emitted += 1
    print(
        f"extracted {emitted} messages from {min(len(paths), args.limit)} transcripts; "
        f"skipped {malformed} malformed lines and {unreadable} unreadable transcripts",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
