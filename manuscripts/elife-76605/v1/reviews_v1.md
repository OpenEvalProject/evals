# Peer review - Round 1

Editors:
- Joseph Lewnard, https://ror.org/01an7q238 University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76605.sa0](https://doi.org/10.7554/eLife.76605.sa0)

This work presents insightful epidemiologic and phylogenetic analyses of tuberculosis cases across Valencia, Spain, and comparator low-burden (Oxfordshire, UK) and high-burden (Karonga, Malawi) regions. Findings reveal that the "low burden" observed in Valencia is not in fact reflective of low transmission in this setting, with detected lineages likely to have circulated locally over the course of decades and to have been transmitted in the community.


---

# Peer review - Round 1

Editors:
- Joseph Lewnard, https://ror.org/01an7q238 University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76605.sa1](https://doi.org/10.7554/eLife.76605.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Population-based sequencing of Mycobacterium tuberculosis reveals how current population dynamics are shaped by past epidemics" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Conor J Meehan (Reviewer #1); Timothy M Walker (Reviewer #2).

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

1) Comments from Reviewer 1 emphasize the need for several refinements to the BEAST analyses, most important among which is the issue of ascertainment biases. If sampling completeness is systematically different over time or in association with particular patient epidemiologic characteristics, then this may raise concerns about interpretation of the findings from this analysis. Specific reference is also made here about distinguishing timing of transmission events vs. time to the most recent common ancestor (coalescent).

2) Reviewer 2 raises the comment that the analysis presented in Table S3 would be stronger if a multivariate analysis had been performed, i.e. controlling for each of the risk factors to determine if they were independently associated with transmission events/clustering.

3) Reviewer 2 also raises points regarding the interpretation of SNP thresholds in settings with differing transmission characteristics, which likewise merit consideration when the authors revise their Discussion.

4) Formatting of the revised manuscript should follow eLife's style guidelines including use of an unstructured abstract. Text in the figures, including in legends and axis labels, is in many places illegibly small and cannot be read on a written page or screen without substantial magnification; this should be fixed.

Reviewer #1 (Recommendations for the authors):

Low burden vs low transmission

The framing of the 'low burden doesn't mean low local transmission' needs a better set up and implications explanation. On line 104 this is somewhat set up but it needs to be more clearly stated as an aim of the study. Additionally, what public health officials should do in low burden settings to better use these findings could be explained in the discussion. This would make it easier to read and help people create actionable decisions from these findings.

Line 352 about the future of the Spain TB profile: What backs this up? This is a crux, I think, of what you are trying to get at overall in the paper but it does not come across.

Potential sample bias

You had a few L5 and L6 in your dataset, yet these are more likely to not grow sufficiently within 3 weeks on 7H11, usually requiring 4 weeks. Do you think this could create bias in your sequenced dataset?

Referencing past work

There are a lot of great points made by the authors that perhaps come across as novel but have been shown before and should be referred to. Some examples (but not limited to): Roetzer et al. Plos Medicine 2013 looked extensively at contact tracing vs SNPs; Meehan et al. Ebiomedicine 2018 looked at time vs SNP cut-off; Meumann et al. Lancet Regional Health 2021 looked at time between cases linked genomically and epidemiologically. Some comparisons and general discussion of the findings in the context of these and other papers would be of benefit here.

This dataset was previously published in Xu et al. Plos Medicine 2019 but little reference is made to that paper or its findings. Indeed authors start the discussion stating they present the first population study in Valencia, but that's not exactly true since it was previously published by Xu, although not analysed in this context. Also, an explanation of why a 15 SNP cut-off was used there but a 12 SNP cut-off is used here should be made evident to the reader.

Time tree creation

I don't see in the main or supplemental data anything about ascertainment bias correction for the phylogenies, especially the BEAST analysis. Were SNP alignments or complete WGS data used for the time trees? If SNP, were the invariant counts included to correct the branch lengths? If not, the dates on the branches are most certainly incorrect and need to be redone. If the full genome was used, this needs to be more apparent in the text. Perhaps the BEAST XML file could be supplied via a figshare link or similar.

As stated above, I feel the historical transmission analyses is weak and not well explained. I found it difficult to follow but it seems that only local-born samples were used for this? Although the authors state they are not trying to estimate all transmission in this period, even their approach will result in large inaccuracies in different settings with different sampling fractions and burdens. For example, even a small difference in sampling fraction can have an effect on these transmission event estimations without something like TransPhylo to correct for the sampling fraction (see Séraphin et al. Am J Trop Med Hyg. 2018 for an example). The Xu et al. paper even showed that in Valencia there is a lot of missed index cases from epidemiological data that is found by TransPhylo. These would potentially also all be missed here without the additional Bayesian analyses of TransPhylo over the standard BEAST analyses.

My feeling is that the authors are actually trying to estimate coalescent events, not transmission events. I.e. when did two random Spanish-derived isolates in the current dataset share a common ancestor? If done within sub-lineages or similar, the distributions of these coalescence times and comparisons between settings may better illustrate the point than trying to estimate the amount of transmission within this time period.

Reviewer #2 (Recommendations for the authors):

The authors use a Fisher's exact test to assess the relationship between risk factors and clustering. Why was a logistic regression model not used, which would have allowed for a multivariable analysis? This would be preferable as would further assess which risk factors remain significant after correcting for others.

Line 221-2: The argument presented here is that 12 SNPs is less applicable where cases can be clustered between consecutive, ever larger SNP intervals. If the idea behind a threshold is essentially pragmatic, denoting a cut-off where sensitivity and specificity are optimised (as elegantly shown in Figure 2), then how is that impacted by the existence of isolates that are 20, 30, 50 or 100 SNPs apart? Is the argument that the existence of such intermediate distances implies possible epidemiological linkage across them that would inform contact tracing in a helpful way? That would seem unlikely, but it seems to be the implication, namely that it renders the 12 SNP threshold (which is/was epidemiologically defined for contact tracing) less applicable. I would have thought that different patterns are seen in Valencia and Malawi than in Oxfordshire because most of the cases there are endemic rather than imported. Long term transmission dynamics (by which we might understand the survival and expansion of particular clones/strains in a population) are indeed best understood phylogenetically rather than based on thresholds. But it's not clear why the data support 12 SNPs being less informative for contact tracing in Valencia or Malawi. If anything, a lower threshold (e.g. 5 SNPs or less) would make more sense where transmission is more intense, as it would be more specific and avoid investigating links between cases who might in truth be separated by several transmission events (i.e. intermediary cases). In subsequent paragraphs, the authors say just this. I would suggest rethinking how these findings are best interpreted in the text here, or at least successfully rebuffing the points above.
