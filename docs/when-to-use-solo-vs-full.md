# When To Use Solo Vs Full

Made by sudal.

Agent Loop OS has two operating modes.

## Use Solo Loop OS

Use Solo when one AI agent must do the work alone.

```text
Builder -> Evidence -> Self-Reviewer -> Rebuttal -> Fix -> Verification -> Memory
```

Good for:

- small and medium code changes
- documentation updates
- simple UI fixes
- local scripts
- low-risk debugging
- quick analysis

Solo is cheaper and faster, but the review is not truly independent. Compensate with memory, explicit self-review, and a real verification gate.

If Solo round 1 passes and only non-critical findings remain, log them as `LATER` and continue. Do not escalate to Full only for polish or low-impact cleanup.

## Use Full Loop OS

Use Full when another AI, tool, or human can review.

```text
Planner -> Builder -> External Reviewer -> Rebuttal & Patch -> Verification -> Memory
```

Good for:

- production data changes
- deployments
- auth, payment, security, or permission work
- unclear root-cause bugs
- complex UI changes
- multi-file refactors
- repeated mistakes from memory

Full is slower, but it gives you an independent pressure test.

Use Full for critical findings. If a Full review finds only non-critical issues and verification passes, record them in the later backlog and move on.

## Escalate From Solo To Full

Escalate when:

- self-review finds more than two material issues
- verification is indirect or weak
- the task would be hard to undo
- the agent cannot explain the root cause
- the leading diagnosis leaves an observed clue unexplained
- the next fix would be risky before a discriminating check
- memory shows this task type has repeated failures
- expected code exceeds 500 lines and needs task splitting
