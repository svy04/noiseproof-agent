# Source-policy No-native-text OCR Execution Plan

Phase marker: `source_policy_no_native_text_ocr_execution_plan_v0`.

This review records the bounded execution contract for the preserved NARA
no-native-text route after dependency availability was resolved.

## What Is Planned

- Adapter: `pymupdf_page_get_textpage_ocr`
- Mode: owner-runtime opt-in smoke
- Target: `nara_911_mfr_00282_no_native_text_candidate`
- Planned pages: 1, 2, 3, 4
- Language: `eng`
- DPI: `300`
- Full-page OCR: `true`
- Output policy: sanitized counts and expected-marker hit booleans only

## Evidence

- Packet: `examples/pdf-extraction-quality/source-policy-no-native-text-ocr-execution-plan.json`
- Report: `docs/evaluation/source-policy-no-native-text-ocr-execution-plan-report.md`
- Command: `app.services.source_policy_no_native_text_ocr_execution_plan_command`
- Previous gate: `source_policy_no_native_text_ocr_dependency_resolution_v0`
- Next gate: `source_policy_no_native_text_ocr_execution_smoke_v0`

## Can Claim

- The source-policy no-native-text OCR execution plan is inspectable and
  bounded.

## Cannot Claim

- not OCR execution evidence
- not OCR quality evidence
- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not table extraction benchmark evidence
- not layout fidelity evidence
- not rendered visual fidelity evidence
- not image/chart interpretation evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This gate plans OCR execution only. It does not download PDFs, parse PDFs, run
OCR, evaluate OCR output, extract tables, compare rendered pages, interpret
images or charts, call LLMs, chunk, retrieve, generate Evidence Ledger entries,
run Noise Gate, or build a dashboard.

No local executable paths, tessdata paths, external PDF binaries, download
caches, raw text, raw OCR text, page images, screenshots, or table rows are
committed in the packet, report, or review artifact.
