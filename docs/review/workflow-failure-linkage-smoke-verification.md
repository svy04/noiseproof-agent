# Workflow failure linkage smoke verification

## Status

Accepted.

This is a test-fixture smoke, not fresh Docker DB evidence.

## Question

Phase 55 kept `failure_cases` at operation-level linkage and deferred `workflow_run_id` on `failure_cases`.

This smoke asks a smaller question:

```text
If an existing deterministic workflow preview stage raises an exception, does the parent workflow run become inspectably failed?
```

## Test path

The route test uses a repository fixture that raises during Evidence Ledger persistence:

```text
tests/test_routes.py::test_workflow_execute_preview_marks_parent_failed_when_stage_errors
```

The endpoint under test is:

```text
POST /workflow-runs/execute-preview
```

The simulated failure is:

```text
simulated evidence persistence failure
```

## Observed behavior

The fixture proves:

- `workflow_run.status = failed`
- `workflow_run.error_message` records the stage exception
- `workflow_run.trace_json.stage` remains `workflow_execute_preview`
- `workflow_run.trace_json.error_type` records `RuntimeError`
- `workflow_run.ended_at` is set
- the retrieval child record created before the failure remains linked to the workflow parent
- failure_cases remain unchanged

## Claim boundary

Allowed claim:

```text
A deterministic workflow preview parent is marked failed when a downstream stage raises in the route-level test fixture.
```

Forbidden claims:

```text
This is not automatic failure detection.
This is not fresh Docker DB evidence.
This is not production incident handling.
This does not add workflow failure cases.
There is no workflow_run_id on failure_cases in this smoke.
This does not prove every workflow stage has complete failure causality.
```

## Why no schema change

This smoke verifies failed workflow parent state. It does not prove that `failure_cases` should directly reference workflow parents.

Adding `workflow_run_id` to `failure_cases` now would still imply more causal certainty than the system has. A future schema gate should wait until a real failure-case creation path decides whether failures are manually recorded, automatically detected, or derived from workflow child records.

## Next bounded gate

The next bounded gate should be:

```text
workflow failure linkage application refresh v0
```

That gate should expose this smoke artifact in application-facing docs without claiming automatic detection, fresh DB runtime proof, or complete workflow failure causality.
