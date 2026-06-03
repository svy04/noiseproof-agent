# External Reviewer Brief

Status: reviewer-facing brief.

Phase marker: external reviewer brief v0.

Label: External reviewer brief.

This is the shortest review packet for someone who has only a few minutes.

It prepares the `external reviewer feedback v0` gate, but it does not complete it.

## 2-minute path

Read only these:

1. `README.md`
2. `docs/review/external-reader-proof-path.md`
3. `docs/application/portfolio-index.md`
4. `docs/review/local-browser-screenshot-walkthrough.md`
5. `docs/review/uploaded-file-intake-manifest-runtime-smoke.md`
6. `docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md`
7. `docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md`
8. `docs/review/uploaded-file-chunk-persistence-runtime-smoke.md`
9. `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md`
10. `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`
11. `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md`
12. `docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md`
13. `docs/review/retrieval-run-linked-report-runtime-smoke.md`
14. `docs/evaluation/semantic-retrieval-quality-report.md`
15. `docs/review/uploaded-raw-file-storage-runtime-smoke.md`
16. `docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md`
17. `docs/review/external-feedback-intake-criteria.md`

uploaded-file intake manifest proof:

```text
docs/review/uploaded-file-intake-manifest-runtime-smoke.md
```

This proof is not raw file storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file intake manifest persistence proof:

```text
docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md
```

This proof is manifest metadata only, not raw file storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file parsed document persistence proof:

```text
docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md
```

This proof is document metadata/profile only, not raw file storage, not parsed text persistence, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file chunk persistence proof:

```text
docs/review/uploaded-file-chunk-persistence-runtime-smoke.md
```

This proof is not automatic persistence from upload preview, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file chunk handoff proof:

```text
docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md
```

This proof is explicit `POST /documents/upload-chunks` handoff evidence, not raw uploaded byte storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file retrieval persistence proof:

```text
docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md
```

This proof is explicit `POST /documents/{document_id}/retrieval-runs` over persisted `document_chunks`, not Evidence Ledger generation, not hosted deployment evidence, and not external reviewer feedback.

uploaded raw file storage proof:

```text
docs/review/uploaded-raw-file-storage-runtime-smoke.md
```

This proof is explicit `POST /documents/upload-raw-files` and `GET /documents/upload-raw-files` over quarantined PostgreSQL BYTEA storage, not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.

uploaded raw file scan result endpoint proof:

```text
docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md
```

This proof is explicit `POST /documents/upload-raw-files/{raw_file_id}/scan-results` and `GET /documents/upload-raw-files/{raw_file_id}/scan-results`, preserves `scan_verdict -> scan_error`, records `response_has_raw_bytes -> false`, and is not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.

retrieval-run-linked Report proof:

```text
docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md
docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md
docs/review/retrieval-run-linked-report-runtime-smoke.md
```

This proof is explicit `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, `POST /retrieval-runs/{retrieval_run_id}/noise-gate`, and `POST /retrieval-runs/{retrieval_run_id}/report`. It records `pre_report_status: 409` before a linked Noise Gate exists and `input_noise_gate_record_id` after the gate exists. It is not hosted deployment evidence, not external reviewer feedback, not LLM judgment, not embeddings, not semantic retrieval, not free-form final report generation, and not financial advice.

toy semantic retrieval quality report:

```text
docs/evaluation/semantic-retrieval-quality-report.md
```

This report is toy fixture metric output with `q-what-missing` kept visible. It is not vector search quality evidence, not a benchmark result, not a model comparison, not hosted deployment evidence, and not external reviewer feedback.

Optional public proof route:

```text
https://svy04.github.io/proof-artifacts/noiseproof-live-route-verification-2026-06-01/
```

Then leave feedback here:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Direct link map:

```text
docs/review/external-reviewer-link-map.md
```

## What this currently proves

NoiseProof Agent currently proves a local, inspectable portfolio workflow:

```text
document/profile boundaries
parser/chunk/retrieval previews
collection planning
Evidence Ledger / Noise Gate / report previews
persisted records
workflow parent linkage
lineage read model
local dashboard screenshot
failure-case persistence and manual workflow-parent provenance
```

## What this does not prove

This does not prove:

```text
production RAG quality
hosted deployment
customer validation
Braincrew acceptance
semantic retrieval
semantic retrieval quality evidence
LLM answer quality
robust PDF extraction
distributed tracing
automatic failure-case creation
complete workflow failure causality
financial prediction quality
trading advice
```

## What I want reviewed

Please focus on:

```text
Is the proof path readable?
Which claim feels over-stated?
Which artifact is strongest?
Which artifact is weakest?
What missing evidence would most improve trust?
Does this signal Forward Deployed Engineer work?
What does it not yet prove for Product Engineer?
What should be cut or compressed?
```

## Feedback intake boundary

Use:

```text
docs/review/external-feedback-intake-criteria.md
```

External reviewer feedback remains pending until an outside reviewer leaves a substantive comment that names inspected evidence and gives actionable critique.

## Allowed Claim

NoiseProof Agent has a 2-minute external reviewer brief that points reviewers to the shortest proof path and feedback issue.

## Boundary

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not hosted deployment evidence.

This is not a stronger proof claim.

This does not prove that any reviewer has inspected the repository.

## Next Gate

The next gate remains:

```text
external reviewer feedback v0
```
