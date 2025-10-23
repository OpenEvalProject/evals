# Peer review - Round 1

Editors:
- Emery N Brown, Massachusetts Institute of Technology , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08935.015](https://doi.org/10.7554/eLife.08935.015)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Human blindsight is mediated by an intact geniculo-extrastriate pathway” for peer review at eLife. Your submission has been favorably evaluated by Eve Marder (Senior Editor) and two reviewers, one of whom is a member of our Board of Reviewing Editors.

The authors performed diffusion weighted MRI imaging in 17 patients with cortical blindness and 9 matched controls. Patients were categorized as displaying blindsight (PB, N = 12) or not (PN, N = 5) based on above chance detection of Gabor patches presented in their affected visual field. The results showed that ipsilesional LGN-hMT + tracts could be reconstructed in all subjects, except 1 PN patient. Investigations of the microstructure of the tract by means of FA and MD revealed normal values for the PBs and abnormal values for the PNs. In addition, the authors investigated 2 alternative projections, i.e. ipsilesional SC-hMT+ and transcallosal hMT+. These tracts could not be identified in all PB patients and all controls, whereas they were present in some PN patients. The authors interpret the results as evidence that an intact LGN-hMT + pathway is both a necessary and sufficient condition for blindsight.

Essential Revisions:

Interpretation:

1) Considering the limited number of tracts investigated (i.e. 3), any claims on the “crucial”, “necessary” or “sufficient” nature of the results, seems a bit over-ambitious. A more provisional interpretation would be more in line with the a priori constraints that the authors choose to apply in the analysis.

2) Can the authors provide any evidence that the LGN-hMT + connectivity results are not explained by grey matter volume of the hMT+? In other words, could the connectivity results secondary to structural integrity of the grey matter of hMT+?

3) There is an additional alternative tract that the authors do not investigate, namely a pulvinar-hMT + tract (e.g. Leh et al., 2008; Wong et al., 2009). Can the authors please comment and address this.

Study Execution and Statistical Analysis:

1) Would the authors say a little more about how the controls were chosen? What criteria were they matched on relative to the blindsight patients? The definition of blindsight depends only on the responds at the 100% contrast level. If this was the plan prospectively in the design if the study then what was the purpose of testing at the other 4 contrast levels? How many correct responses did the patient have to have to be considered blindsight positive?

2) The reviewers did not find a formal statistical assessment showing that the performance difference between the two groups was statistically significant or that the performance in the blindsight positive group was significantly greater than chance, whereas the blindsight negative group was at chance. Moreover, we did not see an assessment that showed that performance between the blindsight positive and the control group was similar. We suspect that the differences between the two groups are even stronger than the authors indicate. It would be more efficient to analyze the data as a logistic regression within subject in which detection performance is measured as a function of contrast. That is use the model Log[(1-p)/p)] = a + b*percent contrast which can easily be fit by using standard statistical software.

For each subject all of the trials go into estimating just two parameters per subject which is far more efficient than estimating response probabilities at different contrast levels, assuming that performance at each contrast level within a subject is unrelated. At a given contrast level for each subject in the blindsight positive group, if the lower bound of the 95% confidence bound is above 0.5 then we can infer that that subject's performance is greater than chance. Similarly, for each subject in the blindsight negative group the 95% confidence intervals at each contrast level should include 0.5.

There should be at least one other formal comparison. There should be an assessment that shows that the performances of the blindsight positive group and the controls are indistinguishable. These are easy to do if a Bayesian hierarchical analysis is used to pool information across the two groups. It suffices to show that confidence interval (posterior credibility intervals) for the difference between the population logistic curves for the two groups include zero.

3) A lot of quantitative comparisons are reported throughout the Results. However, formal statistical testing only appears the subsections “Different microstructure in the geniculate-hMT + tract between blindsight positive and negative patients” (paragraph five),“Superior colliculus tracts” (paragraph three), and “Lesion size and location” (paragraph one). Moreover, these tests are not described in the Methods. Can the authors give a bit better discussion in the Methods about what statistical paradigm they are using to make their inferences? Moreover, formal testing of group differences in both macro- and microstructural parameters of the 3 (or 4 if the suggested one is included) projections of interest could strengthen the claims of the authors, as well as correlation analyses between behavioral and imaging data. This is one of the largest collections of V1 lesion patients. Therefore the data should be analyzed in greater detail.
