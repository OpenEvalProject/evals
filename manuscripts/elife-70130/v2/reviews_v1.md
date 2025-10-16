# Peer review - Round 1

Editors:
- Caigang Liu, Shengjing Hospital of China Medical University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70130.sa0](https://doi.org/10.7554/eLife.70130.sa0)

A mathematical model was established for predicting immunotherapy efficacy in this work. With three convenient available clinical parameters, the model has exhibited considerable predictive capacity with stable performance across several tumor types. It may show great promise in selecting participants for prospective trials and guiding targeted application of immunotherapy in cancer patients.


---

# Peer review - Round 1

Editors:
- Caigang Liu, Shengjing Hospital of China Medical University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70130.sa1](https://doi.org/10.7554/eLife.70130.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Early prediction of clinical response to checkpoint inhibitor therapy in human solid tumors through mathematical modeling" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Mone Zaidi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Multiple parameters could reflect treatment efficacy of immunotherapy to cancers while three specific parameters were included in this model, the selection process and reasons for choosing these three parameters need to be described in detail, the definition of the three parameters seems to in discordant with clinical setting which requires further explanation.

2) As a heterogenous entity, different types of cancer possess distinct features, rationality to employ this model as one fit-in-all with a relatively small training cohort requires additional discussion after validated in a large-scale validation cohort.

3) As a novel model evaluation of the sensitivity and accuracy needs to be addressed, and comparison of this model with current applied parameters for predicting immunotherapy treatment efficacy requires to be supplemented.

Reviewer #1 (Recommendations for the authors):

The authors demonstrate a translational mathematical model dependent on three key parameters for describing efficacy of checkpoint inhibitors in human cancer. This paper describes some very interesting work. However, it remains questions that need to be addressed as follows:

1. The authors need present why they select these three parameters for describing efficacy of checkpoint inhibitors in human cancer. How about other factors?

2. How can the authors make sure that this model is suitable for all human cancer? Is the clinical tumor response dataset (n = 189 patients) enough?

3. What is the accuracy of the model?

4. I think there is no scope of this work shown in this "Introduction part".

5. Please identify the innovation point in the paper.

Reviewer #2 (Recommendations for the authors):

1. Several claims would need to be revised or toned down throughout the manuscript that describe the mathematical model as mechanistic and translatable. For example,

a. 'senescence markers (10) such as CD27, Tim‐3, CD57, and/or T‐cell receptor (TCR) repertoires (11)'. Only CD57 is a senescence marker among the listed proteins.

b. 'Our method may be implemented directly into clinical practice, as it relies on standard‐of‐care imaging and pathology' in Line 79,

c. 'the merit of this approach will rely on its future ability to reliably predict early individual patient response with the goal of improving personalized cancer care.'

d. Line 204-205: 'the model may be adaptable to other types of checkpoint inhibitors affecting the CTLA‐4 pathway'. Studies have described the effect of aCTLA4 therapies to be mediated in peripheral lymphoid organs rather than the tumour microenvironment. Therefore, the model that considers chemotaxis and intratumoural Ab activity will likely not apply to aCTLA4 therapies.

2. In addition to the assumptions described in the text, are the following assumptions implied:

a. The parameters µ and λ are considered constant over time, which implies that the ratio of cancer cells and immune infiltration remains the same over the treatment course.

b. Every cancer cell is assumed to have the same proliferation rate.

c. Each tumour cell has the same likelihood to be recognized by the immune system.

3. The cutoff used to split the µ and λ parameters and compare to responders and non-responders was done 'by maximizing the Youden's J statistic revealed cutoff thresholds where sensitivity'; A correction method needs to be applied to account for multiple testing correction. How does the result compare to using the median values and quantiles? How do changes in cutoff affect the Roc curve?

4. The manuscript text refers to Table S1 and supplementary figures, but supplementary information wasn't submitted for review. Unfortunately, the work on model sensitivity was not provided.

5. The work builds on a recent publication by the authors.

a. The manuscript could benefit from more information on the model, even if described previously elsewhere. For example, parameters in the methods and in Figure 1 are introduced but not described.

b. Importantly, the novelty of this study compared to the previous publication should be highlighted. The comparison with clinical and histology data appears to be the main novelty, which is why demonstrating the correlation with clinical data per patient, would be crucial. It is not clear why the calibration and validation dataset are different from the previous study. How do the estimated parameters differ?

6. The sensitivity and specificity of the λ parameter are low. Does it have an additive predictive value to the µ parameter?

7. How does the predictive value of the parameters compare to previously reported biomarkers of response such as TMB, % PDL1+ cells, T cell count? A predictive model controlling for age, stage, etc. should be implemented to account for these confounders.

8. How does the predictive value of the parameters change when the validation cohort is swapped with one of the calibration cohorts? How robust are the parameters to cross-validation? How does the predictive classification change with a different cancer type?

9. There is a lack of robust predictors of immunotherapy response due to a large number of confounder, such as heterogeneity at molecular and cellular level, immune escape, immunosenescence, etc. How does the model overcome this?

10. Figure 4 could be more clear and informative.

11. The published cohort in JITC has 72 patients but only 64 patients were included in the validation cohort, why is that so?

12. Which other pathological parameters correlate with λ and µwhen measured per patient, not per response group?

Reviewer #3 (Recommendations for the authors):

1) In the Figure 2, it would be helpful to show different cancer types as different panel.

2) An additional figure is favorable to show whether those key parameters were cancer type-specific or the antibody drugs.
