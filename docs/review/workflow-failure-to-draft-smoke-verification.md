# Workflow failure-to-draft smoke verification

## Status

Accepted.

This is a route-level smoke, not fresh Docker DB evidence.

## Scope

This smoke verifies that a failed deterministic workflow parent can feed `POST /failure-cases/draft-preview` without creating a persisted failure case.

The goal is a narrow workflow-failure-to-draft proof. It does not add automatic failure-case creation, automatic failure-case persistence, a confirm endpoint, or complete workflow failure causality.

## Test path

The route test is:

```text
tests/test_routes.py::test_failed_workflow_parent_can_feed_failure_case_draft_preview_without_persistence
```

The route-level smoke path is:

```text
POST /workflow-runs/execute-preview
  -> workflow_run.status: failed
  -> POST /failure-cases/draft-preview
  -> preview_only_not_persisted
  -> failure_cases remain unchanged
```

## Verification command

```powershell
cd apps/api
uv run pytest tests/test_routes.py -q -k "failed_workflow_parent"
```

Observed output:

```text
1 passed, 67 deselected, 1 warning
```

## Smoke input

The workflow failure is produced by an intentionally failing repository fixture:

```text
EvidencePersistenceFailureRepository.create_evidence_ledger_entries
  -> RuntimeError("simulated evidence persistence failure")
```

The failed workflow parent then feeds draft preview with:

```json
{
  "workflow_run_id": "<failed workflow_run.id>",
  "question": "<failed workflow_run.question>",
  "workflow_status": "failed",
  "error_message": "simulated evidence persistence failure",
  "trace_json": {
    "stage": "workflow_execute_preview",
    "error_type": "RuntimeError"
  }
}
```

## Observed behavior

The fixture proves:

- `POST /workflow-runs/execute-preview` returns `status_code: 500` for the fixture failure
- one workflow parent record is created
- `workflow_run.status: failed`
- `workflow_run.error_message: simulated evidence persistence failure`
- `workflow_run.trace_json.stage: workflow_execute_preview`
- `workflow_run.trace_json.error_type: RuntimeError`
- `failure_cases` are empty before draft preview
- `POST /failure-cases/draft-preview` returns `status_code: 200`
- `persistence_boundary: preview_only_not_persisted`
- `human_confirmation_required: true`
- `source_summary.workflow_status: failed`
- `source_summary.stage: workflow_execute_preview`
- `source_summary.error_type: RuntimeError`
- `draft.failure_type: workflow_stage_error`
- `draft.fix_status: draft`
- warnings include that the preview does not create `failure_cases`
- failure_cases remain unchanged after draft preview

## Claim boundary

Allowed claim:

```text
A failed deterministic workflow parent can feed the non-persisting failure-case draft-preview endpoint.
```

Forbidden claims:

```text
This is not automatic failure-case creation.
This is not automatic failure-case persistence.
This is not a confirm endpoint.
This is not fresh Docker DB evidence.
This does not add workflow_run_id to failure_cases.
This is not complete workflow failure causality.
```

## Why this gate comes before automation

The workflow parent can now carry failure-stage evidence into a draft payload, but the system still asks a human to confirm whether the draft should become a durable failure record.

That is the correct boundary until the project can prove stronger incident classification and causality.

## Next bounded gate

The next bounded gate should be:

```text
workflow failure-to-draft application refresh v0
```

That gate should expose this smoke artifact in application-facing docs without implying automatic failure-case creation, automatic persistence, fresh Docker DB runtime proof, or complete workflow failure causality.
