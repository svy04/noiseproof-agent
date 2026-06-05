# Failure-case Workflow Review Queue Dashboard Surfacing

Status: implemented.

Phase marker: failure-case workflow review queue dashboard surfacing v0.

## Goal

Surface the failure-case workflow review queue inside the plain operations dashboard without changing persistence behavior.

The rendered surface is:

```text
GET /ops/dashboard
```

The section title is:

```text
Failure-case Workflow Review Queue
```

## Implemented Surface

The dashboard now shows:

- `pending_review_count`
- `linked_failure_case_count`
- `read_model_only_no_automatic_failure_case_creation`
- workflow detail links
- workflow question
- workflow status
- review status: `needs_failure_case_review` or `failure_case_linked`
- stage
- error type
- linked failure-case count
- linked failure-case ids
- `POST /failure-cases/draft-preview` cue with a reminder that draft preview requires an explicit POST request

Implementation code:

```text
apps/api/app/routes/ops.py
apps/api/app/services/ops_dashboard.py
render_ops_dashboard
build_failure_case_workflow_review_queue
```

The dashboard route reuses `build_failure_case_workflow_review_queue` instead of duplicating queue logic inside the HTML renderer.

## Observed Route Test

The route-level test creates:

- one failed workflow with no linked failure case
- one failed workflow with one manual linked failure case
- one completed workflow
- one manually persisted failure case

Then it verifies `GET /ops/dashboard` contains:

```text
Failure-case Workflow Review Queue
pending_review_count
linked_failure_case_count
needs_failure_case_review
failure_case_linked
workflow_execute_preview
RuntimeError
POST /failure-cases/draft-preview
draft preview requires an explicit POST request
read_model_only_no_automatic_failure_case_creation
does not create failure_cases
```

It also verifies that `GET /failure-cases` still returns only the one manually persisted failure case after dashboard rendering.

## Boundary

This is plain dashboard surfacing only.

It is:

- not automatic failure-case creation
- not root-cause automation
- not complete workflow failure causality
- not a schema change
- not a migration
- not hosted deployment evidence
- not external reviewer feedback
- not a polished dashboard UI

The dashboard may point a human reviewer toward the draft-preview POST boundary, but it does not render that POST-only route as a clickable GET link, confirm the draft, or persist any `failure_cases` row.

## Next Gate

The next bounded gate can be a fresh migrated DB dashboard smoke for this queue section, external reviewer feedback if a qualifying outside comment exists, or another source-first product gate selected from `docs/GOAL.md`.
