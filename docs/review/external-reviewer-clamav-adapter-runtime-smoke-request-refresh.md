# External Reviewer ClamAV Adapter Runtime Smoke Request Refresh

Status: request infrastructure only.

Phase marker: external reviewer ClamAV adapter runtime smoke request refresh v0.

## Purpose

This gate updates the external reviewer request path so a reviewer can inspect the ClamAV adapter runtime smoke proof without reading the full phase history.

It is request infrastructure only.

It does not add runtime behavior.

It does not edit the live public issue body.

## ClamAV adapter runtime smoke proof

Reviewer-facing surfaces now point to:

- `docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md`

The proof is narrow:

```text
The deterministic smoke command exercises ClamAvScannerAdapter mappings for missing binary, clean output, FOUND output, timeout, and unknown return code through fake runners. It reports real_clamav_runtime_verified -> false and binary_probe_only -> true.
```

## Updated request surfaces

- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/external-review-feedback.md`
- `docs/review/external-review-request.md`
- `docs/review/external-reader-proof-path.md`
- `docs/review/external-reviewer-brief.md`
- `docs/review/external-reviewer-link-map.md`
- `docs/application/portfolio-index.md`
- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`

## Boundaries

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not malware scanning.

This is not real ClamAV execution.

This is not ClamAV installation evidence.

This is not ClamAV signature database evidence.

This is not endpoint behavior.

This is not a download endpoint.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next gate

The next bounded request gate can update or verify the live public issue body so issue #1 points reviewers to the ClamAV adapter runtime smoke proof:

```text
external review issue body ClamAV adapter runtime smoke refresh v0
```
