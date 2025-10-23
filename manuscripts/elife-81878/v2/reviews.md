# Peer review - Round 1

Editors:
- Girish N Nadkarni, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81878.sa0](https://doi.org/10.7554/eLife.81878.sa0)

The authors wanted to see which patients with diabetes develop kidney disease and outcomes. They used clinical characteristics, eye pictures, genetic factors and blood levels of metabolites, and they found a combination of these factors predicted kidney disease in people with diabetes.


---

# Peer review - Round 1

Editors:
- Girish N Nadkarni, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81878.sa1](https://doi.org/10.7554/eLife.81878.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Prediction of diabetic kidney disease risk using machine learning models: a population-based cohort study of Asian adults" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Martin Pollak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Statistical significance versus clinical significance:

The authors seem to use recursive feature elimination to come up with a set of top features for each Ml algorithm and select features from a varied feature set. However, the authors may need to pay attention to what the features (that come up as significant) are trying to allude to? for e.g. the authors seem to have dropped the datasets with features that contain the genetic and imaging parameters: D= B+ Genetic parameters and F= B+ Imaging parameters+ Blood metabolites+ Genetic parameters. They provide reasons for the low performance of the ML models for dropping the features but do not elaborate on whether they investigated the reasons for the drop in performance.

2) The authors speak about the advantage of using ML approaches to overcome shortcomings of traditional assumptions from linear models, however, in the consideration of their covariates they might also want to understand the clinical association between some of their selected features. for e.g. BMI, HbA1c, duration of diabetes, and systolic BP may somehow not be entirely independent of each other (especially in the context of influencing one another and driving diabetes) and multi-collinearity may need to be looked into.

3) One of the biggest limitations of the study is its longitudinal nature with 6 yr timeframe for the development of DKD. That is a long timeframe to be able to discount factors other than those mentioned that could have affected the development of kidney disease. For example, patients with diabetes are also at risk for heart diseases, infections, and other hospital admissions, all of which can affect the development of kidney disease over that timeframe and haven't been controlled for in the dataset. Without controlling for these factors, the results have the risk of being hugely biased.

4) How were patients who died within that timeframe treated? Were they classified as DKD or censored? A competing risk methodology (with or without ML) might be better suited for this question or at least merit a sensitivity analysis with it.

5) The definition of DKD solely relies on a decrease in eGFR. Though understandable, it has the potential to be highly flawed, especially with factors discussed in #1. Adding measures to proteinuria/albuminuria, if available, would greatly add to its value.

6) The authors define incident DKD as eGFR < 60. Albuminuria is generally the earliest sign of DKD – the authors say this is because of missing data. This omission may underestimate the incidence of CKD in this study. Screening for DKD with annual UACR should be addressed as well in the introduction, as the authors say that early detection is challenging.

7) Ethnicity should not be included as a "traditional risk factor" as it is not a biological variable, but rather a social construct. How was ethnicity determined in the SEED study?

8) What was the rationale for the hundreds of metabolites that were chosen?

9) We suggest performing subgroup analysis on each of the 3 ethnic groups (Chinese, Malay, and Indian) to look for differences that may be explained by other variables as all "Asians" are not the same.

Reviewer #1 (Recommendations for the authors):

I would recommend the authors look at their wealth of features and their data and perform more association analysis and try and explain their feature selections instead of just depending on the outcome from the RFE.

I would also encourage the authors to look at the development of the model in association with a clinician and a biostatistician so as to understand the outcome of the model in the context of the disease and explain what the model outcomes are telling them about the progression of the disease.

The authors should also try and address the issue of bias that can creep into the model due to the features selected. is the model giving you the 6 yr risk of developing CKD and stating that Malays and Chinese populations are at higher risk for CKD from diabetes or does the model allude to some sort of socioeconomic factors playing a role in not getting medically examined regularly enough to miss the progression of diabetes to CKD?

Reviewer #2 (Recommendations for the authors):

It is an interesting study using various supervised machine learning methods to identify the risk and risk factors for the development of diabetic kidney disease. The study is overall well done. Few comments –

1. One of the biggest limitations of the study is its longitudinal nature with 6 yr timeframe for the development of DKD. That is a long timeframe to be able to discount factors other than those mentioned that could have affected the development of kidney disease. For example, patients with diabetes are also at risk for heart diseases, infections, and other hospital admissions, all of which can affect the development of kidney disease over that timeframe and haven't been controlled for in the dataset. Without controlling for these factors, the results have the risk of being hugely biased.

2. How were patients who died within that timeframe treated? Were they classified as DKD or censored? A competing risk methodology (with or without ML) might be better suited for this question or at least merit a sensitivity analysis with it.

3. The definition of DKD solely relies on a decrease in eGFR. Though understandable, it has the potential to be highly flawed especially with factors as discussed in #1. Adding measures to proteinuria/albuminuria, if available, would greatly add to its value.

4. Another 2 questions that I wasn't able to find answers to were – the average length of follow-up and how much was loss to follow-up.

Reviewer #3 (Recommendations for the authors):

1. The authors define incident DKD as eGFR < 60. Albuminuria is generally the earliest sign of DKD – the authors say this is because of missing data. This omission may underestimate the incidence of CKD in this study. Screening for DKD with annual UACR should be addressed as well in the introduction, as the authors say that early detection is challenging.

2. Ethnicity should not be included as a "traditional risk factor" as it is not a biological variable, but rather a social construct. How was ethnicity determined in the SEED study?

3. What was the rationale for the hundreds of metabolites that were chosen?

4. Suggest performing subgroup analysis on each of the 3 ethnic groups (Chinese, Malay, and Indian) to look for differences that may be explained by other variables as all “Asians” are not the same.

5. There are several mentions in the discussion of ethnicity being a risk factor for CKD or diabetes – ethnicity is not the risk factor.

6. This sentence is problematic on page 16: "One reason for the Indian ethnicity to be at lower risk of developing DKD could be Indian ethnicity being a high-risk group for diabetes, they may be well aware of the risk, and comply with screening, medication, etc. that could reduce their risk of developing DKD."

7. Suggest expanding the discussion of metabolites: why were they chosen and what is the proposed mechanism that increases the risk of DKD?

8. What were the "anti-DM" meds? What percentage were insulin-dependent? This would suggest potentially higher DM severity.

9. Suggest discussing the “top 15” predictors in the 3 models and proposed mechanisms that are not traditional risk factors (e.g. 3-hydroxybutyrate in the GBDT model; acetate in the EN model).

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Prediction of diabetic kidney disease risk using machine learning models: a population-based cohort study of Asian adults" for further consideration by eLife. Your revised article has been evaluated by Martin Pollak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #2 (Recommendations for the authors):

The authors have answered most of the questions adequately. One major concern I still have is its longitudinal nature with 6 yr timeframe for the development of DKD. The authors have noted that as the AUC of the model is 0.85, baseline characteristics are good enough to predict DKD. If we look closely though the incidence of DKD was <12%. It is thus an unbalanced dataset and therefore AUC is likely an inflated value that needs to be interpreted with caution. I realize that ultimately this is the data that the authors have and it is still a valuable addition to the literature but this is an important limitation that needs to be acknowledged upfront.
