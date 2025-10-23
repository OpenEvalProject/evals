# Peer review - Round 1

Editors:
- Miles P Davenport, https://ror.org/03r8z3t63 University of New South Wales Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77943.sa0](https://doi.org/10.7554/eLife.77943.sa0)

This manuscript uses a multi-omics approach to investigate how early immune markers in blood predict subsequent clinical outcome and immune responses. The study uses samples from a previous trial and identifies several immune markers associated with later clinical and immunological outcomes in this cohort. An important next step will be to validate this in other cohorts and test the utility of this in a clinical setting.


---

# Peer review - Round 1

Editors:
- Miles P Davenport, https://ror.org/03r8z3t63 University of New South Wales Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77943.sa1](https://doi.org/10.7554/eLife.77943.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Early immune responses have long-term associations with clinical, virologic, and immunologic outcomes in patients with COVID-19" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Miles Davenport as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

One concern is that the two groups in a clinical trial with an immunomodulatory drug were combined in this analysis. The authors take for granted that the administration of Peg-IFN λ does not modify the course of the disease and therefore that treated and untreated individuals can be analyzed together. This is at odds with other randomized studies, that have shown antiviral and clinical effect of IFN-based therapy. In particular, Peg-λ accelerated viral decline in outpatients and prevented clinical deterioration in a study performed in a similar setting using the same dose than here (Feld et al., Lancet Resp Med 2021). Other positive results in early patients were found with IFN-β (Monk et al., Lancet Resp Med 2020). Even if the administration of IFN in this study had no clinical or virological benefits, it could nonetheless alter the kinetics of ISG. The authors claim it is not the case, but it is difficult to assess it based on the figures shown, using PCA.

Although PegIFN was not associated with significant changes in clinical outcomes, the lack of overall clinical responses was likely due to a mix of responders and non-responders. Were there variables at baseline identified by computational analysis which could predict responses to IFN? Given these difficulties, we would encourage the authors to do a separate analysis, which is a revision.

If the authors decide to continue with this revision we would also encourage them to address the following comments:

1. Add essential information on the clinical trial should be included in the manuscript to suggest whether research findings mostly apply to the β, δ or omicron era. All in all, since this study focuses on the host, findings should be generalizable irrespective of the pathogen.

2. It is questionable whether a strong claim can be made on disease progression, since only 8 patients were hospitalized in this study. In addition, it should be clarified when these patients progressed. Page 10, it is said that the median time to progression is 2 days, so in fact, the data collected at day 0 and 5 are very close, or even perhaps posterior to hospitalization in some cases, making it difficult to claim that it can be used for prediction. More generally data used are up to 14 days post symptom onset, while the median time to hospitalization in these populations is roughly ~8 days. This makes it here as well difficult to really argue that the model has a "predictive" value to anticipate disease progression.

3. If data used in the study are close to hospitalization, then this really diminishes the novelty of the findings, as many studies have already reported an association between these markers and disease severity (see also Young et al., Viral Dynamics and Immune Correlates of Coronavirus Disease 2019 (COVID-19) Severity, CID 2021).

4. The definition of disease progression seems to differ from the original study "Overall, 17 participants had evidence of disease progression, defined as hospitalization, presentation to the emergency department, or worsening cough or shortness of breath defined as an increase in severity of two points or more on a five-point scale"? Please clarify what is your endpoint and why, if relevant, it differs from the original study.

5. Can you clarify how viral shedding was analyzed? The fact that viral load is analyzed with a different metrics than other proteins when looking at predictors of disease progression is puzzling. Figure S5 does not seem to be convincing, which relies on AUC of viral load calculated in patients with high heterogeneity in their symptom onset. Please use the same approach for viral load than what was used for IP-10 in order to demonstrate that IP-10 is a better predictor of disease progression than viral load.

6. Regarding prediction, it is really unclear how the model using demographics was built. It is obvious than many other factors than age and sex are highly predictive of disease progression.

7. If you want these results to be useful for the clinical community then the model used in figure 7 should be explicitly given so that anyone can use these results to build score on its own population.

8. Improve discussion on IFN-λ and propose better graphs to justify the absence of effect of treatment. It would be more helpful to provide simple graphs, such as boxplots of the changes in the 7-10 relevant markers between day 0 and day 5 in treated and untreated individuals (along with p-values), so that the lack of difference can be easily visualized.

9. To build a better model of demographics, consider exploring more covariates. For instance, evaluate models including covariates that are significant in univariate analysis and that have a >10% prevalence (hypertension, diabetes, age>55…).
