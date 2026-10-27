# AI4DigitalPathology Literature Skill

## Purpose

This skill helps an agent maintain and query a curated AI for Digital Pathology literature knowledge base. It is designed for repositories such as `Awesome-AI4DigitalPathology`, where papers, datasets, benchmarks, models, code repositories, and surveys are organized by research type.

The skill has two core modes:

1. **Update mode**: add newly found papers, benchmarks, datasets, models, or repositories into a fixed Markdown format and a structured JSONL index.
2. **Query mode**: answer user questions by quickly retrieving representative papers from a specified category, method type, venue, year, task, model family, or application scenario.

## When to Use This Skill

Use this skill when the user asks for:

- recent or representative papers in AI pathology, digital pathology, computational pathology, WSI analysis, pathology foundation models, pathology VLMs, pathology agents, MIL, dense prediction, multimodal pathology, spatial omics, pathology benchmarks, pathology datasets, or clinical pathology AI;
- updating a GitHub awesome-list with new papers;
- formatting new papers into the repository's fixed Markdown style;
- comparing methods within a category;
- recommending papers for a literature review, related work section, project proposal, benchmark design, or research roadmap;
- generating BibTeX, paper tables, or reading lists from the repository.

Do not use this skill for general medical diagnosis or clinical decision-making.

## Repository Scope

The target knowledge base focuses on AI for digital and computational pathology, including but not limited to:

- Surveys, Reviews, and Perspectives
- Digital Slide Scanners and File Formats
- Datasets and Benchmarks
- Multiple Instance Learning
- Federated Learning in Computational Pathology
- Patch-Level Foundation Models
- Slide-Level Foundation Models and Slide Encoders
- Cytology and Cervical Cytology in Pathology AI
- Generative Models for Computational Pathology
- Computational Pathology with Multi-Omics
- Vision-Language Models and Pathology Agents
- Dense Prediction in Computational Pathology
- Clinical Tasks and Applications
- Pathology Image Registration and Spatial Alignment
- Resources, Toolkits, and Open-Source Projects
- Future Trends and Hot Topics

## Canonical Paper Schema

For every paper or resource, normalize it into the following fields:

```json
{
  "id": "short_unique_id",
  "title": "full paper or resource title",
  "short_name": "common method/model/dataset name",
  "year": 2026,
  "venue": "CVPR / MICCAI / NeurIPS / Nature Medicine / arXiv / etc.",
  "category": "Vision-Language Models and Pathology Agents",
  "type": "paper | dataset | benchmark | code | model | survey | toolkit | website",
  "task": ["WSI classification", "VQA", "report generation"],
  "method_family": ["VLM", "MIL", "foundation model", "agent"],
  "disease_or_organ": ["digestive system", "breast", "prostate", "pan-cancer"],
  "modality": ["H&E WSI", "IHC", "spatial transcriptomics", "text"],
  "contribution": "one-sentence contribution",
  "limitation": "main limitation if known",
  "paper_url": "https://...",
  "pdf_url": "https://...",
  "conference_url": "https://...",
  "venue_status": "official_proceedings_or_program | author_reported_acceptance_official_page_pending | unknown",
  "venue_evidence_url": "https://...",
  "code_url": "https://...",
  "dataset_url": "https://...",
  "model_url": "https://...",
  "bibtex": "optional BibTeX entry",
  "tags": ["open-source", "benchmark", "multi-modal"],
  "updated_at": "YYYY-MM-DD"
}
```

## Canonical Markdown Format

When updating the README, preserve the repository's awesome-list style:

```markdown
- **ShortName** — concise one-sentence description. [![Paper](https://img.shields.io/badge/Paper-Venue%20Year-1f77b4.svg)](paper_url) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](code_url) [![Dataset](https://img.shields.io/badge/Dataset-Website-orange.svg)](dataset_url) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](model_url)
```

Rules:

- Use `ShortName` if the method/model/dataset has a widely used name; otherwise use a compact title.
- The description should be concise and functional, usually 8–18 words.
- Use consistent badges:
  - Paper: `Paper-Venue%20Year-1f77b4.svg`
  - Code: `Code-GitHub-green.svg`
  - Dataset: `Dataset-Website-orange.svg` or dataset platform name
  - Model: `Model-HuggingFace-yellow.svg`
  - Website: `Website-Leaderboard-ffb6c1.svg`
- Place each item under the most specific category. Conference-paper updates also appear in the README's venue section and the generated `VENUES.md` view.
- Link a direct PDF and official conference site when available. Record the evidence for venue attribution; distinguish author-reported acceptance from an official paper page.
- If a paper spans multiple categories, place it in the primary category and add cross-reference tags in the JSONL index.

## Update Mode Workflow

When the user asks to update the knowledge base:

1. **Determine scope**
   - Identify target category, time range, venue range, and whether the update is for papers, datasets, code, models, or benchmarks.
   - If the user gives no category, infer from keywords.

2. **Collect candidates**
   - Search or parse candidate papers from user-provided links, arXiv, PubMed, Semantic Scholar, conference proceedings, or GitHub repositories when tools are available.
   - If online search is unavailable, use only the provided text/files and say that external discovery was not performed.

3. **Filter candidates**
   - Prefer papers that are representative, influential, recent, open-source, benchmark-related, or directly relevant to pathology AI.
   - Remove duplicates and weakly related general medical AI papers unless they clearly involve pathology images or pathology-language data.

4. **Normalize fields**
   - Convert every candidate into the canonical JSON schema.
   - Extract title, short name, year, venue, URL, code/model/dataset links, method family, task, modality, and contribution.

5. **Classify category**
   - Assign one primary category from the repository taxonomy.
   - Add secondary tags for cross-category retrieval.

6. **Generate README entry**
   - Produce Markdown entries in the repository's badge style.
   - Keep descriptions short and comparable across entries.

7. **Generate index entry**
   - Produce JSONL records for retrieval.
   - Include `updated_at`.

8. **Report changes**
   - Return a compact changelog:
     - added items
     - skipped items and reason
     - uncertain metadata
     - recommended category placement

## Query Mode Workflow

When the user asks for papers:

1. Parse intent:
   - category: MIL, foundation models, VLMs, agents, dense prediction, benchmarks, datasets, etc.
   - constraints: year, venue, task, disease, modality, code availability, model availability.
   - output style: quick list, table, literature review paragraph, BibTeX, or comparison.

2. Retrieve candidates:
   - Use the structured JSONL index first.
   - If no index exists, parse the README category sections.
   - Prefer exact category matches, then tag matches, then semantic matches.

3. Rank candidates:
   - For quick answer: prioritize representative and recent papers.
   - For literature review: include canonical early works + recent state-of-the-art works.
   - For implementation: prioritize papers with code/model links.
   - For benchmark design: prioritize datasets, benchmarks, evaluation frameworks, and leaderboards.

4. Answer with fixed format:

```markdown
## Recommended Papers

| Paper | Year/Venue | Type | Why it matters | Link |
|---|---:|---|---|---|
| ShortName | 2025 / CVPR | VLM | One-sentence reason | Paper / Code |

## Reading Order
1. Foundational paper
2. Representative modern method
3. Most relevant recent extension

## How to Use in Related Work
A concise paragraph explaining how these works form a research line.
```

5. Avoid hallucination:
   - Do not invent paper titles, venues, links, or years.
   - If metadata is missing, mark it as `unknown` and suggest verification.

## Category Classification Guide

Use the following mapping:

- MIL, WSI classification, weak supervision, bag-level prediction → `Multiple Instance Learning`
- tile/patch encoders, SSL, DINO, CLIP-style patch encoders → `Patch-Level Foundation Models`
- slide encoders, WSI-level foundation models, gigapixel sequence modeling → `Slide-Level Foundation Models and Slide Encoders`
- pathology VQA, report generation, pathology LMM, WSI assistant, reasoning, agent → `Vision-Language Models and Pathology Agents`
- nucleus segmentation, tissue segmentation, cell detection, dense tasks → `Dense Prediction in Computational Pathology`
- morphology-to-omics, survival with genomics, spatial transcriptomics → `Computational Pathology with Multi-Omics`
- domain adaptation across hospitals, privacy-preserving learning, multi-center FL → `Federated Learning in Computational Pathology`
- public datasets, challenge benchmarks, leaderboards → `Datasets and Benchmarks`
- tool libraries, pipelines, viewers, preprocessing repositories → `Resources, Toolkits, and Open-Source Projects`
- cytology, Pap smear, cervical screening → `Cytology and Cervical Cytology in Pathology AI`
- stain transfer, H&E-to-IHC, synthetic pathology images, diffusion → `Generative Models for Computational Pathology`
- registration, spatial alignment, WSI matching → `Pathology Image Registration and Spatial Alignment`
- prognosis, grading, biomarker prediction, diagnosis applications → `Clinical Tasks and Applications`

## Quality Bar

Prefer adding papers/resources that satisfy at least one of:

- published in a strong venue or journal;
- influential or canonical in pathology AI;
- open-source code/model/dataset is available;
- introduces a new benchmark, dataset, evaluation protocol, or leaderboard;
- directly advances digital pathology foundation models, multimodal pathology, WSI reasoning, MIL, dense prediction, or morphology-to-omics;
- highly relevant to current research trends.

Avoid adding:

- generic medical AI papers without pathology-specific content;
- papers with unclear relation to digital pathology;
- duplicates of existing items;
- very low-quality, non-reproducible, or link-only resources unless historically important.

## Response Templates

### Fast Recommendation

```markdown
我建议优先看这几篇：

1. **ShortName** — why it is important. Paper / Code.
2. **ShortName** — why it is important. Paper / Code.
3. **ShortName** — why it is important. Paper / Code.

如果你是为了写 related work，可以按“早期方法 → foundation model → multimodal/agent”的逻辑组织。
```

### Literature Review Paragraph

```markdown
In computational pathology, prior studies have progressed from weakly supervised WSI learning to pathology-specific foundation models and, more recently, multimodal pathology-language systems. Early MIL methods focused on slide-level prediction from instance bags, while recent foundation models improve transferable patch and slide representations through large-scale self-supervised or multimodal pretraining. Current pathology VLMs and agents further extend this line by enabling report generation, visual question answering, and interactive WSI reasoning. These developments collectively indicate a shift from task-specific pathology models toward general-purpose, multimodal, and agentic pathology AI systems.
```

### README Update Changelog

```markdown
## Update Summary

Added:
- Category: `Vision-Language Models and Pathology Agents`
  - `ShortName` — reason for inclusion.

Skipped:
- `Paper X` — weak pathology relevance / duplicate / missing reliable metadata.

Need verification:
- `Paper Y` — venue or code link uncertain.
```

## Failure Handling

If the agent cannot access the internet or GitHub repository:

- Work from user-provided links, pasted text, uploaded files, or local README content.
- Clearly state that the update is based only on available local/provided information.
- Produce entries marked as `metadata_to_verify` when necessary.

If the user asks for automatic scheduled updates, explain that this requires an external scheduler such as cron, GitHub Actions, or an automation tool. Then provide the update prompt and output format.
