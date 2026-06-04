# Embedding Model Provider Disabled Path

Status: implemented.

Phase marker:

```text
embedding model provider disabled-path v0
```

## Purpose

Add the first runtime boundary for future actual embedding model generation without making a provider call.

This phase turns the source review contract into a safe endpoint that can show whether the OpenAI provider is configured.

## Endpoint

```text
POST /chunks/embedding-model-preview
```

Default request:

```json
{
  "text": "Enterprise demand growth reached 12% in Q1."
}
```

Response states:

```text
disabled_missing_api_key
configured_no_call
```

## Implemented Behavior

When `OPENAI_API_KEY` is absent or blank:

```text
configured: false
embedding_status: disabled_missing_api_key
metadata_json.network_boundary: no_network_call
metadata_json.cost_boundary: no_cost_incurred
metadata_json.persistence_boundary: preview_only_not_persisted
```

When `OPENAI_API_KEY` is configured:

```text
configured: true
embedding_status: configured_no_call
metadata_json.network_boundary: no_network_call
metadata_json.cost_boundary: no_cost_incurred
metadata_json.secret_exposed: false
```

The endpoint uses the selected future default from `docs/review/embedding-provider-source-review.md`:

```text
provider: openai
embedding_model: text-embedding-3-small
embedding_dimension: 1536
encoding_format: float
```

## Boundary

No embedding vector is generated.
no embedding vector is generated.

There is no provider call.
no provider call.

There is no network call.
There is no cost-incurring runtime path.
There is no persistence.
There is no semantic retrieval quality evidence.
There is no secret exposure.

Actual embedding model generation remains unproven.
actual embedding model generation remains unproven.

## Verification

Focused tests:

```bash
cd apps/api
uv run pytest -q tests/test_routes.py -k "embedding_model_preview"
uv run pytest -q tests/test_docs.py -k "embedding_model_provider_disabled_path"
```

Expected route behaviors:

```text
POST /chunks/embedding-model-preview without OPENAI_API_KEY -> configured false
POST /chunks/embedding-model-preview with fake OPENAI_API_KEY -> configured true, no provider call, secret not exposed
```
