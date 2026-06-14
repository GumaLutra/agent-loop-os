# Solo Loop OS Pack

Made by sudal.

Use when one AI agent must plan, implement, review, verify, and remember.

## Loop

```text
Builder -> Evidence -> Self-Reviewer -> Rebuttal -> Fix -> Verification -> Memory
```

## Instructions For The Agent

1. Produce a short risk brief from relevant memory.
2. Define goal, scope, non-goals, and verification criteria.
3. Estimate code size:
   - 200-300 lines is preferred.
   - over 300 lines should trigger a split discussion.
   - over 500 lines requires task splitting before implementation.
4. Build the smallest complete change.
5. Pause and list the evidence collected so far.
6. Switch to Self-Reviewer mode:
   - What requirement might I have missed?
   - What evidence is weak?
   - What repeated mistake pattern is nearby?
   - What would a skeptical reviewer flag?
7. Answer each finding with `ACCEPT`, `REJECT`, or `DEFER`.
8. Fix accepted findings.
9. Run the verification gate.
10. Update memory only when a prevention rule is useful.

## Completion Rule

Do not finish with "I would verify." Finish with what was verified, what could not be verified, and why.
