# Severity-Gated Loop Pack

Made by sudal.

Use this pack when review rounds could consume more time or tokens than the remaining risk deserves.

For the general test-and-review flow, pair this with `review-gate-pipeline.md`.

## Principle

Do not spend extra review rounds on non-critical findings. If the current task is safe to use and verification passes, log non-critical findings as `LATER` and move to the next step. Escalate rounds only for critical findings.

## Severity

Critical findings include:

- real-money, order, position, account, credential, auth, permission, or security risk
- data loss, corruption, deletion, migration, restore, or sync risk
- production deploy, scheduler, automation, or rollback risk
- user-visible core workflow failure
- failed verification with unclear cause
- any change that is hard to undo

Non-critical findings include:

- polish, wording, naming, small layout issues, or style preferences
- nice-to-have tests or refactors
- performance improvements without current user impact
- warnings that do not block the requested workflow
- follow-up cleanup outside the current scope

## Round Policy

```text
Round 1 passed + no critical findings -> next step.
Round 1 non-critical findings only -> log LATER -> next step.
Round 1 critical findings -> round 2.
Round 2 passed -> next step.
Round 2 critical findings remain -> ask user: stop, narrow scope, log later if safe, or run round 3.
Round 3 passed -> next step.
Round 3 critical findings remain -> rounds 4-5 only with explicit user direction.
After round 5 unresolved -> stop and ask user for a decision.
```

## Later Log Shape

```json
{
  "severity": "non-critical",
  "status": "open",
  "finding": "",
  "impact": "",
  "reason_deferred": "",
  "suggested_fix": ""
}
```

Use `python scripts/loopos.py later add ...` or the equivalent project-local path to record these items.
