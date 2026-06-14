import base64
from pathlib import Path


ONE_PIXEL_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/p9sAAAAASUVORK5CYII="
)


def main() -> None:
    root = Path(__file__).resolve().parent
    _write_image_only_pdf(root / "scanned-image.pdf")
    _write_image_heavy_pdf(root / "image-heavy.pdf")
    _write_multi_column_pdf(root / "multi-column-layout.pdf")
    _write_blank_pdf(root / "no-extractable-text.pdf")


def _write_blank_pdf(path: Path) -> None:
    import pymupdf

    document = pymupdf.open()
    document.new_page(width=260, height=160)
    path.write_bytes(document.tobytes())
    document.close()


def _write_image_only_pdf(path: Path) -> None:
    import pymupdf

    document = pymupdf.open()
    page = document.new_page(width=260, height=160)
    page.insert_image(pymupdf.Rect(70, 40, 190, 120), stream=ONE_PIXEL_PNG)
    path.write_bytes(document.tobytes())
    document.close()


def _write_image_heavy_pdf(path: Path) -> None:
    import pymupdf

    document = pymupdf.open()
    page = document.new_page(width=320, height=220)
    page.insert_text((40, 50), "chart title text")
    page.insert_image(pymupdf.Rect(40, 70, 180, 170), stream=ONE_PIXEL_PNG)
    page.insert_text((40, 195), "caption text")
    path.write_bytes(document.tobytes())
    document.close()


def _write_multi_column_pdf(path: Path) -> None:
    import pymupdf

    document = pymupdf.open()
    page = document.new_page(width=420, height=240)
    page.insert_textbox(
        pymupdf.Rect(40, 50, 190, 170),
        "left column claim\nmarket demand increased",
    )
    page.insert_textbox(
        pymupdf.Rect(230, 50, 380, 170),
        "right column limitation\nsample is synthetic",
    )
    path.write_bytes(document.tobytes())
    document.close()


if __name__ == "__main__":
    main()
