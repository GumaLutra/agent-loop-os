# Agent Loop OS Base Principles

Made by sudal.

Use these rules for any AI-agent task that is more than a trivial edit.

## Thinking

- Start with the conclusion and the next action.
- Diagnose from observed clues before proposing a fix.
- Prefer the cheapest useful measurement before a risky change.
- Do not claim a root cause that was not inspected.
- Prefer hypotheses that explain every observed clue. A likely cause that leaves one clue unexplained is not the lead diagnosis yet.
- Separate confidence levels: observed, likely, possible, and unverified.
- When several causes are plausible, name the one measurement that best separates them before changing state.
- Keep explanations readable; do not compress away important reasoning.

## Execution

- Split large work into small, checkable stories.
- Keep coding tasks near 200-300 lines when practical.
- If expected code exceeds 500 lines, split the work into smaller tasks before implementation.
- Prefer JSON for operational data: task state, memory, review records, risk briefs, and verification reports.
- Keep evidence for each meaningful step.
- Preserve unrelated user changes.
- Treat commands, tests, screenshots, logs, inspected files, and diffs as evidence.
- Do not call work complete because the edit was made. Completion requires verification.

## Review

- Use Solo Loop when only one agent is available.
- Use Full Loop when an external reviewer is available or risk is high.
- Classify every review item by severity before deciding what to do.
- Classify decisions as `ACCEPT`, `REJECT`, `DEFER`, or `LATER`.
- Log non-critical findings as `LATER` when the current task is safe to use and verification passes.
- Spend extra rounds only on critical findings.
- Fix accepted items and verify again.

## Memory

- Record repeated mistakes as prevention rules.
- Keep memory short and actionable.
- Use memory before similar work to create a risk brief.
