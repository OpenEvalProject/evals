# Peer review - Round 1

Editors:
- Jenny Tung, Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69808.sa1](https://doi.org/10.7554/eLife.69808.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper finds that common red blood cell phenotypic and genetic variation predicts susceptibility to malarial parasites. Contrary to hypotheses about ancestry-associated malaria selection, however, these variants are not more common in African ancestry populations. Overall, this work presents convincing evidence that in vitro assays of malarial invasion and growth are a practical, effective complement to large-scale genome-wide association studies for understanding the genetics of malarial infection.

Decision letter after peer review:

Thank you for submitting your article "Common host variation drives malaria parasite fitness in healthy human red cells" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by George Perry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Demonstrate the robustness of the results to removing the children from the single large family (one mother and five children) currently included in the analysis. More generally, demonstrate that genotype-based prediction is not confounded with family membership/relatedness.

2. Demonstrate that the LASSO model retains high accuracy when predicting Plasmodium invasion and growth phenotypes out-of-sample. Here, it will be crucial to completely separate the training set for the model from the test set to which it is applied (beyond internal cross-validation), either by cleanly stratifying the current sample or ideally by extending to new samples.

3. Evaluate the invasion measurements at 72 hours (the "re-invasion" phenotype); consider whether this reduces the very large amount of noise associated with the original 24-hour invasion phenotype.

4. Discuss the generalizability of the current findings to strains beyond the two strains (one lab, one clinical isolate) used in this study, including the rationale for the choice of these strains and the differences in results between them.

Reviewer #1 (Recommendations for the authors):

1. I'm most concerned about the estimates of predictive accuracy/generalization error. The permutations used to assess predictive accuracy confirm that the particular set of variants chosen by LASSO are more predictive than randomly chosen variants, in this particular sample. However, they don't provide insight into the predictive accuracy of the model out of sample. Although cross-validation should help with that problem, the CV procedure used in glmnet was not clear (also, I assume that α was fixed to 1 throughout; i.e., the authors only used LASSO, not the elastic net-it would be helpful to provide the exact parameters used). As reflected in my public review, I'm also surprised to see such strong predictive accuracy when the repeatability of growth and invasion measures from the same individuals sampled in different weeks (Figure S1) is modest to low. Is the repeatability much higher after controlling for batch and technical effects (which appear to be very substantial based on Table S1)?

2. Related, the predictive accuracy is so good that the results and methods would be very compelling if the model truly generalizes. Towards that end, I think it is essential to use a true out-of-sample test set. Ideally, this could be done by collecting additional samples and phenotyping/genotyping them. Minimally, a cleaner training/test split could be accomplished, e.g., by fitting the model with n = 50 (using internal CV) and then predicting out of sample in the remaining n = 23-although this compromises sample size in the training set, the model prediction accuracy is so high that it should be robust (note that if this approach is used, it will be important not to leak information from the training set into the test set during data normalization-that is, the values from the training set should not be allowed to influence the values from the test set at all). An additional approach would be to predict the repeated sample phenotype values (from n = 11 donors) based on the n = 73 non-carrier donors with one sample represented per donor (not as good, because the samples in the test set would not be truly independent, but still instructive).

3. If the predictive accuracy does hold up, I think the remarkably large effect sizes need to be reconciled with the difficulty of identifying large effect hits in malaria GWAS. Is this expected based on the strength of the correlation between replication rates in vivo and malaria infection/progression? Are the variants identified in the LASSO model strongly enriched for low p-values in GWAS (beyond linkage to known hits for some subset of variants)?

Reviewer #2 (Recommendations for the authors):

Awesome paper! It was a pleasure to read and very well written. The attention to detail was greatly appreciated. Most of my private recommendations are mainly suggestions for how to improve the presentation of data, but none of them are vital to the manuscript.

1. This isn't necessary, but I would like to suggest a figure that shows the association (pairwise) by carrier status for all of the RBC traits and invasion/growth rate statuses. This could be a heatmap where you would be able to show that certain carriers have a certain pattern of outcomes. You have this already in the text, but it may be easier for the reader to see it in figure format.

2. Most of my private recs are just about figures. Would it be possible to also include the association of RBC traits and African ancestry in Figure 6? I think these are really interesting and not having them in Figure 6 undersells the findings.

3. The scatterplots with the transparent dots are a little confusing to see. I would suggest something like a beeswarm plot for plots like Figure 2A-B, with a separate column for the replicates to show the tight distribution.

4. The first sentence of the discussion reads that "healthy red blood cells (RBCs) harbor extensive phenotypic and genetic variation,". RBCs have no nucleus and therefore no DNA.

Reviewer #3 (Recommendations for the authors):

1. The invasion measurements (fold change parasitaemia over 24 hours) were subject to a tremendous amount of variation, perhaps owing to culture conditions affecting schizont egress and subsequent merozoite invasion of RBCs. The authors acknowledged that these environmental effects could lead to greater experimental noise. How would their invasion measurements and analyses change if they took the parasitaemia measurements of parasites that had already gone through one life-cycle in the test RBCs, e.g. at 72 hours (re-invasion measurements)?

2. Limitations in targeted gene approach: could there be non-identified "disease alleles" in non-carriers that explain the overlap in RBC phenotypes and parasite fitness with carriers? They categorised carriers as those with known RBC disease alleles, mainly in haemoglobin and G6PD genes, while non-carriers as those not carrying these alleles. The genetic variants that they added to their analysis were limited to membrane protein genes. The non-carriers could carry a spectrum of additional gene variants that impact the RBC phenotypes observed, which could therefore influence parasite fitness.

3. The authors used one lab parasite strain and one field parasite isolate for their study, wouldn't it have been beneficial to also select a variety of parasite strains representing different invasion pathways and growth patterns, to check if these genetic and RBC phenotypic factors hold true across different strains? Given the limitations with the field isolate, wouldn't it be worthwhile to test other lab strains that use alternative invasion pathways? Also, it would be good to provide a sentence or two explaining the choice of lab and field strains in the study.

4. It was surprising that no variants in the glycophorins and haemoglobin genes were detected, given their important roles in the function of the RBC, and in parasite invasion (in the case of the glycophorins). They have previously been found to have large effect sizes in populations living in malaria endemic regions. Could the authors discuss this?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Common host variation drives malaria parasite fitness in healthy human red cells" for further consideration by eLife. Your revised article has been evaluated by George Perry as the Senior Editor, and a Reviewing Editor.

The manuscript and response to the previous reviews address nearly all the original reviewer comments and concerns and, overall, represent an excellent contribution to the literature. Revisions to the LASSO prediction analysis now present convincing and realistic evidence that red blood cell phenotypes and common RBC alleles help predict in vitro growth phenotypes.

The remaining issue to be addressed is the inclusion of statistics on training set variance explained as a major result in the text, and as key parts of Figures 4 and 5 (parts B and C of each figure). As the reduction in explanatory power in the external test sets shows, these estimates are over-optimistic and likely a result of overfitting. We ask that you remove the training set statistics from the results and figures, as the test set results alone provide a clearer, more accurate view of model performance to readers, and likely mitigate concerns from readers who are experienced with (and concerned about) overfitting in predictive modeling.
