# Failure-case Workflow Parent Linkage Dashboard Review

Status: review-only gate.

Phase marker: Failure-case workflow parent linkage dashboard review v0.

This review decides how the plain operations dashboard should surface manually persisted failure-case workflow parent links after Phase 78 verified the fresh migrated Docker DB path.

## Current state

The current `GET /ops/dashboard` Failure Cases table renders:

- created time
- failure type
- description
- fix status
- next action

The API and persistence layer can now carry `failure_cases.workflow_run_id`, but the Failure Cases table does not yet show that parent workflow id or link to the workflow detail surface.

## Decision

The next bounded dashboard change should add a workflow parent column to the Failure Cases table when `workflow_run_id` is present.

Preferred rendering:

```text
Workflow Parent
  -> /workflow-runs/{workflow_run_id}
```

If the value is absent, render `n/a`.

## Why not implement it in this gate

Do not add dashboard rendering in this review gate.

This gate exists to avoid quietly turning a fresh DB persistence proof into a broader dashboard or causality claim. The project already has a manual workflow parent link, but it does not automatically create failure cases from workflow failures.

## Boundary

This review does not claim:

- automatic failure-case creation
- automatic failure detection
- complete workflow failure causality
- hosted deployment evidence
- production incident management
- dashboard analytics

It only selects the next small dashboard surface for an already persisted manual `workflow_run_id` field. This is not complete workflow failure causality.

## Next gate

```text
failure-case workflow parent linkage dashboard surfacing v0
```

Acceptance for the next gate:

- Failure Cases table shows `workflow_run_id` when present.
- Workflow parent values link to `/workflow-runs/{id}`.
- Missing workflow parent values render `n/a`.
- Dashboard copy says the link is manual provenance, not automatic failure-case creation.
- No schema, migration, LLM, retrieval, Evidence Ledger, report, or dashboard polish expansion.
