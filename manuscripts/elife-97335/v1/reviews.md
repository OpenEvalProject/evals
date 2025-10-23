# Peer review - Round 1

Editors:
- Lynne-Marie Postovit, Queens University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97335.3.sa0](https://doi.org/10.7554/eLife.97335.3.sa0)

In this useful article, the authors performed scRNA-seq on a diverse cohort of 15 early-stage cervical cancer patients. Correlative data is provided to support the possible establishment of an immunosuppressive microenvironment near SCL26A3+ cells, and an association of these cells with upstaging at time of surgery. However without more extensive validation, the evidence supporting the conclusions remains incomplete. Overall, this article will provide a potentially helpful dataset for researchers studying cervical cancer.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97335.3.sa1](https://doi.org/10.7554/eLife.97335.3.sa1)

Summary:

The authors in this manuscript performed scRNA-seq on a cohort of 15 early-stage cervical cancer patients with a mixture of adeno- and squamous cell carcinoma, HPV status, and several samples that were upstaged at the time of surgery. From their analyses they identified differential cell populations in both immune and tumour subsets related to stage, HPV status, and whether a sample was adenocarcinoma or squamous cell. Putative microenvironmental signaling was explored as a potential explanation for their differential cell populations. Through these analyses the authors also identified SLC26A3 as a potential biomarker for later stage/lymph node metastasis which was verified by IHC and IF. The dataset is likely useful for the community. The accuracy and clarity have been improved from the previous version, and additional immunofluorescence supporting the existence of their proposed cluster is now present. That said, there remain some issues with the strength of some claims (particularly in the abstract and results sections) and some of the cell type definitions.

Strengths

The dataset could be useful for the community

SLC26A3 could potentially be a useful marker to predict lymph node metastasis with further study

Weaknesses

Casual language is used in the abstract around immunosuppressive microenvironment and signal cross-talk between Epi_10_CYSTM1 cluster and Tregs. The data show localization that supports a possible interaction and probable cytokines, but functional experiments would be needed to establish causality.

In the description of the single cell data processing there is no mention of batch effect correction. Given that many patients were analyzed, and no mention was made of pooling or deconvolution, it must be assumed these were run separately which invariably leads to batch effects. Given the good overlays across patients some batch correction must have been performed. How was batch effect correction performed?

While statistics were added to the clinical correlates, it would appear that single variables are being assessed one at a time by chi-squared analysis. This ignores the higher order structure of the data and the correlations between some variables resulting in potentially spurious findings. This is compounded as some categories had below 5 observations violating the assumptions of a chi-squared test.

The description of all analytical steps remains quite truncated. While the inclusion of annotated code is useful, a full description of which tools were used, with which settings, and why each were chosen, is a minimum needed to properly interpret the results. This is as important in a mainly analytical paper as the experimental parameters.

Validation of the clustering results remains a problem. The only details provided are that FindClusters was used. This depends on a manual choice of multiple parameters including the k-nearest neighbours included, whether Louvain or Leiden clustering is used, the resolution parameter, and others (how many variable genes/PCs etc...). Why were these parameters selected, how do you know that you're not over or under-clustering.

The cluster Epi_10_CYSTM1 remains somewhat problematic. None of the additional data supports its existence outside of the single patient who has cells from that population. Additionally, it falls well outside of any of the other Epithelial cells to the point that drawing it as part of a differentiation order doesn't even make sense. Indeed, most of the upregulated pathways in this cluster appear to be related to class II antigen presentation which would fit better with a dendritic cell/macrophage than an epithelial cell. While the IF at the end does support the existence of the cluster, numbers are still very limited, and this doesn't have data on the antigen presenting function. At the least a strong disclaimer should be included in the text that this population is essentially exclusive to one sample in the scRNA data.

The linkage between the cluster types and IHC for prediction of lymph node metastasis is tenuous. Most of the strongly cluster associated markers were not predictive despite their clusters being theoretically enriched. This inability to recognize the clusters in additional samples using alternative methods does not give confidence that these clusters are robust. SLC26A3 being associated with upstaging may very well be a useful marker, however, given the lack of association of the other markers, it may be premature to say this is due to the same Epi_10_CYSTM1 cluster.

There are multiple issues in the classification of T cells and neutrophils. In the analysis of T cell subset, all CD4+ T cells are currently scored as Tregs, what happened to the T-helper cells? Additionally, Activated T and Cytotoxic T both seem to contain CD8+ cells, but all their populations have equivalent expression of the activation marker CD69. Moreover, the "Cytotoxic" ones also express TIGIT, HAVCR2 and LAG3 which are generally exhaustion markers. For neutrophils, several obviously different clusters have been grouped together (Neu_1 containing two diametrically opposite cell clouds being an obvious example).

Again in the CellChat section of the results causal language is being repeatedly used. These are just possible interactions, not validated ones. While the co-localization in the provided IF images certainly supports the co-localization, this still is only correlative and doesn't prove causality.

Minor Issues

The sentence "However, due to the low morbidity of ADC, in-depth investigations are insufficient" could be misinterpreted. Morbidity generally refers to the severity or health burden rather than the frequency of cases, though it's true in some studies prevalence is used for the overall impact of the disease on a population and referred to as morbidity. In this instance though, "incidence" or "prevalence" would be clearer word choices.

The previous rebuttal states that clusters/cell type calls were refined to eliminate issues such as epithelial cells creeping into the T cell cluster, however, the cell %s have not been altered according to the change tracking. Shouldn't all the %s have been altered even if only slightly?


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97335.3.sa2](https://doi.org/10.7554/eLife.97335.3.sa2)

Summary:

Peng et al. present a study using scRNA-seq to examine phenotypic properties of cervical cancer, contrasting features of both adenocarcinomas (ADC) and squamous cell carcinoma (SCC), and HPV-positive and negative tumours. They propose several key findings: unique malignant phenotypes in ADC with elevated stemness and aggressive features, interactions of these populations with immune cells to promote an immunosuppressive TME, and SLC26A3 as a biomarker for metastatic (>=Stage III) tumours.

Strengths:

This study provides a valuable resource of scRNA-seq data from a well-curated collection of patient samples. The analysis provides a high-level view of the cellular composition of cervical cancers. The authors introduce some mechanistic explanations of immunosuppression and the involvement of regulatory T cells that is intriguing.

Weaknesses:

I believe many of the proposed conclusions are over-interpretations or unwarranted generalizations of the single-cell analysis. I believe there may also be some artifacts in the data that may not reflect true biology--eg. The presentation of KRT+ neutrophils, which may reflect doublets with cancer cells. In some cases there is mention of quality control steps to remove contaminant cell clusters, but there is no method or supplemental figure to describe and/or justify these steps.

The key limitation is related to the "ADC-specific" Epi_10_CYSTM1 cluster, which is a central focus of the paper. This population only contains cells from one of the 11 ADC samples and represents only a small fraction of the malignant cells from that sample. Yet, this population is used to derive SLC26A3 as a potential biomarker. SLC26A3 transcripts are only detected in this small population of cells (none of the other ADC samples), which makes me question the specificity of the IHC staining on the validation cohort. The manuscript does not address why this marker is so rare in the scRNA-seq data, but abundant in the IHC.

While I understand it may be out of the scope of this individual study, many of the conclusions are inferred from the data analysis with little follow-up in experimental models or orthogonal assays.
