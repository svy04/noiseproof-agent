# Retrieval Run Semantic Provenance Inspectability

Status: implemented.

Phase marker: retrieval run semantic provenance inspectability v0.

## Purpose

Make persisted semantic retrieval runs easier to inspect without opening nested `metadata_json` first.

Earlier phases exposed semantic retrieval operational counts in `/ops/summary` and `/ops/dashboard`. This phase exposes the per-run provenance that was already stored in `retrieval_runs.metadata_json` through the existing read surfaces.

## Added Read Fields

`GET /retrieval-runs` now includes these derived read-only fields:

```text
is_semantic_retrieval_run
retrieval_mode
query_vector_source
persistence_boundary
```

For caller-provided vector semantic retrieval runs, these values make `metadata_json.retrieval_mode`, `metadata_json.query_vector_source`, and `metadata_json.persistence_boundary` visible without changing the persisted schema.

## Dashboard Surface

`GET /ops/dashboard` now renders the Retrieval Runs table with these columns:

```text
Semantic
Retrieval Mode
Query Vector Source
Persistence Boundary
```

## Changed Surface

```text
GET /retrieval-runs
GET /ops/dashboard
apps/api/app/routes/retrieval_runs.py
apps/api/app/services/retrieval_run_provenance.py
apps/api/app/services/ops_dashboard.py
apps/api/app/schemas.py
```

## Route-level Verification

```text
tests/test_routes.py::test_semantic_retrieval_run_persists_candidates_without_evidence_ledger
tests/test_routes.py::test_ops_dashboard_surfaces_semantic_retrieval_operational_counts
```

The tests create a caller-provided vector semantic retrieval run and verify that the API list and dashboard table surface the semantic retrieval mode, query vector source, and persistence boundary.

## Boundary

This is read-surface inspectability only.

This is not a new retrieval algorithm.

This is not embedding generation.

This is not live OpenAI provider evidence.

This is not semantic retrieval quality evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not distributed tracing.

This is not Evidence Ledger generation.

This is not free-form final report generation.

This is not product-complete.

## Next Gate

```text
local Docker/FastAPI runtime smoke for retrieval run semantic provenance inspectability if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
