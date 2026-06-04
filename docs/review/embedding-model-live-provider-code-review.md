# Embedding Model Live-provider Code Review

Status: implemented.

Phase marker:

```text
embedding model live-provider code review v0
```

## Purpose

Select the smallest safe code boundary for a future live OpenAI embedding provider path without adding runtime behavior in this phase.

This review follows:

- `docs/review/embedding-provider-source-review.md`
- `docs/review/embedding-model-provider-live-call-review.md`
- `docs/review/embedding-model-mocked-provider-call.md`
- `docs/review/embedding-model-live-provider-implementation-review.md`

## Current Code Facts

Current route:

```text
POST /chunks/embedding-model-preview
```

Current implementation surface:

```text
apps/api/app/routes/chunks.py
apps/api/app/services/embedding_model_preview.py
apps/api/app/settings.py
apps/api/app/schemas.py
```

Current boundary:

```text
get_embedding_provider_client returns None
preview_embedding_model_provider handles disabled and injected mocked-provider paths
allow_provider_call: true + OPENAI_API_KEY + no provider client -> 501
injected mocked provider response -> mocked_provider_generated
dimension mismatch -> 502
```

This is the correct live-provider insertion point. Do not bypass it with route-local network code.

## Official Sources Checked

OpenAI official documentation used for the future provider code contract:

- `https://platform.openai.com/docs/guides/embeddings`
- `https://platform.openai.com/docs/api-reference/embeddings/create`

Selected implementation direction:

```text
Use the OpenAI Python SDK behind a tiny provider adapter.
Future call shape: client.embeddings.create(...)
```

Rationale:

- the endpoint already has a provider client injection boundary
- the SDK keeps auth, request shape, and response parsing close to the official API surface
- a tiny adapter keeps tests mocked and prevents route code from directly handling secrets
- the response can be normalized into the existing mocked-provider response shape

## Required Future Adapter Boundary

The future provider adapter interface must stay tiny and testable.

Future file candidate:

```text
apps/api/app/services/openai_embedding_provider.py
```

Future adapter interface:

```text
create_embedding(
  text: str,
  model: str,
  dimension: int,
  encoding_format: str,
  api_key: str,
  timeout_seconds: float,
) -> dict
```

Future normalized response shape:

```text
{
  "embedding": [...],
  "model": "...",
  "usage": {...},
  "provider_call_boundary": "openai_python_sdk_owner_runtime",
}
```

Required metadata handoff:

```text
metadata_json.provider = openai
metadata_json.provider_model
metadata_json.provider_response_dimension_check
metadata_json.usage
metadata_json.network_boundary = live_provider_call_owner_runtime_only
metadata_json.cost_boundary = live_api_cost_possible_owner_runtime
metadata_json.persistence_boundary = preview_only_not_persisted
metadata_json.secret_exposed = false
```

## Required Error Boundary

The future adapter must expose a structured provider error boundary.

The adapter must convert provider failures into structured service errors or warnings before they reach the route:

```text
timeout -> structured provider timeout boundary
auth failure -> structured provider auth boundary with no key echo
rate limit -> structured provider rate limit boundary
bad response shape -> structured provider response boundary
dimension mismatch -> provider response dimension mismatch
```

The route must still perform the provider response dimension check after adapter normalization.

## Dependency Boundary

dependency addition deferred.

Do not add the `openai` runtime dependency in this phase.

Future dependency gate must update:

```text
apps/api/pyproject.toml
uv.lock
README.md
docs/runbook.md
docs/GOAL.md
```

Future tests must prove:

```text
OpenAI client construction receives OPENAI_API_KEY without logging it
timeout_seconds is passed to the client or request options
client.embeddings.create is called only when allow_provider_call is true
no live provider call in CI
```

## Boundary

This phase adds no runtime behavior.
no runtime behavior.

It adds no OpenAI dependency.
It adds no network call.
It adds no live provider call.
It adds no API cost.
It adds no embedding vector.
It adds no persistence.
It adds no retrieval expansion.
It adds no Evidence Ledger generation.
It adds no semantic retrieval quality evidence.
It adds no hosted deployment evidence.

Actual live embedding model generation remains unproven.
actual live embedding model generation remains unproven.

## Next Gate

The next smallest implementation gate should be:

```text
embedding model live-provider dependency review v0
```

That gate should review the exact `openai` package version, dependency impact, and CI/no-live-call behavior before adding the dependency or provider adapter code.
