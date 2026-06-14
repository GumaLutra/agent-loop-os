# Data Recovery Example

Made by sudal.

## Task

Restore missing records from a local backup.

## Mode

Full Loop OS is recommended because data recovery is hard to undo.

## Risk Brief

- Target account, collection, or date range may be confused.
- A successful script run does not prove the right records were restored.
- Duplicate checks are easy to skip.

## Builder Evidence

- backup file path
- target environment and account
- before count
- dry-run count
- restored count
- representative samples
- duplicate scan

## Reviewer Finding

```text
The restore evidence has counts but no sample record comparison.
```

## Rebuttal

```text
Decision: ACCEPT
Reason: Counts alone do not prove record content is correct.
Action: Compared 5 representative restored records against backup source.
Verification: All sampled records matched expected IDs, dates, and amounts.
Memory update: Data recovery gate includes representative sample comparison.
```
