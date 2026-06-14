# Claude Contract Review Prompt

Made by sudal.

Review the Agent Loop OS contract before implementation.

## Required Checks

- Confirm the task goal, scope, and non-goals are clear.
- Confirm `implementation_size_limit` exists.
- Confirm preferred size is 200-300 changed lines.
- Confirm hard max is 500 changed lines.
- If implementation looks likely to exceed 500 changed lines, do not approve.
- Require TASK splitting instead of approving a larger cap.
- Do not suggest relaxing the size cap.

## Response Format

```text
Decision: APPROVE | REQUEST_TASK_SPLIT | REQUEST_CHANGES
Reason:
Size risk:
Required split, if any:
Verification requirements:
```
