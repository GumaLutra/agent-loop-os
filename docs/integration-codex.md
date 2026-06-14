# Integration: Codex

Made by sudal.

## Use As A Skill

Copy or reference:

```text
skills/agent-loop-os/
```

The core file is:

```text
skills/agent-loop-os/SKILL.md
```

Trigger it with:

```text
Use Agent Loop OS for this task.
Mode: solo
```

For risky work:

```text
Use Agent Loop OS Full Loop. Prepare a review request after implementation.
```

Before external review, run:

```bash
python scripts/loopos.py size check
```

If `SIZE_LIMIT_EXCEEDED` appears, stop and split the task. Do not ask to relax the cap.

## Use The CLI

From a project root:

```bash
python path/to/agent-loop-os/scripts/loopos.py init
python path/to/agent-loop-os/scripts/loopos.py risk --type ui
python path/to/agent-loop-os/scripts/task.py start --mode solo --type ui --title "Fix dashboard layout"
```

The CLI stores local state in:

```text
.agent-loop-os/
```

Commit that directory only when you want shared process memory.
