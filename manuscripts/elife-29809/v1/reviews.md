# Peer review - Round 1

Editors:
- Jean Laurens, Baylor College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29809.021](https://doi.org/10.7554/eLife.29809.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Distinct spatial coordinate of visual and vestibular heading signals in macaque FEFsem and MSTd" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor (Richard Ivry).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper studies the representation of visual and vestibular heading in primate cortical areas MSTd and FEFsem. Besides providing novel data for FEFsem, an area for which a heading representation has only recently been described, the main point of the paper is a comparison of references frames (eye-centered vs head-centered) in the two areas and for the two modalities. Results show that the representation is mostly modality specific (eye-centered for optic flow and head-centered for vestibular signals) in both areas. All three reviewers were very positive about the interest of the question, the quality of the experimental approach and the overall presentation of the data.

Essential revisions:

The conclusions of the manuscript strongly depend on the DI statistics. The DI seems suitable for separating between head and eye reference frames in the sense that responses in head reference frames will tend to have smaller values than responses in the eye reference frame. Therefore, it supports the main conclusion of the manuscript. However, the reviewers are concerned that estimation of the DI might be noisy and the exact values of the DI might be biased depending on how well the tuning curves are estimated. Biases in the estimation of the DI might be especially problematic when comparing between conditions. For example, could the difference in DI between FEF and MSTd (Figure 2B and C) result from the difference in the response size of the cell and not a true difference in the reference frames? Could the difference between pursuit and fixation (Figure 4C and D) be a result of the difference in the magnitudes of the responses – or the difference in the way the DI are computed? One way to partly overcome this would be to calculate, when possible, the DI from the population average rather than for each cell separately. Population averages would also provide further important information about the magnitude and pattern of the responses. Alternatively, the authors could perform bootstrapping with their data to assess the statistical significance of DI, or perform simulations to support the use of DI.

The statistical analysis in subsection “Behavioral context for heading estimation” is incorrect. The authors use a one tailed paired t-test; however, a paired t-test may be used only when comparing values that were recorded in the same neurons. Here the authors compare neuronal responses recorded two weeks apart. These can't originate from the same neurons since they author don't perform chronic recordings; therefore the authors can't use a paired t-test. Furthermore, there is no justification for using a one tailed test in this context. The authors should use the correct statistics (two-tailed unpaired test) and update their results accordingly.

Regarding the investigation of smooth pursuit and motion parallax: the most interesting condition is missing. Theoretically, motion parallax is needed to distinguish rotational and translational components of self-motion in the optic flow field. Rotational components are introduced by smooth pursuit. To test the ability of the visual system to deal with rotational components based on flow analysis, researchers have used the paradigm of simulated pursuit, in which the observer fixates while the flow simulates both a translational heading and a rotational pursuit (see for example, Bremmer et al., 2010). It is conceivable that a much larger impact of motion parallax could be observed in a simulated pursuit condition. The reviewers realize that this condition was not part of the experiment, and do NOT think it is necessary to provide this data. However, the limitations of the study in that regard should be discussed. It may explain why excluding motion parallax from the visual stimuli has limited effect on FEFsem and MSTd's tolerance of the eye rotations (subsection “Motion parallax cue in the visual optic flow”).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Distinct spatial coordinate of visual and vestibular heading signals in macaque FEFsem and MSTd" for further consideration at eLife. Your revised article has been favorably evaluated a Reviewing editor along with three reviewers, and overseen by Richard Ivry as Senior Editor.

The reviewers have evaluated the revised version and found that all their comments have been addressed except for one point. The reviewing editor has helped draft the following summary of how we would like to see this issue addressed.

The concern is that the DIs computed in the eccentric fixation and smooth pursuit tasks might be biased towards 0 for cells with noisy tuning curves. Therefore, cells with a lower response magnitude would have a lower signal to noise ratio and the DI would be biased towards zero. As a result, differences between the visual and vestibular cases could result from differences in the magnitude of the responses and not from differences in the coordinates. The bootstrapping methods performed by the authors would not eliminate this bias since the bootstraps would also contain the bias. To test if the DI statistics are biased, the authors could perform simulations in which they construct noiseless tunings curves with a DI of one and then add different levels of noise, calculating the DI in the exact same way they calculate the DI for neurons.

If it turns out that DI is biased, it would still be possible to show that this bias does not affect conclusions. This would entail controlling for the magnitude of the response. For example, calculate the DI as a function of the tuning magnitude. This would allow you to examine the following:

1) Cells with the same magnitude of response have a DI close to one during visual condition and close to 0 in vestibular condition.

2) Cells with the same magnitude of the response during fixation and pursuit have a different DI.

The authors could also use Figure 3 as a control.

To sum up, the authors should, as a first step, run simulations to check if the DIs are biased towards 0 when the signal/noise ratio is low. If this is the case, they should demonstrate that it does not affect their conclusions (for instance using the approach suggested above).
