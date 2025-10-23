# Peer review - Round 1

Editors:
- Jeannie Chin, https://ror.org/02pttbw34 Baylor College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77745.sa0](https://doi.org/10.7554/eLife.77745.sa0)

This paper presents important information about how potential network-based structural and metabolic imaging biomarkers are associated with memory performance during distinct disease stages, in line with previous hypothetical biomarker models. The study is conceptually sound and methodologically convincing and will be of interest to neuroscientists and medical professionals involved in the study of Alzheimer's disease and related neurodegenerative conditions.


---

# Peer review - Round 1

Editors:
- Jeannie Chin, https://ror.org/02pttbw34 Baylor College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77745.sa1](https://doi.org/10.7554/eLife.77745.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Stage dependent differential influence of metabolic and structural networks on memory across Alzheimer's disease continuum" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jeannie Chin as the Senior Editor. We thank you so much for your patience during this unusually long review period. The following individual involved in review of your submission has agreed to reveal their identity: Amy Kuceyeski (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

In your revision, as you address the Reviewers' points, please consider these Essential Revisions:

1) Please clarify whether the validation cohort was truly independent from the original analyses, and include additional information on how the analyses were done.

2) Add discussion regarding the analysis method and whether it may be sensitized to the relative imbalance of group sizes across diagnoses or other parameters or outliers.

3) Please demonstrate that the variance is similar across diagnostic groups, or use a non-parametric test. Also, clarify whether p-values are corrected for multiple comparisons in all figures.

4) It would be helpful to include an assessment of metabolic network scores for a region that might not be (or might be least) affected in AD as a negative control, to address the question of whether the effects being measured are global or localized effects.

5) Please include an analysis that uses a method other than LASSO to assess correlations between network measures.

Reviewer #1 (Recommendations for the authors):

– I would argue that for the PLS analysis, an approach similar to Liu et al. 2019 Molecular Psychiatry would be more reasonable, as back-projecting to a template salience map derived from a healthy subgroup would mostly eliminate the concerns I mention in the public review. Otherwise, a clear justification for the employed scheme should be included.

– The bar charts depicting the network scores suggest that the variance is unequal across diagnostic groups, which would violate ANOVA assumptions. It would increase the strength of the group comparison results if a non-parametric test could be applied.

– It might be outside the scope of this paper but it would be interesting to see a quantification of the divergence between metabolic and structural network contributions to memory scores, e.g. by applying a multiplex graph-based approach (as in, for example, Canal-Garcia et al. 2022 Cerebral Cortex).

Reviewer #2 (Recommendations for the authors):

In figure 2, please represent the data in panel B as a violin or raincloud plot – the bar chart as it is shown obscures the details of the data distribution.

More details are needed in the main text to understand how the z-scores in Figures 3B and 4B are calculated. What value of the GMV and metabolic maps from the individual are used to derive the individual scores? Raw GMV per voxel within the GM covariance network?

Once the network scores are found, what group is used to z-score? From looking at the bar charts, it seems that the entire 708 subjects group was used to calculate the z-scores? or CN only?

From looking at the widespread nature of the metabolic networks in Figure 2A (and to a lesser extend the structural networks in Figure 3A) and the near constant values in the bar plots within the patient groups, it appears that the 7 "different" networks may be measuring more of a global effect rather than a localized one. It would be good to see metabolic network scores for a region that is hypothesized to be least effected in AD as a negative control. If this network still has the same overall effect, then maybe the pathological network effect being measured here is a global phenomena?

It seems odd that the CN group would have lower structural network scores than the MCI in the A-T- group. Please discuss this somewhat surprising finding.

There are many comparisons being done here (although it is unclear how many) – are p-values being corrected for multiple comparisons in Figures 2B and 3B? Please add these details.

There is likely a lot of correlation between the network measures (as evidenced by the fact that the network scores are very consistent across regions within the same group). It is known that LASSO will randomly suppress one of two correlated variables. Please use a different penalty (perhaps ridge) that does not have this drawback so that the interpretation of the coefficients can be more trustworthy.

Relatedly, Sup Figure 9 showing the variable selection frequency for permuted datasets is a bit confusing – the frequency ranges are 0 to 5 (unclear what unit this is representing), do not appear to be uniform/random and vary greatly between the main and validation dataset. I am not sure how these results support the main conclusions about the SVC model. Replication of the main findings using something other than Lasso/Elastic Net would be helpful to support the main findings.

The replication study is a bit confusing. It appears that 468 individuals were added to the original set of 812 to obtain a set of 1280 individuals, 859 of which were used in the final step of the analysis. Unless there is a misunderstanding, doesn't this mean that the "replication dataset" is actually mostly the original dataset? it would be stronger to replicate the study using only the 468 independent individuals – otherwise it is not a replication study.
