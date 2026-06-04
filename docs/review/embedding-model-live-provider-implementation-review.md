# Embedding Model Live-provider Implementation Review

Status: implemented.

Phase marker:

```text
embedding model live-provider implementation review v0
```

## Purpose

Define the exact implementation gate for a future live embedding provider call before adding network behavior, cost, secrets, or any claim that live embedding model generation works.

This review follows:

- `docs/review/embedding-provider-source-review.md`
- `docs/review/embedding-model-provider-live-call-review.md`
- `docs/review/embedding-model-mocked-provider-call.md`

## Official Sources Checked

OpenAI official documentation used for the future provider contract:

- `https://platform.openai.com/docs/guides/embeddings`
- `https://platform.openai.com/docs/api-reference/embeddings/create`

Relevant contract points for the future implementation:

- embedding creation uses a model and input text
- the response contains embedding vectors
- the `dimensions` parameter can constrain supported embedding dimensions for compatible models
- `encoding_format` can be requested
- response usage metadata should be recorded without exposing secrets

## Future Runtime Surface

Route:

```text
POST /chunks/embedding-model-preview
```

The endpoint must remain disabled by default for real provider calls.

Required request guard:

```text
allow_provider_call
```

Required environment guard:

```text
OPENAI_API_KEY
```

Required behavior:

```text
allow_provider_call: false -> configured_no_call or disabled_missing_api_key
allow_provider_call: true + OPENAI_API_KEY absent -> disabled_missing_api_key
allow_provider_call: true + OPENAI_API_KEY present + owner runtime mode -> live provider call may be attempted
```

The live path must not run automatically in CI.

## Required Implementation Checks

Before the live provider call can be claimed, implementation must include:

- explicit provider client boundary
- request timeout
- input text hash
- provider response dimension check
- provider response model metadata
- usage metadata
- secret redaction
- structured provider error boundary
- structured timeout boundary
- no automatic persistence
- no retrieval expansion
- no Evidence Ledger generation
- no final report generation

Required response metadata fields for the future live path:

```text
metadata_json.provider
metadata_json.provider_model
metadata_json.provider_response_dimension_check
metadata_json.usage
metadata_json.network_boundary
metadata_json.cost_boundary
metadata_json.persistence_boundary
metadata_json.secret_exposed
```

Required successful live state:

```text
embedding_status: live_provider_generated
metadata_json.network_boundary: live_provider_call_owner_runtime_only
metadata_json.persistence_boundary: preview_only_not_persisted
metadata_json.secret_exposed: false
```

## Required Verification Order

Keep this order:

```text
mocked client tests
provider error tests
provider timeout tests
dimension mismatch tests
secret redaction tests
no live provider call in CI
manual owner runtime smoke
```

The manual owner runtime smoke must record:

- exact command
- local service URL
- model
- configured dimension
- returned vector length
- provider response dimension check result
- usage metadata presence
- proof that `OPENAI_API_KEY` is not printed
- proof that no row is persisted automatically
- explicit statement that this is local owner-runtime evidence only

## Boundary

This phase is not implemented as runtime provider behavior.

It adds no live OpenAI provider call.
It adds no OpenAI dependency.
It adds no network call.
It adds no API cost.
It adds no embedding vector.
It adds no automatic persistence.
It adds no retrieval expansion.
It adds no Evidence Ledger generation.
It adds no Critic / Noise Gate behavior.
It adds no final report behavior.
It adds no hosted deployment evidence.

Actual live embedding model generation remains unproven.
actual live embedding model generation remains unproven.

## Next Gate

The next smallest implementation gate should be one of:

```text
embedding model live-provider code review v0
embedding model live-provider owner-runtime smoke packet v0
external reviewer feedback v0 if qualifying outside feedback exists
```

Do not claim live provider generation until a manual owner runtime smoke records a real provider response without leaking secrets.
