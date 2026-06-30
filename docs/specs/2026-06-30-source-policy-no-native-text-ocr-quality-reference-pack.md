# Source-policy No-native-text OCR Quality Reference Pack Spec

status: draft_for_tdd

date: 2026-06-30

target_gate: source_policy_no_native_text_ocr_quality_reference_pack_v0

previous_gate: source_policy_no_native_text_ocr_quality_eval_plan_v0

recommended_next_gate_after_this_spec:

```text
source_policy_no_native_text_ocr_marker_proxy_eval_v0
```

## Current Repo State

- `source_policy_no_native_text_ocr_quality_eval_plan_v0` is accepted on main.
- The accepted plan says OCR quality needs reference inputs before scoring.
- The previous execution smoke has two marker hits and `ocr_text_char_count -> 8019`.
- No page-level reference transcript is committed.
- No OCR quality evaluation, CER, WER, robust PDF extraction, or arbitrary-market
  PDF parsing reliability has been proven.

## Sources To Absorb

- OCR-D evaluation: OCR quality requires OCR output compared against
  representative ground truth/manual transcription. CER and WER are
  edit-distance metrics over GT/reference and OCR text.
- JiWER: WER/CER-style tooling is a future reusable metric surface, but it
  needs reference/hypothesis strings and is not introduced in this gate.
- National Archives privacy/use policy: NARA records have source-use caveats;
  not all materials on archives.gov are public-domain by default. Reference
  packs must preserve source policy and avoid copying raw record content.
- Existing quality eval plan: marker hits and character counts are proxy checks
  only, not OCR quality scores.

## Non-goals

- Do not run OCR.
- Do not evaluate OCR quality.
- Do not compute CER, WER, precision, recall, accuracy, or any score.
- Do not add JiWER as a dependency.
- Do not commit source PDFs, download caches, local paths, tessdata paths,
  raw native text, raw OCR text, page-level transcripts, page images,
  screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final
  reports, dashboard, DB persistence, or hosted deployment.
- Do not call LLMs.
- Do not claim robust PDF extraction, arbitrary-market OCR reliability,
  OCR benchmark quality, external reviewer feedback, or product completeness.

## Implementation Scope

- Add a deterministic reference-pack module.
- Load the accepted quality-eval plan.
- Produce a sanitized reference pack that records:
  - source policy URL and source hash binding
  - page mapping for the preserved four-page NARA candidate
  - normalization rules for future marker/proxy checks
  - accepted marker-anchor references only
  - that no full reference transcript is available
  - which metric classes are supported and blocked
  - public claim boundaries and next gate
- Add a deterministic report builder and CLI check mode.
- Update reviewer/public proof surfaces and CI staleness checks.

## Data Or API Contract

Committed reference pack artifact:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-quality-reference-pack.json
```

Committed report:

```text
docs/evaluation/source-policy-no-native-text-ocr-quality-reference-pack-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_quality_reference_pack_v0
previous_gate -> source_policy_no_native_text_ocr_quality_eval_plan_v0
reference_pack_status -> marker_anchor_reference_pack
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
source_policy_url -> https://www.archives.gov/global-pages/privacy.html
page_count -> 4
page_mapping_available -> true
reference_unit_type -> marker_anchor
accepted_marker_anchor_count -> 2
full_reference_transcript_available -> false
supports_marker_proxy_eval -> true
supports_cer -> false
supports_wer -> false
quality_eval_performed -> false
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
can_claim_reference_pack -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_marker_proxy_eval_v0
```

Required accepted marker anchors:

```text
commission
mfr
```

Required normalization rules:

```text
unicode_normalization -> NFC
casefold -> true
strip_outer_whitespace -> true
collapse_internal_whitespace -> true
punctuation_policy -> preserve_for_future_transcript_metrics
```

## Tests

- `apps/api/tests/test_source_policy_no_native_text_ocr_quality_reference_pack.py`
- RED must fail because the new reference-pack module does not exist.
- GREEN must pass committed reference pack/report checks, command check mode,
  rejection tests, artifact safety checks, proof-surface links, proof-gap
  registry updates, and CI staleness checks.

## Docs To Update

- `README.md`
- `docs/MASTER-SPEC.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/review/external-reader-proof-path.md`
- `docs/review/proof-gap-action-surface.md`
- `docs/research/source-assimilation-registry.md`
- `apps/api/app/services/proof_gap_registry.py`
- `.github/workflows/ci.yml`

## Stop Conditions

- Stop if the implementation tries to compute OCR quality without a full
  reference transcript.
- Stop if marker anchors are treated as CER/WER support.
- Stop if any artifact would require committing raw OCR text, raw reference
  text, source PDFs, page images, screenshots, local paths, or tessdata paths.
- Stop if the implementation drifts into retrieval, Evidence Ledger, Critic /
  Noise Gate, final report generation, dashboard, DB persistence, or hosted
  deployment.

## Claim Boundaries

Implemented:

- A sanitized marker-anchor reference pack for the preserved NARA no-native-text
  OCR route.

Not implemented:

- Full ground-truth transcript, OCR quality scoring, CER/WER computation,
  robust PDF extraction, arbitrary-market OCR reliability, retrieval, Evidence
  Ledger, Critic / Noise Gate, final report generation, dashboard, hosted
  deployment, external reviewer feedback.

Can claim:

- The source-policy no-native-text OCR route now has a bounded marker-anchor
  reference pack for a future proxy evaluation.

Cannot claim:

- OCR output is correct, OCR quality is benchmarked, marker anchors prove
  recognition quality, CER/WER can be computed, robust PDF extraction works,
  arbitrary-market PDF parsing is reliable, or the product is complete.

## Next Gate If Passed

```text
source_policy_no_native_text_ocr_marker_proxy_eval_v0
```
