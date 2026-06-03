# ClamAV API Compose Service Review

Status: review-only.

Phase marker: ClamAV API compose service review v0.

## Purpose

This gate selects the future Docker Compose shape for running the FastAPI service on the same Compose network as `clamav`.

It follows `docs/review/clamav-api-service-network-boundary-review.md`, which rejected publishing unauthenticated clamd TCP to the host.

## Source-first Anchors

- Docker Compose networking documentation: https://docs.docker.com/compose/how-tos/networking/
- Docker Compose services reference: https://docs.docker.com/reference/compose-file/services/

Interpretation used for this review:

```text
Compose services can reach each other by service name on the default network.
The API service can use CLAMD_HOST=clamav only when it runs inside the Compose network.
The clamd service must remain internal-only and must not publish host ports.
```

## Decision

Decision summary: select a future profiled `api` Compose service before endpoint runtime proof.

The future implementation should:

```text
add an api service to docker-compose.yml behind an explicit profile
API service joins the same Compose network as `clamav`
set CLAMD_HOST=clamav for the profiled API service
set CLAMD_PORT=3310 for the profiled API service
keep NOISEPROOF_SCANNER=unavailable remains the default
require scanner opt-in must be explicit for any clamd endpoint smoke
depend on db and clamav only for startup ordering, not proof of application readiness
do not publish clamd TCP to the host
do not claim endpoint runtime proof until POST /documents/upload-raw-files/{raw_file_id}/scan is exercised through the API container
```

## Non-selected Paths

Do not make the host-local `uvicorn` path the ClamAV service proof path.

Do not publish `3310:3310`.

Do not set `CLAMD_HOST=localhost`.

Do not switch `NOISEPROOF_SCANNER=clamd` or `NOISEPROOF_SCANNER=clamav` globally.

Do not claim endpoint runtime proof from Compose config alone.

## Boundary

This is review-only.

This is not Compose service code.

This is not API endpoint integration.

This is not endpoint runtime proof with real ClamAV.

This is not production malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
ClamAV API compose service implementation v0
```
