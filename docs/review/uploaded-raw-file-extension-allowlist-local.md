# Uploaded Raw File Extension Allowlist Local

Status: local API behavior implemented and unit-tested.

Phase marker: uploaded raw file extension allowlist local v0.

## Purpose

This gate adds a small local filename extension allowlist before raw upload persistence.

The goal is to make filename policy inspectable before raw bytes enter the quarantine table.

It does not claim robust file-type detection.

It does not claim production file-upload security.

## Implemented Boundary

Endpoint:

```text
POST /documents/upload-raw-files
```

Boundary marker:

```text
local_v0_extension_allowlist_not_production
```

Implementation points:

```text
EXTENSION_ALLOWLIST_BOUNDARY
ALLOWED_RAW_FILE_EXTENSIONS
SOURCE_TYPE_EXTENSIONS
DANGEROUS_INNER_EXTENSIONS
_validate_raw_file_extension
_filename_extensions
_extension_allowlist_decision
```

The route now performs extension validation after size checking and before signature validation or raw byte persistence.

Order:

```text
size check
-> extension allowlist check
-> file signature validation
-> raw byte persistence
```

## Allowlist

Current local v0 allowlist:

```text
.pdf
.csv
.html
.htm
.md
.markdown
.txt
```

The validator URL-decodes the filename before validation, normalizes extensions to lowercase, ignores path components when extracting the basename, and checks source_type-specific extension compatibility when the declared source type is known.

## Success Behavior

Allowed CSV upload:

```text
filename: sample.csv
source_type: csv
status: 201
extension_boundary: local_v0_extension_allowlist_not_production
client_filename_extension: .csv
extension_decision: allowed
```

The response remains metadata-only and includes no raw bytes.

Warnings include:

```text
Extension validation is local v0 and should not be used on its own.
Content-Type header can be spoofed; local extension validation treats it as metadata only.
```

## Block Behavior

Suspicious double extension:

```text
filename: sample.exe.csv
source_type: csv
status: 415
block_reason: suspicious double extension
client_filename_extension: .csv
extension_boundary: local_v0_extension_allowlist_not_production
```

The blocked response includes no raw bytes and the upload is not persisted.

The warning list includes:

```text
double extension detected before extension validation
```

Other local v0 block reasons include:

```text
filename contains null byte
missing filename extension
filename extension not allowed
filename extension source_type mismatch
```

## Tests

Focused route tests:

```powershell
uv run pytest -q tests/test_routes.py -k "extension_allowlist"
```

Observed result:

```text
2 passed, 125 deselected, 1 warning
```

Focused documentation test:

```powershell
uv run pytest -q tests/test_docs.py -k "extension_allowlist_local"
```

Expected after this document is added:

```text
1 passed
```

## Boundary

This is local v0 endpoint code only.

This is not robust file-type detection.

This is not malware scanning evidence.

This is not production authorization.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not production malware scanning evidence.

This is not endpoint malicious-detection runtime proof.

This is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
uploaded raw file extension allowlist runtime smoke v0
```
