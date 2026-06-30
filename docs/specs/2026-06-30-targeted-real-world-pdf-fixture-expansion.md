# Targeted Real-world PDF Fixture Expansion

status: accepted-for-implementation

date: 2026-06-30

target_gate: `targeted_real_world_pdf_fixture_expansion_v0`

## Current Repo State

The previous gate, `multi_publisher_modality_stratified_pdf_eval_v0`, turned the
robust-PDF generalization gap into a 12-cell publisher/modality/failure-class
matrix. The matrix kept `coverage_status -> partial`,
`robust_pdf_eval_status -> blocked`, and
`can_claim_robust_pdf_extraction -> false`.

The next useful gate is not more runtime parsing. The next useful gate is a
source-policy-reviewed fixture expansion plan that maps each missing matrix
cell to a candidate source, acceptance checks, and stop conditions.

## Sources To Absorb

| Source | Pattern Borrowed | Local Adaptation | Boundary |
|---|---|---|---|
| BLS copyright information | Published BLS material can be reused with citation boundaries. | Use BLS report/article PDFs as policy-reviewed candidates for reading order and image/chart cells. | No download or redistribution happens in this gate. |
| BLS Monthly Labor Review about page | MLR text/charts/tables may be public domain with proper credit while some photos remain protected. | Use MLR as a multi-column reading-order candidate with third-party-image stop conditions. | Not visual-fidelity evidence. |
| EIA copyrights and reuse | U.S. government EIA publications are reusable with acknowledgment and protected marks excluded. | Use STEO as a rendered visual-fidelity candidate. | Not parser/runtime evidence. |
| BEA public domain FAQ | BEA pages can seed layout candidate continuity with citation. | Use the existing BEA working paper route for a local layout-label sidecar candidate. | Not DocLayNet/PubLayNet benchmark evidence. |
| NARA 9/11 records policy boundary | Archival records require record-level caution, not blanket rights assumptions. | Use the existing NARA MFR route as a no-native-text candidate while keeping raw text and binary files out. | Not OCR quality evidence. |

## Implementation Target

Add a deterministic source-policy plan from a committed sanitized packet:

```text
examples/pdf-extraction-quality/targeted-real-world-pdf-fixture-expansion-plan.json
packages/ingestion/pdf_quality/targeted_fixture_expansion.py
apps/api/app/services/targeted_real_world_pdf_fixture_expansion_command.py
apps/api/tests/test_targeted_real_world_pdf_fixture_expansion.py
docs/evaluation/targeted-real-world-pdf-fixture-expansion-report.md
docs/review/targeted-real-world-pdf-fixture-expansion.md
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

The plan packet must include:

```text
phase_marker
previous_gate
claim_boundary
plan_status
coverage_status
can_claim_robust_pdf_extraction
runtime/download/parser/OCR/table/LLM booleans
missing_cells
source_policy_sources
candidates
minimum_next_evidence
blocked_reasons
warnings
boundary_notes
recommended_next_gate
```

Each candidate must include:

```text
fixture_id
target_missing_cell
publisher
source_url
policy_source_url
policy_review_status
download_status
local_pdf_path
sha256
evaluation_intent
acceptance_checks
stop_conditions
boundary
```

## Non-goals

- No new PDF downloads.
- No external PDF binaries.
- No download cache.
- No raw extracted text.
- No raw OCR text.
- No raw table rows.
- No page images or screenshots.
- No parser runtime call.
- No OCR runtime call.
- No table extraction runtime call.
- No LLM calls.
- No retrieval, Evidence Ledger, Critic, final report generation, or dashboard work.
- No robust PDF extraction claim.

## Acceptance

- `plan_status -> passed` only means the source-policy plan artifact exists.
- Candidate count is exactly 6.
- Each missing cell from the prior matrix has one candidate or reviewer route.
- Download count remains 0.
- Runtime work remains false.
- `can_claim_robust_pdf_extraction` remains false.
- The next gate is `real_world_pdf_fixture_source_policy_download_hash_v0`.
- CI checks that the generated report is not stale.
