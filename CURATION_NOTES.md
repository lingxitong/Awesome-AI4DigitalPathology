# 2026 Conference Update: Review Notes

Checked on **2026-09-16**. The new conference list contains **66** digital-pathology-related papers: CVPR 27, ECCV 13, ICML 11, ICLR 7 and MICCAI 8. The first four counts come from official proceedings or conference paper/program pages. The MICCAI count is a **publicly verifiable subset** based on author statements and accessible manuscripts; it is not a complete count of accepted main-conference pathology papers.

The selection includes histopathology and whole-slide images, cytology, tissue microscopy, virtual staining, and spatial-omics methods that use histology images. Generic medical imaging, radiology-only work, CT "pathology" segmentation, pure spatial-omics methods without pathology images, and conference workshops were excluded. Candidates were found by screening titles in the conference lists and checking their abstracts; a title-based sweep can miss papers with non-obvious names, so none of these counts should be read as exhaustive census figures.

Primary lists and status references:

- [CVPR 2026 open-access papers](https://openaccess.thecvf.com/CVPR2026?day=all)
- [ECCV 2026 accepted papers](https://eccv.ecva.net/Conferences/2026/AcceptedPapers)
- [ICML 2026 papers](https://icml.cc/virtual/2026/papers.html)
- [ICLR 2026 proceedings](https://proceedings.iclr.cc/paper_files/paper/2026)
- [MICCAI 2026 conference program](https://conferences.miccai.org/2026/en/PROGRAM.html)
- [MICCAI Society's September 2026 update](https://miccai.org/2026/09/07/miccai-quarterly-fall-september-2026/)

Every new record has a paper/manuscript page, direct PDF, conference link, short introduction, primary topic and venue-evidence URL in [`data/conference_papers_2026.json`](data/conference_papers_2026.json). The 2026 CVPR, ECCV, ICLR and ICML paper and venue pages responded during link checks. The direct PDFs from CVPR, ECCV and ICLR also responded. OpenReview blocked automated HTTP checks for all 11 ICML PDFs, but their standard PDF URLs use the IDs linked from the official ICML paper pages. The MICCAI 2026 paper repository was not publicly readable at review time; these rows carry the explicit status `author_reported_acceptance_official_page_pending` and link to each author's venue statement.

The [venue index](VENUES.md) and [local filter](venue-browser.html) also reuse 388 older topic-map entries after removing exact duplicate title-and-paper-link pairs. Eighteen older survey/review rows that lacked an introduction received a short one-line description in the venue view. For older journal rows, 47 direct PDFs were extracted from publisher or PMC metadata and confirmed to return `application/pdf`; 31 candidate PDF URLs were discarded because they returned HTML instead. Other older journal rows retain their paper pages until a stable PDF can be confirmed.

Run `python3 scripts/sync_2026_index.py` after changing the reviewed 2026 metadata, then `python3 scripts/build_venue_index.py` to refresh the README venue section, venue index and local filter. No remote changes were made.
