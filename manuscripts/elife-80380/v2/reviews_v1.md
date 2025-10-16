# Peer review - Round 1

Editors:
- Marcus M Seldin, https://ror.org/04gyf1771 University of California, Irvine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80380.sa0](https://doi.org/10.7554/eLife.80380.sa0)

The authors present an important perspective surrounding a fundamental question of associations between transcriptional noise and the aging process. They develop new methods to probe stochastic gene expression from single-cell sequencing data where their results suggest that associations between noise and age can be attributed to alternative metrics such as shifts in cellular identity. These methods and analyses provide an important framework to guide the fields of gene expression regulation and aging.


---

# Peer review - Round 1

Editors:
- Marcus M Seldin, https://ror.org/04gyf1771 University of California, Irvine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80380.sa1](https://doi.org/10.7554/eLife.80380.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Lack of evidence for increased transcriptional noise in aged tissues" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and David James as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All 3 reviewers find the analyses and conclusions timely and of broad interest. Specifically, the observation that lack of noise is associated with aging is intriguing. While your approach (Scallop) has the potential to be of wide use and interest, the robustness of the pipeline and systematic evaluation should be expanded in more detail. We judge that this would make your Python package more likely to be used for analysis of transcriptional noise in other systems, and, importantly, substantially strengthen the conclusions made in this study. You can see from the comments in the Public Review that all 3 reviewers are supportive overall but list specific suggestions for potential ways to improve. Obviously if you have additional questions about these, feel free to reach out.

Reviewer #2 (Recommendations for the authors):

1. The authors seem to have downloaded count matrices for published datasets. Were they all preprocessed in the same way? Can authors rule out different pre-processing steps affecting the inconsistent results between studies?

2. Overall, I found the comparison across methods particularly interesting, but the authors seem to overlook the possibility that they might capture different biology and search for consistency. I would be interested in a discussion point on what each method can measure biologically.

Reviewer #3 (Recommendations for the authors):

Despite the weaknesses mentioned in the Public Review, this is still an important study and I would support the publication of this manuscript in eLife if it is sufficiently revised.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Lack of evidence for increased transcriptional noise in aged tissues" for further consideration by eLife. Your revised article has been evaluated by David James (Senior Editor) and a Reviewing Editor. We are prepared to consider a revised submission detailing a few minor clarifications.

In particular, all of us found the manuscript to be significantly improved and, with the addition of some minor changes, ready for publication. These include updating the figshare repository code to reflect current manuscript results and several text-based revisions regarding interpretations of transcriptional noise during identity loss and appropriate referencing of previous studies. These are detailed below and we look forward to moving forward with acceptance. Below you will find related comments made by both reviewers:Reviewer #1:

1) The figshare repository with the code does not seem to be updated. It's important that the code related to the generation of synthetic data and their analysis is uploaded.

Reviewer #2:

The revised manuscript is stronger than the original submission. The authors either directly address the concerns or specifically acknowledge what was/is a weak point of the study (for valid reasons related to the technique itself).

There are indeed very few longitudinal studies that focused on cellular aging-noise connection in live cells, therefore additional work is needed to quantitatively/experimentally sort out the contributions of intrinsic/extrinsic factors to the overall transciptional variability. In the Discussion section where the authors discuss the few longitunidal examples (Liu et al. and Sarnoski et al. papers), the current writing gives the impression that no mechanism has been proposed or studied from experimental and/or computational perspective to explain the mechanism of noise-change during aging. Actually, based on stochastic simulations matching experimental results, both of the above papers have already proposed that the observed intracellular variability dynamics in aging haploid/diploid yeast could be due to specific stochastic promoter state transition rates occurring during single-cell aging. While the age-associated changes in chromatin remodeling is just one mechanism (among potentially several) that could explain intrinsic noise dynamics during aging, it is still important and should be appropriately acknowledged in the same discussion paragraph.
