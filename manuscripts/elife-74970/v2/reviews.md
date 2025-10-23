# Peer review - Round 1

Editors:
- Jonathan Flint, https://ror.org/046rm7j60 University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74970.sa0](https://doi.org/10.7554/eLife.74970.sa0)

The findings reported here are important because they address the issue of how complex traits arise from their genetic underpinnings. There is an assumption that genetically mediated variation in transcript abundance, usually detected via analysis of expressed quantitative trait loci, is key to this process, but we lack robust evidence in support of that view. This article finds limited evidence that the baseline expression of trait-related genes explains the associations between complex traits and genetic variants (as identified from genome-wide association studies), leading to the view that the field needs to confront a problem of 'missing regulation.'


---

# Peer review - Round 1

Editors:
- Jonathan Flint, https://ror.org/046rm7j60 University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74970.sa1](https://doi.org/10.7554/eLife.74970.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The missing link between genetic association and regulatory function" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Molly Przeworski as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All the reviewers agreed that you've identified important concerns regarding the hypothesis that the majority of genetic variants contributing to complex traits act by the altering transcript abundance. However we would like you to address the following points:

1) Most importantly, we're not convinced you've chosen an appropriate set of genes to make your case. Your assumption that Mendelian and cognate complex traits share the same set of causal genes needs further justification. One possibility might be to use as a starting point the association between GWAS and rare variant analyses reported in the UK biobank data

https://doi.org/10.1038/s41586-021-04103-z

and/or data from the recent study of obesity (https://www.science.org/doi/10.1126/). The enrichments reported in those papers are higher than the Cell paper you quote, and would provide a set of genes that are not selected on the basis of Mendelian large effects.

2) If you choose to focus on the 143 genes from Mendelian genetics then there are a number of issues you need to resolve.

(i) why are candidate genes were not enriched in the GWAS regions for height and breast cancer?

(ii) we suggest you quantify the number of genes in the GWAS regions expected to be found if the 143 genes had been randomly selected. Correcting the observed number of genes for that expected by chance (e.g., subtracting the observed number by that expected by chance), the proportion of candidate genes in the GWAS regions is likely to be small.

3) Tissue context. The tissues listed in Table 2 omit some that are relevant to the phenotype (such as bone for height (Finucane et al. 2015 NG)). Expanding this list and selecting appropriate tissues might substantially alter your conclusions. Among the 84 putatively causative genes that overlap GWAS signals, the number that overlap is reduced substantially when restricting analysis to the selected tissues for each trait. If genes function only in the relevant tissues, using bulk expression data loses power, but is unlikely to give false positives. Thus, it is possible that for the traits analysed, not all relevant tissues are selected, so that only a fraction of genes identified in the bulk expression analysis can be replicated in the tissue-specific analysis.

4) How much do both LD differences between GWAS and eQTL samples and the presence of allelic heterogeneity contribute to the observed low colocalization rate? While we agree that power for locus detection is probably not a big issue, sample size differences betweenGWAS and GTEx datasets might make small differences in LD between the two samples cause a statistical separation of the signals, even when trait phenotype and gene expression truly share a causal variant.

The presence of more than one causal variant with allelic heterogeneity at the locus may also play a part in the failure of colocalization. Consider two causal variants for the complex trait, one regulating the target gene and the other regulating another gene in co-expression. Potentially, the presence of the second causal variant would diminish the colocalization probability at the target gene.

One possible way to deal with these issues is to perform simulations to quantify the influence of tissue-specific expression effects, LD differences between eQTL and well-powered GWAS, and allelic heterogeneity. At the least, we think you should discuss the problems we raise here in some detail.

5) TWAS results. While only 6% of the putatively causative genes are identified by TWAS with the correct direction of effect, this number is misleading as one may interpret it as meaning that only 6% of the functionally relevant genes are regulated by trait-associated variants. In fact, 46% of the genes are detected by TWAS, but only 11% are confirmed in their selected tissues, among which about half (5/9) have correct direction of effect. The result could be due to the selection of relevant tissues, or it may reflect a nonlinear relationship between expression and trait or the presence of cell type heterogeneity within a tissue. Again we think a more nuanced discussion of this issue is important.

Reviewer #1 (Recommendations for the authors):

The number of traits examined (seven or nine) limits the generalizability of the findings. The study would strongly benefit from adding more traits. In addition, the study would benefit from the inclusion of results from the few available cell-type-specific/dependent eQTLs from single-cell or deconvolved bulk RNA-Seq experiments.
