# Peer review - Round 1

Editors:
- Edward H Egelman, University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68946.sa1](https://doi.org/10.7554/eLife.68946.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

You have fully addressed the concerns of the reviewers. While in some cases you have explained that resolving certain issues is beyond the scope of the present paper, the manuscript as it currently exists will be a useful contribution to the area of template matching for locating complexes in cells.

Decision letter after peer review:

Thank you for submitting your article "Locating Macromolecular Assemblies in Cells by 2D Template Matching with cisTEM" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Edward H Egelman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Aldrich as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Elizabeth Villa (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) A point of concern is the degree of reference-bias in the results of the 2DTM approach. The authors acknowledge this concern and that conventional use of the FSC is not a suitable validation metric for this approach nor for determining an appropriate filtering cutoff for a resulting reconstruction. The proposed validation metric of the emergence of additional known density features in a reconstruction, which are not present in the template, resulting from 2DTM hits is sensible. However, emergence of additional unknown densities in a reconstruction resulting from cellular data will be difficult to segregate from noise, especially since filtering of the reconstruction is determined ad hoc instead of by an objective metric.

2) The work remains on an empirical level as surprising advantages of the 2D approach compared to 3D are revealed, but there is little effort to get to the basis of these observations. Moreover, details on the compared 3D approach (and its parameter optimization analogous to the 2D approach), which the rather general conclusions would require, are missing. Lastly, the 3D approach has been applied to the strongly pre-irradiated sample, which may make observations such as a lower specificity in the 3D case almost a self-fulfilling prophecy. Thus, the 2D vs 3D comparison is not convincing in the current form. The 2D implementation of in situ structure determination is interesting and of potential interest to a large audience. However, the comparison to the 3D equivalent appears somewhat incomplete and the rather general conclusions require further validation. In the absence of further validation, the conclusions need to be toned down.

3) Which concrete recommendations do the authors provide with regards to data acquisition? The researcher has to make a decision whether to spend the most valuable first ~30 e-/Å2 on a projection or a tilt series. In this manuscript, the authors argue for the former, while Mahamid and colleagues have obtained beyond 4 Å resolution using the latter strategy (Tegunov et al., 2021). This leaves people somewhat puzzled.

4) In this work, the provided FSCs suggest that resolutions in the range of 5 Å are achieved, but all figures are low pass filtered to ~20 Å, which appears odd. Of note, the FSCs do not exhibit an extended plateau with FSC approx. 1 at low frequencies, which is normally observed. Please explain.

5) Cross-resolutions of reconstructions and 30S (from B. subtilis and M. pneumoniae) should be provided as an assessment.

6) L. 298: "The pre-exposure of 32 e-/Å2 affects the signal in the tomograms at higher resolution but is expected to have only a small effect in the resolution range relevant for 3DTM, i.e., 20 Å and lower (Grant and Grigorieff, 2015)." This is a very key assumption of the entire study that must be validated experimentally. Nucleic acids are known to considerably more beam sensitive than amino acids and hence 32 e-/Å2 is typically considered a very high dose for ribosomes. The authors must do the reverse experiment to validate the stated assumption, which is to spend the first 32 e-/Å2 on a tilt series, then acquire the 32 e-/Å2 2D image, and finally resume the tilt series.

7) For 3D template matching essential computational details are omitted. Importantly, the spatial and rotational sampling (i.e., voxel size and rotational increment/number of rotated templates) is not specified. Given that the authors point out the importance of rotational sampling this omission is surprising.

8) Regarding the above remark: what is the authors' expectation if sampling is increased for the 3D case (and first 30 e/Å2 on the tilt series): will the suggested trends on 3D vs 2D approach still hold? In other words: is (limited) computation the problem in the 3D case or is there a conceptual advantage resulting in higher specificity for the 2D approach?

9) To make general statements about 2D vs 3D template matching the authors must ensure that they use comparable sampling – or use some other normalization of their approaches (e.g. computation time).

10) The paper lacks any discussion of the 2D vs 3D results in the light of the dose fractionation theorem, as stated by Hegerl and Hoppe theoretically and experimentally confirmed by McEwen. This theorem states that the information content of 2D image or 3D volume imaged with the same dose is the same, albeit different structure factors are sampled in Fourier space.
