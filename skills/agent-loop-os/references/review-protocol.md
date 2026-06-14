# Review Protocol

Made by sudal.

## Reviewer Prompt

Ask the reviewer to inspect the artifact, not to admire the plan.

```text
Review this work using Agent Loop OS.

Focus on:
- bugs or behavioral regressions
- missed requirements
- weak or missing verification
- repeated mistake patterns
- risky assumptions

Return findings only when actionable.
Order by severity.
Do not rewrite the whole solution unless the current one is unsalvageable.
```

## Rebuttal Format

Every review item must receive one of:

```text
ACCEPT: The issue is valid. I fixed it and verified the fix.
REJECT: The issue is not valid. Evidence: <file/log/test/constraint>.
DEFER: The issue may be valid but is outside this task. Follow-up: <specific next task>.
```

## Builder Rules

- Do not accept review items just because they sound confident.
- Do not reject review items without evidence.
- Do not defer issues that break the requested task.
- After any accepted fix, rerun the relevant verification.

## Final Review Summary

Use this shape:

```text
Review response:
- ACCEPT: <count>
- REJECT: <count>
- DEFER: <count>

Verification:
- <commands, screenshots, logs, or inspections>

Memory:
- <new prevention rule or "No new repeated mistake.">
```
