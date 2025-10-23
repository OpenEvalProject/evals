# Peer review - Round 1

Editors:
- Alexander Shackman, University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54055.sa1](https://doi.org/10.7554/eLife.54055.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors describe a novel machine learning approach-opportunistic prediction stacking-with the aim of combining multiple neuroimaging modalities into a single predictive model (“biomarker”) in the face of missing data. Leveraging structural MRI, functional MRI, and MEG data from a large public biobank (Cam-Can), the authors show that each modality had additive incremental value in predicting age.

The reviewers and I were enthusiastic about the report. This approach has the potential to extract valuable information from multimodal databases and improve diagnostic power based on the surrogate biomarker idea. From a translational neuroscience perspective, the paper addresses (1) whether adding MEG improves age prediction and provides incremental predictive validity over sMRI or sMRI + fMRI alone; (2) which MEG features are most predictive of age. From a methodological perspective, the paper extends the original stacking method to address missing data, a common occurrence.

Decision letter after peer review:

Thank you for submitting your article "Combining electrophysiology with MRI enhances learning of surrogate-biomarkers" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Alex Shackman as the Reviewing Editor and Floris de Lange as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kamen Tsvetanov (Reviewer #1); Nelson Trujillo-Barreto (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors describe a novel machine learning approach-opportunistic prediction stacking-with the aim of combining multiple neuroimaging modalities into a single predictive model (“biomarker”) in the face of missing data. Leveraging structural MRI, functional MRI, and MEG data from a large public biobank (Cam-Can), the authors show that each modality had additive incremental value in predicting age.

The reviewers and I were enthusiastic about the report:

• The paper is written and presented well.

• The research idea is interesting and timely and the proposed method has the potential to extract valuable information from multimodal databases and improve diagnostic power based on the surrogate biomarker idea.

• From a translational neuroscience perspective, the paper addresses (1) whether adding MEG improves age prediction and provides incremental predictive validity over sMRI or sMRI + fMRI alone; (2) which MEG features are most predictive of age.

• From a methodological perspective, the paper extends the original stacking method to address missing data, a common occurrence.

Challenges and Recommendations:

Nevertheless, our enthusiasm was somewhat tempered by several key limitations of the report. In this section, I briefly summarize the most important comments.

1) Challenge: – The motivation for including MEG seems to be exclusively based on EEG evidence. In the Introduction, all the evidence about the relationship between electrophysiology and ageing (and the complementarity to fMRI in that context) to motivate its inclusion as an additional modality is drawn from the EEG literature, which is odd, given that the paper uses MEG instead.

Recommendation: – The authors should motivate the use of MEG directly or at least link the evidence from EEG to the use of MEG in a more convincing way. This might be as simple as saying that, although a lot of evidence from EEG is available, there is no available EEG data in multimodal databases (which I think would be a fair statement in general), but given the relationship between the two techniques, it is expected that inclusion of MEG would be valuable as well, this link is not clear in the text.

2) Challenge: – The Materials and methods are not entirely clear. Some of the processing/feature extraction steps are not completely explained or appropriately justified. The taxonomy used for the extracted features in MEG is confusing.

Recommendation: – Clarify the Materials and methods.

3) Challenge: – Missing Statistics. – Statistical significance of some of the results are missing: Many of the results do not report any statistical significance threshold (or p-value), which makes claims about results being above chance, not rigorously justified. (e.g. "…All stacking models performed consistently better than chance…" What does it mean to perform better than chance here? Was a statistical significance test carried out? What was the null hypothesis tested? If so, report the p-value or equivalent used? In some cases, statistical significance is obvious, in others, it is difficult to assess via visual inspection.

Recommendation: – Report statistical significance of any comparisons made (either corrected or not) in the main report and in the supplement e.g. for MAE differences and MAE PE correlations.

4) Challenge: – Generality. – It is important to demonstrate the robustness and reliability of these features to generalize in unseen data.

Recommendation: – The authors could readily address this in the available data by splitting the sample in half (while maintaining the age distribution and data missingness) and test how similar are the loadings of each feature across data splits. The process could be repeated multiple times (1000s) to create a distribution, which can be compared to the distribution from a permuted data.

5) Challenge: – Non-random Missing Data. – It is important to show that the approach is not susceptible to confounds in the missing data (non-random missingness; e.g. more missing data coming from older individuals, which “helps” to learn an age-related effects).

Recommendation: – This could be easily addressed e.g. by comparing model performance between two scenarios of missingness in the fully available dataset. In one scenario the missing data come from subjects with uniform age distribution and in the other scenario a bias in age selection is introduced, i.e. larger portion of missing data comes from older individuals.

6) Challenge: – Need to better integrate or segregate the main report and the supplement. Extensive text is dedicated to supplementary figures (e.g. Figure 2 and Figure 4 figure supplements).

Recommendation: – If the supplementary material so important for reaching the conclusions of the paper, perhaps it would be more helpful to include them in the body of the paper. Otherwise I would suggest the authors to move the relevant explanations to the supplements.

7) Challenge: – The authors demonstrate that their approach can identify variability in the detected signals with behavioral relevance. The authors investigated this question by testing relations between brain age residuals and cognitive measures orthogonalized wrt chronological age. It is interesting why the authors have adopted this modular process, which has faced some criticism, as opposed to a single level model that can flexibly accommodate all variables in a single model (Lindquist, Geuter, Wager and Caffo, 2019).

Recommendation: – Authors should at least address this choice in the paper. (Lindquist, et al., 2019)

8) Challenge: – The authors do not seem to have considered the inclusion of variables of not interest which may lead to spurious correlations.

Recommendation: – Variables such as gender, handedness, head motion, total grey matter and total intracranial volume should be controlled for to ensure the specificity of the findings. One way to address both points would be to evaluate a model with multiple predictors including age, cognitive variable (e.g. Cattell) and covariates of not interest, where the dependent variable is brain age. Then the statistics on the cognitive variable of interest, which would indicate unique contribution to predict brain age over and above chronological age and covariates (i.e. individual variability), can be reported in the format of Figure 3.

9) Challenge: – The previous comment raised the concern about covariates of no interest and their consideration in the post hoc analysis.

Recommendation: – It would be really worthwhile having the authors' view whether the approach can/should include covariates of no interest in Layer I. This could be particularly relevant if each modality is associated with "unique" covariates of no interest (e.g. head motion in fMRI, or empty room recording SNR in MEG). Though, I assume that the combination of multiple datasets will reduce this bias, which brings me to my next point.

10) Recommendation: – It would be a really worthwhile the authors could consider reporting what part of the data in Level I contributed to the overall model performance, i.e. what is the topography in each modality that matters (e.g. atrophy in frontal regions, connectivity in DMN etc.)?

11) Challenge: – Some of the results or explanations for the results in the Discussion are not intuitive or perhaps adequately explained in the context of the existent literature and the design of the analysis.

Recommendation: – Revise the Discussion to address this concern.

12) Challenge: – Limitations – Limitations of the methodology (i.e. its assumptions) or the choice of the features (i.e. static vs dynamic) are not adequately put in context or discussed.

Recommendation: – Authors need to, at least briefly, discuss about how potential assumption violations might affect the results.
