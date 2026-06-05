# Embedding Model Live-provider Owner-runtime Smoke Report Contract

Status: implemented.

Phase marker: embedding model live-provider owner-runtime smoke report contract v0.

## Goal

Expose the no-secret JSON metadata contract that a future owner-provided OpenAI embedding runtime smoke report must satisfy before the validator can accept it.

This is a contract artifact only. It does not read, store, print, or use `OPENAI_API_KEY`.

## Command

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness \
  --print-owner-runtime-smoke-report-contract
```

## Contract Markers

```text
contract_status: ready_for_owner_runtime_report
accepted_report
required_top_level_fields
forbidden_secret_fields
accepted_validator_output
rejected_validator_output
```

Accepted report markers:

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

Forbidden secret fields:

```text
api_key
authorization
openai_api_key
provider_secret
secret
token
```

Accepted validator output:

```text
validation_status: accepted
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
```

Rejected validator output:

```text
validation_status: rejected
accepted_owner_runtime_smoke: false
missing_or_failed_checks: non-empty
```

## Boundary

```text
contract only
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
