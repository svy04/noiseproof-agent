# ClamAV Compose Service Review

Status: review-only.

Phase marker: ClamAV compose service review v0.

## Purpose

This gate selects the future Docker Compose shape for a real ClamAV service before editing `docker-compose.yml`.

It follows `docs/review/clamav-service-boundary-review.md`, which selected a dedicated daemon/service boundary and rejected Docker CLI execution per API request.

It does not add a `clamav` service yet.

It does not change the API scanner default.

## Source-first Anchors

- ClamAV Docker documentation: https://docs.clamav.net/manual/Installing/Docker.html
- ClamAV clamd protocol documentation: https://docs.clamav.net/manual/Usage/ClamdProtocol.html
- ClamAV Scanning documentation: https://docs.clamav.net/manual/Usage/Scanning.html
- ClamAV Signature Management documentation: https://docs.clamav.net/manual/Usage/SignatureManagement.html
- Docker Compose services reference: https://docs.docker.com/reference/compose-file/services/

Interpretation used for this review:

```text
clamd belongs behind a service boundary.
TCP sockets are not encrypted or authenticated, so clamd must stay on an internal-only network.
Compose service startup ordering is not the same thing as scanner readiness.
signature database readiness must be visible before runtime proof can mean anything.
Path-based scans are resolved on the daemon host, so API-generated temporary paths must not be blindly sent to clamd.
```

## Decision

Decision summary: select a future internal-only `clamav` compose service before API integration.

The future implementation should:

```text
add a dedicated clamav service to docker-compose.yml
use an official ClamAV container image unless implementation evidence says otherwise
keep clamd reachable only from the API service on the Compose network
do not publish clamd ports to the host
prefer streamed bytes over API temp-path scanning unless a shared mount is explicitly designed
record ClamAV version and signature database state in runtime proof
map unavailable, timeout, and scanner errors to failed / scan_error, never clean
keep NOISEPROOF_SCANNER=unavailable as the default until real endpoint smoke exists
```

The future implementation may use `depends_on` for startup ordering, but depends_on must not be treated as scanner readiness evidence. Readiness needs an explicit scanner health/readiness check or a runtime smoke artifact that proves clamd accepted scans with a current signature database.

## Non-selected Paths

Do not publish clamd TCP to host or public networks.

Do not rely on Docker CLI execution per API request.

Do not pass API temporary file paths to clamd unless a shared filesystem boundary is intentionally designed and documented.

Do not switch `NOISEPROOF_SCANNER=clamav` as the default in the compose review gate.

Do not claim endpoint runtime proof with real ClamAV until the API endpoint is exercised against the real scanner service.

## Boundary

This is review-only.

This is not Docker Compose code.

This is not clamd runtime verification.

This is not API endpoint integration.

This is not endpoint runtime proof with real ClamAV.

This is not malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
ClamAV compose service implementation v0
```
