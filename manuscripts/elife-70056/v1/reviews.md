# Peer review - Round 1

Editors:
- Noah K Whiteman, https://ror.org/01an7q238 University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70056.sa0](https://doi.org/10.7554/eLife.70056.sa0)

In this study, the authors took an experimental, empirical approach to tackle the thorny problem of micro-scale variation in soil properties within and among field plots in confounding statistical analyses. The issue is that in field experiments, small variation in one or more soil property variables can obscure true effects of experimental variables on plant phenotypes. The main result is that without their framework they would not have found the association between water treatment, plant growth and Microvirga bacterial abundance, it would have been lost to the noise inherent in these kind of large-scale experiments with relatively modest degrees of freedom. Overall, the PC-based approach to de-noise these kinds of datasets provides an important advance by pulling out subtle phenotypic effects in field trials.


---

# Peer review - Round 1

Editors:
- Noah K Whiteman, https://ror.org/01an7q238 University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70056.sa1](https://doi.org/10.7554/eLife.70056.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Increased signal to noise ratios within experimental field trials by regressing spatially distributed soil properties as principal components." for consideration by eLife. Your article has now been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Meredith Schuman as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Andrew Gloss (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Each of the reviewers' specific concerns below should be addressed prior to resubmission of a revised manuscript for publication consideration. A major concern was a lack of detail on many aspects of the statistical model, the location of the raw data and ability of others to re-run the code. This should be the focus of the author's should they consider revising and resubmitting this manuscript.

2) Because the manuscript is, essentially a methods development report, it is of the utmost importance that the authors revise this manuscript in alignment with those goals. It should be straightforward, not difficult, for others to implement the tools developed.

Reviewer #1 (Recommendations for the authors):

I would like to see the raw data and methods for all of these experiments uploaded/appended as supplementary information here--it isn't satisfactory that one should turn to a preprint for this information--it should all be in the present manuscript. In that vein, I was also confused by whether microbes were a treatment or a passive variable here in this study (e.g., I had a hard time differentiating between the Qi et al., biorxiv manuscript and this one).

Reviewer #2 (Recommendations for the authors):

Overall, I found the approach exciting, and the paper makes a good case for its use in future experiments! However, some work is needed to make the presentation more complete in a few different ways, as numbered below. When revising, please consider the following sentence-by-sentence and analysis-by-analysis: is the approach fully described in the methods? Are the necessary results provided so a reader could evaluate support for the statement rather than taking the written interpretation at face value? (e.g., L245: readers should be able to view the results, rather than relying on the vague assurance that the results that aren't shown are "similar" to the one that is. This paper could and probably should have more extensive supplementary results to achieve this).

1. Not all aspects of the method's implementation are described thoroughly in the paper, in both practical and conceptual senses. This includes both the specific formulations of each analysis -- with a careful description of the model inputs, outputs, specification, and software packages -- and very clear explanations of the goal of each step and how the approach achieves it. The incompleteness of these details made it difficult to fully evaluate, and could pose obstacles to its reliable implementation and interpretation by other researchers. In a paper presenting a methodological approach and arguing for its broader use, clearly walking readers through these steps is essential. Addressing this will require revisions to the methods and results alike. While I do appreciate the brevity, other papers implementing spatial models for environmental variation -- such as Pauli et al., 2018 (G3, doi: 10.1534/g3.117.300479) or Velazco et al., 2017 (Theor. Appl. Genet; doi: 10.1007/s00122-017-2894-4) -- walk the reader through their approaches more thoroughly.

2. Results are presented incompletely. For example, Figure 4E shows how PC regression affected variance partitioning among explanatory variables and unexplained noise, but only for one dependent variable. This really should be conducted for every dependent variable included in the study. When conducting many tests, a seemingly compelling result can arise even by chance, so it's difficult to know how to interpret a single strong result that is hand-picked to be presented. Similarly, the effect of spatial modeling should be presented across all OTUs considered in the study, not just one with a particularly strong effect in the desired direction. Otherwise, one is left wondering if this is a chance result (since re-fitting a model on adjusted data will always alter it) that only arose because so many OTUs were tested -- and whether patterns in the opposite direction, where a significant effect emerged only in the unadjusted phenotypes, also were observed. Note that multiple test corrections (likely FDR) should be presented when applicable as well throughout the paper, especially for the large number of OTU tests that must've been conducted but not shown. It seems like the results should pass this scrutiny, but it must be applied nonetheless!

3. How the approach builds on or is unique from previous studies and approaches, and ensuing strengths and weaknesses to be expected as a result, is not sufficiently described; see Public Review for further details.

Specific comments:

I don't quite follow how separation of cluster centers in the PCA plots (Figures 4A-B) suggests that environmental noise has been reduced and treatment signals have been boosted. In these figures, the centers for each condition do appear further apart, but the spread of points within each condition have also increased. If both spread and centers increase, does this actually reflect better separation of conditions, or just a re-scaling of the overall plot? Does variance partitioning (explained vs. unexplained variance) and the significance of the condition effect in a statistical model actually improve? (Also, I'm confused by L223-224 -- wouldn't weakening a true treatment effect also enlarge clusters, albeit in a different way by drawing points toward the center of the plot?)

It would be very helpful to walk through the spatial model selection more -- a bit on the different spatial covariance structures that were tested in particular. The test results used for model selection should also be more fully presented, including parameters relevant to the likelihood ratio tests that were conducted (e.g., degrees of freedom for each comparison, log likelihood scores for each model and associated p-value, etc).

L143-147: Microbiomes of different compartments being affected by different soil elements seems plausible, but this could also just reflect false negatives, a common problem when simply "tallying up" the tests significant at some threshold. As a result of experimental noise (or differences in the amount of unexplained variance within specific compartments), it's possible that an element might have significant effects only in one compartment even if it affects all of them. Evaluating a model of microbiome_composition ~ element * compartment is needed to test this, paying attention the significance of the interaction term.

Table S1: How is model complexity taken into account? Typically, a more complex model will always have reduced error. Do the model comparisons penalize for increasing model complexity?

I was unable to access the scripts on Zenodo, but maybe that was user error on my end!

Reviewer #3 (Recommendations for the authors):

1. It might be helpful to describe the details of the statistical model.

2. To help readers employ the proposed tool in their studies, it is valuable to include the step-by-step procedure of the proposed strategy, such as selection of variables, number of PCs to include in the model etc.

3. For the proposed tool, will the correlations between the phenotypes affect the results/performance?

4. Page 10, line 151: GCMS should be "GC/MS" or "GC-MS"?
