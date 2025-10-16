# Peer review - Round 1

Editors:
- Jennifer L Raymond, Stanford School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26179.018](https://doi.org/10.7554/eLife.26179.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cerebellar re-encoding of self-generated head movements" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Sergio Carmona (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript describes an elegant set of experiments examining the reference frames and neural computations used to encode self-motion from vestibular cues. The responses of cerebellar neurons in the caudal cerebellar vermis to natural vestibular stimuli in freely moving animals, and the recording in freely moving animals is a great strength of this approach. The results indicate that a majority of cerebellar Purkinje cells encode head rotations in a head tilt-dependent manner, and a subset of cells encode head rotations in a gravity/earth-centered reference frame, rather than the head-centered reference frame of the vestibular periphery. These findings about how natural head movements are represented in the cerebellum suggest a possible mechanism for computing head direction for spatial orientation, and thus should be of broad interest.

Essential revisions:

1) The data analysis is complex, and needs to be more clearly described in the main text and justified. In particular, the model free analysis should be more clearly described and justified.

The reviewers struggled to determine whether the parameters (weights and time delays) were determined from the average of instantaneous firing rate of each cell, average from all cells, or changed from case to case. More generally, there was concern about the unstated assumptions, and potential noise and accumulation of small errors associated with the multiple layers of analysis (data smoothing, effectively data binning, multidimensional fitting algorithms across both time and parameters whose amplitudes are normalized, calculating correlation coefficients and then taking correlations of correlation coefficients).

The description around Figure 1F, which assesses the robustness of the analysis, is confusing. For 80% of the units, the Pearson correlation coefficient (R) between independent estimates was greater than 0.6. How was this value of 0.6 selected? What would the Pearson coefficients look like for shuffled data, or some type of null distribution? What about the other 20% of the neurons? If this method is one to confirm the veracity of the analysis, doesn't this imply that for 20% of the neurons the method does not work or that the unit was not the same one throughout the recording? What influenced the decision to keep such units (particularly the 8 or so units with low or no correlation)?

Does the model-free approach do significantly better than more traditional approaches? For smooth pursuit eye movements, the instantaneous firing rate of Purkinje cells does a great job of representing the kinematics as a linear sum of velocity, acceleration and the position of the eye. Does this more standard approach fail for the current data?

The value of looking at sensitivity vs. lag (Figure 3E) is not clear.

In Figure 4A and D, wouldn't the degree of nose up/down tilt effect the yaw sensitivity? The significance of Figure 4B and E should be clarified or those panels not included.

2) There is currently considerable debate as to whether one can use the firing of cerebellar neurons to identify them as a specific cell type. The authors should use additional criteria to confirm cell type identity, or back off on their claims about which cell types were recorded.

3) The "passive whole body movements condition" is very poorly described. How well matched are the vestibular stimuli that the animals experience in the passive and active condition? If they are not similar in the spatial or temporal dynamics, it seems this might explain the poorer correlations in Figure 2H. Could the smaller amount of data for the passive condition be contributing to the discrepancy?

4) Once sub-divided, some of the groups have Ns of less than 5. Can the number of recordings increased to generate more confidence in these divisions and perhaps unravel additional ones which might have been missed?

5) The analysis appears to require knowledge of the distance d, between the IMU and the point around which yaw and pitch movements are made. It is not clear whether the absolute distance is important, and if so, how it is determined. If (as it appears) the non-gravitational linear acceleration is not important for understanding the behavior of the neurons, this should be made clearer (subsection “Cerebellar units exhibit a mixed sensitivity to head angular velocity and gravitational acceleration”).
