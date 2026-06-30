# Source-policy No-native-text OCR Execution Smoke

Phase marker: source_policy_no_native_text_ocr_execution_smoke_v0.

This report records one bounded owner-runtime PyMuPDF/Tesseract OCR smoke for the preserved NARA no-native-text route.

It records execution metadata only.

It is not OCR quality evidence.

It is not robust PDF extraction evidence.

## Gate Result

run_status -> report_written
previous_gate -> source_policy_no_native_text_ocr_execution_plan_v0
run_source -> owner_runtime_pymupdf_ocr_source_policy_smoke
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
publisher -> National Archives and Records Administration
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
byte_size -> 2985436
source_pdf_downloaded_for_smoke -> true
page_count -> 4
planned_pages -> 1, 2, 3, 4
ocr_pages_attempted -> 4
native_text_char_count -> 0
ocr_text_char_count -> 8019
expected_markers_checked -> commission, mfr
expected_markers_found_count -> 2
ocr_engine -> pymupdf_get_textpage_ocr
ocr_language -> eng
ocr_dpi -> 300
full_page_ocr -> true
ocr_execution_performed -> true
ocr_calls_attempted -> true
ocr_quality_eval_performed -> false
binary_files_committed -> false
download_cache_committed -> false
raw_text_committed -> false
raw_ocr_text_committed -> false
page_images_committed -> false
screenshots_committed -> false
tesseract_path_printed -> false
tessdata_path_printed -> false
can_claim_source_policy_no_native_text_ocr_execution_smoke -> true
can_claim_ocr_execution -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false

## Expected Marker Smoke Checks

| Marker | Found |
|---|---:|
| commission | true |
| mfr | true |

## Warnings

- This is one owner-runtime OCR execution smoke over the preserved NARA route.
- Expected-marker hits are smoke checks and are not OCR quality evaluation.
- Raw OCR text is not committed.

## Next Gate

- source_policy_no_native_text_ocr_quality_eval_plan_v0

## Boundary Notes

- source-policy no-native-text OCR execution smoke
- one owner-runtime OCR execution smoke only
- raw OCR text not committed
- no external PDF binaries committed
- no download cache committed
- not OCR quality evidence
- not robust PDF extraction evidence
- not arbitrary-market PDF OCR evidence
- not arbitrary-market PDF parsing evidence
- not table extraction benchmark evidence
- not layout fidelity evidence
- not rendered visual fidelity evidence
- not image/chart interpretation evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a deterministic report over one sanitized owner-runtime OCR execution smoke.

It does not commit external PDF binaries, download caches, local paths, tessdata paths, raw extracted text, raw OCR text, page images, screenshots, or table rows.

Expected-marker hits are smoke checks only and do not prove recognition quality.

It does not prove OCR quality, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, layout fidelity, rendered visual fidelity, image/chart interpretation, or robust PDF extraction.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
