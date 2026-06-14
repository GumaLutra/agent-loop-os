# Full Loop OS Pack

Made by sudal.

Use when another AI agent, human, Cursor, Claude, or separate Codex thread can review.

## Loop

```text
Planner -> Builder -> External Reviewer -> Rebuttal & Patch -> Verification -> Memory
```

## Builder Responsibilities

- State goal, scope, non-goals, and verification criteria.
- Estimate coding size. Keep 200-300 lines when practical; split before implementation if expected code exceeds 500 lines.
- Implement narrowly.
- Provide reviewer with the task, changed files, evidence, and known limitations.
- Do not hide uncertainty.

## Reviewer Responsibilities

- Find actionable defects, not style preferences.
- Focus on bugs, missed requirements, missing verification, risky assumptions, and repeated mistakes.
- Order findings by severity.
- Say when no material issue was found.

## Rebuttal Responsibilities

For each review finding:

```text
ACCEPT: valid; fixed; verification evidence.
REJECT: invalid; evidence from code/log/test/requirement.
DEFER: valid but out of scope; concrete follow-up.
```

## Finish

The final response must include:

- accepted/rejected/deferred counts
- verification evidence
- memory updates or "No new repeated mistake"
