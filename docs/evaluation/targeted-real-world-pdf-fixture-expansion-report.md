# Targeted Real-world PDF Fixture Expansion Plan

Phase marker: targeted_real_world_pdf_fixture_expansion_v0.

This report maps each missing PDF matrix cell to a source-policy-reviewed candidate fixture or reviewer route.

It is a fixture expansion plan, not runtime PDF evidence.

It does not add new runtime evidence.

## Gate Result

plan_status -> passed
coverage_status -> planned
previous_gate -> multi_publisher_modality_stratified_pdf_eval_v0
candidate_count -> 6
missing_cell_count -> 6
covered_missing_cell_count -> 6
source_policy_source_count -> 6
downloaded_candidate_count -> 0
runtime_work_performed -> false
pdf_downloads_performed -> false
parser_calls_performed -> false
ocr_calls_performed -> false
table_extraction_calls_performed -> false
llm_calls_performed -> false
binary_files_committed -> false
raw_text_committed -> false
can_claim_robust_pdf_extraction -> false

## Source Policy Sources

- U.S. Bureau of Labor Statistics -> https://www.bls.gov/opub/copyright-information.htm
- BLS Monthly Labor Review -> https://www.bls.gov/opub/mlr/about.htm
- U.S. Energy Information Administration -> https://www.eia.gov/about/copyrights_reuse.php
- U.S. Bureau of Economic Analysis -> https://www.bea.gov/help/faq/147
- National Archives and Records Administration -> https://www.archives.gov/global-pages/privacy.html
- NoiseProof GitHub issue tracker -> https://github.com/svy04/noiseproof-agent/issues/1

## Missing Cell Coverage

- external_reviewer_validation: github_issue_1_external_reviewer_route
- multi_publisher_image_chart_interpretation: bls_beyond_numbers_figures_candidate
- multi_publisher_labeled_layout_ground_truth: bea_wp2022_10_labeled_layout_candidate
- multi_publisher_no_extractable_text_failure: nara_911_mfr_00282_no_native_text_candidate
- multi_publisher_reading_order: bls_mlr_2011_06_reading_order_candidate
- multi_publisher_rendered_visual_fidelity: eia_steo_full_rendered_visual_fidelity_candidate

## Candidate Plan

| Candidate | Missing cell | Publisher | Policy status | Download status | Boundary |
|---|---|---|---|---|---|
| bls_mlr_2011_06_reading_order_candidate | multi_publisher_reading_order | BLS Monthly Labor Review | source_policy_reviewed_metadata_only | not_downloaded | reading-order candidate only, not natural reading-order proof |
| eia_steo_full_rendered_visual_fidelity_candidate | multi_publisher_rendered_visual_fidelity | U.S. Energy Information Administration | source_policy_reviewed_metadata_only | not_downloaded | rendered visual-fidelity planning only, not visual-fidelity evidence |
| bea_wp2022_10_labeled_layout_candidate | multi_publisher_labeled_layout_ground_truth | U.S. Bureau of Economic Analysis | source_policy_reviewed_metadata_only | not_downloaded | local label-candidate planning only, not DocLayNet or PubLayNet evaluation |
| bls_beyond_numbers_figures_candidate | multi_publisher_image_chart_interpretation | U.S. Bureau of Labor Statistics | source_policy_reviewed_metadata_only | not_downloaded | image/chart candidate only, not image or chart interpretation evidence |
| nara_911_mfr_00282_no_native_text_candidate | multi_publisher_no_extractable_text_failure | National Archives and Records Administration | source_policy_reviewed_metadata_only | not_downloaded | no-native-text candidate only, not OCR quality or robust extraction evidence |
| github_issue_1_external_reviewer_route | external_reviewer_validation | NoiseProof GitHub issue tracker | external_review_route_only | not_downloaded | external review route only, not external reviewer feedback |

## Candidate Evaluation Intent

### bls_mlr_2011_06_reading_order_candidate

- source_url: https://www.bls.gov/opub/mlr/2011/06/mlr201106.pdf
- policy_source_url: https://www.bls.gov/opub/mlr/about.htm
- evaluation_intent:
  - multi-column reading-order sanity check
  - human-reviewable expected section sequence sidecar
  - missed or scrambled order failure-case candidate
- acceptance_checks:
  - download and hash only after owner approval
  - commit only metadata and short expected-marker identifiers
  - record reading-order pass/fail separately from text extraction
- stop_conditions:
  - third-party image rights unclear
  - raw article text would need to be committed
  - candidate cannot be hashed from a stable URL

### eia_steo_full_rendered_visual_fidelity_candidate

- source_url: https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf
- policy_source_url: https://www.eia.gov/about/copyrights_reuse.php
- evaluation_intent:
  - rendered page geometry sanity check
  - chart/table page selection for visual review packet
  - visual-fidelity failure-case candidate if rendering differs from source
- acceptance_checks:
  - use sanitized page-level geometry metrics
  - do not commit page images or screenshots without explicit rights review
  - separate rendered visual fidelity from text/table extraction
- stop_conditions:
  - page images would need to be committed
  - visual comparison cannot be summarized without copyrighted content risk
  - stable publication URL cannot be confirmed

### bea_wp2022_10_labeled_layout_candidate

- source_url: https://www.bea.gov/sites/default/files/papers/BEA-WP2022-10.pdf
- policy_source_url: https://www.bea.gov/help/faq/147
- evaluation_intent:
  - small local human label sidecar for layout classes
  - DocLayNet/PubLayNet-style label vocabulary mapping
  - layout-class mismatch failure-case candidate
- acceptance_checks:
  - label only page regions and class names, not raw text
  - record reviewer initials or owner label boundary
  - do not claim benchmark equivalence
- stop_conditions:
  - labeling requires source page image redistribution
  - layout classes cannot be reviewed without raw content
  - candidate collapses layout labels into a robust extraction claim

### bls_beyond_numbers_figures_candidate

- source_url: https://www.bls.gov/opub/btn/volume-4/pdf/people-who-are-not-in-the-labor-force-why-arent-they-working.pdf
- policy_source_url: https://www.bls.gov/opub/copyright-information.htm
- evaluation_intent:
  - figure presence and image-block diagnostics
  - chart interpretation explicitly marked not claimed
  - image/chart unreadability failure-case candidate
- acceptance_checks:
  - record only figure counts and page references
  - keep chart interpretation separate from visual block detection
  - do not commit screenshots or figure crops
- stop_conditions:
  - figure contains third-party copyrighted material
  - claim would require image semantics rather than block diagnostics
  - page image or crop would need to be committed

### nara_911_mfr_00282_no_native_text_candidate

- source_url: https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/t-0148-911MFR-00282.pdf
- policy_source_url: https://www.archives.gov/global-pages/privacy.html
- evaluation_intent:
  - real-world no-native-text failure candidate
  - OCR-disabled no-extractable-text boundary check
  - OCR-enabled path remains separate and opt-in
- acceptance_checks:
  - record native text character count separately from OCR output
  - commit no archival PDF binary and no raw OCR text
  - surface failure_case_candidate when OCR is unavailable or disabled
- stop_conditions:
  - record-specific rights cannot be bounded by general NARA policy
  - raw OCR text would need to be committed
  - test silently falls back to OCR without explicit opt-in

### github_issue_1_external_reviewer_route

- source_url: https://github.com/svy04/noiseproof-agent/issues/1
- policy_source_url: https://github.com/svy04/noiseproof-agent/issues/1
- evaluation_intent:
  - qualifying outside reviewer comment route
  - reviewer can inspect this fixture expansion plan before runtime work
  - external validation remains pending until a non-owner comment exists
- acceptance_checks:
  - outside reviewer is not repository owner
  - comment references at least one proof route or missing cell
  - owner-authored issue text does not close the gate
- stop_conditions:
  - only owner-authored comments exist
  - comment does not mention the artifact or evidence boundary
  - GitHub issue route is unavailable

## Minimum Next Evidence

- owner-approved download/hash for selected candidates only
- per-candidate source-policy URL captured before download
- no external PDF binaries, page images, screenshots, raw extracted text, raw OCR text, or raw table rows committed
- per-cell pass/fail criteria before parser, OCR, table, layout, or visual runtime work

## Blocked Reasons

- runtime_evidence_not_added
- downloads_not_performed
- robust_pdf_claim_still_blocked
- external_reviewer_validation_still_pending

## Warnings

- This plan does not add new runtime evidence.
- Source-policy review is a prerequisite, not permission to commit external PDF binaries or raw extracted content.
- Candidate coverage is planned coverage, not observed extraction coverage.
- External reviewer validation cannot be self-completed.

## Next Gate

- real_world_pdf_fixture_source_policy_download_hash_v0

## Boundary Notes

- source_policy_reviewed_metadata_only
- does not add new runtime evidence
- no PDF downloads performed
- no external PDF binaries committed
- no raw text committed
- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not OCR quality evidence
- not table extraction benchmark evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a source-policy-reviewed metadata plan only.

It does not download PDFs, hash PDFs, parse PDFs, run OCR, extract tables, call LLMs, commit external binaries, commit raw extracted text, commit screenshots, or add new runtime evidence.

It does not prove robust PDF extraction, arbitrary-market PDF parsing reliability, OCR quality, table extraction benchmark quality, layout fidelity, rendered visual fidelity, image/chart interpretation, or external validation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
