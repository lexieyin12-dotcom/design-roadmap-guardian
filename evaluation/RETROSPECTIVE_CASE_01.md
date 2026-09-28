# Retrospective Evaluation 01 — Long-form design project

## Evaluation type

Retrospective case study using a real multi-week design-and-prototyping workflow, anonymized for public release.

This is **not** a controlled benchmark. It compares observed collaboration friction in the original workflow with the behavior Design Roadmap Guardian is designed to enforce. A future release should repeat the same cases as a blinded A/B test with the same model and project context, once with Design Roadmap Guardian and once without it.

## Project baseline

The original project had a staged path similar to:

```text
prototype validation
→ stable evidence capture
→ interpretation
→ implementation
→ live capability
→ final validation
```

During execution, several useful but premature topics appeared. Some were necessary detours; some were future ideas; some became new dependencies; some were explicitly paused rather than rejected.

---

## Case A — Future intelligent capability appears before prerequisites are ready

### Situation

While the current work was still validating the core prototype, the discussion moved toward a future intelligent capability.

### Observed friction

The future direction was valuable, but the conversation needed repeated clarification about what existed **now** versus what should be built **later**. The user had to explicitly re-establish that the current system only supported an earlier-stage capability and that the future live path should wait until its prerequisite pipeline was ready.

### Design Roadmap Guardian classification

```text
FUTURE_EXPLORATION
Relevance: HIGH
Readiness: LOW
```

### Expected TG behavior

1. Capture the future capability.
2. Explain why it matters.
3. Identify the missing dependencies.
4. Explore only far enough to define its role.
5. Park implementation detail until the prerequisite pipeline is ready.
6. Preserve the current step as the main trajectory.

### Expected state

```yaml
idea: realtime intelligent coaching
status: PARKED
reason: required live-data/evaluation dependencies are incomplete
revisit_trigger: required live capability becomes available
```

### Value

The system does not suppress a strong idea; it prevents a high-value future idea from silently becoming today's implementation task.

---

## Case B — A difficult technical branch is paused, not rejected

### Situation

An experimental technical branch produced unreliable results and consumed significant debugging effort. The project then explicitly prioritized the more reliable core path first.

### Observed friction

Without explicit lifecycle state, a later assistant could incorrectly conclude either:

- the branch is still active because it appeared frequently in history; or
- the branch was permanently abandoned because the team stopped working on it.

Both are wrong.

### Design Roadmap Guardian classification

At the moment of technical debugging:

```text
NECESSARY_DETOUR
```

After the explicit decision to defer it:

```text
PARKED
```

### Expected state

```yaml
idea: optional experimental branch
status: PARKED
reason_type: TEMPORARY_STRATEGY
reason: unreliable results and disproportionate debugging cost at the current phase
revisit_trigger: core path is stable or the experimental branch becomes reliable
```

### Value

Design Roadmap Guardian preserves the difference between **not now** and **not useful**.

---

## Case C — A low-priority product area should not compete with the main flow

### Situation

A secondary product section was considered, but the existing primary flow already covered the necessary user needs. The user explicitly chose to defer the secondary section and continue the original main flow.

### Observed friction

In long AI-assisted projects, every discussed feature remains semantically available, so a deferred section can keep resurfacing and consume attention even when it is not required for the milestone.

### Design Roadmap Guardian classification

```text
FUTURE_EXPLORATION
or LOW-READINESS / LOW-PRIORITY branch
```

### Expected behavior

- record the section as `PARKED`;
- preserve the reason for deferral;
- do not keep proposing expansion unless the original need reappears;
- keep the primary flow as the current trajectory.

### Value

The skill reduces repeated re-negotiation of already-set scope boundaries.

---

## Case D — A discovery inserts new work between two existing steps

### Situation

The initial plan assumed that prototype validation could flow directly into implementation. Testing showed that an interpretation step was necessary first.

### Design Roadmap Guardian classification

```text
PLAN_CHANGING
Signal: DEPENDENCY_CHANGE
```

### Expected behavior

Do **not** rewrite the roadmap at the first mention.

Accumulate the signal, then at the end of the validation milestone propose:

```text
prototype validation
→ interpretation
→ implementation
```

with an explanation of why the insertion is required.

### Value

This is the core replanning problem: the roadmap changes because the project's dependency structure changed, not because the conversation became busy.

---

## Case E — Final narrative must distinguish prototype reality

### Situation

The interface contained placeholder result values while the real evaluation pipeline was still pending.

### Risk

A later summary could accidentally turn:

```text
MOCK → IMPLEMENTED → VALIDATED
```

simply because the mock appeared repeatedly in screenshots and discussions.

### Expected TG behavior

Preserve the evidence status and allow final convergence to say:

> The prototype defines the result experience using placeholder scoring while the real evaluation pipeline is being developed.

rather than claiming the scoring system is already validated.

### Value

Final convergence remains truthful instead of creating a cleaner but inaccurate portfolio story.

---

# Retrospective Findings

Across these cases, the main hidden labor was not idea generation. It was **trajectory maintenance**:

- remembering which phase the project was actually in;
- separating future value from present readiness;
- manually re-stating scope boundaries;
- distinguishing temporary deferral from rejection;
- noticing when a dependency truly changed the plan;
- and reconstructing a truthful final reasoning chain later.

Design Roadmap Guardian targets this management layer rather than trying to make creative work linear.

## What this evaluation supports

The retrospective cases support the usefulness of the following mechanisms:

```text
✓ relevance ≠ readiness
✓ parking ≠ rejection
✓ exploration branch ≠ roadmap change
✓ dependency change can justify replanning
✓ milestone boundaries are preferable to constant replanning
✓ final convergence needs evidence/status preservation
```

## What this evaluation does NOT prove

It does not yet prove that Design Roadmap Guardian reduces time, improves design quality, or outperforms an unassisted model statistically.

Those claims require a controlled evaluation.

# Next evaluation

A controlled A/B evaluation should:

1. provide the same project state and conversation segment to the same model configuration;
2. run once without Design Roadmap Guardian and once with it;
3. blind the evaluator to the condition;
4. score both outputs for:
   - premature deep dives;
   - false rejection or activation;
   - unnecessary roadmap revisions;
   - missed dependency changes;
   - interruption cost;
   - final narrative fidelity.
