import re

from packages.ingestion.types import CollectionPlan


NUMBER_PATTERN = re.compile(r"\d|%|percent|revenue|sales|growth|grew|margin|cost|price|volume", re.IGNORECASE)
BUY_SELL_PATTERN = re.compile(
    r"\b(buy|sell|hold|short|long|target price|price target|invest|investment advice)\b",
    re.IGNORECASE,
)
SOURCE_QUALITY_PATTERN = re.compile(
    r"\b(anonymous|rumou?r|source|reliable|trust|credible|leak|unverified)\b",
    re.IGNORECASE,
)


def create_collection_plan(question: str) -> CollectionPlan:
    normalized_question = " ".join(question.strip().split())
    lower_question = normalized_question.lower()

    required_roles = [
        "direct_support",
        "contradiction",
        "timeline_anchor",
        "missing_data_signal",
    ]
    source_types = ["news", "financial_report", "company_statement", "analyst_note"]
    possible_claims = _possible_claims(normalized_question)
    known_risks = [
        "same-source repeated narrative may look like independent confirmation",
        "marketing narrative may outrun operational evidence",
    ]
    stop_conditions = [
        "only same-source repeated narrative found",
        "no contradiction or missing-data signal found",
    ]
    warnings = [
        "Collection Plan Preview does not judge truth or retrieve evidence.",
        "This plan only defines information roles needed before retrieval.",
    ]

    if _is_underspecified(lower_question):
        _add_roles(required_roles, ["definition_anchor", "scope_boundary", "missing_data_signal"])
        possible_claims = [
            "The question is too underspecified to create a claim without entity, timeframe, and scope."
        ]
        source_types = ["definition_source", "company_statement", "domain_reference"]
        known_risks.append("underspecified questions can make unrelated information look meaningful")
        stop_conditions.append("question is underspecified until entity, timeframe, and scope are clarified")
        warnings.append("question appears underspecified; clarify entity, timeframe, and decision context")

    if BUY_SELL_PATTERN.search(lower_question):
        _add_roles(required_roles, ["user_intent_check", "scope_boundary"])
        known_risks.append("trading advice drift can turn market intelligence into buy/sell guidance")
        stop_conditions.append("question drifts into buy/sell advice or target price recommendation")
        warnings.append("NoiseProof does not provide buy/sell recommendations or financial advice")

    if NUMBER_PATTERN.search(lower_question):
        _add_roles(required_roles, ["quantitative_anchor"])
        _add_sources(source_types, ["price_or_volume_csv", "financial_report"])
        stop_conditions.append("no quantitative anchor found for numeric claim")

    if SOURCE_QUALITY_PATTERN.search(lower_question):
        _add_roles(required_roles, ["source_quality_check"])
        _add_sources(source_types, ["original_source", "independent_report"])
        known_risks.append("source quality may be weak, anonymous, circular, or unverified")
        stop_conditions.append("source quality cannot be checked against an original or independent source")

    information_need = _information_need(normalized_question, required_roles)
    minimum_evidence_needed = _minimum_evidence(required_roles)

    return CollectionPlan(
        question=normalized_question,
        information_need=information_need,
        possible_claims=possible_claims,
        required_roles=required_roles,
        source_types_to_check=source_types,
        minimum_evidence_needed=minimum_evidence_needed,
        known_risks=known_risks,
        stop_conditions=stop_conditions,
        warnings=warnings,
    )


def _possible_claims(question: str) -> list[str]:
    claim_subject = question.rstrip("?.!")
    return [
        f"The available sources support a limited claim about: {claim_subject}.",
        f"The available sources weaken or contradict a claim about: {claim_subject}.",
        f"The current sources are insufficient to make a stronger claim about: {claim_subject}.",
    ]


def _information_need(question: str, roles: list[str]) -> str:
    if "source_quality_check" in roles:
        return f"Determine what source roles are needed to assess source quality for: {question}"
    if "user_intent_check" in roles:
        return f"Reframe risky market question into evidence-based intelligence before retrieval: {question}"
    if "definition_anchor" in roles and "scope_boundary" in roles:
        return f"Clarify entity, timeframe, and scope before collecting information for: {question}"
    if "quantitative_anchor" in roles:
        return f"Determine which numeric, timeline, and contradictory sources are needed for: {question}"
    return f"Determine which role-diverse sources are needed before retrieval for: {question}"


def _minimum_evidence(roles: list[str]) -> str:
    requirements = ["at least one direct support source", "one contradiction or missing-data signal"]
    if "quantitative_anchor" in roles:
        requirements.insert(0, "At least one quantitative anchor")
    if "timeline_anchor" in roles:
        requirements.append("one visible timeline anchor")
    if "source_quality_check" in roles:
        requirements.append("one original or independent source-quality check")
    if "user_intent_check" in roles:
        requirements.append("one explicit user-intent boundary that blocks buy/sell drift")
    return "; ".join(requirements) + "."


def _is_underspecified(question: str) -> bool:
    words = question.split()
    return (
        len(words) <= 5
        or question.startswith("tell me about")
        or question in {"ai", "market", "growth", "demand"}
    )


def _add_roles(existing: list[str], roles: list[str]) -> None:
    for role in roles:
        if role not in existing:
            existing.append(role)


def _add_sources(existing: list[str], sources: list[str]) -> None:
    for source in sources:
        if source not in existing:
            existing.append(source)
