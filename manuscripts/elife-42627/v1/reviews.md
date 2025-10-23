# Peer review - Round 1

Editors:
- Diego Bassani, SickKids Research Institute Canada

Reviewers:
- Jessica Duby, SickKids Hospital Toronto Canada
- Eric Ohuma, SickKids Hospital Toronto Canada

## Review text

DOI: [10.7554/eLife.42627.013](https://doi.org/10.7554/eLife.42627.013)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Postnatal gestational age estimation using newborn metabolic profiles in Matlab, Bangladesh" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Prabhat Jha as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jessica Duby (Reviewer #1); Eric Ohuma (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript by Murphy et al., the authors study the accuracy of a metabolic based model to determine gestational age for neonates in Bangladesh when compared to a first trimester ultrasound. The authors make a strong case for the potential impact of a successful algorithm in determining population rates of preterm birth and small-for-gestational age in low-resource settings. This is a potentially important study but the description of the study design and execution is far from complete.

In addition, whilst there is no doubt an accurate estimate of GA is important, there are fundamental problems with this approach that is based on postnatal estimation of GA. First, it helps to perpetuate a standard of care that even WHO has abandoned, namely managing pregnancies without knowing the due date. This is the reason the new WHO guidelines recommend at least one ultrasound scan, in part to estimate gestational age prenatally.

In addition, the authors do not properly address the model's ability to distinguish small-for-gestational age (SGA) neonates, which should be one of the model's primary advantages over using birth weight alone as a surrogate marker for gestational age.

Essential revisions:

1) There are deviations from the cited, published protocol that remain unexplained by the authors. (Murphy et al., 2017)

Major differences between published protocol and current manuscript:

a) Sample size: The protocol's sample size requirements are calculated to be 3,500 participants. The current manuscript details 1523 samples from 1069 newborns with no discussion regarding the achieved sample size. As part of addressing sample size differences, it may benefit the authors to present a figure detailing number of eligible participants, number approached for consent, number consented, etc.

b) Models: The proposed models to test in the protocol are quite different than the models tested in the current manuscript and no justification is provided. For reference, the models listed in the protocol are: "1) birth weight alone; 2) combination of birth weight and fetal/adult haemoglobin levels; 3) combination of birth weight, haemoglobin levels, thyroid-stimulating hormone and 17-OHP (all non-mass-spectrometry-derived analytes); and 4) birth weight and the full panel of newborn screening analytes. Sex and multiple birth (yes, no) will be included in all models." (Murphy et al., 2017) For models used in the reported study, refer to the subsection “Validation of algorithms”.

2) SGA/large-for-gestational age (LGA) babies: The authors need to provide further analysis and discussion regarding the algorithm's performance in SGA/LGA identification. Specifically, the authors need to identify how many SGA/LGA neonates were in their sample and the models' accuracy for these important sub-groups. The authors had listed this analysis in their protocol and have previously performed similar sub-group analysis on the original Ontario cohort which can be used as a guide. (Wilson et al., 2016).

3) While the authors do sub-group analyses by birth weight (<2500g and ≥2500g) in Table 2, weight alone is unimportant when we consider the overarching goal of finding a model that can distinguish preterm birth from SGA and post-term birth from LGA. I would recommend replacing the columns under each of the sample types in Table 2 to be:

1) Overall;

2) SGA;

3) Appropriate-for-gestational age (AGA); and

4) LGA.

4) Imputation of missing values: As only 46 (11%) of observations were imputed, did the authors do a sensitivity analysis of the performance of the model with and without the imputed missing values to evaluate their influence on the results?

5) Prediction score (nomogram) – it would be useful for the authors to also show the relative contribution of each factor in their model. For example, in the baseline model with birthweight, infant sex and multiple births, what is the greatest predictor of GA? A quantification of the relative contribution of each of the factors is useful in understanding their contribution and justification as important variables the prediction of GA. Similarly, this should be done for models 2 and 3 as it allows one to make judgements on how much more improvements in prediction is provided for by including the clinical and analyte data. Also, a comparison of scores helps to discern whether some factors included in the model are correlated and thus are similar in their prediction of GA.

6) Would also be helpful for the author to show a plot of true GA vs. predicted GA (calibration) as this will evidently show the variability of the prediction as a function of GA as opposed to the aggregated estimates they have presented by GA in Figure 1.

7) The cohort was apparently nested within a PreSSMat study in Matlab but the authors do not provide key information on timing of ultrasound examination, birth examinations and weight and criteria used to categorize infants as either preterm, small for gestational age (SGA) or combinations thereof. Please add the necessary level of detail to the methodology and Results sections.

8) Given the issues with cord blood specificity and the wide range of times in collection of heel prick samples (from a few hours to up to 40 hours), one is left guessing as to the fidelity of design of the gold standard used in this study and early measures. Please explain when were these measurements obtained?

9) Please explain what standards were used for ultrasound based gestational age and add an appropriate justification for adoption of the chosen standards.

10) The overall rates of prematurity in the cohort determined from the study (both cord and heel prick samples) are implausibly low (given what is known from ANISA and AMANHI studies done in Bangladesh). Please explain the reasons for these differences.

11) The authors should comment on what is known about prematurity incidence from prior studies of maternal antenatal care and nutrition supplementation done in Bangladesh on large rural cohorts including Matlab, without that information, it is difficult to place this study in the context of what else is known.
