# Uploaded Raw File Scan Execution Endpoint Runtime Smoke

Status: verified locally.

Phase marker: uploaded raw file scan execution endpoint runtime smoke v0.

## Purpose

This gate verifies the explicit raw upload scan execution endpoint against local Docker PostgreSQL and live FastAPI HTTP.

It verifies endpoint wiring, persistence, metadata-only response behavior, and default scanner-unavailable handling.

It does not verify real ClamAV execution.

It does not verify malware scanning.

## Runtime Environment

Docker:

```text
Docker Desktop 4.74.0
Docker Engine 29.4.3
Docker Compose v5.1.3
```

Database:

```text
container: noiseproof-agent-db
image: pgvector/pgvector:pg16
status: healthy
port: 127.0.0.1:55432 -> 5432
```

Migration status:

```text
Applied migrations: 16
Pending migrations: 0
```

API:

```text
uv run uvicorn app.main:create_app --factory --host 127.0.0.1 --port 8010
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
NOISEPROOF_SCANNER=unavailable
RAW_FILE_SCANNER_TIMEOUT_SECONDS=5
```

## Smoke Flow

Commands exercised:

```text
GET /health
POST /documents/upload-raw-files
POST /documents/upload-raw-files/{raw_file_id}/scan
GET /documents/upload-raw-files/{raw_file_id}/scan-results
```

Observed summary:

```json
{
  "phase_marker": "uploaded raw file scan execution endpoint runtime smoke v0",
  "health_status": "ok",
  "upload_status": "created",
  "raw_file_id": "63fcd75d-a026-4ce9-874f-3b7876864125",
  "scan_status": "failed",
  "scan_verdict": "scan_error",
  "scanner_name": "scanner-unavailable",
  "failure_reason": "scanner_not_configured",
  "temporary_scan_path_present": true,
  "raw_bytes_key_leaked": false,
  "temporary_scan_path_key_leaked": false,
  "download_url_key_leaked": false,
  "listed_scan_result_count": 1,
  "real_clamav_runtime_verified": false,
  "malware_scanning_evidence": false
}
```

## Confirmed

```text
live FastAPI /health returned ok
raw upload persisted to local Docker PostgreSQL
explicit scan endpoint returned 201
default scanner-unavailable result persisted as failed / scan_error
scan result list returned the persisted scan result
response did not expose raw_bytes key
response did not expose temporary_scan_path key
response did not expose download_url key
```

## Not Confirmed

```text
real ClamAV binary execution
ClamAV signature database presence
malware scanning behavior
infected file detection
clean verdict from a real scanner
hosted deployment behavior
external reviewer feedback
```

## Boundary

This is local runtime evidence for endpoint wiring and persistence.

This is not real ClamAV execution evidence.

This is not ClamAV installation evidence.

This is not ClamAV signature database evidence.

This is not malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Evidence Gate

```text
external reviewer scan execution endpoint request refresh v0
```
