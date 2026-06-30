# Robust PDF Extraction Generalization Gap Review

status: accepted-for-implementation

date: 2026-06-30

target_gate: `robust_pdf_extraction_generalization_gap_review_v0`

## Current Repo State

NoiseProof has separate proof gates for cross-publisher real-world PDF fixture
coverage, real-world table extraction observations, one real-world OCR
observation, and one real-world layout metadata sanity observation.

The current proof surface still says:

```text
can_claim_robust_pdf_extraction: false
```

The next gate must not parse more documents, call an LLM, or broaden the
runtime product. It should review the evidence chain and make the remaining
generalization gaps inspectable before any stronger robust-PDF wording is
allowed.

## Sources To Absorb

| Source | Pattern Borrowed | Local Adaptation | Boundary |
|---|---|---|---|
| PyMuPDF text extraction docs | Text, blocks, dict, sorting, and OCR are separate extraction surfaces. | Keep text, table, OCR, layout metadata, and reading-order claims separate. | PyMuPDF output alone is not robust PDF extraction evidence. |
| Docling technical report / project | Robust document conversion is a multi-stage system, not a single parser flag. | Treat extraction generalization as a capability matrix across modalities. | NoiseProof does not claim Docling integration. |
| Unstructured partitioning docs | Partitioned elements carry type and metadata and vary by strategy. | Keep element type, metadata, and source role explicit in future parser outputs. | NoiseProof does not claim Unstructured integration. |
| DocLayNet / PubLayNet papers | Layout quality needs labeled layout classes or benchmark-like ground truth. | Record that current layout metadata sanity checks are not labeled layout evaluation. | NoiseProof does not claim benchmark performance. |

## Implementation Target

Add a deterministic review gate that reads a committed, sanitized JSON review
packet and generates a Markdown report.

Required artifacts:

```text
examples/pdf-extraction-quality/robust-pdf-generalization-gap-review.json
packages/ingestion/pdf_quality/robust_pdf_generalization_gap_review.py
apps/api/app/services/robust_pdf_generalization_gap_review_command.py
apps/api/tests/test_robust_pdf_generalization_gap_review.py
docs/evaluation/robust-pdf-generalization-gap-review-report.md
docs/review/robust-pdf-generalization-gap-review.md
```

Required proof-surface updates:

```text
README.md
docs/MASTER-SPEC.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
docs/review/proof-gap-action-surface.md
docs/research/source-assimilation-registry.md
apps/api/app/services/proof_gap_registry.py
.github/workflows/ci.yml
```

## Data Contract

The review packet must include:

```text
phase_marker
previous_gate
claim_boundary
can_claim_robust_pdf_extraction
generalization_gap_status
evidence_chain
capability_reviews
minimum_next_evidence
blocked_reasons
boundary_notes
recommended_next_gate
```

The review must preserve these distinctions:

- digital text parse observations
- cross-publisher fixture coverage
- table extraction observations
- OCR observation
- layout metadata sanity observation
- labeled layout ground truth
- natural reading order correctness
- rendered visual fidelity
- image/chart interpretation
- arbitrary-market PDF coverage
- external reviewer validation

## Non-goals

- No new PDF downloads.
- No external PDF binaries.
- No raw extracted text.
- No OCR runtime call.
- No table extraction runtime call.
- No retrieval, Evidence Ledger, Critic, report generation, dashboard, or LLM
  call.
- No robust PDF extraction claim.

## Acceptance

- The review status is `passed` only as a review artifact.
- `can_claim_robust_pdf_extraction` remains false.
- The report states that robust PDF extraction remains unproven.
- The proof-gap registry points the next robust-PDF gate to
  `multi_publisher_modality_stratified_pdf_eval_v0`.
- CI checks that the generated report is not stale.
