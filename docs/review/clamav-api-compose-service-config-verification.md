# ClamAV API Compose Service Config Verification

Status: implemented.

Phase marker: ClamAV API compose service config verification v0.

## Purpose

This gate records config-only evidence for the profiled `api` Compose service.

It verifies that Docker Compose can render the API, database, and ClamAV service shape together. It does not start the API container.

## Command

```text
docker compose --profile api --profile scanner config -> exit 0
```

## Observed Rendered Shape

```text
service: api
profiles: api
dockerfile: apps/api/Dockerfile
DATABASE_URL: postgresql://noiseproof:noiseproof@db:5432/noiseproof
CLAMD_HOST: clamav
CLAMD_PORT: "3310"
NOISEPROOF_SCANNER: unavailable
API published port: 8000
api_runtime_started: false
```

ClamAV boundary:

```text
service: clamav
profiles: scanner
expose: 3310
clamav host port published: false
```

Observed boundary flags:

```text
api_runtime_started: false
api_endpoint_verified_with_real_clamav: false
malware_scanning_evidence: false
hosted_deployment_evidence: false
```

## Boundary

This is config-only verification.

This is not API runtime smoke.

This is not endpoint runtime proof with real ClamAV.

This is not production malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
ClamAV API compose service runtime smoke v0
```
