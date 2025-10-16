# Peer review - Round 1

Editors:
- Seunghee Hong, Yonsei University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98469.3.sa0](https://doi.org/10.7554/eLife.98469.3.sa0)

This manuscript presents an important contribution to the field of single-cell transcriptomic analysis in cancer by introducing a novel computational framework-SCellBOW-which applies embedding techniques from natural language processing to model phenotypic heterogeneity in tumors. The revised version includes new validation experiments and significant clarifications that provide convincing evidence for the method's utility. The authors have benchmarked SCellBOW across diverse datasets, including glioblastoma, breast, and metastatic prostate cancer, and have demonstrated its superior performance compared to existing state-of-the-art methods.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98469.3.sa1](https://doi.org/10.7554/eLife.98469.3.sa1)

Summary:

The authors developed a novel tool, SCellBOW, to perform cell clustering and infer survival risks on individual cancer cell clusters from the single cell RNA seq dataset. The key ideas/techniques used in the tool include transfer learning, bag of words (BOW), and phenotype algebra which is similar to word algebra from natural language processing (NLP). Comparisons with existing methods demonstrated that SCellBOW provides superior clustering results and exhibits robust performance across a wide range of datasets. Importantly, a distinguishing feature of SCellBOW compared to other tools is its ability to assign risk scores to specific cancer cell clusters. Using SCellBOW, the authors identified a new group of prostate cancer cells characterized by a highly aggressive and dedifferentiated phenotype.

Strengths:

The application of natural language processing (NLP) to single-cell RNA sequencing (scRNA-seq) datasets is both smart and insightful. Encoding gene expression levels as word frequencies is a creative way to apply text analysis techniques to biological data. When combined with transfer learning, this approach enhances our ability to describe the heterogeneity of different cells, offering a novel method for understanding the biological behavior of individual cells and surpassing the capabilities of existing cell clustering methods. Moreover, the ability of the package to predict risk, particularly within cancer datasets, significantly expands the potential applications.

Weaknesses:

Given the promising nature of this tool, it would be beneficial for the authors to test the risk-stratification functionality on other types of tumors with high heterogeneity, such as liver and pancreatic cancers, which currently lack clinically relevant and well-recognized stratification methods. Additionally, it would be worthwhile to investigate how the tool could be applied to spatial transcriptomics by analyzing cell embeddings from different layers within these tissues.
