# Full Loop OS Pack

Made by sudal.

Use when another AI agent, human, Cursor, Claude, or separate Codex thread can review.

## Loop

```text
Planner -> Builder -> Tests -> External Reviewer -> PASS or REVISION_REQUIRED -> Rebuttal & Patch -> Verification -> Memory
```

## Builder Responsibilities

- State goal, scope, non-goals, and verification criteria.
- Estimate coding size. Keep 200-300 lines when practical; split before implementation if expected code exceeds 500 lines.
- Implement narrowly.
- Run tests or the closest practical verification before review.
- Provide reviewer with the task, changed files, evidence, and known limitations.
- Do not hide uncertainty.

## Reviewer Responsibilities

- Find actionable defects, not style preferences.
- Focus on bugs, missed requirements, missing verification, risky assumptions, and repeated mistakes.
- Order findings by severity.
- Mark each finding as `critical` or `non-critical`.
- Return `PASS` when no critical issue remains.
- Return `REVISION_REQUIRED` when a critical issue, failed test, or missing risky verification remains.
- Say when no material issue was found.

## Rebuttal Responsibilities

For each review finding:

```text
ACCEPT: valid; fixed; verification evidence.
REJECT: invalid; evidence from code/log/test/requirement.
DEFER: valid but out of scope; concrete follow-up.
LATER: non-critical; safe to use now; recorded in later backlog.
```

Only critical findings force another review round. Non-critical findings should be logged as `LATER` when verification passes and the requested workflow is safe to use.

If the gate status is `PASS`, continue to the next step. If it is `REVISION_REQUIRED`, classify severity first; log non-critical findings as later and fix critical findings in the current loop.

## Finish

The final response must include:

- accepted/rejected/deferred counts
- later count
- verification evidence
- memory updates or "No new repeated mistake"
