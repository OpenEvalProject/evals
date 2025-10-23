# Peer review - Round 1

Editors:
- Charles Farber, https://ror.org/0153tk833 University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82535.sa0](https://doi.org/10.7554/eLife.82535.sa0)

In this article, the authors develop a method to identify potentially causal tissues and cell types for complex diseases by performing heritability enrichment estimation using information from gene regulatory networks. This article is of significant interest to geneticists and biologists interested in unraveling the molecular basis of disease. The key claims of the article are well supported by the data. The work has the potential to inform our understanding of the genetics of complex diseases.


---

# Peer review - Round 1

Editors:
- Charles Farber, https://ror.org/0153tk833 University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82535.sa1](https://doi.org/10.7554/eLife.82535.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Heritability enrichment in context-specific regulatory networks improves phenotype-relevant tissue identification" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and David James as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Please improve the description of the advance of the approach relative to other publications. How does this combination of an existing network method and an existing heritability enrichment method constitute substantial progress in the field?

2. Reporting of SpecVar-based heritability enrichment point estimates should be accompanied by appropriate measures of statistical significance (p-values, FDR-adjusted q-values, confidence intervals, etc.).

3. The comparisons between SpecVar and other approaches (AAP, ARE, SAP, SEG) are not sufficiently rigorous.

Reviewer #1 (Recommendations for the authors):

The approach taken in the study is conceptually interesting, however, it's not clear how novel the approach is. Additionally, there are several issues related to reporting results that need to be addressed. In particular, the authors do not report the statistical significance of enrichments using the new annotation aggregation method. Therefore, it is not possible to evaluate whether the higher overall heritability enrichment of the aggregate annotations they report compared to existing annotation approaches is meaningful.

1. Describe the novelty of the approach relative to other publications. How does this combination of an existing network method and an existing heritability enrichment method warrant a substantial advance in the field?

2. Reporting of SpecVar-based heritability enrichment point estimates should be accompanied by appropriate measures of statistical significance (p-values, FDR-adjusted q-values, confidence intervals, etc.).

3. The comparisons between SpecVar and other approaches (AAP, ARE, SAP, SEG) are not sufficiently rigorous.

a. First, please provide additional context. What is the amount of the genome covered by the regions defined by each approach? What is the overlap between these regions? For example, Table S4 shows SpecVar sets typically include substantially fewer regions than SAP. Are SpecVar regions primarily a subset of SAP regions or do they contain distinct/non-overlapping territory in the genome?

b. Second, please provide a way to evaluate whether differences in enrichment between the methods are statistically meaningful.

c. Fitting a joint LDSC model with multiple annotation sets would provide a more rigorous assessment of the performance of SpecVar relative to the other approaches.

4. Y-axes for bar plots in Figure 5 should start at 0. The floating y-axis origin is highly misleading.

5. The approach to defining context-specific REs based on overlap (>50% of bases overlapping for cross-group comparisons, and >60% of bases overlapping for within-group comparisons) seems quite stringent and likely excludes a lot of lineage-specific REs. Calculating enrichments for "group-specific" regulatory networks, where REs are considered group-specific if they do not overlap any of the other 35 groups resulting from the hierarchical clustering (ignoring whether an RE overlaps REs from other contexts within the same group), might provide more biologically relevant region sets.

Reviewer #2 (Recommendations for the authors):

– The authors only show the performance of the SpecVar method on 6 traits, however, it is not clear whether these are representative of all of the traits in UKBiobank. For traits with fewer SNP associations and lower sample numbers it appears that LDSC-SAP produces much high trait relevance scores, however, the authors use different tissues in each method so it may not be a fair comparison.

– The authors use the Pearson correlation coefficient to evaluate the performance of the SpecVar method, however, they should also consider other nonlinear metrics.

– The authors should consider a comparison with other regulatory network-based heritability methods such as CoCoNet, which is based on co-regulated genes. They should also compare to other non-network-based methods.

– The highlighted example SNP-associated network for the FOXC2 variants is interesting, however, the authors should demonstrate whether there are chromatin interactions (HiC or HiChIP) in brain tissues linking these variants in ATAC-seq peaks to the FOXC2 promoter. It would also be helpful to highlight another example using distinct UKBB phenotype and tissue datasets.

– It will be more interesting to adapt this to paired multimodal single-cell data if possible or expand on this in the Discussion.

– Lastly, LDSC-based methods may not perform well on admixed populations, thus some discussion on how this could be adapted using covariate-adjusted approaches (e.g. cov-LDSC) would be helpful.

Reviewer #3 (Recommendations for the authors):

The study would benefit from investigating the following questions:

Which part of the new annotation drives the extreme heritability enrichment from SpecVar, compared to other LDSC-based methods?

How to use the R score for a formal hypothesis test, rather than subjectively picking a few top-ranked tissues for the trait? How to evaluate the false positive rate for the test?

How to explain the inconsistent findings with previous studies, e.g., the association of the liver to LDL?

Are the GWAS signal in context-specific RE colocalised with context-specific eQTL signals?

How to link relevance score correlation across tissues to shared heritability between traits?
