# External Reviewer Workflow Proof Bundle Dashboard Runtime Request Refresh

Status: implemented request-surface refresh.

Phase marker: external reviewer workflow proof bundle dashboard runtime request refresh v0.

## Purpose

Make the workflow proof bundle dashboard runtime smoke discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md
```

It also records this request-refresh artifact:

```text
docs/review/external-reviewer-workflow-proof-bundle-dashboard-runtime-request-refresh.md
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
docs/review/external-reader-proof-path.md
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
docs/runbook.md
```

## Proof Now Highlighted

```text
workflow proof bundle dashboard runtime smoke
```

It shows local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
GET /ops/dashboard
GET /workflow-runs/{id}/proof-bundle
health_status: ok
execute_preview_status_code: 201
dashboard_status_code: 200
dashboard_contains_detail_link: true
dashboard_contains_lineage_link: true
dashboard_contains_proof_bundle_link: true
proof_bundle_status_code: 200
proof_bundle_link_label: proof bundle
bundle_boundary: read_model_only_existing_records_no_new_storage
```

## Explicit Non-claims

This is request-surface refresh only.

It is not a live issue body edit.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not distributed tracing.

It is not hosted observability.

It is not new lineage storage.

Direct Evidence Ledger -> Noise Gate -> Report stage links are now represented by Phase 530 workflow-created link tables; this request refresh remains bounded to reviewer routing.

It is not semantic retrieval quality evidence.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Next Gate

```text
external review issue body workflow proof bundle dashboard runtime refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
