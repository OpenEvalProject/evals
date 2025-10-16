# Peer review - Round 1

Editors:
- Stephen CJ Parker, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58705.sa1](https://doi.org/10.7554/eLife.58705.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this manuscript, Kolberg et al. identified trans-eQTLs from isolated immune cell and blood gene expression data from thousands of samples isolated from individuals of European descent. After careful quality control, they used different approaches to identify co-expressed gene modules in these datasets, and used these modules for the eQTL scans. The careful analyses, including replication across different studies, indicates that the co-expression module-level approach is reliable for discovering trans-eQTLs with broad effects on gene expression.

Decision letter after peer review:

Thank you for submitting your article "Co-expression analysis reveals interpretable gene modules controlled by trans-acting genetic variants" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Stephen CJ Parker as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Helene Ruffieux (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this manuscript, Kolberg et al. identified trans-eQTLs from isolated immune cell and blood gene expression data from thousands of samples isolated from ~1000 individuals of European descent. They assessed the expression levels of ~18,000 genes. After careful quality control, they used five different approaches to identify co-expressed gene modules in these datasets. They identified nearly 4,000 co-expression modules. The sizes of these modules ranged from tens of genes to hundreds. They then summarized the expression of module genes by essentially calculating the first principle component of the module gene expression and labeled this summary statistic as the eigengene. They calculated the association of the eigengene with 6.8 million variants using linear regression and identified ~600 loci significant at the GWAS nominal threshold of 5e-8. They were able to determine that strong cis eQTLs were responsible for the associations of small modules. When they eliminated these cis-eQTL driven modules, they were left with ~300 associations. Correcting for multiple testing with an FDR procedure or Bonferroni approach reduced the number of significant associations to 140 and 4, respectively. They reassuringly identified two known trans eQTLs (IFNB1 and LYZ). The authors then focus on the ARHGEF3 locus, which was identified in a large blood eQTL meta-analysis, but here the authors show that the signal is platelet specific. This is an interesting approach to identify trans eQTL hotspots. All reviewers uniformly felt this work is of interest, but is in need of improvement in several areas. We list these below. If these areas can be satisfactorily addressed, the collection of candidate hits should constitute a valuable resource for generating hypotheses on eQTL regulation in specific cell types, to be explored in further research.

Essential revisions:

1) For the trans eQTL loci identified with the co-expression approach, the authors need to map the expression of individual genes (which they do) and then assess the overlap between the genes in the modules and the genes that significantly map to the same loci individually. The significance of association for each of the genes would not necessarily be genome-wide significant (say 5-e8) but the authors can relax the significance criteria at various p-value thresholds and assess the overlap between the module genes and individually mapped genes. If there is a significant overlap, this further strengthens their argument that eigengene mapping is a useful approach to detect additional trans eQTLs that cannot be detected with individual gene mapping.

2) The pros and cons of the different co-expression methods should be commented more extensively, in light of the data and question asked. The authors should discuss how the specificities of each method are reflected in the uncovered modules; the fact that conclusions are obtained from multiple methods does not justify eluding this discussion. For instance, Figure 1D seems to indicate that WGCNA tends to estimate fewer modules compared to funExplorer, any explanation why? Moreover, most of the co-expression methods involve a large number of tuning parameters. Although these parameters are provided in the Methods section, the strategy for choosing them is not described (data-driven? pilot analyses? are the default parameters always used, and if so, is it justified? etc) and the extent to which this may impact inference is not discussed. Finally, how do the different types of "eigengenes" produced by the co-expression methods (factor loadings, PCs, etc) affect eQTL mapping?

3) The authors mention: "In addition to replicating a number of established trans-eQTL loci". This is vague, can replication rates be provided? Given that trans associations are particularly difficult to uncover, this information would be particularly useful to assess the potential of the approach. The current discussion focuses on dissecting the two loci ARHGEF3 and SLC39A8 and does not allow one to fully appreciate the overall effectiveness of the proposed module-based eQTL mapping. Replication rates for the uncovered hits may be easily obtained: e.g., using the independent study from Kim-Hellmuth et al. for monocytes (which the authors use to confirm signals for the SLC39A8 locus) and, for the cell types with expression measured in two independent datasets (Table 1), one could "discover" the effects in the first dataset and "validate" them in the second dataset.

4) The authors rightly point out that module-based eQTL mapping reduces multiple testing. However, given that a same gene can contribute to multiple modules and that several co-expression methods are used on the same data, another complex source of multiplicity is introduced which would also require proper adjustment. This has not been addressed nor acknowledged. At the very least, a caveat should be formulated.

5) Another layer of complexity arises from the parallel analysis of datasets for each cell type and an "integrated" dataset combining all cell types. Hence, the same samples are analysed twice and the eQTL significance thresholds used in the paper again do not correct for this.

6) What is the overlap between the genes that map to the IFNB1 and LYZ loci in previous trans eQTL studies and the genes in the co-expression modules whose eigengenes mapped to these loci in this study? Is there a significant overlap? This should be reported. If there is no significant overlap, the potential reasons for this should be discussed.

7) What is the overlap among the gene membership of the three modules whose eigengene mapped to the ARHGEF3 locus? This is mentioned in the text but it is not clear how many genes are in each of the three modules. This locus was previously identified in a blood eQTL analysis. What is the overlap with the genes identified in the blood study and this study? If there is no significant overlap, the potential reasons for this should be discussed.

8) The authors should perform a conditional analysis, such as causal inference modeling, network edge orienting, mendelian randomization, etc to identify if the cis-associated gene really regulates the trans-associated gene expression.
