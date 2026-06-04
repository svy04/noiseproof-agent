# Embedding Model Live-provider Route Wiring Review

Status: implemented.

Phase marker:

```text
embedding model live-provider route wiring review v0
```

## Purpose

Define how the disabled OpenAI embedding provider adapter may be wired into `POST /chunks/embedding-model-preview` without allowing accidental live provider calls.

This follows:

- `docs/review/embedding-model-live-provider-adapter-disabled-code.md`
- `docs/review/embedding-model-live-provider-dependency-addition.md`

## Current State

Current default route dependency:

```text
apps/api/app/services/embedding_model_preview.py
get_embedding_provider_client remains None by default
```

Current behavior:

```text
allow_provider_call: false -> no network call
allow_provider_call: true + OPENAI_API_KEY + no provider client -> 501
```

## Selected Future Wiring Gate

Future route wiring must be owner-runtime opt-in only.
owner-runtime opt-in only.

Required conditions before returning a live provider client:

```text
NOISEPROOF_ENABLE_OPENAI_PROVIDER=true
OPENAI_API_KEY is configured
allow_provider_call=true
CI is not true
```

Required default behavior:

```text
NOISEPROOF_ENABLE_OPENAI_PROVIDER absent -> get_embedding_provider_client returns None
NOISEPROOF_ENABLE_OPENAI_PROVIDER=false -> get_embedding_provider_client returns None
CI=true -> get_embedding_provider_client returns None
```

The future wiring must keep `allow_provider_call` as a per-request guard. An environment variable alone must never trigger a provider call.

## Required Future Tests

Before wiring the adapter, add tests for:

```text
default dependency still returns None
CI=true always returns None
NOISEPROOF_ENABLE_OPENAI_PROVIDER=false returns None
NOISEPROOF_ENABLE_OPENAI_PROVIDER=true without OPENAI_API_KEY returns None
NOISEPROOF_ENABLE_OPENAI_PROVIDER=true with OPENAI_API_KEY returns provider client only outside CI
allow_provider_call=false still avoids provider call even when provider client exists
```

## Boundary

This phase is review only.

It adds no runtime behavior.
no runtime behavior.

It does not wire the adapter into the route.
It does not change `get_embedding_provider_client`.
It adds no live provider call.
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
embedding model live-provider route wiring opt-in-disabled v0
```

That gate may add config fields and dependency wiring tests, but must not make live calls by default or in CI.
