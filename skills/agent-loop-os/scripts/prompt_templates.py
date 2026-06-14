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
        2. Plan goal, scope, non-goals, and verification criteria.
        3. Build the smallest complete change.
        4. Pause and list evidence.
        5. Self-review for missed requirements, weak evidence, and repeated mistakes.
        6. Answer findings with ACCEPT, REJECT, or DEFER.
        7. Fix accepted findings and verify.
        8. Update memory only if a prevention rule is useful.
        """,
    "full-review": """\
        Review this work using Agent Loop OS Full Loop.

        Focus on:
        - bugs or behavioral regressions
        - missed requirements
        - weak or missing verification
        - repeated mistake patterns
        - risky assumptions

        Return actionable findings ordered by severity. Say clearly if no material issue is found.
        """,
    "rebuttal": """\
        For each review finding, answer:

        Finding:
        Decision: ACCEPT | REJECT | DEFER
        Reason:
        Action:
        Verification:
        Memory update:
        """,
}


def get_template(name: str) -> str:
    return dedent(TEMPLATES[name]).strip()
