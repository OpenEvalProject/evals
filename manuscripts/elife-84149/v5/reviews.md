# Peer review - Round 1

Editors:
- Stacey D Finley, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84149.sa0](https://doi.org/10.7554/eLife.84149.sa0)

This is an important study that investigates the impact of tyrosine kinase inhibitors (TKIs) in chronic myeloid leukemia. Through a combination of preclinical in vivo measurements, clinical data, and computational modeling, the authors present solid evidence regarding the heterogeneous effects of TKIs in patients and how the response to treatment may be improved. This study is of interest to those working in the fields of mathematical oncology and cancer biology.


---

# Peer review - Round 1

Editors:
- Stacey D Finley, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84149.sa1](https://doi.org/10.7554/eLife.84149.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Predictive nonlinear modeling of malignant myelopoiesis and tyrosine kinase inhibitor therapy" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Jesse A Sharp (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Account for intrinsic differences between leukemic and normal cells. This aspect of the manuscript is poorly justified and weakens the study.

Reviewer #1 (Recommendations for the authors):

A) Several assumptions and hypotheses require a more detailed justification or a more careful discussion, e.g.,

– "For simplicity, we assumed the only difference between the two lineages is a decrease in the feedback strength for leukemic HSC (HSC L ; S L ), as indicated by p 0L in the schematic in Figure 4A." This choice requires a more detailed justification. Why are potential differences in other parameters not considered?

– "TKI treatment was initiated at three different times to achieve varying leukemic stem cell load (6, 18, and 36 months) and was simulated by introducing a death rate of HSC L and MPP L proportional to their proliferation rates, with the HSC L proliferation rate lower than that of normal HSC (Jørgensen et al., 2006)" Several researchers in the field held the strong opinion that TKI do not affect the CML stem cell population in humans (Corbin et al., cited by the authors). Also, the work of Reynaud (cited by the authors) discusses this issue. Please provide a more detailed discussion of the assumption that TKI kills leukemic stem cells.

– Along the lines of point (2) above: "The model further suggests that a key predictor of refractory response to TKI treatment is an increased probability of self-renewal of normal hematopoietic stem cells." and related statements: Please rephrase the statements more carefully pointing out the meaning of the parameter p_{0,max} and the model assumptions underlying this conclusion.

– Along the lines of point (2) above: To support the conclusion that normal and not leukemic stem cell self-renewal matters for TKI response, please consider analyzing a version of the model allowing for different p_{0,max} values for HSC and HSCL. In such a model: What is the predictor of poor TKI response, the p_{0,max} for HSC or the p_{0,max} for HSCL?

– "This is consistent with clinical data that suggest that CML patients with pre-existing mutations in genes such as TET2 and ASXL1, which are known to increase stem cell self-renewal (Steensma, 2018), tend to have inferior outcomes under TKI therapy (Kim et al., 2017; Marum et al., 2017)." In my opinion, the provided references argue for the concept that a simultaneous increase of self-renewal in both leukemic and normal stem cells leads to a low TKI efficacy. The CHIP mutations analyzed in the cited studies most probably affect normal AND leukemic stem cells. Marum et al. study germ-line mutations that naturally affect normal and leukemic cells at the same time.

– "Although our data were derived from mice, we hypothesize that similar cell-cell

signaling occurs in humans." This hypothesis should be discussed in more detail. What are the potential differences between mice and humans that could lead to problems when applying the proposed model to patients?

– "only those with sufficiently large feedforward gains on the MPP division rate (γ 5 >0.01)" Please justify the cutoff of 0.01, how sensitive are the presented results with respect to this choice?

– "We used one eligible parameter set (see Supplemental Tables S4, S5), which is capable of characterizing the normal state of our simplified model of the hematopoietic system." Do other parameter sets lead to comparable results?

B) Several passages of the main text are difficult to follow since important arguments have been moved to the Methods Section at the very end or to the Supplement. Some conclusions merit a more detailed explanation. E.g.

– "Taking all these results into consideration, we arrive at the feedback-feedforward model shown in Figure 2F." This statement should be explained in more detail in the main text. Have the authors performed a systematic search of the literature to search for evidence of such mechanisms, can they name potential factors mediating them?

– "These time points and the number of mice analyzed at each time point were informed by a Bayesian hierarchical framework for optimal experimental design of mathematical models of hematopoiesis (Lomeli et al., 2021)"

Please provide details.

Reviewer #2 (Recommendations for the authors):

Very nicely done work and I appreciate the efforts to validate the model and parameter estimates using sophisticated computational techniques as well as animal data.

A well-written manuscript and the right amount of detail.

Reviewer #3 (Recommendations for the authors):

I commend the authors on a well-written manuscript with important results and clear methodology.

Here are some recommendations which I hope may improve the manuscript. I will preface these recommendations by noting that I have limited experience in a laboratory setting and as such do not have the expertise required to make any comments about the experimental component of this work.

– The authors could provide a brief justification for a grid search as the mechanism for identifying biologically relevant parameters.

– In modelling CML development, there is an assumption that the only difference between normal and leukemic cell lineages is the feedback strength for leukemic HSC self-renewal. Could the validity of this assumption be explored, perhaps via supporting evidence in the literature, or through briefly considering the sensitivity of the model predictions to this assumption?

– In Figure 1, concerning the process of identifying candidate model classes, I am not sure whether it is not present or simply hard to make out in the figure, but it appears to me that the downregulation of q_1 by TD_m marked in blue in Figure 1C is not a possible a factor in any of the four candidate model classes identified through design space analysis (Figure 1B). This is in contrast to the bottom left model of Figure 1B, where the downregulation of p_0 by p (also marked with blue in Figure 1C) is visible as a possibility.
