# Real-world OCR Evidence Gate Spec

status: active

date: 2026-06-30

target_gate: real_world_ocr_evidence_gate_v0

## Current Repo State

The previous accepted local PDF proof gate is
`real_world_table_extraction_evidence_gate_v0`. It reduced the table extraction
blocker for three temporary owner-runtime BEA/EIA PDF observations, but the
robust-PDF proof gap remains open because OCR and layout fidelity are still
missing.

Current next gate in `docs/MASTER-SPEC.md` and `docs/GOAL.md`:

```text
real_world_ocr_evidence_gate_v0
```

## Sources To Absorb

- PyMuPDF OCR documentation: `Page.get_textpage_ocr()` invokes Tesseract and
  returns a `TextPage` that must be passed to later text extraction calls.
- PyMuPDF OCR guide: OCR support is Tesseract-based, slower than normal text
  extraction, and should be run only when beneficial.
- OCRmyPDF documentation: OCR PDF work depends on Tesseract and has known
  limits around accuracy, reading order, handwriting, poor scans, and document
  structure.
- NARA 9/11 Commission Records: use a publicly reachable NARA MFR PDF as one
  owner-runtime observation.
- NARA copyright and permissions notices: NARA material may often be reusable,
  but NARA does not guarantee every holding is in the public domain; avoid
  committing the PDF binary or raw OCR text.

## Non-goals

- No robust PDF extraction claim.
- No arbitrary-market OCR claim.
- No layout fidelity claim.
- No OCRmyPDF integration.
- No file upload, retrieval, Evidence Ledger, Critic / Noise Gate, final report,
  hosted deployment, or dashboard work.
- No external PDF binaries, download cache, raw extracted text, raw OCR text, or
  local tessdata path committed.

## Implementation Scope

Add a deterministic report gate over one sanitized real-world OCR observation:

```text
source: NARA 9/11 Commission MFR PDF
fixture_id: nara_911_mfr_00282
ocr_engine: pymupdf_get_textpage_ocr
pages_attempted: first 2 pages
committed evidence: metadata, counts, hash, source URLs, expected-term hit count
```

## Data Contract

Committed evidence JSON must include:

```text
phase_marker
previous_gate
claim_boundary
source URL
publisher
collection page URL
rights/source policy URL
HTTP metadata
SHA-256
byte size
page count
OCR pages attempted
native text character count
OCR text character count
expected terms checked
expected term hit booleans
warnings
boundary notes
recommended next gate
```

It must not include:

```text
recognized_text
ocr_sample
raw_text
raw_ocr_text
local PDF path
local tessdata path
```

## Tests

- RED: `tests/test_real_world_ocr_evidence_gate.py` must fail before
  implementation with missing module/report artifacts.
- GREEN: focused OCR evidence gate tests must pass.
- Adjacent proof-gap tests must show the robust-PDF route advances from
  `real_world_ocr_evidence_gate_v0` to
  `real_world_layout_fidelity_evidence_gate_v0`.
- CI staleness check must regenerate the OCR report byte-for-byte.

## Docs To Update

- `README.md`
- `docs/GOAL.md`
- `docs/MASTER-SPEC.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/review/proof-gap-action-surface.md`
- `docs/research/source-assimilation-registry.md`
- `docs/review/real-world-ocr-evidence-gate.md`
- `docs/evaluation/real-world-ocr-evidence-gate-report.md`

## Stop Conditions

Stop if:

- the NARA PDF cannot be downloaded and hashed from a temporary owner-runtime
  location,
- OCR cannot run with local Tesseract language data,
- the implementation would need to commit raw OCR text or source binaries,
- source policy is too unclear to even commit sanitized metadata,
- tests require broad PDF or OCR claims.

## Claim Boundaries

Can claim:

```text
one real-world NARA PDF OCR observation was recorded as sanitized metadata
```

Cannot claim:

```text
robust PDF extraction
arbitrary-market PDF OCR reliability
layout fidelity
external validation
hosted deployment
product completeness
```

## Next Gate If Passed

```text
real_world_layout_fidelity_evidence_gate_v0
```
