# Uploaded Raw File Guard Ops Summary Runtime Smoke

Status: implemented.

Phase marker: uploaded raw file guard ops summary runtime smoke v0.

## Purpose

Verify that the uploaded raw file guard counts added to `GET /ops/summary` and
`GET /ops/dashboard` reflect real local HTTP activity against PostgreSQL, not
only in-memory tests.

This runtime smoke used local Docker PostgreSQL plus a live FastAPI process from
the current working tree.

## Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
DATABASE_URL=postgresql://noiseproof:noiseproof@127.0.0.1:55432/noiseproof
FastAPI URL=http://127.0.0.1:8056
```

Migration status before the HTTP smoke:

```text
Applied migrations: 21
Pending migrations: 0
Applied migrations: 21
Pending migrations: 0
```

The first pair is the apply run. The second pair is the status run.

## HTTP Path

The smoke exercised:

```text
GET /health
GET /ops/summary
POST /documents/upload-raw-files
GET /documents/upload-raw-files/{raw_file_id}/download
POST /documents/upload-raw-files/{raw_file_id}/scan-results
POST /documents/upload-raw-files/{raw_file_id}/download-approvals
GET /documents/upload-raw-files/{raw_file_id}/download
GET /ops/summary
GET /ops/dashboard
```

## Observed Result

```json
{
  "health": "ok",
  "raw_file_id": "b1f4cc37-576a-4da1-9bf1-05220dad4939",
  "upload_status_code": 201,
  "missing_scan_download_status_code": 409,
  "failed_scan_status": "failed",
  "failed_scan_verdict": "scan_error",
  "clean_scan_status": "completed",
  "clean_scan_verdict": "clean",
  "approval_status": "approved",
  "allowed_download_status_code": 200,
  "downloaded_byte_count": 25,
  "deltas": {
    "uploaded_raw_file_count": 1,
    "raw_file_scan_result_count": 2,
    "raw_file_clean_scan_count": 1,
    "raw_file_scan_error_count": 1,
    "raw_file_download_approval_count": 1,
    "active_download_approval_count": 1,
    "raw_file_download_event_count": 2,
    "blocked_download_event_count": 1,
    "allowed_download_event_count": 1
  },
  "summary_note_present": true,
  "dashboard_contains": {
    "UploadedRawFiles": true,
    "RawFileScanResults": true,
    "RawFileCleanScans": true,
    "RawFileScanErrors": true,
    "DownloadApprovals": true,
    "ActiveDownloadApprovals": true,
    "RawFileDownloadEvents": true,
    "BlockedDownloads": true,
    "AllowedDownloads": true
  }
}
```

The existing local database already contained earlier raw-file guard rows, so
the smoke records deltas instead of presenting absolute totals as a fresh
dataset.

## Boundary

This is local Docker PostgreSQL plus live FastAPI HTTP evidence.

It is not production authorization.

It is not authenticated identity.

It is not signed URL support.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
