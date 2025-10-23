# Peer review - Round 1

Editors:
- Muireann Irish, https://ror.org/0384j8v12 University of Sydney Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83970.sa0](https://doi.org/10.7554/eLife.83970.sa0)

Sanz Perl and colleagues provide important insights regarding the application of computational brain models from neurodegenerative diseases to evaluate brain stimulation protocols in silico. Solid evidence is provided for the disease-specificity of the framework, however, the real-world impact of such stimulation protocols to alleviate psychiatric and neurological symptoms remains to be evaluated.


---

# Peer review - Round 1

Editors:
- Muireann Irish, https://ror.org/0384j8v12 University of Sydney Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83970.sa1](https://doi.org/10.7554/eLife.83970.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Model-based whole-brain perturbational landscape of neurodegenerative diseases" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jeannie Chin as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Jordi A Matias-Guiu (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. In general, I think the methodology (especially the VAE) should be explained more substantially in the Results, to make the paper easier to follow in the order in which it is presented.

2. Further information is required from participants. For example, age, years of education, years since symptom onset, some cognitive tests, etc. A table reporting this information may be of interest. Further, patients and controls are not "matched", because there is no matching in this study (e.g. 1:1). This sentence that participants are matched in terms of age should be amended.

3. "All patients with bvFTD were in the mild stage of the disease and presented frontal compromise". What is the meaning of "frontal compromise"? Frontal syndrome or frontal atrophy in MRI?

4. It seems that AD did not have amyloid or tau biomarkers. This should be added as a limitation.

5. I wonder if the authors could elaborate on why wave stimulation simulates tACS and synch/noise resembles tDCS? That is stated, but not actually explained, in the manuscript.

6. It would be helpful to assess the robustness of results against alternative atlases.

7. The claim of disease-specificity is weakened by the use of a combined atrophy map to fit both conditions: it would be important to show the results of using the separate AD and FTD maps to fit AD and FTD, respectively (and the reverse): this would be a strong test for specificity, and it would bolster the case for disease-specific applications.

8. How does distance from controls in the 2D latent space match with GOF to the controls' FC? Are the two measures correlated? This would be important to identify how much the VAE really adds to the workflow.

9. Figure 2: I apologise if I missed this, but what are the effect sizes being computed against?

10. Regional results: I appreciate the authors' choice to not use p-values due to their limited meaning in the context of computational models that can be overpowered. However, presumably, there is some likelihood of obtaining effect sizes greater than a given threshold, just by chance – and this should be corrected for, akin to the traditional correction for multiple comparisons.

11. For Figure 5, it would be very helpful to show, not just the single points, but rather the area occupied by each condition, to facilitate the assessment of whether a given stimulation is successful, or simply falls more or less short of the target.

12. It would be a powerful demonstration if any of the results could be related to behavioural aspects, to show that the results are not confined to neuroimaging alone – after all, behavioural effects are the goal for actual brain stimulation.

13. Although the paper is mainly based on bvFTD, in terms of non-invasive brain stimulation, there are some references that may be of interest to support the rationale of the study. For instance, the works by Tsapkini (10.1007/s10072-019-04229-z, 10.1016/j.bandl.2019.104707, 10.1016/j.trci.2018.08.002) or about personalized TMS in PPA (10.3233/JAD-210566).
