# Review Gate Pipeline Pack

Made by sudal.

Use this pack when implementation should move through tests, external review, and severity-based revision without wasting rounds.

## Pipeline

```text
Run tests -> Run Claude/external review -> PASS -> next step
Run tests -> Run Claude/external review -> REVISION_REQUIRED -> classify severity
non-critical -> Later Backlog -> next step
critical -> fix loop -> run tests again -> review again if risk remains
```

## Gate Meanings

`PASS` means:

- tests or the closest practical verification passed
- Claude or the external reviewer found no critical issue
- any remaining issue is safe to use now or logged as `LATER`

`REVISION_REQUIRED` means:

- a test failed
- verification is missing or weak for a risky change
- the reviewer found a critical issue
- the current task is not safe to use as-is

## Required Order

1. Run the planned tests or closest real verification.
2. Run Claude, another AI, or human review with the evidence attached.
3. If the review returns `PASS`, continue to the next step.
4. If the review returns `REVISION_REQUIRED`, classify every finding as `critical` or `non-critical`.
5. Send non-critical findings to the later backlog.
6. Fix only critical findings in the current loop.
7. Re-run the failed tests or the closest verification after each critical fix.

## Rule

Do not start another review round just because non-critical work exists. Start another round only when a critical finding, failed test, missing safety check, or user decision requires it.
