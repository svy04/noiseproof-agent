# External Feedback Acceptance Draft CLI

Status: local acceptance-draft helper.

Phase marker: external feedback acceptance draft cli v0.

Label: External feedback acceptance draft CLI.

## Purpose

This artifact documents the local helper that converts an `external-feedback-screen.json` screening artifact into draft manual acceptance records.

It exists to make the future handoff from `candidate_found_manual_review_required` to a human acceptance decision inspectable.

## Command

Run this after downloading or producing an `external-feedback-screen.json` artifact:

```bash
python -m packages.review.external_feedback_acceptance_cli \
  --input external-feedback-screen.json
```

The GitHub Actions screening workflow also writes this output to:

```text
external-feedback-acceptance-draft.json
```

Remote verification:

```text
docs/review/external-feedback-acceptance-draft-workflow-verification.md
```

## Expected candidate output shape

```json
{
  "status": "manual_acceptance_required",
  "draft_count": 1,
  "next_gate": "external reviewer feedback v0",
  "does_not_close_gate": true,
  "drafts": [
    {
      "manual_acceptance_decision": "pending",
      "accepted_as_external_reviewer_feedback": false,
      "required_next_actions": [
        "manual_acceptance_required",
        "compare_against_external_feedback_intake_criteria",
        "fill_external_feedback_acceptance_template"
      ]
    }
  ]
}
```

## Boundary

This CLI does not close the gate.

It is not external reviewer feedback.

It is not a customer validation signal.

It is not Braincrew acceptance.

It must not automatically accept any comment into the proof path.

The output is a draft only. A human must compare the candidate comment against `docs/review/external-feedback-intake-criteria.md` and then fill `docs/review/external-feedback-acceptance-template.md` if the comment qualifies.

## Next gate

```text
external reviewer feedback v0
```
