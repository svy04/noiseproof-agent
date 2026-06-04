# Uploaded Raw File Download Rate Limit Review

Status: review-only.

Phase marker: uploaded raw file download rate limit review v0.

## Purpose

The guarded raw file download endpoint now blocks raw bytes unless the latest scan result is `completed / clean`.

It still marks download rate limiting as:

```text
planned_not_enforced_local_v0
```

This gate decides the smallest next rate-limit boundary for the local portfolio system before implementing it.

## Source-first Basis

Primary source:

```text
https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
```

Relevant source points, paraphrased:

- Public file retrieval can create disclosure, DoS, and abuse-hosting risks.
- File upload defenses should be layered; one control is not enough.
- If downloads are available, request limits should exist to reduce DoS exposure.
- User permissions remain separate from download rate limiting.

NoiseProof already has:

```text
scan-first guarded download
no raw bytes in upload/list/scan metadata responses
handler-based explicit download endpoint
nosniff response header
safe Content-Disposition filename
local_v0_no_auth_not_production boundary header
planned_not_enforced_local_v0 rate-limit boundary header
```

## Decision

Select a future local v0 download rate-limit gate.

The future implementation should be intentionally small:

```text
per-process in-memory fixed window
keyed by raw_file_id plus client host when available
applies only to successful clean-download attempts and blocked download attempts
returns HTTP 429 when exceeded
keeps response body metadata-only
adds no durable rate-limit store
adds no distributed rate limiting
adds no production authorization
adds no production malware scanning claim
```

Suggested default for local v0:

```text
5 download attempts per 60 seconds per raw_file_id/client-host key
```

## Why This Gate Comes Before Authorization

Authorization remains important, but this repo has no auth model yet.

Adding fake auth would make the project look safer than it is.

A small local rate-limit boundary is lower risk because it can improve inspectability without pretending production access control exists.

The response should still keep:

```text
X-NoiseProof-Authorization-Boundary: local_v0_no_auth_not_production
```

## Required Future Behavior

Future implementation should add:

```text
X-NoiseProof-Download-Rate-Limit-Boundary: local_v0_in_memory_fixed_window_not_production
```

For exceeded attempts:

```text
HTTP 429
detail: raw file download rate limit exceeded
```

Tests should cover:

```text
clean download succeeds before limit
blocked no-scan attempts also count toward the local limit
limit is scoped by raw_file_id
limit does not reveal raw bytes in 429 responses
authorization boundary remains local_v0_no_auth_not_production
```

## Not Selected

Do not implement in this review gate:

```text
Redis-backed rate limiting
tenant/user-level quotas
authentication
authorization
signed URLs
public object storage
global distributed rate limits
production abuse controls
bot detection
WAF integration
```

## Boundary

This is review-only.

This is not endpoint code.

This is not an enforced rate limit.

This is not production authorization.

This is not production malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
uploaded raw file download rate limit local v0
```
