# Failure-case draft preview smoke verification

## Status

Accepted.

This is a route-level smoke, not fresh Docker DB evidence.

## Scope

This smoke verifies that `POST /failure-cases/draft-preview` can prepare a manual failure-case draft from workflow failure evidence without persisting a failure case.

The goal is narrow preview-boundary evidence. It does not test automatic failure detection, incident classification, production workflow causality, or database persistence.

## Test path

The route test is:

```text
tests/test_routes.py::test_failure_case_draft_preview_suggests_manual_payload_without_persistence
```

The endpoint under test is:

```text
POST /failure-cases/draft-preview
```

## Verification command

```powershell
cd apps/api
uv run pytest tests/test_routes.py -q -k "failure_case_draft_preview"
```

Observed output:

```text
1 passed, 65 deselected, 1 warning
```

## Smoke input

```json
{
  "workflow_run_id": "<uuid>",
  "question": "Which segment had enterprise demand growth?",
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

- `status_code: 200`
- `persistence_boundary: preview_only_not_persisted`
- `human_confirmation_required: true`
- `source_summary.workflow_status: failed`
- `source_summary.stage: workflow_execute_preview`
- `source_summary.error_type: RuntimeError`
- `draft.failure_type: workflow_stage_error`
- `draft.fix_status: draft`
- `draft.root_cause: RuntimeError: simulated evidence persistence failure`
- warnings include that the preview does not create `failure_cases`
- warnings include that human confirmation is required
- failure_cases remain unchanged

## Claim boundary

Allowed claim:

```text
The draft-preview endpoint can turn workflow failure evidence into a non-persisting, human-confirmed failure-case draft payload.
```

Forbidden claims:

```text
This is not automatic failure detection.
This is not automatic failure-case persistence.
This is not fresh Docker DB evidence.
This is not production incident classification.
This is not complete workflow failure causality.
There is no workflow_run_id on failure_cases in this smoke.
```

## Why no persistence claim

The endpoint is intentionally a preview boundary. It returns a suggested payload shaped for manual review before a separate `POST /failure-cases` call.

Persisting the draft automatically would imply stronger incident-detection and workflow-causality guarantees than the system has.

## Next bounded gate

The next bounded gate should be:

```text
failure-case draft preview smoke application refresh v0
```

That gate should expose this smoke artifact in application-facing docs without claiming automatic detection, fresh DB runtime proof, or complete workflow failure causality.
