# ClamAV Service Boundary Review

Status: review-only.

Phase marker: ClamAV service boundary review v0.

## Purpose

This gate selects the service boundary for any future API integration with a real ClamAV runtime.

It follows `docs/review/clamav-api-integration-boundary-review.md`, which rejected Docker CLI execution per API request.

It does not add a ClamAV service to Docker Compose yet.

It does not change the API scanner default.

## Source-first Anchors

- ClamAV Docker documentation: https://docs.clamav.net/manual/Installing/Docker.html
- ClamAV clamd protocol documentation: https://docs.clamav.net/manual/Usage/ClamdProtocol.html
- ClamAV Scanning documentation: https://docs.clamav.net/manual/Usage/Scanning.html
- ClamAV Signature Management documentation: https://docs.clamav.net/manual/Usage/SignatureManagement.html

Interpretation used for this review:

```text
clamd is a daemon/service boundary, not a per-request process boundary.
TCP sockets are not encrypted or authenticated, so they must not be exposed to untrusted networks.
Path-based scans are resolved on the daemon host; API temp paths must be meaningful to the scanner service or content must be streamed.
An API-generated temporary path cannot be blindly passed to clamd unless the future compose boundary makes the same path available to the scanner service.
Signature database state is part of scanner readiness and must be visible in runtime proof.
```

## Decision

Select a review-before-code path:

```text
ClamAV compose service review v0
```

The future compose review should decide:

```text
whether to add a clamav service to docker-compose.yml
whether the API should talk to clamd over an internal-only Docker network
whether to use INSTREAM-style scanning instead of path-based scans
how API temporary files, shared mounts, or streamed bytes cross the API-to-scanner boundary
how to record signature database readiness
how to health-check clamd without treating unavailable scanner as clean
how to map clamd timeout/unavailable/error to failed / scan_error
```

## Non-selected Paths

Do not expose clamd TCP to host or public networks in this gate.

Do not use Docker CLI execution per API request.

Do not mount arbitrary host paths into a scanner container from the API yet.

Do not switch `NOISEPROOF_SCANNER=clamav` as the default.

Do not claim endpoint runtime proof with real ClamAV yet.

## Boundary

This is review-only.

This is not Docker Compose service code.

This is not API endpoint integration.

This is not endpoint runtime proof with real ClamAV.

This is not malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
ClamAV compose service review v0
```
