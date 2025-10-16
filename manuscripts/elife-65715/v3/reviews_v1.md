# Peer review - Round 1

Editors:
- Cheryl Ackert-Bicknell, University of Colorado United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65715.sa1](https://doi.org/10.7554/eLife.65715.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

There is substantial interest in finding circulating biomarkers for Paget’s disease of bone for diagnostic applications. DNA methylation patterns in peripheral blood mononuclear cells are identified in this study that are able to differentiate PDB cases from controls with a high level of accuracy. These candidate methylation sites and regions are associated with osteological and immunologic processes, suggesting functional relevance and may be of future clinical use.

Decision letter after peer review:

Thank you for submitting your article "Epigenetic analysis of Paget's disease of bone identifies differentially methylated loci that predict disease status" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Mone Zaidi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. As the authors point out in their discussion the genes identified in cells in the blood. The authors are correct that cells of the osteoclast lineage are in the blood; however, their study would be strengthened if their results could be verified in osteoclasts where possible. The reviewers all recognize bone samples are extremely challenging to obtain. Ebrahimi et al. (PMID: 32692944) provides a nice summary of correlation between methylation levels in blood and bone. The authors should consider looking whether their methylation candidates are correlated with methylation patterns in bone to augment their functional validation methods.

2. Given that the PDB cases were slightly older than controls in the discovery set, is this a concern for conclusions of this paper, given that incidence increases with age. Please comment on this issues. The cases and controls appear to be matched given that controls are spouses. This suggests 1:1 matching. Have the authors considered conditional models or other modeling approaches that more appropriately account for matching?

3. Regarding "The number of patients with SQSTM1 mutations" (p. 5): this supposedly refers to the cases (it's unclear whether the controls were tested for SQSTM1?)

4. Does OPTN have an eQTM in its vicinity?

5. Genomic/test statistic inflation is known to be a potential issue in EWAS. We encourage the authors to provide their q-q plots as a supplement to their analysis.

6. The authors used annotation information to define their regions. This approach depends on mapping information that is dynamic and somewhat subjective. Have the authors considered a more agnostic, data driven approach to identifying DMRs? Comb-p and other DMR approaches allow for identification of DMRs based on spatial correlation.

7. More information is needed about the model selection for the DMR analysis. Why chose a generalized binomial model? What link function did you use? Given case-control study design, readers are going to expect a logistic regression (logit link function). I encourage authors to provide brief rationale for choosing this model over more familiar options.

8. Probes are expected to be correlated within a DMR. I expect multi-collinearity to be an issue when modelling groups of correlated probes together as was done in the DMR analysis. Would authors be better suited modelling methylation on the outcome side of the model, fitting a linear mixed model? This model choice would fit better with the single probe analytic strategy.

9. Did the authors use the same Bonferroni adjusted p value in the discovery and validation sets? Was it based on the total number of probes tested in the discovery set or based on the number of probes carried forward for testing in the validation set? Both are reasonable approaches. However, additional clarification is needed.

10. The authors report using 10 components from the SVA model in their analysis. Can authors provide justification for 10 components, which seems high compared to similar studies.

11. The split sample cross validation approach was appreciated for its ability to maximize experimental rigor. However, this approach is distinct from a true external replication. Given that the 'training' and the 'test' sets come from the same overall population, we expect the 'replication' results to be optimistic relative to results from a true, external replication population. Given the absence of a suitable external replication population due the unique nature of the disease, this limitation is acceptable. Please discuss the potential limitations of this approach in the Discussion section. It is encouraged that the authors to refer to the 'replication' set as a 'cross-validation' set to more appropriately convey their experimental approach to the broader scientific community.

12. It is unclear how the partial correlations, using ggm, were used in the analysis. Please clarify.
