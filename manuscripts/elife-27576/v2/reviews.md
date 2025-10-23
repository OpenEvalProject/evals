# Peer review - Round 1

Editors:
- Nicholas Turk-Browne, Princeton University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27576.037](https://doi.org/10.7554/eLife.27576.037)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The large-scale organization of shape processing in the ventral and dorsal pathways" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Nick Turk-Browne as the Reviewing Editor and David Van Essen as the Senior Editor. The following individual involved in review of your submission agreed to reveal their identity: Hans Op de Beeck.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Note that some of the essential revisions will require additional experimentation and/or significant new analyses. You may thus decide to forego resubmission should these requirements prove onerous. Moreover, as new results will be generated that could impact the conclusions, it remains possible that your manuscript will be rejected upon revision, should you choose to resubmit.

Summary:

This manuscript describes two fMRI experiments assessing shape processing in the ventral and dorsal pathways. Using two forms of scrambling, the authors assess BOLD responses in voxels and ROIs as a function of image coherence, with positive slopes reflecting greater responses to more shape information (i.e., lower levels of scrambling). They then examine how these slopes change as a function of position along the anterior-posterior axis, and find a dissociation between ventral (increasing then plateauing slopes) vs. dorsal (increasing then decreasing slopes) streams. Moreover, shape information in both ventral and dorsal streams correlated with object recognition behavior. The authors conclude that both ventral and dorsal streams contribute to perception, despite differences in how they code for shape information.

There was consensus that this study was rigorous, with two experiments, two manipulations, thorough analyses, good data reporting, and clear writing. Moreover, the findings were robust and interesting, speaking to an issue of fundamental importance about which there has been relatively little work.

At the same time, the reviewers raised several important and consistent concerns that would need to be addressed before a decision about publication can be reached. Below these concerns are described via constructive suggestions about how the manuscript would need to be improved to fare well in the next round.

Essential revisions:

1) Many of the claims relate to what has been learned about the nature of object representations in the dorsal stream. However, the reviewers question whether the approach taken here is adequate to assess representational content. In particular, the use of univariate methods and image scrambling to assess shape information was considered indirect and outdated, compared to the multivariate (or even adaptation) methods used in prior studies. Admittedly, the difference between scrambling techniques across streams (i.e., reduced shape sensitivity in dorsal stream in Experiment 2) speaks to what is being coded, but this was not viewed as sufficient. In particular, this can speak to selectivity for shape and/or identity, but does not address what features are being represented. Although adaptation would not be possible to consider with the current design, I see no reason that a representational similarity analysis couldn't be performed. There were 2 and 4 (Experiments 1 and 2) repetitions of each stimulus, which would allow a cross-correlation of the raw pattern of BOLD activity over searchlights or ROIs for each stimulus with its own repetition(s) and with the other stimuli. Average diagonal vs. off-diagonal correlations would provide an index of shape coding, and this could be examined at different levels of scrambling. Moreover, how this index changes over the longitudinal axis could provide confirmation of the piecewise regression results, and also about differences between scrambling techniques across streams. Finally, second-order correlations of the correlation matrices would speak directly to the question of the similarity between ventral and dorsal stream representations. Other multivariate approaches could achieve the same goals, and the authors are experts in this class of techniques, but something along these lines is necessary.

2) Related to questions about representation, it was unclear which exact properties of the objects were affected by scrambling. For example, reduced sensitivity to diffeomorphic scrambling in the dorsal stream is interpreted as evidence of coding for the presence of a single shape rather than identity. However, this kind of scrambling affects many other features (e.g., curvature, texture, etc.), all of which could be potential explanations. The convex hull analysis is a good start, but the authors should provide a more comprehensive, perhaps computational analysis of the features present in the stimuli from both experiments at different levels of scrambling.

3) This paper builds on a long history of related studies. The reviewers felt that this history and its implications were not adequately presented. This includes the classic work by Grill-Spector and others – and whether the current results would (or would not) have been predicted from it – as well as the more recent work using multivariate methods (e.g., by Bracci and colleagues). Many of these papers are cited, but a more in-depth weighing of the prior literature, discussion of the new findings and why they are novel in this historical context, and consideration of theoretical implications (including for previous conclusions) is needed.

4) The conclusion about differences in the representational gradient of ventral and dorsal streams depends on how the streams are defined. For example, the authors seem to go as anterior as possible in the dorsal stream and obtain a decrease in shape sensitivity. Would a decrease not be observed in the ventral stream if its end was likewise extended further, say into the hippocampus or anterior temporal lobe? Alternatively, if the dorsal stream was defined more conservatively, wouldn't the gradient match the ventral stream? The root concern is that it is unclear whether the gradients are fundamental, organizing properties of these streams, or at least partially artifacts of how the analysis was conducted. The authors need to better justify their definition of the streams, and address this limitation.

5) Relatedly, the anterior-posterior axis is defined simply as Y coordinates. Given the brain's curvature, especially in the dorsal stream, these coordinates do not reflect neural distance. The authors should calculate alternative distance metrics, for example tracing along the surface of inflated cortex from calcarine to central sulci, re-performing their piecewise regressions, and either replacing the existing analyses or reporting one in the supplement.

6) Object recognition performance is almost perfectly correlated with scrambling. As a result, the neural correlations with object recognition almost perfectly mirror the baseline relationships to scrambling. Thus, it is unclear what these results add to the story. More problematically, it is unclear whether neural activity is driven by scrambling or recognition. These can be dissociated, as Grill-Spector did with training, but that hasn't been done in the present manuscript. At a minimum, this issue should be highlighted in the Discussion; better would be an analytical solution to dissociating these factors.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The large-scale organization of shape processing in the ventral and dorsal pathways" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior Editor), Nick Turk-Browne (Reviewing Editor), and one of the original reviewers.

The manuscript has been improved considerably and we plan to accept it if you can address a couple of remaining issues:

1) In light of the block design and mixing of exemplars, the added multivariate analysis is non-standard. Please acknowledge this more thoroughly before presenting the results, including by explaining how this differs from standard RSA over exemplars (which will be more familiar to readers).

2) Please also clarify your interpretation of the multivariate findings. Insofar as these regions represent exemplars and scrambling gradually destroys exemplar identity, why does collapsing over exemplars work at all? What aspects of the exemplar-general representations at each level of scrambling are similar? There are potentially uninteresting explanations, such as that scrambling changes the spatial extent of the image (especially for box scrambling). If you cannot rule out such accounts or provide a more parsimonious explanation, you might consider re-calibrating how much emphasis these findings receive and/or moving them to supplement. At a minimum, this analysis needs more motivation and interpretation.

3) It would be more informative to use Box Scrambling and Diffeomorphic Scrambling as subtitles rather than Experiment 1 and Experiment 2.
