# Uploaded Raw File Scan Result Schema

Status: implemented.

Phase marker: uploaded raw file scan result schema v0.

## Purpose

This gate adds the smallest schema-only place to record future raw-upload scan attempts.

It does not scan files.

It does not run ClamAV.

It does not open a download endpoint.

It does not prove runtime behavior.

## Added Files

```text
db/migrations/017_raw_file_scan_results.sql
```

The fresh database schema in `db/init/001_schema.sql` now also includes:

```text
raw_file_scan_results
```

## Schema Boundary

The new table is:

```sql
CREATE TABLE IF NOT EXISTS raw_file_scan_results
```

It links each scan attempt to an existing quarantined raw upload:

```text
raw_file_id -> uploaded_raw_files(id)
```

The migration uses:

```text
raw_file_id UUID NOT NULL REFERENCES uploaded_raw_files(id) ON DELETE CASCADE
```

This keeps the first boundary simple: scan results are derived records for one quarantined raw file. If future retention rules require scan evidence to survive raw-file deletion, that should be handled in a separate retention/deletion policy gate.

## Columns

The schema records scan provenance and failure state:

```text
id
raw_file_id
scanner_name
scanner_version
signature_db_version
scan_started_at
scan_finished_at
scan_status
scan_verdict
matched_signature
error_message
metadata_json
created_at
```

The indexed fields are:

```text
raw_file_id
scan_status
scan_verdict
```

## Status And Verdict

`scan_status` records execution state:

```text
pending
running
completed
failed
skipped
```

`scan_verdict` records the safety result:

```text
pending
clean
suspicious
infected
scan_error
skipped
```

scan_error is not clean.

`failed` means scanner execution failed.

`scan_error` means no clean verdict was established.

`skipped` must be visible through `metadata_json` or `error_message` when repository/API code is added later.

## Why This Comes Before Scanner Code

The previous review selected schema first because raw-upload safety needs an inspectable place for scanner attempts before introducing a scanner process.

The intended order remains:

```text
uploaded raw file scan result schema v0
uploaded raw file scan result repository review v0
uploaded raw file scan result repository v0
uploaded raw file scan result endpoint review v0
uploaded raw file scan result endpoint v0
scanner adapter review v0
ClamAV adapter v0
```

This gate closes only the first line.

## Verification Surface

Local static verification should confirm:

```text
db/init/001_schema.sql
db/migrations/017_raw_file_scan_results.sql
```

Runtime migration verification is a later smoke gate unless explicitly performed.

## Explicit Non-claims

This is schema-only.

This is not malware scanning.

This is not scanner execution.

This is not ClamAV integration.

This is not file signature validation.

This is not a download endpoint.

This is not runtime evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Next Product Gate

The selected next product gate is:

```text
uploaded raw file scan result repository review v0
```

That gate should decide repository functions and payload shape before any endpoint, scanner execution, ClamAV integration, file signature validation, download endpoint, hosted deployment evidence, or external reviewer feedback.
