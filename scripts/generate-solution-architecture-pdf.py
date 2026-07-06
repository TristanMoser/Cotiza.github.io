#!/usr/bin/env python3
"""Generate AppExchange Solution Architecture PDF from markdown source."""

from __future__ import annotations

import re
from pathlib import Path

from fpdf import FPDF

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "docs/security/solution-architecture-and-usage.md"
OUTPUT_DIR = REPO / "static/appexchange"
OUTPUT = OUTPUT_DIR / "Cotiza-CPQ-Solution-Architecture-and-Usage.pdf"


class DocPDF(FPDF):
    def header(self) -> None:
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(100, 100, 100)
        self.set_x(self.l_margin)
        self.cell(0, 8, "Cotiza CPQ - Solution Architecture and Usage", align="R")
        self.ln(4)

    def footer(self) -> None:
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(100, 100, 100)
        self.set_x(self.l_margin)
        self.cell(0, 8, f"Page {self.page_no()}", align="C")


def strip_md(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    return (
        text.replace("\u2014", "-")
        .replace("\u2192", "->")
        .replace("\u25bc", "v")
        .replace("\u2500", "-")
        .replace("\u2502", "|")
        .replace("\u251c", "+")
        .replace("\u2514", "+")
        .replace("\u2524", "+")
        .replace("\u2534", "+")
    )


def latin1(text: str) -> str:
    return strip_md(text).encode("latin-1", "replace").decode("latin-1")


def write_text(pdf: DocPDF, text: str, h: float = 5) -> None:
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, h, latin1(text))


def write_table(pdf: DocPDF, rows: list[list[str]]) -> None:
    if not rows:
        return
    col_count = max(len(r) for r in rows)
    usable = pdf.w - pdf.l_margin - pdf.r_margin
    width = usable / col_count
    if width < 10:
        pdf.set_font("Helvetica", "", 8)
        for row in rows:
            write_text(pdf, " | ".join(strip_md(c) for c in row), 4)
        pdf.ln(2)
        return
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", 7)
    for cell in rows[0]:
        pdf.cell(width, 5, latin1(cell)[:34], border=1)
    pdf.ln()
    pdf.set_font("Helvetica", "", 7)
    for row in rows[1:]:
        pdf.set_x(pdf.l_margin)
        for i in range(col_count):
            val = row[i] if i < len(row) else ""
            pdf.cell(width, 5, latin1(val)[:34], border=1)
        pdf.ln()
    pdf.ln(2)


def write_code_block(pdf: DocPDF, lines: list[str]) -> None:
    pdf.set_font("Courier", "", 6)
    pdf.set_fill_color(245, 245, 245)
    for line in lines:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, 3.2, latin1(line), fill=True)
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 10)


def render_markdown(pdf: DocPDF, content: str) -> None:
    lines = content.splitlines()
    i = 0
    in_code = False
    code_lines: list[str] = []
    table_rows: list[list[str]] = []

    while i < len(lines):
        line = lines[i].rstrip()

        if line.startswith("```"):
            if in_code:
                write_code_block(pdf, code_lines)
                code_lines = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(re.match(r"^[-:]+$", c.replace(" ", "")) for c in cells):
                i += 1
                continue
            table_rows.append(cells)
            i += 1
            if i >= len(lines) or not lines[i].startswith("|"):
                write_table(pdf, table_rows)
                table_rows = []
            continue

        if not line.strip():
            pdf.ln(2)
            i += 1
            continue

        if line.startswith("# "):
            pdf.set_font("Helvetica", "B", 16)
            write_text(pdf, line[2:], 8)
            pdf.ln(2)
        elif line.startswith("## "):
            pdf.set_font("Helvetica", "B", 13)
            write_text(pdf, line[3:], 7)
            pdf.ln(1)
        elif line.startswith("### "):
            pdf.set_font("Helvetica", "B", 11)
            write_text(pdf, line[4:], 6)
            pdf.ln(1)
        elif line.startswith("- "):
            pdf.set_font("Helvetica", "", 10)
            write_text(pdf, "  - " + line[2:])
        elif re.match(r"^\d+\.\s", line):
            pdf.set_font("Helvetica", "", 10)
            write_text(pdf, "  " + line)
        else:
            pdf.set_font("Helvetica", "", 10)
            write_text(pdf, line)

        i += 1


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    content = SOURCE.read_text(encoding="utf-8")
    content = re.sub(r"```mermaid.*?```", "", content, flags=re.DOTALL)

    pdf = DocPDF()
    pdf.set_margins(15, 15, 15)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    render_markdown(pdf, content)
    pdf.output(str(OUTPUT))
    size_kb = OUTPUT.stat().st_size / 1024
    print(f"Wrote {OUTPUT} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
