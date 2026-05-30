# Workflow failure provenance review

## Status

Accepted.

This is a review-only gate.

## Question

After Phase 53, the system can create a failed `agent_runs` row and a manually submitted `failure_cases` row that carries `agent_run_id`.

The question for this review is whether that is enough to add workflow-level failure links or automatic failure detection.

## Current evidence

Implemented evidence:

- `POST /agent-runs` can create an operation-level failed run.
- `POST /failure-cases` can create a manual failure record.
- `failure_cases.agent_run_id` can retain a link to the failed agent run.
- `GET /failure-cases` can list the linked failure case.
- `GET /agent-runs` can list the linked failed agent run.
- `GET /ops/summary` can count both rows.
- `docs/review/agent-run-failure-linkage-smoke-verification.md` records the fresh DB smoke evidence.

This proves operation-level failure linkage for a manual failure record.

## What remains unproven

The current evidence does not prove workflow-level failure causality.

Still unproven:

- which workflow stage produced the failure
- whether the failure came from retrieval, evidence, gate, report, parser, or user input
- whether a failure case was generated automatically
- whether a `workflow_runs` parent should own the failure
- whether a failed child stage should update the workflow parent status
- whether failure cases should be joined directly to `workflow_runs`
- whether every failed operation should create exactly one failure case

## Decision

Keep the current failure evidence at operation-level failure linkage until a real workflow failure path exists.

Do not add workflow_run_id to failure_cases in this review gate.

Do not add automatic failure detection in this review gate.

Do not claim that the linked failure case proves workflow-level failure causality.

## Why

The linked failure smoke shows that a manual failure record can point at an `agent_runs` row. That is useful and inspectable.

But the current record does not know which workflow parent, deterministic stage, persisted child record, or stage input manifest caused the failure. Adding `workflow_run_id` now would create a false sense of workflow failure causality.

The system should not imply a causal chain that it cannot yet prove.

## Next bounded gate

The next bounded implementation should be:

```text
workflow failure linkage smoke verification v0
```

That gate should use an existing deterministic workflow boundary or a deliberately failed workflow execution path only if the current API can produce one without inventing broad new orchestration.

If no real failed workflow execution path exists yet, the next gate should remain a review or test-fixture gate rather than adding schema.

## Boundary

This review adds no runtime behavior, no schema, no migration, no `workflow_run_id` column on `failure_cases`, no automatic failure detection, no repair automation, no hosted deployment evidence, no distributed tracing, no external observability, no LLM-backed failure analysis, no embeddings, no semantic retrieval, no autonomous workflow execution, and no free-form final answer generation.
