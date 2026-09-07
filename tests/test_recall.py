"""Run with python3 -m unittest discover -s tests. Made by sudal."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/agent-loop-os/scripts/recall.py"
spec = importlib.util.spec_from_file_location("recall", SCRIPT)
recall = importlib.util.module_from_spec(spec)
spec.loader.exec_module(recall)


class RecallTest(unittest.TestCase):
    def test_exact_root_and_no_body_disclosure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            notes = root / "notes"
            notes.mkdir()
            a, b = root / "Desktop/project", root / "Documents/project"
            (notes / "correct.md").write_text(f"project_root: {a}\nPrivate body marker", encoding="utf-8")
            (notes / "wrong.md").write_text(f"project_root: {b}\nmentions {a}", encoding="utf-8")
            (notes / "example.md").write_text(f"project_root: {b}\n\n```\nproject_root: {a}\n```", encoding="utf-8")
            (notes / "conflict.md").write_text(f"project_root: {b}\nproject_root: {a}\n", encoding="utf-8")
            (notes / "link.md").symlink_to(notes / "correct.md")
            output = recall.context(recall.canonical(a), notes)
            self.assertIn("correct.md", output)
            self.assertNotIn("wrong.md", output)
            self.assertNotIn("link.md", output)
            self.assertNotIn("example.md", output)
            self.assertNotIn("conflict.md", output)
            self.assertIn("conflicting", output)
            self.assertNotIn("Private body marker", output)
            self.assertEqual(len(list(notes.iterdir())), 5)

    def test_missing_and_unreadable_store(self):
        with tempfile.TemporaryDirectory() as tmp:
            notes = Path(tmp) / "missing"
            self.assertIn("unavailable", recall.context(tmp, notes))
            self.assertFalse(notes.exists())
            notes.mkdir()
            (notes / "bad.md").write_bytes(b"\xff")
            self.assertIn("incomplete", recall.context(tmp, notes))

    def test_hook_contracts_and_ambiguous_root(self):
        for host in ("claude", "codex", "cursor"):
            result = subprocess.run([sys.executable, str(SCRIPT), "--hook", host],
                                    input=json.dumps({"hook_event_name": "UserPromptSubmit"}),
                                    text=True, capture_output=True, check=True)
            data = json.loads(result.stdout)
            if host == "cursor":
                message = data["additional_context"]
            else:
                self.assertEqual(data["hookSpecificOutput"]["hookEventName"], "UserPromptSubmit")
                message = data["hookSpecificOutput"]["additionalContext"]
            self.assertIn("ambiguous", message)


if __name__ == "__main__":
    unittest.main()
