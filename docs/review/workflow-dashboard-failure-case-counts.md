# Workflow Dashboard Failure-case Counts

Status: implemented.

Phase marker: workflow dashboard failure-case counts v0.

## Purpose

After workflow failure cases became visible in workflow detail and proof bundle read models, the operations dashboard still required a reviewer to open each workflow row before seeing whether a linked failure case already existed.

This gate adds a small read-only dashboard cue: workflow rows now show linked failure-case counts and link to the existing filtered failure-case list when at least one failure case references the workflow parent.

## Implemented Surface

Route:

```text
GET /ops/dashboard
```

Dashboard additions:

```text
Workflow Runs table column: Linked Failure Cases
Linked count greater than 0 links to GET /failure-cases?workflow_run_id={id}
Linked count equal to 0 renders as plain 0 with no failure-case filter link
```

Boundary copy:

```text
Workflow failure-case counts are read-only links over existing records.
```

## Behavior

When an existing `failure_cases` row has `workflow_run_id` equal to a workflow parent:

```text
GET /ops/dashboard shows Linked Failure Cases -> 1
The count links to /failure-cases?workflow_run_id={id}
```

When no linked failure case exists for that workflow parent:

```text
GET /ops/dashboard shows Linked Failure Cases -> 0
No /failure-cases?workflow_run_id={id} filter link is emitted for that workflow row
```

## Boundaries

This is a dashboard read model over existing records.

It is not automatic failure detection.

It is not background automation.

It is not complete workflow failure causality.

It is not root-cause automation.

It is not a retry or repair system.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.

The count proves only that persisted failure-case records explicitly reference a workflow parent by `workflow_run_id`.

## Verification

Targeted route test:

```powershell
cd apps/api
uv run pytest tests/test_routes.py::test_ops_dashboard_surfaces_workflow_failure_case_counts_and_filter_links -q
```

The test first failed because `GET /ops/dashboard` did not emit a workflow-row filter link to `/failure-cases?workflow_run_id={id}`.

The green path verifies:

```text
Linked Failure Cases column exists
linked workflow row links count 1 to /failure-cases?workflow_run_id={id}
unlinked workflow row does not emit a failure-case filter link
dashboard boundary copy says the counts are read-only links over existing records
```

Documentation test:

```powershell
cd apps/api
uv run pytest tests/test_docs.py::test_workflow_dashboard_failure_case_counts_document_read_model_boundary -q
```

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
