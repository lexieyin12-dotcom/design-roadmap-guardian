# Design Roadmap Guardian — Evaluation Cases v0.1

Use these cases to evaluate whether the skill manages nonlinear work without suppressing useful exploration.

## Dimensions

- **D1 Trajectory classification** — ON_TRACK / NECESSARY_DETOUR / FUTURE_EXPLORATION / PLAN_CHANGING
- **D2 Exploration pacing** — enough depth without premature implementation expansion
- **D3 State update** — correct idea/decision/parking/roadmap state
- **D4 Intervention timing** — no unnecessary interruption; review at meaningful boundaries
- **D5 Long-term integrity** — stored state supports future consistency and truthful convergence

## Case 1 — Valuable future capability appears too early

Current step: validate a core prototype.

User asks whether a future AI capability could provide live assistance using project data.

Expected:

- `FUTURE_EXPLORATION`
- relevance HIGH, readiness LOW
- identify major dependencies
- preserve the idea
- do not immediately expand into implementation architecture unless asked
- usually `PARKED` with a revisit trigger

Failure: the model spends the next several turns designing APIs, streaming, memory, and orchestration even though the core prototype has not been validated.

## Case 2 — User deliberately deep-dives a future branch

Same context as Case 1, but the user explicitly says the future direction may affect today's architecture and wants to explore it now.

Expected:

- still `FUTURE_EXPLORATION`
- temporary deep dive permitted
- preserve the original current step
- return to the main trajectory afterward unless the branch reveals a real dependency change

## Case 3 — Necessary detour

Current step: validate the prototype.

Testing shows unreliable results because an implementation dependency is unstable.

Expected:

- `NECESSARY_DETOUR`
- resolve the blocking dependency first
- record the dependency if meaningful
- do not label the project as drifting

## Case 4 — Dependency change

Original roadmap:

`Prototype Test -> Implementation -> Evaluation`

Evidence shows an interpretation/preparation step must occur before implementation.

Expected:

- `PLAN_CHANGING`
- `DEPENDENCY_CHANGE`, severity HIGH
- replan pressure at least WATCH
- propose insertion of missing steps at a meaningful review boundary

## Case 5 — Temporary pause is not rejection

User says: "Pause the unreliable experimental branch for now and prioritize the stable core path."

Expected: `PARKED`, not `REJECTED`.

Failure: later summary states the project permanently does not use that branch.

## Case 6 — Silence is not rejection

Two design directions were explored. The project continues with B; A is never explicitly rejected.

Expected: B `ACTIVE`; A `DORMANT` or possibly `SUPERSEDED` if replacement is explicit enough.

Prohibited: A `REJECTED` solely because B moved forward.

## Case 7 — Explicit rejection

User states that a direction should no longer be used and gives a structural reason.

Expected: `REJECTED`, with the reason and reason type preserved.

Do not resurface it unless the underlying condition changes or the user explicitly reopens it.

## Case 8 — Parked idea becomes actionable

A future capability was parked because its primary dependency was missing. Later that dependency is completed.

Expected: surface it as a revival candidate. Do not make it `ACTIVE` automatically. If user revisits, transition `PARKED -> EXPLORING`.

## Case 9 — User revives a rejected idea

User says a new condition may solve the original rejection reason.

Expected: `REJECTED -> EXPLORING`; recall the old reason and compare it against the new condition.

## Case 10 — Repeated detour becomes structural

The same supposedly future issue appears in research, implementation, and evaluation decisions.

Expected: `REPEATED_DETOUR` signal; increase planning relevance and suggest roadmap review at a sensible boundary.

## Case 11 — High downstream impact

A new decision changes implementation, data handling, interaction, evaluation, and validation.

Expected: `PLAN_CHANGING` + `DOWNSTREAM_IMPACT` HIGH.

## Case 12 — Minor local edit

User changes a label, spacing, icon size, or a single local interaction detail.

Expected: `ON_TRACK`. No plan signal and no roadmap review.

## Case 13 — Many minor edits still do not imply replanning

Several local UI changes happen in one session.

Expected: do not infer plan instability from activity volume.

## Case 14 — A ten-minute discovery invalidates the architecture

A short experiment disproves a core assumption.

Expected: `PLAN_CHANGING` + `ASSUMPTION_BREAK` HIGH. Importance is determined by semantic impact, not time spent.

## Case 15 — Mock must remain mock

A polished interface contains placeholder metrics.

Expected: preserve epistemic state as `MOCK`; final convergence must not describe the metric as implemented, tested, or validated.

## Case 16 — Planned capability must not become current capability

A basic capability exists; a live-data extension is only planned.

Expected final wording distinguishes what exists from what is designed for later.

## Case 17 — Do not rewrite the roadmap three times in one day

A future idea, a UI edit, a technical possibility, and a minor bug appear in one session.

Expected: classify independently; preserve roadmap unless they collectively change project structure.

## Case 18 — Milestone boundary triggers review

Several meaningful plan signals accumulated during a technical milestone, and the milestone is now complete.

Expected: suggest roadmap review before the next stage.

## Case 19 — Critical inconsistency interrupts immediately

The user is about to build on a capability that does not actually exist.

Expected: `CRITICAL`; surface immediately rather than waiting for a milestone.

## Case 20 — Final convergence is not chronology

Real history contains many branches and failed alternatives.

Bad output: a list of everything explored.

Expected L2 output: the smallest evidence -> interpretation -> decision -> outcome chain required to explain the final system.

## Case 21 — Expensive work may be narratively irrelevant

Several hours of setup/debugging do not change design direction, evidence, or project understanding.

Expected: retain in L0 if useful; usually exclude from L1-L3.

## Case 22 — Failed experiment may be central

An experiment fails but invalidates a core assumption and changes architecture.

Expected: retain in the core reasoning chain.

## Case 23 — Portfolio compression

A long project trace must become:

`Problem -> Evidence -> Insight -> Decision -> Prototype -> Validation -> Iteration -> Final System`

Every major claim must remain traceable to real events.

## Case 24 — Research-paper compression

The same trace should become:

`Research Question -> Hypothesis -> Method -> Evidence -> Finding -> Interpretation -> Limitation -> Conclusion`

Do not simply reuse portfolio prose.

## Case 25 — Goal change

The user explicitly changes the project's fundamental purpose.

Expected: `PLAN_CHANGING` + `GOAL_CHANGE` CRITICAL; immediate roadmap review.

## v0.1 success criteria

The skill should:

- preserve a stable main trajectory;
- allow useful exploration;
- prevent premature implementation deep dives;
- track unresolved and parked directions;
- recognize changed dependencies;
- selectively suggest replanning;
- preserve decision history;
- reconstruct a truthful final reasoning chain.
