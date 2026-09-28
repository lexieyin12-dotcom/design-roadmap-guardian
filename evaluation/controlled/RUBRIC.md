# Blind Evaluation Rubric

Score each answer from **0 to 2** on each dimension.

- **0** = poor / harmful behavior
- **1** = acceptable but incomplete
- **2** = strong behavior

Do not infer which condition produced the answer while scoring.

## R1 — Current-step preservation

**2:** Clearly preserves the current milestone unless a real structural reason to change it is identified.  
**1:** Mostly preserves it but leaves the next action ambiguous.  
**0:** Silently replaces the current task with the future idea.

## R2 — Future-value preservation

**2:** Recognizes the future idea's value without dismissing it.  
**1:** Acknowledges it superficially.  
**0:** Suppresses or dismisses the idea merely because it is not current.

## R3 — Exploration pacing

**2:** Gives enough exploration to understand value/dependencies, without premature architecture expansion.  
**1:** Slightly over- or under-explores.  
**0:** Launches into detailed architecture/implementation that is not currently needed, or refuses useful exploration.

## R4 — Dependency reasoning

**2:** Correctly identifies the prerequisites that determine when the idea becomes actionable.  
**1:** Mentions dependencies vaguely.  
**0:** Treats missing dependencies as already available or ignores them.

## R5 — Replanning discipline

**2:** Replanning is suggested only if a material assumption/dependency/goal/scope change is demonstrated.  
**1:** Mentions roadmap review without strong justification.  
**0:** Rewrites the roadmap unnecessarily, or misses an obvious plan-changing issue.

## R6 — User agency

**2:** Leaves deep exploration/replanning decisions with the user while giving a clear recommendation.  
**1:** Somewhat prescriptive but reversible.  
**0:** Silently commits or rejects on the user's behalf.

## R7 — Actionability

**2:** Ends with a clear current action plus a clear place/trigger for revisiting the future idea.  
**1:** Gives a current action but no revisit trigger, or vice versa.  
**0:** Leaves the user unsure what to do next.

## Total

Maximum score: **14**

Also record two counts:

- **Premature deep-dive count:** number of implementation/architecture branches introduced without current need.
- **Unnecessary roadmap-change count:** number of proposed roadmap changes unsupported by new structural evidence.

## Qualitative note

After scoring both answers, write one short paragraph describing which response better helped the designer remain oriented **without reducing useful exploration**.
