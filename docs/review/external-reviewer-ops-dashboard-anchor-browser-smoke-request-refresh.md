# External Reviewer Ops Dashboard Anchor Browser Smoke Request Refresh

Status: implemented.

Phase marker: external reviewer ops dashboard anchor browser smoke request refresh v0.

## Purpose

Point reviewer-facing repository surfaces to the latest `GET /ops/dashboard` browser automation proof.

This request refresh makes the local Playwright browser automation evidence easier for an outside reviewer to find without treating that routing work as feedback.

## Linked Proof

```text
docs/review/ops-dashboard-anchor-browser-smoke.md
docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md
```

The browser proof records:

```text
GET /ops/dashboard
Playwright browser automation
browser_anchor_count: 27
browser_get_anchor_count: 27
browser_post_anchor_count: 0
post_only_draft_preview_anchor_count: 0
post_only_draft_preview_cue_visible: true
all_browser_get_anchors_marked_get: true
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

It is not customer validation.

It is not Braincrew acceptance.

It is not a route behavior change.

It is not background automation.

It is not automatic failure-case creation.

It is not complete workflow failure causality.

It is not design quality evidence.

It is not product-complete.

## Next Gate

```text
external feedback current-state ops dashboard anchor browser smoke issue verification v0, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
