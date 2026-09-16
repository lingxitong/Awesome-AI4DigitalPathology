#!/usr/bin/env python3
"""Merge reviewed 2026 conference records into the literature JSONL index."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/conference_papers_2026.json"
TARGET = ROOT / "ai4pathology_literature_skill/data/papers.jsonl"


def key(title: str) -> str:
    return re.sub(r"[^a-z0-9]", "", title.casefold())


def main() -> None:
    existing = [json.loads(line) for line in TARGET.read_text(encoding="utf-8").splitlines() if line.strip()]
    by_title = {key(item["title"]): item for item in existing}
    changed = 0
    added = 0
    for paper in json.loads(SOURCE.read_text(encoding="utf-8")):
        identity = key(paper["title"])
        item = by_title.get(identity)
        if item is None:
            item = {
                "id": paper["id"], "title": paper["title"], "short_name": "",
                "year": 2026, "venue": paper["venue"], "category": paper["category"],
                "type": "paper", "task": [], "method_family": [], "disease_or_organ": [],
                "modality": [], "contribution": paper["description"],
                "paper_url": paper["paper_url"], "code_url": "", "dataset_url": "",
                "model_url": "", "tags": [paper["venue"].lower(), "2026"],
                "source": "official_venue" if paper["venue_status"] == "official_proceedings_or_program" else "author_venue_statement",
                "arxiv_id": "", "updated_at": paper["updated_at"],
            }
            existing.append(item)
            by_title[identity] = item
            added += 1
        else:
            if item.get("venue") != paper["venue"]:
                item["previous_venue"] = item.get("venue", "")
                item["previous_paper_url"] = item.get("paper_url", "")
                changed += 1
        item.update({
            "year": 2026, "venue": paper["venue"], "category": paper["category"],
            "contribution": paper["description"], "paper_url": paper["paper_url"],
            "pdf_url": paper["pdf_url"], "conference_url": paper["conference_url"],
            "venue_status": paper["venue_status"],
            "venue_evidence_url": paper["venue_evidence_url"],
            "updated_at": paper["updated_at"],
        })
    TARGET.write_text("\n".join(json.dumps(item, ensure_ascii=False) for item in existing) + "\n", encoding="utf-8")
    print(f"Index updated: {added} added, {changed} previous preprints given conference metadata")


if __name__ == "__main__":
    main()
