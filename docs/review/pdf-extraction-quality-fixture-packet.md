# PDF Extraction Quality Fixture Packet

Phase marker: PDF extraction quality fixture packet v0.

Status: implemented as a fixture packet and quality gate definition only.

Purpose: create a small inspectable packet that future PDF extraction work must satisfy before this repository can claim robust PDF extraction. This packet follows the Phase 702 source-first strategy review and turns it into fixture roles, expected behaviors, warning expectations, and quality metrics.

Fixture manifest: `examples/pdf-extraction-quality/fixture-manifest.json`.

## Why this exists

The current PDF parser can extract embedded digital text with PyMuPDF, but it still records:

```text
robust_pdf_extraction: false
table_extraction_performed: false
```

The next risk is not that the code is missing a parser. The next risk is claiming "robust PDF extraction" without a fixture set that proves which PDF situations are supported, weak, or unsupported.

## Fixture roles

The fixture manifest covers these roles:

- born-digital text PDF
- table-heavy report
- scanned image PDF
- encrypted PDF
- image-heavy PDF
- multi-column layout PDF
- no-extractable-text PDF

The packet intentionally stores fixture definitions and expected outcomes, not binary PDF files. Binary fixture evidence should be added later only with provenance, redistribution rights, and expected-span checks.

## Quality metrics

Future extraction implementations should report these metrics before changing public wording:

- page_coverage
- character_coverage
- expected_span_recall
- table_row_coverage
- ocr_page_coverage
- warning_correctness
- failure_case_candidate_correctness

The metric contract is small on purpose. It should make unsupported situations visible before making the parser more ambitious.

## Required future evaluation behavior

For each fixture role, future evaluation should record:

- selected parser or adapter
- text extraction strategy
- whether OCR ran
- whether table extraction ran
- extracted page count
- empty page count
- expected span hits and misses
- warnings emitted
- failure-case candidate emitted, if any

The first implementation that uses this packet should be allowed to fail many cases. The point is to make failures explicit, not to hide them behind a fluent extraction result.

## Boundary

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not binary PDF fixture evidence.

This is not hosted deployment evidence.

This is not product-complete.

Next recommended gate: implement a deterministic PDF extraction quality evaluator over this manifest, still without claiming robust extraction.
