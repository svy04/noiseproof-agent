from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_api_compose_service_exposes_local_otel_span_export_flag():
    compose = yaml.safe_load((REPO_ROOT / "docker-compose.yml").read_text())

    api_environment = compose["services"]["api"]["environment"]

    assert (
        api_environment["NOISEPROOF_ENABLE_OTEL_SPAN_EXPORT"]
        == "${NOISEPROOF_ENABLE_OTEL_SPAN_EXPORT:-false}"
    )
