"""document_processor.py - the Reader.

Reads the markdown knowledge bases and cuts them into labelled pieces.
It does NOT choose pieces and does NOT call the LLM.

Each piece is a dictionary:
{"source": ..., "file": ..., "head": ..., "text": ..., "date": ...}
"""

import re
from pathlib import Path

# knowledge_base/ folder, found from this file: src/ -> project root -> knowledge_base
KNOWLEDGE_BASE = Path(__file__).resolve().parent.parent / "knowledge_base"
FOLDERS = ["primary", "secondary"]


# Step 1: find every .md file
def find_markdown_files(folder: Path) -> list:
    """Find every .md file in a folder and its subfolders."""
    if not folder.exists():
        raise FileNotFoundError(
            f"[find_markdown_files] Folder not found: {folder} | "
            "Suggestion: check that knowledge_base/primary and knowledge_base/secondary exist"
        )
    return sorted(folder.rglob("*.md"))


# Step 2: read the text and the date
def read_file(path: Path) -> str:
    """Read the text of one markdown file."""
    return path.read_text(encoding="utf-8")


def find_date(text: str) -> str:
    """Return the first 'Date' line in the header (before the first ##), or ''."""
    header = text.split("\n## ")[0]
    for line in header.splitlines():
        if "date" in line.lower():
            return line.split(":", 1)[-1].strip(" *")
    return ""


# Step 3: split at every ## heading
def split_by_heading(text: str) -> list:
    """Split the text at every '## ' heading. Returns [(heading, text), ...]."""
    parts = re.split(r"^## +(.+)$", text, flags=re.MULTILINE)
    sections = [("Intro", parts[0])]
    for i in range(1, len(parts), 2):
        sections.append((parts[i].strip(), parts[i + 1]))
    return sections


def clean_text(text: str) -> str:
    """Remove the '# Title' line and extra blank space."""
    lines = [line for line in text.splitlines() if not line.startswith("# ")]
    return "\n".join(lines).strip()


# Step 4: label each piece
def process_file(path: Path, source: str) -> list:
    """Read one file, split it, and label every piece."""
    text = read_file(path)
    date = find_date(text)
    pieces = []
    for heading, section_text in split_by_heading(text):
        section_text = clean_text(section_text)
        if section_text:  # skip empty pieces
            pieces.append({
                "source": source,
                "file": path.name,
                "head": heading,
                "text": section_text,
                "date": date,
            })
    return pieces


def load_pieces() -> list:
    """Run the Reader on both knowledge bases and return all pieces."""
    pieces = []
    for source in FOLDERS:
        for path in find_markdown_files(KNOWLEDGE_BASE / source):
            pieces.extend(process_file(path, source))
    return pieces


# Quick check: python src/document_processor.py
if __name__ == "__main__":
    all_files = [p for s in FOLDERS for p in find_markdown_files(KNOWLEDGE_BASE / s)]
    pieces = load_pieces()

    print(f"Files found: {len(all_files)}")
    for f in all_files:
        print("  -", f.relative_to(KNOWLEDGE_BASE))
    print(f"Pieces created: {len(pieces)}\n")

    for p in pieces[:3]:
        print(f"source: {p['source']}\nfile:   {p['file']}\nhead:   {p['head']}\ntext:   {p['text'][:60]}...\n")

    assert all(p["head"] for p in pieces), "Some pieces have no heading"
    print("✓ Every piece has a heading (M1, M2)")