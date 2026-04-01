#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def build_anchor(profile: dict[str, Any]) -> str:
    parts: list[str] = []
    age = profile.get("age")
    if age:
        parts.append(f"A {age}-year-old child")
    else:
        parts.append("A child")

    appearance = profile.get("appearance", {})
    for key in ["hair", "skin_tone", "eyes", "features", "default_outfit"]:
        value = appearance.get(key)
        if value:
            parts.append(str(value).strip())

    return ", ".join(parts).strip().rstrip(",") + "."


def normalize_story_lines(lines: list[str]) -> list[str]:
    normalized = [line.strip() for line in lines if line and line.strip()]
    if not normalized:
        raise SystemExit("Story lines are empty.")
    return normalized


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare reusable bedtime-story inputs from a JSON profile and story draft.")
    parser.add_argument("--profile", required=True, help="Path to child profile JSON.")
    parser.add_argument("--story-lines", required=True, help="Path to a text file with one story line per page.")
    parser.add_argument("--out-dir", required=True, help="Directory for generated helper files.")
    args = parser.parse_args()

    profile_path = Path(args.profile)
    story_lines_path = Path(args.story_lines)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    anchor = build_anchor(profile)
    lines = normalize_story_lines(story_lines_path.read_text(encoding="utf-8").splitlines())

    (out_dir / "character-anchor.txt").write_text(anchor + "\n", encoding="utf-8")
    (out_dir / "story-lines.clean.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    summary = {
        "child_name": profile.get("name"),
        "page_count": len(lines),
        "character_anchor": anchor,
    }
    (out_dir / "story-summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
