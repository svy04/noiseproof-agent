# Uploaded Raw File Storage Safety Review

Phase marker: uploaded raw file storage safety review v0.

Status: review-only source-first safety decision.

## Purpose

NoiseProof now has local runtime evidence for quarantined PostgreSQL BYTEA raw upload storage.

This review decides what should happen before expanding that behavior.

## Source-first Inputs

Primary references:

- OWASP File Upload Cheat Sheet: `https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html`
- OWASP Unrestricted File Upload: `https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload`
- ClamAV Scanning: `https://docs.clamav.net/manual/Usage/Scanning.html`
- FastAPI Request Files: `https://fastapi.tiangolo.com/tutorial/request-files/`

Relevant source observations:

- OWASP File Upload Cheat Sheet recommends defense in depth for uploads: allowed extension policy, content-type checks that are not trusted alone, file signature validation, generated filename safety, size limits, controlled storage location, user/file permissions, and antivirus or sandbox checks where available.
- OWASP Unrestricted File Upload treats uploaded files as high-risk because metadata, storage location, size, and content can enable server-side and client-side attacks.
- ClamAV Scanning documents `clamscan` for direct scans and `clamdscan` for daemon-backed scans, with path/socket/streaming implications.
- FastAPI Request Files documents `UploadFile`, including metadata access and spooled file behavior, which is useful for handling larger files without reading every upload into memory at once.

## Current NoiseProof Boundary

Already implemented:

```text
POST /documents/upload-raw-files
GET /documents/upload-raw-files
raw_upload_quarantine_db_bytea_no_download_endpoint
max_raw_upload_bytes
oversized upload -> 413
metadata-only responses
storage key does not include original filename
```

Still missing:

```text
allowed extension and type policy
file signature validation
malware scan verdict
retention and deletion policy
download authorization policy
scan quarantine transition policy
```

## Decision

quarantine-only raw storage remains.

do not add a download endpoint yet.

The next bounded product gate should be:

```text
uploaded raw file scan result schema review v0
```

That gate should define the storage boundary for scan evidence before any ClamAV adapter, scan endpoint, or download endpoint is implemented.

## Candidate Scan Result Boundary

The future schema review should decide whether NoiseProof needs a `raw_file_scan_results` table or an equivalent typed record with:

```text
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
```

Suggested status vocabulary:

```text
pending
clean
suspicious
infected
scan_error
skipped
```

## Why Not Download Yet

Opening download before scan evidence would weaken the claim boundary.

The system can currently prove that bytes are stored in quarantine and not returned.

It cannot yet prove:

```text
the file is safe to retrieve
the file type matches the claimed type
the file signature matches an allowlist
the file has a malware scan verdict
the caller is authorized to download it
retention and deletion are enforced
```

## Implementation Notes For Later

For a later scan adapter:

- prefer a narrow adapter interface before binding to ClamAV directly
- keep scan execution optional in local development
- record scan errors as first-class results, not hidden logs
- do not let a missing scanner become a silent clean verdict
- treat `content_type` and original filename as hints, not proof
- keep raw bytes quarantined until policy permits a transition

## Boundary

This is review-only.

It adds no runtime behavior.

It is not malware scanning.

It is not a download endpoint.

It is not hosted deployment evidence.

It is not a ClamAV integration.

It is not a file signature validator.

It is not a retention/deletion implementation.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, or product-complete.
