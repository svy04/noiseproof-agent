# Uploaded Raw File Signature Validation Review

Status: review-only decision.

Phase marker: uploaded raw file signature validation review v0.

## Purpose

Review whether NoiseProof Agent should add a small file signature validation boundary before expanding guarded raw file handling.

This gate is deliberately review-only.

It selects a future local v0 implementation boundary, but it does not add endpoint code.

## Source-first Input

Primary source:

```text
https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
```

Relevant source-derived constraints:

```text
Content-Type header can be spoofed
file signature validation should not be used on its own
use allowlist-oriented validation
treat upload controls as defense in depth
```

## Current Local Context

Implemented local behavior already exists for:

```text
raw upload quarantine storage
scan result metadata persistence
explicit scan execution endpoint
guarded raw file download endpoint
local v0 download rate limiting
```

Still unimplemented:

```text
file signature validation
extension allowlist enforcement
MIME sniffing enforcement
production malware scanning evidence
production authorization
endpoint malicious-detection runtime proof
```

## Decision

Select the smallest future local v0 signature boundary:

```text
planned_not_enforced_local_v0
local_v0_magic_prefix_allowlist_not_production
```

The future local v0 should inspect only a small raw-byte prefix and return structured metadata, warnings, or blocking status.

Initial source types:

```text
pdf
csv
html
markdown
unknown
```

Recommended future result shape:

```text
declared_source_type
declared_content_type
detected_signature_type
signature_boundary
signature_confidence
warnings
block_reason
```

## Local v0 Rules

Recommended future local v0 behavior:

```text
PDF: allow if bytes start with %PDF-
CSV: allow as text-like content only when no binary control-byte signal is present
HTML: allow as text-like content when an html doctype or html tag is visible near the prefix
Markdown: allow as text-like content only when no binary control-byte signal is present
Unknown: warn or block unless explicitly accepted by a later policy
```

This is not robust file-type detection.

This is not malware scanning.

This is not production authorization.

This is only a small local guardrail before download/scanning behavior is allowed to look more trustworthy.

## Why Not Bigger Now

Do not add a broad file identification dependency in this review gate.

Do not parse PDFs, HTML, spreadsheets, or archives for signature validation.

Do not add antivirus policy here.

Do not claim that magic bytes prove safety.

The next implementation should make unsafe or unknown raw files easier to inspect and block locally; it should not imply production-grade upload security.

## Boundary

This is not endpoint code.

This is not an enforced signature validator.

This is not malware scanning evidence.

This is not production authorization.

This is not production file upload security.

This is not hosted deployment evidence.

This is not endpoint malicious-detection runtime proof.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
uploaded raw file signature validation local v0
```
