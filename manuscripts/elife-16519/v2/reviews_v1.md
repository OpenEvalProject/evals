# Peer review - Round 1

Editors:
- Jason Ernst, University of California, Los Angeles , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16519.032](https://doi.org/10.7554/eLife.16519.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A network of epigenetic modifiers and DNA repair genes controls tissue-specific CNA preference" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aviv Regev as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Rameen Beroukhim (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The focus of the paper is on identifying genes whose mutations associate with increased or decreased copy number alterations (CNAs) or changes in their lengths. The identified genes are found to be associated with epigenetic regulators, which motivated the comparison of the location of epigenetic marks with the positions of the CNA. A modestly significant enrichment for H3K9me3 and depletion of DNA methylation for the copy number alteration was then reported.

Since determinants of copy number alterations are poorly understood, the finding of this manuscript could potentially have significant impact. However the reviewers had significant concerns about the robustness of the analyses and to the extent the results were driven by confounders.

Essential revisions:

1) Of the 205 CONIM genes all but TP53 were associated with decreased mutation rates. There is concern that this is driven by confounders in particular variation in mutation rates across cancers. To quote one of the reviewer reports on this point and how this could be addressed:

"…Ciriello et al. showed that mutation and CNA rates are anticorrelated. Because high-mutation rate samples tend to have few CNAs, one would expect that most mutations would tend to be anticorrelated with CNA burden, regardless of whether there is a specific causal association. Indeed, all CONIM genes other than TP53 exhibited an association with low rates of CNAs, suggesting this confounder may be biasing the analysis. Moreover, the Methods indicate that known frequently mutated passengers (e.g. TTN) exhibited associations with CNA depletion, even when considering only silent mutations-suggesting that the results are due to confounders rather than causal relations.

To their credit, the authors recognised this as a potential issue and attempted to control for it by performing analyses within cancer types, on the supposition that CNA and mutation rates are relatively homogenous within cancer types. However, Ciriello et al. described the anticorrelation between mutation and CNA rates as occurring within cancer types as well. A better analysis would simply explicitly control for overall mutation rates when evaluating associations with CNA rates. This is easy to do and was first performed, I believe, in the Ding et al. Nature 2008 analysis of mutations in lung adenocarcinomas."

2) The authors need to better establish the results are robust to different processing pipelines they considered. Of note in the methods section an alternative pipeline with relatively small differences was applied reporting 61 genes of which only 22 were in the intersection. Of these 61, 13 were associated with higher mutations and 48 lower mutations. This raises several issues that should be addressed:

i) Since only about 10% of the 205 CONIM genes are reported by both pipelines a convincing argument needs to be made that the remaining 90% are meaningful and not driven by confounders related to differences between cancers.ii) It should be established that the results from the largest connected component in the PPI network analysis would still hold if focusing on just the set of 22 intersection genes or all 61 genes from the alternative pipeline.iii) Show the significant p-values with respect to the epigenome analysis remain significant when using genes produced from the alternative pipeline. iv) Reconcile the fraction of genes with higher mutations went from 0.5% to 21% between the two pipelines which is qualitatively different.

3) When considering the relationship between CNAs and survival time control for overall tumor ploidy. There is concern that the observed relationship could be explained by whole genome doubling, since that may allow the rate of cancer genome evolution to increase, generating a more aggressive tumor (Dewhurst & McGranahan et al., 2014).

4) When showing increased CADD scores of CONIM genes control for the step of selecting genes which were non-silently mutated. This is necessary to establish the result is not an artifact of filtering silent mutations.

5) To make the association between the enrichment of genes involved in histone methylation in the CONIM genes and the CNA breakpoints are enriched for H3K9me3 more convincing establish that those tissues with H3K9me3-enriched CNA breakpoints also have an increased number of mutations in histone methylation CONIM genes.

6) For the result that 6 of 19 cancer types fewer CNA were associated with significantly better survival and 5 of 19 with shorter CNA additional information should be reported to aid the interpretation of the results. Specifically what is the overlap between the 5 and 6 cancer types and also were there any cancer types associated with significantly worse survival?

7) Aspects of the comparison between the H3K9me3 and DNA-methylation at breakpoints should be expanded upon to enable evaluation of it. It is reported there is a significant depletion at a p-value of 0.05, but it should be stated how many actually were the intersection, which could still be substantial. When comparing H3K9me3 and DNA-methylation sites it should be clarified if only non-intersection sites were considered and stated how many sites were in each group.

8) The comparison of number of CNAs and% of heterochromatin across cancer/tissue types (Figure 6C) raised questions and concerns that should be addressed. The analysis is only based on seven cancer types with one, ovarian cancer, manually excluded for being an outlier so there are concerns related to the robustness of this result. Is there are any justification for treating ovarian cancer separately? Since ovarian cancer has frequent TP53 mutations, the question was raised as to whether TP53-mutatant cancers exhibit the same relations between heterochromatin and CNA burden. It is also not clear why additional cell types with matched epigenomes listed in Table S2 and in the methods were not included in the analysis. It should be established that the relationship still holds when considering additional cell types. Also it should be clarified how in some cases the reference epigenome for the cancer type was selected when there was multiple matching ones and establish that the results are robust to that selection. For instance epigenome E061 was used for Foreskin Melanocyte Primary Cells, but there exists another reference epigenomes (E059) in the same cell type for a different individual that was not used.

9) A number of statements of causality are made in the manuscript based on correlative evidence. These statements should be adjusted to reflect their correlative nature assuming the authors do not have functional data to support them.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A network of epigenetic modifiers and DNA repair genes controls tissue-specific copy number alteration preference" for further consideration at eLife. Your revised article has been favorably evaluated by Aviv Regev (Senior editor), a Reviewing editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The reviewers remain concerned that TP53 is the only CONIM gene not associated with decreased mutation rates and that this was not reproduced with alternative pipelines. There is concern that this result is still being driven by confounders for which the linear correction applied is inadequate. Below is a quote of one reviewer describing the issue and a better way to do the correction. It is essential that this issue be addressed.

"The manuscript is improved but the primary result-that 62 genes are associated with decreased CNA rates and only one (TP53) was associated with increased rates-raises the concern that a confounder continues to drive much of the association between mutation rates in specific genes and lack of CNAs. This may be because the authors used a linear regression model to control for varying CNA rates, whereas the relation may be non-linear and indeed appears so in Ciriello et al. The method I indicated previously should not have such an issue. This method was to control for CNA rates as per Ding et al. Nature 2008 in their analysis of lung adenocarcinomas. In this, they simply permute mutations in any gene across samples, while maintaining overall mutation rates in that sample. For instance, if one has a list of mutations as: column 1: sample id, column 2: mutated gene in that sample, one could simply permute the second column. These permutations would form a background model against which one could compare observed data to generate p-values."

A few additional points were raised that should be addressed as appropriate:

1) No CONIM genes are directly implicated in histone methylation, this should be stated in the manuscript and possible explanations discussed. In addition, the cherry-picking of a single CONIM gene for establishing a link between H3K9me3 enrichment and CONIM genes is a weakness. This portion of the manuscript could be strengthened by a similar analysis performed in a more unbiased analysis (e.g., including all genes involved in methylation "reading" instead of just EP400).

2) For the part "Out of these 540 genes, 122 were also…", these numbers were not updated to reflect the other revisions from the previous submission

3) The discussion of the VAF analysis (Discussion section, paragraph two) slightly overstates the conclusions that can be drawn from the results, since only 2 of the 5 cancer types tested had lower VAFs associated with CONIM gene mutations (subsection “Gene mutations are linked to a differential CNA number”).

4) Include some mention of the extent of agreement between alternative pipelines in results/discussion and not just methods.
