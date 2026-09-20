"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass

import config
from ingest import Document


# ─── Milestone 3 settings ────────────────────────────────────────────────────
# My corpus is 14 markdown guides, each with a `# Town` title and a handful of
# `## Section` headings under it. A section is already the unit a question maps
# to, so these are guard rails for the odd section that runs long or short,
# not a window size.

MAX_CHUNK = 900     # split a section that runs past this, at a paragraph break
MIN_CHUNK = 150     # a piece this short gets merged into the next one
SENTENCE_OVERLAP = 1  # sentences carried over when one section has to be split


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


# ─── Helpers for my strategy ─────────────────────────────────────────────────


def _split_sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    """
    Pull a document apart at its `##` headings.

    Returns the title line (the `#` heading, without the hash) and a list of
    (heading, body) pairs. Anything before the first `##` — the opening
    paragraph most of my guides have — comes back as a section with the
    heading "Overview", because it is real content and it would otherwise be
    thrown away.
    """
    lines = text.split("\n")

    title = ""
    start = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            start = i + 1
            break

    sections: list[tuple[str, str]] = []
    heading = "Overview"
    body: list[str] = []

    for line in lines[start:]:
        if line.startswith("## "):
            if "\n".join(body).strip():
                sections.append((heading, "\n".join(body).strip()))
            heading = line[3:].strip()
            body = []
        else:
            body.append(line)

    if "\n".join(body).strip():
        sections.append((heading, "\n".join(body).strip()))

    return title, sections


def _sentences(text: str) -> list[str]:
    """Rough sentence split — good enough for prose guides."""
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p for p in parts if p.strip()]


def _split_long_body(body: str, budget: int) -> list[str]:
    """
    Break a section that runs past the budget, preferring paragraph breaks and
    falling back to sentence breaks. Carries `SENTENCE_OVERLAP` sentences from
    the end of one piece to the start of the next so a split paragraph keeps
    its thread.
    """
    if len(body) <= budget:
        return [body]

    units = [p.strip() for p in body.split("\n\n") if p.strip()]
    if len(units) == 1:
        units = _sentences(body)

    pieces: list[str] = []
    current: list[str] = []

    for unit in units:
        candidate = current + [unit]
        if current and len("\n\n".join(candidate)) > budget:
            pieces.append("\n\n".join(current))
            tail = _sentences("\n\n".join(current))[-SENTENCE_OVERLAP:]
            current = tail + [unit]
        else:
            current = candidate

    if current:
        pieces.append("\n\n".join(current))

    return pieces


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split each guide at its `##` headings, one chunk per section.

    Every chunk is rebuilt as:

        # Town name
        ## Section heading

        body text

    The title line is repeated into every chunk on purpose. All ten of my town
    guides use the same seven headings, so a bare "Getting around" section
    reads "the town is walkable end to end in about 35 minutes" with nothing in
    it to say which town that is. Repeating the title costs about 15 characters
    and is what makes a chunk answerable on its own.

    Sections longer than MAX_CHUNK are split at paragraph breaks with one
    sentence of overlap; sections shorter than MIN_CHUNK are merged into the
    next one so I don't get a heading with a single line under it.
    """
    chunks: list[Chunk] = []

    for doc in documents:
        title, sections = _split_sections(doc.text)
        header = f"# {title}" if title else ""

        # Merge sections that are too thin to stand alone into the next one.
        merged: list[tuple[str, str]] = []
        carry: tuple[str, str] | None = None

        for heading, body in sections:
            if carry:
                heading = f"{carry[0]} / {heading}"
                body = f"{carry[1]}\n\n{body}"
                carry = None
            if len(body) < MIN_CHUNK:
                carry = (heading, body)
            else:
                merged.append((heading, body))

        if carry:
            if merged:
                last_heading, last_body = merged[-1]
                merged[-1] = (
                    f"{last_heading} / {carry[0]}",
                    f"{last_body}\n\n{carry[1]}",
                )
            else:
                merged.append(carry)

        index = 0
        for heading, body in merged:
            for piece in _split_long_body(body, MAX_CHUNK):
                parts = [p for p in (header, f"## {heading}", "", piece) if p != ""]
                text = "\n".join(parts).strip()
                chunks.append(
                    Chunk(
                        text=text,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::split_documents",
                    )
                )
                index += 1

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
