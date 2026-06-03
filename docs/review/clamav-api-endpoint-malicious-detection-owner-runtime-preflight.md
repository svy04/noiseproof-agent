# ClamAV API Endpoint Malicious-detection Owner-runtime Preflight

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner-runtime preflight v0

## Goal

Record the non-payload runtime prerequisites for the future owner-provided malicious/test-signature endpoint smoke, without generating, storing, printing, or uploading a test signature.

## Commands

```bash
docker compose --profile api --profile scanner ps
curl http://localhost:8000/health
docker compose exec -T api printenv NOISEPROOF_SCANNER
docker compose exec -T api printenv CLAMD_HOST
docker compose exec -T api printenv CLAMD_PORT
docker compose exec -T clamav sh -lc "printf 'PING\n' | nc -w 3 127.0.0.1 3310"
```

## Observed Runtime State

```text
API service: Up
DB service: Up (healthy)
ClamAV service healthy
GET /health -> 200
NOISEPROOF_SCANNER=clamd
CLAMD_HOST=clamav
CLAMD_PORT=3310
clamd PING -> PONG
```

The API health response was:

```json
{"status":"ok","service":"noiseproof-agent-api","workflow_version":"phase40-lineage-warning-code-dashboard"}
```

## Payload Boundary

```text
owner-provided test signature absent
no scan endpoint request was made
no raw upload request was made
payload_committed_to_repo: false
raw_payload_logged: false
owner-provided runtime smoke remains pending
```

## Non-claims

This is a runtime preflight only.

It is not:

```text
not malware detection proof
```

It is also not:

- EICAR-through-API proof
- production malware scanning evidence
- hosted deployment evidence
- external reviewer feedback
- customer validation
- product-complete claim

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
