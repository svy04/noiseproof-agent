# Embedding Model Live-provider Adapter Disabled-code

Status: implemented.

Phase marker:

```text
embedding model live-provider adapter disabled-code v0
```

## Purpose

Add a tiny OpenAI SDK adapter that can be unit-tested with fake clients while keeping the FastAPI route unwired from live provider calls.

This follows:

- `docs/review/embedding-model-live-provider-code-review.md`
- `docs/review/embedding-model-live-provider-dependency-addition.md`

## Implemented Code

```text
apps/api/app/services/openai_embedding_provider.py
OpenAIEmbeddingProviderClient
EmbeddingProviderError
```

Adapter call shape:

```text
client.embeddings.create(
  input=text,
  model=model,
  dimensions=dimension,
  encoding_format=encoding_format,
)
```

Normalized response fields:

```text
embedding
model
usage
provider_call_boundary = openai_python_sdk_disabled_adapter
timeout_seconds
secret_exposed = false
```

Failure boundaries:

```text
provider_timeout
provider_error
secret redaction
```

## Route Boundary

The route remains unwired.
route remains unwired.

Current default dependency remains:

```text
apps/api/app/services/embedding_model_preview.py
get_embedding_provider_client -> return None
```

Therefore:

```text
POST /chunks/embedding-model-preview
allow_provider_call: true + OPENAI_API_KEY + no provider client -> 501
```

The adapter exists as disabled code only. It is not installed into the route dependency by default.

## Verification

Focused tests:

```bash
cd apps/api
uv run pytest -q tests/test_openai_embedding_provider.py
uv run pytest -q tests/test_routes.py -k "embedding_model_preview"
uv run pytest -q tests/test_docs.py -k "embedding_model_live_provider_adapter_disabled_code"
```

The adapter tests use fake SDK clients only.

## Boundary

This phase adds adapter code but no route wiring.
It adds no default live provider call.
It adds no live provider call in CI.
no live provider call in CI.

It adds no API cost.
It adds no automatic persistence.
It adds no retrieval expansion.
It adds no Evidence Ledger generation.
It adds no semantic retrieval quality evidence.
It adds no hosted deployment evidence.

Actual live embedding model generation remains unproven.
actual live embedding model generation remains unproven.

## Next Gate

The next smallest implementation gate should be:

```text
embedding model live-provider route wiring review v0
```

That gate should decide how to opt in to the adapter without allowing accidental live provider calls in CI or default local runs.
