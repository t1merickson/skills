#!/usr/bin/env python3
"""Validate and link this repository's skills into supported agent hosts.

Installed host directories are deployment targets, never authored source. Existing
directories are preserved in quarantine before replacement; unmanaged entries are left alone.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
from pathlib import Path
import re
import shutil
import sys
import tomllib


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = REPO_ROOT / "skillset.toml"
SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
IGNORED_TREE_NAMES = {".DS_Store"}


def load_manifest() -> tuple[dict[str, Path], list[dict[str, object]], dict[str, object]]:
    data = tomllib.loads(MANIFEST_PATH.read_text())
    if data.get("schema") != 1:
        raise ValueError(f"unsupported manifest schema: {data.get('schema')!r}")

    hosts: dict[str, Path] = {}
    for name, config in data.get("hosts", {}).items():
        override = os.environ.get(f"SKILLS_{name.upper()}_ROOT")
        raw = override or config["root"]
        hosts[name] = Path(os.path.expanduser(raw)).resolve(strict=False)

    skills = data.get("skills", [])
    if not isinstance(skills, list):
        raise ValueError("manifest 'skills' must be an array of tables")
    policy = data.get("policy", {})
    dependencies = data.get("dependencies", {})
    retired = data.get("retired", {})
    metadata: dict[str, object] = {
        "explicit": set(policy.get("explicit", [])),
        "volatile": set(policy.get("volatile", [])),
        "dependencies": {name: set(required) for name, required in dependencies.items()},
        "retired": {name: set(targets) for name, targets in retired.items()},
    }
    return hosts, skills, metadata


def lexical_exists(path: Path) -> bool:
    return os.path.lexists(path)


def tree_digest(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        if path.name in IGNORED_TREE_NAMES:
            continue
        rel = path.relative_to(root).as_posix()
        digest.update(rel.encode())
        if path.is_symlink():
            digest.update(b"L")
            digest.update(os.readlink(path).encode())
        elif path.is_file():
            digest.update(b"F")
            digest.update((path.stat().st_mode & 0o111).to_bytes(2, "big"))
            digest.update(path.read_bytes())
        elif path.is_dir():
            digest.update(b"D")
    return digest.hexdigest()


def classify(target: Path, source: Path) -> str:
    if not lexical_exists(target):
        return "missing"
    if target.is_symlink():
        if target.resolve(strict=False) == source.resolve(strict=False):
            return "canonical-link"
        return "other-link" if target.exists() else "broken-link"
    if target.is_dir():
        return "matching-copy" if tree_digest(target) == tree_digest(source) else "diverged-copy"
    return "non-directory"


def frontmatter(path: Path) -> tuple[dict[str, str], set[str], list[str]]:
    lines = path.read_text().splitlines()
    errors: list[str] = []
    if not lines or lines[0] != "---":
        return {}, set(), ["SKILL.md must start with ---"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, set(), ["SKILL.md has no closing --- for frontmatter"]

    values: dict[str, str] = {}
    keys: set[str] = set()
    block_key: str | None = None
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if match:
            key, value = match.group(1), (match.group(2) or "").strip()
            keys.add(key)
            values[key] = value.strip("\"'")
            block_key = key if value in {">", "|", ">-", "|-"} else None
        elif block_key and line.startswith((" ", "\t")) and line.strip():
            values[block_key] = f"{values[block_key]} {line.strip()}".strip()
    return values, keys, errors


def markdown_reference_errors(skill_root: Path) -> list[str]:
    errors: list[str] = []
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for markdown in skill_root.rglob("*.md"):
        text = markdown.read_text()
        # Examples often contain markdown-looking placeholders. They are not
        # repository references and should not fail validation.
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        text = re.sub(r"~~~.*?~~~", "", text, flags=re.DOTALL)
        text = re.sub(r"`[^`\n]*`", "", text)
        for raw in link_pattern.findall(text):
            target = raw.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "/")):
                continue
            resolved = (markdown.parent / target).resolve(strict=False)
            if not resolved.exists():
                errors.append(f"{markdown.relative_to(skill_root)}: missing relative reference {target}")
    return errors


def validate_manifest(
    hosts: dict[str, Path],
    skills: list[dict[str, object]],
    metadata: dict[str, object],
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    names: set[str] = set()
    sources: set[str] = set()

    for entry in skills:
        name = str(entry.get("name", ""))
        source_rel = str(entry.get("source", ""))
        target_hosts = entry.get("hosts", [])
        portable = bool(entry.get("portable", False))

        if not name or name in names:
            errors.append(f"duplicate or empty skill name: {name!r}")
            continue
        names.add(name)
        sources.add(source_rel)

        unknown_hosts = sorted(set(target_hosts) - set(hosts))
        if unknown_hosts:
            errors.append(f"{name}: unknown hosts {unknown_hosts}")

        source = REPO_ROOT / source_rel
        skill_file = source / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{name}: missing {source_rel}/SKILL.md")
            continue
        if source.name != name:
            errors.append(f"{name}: source directory must also be named {name!r}")

        values, keys, fm_errors = frontmatter(skill_file)
        errors.extend(f"{name}: {message}" for message in fm_errors)
        if values.get("name") != name:
            errors.append(f"{name}: frontmatter name is {values.get('name')!r}")
        description = values.get("description", "").strip(" >|-")
        if not description:
            errors.append(f"{name}: frontmatter description is missing or empty")
        if portable:
            extensions = sorted(keys - SPEC_FIELDS)
            if extensions:
                errors.append(f"{name}: portable skill uses host-specific frontmatter {extensions}")

        errors.extend(f"{name}: {message}" for message in markdown_reference_errors(source))
        line_count = len(skill_file.read_text().splitlines())
        if line_count > 500:
            warnings.append(f"{name}: SKILL.md is {line_count} lines; consider progressive disclosure")

    discovered = {
        path.parent.relative_to(REPO_ROOT).as_posix()
        for path in REPO_ROOT.glob("*/SKILL.md")
    }
    for source in sorted(discovered - sources):
        errors.append(f"unmanaged repo skill: {source}")
    for source in sorted(sources - discovered):
        errors.append(f"manifest source is not a root skill: {source}")

    explicit = set(metadata["explicit"])
    volatile = set(metadata["volatile"])
    dependencies = dict(metadata["dependencies"])
    retired = dict(metadata["retired"])
    for policy_name, policy_skills in (("explicit", explicit), ("volatile", volatile)):
        for name in sorted(policy_skills - names):
            errors.append(f"policy.{policy_name} names unmanaged skill: {name}")
    for name in sorted(set(dependencies) - names):
        errors.append(f"dependencies names unmanaged skill: {name}")
    for name, target_hosts in sorted(retired.items()):
        if name in names:
            errors.append(f"retired skill is still managed: {name}")
        unknown_hosts = sorted(set(target_hosts) - set(hosts))
        if unknown_hosts:
            errors.append(f"retired {name}: unknown hosts {unknown_hosts}")

    by_name = {str(entry["name"]): entry for entry in skills}
    for name, required in sorted(dependencies.items()):
        for dependency in sorted(required):
            if dependency not in names:
                errors.append(f"{name}: unknown dependency {dependency}")
                continue
            missing_hosts = sorted(set(by_name[name]["hosts"]) - set(by_name[dependency]["hosts"]))
            if missing_hosts:
                errors.append(f"{name}: dependency {dependency} is absent from hosts {missing_hosts}")

    for name, entry in by_name.items():
        source = REPO_ROOT / str(entry["source"])
        policy_file = source / "agents" / "openai.yaml"
        is_explicit = name in explicit
        declares_explicit = policy_file.is_file() and bool(
            re.search(r"^\s*allow_implicit_invocation:\s*false\s*$", policy_file.read_text(), re.MULTILINE)
        )
        if is_explicit and not declares_explicit:
            errors.append(f"{name}: explicit policy lacks agents/openai.yaml opt-out")
        if declares_explicit and not is_explicit:
            errors.append(f"{name}: agents/openai.yaml is explicit but manifest policy is not")
        if bool(entry.get("portable", False)) and "/Users/" in (source / "SKILL.md").read_text():
            warnings.append(f"{name}: portable SKILL.md contains a machine-specific /Users path")
    return errors, warnings


def selected_hosts(all_hosts: dict[str, Path], requested: str) -> list[str]:
    return sorted(all_hosts) if requested == "all" else [requested]


def command_check(
    hosts: dict[str, Path], skills: list[dict[str, object]], metadata: dict[str, object]
) -> int:
    errors, warnings = validate_manifest(hosts, skills, metadata)
    for warning in warnings:
        print(f"WARN  {warning}")
    for error in errors:
        print(f"ERROR {error}")
    if errors:
        print(f"\ncheck failed: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"check passed: {len(skills)} skills, {len(warnings)} warning(s)")
    return 0


def command_status(
    hosts: dict[str, Path],
    skills: list[dict[str, object]],
    metadata: dict[str, object],
    requested: str,
) -> int:
    chosen = selected_hosts(hosts, requested)
    width = max(len(str(entry["name"])) for entry in skills)
    print(f"{'skill':<{width}}  " + "  ".join(f"{host:<15}" for host in chosen))
    print(f"{'-' * width}  " + "  ".join("-" * 15 for _ in chosen))
    for entry in skills:
        name = str(entry["name"])
        source = REPO_ROOT / str(entry["source"])
        target_hosts = set(entry["hosts"])
        states = []
        for host in chosen:
            state = classify(hosts[host] / name, source) if host in target_hosts else "not-targeted"
            states.append(f"{state:<15}")
        print(f"{name:<{width}}  " + "  ".join(states))

    managed_names = {str(entry["name"]) for entry in skills} | set(metadata["retired"])
    for host in chosen:
        root = hosts[host]
        if not root.is_dir():
            print(f"\n{host}: target root does not exist yet: {root}")
            continue
        unmanaged = sorted(path.name for path in root.iterdir() if path.name not in managed_names)
        print(f"\n{host}: {len(unmanaged)} unmanaged entries left untouched in {root}")
    for name, target_hosts in sorted(dict(metadata["retired"]).items()):
        states = [host for host in chosen if host in target_hosts and lexical_exists(hosts[host] / name)]
        if states:
            print(f"retired entry still installed: {name} ({', '.join(states)})")
    print(f"\nexplicit invocation: {', '.join(sorted(metadata['explicit']))}")
    print(f"volatile guidance: {', '.join(sorted(metadata['volatile']))}")
    return 0


def unique_quarantine_path(root: Path, host: str, name: str) -> Path:
    candidate = root / host / name
    if not lexical_exists(candidate):
        return candidate
    index = 2
    while lexical_exists(candidate.with_name(f"{name}-{index}")):
        index += 1
    return candidate.with_name(f"{name}-{index}")


def move_then_link(target: Path, source: Path, backup: Path) -> None:
    backup.parent.mkdir(parents=True, exist_ok=True)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(target), str(backup))
    try:
        target.symlink_to(source, target_is_directory=True)
    except Exception:
        if lexical_exists(target):
            target.unlink()
        shutil.move(str(backup), str(target))
        raise


def command_link(
    hosts: dict[str, Path],
    skills: list[dict[str, object]],
    metadata: dict[str, object],
    requested: str,
    apply: bool,
    migrate_existing: bool,
    quarantine_arg: str | None,
) -> int:
    errors, warnings = validate_manifest(hosts, skills, metadata)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print("link aborted: repository check failed")
        return 1
    for warning in warnings:
        print(f"WARN  {warning}")

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    quarantine_root = Path(os.path.expanduser(quarantine_arg or f"~/.agent-skill-quarantine/{stamp}"))
    chosen = set(selected_hosts(hosts, requested))
    blocked = 0
    changed = 0

    for entry in skills:
        name = str(entry["name"])
        source = (REPO_ROOT / str(entry["source"])).resolve()
        for host in sorted(set(entry["hosts"]) & chosen):
            target = hosts[host] / name
            state = classify(target, source)
            if state == "canonical-link":
                print(f"KEEP    {host:<6} {name}")
                continue
            if state == "missing":
                print(f"LINK    {host:<6} {name} -> {source}")
                if apply:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.symlink_to(source, target_is_directory=True)
                    changed += 1
                continue

            backup = unique_quarantine_path(quarantine_root, host, name)
            if not migrate_existing:
                print(f"BLOCK   {host:<6} {name}: {state}; rerun with --migrate-existing to preserve and replace it")
                blocked += 1
                continue
            print(f"MIGRATE {host:<6} {name}: {state} -> {backup}")
            if apply:
                move_then_link(target, source, backup)
                changed += 1

    for name, target_hosts in sorted(dict(metadata["retired"]).items()):
        for host in sorted(set(target_hosts) & chosen):
            target = hosts[host] / name
            if not lexical_exists(target):
                print(f"ABSENT  {host:<6} {name} (retired)")
                continue
            backup = unique_quarantine_path(quarantine_root, host, name)
            if not migrate_existing:
                print(f"BLOCK   {host:<6} {name}: retired; rerun with --migrate-existing to preserve and remove it")
                blocked += 1
                continue
            print(f"RETIRE  {host:<6} {name} -> {backup}")
            if apply:
                backup.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(target), str(backup))
                changed += 1

    mode = "applied" if apply else "preview"
    print(f"\n{mode}: {changed if apply else 0} changed, {blocked} blocked")
    if not apply:
        print("No files changed. Add --apply after reviewing the preview.")
    elif changed and migrate_existing:
        print(f"Preserved replaced entries under {quarantine_root}")
    return 1 if blocked else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="validate the manifest and every source skill")

    status = sub.add_parser("status", help="compare canonical sources with installed targets")
    status.add_argument("--host", choices=["all", "claude", "codex"], default="all")

    link = sub.add_parser("link", help="preview or apply manifest-owned leaf symlinks")
    link.add_argument("--host", choices=["all", "claude", "codex"], default="all")
    link.add_argument("--apply", action="store_true", help="perform the previewed changes")
    link.add_argument(
        "--migrate-existing",
        action="store_true",
        help="move existing entries to quarantine before linking canonical source",
    )
    link.add_argument("--quarantine-root", help="override the dated quarantine directory")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        hosts, skills, metadata = load_manifest()
    except (OSError, KeyError, TypeError, ValueError, tomllib.TOMLDecodeError) as error:
        print(f"manifest error: {error}", file=sys.stderr)
        return 2

    if args.command == "check":
        return command_check(hosts, skills, metadata)
    if args.command == "status":
        return command_status(hosts, skills, metadata, args.host)
    return command_link(
        hosts,
        skills,
        metadata,
        args.host,
        args.apply,
        args.migrate_existing,
        args.quarantine_root,
    )


if __name__ == "__main__":
    raise SystemExit(main())
