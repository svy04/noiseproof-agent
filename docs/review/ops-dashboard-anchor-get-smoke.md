# Ops Dashboard Anchor GET Smoke

Status: implemented.

Phase marker: ops dashboard anchor GET smoke v0.

## Purpose

Verify that clickable `GET /ops/dashboard` anchors marked with `data-method="GET"` resolve as GET 200 inspection routes in the local FastAPI test client.

Phase 520 made dashboard link methods machine-readable. Phase 521 checks that the machine-readable links still lead to live inspection surfaces instead of stale or wrong routes.

## Implemented Surface

Regression test:

```text
apps/api/tests/test_routes.py::test_ops_dashboard_get_anchors_resolve_as_inspection_routes
```

The test creates a deterministic workflow preview, links a manual failure case to the workflow parent, renders `GET /ops/dashboard`, extracts every clickable anchor with:

```text
data-method="GET"
```

and then requests each unique href with the FastAPI test client.

Expected result:

```text
each dashboard anchor resolves as a GET 200 inspection route
```

POST-only actions remain non-clickable method cues.

## Boundary

This is local API test-client smoke evidence only.

It is not browser automation evidence.

It is not hosted deployment evidence.

It is not a route behavior change.

It is not background automation.

It is not automatic failure-case creation.

It is not root-cause automation.

It is not complete workflow failure causality.

It is not external reviewer feedback.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
