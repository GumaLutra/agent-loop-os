# Operating Model

Made by sudal.

Agent Loop OS combines four layers.

## 1. Thinking Layer

Use conclusion-first communication, clue-first diagnosis, cheap measurement before risky action, and readable explanations.

Diagnosis has its own discipline. Start from observed clues, prefer hypotheses that explain all of them, and mark confidence before recommending a fix. When several causes are plausible, pick the cheapest measurement that separates them instead of listing generic possibilities.

## 0.1.1 Review Gate Pipeline

The general loop is:

```text
Run tests -> Run Claude/external review -> PASS -> next step
Run tests -> Run Claude/external review -> REVISION_REQUIRED -> classify severity
non-critical -> later backlog -> next step
critical -> fix loop -> verify again
```

`PASS` means tests or the closest practical verification passed and no critical review issue remains. `REVISION_REQUIRED` means a test failed, verification is missing for a risky change, or a critical review issue remains.

## 0.1.0 Severity-Gated Rounds

Agent Loop OS does not require extra rounds for every finding. Non-critical findings are recorded as later work when the current task is safe to use and verification passes. Critical findings are the only reason to spend another round.

The default escalation is:

```text
1round non-critical only -> later log -> next step
1round critical -> 2round -> passed -> next step
2round critical remains -> user decision before 3round
3round critical remains -> 4round/5round only with user direction
5round unresolved -> stop for user decision
```

## 2. Execution Layer

Split large work into small stories. Each meaningful story needs evidence. Evidence can be a test, command output, inspected file, diff, screenshot, log, deployment status, count comparison, or sample check.

Prefer coding tasks around 200-300 lines. If a task is expected to exceed 500 lines, split it before implementation. The split should create smaller tasks with their own goal, evidence, review, verification, and memory update.

Operational records should be JSON-first when possible. Markdown remains useful for public guides and AI-readable instructions, but task state, memory entries, review records, risk briefs, and verification reports should have JSON templates.

The default operating preferences live in `config/defaults.json`.

## Implementation Size Gate

Every implementation contract should include `implementation_size_limit`:

- preferred: 200-300 changed lines
- hard max: 500 changed lines
- measurement: `git diff --numstat` staged + unstaged added/deleted lines

Before Claude or another external reviewer receives the implementation, run:

```bash
python scripts/loopos.py size check
```

If the gate reports `SIZE_LIMIT_EXCEEDED`, stop the review handoff, record the event, and return:

```text
TASK 분할 필요
```

Do not loosen the cap. Split the work into smaller tasks.

## 3. Review Layer

Use Solo Loop when one AI is available. Use Full Loop when another reviewer is available or risk is high. Every review item must be labeled by severity and answered with `ACCEPT`, `REJECT`, `DEFER`, or `LATER`.

## 4. Memory Layer

Record only patterns that should change future behavior. Before similar work, create a short risk brief from memory.

## Why This Exists

AI agents often fail in predictable ways:

- they edit without verifying
- they confuse a passing command with user-visible correctness
- they accept confident reviews without evidence
- they repeat the same mistake across tasks
- they produce long logs but no prevention rule

Agent Loop OS turns these failures into an operating loop.
