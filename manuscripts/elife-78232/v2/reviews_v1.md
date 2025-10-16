# Peer review - Round 1

Editors:
- Karla L Miller, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78232.sa0](https://doi.org/10.7554/eLife.78232.sa0)

This manuscript considers whether genetic information can improve the clinical utility of population norms derived from brain imaging data. The authors propose to incorporate polygenic scores into normative models of hippocampal volume to improve predictions of neurodegenerative disease. This approach is elegantly demonstrated in this manuscript and may be useful for clinical translation of population neuroimaging.


---

# Peer review - Round 1

Editors:
- Karla L Miller, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78232.sa1](https://doi.org/10.7554/eLife.78232.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Nomograms of Human Hippocampal Volume Shifted by Polygenic Scores" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jeannie Chin as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Andre F Marquand (Reviewer #1); Richard AI Bethlehem (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The authors argue that the use of Gaussian processes enables predictions outside the age range that the model is trained on. This would enable a model trained on UK Biobank to be applied to the ADNI dataset. The reviewers express scepticism about this claim and request further evidence for its validity.

2. The reviewers note the need for a more rigorous quantification and/or detailed presentation of the amount of improvement provided by the genetically informed models, and of the quality of fit.

3. Please provide a more in-depth consideration of potential sources of confounds, particularly site effects for the ADNI data.

4. It would appear that the UK Biobank and ADNI datasets deviate in several key properties relevant to the modelling. Some investigation into the implications of this would considerably strengthen the paper.

5. All reviewers request more in-depth consideration of the details of modelling including:

5a. How to deal with non-Gaussianities in the data;

5b. How the models are trained in practice (e.g., test/train split, initialisation);

5c. Effect of selection of subjects with high vs low polygenic score, and the application.

Reviewer #2 (Recommendations for the authors):

This is a very interesting and well-written paper and I only have some small suggestions and comments related to mainly the methods and results.

As noted in the public review I think the section on GPR methodology could do with a lot more detail. Such as but not limited to discussion of:

– What does the test train split look like;

– Does the initiation of GPR at the mean pose an issue for data that may not be normally distributed at a given age (I assume not since these are Gaussian processes)?

– Would there be an issue if the variability of a given phenotype (HV in this case) varies across the lifespan? In our own recent work, we observed that certainly for many cortical phenotypes there is an enormous change in variability across the lifespan and so would not expect to see nice parallel quantiles/centile lines such as the ones produced by GPR.

I wasn't sure why the sliding window approach could not be closer to the actual range of the data with perhaps some kind of padding approach that for example, LOESS allows you to use. So I think it is a bit of an oversell of GPR to say it extends the age range as it doesn't extend it really beyond the data that is actually available. I don't think this paper needs to emphasize that as an improvement or to make that contrast so explicit.

The results themselves could perhaps be further strengthened with a visualisation of centile/quantile distributions in the ADNI dataset as they are discussed quite a lot in the results and since these are all effectively age-normalised scores can easily be put into a box/violin/raincloud plot. I think that would also satisfy my curiosity about the skewness of some of the results as it is noted that in the original model AD patient has a mean quantile of 4% with an SD of 10%, so this must be a highly skewed distribution? If so, then maybe it's more appropriate to report the medians of each group.

Finally, it was interesting to see that the CN group in the ADNI dataset had a mean quantile around 41% which to me would suggest that this dataset as a whole is somewhat offset from the UK BioBank sample as a perfectly "normal" other group should hover around the 50% by definition. While the PGS weighting seems to normalise this somewhat it did make we wonder whether there should be some kind of a prior normalisation or general study weighting to apply a UKB-derived model to a new dataset? On a related note: how did the authors deal with the enormous site-level variation within ADNI?

Reviewer #3 (Recommendations for the authors):

1) As already mentioned in my public review, my main concern is the applicability of the model to the ADNI dataset. The model can clearly not be extended outside of the age range when considering younger ages. I must admit that for the ADNI cohort / older ages the model seems more reliable based on what we know from the literature but that is not sufficient. I am not sure how to solve this problem, other than adding the CN subjects from ADNI to the creation of the nomograms, although that could lead to a whole range of other harmonisation problems. Another option would be to limit the analysis to include only those subjects that are within the age range.

2) Is it possible to quantify the improvement when adding the genetic information to the nomograms? See also point 6) below.

3) Line 152: "… and scan date were regressed out of the TVs" How? Is it reasonable to assume that the scanner drift is linear (the Github scripts seem to suggest this is what was modelled) but this also suggests e.g. no scanner updates, hardware changes, and so on? Was there also a correction for the different scanners that may have been used (as far as I am aware, UKB has several imaging sites).

4) Line 220: What is the rationale for splitting high-versus low PGS at 30%? What happens at the other thresholds? Why is there a different choice for ADNI?

5) Line 239: The dropout number for HV in ADNI is pretty large and probably non-random. Please comment.

6) What is the meaning of {plus minus}30% in statements like "cognitively normal (CN) participants (n = 225) had a mean bilateral HV percentile of 41% ({plus minus}30%)"? Is it standard deviation/standard error? These errors seem rather large, so that leads me to believe that the e.g. 4% drop could be too small to be meaningful.

7) Discussion, first paragraph: "Therefore, accounting for … " This statement seems to contradict the results. Maybe this discussion is better placed elsewhere.

8) Discussion, second paragraph / Figure 3 / Supplementary FiguresS1/S2 / Supplementary Table S1.

The (supplementary) Figures are very misleading if you compare these with supplementary Table 1: from Table 1 I conclude that every threshold predicts HV about equally well, but the figure suggests otherwise if you do not pay attention to the cut-off in the y-axis. The paragraph in the discussion that describes the so-called bimodal distribution supports this (false) idea and should be removed.

9) Discussion, Line 423: "Therefore, other brain regions with higher heritability like the cerebellum or whole brain volume may show more sensitivity on nomograms." I am somewhat confused about this sentence. Do the authors mean to imply that structures with higher heritability might benefit more from stratifying on PGS? This would only be the case if not only heritability but also SNP heritability should be higher (and the latter also depends on the genetic architecture and discovery sample size).

10) Discussion, final sentence, the brain age gap has not been mentioned in the paper up to this point. While potentially relevant, it is strange to introduce it in the final sentence.

11) Ethics: I would have expected some statements about the use of human data from UKB and ADNI in this paragraph.

12) Supplementary Figure S5: there are people that seem to switch diagnosis from AD back to MCI, this cannot be right?

13) Throughout the paper there are statements like "Importantly, this magnitude corresponds to ~3 years' worth of HV loss during normal aging." This suggests a constant loss over the lifespan (i.e. a linear pattern with age, but the data shows a different pattern. Please rephrase.

14) The (Supplementary) Figures could use a little bit more attention:

- A little bit more information on what is shown in the figures is needed to be able to assess what is displayed; e.g. add abbreviations to the captions, there are no units for some of the axes. None of the nomogram figures have labels for percentile lines, which is essential. Figure S1&S2 please explain the percentile figures.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Nomograms of Human Hippocampal Volume Shifted by Polygenic Scores" for further consideration by eLife. Your revised article has been evaluated by Jeannie Chin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. Regarding tests for Gaussianity in the UKB samples. We recommend in Figure 4 —figure supplement 3 that the interpretation of the Shapiro-Wilks test is clarified. That is, state explicitly that a given distribution is designated as non-Gaussian if the SW test yields p below some threshold. Also, we believe it is the "Shapiro-Wilk" or "Shapiro-Wilks" test, not "Shapiro-Wilkens".

2. Throughout, the authors use the term "PGS score" which would be written in full as "polygenic score score". We appreciate the awkwardness that sometimes comes with acronyms, but suggest sticking to either "PGSs" or "PG scores".

3. It might be worthwhile adding some discussion regarding Reviewer 1's comments about the potential benefits of directly incorporating PGSs in normative modelling, alongside the challenges that the authors raise in their response letter.

4. It might help readers less familiar with sliding window techniques to be even more explicit about the reason why smoothing restricts the age range. The authors state this but do not note that this is due to "edge effects", in which smoothed sliding window curves become highly sensitive to noisy data at the limits of data ranges.

5. The new results in Figure 5 might be better visualised as violin or raincloud plots. However, we do appreciate that Reviewer 2, who requested this information, did also suggest that boxplots would suffice.

6. Please consider dampening the conclusions ever so slightly. NeuroCombat generally does an excellent job at removing some site related variation, but does not remove the tenacious issue of site effect altogether.
