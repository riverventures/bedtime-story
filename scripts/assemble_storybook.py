#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

from PIL import Image, ImageDraw, ImageFont


DEFAULT_DPI = 200
DEFAULT_WIDTH_IN = 11
DEFAULT_HEIGHT_IN = 8.5
DEFAULT_TEXT_RATIO = 0.10


def load_lines(path: Path) -> List[str]:
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]
    return [line for line in lines if line]


def fit_cover(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
    ratio = max(target_w / img.width, target_h / img.height)
    new_w, new_h = int(img.width * ratio), int(img.height * ratio)
    resized = img.resize((new_w, new_h), Image.LANCZOS)
    crop_x = max((new_w - target_w) // 2, 0)
    crop_y = max((new_h - target_h) // 2, 0)
    return resized.crop((crop_x, crop_y, crop_x + target_w, crop_y + target_h))


def build_pages(images_dir: Path, lines: List[str], output: Path, font_path: str | None) -> None:
    image_paths = sorted([p for p in images_dir.iterdir() if p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp'}])
    if len(image_paths) != len(lines):
        raise SystemExit(f"Need one image per line of story text. Found {len(image_paths)} images and {len(lines)} lines.")

    page_w = int(DEFAULT_WIDTH_IN * DEFAULT_DPI)
    page_h = int(DEFAULT_HEIGHT_IN * DEFAULT_DPI)
    img_area_h = int(page_h * (1 - DEFAULT_TEXT_RATIO))
    text_area_h = page_h - img_area_h

    if font_path:
        font = ImageFont.truetype(font_path, 42)
    else:
        font = ImageFont.load_default()

    pages: List[Image.Image] = []
    for image_path, text in zip(image_paths, lines):
        page = Image.new("RGB", (page_w, page_h), "white")
        draw = ImageDraw.Draw(page)

        img = Image.open(image_path).convert("RGB")
        page.paste(fit_cover(img, page_w, img_area_h), (0, 0))

        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        text_x = max((page_w - text_w) // 2, 20)
        text_y = img_area_h + max((text_area_h - text_h) // 2, 10)
        draw.text((text_x, text_y), text, fill="black", font=font)

        pages.append(page)

    output.parent.mkdir(parents=True, exist_ok=True)
    pages[0].save(output, "PDF", resolution=DEFAULT_DPI, save_all=True, append_images=pages[1:])


def main() -> None:
    parser = argparse.ArgumentParser(description="Assemble landscape bedtime-story pages into a printable PDF.")
    parser.add_argument("--images-dir", required=True, help="Directory containing page images in sorted order.")
    parser.add_argument("--text-file", required=True, help="UTF-8 text file with one story line per page.")
    parser.add_argument("--output", required=True, help="Output PDF path.")
    parser.add_argument("--font-path", default=None, help="Optional path to a TTF font.")
    args = parser.parse_args()

    build_pages(Path(args.images_dir), load_lines(Path(args.text_file)), Path(args.output), args.font_path)


if __name__ == "__main__":
    main()
