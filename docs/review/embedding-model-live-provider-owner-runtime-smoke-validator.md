# Embedding Model Live-provider Owner-runtime Smoke Validator

Phase marker: embedding model live-provider owner-runtime smoke validator v0.

## Purpose

This gate adds a metadata-only validator for a future owner-runtime OpenAI embedding smoke report.

The validator does not call OpenAI, does not read or print `OPENAI_API_KEY`, and does not prove live embedding generation by itself. It only checks whether a future owner-provided report has the expected success metadata and no obvious secret fields.

## Command

```bash
uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

## Accepted Report Shape

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

Accepted validator output:

```text
validation_status: accepted
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
```

## Rejection Rules

The validator rejects:

```text
report paths inside the repository
unexpected top-level fields
openai_api_key
api_key
authorization
token
secret
provider_secret
wrong embedding_status
wrong embedding_length
missing or failed provider_response_dimension_check
secret_exposed: true
openai_api_key_printed: true
secret_logged: true
secret_committed_to_repo: true
```

The report path must remain outside the repository.

## Boundary

```text
metadata validator only
not live embedding generation proof by itself
not hosted deployment evidence
not external reviewer feedback
not semantic retrieval quality evidence
not product-complete
```

Actual live embedding model generation remains unproven until an owner-provided `OPENAI_API_KEY` is configured outside the repository, the opt-in provider path is run outside CI, and a secret-free runtime report is produced and accepted by this validator.
