# Embedding Model Live-provider Route Wiring Opt-in Disabled

Status: implemented.

Phase marker:

```text
embedding model live-provider route wiring opt-in-disabled v0
```

## Purpose

Wire the disabled OpenAI embedding provider adapter into the FastAPI dependency boundary without enabling live provider calls by default or in CI.

This follows:

- `docs/review/embedding-model-live-provider-route-wiring-review.md`
- `docs/review/embedding-model-live-provider-adapter-disabled-code.md`
- `docs/review/embedding-model-live-provider-dependency-addition.md`

## Implemented Boundary

The route dependency now has an owner-runtime opt-in only path.
owner-runtime opt-in only.

`get_embedding_provider_client` returns an `OpenAIEmbeddingProviderClient` only when all of these are true:

```text
NOISEPROOF_ENABLE_OPENAI_PROVIDER=true
OPENAI_API_KEY configured
CI is not true
OPENAI_PROVIDER_TIMEOUT_SECONDS is positive
```

The request-level guard remains separate:

```text
allow_provider_call=false -> no provider call
allow_provider_call=true -> provider call is still required before generation
```

Required default behavior:

```text
NOISEPROOF_ENABLE_OPENAI_PROVIDER absent -> provider client remains disabled
NOISEPROOF_ENABLE_OPENAI_PROVIDER=false -> provider client remains disabled
OPENAI_API_KEY missing -> provider client remains disabled
CI=true -> provider client remains disabled
CI=true -> provider client remains disabled
allow_provider_call=false -> no provider call
```

## Files

```text
apps/api/app/settings.py
apps/api/app/services/embedding_model_preview.py
apps/api/tests/test_embedding_provider_wiring.py
.env.example
```

## Boundary

This phase adds opt-in dependency wiring only.

It does not make a live OpenAI provider call in CI.
no live provider call in CI.

It does not make a live OpenAI provider call by default.
It does not persist generated vectors.
It does not expand retrieval.
It does not generate an Evidence Ledger.
It does not prove semantic retrieval quality.
It does not provide hosted deployment evidence.

Actual live embedding model generation remains unproven.
actual live embedding model generation remains unproven.

## Verification

Expected local checks:

```text
uv run pytest -q tests/test_embedding_provider_wiring.py
uv run pytest -q tests/test_routes.py -k "embedding_model_preview"
uv run pytest -q tests/test_docs.py -k "embedding_model_live_provider_route_wiring_opt_in_disabled"
uv run python -m compileall app ../../packages/ingestion ../../packages/review
uv run pytest -q
git diff --check
```

## Next Gate

The next smallest implementation gate should be selected from `docs/GOAL.md`.

Possible next gates:

```text
owner-runtime manual live embedding smoke review v0
external reviewer feedback v0 if qualifying outside feedback exists
another source-first product gate selected from this file
```
