# Source-policy No-native-text OCR Owner Rights Decision Record

Phase marker:
`source_policy_no_native_text_ocr_owner_rights_decision_record_v0`.

This gate records a repository-owner hold decision for the preserved NARA
no-native-text OCR route.

## Implemented

- A deterministic owner rights decision record.
- A report builder and check-mode command.
- A conservative hold decision that blocks transcript collection, transcript
  text commits, transcript hash commits, CER/WER, OCR quality, and robust-PDF
  claims until source-rights response evidence exists.

## Not Implemented

- Request sending.
- Rights response receipt.
- Rights clearance.
- Source-rights owner approval completion.
- Source-rights owner decision receipt.
- Transcript collection.
- Reference transcript availability.
- Transcript hash commitment.
- OCR quality scoring.
- CER or WER computation.
- Robust PDF extraction.
- External reviewer feedback.

## Can Claim

- NoiseProof has an owner decision record that keeps transcript text and hashes
  out of the repository until source-rights response evidence exists.

## Cannot Claim

- Rights are cleared.
- A request was sent.
- A response was received.
- Source-rights owner approval is recorded.
- A source-rights owner decision exists.
- A reference transcript exists.
- Transcript collection has happened.
- OCR output is correct.
- OCR quality has been benchmarked.
- CER or WER can be computed.
- Robust PDF extraction works.
- The product is complete.

## Boundary

This is not rights clearance evidence.

This is not request-sent evidence.

This is not source-rights approval evidence.

This is not source-rights owner decision evidence.

This is not transcript collection evidence.

This is not reference transcript availability.

This is not OCR quality evidence.

This is not CER/WER support.

This is not robust PDF extraction evidence.

This is not arbitrary-market PDF parsing evidence.

This is not rendered visual fidelity evidence.

This is not image/chart interpretation evidence.

This is not external reviewer feedback.

This is not product-complete.

## Next Gate

`source_policy_no_native_text_ocr_rights_request_delivery_record_v0`
