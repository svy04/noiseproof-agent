# Workflow Failure-case Persistence Handoff

Status: accepted.

Phase marker: workflow failure-case persistence handoff v0.

## Purpose

Add an explicit persistence handoff from a reviewable workflow parent into a durable failure-case record.

Implemented endpoint:

```text
POST /failure-cases/workflow-runs/{workflow_run_id}
```

Response boundary:

```text
caller_triggered_workflow_failure_case_persistence
```

## Behavior

The endpoint:

```text
1. reads the workflow_run by id
2. accepts only failed, blocked, or needs_revision workflow statuses
3. rejects duplicate failure_cases for the same workflow_run_id
4. reuses the existing deterministic failure-case draft logic
5. persists one failure_cases row with workflow_run_id linkage
6. returns the persisted failure case, source summary, persistence boundary, and warnings
```

## Why this gate exists

Before this gate, NoiseProof had:

```text
POST /failure-cases/draft-preview
GET /failure-cases/workflow-review-queue
manual POST /failure-cases
```

That proved reviewability, but it still required a human to copy the draft payload into the persistence endpoint.

This gate closes one small operational step: the system can now persist a deterministic failure case from the workflow parent when the caller explicitly requests that handoff.

## Boundaries

This is caller-triggered.

It is not background automation.

It is not automatic root-cause classification.

It is not complete workflow failure causality.

It does not retry the workflow.

It does not mutate workflow child records.

It does not call an LLM.

It does not generate a repair plan beyond the bounded `next_action` string.

## Rejected behavior

This gate does not create failure cases automatically when a workflow fails.

That remains intentionally unclaimed because background creation would need:

```text
idempotency policy
retry policy
operator notification policy
failure taxonomy governance
workflow stage ownership rules
production observability proof
```

## Test Evidence

Targeted route tests:

```text
tests/test_routes.py::test_failure_case_workflow_parent_handoff_persists_failure_case_and_updates_review_queue
tests/test_routes.py::test_failure_case_workflow_parent_handoff_rejects_completed_workflow_and_duplicate_persistence
```

Targeted docs test:

```text
tests/test_docs.py::test_workflow_failure_case_persistence_handoff_documents_caller_triggered_boundary
```

Focused regression:

```text
uv run pytest -q tests/test_routes.py -k "failure_case or workflow_review_queue or failed_workflow_parent"
```

Full verification should still run before completion:

```text
uv run python -m compileall app ../../packages/ingestion ../../packages/review
uv run pytest -q
```
