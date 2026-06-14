# UI Task Example

Made by sudal.

## Task

Fix a dashboard button that overlaps text on mobile.

## Mode

Solo Loop OS, unless the screen is production-critical or the layout touches many shared components.

## Risk Brief

- UI changes can look correct in code but fail in the rendered viewport.
- Mobile and desktop may need separate checks.
- Text overflow and overlap are common repeated mistakes.

## Verification Gate

- Open the page or component.
- Check the affected mobile viewport.
- Check the relevant desktop viewport if shared layout changed.
- Confirm no console errors.
- Capture screenshot evidence when visual quality matters.

## Memory Candidate

```json
{
  "task_type": "ui",
  "mistake_type": "visual-not-verified",
  "lesson": "UI layout changes require rendered viewport verification before completion.",
  "severity": "medium",
  "source": "self-review",
  "evidence": "Mobile overlap would not be caught by syntax checks."
}
```
