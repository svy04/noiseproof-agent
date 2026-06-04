# External Review Issue Body BOM Cleanup

Status: owner-authored issue body edit only.

Phase marker: external review issue body BOM cleanup v0.

## Purpose

This gate cleans up the live public external review issue body after the owner-runtime input discovery refresh introduced a leading UTF-8 byte order mark before `## Request`.

It restores the issue body so the first visible and actual codepoint is `#`.

It is request-surface hygiene only.

It does not close external reviewer feedback v0.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed after cleanup:

```json
{
  "previous_first_codepoint": 65279,
  "updatedAt": "2026-06-04T03:26:20Z",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_owner_input_discovery_refresh": true,
  "has_remote_link": true,
  "comment_count": 1
}
```

## Preserved Links

Owner-runtime input discovery issue body refresh:

```text
docs/review/external-review-issue-body-owner-runtime-input-discovery-refresh.md
```

ClamAV owner-runtime input discovery CI remote verification:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-input-discovery-ci-remote-verification.md
```

## Boundary

This is an owner-authored issue body edit.

This is not external reviewer feedback.

This does not close external reviewer feedback v0.

This is not hosted deployment evidence.

This is not endpoint malicious-detection runtime proof.

This does not include a test signature payload.

This is not real malware scanning.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Gate

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```
