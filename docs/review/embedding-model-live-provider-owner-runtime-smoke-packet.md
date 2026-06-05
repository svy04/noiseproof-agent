# Embedding Model Live-provider Owner-runtime Smoke Packet

Status: implemented.

Phase marker:

```text
embedding model live-provider owner-runtime smoke packet v0
```

## Purpose

Generate a no-secret, no-call owner-runtime smoke packet for the future manual OpenAI embedding provider smoke.

This packet follows:

- `docs/review/embedding-model-live-provider-implementation-review.md`
- `docs/review/embedding-model-live-provider-route-wiring-opt-in-disabled.md`

## Command

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness --print-owner-runtime-smoke-packet
```

## Observed Packet

```text
phase_marker: embedding model live-provider owner-runtime smoke packet v0
packet_status: ready_for_owner_input
required_input: owner-provided OPENAI_API_KEY via environment outside the repository
api_calls_attempted: false
openai_api_key_printed: false
secret_committed_to_repo: false
secret_logged: false
route: POST /chunks/embedding-model-preview
```

OPENAI_API_KEY is owner-provided and must not be printed.

Required runtime environment:

```text
NOISEPROOF_ENABLE_OPENAI_PROVIDER=true
OPENAI_API_KEY configured outside the repository
CI=false
```

Success criteria for the later manual smoke:

```text
http_status: 200
embedding_status: owner_runtime_provider_generated
embedding_length: 1536
provider_response_dimension_check: passed
usage_metadata_present: true
secret_exposed: false
persistence_boundary: preview_only_not_persisted
```

Post-run validation command for a future outside-repo runtime report:

```bash
uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

Post-run validation cross-shell commands:

```text
post_run_validation_commands
posix: uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
powershell: uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report '<runtime-report-path-outside-repo>'
```

Post-run validation success criteria:

```text
validation_status: accepted
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
```

Failure states:

```text
missing_openai_api_key
opt_in_disabled
ci_runtime
provider_timeout
provider_error
dimension_mismatch
```

## Boundary

This phase emits the smoke packet only.

It does not make a live OpenAI provider call.
It does not print `OPENAI_API_KEY`.
It does not persist embeddings.
It does not expand retrieval.
It does not generate an Evidence Ledger.
It does not prove semantic retrieval quality.
It does not provide hosted deployment evidence.
It does not provide external reviewer feedback.

live embedding generation proof remains pending.
external reviewer feedback remains pending.

## Current Environment Observation

At implementation time, local secret discovery reported:

```text
OPENAI_API_KEY_PRESENT=false
NOISEPROOF_ENABLE_OPENAI_PROVIDER_PRESENT=false
```

Therefore no live OpenAI provider smoke was attempted.

## Next Gate

The next smallest implementation gate should be selected from `docs/GOAL.md`.

Possible next gates:

```text
owner-runtime manual live embedding smoke v0, only when OPENAI_API_KEY is configured by the owner
external reviewer feedback v0 if qualifying outside feedback exists
another source-first product gate selected from this file
```
