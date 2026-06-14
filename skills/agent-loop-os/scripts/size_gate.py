#!/usr/bin/env python3
"""Implementation size gate for Agent Loop OS.

Made by sudal.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Callable


def parse_numstat(output: str) -> tuple[int, list[dict]]:
    total = 0
    files: list[dict] = []
    for line in output.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        added_raw, deleted_raw, path = parts[0], parts[1], parts[2]
        added = int(added_raw) if added_raw.isdigit() else 0
        deleted = int(deleted_raw) if deleted_raw.isdigit() else 0
        changed = added + deleted
        total += changed
        files.append({"path": path, "added": added, "deleted": deleted, "changed": changed})
    return total, files


def git_numstat(root: Path, cached: bool) -> tuple[int, list[dict]]:
    command = ["git", "diff", "--numstat"]
    if cached:
        command.insert(2, "--cached")
    result = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or "git diff --numstat failed")
    return parse_numstat(result.stdout)


def run_size_check(
    args,
    root: Path,
    append_event: Callable[[object, dict], None],
    now_iso: Callable[[], str],
    brand: str,
) -> int:
    unstaged_total, unstaged_files = git_numstat(root, cached=False)
    staged_total, staged_files = git_numstat(root, cached=True)
    total = unstaged_total + staged_total
    payload = {
        "date": now_iso(),
        "event": "SIZE_CHECK",
        "changed_lines": total,
        "preferred_max_lines": args.preferred_max,
        "hard_max_lines": args.hard_max,
        "staged_changed_lines": staged_total,
        "unstaged_changed_lines": unstaged_total,
        "made_by": "sudal",
    }

    if args.json:
        print(json.dumps({**payload, "files": staged_files + unstaged_files}, ensure_ascii=False, indent=2))
    else:
        print("Implementation size check")
        print(brand)
        print(f"Changed lines: {total}")
        print(f"Preferred: 200-{args.preferred_max}")
        print(f"Hard max: {args.hard_max}")

    if total > args.hard_max:
        event = {**payload, "event": "SIZE_LIMIT_EXCEEDED", "required_action": "TASK_SPLIT"}
        append_event(args, event)
        print("SIZE_LIMIT_EXCEEDED")
        print("TASK 분할 필요")
        print("Stop before Claude review. Do not relax the cap; split scope.")
        return 3

    if total > args.preferred_max:
        append_event(args, {**payload, "event": "SIZE_LIMIT_WARNING"})
        print("SIZE_LIMIT_WARNING")
        print("Consider splitting scope before implementation grows further.")
        return 0

    append_event(args, payload)
    print("SIZE_LIMIT_OK")
    return 0
