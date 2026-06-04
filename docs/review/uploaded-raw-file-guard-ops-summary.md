# Uploaded Raw File Guard Ops Summary

Status: implemented.

Phase marker: uploaded raw file guard ops summary v0.

## Purpose

Expose raw-file guard activity in the existing operations surface so a reviewer
can inspect whether uploads, scan records, manual approvals, and guarded
download audit events exist without opening each route separately.

This extends:

```text
GET /ops/summary
GET /ops/dashboard
```

It does not add a new endpoint.

## Implemented Counts

`OpsSummaryOut` now includes:

```text
uploaded_raw_file_count
raw_file_scan_result_count
raw_file_clean_scan_count
raw_file_scan_error_count
raw_file_download_approval_count
active_download_approval_count
raw_file_download_event_count
blocked_download_event_count
allowed_download_event_count
```

The dashboard surfaces the same guard counts as compact metrics:

```text
Uploaded Raw Files
Raw File Scan Results
Raw File Clean Scans
Raw File Scan Errors
Download Approvals
Active Download Approvals
Raw File Download Events
Blocked Downloads
Allowed Downloads
```

`GET /ops/summary` also includes a note beginning with:

```text
Raw file guard records
```

## Source Tables

The counts come from existing local v0 tables:

```text
uploaded_raw_files
raw_file_scan_results
raw_file_download_approvals
raw_file_download_events
```

This is operational visibility over existing metadata and audit rows.

## Test Evidence

Route test:

```text
test_ops_summary_and_dashboard_surface_raw_file_guard_counts
```

The test exercises:

```text
POST /documents/upload-raw-files
GET /documents/upload-raw-files/{raw_file_id}/download
POST /documents/upload-raw-files/{raw_file_id}/scan-results
POST /documents/upload-raw-files/{raw_file_id}/download-approvals
GET /ops/summary
GET /ops/dashboard
```

Expected local behavior:

```text
uploaded_raw_file_count: 1
raw_file_scan_result_count: 2
raw_file_clean_scan_count: 1
raw_file_scan_error_count: 1
raw_file_download_approval_count: 1
active_download_approval_count: 1
raw_file_download_event_count: 2
blocked_download_event_count: 1
allowed_download_event_count: 1
```

## Boundary

This is local operations metadata only.

It is not download readiness call persistence.

It is not raw byte exposure.

It is not malware scanning proof.

It is not production authorization.

It is not authenticated user identity.

It is not signed URL support.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Next Gate

```text
uploaded raw file guard ops summary runtime smoke v0 if Docker/API verification is desired, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
