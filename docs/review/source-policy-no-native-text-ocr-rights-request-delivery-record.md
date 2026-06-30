# Source-policy No-native-text OCR Rights Request Delivery Record

Phase marker:
`source_policy_no_native_text_ocr_rights_request_delivery_record_v0`.

This gate records a metadata-only delivery record boundary for the preserved
NARA no-native-text OCR route.

## Implemented

- A deterministic rights request delivery record artifact.
- A report builder and check-mode command.
- Delivery route candidates for an owner-runtime request submission.
- Required future delivery evidence fields.
- Missing owner-runtime inputs that block any request-sent or delivery claim.

## Not Implemented

- Request sending.
- Request delivery.
- Delivery channel selection.
- Delivery destination recording.
- Delivery timestamp recording.
- Delivery receipt recording.
- Owner contact identity recording.
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

- NoiseProof has a rights request delivery record that lists delivery route
  candidates and missing owner-runtime evidence before any request-sent claim is
  allowed.

## Cannot Claim

- Rights are cleared.
- A request was sent.
- A request was delivered.
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

This is not request-delivery evidence.

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

`source_policy_no_native_text_ocr_owner_runtime_rights_request_delivery_v0`
