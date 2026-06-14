# Integration: Claude

Made by sudal.

Agent Loop OS is not tied to Codex. Use the packs as project instructions or paste them into a Claude task.

## Solo Claude

Paste:

```text
packs/base-principles.md
packs/solo-loop.md
packs/verification-gate.md
packs/memory-ledger.md
```

Then ask:

```text
Use Agent Loop OS Solo Loop.
Before editing, create a risk brief.
After editing, self-review, rebut, verify, and update memory.
```

## Claude As External Reviewer

Give Claude:

```text
templates/review-request.md
packs/rebuttal-protocol.md
```

Ask it to focus on bugs, missed requirements, weak verification, risky assumptions, and repeated mistake patterns. The builder should answer every finding with `ACCEPT`, `REJECT`, or `DEFER`.

For contract review, give Claude:

```text
templates/contract.json
packs/claude-contract-review.md
```

Claude must not approve a contract that is likely to exceed 500 changed lines. It should require TASK splitting instead of cap relaxation.
