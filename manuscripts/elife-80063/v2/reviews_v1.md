# Peer review - Round 1

Editors:
- Siming Zhao, https://ror.org/049s0rh22 Dartmouth College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80063.sa0](https://doi.org/10.7554/eLife.80063.sa0)

This paper investigated the identification of causal risk factors on health outcomes. It applies sparse dimension reduction methods on highly correlated traits in the Mendelian randomization framework. The implementation of this method helps to identify risk factors when given high dimensional traits data.


---

# Peer review - Round 1

Editors:
- Siming Zhao, https://ror.org/049s0rh22 Dartmouth College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80063.sa1](https://doi.org/10.7554/eLife.80063.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Sparse Dimensionality Reduction Approaches in Mendelian Randomization with highly correlated exposures" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Martin Pollak as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Stephen Burgess (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Clarification of the method details. All three reviewers have clarification comments.

2) Interpretation of results. See comments from reviewer 3.

3) Demonstration of benefits in real data analysis. See comments from reviewers 1 and 3.

Reviewer #1 (Recommendations for the authors):

I'm not the best person to judge, but I'm not sure how accessible this work would be to someone who doesn't understand multivariable Mendelian randomization. Figure 1 is a great overview, but I'd appreciate the viewpoint of someone who is less familiar with these methods.

The description of the different sparse PCA methods was a helpful summary.

I'm not sure that the foray into instrument strength is valuable – it is over 2 pages and 2 figures, and I'm not sure how much this adds – maintaining high conditional F statistics is important, but their calculation is not a major part of the analysis report. The whole section is a bit distracting and disproportionate.

All MR estimates seem to be on quite odd scales – the estimates are all close to 1 – 1.001 or 0.999. Could the PCs be standardized, so that the estimates are per 1 SD increase in the PC? This would improve communication of the results. Currently, there is no sense of scale – what is the corresponding change in lipids on a meaningful scale?

While I understand that the main thrust of the manuscript is methodological, I didn't get a strong sense of what the conclusion from the applied analysis is. If the authors could communicate a strong finding, this would help to justify the use of the method. Eg what are the estimates for the HDL clusters in the SCA method? This isn't clear.

Figure 6 would be key to this – currently, it's not clear what the various PCs represent. Maybe a radar chart would help? Also, the caption for Figure 6 is incorrect – the caption from Figure 8 has inadvertently been duplicated here.

While I wouldn't want to insist that the authors change their paper, the obvious application of this work appears to be imaging studies – this is currently under-explored.

Figure 5 is a really helpful summary of the performance of the different methods in this investigation.

Reviewer #2 (Recommendations for the authors):

This is a nice paper, with convincing and very useful results. I have mainly some clarification questions and suggestions.

1. The main idea is to treat the matrix of SNP-exposures associations γ^ as explanatory variables in the regression Γ^=γ^β+e, although this is clearly not a standard regression model, just that a WLS or GLS estimator for β is equivalent to the 2sls estimator on single-sample data. I think it would therefore be instructive to link to the construction of PCs in a single-sample individual-level data sets. There the model is y=Xβ+uX=Gγ+V and one could do a PCA on X. Alternatively, as the 2sls estimator is least-squares in y=X^β+u~ where X^=Gγ~, one could perhaps consider PCA on X^. As X^TX^=γ^TGTGγ^ this is getting close to the PCA on γ^ if GTG is normalized, for example GTG/n = Ip. If it is not normalized, then it is hard to make a connection. It may therefore be worthwhile considering PCA on the weighted γ^ as per the (extended) IVW estimator in (1) on page 4. With such a link in place, it seems easier to motivate the proposed method.2. Are the covariances σlkj reported in the GWAS? I assume the estimators are simply IVW throughout, as implied at the top of page 5?3. It is unclear to me why ∆ is estimated by OLS in (2).

4. Notation. It would be easier to follow the notation if matrices are upper case and vectors lower case. That would change for example the current vector γ to a lower case letter and the current matrix γ to an upper case letter.

5. It is not straightforward to follow the steps for Sparse PCA on page 56, as not all symbols are clear. It is not clear in 1. what "Setting a fixed matrix," means and what the αj are. Also, define Xi. In 2 you simply do an svd? Should there be "hats" on γ? UDVT in step 2. are not the same values as in the svd for γ^.

Reviewer #3 (Recommendations for the authors):

Here are some detailed comments.

1. Usually a good idea to number figures in the order they appear in the text (Figure 12 out of order).

2. UVMR is referred to as UMVR three times and as UMVMR once

3. At the beginning of the Methods section, it would be good to specify the dimension of \γ. It is also important to specify how the variants used are selected.

4. Figure 1 is a bit chaotic and inconsistent with the text. Figure 1 top, the graph indicates that there are 118 exposures. I assume this was chosen because it is the number of lipid exposures in the data application but it doesn't look like the lipid data is used in this figure. Figure 1 top right, the dimension of the matrix is given as L x 118. The variable L does not appear elsewhere in the paper. What is printed appears to be a 60x60 square matrix. Is this matrix meant to represent γ⊤γ? The statement "MR estimates affected by multi-colinearity" printed next to this matrix doesn't appear to relate to the figure because the figure doesn't indicate anything about the MR estimates.5. Figure 5. It looks like none of the matrices shown have all 118 rows. The sparse PCA matrix has many fewer exposures than the other methods. It would be good to clarify this in the caption.

6. Figure 6 is labeled as "Extrapolated ROX curves" but appears to be a comparison of UVMR and MVMR results. For the top right plot, I would have expected UVMR and MVMR results to be identical since the PCs are exactly orthogonal. Why is this not the case?

7. Page 12 describes Figure 5 as "The loadings for all methods (Figures 5a-e) are presented for LDL.c, a previously prioritised trait." I am confused about what "for LDL.c" means here. It appears that LDL.c is one of the traits in Figure 5 but these appear to be loadings across some large subset of traits?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Sparse Dimensionality Reduction Approaches in Mendelian Randomization with highly correlated exposures" for further consideration by eLife. Your revised article has been evaluated by Martin Pollak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved and all reviewers agree this study will be useful for the field. However, there are remaining issues and we would like to invite you to further revise this manuscript.

Revision outline:

1. Adding a deeper more nuanced discussion of what is meant by causality and how to interpret the components. The major advancement of this study comes from method development and it is important to not overstate the significance of results. See comment 1 from reviewer 3 and comment 4 from reviewer 1.

2. The choice of method. Discussing scenarios that will work or fail for the method will be helpful for the readers to better utilize this tool. See comment 4 from reviewer 1 and comment 2 from reviewer 3.

3. Adding details of simulation. Other clarification issues raised by reviewers.

Reviewer #1 (Recommendations for the authors):

1. While I appreciate the simulation study, and believe this is worthwhile, it strikes me that the primary reason for choosing one or other of these sparse methods is not performance in a simulation study, but rather how the methods define the PCs, and how the analyst could interpret the results. As there's no point running an analysis if you can't interpret the results. This will depend on the specific characteristics of the investigation, so I am not expecting a single method recommendation. But I'd appreciate a bit more acknowledgement of this in the choice of methods – what characteristics to these methods tend to result in? Interesting (and reassuring) to see that clusters from the SCA and sPCA methods look similar in Figure 2 (although then odd that in Table 3, the significance differs for the VLDL and LDL components…).

Overall, I appreciate the authors' manuscript in that it proposes sparse dimension reduction as a method and explores the properties of MVMR estimates from this approach. My sense is that it is difficult to say anything more authoritative/general than "hey, look – we tried this and it sort of worked!", but the authors do this in a way that is mostly clear (see comments above) and should be helpful to future researchers.

Reviewer #2 (Recommendations for the authors):

I am happy with this revision. The authors have responded well to my previous comments and suggestions, or clarified their preferred choices.

Reviewer #3 (Recommendations for the authors):

The resubmission has corrected some of the issues I raised previously. However, I have some remaining concerns, primarily about the interpretation of the proposed causal effects and the simulation results.

1. My largest issue is still in the causal interpretation of genetically determined PCs are sparse components. To me, I don't think there is a way to turn the components into well-defined exposures that admit a counterfactual or interventional definition of a causal effect. This approach seems closer to "causality adjacent" methods like TWAS. There was a paper a few years ago using sparse CCA in combination with TWAS (https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1008973) and this seems similar to that to me. I think one option for this paper would be to add a deeper discussion of what it means to test for a causal effect of a component that may or may not represent a latent biological variable. On one end of interpretation you have "association with genetically predicted exposure component" and then I think you could add as a bonus that if you have successfully identified a biological component, this could be interpretable as a causal effect.

2. Using the components introduces an issue of horizontal pleiotropy if a single variant is allowed to affect multiple components. This suggests that the component-based MVMR results would be more appropriate than component-based UVMR results, though for PCA this is not an issue due to orthogonality and approximate equivalence of UVMR and MVMR.

Some questions about the simulations:

3. In Figure 4, it seems like the MVMR plot should have 6 lines and not two. How were the 6 traits combined into two lines here? It seems unfair to average the rejection rate for the X_1-3 into the black line since, if MVMR performed perfectly, it would never reject X_3 and always reject X_1 and X_2.

4. Why is there an interval around only the black line in the MVMR plot and not the other plots?

5. The sentence in the caption presumably describing the color scheme is cutoff. "The results are split according to group n black…"

6. Is the appropriate number of components known a-priori in the simulations?

7. The description of Figure 4 suggests that PCA and SCA are out-performing MVMR. However, PCA has exactly the same rejection rate for the causal and non-causal block of traits which seems like bad performance to me. SCA has a Type 1 error rate between 20 and 30% at a nominal level of 0.05 which also seems quite bad to me. I would not view improving power at the cost of uncontrolled type 1 error as a good outcome.

8. The description of the Figure 5 at the top of page 9 does not align with the image in Figure 5. "Both standard and Bonferroni-corrected MVMR performed poorly in terms of AUC (AUC 0.660 and 0.885 respectively), due to poor sensitivity. While there was a modest improvement with PCA (AUC 0.755), it appears that PCA and RSPCA do not accurately identify negative results (median specificity 0 and 0.28 respectively)." Reading these numbers, it sounds like MVMR is the worst followed by PCA, followed by MVMR_B. However, in the figure, PCA and RSPCA both have lower AUC than MVMR and MVMR_B. These numbers are also inconsistent with Table 4.

9. I think I may be a little confused about how the ROC curves are constructed.

9a. In my experience, an ROC curve is usually constructed by varying a threshold (e.g. α). However, it seems here like α was fixed and we are averaging over the single point obtained for each simulation setting according to the Reitsma et al. method. This method makes sense when the data are real observations, however, in the case of simulations, why not use the traditional method of varying to threshold and then averaging the full curves across simulations?

9b. I think this method of displaying results also obscures the issue of calibration. If there is a nominal significance threshold, we would like to see that type 1 error is controlled below that threshold.

9c. Visually, Figure 15 looks inconsistent with Figure 5 to me. There are no blue points in the upper right of Figure 15 -- does it make sense to extrapolate this part of the curve? Figure 5 suggests that the red methods at least have the potential to do very well in differentiating true and false positives but this doesn't seem born out by Figure 15 where most of the red points cluster in the upper right.

10. On the selection of instruments -- is it correct that you are assuming that all variants affecting any of the component metabolites also affect LDL/HDL or Triglycerdies as measured in the GLGC study? Does this assumption limit your ability to identify components that separate LDL or HDL sub-components? For example, variants that affect only a small number of components will be less likely to be selected using the GLGC reference.
