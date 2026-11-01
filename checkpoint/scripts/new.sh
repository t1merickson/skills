#!/usr/bin/env bash
# Scaffold a checkpoint file with the prescribed header, filename, and section order.
# Usage: new.sh <task-slug> "<scope: goal and altitude>" [project-root]
# Prints the path. Refuses to overwrite. Adds checkpoints/ to .gitignore unless the
# repo already tracks checkpoints (opt-in by prior convention).
set -euo pipefail

if [[ $# -lt 2 || $# -gt 3 ]]; then
  echo "usage: new.sh <task-slug> \"<scope>\" [project-root]" >&2
  exit 64
fi

slug="$1"
scope="$2"
root="${3:-$PWD}"

if [[ ! "$slug" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "slug must be lowercase kebab-case: got '$slug'" >&2
  exit 64
fi

root="$(cd -- "$root" && pwd)"
dir="$root/checkpoints"
mkdir -p "$dir/archive"

date_day="$(date +%F)"
date_min="$(date '+%F %H:%M')"
file="$dir/$date_day-$slug.md"

if [[ -e "$file" ]]; then
  echo "exists, not overwriting: $file" >&2
  exit 73
fi

cat > "$file" <<MD
Task: $slug · Written: $date_min · Scope: $scope

## Now

## Plates

## Terrain

## Decided

## Discards

## Live wires
MD

# gitignore unless the repo already tracks checkpoints
if git -C "$root" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if [[ -z "$(git -C "$root" ls-files checkpoints 2>/dev/null)" ]]; then
    gi="$root/.gitignore"
    if ! grep -qxF 'checkpoints/' "$gi" 2>/dev/null; then
      printf 'checkpoints/\n' >> "$gi"
      echo "added checkpoints/ to .gitignore" >&2
    fi
  else
    echo "repo tracks checkpoints; leaving .gitignore alone" >&2
  fi
fi

printf '%s\n' "$file"
