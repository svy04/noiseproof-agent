# External Reviewer Workflow Proof Bundle Failure-case Links Runtime Request Refresh

Status: implemented request-surface refresh.

Phase marker: external reviewer workflow proof bundle failure-case links runtime request refresh v0.

## Purpose

Make the workflow proof bundle failure-case links runtime smoke discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md
```

It also records this request-refresh artifact:

```text
docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md
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
workflow proof bundle failure-case links runtime smoke
```

It shows local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
GET /workflow-runs/{id}
GET /workflow-runs/{id}/proof-bundle
GET /failure-cases?workflow_run_id={id}
detail_failure_case_count: 1
bundle_failure_case_count: 1
filtered_failure_case_count: 1
unrelated_filtered_out: true
proof_surface_has_failure_case_filter: true
```

## Explicit Non-claims

This is request-surface refresh only.

It is not a live issue body edit.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not automatic failure detection.

It is not background automation.

It is not root-cause automation.

It is not complete workflow failure causality.

It is not LLM-backed repair.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Next Gate

```text
external review issue body workflow proof bundle failure-case links runtime refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
