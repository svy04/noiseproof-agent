from __future__ import annotations

import argparse
import json
from pathlib import Path

from .external_feedback import screen_issue_view_payload, screen_result_to_dict


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Screen GitHub issue comments for external feedback candidates."
    )
    parser.add_argument("--input", required=True, help="Path to gh issue JSON output.")
    parser.add_argument("--repository-owner", required=True)
    args = parser.parse_args()

    payload = json.loads(Path(args.input).read_text(encoding="utf-8-sig"))
    result = screen_issue_view_payload(payload, repository_owner=args.repository_owner)
    print(json.dumps(screen_result_to_dict(result), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
