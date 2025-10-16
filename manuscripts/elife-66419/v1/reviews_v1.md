# Peer review - Round 1

Editors:
- Arduino A Mangoni, Flinders Medical Centre Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66419.sa1](https://doi.org/10.7554/eLife.66419.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this work, the authors developed easy-to-use simple nomograms to predict the 10-year probability of hypertension from easily accessible health metrics. The study deposits an important dataset, and carries out classical multivariate analyses to arrive to a usable model. Not accounting for inter-dependencies may, however, limit the performance of the generated models. Going beyond nomograms and employing advanced, yet easily accessible, machine learning approaches may show the real potential of the compiled data.

Decision letter after peer review:

Thank you for submitting your article "Development and validation of a nomogram to better predict hypertension based on a 10-year retrospective cohort study" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Matthias Barton as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Richard Woodman (Reviewer #1).

The reviewers and Editors have discussed their reviews with one another, and this letter will help you prepare a revised submission.

Essential revisions:

– The title would benefit from the mention of the population involved in the study, as the outcomes will likely not be transferrable to other populations. For the sake of clarity, it will also help if the manuscript body explicitly mentions that the predicted hypertension probabilities are for the 10-year risk.

– The search for independent features zooms in to 10 features for nomogram140/90 and 6 features for nomogram130/80. Biologically, any feature that has an association in defining the hypertension probability, should have a predictive relevance regardless whether the cutoff for the hypertension definition is 140/90 or 130/80. The used approach of feature trimming, and different numbers of features for the two nomograms, may neglect important interactions. Furthermore, the overall low number of features warrant the application of higher-end machine learning techniques for feature selection (if at all deemed to be necessary to eliminate any). For this, decision-tree-based techniques, such as random forests or gradient boosting machines, may have greater promise for arriving to better models, while internally producing feature importance rankings for possible elimination of the low performing ones (all done while accounting possible complex and multiplexed interactions between the features).

– The authors should explain their rationale for using the LASSO e.g. that they used it as a variable selection technique to reduce the number of parameters and thereby simply the risk prediction model? What was the degree of correlation amongst the 40 available covariates? Details of the package used in R to perform the LASSO should be provided. What was the approach used for the chosen value of lambda to identify the final LASSO model e.g. lambda that provides the minimum cross-validated MSE or lambda with minimum MSE +1SE? Were interactions and higher-order variables assessed in the LASSO. If not, why not?

– The calibration curve for BP 140/90 is, as the authors point out, poor especially for higher risk patients. This is a real concern if the model is to be used for accurate risk prediction in those at higher risk.

– It seems the NRI and IDI were used to determine the best model using an estimated risk prediction score from 130/80 versus 140/90 as the outcome. Normally the NRI and IDI are used to determine the value of additional covariates for risk prediction whereas here the authors are basing the choice of the outcome on the NRI and IDI. The authors should explain the logic of this and justify the approach to the Journal readers.

– How are the cases handled when only the SBP or the DBP falls beyond the cutoff, but not the pair? If excluded, can excluding such cases eliminate an important, high-risk subpopulation from the model development?

– The discriminatory power of the model is relatively modest. The authors should describe how the prediction accuracy could perhaps be improved.

– P-values to 5 decimal places are not necessary – consult the Journal guidelines.

– TG and TBIL, as predictors of hypertension, may be result of chance and the chosen sample and random sample. Except for the internal validation, the authors should discuss the need for external validation of the risk prediction model.

– Section 2.2, the second to last line. Written "weight (Kg)", should be "weight (kg)".

– Section 2.3, the C-index metric is introduced first time in the text (not counting the Abstract), without defining and expanding it.

– Section 3.3, written "… was assessed with the AUC and c-index", c should be capitalised for consistency.

– Section 4 (Discussion), 3rd paragraph. Written "… AUC of nomogram140/90 was higher than that of monogram140/90". The last one should be "nomogram130/80".

– In the same section, written "Similar to our study, the Iranian research from revealed the same result…". Seems there is a missing word in between "from" and "revealed".

– Figure 1 caption. Needs an expansion with a brief description of the content.

– Figure 2. The x-axes in A and C are labelled as Log(λ), while those for B and D are labelled as Log Lambda. Please, change them to be the same.

– Figure 2 caption. The caption needs comments about the line colours and about the lines that stand out in B and D.

– Figure 3 and the associate text will benefit from a brief description of how one should use the nomogram. It is easy to infer from the nomogram itself, but, considering the presence of multiple types of nomograms, explicitly describing the usage of this particular type will save a few minutes for the readers.

– Figure 4. Please organise the line labelling brought next to the plots in an ascending or descending order for the corresponding AUC values.

– Most tables are missing footnotes to describe the abbreviations.
