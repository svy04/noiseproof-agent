# External Reviewer Workflow Proof Bundle Request Refresh

Status: implemented request-surface refresh.

Phase marker: external reviewer workflow proof bundle request refresh v0.

## Purpose

Make the workflow proof bundle runtime smoke discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/workflow-proof-bundle-runtime-smoke.md
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
workflow proof bundle runtime smoke
```

It shows local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
GET /workflow-runs/{id}/proof-bundle
health_status: ok
execute_preview_status_code: 201
proof_bundle_status_code: 200
metadata_only_proof_bundle_status_code: 200
bundle_boundary: read_model_only_existing_records_no_new_storage
metadata_only_trace_is_null: true
```

## Explicit Non-claims

This is request-surface refresh only.

It is not live issue body edit.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not distributed tracing.

It is not hosted observability.

It is not new lineage storage.

It is not direct Evidence Ledger -> Noise Gate -> Report foreign-key lineage.

It is not semantic retrieval quality evidence.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Next Gate

```text
external review issue body workflow proof bundle refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
