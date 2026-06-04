# Uploaded Raw File Signature Validation Local

Status: local API behavior.

Phase marker: uploaded raw file signature validation local v0.

## Purpose

Add the smallest local v0 file signature validation behavior to `POST /documents/upload-raw-files`.

The goal is not robust file-type detection.

The goal is to stop obvious raw-upload type mismatches before bytes are persisted, and to make accepted uploads carry explicit signature-boundary metadata in `warnings_json`.

## Implemented Boundary

```text
local_v0_magic_prefix_allowlist_not_production
```

The route inspects a small byte prefix before persistence.

It records structured warning strings for accepted files:

```text
signature_boundary
declared_source_type
declared_content_type
detected_signature_type
signature_confidence
```

It also records the warning:

```text
Content-Type header can be spoofed
```

## Route Behavior

Endpoint:

```text
POST /documents/upload-raw-files
```

Accepted local v0 route test:

```text
source_type=csv
declared Content-Type: application/pdf
detected_signature_type: csv
status: 201
raw_bytes omitted from response
```

Blocked local v0 route test:

```text
source_type=pdf
declared Content-Type: application/pdf
raw bytes: CSV-like text without %PDF- prefix
detected_signature_type: csv
status: 415
block_reason: file signature mismatch
no raw bytes in error detail
no persisted raw file row
```

## Verification

Focused route verification:

```text
uv run pytest -q tests/test_routes.py -k "signature_validation"
2 passed, 123 deselected, 1 warning
```

Raw-file route regression verification:

```text
uv run pytest -q tests/test_routes.py -k "upload_raw_file or raw_file_download or scan_execution or scan_result"
12 passed, 113 deselected, 1 warning
```

## What This Proves

NoiseProof Agent now has a local v0 guard before raw upload persistence.

It treats `Content-Type` as metadata that can be spoofed.

It can accept a CSV payload even when the declared header is misleading.

It can block a declared PDF when the raw prefix is clearly not PDF-like.

## Boundary

This is local API behavior only.

This is not robust file-type detection.

This is not a full allowlist policy.

This is not malware scanning evidence.

This is not production authorization.

This is not production file upload security.

This is not hosted deployment evidence.

This is not endpoint malicious-detection runtime proof.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
uploaded raw file signature validation runtime smoke v0
```
