# External Review Issue Body Signature-validation Refresh

Status: owner-authored issue body edit only.

Phase marker: external review issue body signature-validation refresh v0.

## Purpose

This gate updates the live public external review issue body so reviewers can reach the raw file signature validation runtime smoke proof from issue #1.

It is request infrastructure only.

It does not add runtime behavior.

It does not close external reviewer feedback v0.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed after edit:

```json
{
  "updatedAt": "2026-06-04T11:40:14Z",
  "state": "OPEN",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_signature_validation_proof": true,
  "has_signature_validation_request_refresh": true,
  "has_external_feedback_boundary": true,
  "comment_count": 1,
  "labels": "external-review,feedback"
}
```

Text markers:

```text
starts_with_request: true
first_codepoint: 35
comment_count: 1
has_signature_validation_proof: true
has_signature_validation_request_refresh: true
```

## Added Links

Raw file signature validation runtime smoke:

```text
docs/review/uploaded-raw-file-signature-validation-runtime-smoke.md
```

External reviewer signature-validation request refresh:

```text
docs/review/external-reviewer-signature-validation-request-refresh.md
```

## Added Boundary

The issue body now states that the raw file signature validation runtime smoke:

```text
local Docker PostgreSQL plus live FastAPI HTTP for local v0 raw file signature validation
spoofed CSV upload returns 201
declared PDF mismatch returns 415
blocked response has no raw bytes
mismatch hash is not recently persisted
not hosted deployment evidence
not external reviewer feedback
not robust file-type detection
not malware scanning evidence
not endpoint malicious-detection runtime proof
not production authorization
not product-complete
```

The request refresh boundary also states:

```text
owner-authored request-surface update only
does not close external reviewer feedback v0
not hosted deployment evidence
not robust file-type detection
not malware scanning evidence
not endpoint malicious-detection runtime proof
not production authorization
not product-complete
```

## Boundary

This is an owner-authored issue body edit.

This does not close external reviewer feedback v0.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not robust file-type detection.

This is not malware scanning evidence.

This is not production authorization.

This is not production malware scanning evidence.

This is not endpoint malicious-detection runtime proof.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
external feedback current-state signature-validation issue verification v0
```
