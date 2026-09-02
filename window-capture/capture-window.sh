#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: capture-window.sh <CGWindowID> <new-output.png>" >&2
  exit 64
fi
if [[ ! "$1" =~ ^[0-9]+$ ]]; then
  echo "CGWindowID must be numeric" >&2
  exit 64
fi

window_id="$1"
output="$2"
if [[ -e "$output" ]]; then
  echo "refusing to overwrite existing output: $output" >&2
  exit 73
fi

created=false
cleanup_failed_capture() {
  if [[ "$created" == true && -e "$output" ]]; then
    rm -f -- "$output"
  fi
}
trap cleanup_failed_capture EXIT

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
row="$(swift "$script_dir/windowid.swift" --id "$window_id" | tail -n 1)"
expected_size="$(printf '%s\n' "$row" | awk -F '\t' '{print $2}')"
expected_width="${expected_size%x*}"
expected_height="${expected_size#*x}"

if [[ ! "$expected_width" =~ ^[0-9]+$ || ! "$expected_height" =~ ^[0-9]+$ ]]; then
  echo "could not establish window bounds; capture refused" >&2
  exit 65
fi

screencapture -o -l "$window_id" "$output"
created=true

actual_width="$(sips -g pixelWidth "$output" | awk '/pixelWidth:/ {print $2}')"
actual_height="$(sips -g pixelHeight "$output" | awk '/pixelHeight:/ {print $2}')"
if [[ ! "$actual_width" =~ ^[0-9]+$ || ! "$actual_height" =~ ^[0-9]+$ ]]; then
  echo "could not verify capture dimensions; removed unsafe output" >&2
  exit 74
fi

matches_scale() {
  local scale="$1"
  local target_width=$((expected_width * scale))
  local target_height=$((expected_height * scale))
  local width_delta=$((actual_width - target_width))
  local height_delta=$((actual_height - target_height))
  (( width_delta < 0 )) && width_delta=$((-width_delta))
  (( height_delta < 0 )) && height_delta=$((-height_delta))
  (( width_delta <= 8 && height_delta <= 8 ))
}

if ! matches_scale 1 && ! matches_scale 2; then
  echo "capture dimensions did not match the requested window; removed unsafe output" >&2
  exit 74
fi

created=false
printf '%s\n' "$output"
