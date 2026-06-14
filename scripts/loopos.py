#!/usr/bin/env python3
"""Repository-level wrapper for the Agent Loop OS CLI.

Made by sudal.
"""

from pathlib import Path
import runpy


SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "agent-loop-os" / "scripts" / "loopos.py"
runpy.run_path(str(SCRIPT), run_name="__main__")
