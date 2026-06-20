# Rebuttal Protocol Pack

Made by sudal.

Use this after any review.

## Labels

```text
ACCEPT: The reviewer is right. Patch it.
REJECT: The reviewer is wrong or the issue does not apply. Provide evidence.
DEFER: The reviewer found a real issue outside this task. Create a follow-up.
LATER: The reviewer found a non-critical issue. Log it and continue because the current task is safe to use.
```

## Rules

- Never silently ignore a review item.
- Never accept without implementing or creating a follow-up.
- Never reject without evidence.
- Never defer a blocker for the current task.
- Never spend another review round on non-critical-only findings after verification has passed.
- Never mark a critical finding as LATER.
- Rerun verification after accepted fixes.

## Response Shape

```text
Finding: <short title>
Severity: critical | non-critical
Decision: ACCEPT | REJECT | DEFER | LATER
Reason:
Action:
Verification:
Later log:
Memory update:
```
