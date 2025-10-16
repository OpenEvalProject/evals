# Peer review - Round 1

Editors:
- Jack L Gallant, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36928.033](https://doi.org/10.7554/eLife.36928.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Spatial sampling in human visual cortex is modulated by both spatial and feature-based attention" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Sabine Kastner as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Michael Silver (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study measured effects of feature-based attention on pRF eccentricity and size changes related to spatial attention. The authors investigated the hypothesis that feature-based attention optimizes the attended feature's spatial sampling by using a pRF mapping stimulus that varied along two feature dimensions: color and temporal frequency, and they found that attention to color showed stronger modulation of pRF eccentricity and size change compared to attention to temporal frequency. The authors interpret these results with an attentional gain field model by noting that receptive fields preferring color are typically smaller and more foveal compared to those preferring temporal frequency, consistent with these receptive fields having greater changes in eccentricity. They further demonstrate that attentional gain fields were smaller for the Attend Color condition, indicating greater precision of the attentional gain field for color receptive fields. The editors were impressed with this elegant and well-written paper that contains thorough and principled analysis procedures. However, they were concerned regarding some of the statistical analyses (see details below). Also, the authors should clarify how the results advance the field's knowledge about effects of spatial and feature-based attention (and their interaction). The application of the attentional gain field model to these findings was perceived as a strength. Overall, the editors felt that major revisions will be necessary to strengthen the study, so that it can be further pursued at eLife.

Essential revisions:

1) Feature-based attention has long been thought to have modulatory effects on spatial attention (Saenz, Buračas and Boynton, 2002; Maunsell and Treue, 2006). The current study supports this idea by reporting specific analyses where color and temporal frequency are used as attended features and spatial resampling is assessed by measuring populations receptive fields. Despite the effort, the findings of the study are mostly confirmatory in nature. The manuscript would benefit from a reorganized presentation of the results to highlight the novel contributions of the study as opposed to confirmation of prior findings.

2) There isn't adequate information about how the target features were selected. Why should we be interested in attending to temporal frequency versus color in the context of this study? (It is also unclear/unexplained why blue-yellow and cyan-magenta were selected as representative colors.) Would anything change if different colors, a broader range of temporal frequencies, or entirely different feature sets (e.g., orientation) were used?

3) It is reported that pRF changes for Attend Color case are larger compared to Attend Temporal Frequency case. It would, however, be better if the difference could be presented in a more conspicuous way. For instance, the way it is presented in Figure 5A gives the impression that the difference is almost negligible. If there is merely a slight difference, more detailed discussion is warranted regarding the reasons underlying pRF changes when attending to color vs. temporal frequency.

4) Related to the previous comment: When the regions primarily engaged by the two distinct features compared lie at different points in the hierarchy of visual cortex, the strength of retinotopic representations (and thus spatial) will inevitably vary. Wouldn't that introduce a bias in assessment of interactions between spatial and feature-based attention?

5) There is too much variability across subjects in the attentional gain field sizes of temporal frequency vs. color (Figure 7). Given that there appears to be poor consistency across subjects for this measure, this figure does not convey information in a convincing way.

6) The authors combine pRF eccentricity and size to obtain a single index, because they claim there's a high correlation between the two. We don't think this is warranted. For instance, Table 22 shows that there's a significant correlation between eccentricity and size changes in V1 for only 2 out of 5 subjects, and the average correlation is not very high for this ROI either (R=0.461). This also makes it questionable to present the results using voxels from a "combined ROI", given the large degree of variability across individual ROIs.

7) In most of the supplementary figures (e.g., the first one), results for individual subjects are not shown at the same scale across subjects, which makes them confusing. Also, there's barely any change in the pRF size with increasing eccentricity for some ROIs of some subjects (e.g., V1 of s5). Some extended treatment and discussion of the consistency of the presented results across subjects would greatly benefit the manuscript.

8) We found it difficult that when statistical analyses are performed across voxels bootstrap tests were applied, and yet across subject tests were based on ANOVA or t-tests. If the same type of metric is evaluated in both cases, shouldn't you make the same assumptions about the distribution of the metric?

9) More detailed description of the outlier rejection method is needed, as this changes the set of voxels over which the results are reported. This procedure can potentially introduce biases within and across analyses, so it must be motivated very clearly. It is uncommon to reject voxels like this. If the goal is to report robust estimates of central tendency and variance of parameter estimates, then why not calculate them based on median and IQR?

10) It is stated that explained variance during pRF estimation is used to weigh the contributions of individual voxels to estimated parameters. This is understandable, but we would have expected to see actual reports of the explained variance across ROIs as well. This could help readers to judge and interpret the differences observed across ROIs.

11) The stimulus aperture size comprises a very small proportion of the visual field and is also much smaller than those used in other fMRI studies of attentional modulation of pRFs. The authors should provide more discussion about this issue, particularly with respect to the generalizability of their findings. Also, it seems problematic to make the distinction between parafoveal and peripheral pRFs, given that the locations of these pRFs only differ by a couple degrees of visual angle.

12) Figure 8 shows that behavioral accuracy (proportion correct trials) was approximately 80% for the different tasks and eccentricity bins. However, a Quest procedure was used to adaptively change stimulus parameters to generate target performance levels of 83%. Thus, the finding that percent correct did not vary across tasks and eccentricity thresholds is a trivial consequence of the adaptive psychophysical procedure, and statistical analysis providing evidence for the null hypothesis is relatively meaningless. While it would be difficult to directly compare task difficulty across the three tasks, the authors could compute psychophysical thresholds for each task and test whether these are influenced by eccentricity.
