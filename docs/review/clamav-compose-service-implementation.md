# ClamAV Compose Service Implementation

Status: implemented.

Phase marker: ClamAV compose service implementation v0.

## Purpose

This gate adds a minimal optional ClamAV service to `docker-compose.yml` after the compose service review selected an internal-only service boundary.

It does not connect the API endpoint to the service yet.

It does not make ClamAV the default scanner.

## Implemented

`docker-compose.yml` now includes:

```text
clamav service using clamav/clamav:stable
optional scanner profile
internal Compose exposure on 3310
no host port publishing
not host port publishing
signature database volume at /var/lib/clamav
clamdscan --ping=1 healthcheck
```

The default scanner remains:

```text
NOISEPROOF_SCANNER=unavailable
```

This means the existing scan endpoint still defaults to `failed / scan_error` with `scanner_not_configured` unless future gates explicitly wire a real scanner adapter path.

## Boundary

This is Docker Compose service configuration only.

This is not clamd runtime verification.

This is not API endpoint integration.

This is not endpoint runtime proof with real ClamAV.

This is not malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Verification Target

The intended config-only check is:

```text
docker compose --profile scanner config
```

That command can verify Compose syntax and service shape. It cannot prove that clamd is healthy, that signature databases are current, that the API endpoint can scan with real ClamAV, or that malware scanning works in production.

## Next Product Gate

```text
ClamAV compose service config verification v0
```
