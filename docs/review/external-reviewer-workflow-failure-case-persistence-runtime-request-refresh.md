# External Reviewer Workflow Failure-case Persistence Runtime Request Refresh

Status: implemented request-surface refresh.

Phase marker: external reviewer workflow failure-case persistence runtime request refresh v0.

## Purpose

Make the workflow failure-case persistence handoff runtime smoke discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md
```

It also records this request-refresh artifact:

```text
docs/review/external-reviewer-workflow-failure-case-persistence-runtime-request-refresh.md
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
docs/runbook.md
```

## Proof Now Highlighted

```text
workflow failure-case persistence handoff runtime smoke
```

It shows local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
POST /failure-cases/workflow-runs/{workflow_run_id}
persistence_boundary -> caller_triggered_workflow_failure_case_persistence
queue_status_for_workflow -> failure_case_linked
completed_workflow_status_code -> 409
duplicate_status_code -> 409
```

## Explicit Non-claims

This is request-surface refresh only.

It is not a live issue body edit.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not background automation.

It is not automatic root-cause classification.

It is not complete workflow failure causality.

It is not LLM-backed repair.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Next Gate

```text
external review issue body workflow failure-case persistence runtime refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
