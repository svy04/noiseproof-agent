import re

from packages.ingestion.types import EvidenceLedgerEntry, NoiseGateCheck, NoiseGateResult


FALLBACK_MESSAGE = (
    "현재 근거만으로는 결론을 내릴 수 없습니다. 가능한 해석은 다음과 같고, "
    "추가로 확인해야 할 데이터는 다음과 같습니다."
)
BUY_SELL_PATTERN = re.compile(
    r"\b(buy|sell|hold|short|long|target price|price target|invest|investment advice)\b",
    re.IGNORECASE,
)
OVERCONFIDENT_PATTERN = re.compile(
    r"\b(proves?|guarantees?|certainly|definitely|must|will|no doubt|undeniable)\b",
    re.IGNORECASE,
)


def run_noise_gate(
    question: str,
    entries: list[EvidenceLedgerEntry],
    draft_claims: list[str] | None = None,
) -> NoiseGateResult:
    normalized_question = " ".join(question.strip().split())
    draft_claims = draft_claims or []
    warnings = [
        "Noise Gate Preview does not generate a report or call an LLM.",
        "It only checks whether current ledger evidence can pass into a future report stage.",
    ]

    blocked_claims = _claims_with_status(entries, {"blocked", "unsupported"})
    downgraded_claims = sorted(
        set(
            _claims_with_status(entries, {"contradicted"})
            + _claims_missing_recency(entries)
            + _high_confidence_claims_with_too_few_sources(entries)
        )
    )
    allowed_claims = sorted(
        {
            entry.claim
            for entry in entries
            if entry.status == "supported"
            and entry.claim not in blocked_claims
            and entry.claim not in downgraded_claims
        }
    )

    checks = [
        _check_every_strong_claim_has_evidence(entries),
        _check_unsupported_claim_blocking(blocked_claims),
        _check_contradictions(entries),
        _check_source_recency(entries),
        _check_high_confidence_sources(entries),
        _check_limitations(entries),
        _check_trading_advice(normalized_question, draft_claims),
        _check_overconfidence(draft_claims),
    ]

    required_revisions = _required_revisions(checks)
    decision = _decision(checks)
    return NoiseGateResult(
        question=normalized_question,
        decision=decision,
        final_response_allowed=decision == "pass",
        checks=checks,
        blocked_claims=blocked_claims,
        downgraded_claims=downgraded_claims,
        allowed_claims=allowed_claims if decision == "pass" else [],
        required_revisions=required_revisions,
        fallback_message=FALLBACK_MESSAGE if decision in {"blocked", "needs_revision"} else None,
        warnings=warnings,
    )


def _check_every_strong_claim_has_evidence(entries: list[EvidenceLedgerEntry]) -> NoiseGateCheck:
    unsupported = [
        entry.claim
        for entry in entries
        if entry.status in {"blocked", "unsupported"} or not entry.source_id or not entry.evidence_span
    ]
    if unsupported:
        return NoiseGateCheck(
            name="every_strong_claim_has_evidence",
            status="fail",
            message=f"{len(set(unsupported))} claim(s) lack source-linked evidence.",
        )
    return NoiseGateCheck(
        name="every_strong_claim_has_evidence",
        status="pass",
        message="Every current ledger claim has source-linked evidence.",
    )


def _check_unsupported_claim_blocking(blocked_claims: list[str]) -> NoiseGateCheck:
    if blocked_claims:
        return NoiseGateCheck(
            name="unsupported_claim_blocking",
            status="block",
            message="Unsupported or blocked ledger claims cannot pass into report generation.",
        )
    return NoiseGateCheck(
        name="unsupported_claim_blocking",
        status="pass",
        message="No unsupported or blocked ledger claims were found.",
    )


def _check_contradictions(entries: list[EvidenceLedgerEntry]) -> NoiseGateCheck:
    contradictions = [
        entry.claim
        for entry in entries
        if entry.status == "contradicted" or entry.contradicting_source_ids
    ]
    if contradictions:
        return NoiseGateCheck(
            name="contradictions_are_surfaced",
            status="fail",
            message="Contradictions are present and must be resolved or explicitly framed.",
        )
    return NoiseGateCheck(
        name="contradictions_are_surfaced",
        status="pass",
        message="No contradiction entries are present.",
    )


def _check_source_recency(entries: list[EvidenceLedgerEntry]) -> NoiseGateCheck:
    missing_recency = [
        entry.claim
        for entry in entries
        if entry.status in {"supported", "weakly_supported", "contradicted"} and not entry.source_date
    ]
    if missing_recency:
        return NoiseGateCheck(
            name="source_recency_visible",
            status="fail",
            message="One or more source-linked claims are missing source_date.",
        )
    return NoiseGateCheck(
        name="source_recency_visible",
        status="pass",
        message="Source recency is visible for source-linked claims.",
    )


def _check_high_confidence_sources(entries: list[EvidenceLedgerEntry]) -> NoiseGateCheck:
    weak_high_confidence = _high_confidence_claims_with_too_few_sources(entries)
    if weak_high_confidence:
        return NoiseGateCheck(
            name="high_confidence_has_two_sources",
            status="fail",
            message="High-confidence claims need at least two distinct source ids.",
        )
    return NoiseGateCheck(
        name="high_confidence_has_two_sources",
        status="pass",
        message="High-confidence source-count rule is satisfied or not applicable.",
    )


def _check_limitations(entries: list[EvidenceLedgerEntry]) -> NoiseGateCheck:
    missing = [entry.claim for entry in entries if not entry.limitation.strip()]
    if missing:
        return NoiseGateCheck(
            name="limitations_explicit",
            status="fail",
            message="One or more ledger entries are missing explicit limitations.",
        )
    return NoiseGateCheck(
        name="limitations_explicit",
        status="pass",
        message="Ledger entries include explicit limitations.",
    )


def _check_trading_advice(question: str, draft_claims: list[str]) -> NoiseGateCheck:
    combined = " ".join([question, *draft_claims])
    if BUY_SELL_PATTERN.search(combined):
        return NoiseGateCheck(
            name="trading_advice_drift",
            status="block",
            message="Question or draft drifts into buy/sell, target price, or investment advice.",
        )
    return NoiseGateCheck(
        name="trading_advice_drift",
        status="pass",
        message="No trading-advice drift detected.",
    )


def _check_overconfidence(draft_claims: list[str]) -> NoiseGateCheck:
    if any(OVERCONFIDENT_PATTERN.search(claim) for claim in draft_claims):
        return NoiseGateCheck(
            name="overconfident_language",
            status="fail",
            message="Draft contains overconfident language that must be bounded.",
        )
    return NoiseGateCheck(
        name="overconfident_language",
        status="pass",
        message="No overconfident draft language detected.",
    )


def _required_revisions(checks: list[NoiseGateCheck]) -> list[str]:
    revisions: list[str] = []
    for check in checks:
        if check.status == "pass":
            continue
        if check.name == "trading_advice_drift":
            revisions.append("Reframe buy/sell or target-price intent into evidence-based market intelligence.")
        elif check.name == "overconfident_language":
            revisions.append("Replace overconfident draft language with claim-bounded wording.")
        elif check.name == "contradictions_are_surfaced":
            revisions.append("Surface contradictions before making or strengthening the claim.")
        elif check.name == "source_recency_visible":
            revisions.append("Add source_date or mark source recency as unknown before report generation.")
        elif check.name == "high_confidence_has_two_sources":
            revisions.append("Downgrade confidence or add a second distinct source for high-confidence claims.")
        elif check.name == "unsupported_claim_blocking":
            revisions.append("Remove or block unsupported claims before report generation.")
        elif check.name == "every_strong_claim_has_evidence":
            revisions.append("Attach source id and evidence span to every strong claim.")
        elif check.name == "limitations_explicit":
            revisions.append("Add explicit limitations to each ledger entry.")
    return revisions


def _decision(checks: list[NoiseGateCheck]) -> str:
    if any(check.status == "block" for check in checks):
        return "blocked"
    if any(check.status == "fail" for check in checks):
        return "needs_revision"
    return "pass"


def _claims_with_status(entries: list[EvidenceLedgerEntry], statuses: set[str]) -> list[str]:
    return sorted({entry.claim for entry in entries if entry.status in statuses})


def _claims_missing_recency(entries: list[EvidenceLedgerEntry]) -> list[str]:
    return sorted(
        {
            entry.claim
            for entry in entries
            if entry.status in {"supported", "weakly_supported", "contradicted"} and not entry.source_date
        }
    )


def _high_confidence_claims_with_too_few_sources(entries: list[EvidenceLedgerEntry]) -> list[str]:
    claims: set[str] = set()
    for entry in entries:
        if entry.confidence != "high":
            continue
        source_count = len(
            {
                candidate.source_id
                for candidate in entries
                if candidate.claim == entry.claim and candidate.source_id
            }
        )
        if source_count < 2:
            claims.add(entry.claim)
    return sorted(claims)
