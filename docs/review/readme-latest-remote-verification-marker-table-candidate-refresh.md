# README Latest Remote Verification Marker Table-candidate Refresh

Status: implemented.

Phase marker: readme latest remote verification marker table-candidate refresh v0.

## Purpose

Keep the first-screen README latest remote verification marker aligned with the current table-candidate proof route.

The README previously pointed that marker to an older Compose service-name runbook refresh. The current first-screen proof route now points to the uploaded PDF table-candidate downstream runtime proof, so the remote verification marker should point to the README table-candidate proof route refresh verification.

## Current Marker

The README first-screen marker now says:

```text
Latest remote verification state: the README table-candidate proof route refresh was remotely checked by CI run `27040299642` and External Feedback Screen run `27040299666`; see `docs/review/readme-current-proof-route-table-candidate-refresh-remote-verification.md`. This is workflow evidence only, not external feedback or runtime product proof.
```

Linked verification:

```text
docs/review/readme-current-proof-route-table-candidate-refresh-remote-verification.md
```

## Preserved Boundary

This is README marker clarity only.

This is not a new runtime smoke.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not runtime product proof.

This is not customer validation.

This is not Braincrew acceptance.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
