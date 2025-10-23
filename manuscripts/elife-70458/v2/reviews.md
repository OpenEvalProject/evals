# Peer review - Round 1

Editors:
- Jos W Van der Meer, Radboud University Medical Centre Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70458.sa1](https://doi.org/10.7554/eLife.70458.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors performed a systematic literature review and meta-analysis to develop a dataset of respiratory viral loads (rVLs) for SARS-CoV-2. Focus was on finding the relation between individual case characteristics (e.g. disease severity, age and sex) and lower and upper respiratory tract viral loads. COVID-19 severity, rather than sex or age, predicts SARS-CoV-2 kinetics, and SARS-CoV-2 viral load from lower respiratory tract specimens seems to predict severe disease days before clinical deterioration for COVID-19 patients.

Decision letter after peer review:

Thank you for submitting your article "SARS-CoV-2 shedding dynamics across the respiratory tract, sex and disease severity for adult and pediatric COVID-19: a systematic review and modeling study" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Jos Van der Meer as the Senior and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Lucie Vermeulen (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) It is not clear how surprising the association between LRT and disease severity is. For example, a similar result was found by Buetti et al., Critical Care, 2020 ("viral shedding in LRT lasted almost 30 days in median in critically ill patients, and the viral load in the LRT was associated with the 6-week mortality.") and the statement made in the methods of this paper ("In COVID-19 cases, rVL tends to diminish exponentially after 1 DFSO in the URT, whereas it tends to do so after 4 DFSO in the LRT (Bernheim et al., 2020; Chen et al., 2021; Wolfel et al., 2020)." ) also indicates that a faster decrease of viral load has been observed in URT compared to LRT. The present analysis certainly adds to these findings, but the observation does not seem to be completely new.

2) Lines 322-: "Data from serially sampled asymptomatic cases were included, and the day of laboratory diagnosis was referenced as 0 DFSO". It would be interesting to compare the dynamics observed in those serially sampled patients to the patterns shown in Figure 2 and derived mostly from cross-sectional data.

3) Lines 366-:"We used regression analysis to assess the respiratory shedding of SARS-CoV-2 and compare age, sex or severity groups. " Please specify the type of regression analysis (I guess this was "normal" linear regression assuming normally distributed erros). How are measurements with undetectable virus loads included in the analysis? Wouldn't these measurements call for the use of censored regression models?

4) The approach of how the authors estimated the AUC-ROC for the prediction of disease severity is not fully clear. Why did the authors need to first fit a distribution to the viral load values? The ROC curve and its AUC value can be computed directly from the observations, without this intermediate step.

5) Line 381-382: You write "Regression models were extrapolated (to 0 log10 copies/ml, rather than an assay detection limit) to estimate the duration of shedding." How large is the effect of extrapolating to 0 instead of to the detection limit? Some discussion on this is warranted.

6) Line 390: Why was the Weibull distribution chosen? Some reasoning for this could be added to the paper (in methods, discussion or supplement)

7) Line 399-400: "The fitted Weibull distributions were used to estimate the accuracy when using URT or LRT rVLs of SARS-CoV-2 as a prognostic indicator for SARS-CoV-2 infection." Do you mean severity of infection here?

8) Table 1: There are relatively few lower respiratory samples included in the analysis, compared to the number of upper respiratory samples. What is typically the reason that a LRT sample is taken from a patient? And following, is there any possible association of taking an LRT sample with patient characteristics included or excluded in this study that could influence the results? Then some discussion on this would be warranted.

9) Figure 4: Could it be made clearer in the figure which panels concern URT and which LRT? Now the reader has to carefully read the caption in order to deduce this.Reviewer #1 (Recommendations for the authors):

This manuscript presents a systematic review and regression analysis to analyze the association between upper and lower respiratory tract shedding (URT and LRT) of SARS-CoV-2 and disease severity. In addition, the authors study the impact of the days from symptoms onset on shedding in the two compartments. Overall, the presented results provide an interesting synthesis of the literature on these issues.

Reviewer #2 (Recommendations for the authors):

The study appears robust and comprehensive, and relevant quality checks for systematic review have been applied. The results are valuable and contribute to the scientific knowledge in this field.

Interesting findings include:

– Adult patients with severe disease had on average a somewhat higher upper respiratory tract viral load at 1 day from symptom onset than patients with non-severe disease. After this stratification for severity, respiratory viral loads did not differ significantly for age and sex. Rates of viral clearing were similar. Children and adults with non-severe disease had similar upper respiratory tract viral loads and viral clearance rates.

– High and persistent lower respiratory tract shedding of SARS-CoV-2 was associated with severe but not non-severe illness. The difference in lower respiratory viral load for severe and non-severe cases was more pronounced than for upper respiratory tract viral loads. In contrast to the upper respiratory tract, viral clearance from the lower respiratory tract was more rapid in non-severe than in severe cases. Again, age and sex did not differ significantly after stratification for severity.

– The authors then aimed to assess whether the observed difference in shedding in the first days after start of symptoms could be used to predict which people would develop more severe COVID-19. Typically, deterioration into severe disease only happens around 10 days from symptom onset. The authors conclude that upper respiratory tract viral shedding is so heterogeneous that its predictive capacity of disease severity is inaccurate. In contrast, lower respiratory tract shedding does have a predictive accuracy of up to 81% for disease severity.

Potential impact: Lower respiratory tract viral load could thus potentially be used as an early warning for developing severe COVID-19. However, lower respiratory tract samples are not routinely taken, the standard nasopharyngeal swab is an upper respiratory sample. Some discussion on the practical applicability of this suggestion could enhance the paper's impact.
