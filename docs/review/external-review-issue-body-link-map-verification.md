# External Review Issue Body Link-map Verification

Status: external request surface verification artifact.

Phase marker: external review issue body link-map verification v0.

Label: External review issue body link-map verification.

This artifact records that the live public GitHub issue body points reviewers to the direct link map and shortest proof path. It verifies the request surface only. It does not claim that external reviewer feedback has been received.

## Verified Surface

Public request issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Verification Command

```powershell
$json = gh issue view 1 --repo svy04/noiseproof-agent --json number,state,title,body,comments,url | ConvertFrom-Json
[PSCustomObject]@{
  number = $json.number
  state = $json.state
  title = $json.title
  comment_count = $json.comments.Count
  url = $json.url
  starts_with_request = $json.body.StartsWith('## Request')
  has_link_map = $json.body.Contains('external-reviewer-link-map.md')
  has_direct_readme = $json.body.Contains('blob/main/README.md')
} | ConvertTo-Json -Compress
```

## Observed Result

```json
{
  "number": 1,
  "state": "OPEN",
  "title": "External review request: NoiseProof Agent proof path",
  "comment_count": 0,
  "url": "https://github.com/svy04/noiseproof-agent/issues/1",
  "starts_with_request": true,
  "has_link_map": true,
  "has_direct_readme": true
}
```

## What This Proves

The public issue request body is live and points reviewers to:

```text
docs/review/external-reviewer-link-map.md
README.md
docs/review/external-reviewer-brief.md
docs/review/external-reader-proof-path.md
docs/application/portfolio-index.md
docs/review/external-feedback-intake-criteria.md
```

The issue body still preserves the boundary that self-authored issue edits or comments do not close the `external reviewer feedback v0` gate.

## Allowed Claim

NoiseProof Agent has a public GitHub issue request body that includes direct links to the reviewer link map and README.

## Boundary

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not hosted deployment evidence.

This does not prove that any reviewer has inspected the repository.

This does not accept any issue comment into the proof path.

The observed `comment_count` is `0`.

## Next Gate

The next gate remains:

```text
external reviewer feedback v0
```
