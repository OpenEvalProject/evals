# Peer review - Round 1

Editors:
- Gian Paolo Rossi, University of Padua Padua Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72930.sa0](https://doi.org/10.7554/eLife.72930.sa0)

Salt intake is a major determinant of volume status, blood pressure values, and congestion, but its estimation is challenging because of the need of measuring 24-h urinary sodium excretion over a number of days, which is unfeasible in most countries. The demonstration of the feasibility of estimating accurately salt intake at the population level using artificial intelligence starting from simple and widely available variable is therefore important for epidemiological and intervention studies in which salt intake is a major player, particularly, but not only, in countries experiencing economic hardships.


---

# Peer review - Round 1

Editors:
- Gian Paolo Rossi, University of Padua Padua Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72930.sa1](https://doi.org/10.7554/eLife.72930.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Estimating salt consumption in 49 low-and middle-income countries: Development, validation and application of a machine learning model" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Gian Paolo Rossi as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Both reviewers have found your manuscript of interest and potential relevance, as estimation of salt consumption by artificial intelligence in the population is a general problem. The Reviewers also agreed that this is more important for the low-mid income countries, which cannot afford measurements of sodium in a 24 hour urine collection or in a spot urinary sample. However, since the problem of estimating salt intake is not confined to such countries, a valuable addition that can increase the scientific merit of the study would be to provide data also on middle and high income countries.

They regarded as strengths of the study the development of a tool for estimating the sodium intake applicable to each country, particularly to those where it is difficult to collect urine specimens, and also the novel machine learning approach applied to 19 WHO STEPS surveys including more than 45,000 people.

However, some methodological limitations were also noted, including the fact that your ML model was developed and validated using, as reference, data obtained from a 'golden' (spot urine samples), not a gold standard method (i.e. 24-hour urine sample). One Reviewer underlined that all equations, including the Intersalt's used as outcome in this study, can imply a bias in predicting 24h U-Na+ excretion, even with use of correction formulas (see Charlton KE, Schutte A et al., 2020). Hence, the finding that mean salt consumption predicted by the supervised ML model did not differ significantly from the mean observed value, should be validated with the Na+ intake determined by the 24h U-Na+ excretion.

Reviewer #1 (Recommendations for the authors):

I find these results to be important. The manuscript is well written and the methodology seems to be correct. However, since the problem of estimating salt intake is not confined to low income countries, a valuable addition that can increase the scientific merit of the study would be to provide data also on middle and high income countries.

Reviewer #2 (Recommendations for the authors):

In this study Guzman-Vilca et al., investigated if a machine learning (ML) model based on predictors that are routinely available in large scale surveys could predict salt intake in low- and middle-income countries (LMICs), and could be an appropriate tool to estimate sodium/salt intake in the national health surveys.

This is an interesting study that moves from the need of estimating sodium intake in countries that have no access to urine samples, and exploits a novel method to pursue the aim. However, the study suffers a major methodological limitation that should be deeply considered.

Major criticisms:

The Authors trained, tested and validated the ML model using data obtained from ‘golden standard’ methods (spot urine samples), not a gold standard method as reference (i.e. 24-hour urine sample) as recommended by STARD (Bossuyt PM. Ann Intern Med 2003). Even though not updated, there are survey from LMICs considering 24h U-Na+ excretion. This is a methodological limitation that should be amended.

Moreover, all equations, including the Intersalt used as outcome in this study, can implies a bias in predicting 24h U-Na+ excretion, even after using correction formulas (e.g. see Charlton KE, Schutte A et al., 2020). Hence, the mean salt consumption predicted by the supervised ML model, which was found not significantly different from the mean observed value, could be significantly different from the intake calculated with 24h U-Na+ excretion. Finally, the deviations from WHO recommendations (<5g daily) in the LMICs could be different from those resulting from the golden (not gold) standard approach-ML based model.

The quality of each survey, including the 19 surveys used for ML training and validation and those 49 used for estimating salt intake, should be preliminary evaluated using a validated scoring system before data processing as QUADAS-2. Quality could be crucial to understand differences between observed and predicted values.

Only a sub-analysis by sex was reported. It could be interesting to also evaluate how the ML model works at different ages, BP and BMI values.

Age range 15-69. Data from old/very old people were not considered at all. It is unclear if the exclusion of old people is related to the STEPS templates that include limited classes of age, or not.

Figure Pipeline Modeling Analysis. Please introduce abbreviations and provide a brief legend.

Last Figure (number is missing). Please add number, title and legend; enlarge dots and text on the right.

Tables. Please remove decimals from SBP and DBP.
