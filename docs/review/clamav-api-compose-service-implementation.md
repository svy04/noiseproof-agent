# ClamAV API Compose Service Implementation

Status: implemented.

Phase marker: ClamAV API compose service implementation v0.

## Purpose

This gate adds the minimal profiled FastAPI Compose service needed for a future API-to-clamd runtime smoke.

It follows `docs/review/clamav-api-compose-service-review.md`.

Implementation summary: profiled api Compose service.

It does not switch the scanner default.

It does not run the API container against ClamAV yet.

## Implemented

```text
apps/api/Dockerfile
docker-compose.yml api service
api profile
DATABASE_URL points at db service hostname
CLAMD_HOST=clamav
CLAMD_PORT=3310
NOISEPROOF_SCANNER=unavailable remains the default
API_PORT=8000 example
```

The Dockerfile:

```text
uses python:3.13-slim
sets PYTHONPATH=/app
installs uv
uses uv sync --frozen --no-dev
runs uvicorn app.main:create_app --factory on 0.0.0.0:8000
```

## Boundary

This is Dockerfile and Compose service configuration only.

This is not default scanner switch.

This is not endpoint runtime proof with real ClamAV.

This is not API scan endpoint proof.

This is not production malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Verification Target

The next gate should run:

```text
docker compose --profile api --profile scanner config
```

That is config-only verification. A later runtime smoke must start the API container before claiming service runtime behavior.

## Next Product Gate

```text
ClamAV API compose service config verification v0
```
