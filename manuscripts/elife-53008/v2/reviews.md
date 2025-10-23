# Peer review - Round 1

Editors:
- C Daniela Robles-Espinoza, International Laboratory for Human Genome Research Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53008.sa1](https://doi.org/10.7554/eLife.53008.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We believe this work is highly valuable for the scientific community, especially the melanoma community, because it investigates and sheds light into the relationship between a tumour with true lymphocytic activation, and therefore with better prognosis, and the typical "brisk/non-brisk" morphological classification still in use by many research groups around the world. We also find these studies into the spatial relationship between cell types highly valuable, especially the confirmatory finding that brisk tumours have cytotoxic lymphocytes and melanoma cells in closer contact than non-brisk cases. This study makes a compelling case for considering both T cell activation and morphology when assessing patient prognosis, and therefore are delighted to accept it for publication.

Decision letter after peer review:

Thank you for submitting your article "Functional heterogeneity of lymphocytic patterns in primary melanoma dissected through single-cell multiplexing" for consideration by eLife. Your article has been reviewed by four peer reviewers, including C Daniela Robles-Espinoza as the Reviewing Editor and Reviewer #4, and the evaluation has been overseen by Tadatsugu Taniguchi as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript titled "Functional heterogeneity of lymphocytic patterns in primary melanoma dissected through single-cell multiplexing", Bosisio and collaborators describe a powerful method to infer the functional status of immune cells in melanoma FFPE slides through multiplex imaging and single-cell deconvolution. They analyzed 60 cores from 29 patients for a total of 179,304 identified cells forming 19 clusters of 47 functional cell populations. To put this into perspective, most single-cell sequencing studies consist of a maximum of tens of thousands and not hundreds of thousands of cells, so this represents a deep single-cell expression data set that can be used to address many interesting questions. In particular, the authors attempted to better refine the currently broad classification that is used to determine whether a tumor has an ongoing inflammatory reaction that would suggest the patient will respond well to immunotherapy.

Essential revisions:

1) In general, confounders and the role of heterogeneity are not well controlled in most of the analyses. It seems that it is rather a difficult task to score TIL status and functional states from any small piece of biopsy and assume it will accurately represent the whole tumor, or even multiple tumors a patient may have.a) Please clarify: How did the authors combine scores from multiple cores, how did they control for heterogenous core classifications, since the read-out is patient-specific (i.e., OS)? Treatments are not mentioned, but obviously if these tumors were collected within the last 8 years, these patients may have divergent treatment histories. How were these factored into the model, as well as age, gender, tumor location (especially with the potential confounding of immune cells in lymph-node metastases), etc?b) Reviewers suggest reproducing the survival analysis from Figure 2E in another dataset (could be one previously published and posted online) and see whether the conclusions replicate. It could perhaps be done with bulk RNA sequencing data, using deconvolution methods to search for the presence of the same markers.c) Related with the previous point, reviewers suggest looking more closely at the results of other single-cell melanoma studies that have investigated correlations with exhaustion (e.g., Kumar et al., 2018 doi.org/10.1016/j.celrep.2018.10.047) and putting in context results of the present study with those already published.

2) Neighbourhood analysis. The reviewers agree that this is one of the most interesting results in this manuscript as it adds information that other non-spatial single-cell-based are not able to provide.a) Please place relevant cell-cell interactions (e.g. melanoma:T-cell) in the main text instead of the supplementary materials, and mention panels C and D in the Results section.b) Please improve Figure quality by increasing font size and adding legends, and clarify why some cell types (e.g., TIM3 + cDC2) are not shown in Figure 4C.c) Please discuss how the fact that the "active" and "brisk" plots are nearly identical fits with the paper's main conclusion that the "brisk" state consists of both active and exhausted.

3) It is unclear what the qPCR and proteomics experiments add to the results. Please clarify how the fact that 50% of the brisk and 43% of the non-brisk tumours can be classified as "active" fits with the neighbourhood analysis, particularly point 2C above.

4) Please add more explanation in this manuscript about what the MILAN technique entails, given that it does not seem to be in widespread use.

5) Principal component analyses. Please clarify the following points:a) Are the PCAs in Figure 2 created with all markers or just the select markers shown in Figure 2?b) For the classification of cells into the "active" and "exhausted" states, were all cells from all patients put together in the analysis, and if so, did PC1 divide cells by patient? What variability did the axis of maximum variation capture?

6) Correlation between core status and tumour regression. Please answer the following questions:a) How is a late regression area defined?b) Do the authors think the reported correlation may have arisen by chance, given that No Regression vs Early regression (comparison of the most different states) did not show any differences? Were the differences that were detected in the expected direction (i.e. early regressed tumours had a higher activation status than late regressed tumours)?

7) The reviewers agreed that it is necessary to add a section in the discussion regarding how the authors' results compare and fit with previous publications, in particular Sade-Feldman et al., 2018; Ayers et al., 2017; Prat et al., 2017; Riaz et al., 2017 and Tirosh et al., 2017.

8) Regarding statistics in general. The reviewers suggest displaying p-values in all Figures where there have been statistical tests and justify the use of the chosen tests. (For example, reviewers mention that authors could have used logistic regression to analyze the relationship between their variables, as well as ANOVA instead of t-tests with Holm's or FDR corrections). Clarifications about when multi-testing correction was applied (or not) should be added.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Functional heterogeneity of lymphocytic patterns in primary melanoma dissected through single-cell multiplexing" for further consideration by eLife. Your revised article has been evaluated by Tadatsugu Taniguchi (Senior Editor) and a Reviewing Editor.

The reviewers agree that the manuscript has been substantially improved but there are some minor remaining issues that need to be addressed before acceptance, as outlined below:

Could you please add some discussion on the following:

1) To assign an activation state to patients, the authors didn't combine states per core but per cell – Doesn't this depend on the number of cells that were successfully assessed? Reviewers would like to see an acknowledgment that perhaps sampling more/less cells per patient could have an influence in this classification.

2) Can the authors please expand a little on the logic behind classifying "non-brisk with exhaustion" as poor prognosis one whereas "brisk with exhaustion" is classified as good prognosis? How do the authors define the relationship between these two different classification methods? Is morphology then also important to take into account even when the single cell status is being considered? (And, was this the comparison that got the better p-value? Were the other possibilities (e.g. classifying brisk with exhaustion as poor prognosis) also considered?

The reviewers would also like to see clarification for one of the points in the rebuttal letter, please. One of them wrote, "The two explanations for categorising the "transition" patients into active or exhausted (p values 0.053 or 0.079) sound exactly the same to me. What is different? (However, I do not think this is mentioned in the main text)."
