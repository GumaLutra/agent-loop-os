# Agent Loop OS

Made by sudal.

Current version: 0.1.0.

Agent Loop OS는 AI-agent 작업을 위한 툴 중립 운영체계입니다. 핵심은 네 가지입니다.

- 작업 전에 잘 생각한다.
- 큰 작업은 증거 기반 단계로 쪼갠다.
- 완료 전에 리뷰하고 검증한다.
- 반복 실수를 기억해서 다음 작업의 위험을 줄인다.

여기에 진단 규율을 더합니다. 관찰된 단서에서 시작하고, 모든 단서를 설명하는 가설을 우선하며, 확신도를 표시하고, 위험한 수정 전에는 가장 싼 감별 확인을 먼저 고릅니다.

0.1.0에서는 severity-gated loop를 추가했습니다. 비치명 이슈는 `LATER`로 기록하고 현재 작업이 실사용 가능하면 추가 리뷰 round를 강제하지 않습니다. 치명 이슈만 다음 round로 올리고, 계속 남으면 사용자 결정으로 넘어갑니다.

운영 데이터는 JSON-first로 둡니다. Markdown은 사람이 읽는 가이드와 AI에게 붙여넣는 pack에 적합하고, task state, review record, risk brief, verification report, memory entry는 JSON 템플릿을 함께 제공합니다.

코딩 작업은 가능하면 200~300줄 안팎을 선호합니다. 예상 코드가 500줄을 넘을 것 같으면 구현 전에 task를 쪼개도록 강제합니다.

이 프로젝트는 Fablize식 검증, VFF식 진단, cross-review workflow에서 배운 장점을 합친 구조입니다. 하지만 특정 프로젝트의 복사본은 아닙니다. Codex, Claude, Cursor 또는 다른 AI-agent에서도 쓸 수 있게 만들었습니다.

## 두 가지 모드

### Solo Loop OS

AI 하나만 쓸 때 사용합니다.

```text
Builder -> Evidence -> Self-Reviewer -> Rebuttal -> Fix -> Verification -> Memory
```

하나의 AI가 작업자, 증거 정리자, 리뷰어, 반박자, 기록자의 역할을 차례로 수행합니다. 외부 리뷰만큼 독립적이지는 않지만, 그냥 작업하고 바로 완료하는 것보다 훨씬 안전합니다.

### Full Loop OS

여러 AI나 리뷰 도구를 쓸 수 있을 때 사용합니다.

```text
Planner -> Builder -> External Reviewer -> Rebuttal & Patch -> Verification -> Memory
```

리뷰어는 Claude, Cursor, 다른 Codex thread, 사람, 또는 다른 모델일 수 있습니다. Builder는 각 리뷰 지적에 `ACCEPT`, `REJECT`, `DEFER` 중 하나로 답해야 합니다.

## 언제 쓰나

다음 작업에 사용하세요.

- 위험한 코드 변경
- 실제 화면 확인이 필요한 UI 작업
- 데이터 복구, 마이그레이션, 삭제
- 배포와 릴리즈
- 원인 모르는 버그
- 반복되는 실수를 줄이고 싶은 작업
- "완료"에 증거가 필요한 작업

아주 작은 수정에는 가볍게 쓰면 됩니다. 목표를 말하고, 고치고, 한 번 검증하고, 문제가 있었을 때만 memory를 남기세요.
1round가 통과했고 남은 문제가 비치명이라면 later backlog에 기록하고 다음 단계로 넘어갑니다.

## 빠른 시작

프로젝트 안에 memory 저장소를 초기화합니다.

```bash
python scripts/loopos.py init
```

작업을 시작합니다.

```bash
python scripts/task.py start --mode solo --type ui --title "Fix dashboard mobile layout"
```

과거 실수에서 risk brief를 뽑습니다.

```bash
python scripts/loopos.py risk --type ui
```

반복 실수를 기록합니다.

```bash
python scripts/memory.py add --type ui --mistake visual-not-verified --lesson "UI 변경은 브라우저 또는 스크린샷 검증 전 완료 선언 금지."
```

저장된 memory를 확인합니다.

```bash
python scripts/memory.py list
```

## AI에게 붙여넣는 사용법

```text
Use Agent Loop OS.
Mode: solo
Task: <작업 내용>

작업 전에 비슷한 과거 실수 기반 risk brief를 짧게 작성하라.
작업 중 의미 있는 단계마다 evidence를 남겨라.
완료 전에 verification gate를 통과하라.
완료 후 반복 실수나 예방 규칙을 memory ledger에 기록하라.
```

Full Loop용:

```text
Use Agent Loop OS Full Loop.
Builder는 작업을 구현한다.
Reviewer는 독립적으로 결과를 검사한다.
Builder는 모든 리뷰 지적에 ACCEPT, REJECT, DEFER 중 하나로 답하고, accepted 항목을 수정 후 검증한다.
반복 실패 패턴은 memory ledger에 기록한다.
```

## 폴더 구조

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

## 흔적 남기기

이 프로젝트는 재사용을 환영합니다. 복사하거나 변형해도 이 흔적은 남겨주세요.

```text
Made by sudal.
```

MIT 라이선스도 주요 복사본에 저작권 고지를 유지하도록 요구합니다.
