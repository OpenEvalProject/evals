# Peer review - Round 1

Editors:
- Evangelos J Giamarellos-Bourboulis, Attikon University Hospital Greece

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60519.sa1](https://doi.org/10.7554/eLife.60519.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper provides meaningful information on the risk factors for ICU admission and mechanical ventilation. The authors used data from the largest healthcare system in Massachusetts to develop models to predict hospitalization, ICU admission, and need for mechanical ventilation in patients presenting with COVID-19.

Decision letter after peer review:

Thank you for submitting your article "Early prediction of level-of-care requirements in patients with COVID-19" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Evangelos J Giamarellos-Bourboulis as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Jos van der Meer as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

This paper provides potentially meaningful information about the risk factors for ICU admission and mechanical ventilation. The authors used data from the largest healthcare system in Massachusetts to develop models to predict hospitalization, ICU admission, and need for mechanical ventilation in patients presenting with COVID-19.

Essential revisions:

1) The authors use three main outcomes for their prediction: hospitalization, ICU admission and mechanical ventilation (MV). From these outcomes, the authors need to explain how their model is superior over the traditional medical approach of an ICU physician. We doubt that one such model is superior to clinical judgment on the need of hospital admission or ICU admission. The authors need to provide evidence that patients who were missed from clinical judgment cannot be missed from their models and vice versa.

2) The equation of the models is not clear, although the regression factors are provided.

3) What does "a comorbidity of adrenal insufficiency" mean?

4) The results of the derivation and confirmation cohorts should be provided side by side.

5) How earlier does the model predict the need for MV?

6) Subsection “Data description” and Supplementary Table 2: The Pearson correlation coefficient is not a meaningful way to measure the correlation of binary data. A chi-square test or a logit model would be more appropriate.

7) Subsection “Pre-processing and variable selection”. The authors state that they have extracted 164 features, and after preprocessing they retained 106 variables for the hospitalization model and 130 variables for ICU and ventilation. More information about the variables used should be given. Were similar variables grouped together? For example, pyrexia, fever and febrile are used interchangeably in patient notes. The extracted variables should be provided in a supplementary table, and some statistics should be given for these variables (number of missing values, mean, sd, etc) so that the reader can understand and assess the significance of the variables used.

8) Appendix subsection “Representative statistics of patients and variables highly correlated with the outcomes” and Appendix 1—table 1. A t-test (difference between two means) should not be used for binary variables. A chi-squared test or fisher's exact test could be used instead.

9) The authors used natural language processing to extract vitals, medical history, medications, and symptoms. However, they do not mention if they performed (and how) a validation of the NLP model and if they evaluated the correctness of the extracted variables. Was a subset of the extraction manually checked for correctness? Was the extracted medical history compared to coded ICD-10 codes? More information should be given, and the authors need to at least discuss the limitations of the method.

10) The authors state that they "calculated a p-value for each variable as described earlier". In the Appendix subsection “Representative statistics of patients and variables highly correlated with the outcomes” they state that they computed a p-value using a two-sited t-test for binary variables, which is inappropriate (see comment 3). If this is what they did (which is also suggested by the p-values in Table 1), the feature selection process needs to be repeated using the appropriate statistical tests, and the models re-run

11) The authors should discuss the sparsity of the variables and the efficiency of Random forests on sparse data compared to XGBoost.

12) The authors should mention when and why they used each model. Why wasn't XGBoost used in the 'big' ICU prediction model and why RF wasn't used in the restricted ICU model using all 130 features? Ideally, all model architectures should be compared for the reader to be able to understand when to use each model, and for consistency.

13) Abstract and Discussion. "Complex disease" should be rephrased or defined well. We understand that these patients were just hospitalized, and authors give no information on the severity of their disease (for example if these patients required oxygen supplementation, their SpO2 on presentation, etc.)

14) The authors state that they employed "custom" linear methods. Did the authors use a custom loss function in addition to l1 regularization?
