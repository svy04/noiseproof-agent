# Embedding Model Live-provider Owner-runtime Input Discovery CI Check

Phase marker: embedding model live-provider owner-runtime input discovery ci check v0.

## Purpose

This gate keeps the OpenAI embedding provider owner-runtime input discovery guard visible in CI. It checks the missing-key path only and must not attempt a provider call.

## CI Step

```text
Check embedding provider owner runtime input discovery missing state
```

The workflow runs:

```bash
uv run python -m app.services.embedding_model_live_provider_harness --discover-owner-runtime-input
```

Then it checks:

```text
phase_marker: embedding model live-provider owner-runtime input discovery v0
owner_runtime_input_status: missing_openai_api_key
openai_api_key_present: false
openai_api_key_printed: false
opt_in_enabled: false
api_calls_attempted: false
secret_logged: false
secret_committed_to_repo: false
live_embedding_generation_proof: false
```

## Boundary

```text
CI missing-input guard only
not live embedding generation proof
not hosted deployment evidence
not external reviewer feedback
not semantic retrieval quality evidence
not product-complete
```

The CI step does not configure `OPENAI_API_KEY`, does not set `NOISEPROOF_ENABLE_OPENAI_PROVIDER=true`, and does not call the OpenAI provider. Actual live embedding model generation remains unproven.
