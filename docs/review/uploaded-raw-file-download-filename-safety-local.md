# Uploaded Raw File Download Filename Safety Local v0

Phase marker: uploaded raw file download filename safety local v0.

## Goal

Make the guarded raw file download endpoint's `Content-Disposition` filename boundary inspectable without expanding the file-serving scope.

This gate handles only the display filename used in the HTTP attachment header.
It does not change raw upload persistence, scan requirements, download authorization, scanner behavior, or storage keys.

## Source-first basis

Primary source:

- OWASP File Upload Cheat Sheet: file upload defenses should be layered; user-provided file metadata such as filenames and content types should not be trusted as proof, and applications should control storage and filename handling.

Local interpretation:

- Keep the original filename as metadata only.
- Do not use the original filename as a storage key, scan temporary path, or authorization signal.
- For downloads, derive a conservative ASCII attachment filename from the metadata value.
- Make the boundary visible in a response header so reviewers can inspect it.

## Implemented boundary

The guarded download endpoint now returns:

```text
X-NoiseProof-Download-Filename-Boundary: local_v0_content_disposition_filename_safety_not_production
```

The filename helper:

```text
URL-decodes the metadata filename
ignores path components
allows only A-Z, a-z, 0-9, dot, underscore, and hyphen
strips unsafe leading/trailing dot, underscore, and hyphen characters
falls back to raw-file-<uuid>.bin if the candidate becomes empty
limits the filename to 120 characters
preserves a short alphanumeric extension when truncating
```

## Tests

Focused command:

```bash
cd apps/api
uv run pytest -q tests/test_routes.py -k "safe_download_filename or download_returns_bytes_after_latest_clean_scan_only"
```

Observed result:

```text
3 passed, 126 deselected, 1 warning
```

The tests check:

```text
path separators are removed
CRLF/control-like filename input is removed after URL decoding
overlong names are capped
the extension is preserved when possible
empty normalized candidates fall back to raw-file-<uuid>.bin
successful guarded downloads expose the filename-boundary header
```

## What this proves

This proves only a local v0 filename-safety boundary for the guarded raw download attachment header.

It makes the response easier to inspect and reduces accidental path/header-shaped filename leakage in local API behavior.

## What this does not prove

This is not:

```text
production authorization
distributed rate limiting
production malware scanning evidence
hosted deployment evidence
robust file serving
robust file-type detection
endpoint malicious-detection runtime proof
external reviewer feedback
customer validation
Braincrew acceptance
product-complete evidence
```

## Next recommended gate

```text
uploaded raw file download filename safety runtime smoke v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
