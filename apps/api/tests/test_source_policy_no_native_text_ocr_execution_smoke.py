import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
OBSERVATION_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-execution-smoke.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-execution-smoke-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_execution_smoke import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_source_policy_no_native_text_ocr_execution_smoke_report,
    build_source_policy_no_native_text_ocr_execution_smoke_summary,
    discover_source_policy_no_native_text_ocr_smoke_input,
    load_source_policy_no_native_text_ocr_execution_smoke,
    run_source_policy_no_native_text_ocr_smoke,
)


class FakeDownloader:
    def __init__(self, content: bytes):
        self.content = content
        self.calls: list[str] = []

    def __call__(self, url: str) -> bytes:
        self.calls.append(url)
        return self.content


class FakeOcrAdapter:
    def extract_page_text(
        self,
        *,
        content: bytes,
        language: str,
        dpi: int,
        full_page: bool,
        planned_pages: list[int],
        tessdata: str | None,
    ) -> list[str]:
        assert content == b"%PDF-1.7 fake source-policy pdf"
        assert language == "eng"
        assert dpi == 300
        assert full_page is True
        assert planned_pages == [1, 2, 3, 4]
        assert tessdata is not None
        return [
            "Commission memorandum",
            "MFR source-policy smoke",
            "",
            "NoiseProof OCR execution smoke",
        ]


def test_source_policy_no_native_text_ocr_execution_smoke_commits_sanitized_runtime_observation():
    observation = load_source_policy_no_native_text_ocr_execution_smoke(
        OBSERVATION_PATH
    )
    summary = build_source_policy_no_native_text_ocr_execution_smoke_summary(
        observation
    )

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == (
        "source_policy_no_native_text_ocr_execution_plan_v0"
    )
    assert summary["run_source"] == "owner_runtime_pymupdf_ocr_source_policy_smoke"
    assert summary["target_fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["publisher"] == "National Archives and Records Administration"
    assert summary["source_sha256"] == (
        "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
    )
    assert summary["page_count"] == 4
    assert summary["ocr_pages_attempted"] == 4
    assert summary["native_text_char_count"] == 0
    assert summary["ocr_text_char_count"] > 0
    assert summary["expected_markers_checked"] == ["commission", "mfr"]
    assert summary["expected_markers_found_count"] >= 1
    assert summary["ocr_execution_performed"] is True
    assert summary["ocr_calls_attempted"] is True
    assert summary["ocr_quality_eval_performed"] is False
    assert summary["raw_ocr_text_committed"] is False
    assert summary["page_images_committed"] is False
    assert summary["screenshots_committed"] is False
    assert summary["can_claim_source_policy_no_native_text_ocr_execution_smoke"] is True
    assert summary["can_claim_ocr_execution"] is True
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_execution_smoke_report_is_current_and_bounded():
    observation = load_source_policy_no_native_text_ocr_execution_smoke(
        OBSERVATION_PATH
    )
    summary = build_source_policy_no_native_text_ocr_execution_smoke_summary(
        observation
    )
    report = build_source_policy_no_native_text_ocr_execution_smoke_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Execution Smoke" in report
    assert "source_policy_no_native_text_ocr_execution_smoke_v0" in report
    assert "run_source -> owner_runtime_pymupdf_ocr_source_policy_smoke" in report
    assert "ocr_execution_performed -> true" in report
    assert "ocr_quality_eval_performed -> false" in report
    assert "raw_ocr_text_committed -> false" in report
    assert "can_claim_source_policy_no_native_text_ocr_execution_smoke -> true" in report
    assert "can_claim_ocr_execution -> true" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "source_policy_no_native_text_ocr_quality_eval_plan_v0" in report
    assert "not OCR quality evidence" in report
    assert "not robust PDF extraction evidence" in report


def test_source_policy_no_native_text_ocr_execution_smoke_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_execution_smoke_command",
            "--observation",
            str(OBSERVATION_PATH),
            "--output",
            str(REPORT_PATH),
            "--check",
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "source_policy_no_native_text_ocr_execution_smoke_report_current" in result.stdout
    assert "ocr_execution_performed=true" in result.stdout
    assert "can_claim_ocr_execution=true" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_no_native_text_ocr_smoke_discovery_keeps_paths_sanitized():
    missing = discover_source_policy_no_native_text_ocr_smoke_input({})
    assert missing["owner_runtime_input_status"] == "missing_opt_in"
    assert missing["ocr_calls_attempted"] is False
    assert missing["tesseract_path_printed"] is False
    assert missing["tessdata_path_printed"] is False

    ready = discover_source_policy_no_native_text_ocr_smoke_input(
        {
            "NOISEPROOF_ENABLE_SOURCE_POLICY_OCR_SMOKE": "true",
            "NOISEPROOF_TESSERACT_AVAILABLE": "true",
            "NOISEPROOF_TESSDATA_AVAILABLE": "true",
            "NOISEPROOF_TESSDATA_PREFIX": "C:/secret/tessdata",
            "CI": "false",
        }
    )
    assert ready["owner_runtime_input_status"] == "ready_for_owner_runtime_smoke"
    assert ready["tesseract_available"] is True
    assert ready["tessdata_available"] is True
    assert "C:/secret" not in json.dumps(ready)


def test_source_policy_no_native_text_ocr_smoke_runner_rejects_repo_output_path():
    result = run_source_policy_no_native_text_ocr_smoke(
        output_path=REPO_ROOT / "examples/pdf-extraction-quality/forbidden.json",
        env={
            "NOISEPROOF_ENABLE_SOURCE_POLICY_OCR_SMOKE": "true",
            "NOISEPROOF_TESSERACT_AVAILABLE": "true",
            "NOISEPROOF_TESSDATA_AVAILABLE": "true",
            "NOISEPROOF_TESSDATA_PREFIX": "C:/secret/tessdata",
            "CI": "false",
        },
        downloader=FakeDownloader(b"%PDF-1.7 fake source-policy pdf"),
        ocr_adapter=FakeOcrAdapter(),
    )

    assert result["run_status"] == "output_path_rejected"
    assert result["ocr_calls_attempted"] is False


def test_source_policy_no_native_text_ocr_smoke_runner_writes_sanitized_report_with_fake_adapter(tmp_path):
    output_path = tmp_path / "source-policy-ocr-smoke.json"
    fake_content = b"%PDF-1.7 fake source-policy pdf"
    downloader = FakeDownloader(fake_content)

    result = run_source_policy_no_native_text_ocr_smoke(
        output_path=output_path,
        env={
            "NOISEPROOF_ENABLE_SOURCE_POLICY_OCR_SMOKE": "true",
            "NOISEPROOF_TESSERACT_AVAILABLE": "true",
            "NOISEPROOF_TESSDATA_AVAILABLE": "true",
            "NOISEPROOF_TESSDATA_PREFIX": "C:/secret/tessdata",
            "NOISEPROOF_ALLOW_TEST_SHA": "true",
            "CI": "false",
        },
        downloader=downloader,
        ocr_adapter=FakeOcrAdapter(),
    )

    assert result["run_status"] == "report_written"
    assert result["ocr_execution_performed"] is True
    assert result["ocr_calls_attempted"] is True
    assert result["ocr_pages_attempted"] == 4
    assert result["ocr_text_char_count"] > 0
    assert result["expected_markers_found_count"] == 2
    assert result["raw_ocr_text_committed"] is False
    assert result["tessdata_path_printed"] is False
    assert result["tessdata_path_committed_to_repo"] is False
    assert output_path.is_file()
    assert "C:/secret" not in output_path.read_text(encoding="utf-8")
    assert "Commission memorandum" not in output_path.read_text(encoding="utf-8")
    assert downloader.calls


def test_source_policy_no_native_text_ocr_execution_smoke_rejects_raw_text_or_quality_claim(tmp_path):
    observation = load_source_policy_no_native_text_ocr_execution_smoke(
        OBSERVATION_PATH
    )
    raw_observation = dict(observation)
    raw_observation["raw_ocr_text"] = "forbidden"
    raw_path = tmp_path / "raw.json"
    raw_path.write_text(json.dumps(raw_observation), encoding="utf-8")

    with pytest.raises(ValueError, match="raw_ocr_text"):
        load_source_policy_no_native_text_ocr_execution_smoke(raw_path)

    quality_observation = dict(observation)
    quality_observation["ocr_quality_eval_performed"] = True
    quality_path = tmp_path / "quality.json"
    quality_path.write_text(json.dumps(quality_observation), encoding="utf-8")

    with pytest.raises(ValueError, match="ocr_quality_eval_performed"):
        load_source_policy_no_native_text_ocr_execution_smoke(quality_path)


def test_source_policy_no_native_text_ocr_execution_smoke_artifacts_do_not_commit_paths_or_raw_content():
    artifacts = [
        OBSERVATION_PATH,
        REPORT_PATH,
        REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-execution-smoke.md",
        REPO_ROOT
        / "docs/specs/2026-06-30-source-policy-no-native-text-ocr-execution-smoke.md",
    ]
    forbidden = [
        "Users\\admin",
        "tessdata_path:",
        "tesseract_path:",
        "raw_text:",
        "raw_ocr_text:",
        "raw_extracted_text:",
        "recognized_text:",
        "page_image:",
        "screenshot:",
    ]

    for artifact in artifacts:
        text = artifact.read_text(encoding="utf-8")
        for marker in forbidden:
            assert marker not in text


def test_source_policy_no_native_text_ocr_execution_smoke_docs_and_surfaces_are_linked():
    review_path = (
        REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-execution-smoke.md"
    )
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-source-policy-no-native-text-ocr-execution-smoke.md"
    )
    assert review_path.is_file()
    assert spec_path.is_file()
    assert REPORT_PATH.is_file()

    surfaces = [
        review_path.read_text(encoding="utf-8"),
        (REPO_ROOT / "README.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/MASTER-SPEC.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "docs/review/proof-gap-action-surface.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "apps/api/app/services/proof_gap_registry.py").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8"),
    ]

    for surface in surfaces:
        assert "source_policy_no_native_text_ocr_execution_smoke_v0" in surface
        assert "source_policy_no_native_text_ocr_quality_eval_plan_v0" in surface

    for boundary in [
        "not OCR quality evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in surfaces[0]
