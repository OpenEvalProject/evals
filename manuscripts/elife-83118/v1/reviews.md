# Peer review - Round 1

Editors:
- Nicholas E Banovich, https://ror.org/02hfpnk21 Translational Genomics Research Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83118.sa0](https://doi.org/10.7554/eLife.83118.sa0)

This study is of interest to epidemiologists and geneticists studying the association between telomere length and lung cancer risk. This work provides useful insight into risk factors for lung cancer. Overall, the results of this study are solid, as the genetic instrument used here is better powered and the battery of Mendelian randomization analysis makes this broad set of results convincing compared to previous work.


---

# Peer review - Round 1

Editors:
- Nicholas E Banovich, https://ror.org/02hfpnk21 Translational Genomics Research Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83118.sa1](https://doi.org/10.7554/eLife.83118.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Common genetic variations in telomere length genes and lung cancer: a Mendelian Randomization study and its novel application in lung tumor transcriptome" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Ben Voight (Reviewer #2).

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revision:

The reviewers provided a set of critiques that are manageable in scale. Please respond to all of the reviewer comments.

Reviewer #1 (Recommendations for the authors):

Figures are difficult to read as they are poor resolution.

Reviewer #2 (Recommendations for the authors):

1. Resolution is not great on some of the figures – made reading them a little bit hard. I trust the authors will provide higher-resolution versions in the proofing phases!

2. Figure 1B – Not sure what this overall means/how to be interpreted – I think this is too much data plotted on the same figure for my taste.

3. I think the authors should create a supplementary table that enumerates the list of SNPs used for their instrument, along with annotated info about the SNP (pos, alleles, allele frequency), effect estimate, p-value report; then, for each SNP, the relevant outcome data of interest in the paper (effect sizes, se, P-value). That way, it is perfectly clear what SNPs are used and what estimated effects are used as input for MR experiments.

4. I'm a little confused about the colocalization analysis:

a. Suppl. Table 6: it looks to me like there are annotation mislabelling issues.

b. Also it isn't clear in this table which LTL loci have /any/ evidence of lung cancer association, i.e., PP1/2 vs. PP3.

For these, suggest checking the table and adding a column for the top lung cancer association (and SNP) in the interval tested by coloc.

c. But also confusing somewhat that there appear to be multiple TERT signals and those with colocalization but are basically on top of one another whilst still being LD independent (e.g., rs61748181 and rs33977403).

Overall here it looks like there may be some differences between genetic variants selected at this locus compared between Codd et al. and here. It could be these choices make sense and are reasonable, but might be worth looking back at differences to see if different choices drive the results they see.

5. In methods describing the Lung cancer data, are histologic data a complete subset of the overall data? It looks like there are shared controls (? a small limitation if so), but why is the number of controls in two strata greater than the overall? The cases totals are also less than overall, are 'lost' cases here simply because a subtype isn't specified? Perhaps the authors can clarify this a bit in methods.

6. Given the sample size differences, what effect sizes were the authors powered to observe in the Lung Squamous cell carcinoma and Lung Small Cell Carcinoma groups? Should this be interpreted as a false negative due to lack of power OR were the authors reasonably powered to observe (say) the estimated effect size overall in the univariate or epidemiological correlation data (but failed to see that effect), consistent with apparent heterogeneity in these strata?

7. As the author indicates, the MR Egger results (Table S2) suggest substantial 'negative' confounding. This is a little confusing – in my experience, I have seen negative confounding for sure previously, but this is probably some of the stronger effects that I've seen before. I don't have any great advice about how to look at this in detail, other than perhaps through MVMR, or by looking carefully at the IV regression plot to see if there are outliers that are somehow strongly influencing MR-Egger.

8. Inclusion of an epidemiological correlational data baseline between LTL >> lung cancer to compare to the MR estimates would also add value.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Common genetic variations in telomere length genes and lung cancer: a Mendelian Randomization study and its novel application in lung tumour transcriptome" for further consideration by eLife. Your revised article has been evaluated by a Senior Editor and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

New revisions required:

Reviewer #2 (Recommendations for the authors):

The authors have responded to most comments reasonably.

However, I still have some concerns about the given report. I know the collection of these points below are a little extra work -- I am honestly not trying to "add on" but do think these experiments are important to bring out the robustness of the author's claim, add value to the extant literature, and interpretation at these key points around the MR they describe.

1. First, focused around my original comment #2 (in the author's response, their point #6) on multivarible MR experiments. To my point that there are actually multiple potential confounders – including smoking, BMI, and waist-hip ratio that could potentially confound the interpretation that LTL explains the lung-cancer associations, the authors performed one experiment focused on BMI. They note that for each cancer trait there appears to be no impact on their primary association between LTL and Lung cancer data when considering BMI.

However, what they present is still a bit inadequate from my point of view, in the following ways.

1a. The authors perform a form of this MVMR which is a little 'less' good in my view for this -- they build a new instrument based on SNPs ascertained for association with BMI, and then include that in the MVMR regression analysis. This is not how I would do this -- this result describes a "joint" model for the effect of exposures (BMI, LTL) on outcome (Lung cancer). This version does not regress out any potential association of the SNPs *selected for association with LTL* has with the potential confounder. In this case, if the LTL variants had strong association with the confounder (e.g., BMI), I don't think that this would be fully accounted for.

Instead, the authors should take the n=144 SNPs selected for the LTL instrument, identify associations from extant data with the putative confounder of interest (e.g., BMI), create an instrument for the genetically mediated effects of that confounder, and include that as an instrument for covariate confounding.

I.e., "regress out" any effect that the LTL instrument might have on the confounder, and report adjusted effects of the LTL instrument on cancer risk.

Yes: this may NOT be a very strong instrument for the confounder -- but that's not the point here. The point is to determine the effect of genetically mediated LTL on cancer adjusting for any effect that instrument the authors built for it has on the confounder.

1b. Furthermore, considering a single confounder here is really suboptimal. As indicated in the previous comments and as the authors know, smoking behavior and other anthropomorphic measures (e.g., waist-hip ratio) are also correlated with everything here. So the authors should really consider an expanded list of confounders for this to be clearly convincing that LTL really does operate as a causal exposure independently of these other risk factors.

1c. In addition to experiments that are pairwise, they should also consider performing an experiment with all potential confounders included in the model

Cancer ~ LTL + BMI + WHR + SMOKING + …..

I.e., can the authors convincingly demonstrate that the observed relationship between LTL and these lung cancer outcomes is not explained by a battery of obvious confounders individually or as a collective

1d. As suggested earlier – I think value and novelty would be added if the authors really took this on and explored this space a bit more -- look hard and think carefully about what confounders really *COULD* explain this result and work hard to refute that those could explain these observations

I do think a robust set of experiments should be included in the primary report beyond smoking, either way (in the supplement). I think the authors report the BMI result in the rebuttal response to me but don't add those back to the paper. I'd honestly like to see a healthy version of that added to the paper, but that's my taste on this point.

2. On my previous point #4 (in the rebuttal, point #8), I asked the authors to consider a subset MR analysis which focused on those where the genes/signals map quite obviously on known telomere length biology and represent some of the strongest signals. The authors respond that they can't actually do this analysis, suggesting that using the data for co-localization somehow invalidates an MR sub-set analysis.

I thought about this a little bit and while I admit that I can be daft sometimes I honestly do not understand what basis – empirical or theoretical – this argument has to somehow drive positive or negative biases here, i.e., why they need an "out of sample" set to perform the MR after they used this data to perform colocalization. If there's specific literature or reasoning the authors would like to articulate this in more detail, that would certainly be appreciated!

My intuition is that this actually isn't much of an issue -- performing subset analyses for different reasons (biological or otherwise) is actually pretty reasonable and there are MR methods that actually try to cluster / subset instruments used.

This all goes to interpretation and as a sensitivity analysis -- if the result is driven entirely by variation at TERT, TERC, OBFC1 but not obviously by other variation that influences telomere length, then I personally think that is worth trying to understand and report. Analytically, this is a *trivial* experiment to perform in the UVMR space.

3. Regarding the rebuttal point #13, which involved my point about power for discovery in the subset given the sample size, the authors state that there are sample size difference but then write something about confidence intervals overlapping that I don't quite understand.

What I think the authors SHOULD do with respect to the tumor histology analysis is to report a credible set based on power calculation which determine what range of causal effect sizes the Lung Squamous CC and Lung Small CC were powered to discover (at an α type-1 error rate) of 5% and/or 1%, say, given the instruments used and sample sizes involved here.

This is actually a very easy thing to do analytically with some assumptions – back of envelope -- you could check out what formula I pulled together in PMID: 25165093 to get the distribution under the alternative; I believe there are also MR power calculators out there as web tools. You easily do this with some R calculations in a straight forward way.

I think the authors should be able to articulate is that effect sizes (say) of OR=1.6 or better would be discoverable in those lung cell subsets that basically catch the null hypothesis. Or, that those sets were well powered to discover ORs that were even smaller than that. This would then give you a quantitative assessment that this isn't simply a false-negative result, but that there is putative heterogeneity here. But if they are small enough that they AREN'T particularly well powered, then that's a pretty important interpretive point on this plot.
