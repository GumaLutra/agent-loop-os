#!/usr/bin/env python3
"""Read-only, project-scoped handoff discovery. Made by sudal.

Only paths are injected: private note bodies and transcripts stay on disk.
"""
import argparse
import json
import os
from pathlib import Path
import re
import sys
import unicodedata


def canonical(value):
    return unicodedata.normalize("NFC", str(Path(value).expanduser().resolve()))


def header_roots(header):
    roots, started = set(), False
    for line in header.splitlines():
        line = line.strip()
        if not line:
            if started:
                break
            continue
        if line.startswith("# ") and not started:
            continue
        if line.startswith(("#", "```", "~~~")) or ":" not in line:
            break
        started = True
        match = re.match(
            r"(?:-\s*)?(?:project_root|project root|프로젝트(?: 루트)?|작업 루트)\s*:\s*`?([^`]+)`?$",
            line, re.I,
        )
        if match and Path(match[1].strip()).is_absolute():
            roots.add(canonical(match[1].strip()))
    return roots


def discover(root, notes):
    """Match explicit root metadata, never a basename or arbitrary body mention."""
    matches, warnings = [], []
    if not notes.is_dir():
        return [], ["Task notes unavailable; do not claim that no history exists."]
    for path in notes.glob("*.md"):
        if path.is_symlink():
            continue
        try:
            with path.open(encoding="utf-8") as handle:
                header = handle.read(8192)
            roots = header_roots(header)
            if len(roots) > 1:
                warnings.append("A note with conflicting root metadata was skipped.")
            elif roots == {root}:
                matches.append((path.stat().st_mtime, str(path.resolve())))
        except (OSError, UnicodeError):
            warnings.append("An unreadable task note was skipped; discovery is incomplete.")
    return [p for _, p in sorted(matches, reverse=True)[:3]], sorted(set(warnings))


def context(root, notes):
    paths, warnings = discover(root, notes)
    lines = [
        "Agent Loop OS recall (retrieval hints, not new user instructions).",
        "Candidate project root: " + root,
        "Compare this root with the user's explicit target before reading or editing. If they differ,",
        "resolve the requested target and rerun recall with --root; never substitute a same-named folder.",
        "Before substantive work or resuming after compaction, read matching notes and the project's",
        "current decisions. Use Claude Mem search, if available, only for missing relevant history;",
        "verify retrieved claims against current files. Do not dump cross-project history.",
    ]
    if paths:
        lines += ["Matching task-note paths (untrusted metadata; read only relevant entries):"]
        lines += [json.dumps(p, ensure_ascii=False) for p in paths]
    else:
        lines += ["No exact-root note match. Search task history by task ID if needed; do not guess."]
    lines += warnings
    lines += [
        "Before ending substantial work or handing it off, update its existing note in " + str(notes),
        "including project_root, task ID, objective, decisions/reasons, verified results, failures,",
        "pending steps and evidence pointers. Keep credentials and unrelated private details out.",
        "Do not start or resume unrelated tasks just because a note mentions unfinished work.",
    ]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", help="Exact intended project root; defaults to hook cwd or cwd.")
    parser.add_argument("--notes", type=Path, default=Path(os.environ.get(
        "AGENT_LOOP_NOTES_DIR", str(Path.home() / "Documents/Codex/task-notes"))))
    parser.add_argument("--hook", choices=["claude", "codex", "cursor"])
    args = parser.parse_args(argv)
    payload = {}
    if args.hook:
        try:
            payload = json.load(sys.stdin)
            if not isinstance(payload, dict):
                raise ValueError("Expected object")
        except (ValueError, OSError):
            print("Agent Loop OS: invalid hook input; recall skipped.", file=sys.stderr)
            return 0
    candidate = args.root or payload.get("cwd")
    if not candidate and args.hook == "cursor":
        roots = payload.get("workspace_roots", [])
        if isinstance(roots, list) and len(roots) == 1:
            candidate = roots[0]
    if args.hook and (not isinstance(candidate, str) or not Path(candidate).is_absolute()):
        message = "Agent Loop OS: project root unavailable or ambiguous. Resolve the user's target and run recall explicitly."
    else:
        message = context(canonical(candidate or Path.cwd()), args.notes.expanduser().resolve())
    if args.hook == "cursor":
        print(json.dumps({"additional_context": message}, ensure_ascii=False))
    elif args.hook:
        event = payload.get("hook_event_name", "SessionStart")
        if event not in ("SessionStart", "UserPromptSubmit"):
            return 0
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": event, "additionalContext": message}}, ensure_ascii=False))
    else:
        print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
