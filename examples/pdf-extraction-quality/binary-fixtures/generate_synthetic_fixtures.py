from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    _write_born_digital_text_pdf(root / "born-digital-text.pdf")
    _write_deterministic_table_pdf(root / "deterministic-table-adapter.pdf")


def _write_born_digital_text_pdf(path: Path) -> None:
    import pymupdf

    document = pymupdf.open()
    page = document.new_page(width=360, height=180)
    page.insert_text(
        (40, 80),
        "company revenue increased and source date visible",
    )
    path.write_bytes(document.tobytes())
    document.close()


def _write_deterministic_table_pdf(path: Path) -> None:
    import pymupdf

    document = pymupdf.open()
    page = document.new_page(width=300, height=200)
    x0, y0, x1, y1 = 40, 40, 260, 120
    for x in [x0, (x0 + x1) / 2, x1]:
        page.draw_line((x, y0), (x, y1), color=(0, 0, 0), width=1)
    for y in [y0, (y0 + y1) / 2, y1]:
        page.draw_line((x0, y), (x1, y), color=(0, 0, 0), width=1)
    page.insert_text((50, 65), "Segment")
    page.insert_text((160, 65), "Growth")
    page.insert_text((50, 105), "Enterprise")
    page.insert_text((160, 105), "12%")
    path.write_bytes(document.tobytes())
    document.close()


if __name__ == "__main__":
    main()
