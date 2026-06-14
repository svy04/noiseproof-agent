from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    _write_ocr_smoke_text_image_pdf(root / "ocr-smoke-text-image.pdf")


def _write_ocr_smoke_text_image_pdf(path: Path) -> None:
    import pymupdf

    source = pymupdf.open()
    source_page = source.new_page(width=420, height=180)
    source_page.insert_text((54, 104), "ocr smoke text", fontsize=34)
    pixmap = source_page.get_pixmap(dpi=220)
    image = pixmap.tobytes("png")
    source.close()

    document = pymupdf.open()
    page = document.new_page(width=420, height=180)
    page.insert_image(page.rect, stream=image)
    path.write_bytes(document.tobytes())
    document.close()


if __name__ == "__main__":
    main()
