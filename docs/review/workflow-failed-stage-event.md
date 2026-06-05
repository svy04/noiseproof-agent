# Workflow Failed Stage Event v0

Phase marker: workflow failed stage event v0.

## Purpose

Make deterministic workflow preview failures easier to inspect by recording the
stage that failed in the existing `workflow_stage_events` log.

## Implemented Behavior

When `POST /workflow-runs/execute-preview` fails after a workflow parent is
created, the workflow parent is still marked `failed`. In addition, the active
workflow stage now writes a `workflow_stage_events` row with:

- `stage_status = failed`
- the stage name and order that were active when the exception occurred
- the stage input summary available before the failure
- `error_type`
- `error_message`
- `failed_stage_boundary = local_workflow_stage_failure_event_no_retry_no_auto_failure_case`

For the covered regression fixture, a simulated Evidence Ledger persistence
failure leaves:

```text
retrieval -> completed
evidence_ledger -> failed
```

The failed event is exposed through:

```text
GET /workflow-runs/{workflow_run_id}
GET /workflow-runs/{workflow_run_id}/proof-bundle
```

## Test Evidence

```text
uv run pytest -q tests/test_routes.py::test_workflow_execute_preview_records_failed_stage_event_when_stage_errors
```

Observed local result:

```text
1 passed
```

## Boundary

This is local workflow failure observability only.

It does not retry the workflow, persist a failure case automatically, classify
root cause automatically, repair the failed stage, call an LLM, add distributed
tracing, provide hosted observability, prove hosted deployment, or make the
project product-complete.
