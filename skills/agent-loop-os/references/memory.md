# Memory Ledger

Made by sudal.

Memory exists to change future behavior. Do not record every detail. Record patterns.

## Entry Shape

```json
{
  "date": "2026-06-14T12:00:00Z",
  "task_type": "ui",
  "mistake_type": "visual-not-verified",
  "lesson": "UI changes require browser or screenshot verification before completion.",
  "severity": "medium",
  "source": "review",
  "evidence": "Reviewer found CSS change with no rendered check."
}
```

## What To Record

Record:

- repeated mistakes
- dangerous assumptions
- missing verification that caused rework
- review findings likely to recur
- prevention rules that are short and actionable

Do not record:

- one-off typos
- vague regrets
- huge transcripts
- issues that cannot change future behavior

## Promotion Rule

- 1 occurrence: keep as memory.
- 2 occurrences: include in future risk briefs.
- 3 occurrences: turn into a standard verification rule.
- recurrence after a rule exists: strengthen the gate or add a checklist item.

## Risk Brief Rule

Before work, read only the top relevant memories. A good risk brief is 3-5 bullets. Long memory dumps make agents worse.
