# Failure-case draft manual handoff smoke verification

## Status

Accepted.

This is a route-level smoke, not fresh Docker DB evidence.

## Scope

This smoke verifies that a draft produced by `POST /failure-cases/draft-preview` can be manually inspected, explicitly confirmed, and submitted to the existing `POST /failure-cases` persistence endpoint.

The goal is a narrow handoff proof. It does not add automatic persistence, a confirm endpoint, incident classification, or workflow-level failure causality.

## Test path

The route test is:

```text
tests/test_routes.py::test_failure_case_draft_can_be_manually_handed_to_failure_case_persistence
```

## Verification command

```powershell
cd apps/api
uv run pytest tests/test_routes.py -q -k "failure_case_draft_can_be_manually_handed"
```

Observed output:

```text
1 passed, 66 deselected, 1 warning
```

## Smoke path

```text
POST /failure-cases/draft-preview
  -> response.draft
  -> human changes draft.fix_status from draft to open
  -> POST /failure-cases
  -> GET /failure-cases
```

## Observed behavior

The fixture proves:

- draft preview returns `status_code: 200`
- draft preview returns `persistence_boundary: preview_only_not_persisted`
- draft preview returns `human_confirmation_required: true`
- draft.fix_status: draft
- `GET /failure-cases` is empty before manual handoff
- the human-confirmed payload is submitted to `POST /failure-cases`
- persistence returns `status_code: 201`
- persisted.failure_type: workflow_stage_error
- persisted.fix_status: open
- persisted.root_cause matches the draft root cause
- `GET /failure-cases` returns one persisted row

## Human confirmation boundary

The smoke intentionally changes `draft.fix_status` to `open` before persistence.

That small edit is the human confirmation boundary. The system prepares a draft; it does not decide that the draft is a durable failure record without review.

## Claim boundary

Allowed claim:

```text
Draft-preview output can be manually handed to the existing failure-case persistence endpoint after human confirmation.
```

Forbidden claims:

```text
This is not automatic failure detection.
This is not automatic failure-case persistence.
This is not a confirm endpoint.
This is not fresh Docker DB evidence.
This does not add workflow_run_id to failure_cases.
This does not prove complete workflow failure causality.
```

## Next bounded gate

The next bounded gate should be:

```text
failure-case draft manual handoff application refresh v0
```

That gate should expose this smoke artifact in application-facing docs without implying automatic persistence or complete workflow failure causality.
