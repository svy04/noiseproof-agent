# Embedding Model Live-provider Owner-runtime Input Discovery

Phase marker: embedding model live-provider owner-runtime input discovery v0.

## Purpose

Before running any owner-runtime OpenAI embedding smoke, this gate makes the required owner input inspectable without printing secrets and without attempting a provider call.

This is a readiness discovery step only. It is not live embedding generation proof.

## Command

Run from `apps/api`:

```bash
uv run python -m app.services.embedding_model_live_provider_harness --discover-owner-runtime-input
```

## Current local observation

Observed in the current local environment:

```text
OPENAI_API_KEY_PRESENT=false
NOISEPROOF_ENABLE_OPENAI_PROVIDER_PRESENT=false
```

Observed discovery result:

```text
phase_marker: embedding model live-provider owner-runtime input discovery v0
owner_runtime_input_status: missing_openai_api_key
openai_api_key_present: false
openai_api_key_printed: false
opt_in_enabled: false
ci_runtime: false
api_calls_attempted: false
secret_logged: false
secret_committed_to_repo: false
next_action: configure OPENAI_API_KEY outside the repository and set NOISEPROOF_ENABLE_OPENAI_PROVIDER=true for owner-runtime smoke only
```

## Discovery states

```text
missing_openai_api_key
opt_in_disabled
blocked_by_ci
ready_for_owner_runtime_smoke
```

## Guardrails

```text
api_calls_attempted: false
openai_api_key_printed: false
secret_logged: false
secret_committed_to_repo: false
```

The command returns booleans only. It must not print, log, commit, or infer the actual API key value.

## Claim Boundary

This artifact is:

```text
owner-runtime input discovery only
not live embedding generation proof
not hosted deployment evidence
not external reviewer feedback
not semantic retrieval quality evidence
not product-complete
```

actual live embedding model generation remains unproven until the owner provides `OPENAI_API_KEY` outside the repository, explicitly sets `NOISEPROOF_ENABLE_OPENAI_PROVIDER=true`, runs outside CI, and records a secret-free runtime smoke result.
