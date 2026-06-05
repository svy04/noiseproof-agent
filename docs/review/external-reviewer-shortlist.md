# External Reviewer Shortlist

Status: implemented.

Phase marker: external reviewer shortlist v0.

## Purpose

Give outside reviewers a 90-second shortlist before they open the full proof path.

This file points to a maximum five proof artifacts that cover the current portfolio signal without asking the reviewer to read the whole repository.

It does not replace the full proof path.

## 90-second shortlist

1. `README.md`
   - Scope, non-goals, implementation status, and the current proof boundaries.
2. `docs/review/ops-dashboard-anchor-get-runtime-smoke.md`
   - Local Docker PostgreSQL plus live FastAPI HTTP proof that `GET /ops/dashboard` exposes clickable `data-method="GET"` inspection anchors and every unique dashboard href returns GET 200.
   - Request refresh: `docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md`.
   - Browser proof: `docs/review/ops-dashboard-anchor-browser-smoke.md`.
   - Browser request refresh: `docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md`.
   - Related dashboard proof: `docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md`.
   - Related direct stage links runtime proof: `docs/review/workflow-direct-stage-links-runtime-smoke.md`.
   - Direct stage links request refresh: `docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md`.
   - Related stage event log runtime proof: `docs/review/workflow-stage-event-log-runtime-smoke.md`.
   - Stage event log request refresh: `docs/review/external-reviewer-workflow-stage-event-log-runtime-request-refresh.md`.
   - Related failed stage event runtime proof: `docs/review/workflow-failed-stage-event-runtime-smoke.md`.
   - Failed stage event request refresh: `docs/review/external-reviewer-workflow-failed-stage-event-runtime-request-refresh.md`.
   - Related workflow failure auto-created failure-case runtime proof: `docs/review/workflow-failure-auto-failure-case-creation-runtime-smoke.md`.
   - Workflow failure auto-creation request refresh: `docs/review/external-reviewer-workflow-failure-auto-creation-runtime-request-refresh.md`.
   - Related workflow failure auto-created failure-case dashboard runtime proof: `docs/review/workflow-failure-auto-created-failure-case-dashboard-runtime-smoke.md`.
   - Workflow failure auto-created failure-case dashboard request refresh: `docs/review/external-reviewer-workflow-failure-auto-created-dashboard-runtime-request-refresh.md`; records `dashboard_contains_auto_created_failure_case_id`, `dashboard_contains_workflow_parent_link`, `dashboard_contains_review_queue_linked_count`, and `not external reviewer feedback`.
   - Related uploaded PDF no-text failure candidate runtime proof: `docs/review/uploaded-pdf-no-text-failure-candidate-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-pdf-no-text-failure-candidate-runtime-request-refresh.md`; records `pdf_no_extractable_text`, `chunk_handoff_no_chunks`, and `not robust PDF extraction`.
   - Related persisted document failure candidate draft preview runtime proof: `docs/review/persisted-document-failure-candidate-draft-preview-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-persisted-document-failure-candidate-draft-runtime-request-refresh.md`; records `preview_only_not_persisted`, `failure_case_count_delta -> 0`, and `not automatic failure-case creation`.
   - Related persisted document failure candidate manual handoff runtime proof: `docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-persisted-document-failure-candidate-manual-handoff-runtime-request-refresh.md`; records `failure_case_count_delta -> 1`, human confirmation, and `not a confirm endpoint`.
3. `docs/review/uploaded-raw-file-guard-ops-summary-runtime-smoke.md`
   - Local runtime proof that raw-file guard decisions surface in `/ops/summary` and `/ops/dashboard`.
4. `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md`
   - Owner-runtime proof that the ClamAV endpoint detects an owner-provided malicious test input without committing or logging the payload.
5. `docs/review/retrieval-run-linked-report-runtime-smoke.md`
   - Proof that report generation is linked to retrieval, Evidence Ledger, and Noise Gate records while refusing unsupported pre-report flow.

Then use:

```text
docs/review/external-feedback-intake-criteria.md
```

to decide whether a comment would count as external reviewer feedback.

## Why These Five

These artifacts show:

```text
service operation
reviewer navigation
guarded raw-file handling
malware-scanning boundary evidence
retrieval -> ledger -> gate -> report linkage
```

They are intentionally not exhaustive.

The full path remains:

```text
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-link-map.md
docs/application/portfolio-index.md
```

## Boundary

This is reviewer navigation only.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

It does not make any proof stronger than the linked artifacts.
