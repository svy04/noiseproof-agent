# ClamAV API Integration Boundary Review

Status: review-only.

Phase marker: ClamAV API integration boundary review v0.

## Purpose

This gate decides how the proven Dockerized ClamAV EICAR runtime smoke should affect the API integration path.

The previous gate proved that `clamav/clamav:stable` can detect a container-internal EICAR file. It did not prove `POST /documents/upload-raw-files/{raw_file_id}/scan` with `NOISEPROOF_SCANNER=clamav`.

This review prevents the project from jumping from a scanner runtime smoke to an unsafe or misleading API integration.

## Source-first Anchors

- ClamAV Docker documentation: https://docs.clamav.net/manual/Installing/Docker.html
- ClamAV Scanning documentation: https://docs.clamav.net/manual/Usage/Scanning.html
- ClamAV On-Access and daemon-oriented documentation index: https://docs.clamav.net/
- Python subprocess documentation: https://docs.python.org/3/library/subprocess.html

Interpretation used for this review:

```text
Dockerized clamscan is useful for a bounded local runtime smoke.
Running docker run once per API request is a poor default service boundary because it couples the API to Docker CLI availability, path mounting semantics, image startup latency, and host Docker permissions.
The current API endpoint should keep NOISEPROOF_SCANNER=unavailable by default.
A future real scanner integration should be reviewed as a service boundary, likely clamd/clamdscan or a dedicated scanner service, before code changes.
```

## Alternatives Considered

### Alternative A: Host clamscan

Pros:

```text
matches the current ClamAvScannerAdapter process shape
simple command execution
```

Cons:

```text
requires host installation
does not match the current verified Docker evidence
harder to make portable across Windows, CI, and deployment targets
signature database state is external to the repo
```

### Alternative B: docker run per scan request

Pros:

```text
matches the verified Dockerized EICAR smoke
no host ClamAV install required
```

Cons:

```text
slow per request
requires Docker CLI and Docker daemon access from the API process
requires host path mounting for every upload
creates a large operational/security boundary
poor production default
```

### Alternative C: ClamAV daemon/service boundary

Pros:

```text
keeps scanner runtime outside the API process
fits a service architecture better than docker run per request
can make health, signature database state, timeout, and failure behavior explicit
```

Cons:

```text
requires a new compose service or external runtime
requires a review of clamd socket/TCP exposure
requires careful failure mapping before endpoint integration
```

## Decision

Do not change the API scanner default yet.

Do not add Docker CLI execution to the API endpoint in the next code gate.

Select a service-boundary review before any API integration:

```text
ClamAV service boundary review v0
```

The future review must decide:

```text
clamd vs clamdscan vs host clamscan
Docker Compose service shape
health check and signature DB visibility
socket/TCP exposure boundary
timeout behavior
mapping unavailable scanner to scan_error
whether endpoint runtime smoke can safely run with real ClamAV
```

## Boundary

This is review-only.

This is not API endpoint integration.

This is not endpoint runtime proof with real ClamAV.

This is not malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
ClamAV service boundary review v0
```
