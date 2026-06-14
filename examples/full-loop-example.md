# Full Loop Example

Made by sudal.

## Task

Restore missing records from a backup file.

## Builder Evidence

- identified backup file and target collection
- confirmed date range
- ran dry-run count comparison
- restored records
- sampled restored records

## Reviewer Finding

```text
The restore evidence includes total counts, but no duplicate check.
```

## Rebuttal

```text
Decision: ACCEPT
Reason: Data restore verification should include duplicate checks.
Action: Ran duplicate scan on restored IDs.
Verification: Duplicate count was 0.
Memory update: Data restore gate now includes duplicate scan.
```

## Final

The task is complete only after restore, count comparison, sample checks, duplicate scan, and memory update.
