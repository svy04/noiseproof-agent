# Uploaded File Parsed Document Persistence

Phase marker: uploaded file parsed document persistence v0.

This gate adds a bounded persistence step after uploaded-file preview and manifest persistence.

`POST /documents/upload-parsed-documents` accepts a multipart file, runs the existing upload parser/profile preview, and creates a `documents` row with upload metadata and parser/profile summary.

## Implemented Surface

```text
POST /documents/upload-parsed-documents
```

Persisted document fields:

- `source_type`
- `source_uri` as `upload://<filename>`
- `filename`
- `title`
- `extraction_quality`
- `status = parsed_metadata_only`
- `profile_json`

Persisted `profile_json` boundary:

```text
persistence_boundary = document_metadata_and_profile_only_no_raw_file_storage
raw_file_storage = false
parsed_text_storage = false
```

`profile_json` includes parser name, parser metadata, profile summary, parse warnings, failure-case candidate if one exists, and upload byte count.

## Boundaries

This gate stores no raw uploaded bytes.

It also stores no parsed text persistence. The parsed text is only used in-process to produce parser metadata and the document profile.

This is not robust PDF extraction. Phase 340 adds uploaded digital PDF text extraction for `POST /documents/upload-preview`, but this parsed-document persistence gate still does not claim OCR, table extraction, layout fidelity, raw uploaded byte storage, or robust PDF extraction.

This gate does not create chunks, retrieval runs, Evidence Ledger entries, Noise Gate records, report records, workflow runs, hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, LLM calls, embeddings, semantic retrieval, automatic failure-case creation, or product-complete claims.

## Test Evidence

Route-level test:

```text
tests/test_routes.py::test_document_upload_parsed_document_persists_profile_without_raw_file_storage
```

Docs guard:

```text
tests/test_docs.py::test_uploaded_file_parsed_document_persistence_keeps_raw_storage_boundary_visible
```

## Next Gate

The next product gate should be runtime smoke verification for this endpoint against the local Docker PostgreSQL service, if Docker is available.

External reviewer feedback v0 remains open and cannot be closed by owner-authored artifacts.
