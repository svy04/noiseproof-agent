# Ops Dashboard Anchor Method Metadata

Status: implemented.

Phase marker: ops dashboard anchor method metadata v0.

## Purpose

Make the `GET /ops/dashboard` link-method boundary machine-readable.

Phase 519 made the boundary visible in copy. Phase 520 adds method metadata to each clickable dashboard anchor so future tests and reviewers can distinguish inspection links from POST-only method cues.

## Implemented Surface

Clickable dashboard anchors now render with:

```text
data-method="GET"
```

POST-only actions remain method cues, not anchors.

For example:

```text
POST /failure-cases/draft-preview
draft preview requires an explicit POST request
```

That POST-only action has no clickable dashboard anchor.

## Code Boundary

Changed code:

```text
apps/api/app/services/ops_dashboard.py
```

The `_link(...)` helper now emits machine-readable GET method metadata for every clickable dashboard link.

Regression test:

```text
apps/api/tests/test_routes.py::test_ops_dashboard_marks_clickable_anchors_as_get_method_links
```

The route test verifies:

```text
GET /ops/dashboard -> 200
every clickable anchor includes data-method="GET"
workflow detail links remain clickable
POST-only draft preview is not exposed as a clickable GET link
```

## Boundary

This is dashboard anchor metadata only.

It is not a route behavior change.

It is not automatic failure-case creation.

It is not background automation.

It is not root-cause automation.

It is not complete workflow failure causality.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
