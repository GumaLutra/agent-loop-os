#!/usr/bin/env python3
"""Copy-paste prompt templates for Agent Loop OS.

Made by sudal.
"""

from __future__ import annotations

from textwrap import dedent


TEMPLATES = {
    "solo": """\
        Use Agent Loop OS Solo Loop.

        Task:

        Steps:
        1. Create a short risk brief from relevant memory.
        2. List observed clues, leading hypothesis, confidence, and the cheapest discriminating check.
        3. Plan goal, scope, non-goals, and verification criteria.
        4. Build the smallest complete change.
        5. Run tests or the closest practical verification.
        6. Self-review for missed requirements, weak evidence, unexplained clues, and repeated mistakes.
        7. Return PASS when verification passed and no critical issue remains.
        8. Return REVISION_REQUIRED when a critical issue, failed test, or risky verification gap remains.
        9. Classify findings as critical or non-critical.
        10. Answer findings with ACCEPT, REJECT, DEFER, or LATER.
        11. If only non-critical findings remain and verification passes, log them as LATER and continue.
        12. Fix accepted critical findings and verify.
        13. Update memory only if a prevention rule is useful.
        """,
    "full-review": """\
        Review this work using Agent Loop OS Full Loop.

        Focus on:
        - bugs or behavioral regressions
        - missed requirements
        - weak or missing verification
        - diagnoses that do not explain every observed clue
        - critical vs non-critical severity
        - repeated mistake patterns
        - risky assumptions

        Return gate status: PASS or REVISION_REQUIRED.
        Use PASS when verification passed and no critical issue remains.
        Use REVISION_REQUIRED when a critical issue, failed test, or risky verification gap remains.
        Return actionable findings ordered by severity. Say clearly if no material issue is found.
        """,
    "rebuttal": """\
        For each review finding, answer:

        Gate status: PASS | REVISION_REQUIRED
        Finding:
        Severity: critical | non-critical
        Decision: ACCEPT | REJECT | DEFER | LATER
        Reason:
        Action:
        Verification:
        Remaining uncertainty:
        Later log:
        Memory update:
        """,
}


def get_template(name: str) -> str:
    return dedent(TEMPLATES[name]).strip()
