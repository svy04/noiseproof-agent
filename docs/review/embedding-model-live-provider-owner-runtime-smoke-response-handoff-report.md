# Embedding Model Live-provider Owner-runtime Smoke Response Handoff Report

Status: implemented.

Phase marker: embedding model live-provider owner-runtime smoke response handoff report v0.

## Goal

Convert a future owner-runtime `POST /chunks/embedding-model-preview` response capture into the strict metadata-only report accepted by the owner-runtime smoke validator.

This is a response-to-report handoff only. It does not call OpenAI, does not read `OPENAI_API_KEY`, and does not prove live embedding generation by itself.

## Input Shape

The command expects a response capture JSON outside the repository:

```json
{
  "http_status": 200,
  "response_body": {
    "embedding_status": "owner_runtime_provider_generated",
    "embedding_model": "text-embedding-3-small",
    "embedding": ["<1536 floats>"],
    "metadata_json": {
      "provider_response_dimension_check": "passed",
      "usage": {"total_tokens": 8},
      "secret_exposed": false,
      "persistence_boundary": "preview_only_not_persisted"
    }
  }
}
```

## Command

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness \
  --build-owner-runtime-smoke-report-from-response <owner-runtime-response-json-outside-repo> \
  --output <runtime-report-path-outside-repo>
```

## Output Report

Accepted handoff output is the validator report shape only:

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

Post-run validation:

```bash
uv run python -m app.services.embedding_model_live_provider_harness \
  --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

Expected validator markers:

```text
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
```

## Safety Boundaries

```text
response-to-report handoff only
response capture path must be outside repository
output report path must be outside repository
does not write embedding vectors into the report
does not write metadata_json into the report
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
owner-runtime smoke packet command-template handoff alignment v0, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
