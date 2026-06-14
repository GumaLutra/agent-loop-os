# Codex Implementation Prompt

Made by sudal.

Implement the approved Agent Loop OS contract.

## Size Limit

- Target 200-300 changed lines.
- Do not exceed 500 changed lines.
- Before Claude review, run:

```bash
python scripts/loopos.py size check
```

- If the gate returns `SIZE_LIMIT_EXCEEDED`, stop.
- Return `TASK 분할 필요`.
- Do not ask to relax the cap; split scope.

## Implementation Loop

1. Re-read the contract.
2. Implement the smallest complete scope.
3. Run size check before external review.
4. Run verification gate.
5. Prepare review request only if size gate passes.
6. Record repeated mistakes or size violations in memory/events.
