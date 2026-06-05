# External Reviewer Ops Dashboard Anchor GET Runtime Request Refresh

Status: implemented.

Phase marker: external reviewer ops dashboard anchor GET runtime request refresh v0.

## Purpose

Point reviewer-facing repository surfaces to the latest `GET /ops/dashboard` anchor runtime proof.

This request refresh makes the local Docker DB plus live FastAPI dashboard-link evidence easier for an outside reviewer to find without treating that routing work as feedback.

## Linked Proof

```text
docs/review/ops-dashboard-anchor-get-runtime-smoke.md
docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md
```

The runtime proof records:

```text
GET /ops/dashboard
data-method="GET"
extracted_anchor_count: 38
unique_anchor_count: 25
all_extracted_dashboard_get_anchors_returned_200: true
post_only_draft_preview_was_not_clickable: true
```

## Updated Reviewer-facing Surfaces

```text
CONTRIBUTING.md
.github/ISSUE_TEMPLATE/external-review-feedback.md
docs/review/external-reader-proof-path.md
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
docs/review/external-reviewer-shortlist.md
docs/application/portfolio-index.md
README.md
docs/GOAL.md
docs/runbook.md
```

## Boundary

This is request-surface refresh only.

It is not a live issue body edit.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not browser automation evidence.

It is not a route behavior change.

It is not background automation.

It is not automatic failure-case creation.

It is not complete workflow failure causality.

It is not product-complete.

## Next Gate

```text
external review issue body ops dashboard anchor GET runtime refresh v0 if updating the live public issue body is useful, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
