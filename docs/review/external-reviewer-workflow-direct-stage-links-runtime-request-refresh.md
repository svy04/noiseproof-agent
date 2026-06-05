# External Reviewer Workflow Direct Stage Links Runtime Request Refresh

Status: implemented request-surface refresh.

Phase marker: external reviewer workflow direct stage links runtime request refresh v0.

## Purpose

Make the workflow direct stage links runtime smoke discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/workflow-direct-stage-links.md
docs/review/workflow-direct-stage-links-runtime-smoke.md
```

It also records this request-refresh artifact:

```text
docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md
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
workflow direct stage links runtime smoke
```

It shows local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
POST /workflow-runs/execute-preview
GET /workflow-runs/{id}/lineage
direct_stage_link_count: 3
evidence_to_report
evidence_to_noise_gate
noise_gate_to_report
direct_stage_link_table
workflow_created_records_only_not_standalone_payload_lineage
```

## Explicit Non-claims

This is request-surface refresh only.

It is not a live issue body edit.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not distributed tracing.

It is not hosted observability.

It is not autonomous workflow execution.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Next Gate

```text
external review issue body workflow direct stage links runtime refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
