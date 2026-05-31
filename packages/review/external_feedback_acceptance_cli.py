from __future__ import annotations

import argparse
import json
from pathlib import Path

from .external_feedback_acceptance import (
    acceptance_draft_result_to_dict,
    build_external_feedback_acceptance_drafts_from_dict,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Draft manual acceptance records for screened external feedback."
    )
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    payload = json.loads(Path(args.input).read_text(encoding="utf-8-sig"))
    result = build_external_feedback_acceptance_drafts_from_dict(payload)
    print(json.dumps(acceptance_draft_result_to_dict(result), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
