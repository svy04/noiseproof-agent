# Uploaded Raw File Extension Allowlist Review

Status: source-first review only.

Phase marker: uploaded raw file extension allowlist review v0.

## Purpose

This review decides whether NoiseProof should add a small local filename extension allowlist before raw upload persistence.

It is intentionally narrower than production file-upload security.

It does not implement endpoint code.

It does not claim that extension checks prove file type.

It does not replace file signature validation, malware scanning, download gating, rate limiting, or production authorization.

## Sources Inspected

- OWASP File Upload Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

OWASP frames file upload security as defense in depth. The guidance includes extension validation using an allowlist, validating after decoding the filename, protecting against double extension and null byte bypasses, treating the Content-Type header as spoofable, and using file signature validation as another check that should not be used on its own.

## Decision

Selected:

```text
planned_not_enforced_local_v0
local_v0_extension_allowlist_not_production
```

The next local v0 should reject or warn on raw uploads whose client filename extension is outside the small source-type allowlist.

Initial local allowlist:

```text
.pdf
.csv
.html
.htm
.md
.markdown
.txt
```

The local v0 should validate after decoding the filename, lowercase the extension before comparison, and represent suspicious names as structured warnings or a 415 block response before persistence.

Minimum bypass cases to test:

```text
double extension
null byte
missing extension
unknown extension
extension/source_type mismatch
Content-Type header can be spoofed
```

The extension allowlist should be treated as one local signal next to the current local magic-prefix file signature boundary.

File signature validation should not be used on its own, and extension validation should not be used on its own.

## Why This Fits NoiseProof

NoiseProof's raw upload path is becoming a proof surface for inspectable input boundaries.

Before the service stores raw bytes, it should make the declared source type, client filename, Content-Type metadata, local signature result, and extension decision visible.

That keeps the system aligned with the project thesis:

```text
Prevent unsupported or unsafe inputs from silently flowing into downstream evidence work.
```

## Alternatives Considered

### Do nothing

This keeps the current signature validation boundary small, but it misses a basic file-upload hygiene signal that is cheap to inspect.

### Use only MIME or Content-Type

Rejected for local v0 because Content-Type header can be spoofed and should be metadata only.

### Use only file signature validation

Rejected because file signature validation should not be used on its own and does not cover every naming and policy issue.

### Add production-grade upload security now

Rejected because that would expand scope into authentication, storage isolation, asynchronous scanning policy, file quarantine, and operational response. Those are not this gate.

## Planned Local v0 Behavior

The next gate should implement uploaded raw file extension allowlist local v0:

```text
POST /documents/upload-raw-files
```

Expected local v0 shape:

```text
extension_boundary: local_v0_extension_allowlist_not_production
declared_source_type: <source_type>
client_filename_extension: <normalized extension or none>
extension_decision: allowed | mismatch | missing | blocked
warnings: [...]
```

Suggested behavior:

```text
allowed source_type=pdf with .pdf
allowed source_type=csv with .csv
allowed source_type=html with .html or .htm
allowed source_type=markdown with .md, .markdown, or .txt
block or warn on .exe, .js, .bat, .cmd, .ps1, and unknown binary/script-like extensions
block double-extension and null-byte suspicious filenames before persistence
```

## Boundary

This is not endpoint code.

This is not an enforced extension validator.

This is not robust file-type detection.

This is not malware scanning evidence.

This is not production authorization.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation, Braincrew acceptance, production readiness, endpoint malicious-detection runtime proof, robust PDF extraction, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
uploaded raw file extension allowlist local v0
```
