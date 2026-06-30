# Real-world OCR Evidence Gate

Phase marker: real_world_ocr_evidence_gate_v0.

This report records a sanitized PyMuPDF OCR observation for a temporary owner-runtime NARA PDF download.

It is real-world OCR evidence, not robust PDF extraction evidence.

raw OCR text is not committed.

## Gate Result

ocr_gate_status -> passed
previous_gate -> real_world_table_extraction_evidence_gate_v0
observed_fixture_count -> 1
ocr_observed_fixture_count -> 1
total_page_count -> 4
total_ocr_pages_attempted -> 2
total_native_text_char_count -> 0
total_ocr_text_char_count -> 3992
ocr_page_coverage_ratio -> 0.50
expected_terms_found_count -> 4
has_real_world_ocr_evidence -> true
has_layout_fidelity_evidence -> false
can_claim_real_world_ocr_evidence -> true
can_claim_robust_pdf_extraction -> false

## Publishers

- National Archives and Records Administration

## Fixtures

| Fixture | Publisher | Pages | OCR pages | Native chars | OCR chars | Expected terms | SHA-256 |
|---|---|---:|---:|---:|---:|---:|---|
| nara_911_mfr_00282 | National Archives and Records Administration | 4 | 2 | 0 | 3992 | 4 | 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba |

## Passed Checks

- real_world_ocr_observed
- collection_page_visible
- source_policy_visible
- sha256_visible
- external_binaries_not_committed
- raw_ocr_text_not_committed
- tessdata_path_not_committed

## Remaining Blocked Reasons

- layout_fidelity_evidence_missing

## Warnings

- PyMuPDF get_textpage_ocr produced OCR text from a temporary owner-runtime NARA PDF download.
- The PDF binary, download cache, local path, tessdata path, raw extracted text, and raw OCR text are not committed.
- This gate records one real-world OCR observation only; layout fidelity remains missing.
- The NARA rights URL is a general policy source, not a guarantee for every archival record.

## Next Gate

- real_world_layout_fidelity_evidence_gate_v0

## Boundary Notes

- real-world OCR evidence
- single NARA fixture observation
- sanitized OCR metadata only
- no external PDF binaries committed
- no download cache committed
- no raw extracted text committed
- no raw OCR text committed
- not robust PDF extraction evidence
- not arbitrary-market PDF OCR evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a deterministic report over one sanitized owner-runtime OCR observation.

It does not commit external PDF binaries, download caches, local paths, tessdata paths, raw extracted text, or raw OCR text.

It does not prove layout fidelity, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, or robust PDF extraction.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
