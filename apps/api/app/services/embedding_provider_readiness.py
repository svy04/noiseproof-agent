from app.schemas import EmbeddingProviderReadinessOut
from app.settings import Settings


def summarize_embedding_provider_readiness(
    settings: Settings,
) -> EmbeddingProviderReadinessOut:
    configured = bool(settings.openai_api_key.strip())
    provider_enabled = bool(settings.enable_openai_provider and not settings.ci)
    timeout_valid = settings.openai_provider_timeout_seconds > 0
    provider_client_available = configured and provider_enabled and timeout_valid
    blocking_reasons: list[str] = []
    if not configured:
        blocking_reasons.append("openai_api_key_missing")
    if not settings.enable_openai_provider:
        blocking_reasons.append("provider_flag_disabled")
    if settings.ci:
        blocking_reasons.append("ci_disables_provider_client")
    if not timeout_valid:
        blocking_reasons.append("provider_timeout_invalid")

    if provider_client_available:
        readiness_status = "ready_for_owner_runtime_opt_in"
        provider_call_boundary = "owner_runtime_opt_in_only"
    else:
        readiness_status = (
            "disabled_missing_api_key"
            if not configured
            else "disabled_provider_boundary"
        )
        provider_call_boundary = "provider_call_disabled"

    warnings = [
        "This is readiness metadata only, not a provider call.",
        "No OpenAI provider call is made by ops summary or dashboard rendering.",
        "Embedding generation remains unproven until owner-runtime smoke evidence exists.",
    ]
    if blocking_reasons:
        warnings.append("Blocking reason(s): " + ", ".join(blocking_reasons) + ".")

    return EmbeddingProviderReadinessOut(
        provider="openai",
        configured=configured,
        provider_enabled=provider_enabled,
        provider_client_available=provider_client_available,
        readiness_status=readiness_status,
        provider_call_boundary=provider_call_boundary,
        network_boundary="no_network_call",
        cost_boundary="no_cost_incurred",
        persistence_boundary="readiness_only_not_persisted",
        secret_exposed=False,
        blocking_reasons=blocking_reasons,
        warnings=warnings,
    )
