# Failure-case creation path review

## Status

Accepted.

This is a review-only gate.

## Question

The system can already:

- manually store failure cases through `POST /failure-cases`
- link manual failure cases to `agent_runs` through `agent_run_id`
- mark deterministic workflow preview parents as `failed` when a downstream stage raises

The question is what should create the next failure case:

- the system automatically
- a human manually after inspection
- a draft produced from failed workflow evidence and then confirmed by a human

## Decision

Select a manual failure-case draft path before automation.

Do not automatically create failure_cases from workflow failures.

Policy phrase:

```text
do not automatically create failure_cases from workflow failures
```

Keep a human confirmation boundary.

The schema remains unchanged.

There is no new API endpoint in this review gate.

## Why

Automatic failure creation would make the system look more mature than it is.

The current workflow failure smoke proves that a parent workflow can be marked failed when a stage raises. It does not prove that the system can classify root cause, choose a durable failure type, decide owner/action, or distinguish expected blocked outcomes from actual defects.

A manual failure-case draft is the smallest safe next direction:

- inspect a failed workflow parent
- propose a failure type
- propose a description
- propose a root cause if visible
- propose a next action
- require a human to submit or edit the final failure record

That keeps the evidence inspectable without pretending the system has automatic incident classification.

## Alternatives considered

### Automatic creation on every failed workflow

Rejected for now.

It would overclaim root-cause classification and likely create noisy failure records.

### Add `workflow_run_id` to `failure_cases` first

Rejected for now.

The relationship should follow the creation path, not precede it.

### Keep only manual `POST /failure-cases`

Acceptable, but not the highest-value next step.

The next useful improvement is to make workflow failure evidence easier for a human to turn into a failure record.

## Allowed next implementation

```text
failure-case draft preview v0
```

The preview should not persist anything. It should inspect provided workflow/failure evidence and return a suggested failure-case payload shape for human review.

## Boundaries

This review adds no runtime behavior, no schema, no migration, no API endpoint, no automatic failure detection, no automatic failure-case persistence, no workflow_run_id column on failure cases, no hosted deployment evidence, no LLM-backed root-cause analysis, no embeddings, no semantic retrieval, no autonomous workflow execution, and no free-form final answer generation.
