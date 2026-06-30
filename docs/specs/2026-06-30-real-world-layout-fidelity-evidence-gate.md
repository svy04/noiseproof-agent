# Real-world Layout Fidelity Evidence Gate Spec

status: active

date: 2026-06-30

target_gate: real_world_layout_fidelity_evidence_gate_v0

## Current Repo State

The previous accepted local PDF proof gate is `real_world_ocr_evidence_gate_v0`.
It reduced the OCR blocker for one NARA fixture, but robust PDF extraction
remains unproven because layout fidelity has no real-world evidence gate.

Current next gate in `docs/MASTER-SPEC.md` and `docs/GOAL.md`:

```text
real_world_layout_fidelity_evidence_gate_v0
```

## Sources To Absorb

- PyMuPDF Appendix 1 text extraction documentation: block output and `sort`
  modes expose geometry and reading-order-sensitive extraction surfaces.
- PyMuPDF `Page.get_text()` documentation: dictionary/block extraction exposes
  page-level layout metadata such as block bboxes and types.
- Unstructured partitioning documentation: document parsing should preserve
  element coordinates and metadata separately from final answer claims.
- DocLayNet paper/dataset: layout analysis is a labeled document-understanding
  capability and should not be collapsed into generic text extraction.

## Non-goals

- No robust PDF extraction claim.
- No arbitrary-market layout fidelity claim.
- No layout model, DocLayNet evaluation, Docling integration, or Unstructured
  integration.
- No file upload, retrieval, Evidence Ledger, Critic / Noise Gate, final report,
  hosted deployment, or dashboard work.
- No external PDF binaries, download cache, raw extracted text, raw block text,
  screenshot, rendered page image, or local file path committed.

## Implementation Scope

Add a deterministic report gate over one sanitized real-world layout observation:

```text
source: BEA Working Paper 2022-10 PDF
fixture_id: bea_open_source_software_innovation_wp_2022_10
layout_adapter: pymupdf_get_text_blocks_dict_sort
observed page: first page only
committed evidence: metadata, counts, hash, page geometry, bbox samples, expected marker hit count, marker order sanity
```

## Data Contract

Committed evidence JSON must include:

```text
phase_marker
previous_gate
claim_boundary
source URL
publisher
license/source policy URL
HTTP metadata
SHA-256
byte size
page count
observed page index
page width and height
block counts
text block count
image block count
text blocks with bbox inside page bounds
sample text block bboxes without text
expected layout markers checked
expected marker hit booleans
expected marker order observed
warnings
boundary notes
recommended next gate
```

It must not include:

```text
text_sample
raw_text
raw_extracted_text
raw_block_text
page_image
screenshot
local PDF path
```

## Tests

- RED: `tests/test_real_world_layout_fidelity_evidence_gate.py` must fail
  before implementation with missing module/report artifacts.
- GREEN: focused layout evidence gate tests must pass.
- Adjacent proof-gap tests must show the robust-PDF route advances from
  `real_world_layout_fidelity_evidence_gate_v0` to
  `robust_pdf_extraction_generalization_gap_review_v0`.
- CI staleness check must regenerate the layout report byte-for-byte.

## Docs To Update

- `README.md`
- `docs/GOAL.md`
- `docs/MASTER-SPEC.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/review/proof-gap-action-surface.md`
- `docs/research/source-assimilation-registry.md`
- `docs/review/real-world-layout-fidelity-evidence-gate.md`
- `docs/evaluation/real-world-layout-fidelity-evidence-gate-report.md`

## Stop Conditions

Stop if:

- the BEA PDF cannot be downloaded and hashed from a temporary owner-runtime
  location,
- PyMuPDF cannot expose block/bbox metadata for the first page,
- the implementation would need to commit raw text, rendered images, screenshots,
  or source binaries,
- source policy is too unclear to commit sanitized metadata,
- tests require broad PDF or layout claims.

## Claim Boundaries

Can claim:

```text
one real-world BEA PDF layout-metadata sanity observation was recorded as sanitized metadata
```

Cannot claim:

```text
robust PDF extraction
arbitrary-market PDF parsing reliability
arbitrary-market layout fidelity
natural reading order correctness
rendered visual fidelity
external validation
hosted deployment
product completeness
```

## Next Gate If Passed

```text
robust_pdf_extraction_generalization_gap_review_v0
```
