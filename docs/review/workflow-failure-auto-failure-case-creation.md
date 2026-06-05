# Workflow Failure Auto Failure-case Creation

Status: implemented.

Phase marker: workflow failure auto failure-case creation v0.

## Purpose

Record the current route-level behavior where a deterministic workflow preview failure creates one linked local v0 failure case before the response returns the original workflow failure.

This closes the older local gap where failed workflow stage events were inspectable but still required a separate caller-triggered handoff to create a failure case.

## Implemented Behavior

Covered by:

```text
test_workflow_execute_preview_auto_creates_failure_case_when_stage_errors
```

Observed route-level behavior:

```text
POST /workflow-runs/execute-preview -> 500
workflow_run.status -> failed
failed_stage: evidence_ledger
workflow_stage_event_count -> 2
failure_case_count -> 1
failure_type: workflow_stage_error
fix_status: open
root_cause: RuntimeError: simulated evidence persistence failure
auto_failure_case_id -> linked failure_cases.id
failed_stage_boundary: local_workflow_stage_failure_event_auto_failure_case_local_v0
failure_case_persistence_boundary: auto_created_from_workflow_failure_local_v0
```

The created failure case is linked by `workflow_run_id`, keeps `agent_run_id` empty, records a `workflow_stage_error`, and tells the operator to inspect the failed stage event before retrying or changing data.

The workflow trace also records `auto_failure_case_id` and `failure_case_persistence_boundary` so the failed workflow parent can be inspected without guessing which failure case came from the local v0 auto-creation path.

## Code Boundary

The implementation lives in:

```text
apps/api/app/services/workflow_execution.py
```

Current markers:

```text
auto_created_from_workflow_failure_local_v0
local_workflow_stage_failure_event_auto_failure_case_local_v0
```

Read models that surface the linked failure case remain existing inspection surfaces:

```text
GET /workflow-runs/{workflow_run_id}
GET /workflow-runs/{workflow_run_id}/proof-bundle
GET /failure-cases?workflow_run_id={workflow_run_id}
GET /ops/dashboard
```

## Boundary

This is route-level local v0 failure-case creation.

It is not retry behavior.

It is not root-cause automation.

It is not complete workflow failure causality.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not Docker runtime smoke.

It is not distributed tracing.

It is not hosted observability.

It is not product-complete.

## Next Gate

```text
workflow failure auto failure-case creation runtime smoke v0 if Docker/API runtime proof is desired, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
