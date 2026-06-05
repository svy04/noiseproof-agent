# Ops Dashboard GET-only Link Method Boundary

Status: implemented.

Phase marker: ops dashboard GET-only link method boundary v0.

## Purpose

Make the `GET /ops/dashboard` HTML explicit about how reviewers should interpret links and method cues.

Dashboard links are GET-only inspection routes.

POST-only actions render as method cues, not anchors.

## Implemented Cue

The dashboard boundary section now includes:

```text
Dashboard links are GET-only inspection routes.
POST-only actions render as method cues, not anchors.
```

The workflow review queue keeps the POST-only draft preview route visible as text:

```text
POST /failure-cases/draft-preview
draft preview requires an explicit POST request
```

The dashboard must not render the draft-preview POST route as a clickable href.

## Code Boundary

Changed code:

```text
apps/api/app/services/ops_dashboard.py
```

Regression test:

```text
apps/api/tests/test_routes.py::test_ops_dashboard_declares_get_only_link_method_boundary
```

The route test verifies:

```text
GET /ops/dashboard -> 200
Dashboard links are GET-only inspection routes.
POST-only actions render as method cues, not anchors.
workflow detail link remains clickable
POST /failure-cases/draft-preview remains visible as a method cue
draft-preview POST route is not exposed as a clickable href
```

## Boundary

This is not a route behavior change.

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
