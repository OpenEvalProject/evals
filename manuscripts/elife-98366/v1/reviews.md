# Peer review - Round 1

Editors:
- Ching-Hao X Wang, GlaxoSmithKline United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98366.3.sa0](https://doi.org/10.7554/eLife.98366.3.sa0)

The authors utilized single-cell RNA-seq profiling of non-small cell lung cancer (NSCLC) patient tumor samples to generate useful insights into the determinants of immune checkpoint inhibitor (ICI) responsiveness in NSCLC patients. While some of the findings add weight to the current literature, the analysis is incomplete due to the small cohort size and heterogeneous population which has limited their ability to draw statistically supported conclusion after adjusting for multiple hypothesis testing, as well as the lack of functional characterization of the findings. This study would benefit from external cohorts to both validate the findings and justify the statistical analysis undertaken.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98366.3.sa1](https://doi.org/10.7554/eLife.98366.3.sa1)

Summary:

The authors study the variability of patient response of NSCLC patients on immune checkpoint inhibitors using single-cell RNA sequencing in a cohort of 26 patients and 33 samples (primary and metastatic sites), mainly focusing on 11 patients and 14 samples for association analyses, to understand the variability of patient response based on immune cell fractions and tumor cell expression patterns. The authors find immune cell fraction and clonal expansion differences, as well as tumor expression differences between responders and non-responders, partly validating previous hypotheses, and partly suggesting new markers for ICI response. Integrating immune and tumor sources of signal the authors claim to improve prediction of response markedly, albeit in a small cohort and using in-sample metrics.

Strengths:

- The problem of studying the tumor microenvironment, as well as the interplay between tumor and immune features is important and interesting and needed to explain heterogeneity of patient response and be able to predict it.

- Extensive analysis of the scRNAseq data with respect to immune and tumor features on different axes of hypothesis relating to immune response and tumor immune evasion using state of the art methods.

- The authors provide an interesting scRNAseq data set with well-curated cell types linked to outcomes data, which is valuable

- High-quality immune cell type annotation including annotations based on additional ADT data

- Integration of TCRseq to confirm subtype of T-cell annotation and clonality analysis

- Interesting analysis of cell programs/states of the (predicted) tumor cells and characterization thereof

Weaknesses:

- Generally a very heterogeneous and small cohort where adjustments for confounding is hard. Additionally, there are many tests for association with outcome, where necessary multiple testing adjustments negate signal and confirmation bias likely, so biological take-aways have to be questioned.

- The authors claim a very high "accuracy" performance, however given the small cohort and possible overfitting due to in-sample ROC the generalization of this to other cohorts is questionable.

- Due to the small cohort with a lot of variability, more external validation is needed to be convincingly reproducible, especially when talking about AUC/accuracy of a predictor.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98366.3.sa2](https://doi.org/10.7554/eLife.98366.3.sa2)

Summary:

The authors have utilised deep profiling methods to generate deeper insights into the features of the TME that drive responsiveness to PD-1 therapy in NSCLC.

Strengths:

The main strengths of this work lie in the methodology of integrating single cell sequencing, genetic data and TCRseq data to generate hypotheses regarding determinants of IO responsiveness.

Some of the findings in this study are not surprising and well precedented eg. association of Treg, STAT3 and NFkB with ICI resistance and CD8+ activation in ICI responders and thus act as an additional dataset to add weight to this prior body of evidence. Whilst the role of Th17 in PD-1 resistance has been previously reported (eg. Cancer Immunol Immunother 2023 Apr;72(4):1047-1058, Cancer Immunol Immunother 2024 Feb 13;73(3):47, Nat Commun. 2021; 12: 2606) these studies have used non-clinical models or peripheral blood readouts. Here the authors have supplemented current knowledge by characterization of the TME of the tumor itself.

Weaknesses:

Unfortunately, the study is hampered by the small sample size and heterogeneous population and whilst the authors have attempted to bring in an additional dataset to demonstrate robustness of their approach, the small sample size has limited their ability to draw statistically supported conclusions. There is also limited validation of signatures/methods in independent cohorts and no functional characterisation of the findings. Because of these factors, this work (as it stands) does have value to the field but will likely have a relatively low overall impact.
