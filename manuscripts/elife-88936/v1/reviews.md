# Peer review - Round 1

Editors:
- Xiaobing Shi, Van Andel Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88936.4.sa0](https://doi.org/10.7554/eLife.88936.4.sa0)

This valuable study aims to identify pioneer transcription factors - which are defined as transcription factors that compete with nucleosomes for DNA binding. The authors provide methods for identifying pioneer transcription factors on a cell type basis, using nucleosome positioning and motif information across different cell lines. The evidence to support the claims is largely solid. This work will be of interest to computational and molecular biologists working on transcription factors.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88936.4.sa1](https://doi.org/10.7554/eLife.88936.4.sa1)

Peng et al develop a computational method to predict/rank transcription factors (TFs) according to their likelihood of being pioneer transcription factors--factors that are capable of binding nucleosomes--using ChIP-seq for 225 human transcription factors, MNase-seq and DNase-seq data from five cell lines. The authors developed relatively straightforward, easy to interpret computational methods that leverage the potential for MNase-seq to enable relatively precise identification of the nucleosome dyad. Using an established smoothing approach and local peak identification methods to estimate positions together with identification of ChIP-seq peaks and motifs within those peaks which they referred to as "ChIP-seq motifs", they were able to quantify "motif profiles" and their density in nucleosome regions (NRs) and nucleosome depleted regions (NDRs) relative to their estimated nucleosome dyad positions. Using these profiles, they arrived at an odd-ratio based motif enrichment score along with a Fisher's exact test to assess the odds and significance that a given transcription factor's ChIP-seq motifs are enriched in NRs compared to NDRs, hence, its potential to be a pioneer transcription factor. They showed that known pioneer transcription factors had among the highest enrichment scores, and they could identify a number of relatively novel pioneer TFs with high enrichment scores and relatively high expression in their corresponding cell line. They used multiple validation approaches including (1) calculating the ROC-AUC and Matthews correlation coefficient (MCC) and generating ROC and precision-recall curves associated with their enrichment score based on 32 known pioneer TFs among their 225 TFs which they used as positives and the remaining TFs (among the 225) as negatives; (2) use of the literature to note that known pioneer TFs that acted as key regulators of embryonic stem cell differentiation had a highest enrichment scores; (3) comparison of their enrichment scores to three classes of TFs defined by protein microarray and electromobility shift assays (1. strong binder to free and nucleosomal DNA, 2. weak binder to free and nucleosomal DNA, 3. strong binding to free but not nucleosomal DNA); and (4) correlation between their calculated TF motif nucleosome end/dyad binding ratio and relevant data from an NCAP-SELEX experiment. They also characterize the spatial distribution of TF motif binding relative to the dyad by (1) correlating TF motif density and nucleosome occupancy and (2) clustering TF motif binding profiles relative to their distance from the dyad and identifying 6 clusters.

The strengths of this paper are the use of MNase-seq data to define relatively precise dyad positions and ChIP-seq data together with motif analysis to arrive at relatively accurate TF binding profiles relative to dyad positions in NRs as well as in NDRs. This allowed them to use a relatively simple odds ratio based enrichment score which performs well in identifying known pioneer TFs. Moreover, their validation approaches either produced highly significant or reasonable, trending results.

The weaknesses of the paper are relatively minor, and the authors do a good job of describing the limitations of the data and approach.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88936.4.sa2](https://doi.org/10.7554/eLife.88936.4.sa2)

In this study, the authors utilize a compendium of public genomic data to identify transcription factors (TF) that can identify their DNA binding motifs in the presence of nuclosome-wrapped chromatin and convert the chromatin to open chromatin. This class of TFs are termed Pioneer TFs (PTFs). A major strength of the study is the concept, whose premise is that motifs bound by PTFs (assessed by ChIP-seq for the respective TFs) should be present in both "closed" nucleosome wrapped DNA regions (measured by MNase-seq) as well as open regions (measured by DNAseI-seq) because the PTFs are able to open the chromatin. Use of multiple ENCODE cell lines, including the H1 stem cell line, enabled the authors to assess if binding at motifs changes from closed to open. Typical, non-PTF TFs are expected to only bind motifs in open chromatin regions (measured by DNaseI-seq) and not in regions closed in any cell type. This study contributes to the field a validation of PTFs that are already known to have pioneering activity and presents an interesting approach to quantify PTF activity.

For this reviewer, there were a few notable limitations. One was the uncertainty regarding whether expression of the respective TFs across cell types was taken into account. This would help inform if a TF would be able to open chromatin. Another limitation was the cell types used. While understandable that these cell types were used, because of their deep epigenetic phenotyping and public availability, they are mostly transformed and do not bear close similarity to lineages in a healthy organism. Next, the methods used to identify PTFs were not made available in an easy-to-use tool for other researchers who may seek to identify PTFs in their cell type(s) of interest. Lastly, some terms used were not defined explicitly (e.g., meaning of dyads) and the language in the manuscript was often difficult to follow and contained improper English grammar.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88936.4.sa3](https://doi.org/10.7554/eLife.88936.4.sa3)

Peng et al. designed a computational framework for identifying pioneer factors using epigenomic data from five cell types. The identification of pioneer factors is important for our understanding of the epigenetic and transcriptional regulation of cells. A computational approach toward this goal can significantly reduce the burden of labor-intensive experimental validation.

The authors have addressed my previous comments.

The main issue identified in this re-review is based on the authors' additional experiments to investigate the reproducibility of the pioneer factors identified in the previous analysis that anchored on H1 ESCs.

The additional analysis that uses the other four cell types (HepG2, HeLa-S3, MCF-7, and K562) as anchors reveals the low reproducibility/concordance and high dependence on the selection of anchor cell type in the computational framework. In particular, now several stem cell related TFs (e.g. ESRRB, POU5F1) are ranked markedly higher when H1 ESC is not used as the anchor cell type as shown in Supplementary Figure 5.

Of note, the authors have now removed the shape labels that denote Yamanaka factors in Figure 2c (revised manuscript) that was presented in the main Figure 2a in the initial submission. The NFYs and ESRRB labels in Supplementary 4a are also removed and the boxplot comparing NFYs and ESRRB with other TF are also removed in this figure. Removing these results effectively hides the issues of the computational framework we identified in this revision. Please justify why this was done.

In summary, these new results reveal significant limitations of the proposed computational framework for identifying pioneer factors. The current identifications appear to be highly dependent on the choice of cell types.
