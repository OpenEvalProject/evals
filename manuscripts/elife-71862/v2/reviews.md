# Peer review - Round 1

Editors:
- Nicola Napoli, https://ror.org/04gqx4x78 Campus Bio-Medico University of Rome Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71862.sa0](https://doi.org/10.7554/eLife.71862.sa0)

The authors have used the UK Biobank with sophisticated statistical modeling to predict the risk of type 2 diabetes mellitus development. Prognosis and early detection of diabetes are key factors in clinical practice, and the current data suggest a new machine-learning-based algorithm that further advances our ability to prevent diabetes.


---

# Peer review - Round 1

Editors:
- Nicola Napoli, https://ror.org/04gqx4x78 Campus Bio-Medico University of Rome Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71862.sa1](https://doi.org/10.7554/eLife.71862.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Prediction of type 2 diabetes mellitus onset using logistic regression-based scorecards" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Sina Azadnajafabad (Reviewer #1); Promi Das (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Methodological issues and subjects inclusion raised in points 2-5 of reviewer 2 are crucial for the potential acceptance of this manuscript.

2) Further validation with another cohort as requested by reviewer 3 is needed.

Reviewer #1 (Recommendations for the authors):

1. Abstract, background: authors claim that their aim was to propose non-lab-based models for the use of lower socio-economic countries. However, almost half of the methods of this paper are on lab-based models. A revision of the aim of the study is necessary.

2. Abstract, background: "Early detection of T2D high-risk patients can reduce the incidence of the disease through a change in lifestyle, diet, or medication." Incidence of a disease is a multi-dimensional phenomenon and the claim that early detection of high-risk patients could reduce the incidence of a disease is not clinically sound. Maybe changing the sentence to a condition that this early detection may provide health authorities the proper vision to prepare the health systems for upcoming events be a better idea.

3. Abstract, methods: the "scoreboard form" and the comparison of the developed models with two previous prediction models should be explained in the methods clearly before proposing results and conclusion.

4. Introduction: the first part on the epidemiology of diabetes needs more updated statistics and references. There are multiple databases like the updated Global Burden of Disease 2019 database that authors could use. Also, comparing the burden of diabetes in various socio-economic levels of countries could benefit this section.

5. Methods: this section needs a clear elaboration on the reason for choosing the mentioned variables for non-lab and lab models. Definitely, the statistical aspects are well drafted. However, the manuscript needs a simple explanation for this issue.

6. Results: well-drafted and visualized.

7. Discussion and conclusion: a major part is missing on the link of the utilization of these models and reducing the burden of diabetes. Whether individual or population investigation and implementation of such models would be better needs to be discussed, providing essential points for those who want to benefit from what was introduced in this study.

Reviewer #2 (Recommendations for the authors):

Here is a summary of my main concerns:

1. The authors don't mention previous work of predicting T2D, except the GDRS and FINDRISC. There are many such studies, including studies that use the UKB. To name a few: Di Camillo et al., European Journal of Endocrinology, 2018; Lama et al., Heliyon, 2021; Zhang et al., Scientific Reports, 2020; Dolezalova et al., arxiv, 2021; He et al., Diabetes Care, 2021. This is just a few found on simple google search, but there are many more.

2. The numbers from the UKB don't look right to me. There is available clinical data for UKB participants, therefore no need to focus only on those that came back for additional visit. This limits the data in the study to ~70K individuals, and after exclusions to ~45K with only ~1K cases. In comparison, a recent study (He et al., Diabetes Care 2021) that used the same dataset, there were 7513 T2D cases.

3. It is also unclear to me how the "years of prediction" is calculated – is that the time between first and second visit? If so, that doesn't represent the time between the first visit and the in identification of T2D. This might be a major issue that needs to be addressed.

4. In addition, in this study a simple logistic regression method was used. However, this is a clear case of censored data. LR is not the right method for these kind of prediction tasks.

5. Another issue I find with the data is that pre-diabetic individuals are not excluded. Predicting that someone that is pre-diabetic will be diabetic is a very different task than predicting healthy individual to become diabetic. I understand that in the first model, we assume that blood tests are unavailable, so in theory in this model a pre-diabetic individual will not have access to HbA1c test and won't know that they are pre-diabetic. However, in the UKB cohort, that person knows about the condition, and thus, it confounds the prediction. I do see that a model without the pre-diabetic individuals was performed, but it is only a secondary analysis, and I think it should be the main analysis.

6. The issues above make it hard to compare the results in this study with previous studies. Previous analyses (including using the UKB) with GDRS and FINDRISC have showed an AUC of about 0.75. I find it hard to believe the GDRS results are only 0.58. This suggests that there are inconsistencies in the data and analysis in this study.

Reviewer #3 (Recommendations for the authors):

Specific suggestion:

As the model metrics and the cohort chosen are very similar to one another, it is highly suggested to conduct such analyses on a different country cohort if possible, the findings would be of additional value.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Prediction of type 2 diabetes mellitus onset using logistic regression-based scorecards" for further consideration by eLife. Your revised article has been evaluated by Matthias Barton (Senior Editor), a Reviewing Editor, and the original reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

The authors of this study made their best to address the comments and improve the draft in this revision. Although the changes based on my previously provided comments are enough and sound, the manuscript is a little bit messy and needs a comprehensive language revision and checking. For example, changing the sort of the sections of the manuscript has caused some errors in the number of sections and subsections. A general revision in this regard could finalize the manuscript in my opinion.

Reviewer #2 (Recommendations for the authors):

The authors fixed most of my concerns, but I still have some unresolved issues.

1. In the response the authors explain that they don't want to use the full cohort of patients with baseline information alone. The logic used is that there is 'diagnostic access' bias. It might be true, but its unclear to me how much this is a concern in UK. If this was a major concern, then it affects the questionnaires, not just the clinical data. It should also be noted that there is 'report' bias (as the authors note in the methods). I also disagree that those individuals that returned to another visit can be regarded as a "controlled cohort", on the contrary, this is a selected group, not randomized, as in the first visit. Finally, as I noted in the previous review, the 'time to event' is wrong – its not ~7 years to diagnosis – its ~7 years between visits. The outcome is an answer whether the individual has T2D or not, and it could have manifested 6 years earlier. For all these reasons and more (cohort size, selection bias, etc.) I urge you to reconsider, use the full cohort and infer outcome of T2D from the clinical data, not the questionnaire.

2. This continues to my previous concerns – I was happy to see the addition of a Cox model, but I can't understand why the logistic regression model is still being used. If you insist of using such a model, please don't refer to it as prediction of T2D ~7 years in advance – it's a prediction of answering true to a question whether you were diagnosed with T2D in the time between first and second visit. All the models, including the scorecards, should be based on the 'real' time to diagnosis. If time-varying models do not fit with a scorecard, you can create a model that predicts diabetes 1,2 or 5 years in advance.

3. Another comment I had that is still an issue is regarding the deciles fold-ratio. Confidence intervals are good, but as I noted, the ratio should not be between the top and bottom deciles but top and median deciles. The current approach can provide very impressive results for a useless model (for example – ~0% in bottom decile, ~1% in all other deciles).

4. It is great to see the external validation cohort. It would have been great to see the other models implemented in that external cohort (GDRC and FINDRISC) and get some sense how much this model can improve current risk stratification approaches.

5. The paper still requires major editing and grammar corrections.

Reviewer #3 (Recommendations for the authors):

Each of my suggestions has been sufficiently addressed and has been added to the updated manuscript by the authors.
