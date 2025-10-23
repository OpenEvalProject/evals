# Peer review - Round 1

Editors:
- Alex Fornito, Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58116.sa1](https://doi.org/10.7554/eLife.58116.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper uses brain imaging in neonates to show that brain structure at birth can predict behaviour up to 2 years later. This work provides an important link between brain health at birth and later cognitive development.

Decision letter after peer review:

Thank you for submitting your article "Diffusion-MRI-based regional cortical microstructure at birth for predicting neurodevelopmental outcomes of 2-year-olds" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Richard Ivry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary

This manuscript focuses on trying to predict cognitive assessment scores, collected at 18 months of age, from neonatal cortical structure. In 46 neonates, they use support vector regression with leave-one-out cross-validation to model the multivariate relationship between cortical microstructure and later scores. The authors are able to calculate predicted individual cognitive and language scores that correlate with actual scores.

All reviewers appreciate the challenge in collecting these kinds of data and the cross-validation procedure used for outcome prediction. However, we shared a series of concerns that must be addressed before we can consider publication.

Essential revisions

– We are concerned about the representativeness and size of the sample, and therefore how generalisable these results might be to the larger neonatal population. The infants are both born and scanned across a very wide age range, 32-42 postnatal weeks. This means that some of the infants were both very preterm at birth and at scan, with very different cortical microstructure (seen in the supplementary figures). There is also very different partial voluming in these two ages simply due to brain volume differences. Moreover, the study population is not described very well. We cannot discern what the relative proportions of preterm and term infants are. The authors only report that the gestational age ranged from 26 to 41 weeks and that images were obtained at postmenstrual ages ranging from 31 to 41 weeks. More detail is needed regarding the study population and who was imaged when. In addition, more than half of the recruited infants didn't finish the study, and it is important to know if there were differences between those subjects who were apparently lost to follow up and those that weren't.

– The mixing of term and preterm groups in the analysis raises an interpretation issue. These two populations aren't equivalent, and few would argue that preterm infants are "normal" despite having normal conventional neuroimaging studies. It is conceivable that the findings of the study are driven by abnormalities in the preterm infants, and are thereby an indication of areas which are most commonly injured in preterm infants. We suggest the authors consider i) comparing findings of preterm with term infants and ii) evaluating outcome correlations for these populations separately. An alternative would be to examine term-equivalent scans for all participants.

– Please clarify the extent to which the correlations between real and predicted scores driven by extreme scorers.

– The authors have demonstrated the quite dramatic changes that occur over this period (Ouyang et al., 2019). It's difficult to see how you could combine datasets that have the transient anisotropic features in cortex (early) and more isotropic mature features (late) without testing on a hold out. Linear age adjustment doesn't really help in this context as the changes are nonlinear. As an example, the positive and negative scores at both ends of the tails of the Bailey-III cognitive scores are preterm and term born infants respectively which again makes me worry about the confound of age in the results of the regression.

– The average assessment score is nearly a full standard deviation below what you'd expect in a typical population at the same age, averaging 85-90 in the three subscales. Is there a reason the average is so low?

– The predicted scores are also in a very restricted range – although the raw scores range from 65-110 (cognitive) and 55-110 (language) the predictions seem to only range from 80-90. As you move away from the mean, the absolute error increases substantially.

– More generally, the analysis provides a useful proof-of-principle that early FA measures can predict later outcomes, but the predictions are not sufficiently accurate for clinical use. The MAE for the models is around 1 SD of the cognitive scores, and the accuracy using performance cut-offs was 61%/76%. Although sensitivity/specificity are not reported, FA does not seem to be a highly sensitive marker of these outcomes (as suggested in text). This approach may work at a population level but is not particularly effective for meaningfully predicting the outcome for a single individual. A more measured tone in describing the findings and their limitations would provide a more balanced account of the findings.

– With samples sizes this small there is substantial risk of overestimation of the accuracy of any machine learning techniques. The sample size is small, but 5-fold or 10-fold CV is possible here – see Poldrack et al. 10.1001/jamapsychiatry.2019.3671

– White matter FA showed a similar prediction accuracy to cortical FA. This raises questions about specificity. Could simpler measures (e.g., T1 or T2 signal) provide comparable prediction? If so, this may challenge the biological interpretation that the prediction derives from FA's capacity to measure cortical microstructure. Perhaps the authors could further examine this issue by comparing the relative prediction efficacy of simpler and FA-derived measures and looking at how strongly cortical and white matter measures correlate with each other. Is there anything to be gained by combining them?

– Please clarify how motion corruption of the DWI data was assessed and determined?

– Please explain reasons for participant dropout over the 2 year follow-up.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Diffusion-MRI-based regional cortical microstructure at birth for predicting neurodevelopmental outcomes of 2-year-olds" for further consideration by eLife. Your revised article has been evaluated by Richard Ivry (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below. We emphasise that these issues must be addressed to the satisfaction of the reviewers before the manuscript can be accepted.

The first major concern is that the motion threshold is very large (>3 times voxel dimensions) and the replacement scan seems to be taken from a different session. The eddy correction approach is also out of date and seems to just be an affine registration (no outlier rejection like in tortoise, eddy, shard). The authors need to comprehensively demonstrate that the results are not driven by motion-related artefact.

Second, it may not be appropriate to classify prematurely-born infants as "normal." Although the MRI may appear normal at early neurodevelopmental follow up, many cognitive issues aren't detectable until these children reach school age. This should be identified as a weakness in the Discussion.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for sending your article entitled "Diffusion-MRI-based regional cortical microstructure at birth for predicting neurodevelopmental outcomes of 2-year-olds" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Richard Ivry as the Senior Editor.

The reviewers feel that the issue of head motion has not been fully addressed. The reviewers requested that you comprehensively show that motion cannot explain the findings. Showing the distribution of motion estimates in the sample is not sufficient. For publication, we would require a stronger demonstration that motion does not contaminate or confound the predictions by, for example, examining correlations between motion estimates (e.g., framewise displacement) and the outcome/connectivity measures used in the analysis.
