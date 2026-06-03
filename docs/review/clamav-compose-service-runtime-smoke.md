# ClamAV Compose Service Runtime Smoke

Status: implemented.

Phase marker: ClamAV compose service runtime smoke v0.

## Purpose

This gate verifies that the optional Compose-managed ClamAV service can start and respond to a daemon ping.

It does not connect the API endpoint to ClamAV.

It does not scan EICAR through the Compose service.

## Commands

```text
docker compose --profile scanner up -d clamav -> exit 0
docker inspect -f '{{.State.Health.Status}}' noiseproof-agent-clamav -> healthy
docker compose --profile scanner exec -T clamav clamdscan --ping=1 -> PONG
docker compose --profile scanner exec -T clamav clamdscan --version -> ClamAV 1.5.2/28017/Sun May 31 06:27:13 2026
docker inspect noiseproof-agent-clamav --format '{{json .NetworkSettings.Ports}}' -> {"3310/tcp":null,"7357/tcp":null}
```

## Observed Runtime State

```text
container_name: noiseproof-agent-clamav
container_health: healthy
clamd_ping_verified: true
clamd_ping_output: PONG
clamav_version: ClamAV 1.5.2
signature_database_version: 28017
signature_database_date: Sun May 31 06:27:13 2026
signature_database_observed: true
clamav_host_port_bindings: null
real_clamav_runtime_verified: true
api_endpoint_verified_with_real_clamav: false
malware_scanning_evidence: false
```

`docker compose ps` shows container ports such as `3310/tcp` and `7357/tcp`, but `docker inspect` reports null host bindings for both ports. This is not host port publishing.

## Boundary

This is local Docker Compose runtime evidence for the ClamAV service only.

This is not API endpoint integration.

This is not endpoint runtime proof with real ClamAV.

This is not malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
ClamAV compose EICAR runtime smoke v0
```
