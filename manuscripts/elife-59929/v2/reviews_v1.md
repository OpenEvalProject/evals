# Peer review - Round 1

Editors:
- Hunter B Fraser, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59929.sa1](https://doi.org/10.7554/eLife.59929.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Individuals show heritable variation in gene expression, which is associated with disease susceptibility. In contrast to many other studies that have focused on mapping associations between genetic and gene regulatory variation, the current work addresses group dispersion/variance of gene expression among samples as well as the evolutionary processes that shape differences in gene expression between individuals, in both humans and chimpanzees. Using computational deconvolution, the authors demonstrate that cell-type heterogeneity is an important component of expression variability, with significant overlap of orthologous genes associated with eQTLs in both species. The conclusion is that gene expression variability in humans and chimpanzees often evolves under similar evolutionary pressures.

Decision letter after peer review:

Thank you for submitting your article "Gene expression variability in human and chimpanzee populations share common determinants" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Charles G Danko (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This is a solid study, with a large sample size, identifying quantitative trait loci (eQTLs) in humans and chimpanzees, using gene expression data from primary heart samples. The authors complemented the analysis of gene expression with a comparative eQTL mapping, as opposed to relying on mean expression levels, as most comparative studies like this one do. Also unlike many studies focused on mapping associations between genetic and gene regulatory variation, the authors paid attention to the group dispersion/variance of gene expression among samples as well as the evolutionary processes that shape the differences in gene regulation between individuals. The calculation of power for discovering differentially expressed genes as a function of sample size at the beginning of the paper is a thoughtful analysis that is useful to many in the community. All of the analyses are extremely thorough and well-executed. The statistical tests are appropriate and rigorous. Results are interpreted in a conservative fashion.

The main limitation is that the authors are not able to conclusively disambiguate between different causes of dispersion. Genetics, cell type, and technical variation may all contribute to dispersion. The authors state this very clearly throughout the manuscript. In part, this may reflect the authors' underselling their results somewhat. But in part, this really does reflect reality: Cell type is a major confounder that may provide false signals in other analyses.

Revisions for this paper:

The reviewers suggested a number of potential additions to clarify current results or build upon them. I will leave it up to the authors to decide which are worth including in their revision.

1) The first test authors conducted is to identify differentially variable (DV) genes. A total of 2658 DV genes were identified. The problem of the result is that almost equal number of up- and down-regulated DV genes symmetrically distributed around DV=0. Often, this is an indication of a lack of biological signals in data analysis. This might be due to the pooling of gene groups with diverse functionality together. Therefore, this reviewer suggests that authors should break down genes into subgroups to detail the up and down-regulatory patterns with the hope that some of the gene groups give interpretable results

2) The second test is to correlate the higher coding sequence conservation with lower dispersion. Again, the positive result is not unexpected. There are many indirect and/or confounding factors that may explain the effect. This reviewer, however, understands it is impossible to control them all (also authors have attempted to address some of them in the next few tests). However, here it is better to add exploratory analyses for genes in different functional groups and also give examples of outlier genes that do not follow the rule.

3) The third test is to examine the correlation between gene expression variability with single-cell type heterogeneity of samples. Authors first used Tabula Muris dataset to show dispersion is strongly correlated with cell-type specificity/diversity. If this is true, then the point that authors really wanted to demonstrate is, in fact, hampered. Authors might really want to show the "true" single-cell variability (see, for example, PMID: 31861624) is correlated with the level of group variance of gene expression.

4) The fourth test authors conducted is to show that dN/dS and Pn/Ps ratios of genes are correlated with gene expression variability (variance). However, because of the existence of heterogeneity of cell-type composition in samples, any correlation observed may be utterly biased by this single uncontrollable confounding factor. Furthermore, heart tissues contain an over-abundant expression of genes encoded in the mitochondrial genome. The expression level of these mt-genes may vary substantially between samples and reflect the health status of primary sample donors. PEER normalization may have to take this into account as a covariant.

5) Several other tests authors performed are around eQTLs (eGene overlap and eSNP overlap) between the two species. These are typical tests evolutionary biologists usually try to do whenever data are available. However, the issues with these types of tests are the low power in general. More importantly, in order to be consistent with previous tests which are all around the explanation of gene expression variance, this part should address the overlap between expression vQTLs in humans and chimps.

6) I would like to see more discussion about the inter-relatedness of the chimpanzees in the analysis of gene expression. Is that contributing to the power of the DE analysis, which has really high numbers of DE genes. That may certainly be due to the large samples size, but should be addressed. Related to that, the support that the gene-wise dispersion estimates are well correlated in humans and chimpanzees overall (Figure 1C, and Figure 2—figure supplement 1) seems qualitative. It looks like the chimpanzees might have less dispersion overall?

7) What do the authors think these findings mean for study systems outside of humans and captive chimpanzees? Both on the technical level (e.g. sample size), and for how their approach could be helpful outside of these species. Generalizing this approach would broaden the impact and audience of the paper.

8) Did the authors test directly whether eQTLs were enriched in genes with a high dispersion? I could not find this going back through the paper. This seems almost trivially likely to be true. I may have missed this result? Or did the authors worry this is too likely to be confounded with cell type? Either way, this seems like a result that may be useful to show even if the authors did acknowledge that it was likely to be confounded.

9) Did the authors consider looking for cell-type QTLs? They state several times in the paper the possibility that genetic factors may influence cell types. They have enough data – at least in human – to obtain QTLs for specific cell types, as others have done (Marderstein et al., 2020; Donovan et al., 2020). If these cell type QTLs were enriched near genes with a high dispersion, this may bolster the author's argument that genetic factors underlie dispersion by affecting cell type composition.

10) The scRNA-seq reference used for estimating cell types in heart tissue was derived from mice. Could this lead the authors to underestimate the degree to which cell types drive dispersion in genes that are variable between human and chimp? Genes that are variable between human/ chimp may also be more likely to be variable between either species and mouse, and perhaps this variability has led to them becoming more/ less of a marker of a specific cell population (and hence their dispersion in primates does not correlate with cell type specificity in mouse).

11) Have the authors tried estimating dispersion on top of what is expected based on differences in cell type? There are several strategies that might work for this: There are new strategies for estimating a posterior of cell type specific expression from a bulk sample, conditional on scRNA-seq data as prior information (Chu and Danko, 2020). These cell type specific expression estimates could then be analyzed for dispersion. Alternatively, it may also work to regress the estimated proportion of each cell type out of the dispersion estimates. While there are certainly a lot of pitfalls with using these strategies, especially in the setting shown here (all of this would work better if there were species matched reference data), they might provide an avenue for depleting the contribution of cell type differences from dispersion estimates.

12) Can the authors add a dotted line to show the shape of the distribution for genes with low dispersion, or where dispersion is shared in both human and chimpanzee, in Figure 4B? Is this different from genes that are dispersed in either chimp or human?
