"""Deterministic state rules for Design Roadmap Guardian v0.1.

Semantic classification belongs to the host LLM. This module only enforces
state transitions that should not depend on model creativity.
"""

IDEA_STATES = {
    "EXPLORING",
    "ACTIVE",
    "DORMANT",
    "PARKED",
    "REJECTED",
    "SUPERSEDED",
}

ALLOWED_TRANSITIONS = {
    "EXPLORING": {"ACTIVE", "PARKED", "REJECTED", "DORMANT", "SUPERSEDED"},
    "ACTIVE": {"DORMANT", "PARKED", "SUPERSEDED", "REJECTED"},
    "DORMANT": {"EXPLORING", "ACTIVE", "PARKED"},
    "PARKED": {"EXPLORING"},
    "REJECTED": {"EXPLORING"},
    "SUPERSEDED": {"EXPLORING"},
}

HUMAN_AUTHORITY_TARGETS = {"REJECTED", "ACTIVE"}


def can_transition(current: str, target: str) -> bool:
    if current not in IDEA_STATES or target not in IDEA_STATES:
        return False
    return target in ALLOWED_TRANSITIONS.get(current, set())


def transition_idea(
    current: str,
    target: str,
    *,
    explicit_user_intent: bool = False,
    changed_context: bool = False,
) -> str:
    """Return the new state or raise ValueError.

    Special safeguards:
    - PARKED/REJECTED/SUPERSEDED cannot jump straight to ACTIVE.
    - REJECTED revival requires explicit user intent or changed context.
    - Entering REJECTED or ACTIVE requires explicit user intent in v0.1.
    """
    if not can_transition(current, target):
        raise ValueError(f"Invalid transition: {current} -> {target}")

    if target in HUMAN_AUTHORITY_TARGETS and not explicit_user_intent:
        raise ValueError(f"Human authority required for target state {target}")

    if current == "REJECTED" and target == "EXPLORING":
        if not (explicit_user_intent or changed_context):
            raise ValueError("Rejected idea can be reopened only with changed context or explicit user intent")

    return target


def revival_candidate(status: str, *, blocker_resolved: bool, user_reopens: bool) -> bool:
    if status not in {"PARKED", "REJECTED", "DORMANT", "SUPERSEDED"}:
        return False
    return blocker_resolved or user_reopens
