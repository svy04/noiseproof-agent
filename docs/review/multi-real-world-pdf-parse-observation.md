# Multi Real-world PDF Parse Observation Matrix

Status: implemented.

This gate records a bounded owner-runtime observation matrix for three real-world BEA PDFs.

It extends the previous single-PDF parse observation into a small matrix while keeping the same claim boundary:

```text
not robust PDF extraction evidence
```

## Artifact

- Matrix: `examples/pdf-extraction-quality/multi-real-world-pdf-parse-observations.json`
- Report: `docs/evaluation/multi-real-world-pdf-parse-observation-report.md`
- Command: `app.services.multi_real_world_pdf_parse_observation_command`
- Phase marker: `multi_real_world_pdf_parse_observation_matrix_v0`

## Observed Fixtures

| Fixture | Source | Pages | Text chars | Table candidates |
|---|---|---:|---:|---:|
| `bea_nipa_glossary_2019` | BEA NIPA Handbook Glossary | 35 | 92219 | 35 |
| `bea_nipa_chapter_04_2024` | BEA NIPA Handbook Chapter 4 | 30 | 65113 | 8 |
| `bea_open_source_software_innovation_wp_2022_10` | BEA Working Paper 2022-10 | 30 | 60223 | 0 |

Observed aggregate:

```text
observed_fixture_count -> 3
parsed_fixture_count -> 3
total_page_count -> 95
total_text_char_count -> 217555
total_table_candidate_count -> 43
table_extraction_performed -> false
ocr_calls_attempted -> false
binary_files_committed -> false
download_cache_committed -> false
raw_extracted_text_committed -> false
can_claim_robust_pdf_extraction -> false
```

## Source and Rights Boundary

The fixtures come from BEA URLs and cite the BEA public-domain FAQ as the source policy reference:

- `https://www.bea.gov/help/faq/147`

The repository commits only sanitized metadata, hashes, counts, short text samples, warnings, and boundary notes.

No external PDF binaries, download caches, or raw extracted text are committed.

## Why This Exists

The previous gate proved only one real-world PDF parse observation. This gate checks whether the same bounded observation path can be repeated across a small set of BEA PDF shapes:

- glossary-style methodology PDF
- handbook chapter methodology PDF
- research working paper PDF

This improves inspectability of the PDF proof surface without claiming robust extraction.

## Boundary

This is a multi-fixture real-world PDF parse observation matrix only.

It does not prove:

- robust PDF extraction
- arbitrary market PDF parsing reliability
- OCR
- table extraction
- layout fidelity
- hosted deployment
- external reviewer feedback
- product completeness

## Next Gate

```text
multi_real_world_pdf_parse_observation_matrix_remote_verification_v0
```
