# Multi-publisher Modality-stratified PDF Eval

status: accepted-for-implementation

date: 2026-06-30

target_gate: `multi_publisher_modality_stratified_pdf_eval_v0`

## Current Repo State

The previous gate, `robust_pdf_extraction_generalization_gap_review_v0`,
reviewed the current PDF proof chain and kept the robust-PDF claim blocked.
It recommended a multi-publisher, modality-stratified PDF evaluation matrix
before any stronger wording is allowed.

This gate must not add runtime extraction work. It should convert the
generalization gap review into a deterministic matrix that shows which
publisher/modality/failure-class cells are covered in a limited way and which
remain missing.

## Sources To Absorb

| Source | Pattern Borrowed | Local Adaptation | Boundary |
|---|---|---|---|
| Docling technical report | Document conversion is multi-stage and capability-specific. | Keep PDF text, tables, OCR, layout, and serialization claims separated. | No Docling integration or accuracy claim. |
| Unstructured partitioning docs | Element extraction strategies and metadata are explicit. | Treat matrix cells as typed evidence roles, not one opaque PDF success. | No Unstructured integration claim. |
| DocLayNet / PubLayNet | Layout quality needs labeled or benchmark-like ground truth. | Mark layout-class and visual-fidelity cells missing until there is ground truth. | No benchmark performance claim. |
| PubTables-1M / TableBank | Table extraction quality needs table-level structure ground truth. | Keep row/cell counts as limited evidence until table structure quality is evaluated. | No table benchmark claim. |
| OCR-D evaluation | OCR quality should be measured with error-rate-like criteria. | Keep one OCR observation limited until CER/WER-style or expected-span checks expand. | No OCR quality benchmark claim. |

## Implementation Target

Add a deterministic matrix gate from a committed sanitized packet:

```text
examples/pdf-extraction-quality/multi-publisher-modality-stratified-pdf-eval.json
packages/ingestion/pdf_quality/multi_publisher_modality_stratified_pdf_eval.py
apps/api/app/services/multi_publisher_modality_stratified_pdf_eval_command.py
apps/api/tests/test_multi_publisher_modality_stratified_pdf_eval.py
docs/evaluation/multi-publisher-modality-stratified-pdf-eval-report.md
docs/review/multi-publisher-modality-stratified-pdf-eval.md
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

The packet must include:

```text
phase_marker
previous_gate
claim_boundary
matrix_status
coverage_status
robust_pdf_eval_status
can_claim_robust_pdf_extraction
stratification_axes
publisher_strata
modality_strata
matrix_cells
minimum_next_evidence
blocked_reasons
boundary_notes
recommended_next_gate
```

Matrix cells must separate:

- publisher
- modality
- evidence role
- source route
- evidence status
- current evidence summary
- missing evidence
- boundary

## Non-goals

- No new PDF downloads.
- No external PDF binaries.
- No raw extracted text.
- No OCR runtime call.
- No parser runtime call.
- No table extraction runtime call.
- No LLM calls.
- No retrieval, Evidence Ledger, Critic, report generation, or dashboard work.
- No robust PDF extraction claim.

## Acceptance

- The matrix status is `passed` only for creating the matrix artifact.
- Coverage remains `partial`.
- Robust PDF eval status remains `blocked`.
- `can_claim_robust_pdf_extraction` remains false.
- The next gate is `targeted_real_world_pdf_fixture_expansion_v0`.
- CI checks that the generated report is not stale.
