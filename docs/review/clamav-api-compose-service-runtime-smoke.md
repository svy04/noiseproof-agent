# ClamAV API Compose Service Runtime Smoke

Status: implemented

Phase marker: ClamAV API compose service runtime smoke v0

## Goal

Verify that the profiled FastAPI Compose service can start inside the Docker Compose stack and answer a basic health request through the host-mapped API port.

This is API runtime smoke evidence only. It is not scan endpoint proof and not endpoint runtime proof with real ClamAV.

## Commands Observed

```text
docker compose --profile api up -d api -> exit 0
```

```text
curl.exe -s -i http://localhost:8000/health -> 200
```

## Observed Runtime Shape

```text
api_container_running: true
GET /health -> 200
api_state=running
NOISEPROOF_SCANNER: unavailable
CLAMD_HOST: clamav
CLAMD_PORT: 3310
api_scan_endpoint_verified_with_real_clamav: false
malware_scanning_evidence: false
```

Observed health body:

```json
{"status":"ok","service":"noiseproof-agent-api","workflow_version":"phase40-lineage-warning-code-dashboard"}
```

## Boundary

This smoke only proves that the profiled API service can run in Docker Compose and answer `GET /health`.

It does not prove:

- scan endpoint behavior
- endpoint runtime proof with real ClamAV
- production malware scanning evidence
- file signature validation
- scanner default switch
- hosted deployment evidence
- external reviewer feedback
- customer validation
- Braincrew acceptance
- product completeness

## Next Gate

ClamAV API endpoint scanner opt-in review v0
