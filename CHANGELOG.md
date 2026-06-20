# Changelog

Made by sudal.

## 0.1.1 - 2026-06-21

- Added the review gate pipeline: run tests, run Claude or external review, continue on `PASS`, and classify `REVISION_REQUIRED` findings by severity.
- Clarified that non-critical `REVISION_REQUIRED` findings go to the later backlog while only critical findings enter the fix loop.
- Added AI-facing instructions and templates for `PASS` vs `REVISION_REQUIRED` review status.

## 0.1.0 - 2026-06-21

- Added severity-gated loop policy: non-critical findings are logged as `LATER` and do not force extra review rounds when the current task is safe to use.
- Added critical-only escalation: critical findings drive round 2, user decision before round 3, and stop for user decision after unresolved rounds 4-5.
- Added `later.jsonl` backlog support through `loopos.py later add/list`.
- Added diagnostic and round policy fields to JSON templates and defaults.
- Updated AI-facing packs and prompts to classify findings by severity before deciding whether to continue, fix, defer, or log for later.
