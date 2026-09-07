# Diagnostic Discipline Pack

Made by sudal.

Use this pack when the task involves debugging, root-cause analysis, operational incidents, data repair, model evaluation, or any answer where a confident but unverified diagnosis could mislead the user.

## Diagnostic Rules

- Start from observed clues, not from the most common cause.
- Prefer the hypothesis that explains all known clues: timing, intermittency, exact numbers, changed files, environment, user-visible behavior, and prior failures.
- If a clue does not fit the leading hypothesis, lower confidence and say what would decide it.
- Before a risky fix, pick the cheapest useful measurement that separates the top causes.
- Give the user the next action that changes the diagnosis, not a catalog of generic possibilities.
- Mark confidence plainly: observed, likely, possible, or unverified.
- Do not turn a pattern match into a root cause. A root cause needs evidence.

## Diagnostic Output Shape

```text
Conclusion:
Observed clues:
Leading hypothesis:
Confidence:
Cheapest discriminating check:
Fix or next action:
Unverified areas:
```

## When To Escalate

Escalate from Solo to Full review when:

- the issue crosses more than one system boundary
- the first fix fails
- the evidence is indirect
- the task touches production, auth, money, permissions, or user data
- memory shows this task type has repeated mistakes
