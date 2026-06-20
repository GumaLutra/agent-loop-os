# Memory System

Made by sudal.

Memory turns repeated mistakes into future risk controls.

## Storage

The CLI stores local memory in:

```text
.agent-loop-os/memory.jsonl
```

Non-critical findings that should not block the current task are stored separately:

```text
.agent-loop-os/later.jsonl
```

Use later items for small, safe-to-use issues that should be batched later. Promote them to memory only when they repeat or should change future behavior.

Each line is one JSON object. JSONL is easy to append, diff, search, and move between tools.

## Entry Fields

- `date`: ISO timestamp
- `task_type`: short category such as `ui`, `data`, `deploy`, `debug`, `docs`
- `mistake_type`: stable short name
- `lesson`: prevention rule
- `severity`: `low`, `medium`, `high`
- `source`: `self-review`, `external-review`, `test`, `incident`, or `human`
- `evidence`: short supporting note
- `made_by`: defaults to `sudal`

## Risk Briefs

Before a similar task, read the relevant entries and return 3-5 risks. Do not dump the whole memory file into context.

## Promotion

When a mistake repeats, strengthen the process:

- once: record memory
- twice: include in risk brief
- three times: make it a standard verification rule
- after that: add a stronger gate or human review
