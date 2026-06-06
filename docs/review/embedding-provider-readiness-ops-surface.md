# Embedding Provider Readiness Ops Surface

Status: implemented.

## Purpose

Make the current OpenAI embedding provider runtime boundary visible from operations surfaces without calling OpenAI, printing secrets, persisting readiness metadata, or claiming live embedding generation proof.

## Implemented surface

```text
GET /ops/summary
GET /ops/dashboard
Embedding Provider Readiness
```

`GET /ops/summary` now attaches `embedding_provider_readiness` with:

```text
provider: openai
configured
provider_enabled
provider_client_available
readiness_status
provider_call_boundary
network_boundary
cost_boundary
persistence_boundary
secret_exposed
blocking_reasons
warnings
```

When `OPENAI_API_KEY` is configured, `NOISEPROOF_ENABLE_OPENAI_PROVIDER=true`, `CI=false`, and the provider timeout is positive, the metadata can report:

```text
readiness_status: ready_for_owner_runtime_opt_in
provider_call_boundary: owner_runtime_opt_in_only
network_boundary: no_network_call
cost_boundary: no_cost_incurred
persistence_boundary: readiness_only_not_persisted
secret_exposed: false
```

`GET /ops/dashboard` renders `Embedding Provider Readiness`, `Embedding Provider Boundary`, and the boundary statement:

```text
No OpenAI provider call is made by ops summary or dashboard rendering.
```

## Tests

```text
apps/api/tests/test_routes.py::test_ops_summary_surfaces_embedding_provider_readiness_without_secret_leak
apps/api/tests/test_routes.py::test_ops_dashboard_surfaces_embedding_provider_readiness_boundary
apps/api/tests/test_docs.py::test_embedding_provider_readiness_ops_surface_is_recorded
```

## Boundary

This is ops readiness metadata only. It is not live embedding generation proof, not a live OpenAI provider call, not semantic retrieval quality evidence, not hosted deployment evidence, not external reviewer feedback, not customer validation, not Braincrew acceptance, and not product-complete.

## Next gate

Owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, external reviewer feedback v0 if qualifying outside feedback exists, remote verification after push if needed, or another source-first product gate selected from the current repository state.
