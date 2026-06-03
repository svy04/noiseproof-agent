# ClamAV API Service Network Boundary Review

Status: review-only.

Phase marker: ClamAV API service network boundary review v0.

## Purpose

This gate decides how the FastAPI runtime may reach the Compose-managed `clamav` service before endpoint integration.

It follows `docs/review/clamav-service-scanner-adapter.md`, which added `ClamdScannerAdapter` but did not wire it into the API endpoint.

## Source-first Anchors

- Docker Compose networking documentation: https://docs.docker.com/compose/how-tos/networking/
- ClamAV clamd protocol documentation: https://docs.clamav.net/manual/Usage/ClamdProtocol.html

Interpretation used for this review:

```text
Compose service names resolve inside the Compose network.
A host-local API process cannot rely on the Compose service name `clamav`.
clamd TCP is unauthenticated and unencrypted.
Publishing clamd TCP to the host would solve reachability by weakening the boundary.
```

## Decision

Decision summary: do not publish clamd TCP to the host.

Decision summary: do not set CLAMD_HOST=localhost for the local host-run API path.

The API must run inside the Compose network before service-host integration.

The next gate should review an API Compose service shape that can share the internal Docker network with `clamav` without making `clamav` reachable from the host.

Required next-gate constraints:

```text
API service joins the same internal Docker network as clamav
API can address clamd by service name: clamav
clamd remains internal-only
NOISEPROOF_SCANNER=unavailable remains the default unless a later smoke explicitly opts into clamd
no host port publication for clamd
no endpoint runtime proof claim until the API scan endpoint runs against real clamd
```

## Non-selected Paths

Do not publish `3310:3310` for clamd.

Do not route the host-local API to `localhost:3310`.

Do not use `docker compose exec` from inside the API runtime.

Do not switch the default scanner from `NOISEPROOF_SCANNER=unavailable`.

## Boundary

This is review-only.

This is not endpoint code.

This is not API endpoint integration.

This is not endpoint runtime proof with real ClamAV.

This is not production malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
ClamAV API compose service review v0
```
