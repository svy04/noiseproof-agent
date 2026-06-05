# Workflow Proof Bundle Failure-case Links

Status: implemented.

Phase marker: workflow proof bundle failure-case links v0.

## Purpose

After caller-triggered workflow failure-case persistence, a reviewer should not have to inspect `/failure-cases` separately to discover whether a failed workflow parent already has a linked failure case.

This gate extends the existing workflow detail and proof bundle read models so linked failure cases are visible through the workflow inspection path.

## Implemented Surface

Routes:

```text
GET /workflow-runs/{id}
GET /workflow-runs/{id}/proof-bundle
GET /failure-cases?workflow_run_id={id}
```

Read-model additions:

```text
WorkflowRunDetailOut.failure_cases
WorkflowRunDetailSummaryOut.failure_case_count
WorkflowProofBundleOut.detail.failure_cases
WorkflowProofBundleOut.detail.summary.failure_case_count
WorkflowProofBundleOut.proof_surfaces includes /failure-cases?workflow_run_id={id} when linked failure cases exist
```

Repository lookup:

```text
lookup_workflow_run_records(workflow_run_id) now includes failure_cases linked by workflow_run_id.
```

## Behavior

When a failure case has `workflow_run_id` equal to the inspected workflow run:

```text
GET /workflow-runs/{id} returns failure_cases[] and failure_case_count.
GET /workflow-runs/{id}/proof-bundle returns the same linked failure_cases[] through detail.
GET /failure-cases?workflow_run_id={id} filters the failure-case list to that workflow parent.
```

This keeps the proof bundle aligned with the existing caller-triggered persistence handoff:

```text
POST /failure-cases/workflow-runs/{workflow_run_id}
persistence_boundary -> caller_triggered_workflow_failure_case_persistence
```

## Boundaries

This is a read model only.

It is not automatic failure detection.

It is not background automation.

It is not complete workflow failure causality.

It is not root-cause automation.

It is not a retry or repair system.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.

The linked failure case proves only that a persisted failure-case record explicitly references the workflow parent by `workflow_run_id`.

## Verification

Targeted route test:

```powershell
cd apps/api
uv run pytest -q tests/test_routes.py -k "workflow_proof_bundle_surfaces_linked_failure_cases_read_only"
```

The test first failed because `GET /workflow-runs/{id}` did not expose `failure_cases`.

The green path verifies:

```text
linked failure_cases are returned from GET /workflow-runs/{id}
linked failure_cases are returned through GET /workflow-runs/{id}/proof-bundle detail
failure_case_count is 1 for the workflow parent
GET /failure-cases?workflow_run_id={id} filters out unrelated failure cases
proof_surfaces includes /failure-cases?workflow_run_id={id}
```

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
