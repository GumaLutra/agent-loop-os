#!/usr/bin/env python3
"""Agent Loop OS local memory and task helper.

Made by sudal.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompt_templates import get_template
from size_gate import run_size_check


BRAND = "Made by sudal."
STATE_DIR = ".agent-loop-os"
MEMORY_FILE = "memory.jsonl"
EVENTS_FILE = "events.jsonl"
TASK_DIR = "tasks"
PREFERRED_MAX_LINES = 300
HARD_MAX_LINES = 500


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9가-힣]+", "-", value)
    value = value.strip("-")
    return value[:60] or "task"


def root_path(args: argparse.Namespace) -> Path:
    return Path(args.root).resolve()


def state_path(args: argparse.Namespace) -> Path:
    return root_path(args) / STATE_DIR


def memory_path(args: argparse.Namespace) -> Path:
    return state_path(args) / MEMORY_FILE


def events_path(args: argparse.Namespace) -> Path:
    return state_path(args) / EVENTS_FILE


def ensure_state(args: argparse.Namespace) -> Path:
    state = state_path(args)
    (state / TASK_DIR).mkdir(parents=True, exist_ok=True)
    memory = memory_path(args)
    if not memory.exists():
        memory.write_text("", encoding="utf-8")
    events = events_path(args)
    if not events.exists():
        events.write_text("", encoding="utf-8")
    readme = state / "README.md"
    if not readme.exists():
        readme.write_text(
            dedent(
                f"""\
                # Agent Loop OS State

                {BRAND}

                This directory stores local task briefs and repeated-mistake memory.

                - `memory.jsonl`: one memory entry per line
                - `events.jsonl`: gate events such as SIZE_LIMIT_EXCEEDED
                - `tasks/`: generated task briefs

                Commit this directory only when your team wants shared process memory.
                """
            ),
            encoding="utf-8",
        )
    return state


def load_memory(args: argparse.Namespace) -> list[dict]:
    ensure_state(args)
    entries: list[dict] = []
    for line_number, line in enumerate(memory_path(args).read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            entries.append(json.loads(stripped))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Invalid JSON in memory line {line_number}: {exc}") from exc
    return entries


def append_memory(args: argparse.Namespace, entry: dict) -> None:
    ensure_state(args)
    with memory_path(args).open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")


def append_event(args: argparse.Namespace, entry: dict) -> None:
    ensure_state(args)
    with events_path(args).open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")


def cmd_init(args: argparse.Namespace) -> int:
    state = ensure_state(args)
    print(f"Initialized Agent Loop OS at {state}")
    print(BRAND)
    return 0


def cmd_size_check(args: argparse.Namespace) -> int:
    ensure_state(args)
    return run_size_check(args, root_path(args), append_event, now_iso, BRAND)


def cmd_task_start(args: argparse.Namespace) -> int:
    ensure_state(args)
    split_required = args.estimated_lines > HARD_MAX_LINES
    over_preferred = args.estimated_lines > PREFERRED_MAX_LINES
    if split_required and not args.allow_oversize:
        print("Task split required.")
        print(BRAND)
        print(f"Estimated lines: {args.estimated_lines}")
        print(f"Hard max lines: {HARD_MAX_LINES}")
        print("Split this work into smaller tasks before implementation.")
        return 2

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    filename = f"{timestamp}-{slugify(args.title)}.md"
    path = state_path(args) / TASK_DIR / filename
    content = dedent(
        f"""\
        # Task Brief

        {BRAND}

        Mode: {args.mode}
        Task type: {args.type}
        Title: {args.title}
        Date: {now_iso()}

        ## Goal

        {args.goal or ""}

        ## Scope

        {args.scope or ""}

        ## Non-Goals

        {args.non_goals or ""}

        ## Risk Brief

        Code budget:

        ```text
        estimated_lines: {args.estimated_lines}
        preferred_max_lines: {PREFERRED_MAX_LINES}
        hard_max_lines: {HARD_MAX_LINES}
        over_preferred: {str(over_preferred).lower()}
        split_required: {str(split_required).lower()}
        ```

        Run:

        ```bash
        python skills/agent-loop-os/scripts/loopos.py risk --type {args.type}
        ```

        ## Stories

        - [ ] Story 1:
          - Evidence expected:
        - [ ] Final verification:
          - Evidence expected:

        ## Verification Criteria

        {args.verification or ""}

        ## Evidence Log

        - 

        ## Review Response

        ACCEPT:
        REJECT:
        DEFER:

        ## Memory Update

        - 
        """
    )
    path.write_text(content, encoding="utf-8")
    (state_path(args) / "active-task.txt").write_text(str(path), encoding="utf-8")
    print(f"Created task brief: {path}")
    return 0


def cmd_risk(args: argparse.Namespace) -> int:
    entries = load_memory(args)
    relevant = [entry for entry in entries if args.type == "all" or entry.get("task_type") == args.type]
    relevant = relevant[-args.limit :]

    print("Risk brief")
    print(BRAND)
    print(f"Task type: {args.type}")

    if not relevant:
        print("- No relevant memory found.")
        print("- Use the standard verification gate for this task type.")
        return 0

    counts = Counter(entry.get("mistake_type", "unknown") for entry in relevant)
    print("\nTop repeated patterns:")
    for mistake, count in counts.most_common(5):
        print(f"- {mistake}: {count}")

    print("\nPrevention rules:")
    seen: set[str] = set()
    for entry in reversed(relevant):
        lesson = entry.get("lesson")
        if lesson and lesson not in seen:
            print(f"- {lesson}")
            seen.add(lesson)
        if len(seen) >= 5:
            break
    return 0


def cmd_memory_add(args: argparse.Namespace) -> int:
    entry = {
        "date": now_iso(),
        "task_type": args.type,
        "mistake_type": args.mistake,
        "lesson": args.lesson,
        "severity": args.severity,
        "source": args.source,
        "evidence": args.evidence or "",
        "task": args.task or "",
        "made_by": "sudal",
    }
    append_memory(args, entry)
    print("Added memory entry:")
    print(json.dumps(entry, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


def cmd_memory_list(args: argparse.Namespace) -> int:
    entries = load_memory(args)
    if args.type != "all":
        entries = [entry for entry in entries if entry.get("task_type") == args.type]
    if args.mistake:
        entries = [entry for entry in entries if entry.get("mistake_type") == args.mistake]
    entries = entries[-args.limit :]

    if args.json:
        print(json.dumps(entries, ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    if not entries:
        print("No memory entries found.")
        return 0

    for entry in entries:
        print(f"- [{entry.get('task_type')}] {entry.get('mistake_type')}: {entry.get('lesson')}")
        if entry.get("evidence"):
            print(f"  evidence: {entry.get('evidence')}")
    return 0


def cmd_template(args: argparse.Namespace) -> int:
    print(get_template(args.name))
    print()
    print(BRAND)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Agent Loop OS local task and memory helper.")
    parser.add_argument("--root", default=".", help="Project root where .agent-loop-os is stored.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize .agent-loop-os state.")
    init_parser.set_defaults(func=cmd_init)

    size_parser = subparsers.add_parser("size", help="Implementation size gates.")
    size_sub = size_parser.add_subparsers(dest="size_command", required=True)
    size_check = size_sub.add_parser("check", help="Check git diff --numstat changed lines.")
    size_check.add_argument("--preferred-max", type=int, default=PREFERRED_MAX_LINES)
    size_check.add_argument("--hard-max", type=int, default=HARD_MAX_LINES)
    size_check.add_argument("--json", action="store_true")
    size_check.set_defaults(func=cmd_size_check)

    task_parser = subparsers.add_parser("task", help="Task helpers.")
    task_sub = task_parser.add_subparsers(dest="task_command", required=True)
    task_start = task_sub.add_parser("start", help="Create a task brief.")
    task_start.add_argument("--mode", choices=["solo", "full"], required=True)
    task_start.add_argument("--type", required=True, help="Task type such as ui, data, deploy, debug, docs.")
    task_start.add_argument("--title", required=True)
    task_start.add_argument("--goal", default="")
    task_start.add_argument("--scope", default="")
    task_start.add_argument("--non-goals", default="")
    task_start.add_argument("--verification", default="")
    task_start.add_argument("--estimated-lines", type=int, default=0)
    task_start.add_argument("--allow-oversize", action="store_true", help="Create the brief even when estimated lines exceed the hard max.")
    task_start.set_defaults(func=cmd_task_start)

    risk_parser = subparsers.add_parser("risk", help="Print a risk brief from memory.")
    risk_parser.add_argument("--type", default="all")
    risk_parser.add_argument("--limit", type=int, default=20)
    risk_parser.set_defaults(func=cmd_risk)

    memory_parser = subparsers.add_parser("memory", help="Memory ledger helpers.")
    memory_sub = memory_parser.add_subparsers(dest="memory_command", required=True)
    memory_add = memory_sub.add_parser("add", help="Append a memory entry.")
    memory_add.add_argument("--type", required=True)
    memory_add.add_argument("--mistake", required=True)
    memory_add.add_argument("--lesson", required=True)
    memory_add.add_argument("--severity", choices=["low", "medium", "high"], default="medium")
    memory_add.add_argument("--source", default="self-review")
    memory_add.add_argument("--evidence", default="")
    memory_add.add_argument("--task", default="")
    memory_add.set_defaults(func=cmd_memory_add)

    memory_list = memory_sub.add_parser("list", help="List memory entries.")
    memory_list.add_argument("--type", default="all")
    memory_list.add_argument("--mistake", default="")
    memory_list.add_argument("--limit", type=int, default=20)
    memory_list.add_argument("--json", action="store_true")
    memory_list.set_defaults(func=cmd_memory_list)

    template_parser = subparsers.add_parser("template", help="Print copy-paste prompts.")
    template_parser.add_argument("name", choices=["solo", "full-review", "rebuttal"])
    template_parser.set_defaults(func=cmd_template)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
