# Peer review - Round 1

Editors:
- Nicole Rust, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31873.024](https://doi.org/10.7554/eLife.31873.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Integrative and distinctive coding of perceptual and conceptual object features in the ventral visual stream" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Anna C Schapiro (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This paper aims to uncover where in the brain perceptual and conceptual information is integrated. The authors compare behavioral and neural similarity amongst objects processed in visual and conceptual task contexts. They find that visual structure is represented in LOC, conceptual structure is represented in the temporal pole and parahippocampal cortex, and that perirhinal cortex is uniquely sensitive to both perceptual and conceptual information, across task contexts, suggesting that this is where conceptual and perceptual information is integrated.

The reviewers commented on the elegant nature of the study design, the stringent analysis, and how clean results were in the context of brain areas that are often difficult to get signals from (with fMRI). The paper was judged to be of broad interest and impactful.

Essential revisions:

The following issues were highlighted as items that must be addressed before publication.

1) It looks like the statistics were computed using objects – not participants – as the random effects factor, which makes it unclear if we can generalize the findings to the population. The correlation between behavioral and neural RDMs could be calculated for each individual, and then statistical testing could be done across these 16 (fisher-transformed) values. Or it may make sense to run the permutation test within each individual and then compute group statistics across the 16 zscores of the individuals relative to their own null distributions. The object-based statistics are useful, but additionally reporting these participant-based statistics will allow the reader to understand whether these findings are likely to generalize to new participants.

2) These analyses tell us about how relationships between objects are represented similarly or differently in different task contexts, but it seems like it would be useful to also report how similarly the objects themselves are represented in different task contexts. In other words, in an RDM with visual brain response as rows and conceptual as columns, does perirhinal (and perhaps temporal pole) have the strongest diagonal in that matrix?

3) There looks to be a strong interaction effect in perirhinal cortex, with its patterns of activity showing more similarity to the behavior-based visual RDM vs. the behavior-based conceptual RDM when the task is visual, and vice versa when the task is conceptual. Could the authors assess this interaction? If the authors are concerned about the assumptions of an ANOVA being violated, then perhaps a non-parametric test of an interaction can be used. The presence of an interaction does not in any way contradict what the authors are stating, but would instead add to it by suggesting that, on top of PRC representing both conceptual and perceptual information regardless of task, there is a small modulation by the task state or attentional state.

4) There is something a little odd about the depiction of the visual and conceptual RDMs in Figure 1. Why are there vertical "streaks" though the columns? Shouldn't these RDMs be completely symmetrical? Perhaps this is an artifact of the normalization procedure, which is mentioned in the methods but not described in detail. As a general point, although it is fine to scale the RDMs to use the full light/dark range, I think that it would give a better idea of the similarity space if the actual values of the similarity measures were used rather than percentile scores. Also, in the uploaded RDMs, it is puzzling to me that the values for dissimilar pairs are all 1 for the visual RDM, as this was based on a 5-point Likert scale. Surely the same value wasn't obtained for every object pairing.

5) Although I think that the procedure used to obtain behavioral measures of conceptual and perceptual similarity is a strength of the paper, it would be useful to know how these measures compare to other measures of conceptual similarity, like WordNet distances, or text corpus co-occurrence, and whether similar results are obtained when these other measures are used.

6) Although the paper focuses primarily on the ROIs, the results of the searchlight analysis will be of considerable interest to many readers and deserve more emphasis. I suggest that the brains in Figure 7A and 7B be made larger (perhaps by removing the RDMs, which take up considerable space but aren't really essential). In addition, it would be useful to plot the borders of the ROIs as outlines on the brains so that the consistency between the ROI boundaries and the searchlight analyses could be visually assessed. (As an aside, the fact that PRC is the only area showing overlap between the visual and conceptual effects in the searchlight analysis is very impressive and really underscores the strength of the effect.)

7) The results in PHC are very interesting, but the use of the PHC ROI is not strongly justified in the paper, and the implications of this result are not discussed at all. Although the paper states that PHC has been implicated by previous work on conceptual knowledge, the papers that are referenced (by Bar and Aminoff, and Ranganath) discussed a very specific kind of conceptual knowledge: knowledge about co-occurrence of objects within the same context. In my opinion, an important aspect of the current results is that they offer an important new data point in support of this idea. One possible interpretation of the PHC results is that participants bring to mind a contextual setting for the object when they perform the conceptual tasks but not when they perform the perceptual tasks. For example, "comb" and "hairdryer" might bring to mind a bathroom or a barbershop, but only when thinking about the conceptual meaning of these objects, not when thinking about their shape or color.

8) It would be useful to have more precise information about the locus of the PHC effect relative to the "parahippocampal place area" (PPA), which tends to extend posterior of PHC proper. Several papers suggest an anterior/posterior division within the PPA whereby the more anterior portions represent more abstract/conceptual information and the more posterior portions represent more visual/spatial information (e.g. Baldassano et al., 2013; Marchette et al., 2015; Aminoff et al., 2006). The functional localizer includes both scenes and objects so it should be possible for the authors to identify the PPA, and thus report whether their effects are in PPA or not, and if so, if they are in the more anterior portion.

9) I wonder if the authors could comment on whether they think the results would change if pictures, rather than words, were used for the objects in the fMRI experiment. For example, might LOC represent visual similarity structure in a task-invariant way if pictures are presented, because their visual features would be processed more automatically than if words are presented, and visual features of the objects have to be brought to mind? I was also curious if the authors could explain their motivation for using words rather than images – was it to force participants to bring to mind both visual and conceptual information?

10) It is notable that conceptual effects were limited to PRC, PHC, and TP, and were not found in other regions of the brain. What implications does this have in light of previous work that has found a wider distribution of conceptual regions? For example, Fairhall and Caramazza (2013) identified "amodal" conceptual processing in inferior temporal gyrus, posterior cingulate, angular gyrus, prefrontal regions? What about the ventral stream regions outside of LO, PRC, and PHC, like the fusiform gyrus? (I'm not actually suggesting that the authors use these regions as ROIs, but more focus on the whole-brain results and comparison to these earlier findings would be recommended.)

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Integrative and distinctive coding of visual and conceptual object features in the ventral visual stream" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) It was a great idea to put the ROI boundaries on the brains depicting the searchlight results. I'd recommend making the ROI borders a bit thicker, though, and perhaps changing their colors, to make them easier to see. The perirhinal and parahippocampal ROIs are fairly clear, but the LOC and temporal pole less so.

2) Now that the ROI outlines have been added to the searchlight results, it is apparent (Figure 10B) that the locus of conceptual decoding in parahippocampal cortex straddles the perirhinal/parahippocampal border. This fact is perhaps worth mentioning in the text. At present, the overlap with anterior PPA is emphasized, but one might equally emphasize that the overlap with PPA – and even PHC – is only partial.

3) Also, there seems to be an error in the caption for Figure 10B, which is described as depicting correlation between brain-based VISUAL and behavior-based conceptual RDMs – both should be conceptual. The label on the figure itself is different (and presumably correct).
