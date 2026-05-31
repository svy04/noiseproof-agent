# Failure-case Workflow Parent Linkage Fresh DB Dashboard Smoke Review

Status: review-only gate.

Phase marker: Failure-case workflow parent linkage fresh DB dashboard smoke review v0.

This review decides whether the Phase 81 dashboard rendering should be verified against a fresh migrated Docker DB before making stronger application-facing claims.

## Current state

Phase 81 added a `Workflow Parent` column to the `GET /ops/dashboard` Failure Cases table.

The column renders:

- `n/a` when `failure_cases.workflow_run_id` is absent
- a `/workflow-runs/{id}` link when `failure_cases.workflow_run_id` is present
- boundary copy that calls the link a manual workflow parent link and not automatic failure-case creation

Route-level tests prove the HTML renderer behavior. Phase 78 proves manual `workflow_run_id` persistence on a fresh migrated Docker DB. The missing proof is the combined path:

```text
fresh migrated Docker DB
  -> migration runner
  -> FastAPI process
  -> POST /workflow-runs
  -> POST /failure-cases with workflow_run_id
  -> GET /ops/dashboard
  -> HTML contains Workflow Parent link
```

## Decision

Run a fresh DB dashboard smoke verification next.

The goal should be to prove only that the browser-readable operations surface can display the already persisted manual workflow parent link in a fresh local runtime.

## Boundary

Do not run the fresh DB smoke in this review gate.

This review does not claim:

- hosted deployment evidence
- production migration orchestration
- automatic failure-case creation
- automatic failure detection
- complete workflow failure causality
- dashboard analytics
- incident management readiness

In short: this is not automatic failure-case creation and not complete workflow failure causality.

It only selects the next smoke check.

## Next gate

```text
failure-case workflow parent linkage fresh-db dashboard smoke verification v0
```

Acceptance for the next gate:

- Use an isolated Docker Compose project and port.
- Apply migrations through `python -m app.migration_runner apply`.
- Start a real FastAPI process with `DATABASE_URL` pointing at the fresh DB.
- Create a workflow run.
- Create a failure case with that `workflow_run_id`.
- Fetch `GET /ops/dashboard`.
- Record that the HTML includes `Failure Cases`, `Workflow Parent`, the workflow id link, `manual workflow parent link`, and `not automatic failure-case creation`.
- Clean up the API process and Docker volume.
