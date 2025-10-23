# Peer review - Round 1

Editors:
- Shella Keilholz, https://ror.org/03czfpz43 Emory University and Georgia Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86453.sa0](https://doi.org/10.7554/eLife.86453.sa0)

This manuscript addresses the important issue of hemodynamic response function (HRF) variability across brain areas and will be valuable to researchers who use fMRI and other types of functional imaging that rely on neurovascular coupling. Using simulations and experiments, the authors provide compelling evidence that differences in the HRF can impact spectrum-based metrics such as ALFF and fALFF. A better understanding of the variability of the HRF is critical for the proper interpretation of activation onset times and of differences observed in clinical populations where both neural and vascular alterations can be expected.


---

# Peer review - Round 1

Editors:
- Shella Keilholz, https://ror.org/03czfpz43 Emory University and Georgia Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86453.sa1](https://doi.org/10.7554/eLife.86453.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Resting-state fMRI signals contain spectral signatures of local hemodynamic response timing" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The authors should consider and discuss the impact of potential differences in HRF shape beyond the standard model and visual cortex. Simulations considering other variations of hemodynamic responses, especially those derived empirically, would be valuable in determining the extent to which their findings are generalizable.

2) The authors should clarify the selection of voxels for training and testing, keeping proximity in mind.

3) Additional context for the interpretation of fast vs slow responders should be given (anatomical/functional location, proximity to vasculature).

Reviewer #2 (Recommendations for the authors):

1. If the authors have collected any similar data with different acquisition parameters (such as 3T, lower resolution), a comparison could be helpful for understanding how well the approach translates to other imaging parameters.

2. For the SVM classification, it is mentioned that voxels are randomly sampled for the 80-20 splits. It would seem possible that certain voxels in an instance of the test set could happen to be in close proximity to voxels in the associated training set, and any smoothness in the reconstructed fMRI data might introduce bias in the performance (despite the fact that the authors have not applied spatial smoothing in post-processing). To examine this possibility, voxels in each test partition could be constrained to be at least a certain distance away from voxels in the associated training split.

3. The interpretation of the slow v. fast V1 voxel groups could be discussed. Are the fast and slow voxels found in consistent locations across different subjects, and do they map to different anatomic regions within the visual cortex (similar to the example in Figure 1E)? What might cause a voxel to belong to one or the other group – is there a relation to the underlying neural or vascular anatomy of these subjects?

4. To examine the influence of thermal noise, the authors have taken care to show that removing a fitted noise floor alters the spectral measures of interest by only a small amount (Figure S2). To further test if there is a relationship between the thermal noise content and the HRF phase, perhaps one could see if the fast versus slow V1 voxel groups have any difference in the estimated noise floor (using an appropriate normalization scheme to handle the arbitrary units of fMRI).

5. The amount of head motion in these subjects during each condition (breath-hold, rest, visual) could be reported.
