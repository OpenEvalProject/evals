# Peer review - Round 1

Editors:
- Chris I Baker, https://ror.org/04xeg9z08 National Institute of Mental Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85082.sa0](https://doi.org/10.7554/eLife.85082.sa0)

This is a rigorous and compelling extension of previous normative modeling work. The current study demonstrates that normative models incorporating lifespan trajectories of structural and functional connectivity provide a strong basis for brain imaging studies across a range of tasks including, univariate group difference assessment, classification, and building regression models. The work is important, rigorous and a valuable contribution to the field.


---

# Peer review - Round 1

Editors:
- Chris I Baker, https://ror.org/04xeg9z08 National Institute of Mental Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85082.sa1](https://doi.org/10.7554/eLife.85082.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Evidence for Embracing Normative Modeling" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Todd Constable (Reviewer #1); Oscar Esteban (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While the reviewers are convinced of the potential importance of this extension of your earlier work, they raise some comments about the clarity of aspects of the. In your revision, it is important for you to consider each of these issues and revise the manuscript as appropriate.

Reviewer #1 (Recommendations for the authors):

This is a clearly written and scientifically rigorous presentation of the utility of normative modeling with structural and functional MR data. I have no suggestions for improving the work and find it acceptable for publication in its current form.

Reviewer #2 (Recommendations for the authors):

Please clarify: Are all normative models (i.e. across all modalities) based on the same set of covariates?

What exactly is the input to models in the benchmarking tasks? I.e. is it a single value (deviation score) per individual for the normative model but the full functional network for the raw data model?

As mentioned in the manuscript, the null findings for raw data models in the group difference task are surprising. Could you elaborate on the difference between cited work that has found significant effects? (E.g. differences in sample sizes, differences in preprocessing steps, did previous work not include multiple comparisons corrections?)

The choice of a linear kernel for the SVM classification task is not clear to me. Since the input vectors are low dimensional, would a non-linear (e.g. rbf) kernel not perform better?

Is there any expected reason why classification in the case of the raw data models would work on the functional but not on the structural measures? (Generally, I would expect a higher noise level in the functional data and thus a more challenging classification scenario.)

In line 415ff, you mention that normative models allow for the interrogation of patterns in classified vs misclassified samples. Have you seen any such patterns in the schizophrenia vs control benchmark test? (If so, I think it would be instructive for readers to include a brief discussion of observed patterns for the schizophrenia vs controls application.)

Reviewer #3 (Recommendations for the authors):

I believe this manuscript is in an advanced maturity status; therefore, my recommendations are not particularly major. In no particular order:

– Colab examples and tutorials: for some reason, the pnctoolkit package cannot be installed due to dependencies issues. Unfortunately, that dissuaded me from executing the examples (which I was really looking forward to doing and, I believe, is a significant aspect of the overall work).

– Abstract. The sentence "Across all benchmarks, we confirm the advantage (i.e., stronger effect sizes, more accurate classification, and prediction) of using normative modeling features" is bordering the overstatement. I would suggest bringing up more specific aspects of the results (more quantitative statements, if you will).

– Introduction (ll. 63--72): this paragraph feels a bit out of place. I think the intent is to connect the last sentence (69--72), which I agree is relevant. However, I am not convinced by the flow of the paragraph (e.g., not sure the references to Gau et al. (2021) and Levitis et al. (2021) are a good fit here, as opposed to a discussion). I would invite the authors to rethink how this paragraph is carried out.

– Table 1. HCP's sex ratios. I believe it should say 46.6% of males.

– Figure 1. I suggest annotating the different tasks within (C) and (D), and updating the caption accordingly.

– Methods (l. 203). For ignorant readers like this reviewer, a reduced mention of why this particular test (Mann-Whitney U-test) was chosen would be appreciated. Perhaps some further details could also be given in the appendix.

– Methods (l. 212). Some elaboration on how the hyperparameters were selected (i.e., kernel and C constant). I have looked into the corresponding jupyter notebook (which was of course, available, thanks!), and it seems the defaults were used. Could this have an impact on the advantages of normative modeling?

– Methods (l. 232) Evaluation. I would suggest (i) moving the metrics within the body of each task previously (i.e.,) the definition of $\theta$ in equations. (1, 2, 3); and (ii) keeping a subsection with ll. 244--254 with perhaps a more detailed section title (e.g., statistical inference --or evaluation-- of model comparisons).

– Results section: I would suggest the authors provide subsection titles that advance the contents of the subsection. E.g., in line 271, something along the lines of "Normative modeling showcased larger effect sizes in mass univariate group differences."

– ll. 290--292. I suggest reflecting this in Figure 4A, showcasing the corresponding results without multiple comparisons correction (which should be clearly indicated) to give further support to the idea that they were along the same lines.

– ll. 285--286. "The lack of any group differences in the raw data was initially a puzzling finding…" Can this be interpreted as normative models being more powered in the discussion? This is sideways mentioned when indicating that normative models have a harmonization effect on the individual metrics, more effective than regressing out obvious confounders. A more frontal/intentional incursion into this discussion would be appreciated.

– l. 301. The subsection hierarchy seems broken. It is confusing that this particular result is not at the same level as the other (e.g., l. 311).

– l. 365. That "from this work" seemed out of place.
