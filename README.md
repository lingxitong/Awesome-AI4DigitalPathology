# Awesome-AI4DigitalPathology

<div align="center">


[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Digital Pathology](https://img.shields.io/badge/Topic-Digital%20Pathology-8A2BE2.svg)](#)
[![License](https://img.shields.io/badge/License-CC0_1.0-blue.svg)](LICENSE.txt)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**📜 A Curated List of Awesome Works in AI4DigitalPathology, Aiming to Serve as a One-stop Resource for Researchers, Practitioners, and Enthusiasts Interested in AI4DigitalPathology.**  
*Focused on papers, benchmarks, datasets, and open-source repositories for modern digital pathology.*

<p align="center">
  <img src="assets/ACPATH-logo.png" alt="Awesome World Models" width="100%" style="border-radius: 15px; box-shadow: 0 4px 24px rgba(0,0,0,.1); margin: 5px 0;">
</p>


*Photo Credit: [Gemini-Nano-Banana🍌](https://aistudio.google.com/models/gemini-2-5-flash-image)*.
</div>

---

## 🚩 News & Updates

_Major updates and repository announcements are shown below._

🚧 **[Ongoing] Repository Refocus** — This list is being rebuilt around **AI4DigitalPathology**, with the original awesome-list visual style preserved.

💡 **[Ongoing] Contributions Welcome** — If you would like to add missing papers, repos, or benchmarks, feel free to open a PR.

📌 **[Ongoing] Repository Support** — If this list helps your research, consider sharing the repository and citing it in your own awesome lists.

---

## Overview

- 🎯 [Aim of the Project](#aim-of-the-project)
- 📖 [Surveys, Reviews, and Perspectives](#surveys-reviews-and-perspectives)
- 🖨️ [Digital Slide Scanners and File Formats](#digital-slide-scanners-and-file-formats)
- 🗂️ [Datasets and Benchmarks](#datasets-and-benchmarks)
- 🧩 [Multiple Instance Learning](#multiple-instance-learning)
- 🌐 [Federated Learning in Computational Pathology](#federated-learning-in-computational-pathology)
- 🤖 [Patch-Level Foundation Models](#patch-level-foundation-models)
- 🖼️ [Slide-Level Foundation Models and Slide Encoders](#slide-level-foundation-models-and-slide-encoders)
- 🧫 [Cytology and Cervical Cytology in Pathology AI](#cytology-and-cervical-cytology-in-pathology-ai)
- 🎨 [Generative Models for Computational Pathology](#generative-models-for-computational-pathology)
- 🧬 [Computational Pathology with Multi-Omics](#computational-pathology-with-multi-omics)
- 💬 [Vision-Language Models and Pathology Agents](#vision-language-models-and-pathology-agents)
- 🧱 [Dense Prediction in Computational Pathology](#dense-prediction-in-computational-pathology)
- 🏥 [Clinical Tasks and Applications](#clinical-tasks-and-applications)
- 🧭 [Pathology Image Registration and Spatial Alignment](#pathology-image-registration-and-spatial-alignment)
- 🚀 [Resources, Toolkits, and Open-Source Projects](#resources-toolkits-and-open-source-projects)
- 🔭 [Future Trends and Hot Topics](#future-trends-and-hot-topics)
- 🙏 [Acknowledgements](#acknowledgements)
- 📝 [Citation](#citation)

---

## Aim of the Project

Computational pathology has rapidly evolved from handcrafted image analysis pipelines to **whole-slide learning**, **foundation models**, **multimodal pathology-language systems**, and **morphology-to-omics prediction**.  
At the same time, the literature has become fragmented across pathology, machine learning, computer vision, spatial biology, and multimodal AI.

This repository aims to:

- 🔍 **Organize** representative papers, datasets, toolkits, and repositories in computational pathology
- 🗺️ **Provide** a clean map of the field from classical WSI learning to modern foundation models
- 🤝 **Bridge** communities working on digital pathology, multimodal medicine, spatial biology, and medical AI
- 📚 **Serve** as a compact reading list for new researchers and a practical reference for experienced practitioners
- 🚀 **Track** open-source progress in pathology AI, especially around benchmarks and reproducibility

---

## Surveys, Reviews, and Perspectives

<em>Surveys, reviews, and perspectives that summarize the evolution, challenges, and future directions of computational pathology.</em>

- **Computational Pathology: Challenges and Promises**. [![Paper](https://img.shields.io/badge/Paper-CMIG%202011-1f77b4.svg)](https://www.sciencedirect.com/science/article/abs/pii/S0895611111000383)
- **Digital Pathology and Artificial Intelligence**. [![Paper](https://img.shields.io/badge/Paper-Lancet%20Oncol%202019-1f77b4.svg)](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045%2819%2930154-8/abstract)
- **AI in Digital Pathology for Precision Oncology**. [![Paper](https://img.shields.io/badge/Paper-Nat%20Rev%20Clin%20Oncol%202019-1f77b4.svg)](https://www.nature.com/articles/s41571-019-0252-y)
- **Computational Pathology White Paper**. [![Paper](https://img.shields.io/badge/Paper-J%20Pathol%202019-1f77b4.svg)](https://pathsocjournals.onlinelibrary.wiley.com/doi/10.1002/path.5331)
- **Digital Pathology in Nephropathology**. [![Paper](https://img.shields.io/badge/Paper-Nat%20Rev%20Nephrol%202020-1f77b4.svg)](https://www.nature.com/articles/s41581-020-0321-6)
- **Artificial Intelligence and Computational Pathology**. [![Paper](https://img.shields.io/badge/Paper-Lab%20Invest%202021-1f77b4.svg)](https://www.nature.com/articles/s41374-020-00514-0)
- **Digital Pathology in Translational Medicine**. [![Paper](https://img.shields.io/badge/Paper-Mod%20Pathol%202022-1f77b4.svg)](https://www.nature.com/articles/s41379-021-00919-2)
- **AI in Computational Pathology of Cancer**. [![Paper](https://img.shields.io/badge/Paper-Ann%20Rev%20Cancer%20Biol%202023-1f77b4.svg)](https://www.annualreviews.org/content/journals/10.1146/annurev-cancerbio-061521-092038)
- **Computational Pathology in 2030**. [![Paper](https://img.shields.io/badge/Paper-EBioMedicine%202023-1f77b4.svg)](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964%2822%2900609-0/fulltext)
- **AI for Digital and Computational Pathology**. [![Paper](https://img.shields.io/badge/Paper-Nat%20Rev%20Bioeng%202023-1f77b4.svg)](https://www.nature.com/articles/s44222-023-00096-8)
- **Applications of Digital Pathology in Cancer**. [![Paper](https://img.shields.io/badge/Paper-Ann%20Rev%20Cancer%20Biol%202024-1f77b4.svg)](https://www.annualreviews.org/content/journals/10.1146/annurev-cancerbio-062822-010523)
- **Explainable AI for Precision Pathology**. [![Paper](https://img.shields.io/badge/Paper-Ann%20Rev%20Pathol%202024-1f77b4.svg)](https://www.annualreviews.org/content/journals/10.1146/annurev-pathmechdis-051222-113147)
- **AI in Digital Pathology: Diagnostic Meta-analysis**. [![Paper](https://img.shields.io/badge/Paper-npj%20Digit%20Med%202024-1f77b4.svg)](https://www.nature.com/articles/s41746-024-01106-8)
- **Pathology in the Era of Generative AI**. [![Paper](https://img.shields.io/badge/Paper-Lancet%20Digit%20Health%202024-1f77b4.svg)](https://www.thelancet.com/journals/landig/article/PIIS2589-7500%2824%2900157-2/fulltext)
- **Artificial Intelligence in Pathology**. [![Paper](https://img.shields.io/badge/Paper-Ann%20Rev%20Biomed%20Data%20Sci%202025-1f77b4.svg)](https://www.annualreviews.org/content/journals/10.1146/annurev-biodatasci-103123-095814)
- **AI and Digital Tools in Cancer Pathology**. [![Paper](https://img.shields.io/badge/Paper-Lancet%20Digit%20Health%202025-1f77b4.svg)](https://www.thelancet.com/journals/landig/article/PIIS2589-7500%2825%2900115-3/fulltext)
---

## Digital Slide Scanners and File Formats

<em>Digital slide scanners, image formats, and technical standards that support whole-slide imaging acquisition, storage, and interoperability.</em>

- **OpenSlide** — open-source library for reading WSI formats across scanner vendors. [![Paper](https://img.shields.io/badge/Paper-JPI%202013-1f77b4.svg)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3815078/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/openslide/openslide)
- **opensdpc** — Python library for processing SDPC whole-slide images. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/WonderLandxD/opensdpc)
- **Bio-Formats** — library for reading and converting microscopy formats. [![Paper](https://img.shields.io/badge/Paper-Nat%20Methods%202010-1f77b4.svg)](https://www.nature.com/articles/nmeth.1426) [![Website](https://img.shields.io/badge/Website-OME-ffb6c1.svg)](https://www.openmicroscopy.org/bio-formats/)
- **DICOM WSI** — standard for digital pathology image interoperability. [![Paper](https://img.shields.io/badge/Paper-JDI%202018-1f77b4.svg)](https://link.springer.com/article/10.1007/s10278-017-0034-3) [![Website](https://img.shields.io/badge/Website-NEMA-ffb6c1.svg)](https://dicom.nema.org/dicom/dicomwsi/)
---

## Datasets and Benchmarks

<em>Representative datasets and evaluation benchmarks for computational pathology.</em>

- **TCGA** — multi-cancer WSIs + clinical/molecular. [![Dataset](https://img.shields.io/badge/Dataset-GDC-orange.svg)](https://portal.gdc.cancer.gov/)
- **CPTAC** — proteogenomic + histology cohorts. [![Dataset](https://img.shields.io/badge/Dataset-CPTAC-orange.svg)](https://proteomics.cancer.gov/programs/cptac)
- **CAMELYON16** — lymph node metastasis detection. [![Dataset](https://img.shields.io/badge/Dataset-CAMELYON16-orange.svg)](https://camelyon16.grand-challenge.org/Data/)
- **CAMELYON17** — WSI and patient-level metastasis. [![Dataset](https://img.shields.io/badge/Dataset-CAMELYON17-orange.svg)](https://camelyon17.grand-challenge.org/)
- **PANDA** — prostate cancer grading benchmark. [![Dataset](https://img.shields.io/badge/Dataset-PANDA-orange.svg)](https://panda.grand-challenge.org/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DIAGNijmegen/panda-challenge)
- **PatchCamelyon (PCam)** — patch metastasis classification. [![Dataset](https://img.shields.io/badge/Dataset-PCam-orange.svg)](https://github.com/basveeling/pcam)
- **MHIST** — colorectal polyp classification. [![Dataset](https://img.shields.io/badge/Dataset-MHIST-orange.svg)](https://bmirds.github.io/MHIST/)
- **NCT-CRC-HE-100K** — 100k colorectal patches. [![Dataset](https://img.shields.io/badge/Dataset-Zenodo-orange.svg)](https://zenodo.org/record/1214456)
- **BCNB** — breast cancer nodule and biomarker dataset. [![Dataset](https://img.shields.io/badge/Dataset-Website-orange.svg)](https://bupt-ai-cz.github.io/BCNB/)
- **MUT-HET-RCC** — intra-tumor heterogeneity and mutation dataset. [![Dataset](https://img.shields.io/badge/Dataset-Figshare-orange.svg)](https://doi.org/10.25452/figshare.plus.c.5983795)
- **HER2-Tumor-ROIs** — annotated ROIs for HER2 scoring. [![Dataset](https://img.shields.io/badge/Dataset-TCIA-orange.svg)](https://www.cancerimagingarchive.net/collection/her2-tumor-rois/)
- **EBRAINS** — ultra-high-resolution whole-slide brain mapping. [![Dataset](https://img.shields.io/badge/Dataset-EBRAINS-orange.svg)](https://doi.org/10.25493/WQ48-ZGX)
- **VisioMel** — melanoma and lymph node metastasis dataset. [![Dataset](https://img.shields.io/badge/Dataset-DrivenData-orange.svg)](https://www.drivendata.org/competitions/148/visiomel-melanoma/)
- **IMP** — multi-institutional cervical and tissue data. [![Dataset](https://img.shields.io/badge/Dataset-INESC%20TEC-orange.svg)](https://rdm.inesctec.pt/dataset/nis-2023-008)
- **Selected Cohorts** — CPTAC multi-cancer cohorts. [![Dataset](https://img.shields.io/badge/Dataset-TCIA-orange.svg)](https://www.cancerimagingarchive.net/collections/)
- **AGGC2022** — large-scale prostate Gleason scoring. [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://aggc22.grand-challenge.org/)
- **TIGER** — breast TIL segmentation and scoring. [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://tiger.grand-challenge.org/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DIAGNijmegen/tiger-challenge-eval)
- **GlaS** — colon gland instance segmentation. [![Paper](https://img.shields.io/badge/Paper-MedIA%202017-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841516301736) [![Dataset](https://img.shields.io/badge/Dataset-Warwick-orange.svg)](https://warwick.ac.uk/fac/cross_fac/tia/data/glascontest/)
- **TCGA-TIL Maps** — pan-cancer TIL spatial maps. [![Paper](https://img.shields.io/badge/Paper-Cell%20Reports%202018-1f77b4.svg)](https://www.cell.com/cell-reports/fulltext/S2211-1247(18)31438-5) [![Dataset](https://img.shields.io/badge/Dataset-TCIA-orange.svg)](https://www.cancerimagingarchive.net/analysis-result/til-maps/)
- **BACH** — breast cancer classification and segmentation. [![Paper](https://img.shields.io/badge/Paper-MedIA%202019-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841518301789) [![Dataset](https://img.shields.io/badge/Dataset-Website-orange.svg)](https://iciar2018-challenge.grand-challenge.org/)
- **MoNuSeg** — multi-organ nucleus segmentation. [![Paper](https://img.shields.io/badge/Paper-TMI%202020-1f77b4.svg)](https://ieeexplore.ieee.org/document/8880654) [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://monuseg.grand-challenge.org/)
- **SICAPv2** — prostate cancer Gleason grading. [![Paper](https://img.shields.io/badge/Paper-JBHI%202020-1f77b4.svg)](https://ieeexplore.ieee.org/document/9144365) [![Dataset](https://img.shields.io/badge/Dataset-Mendeley-orange.svg)](https://data.mendeley.com/datasets/9xxm58dvs3/1)
- **UniToPatho** — colon cancer with class imbalance and domain shift. [![Paper](https://img.shields.io/badge/Paper-ECCV%202020-d62728.svg)](https://arxiv.org/abs/2009.00650) [![Dataset](https://img.shields.io/badge/Dataset-Zenodo-orange.svg)](https://zenodo.org/record/3934241)
- **NADT-Prostate** — prostate cancer with androgen-deprivation therapy. [![Paper](https://img.shields.io/badge/Paper-medRxiv%202020-6A5ACD.svg)](https://www.medrxiv.org/content/10.1101/2020.09.29.20199711v1)
- **MoNuSAC2020** — multi-organ nuclei segmentation and classification. [![Paper](https://img.shields.io/badge/Paper-TMI%202021-1f77b4.svg)](https://ieeexplore.ieee.org/document/9446924) [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://monusac-2020.grand-challenge.org/)
- **Lizard** — large-scale colonic nuclei benchmark. [![Paper](https://img.shields.io/badge/Paper-ICCV%202021-d62728.svg)](https://openaccess.thecvf.com/content/ICCV2021/html/Graham_Lizard_A_Large-Scale_Dataset_for_Colonic_Nuclear_Instance_Segmentation_and_Classification_ICCV_2021_paper.html)
- **PAIP** — liver cancer segmentation and survival prediction. [![Paper](https://img.shields.io/badge/Paper-MedIA%202021-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841521000577) [![Dataset](https://img.shields.io/badge/Dataset-Website-orange.svg)](https://paip2019.grand-challenge.org/)
- **TissueNet** — large-scale cell segmentation across modalities. [![Paper](https://img.shields.io/badge/Paper-Nat%20Methods%202021-1f77b4.svg)](https://www.nature.com/articles/s41592-021-01249-6) [![Dataset](https://img.shields.io/badge/Dataset-DeepCell-orange.svg)](https://datasets.deepcell.org/)
- **BRACS** — breast carcinoma subtyping. [![Paper](https://img.shields.io/badge/Paper-Sci%20Data%202022-1f77b4.svg)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575967/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/histocartography/hact-net)
- **CoNIC** — colon nuclei identification and counting. [![Paper](https://img.shields.io/badge/Paper-MedIA%202022-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841522000755) [![Dataset](https://img.shields.io/badge/Dataset-Zenodo-orange.svg)](https://zenodo.org/record/6559981)
- **OV-Bevacizumab** — multimodal ovarian cancer response dataset. [![Paper](https://img.shields.io/badge/Paper-Sci%20Data%202022-1f77b4.svg)](https://www.nature.com/articles/s41597-022-01127-6)
- **BCI** — H&E to IHC translation benchmark. [![Paper](https://img.shields.io/badge/Paper-CVPR%202022-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Liu_Translating_From_HE_to_IHC_A_New_Trajectory_for_Translational_CVPR_2022_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/bupt-ai-cz/BCI)
- **EBHI-Seg** — digestive tumor segmentation. [![Paper](https://img.shields.io/badge/Paper-Sci%20Data%202022-1f77b4.svg)](https://www.nature.com/articles/s41597-022-01435-y) [![Dataset](https://img.shields.io/badge/Dataset-Figshare-orange.svg)](https://figshare.com/articles/dataset/EBHI-Seg/19602495)
- **HEROHE** — HER2 status prediction from routine H&E. [![Paper](https://img.shields.io/badge/Paper-MedIA%202022-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841521002369) [![Dataset](https://img.shields.io/badge/Dataset-Website-orange.svg)](https://herohe.inesctec.pt/)
- **DigestPath** — colonoscopytissue segmentation. [![Paper](https://img.shields.io/badge/Paper-MedIA%202022-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841521003571) [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://digestpath2019.grand-challenge.org/)
- **OCELOT** — cell detection with tissue context. [![Paper](https://img.shields.io/badge/Paper-CVPR%202023-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Ryu_OCELOT_Overlapping_Cell_on_Tissue_Dataset_for_Histopathology_CVPR_2023_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lunit-io/ocelot-benchmark)
- **Benchmarking SSL on Pathology** — SSL benchmarking across pathology datasets. [![Paper](https://img.shields.io/badge/Paper-CVPR%202023-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Kang_Benchmarking_Self-Supervised_Learning_on_Diverse_Pathology_Datasets_CVPR_2023_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lunit-io/benchmark-ssl-pathology)
- **EVA** — evaluation framework for oncology foundation models. [![Paper](https://img.shields.io/badge/Paper-MIDL%202024-d62728.svg)](https://openreview.net/forum?id=FNBQOPj18N) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/kaiko-ai/eva)
- **HEST-1k / HEST-Benchmark** — wsi and spatial transcriptomics benchmark. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202024-d62728.svg)](https://arxiv.org/abs/2406.16192) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/MahmoodLab/hest)
- **PathMMU** — pathology large multimodal model benchmark. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2401.16355) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathMMU-Benchmark/PathMMU) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/jamessyx/PathMMU)
- **KidRare** — pediatric rare tumor WSI dataset. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202026-1f77b4.svg)](https://doi.org/10.1038/s41467-026-71715-2) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/Firehdx233/KidRare)
- **HISTAI** — open-access WSI resource with models. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2505.12120) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/HistAI/HISTAI)
- **PLISM Benchmark** — robustness benchmark for pathology foundation models. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-d62728.svg)](https://arxiv.org/abs/2506.19674) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/owkin/plism-benchmark)
- **PFM-DenseBench** — dense prediction benchmark for pathology foundation models. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2602.03887) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lingxitong/PFM_Segmentation)
- **PathBench** — multi-task and multi-organ foundation-model benchmark. [![Website](https://img.shields.io/badge/Website-Leaderboard-ffb6c1.svg)](https://birkhoffkiki.github.io/PathBench/)
- **Patho-Bench** — standardized pathology foundation-model benchmark. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/Patho-Bench)
- **HistoBoard** — unified dashboard for pathology foundation model benchmarks. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/wearewaiv/histoboard) [![Website](https://img.shields.io/badge/Website-Leaderboard-ffb6c1.svg)](https://wearewaiv.github.io/histoboard/)
- **Stanford PathBench** — pathology foundation model benchmark and leaderboard. [![Website](https://img.shields.io/badge/Website-Leaderboard-ffb6c1.svg)](https://pathbench.stanford.edu/)
- **Sinai Benchmark** — tile-level SSL benchmark for pathology foundation models. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/sinai-computational-pathology/SSL_tile_benchmarks)
- **STAMP** — solid tumor associative modeling benchmark in pathology. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/KatherLab/STAMP-Benchmark)
- **THUNDER** — benchmark for classification, calibration, robustness, and segmentation. [![Website](https://img.shields.io/badge/Website-Leaderboard-ffb6c1.svg)](https://mics-lab.github.io/thunder/)
- **PathoROB** — robustness benchmark for pathology foundation models. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/bifold-pathomics/PathoROB)
- **MindLab-DP/Datasets** — practical collection of digital pathology datasets. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MindLab-DP/Datasets)
- **TCGA Processing Pipeline for MIL** — WSI preprocessing for weak supervision. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/liupei101/Pipeline-Processing-TCGA-Slides-for-MIL)
---

## Multiple Instance Learning

<em>Multiple instance learning methods for weakly supervised whole-slide image analysis.</em>

- **ABMIL** — attention-based deep multiple instance learning. [![Paper](https://img.shields.io/badge/Paper-arXiv%202018-6A5ACD.svg)](https://arxiv.org/abs/1802.04712) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/AMLab-Amsterdam/AttentionDeepMIL)
- **Clinical-grade WSI** — large-scale weakly supervised WSI classification. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202019-1f77b4.svg)](https://www.nature.com/articles/s41591-019-0508-1)
- **CAMEL** — weakly supervised WSI segmentation via class activation maps. [![Paper](https://img.shields.io/badge/Paper-ICCV%202019-d62728.svg)](https://openaccess.thecvf.com/content_ICCV_2019/html/Li_Camel_A_Weakly_Supervised_Learning_Framework_for_Histopathology_Image_Segmentation_ICCV_2019_paper.html)
- **DeepAttnMISL** — multi-scale attention-guided MIL for WSI survival prediction. [![Paper](https://img.shields.io/badge/Paper-MedIA%202020-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841520301535) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/uta-smile/DeepAttnMISL)
- **CLAM** — clustering-constrained attention MIL for WSI classification. [![Paper](https://img.shields.io/badge/Paper-Nat%20BME%202021-1f77b4.svg)](https://www.nature.com/articles/s41551-020-00682-w) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CLAM)
- **DSMIL** — dual-stream MIL for WSI classification. [![Paper](https://img.shields.io/badge/Paper-CVPR%202021-d62728.svg)](https://arxiv.org/abs/2011.08939) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/binli123/dsmil-wsi)
- **Patch-GCN** — graph-based context-aware WSI survival modeling. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202021-d62728.svg)](https://arxiv.org/abs/2107.13048) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/Patch-GCN)
- **DT-MIL** — deformable transformer for MIL on histopathology. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202021-d62728.svg)](https://link.springer.com/chapter/10.1007/978-3-030-87240-3_34) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/yfzon/DT-MIL)
- **SparseConvMIL** — sparse convolutional context-aware MIL. [![Paper](https://img.shields.io/badge/Paper-COMPAY%202021-d62728.svg)](https://proceedings.mlr.press/v156/lerousseau21a.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MarvinLer/SparseConvMIL)
- **TransMIL** — correlated MIL with transformers. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202021-d62728.svg)](https://proceedings.neurips.cc/paper/2021/hash/10c272d06794d3e5785d5e7c5356e9ff-Abstract.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/szc19990412/TransMIL)
- **ReMix** — general MIL data augmentation method for WSIs. [![Paper](https://img.shields.io/badge/Paper-ICCV%202021-d62728.svg)](https://openaccess.thecvf.com/content/ICCV2021/html/Yang_ReMix_Towards_Image_Mixup_for_Whole_Slide_Image_Classification_ICCV_2021_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Jiawei-Yang/ReMix)
- **HIPT** — hierarchical transformer for gigapixel pathology. [![Paper](https://img.shields.io/badge/Paper-CVPR%202022-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_Scaling_Vision_Transformers_to_Gigapixel_Images_via_Hierarchical_Self-Supervised_Learning_CVPR_2022_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HIPT)
- **DTFD-MIL** — double-tier feature distillation MIL. [![Paper](https://img.shields.io/badge/Paper-CVPR%202022-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Zhang_DTFD-MIL_Double-Tier_Feature_Distillation_Multiple_Instance_Learning_for_Histopathology_Whole_CVPR_2022_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/hrzhang1123/DTFD-MIL)
- **ZoomMIL** — differentiable zooming for MIL on whole-slide images. [![Paper](https://img.shields.io/badge/Paper-ECCV%202022-d62728.svg)](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136810689.pdf) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/histocartography/zoommil)
- **IBMIL** — intervention-based MIL for deconfounded WSI prediction. [![Paper](https://img.shields.io/badge/Paper-CVPR%202022-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Lin_Interventional_Multi-Instance_Learning_with_Deconfounded_Instance-Level_Prediction_CVPR_2022_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TencentAILabHealthcare/IBMIL)
- **GTP** — graph-transformer fusion for WSI classification. [![Paper](https://img.shields.io/badge/Paper-TMI%202022-1f77b4.svg)](https://ieeexplore.ieee.org/document/9779215) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/vkola-lab/tmi2022)
- **MHIM-MIL** — masked hard instance mining for WSI classification. [![Paper](https://img.shields.io/badge/Paper-ICCV%202023-d62728.svg)](https://arxiv.org/abs/2307.15254) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DearCaat/MHIM-MIL)
- **ILRA-MIL** — low-rank MIL for WSI classification. [![Paper](https://img.shields.io/badge/Paper-ICLR%202023-d62728.svg)](https://openreview.net/forum?id=8hH4Q3f8c2) [![Code](https://img.shields.io/badge/Code-MIL__BASELINE-green.svg)](https://github.com/lingxitong/MIL_BASELINE)
- **LNPL-MIL** — learning from noisy pseudo labels for WSI MIL. [![Paper](https://img.shields.io/badge/Paper-ICCV%202023-d62728.svg)](https://openaccess.thecvf.com/content/ICCV2023/html/Shao_LNPL-MIL_Learning_from_Noisy_Pseudo_Labels_for_Promoting_Multiple_Instance_ICCV_2023_paper.html)
- **MILBooster** — boosting WSI classification via distribution and correlation. [![Paper](https://img.shields.io/badge/Paper-ICCV%202023-d62728.svg)](https://openaccess.thecvf.com/content/ICCV2023/html/Qu_Boosting_Whole_Slide_Image_Classification_from_the_Perspectives_of_Distribution_ICCV_2023_paper.html)
- **PromptMIL** — prompting language-image models for pathology MIL. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202023-d62728.svg)](https://arxiv.org/abs/2303.03362) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Zhenghui-Wu/PromptMIL)
- **S4MIL** — structured state space models for pathology MIL. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202023-d62728.svg)](https://conferences.miccai.org/2023/papers/622-Paper3313.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MICS-Lab/s4_digital_pathology)
- **WiKG** — whole-slide image as a knowledge graph. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-d62728.svg)](https://arxiv.org/abs/2403.07719) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/WonderLandxD/WiKG)
- **CA-MIL** — context-aware MIL for WSI classification. [![Paper](https://img.shields.io/badge/Paper-ICLR%202024-d62728.svg)](https://openreview.net/forum?id=rzBskAEmoc) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/olgarithmics/ICLR_CAMIL)
- **AC-MIL** — attention-challenging MIL. [![Paper](https://img.shields.io/badge/Paper-ECCV%202024-d62728.svg)](https://arxiv.org/abs/2403.05351) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/dazhangyu123/ACMIL)
- **LongMIL** — long-contextual MIL for WSI analysis. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202024-d62728.svg)](https://arxiv.org/abs/2410.14195) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/invoker-LL/Long-MIL)
- **RRT-MIL** — feature re-embedding for WSI analysis. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Tang_Feature_Re-Embedding_Towards_Foundation_Model-Level_Performance_in_Computational_Pathology_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DearCaat/RRT-MIL)
- **RetMIL** — retentive MIL for long histopathology sequences. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202024-d62728.svg)](https://papers.miccai.org/miccai-2024/657-Paper1723.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Hongbo-Chu/RetMIL)
- **MambaMIL** — Mamba-based long-sequence MIL. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202024-d62728.svg)](https://arxiv.org/abs/2403.06800) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/isyangshu/MambaMIL)
- **cDP-MIL** — robust MIL via cascaded Dirichlet process. [![Paper](https://img.shields.io/badge/Paper-ECCV%202024-d62728.svg)](https://arxiv.org/abs/2407.11448) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/HKU-MedAI/cDPMIL)
- **ViLa-MIL** — dual-scale vision-language MIL for WSI classification. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Shi_ViLa-MIL_Dual-scale_Vision-Language_Multiple_Instance_Learning_for_Whole_Slide_Image_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Jiangbo-Shi/ViLa-MIL)
- **SI-MIL** — self-interpretable MIL for gigapixel histopathology. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Bhattacharya_SI-MIL_Taming_Deep_MIL_for_Self-Interpretability_in_Gigapixel_Histopathology_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/bmi-imaginelab/SI-MIL)
- **FG-VSI** — fine-grained visual-semantic WSI classification. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Generalizable_Whole_Slide_Image_Classification_with_Fine-Grained_Visual-Semantic_Interaction_CVPR_2024_paper.html)
- **AMD-MIL** — agent aggregator with mask denoise for WSI analysis. [![Paper](https://img.shields.io/badge/Paper-ACM%20MM%202024-d62728.svg)](https://arxiv.org/abs/2409.11664) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/sigsminx/AMD-MIL)
- **SAM-MIL** — spatial contextual aware MIL with SAM guidance. [![Paper](https://img.shields.io/badge/Paper-ACM%20MM%202024-d62728.svg)](https://dl.acm.org/doi/10.1145/3664647.3681534) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/FangHeng/SAM-MIL)
- **DGR-MIL** — diverse global representation learning for robust WSI MIL. [![Paper](https://img.shields.io/badge/Paper-ECCV%202024-d62728.svg)](https://arxiv.org/abs/2407.03575) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ChongQingNoSubway/DGR-MIL)
- **FR-MIL** — distribution re-calibration MIL with Transformer. [![Paper](https://img.shields.io/badge/Paper-TMI%202025-1f77b4.svg)](https://pubmed.ncbi.nlm.nih.gov/39163176/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PhilipChicco/FRMIL)
- **HMIL** — hierarchical MIL for fine-grained WSI classification. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2411.07660) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ChengJin-git/HMIL)
- **PseMix** — pseudo-bag mixup augmentation for MIL-based WSI classification. [![Paper](https://img.shields.io/badge/Paper-TMI%202024-1f77b4.svg)](https://arxiv.org/abs/2306.16180) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/liupei101/PseMix)
- **Lin-MIL** — linear attention MIL for scalable WSI analysis. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2502.13417) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/charlotterchtr/Lin-MIL)
- **PackMIL** — pack-based MIL training framework for pathology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2502.12917) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/FangHeng/PackMIL)
- **Flow-MIL** — normalizing-flow latent feature space for WSI classification. [![Paper](https://img.shields.io/badge/Paper-ICCV%202025-d62728.svg)](https://openaccess.thecvf.com/content/ICCV2025/html/Ma_Flow-MIL_Constructing_Highly-expressive_Latent_Feature_Space_For_Whole_Slide_Image_ICCV_2025_paper.html)
- **SMMILe** — SMMILe enables accurate spatial quantification in digital pathology using MIL. [![Paper](https://img.shields.io/badge/Paper-Nature%20Cancer%202025-1f77b4.svg)](https://www.nature.com/articles/s43018-025-01060-8)
- **MIL_BASELINE** — unified implementation hub for pathology MIL methods. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lingxitong/MIL_BASELINE)
- **MIL-Lab** — standardized MIL library with pretrained slide models. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/MIL-Lab)
- **MIL Tutorial** — hands-on tutorial for pathology MIL pipelines. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/guillaumejaume/mil-tutorial)

---
## Federated Learning in Computational Pathology

<em>Federated learning methods and privacy-preserving frameworks for collaborative computational pathology.</em>

- **HistoFL** — federated learning for WSI classification and survival prediction. [![Paper](https://img.shields.io/badge/Paper-MedIA%202022-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841521003431) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HistoFL)
- **FedStain** — federated stain normalization for pathology. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202022-d62728.svg)](https://link.springer.com/chapter/10.1007/978-3-031-16434-7_2) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MECLabTUDA/BottleGAN)
- **FLamby** — cross-silo federated learning benchmark. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202022-d62728.svg)](https://proceedings.neurips.cc/paper_files/paper/2022/hash/5e637100c63800cc078ad0da3d1697e9-Abstract-Datasets_and_Benchmarks.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/owkin/FLamby)
- **FedCamelyon16** — federated Camelyon16 benchmark in FLamby. [![Dataset](https://img.shields.io/badge/Dataset-FLamby-orange.svg)](https://github.com/owkin/FLamby/tree/main/flamby/datasets/fed_camelyon16)
- **WSI-FL Tool** — federated training tool for WSI segmentation. [![Paper](https://img.shields.io/badge/Paper-JPI%202022-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S2153353922006952) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/SarderLab/federated_learning)
- **FedMM** — federated multimodal learning for computational pathology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2402.15858)
- **CPath-FL Review** — review of federated learning in computational pathology. [![Paper](https://img.shields.io/badge/Paper-CSBJ%202024-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S200103702400357X)
- **FLCP Review** — literature review of federated learning for computational pathology. [![Paper](https://img.shields.io/badge/Paper-JMI%202025-1f77b4.svg)](https://www.spiedigitallibrary.org/journals/journal-of-medical-imaging/volume-12/issue-06/061412/Federated-learning-in-computational-pathology-a-literature-review/10.1117/1.JMI.12.6.061412.full)
- **HistoFS** — non-IID WSI classification via federated style transfer. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2025/html/Raswa_HistoFS_Non-IID_Histopathologic_Whole_Slide_Image_Classification_via_Federated_Style_CVPR_2025_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lalakitchen/HistoFS)
- **PathFL** — federated pathology image segmentation across centers. [![Paper](https://img.shields.io/badge/Paper-MedIA%202025-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841525002178) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/yuanzhang7/PathFL)
- **RW-CPath-FL** — real-world federated learning for clinical pathology. [![Paper](https://img.shields.io/badge/Paper-JPI%202025-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S2153353925000501)
- **FedPathHarmony** — federated harmonization for multi-center pathology data. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/collaborativebioinformatics/FedPathHarmony)
- **FedWSIDD** — federated WSI classification via dataset distillation. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-d62728.svg)](https://papers.miccai.org/miccai-2025/0331-Paper1647.html)
- **Fed-cSCC** — federated model for cSCC progression prediction. [![Paper](https://img.shields.io/badge/Paper-npj%20Precis%20Oncol%202025-1f77b4.svg)](https://www.nature.com/articles/s41698-025-00997-4)
- **FedDMIL** — federated deep MIL for histopathology WSI classification. [![Paper](https://img.shields.io/badge/Paper-BSPC%202026-1f77b4.svg)](https://www.sciencedirect.com/science/article/abs/pii/S1746809425015708)

---

## Patch-Level Foundation Models

<em>Patch-level foundation models and visual encoders for histopathology representation learning.</em>

- **CTransPath** — transformer-based self-supervised pathology encoder. [![Paper](https://img.shields.io/badge/Paper-MedIA%202022-1f77b4.svg)](https://www.sciencedirect.com/science/article/abs/pii/S1361841522002043) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/jamesdolezal/CTransPath)
- **HIPT** — hierarchical transformer for pathology images. [![Paper](https://img.shields.io/badge/Paper-arXiv%202022-6A5ACD.svg)](https://arxiv.org/abs/2206.02647) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HIPT)
- **RetCCL** — contrastive pathology patch representation model. [![Paper](https://img.shields.io/badge/Paper-MedIA%202023-1f77b4.svg)](https://www.sciencedirect.com/science/article/abs/pii/S1361841522002730) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/jamesdolezal/RetCCL)
- **Lunit-DINO** — self-supervised ViT for pathology. [![Paper](https://img.shields.io/badge/Paper-CVPR%202023-d62728.svg)](https://arxiv.org/abs/2212.04690) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lunit-io/benchmark-ssl-pathology)
- **Phikon** — large-scale self-supervised pathology ViT. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202023-d62728.svg)](https://arxiv.org/abs/2309.16864) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/owkin/phikon)
- **PLIP** — pathology vision-language pretraining model. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202023-1f77b4.svg)](https://www.nature.com/articles/s41591-023-02504-3) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/vinid/plip)
- **PathoDuet** — pathology foundation model for H&E and IHC. [![Paper](https://img.shields.io/badge/Paper-arXiv%202023-6A5ACD.svg)](https://arxiv.org/abs/2312.09894) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/openmedlab/pathoduet)
- **CONCH** — caption-based pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202024-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02856-4) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/MahmoodLab/CONCH)
- **UNI** — general-purpose pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202024-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02857-3) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/MahmoodLab/UNI)
- **Virchow** — clinical-grade pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202024-1f77b4.svg)](https://www.nature.com/articles/s41591-024-03141-0) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/paige-ai/Virchow)
- **Virchow2** — mixed-magnification pathology encoder. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2408.00738) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/paige-ai/Virchow2)
- **Phikon-v2** — upgraded pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2409.09173) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/owkin/phikon-v2)
- **Hibou** — DINOv2-based pathology vision transformer. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2406.05074) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/histai/hibou-b)
- **kaiko Pathology FMs** — large-scale pathology ViT family. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2404.15217) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/collections/1aurent/kaikoai-models)
- **Prov-GigaPath** — pathology tile-level foundation encoder. [![Paper](https://img.shields.io/badge/Paper-Nature%202024-1f77b4.svg)](https://www.nature.com/articles/s41586-024-07441-w) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/prov-gigapath/prov-gigapath)
- **PLUTO** — lightweight multi-scale pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2405.07905)
- **UNI2-h** — second-generation pathology encoder from UNI. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/MahmoodLab/UNI2-h)
- **H-Optimus-0** — open foundation model for histology. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/bioptimus/H-optimus-0)
- **H-Optimus-1** — next-generation histology encoder. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/bioptimus/H-optimus-1)
- **Path Foundation** — Google pathology patch encoder. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/google/path-foundation)
- **BEPH** — BEiT-based pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202025-1f77b4.svg)](https://www.nature.com/articles/s41467-025-57587-y) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Zhcyoung/BEPH)
- **MUSK** — multimodal pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-Nature%202025-1f77b4.svg)](https://www.nature.com/articles/s41586-024-08437-2) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/xiangjx/musk)
- **Digepath** — gastrointestinal pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2505.21928) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/xtxx/Digepath)
- **PathOrchestra** — pathology foundation model for clinical tasks. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2503.24345) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/yanfang-research/PathOrchestra)
- **PLUTO-4** — next-generation PLUTO model family. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2511.02826)
- **StainNet** — pathology foundation model for special stains. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2512.10326) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/JWonderLand/StainNet)
- **Midnight** — efficient pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-d62728.svg)](https://arxiv.org/abs/2504.05186) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/kaiko-ai/midnight)
- **OpenMidnight** — open reproduction of Midnight. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/SophontAI/OpenMidnight)
- **GPFM** — pathology foundation model toolkit. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/birkhoffkiki/GPFM)
- **KEEP** — knowledge-enhanced pathology vision-language model. [![Paper](https://img.shields.io/badge/Paper-Cancer%20Cell%202026-1f77b4.svg)](https://www.cell.com/cancer-cell/fulltext/S1535-6108(26)00058-9) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/Astaxanthin/KEEP)
- **GenBio-PathFM** — pathology foundation model from public data. [![Paper](https://img.shields.io/badge/Paper-Preprint%202026-6A5ACD.svg)](https://genbio.ai/papers/genbio-pathfm.pdf) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/genbio-ai/genbio-pathfm)
- **Atlas 2** — clinical pathology foundation model family. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2601.05148) [![Website](https://img.shields.io/badge/Website-Aignostics-ffb6c1.svg)](https://www.aignostics.com/products/foundation-models)
- **GloPath** — entity-centric renal pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-Advanced%20Science%202026-1f77b4.svg)](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202520580)
- **CerS-Path** — cervical subspecialty pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2510.10196)


---

## Slide-Level Foundation Models and Slide Encoders

<em>Slide-level foundation models and whole-slide encoders for gigapixel pathology image understanding.</em>

- **Prov-GigaPath** — first whole-slide foundation model. [![Paper](https://img.shields.io/badge/Paper-Nature%202024-1f77b4.svg)](https://www.nature.com/articles/s41586-024-07441-w) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/prov-gigapath/prov-gigapath)
- **CHIEF** — clinical histopathology imaging evaluation foundation. [![Paper](https://img.shields.io/badge/Paper-Nature%202024-1f77b4.svg)](https://www.nature.com/articles/s41586-024-07894-z) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/hms-dbmi/CHIEF)
- **PANTHER** — morphological prototyping for slide foundation model. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-d62728.svg)](https://arxiv.org/abs/2405.11643) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/PANTHER)
- **TANGLE** — transcriptomics-guided slide representation learning. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-d62728.svg)](https://arxiv.org/abs/2405.11618) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TANGLE)
- **PRISM** — multimodal foundation model for slide-level histopathology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2405.10254) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/paige-ai/Prism)
- **CPath-Omni** — unified multimodal foundation model spanning patches and WSIs. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_CPath-Omni_A_Unified_Multimodal_Foundation_Model_for_Patch_and_Whole_CVPR_2025_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathFoundation/CPath-Omni)
- **SlideChat** — slide-level vision-language assistant model. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_SlideChat_A_Large_Vision-Language_Assistant_for_Whole-Slide_Pathology_Image_Understanding_CVPR_2025_paper.html) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/General-Medical-AI/SlideChat_Weight)
- **MADELEINE** — multistain pretraining for slide representation learning. [![Paper](https://img.shields.io/badge/Paper-ECCV%202024-d62728.svg)](https://link.springer.com/chapter/10.1007/978-3-031-73414-4_2) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/MahmoodLab/madeleine)
- **PathAlign** — vision-language model for whole-slide images in histopathology. [![Paper](https://img.shields.io/badge/Paper-MIDL%202024-d62728.svg)](https://proceedings.mlr.press/v254/ahmed24a.html)
- **TITAN** — multimodal whole-slide foundation model for pathology. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202025-1f77b4.svg)](https://www.nature.com/articles/s41591-025-03982-3) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/MahmoodLab/TITAN)
- **THREADS** — molecular-driven foundation model for oncologic pathology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2501.16652)
- **FEATHER** — lightweight supervised slide foundation models. [![Paper](https://img.shields.io/badge/Paper-ICML%202025-d62728.svg)](https://arxiv.org/abs/2506.09960) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/collections/MahmoodLab/feather)
- **mSTAR** — knowledge-enhanced whole-slide foundation model. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202025-1f77b4.svg)](https://www.nature.com/articles/s41467-025-66220-x) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/Wangyh/mSTAR)
- **EXAONE Path 2.5** — pathology foundation model with multi-omics alignment. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2512.14019) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/LGAI-EXAONE/EXAONE-Path-2.5)
- **WSI-Concepts** — supervised foundation model trained from whole-slide images. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2507.05742) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/FraunhoferMEVIS/MedicalMultitaskModeling)
- **HistoGPT** — slide foundation model for WSI report generation. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202025-1f77b4.svg)](https://www.nature.com/articles/s41467-025-60014-x) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/marr-peng-lab/histogpt)
- **Democratizing_WSI / GigaSSL** — optimized slide-level representations for TCGA-scale analysis. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/trislaz/Democratizing_WSI)
- **MOOZY** — patient-first foundation model for computational pathology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2603.27048) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/AtlasAnalyticsLab/MOOZY)
- **CARE** — molecular-guided slide-level foundation model. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2602.21637) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/Zipper-1/CARE)

---

## Cytology and Cervical Cytology in Pathology AI

<em>Cytology and cervical cytology studies for cell-level screening, diagnosis, and pathology AI applications.</em>

- **Computational Cytology Survey**. [![Paper](https://img.shields.io/badge/Paper-MedIA%202023-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S136184152200319X)
- **Cervical Cytology Deep Learning Review**. [![Paper](https://img.shields.io/badge/Paper-Neurocomputing%202024-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S0925231224014012)
- **DeepPap** — deep learning for cervical cytology cell classification. [![Paper](https://img.shields.io/badge/Paper-JBHI%202017-1f77b4.svg)](https://pubmed.ncbi.nlm.nih.gov/28541229/)
- **Multi-Task Feature Fusion** — feature-fusion model for cervical cell classification. [![Paper](https://img.shields.io/badge/Paper-JBHI%202022-1f77b4.svg)](https://pubmed.ncbi.nlm.nih.gov/35671309/)
- **TDCC-Net** — task decomposing and cell comparing for cervical lesion cell detection. [![Paper](https://img.shields.io/badge/Paper-TMI%202022-1f77b4.svg)](https://ieeexplore.ieee.org/document/9744114)
- **Comparison Detector** — comparison-based detector for cervical cells. [![Paper](https://img.shields.io/badge/Paper-Neurocomputing%202021-1f77b4.svg)](https://www.sciencedirect.com/science/article/abs/pii/S092523122100014X) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/kuku-sichuan/ComparisonDetector)
- **Robust Cervical Detection** — local-scale consistency distillation for cell detection. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202023-d62728.svg)](https://conferences.miccai.org/2023/papers/552-Paper2082.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/feimanman/Cervical-Abnormal-Cell-Detection)
- **CellGAN** — conditional cervical cell synthesis for data augmentation. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202023-d62728.svg)](https://doi.org/10.1007/978-3-031-43987-2_47) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ZhenrongShen/CellGAN)
- **SIPaKMeD** — Pap smear dataset for cervical cell classification. [![Paper](https://img.shields.io/badge/Paper-ICIP%202018-d62728.svg)](https://www.cse.uoi.gr/~cnikou/Publications/C072%20-%20Plissiti%20-%20icip%202018%20-%20Athens.pdf) [![Dataset](https://img.shields.io/badge/Dataset-Kaggle-orange.svg)](https://www.kaggle.com/datasets/marinaeplissiti/sipakmed)
- **HiCervix** — hierarchical dataset and benchmark for cervical cytology classification. [![Paper](https://img.shields.io/badge/Paper-TMI%202024-1f77b4.svg)](https://pubmed.ncbi.nlm.nih.gov/38923481/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Scu-sen/HiCervix)
- **BMT** — cross-validated ThinPrep Pap dataset. [![Paper](https://img.shields.io/badge/Paper-Sci%20Data%202024-1f77b4.svg)](https://www.nature.com/articles/s41597-024-04328-3)
- **HMCHH-TCT-CellDet** — large ThinPrep cytologic test dataset. [![Paper](https://img.shields.io/badge/Paper-Sci%20Data%202025-1f77b4.svg)](https://www.nature.com/articles/s41597-025-04374-5) [![Dataset](https://img.shields.io/badge/Dataset-Figshare-orange.svg)](https://springernature.figshare.com/articles/dataset/A_large_annotated_cervical_cytology_images_dataset_for_AI_models_to_aid_cervical_cancer_screening/27901206)
- **AIATBS** — AI-assisted TBS classification for cervical smears. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202021-1f77b4.svg)](https://www.nature.com/articles/s41467-021-23913-3)
- **Cervical WSI Screening** — WSI analysis for cervical cancer screening. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202021-1f77b4.svg)](https://www.nature.com/articles/s41467-021-25296-x) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ShenghuaCheng/Aided-Diagnosis-System-for-Cervical-Cancer-Screening)
- **Detection-Free Pipeline** — detection-free cervical WSI screening. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202023-d62728.svg)](https://dl.acm.org/doi/10.1007/978-3-031-43987-2_24) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/thebestannie/Detection-free-MICCAI2023)
- **LESS** — label-efficient multi-scale learning for cytology WSIs. [![Paper](https://img.shields.io/badge/Paper-MedIA%202024-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841524000343) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ubc-tea/LESS-WSI)
- **STRIDE** — large-scale AI-assisted cervical cytology screening. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2407.19512)
- **AICCS** — AI system for cervical cytology screening. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202024-1f77b4.svg)](https://www.nature.com/articles/s41467-024-48705-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/cellsvision/AICCS)
- **Patch-to-Sample Reasoning** — patch-to-sample reasoning for cervical WSI screening. [![Paper](https://img.shields.io/badge/Paper-TAI%202024-1f77b4.svg)](https://www.computer.org/csdl/journal/ai/2024/06/10285382/1Rd2FdKWJHO)
- **Smart-CCS** — cervical screening with pretraining and test-time adaptation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2502.09662) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/hjiangaz/Smart-CCS)
- **DualCytoNet** — AI-assisted cervical cytology for low-resource settings. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202025-1f77b4.svg)](https://www.nature.com/articles/s41467-025-62589-x)
- **LBC-DL** — LBC model for cervical precancer and cancer detection. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202025-1f77b4.svg)](https://www.nature.com/articles/s41467-025-58883-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/LuZWCHA/LBC_WSI_Classification)
- **UniCAS** — foundation model for cervical cytology screening. [![Paper](https://img.shields.io/badge/Paper-Cell%20Rep%20Med%202025-1f77b4.svg)](https://www.cell.com/cell-reports-medicine/fulltext/S2666-3791%2825%2900643-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/peter-fei/UniCAS)
- **CellProfiler** — open-source cell image analysis platform. [![Paper](https://img.shields.io/badge/Paper-Nat%20Methods%202012-1f77b4.svg)](https://www.nature.com/articles/nmeth.2083) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/CellProfiler/CellProfiler)
- **HoVer-Net** — nuclear instance segmentation and classification. [![Paper](https://img.shields.io/badge/Paper-MedIA%202019-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841519301045) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/vqdang/hover_net)
- **MoNuSeg** — multi-organ nucleus segmentation benchmark. [![Paper](https://img.shields.io/badge/Paper-TMI%202019-1f77b4.svg)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10439521/) [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://monuseg.grand-challenge.org/)
- **Cellpose** — generalist cellular segmentation model. [![Paper](https://img.shields.io/badge/Paper-Nat%20Methods%202021-1f77b4.svg)](https://www.nature.com/articles/s41592-020-01018-x) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MouseLand/cellpose)
- **Mesmer** — whole-cell and nuclear segmentation for multiplexed images. [![Paper](https://img.shields.io/badge/Paper-Nat%20Biotechnol%202021-1f77b4.svg)](https://www.nature.com/articles/s41587-021-01094-0) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/vanvalenlab/deepcell-tf)
- **Lizard** — large-scale colonic nuclei dataset. [![Paper](https://img.shields.io/badge/Paper-ICCV%20Workshop%202021-d62728.svg)](https://arxiv.org/abs/2108.11195) [![Dataset](https://img.shields.io/badge/Dataset-Warwick-orange.svg)](https://warwick.ac.uk/fac/cross_fac/tia/data/lizard/)
- **MoNuSAC** — multi-organ nuclei segmentation and classification challenge. [![Paper](https://img.shields.io/badge/Paper-TMI%202021-1f77b4.svg)](https://ieeexplore.ieee.org/document/9446924) [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://monusac-2020.grand-challenge.org/)
- **PanNuke** — pan-cancer nuclei dataset. [![Paper](https://img.shields.io/badge/Paper-ECCV%20Workshop%202021-d62728.svg)](https://arxiv.org/abs/2003.10778) [![Dataset](https://img.shields.io/badge/Dataset-Website-orange.svg)](https://jgamper.github.io/PanNukeDataset/)
- **NuCLS** — crowdsourced nuclei classification and segmentation dataset. [![Paper](https://img.shields.io/badge/Paper-GigaScience%202022-1f77b4.svg)](https://academic.oup.com/gigascience/article/doi/10.1093/gigascience/giac037/6586817) [![Dataset](https://img.shields.io/badge/Dataset-Website-orange.svg)](https://sites.google.com/view/nucls/home)
- **CoNIC** — colon nuclei segmentation and classification challenge. [![Paper](https://img.shields.io/badge/Paper-MedIA%202023-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841523003079) [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://conic-challenge.grand-challenge.org/)
- **CellViT** — ViT for nuclei instance segmentation in pathology. [![Paper](https://img.shields.io/badge/Paper-MedIA%202024-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841524000689) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TIO-IKIM/CellViT)
- **CellViT++** — WSI-scale cell segmentation and classification framework. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TIO-IKIM/CellViT-plus-plus)

---


## Computational Pathology with Multi-Omics

<em>Computational pathology studies integrating histology with genomics, transcriptomics, proteomics, and other omics data.</em>


- **DeepPATH** — histology-based cancer gene mutation prediction. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202018-1f77b4.svg)](https://www.nature.com/articles/s41591-018-0177-5) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ncoudray/DeepPATH)
- **SpaCell** — morphology and ST to predict disease cells. [![Paper](https://img.shields.io/badge/Paper-Bioinformatics%202020-1f77b4.svg)](https://academic.oup.com/bioinformatics/article/36/7/2293/5663455) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/BiomedicalMachineLearning/SpaCell)
- **HE2RNA** — bulk RNA-seq prediction from WSIs. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202020-1f77b4.svg)](https://www.nature.com/articles/s41467-020-17678-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/owkin/HE2RNA_code)
- **ST-Net** — histology and ST for spatial gene expression. [![Paper](https://img.shields.io/badge/Paper-Nat%20BME%202020-1f77b4.svg)](https://www.nature.com/articles/s41551-020-0578-x) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/bryanhe/ST-Net)
- **SpaGCN** — ST domains via expression and histology. [![Paper](https://img.shields.io/badge/Paper-Nat%20Methods%202021-1f77b4.svg)](https://www.nature.com/articles/s41592-021-01255-8) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/jianhuupenn/SpaGCN)
- **XFuse** — super-resolve ST via histology fusion. [![Paper](https://img.shields.io/badge/Paper-Nat%20Biotechnol%202021-1f77b4.svg)](https://doi.org/10.1038/s41587-021-01075-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ludvb/xfuse)
- **Hist2ST** — gene expression prediction from histology images. [![Paper](https://img.shields.io/badge/Paper-Brief%20Bioinform%202022-1f77b4.svg)](https://academic.oup.com/bib/article/23/5/bbac297/6645485) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/biomed-AI/Hist2ST)
- **HisToGene** — super-resolution spatial gene expression. [![Paper](https://img.shields.io/badge/Paper-bioRxiv%202021-6A5ACD.svg)](https://www.biorxiv.org/content/10.1101/2021.11.28.470212) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/maxpmx/HisToGene)
- **MCAT** — multimodal co-attention transformer for survival prediction. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202021-d62728.svg)](https://link.springer.com/chapter/10.1007/978-3-030-87240-3_67) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/mcat)
- **DeepSpaCE** — ST profile prediction from tissue images. [![Paper](https://img.shields.io/badge/Paper-Sci%20Rep%202022-1f77b4.svg)](https://doi.org/10.1038/s41598-022-07685-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/tmonjo/DeepSpaCE)
- **PathomicFusion** — histology and genomics fusion. [![Paper](https://img.shields.io/badge/Paper-Cell%20Rep%20Med%202022-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S2666379122003171) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/PathomicFusion)
- **PORPOISE** — pan-cancer histology and molecular prognosis. [![Paper](https://img.shields.io/badge/Paper-Cancer%20Cell%202022-1f77b4.svg)](https://doi.org/10.1016/j.ccell.2022.07.004) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/PORPOISE)
- **TESLA** — H&E-guided super-resolution ST. [![Paper](https://img.shields.io/badge/Paper-Cell%20Syst%202023-1f77b4.svg)](https://www.cell.com/cell-systems/fulltext/S2405-4712(23)00084-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/jianhuupenn/TESLA)
- **PathOmics** — pathology-genomics transformer for survival. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202023-d62728.svg)](https://conferences.miccai.org/2023/papers/485-Paper1847.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Cassie07/PathOmics)
- **MOTCat** — OT co-attention for multimodal survival. [![Paper](https://img.shields.io/badge/Paper-ICCV%202023-d62728.svg)](https://openaccess.thecvf.com/content/ICCV2023/papers/Xu_Multimodal_Optimal_Transport-based_Co-Attention_Transformer_with_Global_Structure_Consistency_for_ICCV_2023_paper.pdf) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Innse/MOTCat)
- **BLEEP** — bimodal embedding model for morphology-to-expression prediction. [![Paper](https://img.shields.io/badge/Paper-Nat%20Methods%202024-1f77b4.svg)](https://www.nature.com/articles/s41592-024-02318-8) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/bowang-lab/BLEEP)
- **HEST-1k** — histology–ST benchmark. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202024-d62728.svg)](https://arxiv.org/abs/2406.16192) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/MahmoodLab/hest) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HEST)
- **HE2Gene** — histology to ST via multi-task learning. [![Paper](https://img.shields.io/badge/Paper-Bioinformatics%202024-1f77b4.svg)](https://academic.oup.com/bioinformatics/article/40/6/btae343/7688334) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Microbiods/HE2Gene)
- **HGGEP** — histology to expression via hypergraph neural networks. [![Paper](https://img.shields.io/badge/Paper-Brief%20Bioinform%202024-1f77b4.svg)](https://academic.oup.com/bib/article/25/6/bbae500/7821151) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/QSong-github/HGGEP)
- **THItoGene** — histology to ST prediction. [![Paper](https://img.shields.io/badge/Paper-bioRxiv%202024-6A5ACD.svg)](https://www.biorxiv.org/content/10.1101/2024.01.25.577035v1) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/yrjia1015/THItoGene)
- **MMP** — multimodal prototyping for survival. [![Paper](https://img.shields.io/badge/Paper-ICML%202024-d62728.svg)](https://proceedings.mlr.press/v235/song24b.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/MMP)
- **SurvPath** — pathways and histology survival modeling. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Shao_Modeling_Dense_Multimodal_Interactions_Between_Biological_Pathways_and_Histology_for_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/SurvPath)
- **MERGE** — graph-based morphology-to-expression. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-d62728.svg)](https://arxiv.org/abs/2412.02601) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ags3927/MERGE)
- **M2OST** — multi-scale WSI Transformer for ST prediction. [![Paper](https://img.shields.io/badge/Paper-AAAI%202025-d62728.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/32830/34985) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/dootmaan/m2ost)
- **DeepSpot** — ST prediction from H&E with spatial context. [![Paper](https://img.shields.io/badge/Paper-medRxiv%202025-6A5ACD.svg)](https://www.medrxiv.org/content/10.1101/2025.02.09.25321567v2) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ratschlab/DeepSpot)
- **HistoCell** — super-resolution cell spatial profiles from H&E. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202025-1f77b4.svg)](https://www.nature.com/articles/s41467-025-57072-6) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/recolyce/HistoCell)
- **iSCALE** — large-tissue ST super-resolution. [![Paper](https://img.shields.io/badge/Paper-Nat%20Methods%202025-1f77b4.svg)](https://www.nature.com/articles/s41592-025-02770-8) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/amesch441/iSCALE)
- **OmiCLIP / Loki** — histology–ST contrastive foundation model. [![Paper](https://img.shields.io/badge/Paper-Nat%20Methods%202025-1f77b4.svg)](https://www.nature.com/articles/s41592-025-02707-1) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/GuangyuWangLab2021/Loki)
- **HEX** — virtual spatial proteomics from histology. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202025-1f77b4.svg)](https://www.nature.com/articles/s41591-025-04060-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lilab-stanford/HEX)
- **GHIST** — single-cell resolution ST prediction. [![Paper](https://img.shields.io/badge/Paper-Nat%20Methods%202025-1f77b4.svg)](https://www.nature.com/articles/s41592-025-02795-z) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/SydneyBioX/GHIST)
- **sCellST** — predicting single-cell gene expression from H&E. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202025-1f77b4.svg)](https://www.nature.com/articles/s41467-025-67965-1) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/loicchadoutaud/sCellST)
- **FmH2ST** — foundation model for H&E to ST generation. [![Paper](https://img.shields.io/badge/Paper-NAR%202025-1f77b4.svg)](https://academic.oup.com/nar/article/53/17/gkaf865/8249850) [![Website](https://img.shields.io/badge/Website-Code-ffb6c1.svg)](https://www.sdu-idea.cn/codes.php?name=FmH2ST)
- **MurreNet** — histology–genomics survival modeling. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-d62728.svg)](https://papers.miccai.org/miccai-2025/paper/0057_paper.pdf)
- **MRePath** — hypergraph multimodal survival. [![Paper](https://img.shields.io/badge/Paper-IJCAI%202025-d62728.svg)](https://www.ijcai.org/proceedings/2025/0201.pdf) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MCPathology/MRePath)
- **PS3** — pathology reports, histology, and pathways for survival prediction. [![Paper](https://img.shields.io/badge/Paper-ICCV%202025-d62728.svg)](https://iccv.thecvf.com/virtual/2025/poster/1823) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/manahilr/PS3)
- **KRONOS** — foundation model for spatial proteomics. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2506.03373) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/MahmoodLab/KRONOS)
- **CARE** — molecular-guided WSI foundation model. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2602.21637) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/Zipper-1/CARE)
- **STimage** — ST gene and cell prediction from H&E. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202026-1f77b4.svg)](https://doi.org/10.1038/s41467-026-68487-0) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/BiomedicalMachineLearning/STimage)
- **SpatialFusion** — multimodal niche discovery from ST and histology. [![Paper](https://img.shields.io/badge/Paper-bioRxiv%202026-6A5ACD.svg)](https://www.biorxiv.org/content/10.64898/2026.03.16.712056v1) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/uhlerlab/spatialfusion)
- **InSTaPath** — histology and ST topic learning. [![Paper](https://img.shields.io/badge/Paper-bioRxiv%202026-6A5ACD.svg)](https://www.biorxiv.org/content/10.64898/2026.03.16.712067v1) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/xwymary/InSTaPath)
- **HistoAtlas** - a pan-cancer morphology atlas linking histomics to molecular programs and clinical outcomes. [![Paper](https://arxiv.org/abs/2603.16587)] [![Website](https://histoatlas.com/)] 
---

## Generative Models for Computational Pathology

<em>Generative models for stain normalization, virtual staining, image synthesis, and data augmentation in computational pathology.</em>

- **StainGAN** — GAN-based stain transfer for histopathology. [![Paper](https://img.shields.io/badge/Paper-ISBI%202019-d62728.svg)](https://ieeexplore.ieee.org/document/8759152) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/xtarx/StainGAN)
- **Virtual Re-staining** — GAN-based virtual re-staining for WSIs. [![Paper](https://img.shields.io/badge/Paper-arXiv%202019-6A5ACD.svg)](https://arxiv.org/abs/1901.04059) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Zhaoyang-XU/Virtual-Staining)
- **PCGAN** — pathology-consistent GAN for unpaired stain transfer. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202021-d62728.svg)](https://arxiv.org/abs/2104.09462) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Pathology-Consistent-Stain-Transfer/Unpaired-Stain-Transfer-using-Pathology-Consistent-Constrained-Generative-Adversarial-Networks)
- **HistAuGAN** — structure-preserving stain color augmentation. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202021-d62728.svg)](https://miccai2021.org/openaccess/paperlinks/2021/09/01/456-Paper1521.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/sophiajw/HistAuGAN)
- **Residual CycleGAN** — robust domain transformation for histopathology. [![Paper](https://img.shields.io/badge/Paper-MedIA%202021-1f77b4.svg)](https://doi.org/10.1016/j.media.2021.102108) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/computationalpathologygroup/pathology-cyclegan-stain-transformation)
- **CAGAN** — colour adaptive GAN for stain normalization. [![Paper](https://img.shields.io/badge/Paper-MedIA%202021-1f77b4.svg)](https://doi.org/10.1016/j.media.2021.102204) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/thomascong121/CAGAN_Stain_Norm)
- **MultiPathGAN** — multi-domain stain normalization for WSIs. [![Paper](https://img.shields.io/badge/Paper-arXiv%202022-6A5ACD.svg)](https://arxiv.org/abs/2204.09782) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mlandcv/MultiPathGAN)
- **ScoreDiff StainNorm** — score-based diffusion for stain normalization. [![Paper](https://img.shields.io/badge/Paper-CBM%202023-1f77b4.svg)](https://pubmed.ncbi.nlm.nih.gov/36473344/)
- **DiffInfinite** — large histology synthesis via patch diffusion. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202023-d62728.svg)](https://arxiv.org/abs/2306.13384) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/marcoaversa/diffinfinite)
- **PathLDM** — text-conditioned latent diffusion for histopathology. [![Paper](https://img.shields.io/badge/Paper-WACV%202024-d62728.svg)](https://arxiv.org/abs/2309.00748) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/cvlab-stonybrook/PathLDM)
- **StainFuser** — diffusion-based neural stain style transfer. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2403.09302) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/R-J96/stainFuser)
- **Multi-target StainNorm** — multi-reference stain normalization for histology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2406.02077)
- **VIMs** — text-to-stain diffusion for virtual IHC multiplexing. [![Paper](https://img.shields.io/badge/Paper-MLMI%202024-d62728.svg)](https://arxiv.org/abs/2407.19113)
- **Histo-Diffusion** — diffusion super-resolution for digital pathology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2408.15218) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/zhexu1997/I2I-Generation)
- **StainPrompt** — prompted inversion for virtual staining. [![Paper](https://img.shields.io/badge/Paper-AAAI%202025-d62728.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/32949) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DianaNerualNetwork/StainPromptInversion)
- **PathoPainter** — tumor-aware inpainting for segmentation augmentation. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-d62728.svg)](https://arxiv.org/abs/2503.04634) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/HongLiuuuuu/PathoPainter)
- **HistDiST** — diffusion-based stain transfer for histopathology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2505.06793) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ErikGro/HistDiST)
- **PixCell** — generative foundation model for histopathology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2506.05127) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/cvlab-stonybrook/PixCell)
- **F2FLDM** — latent diffusion for frozen-to-FFPE translation. [![Paper](https://img.shields.io/badge/Paper-WACV%202025-d62728.svg)](https://openaccess.thecvf.com/content/WACV2025/papers/Ho_F2FLDM_Latent_Diffusion_Models_with_Histopathology_Pre-Trained_Embeddings_for_Unpaired_WACV_2025_paper.pdf) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/minhmanho/f2f_ldm)
- **ODA-GAN** — weakly supervised GAN for virtual IHC staining. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_ODA-GAN_Orthogonal_Decoupling_Alignment_GAN_Assisted_by_Weakly-supervised_Learning_for_CVPR_2025_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ittong/ODA-GAN)
- **SAStainDiff** — self-supervised diffusion for stain normalization. [![Paper](https://img.shields.io/badge/Paper-BSPC%202025-1f77b4.svg)](https://www.sciencedirect.com/science/article/abs/pii/S1746809425003726) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/yhuaishui/SAStainDiff)
- **GANs vs Diffusion for Virtual Staining** — compares GANs and diffusion for virtual staining. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2506.18484)
- **ZoomLDM** — multi-scale latent diffusion for histopathology generation. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2025/papers/Yellapragada_ZoomLDM_Latent_Diffusion_Model_for_Multi-scale_Image_Generation_CVPR_2025_paper.pdf) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/cvlab-stonybrook/ZoomLDM)
- **PathDiff** — text- and mask-conditioned histopathology synthesis. [![Paper](https://img.shields.io/badge/Paper-ICCV%202025-d62728.svg)](https://openaccess.thecvf.com/content/ICCV2025/papers/Bhosale_PathDiff_Histopathology_Image_Synthesis_with_Unpaired_Text_and_Mask_Conditions_ICCV_2025_paper.pdf)[![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/bhosalems/PathDiff)
- **Pixel SR Virtual Staining** — super-resolved virtual staining with diffusion. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202025-1f77b4.svg)](https://www.nature.com/articles/s41467-025-60387-z) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Yijie-Zhang/Super-resolved-virtual-staining)
- **MaskGAN** — mask-constrained virtual histological staining. [![Paper](https://img.shields.io/badge/Paper-Optik%202025-1f77b4.svg)](https://www.sciencedirect.com/science/article/abs/pii/S0030399225015567)
- **D-VST** — diffusion transformer for pathology virtual staining. [![Paper](https://img.shields.io/badge/Paper-OpenReview%202025-6A5ACD.svg)](https://openreview.net/pdf/01a05d9580a2101283275c60780b243faa2836b0.pdf)
- **Pathology Autoencoder** — pretrained autoencoders for pathology image compression. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-d62728.svg)](https://papers.miccai.org/miccai-2025/0671-Paper1570.html)
- **CytoSyn** — foundation diffusion model for histopathology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2603.18089) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/Owkin-Bioptimus/CytoSyn)
- **MUPAD** — generative foundation model for multimodal histopathology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2604.03635)
- **HistDiT** — diffusion transformer for H&E-to-IHC virtual staining. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2604.08305)
---

## Vision-Language Models and Pathology Agents

<em>Vision-language models, multimodal large models, and pathology agents for report generation, reasoning, and interactive diagnosis.</em>

- **PathVQA** — pathology VQA benchmark. [![Paper](https://img.shields.io/badge/Paper-CVPRW%202020-d62728.svg)](https://arxiv.org/abs/2003.10286)
- **TraP-VQA** — transformer-based pathology VQA. [![Paper](https://img.shields.io/badge/Paper-IEEE%20JBHI%202022-1f77b4.svg)](https://ieeexplore.ieee.org/document/9733299)
- **MI-Zero** — zero-shot WSI transfer. [![Paper](https://img.shields.io/badge/Paper-CVPR%202023-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Lu_Visual_Language_Pretrained_Multiple_Instance_Zero-Shot_Transfer_for_Histopathology_Images_CVPR_2023_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/MI-Zero)
- **PLIP / OpenPath** — pathology language-image pretraining. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202023-1f77b4.svg)](https://www.nature.com/articles/s41591-023-02504-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathologyFoundation/plip)
- **Quilt-1M / QuiltNet** — million-scale pathology image-text data. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202023-d62728.svg)](https://openreview.net/forum?id=OL2JQoO0kq) [![Website](https://img.shields.io/badge/Website-Project-ffb6c1.svg)](https://quilt1m.github.io/)
- **K-PathVQA** — knowledge-aware pathology VQA. [![Paper](https://img.shields.io/badge/Paper-IEEE%20JBHI%202023-1f77b4.svg)](https://ieeexplore.ieee.org/document/10177791)
- **PathPT** — few-shot prompt tuning for rare cancer subtyping. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202026-1f77b4.svg)](https://doi.org/10.1038/s41467-026-71715-2) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MAGIC-AI4Med/PathPT)
- **PathAsst / PathCLIP** — pathology assistant and CLIP model. [![Paper](https://img.shields.io/badge/Paper-AAAI%202024-d62728.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/28308) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/jamessyx/pathclip)
- **CONCH** — caption-aligned pathology VLM. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202024-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02856-4) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/MahmoodLab/CONCH)
- **PRISM** — slide-level generative pathology model. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2405.10254) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/paige-ai/Prism)
- **PathMMU** — pathology LMM benchmark. [![Paper](https://img.shields.io/badge/Paper-ECCV%202024-d62728.svg)](https://arxiv.org/abs/2401.16355) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/jamessyx/PathMMU)
- **Dr-LLaVA** — clinically grounded medical VLM. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2405.19567) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/AlaaLab/Dr-LLaVA)
- **CPLIP** — comprehensive pathology-language alignment. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Javed_CPLIP_Zero-Shot_Learning_for_Histopathology_with_Comprehensive_Vision-Language_Alignment_CVPR_2024_paper.html) [![Website](https://img.shields.io/badge/Website-Project-ffb6c1.svg)](https://cplip.github.io/)
- **Quilt-LLaVA** — pathology visual instruction tuning. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Seyfioglu_Quilt-LLaVA_Visual_Instruction_Tuning_by_Extracting_Localized_Narratives_from_Open-Source_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/aldraus/quilt-llava)
- **ViLa-MIL** — vision-language MIL for WSIs. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Shi_ViLa-MIL_Dual-scale_Vision-Language_Multiple_Instance_Learning_for_Whole_Slide_Image_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Jiangbo-Shi/ViLa-MIL)
- **PathAlign** — WSI-report vision-language alignment. [![Paper](https://img.shields.io/badge/Paper-PMLR%202024-d62728.svg)](https://proceedings.mlr.press/v254/ahmed24a.html) [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2406.19578)
- **PathChat** — multimodal pathology copilot. [![Paper](https://img.shields.io/badge/Paper-Nature%202024-1f77b4.svg)](https://www.nature.com/articles/s41586-024-07618-3) [![Website](https://img.shields.io/badge/Website-Demo-ffb6c1.svg)](https://www.modella.ai/pathchat)
- **TM-PATHVQA** — multilingual spoken pathology VQA. [![Paper](https://img.shields.io/badge/Paper-INTERSPEECH%202024-d62728.svg)](https://www.isca-archive.org/interspeech_2024/rajkhowa24_interspeech.html)
- **WSI-VQA** — generative WSI visual QA. [![Paper](https://img.shields.io/badge/Paper-ECCV%202024-d62728.svg)](https://arxiv.org/abs/2407.05603) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/cpystan/WSI-VQA)
- **PathInsight** — histopathology instruction tuning. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2408.07037)
- **HistGen** — WSI pathology report generation. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202024-d62728.svg)](https://papers.miccai.org/miccai-2024/387-Paper0796.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/dddavid4real/HistGen)
- **PathM3** — WSI classification and captioning. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202024-d62728.svg)](https://papers.miccai.org/miccai-2024/593-Paper3991.html)
- **Path-RAG** — pathology RAG for VQA. [![Paper](https://img.shields.io/badge/Paper-ML4H%202024-d62728.svg)](https://arxiv.org/abs/2411.17073)
- **MUSK** — precision-oncology pathology VLM. [![Paper](https://img.shields.io/badge/Paper-Nature%202024-1f77b4.svg)](https://www.nature.com/articles/s41586-024-08378-w) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lilab-stanford/MUSK)
- **WSI-LLaVA** — whole-slide LLaVA model. [![Paper](https://img.shields.io/badge/Paper-ICCV%202025-d62728.svg)](https://openaccess.thecvf.com/content/ICCV2025/html/Liang_WSI-LLaVA_A_Multimodal_Large_Language_Model_for_Whole_Slide_Image_ICCV_2025_paper.html)
- **PathVLM-Eval** — pathology VLM evaluation study. [![Paper](https://img.shields.io/badge/Paper-J%20Pathol%20Inform%202025-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S2153353925000409)
- **MLLM4PUE** — universal pathology embeddings. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2502.07221)
- **PolyPath** — multi-slide report generation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2502.10536)
- **PathFinder** — multi-agent histopathology diagnosis. [![Paper](https://img.shields.io/badge/Paper-ICCV%202025-d62728.svg)](https://openaccess.thecvf.com/content/ICCV2025/html/Ghezloo_PathFinder_A_Multi-Modal_Multi-Agent_System_for_Medical_Diagnostic_Decision-Making_Applied_ICCV_2025_paper.html)
- **CLOVER** — efficient pathology instruction learning. [![Paper](https://img.shields.io/badge/Paper-Nat%20Comput%20Sci%202025-1f77b4.svg)](https://www.nature.com/articles/s43588-025-00818-5) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/jlinekai/clover)
- **PA-LLaVA / Pathology-LLaVA** — pathology LLaVA model. [![Paper](https://img.shields.io/badge/Paper-AI%20Review%202025-1f77b4.svg)](https://link.springer.com/article/10.1007/s10462-025-11190-1) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/OpenFace-CQUPT/Pathology-LLaVA)
- **HistoGPT** — dermatopathology report generation. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202025-1f77b4.svg)](https://www.nature.com/articles/s41467-025-60014-x) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/marr-peng-lab/histogpt)
- **TITAN** — WSI image-text alignment model. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202025-1f77b4.svg)](https://www.nature.com/articles/s41591-025-03982-3) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/MahmoodLab/TITAN)
- **VLSA** — vision-language survival analysis. [![Paper](https://img.shields.io/badge/Paper-ICLR%202025-d62728.svg)](https://openreview.net/forum?id=trj2Jq8riA) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/liupei101/VLSA)
- **PathGen-1.6M** — multi-agent pathology image-text data. [![Paper](https://img.shields.io/badge/Paper-ICLR%202025-d62728.svg)](https://openreview.net/forum?id=rFpZnn11gj) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/jamessyx/PathGen)
- **PathGen-CLIP** — PathGen-trained CLIP model. [![Paper](https://img.shields.io/badge/Paper-ICLR%202025-d62728.svg)](https://openreview.net/forum?id=rFpZnn11gj) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/jamessyx/PathGen-CLIP)
- **PathGen-LLaVA** — PathGen-based LLaVA model. [![Paper](https://img.shields.io/badge/Paper-ICLR%202025-d62728.svg)](https://openreview.net/forum?id=rFpZnn11gj) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/jamessyx/PathGen-LLaVA)
- **PathVLM-R1** — RL pathology VLM reasoner. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2504.09258)
- **ChatEXAONEPath** — expert-level WSI pathology MLLM. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2504.13023)
- **ALPaCA / Llama-slideQA** — slide-level pathology QA model. [![Paper](https://img.shields.io/badge/Paper-medRxiv%202025-6A5ACD.svg)](https://www.medrxiv.org/content/10.1101/2025.04.22.25326190v1) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/CNX-PathLLM/Llama-slideQA)
- **VideoPath-LLaVA** — video-tuned pathology reasoning. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2505.04192) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/trinhvg/VideoPath-LLaVA)
- **Patho-R1** — RL pathology expert reasoner. [![Paper](https://img.shields.io/badge/Paper-AAAI%202026-d62728.svg)](https://arxiv.org/abs/2505.11404) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Wenchuan-Zhang/Patho-R1)
- **CPathAgent** — agentic high-resolution pathology model. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202025-d62728.svg)](https://arxiv.org/abs/2505.20510)
- **MR-PLIP** — multi-resolution pathology-language pretraining. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2025/html/Albastaki_Multi-Resolution_Pathology-Language_Pre-training_Model_with_Text-Guided_Visual_Representation_CVPR_2025_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/BasitAlawode/MR-PLIP)
- **CPath-Omni** — unified patch-WSI pathology MLLM. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_CPath-Omni_A_Unified_Multimodal_Foundation_Model_for_Patch_and_Whole_CVPR_2025_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathFoundation/CPath-Omni)
- **SlideChat** — whole-slide pathology assistant. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-d62728.svg)](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_SlideChat_A_Large_Vision-Language_Assistant_for_Whole-Slide_Pathology_Image_Understanding_CVPR_2025_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/uni-medical/SlideChat)
- **OpenPath Active Learning** — VLM-based pathology active learning. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2506.15318)
- **PathGenIC** — in-context pathology report generation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2506.17645)
- **PathChat+ / SlideSeek** — multi-agent WSI diagnosis. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2506.20964)
- **PathCoT** — CoT prompting for pathology reasoning. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2507.01029)
- **TCP-LLaVA** — token-compressed WSI VQA. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2507.14497)
- **SmartPath-R1** — reasoning-enhanced pathology copilot. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2507.17303)
- **DiagR1** — RL digestive pathology VLM. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2507.18433)
- **PathBench** — pathology LMM evaluation benchmark. [![Paper](https://img.shields.io/badge/Paper-IEEE%20TMI%202025-1f77b4.svg)](https://pubmed.ncbi.nlm.nih.gov/40601458/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/superjamessyx/PathBench)
- **mSTAR** — WSI report-omics foundation model. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202025-1f77b4.svg)](https://www.nature.com/articles/s41467-025-66220-x)
- **PathVG / RefPath** — pathology visual grounding benchmark. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-d62728.svg)](https://papers.miccai.org/miccai-2025/0678-Paper1180.html) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/fengluo/RefPath)
- **PathoPrompt** — cross-granular pathology prompting. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-d62728.svg)](https://papers.miccai.org/miccai-2025/0677-Paper4278.html)
- **WSI-Agents** — collaborative WSI analysis agents. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-d62728.svg)](https://papers.miccai.org/miccai-2025/1022-Paper0994.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/CVI-SZU/WSI-Agents)
- **PathoHR** — hierarchical pathology reasoning. [![Paper](https://img.shields.io/badge/Paper-EMNLP%202025-d62728.svg)](https://aclanthology.org/2025.findings-emnlp.124/)
- **PathAgent** — training-free pathology agent. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2511.17052) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/G14nTDo4/PathAgent)
- **GIANT** — gigapixel pathology navigation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2511.19652)
- **PathReasoning** — query-guided ROI navigation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2511.21902)
- **LoC-Path** — compressed pathology MLLM. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2512.05391)
- **MPath** — visual-prefix WSI reporting. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2512.11906)
- **ANTONI-α** — open WSI pathology copilot. [![Paper](https://img.shields.io/badge/Paper-MIDL%202026-d62728.svg)](https://openreview.net/forum?id=aGPowreqPi)
- **PathFound** — agentic pathology diagnosis. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2512.23545)
- **DomainSAT for Pathology VLMs** — pathology VLM shift detection. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2601.00716)
- **PathReasoner-R1** — knowledge-guided WSI reasoning. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2601.21617) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/cyclexfy/PathReasoner-R1)
- **KEEP** — knowledge-enhanced pathology VLM. [![Paper](https://img.shields.io/badge/Paper-Cancer%20Cell%202026-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1535610826000589)
- **Hepato-LLaVA** — hepatocellular WSI MLLM. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2602.19424)
- **Patho-AgenticRAG** — agentic pathology RAG. [![Paper](https://img.shields.io/badge/Paper-AAAI%202026-d62728.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/40239)
- **QCAgent** — agentic pathology report generation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2603.01647)
- **MLLM-HWSI** — holistic WSI MLLM analysis. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2603.23067)
- **PBSBench** — pathology slide VL benchmark. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2604.17570)
- **CONCH v1.5** — upgraded pathology VLM encoder. [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/MahmoodLab/conchv1_5)
- **MLLM4BioMed** — biomedical MLLM paper tracker. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ncbi-nlp/MLLM4BioMed)

---


## Dense Prediction in Computational Pathology

<em>Dense prediction methods for segmentation, detection, localization, and pixel-level pathology image analysis.</em>

- **NucleiSegmentation (MahmoodLab)** — early deep learning pipeline for nuclei segmentation. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/NucleiSegmentation)
- **HoVer-Net** — nuclei instance segmentation and classification. [![Paper](https://img.shields.io/badge/Paper-MedIA%202019-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841519301045) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/vqdang/hover_net)
- **PointNu-Net** — keypoint-assisted nuclei segmentation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202021-6A5ACD.svg)](https://arxiv.org/abs/2111.01557) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Kaiseem/PointNu-Net)
- **MPS** — weakly supervised tissue segmentation from slide-level labels. [![Paper](https://img.shields.io/badge/Paper-MedIA%202022-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841522001347) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ChuHan89/WSSS-Tissue)
- **OEEM** — weakly supervised gland segmentation. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202022-d62728.svg)](https://arxiv.org/abs/2206.06665) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/xmed-lab/OEEM)
- **HistoSeg** — multi-structure histology segmentation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202022-6A5ACD.svg)](https://arxiv.org/abs/2209.00729) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/saadwazir/HistoSeg)
- **CellViT** — ViT-based cell segmentation and classification. [![Paper](https://img.shields.io/badge/Paper-arXiv%202023-6A5ACD.svg)](https://arxiv.org/abs/2306.15350) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TIO-IKIM/CellViT)
- **HistoPLUS** - cell detection, segmentation and classification/ [![Paper](https://arxiv.org/abs/2508.09926)] [![Code](https://github.com/owkin/histoplus/)]
- **SAM-Path** — SAM for digital pathology segmentation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202023-6A5ACD.svg)](https://arxiv.org/abs/2307.09570) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/cvlab-stonybrook/SAMPath)
- **UniCell** — prompt-based universal nucleus classification. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2402.12938) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lhaof/UniCell)
- **AWGUNET** — wavelet-guided U-Net for nuclei segmentation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2406.08425) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/AyushRoy2001/AWGUNET)
- **LKCell** — large-kernel nuclei instance segmentation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2407.18054) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/hustvl/LKCell)
- **SAM2-PATH** — SAM2 for pathology segmentation. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2408.03651) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/simzhangbest/SAM2PATH)
- **CISCA** — cell instance segmentation and classification. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2409.04175)
- **HisynSeg** — weakly supervised segmentation via image mixing. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2412.20924) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Vison307/HisynSeg)
- **PathoSAM** — Segment Anything for histopathology. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2502.00408) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/computational-cell-analytics/patho-sam)
- **HoVer-NeXt** — fast nuclei segmentation and classification. [![Paper](https://img.shields.io/badge/Paper-OpenReview%202025-6A5ACD.svg)](https://openreview.net/forum?id=3vmB43oqIO) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/digitalpathologybern/hover_next_train)
- **SIA-WSSS** — weakly supervised pathology segmentation. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-d62728.svg)](https://papers.miccai.org/miccai-2025/paper/5096_paper.pdf) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Jsf826/SIA-WSSS)
- **PFM-DenseBench** — dense prediction benchmark for pathology foundation models. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2602.03887) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lingxitong/PFM_Segmentation)

---

## Clinical Tasks and Applications

<em>Clinical task-driven computational pathology studies for diagnosis, prognosis, biomarker prediction, treatment response, and real-world applications.</em>

- **Breast LN Metastasis** — detects breast lymph-node metastases in WSIs. [![Paper](https://img.shields.io/badge/Paper-JAMA%202017-1f77b4.svg)](https://jamanetwork.com/journals/jama/fullarticle/2665774)
- **Breast Invasion Detection** — detects invasive breast tumor regions. [![Paper](https://img.shields.io/badge/Paper-Sci%20Rep%202017-1f77b4.svg)](https://www.nature.com/articles/srep46450)
- **NSCLC Mutation Prediction** — predicts lung subtype and driver mutations. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202018-1f77b4.svg)](https://www.nature.com/articles/s41591-018-0177-5) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ncoudray/DeepPATH)
- **MSI from H&E** — predicts MSI from gastrointestinal H&E slides. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202019-1f77b4.svg)](https://www.nature.com/articles/s41591-019-0462-y)
- **AI Prostate Grading** — performs specialist-level Gleason grading. [![Paper](https://img.shields.io/badge/Paper-Lancet%20Oncol%202020-1f77b4.svg)](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(19)30738-7/fulltext)
- **Prostate AI Validation** — validates AI for prostate diagnosis and Gleason grading. [![Paper](https://img.shields.io/badge/Paper-Lancet%20Digit%20Health%202020-1f77b4.svg)](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(20)30159-X/fulltext)
- **Pan-cancer Genetic Alterations** — predicts actionable alterations from WSIs. [![Paper](https://img.shields.io/badge/Paper-Nat%20Cancer%202020-1f77b4.svg)](https://www.nature.com/articles/s43018-020-0087-6) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/jnkather/DeepHistology)
- **Self-learning Gleason Grading** — weakly supervised Gleason grading from WSIs. [![Paper](https://img.shields.io/badge/Paper-IEEE%20JBHI%202021-1f77b4.svg)](https://ieeexplore.ieee.org/document/9361085) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/jusiro/mil_histology)
- **AI-assisted Gleason Grading** — improves pathologist grading performance. [![Paper](https://img.shields.io/badge/Paper-Mod%20Pathol%202021-1f77b4.svg)](https://www.nature.com/articles/s41379-020-0640-y)
- **Ovarian Platinum Response** — predicts platinum chemotherapy response. [![Paper](https://img.shields.io/badge/Paper-Sci%20Rep%202021-1f77b4.svg)](https://www.nature.com/articles/s41598-021-98480-0)
- **TOAD** — predicts tumor origin for cancers of unknown primary. [![Paper](https://img.shields.io/badge/Paper-Nature%202021-1f77b4.svg)](https://www.nature.com/articles/s41586-021-03512-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TOAD)
- **Prostate Diagnosis & Grading** — diagnoses prostate cancer and predicts Gleason grade. [![Paper](https://img.shields.io/badge/Paper-Nat%20Med%202022-1f77b4.svg)](https://www.nature.com/articles/s41591-021-01620-2)
- **Breast IDC Classification** — classifies invasive ductal carcinoma in breast WSIs. [![Paper](https://img.shields.io/badge/Paper-Sci%20Rep%202021-1f77b4.svg)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8582388/)
- **Breast LN Metastasis Workflow** — detects nodal metastasis in digital pathology. [![Paper](https://img.shields.io/badge/Paper-Mod%20Pathol%202023-1f77b4.svg)](https://pubmed.ncbi.nlm.nih.gov/37178923/)
- **Breast TP53 Prediction** — predicts TP53 mutation status from breast H&E WSIs. [![Paper](https://img.shields.io/badge/Paper-Breast%20Cancer%20Res%20Treat%202024-1f77b4.svg)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11638532/)
- **DeepHRD** — predicts HRD and platinum response from histologic slides. [![Paper](https://img.shields.io/badge/Paper-JCO%202024-1f77b4.svg)](https://ascopubs.org/doi/10.1200/JCO.23.02641) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/AlexandrovLab/DeepHRD)
- **PathoRiCH** — predicts platinum response in ovarian cancer. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202024-1f77b4.svg)](https://www.nature.com/articles/s41467-024-48667-6) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/dmmoon/PathoRICH)
- **MERGE** — predicts gene expression from pathology WSIs. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-d62728.svg)](https://arxiv.org/abs/2412.02601) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ags3927/MERGE)
- **Breast LN Staging** — detects, localizes, and stages nodal metastasis. [![Paper](https://img.shields.io/badge/Paper-Sci%20Rep%202025-1f77b4.svg)](https://www.nature.com/articles/s41598-025-21787-9)
- **Orpheus** — predicts recurrence risk in HR-positive early breast cancer. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202025-1f77b4.svg)](https://www.nature.com/articles/s41467-025-57283-x) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/kmboehm/orpheus)
- **PARP Benefit Prediction** — predicts HRD and PARP inhibitor benefit from ovarian WSIs. [![Paper](https://img.shields.io/badge/Paper-Eur%20J%20Cancer%202025-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S0959804924018069)
- **Breast DCIS Recurrence** — predicts invasive recurrence risk in DCIS. [![Paper](https://img.shields.io/badge/Paper-eBioMedicine%202025-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S235239642500194X)
- **Early Breast Cancer Recurrence** — predicts recurrence risk from H&E WSIs. [![Paper](https://img.shields.io/badge/Paper-Sci%20Rep%202025-1f77b4.svg)](https://www.nature.com/articles/s41598-025-16679-x)
- **Gastric Early Recurrence** — predicts early gastric cancer recurrence. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202026-1f77b4.svg)](https://www.nature.com/articles/s41467-026-71347-6)
- **Breast pTNM Stage Prediction** — predicts breast cancer pTNM stage from H&E WSIs. [![Paper](https://img.shields.io/badge/Paper-J%20Pathol%20Inform%202026-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S2153353926001021)
---

## Pathology Image Registration and Spatial Alignment

<em>Pathology image registration and spatial alignment methods for serial sections, multi-stain slides, and spatial omics integration.</em>

- **HistoReg** — registration framework for variably stained histology slices. [![Paper](https://img.shields.io/badge/Paper-arXiv%202019-6A5ACD.svg)](https://arxiv.org/abs/1904.11929) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/CBICA/HistoReg)
- **Re-stained-Regist** — robust co-registration for re-stained histological WSIs. [![Paper](https://img.shields.io/badge/Paper-PLOS%20ONE%202019-1f77b4.svg)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0220074) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/smujiang/Re-stained_WSIs_Registration)
- **ANHIR** — benchmark for automatic non-rigid histology registration. [![Paper](https://img.shields.io/badge/Paper-TMI%202020-1f77b4.svg)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7584382/) [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://anhir.grand-challenge.org/)
- **PathFlow-MixMatch** — segment-based scalable WSI registration. [![Paper](https://img.shields.io/badge/Paper-bioRxiv%202020-6A5ACD.svg)](https://www.biorxiv.org/content/10.1101/2020.03.22.002402.full) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/jlevy44/PathFlow-MixMatch)
- **GridNet** — registration for histology and spatial transcriptomics. [![Paper](https://img.shields.io/badge/Paper-Bioinformatics%202021-1f77b4.svg)](https://academic.oup.com/bioinformatics/article/37/22/4216/6299384) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/flatironinstitute/st_gridnet)
- **ASHLAR** — stitching and registration for multiplexed WSI. [![Paper](https://img.shields.io/badge/Paper-Bioinformatics%202022-1f77b4.svg)](https://academic.oup.com/bioinformatics/article/38/19/4613/6668278) [![Website](https://img.shields.io/badge/Website-Docs-ffb6c1.svg)](https://labsyspharm.github.io/ashlar/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/labsyspharm/ashlar)
- **DeepLIIF** — deep learning-inferred mif for IHC quantification. [![Paper](https://img.shields.io/badge/Paper-Nat%20Mach%20Intell%202022-1f77b4.svg)](https://www.nature.com/articles/s42256-022-00471-x.epdf?sharing_token=TfIQdFzqGrYolrSS_NyOJtRgN0jAjWel9jnR3ZoTv0P90KdmGq_lkIuepQpaAnx9M_HMX0dkqP8OF91EhA0P9AAsgUeGoCtaqab2DQMx50ft_LVCW8JvZUJ-qQxqZjpYLSzzUo00YLH8PJ-XBckUsuikhsZl8LQ1us1rXPrAWKE%3D) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/nadeemlab/DeepLIIF)
- **CGNReg** — deep registration for serial H&E and IHC WSIs. [![Paper](https://img.shields.io/badge/Paper-J%20Pathol%20Inform%202023-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S2153353923001256)
- **Valis** — virtual alignment pipeline for multi-gigapixel WSI series. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202023-1f77b4.svg)](https://www.nature.com/articles/s41467-023-40218-9) [![Website](https://img.shields.io/badge/Website-Docs-ffb6c1.svg)](https://valis.readthedocs.io/en/latest/index.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MathOnco/valis)
- **STalign** — diffeomorphic alignment for spatial transcriptomics. [![Paper](https://img.shields.io/badge/Paper-Nat%20Commun%202023-1f77b4.svg)](https://www.nature.com/articles/s41467-023-43915-7) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/JEFworks-Lab/STalign)
- **WSIMIR** — mutual-information-based multi-modality WSI registration. [![Paper](https://img.shields.io/badge/Paper-J%20Pathol%20Inform%202023-1f77b4.svg)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10527458/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/AstroPathJHU/WSIMIR)
- **ACROBAT** — benchmark for automatic breast cancer WSI registration. [![Paper](https://img.shields.io/badge/Paper-MedIA%202024-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1361841524001828) [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://acrobat.grand-challenge.org/)
- **DeeperHistReg** — robust framework for multi-stain WSI registration. [![Paper](https://img.shields.io/badge/Paper-arXiv%202024-6A5ACD.svg)](https://arxiv.org/abs/2404.14434) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MWod/DeeperHistReg)
- **RegWSI** — WSI registration with combined global and local alignment. [![Paper](https://img.shields.io/badge/Paper-CMPB%202024-1f77b4.svg)](https://dl.acm.org/doi/10.1016/j.cmpb.2024.108187)
- **NEMESIS** — neural implicit representation for WSI registration. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MIAGroupUT/NEMESIS)
- **TIAToolbox WSI Registration** — practical WSI registration tutorial and toolkit support. [![Website](https://img.shields.io/badge/Website-Docs-ffb6c1.svg)](https://tia-toolbox.readthedocs.io/en/latest/_notebooks/jnb/10-wsi-registration.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TissueImageAnalytics/tiatoolbox)

---

## Resources, Toolkits, and Open-Source Projects

<em>Open-source resources, toolkits, and software platforms for computational pathology research and deployment.</em>

- **OpenSlide** — standard library for reading WSI. [![Paper](https://img.shields.io/badge/Paper-J%20Pathol%20Inform%202013-1f77b4.svg)](https://pubmed.ncbi.nlm.nih.gov/24244884/) [![Website](https://img.shields.io/badge/Website-OpenSlide-ffb6c1.svg)](https://openslide.org/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/openslide/openslide)
- **QuPath** — open-source platform for digital pathology analysis. [![Paper](https://img.shields.io/badge/Paper-Sci%20Rep%202017-1f77b4.svg)](https://www.nature.com/articles/s41598-017-17204-5) [![Website](https://img.shields.io/badge/Website-QuPath-ffb6c1.svg)](https://qupath.github.io/)
- **ASAP** — slide visualization, annotation, and analysis platform. [![Website](https://img.shields.io/badge/Website-ASAP-ffb6c1.svg)](https://computationalpathologygroup.github.io/ASAP/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ComputationalPathologyGroup/ASAP)
- **HistoQC** — quality control toolbox for digital pathology cohorts. [![Paper](https://img.shields.io/badge/Paper-JCO%20Clin%20Cancer%20Inform%202019-1f77b4.svg)](https://pubmed.ncbi.nlm.nih.gov/30990737/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/choosehappy/HistoQC)
- **caMicroscope** — pathology viewer for human and machine annotations. [![Website](https://img.shields.io/badge/Website-caMicroscope-ffb6c1.svg)](https://camicroscope.org/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/camicroscope/caMicroscope)
- **pathology-whole-slide-data** — efficient WSI data pipelines and batch iterators. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DIAGNijmegen/pathology-whole-slide-data)
- **TIAToolbox** — end-to-end toolbox for computational pathology. [![Paper](https://img.shields.io/badge/Paper-Commun%20Med%202022-1f77b4.svg)](https://www.nature.com/articles/s43856-022-00186-5) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TissueImageAnalytics/tiatoolbox)
- **PathML** — pathology ML toolkit with reusable pipelines. [![Paper](https://img.shields.io/badge/Paper-JAMIA%202022-1f77b4.svg)](https://pubmed.ncbi.nlm.nih.gov/34880124/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Dana-Farber-AIOS/pathml)
- **histolab** — Python toolkit for reproducible WSI preprocessing. [![Paper](https://img.shields.io/badge/Paper-SoftwareX%202022-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S2352711022001558) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/histolab/histolab)
- **Slideflow** — deep learning framework for whole-slide images. [![Paper](https://img.shields.io/badge/Paper-arXiv%202023-6A5ACD.svg)](https://arxiv.org/abs/2304.04142) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/slideflow/slideflow)
- **PrismToolBox** — patch extraction, embeddings, and QuPath interoperability. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/gustaveroussy/prismtoolbox)
- **TRIDENT** — large-scale WSI processing and feature extraction toolkit. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2502.06750) [![Website](https://img.shields.io/badge/Website-Docs-ffb6c1.svg)](https://trident-docs.readthedocs.io/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TRIDENT)
- **MIL-Lab** — standardized MIL codebase with pretrained model weights. [![Paper](https://img.shields.io/badge/Paper-arXiv%202025-6A5ACD.svg)](https://arxiv.org/abs/2506.09022) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-yellow.svg)](https://huggingface.co/MahmoodLab)
- **LazySlide** — pathology analysis utilities with model zoo support. [![Paper](https://img.shields.io/badge/Paper-bioRxiv%202025-6A5ACD.svg)](https://www.biorxiv.org/content/10.1101/2025.05.28.656548v1) [![Website](https://img.shields.io/badge/Website-Docs-ffb6c1.svg)](https://lazyslide.readthedocs.io/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/rendeirolab/LazySlide)
- **PFM_Segmentation** — pathology foundation model segmentation framework. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2602.03887) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lingxitong/PFM_Segmentation)
- **AtlasPatch** — scalable tissue detection and patch extraction. [![Paper](https://img.shields.io/badge/Paper-arXiv%202026-6A5ACD.svg)](https://arxiv.org/abs/2602.03998) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/AtlasAnalyticsLab/AtlasPatch)
- **MIL_BASELINE** — unified pathology MIL library. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lingxitong/MIL_BASELINE)
---

## Future Trends and Hot Topics

**🤖 Agentic & Multimodal Pathology**  Pathology agents will move beyond single-image prediction toward WSI navigation, multimodal reasoning, report generation, tool use, and interactive diagnostic assistance.

**🏥 Clinical Translation & Deployment**  Future systems will focus on external validation, workflow integration, uncertainty estimation, regulatory readiness, and real-world robustness across hospitals and scanners.

**🧬 Multi-omics & High-level Clinical Tasks**  Pathology AI will increasingly target molecular subtyping, treatment response prediction, recurrence risk, survival stratification, and pathology-genomics integration.

**🧠 General-purpose Pathology Foundation Models**  Unified pathology backbones will integrate patch, cell, tissue, slide, language, and clinical knowledge to support diverse downstream tasks with minimal adaptation.

**🔬 Cell-level and Spatial Intelligence**  Models will shift from slide-level labels toward cell states, tissue microenvironment, spatial organization, and biologically interpretable disease mechanisms.

## Acknowledgements

This repository is built upon the open-source efforts of many researchers and groups across. We sincerely thank the authors, maintainers, and contributors of the papers, datasets, benchmarks, and toolkits collected in this project.
We also thank the **[Awesome World Models](https://github.com/knightnemo/Awesome-World-Models)** repository for providing an excellent README organization template and design inspiration.
Special thanks to the supporting teams from **[Tsinghua University](https://www.tsinghua.edu.cn/en/)** for their continuous support, discussions, and contributions.

### Core Contributors

<table>
  <tr>
    <td align="center" width="160">
      <img src="assets/people/lingxitong.png" width="120" height="168" style="object-fit: cover; object-position: center;"><br>
      <div style="line-height: 1.2; font-size: 13px;">
        <b>Xitong Ling</b><br>
        PhD Student<br>
        Tsinghua
      </div>
    </td>
    <td align="center" width="160">
      <img src="assets/people/heyonghong.png" width="120" height="168" style="object-fit: cover; object-position: center;"><br>
      <div style="line-height: 1.2; font-size: 13px;">
        <b>Yonghong He</b><br>
        Professor<br>
        Tsinghua
      </div>
    </td>
    <td align="center" width="160">
      <img src="assets/people/guantian.png" width="120" height="168" style="object-fit: cover; object-position: center;"><br>
      <div style="line-height: 1.2; font-size: 13px;">
        <b>Tian Guan</b><br>
        Professor<br>
        Tsinghua
      </div>
    </td>
    <td align="center" width="160">
      <img src="assets/people/zhulianghui.png" width="120" height="168" style="object-fit: cover; object-position: center;"><br>
      <div style="line-height: 1.2; font-size: 13px;">
        <b>Lianghui Zhu</b><br>
        Postdoc<br>
        Tsinghua
      </div>
    </td>
    <td align="center" width="160">
      <img src="assets/people/huangqiang.png" width="120" height="168" style="object-fit: cover; object-position: center;"><br>
      <div style="line-height: 1.2; font-size: 13px;">
        <b>Qiang Huang</b><br>
        PHD Candidate<br>
        Tsinghua
      </div>
    </td>
  </tr>

  <tr>
    <td align="center" width="160">
      <img src="assets/people/ouyangminxi.png" width="120" height="168" style="object-fit: cover; object-position: center;"><br>
      <div style="line-height: 1.2; font-size: 13px;">
        <b>Minxi Ouyang</b><br>
        PHD Student<br>
        Tsinghua
      </div>
    </td>
    <td align="center" width="160">
      <img src="assets/people/lixiaoxiao.png" width="120" height="168" style="object-fit: cover; object-position: center;"><br>
      <div style="line-height: 1.2; font-size: 13px;">
        <b>Xiaoxiao Li</b><br>
        Master Student<br>
        Tsinghua
      </div>
    </td>
    <td align="center" width="160">
      <img src="assets/people/ruanshiting.png" width="120" height="168" style="object-fit: cover; object-position: center;"><br>
      <div style="line-height: 1.2; font-size: 13px;">
        <b>Shiting Ruan</b><br>
        Master Student<br>
        Tsinghua
      </div>
    </td>
    <td align="center" width="160">
      <img src="assets/people/yejiatong.png" width="120" height="168" style="object-fit: cover; object-position: center;"><br>
      <div style="line-height: 1.2; font-size: 13px;">
        <b>Jiatong Ye</b><br>
        Master Student<br>
        Tsinghua
      </div>
    </td>
    <td align="center" width="160">
      <img src="assets/people/yangbo.png" width="120" height="168" style="object-fit: cover; object-position: center;"><br>
      <div style="line-height: 1.2; font-size: 13px;">
        <b>Bo Yang</b><br>
        Master Student<br>
        Tsinghua
      </div>
    </td>
  </tr>
</table>

We also gratefully acknowledge Weiming Chen, Chang Qin, Jiawen Li ,Yizhi Wang and Mingxi Fu for their outstanding contributions that greatly advanced this project.

### Supporting Groups

<p align="center">
  <img src="assets/logos/tsinghua.png" width="190"/>
</p>

---

## Citation

If you find this repository helpful, please consider citing it in your own project page or awesome list.

```bibtex
@misc{awesome_ai4digitalpathology,
  title={Awesome AI4DigitalPathology},
  author={Contributors},
  year={2026},
  howpublished={\url{https://github.com/lingxitong/Awesome-AI4DigitalPathology}}
}
```

## ⭐ Star History

<p align="center">
  <a href="https://star-history.com/#lingxitong/Awesome-AI4DigitalPathology&Date" target="_blank">
    <img width="500" src="https://api.star-history.com/svg?repos=lingxitong/Awesome-AI4DigitalPathology&type=Date" alt="Star History Chart">
  </a>
</p>
