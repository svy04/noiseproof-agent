import re

from packages.ingestion.types import (
    EvidenceLedger,
    EvidenceLedgerCandidate,
    EvidenceLedgerEntry,
    EvidenceLedgerSummary,
)


BUY_SELL_PATTERN = re.compile(
    r"\b(buy|sell|hold|short|long|target price|price target|invest|investment advice)\b",
    re.IGNORECASE,
)
CONTRADICTION_PATTERN = re.compile(
    r"\b(decline[ds]?|declined|fall|fell|drop|dropped|decrease[ds]?|no growth|not grown|"
    r"contradict|den(y|ies|ied)|weak|감소|하락|부인|반박)\b",
    re.IGNORECASE,
)


def create_evidence_ledger(
    question: str,
    candidates: list[EvidenceLedgerCandidate],
) -> EvidenceLedger:
    normalized_question = " ".join(question.strip().split())
    warnings = [
        "Evidence Ledger Preview does not judge final truth or generate a final report.",
        "Entries are derived from retrieval candidates and must still pass a future Critic / Noise Gate.",
    ]

    if BUY_SELL_PATTERN.search(normalized_question):
        warnings.append("NoiseProof does not provide buy/sell recommendations or financial advice.")
        entry = EvidenceLedgerEntry(
            claim=_claim_from_question(normalized_question),
            source_id=None,
            source_type=None,
            source_date=None,
            evidence_span="",
            confidence="none",
            limitation="Question drifts into buy/sell or financial-advice intent; evidence ledger blocks answer generation.",
            contradicting_source_ids=[],
            status="blocked",
            role="user_intent_check",
        )
        return _ledger(normalized_question, [entry], warnings)

    if not candidates:
        entry = EvidenceLedgerEntry(
            claim=_claim_from_question(normalized_question),
            source_id=None,
            source_type=None,
            source_date=None,
            evidence_span="",
            confidence="none",
            limitation="No retrieval candidates were provided, so no claim can be supported.",
            contradicting_source_ids=[],
            status="blocked",
            role="missing_data_signal",
        )
        return _ledger(normalized_question, [entry], warnings)

    support_ids = [
        candidate.source_id
        for candidate in candidates
        if candidate.source_id and not _is_contradictory(candidate.text)
    ]
    contradiction_ids = [
        candidate.source_id for candidate in candidates if candidate.source_id and _is_contradictory(candidate.text)
    ]

    entries = [
        _entry_from_candidate(
            question=normalized_question,
            candidate=candidate,
            contradicting_source_ids=(
                support_ids if _is_contradictory(candidate.text) else contradiction_ids
            ),
        )
        for candidate in candidates
    ]
    return _ledger(normalized_question, entries, warnings)


def _entry_from_candidate(
    question: str,
    candidate: EvidenceLedgerCandidate,
    contradicting_source_ids: list[str],
) -> EvidenceLedgerEntry:
    status = _status_for_candidate(candidate)
    return EvidenceLedgerEntry(
        claim=_claim_from_question(question),
        source_id=candidate.source_id,
        source_type=candidate.source_type,
        source_date=_source_date(candidate),
        evidence_span=_evidence_span(candidate.text, candidate.matched_terms),
        confidence=_confidence_for_candidate(candidate, status),
        limitation=_limitation_for_candidate(status),
        contradicting_source_ids=contradicting_source_ids,
        status=status,
        matched_terms=sorted(set(candidate.matched_terms)),
        role="contradiction" if status == "contradicted" else "direct_support",
        metadata_json=dict(candidate.metadata),
    )


def _status_for_candidate(candidate: EvidenceLedgerCandidate) -> str:
    if not candidate.source_id:
        return "unsupported"
    if _is_contradictory(candidate.text):
        return "contradicted"
    if candidate.score >= 0.6:
        return "supported"
    if candidate.score > 0:
        return "weakly_supported"
    return "unsupported"


def _confidence_for_candidate(candidate: EvidenceLedgerCandidate, status: str) -> str:
    if status in {"blocked", "unsupported"}:
        return "none"
    if status == "contradicted":
        return "low"
    if candidate.score >= 0.75:
        return "medium"
    return "low"


def _limitation_for_candidate(status: str) -> str:
    if status == "supported":
        return "Supported by a lexical retrieval candidate; not yet validated by a Critic / Noise Gate."
    if status == "weakly_supported":
        return "Only weak lexical overlap was found; more source roles are needed before a stronger claim."
    if status == "contradicted":
        return "Candidate contains contradiction language and must be surfaced before any report claim."
    return "Candidate lacks enough source-linked support to become evidence."


def _evidence_span(text: str, matched_terms: list[str]) -> str:
    normalized_text = " ".join(text.strip().split())
    if not normalized_text:
        return ""

    sentences = re.split(r"(?<=[.!?])\s+", normalized_text)
    normalized_terms = {term.lower() for term in matched_terms}
    for sentence in sentences:
        lower_sentence = sentence.lower()
        if any(term in lower_sentence for term in normalized_terms):
            return sentence[:280]
    return normalized_text[:280]


def _source_date(candidate: EvidenceLedgerCandidate) -> str | None:
    value = candidate.metadata.get("source_date") or candidate.metadata.get("date")
    return str(value) if value is not None else None


def _is_contradictory(text: str) -> bool:
    return bool(CONTRADICTION_PATTERN.search(text or ""))


def _claim_from_question(question: str) -> str:
    return question.rstrip("?.!")


def _ledger(question: str, entries: list[EvidenceLedgerEntry], warnings: list[str]) -> EvidenceLedger:
    return EvidenceLedger(
        question=question,
        entries=entries,
        summary=EvidenceLedgerSummary(
            supported_count=sum(entry.status == "supported" for entry in entries),
            weakly_supported_count=sum(entry.status == "weakly_supported" for entry in entries),
            contradicted_count=sum(entry.status == "contradicted" for entry in entries),
            unsupported_count=sum(entry.status == "unsupported" for entry in entries),
            blocked_count=sum(entry.status == "blocked" for entry in entries),
            source_count=len({entry.source_id for entry in entries if entry.source_id}),
        ),
        warnings=warnings,
    )
