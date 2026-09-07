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
Classify every finding as critical or non-critical.

Return findings only when actionable.
Order by severity.
Do not rewrite the whole solution unless the current one is unsalvageable.
```

## Rebuttal Format

Every review item must receive a severity and one decision:

```text
ACCEPT: The issue is valid. I fixed it and verified the fix.
REJECT: The issue is not valid. Evidence: <file/log/test/constraint>.
DEFER: The issue may be valid but is outside this task. Follow-up: <specific next task>.
LATER: The issue is non-critical, safe to use now, and recorded in the later backlog.
```

## Builder Rules

- Do not accept review items just because they sound confident.
- Do not reject review items without evidence.
- Do not defer issues that break the requested task.
- Do not run extra rounds for non-critical-only findings after verification passes.
- Do not mark critical findings as LATER.
- After any accepted fix, rerun the relevant verification.

## Final Review Summary

Use this shape:

```text
Review response:
- ACCEPT: <count>
- REJECT: <count>
- DEFER: <count>
- LATER: <count>

Verification:
- <commands, screenshots, logs, or inspections>

Memory:
- <new prevention rule or "No new repeated mistake.">
```
