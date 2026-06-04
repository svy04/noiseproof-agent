# Uploaded Raw File Download Audit Schema

Status: local v0 schema, repository, and route-level audit event persistence.

Phase marker: uploaded raw file download audit schema v0.

## Purpose

This gate implements the smallest audit boundary selected by `docs/review/uploaded-raw-file-download-authorization-audit-review.md`.

It records guarded raw file download decisions before making any production authorization claim.

## Implemented

```text
db/migrations/020_raw_file_download_events.sql
db/init/001_schema.sql raw_file_download_events
RawFileDownloadEventCreate
RawFileDownloadEventOut
Repository.create_raw_file_download_event
Repository.list_raw_file_download_events
PostgresRepository raw_file_download_events insert/list
GET /documents/upload-raw-files/{raw_file_id}/download-events
download route audit events for 409 missing scan, 429 rate-limited, and 200 allowed download
```

Inspectable API:

```text
GET /documents/upload-raw-files/{raw_file_id}/download-events
```

## Data Model

```text
raw_file_download_events
  id
  raw_file_id
  latest_scan_result_id
  download_result
  blocked_reason
  http_status_code
  authorization_boundary
  rate_limit_boundary
  filename_boundary
  client_host_boundary
  metadata_json
  created_at
```

Decision values:

```text
download_result: allowed | blocked
blocked_reason: missing_clean_scan
blocked_reason: latest_scan_not_clean
blocked_reason: quarantine_status_blocked
blocked_reason: rate_limited
```

Current local boundaries:

```text
authorization_boundary: local_v0_no_auth_not_production
rate_limit_boundary: local_v0_in_memory_fixed_window_not_production
filename_boundary: local_v0_content_disposition_filename_safety_not_production
client_host_boundary: local_request_client_host_not_identity
```

## Route Behavior

The guarded download route records audit events for:

```text
missing latest clean scan -> blocked / missing_clean_scan / 409
latest scan not clean -> blocked / latest_scan_not_clean / 409
rate limit exceeded -> blocked / rate_limited / 429
stored quarantined clean download -> allowed / null / 200
```

The success metadata records the safe `Content-Disposition` filename, not raw bytes.

## Verification

Focused tests:

```powershell
uv run pytest tests/test_routes.py -q -k "download_records"
uv run pytest apps/api/tests/test_docs.py -q -k "download_audit_schema"
```

Local migration runner check against Docker PostgreSQL:

```text
applied 020_raw_file_download_events.sql
Applied migrations: 19
Pending migrations: 0
```

Expected route examples:

```text
GET /documents/upload-raw-files/{raw_file_id}/download -> 409
GET /documents/upload-raw-files/{raw_file_id}/download-events -> 200
download_result: blocked
blocked_reason: missing_clean_scan

GET /documents/upload-raw-files/{raw_file_id}/download -> 429
GET /documents/upload-raw-files/{raw_file_id}/download-events -> 200
download_result: blocked
blocked_reason: rate_limited

GET /documents/upload-raw-files/{raw_file_id}/download -> 200
GET /documents/upload-raw-files/{raw_file_id}/download-events -> 200
download_result: allowed
latest_scan_result_id: present
```

## Boundary

This is local v0 audit persistence.

This is not production authorization.

This is not user identity.

This is not hosted deployment evidence.

This is not RBAC, ABAC, tenant isolation, sessions, JWT verification, OAuth, signed URL, or cloud IAM integration.

This is not malware detection proof.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust file serving, robust file-type detection, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
uploaded raw file download audit runtime smoke v0
```
