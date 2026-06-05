# Embedding Model Live-provider Owner-runtime Smoke Report Schema

Status: implemented.

Phase marker: embedding model live-provider owner-runtime smoke report schema v0.

## Goal

Expose a strict JSON Schema for the secret-free metadata report that a future owner-runtime OpenAI embedding smoke should write outside the repository.

This is a schema artifact only. It does not read, store, print, or use `OPENAI_API_KEY`.

## Command

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness \
  --print-owner-runtime-smoke-report-schema
```

## Schema Markers

```text
schema_status: ready_for_owner_runtime_report
$schema: https://json-schema.org/draft/2020-12/schema
title: NoiseProof embedding owner runtime smoke report
type: object
additionalProperties: false
required
properties
```

Required fields:

```text
api_calls_attempted
embedding_length
embedding_model
embedding_status
http_status
openai_api_key_printed
persistence_boundary
provider_response_dimension_check
route
secret_committed_to_repo
secret_exposed
secret_logged
usage_metadata_present
```

Accepted constants include:

```text
route: POST /chunks/embedding-model-preview
http_status: 200
embedding_status: owner_runtime_provider_generated
embedding_model: text-embedding-3-small
embedding_length: 1536
provider_response_dimension_check: passed
usage_metadata_present: true
secret_exposed: false
persistence_boundary: preview_only_not_persisted
api_calls_attempted: true
openai_api_key_printed: false
secret_logged: false
secret_committed_to_repo: false
```

## Boundary

```text
schema only
does not read OPENAI_API_KEY
does not print OPENAI_API_KEY
does not call the OpenAI provider
does not persist embeddings
not live embedding generation proof
not semantic retrieval quality evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Next Gate

```text
owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
