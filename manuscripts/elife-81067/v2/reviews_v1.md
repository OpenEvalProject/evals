# Peer review - Round 1

Editors:
- Karla L Miller, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81067.sa0](https://doi.org/10.7554/eLife.81067.sa0)

The study has significance for the field of dementia research and neurodegenerative diseases more broadly. Using the brain-age paradigm, the main findings are that having an older-appearing brain is associated with more advanced stages of amyloid and tau pathology, higher white matter hyperintensities, higher plasma NfL and carrying the APOE-e34 allele. Findings were broadly similar in cognitively normal people and people with mild cognitive impairment and there is also some evidence for sex differences.


---

# Peer review - Round 1

Editors:
- Karla L Miller, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81067.sa1](https://doi.org/10.7554/eLife.81067.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Prediction Using Machine Learning on Structural Neuroimaging Data: Multi-Cohort Validation Against Biomarkers of Alzheimer's Disease and Neurodegeneration stratified by sex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jeannie Chin as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Rory Boyle (Reviewer #2); James Cole (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Given the large number of tests conducted, the lack of multiple comparison correction means that some apparently significant associations may be statistically inflated.

2) Claims regarding sex differences should be tempered to be more in line with the strength of evidence.

3) Reviewers noted that brain-age δ was not associated with longitudinal brain change and that the current study is solely a cross-sectional analysis. The implications for this should be discussed – specifically, whether it indicates that brain-age δ does not reflect accelerated brain aging but instead early life factors.

Reviewer #1 (Recommendations for the authors):

– ADNI dataset includes participants with a dementia diagnosis and many of those are in the AD continuum. What was the reason for not including those cases in this study?

– When correcting brain-age estimates for bias, the bias regression line was estimated for each cohort separately. I believe cohort refers to CU vs MCI cases in this context. Is there a rationale for expecting disease stage-dependent bias in brain-age estimates?

– Please clarify the use of the term 'cohort'. does it refer to CU vs MCI diagnostic groups or does it refer to different datasets? if lateral, then I think certain analyses should have been performed by cohort and diagnostic groups since the brain age behavior might be different at different disease stages. for instance, since UKBioBank is all CU participants, it is highly likely that the model performance within ADNI CU and within ADNI MCI cases might be different in terms of R2 and MAE.

– Once the brain-age estimates are corrected for bias based on regression against chronological age, including age as a covariate in linear regression models for each validation variable might lead to double correction for age bias.

– In reference to the paragraph: "We also studied the differences in volumes and cortical thickness between females and males in the UKBioBank for the brain regions that contributed the most to the prediction according to the SHAP values. With this aim we performed regression models for each ROI with sex as a predictor variable, in which linear and quadratic expansions of age, site, and TIV (only included for volume ROIs), were included as covariates.", it is not clear why this regression modeling was necessary if SHAP was used to identify regions contributing the most to brain age prediction. Furthermore, ROI volumes were initially residualized for site and TIV and similarly, thickness values were residualized for site effects. If that's the case, why include site and TIV as a covariate in this analysis? Also, this is the only analysis that higher order age associations were considered. What was the rationale for pursuing non-linear age associations in this case but not in other models?

Reviewer #2 (Recommendations for the authors):

This is very nice work but I think that the findings could be really strengthened by addressing the limitations highlighted in the public review. I can definitely appreciate the impressive amount of work that has already gone into this study and I do not lightly ask for additional work. My concerns would be addressed by correcting your findings for multiple comparisons, re-interpreting your results after correction for multiple comparisons, and discussing the other limitations in-text that can address my concerns.

I have two other main concerns that can be addressed by text edits. First, the novelty of this work is overstated and does not fairly represent the brain-age δ literature. The authors incorrectly state that "there are no comprehensive studies validating this measurement in association with specific biological markers of AD pathology (i.e. Amyloid-B [Ab] and tau pathology), neurodegeneration and cerebrovascular disease. Various studies have reported associations between brain-age δ and biomarkers of amyloid-B, tau, neurodegeneration, and cerebrovascular disease (Cole et al., 2017 Neurobiology of Aging; Huang et al., 2021 Radiology Artificial Intelligence; Millar et al., 2022 bioRxiv; Popescu et al., 2020 Human Brain Mapping; Wagen et al., 2022 Lancet Healthy Longevity). Therefore, this particular emphasis on novelty is not correct and is not representative of the literature. Can the authors please de-emphasize this novelty and acknowledge the good work carried out by other researchers that have addressed some of these questions previously?

Second, "trend" or "trending" is used in the manuscript to refer to findings that are nearly statistically significant. For example, see Lines 333-336, Lines 291-294, and Line 444. However, this is not a meaningful description of a statistical result as we do not know which way these results are 'trending'. It can give the impression that the results are likely significant but did not reach significance for some unstated reason. However, the distance between the sex*plasma interaction in CU (P=.092) than reaching statistical significance (.092 –.05 = .042) is further than the distance of the significant result for APOE-e4 carriers vs APOE-e33 carriers of P = .032 reaching 'non-significance' (.05 –.032 = .018). Likewise for the A+T+*sex interaction (P=.071). In that sense, if you are using language such as the trend to describe findings, you could equally use it to describe findings showing a trend towards non-significance. As such, please avoid using this language and state your results as they are.

References:

Cole et al., 2017 Neurobiology of Aging: https://doi.org/10.1016/j.neurobiolaging.2017.04.006

Huang et al., 2021 Radiology Artificial Intelligence: https://doi.org/10.1148/ryai.2021200171

Millar et al., 2022 bioRxiv: https://doi.org/10.1101/2022.08.25.505251

Popescu et al., 2020 Human Brain Mapping: https://doi.org/10.1002/hbm.25133

Wagen et al., 2022 Lancet Healthy Longevity: https://doi.org/10.1016/S2666-7568(22)00167-2

Sanford et al., 2022, Human Brain Mapping: https://doi.org/10.1002/hbm.25983

Subpramaniapillai et al., 2021 NeuroImage Clinical: https://doi.org/10.1016/j.nicl.2021.102620

Vidal-Pineiro et al. 2021 eLife: https://doi.org/10.7554/eLife.69995

Reviewer #3 (Recommendations for the authors):

– Consider the impact that the number of tests run has on the interpretation.

– It was not entirely clear from the Methods how MCI was defined in each cohort. If these definitions are not consistent between cohorts, this should be highlighted as a limitation.

– It is inappropriate to report accuracy performance metrics after correction for brain-age bias (e.g., Table 3). The point of the correction process is not to improve model performance post hoc, but instead to improve the interpretability of the metrics by removing residual correlation with age. All performance metrics 'after bias correction' should be removed from the manuscript

– Figure 4. It was not obvious what the interactions related to. Of the 9 interactions reported, one is by sex, the other by age. Also, why were the points grouped and coloured by positive versus negative brain-age δ? Generally, this figure could be improved for the sake of clarity.

– Why was the 'aging signature' included? Please provide stronger motivation for why this was relevant.

– The analysis on the top and bottom 10% of participants were not well motivated. Why include this when regression models have already by used that assess 100% of the data, instead of 20%? It was not clear where these results were reported either, so I would recommend omitting this analysis.

– Avoid drawing interpretations that males and females are different in cases where there is no statistical test of this hypothesis. Being non-identical does not necessarily mean that sex differences are statistically significant (e.g., Figure 1d).

– I recommend reporting confidence intervals whenever you report an effect size. This facilitates the comparison of effect sizes between tests.
