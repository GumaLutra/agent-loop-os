# Mode Selection

Made by sudal.

## Solo Loop OS

Use Solo when:

- only one AI agent is available
- the task is small or medium risk
- speed matters more than independent review
- there is enough local verification to catch most mistakes

Solo roles:

```text
Builder -> Evidence -> Self-Reviewer -> Rebuttal -> Fix -> Verification -> Memory
```

The agent must pause between Builder and Reviewer. The review should focus on evidence gaps, missed requirements, repeated mistakes, and verification weakness.

## Full Loop OS

Use Full when:

- production data may change
- deployment, auth, payment, security, or permissions are involved
- UI quality matters and needs a second eye
- the bug root cause is unclear
- the task crosses many files or systems
- the same mistake has happened before

Full roles:

```text
Planner -> Builder -> External Reviewer -> Rebuttal & Patch -> Verification -> Memory
```

The reviewer may be another AI, Cursor, Claude, Codex in a separate thread, or a human. The reviewer should not rewrite the solution first; it should identify risks, bugs, missing evidence, and test gaps.

## Escalation Rule

Start Solo for ordinary tasks. Escalate to Full if:

- the self-review finds more than two material issues
- the agent cannot reproduce or explain the bug
- verification is indirect or weak
- the task would be expensive to undo
- a memory rule marks the task type as repeated-risk
