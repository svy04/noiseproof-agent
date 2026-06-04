# Uploaded Raw File Download Audit Runtime Smoke

Status: local Docker FastAPI plus PostgreSQL runtime proof.

Phase marker: uploaded raw file download audit runtime smoke v0.

## Purpose

This smoke verifies that the `raw_file_download_events` audit path works through the live FastAPI container and Docker PostgreSQL, not only through unit tests.

## Runtime Setup

```powershell
docker compose --profile api up -d --build api
```

The API container was rebuilt after adding `raw_file_download_events`.

Migration runner had already applied `020_raw_file_download_events.sql` and then reported:

```text
Applied migrations: 19
Pending migrations: 0
```

## Smoke Flow

The smoke used CSV bytes:

```text
ticker,revenue
ALPHA,120
```

Observed health:

```text
GET /health -> 200
```

Missing scan path:

```text
POST /documents/upload-raw-files -> 201
GET /documents/upload-raw-files/{raw_file_id}/download -> 409
GET /documents/upload-raw-files/{raw_file_id}/download-events -> 200
missing_download -> 409
missing_blocked_reason -> missing_clean_scan
```

Rate-limited path:

```text
POST /documents/upload-raw-files -> 201
GET /documents/upload-raw-files/{raw_file_id}/download repeated six times
rate_statuses -> [409, 409, 409, 409, 409, 429]
GET /documents/upload-raw-files/{raw_file_id}/download-events -> 200
rate_blocked_reason -> rate_limited
```

Allowed path:

```text
POST /documents/upload-raw-files -> 201
POST /documents/upload-raw-files/{raw_file_id}/scan-results -> 201
GET /documents/upload-raw-files/{raw_file_id}/download -> 200
GET /documents/upload-raw-files/{raw_file_id}/download-events -> 200
allowed_download -> 200
allowed_latest_scan_matches -> true
allowed_filename -> audit-allowed.csv
```

Summary:

```json
{
  "allowed_filename": "audit-allowed.csv",
  "allowed_latest_scan_matches": true,
  "allowed_result": "allowed",
  "missing_blocked_reason": "missing_clean_scan",
  "rate_blocked_reason": "rate_limited",
  "rate_statuses": [409, 409, 409, 409, 409, 429]
}
```

## What This Proves

The live API can write and read `raw_file_download_events` for:

```text
blocked / missing_clean_scan / 409
blocked / rate_limited / 429
allowed / latest clean scan result linked / 200
```

The allowed event preserved:

```text
latest_scan_result_id matched the scan-result id
metadata_json.content_disposition_filename = audit-allowed.csv
```

## Boundary

This is local Docker runtime evidence only.

This is not production authorization.

This is not user identity.

This is not hosted deployment evidence.

This is not malware detection proof.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, RBAC, ABAC, tenant isolation, sessions, JWT verification, OAuth, signed URL, cloud IAM integration, robust file serving, robust file-type detection, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
external reviewer download-audit request refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
