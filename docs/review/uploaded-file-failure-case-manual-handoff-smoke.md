# Uploaded File Failure-case Manual Handoff Smoke

Phase marker: uploaded file failure-case manual handoff smoke v0.

## What changed

This gate records a route-level smoke path from uploaded file failure-case draft preview to manual failure-case persistence.

The smoke path is:

1. `POST /documents/upload-failure-case-draft-preview`
2. inspect the returned draft payload
3. manually submit that draft payload to `POST /failure-cases`
4. verify `GET /failure-cases` returns the manually persisted record

## Current behavior

The test proves that an uploaded file question that is blocked or needs revision can produce a draft payload, and that the same payload shape can be manually persisted through the existing failure-case endpoint.

## Boundary

This is manual handoff evidence only.

It is not automatic failure-case creation.

It is not automatic failure detection, not root-cause automation, not customer validation, not hosted deployment evidence, not Braincrew acceptance, and not production readiness.

The system still requires a human to inspect the draft, decide whether it should become a failure case, and submit or edit the payload.

## Why this gate matters

The previous uploaded file failure-case draft preview proved that the upload chain can produce a draft payload without persistence.

Uploaded file failure-case manual handoff smoke v0 proves that the draft can cross the existing manual persistence boundary without inventing a separate upload-specific failure-case table or claiming automation.

This keeps the system honest: the route can help create a failure-case draft, but the human still owns the persistence decision.

## Next product gate

The next product implementation gate should consolidate the reader path rather than expand behavior:

```text
uploaded file proof path index refresh v0
```
