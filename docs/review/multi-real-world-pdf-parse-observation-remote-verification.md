# Multi Real-world PDF Parse Observation Matrix Remote Verification

Status: implemented.

This document records remote GitHub Actions verification for the multi real-world PDF parse observation matrix gate.

## Verified Commit

```text
verified_head_sha -> a37fe32f0f46c5d04008ea425a053966f063950c
commit -> feat: add multi real-world pdf parse observation matrix
```

## GitHub Actions

```text
CI run `27496475781`: success
CI job_id -> 81271370552
External Feedback Screen run `27496475772`: success
External Feedback Screen job_id -> 81271370589
```

The CI run included:

```text
Compile API and local packages
Check multi real-world PDF parse observation report staleness
Run API smoke tests
```

## What This Verifies

This verifies that the committed matrix report is byte-for-byte current with:

```text
examples/pdf-extraction-quality/multi-real-world-pdf-parse-observations.json
docs/evaluation/multi-real-world-pdf-parse-observation-report.md
app.services.multi_real_world_pdf_parse_observation_command
```

It also verifies that the API smoke test suite passed on GitHub Actions for the same commit.

## Boundary

This is remote workflow verification only.

It is not robust PDF extraction evidence.

It is not:

- the owner-runtime PDF downloads themselves
- new PDF parser behavior
- robust PDF extraction evidence
- arbitrary market PDF parsing evidence
- OCR evidence
- table extraction evidence
- hosted deployment evidence
- external reviewer feedback
- product-complete
