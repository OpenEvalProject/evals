# Peer review - Round 1

Editors:
- Richard M White, Memorial Sloan Kettering Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26014.036](https://doi.org/10.7554/eLife.26014.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "microCT-Based Skeletal Phenomics in Zebrafish Reveals Virtues of Deep Phenotyping at the Whole-Organism Scale" for consideration by eLife. Your article has been favorably evaluated by Didier Stainier (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

General comments:

In general, all three reviewers felt this is an important contribution to the field, since it allows the zebrafish to be more readily used for analysis of complex phenotypes. Broadly, this falls under the category of phenomics, a rapidly growing field across multiple disciplines. The methodology and algorithms implemented here are well-executed and appear technically sound. However, the reviewers also felt that the authors tended to overstate their findings, and that they did not truly demonstrate that this could be used for high throughput analysis across many different mutants/backgrounds. Several times they refer to their approach as "whole-body" phenotyping; even with respect to the skeleton, they are not looking at the whole body, but only to a limited portion (the axial skeleton), of uniform embryological origin. They also say they are looking at "hundreds" of traits. This is only accurate if you count each aspect of each vertebra as a unique trait. For example, I would argue that tissue mineral density almost certainly is not unique for each vertebra, but rather varies systematically as one aspect of a mutant phenoptype. In addition, as detailed below, there are some questions regarding both the sensitivity and resolution of their methods, and how easily it can be generalized for new users. By addressing these concerns, we believe the paper will be greatly improved.

Essential required revisions:

1) Given the methods focus of this manuscript, the results in Figure 4 are critical to the conclusions of the study. There are several concerns regarding this figure.a) The authors utilize Monte Carlo simulations to estimate the power, sensitivity, and specificity of their method. However, important details regarding this simulation are absent. In particular, what type of probability distribution was used for the simulation? What evidence do the authors have that the measured phenotype (total TMD) follows this distribution function in wild type zebrafish? Are 3 fish per arm sufficient to support the assumption that this is the true probability distribution function, and to reliably measure it? If this cannot be justified, the authors should include additional fish in this analysis. Given that the authors describe their method as "enabling rapid (<5min/fish), whole body profiling," it is surprising that only 3 fish per arm were used for this figure. This is particularly concerning for panel 4F, in which two groups of n=2 are being sampled from a population of 3 fish.

b) While the authors devote considerable attention to total TMD, it is unclear how this test performs for other phenotypic measures. Does their method also provide increased sensitivity with similar specificity for other measures? An exploration of additional measures should be included to provide a more complete picture of the performance of this assay.

2) The authors clearly demonstrate in Figure 3 that for the second pre-caudal vertebrae there is a strong linear relationship between data acquired at high and medium resolution. In order to demonstrate how robust this relationship is across all vertebrae, the authors should provide a summary panel. For example, they could generate a plot analogous to that in Figure 2 using r-squared values instead of correlation coefficients.

3) One of the assumptions of removing allometric effects as the authors have done in Figures 7 and 8 is that, as stated in Lleonart, Salat and Torres, 2000 "the available observations cover different values of X and it is recommended that sampling should cover systematically the entire range of variation of X in order to get good estimates of a and b." Related to the point discussed for Figure 4, the authors should address (and provide evidence) whether n=3 (Figure 8) is sufficient to meet this criteria. If not, additional fish should be included in order to accurately account for allometric effects.

4) The authors should provide example data along with their FishCuT source code to allow readers to better understand the method when attempting to implement it for their own data.

5) Zebrafish have the potential for use in overexpression screens, where phenotypes would exist as gradations instead of binary outcomes. Have the authors ever looked at fish with an overexpression phenotype where the phenotype is variable or incompletely penetrant? How robust is their analytic method to this type of data? This would be useful for ensuring the broad applicability of the method, but is not a requirement for publication.
