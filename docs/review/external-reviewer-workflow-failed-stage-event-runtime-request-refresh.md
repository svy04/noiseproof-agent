# External Reviewer Workflow Failed Stage Event Runtime Request Refresh

Status: implemented request-surface refresh.

Phase marker: external reviewer workflow failed stage event runtime request refresh v0.

## Purpose

Make the workflow failed stage event runtime smoke discoverable from
reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/workflow-failed-stage-event.md
docs/review/workflow-failed-stage-event-runtime-smoke.md
```

It also records this request-refresh artifact:

```text
docs/review/external-reviewer-workflow-failed-stage-event-runtime-request-refresh.md
```

It updates repository request surfaces only.

It does not edit the live public GitHub issue body.

## Reviewer-facing Surfaces Refreshed

Updated surfaces:

```text
CONTRIBUTING.md
.github/ISSUE_TEMPLATE/external-review-feedback.md
README.md
docs/GOAL.md
docs/application/braincrew-role-map.md
docs/application/portfolio-index.md
docs/review/application-ready-review.md
docs/review/external-reader-proof-path.md
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
docs/review/external-reviewer-shortlist.md
docs/runbook.md
```

## Proof Now Highlighted

```text
workflow failed stage event runtime smoke
```

It shows local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
POST /workflow-runs/execute-preview -> 500
GET /workflow-runs/{id} -> 200
GET /workflow-runs/{id}/proof-bundle -> 200
workflow_stage_event_count: 2
retrieval -> completed
evidence_ledger -> failed
failure_case_count_delta -> 0
local_workflow_stage_failure_event_no_retry_no_auto_failure_case
```

## Explicit Non-claims

This is request-surface refresh only.

It is not a live issue body edit.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not retry behavior.

It is not automatic failure-case creation.

It is not root-cause automation.

It is not distributed tracing.

It is not hosted observability.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Next Gate

```text
external review issue body workflow failed stage event runtime refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
