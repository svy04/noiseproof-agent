# Embedding Model Live-provider Error Boundary

Status: implemented.

Phase marker:

```text
embedding model live-provider error boundary v0
```

## Purpose

Make the owner-runtime OpenAI embedding provider path fail inspectably when the provider adapter raises a handled provider error.

Before this gate, an `EmbeddingProviderError` raised from the injected provider boundary could escape the route as an unstructured server exception. The route now maps that condition to an HTTP 502 response with metadata-only error detail.

## Implemented Boundary

`POST /chunks/embedding-model-preview` catches `EmbeddingProviderError` only inside the explicit provider-call branch:

```text
allow_provider_call=true
OPENAI_API_KEY configured
provider_client present
provider_client raises EmbeddingProviderError
```

The response boundary is:

```text
status_code: 502
error_type: provider_timeout or provider_error
provider_call_boundary: owner_runtime_provider_error
secret_exposed: false
```

The route redacts `OPENAI_API_KEY` from the provider error message before returning the response.

## Files

```text
apps/api/app/services/embedding_model_preview.py
apps/api/tests/test_routes.py
```

## Verification

Route test:

```text
test_embedding_model_preview_maps_provider_errors_without_secret_leak
```

Observed behavior:

```text
fake provider raises EmbeddingProviderError("provider_timeout", ...)
POST /chunks/embedding-model-preview -> 502
provider_call_boundary -> owner_runtime_provider_error
secret_exposed -> false
no secret leak
```

This is provider error metadata only.
provider error metadata only.

## Boundary

This is not live embedding generation proof.
It is not semantic retrieval quality evidence.
It is not a live OpenAI provider call in CI.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not product-complete.

Actual live embedding model generation remains unproven until an owner-runtime smoke with `OPENAI_API_KEY`, `NOISEPROOF_ENABLE_OPENAI_PROVIDER=true`, `allow_provider_call=true`, and the existing no-secret report validator succeeds.

## Next Gate

Owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from `docs/GOAL.md`.
