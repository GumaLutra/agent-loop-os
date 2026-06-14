# Codex Contract Revision Prompt

Made by sudal.

Revise the Agent Loop OS contract after review.

## Rules

- Keep `implementation_size_limit`.
- Keep preferred changed lines at 200-300.
- Keep hard max at 500 changed lines.
- If Claude or another reviewer says the task is too large, split scope.
- Do not relax the cap as the first response.
- Create smaller tasks with separate goals, evidence, review, verification, and memory updates.

## Response Format

```text
Decision: ACCEPT | REJECT | DEFER
Contract changes:
Task split:
Verification impact:
Memory impact:
```
