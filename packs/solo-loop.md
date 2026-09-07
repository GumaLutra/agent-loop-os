# Solo Loop OS Pack

Made by sudal.

Use when one AI agent must plan, implement, review, verify, and remember.

## Loop

```text
Builder -> Tests -> Self-Reviewer -> PASS or REVISION_REQUIRED -> Rebuttal -> Fix -> Verification -> Memory
```

## Instructions For The Agent

1. Produce a short risk brief from relevant memory.
2. Define goal, scope, non-goals, and verification criteria.
3. Estimate code size:
   - 200-300 lines is preferred.
   - over 300 lines should trigger a split discussion.
   - over 500 lines requires task splitting before implementation.
4. Build the smallest complete change.
5. Run tests or the closest practical verification.
6. Pause and list the evidence collected so far.
7. Switch to Self-Reviewer mode:
   - What requirement might I have missed?
   - What evidence is weak?
   - What repeated mistake pattern is nearby?
   - What would a skeptical reviewer flag?
8. Return `PASS` if verification passed and no critical finding remains.
9. Return `REVISION_REQUIRED` if a critical issue, failed test, or risky verification gap remains.
10. Classify each finding as `critical` or `non-critical`.
11. Answer each finding with `ACCEPT`, `REJECT`, `DEFER`, or `LATER`.
12. If round 1 passes and only non-critical findings remain, log them as `LATER` and continue.
13. If critical findings remain, fix them and run another round.
14. Run the verification gate.
15. Update memory only when a prevention rule is useful.

## Round Policy

```text
Round 1 passed + non-critical only -> LATER log -> next step.
Round 1 critical -> round 2.
Round 2 critical remains -> ask user before round 3.
Round 3 critical remains -> rounds 4-5 only with user direction.
Unresolved after round 5 -> stop for user decision.
```

## Completion Rule

Do not finish with "I would verify." Finish with what was verified, what could not be verified, and why.
