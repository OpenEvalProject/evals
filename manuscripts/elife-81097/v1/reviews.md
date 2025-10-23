# Peer review - Round 1

Editors:
- Evan Graehl Williams, https://ror.org/036x5ad56 University of Luxembourg Luxembourg

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81097.sa0](https://doi.org/10.7554/eLife.81097.sa0)

The reviewers found that your article brings important new methods and insight for how to analyze large, complex, multi-omic datasets in order to highlight specific molecular hypotheses for follow-up validation. As realistic/affordable sample sizes for population studies with omics data have recently exploded in size, this has raised the clear need for new or adapted statistical methods for best exploiting the increased statistical power. This work is compelling and we believe it should be of general interest to biologists and biostatisticians, and of particular interest to those working on (or those who could work on) large cohorts.


---

# Peer review - Round 1

Editors:
- Evan Graehl Williams, https://ror.org/036x5ad56 University of Luxembourg Luxembourg

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81097.sa1](https://doi.org/10.7554/eLife.81097.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Exploiting the mediating role of the metabolome to unravel transcript-to-phenotype associations" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Evan Graehl Williams as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by David James as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

In brief, besides the reviewer-specific comments, there was a common thread regarding significances of the findings (both in the statistical sense and in the colloquial sense) and description of the method. I also apologize for the delay in the reviews; it was a huge challenge to get reviewers in July and August, and we potentially may consult a third reviewer for the revision.

Reviewer #1 (Recommendations for the authors):

Auwerx et al. have taken a new (or recent?) approach to mine large existing datasets of intermediary molecular data between GWAS and phenotype, with the aim of uncovering novel insight into the molecular mechanisms which lead a GWAS hit to have a phenotypic effect. The authors show that you can get additional insight by integrating multiple omics layers rather than analyzing only a single molecular type, including a handful of specific examples, e.g. that the effect of SNPs in ANKH on calcium are mediated by citrate. Such additional data is necessary because, as the authors' point out, while we have thousands of SNPs with significant impact on phenotypes of interest, we often don't know at all the mechanism, given that the majority of significant SNPs found through GWAS are in non-coding (and often intergenic) regions.

Scientific comments

(1) It's not quite clear to me whether the authors have designed a new method or have applied a recently-developed method. I follow that the general approach uses MR across multiple data types and then merges the results. I did look at the Github repo ("Gene_Metab_Pheno") but I'm not enough of a mathematical bioinformatician to really judge the novelty there, as to whether this is a new method or application of relatively recent other methods.

(2) The sample sizes are huge here since it is a meta-analysis, which means it's not quite clear to me how this method would scale to studies where there are not tens of thousands of individuals measured. It would be good to already have some general idea of what are the requirements in terms of power (sample size/target effect size / etc) for this approach – either added as a figure panel or two in this paper or just as text if the necessary parameters have already been explained elsewhere. I guess this comes back to the p >> n issue. I see for instance that the authors have 21k transcripts but they narrow it down to 7883 with {greater than or equal to} 3 IVs, used against their sample size of n = 7824 patients. Is this just convenient that n ~= p, or were the required parameters tweaked exactly so that you could reduce the number of transcripts down to more or less the sample size? You have a section on "Power Analysis" already which I appreciate, but reading through it again I can't tell what the minimum N would be. Or can I use an N = 500 I just have to use some other way to select only 500 (or whatever) transcripts? The power calculations go up to N = 90'000 which indeed is "state-of-the-art sample sizes" and would be unattainably large for all but the largest of international human cohorts, and perhaps a few large yeast or cell line studies.

(3) Related, I wasn't quite clear if the data from TwinsUK and KORA were analyzed separately, or if they were somehow merged.

(4) The authors mention "overall, 83% of the involved genes were causally influencing the level of a single metabolite, while TMEM258 and FADS2 affected 12 metabolites". Firstly I would mention that they affect 12 metabolites each just to be clear – although it's clearly annotated in Table S1. Second, and more relevantly, it would be nice to know in this table how many of these hits already are known in the literature. For instance I see the most significant hit is MAF1 with 5-oxoproline which doesn't immediately turn up anything (albeit I did not look very long). Hit #7, for SLC22A4 and isovalerylcarnitine does appear to be known in the literature ( http://www.metabolomix.com/rs272889-slc22a4-octn1-with-acylcarnitines/ ). Doing a decent literature analysis on all 257 of these hits in Table S1 might take a while (and/or require someone who knows how to do automated literature mining, which isn't trivial for this type of task especially given metabolite names like "X-12696") but even just some cherry-picking and/or (better) systematic analysis of the top 20-50 would be nice to see. It greatly improved my confidence in the findings when I just looked into two of your hits just now and found that one of them appears to be reasonably well known by literature.

(5) The authors mention that only 33% of the transcript-metabolite-phenotype triplets were observed by TWMR, but that 91% of those observed by all are in concordant directionality. I guess that means for those with concordant directionality, if no significant association was observed in one layer, there was just no cross-layer comparison? i.e. that the 91% "concordant directionality" are only checking among the 33% of hits by TWMR that were also observed both within and across layer?

(6) The authors mention no availability of trans-eQTL data; is that because the sample size is not sufficient to do a proper trans-eQTL analysis, or is it because of data privacy and an inability to get the precomputed trans-eQTLs from the eQTLGen Consortium due to some potential conflict (GDPR?).

(7) Back to Table S1: There are 257 hits here, with 191 genes (out of 7883) and 154 metabolites (out of 453), meaning that 299 metabolites didn't even have one significant association?

Reviewer #2 (Recommendations for the authors):

1. In general, the methodological approach should be explained in more detail. The study presents a novel MR-based approach and thus, the discussion of the method basics should be elaborated. This pertains to the following points:

– In the definition of causal effects from molecular traits on the outcome (eq. (1)), the symbol β' is not explained. The method used for standardization of effect sizes is not elaborated.

– For the multivariable MR analysis (equation not numbered), no causal effect statistic is specified. As discussed in the public review, no significance testing has been performed, but we strongly urge the authors to do so or give reasons for this lack of testing in the case of causal triplets.

– In the description of the simulation analyses, it should be made more clear how the definition of βGWAS as a function of βmQTL is reached.

– The authors should include a thorough discussion and a description of the method employed to evaluate the comparison between total and direct transcript-phenotype effects in Figure 2B.

2. There is some apparent inconsistency in the interpretation of results from the empirical study: The abstract states that 67 transcript-phenotype effects present within the 206 causal triplets were missed in a TWMR-only analyses, while the paragraph "Power Analysis" states that only 67 triplets showed a significant effect estimated by TWMR. The text relating to Figure 2B states that 79 % (~163) of the triplets were estimated to be due to direct effects by the transcript only. This should be presented in a more consistent and clear manner.

3. Plots for the distribution of the number of IVs per transcript/metabolite should be included (as supplemental figures).

4. It would be interesting to discuss potential modes of mediation between transcripts, metabolites and phenotypes. For example, individual metabolites might integrate the effects of several transcripts. This would not result in triplets, but ultimately, networks of mediation as shown for the TMEM258, FADS1, FADS2 case. How would such cases be treated in a statistically sound manner?
