#!/usr/bin/env python3
"""Build a venue view from the topic README and verified 2026 paper metadata."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NEW_PAPERS = ROOT / "data/conference_papers_2026.json"
VENUES = ROOT / "VENUES.md"
BROWSER = ROOT / "venue-browser.html"
TEMPLATE = ROOT / "scripts/venue_browser_template.html"
INTRO_OVERRIDES = ROOT / "data/legacy_intro_overrides.json"
LEGACY_INTROS = json.loads(INTRO_OVERRIDES.read_text(encoding="utf-8"))
PDF_OVERRIDES = json.loads((ROOT / "data/legacy_pdf_overrides.json").read_text(encoding="utf-8"))
START = "<!-- 2026 CONFERENCE PAPERS START -->"
END = "<!-- 2026 CONFERENCE PAPERS END -->"
TOPIC_BLOCK_RE = re.compile(r"\n*<!-- 2026 TOPIC [^>]+ START -->.*?<!-- 2026 TOPIC [^>]+ END -->\n*", re.S)

CONFERENCES = {
    "AAAI", "ACM MM", "CVPR", "ECCV", "ICCV", "ICLR", "ICML", "ICIP",
    "IJCAI", "ISBI", "MICCAI", "MIDL", "ML4H", "MLMI", "NeurIPS",
    "EMNLP", "INTERSPEECH", "WACV",
}
WORKSHOPS = {"COMPAY", "CVPRW", "ECCV Workshop", "ICCV Workshop"}
PREPRINTS = {"arXiv", "bioRxiv", "medRxiv", "OpenReview", "Preprint"}
CONFERENCE_URLS = {
    "CVPR": "https://cvpr.thecvf.com/Conferences/{year}",
    "ECCV": "https://eccv.ecva.net/Conferences/{year}",
    "ICCV": "https://iccv.thecvf.com/Conferences/{year}",
    "ICLR": "https://iclr.cc/Conferences/{year}",
    "ICML": "https://icml.cc/Conferences/{year}",
    "MICCAI": "https://conferences.miccai.org/{year}/en/",
    "NeurIPS": "https://neurips.cc/Conferences/{year}",
    "AAAI": "https://aaai.org/conference/aaai/",
    "MIDL": "https://www.midl.io/",
    "WACV": "https://wacv.thecvf.com/Conferences/{year}",
}


def markdown_entry(record: dict) -> str:
    venue = record["venue"]
    year = record["year"]
    badge_venue = f"{venue}%20{year}"
    paper = (
        f"[![Paper](https://img.shields.io/badge/Paper-{badge_venue}-d62728.svg)]"
        f"({record['paper_url']})"
    )
    pdf = f"[![PDF](https://img.shields.io/badge/PDF-Open_Access-blue.svg)]({record['pdf_url']})"
    conference = (
        "[![Conference](https://img.shields.io/badge/Conference-Official-purple.svg)]"
        f"({record['conference_url']})"
    )
    evidence = ""
    if record["venue_status"] != "official_proceedings_or_program":
        evidence = f" [Author's venue statement]({record['venue_evidence_url']})"
    return f"- **{record['title']}** — {record['description']} {paper} {pdf} {conference}{evidence}"


def new_papers_block(records: list[dict]) -> str:
    lines = [
        START,
        "## 2026 Conference Papers",
        "",
        "Browse these papers together with earlier conference and journal entries in the [venue index](VENUES.md); "
        "see the [curation notes](CURATION_NOTES.md) for sources and coverage limits. "
        "Each entry has a short introduction, paper page, direct PDF and conference link. "
        "Scope: digital pathology images, histology-linked spatial omics, cytology and directly related pathology models; main-track papers only.",
        "",
    ]
    for venue in ("CVPR", "ECCV", "MICCAI", "ICML", "ICLR"):
        selected = sorted((r for r in records if r["venue"] == venue), key=lambda r: r["title"].casefold())
        lines += [f"### {venue} 2026", ""]
        if venue == "MICCAI":
            lines += [
                "**Public-availability note (2026-09-16):** The official MICCAI 2026 paper repository is not yet publicly readable. "
                "These entries have author-reported acceptance and accessible manuscripts; official paper pages remain pending. "
                "This is a verified public subset, not a complete count of all accepted MICCAI pathology papers.",
                "",
            ]
        lines.extend(markdown_entry(r) for r in selected)
        lines.append("")
    lines += [END, ""]
    return "\n".join(lines)


def add_papers_to_topics(readme: str, records: list[dict]) -> str:
    readme = TOPIC_BLOCK_RE.sub("\n\n", readme)
    by_category = defaultdict(list)
    for record in records:
        by_category[record["category"]].append(record)
    for category, papers in by_category.items():
        heading = f"## {category}\n"
        start = readme.find(heading)
        if start < 0:
            raise ValueError(f"Topic heading missing: {category}")
        next_heading = readme.find("\n## ", start + len(heading))
        section_end = next_heading if next_heading >= 0 else len(readme)
        intro_end = readme.find("</em>", start, section_end)
        insert_at = intro_end + len("</em>") if intro_end >= 0 else start + len(heading)
        marker = slug(category)
        block = [
            f"<!-- 2026 TOPIC {marker} START -->",
            "",
            "**2026 conference additions**",
            "",
        ]
        block.extend(markdown_entry(p) for p in sorted(papers, key=lambda r: (r["venue"], r["title"].casefold())))
        block += ["", f"<!-- 2026 TOPIC {marker} END -->"]
        readme = readme[:insert_at] + "\n\n" + "\n".join(block) + readme[insert_at:]
    return readme


def parse_legacy(readme: str) -> list[dict]:
    readme = re.sub(re.escape(START) + r".*?" + re.escape(END), "", readme, flags=re.S)
    readme = TOPIC_BLOCK_RE.sub("\n\n", readme)
    current_section = ""
    records = []
    seen = set()
    for line in readme.splitlines():
        if line.startswith("## "):
            current_section = line[3:].strip()
        if not line.startswith("- **") or "[![Paper]" not in line:
            continue
        badge = re.search(r"Paper-([^)]*?)\.svg", line)
        paper_url = markdown_target(line, "[![Paper]")
        title = re.search(r"^- \*\*(.*?)\*\*", line)
        if not (badge and paper_url and title):
            continue
        label = unquote(badge.group(1).rsplit("-", 1)[0])
        year_match = re.search(r"\b((?:19|20)\d{2})$", label)
        year = int(year_match.group(1)) if year_match else 0
        venue = label[: year_match.start()].strip() if year_match else label.strip()
        if not venue:
            venue = "Unspecified"
        key = (title.group(1).casefold(), paper_url)
        if key in seen:
            continue
        seen.add(key)
        records.append({
            "title": title.group(1), "venue": venue, "year": year,
            "paper_url": paper_url, "line": line,
            "category": current_section,
        })
    return records


def markdown_target(line: str, marker: str) -> str:
    """Read a Markdown link target even when the URL contains parentheses."""
    start = line.find(marker)
    if start < 0:
        return ""
    start = line.find(")](", start)
    if start < 0:
        return ""
    start += 3
    depth = 1
    for pos in range(start, len(line)):
        if line[pos] == "(":
            depth += 1
        elif line[pos] == ")":
            depth -= 1
            if depth == 0:
                return line[start:pos]
    return ""


def direct_pdf(url: str) -> str:
    if url in PDF_OVERRIDES:
        return PDF_OVERRIDES[url]
    if re.search(r"\.pdf(?:\?|$)", url, flags=re.I):
        return url
    if match := re.search(r"https?://arxiv\.org/abs/([\d.]+)(?:v\d+)?", url):
        return f"https://arxiv.org/pdf/{match.group(1)}"
    if match := re.search(r"https?://openreview\.net/forum\?id=([A-Za-z0-9_-]+)", url):
        return f"https://openreview.net/pdf?id={match.group(1)}"
    if "openaccess.thecvf.com" in url and "/html/" in url and url.endswith("_paper.html"):
        return url.replace("/html/", "/papers/").removesuffix(".html") + ".pdf"
    return ""


def legacy_line(record: dict) -> str:
    line = record["line"]
    intro = LEGACY_INTROS.get(record["title"], "")
    if intro:
        line = re.sub(r"^(- \*\*.*?\*\*)(?:\.)?(\s+)(?=\[!\[Paper\])", lambda m: f"{m.group(1)} — {intro}{m.group(2)}", line, count=1)
    pdf = direct_pdf(record["paper_url"])
    if pdf:
        line += f" [PDF]({pdf})"
    venue = record["venue"]
    year = record["year"]
    if venue in CONFERENCE_URLS and year:
        line += f" [Conference]({CONFERENCE_URLS[venue].format(year=year)})"
    if record["category"]:
        line += f" [Topic](README.md#{slug(record['category'])})"
    return line


def slug(s: str) -> str:
    s = re.sub(r"[^\w\s-]", "", s.casefold(), flags=re.UNICODE)
    return re.sub(r"\s+", "-", s.strip())


def build_venues(records: list[dict], legacy: list[dict]) -> str:
    groups = defaultdict(lambda: defaultdict(list))
    for r in records:
        groups["Conferences"][r["venue"]].append((r["year"], markdown_entry(r), r["title"]))
    for r in legacy:
        venue = r["venue"]
        family = (
            "Conferences" if venue in CONFERENCES else
            "Workshops" if venue in WORKSHOPS else
            "Preprints and unclassified venues" if venue in PREPRINTS or venue in {"PMLR", "Unspecified"} else
            "Journals"
        )
        groups[family][venue].append((r["year"], legacy_line(r), r["title"]))
    lines = [
        "# Browse AI4DigitalPathology by Venue",
        "",
        "This is an alternative view of the [topic map](README.md), generated from the existing README and verified 2026 conference records. "
        "Select a venue below, then scan papers by year. This index was checked on 2026-09-16.",
        "",
        "The 2026 CVPR, ECCV, ICML and ICLR entries link to official proceedings or program pages and direct PDFs. "
        "MICCAI 2026 entries are clearly marked by author-reported acceptance while its official paper pages are pending. "
        "Older entries retain their repository descriptions and paper links; a direct PDF is added only when the URL can be derived reliably. "
        "Some older journal PDFs still require individual verification.",
        "",
    ]
    for family in ("Conferences", "Journals", "Workshops", "Preprints and unclassified venues"):
        venues = groups.get(family, {})
        lines += [f"## {family}", ""]
        if family == "Conferences":
            order = sorted(venues, key=lambda v: (v not in {"CVPR", "ECCV", "MICCAI", "ICML", "ICLR"}, v.casefold()))
        else:
            order = sorted(venues, key=str.casefold)
        lines.append(" · ".join(f"[{v}](#{slug(v)})" for v in order))
        lines.append("")
        for venue in order:
            items = venues[venue]
            lines += [f"### {venue}", "", f"{len(items)} papers in this venue.", ""]
            years = sorted({year for year, _, _ in items}, reverse=True)
            for year in years:
                lines += [f"#### {year if year else 'Year unspecified'}", ""]
                rows = sorted((item for item in items if item[0] == year), key=lambda item: item[2].casefold())
                lines.extend(line for _, line, _ in rows)
                lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_browser(records: list[dict], legacy: list[dict]) -> str:
    entries = []
    for r in records:
        entries.append({
            "title": r["title"], "description": r["description"], "venue": r["venue"],
            "year": r["year"], "kind": "Conference", "category": r["category"],
            "paper_url": r["paper_url"], "pdf_url": r["pdf_url"],
            "venue_url": r["conference_url"], "status": r["venue_status"],
        })
    for r in legacy:
        venue = r["venue"]
        kind = (
            "Conference" if venue in CONFERENCES else "Workshop" if venue in WORKSHOPS else
            "Preprint / other" if venue in PREPRINTS or venue in {"PMLR", "Unspecified"} else "Journal"
        )
        after_title = r["line"].split("**", 2)[-1]
        description = re.split(r"\[!\[Paper\]", after_title, maxsplit=1)[0].strip(" —. ")
        if not description:
            description = LEGACY_INTROS.get(r["title"], "")
        entries.append({
            "title": r["title"], "description": description, "venue": venue,
            "year": r["year"], "kind": kind, "category": r["category"],
            "paper_url": r["paper_url"], "pdf_url": direct_pdf(r["paper_url"]),
            "venue_url": CONFERENCE_URLS[venue].format(year=r["year"]) if venue in CONFERENCE_URLS and r["year"] else "",
            "status": "legacy_readme",
        })
    payload = json.dumps(entries, ensure_ascii=False).replace("</", "<\\/")
    return TEMPLATE.read_text(encoding="utf-8").replace("__PAPER_DATA__", payload)


def main() -> None:
    records = json.loads(NEW_PAPERS.read_text(encoding="utf-8"))
    readme = README.read_text(encoding="utf-8")
    legacy = parse_legacy(readme)
    block = new_papers_block(records)
    if START in readme and END in readme:
        readme = re.sub(re.escape(START) + r".*?" + re.escape(END), block.rstrip(), readme, flags=re.S)
    else:
        readme = readme.replace("## Surveys, Reviews, and Perspectives", block + "\n## Surveys, Reviews, and Perspectives", 1)
        readme = readme.replace("- 📖 [Surveys, Reviews, and Perspectives]", "- 🏛️ [2026 Conference Papers](#2026-conference-papers)\n- 🔎 [Filter by Conference or Journal](venue-browser.html)\n- 📑 [Venue Index](VENUES.md)\n- 📖 [Surveys, Reviews, and Perspectives]", 1)
    readme = add_papers_to_topics(readme, records)
    README.write_text(readme, encoding="utf-8")
    VENUES.write_text(build_venues(records, legacy), encoding="utf-8")
    BROWSER.write_text(build_browser(records, legacy), encoding="utf-8")
    print(f"Built {VENUES.name} and {BROWSER.name}: {len(records)} new records, {len(legacy)} older entries")


if __name__ == "__main__":
    main()
