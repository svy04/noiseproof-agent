# Embedding Provider Source Review

Status: implemented.

Phase marker:

```text
embedding provider source review v0
```

## Purpose

Select the smallest source-first contract for future actual embedding model generation before adding any cost-incurring runtime path.

This review exists because NoiseProof currently has:

- caller-provided vector persistence
- deterministic local hash embedding preview
- caller-provided semantic retrieval preview/persistence

It does not yet have actual embedding model generation.

## Primary Sources Checked

OpenAI Embeddings guide:

```text
https://platform.openai.com/docs/guides/embeddings
```

OpenAI Create embeddings API reference:

```text
https://platform.openai.com/docs/api-reference/embeddings/create
```

Source facts used for this contract:

- the create embeddings API accepts `input`
- the create embeddings API requires `model`
- the create embeddings API supports `dimensions` on supported models
- `encoding_format: float` returns numeric vectors suitable for existing vector storage paths
- `text-embedding-3-small` is the initial cost/latency default candidate
- `text-embedding-3-small` default output dimension is 1536
- `text-embedding-3-large` is the higher-capability candidate
- `text-embedding-3-large` default output dimension is 3072

## Selected Future Contract

Future endpoint candidate:

```text
POST /chunks/embedding-model-preview
```

Future request fields:

```text
text
embedding_model
embedding_dimension
encoding_format
provider
```

Default future values:

```text
provider: openai
embedding_model: text-embedding-3-small
embedding_dimension: 1536
encoding_format: float
```

Required configuration:

```text
OPENAI_API_KEY
```

Required response boundary fields:

```text
embedding_model
embedding_dimension
embedding_text_hash
distance_metric
embedding_status
embedding
metadata_json.provider
metadata_json.provider_model
metadata_json.provider_dimension
metadata_json.cost_boundary
metadata_json.persistence_boundary
warnings
```

## Implementation Boundary

This phase is not implemented as a runtime provider.

It adds no API call.
It adds no cost-incurring runtime path.
It adds no dependency.
It adds no `OPENAI_API_KEY` requirement to normal local tests.
It adds no embedding persistence change.
It adds no semantic retrieval quality evidence.

Actual embedding model generation remains unproven.
actual embedding model generation remains unproven.

## Next Gate

If this direction remains selected, the next small gate should be:

```text
embedding model provider disabled-path v0
```

That gate should add only a safe readiness/disabled response before any live OpenAI call:

- no API key -> `configured: false`
- no network call
- no persistence
- no semantic quality claim
- no hidden cost

Only after that should a live provider call be added behind explicit environment configuration.
