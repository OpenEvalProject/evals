# Peer review - Round 1

Editors:
- Jian Xu, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71735.sa0](https://doi.org/10.7554/eLife.71735.sa0)

This study describes an integrative analysis of the location, regulation, and function of melanoma cell state-specific enhancer elements. By comparing enhancer activity through massively parallel reporter assays, chromatin features, and underlying TF binding profiles in melanocytic and mesenchymal-like melanoma cell states, the authors identify candidate regulators and mechanisms that explain enhancer activity and specificity in melanoma biology. These findings will be of broad interest to those seeking to understand cell type- or cell identify-specific gene regulation at the level of transcriptional and epigenetic control of cis-regulatory elements.


---

# Peer review - Round 1

Editors:
- Jian Xu, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71735.sa1](https://doi.org/10.7554/eLife.71735.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Analysis of long and short enhancers in melanoma cell states" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jian Xu as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard White as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Provide more details on the filtering and selection criteria for the identification of MES- and MEL-specific regions. A simple flowchart to illustrate the major selection criteria might be helpful.

2) Consider improving the nomenclature for various enhancer regions, as commented by Reviewer #1.

3) For the identification of candidate TFs and their combinations responsible for differential enhancer activity in MEL vs MES cells, DeepMEL2-based analysis does not seem to provide robust predictions. This is also exemplified by the analysis of binding sites for MITF and AP-1, as commented by Reviewer #2. Therefore, the authors may use available ChIP-seq data for candidate TFs and quantitatively compare signals at the respective enhancers in different cell states. This analysis may be further extended to other differentially enriched H3K27ac and/or ATAC-seq peaks to evaluate whether the identified TFs are generally associated with differential H3K27ac and/or ATAC-seq signals between cell states.

4) Provide information about AP-1 expression in MEL-intermediate cells with and without SOX10 knockdown, as commented by Reviewer #2.

5) While altering TF binding sites at native gene loci may be technically challenging (and would be good for future studies), it would be helpful to include an analysis of SOX10, MITF or AP-1 mutations in the context of a larger MPRA sequence on a few test cases to determine the effect on enhancer activity, as commented by Reviewer #3. This would be informative for future investigators that the MPRA assay would be a useful method for figuring out which TF sites would be good to go after in vivo.

6) Additional discussion on the functional roles of SOX10 and MITF in melanoma pathophysiology would be helpful to highlight the broad relevance of findings in the current study.

7) Consider revising figures to increase readability.

Reviewer #1 (Recommendations for the authors):

1. It would be helpful to provide more details on the filtering and selection criteria for the identification of 35 MES- and 18 MEL-specific regions as H3K27ac ChIP-seq based library. Is there any normalization steps for ChIP-seq and ATAC-seq signals across samples? How are enhancer target genes defined? A simple flowchart to illustrate the major selection criteria might be helpful.

2. Line 102, 18 MES-specific ATAC-seq peaks were selected from 35 MES-specific H3K27ac peaks. Are there H3K27ac peaks without selected ATAC-seq peaks? If so, why were those H3K27ac peaks excluded for the current study?

3. It is advised to improve the nomenclature for various enhancer regions. Instead of using Gene_1, Gene_2, etc, it would be more informative to show the location and distance of the enhancers to the TSS of putative gene targets. For example, Gene_+10kb indicates an enhancer located 10kb upstream of the TSS while Gene_-10kb indicates 10kb downstream of TSS. The distance could be determined by distance between the peak summit of ATAC-seq (or H3K27ac if they overlap) and TSS.

4. For the identification of candidate TFs and their combinations responsible for differential enhancer activity in MEL vs MES cells, DeepMEL2-based analysis does not seem to provide robust predictions. Therefore, the authors may also use available ChIP-seq data for candidate TFs and quantitatively compare the normalized ChIP-seq signals at the respective enhancers in different cell states. This analysis may also be extended to include other differentially enriched H3K27ac and/or ATAC-seq peaks to evaluate whether the identified TFs (e.g. SOX10-MITF for MEL and AP1 for MES) are generally associated with differential H3K27ac and/or ATAC-seq signals between cell states.

Reviewer #2 (Recommendations for the authors):

This manuscript is mostly convincing, but a few aspects of data need to be clarified to strengthen the main conclusions.

1. In Figure 1a, a MITF binding site was predicted within IRF4 enhancer and a serial of tiles with mutated MITF motif were constructed based on the prediction. However, in comparison with the MITF ChIP-seq track, the predicted MITF motif apparently located outside of the MITF ChIP peak. This is also true for predicted AP-1 binding sites in COL5A1 and HEG1 enhancers. How accurately can those predicted TF bind sites based on DNA sequence represent the TF binding on chromatin in vivo?

2. SOX10 KD shifts MEL-intermediate cell to MES phenotype and shapes the landscape of chromatin accessibility. Upon SOX10 KD, does AP-1 expression increase and gained ATAC-seq peaks display high predictions score for topic 19?

3. Authors conclude that AP-1 binding alone drives MES state specific enhancer activity. However, MES enhancers, such as COL5A1_5 region, show strong enhancer activities by reporter assay in MEL-intermediate cell as well, despite that the endogenous loci remain close in those cells (as shown in Figure 6a). How much AP-1 protein is expressed in MEL-intermediate cells?

Reviewer #3 (Recommendations for the authors):

To address weaknesses:

1) To better contextualize the role of specific TFs in regulating a given gene in Weakness 1 – Altering or deleting TF binding sites or subregions of specific enhancers, especially at the scale of test sequences discussed in this study, at the native gene locus seems destined for future studies, although could be argued is the truest measure of the role of an individual TF site/enhancer subregion. As a potentially more intermediate/approachable assay, could an analysis of SOX or MITF or AP-1 mutations in the context of a larger MPRA sequence (e.g. 510 bp or in the H3K27Ac 1-2 kb sequence) in addition to the tiled versions (Supp Figure 7 or 10) be done on a few test cases to capture enhancer context better. As the authors note on page 19, lines 496-497, ~500 bp sequences may be needed to capture sufficient complexity of the enhancer.

2) Brief mention of the demonstrated functional role of SOX10 and MITF protein in melanoma onset/growth/survival could be included (e.g. shRNA knockdown of sox10 decreasing human melanoma growth in culture or knockdown/deletion delaying/blocking melanoma in animal models). The binding sites for these TFs are clearly relevant in the assays shown, but the larger context/support for these TFs role in melanomagenesis could thus be better highlighted. Similarly, SOXE dimer sites have been noted to be over-represented in melanoma-specific DNase I hypersensitive sites previously (Huang et al., and Jauch, Scientific Reports, 2015) and supports the papers conclusions.

Data availability appears appropriate.
