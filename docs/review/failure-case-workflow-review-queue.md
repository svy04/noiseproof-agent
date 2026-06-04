# Failure-case Workflow Review Queue

Phase marker: failure-case workflow review queue v0.

Status: implemented.

## Goal

Surface workflow parents that need human failure-case review before they are converted into persisted failure cases.

The new read model is exposed at:

```text
GET /failure-cases/workflow-review-queue
```

It reads existing `workflow_runs` and `failure_cases` rows, then groups failed, blocked, or needs-revision workflow parents by whether a manual failure case is already linked through `failure_cases.workflow_run_id`.

## Implemented Surface

Runtime boundary:

```text
queue_boundary: failed_workflow_review_queue_read_model_only
persistence_boundary: read_model_only_no_automatic_failure_case_creation
```

Response statuses:

```text
needs_failure_case_review
failure_case_linked
```

The queue item points reviewers to:

```text
POST /failure-cases/draft-preview
```

That route can prepare a draft payload, but a human still has to confirm and persist the final failure case.

## Observed Test Fixture

The route-level test covers:

- a failed workflow without a linked failure case becomes `needs_failure_case_review`
- a failed workflow with a linked failure case becomes `failure_case_linked`
- a completed workflow is excluded from the queue
- `GET /failure-cases` still returns only the manually created failure case
- the queue does not create failure_cases

## Boundary

This is a read model only.

It is:

- not automatic failure-case creation
- not root-cause automation
- not complete workflow failure causality
- not a DB migration or schema expansion
- not hosted deployment evidence
- not external reviewer feedback

The human confirmation boundary remains required before any workflow failure becomes a persisted `failure_cases` row.

## Next Gate

The next product gate can be a runtime smoke for this queue on a fresh migrated DB, or another source-first product gate. External reviewer feedback remains pending.
