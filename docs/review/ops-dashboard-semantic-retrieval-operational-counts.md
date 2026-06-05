# Ops Dashboard Semantic Retrieval Operational Counts

Status: implemented.

Phase marker: ops dashboard semantic retrieval operational counts v0.

## Purpose

Surface the `/ops/summary` semantic retrieval operational counts in the human-readable `/ops/dashboard`.

Phase 614 added the counts to the API response. This phase makes those counts visible in the dashboard summary grid so a reviewer can inspect semantic retrieval activity without reading JSON first.

## Added Dashboard Metrics

```text
Retrieval Runs Recorded
Semantic Retrieval Runs
Chunk Embedding Rows
Caller-provided Embeddings
```

## Boundary Text

The dashboard boundary list now includes:

```text
Semantic retrieval and caller-provided embedding metrics are operational counts, not semantic retrieval quality evidence.
```

## Changed Surface

```text
GET /ops/dashboard
apps/api/app/services/ops_dashboard.py
```

## Route-level Verification

```text
tests/test_routes.py::test_ops_dashboard_surfaces_semantic_retrieval_operational_counts
```

The test creates one semantic retrieval run over two caller-provided embedding rows, then verifies that the dashboard renders the four labels and the quality boundary.

## Boundary

This is dashboard inspectability only.

This is not a new retrieval algorithm.

This is not embedding generation.

This is not live OpenAI provider evidence.

This is not semantic retrieval quality evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not distributed tracing.

This is not free-form final report generation.

This is not product-complete.

## Next Gate

```text
local Docker/FastAPI runtime smoke for dashboard semantic retrieval operational counts if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
