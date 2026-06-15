# Verification Gate Pack

Made by sudal.

Before completion, choose the closest real signal.

## Universal Gate

```text
Goal satisfied:
Evidence collected:
Checks run:
Known unverified areas:
Reason unverified areas are acceptable:
```

## UI Gate

- Render the page or component when practical.
- Check the changed viewport sizes.
- Check console errors if browser-based.
- Use screenshots for visual quality.
- Confirm text does not overlap or overflow.

## Data Gate

- Confirm target account, environment, collection/table, and date range.
- Confirm backup or rollback path.
- Compare before/after counts.
- Sample representative records.
- Check duplicates and missing records.

## Deploy Gate

- Validate config.
- Deploy to the intended target.
- Check deploy status.
- Run smoke checks.
- Name rollback or recovery path.

## Debug Gate

- Reproduce or explain why reproduction is not available.
- List the observed clues before naming the root cause.
- Identify the root cause with evidence, or mark it as likely/possible/unverified.
- Show why the leading hypothesis explains every clue. If one clue does not fit, name the gap.
- Run or name the cheapest discriminating check before a risky fix.
- Show why the fix addresses the cause, not only the symptom.
- Add or run a regression check when possible.
