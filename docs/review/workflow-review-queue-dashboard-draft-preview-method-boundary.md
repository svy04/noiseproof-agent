# Workflow Review Queue Dashboard Draft-preview Method Boundary

Status: implemented.

Phase marker: workflow review queue dashboard draft-preview method boundary v0.

## Purpose

Make the `Failure-case Workflow Review Queue` section in `GET /ops/dashboard` honest about the draft-preview route method.

The route is:

```text
POST /failure-cases/draft-preview
```

It is not a clickable GET page.

## Change

Before this gate, the dashboard rendered `draft preview` as a link to `/failure-cases/draft-preview`.

That looked inspectable but was misleading because the route is POST-only.

The dashboard now renders a method-aware cue:

```text
POST /failure-cases/draft-preview
draft preview requires an explicit POST request
```

This is not a clickable GET link.

The old clickable anchor shape is intentionally absent from the dashboard:

```text
anchor to /failure-cases/draft-preview with label "draft preview"
```

## Code Boundary

Changed code:

```text
apps/api/app/services/ops_dashboard.py
```

The review queue table now uses `_post_only_cue(...)` instead of linking `item.draft_preview_path`.

Regression test:

```text
apps/api/tests/test_routes.py::test_ops_dashboard_surfaces_failure_case_workflow_review_queue_without_persistence
```

The test verifies:

```text
old clickable draft-preview anchor absent
POST /failure-cases/draft-preview present
draft preview requires an explicit POST request present
```

## Boundary

This is dashboard method-boundary hardening only.

It is not automatic failure-case creation.

It is not background automation.

It is not root-cause automation.

It is not complete workflow failure causality.

It is not a schema change.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
