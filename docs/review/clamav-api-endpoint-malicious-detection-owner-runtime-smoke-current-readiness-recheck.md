# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Current-readiness Recheck

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke current-readiness recheck v0

## Goal

Record the current Docker/API/clamd readiness state before the owner-provided runtime smoke without creating, storing, printing, or supplying a test signature payload.

This is a current-state recheck only. It keeps the next product gate honest by separating runtime readiness from malicious-detection proof.

## Observed Environment

Observed locally on 2026-06-03:

```text
docker_client_version: 29.4.3
docker_server_version: 29.4.3
docker_compose_version: v5.1.3
api_container_status: up
clamav_container_status: up_healthy
db_container_status: up_healthy
api_scanner: clamd
clamd_host: clamav
clamd_port: 3310
api_health_status: ok
clamd_ping: PONG
```

## Current Gate Status

```text
owner_runtime_signature_input_present: false
api_scan_request_attempted: false
malicious_detection_verified: false
payload_committed_to_repo: false
raw_payload_logged: false
does not include a test signature payload
```

## Commands Run

```powershell
docker --version
docker compose version
docker info --format '{{json .ServerVersion}}'
docker compose --profile api --profile scanner ps
docker compose --profile api --profile scanner exec -T api printenv NOISEPROOF_SCANNER CLAMD_HOST CLAMD_PORT
Invoke-RestMethod -Uri 'http://localhost:8000/health' -Method Get
docker compose --profile api --profile scanner exec -T clamav clamdscan --ping=1
```

## Boundary

```text
not endpoint malicious-detection runtime proof
not EICAR-through-API proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not customer validation
not Braincrew acceptance
not product-complete
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0.

That gate still requires an owner-provided runtime-only signature input outside the repository and a report output path outside the repository.
