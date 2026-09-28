# Controlled Blind Evaluation

This folder defines a reproducible A/B evaluation for Design Roadmap Guardian.

## Goal

Compare the same model on the same project context under two conditions:

- **Baseline** — normal project-assistant instruction.
- **Guardian** — the same instruction plus Design Roadmap Guardian behavior.

The evaluator should not know which output came from which condition until scoring is complete.

## Protocol

1. Start two fresh chats using the **same model/configuration**.
2. Use `scripts/build_blind_eval.py` to assign Baseline/Guardian randomly to A and B.
3. Paste the generated Condition A prompt into Chat A and Condition B into Chat B.
4. Do not add extra context to only one condition.
5. Save both answers exactly as produced.
6. Give the two answers, labelled only A and B, to an evaluator.
7. Score using `RUBRIC.md`.
8. Reveal `answer_key.json` only after scoring.

## What this test measures

The rubric focuses on observable collaboration behavior:

- unnecessary deep dives;
- suppression of useful ideas;
- false commitment/rejection;
- unnecessary roadmap rewrites;
- missed dependency changes;
- interruption burden;
- ability to preserve a stable current step;
- quality and truthfulness of final convergence.

## What it does not measure yet

This protocol does not directly prove improved product quality, time savings, or long-term retention. Those require longer longitudinal studies.

## First case

`cases/case_01.md` models a common design-project situation: a valuable future capability appears while the current milestone is still validating a prerequisite. The case intentionally includes enough ambiguity to test whether the assistant can preserve the idea without prematurely turning it into today's task.
