# Embedding Model Live-provider Owner-runtime Smoke Report Contract Alignment

Status: implemented.

Phase marker: embedding model live-provider owner-runtime smoke report contract alignment v0.

## Goal

Check that the owner-runtime smoke report contract, JSON Schema artifact, and authoritative Python validator still describe the same secret-free metadata shape.

This is an alignment check only. It does not read, store, print, or use `OPENAI_API_KEY`.

## Command

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness \
  --check-owner-runtime-smoke-report-contract-alignment
```

## Alignment Markers

```text
alignment_status: aligned
missing_or_failed_checks: []
contract_fields_match_validator_expected_fields
schema_required_fields_match_contract
schema_properties_match_contract_constants
schema_additional_properties_closed
accepted_report_passes_validator
accepted_report_contains_no_forbidden_secret_fields
forbidden_secret_fields_match_validator
```

Expected counts:

```text
accepted_report_field_count: 13
schema_required_field_count: 13
validator_expected_field_count: 13
```

## Boundary

```text
schema/contract/validator alignment only
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
