# Failure-case Workflow Review Queue Dashboard Surfacing Review

Status: review-only gate.

Phase marker: failure-case workflow review queue dashboard surfacing review v0.

## Goal

Decide how the failure-case workflow review queue should appear in the plain operations dashboard before changing dashboard rendering.

The existing queue endpoint is:

```text
GET /failure-cases/workflow-review-queue
```

The future dashboard surface is:

```text
GET /ops/dashboard
```

## Current Evidence

Phase 357 implemented the read model:

```text
queue_boundary: failed_workflow_review_queue_read_model_only
persistence_boundary: read_model_only_no_automatic_failure_case_creation
review statuses: needs_failure_case_review, failure_case_linked
```

Phase 358 verified it against a local fresh migrated Docker DB and live FastAPI process:

```text
pending_review_count: 1
linked_failure_case_count: 1
completed workflow excluded
failure_cases still manual
```

## Selected Dashboard Surface

The next dashboard implementation should add a compact section named:

```text
Failure-case Workflow Review Queue
```

It should show:

- `pending_review_count`
- `linked_failure_case_count`
- workflow id or detail link
- workflow status
- stage
- error type
- review status: `needs_failure_case_review` or `failure_case_linked`
- linked failure-case count
- draft preview link to `POST /failure-cases/draft-preview`

The section should reuse the existing queue builder rather than duplicate queue logic inside the HTML route.

## Explicit Non-change

Do not add dashboard rendering in this review gate.

This review does not change:

- route behavior
- dashboard HTML
- database schema
- migration files
- failure-case persistence rules
- root-cause handling

## Boundary

This is a review-only gate.

It is:

- not automatic failure-case creation
- not root-cause automation
- not complete workflow failure causality
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete evidence

The dashboard must keep the human confirmation boundary visible. A row that needs review may point toward draft preview, but it must not imply that the dashboard creates or confirms `failure_cases`.

## Next Gate

next product gate: failure-case workflow review queue dashboard surfacing v0

That implementation gate may update `GET /ops/dashboard` to show the selected compact section, with tests proving the section displays counts and rows without creating failure cases.
