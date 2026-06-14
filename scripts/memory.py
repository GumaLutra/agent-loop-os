#!/usr/bin/env python3
"""Shortcut for `loopos.py memory ...`.

Made by sudal.
"""

from pathlib import Path
import runpy
import sys


SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "agent-loop-os" / "scripts" / "loopos.py"
sys.argv = [sys.argv[0], "memory", *sys.argv[1:]]
runpy.run_path(str(SCRIPT), run_name="__main__")
