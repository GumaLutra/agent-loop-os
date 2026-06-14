#!/usr/bin/env python3
"""Print Agent Loop OS review prompts.

Made by sudal.
"""

from pathlib import Path
import runpy
import sys


SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "agent-loop-os" / "scripts" / "loopos.py"

if len(sys.argv) == 1:
    sys.argv = [sys.argv[0], "template", "full-review"]
elif sys.argv[1] in {"request", "full-review"}:
    sys.argv = [sys.argv[0], "template", "full-review", *sys.argv[2:]]
elif sys.argv[1] == "rebuttal":
    sys.argv = [sys.argv[0], "template", "rebuttal", *sys.argv[2:]]
else:
    print("Usage: python scripts/review.py [request|rebuttal]", file=sys.stderr)
    raise SystemExit(2)

runpy.run_path(str(SCRIPT), run_name="__main__")
