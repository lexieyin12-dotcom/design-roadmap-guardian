# Design Roadmap Guardian

**An AI skill that helps designers stay oriented through nonlinear projects—managing exploration, detecting when plans need to change, and converging complex processes into clear reasoning chains.**

*Explore freely. Commit deliberately. Replan selectively. Converge clearly.*

Design Roadmap Guardian is an experimental agent skill for long-term human–AI collaboration in design, research, prototyping, writing, and other nonlinear project work.

It addresses a recurring problem: AI is very good at expanding possibilities, but long projects need more than expansion. Users need help distinguishing useful detours from premature deep dives, deciding when a roadmap really deserves revision, preserving parked or rejected ideas without losing their history, and finally compressing a messy process into a truthful reasoning chain.

## What it does

Design Roadmap Guardian tracks five things:

1. **Current trajectory** — goal, phase, current step, dependencies.
2. **Exploration state** — active, exploring, dormant, parked, rejected, superseded.
3. **Plan signals** — assumption breaks, dependency changes, repeated detours, downstream impact, goal/scope changes.
4. **Replan pressure** — QUIET, WATCH, REVIEW, CRITICAL.
5. **Convergence** — transforms the nonlinear project history into an evidence-backed final reasoning chain.

## Core interaction model

A meaningful discussion is classified as one of:

- `ON_TRACK`
- `NECESSARY_DETOUR`
- `FUTURE_EXPLORATION`
- `PLAN_CHANGING`

The skill does **not** suppress future ideas. It separates **idea relevance** from **execution readiness** so that a high-value but premature direction can be preserved without becoming today's implementation task.

## Repository structure

```text
design-roadmap-guardian/
├── README.md
├── SKILL.md
├── STATE_SCHEMA.md
├── EVALUATION_CASES.md
├── examples/
│   └── state.example.json
├── evaluation/
│   └── RETROSPECTIVE_CASE_01.md
├── src/
│   └── state_rules.py
└── tests/
    └── test_state_rules.py
```

## Run the v0.1 state-rule tests

Requires Python 3.10+ and no external packages.

```bash
python -m unittest discover -s tests -v
```

The runnable v0.1 validates the parts that should be deterministic: lifecycle transitions, human-authority constraints, and revival logic. Semantic classification is intentionally kept in `SKILL.md` because it should be performed by the host LLM using project context, rather than reduced to brittle keyword rules.

## Design principles

- Silence is not rejection.
- Rejection is not deletion.
- Not now does not mean not valuable.
- Revival requires changed context or explicit human intent.
- Importance is measured by semantic impact, not time spent.
- A roadmap should change because project meaning changed, not because conversation volume increased.
- Final convergence may simplify the story, but must not invent a linear process that never happened.

## v0.1 scope

This release focuses on the behavioral model and project-state logic. It does not yet include a GUI, vector database, autonomous file ingestion, or automatic integration with Figma/Codex/Notion.

## Evaluation

`evaluation/RETROSPECTIVE_CASE_01.md` contains the first real-project retrospective evaluation. The public case is anonymized and deliberately does not claim controlled A/B evidence.

The next release should add a controlled evaluation harness that gives the same project context to an LLM with and without Design Roadmap Guardian, then compares:

- premature deep dives;
- unnecessary roadmap revisions;
- false rejections;
- missed replan triggers;
- final narrative fidelity.

## Status

Experimental research prototype. Not a project-management replacement; it is a reasoning layer for maintaining intentionality during nonlinear human–AI work.
