# Peer review - Round 1

Editors:
- Wadih Arap, Rutgers Cancer Institute of New Jersey United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71562.sa0](https://doi.org/10.7554/eLife.71562.sa0)

We feel that your work will be of interest to breast medical oncologists, cardiologists, and primary care providers who treat patients with breast cancer. We commend you for this study, which achieves its goal of identifying the incidence and hazard ratio of cardio-toxicity associated with breast cancer treatment within a general breast cancer population. The international nature of your collaborative study along with its large patient cohort size and long horizontal follow up are quite attractive features in solidifying previous findings and discovering future areas of exploration.


---

# Peer review - Round 1

Editors:
- Wadih Arap, Rutgers Cancer Institute of New Jersey United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71562.sa1](https://doi.org/10.7554/eLife.71562.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you very much for submitting your work to eLife. Your article has been reviewed by 3 peer reviewers and the evaluation has been overseen by Eduardo Franco as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Philip Boonstra (Reviewer #3).

As you will see in the attached reviews, while the Referees generally recognized the merits of your draft, several technical points of concern in your methodology and findings were also highlighted. Thus, we remain interested potentially publishing an extensively revised version of your manuscript. However, we would like you to specifically address the following perceived weaknesses of your work, in particular the biostatistical methodology, as follows:

Essential revisions:

1. The title of the draft suggests the risk of heart disease is associated with breast cancer itself, but the content of the manuscript and conclusions emphasize the risk based upon treatment effects. Please, modify the title to reflect the risk of breast cancer therapy.

2. For Table 1: In addition to Charlson Comorbidity Index (CCI score), please include CVD risk factors (e.g., HTN, HLD, DM2, BMI, tobacco-smoking) to help readers understand the baseline cardiovascular risk of your patients. This criticism assumes importance as these risk factors were used in the risk models, and independent of cancer treatment are known to be associated with risk of arrhythmias, ischemic heart disease, and congestive heart failure.

3. For Table 2: Please add the word "Ratio" i.e. "Hazard ratio for heart diseases" in the title.

4. The finding of no significant increased risk of ischemic heart disease after left breast radiation is quite interesting. This provocative result would become more powerful (and better supported) if estimates of mean heart dose of radiation or even total cumulative radiation dose administered were included. If those may not be available from the registry data, please discuss this potentially counterintuitive finding.

5. Regarding hypotheses made in the Discussion section: The authors appropriately provide citations regarding early increased risk of ischemic heart disease due to emotional distress, however there are several other factors that could potentially increase this risk that warrant consideration, namely: surgery for breast cancer (98.9% of patients in this cohort) typically takes place within the first year of diagnosis and may increase risk of arrhythmia, ischemic event; patients with cancer are at increased risk of arterial thromboembolism (ATE) which includes myocardial infarction 150 days prior to cancer diagnosis and this risk appears to attenuate 1 year after diagnosis. (Navi, B. B., et al., (2017). "Risk of Arterial Thromboembolism in Patients with Cancer." J Am Coll Cardiol 70(8): 926-938) (Navi, B. B., et al., (2019). "Arterial thromboembolic events preceding the diagnosis of cancer in older persons." Blood 133(8): 781-789.)

6. Please discuss the fact that while the results are generally interesting and hypothesis-generating, the patient population is overall young and healthy (median age 59, majority CCI = 0); thus, one should be cautious to extrapolate results to guide individual therapy decisions in clinical practice.

7. It is also unclear whether there was any protocol in place for cardiac monitoring for patients receiving cardiotoxic chemotherapy or Anti Her2neu agents. Please clarify it in the revised draft, either way.

8. With regard to the matched analysis of time to heart disease diagnosis: For the breast cancer cohort, were patients with a diagnosis of heart disease prior to cancer diagnosis included in the analysis? If so, how was the event (which precedes time = 0) incorporated into the analysis? If not, please make sure to make note of this important restriction. Please, keep in mind that Referee 3 clearly favors the latter approach.

9. Moreover, for the matched cohort: What is time = 0 for these persons? i.e. how does one interpret "Time since diagnosis" on Figure 1 for a patient who has not been diagnosed with breast cancer?

10. Finally, for the matched cohort: How was the matching incorporated into the FPM? Presumably there should be a frailty term of some sort to indicate the matched groups, within which there is expected to be correlation.

11. Kaplan-Meier curves were used to estimate the cumulative incidence of heart disease. How was death of the patient prior to diagnosis of heart disease handled? Of note, Referee #3 argues that Kaplan-Meier is not the best analytical approach here because Kaplan-Meier tends to overestimate the event rate when competing events are counted as censoring. In this setting, Referee #3 favors an Aaalen-Johansen-type estimator, which treats death as a competing event. For instance, please see: https://pubmed.ncbi.nlm.nih.gov/10204198/

12. Please address and correct: The sentence "Missing indicators were included for the analysis of these covariates in the model" and the results in Table 3 suggest that some missing values were analyzed "as is", meaning that "missingness" was used as a category itself. This, of course, is not desirable and there exists methodology+software for more appropriately handling these data, e.g. multiple imputation with chained equations. For example, how does one interpret that "unknown chemotherapy" status is positively associated with heart failure but less so than anthracycline-based chemotherapy.

13. Please address and correct: The reported HRs (at the top of p. 10) seem incongruous with the FPM model demonstrated in Figure 1, since there is clearly a non-linear relationship between the hazard and the outcome.

14. Please address and correct: It seems unlikely that breast cancer diagnosis could ever be "protective" for ischemic heart disease. A more constrained model that does not allow for the possibility of HR < 1 could provide a more sensible estimate of this time-dependent HR.

15. Please address and correct: As an alternative to a four-category radiotherapy variable, which (as the authors note) requires assuming that bilateral radiotherapy is equivalent to left-sided radiotherapy, it would seem sensible to create two separate binary variables (left, y vs. no and right, y vs. no).

16. Please double-check rows two and three of the first column of Table 2. One would expect the HRs for disease history (No, 1.28 and Yes, 1.30) to fall on either side of the overall HR (1.27), but they don't: Is this Simpson's paradox or a mistake or something else? Please verify and clarify.

Reviewer #1 (Recommendations for the authors):

Thank you for the opportunity to review this manuscript.

– The title of the paper suggests the risk of heart disease is associated with breast cancer itself, but the content of the manuscript and conclusions emphasize the risk based upon treatment effects. I would consider changing the title to reflect the risk of breast cancer therapy.

– For Table 1: In addition to Charlson Comorbidity Index (CCI score), would also include CVD risk factors (HTN, HLD, DM2, BMI, tobacco smoking) to better understand patients' baseline cardiovascular risk, particularly as these risk factors were used in the risk models, and independent of cancer treatment are known to be associated with risk of arrhythmias, ischemic heart disease, and congestive heart failure.

– For Table 2: Would add the word "Ratio" ie "Hazard ratio for heart diseases" in the title.

– The finding of no significant increased risk of ischemic heart disease after left breast radiation is quite interesting. This finding would be more powerful and better supported if estimates of mean heart dose of radiation or even total cumulative radiation dose administered was included (which may not be possible from the available registry data).

– Regarding hypotheses made in the Discussion section: the authors appropriately provide citations regarding early increased risk of ischemic heart disease due to emotional distress, however there are several other factors that could potentially increase this risk that warrant consideration: surgery for breast cancer (98.9% of patients in this cohort) typically takes place within the first year of diagnosis and may increase risk of arrhythmia, ischemic event; patients with cancer are at increased risk of arterial thromboembolism (ATE) which includes myocardial infarction 150 days prior to cancer diagnosis and this risk appears to attenuate 1 year after diagnosis. (Navi, B. B., et al., (2017). "Risk of Arterial Thromboembolism in Patients With Cancer." J Am Coll Cardiol 70(8): 926-938) (Navi, B. B., et al., (2019). "Arterial thromboembolic events preceding the diagnosis of cancer in older persons." Blood 133(8): 781-789.)

– While the results are interesting and hypothesis generating, the patient population is overall young and healthy (median age 59, majority CCI = 0) therefore would be cautious to recommend extrapolating results to guide individual therapy decisions in clinical practice.

Reviewer #3 (Recommendations for the authors):

As an alternative to a four-category radiotherapy variable, which as the authors note requires assuming that bilateral radiotherapy is equivalent to leftsided radiotherapy, it would seem sensible to create two separate binary variables (left, y vs. no and right, y vs. no).

Can the authors double check rows two and three of the first column of Table 2? Intuitively, I would expect the HRs for disease history (No, 1.28 and Yes, 1.30) to fall on either side of the overall HR (1.27), but they don't. Is this Simpsons paradox or a mistake or something else?
