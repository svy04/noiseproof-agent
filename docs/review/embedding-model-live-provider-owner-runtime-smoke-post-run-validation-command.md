# Embedding Model Live-provider Owner-runtime Smoke Post-run Validation Command

Phase marker: embedding model live-provider owner-runtime smoke post-run validation command v0.

## Purpose

The owner-runtime smoke packet now points to the metadata-only validator that should be run after a future owner-provided OpenAI embedding smoke writes a runtime report outside the repository.

This phase does not run the live smoke.

## Post-run Command

```bash
uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

## Success Criteria

```text
validation_status: accepted
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
```

## Updated Packet

Updated artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
```

The packet now includes:

```text
post_run_validation_command
post_run_validation_success_criteria
```

## Boundary

```text
packet refresh only
not live embedding generation proof
not hosted deployment evidence
not external reviewer feedback
not semantic retrieval quality evidence
not product-complete
```

Actual live embedding model generation remains unproven until owner-provided runtime input exists, the live smoke runs outside CI, and the generated outside-repo report is accepted by the validator.
