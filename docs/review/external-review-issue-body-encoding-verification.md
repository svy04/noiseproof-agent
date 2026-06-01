# External Review Issue Body Encoding Verification

Status: external request surface verification artifact.

Phase marker: external review issue body encoding verification v0.

Label: External review issue body encoding verification.

This artifact records that the live public GitHub issue body starts directly with the request heading and does not carry a UTF-8 byte order mark in front of `## Request`. It verifies issue-body readability only. It does not claim that external reviewer feedback has been received.

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
  first_codepoint = [int][char]$json.body[0]
  has_root_review_guide = $json.body.Contains('blob/main/CONTRIBUTING.md')
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
  "comment_count": 1,
  "url": "https://github.com/svy04/noiseproof-agent/issues/1",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_root_review_guide": true,
  "has_link_map": true,
  "has_direct_readme": true
}
```

## What This Proves

The live issue body begins with:

```text
## Request
```

The first codepoint is `35`, which is the `#` character. This confirms that the public request surface is not prefixed by a byte order mark that would make `StartsWith('## Request')` false.

The issue body still points reviewers to:

```text
CONTRIBUTING.md
docs/review/external-reviewer-link-map.md
README.md
docs/review/external-reviewer-brief.md
docs/review/external-reader-proof-path.md
docs/application/portfolio-index.md
docs/review/external-feedback-intake-criteria.md
```

Related root-guide issue-body verification:

```text
docs/review/external-review-issue-body-root-guide-verification.md
```

## Allowed Claim

NoiseProof Agent has a public GitHub issue request body that starts cleanly with the request heading and includes direct reviewer links.

## Boundary

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not hosted deployment evidence.

This does not prove that any reviewer has inspected the repository.

This does not accept any issue comment into the proof path.

The observed `comment_count` is `1`, and the only current comment is owner-authored request/status context.

## Next Gate

The next gate remains:

```text
external reviewer feedback v0
```
