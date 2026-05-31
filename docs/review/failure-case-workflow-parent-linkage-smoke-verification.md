# Failure-case workflow parent linkage smoke verification

## Status

Accepted.

This is a route-level smoke, not fresh Docker DB evidence.

## Scope

This smoke verifies that the API can manually persist a failure case with a workflow parent link and return that link on list output.

It also verifies that `POST /failure-cases/draft-preview` carries `workflow_run_id` into its suggested draft payload.

The goal is narrow linkage proof. It does not add automatic failure-case creation, automatic failure-case persistence, a confirm endpoint, hosted deployment evidence, or complete workflow failure causality.

## Test paths

The route tests are:

```text
tests/test_routes.py::test_failure_case_can_retain_manual_workflow_parent_link
tests/test_routes.py::test_failure_case_draft_preview_suggests_manual_payload_without_persistence
```

## Verification command

```powershell
cd apps/api
uv run pytest tests/test_routes.py -q -k "failure_case_can_retain_manual_workflow_parent_link or failure_case_draft_preview_suggests_manual_payload"
```

Observed output:

```text
2 passed, 67 deselected, 1 warning
```

## Smoke path A

```text
POST /workflow-runs
  -> workflow_run.id
  -> POST /failure-cases with workflow_run_id
  -> GET /failure-cases
```

Observed behavior:

- workflow parent creation returns `status_code: 201`
- failure-case creation returns `status_code: 201`
- workflow_run_id retained in the created failure-case response
- workflow_run_id retained in `GET /failure-cases`
- persistence remains manual and explicit

## Smoke path B

```text
POST /failure-cases/draft-preview
  -> response.draft.workflow_run_id
```

Observed behavior:

- draft-preview returns `status_code: 200`
- `persistence_boundary: preview_only_not_persisted`
- `human_confirmation_required: true`
- draft-preview carries workflow_run_id into the suggested draft payload
- preview still does not create `failure_cases`

## Claim boundary

Allowed claim:

```text
The API can manually persist a failure case with a workflow parent link, and draft-preview can preserve workflow_run_id for a human-confirmed handoff.
```

Forbidden claims:

```text
This is not automatic failure-case creation.
This is not automatic failure-case persistence.
This is not fresh Docker DB evidence.
This is not hosted deployment evidence.
This is not complete workflow failure causality.
```

## Next bounded gate

The next bounded gate should be:

```text
failure-case workflow parent linkage fresh-db verification v0
```

That gate should run the migration and the manual workflow-parent failure-case path against a fresh migrated PostgreSQL database before application-facing docs treat the linkage as runtime DB evidence.
