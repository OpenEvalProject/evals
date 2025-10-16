# Peer review - Round 1

Editors:
- Eduardo Franco, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78491.sa0](https://doi.org/10.7554/eLife.78491.sa0)

This work would be valuable to global health scientists, particularly in low- and middle-income countries where childhood stunting is an ongoing challenge, and to statisticians interested in building clinical prediction rules. The authors' solid methodology leveraged large, rich datasets from multi-center studies to build and validate predictive models.


---

# Peer review - Round 1

Editors:
- Eduardo Franco, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78491.sa1](https://doi.org/10.7554/eLife.78491.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Derivation and external validation of clinical prediction rules identifying children at risk of linear growth faltering (stunting) presenting for diarrheal care" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by me in my joint role as Reviewing Editor and Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Andrew N Mertens (Reviewer #2).

As is customary in eLife, the reviewers have discussed their critiques with one another and with the Editors, and I prepared this decision letter to help you prepare a revised submission. Given the extent of the suggestions, I prefer to provide you with a compilation of the relevant suggestions in the two critiques to assist you in preparing the revisions for an eventual resubmission.

Essential revisions:

Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you amend or expand the text to clarify the narrative accordingly.

The outcome used for prediction in a binary indicatory for a decrease in height-for-age Z-score >= 0.5. A child who fails to gain height by future measurements is of concern, but this outcome also misses children who are already experiencing growth failure, and is vulnerable to regression to the mean effect. The two most important predictors were age and current size, with current size having a positive association with risk of growth faltering. As mentioned in the discussion, there is "the possibility that children need to have high enough HAZ in order to have the potential to falter." Additionally, there may be children with erroneously high height measurements at the first measurement, so that the HAZ change >= 0.5 associated with high baseline HAZ is from measurement-error regression to the mean. I recommend also predicting absolute HAZ (or stunting status) as a secondary outcome and comparing if the important predictors change. Were alternative specifications (e.g., quantitative decrease in HAZ, incident stunting) considered?

In its current form, the results and conclusions from the results have problematic implications for the treatment of child malnutrition. The conclusion states: "In settings with high mortality and morbidity in early childhood, such tools could represent a cost-effective way to target resources towards those who need it most." If the current CPR was used in a resource-constrained setting, it would recommend that larger children should be prioritized for nutritional supplementation over already stunted children who may have reached their growth faltering floor. In addition, with a sensitivity of 80%, the tool would miss treating a large number of children who would experience growth faltering. The results of the clinical prediction tool need to be presented with care in how it could be used to prioritize treatment without missing treating children who would benefit from nutritional supplementation. Including absolute HAZ as an outcome will help, along with additional discussion of how the CPR fits alongside current treatment recommendations. For example, does this rule indicate treating children who aren't currently treated, or are there children who don't need treatment given current guidelines and the created CPR.

The results from these datasets may not have identified novel and strong predictors of growth faltering, as the current results indicate that additional predictors beyond current size and age don't help with predictions, but the analysis could be reframed as a template for developing a CPR, using this data as a case study. If age and current size are the only important predictors, then a simple rule based on age and a current HAZ cutoff could be created, negating the need for a more complicated model, but this manuscript also provides a good template for other clinical prediction analyses. Could you comment more on the methods and performance metrics used in the discussion, and make a recommendation for future analyses?

Why use the MAL-ED data to externally validate the CPR developed using GEMS data, given the different study designs, definitions of diarrheal disease, and predictors measured. Because GEMS is a multisite study, wouldn't it be easier, and allow more complex models to be validated, if the model was fit using data from some countries, then validated in populations from other countries?

In addition to the coefficients for the 10-variable model, it would be helpful to present coefficients for the final 2-variable model that was assessed in both GEMS and MAL-ED.

Although the authors opted to use logistic regression based on AUC, the AUC values for random forest models were only slightly lower (Figure S2), and random forest may provide simpler clinical prediction rules. It may be interesting to also describe the rules that were developed by the random forest models. The last panel in Figure S2 may be mislabeled (0-23 mo for MAL-ED instead of 0-59 mo).

I am not very familiar with the variable importance calculated from random forest models. What is the implication of certain features having high variable importance, but also having coefficient estimates that are indistinguishable from the null (e.g., age in MAL-ED, respiratory rate in GEMS in Table S4)?

In the Discussion (p.20), the authors note that the entire diarrheal history of a child may be a more important indicator of linear growth faltering than a single episode. These datasets seem potentially well-suited to directly explore this question ¬- were frequency/number of prior diarrheal episodes investigated as predictors in GEMS / MAL-ED?

For reproducibility, please specify the software and key packages with corresponding versions that were used for this analysis.

The best performing model was logistic regressions fit with variables chosen by random forest models. Any idea why this would be? Is it because they are simpler and the random forest models are overfit to the training data? I would expect them to perform worse because they don't allow for nonlinearity and interactions like a RF model. If generalized linear models perform better than random forest for prediction in this situation, penalized logistic regression models may also improve predictive performance by incorporating variable selection with prediction in a simpler model than random forests.

The conclusion in the abstract is "Our findings indicate that use of prediction rules could help identify children at risk of poor outcomes after an episode of diarrheal illness", but prediction performance is the same in control children, so while its important to retain the discussion of lack of association between diarrhea and growth, the framing of the paper could be expanded around all children in LMIC, rather than just children with acute diarrhea. This could just be a slight reframing in the writing, or you could expand the MAL-ED prediction model to use all children in addition to the prediction on the subset of children with diarrhea.

What is the rationale for comparing HAZ and MUAC as separate and combined predictors of growth? On one hand, it's interesting to compare which current measures of anthropometry are most associated with future measures of anthropometry, in which case you'd want to include other outcomes such as WHZ, WAZ, and MUAC. But if the goal is to develop the best clinical prediction tool, it makes more sense to include all measures of growth that can be easily clinically collected as predictors to see if performance increases by including WHZ, WAZ, and MUAC on top of HAZ.

Line 125-128: "Model performance was assessed using the receiver operating characteristic (ROC) curves and the cross-validated C-statistic (area under the ROC curve (AUC)), a measures which describes how well a model can discriminate between the two outcomes, from the cross-validation." Confusingly worded… do you mean "AUC is a measure which describes how well a model can predict a binary outcome in test data from the cross-validated folds."

Line 129-142: Model calibration performance metrics: these were new to me, and I wasn't sure what to be looking for or what story they could tell us about model performance beyond the AUC. What is the reader looking for? Can they tell us something different than the AUC?

Line 173: separately report missing versus implausible values, because the percent implausible gives an indication of data quality.

Lines 177-182: Report mean HAZ by country as well to show if it there is lower growth faltering in some countries because of high existing stunting by the age of first measurement.

Line 199: This is the first mention of death as an outcome (and the results of the CPR for death are not discussed).

Page 20: "It is possible that the entire diarrheal history of a child (e.g. frequency and severity of acute diarrhea), or subclinical enteric infections that do not result in diarrhea, are more important to their growth trajectory than a single diarrheal episode, though evidence is mixed." As you have longitudinal data from MAL-ED, can't you explicitly check this by using diarrhea history as a predictor?

Page 21: "Unlike previous work in this area, we used random forests for variable selection which do not require assumptions about the underlying variables and generally outperform(49) conventional model building techniques."

– Need to clarify that random forests have no assumptions about the relationship between variables, not about the variables themselves, which still have assumptions around how they are coded/categorized.

Tables S4- Age is the most important predictor, but the OR is 1 with 1,1 confidence intervals. Can you convert the predictor to age in months or report more decimal places so direction of effect can be seen?
