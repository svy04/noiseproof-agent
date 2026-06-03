# ClamAV Service Scanner Adapter Review

Status: review-only.

Phase marker: ClamAV service scanner adapter review v0.

## Purpose

This gate selects the adapter boundary for connecting the API scan execution path to the Compose-managed ClamAV service.

It follows the local Compose ClamAV runtime and EICAR smoke proofs. Those proofs verify that clamd can run and detect EICAR, but they do not prove API endpoint integration.

## Source-first Anchors

- ClamAV clamd protocol documentation: https://docs.clamav.net/manual/Usage/ClamdProtocol.html
- ClamAV Scanning documentation: https://docs.clamav.net/manual/Usage/Scanning.html
- Python socket documentation: https://docs.python.org/3/library/socket.html

Interpretation used for this review:

```text
clamd TCP is unauthenticated and unencrypted, so it must stay on the internal Docker network.
API temporary paths are not meaningful to a separate clamd service unless a shared filesystem boundary is explicitly designed.
INSTREAM lets the API send bytes to clamd without sharing host or container paths.
Timeouts, unavailable service, protocol errors, and scan errors must map to failed / scan_error, never clean.
```

## Decision

Decision summary: select `ClamdScannerAdapter` as the future service adapter.

The future adapter should:

```text
connect to clamd only over the internal Docker network
use the clamd INSTREAM command for scan bytes
do not pass API temporary paths to clamd
do not expose unauthenticated clamd TCP outside the internal network
do not make `clamdscan` a required API subprocess dependency
map timeout, unavailable service, protocol error, and scanner error to failed / scan_error
keep NOISEPROOF_SCANNER=unavailable as the default until API endpoint runtime smoke proves the service path
```

## Non-selected Paths

Do not extend the current subprocess-oriented `ClamAvScannerAdapter` to call `docker compose exec`.

Do not use `clamdscan` as a required API subprocess dependency.

Do not pass API temporary file paths to clamd.

Do not publish clamd TCP to host or public networks.

Do not switch `NOISEPROOF_SCANNER=clamd` or `NOISEPROOF_SCANNER=clamav` as the default in this review gate.

## Boundary

This is review-only.

This is not adapter code.

This is not API endpoint integration.

This is not endpoint runtime proof with real ClamAV.

This is not production malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
ClamAV service scanner adapter v0
```
