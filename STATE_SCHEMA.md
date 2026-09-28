# Design Roadmap Guardian — State Schema v0.1

The project state should represent the **current meaning of the project**, not a transcript of everything discussed.

## Root structure

```yaml
project:
  identity: {}
  roadmap: []
  ideas: []
  decisions: []
  parking_lot: []
  trajectory: []
  plan_signals: []
  replan_state: {}
  milestones: []
  convergence: {}
```

## Project identity

Fields:

- `name`
- `goal`
- `current_phase`
- `current_step_id`
- `success_definition`
- `last_updated`

Do not rewrite the high-level goal because of minor implementation changes.

## Roadmap step

```yaml
id:
title:
purpose:
status: PLANNED | CURRENT | BLOCKED | COMPLETED | REVISED | REMOVED
dependencies: []
completion_criteria: []
evidence_required: []
created_at:
updated_at:
```

## Idea

```yaml
id:
name:
description:
status: EXPLORING | ACTIVE | DORMANT | PARKED | REJECTED | SUPERSEDED
relevance: LOW | MEDIUM | HIGH
readiness: LOW | MEDIUM | HIGH
status_confidence: LOW | MEDIUM | HIGH
explicitness: EXPLICIT_USER_DECISION | STRONG_INFERENCE | WEAK_INFERENCE
reason:
reason_type: DEPENDENCY | EVIDENCE | DESIGN_PRINCIPLE | USER_PREFERENCE | RESOURCE | SCOPE | TECHNICAL_CONSTRAINT | TEMPORARY_STRATEGY
revisit_trigger:
related_steps: []
first_seen:
last_seen:
recurrence_count:
history: []
```

## Decision

```yaml
id:
statement:
status: ACTIVE | TEMPORARY | REVERSED | SUPERSEDED
rationale:
evidence: []
source_ideas: []
affected_steps: []
decision_type: DESIGN | TECHNICAL | RESEARCH | SCOPE | PRIORITY | PROCESS
validity:
  type: PERMANENT | TEMPORARY | UNTIL_DEPENDENCY_CHANGES | UNTIL_NEW_EVIDENCE | UNTIL_MILESTONE
  condition:
revisit_trigger:
created_at:
updated_at:
```

## Parking-lot entry

```yaml
idea_id:
parked_reason:
dependency_gap: []
revisit_trigger:
parked_at:
```

Parking is not rejection.

## Trajectory event

```yaml
id:
timestamp:
type: DISCOVERY | ASSUMPTION | EXPERIMENT | OBSERVATION | DECISION | REVISION | REJECTION | REVIVAL | MILESTONE | ROADMAP_CHANGE
summary:
related_step:
related_ideas: []
evidence: []
impact: LOCAL | STEP_LEVEL | MULTI_STEP | PROJECT_LEVEL
```

Store meaningful changes, not every conversation turn.

## Evidence item

```yaml
type: USER_RESEARCH | EXPERT_INPUT | EXPERIMENT | PROTOTYPE_TEST | IMPLEMENTATION | LITERATURE | OBSERVATION | USER_DECISION
description:
source:
confidence: LOW | MEDIUM | HIGH
```

## Plan signal

```yaml
id:
type: ASSUMPTION_BREAK | DEPENDENCY_CHANGE | REPEATED_DETOUR | DOWNSTREAM_IMPACT | GOAL_CHANGE | SCOPE_CHANGE | BLOCKER
description:
severity: LOW | MEDIUM | HIGH | CRITICAL
affected_steps: []
unresolved: true
created_at:
```

## Replan state

```yaml
level: QUIET | WATCH | REVIEW | CRITICAL
reasons: []
last_reviewed:
recommended_review_point:
```

## Milestone

```yaml
id:
title:
completed_at:
original_goal:
actions: []
evidence: []
findings: []
decisions: []
unresolved: []
roadmap_effect:
```

## Convergence

```yaml
mode: PORTFOLIO | RESEARCH_PAPER | PRODUCT_CASE_STUDY | GENERAL
compression_level: L0_FULL_TRACE | L1_DECISION_TRACE | L2_CORE_REASONING | L3_NARRATIVE | L4_THESIS
selected_events: []
excluded_events: []
core_reasoning_chain: []
unresolved_claims: []
```

A core reasoning item may contain:

```yaml
question:
evidence:
interpretation:
decision:
outcome:
```

## Allowed idea transitions

Common valid transitions:

```text
EXPLORING -> ACTIVE
EXPLORING -> PARKED
EXPLORING -> REJECTED
ACTIVE -> DORMANT
ACTIVE -> SUPERSEDED
ACTIVE -> PARKED
DORMANT -> EXPLORING
PARKED -> EXPLORING
REJECTED -> EXPLORING
SUPERSEDED -> EXPLORING
```

A transition out of `REJECTED` requires explicit user intent, new evidence, a changed dependency, changed scope, or changed project assumptions.

## Never infer

Never infer:

- `DORMANT -> REJECTED` because time passed.
- `EXPLORING -> ACTIVE` because an idea was discussed deeply.
- `PARKED -> ACTIVE` because a dependency was resolved.

Use `PARKED -> EXPLORING` and return authority to the user.

## Minimal update principle

Update state only when project meaning changes: commitment, uncertainty, evidence, assumption, dependency, branch state, or roadmap structure.

Do not update for wording changes, repeated statements, or minor factual questions.

## Human-authority constraint

Do not finalize these solely from model inference:

- `REJECTED`
- `ACTIVE` commitment
- `GOAL_CHANGE`
- `SCOPE_CHANGE`
- roadmap rewrite
- final narrative claim
