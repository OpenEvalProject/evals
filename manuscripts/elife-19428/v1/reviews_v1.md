# Peer review - Round 1

Editors:
- Marc Howard, Boston University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19428.022](https://doi.org/10.7554/eLife.19428.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cell assemblies at multiple time scales with arbitrary lag distributions" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Marc Howard (Reviewer #1), is a member of our Board of Reviewing Editors and the evaluation has been overseen by David Van Essen as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Peter König (Reviewer #2); Bruno Averbeck (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Noting the many definitions of “cell assembly” the paper introduces a novel technique for measuring coordinated motifs of sequential firing. This method is computationally efficient and, because it makes minimal assumptions about scale, could be widely used to clarify the notion of cell assemblies, a much-needed theoretical development. Results from different brain regions in different behavioral tasks show a range of time scales suggesting that these reflect a diversity of mechanisms supporting sequences of firing patterns.

Essential revisions:

1) It is essential that a revision better discuss the filtering properties implicit in the method and address a specific concern:

The binning is equivalent to a boxcar average, i.e. temporal filtering with a rectangular window. I could say no window, see Press, W. H., & Teukolsky, S. A. (1988). Numerical recipes in C. Cambridge Figure 2.4.2. This implies that different frequencies are mapped to very different frequency bins. As here no Fourier analysis is performed, in itself it is not that bad. However, the comparison with the time reversed pattern is for different patterns at different distance. Thus, the implicit filtering is suddenly very important. At the very least, the sensitivity varies for patterns of different distance. Moreover, for the important case of perfect 0-lag synchrony, the choice of reference is important. Too close by might lead to a spill over, too far away might allow non stationarities to creep in.

This problem might be addressed either by a convolution with e.g. a Gaussian kernel before binning, in order to create well defined and better behaved temporal properties. And/or, a standard and uniform across tests distance to the reference bin could help. Alternatively, I'm open to very good arguments, why it is not a problem after all jointly with an investigation of sensitivity.

2) A revision should better discuss the generality of the method. The method is advertised as a unified tool for all cases. Although I like it a lot, there might be a few gaps. Consider an avalanche model, where the avalanche might propagate in either one of the other direction. This creates a pair of above chance co-activation with reverse sequence, the present method is blind to. Such limitations have to be better discussed.
