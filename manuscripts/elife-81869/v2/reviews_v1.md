# Peer review - Round 1

Editors:
- Karla L Miller, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81869.sa0](https://doi.org/10.7554/eLife.81869.sa0)

This is a useful study exploring multi-modality brain age (structural plus resting state MRI) in people in the early stages or at risk of Alzheimer's disease. They found solid evidence that people with cognitive impairment had older-appearing brains and that older-appearing brains were related to Alzheimer's risk factors such as amyloid and tau deposition. Their data suggest that the multi-modality brain age model is more accurate than a unimodal structural MRI model.


---

# Peer review - Round 1

Editors:
- Karla L Miller, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81869.sa1](https://doi.org/10.7554/eLife.81869.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Multimodal brain age estimates relate to Alzheimer disease biomarkers and cognition in early stages: a cross-sectional observational study" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jeannie Chin as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: James Cole (Reviewer #1); Didac Vidal-Pineiro (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The overall consensus from the reviewers is that some of the hypotheses (and conclusions) are supported by the results (specifically, the Vol-BAG model) while others are much weaker (specifically, the FC-BAG models). In consultation between the reviewers, they agreed that the work is "useful" but found the evidence to be "incomplete" for the conclusions as presented.

1. The functional connectivity model provides a poor fit to the data. Given that the FC-based models have been recently published (Millar 2022), the reviewers feel that the authors should temper claims about the importance of the FC-based modelling.

2. The reviewers are skeptical about claims regarding the improvements afforded by multi-modal brain age models. In particular, the bootstrapping analyses actually support the claims that FC data improve the quality of brain age modelling.

3. Overall, the reviewers feel that some of the conclusions, such as the biphasic relationships between functional brain-age models and pathological status, are not strongly supported and need to be tempered. In particular, the reviewers object to referring to results as "marginal".

4. Discussion about the potential implications of sample size would be welcome.

Reviewer #1 (Recommendations for the authors):

– In the Methods, they say they used a Gaussian mixture model to define pTau positivity. There are multiple ways to implement GMMs, so more details should be included here.

– The presentation of the MRI Acquisition section in the Methods is not very clear. I suggest the authors consider an alternative format, possibly a supplementary table, where the acquisition details can be more easily appraised. Currently, the acquisition details on the DIAN participants are scarce relative to the ADRC participants.

– Can the authors explain and justify why the fMRI processing included registration to an older-adult template? Could this have caused a bias in the registration accuracy for younger participants?

– It is unclear to me why they chose to perform 10-fold CV and hold-out validation with 1000 bootstraps. To my mind, the latter would have been sufficient. If the authors think including the initial 10-fold CV as well is important, this should be clearly justified.

– It is important that R2 is reported for each model performance, not just MAE. As R2 is a ratio the values can readily be compared across published studies, while the MAE cannot as it is heavily dependent on the age distribution of the test set. For completeness, they could also consider reporting the Pearson's r correlation between predicted age and age, and the root mean square error as well.

– It is unclear how the model performance comparisons were conducted (Results, pg. 12). While t-tests are mentioned in the text, the exact details should be included in the Methods. My concern here is that the n (sample size) for these comparisons is based on the number of bootstraps (arbitrarily determined by the authors to be 1000), rather than the actual sample size. If that is the case (and Figure 1D suggests it is), this is procedure is incorrect as the sensitivity that these tests have to detect differences would be purely a factor of the number of bootstraps, rather than the number of observations. This means that the experimenter can simply choose to make smaller differences 'significant' simply by adding more bootstraps. This needs to be clarified and corrected if appropriate. One approach to achieve the goal of comparing model performances is to take Pearson's correlations with age from each model and use Z-transformations to test the alternative hypothesis that the correlations are different (e.g., the Steiger test). In that way, the n would be determined by the number of observations, so statistical power would appropriately reflect the data.

– I recommend avoiding saying things like 'marginally lower' when a p-value = 0.110. There's no real evidence that there's a difference here, so hard to say whether it's truly lower or not. Generally avoiding 'trends' at 0.1> p >0.05 is best practice. P-values are important, but effect sizes (with confidence intervals) are often more informative.

– In the Discussion, when comparing age prediction accuracy between studies, it's important not to rely on MAE alone as this can vary greatly as a function of the test set age distribution. They should use R2 instead. Where R2 is unavailable, it's essential that the age range of each study mentioned in comparison is reported to provide context to the MAE values.

– The evidence for a biphasic relationship between FC-BAG and pre-clinical/clinical status is somewhat over-interpreted, particularly given there was no difference between A+T- and A+T+ people (p=0.11) and the fit of FC brain age is quite poor (i.e., far from the line of identity in Figure 2A). I suggest more caution when discussing this.

– A key limitation that was not mentioned was the small sample size relative to other studies. Perhaps the model performance is similar but given that only MAE is used to compare studies it is hard to draw meaningful conclusions. My impression is that had larger datasets been available, then performance would have improved.

Reviewer #2 (Recommendations for the authors):

– As explained in the previous section, the FC-BAG model has very limited prediction power, and therefore the results from the FC-BAG model are not reliable while providing marginal benefit. The FC-BAG results should be moved to the supplementary materials.

– For the FC-BAG models and its relation to other clinical variables, please also another version of the model including mean, median, and maximum head motion during the entire rsfMRI scan as covariates in the model to further ensure the reliability of the results.

– It is not clear to me that the bootstrapped based t-test provides evidence in favor of the Vol+FC-BAG model. In other words, a stacked model combining FC-BAG and Vol-BAG will always perform as well or worse than each model. If the stacking approach takes this into account (not clear in the method section, needs further explanation) the marginal increase in performance can be explained to this unidirectional effect and needs further confirmation based on a model selection step (e.g. using new independent data not used in the training-validation of FC-BAG and Vol-BAG model to compare Vol+FC-BAG and Vol-BAG model).

– After the previous step authors can choose the best performing model (either Vol-BAG or Vol+FC-BAG model) and only present the data for the selected model since results between the two models are redundant and don't add extra information to the reader.

– The analysis of hippocampal volume (specially related to the preclinical AD) needs to be confirmed. To do so, hippocampal volume as well as volumetric features from regions highly correlated with hippocampal volume should be removed from the feature set of Vol-BAG and Vol+FC-BAG models. The models need to be retrained using the same procedure. The relationship between hippocampal volume and the newly calculated Vol-BAG and Vol+FC-BAG values should be reported alongside the current results.

Reviewer #3 (Recommendations for the authors):

Find below some recommendations on how (I think) the science in this manuscript might be improved in no particular order.

1. Training sample. It is unclear why one would like to minimize undetected AD pathology (amyloid positivity, that is) in the cognitively healthy training sample as many of these individuals (when Tau negative) have minimal changes in brain structure and function. Since you create a BA "norm" from these individuals, one may benefit from including a bigger, more representative sample using more lenient inclusion criteria. Decisions regarding the training sample can have a big impact on the subsequent interpretation of BA results (e.g. Hwang, 2022, Brain Comm).

2. Group descriptors. It is still a matter of ongoing debate, but I recommend using another descriptor for the amyloid positive group rather than "preclinical AD". Even in the NIAA-AA Research framework from 2018 (Jack Jr.) they only use this tag for individuals that are amyloid and tau positive.

3. Biomarker definition. I am not an expert on biomarkers, but the definition of pTau positivity is uncommon to me "Gaussian mixture model approach to defining pTau positivity based on the CSF pTau/Aβ40 ratio.". Could the authors justify and or cite the correspondent references?

4. Statistical analysis. If I have not misread, the methods section only mentions three test groups (A-, A+, and CDR>0) but the analysis is performed with four groups. This leads to confusion and should be corrected. Also, most higher-level analyses reported in the results are not described in this section. These analyses should be described in the methods section. It is difficult to evaluate whether the performed analyses are appropriate without this description. For example, (lines 323-7) the authors report three different regression models and then a fourth analysis combining the four groups, but only for FC-BAG. This procedure is unclear, not described (as far as I can see), and not justified. Another example is the analysis with NFL which is not mentioned until line 412 (p.20) in the Results section. Also, the authors use different samples for different tests, due to the lack of Biomarker information for some individuals. I suggest adding degrees of freedom/n when reporting the results, so the reader has some information regarding the sample used.

5. The authors are repeating the same analysis in three different modalities (also sometimes they repeat the analyses across several pairs of groups [e.g. lines 323-7]). Thus, I would strongly recommend using some type of multiple comparison corrections.

6. Table 2. The authors should mention what the units in the table represent. Also, I recommend adding df and exact significance values (at least if p >.001).

7. Atlas. The authors used the D-K atlas (not strictly the FS-defined) for BA computation. This is a suboptimal choice, and I would recommend in the future using more fine-grained parcellations. This is not a strong issue, but the choice surprised me since the authors used a 300-ROI parcellation for the rs-fMRI. Also, since the authors use cortical thickness for sampling the cortex, I would not use "Volumetric"-BA as a descriptor.

8. Movement and rs-fMRI. The rs-fMRI preprocessing used might still lead to a signal that is related to movement. Since movement is almost always related to age and disease [and thus can affect both the BA computation and the tests in the test sample], I would suggest taking additional steps in this regard. At the minimum, I would include total motion as an additional covariate in the higher-level analysis and discuss this issue in the limitations section.

9. The results in cognitively healthy samples are largely negative (i.e. do not differ with groups). One possible explanation is that the authors are using cross-sectional samples and thus – even when using BA metrics – have a signal that captures ongoing aging (accelerated aging, if you wish) and baseline (lifelong, preexisting) variability between individuals. The latter may obscure possible existing effects. I recommend the authors acknowledge the limitations of using cross-sectional data to study changes that ought to be longitudinal.
