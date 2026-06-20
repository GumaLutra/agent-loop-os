# Agent Loop OS

Made by sudal.

Current version: 0.1.0.

Agent Loop OS is a tool-neutral operating system for AI-agent work. It combines four habits:

- Think clearly before acting.
- Break large work into evidence-backed steps.
- Review the work before calling it done.
- Remember repeated mistakes so the next task starts wiser.

It also adds diagnostic discipline: start from observed clues, prefer the hypothesis that explains every clue, name confidence, and run the cheapest useful measurement before a risky fix.

Version 0.1.0 adds severity-gated loops. Non-critical findings are logged as `LATER` and do not force extra review rounds when the current task is safe to use. Critical findings escalate review rounds and eventually require a user decision if they remain unresolved.

Operational data is JSON-first. Markdown is kept for human guides and AI-readable packs, while task state, review records, risk briefs, verification reports, and memory entries have JSON templates.

Coding tasks should stay near 200-300 lines when practical. If a task is expected to exceed 500 lines, Agent Loop OS requires splitting it into smaller tasks before implementation.

It is inspired by the practical lessons behind Fablize-style verification, VFF-style diagnosis, and cross-review workflows, but it is not a clone of any one project. It is designed to work with Codex, Claude, Cursor, or any capable AI agent.

## Two Modes

### Solo Loop OS

Use Solo Loop OS when one AI agent must handle the whole job.

```text
Builder -> Evidence -> Self-Reviewer -> Rebuttal -> Fix -> Verification -> Memory
```

The same agent changes roles deliberately. This is not as independent as an external review, but it prevents the common "I edited it, so it must be done" failure.

### Full Loop OS

Use Full Loop OS when multiple AI agents or tools are available.

```text
Planner -> Builder -> External Reviewer -> Rebuttal & Patch -> Verification -> Memory
```

The reviewer may be Claude, Cursor, another Codex thread, a human, or any model that can inspect the work. The builder must answer each review item with `ACCEPT`, `REJECT`, or `DEFER`.

## When To Use

Use Agent Loop OS for:

- risky code changes
- UI work that needs visual verification
- data repair, migration, restore, or deletion
- deployment and release work
- unclear bugs
- repeated mistakes you want to stop seeing
- any task where "done" needs evidence

For tiny edits, use the lightweight version: state the goal, make the change, verify once, and record memory only if something went wrong.

For tiny or low-risk edits, do not burn tokens on extra rounds. If round 1 passes and remaining findings are non-critical, record them in the later backlog and continue.

## Quick Start

Initialize a local memory store inside any project:

```bash
python scripts/loopos.py init
```

Create a task:

```bash
python scripts/task.py start --mode solo --type ui --title "Fix dashboard mobile layout"
```

Generate a risk brief from past mistakes:

```bash
python scripts/loopos.py risk --type ui
```

Record a repeated mistake:

```bash
python scripts/memory.py add --type ui --mistake visual-not-verified --lesson "UI changes require browser or screenshot verification before completion."
```

List stored memories:

```bash
python scripts/memory.py list
```

## AI Usage

Give this to any AI agent:

```text
Use Agent Loop OS.
Mode: solo
Task: <your task>

Before acting, produce a short risk brief from similar past mistakes.
During work, keep evidence for each meaningful step.
Before completion, run the verification gate.
After completion, record any repeated mistake or prevention rule.
```

For multi-agent review:

```text
Use Agent Loop OS Full Loop.
Builder: implement the task.
Reviewer: inspect the result independently.
Builder: answer every review item with ACCEPT, REJECT, or DEFER, then patch and verify accepted items.
Update the memory ledger with any repeated failure pattern.
```

## Repository Map

```text
README.md
README.ko.md
LICENSE
NOTICE

config/
  defaults.json

skills/agent-loop-os/
  SKILL.md
  references/
  scripts/

packs/
  base-principles.md
  claude-contract-review.md
  codex-contract-revision.md
  codex-implementation.md
  solo-loop.md
  full-loop.md
  verification-gate.md
  severity-gated-loop.md
  memory-ledger.md
  rebuttal-protocol.md
  risk-brief.md
  diagnostic-discipline.md

templates/
  contract.json
  task-brief.md
  task-brief.json
  review-request.md
  review-request.json
  review-response.md
  review-response.json
  memory-entry.json
  later-item.md
  later-item.json
  risk-brief.md
  risk-brief.json
  verification-report.md
  verification-report.json

schemas/
  contract.schema.json

scripts/
  loopos.py
  memory.py
  task.py
  review.py

examples/
  solo-loop-example.md
  full-loop-example.md
  ui-task-example.md
  data-recovery-example.md

docs/
  operating-model.md
  when-to-use-solo-vs-full.md
  integration-codex.md
  integration-claude.md
  integration-cursor.md
  memory-system.md
```

## Attribution

This project is designed to be reused. Keep the attribution when you copy or adapt it:

```text
Made by sudal.
```

The MIT license also requires the copyright notice to remain in substantial copies.
