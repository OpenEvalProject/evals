# Peer review - Round 1

Editors:
- Heidi Johansen-Berg, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35718.016](https://doi.org/10.7554/eLife.35718.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Assessing Reliability in Neuroimaging Research Through Intra-Class Effect Decomposition (ICED)" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Sabine Kastner as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Nico Dosenbach (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this article Brandmaier et al. discuss the differences between coefficient of variation (CV) and intra-class correlation coefficient (ICC) and then introduce a novel measure called the intra-class effect decomposition (ICED). The ICED estimates sources of error by explicitly modeling the contributions of each latent source of variance (e.g., person, session, day) to each scan via confirmatory SEM. These sources are then combined into a power equivalence form of the ICC, and used to estimate ICC under different conditions. The analyses of Arshad et al. (2017) are replicated using this method in order to demonstrate that different forms of the ICC (using different error components) can be estimated from the full dataset.

Essential revisions:

1) The motivation for the approach, and what it adds over existing methods, needs to be clarified. The authors state that the "key feature of this method is its ability to distinguish among multiple sources of unreliability, with understanding that not all errors are equally important and meaningful in repeated-measures design", and again highlight this in the subsection “An Empirical Example: Myelin Water Fraction Data from Arshad et al. (2017)”, last paragraph. However, these benefits are already present in ANOVA-based ICC. Generalizability Theory (G-Theory; Webb and Shavelson, 2005) has been used in neuroimaging to decompose error into constituent sources and re-estimate ICCs (e.g., Gee et al., 2015, Noble et al., 2017). Despite this crucial point, the authors only mention G-Theory in the third paragraph of the subsection “When the true scores are changing: Extending ICED to growth curve modeling”. From a practical standpoint, the estimates of the ICC2 are very similar to the estimates of Arshad et al. (2017). Although they use a subset of the data to estimate back-to-back versus repositioned ICCs, this can be estimated with the full data and an ANOVA using G-Theory.

While the authors state another motivating virtue – the ability to use "likelihood ratio tests to efficiently assess whether individual variance components significantly differ from zero" – they do not acknowledge that this is also possible in a traditional ANOVA framework, e.g., via simple F-test.

The value of this approach, which should be at the heart of its motivation, is that it provides a theoretically more valid way of estimating error from multiple sources, particularly in complex and time-dependent designs. The ANOVA and repeated-measures ANOVA become increasingly invalid with the complexity of the design. In addition, the SEM framework allows the user to test different assumptions about the structure of the model (e.g., tau-equivalent vs. con-generic). The aforementioned subsection starts to hint at this, though this should be the core feature throughout. Note however, that this is a theoretical argument; it is difficult to demonstrate the "utility" of this method over the simpler ANOVA, especially for simpler designs where the gains may be small.

2) Subsection “Intra-class effect decomposition (ICED)”, fifth paragraph: Significantly, this form of the ICC, with error variance divided by k (here, 4), represents an average measure over multiple scans. Reliability of averages are not relevant to most purposes, where a single scan is of interest. Arshad et al. get similar values (ICC=0.83) as the value in the third paragraph of the subsection “An Empirical Example: Myelin Water Fraction Data from Arshad et al. (2017)” in ALIC with repositioning, though it is difficult to tell whether they are using average measures from their methods (the exact form of the ICC is not given).

3) The extensive discussion in the Introduction/subsection “Comparing CV and ICC: Different but compatible conceptions of signal and noise” of the relative pros and cons of ICC and CV, alongside language about reconciling disparate approaches (Abstract and Introduction, first paragraph), leads the reader to anticipate a measure that reconciles CV and ICC. However, this is not the case. Therefore, the in-depth discussion of CV therefore seems out of place. The authors also return to a confusing/imprecise discussion about this in the fourth paragraph of the subsection “When the true scores are changing: Extending ICED to growth curve modeling”.

4) Subsection “Intra-class effect decomposition (ICED)”, fourth paragraph: More details are needed for the SEM estimation procedure. For instance, does "identical and fixed" mean tau-equivalent same weight across paths, but that weight is freely estimated? Since each residual is estimated separately for each scan, how are these residuals then combined into a single residual error term for the ICC?

5) Subsection “Intra-class effect decomposition (ICED)”, fifth paragraph: Do the reliability curves mentioned here refer to explicitly varying the magnitude of the error terms? If so, what is the utility of this? Or does this refer to vary the number of measurements in a Decision Study, as in Noble et al. (2017)?
