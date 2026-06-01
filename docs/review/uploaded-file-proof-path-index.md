# Uploaded File Proof Path Index

Phase marker: uploaded file proof path index refresh v0.

## Purpose

This index gives a short reader path for the uploaded-file proof chain. It exists so a reviewer can inspect the current upload boundary without reading the entire phase history in `docs/GOAL.md`.

## Current upload proof path

Read in this order:

1. `docs/review/file-upload-preview.md`
   - Parser/profile preview over an uploaded file.
   - Boundary: does not create documents and does not claim robust PDF extraction.

2. `docs/review/uploaded-file-chunk-preview.md`
   - Uploaded file parser/profile output can reach chunk strategy preview.
   - Boundary: does not create documents or chunks.

3. `docs/review/uploaded-file-retrieval-preview.md`
   - Uploaded file chunks can reach lexical retrieval preview.
   - Boundary: does not create retrieval_runs and does not treat retrieval candidates as truth.

4. `docs/review/uploaded-file-evidence-preview.md`
   - Uploaded file retrieval candidates can become preview Evidence Ledger entries.
   - Boundary: does not create Evidence Ledger entries.

5. `docs/review/uploaded-file-noise-gate-preview.md`
   - Uploaded file Evidence Ledger preview entries can be checked by the deterministic Noise Gate preview.
   - Boundary: does not create Noise Gate records and does not generate a final report.

6. `docs/review/uploaded-file-report-preview.md`
   - Uploaded file evidence can reach deterministic report preview while obeying the embedded Noise Gate.
   - Boundary: does not create report records, and `needs_revision` or `blocked` keeps the report body null.

7. `docs/review/uploaded-file-failure-case-draft-preview.md`
   - Blocked or needs-revision upload report previews can produce a human-confirmed failure-case draft.
   - Boundary: does not create failure_cases, does not automate failure detection, and does not automate root-cause analysis.

8. `docs/review/uploaded-file-failure-case-manual-handoff-smoke.md`
   - The draft payload can be manually submitted to the existing `POST /failure-cases` endpoint.
   - Boundary: manual handoff only, not automatic failure-case creation.

## What this proves

The upload chain can move an uploaded file through parser/profile inspection, chunk preview, lexical retrieval preview, Evidence Ledger preview, Noise Gate preview, report preview, failure-case draft preview, and manual failure-case persistence handoff.

## What this does not prove

This index is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, semantic retrieval, embeddings, LLM output, automatic failure-case creation, automatic failure detection, or root-cause automation.

## Next gate

The next useful product gate should be selected from the upload proof path after external review or a focused runtime gap review. A bounded candidate is:

```text
uploaded file runtime smoke packet v0
```

That would verify the upload proof path through a live local server/curl sequence, without claiming hosted deployment or external validation.
