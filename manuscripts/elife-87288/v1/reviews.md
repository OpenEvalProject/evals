# Peer review - Round 1

Editors:
- Tony Ng, King's College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87288.4.sa0](https://doi.org/10.7554/eLife.87288.4.sa0)

This study presents a valuable inventory of immune signatures that are correlated with cancer treatment-related pneumonitis. The data were collected and analyzed using validated methodology and can be used as a starting point for further prospective studies. The authors have provided an scRNA-seq analysis with an HD baseline using publicly available dataset and the evidence for their claims is convincing.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87288.4.sa1](https://doi.org/10.7554/eLife.87288.4.sa1)

Yanagihara and colleagues investigated the immune cell composition of bronchoalveolar lavage fluid (BALF) samples in a cohort of patients with malignancy undergoing chemotherapy and with lung adverse reactions including Pneumocystis jirovecii pneumonia (PCP) and immune-checkpoint inhibitors (ICIs) or cytotoxic drug induced interstitial lung diseases (ILDs). Using mass cytometry, their aim was to characterize the cellular and molecular changes in BAL to improve our understanding of their pathogenesis and identify potential biomarkers and therapeutic targets. In this regard, the authors identify a correlation between CD16 expression in T cells and the severity of PCP and an increased infiltration of CD57+ CD8+ T cells expressing immune checkpoints and FCLR5+ B cells in ICI-ILD patients.

The conclusions of this paper are mostly well supported by data, but some aspects of the data analysis need to be clarified and extended.

The authors should elaborate on why different sets of markers were selected for each analysis step. E.g., Different sets of markers were used for UMAP, CITRUS and viSNE in the T cell and myeloid analysis.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87288.4.sa2](https://doi.org/10.7554/eLife.87288.4.sa2)

The authors collected BALF samples from lung cancer patients newly diagnosed with PCP, DI-ILD or ICI-ILD. CyTOF was performed on these samples, using two different panels (T-cell and B-cell/myeloid cell panels). Results were collected, cleaned-up, manually gated and pre-processed prior to visualisation with manifold learning approaches t-SNE (in the form of viSNE) or UMAP, and analysed by CITRUS (hierarchical clustering followed by feature selection and regression) for population identification - all using Cytobank implementation - in an attempt to identify possible biomarkers for these disease states. By comparing cell abundances from CITRUS results and qualitative inspection of a small number of marker expressions, the authors claimed to have identified an expansion of CD16+ T-cell population in PCP cases and an increase in CD57+ CD8+ T-cells, FCRL5+ B-cells and CCR2+ CCR5+ CD14+ monocytes in ICI-ILD cases.

By the authors' own admission, there is an absence of healthy donor samples and, perhaps as a result of retrospective experimental design and practical clinical reasons, also an absence of pre-treatment samples. The entire analysis effectively compares three yet-established disease states with no common baseline - what really constitutes a "biomarker" in such cases? These are very limited comparisons among three, and only these three, states.

By including a new scRNA-Seq analysis using a publicly available dataset, the authors addressed this fundamental problem. Though a more thorough and numerical analysis would be appreciated for a deeper and more impactful analysis, this is adequate for the intended objectives of the study.
