# Uploaded Raw File Storage

Status: implemented.

Phase marker: uploaded raw file storage v0.

## Source-first anchors

- FastAPI file upload handling: https://fastapi.tiangolo.com/tutorial/request-files/
- OWASP File Upload Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

Interpretation used for this gate:

- `UploadFile` is the existing FastAPI boundary for multipart upload bytes.
- The original filename is recorded as metadata only and is not used as a storage key.
- The storage surface is deliberately quarantined and metadata-heavy before any parser, download, scanning, or production file-serving behavior is claimed.

## Implemented Surface

Endpoint:

```text
POST /documents/upload-raw-files
GET /documents/upload-raw-files
```

Schema:

```text
uploaded_raw_files
```

Persistence boundary:

```text
raw_upload_quarantine_db_bytea_no_download_endpoint
```

Storage behavior:

```text
raw bytes stored in PostgreSQL BYTEA
metadata response only
content_sha256 recorded
storage_key generated internally with UUID hex
filename retained only as original metadata
max_raw_upload_bytes default: 1000000
oversized uploads rejected with HTTP 413
```

The response returns:

```text
id
content_sha256
storage_key
filename
source_type
content_type
size_bytes
storage_backend
quarantine_status
persistence_boundary
raw_file_storage
warnings_json
created_at
```

The response does not return:

```text
raw_bytes
```

## Verification

Route tests:

```bash
cd apps/api
uv run pytest tests/test_routes.py -q -k "upload_raw_file"
```

Expected result:

```text
2 passed
```

The tests verify:

```text
POST /documents/upload-raw-files -> 201
GET /documents/upload-raw-files -> 200
storage_key does not use ../../evil.csv
storage_key contains no slash, backslash, dot-dot, or original filename
raw_bytes are not exposed in responses
oversized upload -> 413
oversized upload does not create a listed record
```

## Boundary

This is raw upload quarantine storage only.

This is not malware scanning.

This is not a download endpoint.

This is not robust PDF extraction.

This is not parser quality evidence.

This is not semantic retrieval evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.
