# Peer review - Round 1

Editors:
- Jonathan Flint, University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61076.sa1](https://doi.org/10.7554/eLife.61076.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Genetic architecture underlying ecological adaptation in Atlantic herring is not consistent with the infinitesimal model" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Title: We suggest changing the title to avoid raising expectations about dismissing an infinitesimal model. For example: The genetic architecture underlying ecological adaptation in Atlantic herring.

Summary:

This paper reports population sampling and a scan for selection in Atlantic herring. The importance of the work derives from the application of genetic results for assessing herring stock, and hence help safeguard sustainable fishing, from better understanding of the genetic changes associated with different marine environments (herring have adapted to brackish sea water) and with the herring's photoperiodic regulation of reproduction. The paper reports analysis of whole genome sequence data from 53 population samples, selected from the entire species distribution, and identifies multiple loci underlying ecological adaptation to different geographic areas and spawning conditions.

Revisions for this paper:

1) Calibrating the test statistics. The P-values for selection are not well-calibrated. The null hypothesis is that the allele frequencies are identical between subgroups, which is inappropriate because even under neutrality they will vary because of drift and shared ancestry between populations. The selection test needs to be corrected for this population structure. There are a number of approaches that could be used, e.g. post-hoc (e.g. genomic control), or model-based (e.g. a mixed model or including PCs as covariates).

2) The paper does not make a convincing case that the findings are "in conflict with the infinitesimal model for complex traits". Overall the arguments presented are over-simplistic and fail to take into account the following:

i) An important question about adaption is the distribution of selection coefficients across mutations, for example whether adaptation is driven by new beneficial mutations of large effects that are selected to fixation or if adaptation is polygenic (e.g. Prichard et al., 2010, Current Biology). If the latter, then does it matter how “poly” polygenic is? In any case, even though the authors report a number of loci with large allele frequency shifts, can they actually reject an adaptation model with some loci with large effect sizes and many others with tiny effect sizes?

ii) The "pure" infinitesimal model is something of a straw man, since we know that there are a finite number of causal variants, with substantial variation in effect size and that we expect the change in allele frequency of any variant to depend on effect size. Instead, the results from the herring analyses seem consistent with the observations made in many systems (e.g body size in dogs or skin pigmentation in humans) that strong selection can lead to rapid differentiation driven by large-effect variants, even if the within-population architecture remains relatively infinitesimal.

iii) There is a distinction between the within-population variance (which may still be infinitesimal), and the between-population variation, which may be driven by a small number of large-effect and highly differentiated variants. Imagine you had two populations with exactly the same infinitesimal genetic architecture, but that differed by a single fixed variant with large effect. Would you say that was "in conflict" with the infinitesimal model?

3) It's possible that most, if not all, of the observed differentiation is due to adaptation. If Ne is very large, then natural selection and adaptation are efficient in eliminating deleterious alleles and fixing beneficial alleles. Do the authors have a model that is consistent with the observed presumed “neutral” variation? For example, the pairwise Fst values (0.01 to 0.06) are not small – are they consistent with the “long-term effective population size” that the authors hypothesise to be determined by periods of glaciation? Also, if short-term Ne is huge then why are the alleles under selection not swept to fixation? For a very large number of breeding individuals, Ne may be more limited by linkage than by demographic factors, a phenomenon that has been termed “genetic draft” (Walsh and Lynch, 2018, page 76).

4) The authors' interpretation of the PCA results is open to question. The authors first estimate frequency differentiation on all polymorphisms, then select the least and most differentiated loci and perform PCA plots on the ascertained sets of loci (Figure 2). The authors contrast the variance explained by the first PCs and the resulting structure from the two sets of loci and claim that the set of highly differentiated loci reflect ecological niche adaptation, whereas the less differentiated loci reflect location. While it's reasonable to identify the highly differentiated variants as Ancestry Informative Markers, the comparison of the variance explained likely does not mean that much. In any dataset, if you select highly differentiated variables, you will explain more of the variance with the first PC just by construction. For almost any genomic dataset, you would be able to select a small number of SNPs such that you could cluster populations based on PCA of those SNPs, but it does not necessarily follow that those highly differentiated SNPs are actually under selection – that needs to be shown. A related question is whether the extra clusters that appear with the differentiated markers are actually visible in the higher PC of the undifferentiated markers. It would be helpful to show maybe PC 3,4 etc… for those data.

5) The block-like structures in the selection scan are interpreted as inversions or structural rearrangements that are under selection. Inversions suppress recombination in the inversion, but not in the flanking regions, so if the inversion were under selection, you expect to see the normal decay of signal around the fringes of the inversion. Or is it just that the scale is different so you can't see the decay on the plots? Is it possible that the high differentiation in these regions is due to mapping errors in the rearranged regions? For example, a duplication would lead to apparently highly differentiated allele frequencies.

6) A related concern to the first point is whether there are technical batch effects due to i) combination of data sequenced in different experiments (i.e. previously published) and ii) combination of pooled and individual sequencing data. It would be helpful to make sure that these do not further inflate the test statistics.

7) Pooling errors. The authors use pools for sequencing and use a Neff allele count correction for read depth to minimise technical bias. They then use the estimated allele count in 2x2 tables to contrast allele frequencies between (super) pools, using an arbitrary p-value threshold of 1e-10. Not observing the actual allele count in the sample can lead to an increased variance and therefore a biased test for association.

Revisions expected in follow-up work:

1) P-value calibration. The selection scan uses an inappropriate null distribution and therefore all the P-values are poorly calibrated and thus uninterpretable. Whichever approach is chosen to calibrate P-values, please assess its performance and include QQ plots in the paper. Without this it's impossible to know how many of the selection hits are actually significant.

2) Either remove the claim that the results are in conflict with the infinitesimal model ( our recommendation) or provide a more convincing case to support the claim.

3) Please explain the extent to which the observed differentiation could be due to adaptation, dealing with the points we raised in point 3.

4) Please respond to our criticism of your interpretation of the PCA results.

5) Please defend your interpretation of the block-like structures in the selection scan, in response to our point 5.

6) Include batch in the model and check that none of the PCs are predicting batch or data type. Make sure that these do not further inflate the test statistics.

7) Provide data on how pooling errors might have affected your results. Please show Q-Q plots for their statistical test and estimate the sensitivity of your conclusions with respect to the chosen P-value threshold.
