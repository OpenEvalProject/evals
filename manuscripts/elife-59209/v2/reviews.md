# Peer review - Round 1

Editors:
- Frank L van de Veerdonk, Radboud University Medical Center Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59209.sa1](https://doi.org/10.7554/eLife.59209.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper analyzes a large EHR-based dataset of coagulation tests in COVID-19 patients to obtain an understanding of the kinetics of COVID-19 associated coagulopathy. By using machine learning to extract patterns data are provided which support that the majority of thrombotic events in COVID-19 patients are not the result of a DIC-like consumptive coagulopathy, and that this only occurs in a small subset.

Decision letter after peer review:

Thank you for submitting your article "Longitudinal laboratory testing tied to PCR diagnostics in COVID-19 patients reveals temporal evolution of coagulopathy" for consideration by eLife. Your article has been reviewed by four peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jos van der Meer as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Coen Maas (Reviewer #1); Jinbo Chen (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

The authors analyze a large EHR-based dataset of coagulation tests in COVID-19 patients to obtain an understanding of the kinetics of COVID-19 associated coagulopathy. It is a clear approach and the data are important for the clinics. They used machine learning to extract patterns. Overall the conclusions were drawn in many directions. Nonetheless, the paper asks a potentially important question and is adequately written and presented. The data support that the majority of thrombotic events in COVID-19 patients are not the result of a DIC-like consumptive coagulopathy, this only occurs in a small subset. This should also be the focus of the Discussion.

Essential revisions:

Patient characteristics:

– Please clinically define "pre-existing coagulopathies".

– It is a unclear what the comparator cohort adds: In part it is not clear who these patients are. Perhaps the controls should be age/sex-matched patients with other causes of hypoxemic respiratory failure/pneumonia? Or different COVID-19 disease severity subgroups? Otherwise what are we inferring from comparing these two groups?

– Ascertained rates of venous thromboembolism are much lower than what others have observed (e.g., Helms ICM 2020, Middeldorp pre-prints, etc.). Could this relate to ascertainment bias in this cohort? Perhaps a push not to perform diagnostic imaging studies lead to lower objective identification of venous thromboembolism than has been generally described in COVID-19?

– Patients are identified as COVID-19 positive or negative based on PCR testing. Actually, using the PCR test a positive/negative infection by SARS-CoV-2 is assessed; COVID-19 is the disease that can follow upon infection. This distinction should be made clear, as not all patients tested positive for SARS-CoV-2 infection necessarily develop COVID-19. What was the guideline followed for PCR-testing: displaying COVID-19 symptoms/ contact with infected persons/ other? This should also be explained and included.

– Introduction: "… straddling the date of the PCR test.…" Do the authors refer to the first PCR test here, as it is mentioned that multiple PCR tests may have been performed? Please include a definition.

Analysis:

– The analysis was restricted to patients who had serial (>/= 3) tests done. This could have led to a survival bias which should be acknowledged.

– This restriction also led to the exclusion of the vast majority of the cohort: 1,192 -> 181 COVID-19pos patients. Why was there such a strong emphasis on longitudinal markers?

– The potential significance of these longitudinal trends are assessed with these tests as far as I can understand, which both only looks to see whether mean/median change was different between the groups, but moreover does not allow for adjustment. Why not use multilevel regression mixture models, longitudinal regression, etc?

– One of the three covariates used in the regularized logistic regression model to predict the likelihood of a positive infection (subsection “Propensity score matching to select the final COVIDneg cohort”) is anticoagulant/antiplatelet medication use. Is this covariate positively or negatively correlated to infection and what is the rationale for this? Table 1 comprises more details; however, these add to further confusion. The Table 1 legend states "anticoagulant/antiplatelet use within 30 days/1 year of PCR testing date" i.e. after the PCR test, while the table itself mentions "medication use in the preceding 30 days/1yr", so before the PCR test. Please clarify and adapt.

Figures:

– Figure 2A: Why are no data points provided for the -30 to 0 days of the COVID negative patients while these data are shown in Figure 2B and E?

– The same question as above but then for the APTT and D-dimer data in Figure 2 vs. Figure 3 and magnesium in Figure 1 vs. Figure 3. I guess the cohorts are different between the two figures, maybe this should be stated in the figure legends.

– Figure 3: we agree with the authors that the fibrinogen decline and platelet increase in COVID positive patients is re-emphasized in this manner. Also the increase in magnesium and decrease in alkaline phosphatase seem to stand out. Could the authors comment on this?

– Could the authors comment on the number of thrombotic events that were radiographically-confirmed?

– Figure 5: for the individual patients could the authors comment on the heparin therapy with regard to the source of heparin (LMWH vs. UFH) and dosing (prophylactic vs. therapeutic)?

– Figure 6 is very hard to understand; please find another way to graphically display the findings in a clear manner.

Specific statistical comments:

1) Cohort identification and description. (a) For the 1.3 million lab tests on 194 assays over the 60-day window: provide the mean/range of number of tests separately for positive and negative patients, and also provide the mean/range of the number of tests for pre- vs. post-index "0" date; (b) For positive patients, the proportion of those whose PCR positive test is the first test in the 60-day window; (c) If at all possible, COVID-19 related info at the first PCR test for all patients; (4) If possible, reasons for hospitalizations at the day=0;

2) It is not clear why it is important to assess lab tests in relation to diagnosis. For studying association between lab tests with diagnosis, ideally, the positive cases should use the "time of infection" as time zero which of course is intractable. But before variation in time from infection to diagnosis by PCR tests, the relevance of test results for diagnosis is unclear. Further, because of the propensity score matching, the cohort may not be suitable for assess the diagnosis: if some matching variables are associated with any of the test results, matching will artificially deflate the association. We therefore suggest the focus of this paper on prognosis only. The Abstract indeed focused on the prognosis, but diagnosis was mentioned multiple times in the manuscript.

3) BERT method: The accuracy of BERT was established in an unpublished manuscript developed by the same research group. What is the proportion of patients who were classified as "Maybe", "Yes" AND "No"? It is helpful if chart review is performed on 100, say, patients, to validate this algorithm in the study context;

4) Tables 3 and 4 indicate that the endpoints were significantly enriched for positive cases who had longitudinal data. But it is possible that patients received more tests because of indications of more negative outcomes. As a result, patients with longitudinal lab tests are representative of all positive patients as indicated by the enrichment. This is an important weakness of the study as this may be a source of bias, making the study results not generalizable. It is important to provide additional information on the comparing characteristics of patients with and without longitudinal tests. It may be worthwhile to provide information on reasons of repeating tests for negative patients.
