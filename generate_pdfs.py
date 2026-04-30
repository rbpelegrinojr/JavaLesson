#!/usr/bin/env python3
"""
generate_pdfs.py
Converts each weeks/week-XX.md into a separate PDF inside the pdfs/ directory.
Requires: pip install weasyprint markdown

Usage:
    python3 generate_pdfs.py
"""

import os
import markdown
from weasyprint import HTML, CSS

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WEEKS_DIR  = os.path.join(SCRIPT_DIR, "weeks")
PDFS_DIR   = os.path.join(SCRIPT_DIR, "pdfs")
os.makedirs(PDFS_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# CSS — clean, student-friendly typography
# ---------------------------------------------------------------------------
STYLESHEET = CSS(string="""
@page {
    size: A4;
    margin: 2cm 2.2cm 2.2cm 2.2cm;
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-size: 9pt;
        color: #888;
    }
}

body {
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.65;
    color: #222;
}

h1 {
    font-size: 20pt;
    color: #1a237e;
    border-bottom: 3px solid #1a237e;
    padding-bottom: 6px;
    margin-top: 0;
    page-break-after: avoid;
}

h2 {
    font-size: 14pt;
    color: #283593;
    border-left: 4px solid #3949ab;
    padding-left: 8px;
    margin-top: 26px;
    page-break-after: avoid;
}

h3 {
    font-size: 12pt;
    color: #37474f;
    margin-top: 18px;
    page-break-after: avoid;
}

h4 {
    font-size: 11pt;
    color: #455a64;
    page-break-after: avoid;
}

blockquote {
    border-left: 4px solid #90caf9;
    margin: 0 0 12px 0;
    padding: 6px 12px;
    background: #e3f2fd;
    border-radius: 4px;
    font-style: italic;
    color: #37474f;
}

code {
    background: #f5f5f5;
    border: 1px solid #e0e0e0;
    border-radius: 3px;
    padding: 1px 4px;
    font-family: "Consolas", "Courier New", monospace;
    font-size: 9.5pt;
    color: #c62828;
}

pre {
    background: #1e1e2e;
    color: #cdd6f4;
    border-radius: 6px;
    padding: 14px 16px;
    overflow-x: auto;
    margin: 12px 0;
    page-break-inside: avoid;
}

pre code {
    background: transparent;
    border: none;
    padding: 0;
    color: inherit;
    font-size: 9pt;
    line-height: 1.55;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 10pt;
    page-break-inside: avoid;
}

th {
    background: #3949ab;
    color: white;
    padding: 7px 10px;
    text-align: left;
}

td {
    padding: 6px 10px;
    border-bottom: 1px solid #e0e0e0;
}

tr:nth-child(even) td {
    background: #f5f7ff;
}

ul, ol {
    margin: 6px 0;
    padding-left: 22px;
}

li {
    margin: 3px 0;
}

p {
    margin: 8px 0;
}

hr {
    border: none;
    border-top: 1px solid #bdbdbd;
    margin: 20px 0;
}

strong {
    color: #1a237e;
}

em {
    color: #455a64;
}

/* Quiz / checklist styling */
input[type="checkbox"] {
    margin-right: 6px;
}
""")

# ---------------------------------------------------------------------------
# Markdown extensions
# ---------------------------------------------------------------------------
MD_EXTENSIONS = [
    "tables",
    "fenced_code",
    "codehilite",
    "nl2br",
    "sane_lists",
    "smarty",
]

MD_EXTENSION_CONFIGS = {
    "codehilite": {"guess_lang": False, "noclasses": True},
    "smarty": {"smart_quotes": False},
}

# ---------------------------------------------------------------------------
# Conversion
# ---------------------------------------------------------------------------
def convert_week(md_path: str, pdf_path: str) -> None:
    """Convert a single Markdown file to PDF."""
    with open(md_path, encoding="utf-8") as fh:
        md_text = fh.read()

    html_body = markdown.markdown(
        md_text,
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXTENSION_CONFIGS,
    )

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{os.path.basename(md_path)}</title>
</head>
<body>
{html_body}
</body>
</html>"""

    HTML(string=full_html).write_pdf(pdf_path, stylesheets=[STYLESHEET])


def main() -> None:
    md_files = sorted(
        f for f in os.listdir(WEEKS_DIR)
        if f.startswith("week-") and f.endswith(".md")
    )

    if not md_files:
        print("No week-XX.md files found in", WEEKS_DIR)
        return

    print(f"Generating {len(md_files)} PDFs into {PDFS_DIR}/\n")
    for filename in md_files:
        md_path  = os.path.join(WEEKS_DIR, filename)
        pdf_name = filename.replace(".md", ".pdf")
        pdf_path = os.path.join(PDFS_DIR, pdf_name)

        print(f"  {filename}  →  {pdf_name} ...", end=" ", flush=True)
        convert_week(md_path, pdf_path)
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"done  ({size_kb:.0f} KB)")

    print(f"\n✅  All {len(md_files)} PDFs generated successfully.")


if __name__ == "__main__":
    main()
