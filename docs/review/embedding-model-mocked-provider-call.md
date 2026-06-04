# Embedding Model Mocked-provider Call

Status: implemented.

Phase marker:

```text
embedding model mocked-provider call v0
```

## Purpose

Verify provider response handling for `POST /chunks/embedding-model-preview` through dependency injection before any live provider integration.

## Implemented Behavior

Route:

```text
POST /chunks/embedding-model-preview
```

When the request uses:

```text
allow_provider_call: true
```

and tests inject a mocked provider client, the endpoint can return:

```text
embedding_status: mocked_provider_generated
metadata_json.network_boundary: mocked_provider_call_only
metadata_json.provider_call_boundary: mocked_provider_client
metadata_json.provider_response_dimension_check: passed
metadata_json.persistence_boundary: preview_only_not_persisted
```

The mocked provider path verifies:

- provider response embedding is surfaced
- provider response dimension check passes for matching vector length
- provider response dimension mismatch is rejected
- fake `OPENAI_API_KEY` is not exposed
- provider usage metadata can be carried under `metadata_json.usage`

## Failure Boundary

If the mocked provider returns a vector with the wrong dimension, the endpoint returns:

```text
provider response dimension mismatch
```

## Boundary

There is no live OpenAI provider call.
no live OpenAI provider call.

There is no live provider call in CI.
no live provider call in CI.

There is no network call.
There is no live API cost.
There is no automatic persistence.
There is no retrieval expansion.
There is no Evidence Ledger generation.
There is no semantic retrieval quality evidence.

Actual live embedding model generation remains unproven.
actual live embedding model generation remains unproven.

## Verification

Focused tests:

```bash
cd apps/api
uv run pytest -q tests/test_routes.py -k "embedding_model_preview"
uv run pytest -q tests/test_docs.py -k "embedding_model_mocked_provider_call"
```

Observed test cases:

```text
allow_provider_call true without provider client -> 501
allow_provider_call true with mocked provider client -> mocked_provider_generated
mocked provider dimension mismatch -> 502
```
