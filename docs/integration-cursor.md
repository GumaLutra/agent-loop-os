# Integration: Cursor

Made by sudal.

Use Agent Loop OS with Cursor by adding the packs to project rules or by pasting them into a review task.

## Project Rule Setup

Recommended files:

```text
packs/base-principles.md
packs/solo-loop.md
packs/full-loop.md
packs/verification-gate.md
packs/rebuttal-protocol.md
```

## Cursor Review Prompt

```text
Use Agent Loop OS Full Loop as the reviewer.
Inspect the changed files for bugs, missed requirements, missing verification, risky assumptions, and repeated mistake patterns.
Return actionable findings ordered by severity.
```

## Cursor As Builder

When Cursor implements the work, ask it to produce:

- risk brief
- evidence log
- self-review or external review request
- ACCEPT/REJECT/DEFER response
- verification report
- memory update

Before external review, Cursor should run or simulate:

```bash
python scripts/loopos.py size check
```

If changed lines exceed 500, it should request TASK splitting instead of continuing review.
