# Peer review - Round 1

Editors:
- Christian Büchel, University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- Christian Büchel, University Medical Center Hamburg-Eppendorf Germany

## Review text

DOI: [10.7554/eLife.44422.021](https://doi.org/10.7554/eLife.44422.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Dissociable laminar profiles of concurrent bottom-up and top-down modulation in the human visual cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Christian Buchel as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you can see from the comments below the reviewers found the data and the study of high interest, However, they have also indicated that they need to see more details to fully judge the validity of the claims. This refers to the details of normalization (Reviewer #2) and overall quality control issues (Reviewer #3) including the wish to see more raw data (Reviewers #2 and #3). Reviewer #2 also questions whether the task employed is a classical feature-based attention task. This would also need to be addressed. Finally, Reviewer #3 wonders if the pre-selection of voxels is statistical valid ('double dipping').

Note from Deputy Editor: eLife prefers supplemental data to be supplements to specific figures, so that all data are included in the body of the paper. Please see if your existing supplemental figures can be thought of as supplements to figures in the paper, and whether the additional data asked for in the paper can also be included in that form. You will see that some eLife papers have 2 or 3 supplements to some figures, so that the relevant additional data are grouped with the primary result. And of course, there is nothing to prevent you from just adding additional figures to the paper. We prefer that controls be viewed as an important part of the paper.

Reviewer #1:

This is the first study combining high resolution, layer resolving fMRI at 7T with a task that allows to investigate top-down and bottom-up processing in a robust and elegant task. The methodology is sound and the authors have successfully established layer resolved fMRI. Based on retinotopically identified areas they investigate how attending to a particularly oriented grating CW or CCW is represented in early visual areas (V1, V2 and V3). The bottom-up manipulation was implemented by changes in contrast. The top-down manipulation was feature attention i.e. detecting changes in bar width. In a first step the authors identified voxels in the mapped areas that preferentially responded to either orientation. They then investigated both main effects i.e. high vs. low stimulus contrast and attended vs. unattended orientation. Finally, they analyzed whether these main-effects are stronger in a specific cortical layer (deep, middle and superficial). With respect to feature based attention they observed a trend that the superficial layer showed the strongest modulation, but this was not significant (p=0.07). In contrast, the bottom up contrast effect showed a significantly smaller main effect in the middle layer. They can also show a significant interaction (i.e. layer by type of attention). In a final step they investigated whether these effects differ between V1, V2 and V3. This analysis revealed no relevant differences in the observed patterns.

This is an interesting study showing that changes in stimulus contrast are predominantly represented in middle cortical layers. The study further suggests that feature based attention shows the opposite effect, yet this was only a trend. This a clear data set and very interesting result.

The paradigm employed is in essence a 2x2 factorial design with the factors bottom-up (i.e. stimulus contrast) and top-down (feature attention). Although Figure 2 suggests that there is no interaction, I was wondering whether (i) any voxels show such an interaction and (ii) whether this interaction would be differently expressed in different layers. Along these lines, Figure 4 collapses single main effects into a difference score, which does not allow the reader to interpret the full data. I agree that this might clutter the figure, but the authors should add a supplemental figure showing for each layer the responses to all 4 conditions without subtraction as a bar graph or in other words providing Figure 2 for each of the 3 layers.

Reviewer #2:

The authors present a 7T fMRI study examining whether top-down dependent processes (such as feature-based attention) can be dissociated from bottom-up processes (difference in contrast) in the different layers of early visual cortex. Many of the conclusions appear to rely on the computation of z-scores per layer and I have several methodological questions about the quantification, some of which may undermine the conclusions (but I hope the authors can address them – my point #1). I also have some issues with the behavioral paradigm (point #2) and whether this is truly a feature-based attention paradigm. The laminar differences in the attention effect are quite small but the comparison between agranular and granular layers might be possibly interesting. However, the authors use a distinction between granular and agranular (deep + superficial) in their analysis that does not describe the results well. The attentional effects are in fact strongest in the superficial layers and weakest in the deep layers, an intermediate in layer 4. It does therefore not make much sense to average across the superficial and deep layers, and the results are actually quite different from previous studies studying spiking activity in monkeys so that one wonders if laminar fMRI using the present methodology is a valid approach.

1) The authors indicate (subsection “Quantification of laminar-specific effects of feature-based attention and stimulus contrast”) that the BOLD signal in superficial layers is stronger than in the deeper layers, which is generally thought to be caused by the direction of blood flow in cortex. However, the raw data (before normalization) are not shown, and the normalization steps that carried out to correct for these differences in BOLD amplitude remained a bit obscure. This is an important point because I suspect that the laminar profile might actually reflect the choices that are made for the normalization.

As I understand it, the authors used the magnitude of the visually driven activity for normalization when they write "we converted time courses within depth bins to z scores". Does this imply that they normalized to the magnitude of visually driven activity per layer? If so, it seems somewhat surprising to see differences in visually driven activity between the layers, and in particular when considering Figure 3—figure supplement 4 suggesting that normalization was done per layer. I do understand that this can come out, because of the comparison between the activity elicited by high and low-contrast stimuli. But it is not immediately clear to me how one should interpret that difference, which should depend on the contrast response function of the voxels, not on visually driven response. Are the results in Figure 3—figure supplement 4 are obtained by pooling across the lower and higher contrasts? If the contrast response function is flat around the contrasts that are chosen, one might expect a small difference and a larger difference if the contrast response function is steeper. However, the authors seem to interpret the slightly stronger activity in layer 4 as evidence for a feedforward effect, and I am not sure if this interpretation is supported by the data, given these normalization issues.

– These normalization issues are aggravated when one also considers the s.d. (i.e. the variability) of activity across trials, a term appearing in the denominator when computing z-scores. Again, the outcome of the analysis may now become sensitive to arbitrary choices, which have not been well described. Are these z-scores computed per condition? Or across conditions? All conditions? In one possible scenario, the z-scores are computed across all stimuli (both low and high contrast stimuli- a similar argument holds for attended vs. non-attended stimuli). In that case, the outcome of the normalization depends on the effect size of the contrast manipulation which will contribute to the overall variance of activity across trials, and hence will contribute to the denominator when computing z-scores. In the most extreme case, contrast/attention explains a large fraction of the variance, and part of the effect of the contrast manipulation would be removed during the computation of z-scores because of the normalization. I am not sure if these problematic issues arose during the analysis, but the computation of z-scores and the effect sizes before normalization are not described in sufficient detail for a proper evaluation.

– The variance in activity might differ across the layers, have the authors also investigated these effects?

– If these normalization issues can be solved, which I hope to be the case, I would like to see a thorough discussion of a rational approach to normalize for the strength of BOLD signals in the different layers, how this affects the difference in activity elicited by low and high contrast stimuli, attended and non-attended stimuli and the possible issues that can occur when computing z-scores.

– I can imagine that systematic approaches to this problem must exist. If not, the authors may be in an excellent position to propose such an approach.

– I think it should be made clear already in the Results section that the laminar profiles have been z-scored within depth bins. This is important for interpretation of the results and on my initial reading I was wondering why there was no overall bias towards the superficial layers. I would also like to see a figure showing the non-z-scored BOLD signal changes for the different attention/contrast conditions to get a better impression of the data.

– In the Discussion the authors remark "That said, any influence of spatial hemodynamics should be consistent across experimental conditions, and therefore accounted for in our calculation of bottom-up/top-down modulations via a subtraction of the responses to different contrast/attention conditions." I was a bit confused, what do they mean with a subtraction?

– Is the increase in BOLD in the superficial layers a property of the chosen EPI sequence?

– Did the degree of orientation tuning differ between the areas. If yes, did that impact on the results?

– Figure 3F: not all subjects had more activity if the stimulus was attended. Is that a reliable within subject effect, opposite for some subjects than what was expected? Or does this reflect noise in the quality of the data of individual subjects?

2) The authors frame their paradigm as a feature-based attention paradigm. However, the design of the stimulus is quite different to a typical feature-based attention paradigm and I doubt whether the participants required feature-based attention to solve the task. For example, if I'm being cued to attend to the clockwise bars, my strategy would be to fixate one of the bars of the appropriate color (e.g. white) and monitor that bar for width changes. Eye-movements weren't monitored as far as I can tell, but even if the participants did maintain fixation then this is still more reminiscent of a spatial-attention task. True feature-based attention requires the participant to attend to a feature in one part of space, and this modulates activity related to that feature in another part of space. The interpretation of the paradigm is not just of semantic interest but has a large-impact on much of the discussion and the relevance and impact of this work, so I would like to hear the authors thoughts on this.

3) In the previous Current Biology paper, the orientation-mask had quite an interesting spatial distribution in V1. Are these the same subjects? If not, was the same distribution observed?

– In that paper in V1 bottom up signals are stronger in deep and superficial and weaker in L4 – their Figure 3B. Can you explain the difference?

4) I think that the pooling across deep and superficial layers and then report "agranular layers" is misleading, given that the results for layer 4 are more similar to the deep than to the superficial layers. The dissimilarity between the low attention modulation in the deep layers in the present study with the previous monkey studies should be discussed.

– The conclusion in the Discussion first paragraph "Moreover, our results pointed to stronger attention modulations in agranular cortical layers compared to contrast effects, which were strongest in the granular layer." seems to be a bit too optimistic to me.

Reviewer #3:

This study demonstrates clear modulations of relative layer-specific activation with a bottom up (contrast modulation) and top down (attention modulation) tasks. Specifically, in early visual regions, bottom up modulation was seen mostly in middle layers and top down modulation was mostly seen in superficial layers however with less modulation in middle layers. This is a well thought out experiment that certainly collapses challenging data in a manner that comes close to convincingly revealing the hypothezised modulations, however, as detailed in the specific comments, I have concerns with the fact that no actual maps nor raw BOLD activation laminar profiles nor even selected ROIs were shown, leaving the reader completely in the dark as to the data quality. It's mentioned that because there were two task modulations and a comparison between the two, large pial vessel effects were eliminated. This, I would argue is not entirely true as the baseline blood volume not only modulates the degree of BOLD signal change but can also have a secondary effect of enhancing the BOLD signal change difference as a function of underlying blood volume. Lastly, since the contrast modulation was used to create the ROI's and then used in the analysis, this paper has the potential for falling into the statistically unsound "double dipping" trap that would elevate the effects at least for the bottom up modulations. The way around this would be to demonstrate that these differences are mappable onto the cortical layer architecture. If this cannot be done, then it is questionable whether or not the data are of sufficient quality to make any conclusive statements.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Dissociable laminar profiles of concurrent bottom-up and top-down modulation in the human visual cortex" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. As a consequence, I am delighted to say that we are happy, in principle, to publish a suitably revised version.

Essential revisions:

As you can see both reviewers still have issues with the paper. However, the editors feel that these concerns can be addressed by (i) a figure showing layer specific activation (Reviewer #3) (ii) by changing the wording as suggested by Reviewer #2 in critical parts of the manuscript, (iii) by further discussing the pooling of deep and superficial layers (Reviewer #2).

Should these revisions convince the editors, we are in principle happy to publish this paper,

Reviewer #2:

I am still a bit mixed about this paper. On the one hand, the authors convincingly addressed all issues that I had with the normalization.

On the other hand, my issue with the grouping of superficial and deep layers into an "agranular compartment" was not addressed satisfactorily. As I mentioned in my first review, the attentional effects (or the ratio with bottom-up effects) in fact seem strongest in the superficial layers and weakest in the deep layers, and intermediate in layer 4. It does therefore not make much sense to average across the superficial and deep layers. The results are actually quite different from previous studies on spiking activity in monkeys, so that one wonders if laminar fMRI using the present methodology reflects the underlying neurophysiology.

Several misleading statements remained in the revision:

– In the Abstract: "top-down modulation is significantly stronger in deep and superficial layers than top down effects", which is not shown for the deep layers but only by using the misleading grouping into "agranular layers". I suspect that the effects are driven by the superficial layers.

– Same at the end of the Introduction, final sentence.

– In reality there are no clear differences in top-down effects between the layers (subsection “Dissociable laminar profiles of bottom-up and top-down response modulations”) but it is only if a comparison (subtraction) is made to the bottom-up effects.

– This is also visible in Figure 4A, where the weakest attention effects are present in the deep layers, the strongest in the superficial layers and the granular layers are intermediate.

– Discussion section: "We have shown that, in a task where bottom-up and top-down influences are manipulated independently, the overall BOLD response can be separated into top-down and bottom-up components by examining how these effects are organized across depth." I think that this is an overstatement. The only reliable laminar difference seems to be in the bottom up response across layers.

– It should also be clarified consistently that these effects are driven by a difference in the contrast sensitivity rather than be a difference in the attention effects between layers.

What is the rationale of the grouping of superficial and deep layers? Is it the wish to replicate the non-human primate studies?

I would recommend that the three laminar compartments stay separate throughout the analysis (e.g. Figure 3E, F), and also in the Abstract and in the Discussion. It seems conceivable that in such an analysis with three laminar compartments, there is a difference in the ratio between top-down and bottom-up effects between superficial layers and the granular layers, but no such difference between the granular and deep layers. Such a discrepancy with the non-human primate work would also be a valuable outcome, and useful for future studies that plan to use laminar fMRI.

Reviewer #3:

Overall, I appreciate that the authors put in a tremendous amount of work to address all the questions from all three reviewers. I am satisfied with all the answers except this answer:

"Our revised manuscript includes three additional figures displaying raw data to allow the reader to better assess the data quality. (1) A figure showing raw, layer-specific BOLD time courses for each experimental condition and each ROI (Figure 3—figure supplement 3)"

This is a time course but not a map of actual layer activity.

"(2) A replication of our main results obtained by performing our analysis to raw data that had not been normalized, showing that the steps we took to minimize the impact of overall BOLD signal differences between layers, i.e. z scoring data within layers, were not critical to our results (Figure 3—figure supplement 5)."

This is certainly appreciated but not a map of layer specific activity.

"(3) A cross section of V1 from a representative example subject, where voxels are color coordinated based on which layer they belong to (Figure 3—figure supplement 7). We thank the reviewer for these helpful suggestions."

This is a mask and not an activation map of layer specific activity.
