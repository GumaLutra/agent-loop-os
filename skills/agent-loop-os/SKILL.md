---
name: agent-loop-os
description: Tool-neutral AI-agent operating workflow for risky or non-trivial tasks that need planning, evidence-backed execution, solo self-review or multi-agent review, ACCEPT/REJECT/DEFER rebuttal, verification gates, and repeated-mistake memory. Use when Codex, Claude, Cursor, or another AI agent is asked to implement, debug, review, ship, restore data, change UI, or reduce recurring mistakes.
---

# Agent Loop OS

Made by sudal.

Current version: 0.1.2.

Use Agent Loop OS to avoid shallow completion. The work is not done until the agent can show evidence, review the result, answer review items, verify the final state, and record any repeated mistake worth preventing next time.

## Resume and Handoff

Before substantive work, delegation, task switches or resuming after compaction,
read `references/handoff.md` and run the read-only `scripts/recall.py` with the
exact intended project root. Preserve fixed decisions and existing authorization.
Update the task note before handoff or ending substantial work.
Repository-level resources (`packs`, `config`, `templates`) live two directories
above this skill in a full installation; resolve the installed path first.

## Choose Mode

Use **Solo Loop OS** when only one AI agent is available.

```text
Builder -> Tests -> Self-Reviewer -> PASS or REVISION_REQUIRED -> Rebuttal -> Fix -> Verification -> Memory
```

Use **Full Loop OS** when another model, tool, thread, or human can review.

```text
Planner -> Builder -> Tests -> External Reviewer -> PASS or REVISION_REQUIRED -> Rebuttal & Patch -> Verification -> Memory
```

Escalate from Solo to Full when the task touches production data, deployment, auth, payment, security, destructive changes, unclear bugs, or a repeated failure pattern.

## Core Rules

1. Start with the conclusion and the next action.
2. Diagnose from observed clues before proposing fixes.
3. Prefer the cheapest useful measurement before a risky change.
4. Do not claim a root cause that was not inspected.
5. Prefer the explanation that accounts for every observed clue; if a clue does not fit, lower confidence.
6. Name confidence and unverified areas before recommending a risky fix.
7. Split large tasks into evidence-backed steps.
8. Keep coding tasks near 200-300 lines when practical.
9. Force a task split before implementation if the expected code exceeds 500 lines.
10. Prefer JSON for operational state, memory, review records, and automation inputs.
11. Treat every review item as `ACCEPT`, `REJECT`, or `DEFER`.
12. Classify each finding as `critical` or `non-critical` before spending another review round.
13. Log non-critical findings as `LATER` and continue when round 1 passes and the current task is safe to use.
14. Escalate extra rounds only for critical findings.
15. Run tests or the closest practical verification before Claude or external review.
16. Treat review status as `PASS` or `REVISION_REQUIRED`.
17. On `PASS`, continue to the next step.
18. On `REVISION_REQUIRED`, classify severity before choosing a fix loop or later backlog.
19. Verify with the closest real signal available.
20. Record repeated mistakes as prevention rules.

## Standard Workflow

1. **Risk Brief**
   - Search memory for similar task types.
   - Name 3-5 risks or say no relevant memory exists.
   - Keep it short enough to affect behavior.

2. **Plan**
   - Define goal, scope, non-goals, and verification criteria.
   - For large work, split into small stories with evidence expected for each.
   - Estimate coding size. If expected code is over 500 lines, stop and split into smaller tasks first. If expected code is over 300 lines, warn and prefer splitting.

3. **Build**
   - Implement narrowly.
   - Preserve unrelated user changes.
   - Keep evidence from commands, diffs, screenshots, logs, tests, or inspected files.
   - Before external review, run `python scripts/loopos.py size check`.
   - If the gate emits `SIZE_LIMIT_EXCEEDED`, stop and split the task. Do not relax the cap.
   - Run tests or the closest practical verification before Claude or another reviewer.

4. **Review Gate**
   - Solo: switch into self-reviewer mode and inspect the work as if someone else wrote it.
   - Full: ask the external reviewer to find bugs, missed requirements, weak evidence, and missing tests.
   - Return `PASS` when tests or verification passed and no critical issue remains.
   - Return `REVISION_REQUIRED` when a critical issue, failed test, or risky verification gap remains.
   - Classify each finding as critical or non-critical.

5. **Rebuttal**
   - For each review item:
     - `ACCEPT`: fix it and verify.
     - `REJECT`: explain with evidence.
     - `DEFER`: acknowledge but keep outside current scope.
     - `LATER`: non-critical, safe to use now, recorded in the later backlog.
   - If the review gate is `PASS`, continue to the next step.
   - If the review gate is `REVISION_REQUIRED`, fix critical findings only and verify again.
   - If round 1 passes and only non-critical findings remain, log `LATER` items and continue.
   - If critical findings remain after round 2, ask the user before spending round 3.
   - If critical findings remain after rounds 4-5, stop and ask the user for a decision.

6. **Verification Gate**
   - Run the best available checks before completion.
   - UI requires render/browser/screenshot when practical.
   - Data work requires before/after counts, sample checks, and target confirmation.
   - Deployment requires status, smoke checks, and rollback awareness.

7. **Memory Update**
   - Record repeated mistakes or useful prevention rules.
   - Do not record noise. Memory should change future behavior.

## Resources

Read only what is needed:

- `references/mode-selection.md` for choosing Solo vs Full.
- `references/review-protocol.md` for reviewer and rebuttal rules.
- `references/verification.md` for verification gates by task type.
- `references/memory.md` for memory schema and promotion rules.
- `packs/diagnostic-discipline.md` when a task needs clue-first diagnosis, calibrated confidence, or cheap discriminating measurements.
- `packs/severity-gated-loop.md` when findings should be logged for later instead of forcing extra rounds.
- `packs/review-gate-pipeline.md` when tests, Claude review, `PASS`, and `REVISION_REQUIRED` need a single operating flow.
- `scripts/loopos.py` for local `.agent-loop-os` memory and task files.
- `config/defaults.json` and `templates/*.json` when the user prefers JSON-first operation.
- `templates/contract.json` and `schemas/contract.schema.json` for implementation contracts.
- `packs/claude-contract-review.md`, `packs/codex-contract-revision.md`, and `packs/codex-implementation.md` for contract review and implementation prompts.

## CLI Quick Start

From a project root:

```bash
python path/to/skills/agent-loop-os/scripts/loopos.py init
python path/to/skills/agent-loop-os/scripts/loopos.py task start --mode solo --type ui --title "Fix mobile dashboard"
python path/to/skills/agent-loop-os/scripts/loopos.py risk --type ui
python path/to/skills/agent-loop-os/scripts/loopos.py memory add --type ui --mistake visual-not-verified --lesson "UI changes require browser or screenshot verification before completion."
python path/to/skills/agent-loop-os/scripts/loopos.py size check
```
