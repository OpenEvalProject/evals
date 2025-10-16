# Peer review - Round 1

Editors:
- David C Van Essen, Washington University in St Louis , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10163.019](https://doi.org/10.7554/eLife.10163.019)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Mouse V1 population correlates of visual detection rely on heterogeneity within neuronal response patterns" for peer review at eLife. Your submission has been evaluated by Eve Marder (Senior editor), a Reviewing editor, and three reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

The reviewers articulated a desire to see your responses to their critiques and felt you should be given a chance to revise your work. We are allowing you to submit a revision, as long as you understand that a positive outcome is not assured, and will depend on whether the reviewers and Reviewing editor feel that you have adequately revised your manuscript and/or rebutted the critiques.

Summary:

The statistics of population neuronal responses of early sensory cortices associated with animal perceptual behavior is an important issue in neuroscience. In this paper, Montijn and collaborators compared neuronal fluorescence signals from L2/3 mouse V1 with behavioral responses in a detection visual task. The reviewers think that there are interesting results but it is not clear up to what point the observed correlation between behavior and the heterogeneity measure supports the authors' claim. An important issue is that authors neglect many previous developments on the neuronal correlates in other early primary cortical areas (somatosensory cortex and auditory cortex). The paper focuses on the neuronal correlates of V1 with visual detection performance, but this is a general problem and the authors should mention this.

Essential revisions:

Reviewer #1:

1) The authors state that "for each trial took the responses of only neurons that preferred the presented stimulus orientation" (subsection “Response dissimilarity within neuronal populations correlates with detection”). This practice is extremely dubious. First, it is totally unclear how it affects subsequent analysis. Were Z-scores calculated once over all orientations or calculated for separately each orientation for those neurons that preferred it? When examining the relationship between behavior and heterogeneity, was a correlation calculated for each orientation or over all orientations?

2) The presented stimuli consist of square wave gratings with 8 different directions but a response to any orientation was rewarded. In essence, this becomes a matter of responding to a change in light level. Thus analyzing responses to oriented stimuli may result in a bias towards those neurons with inherent responses to the stimuli which obscures or masks the responses from the neurons actually involved in the discrimination of the change in intensity. Nonetheless, the authors, on the basis of Ca2 -transient measurements from ~100 L2 neurons in monocular V1, conclude that "visual perception does not correlate well with mean response strength, but is significantly correlated with population heterogeneity." This statement ought to be drastically revised to reflect that it is contingent on the ad-hoc procedures chosen by the authors, and how the correlation is calculated using data-selection procedures based on orientation, which was not part of the behavioral task.

3) Since the animal needs in principle only to respond to an increase in ambient light intensity brought about by the stimulus and since no behavioral dependence on orientation has been reported, all of the analysis concerning orientation selectivity (preferred populations etc.) is potentially irrelevant, and the logic behind this experimental design is not clear. If one were designing an experiment to test for a correlation between mean response strength and visual perception, surely it would be wise to do one's best to ensure that the neurons from which responses were recorded had response properties that were at least to some degree related to the discrimination target? While it would be equally unwise to assume that orientation selective neurons in V1 do not play a role in visual discriminations not involving oriented stimuli at their preferred orientation, the failure on the authors' side to discuss in any way the caveats associated with their experimental design and simultaneously to draw the conclusions that they do and state them as strongly as they do is remarkable.

4) The heterogeneity measure, the sum of pairwise absolute z-score differences, does not correspond to any normal usage of the word heterogeneity and is never adequately justified. For example, if all neurons respond to a given stimulus with the same fluorescence increase, the heterogeneity of that stimulus will not be zero but will depend on their responses to other stimuli. Even a trial that elicits no fluorescence change in any neuron the heterogeneity will not be zero. Since the measure is based on z-scores, it will amplify fluorescence noise in neurons that are less frequently active so that for sparse activity noise can dominate the measure, but this issue is never discussed. While it does indeed seem to correlate better than some other measures with behavior, the manuscript does not adequately explain how this measure was calculated and in any case this measure would not tell us what is going on the brain.

5) The alternative measure "instantaneous Pearson correlations" suffers from the same problems as "heterogeneity." It is improperly named as it is not a Pearson correlation. Time varying correlation measures already exist and should be mentioned; they are generally based on sliding windows (e.g. "Time-varying correlation coefficients estimation and its application to dynamic connectivity analysis of fMRI" Fu et al. 2013 or "The sliding window correlation procedure for detecting hidden correlations: existence of behavioral subgroups illustrated with aged rats" Schulz and Huston 2002).

6) The nature of the decoder used (subsection “Heterogeneity predicts reaction time”) is never explained in the main text or Methods. The extremely convoluted use of a similarity metric and p-value based on comparison to randomly shuffled data (Figure 4E) to claim that the decoder and the animal behave similarly is not a clear and honest presentation of results. The similarity metric was not explained in the Methods. There is nothing to support the statement that "the performance as a function of contrast was strikingly similar to the animals' actual behavioral performance."

7) The assertion, in the Introduction, that "a widely held assumption in computational models of vision is that neurons in distributed cortical architectures have relatively fixed roles in information coding" is a straw-man argument. The authors do not adequately characterize what this assumption of "fixed roles" means, and also fail to characterize the diverse set of existing theories and conjectures about how the visual system may function.

8) We need to see much more raw data so as to evaluate data quality. In particular, we should see supplementary movies showing simultaneous raw, unprocessed imaging data, behavior, and "heterogeneity" for ~10 consecutive trials.

9) The very large responses of some neurons with nearly 100% DF/F in Figure 1d don't seem to match the very modest DF/F of 4% over "preferred populations" in Figure 2d. Are the data in Figure 1 not representative of the full dataset? Or is the time window for averaging each trial's responses perhaps too long? The presentation, figure and analyses are unclear.

10) The first stated aim is to ask: “does visual detection correlate with mean visual response strength or other metrics?". This may be of interest if one could determine for certain that the response strength was being determined for the neurons really involved in the detection/perception required by the task. But why should we care what L2/3 is doing during this task, when it may not even be involved in generating the behavioral response?

11) The authors assert in the Introduction that "specific ensemble activation patterns reoccur across temporally spaced trials in association with hit responses, but not when the animal fails to report a stimulus." I do not understand how, on the basis of the data presented in Figure 6 and the manuscript text associated with it, that this conclusion can be drawn. The authors state: "We again split the data into miss, fast and slow response trials, and computed the correlations between response patterns from different trials separately for preferred and non-preferred neuronal populations…" What response patterns are being correlated? The Methods states that the "mean inter-trial correlations over animals" was compared. I find the link between this measure and the conventional definition of ensemble tenuous at best. Further, the calculated correlation coefficients are very low (<0.12), which does not support well the claim made above.

12) The authors describe their method for assessing the extent of slow drift in the z-plane, which they quantize into 10μm bins. It is unclear what additional effects this may have on the measured Ca2 -transients, something that would be best determined empirically using simultaneous electrophysiology. More importantly, fast shifts in the z-plane are a considerably larger problem, and these would be anticipated as the animal changes its posture or shifts fore- or hindlimb. This sort of "fidgeting" is commonly observed in advance of a rodent making a behavioural response. How the authors measured these postural adjustments is not clear, neither is the effect that these movements have on the activity recorded. It is certainly conceivable that a z-shift could move the focal plane further inside some neurons and further outside others, thereby increasing "heterogeneity."

13) Previous multiphoton Ca2 -imaging studies have shown that correcting xy-shifts uniformly across the whole image is not sufficient for motion correction in awake animals (see Dombeck et al. 2007, Greenberg and Kerr 2009). As described above, motion-associated artefacts resulting from the fidgeting of the animal around a response are not quantified and potentially important.

14) The caveat that the only neurons from which recordings were made were superficial neurons ought to have been explicitly discussed. Is it not conceivable that the correlation of mean activity with perception might be significantly higher for neurons in deeper layers?

15) How did the authors control for possible ocular torsion (twisting of the eye and retina round the optic axis) during the experiment? This would totally invalidate all analyses based on orientation if present but not accounted for.

Reviewer #2:

1) The concern is about the animal's behavior. The performances shown in Figure 1C, E are relatively low at 100% contrast; in many cases slightly different than the ones at 32%. The presence of errors at full contrast imply mechanisms other than visual detection contributing to the animal's response variability that will potentially contaminate all other conditions as well.

2) Regarding the correlation between heterogeneity and behavior, the authors claim that "…the increased spread of neuronal response strengths within a population determine the behavioral accuracy". This reviewer is concerned about how strong is the change in heterogeneity between hit and misses to support this claim. In his opinion the authors should explicitly quantify how predictive is the animal's decision from this population measure, on a trial-by-trial basis.

3) He finds very interesting the fact that the measure of heterogeneity – but not the mean population response – correlates with detection. However, as far as he understands, this would be the case in any situation in which the detection of the stimulus is represented by a population code that is not merely an increase of activity of all neurons. The mean population response is only one particular projection of the population activity (let's say, described by the vector [1 1 … 1]). If detecting the stimulus activates the neural population in any other direction in neural space, this measure of heterogeneity will increase (because some neurons increase activity while others decrease). In particular, if detecting or not the stimulus modulates the population activity in a direction orthogonal to [1 1 … 1], the mean population response will not be affected (and won't correlate with the animal's behavior). His concern is that, if this is the case, it is not heterogeneity per se that is relevant, but the presence of complex population patterns of activity that are not visible at the level of the mean response. He thinks the authors should check if there is a population signal other than the mean response that correlates with the animal's decision.

4) The authors claim that ensemble patterns reoccur upon presentation of the same stimulus. However, inter-trial correlations of population responses are relatively low (~0.11). They should explain what value they take as a reference to validate this claim and why. Correlations could increase because of reasons other than reoccurring of the same activity pattern; a more detailed analysis is needed to support this claim.

5) He believes it is necessary to explain why the authors chose this particular measure of spread in neural responses, as opposed to – arguably – more natural ones like the variance. If the variance does not correlate with behavior as much as heterogeneity does, then this might also be informative of the properties of the population code. A set of related statistics are examined in regard to reaction times (Figure 4C) but not in relation to the decision of the animal.

Reviewer #3:

Positive points:

1) Evaluated multiple metrics for stimuli detection.

2) Propose a new metric for population heterogeneity, where dissimilarly activated neurons have high population heterogeneity.

3) Data from a sufficient number of mice, 8, were collected and analyzed and the results hold across animals.

Negative points:

1) Preferred orientation and non-preferred orientation neurons are analyzed separately – this ignores potential interactions between neurons (subsection “Data processing”).

2) The preferred orientation neurons are selected using the mean dF/F0 value, however, the main result of the paper suggests that a different metric, heterogeneity, is more robust in capturing stimuli recognition; how will the analysis be affected if the same metric is used for pruning the neurons? (subsection “Calculation of preferred stimulus orientation”).

3) As defined, heterogeneity seems a reasonable metric, however, it only considers pairwise relationships between neurons; a more holistic, group-level metric should be considered, since the goal of the analysis is to discover groups of neurons.

4) Can you explain or cite the reasoning behind using the procedure in the subsection “Behavioral response predictability on single trial basis”, to compute a prediction? Can the model likelihood be used to make predictions instead?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mouse V1 population correlates of visual detection rely on heterogeneity within neuronal response patterns" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior editor) and two reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

In brief, both reviewers had positive comments about the revisions but also request minor additional revisions that will not require re-review.

Reviewer #1:

Regarding the authors’ response to Reviewer #1, comment 10: The study by Glickfeld activated PV neurons in a 1mm diameter around the injection pipettes ~up to 1mm below the V1 surface and showed that this increased the threshold for detection of both orientation and contrast by the animals. I do not see the relationship between the author's response to my question and the question. Why is it reasonably assumed that L2/3 is involved in the task that is presented?

Regarding the authors’ response to Reviewer #1, comment 11: Please change the last sentence in the Abstract to reflect the changes in terminology by removing ensembles (see below). I’m not sure what “selective and dynamic neuronal ensembles” are. Please also rephrase the first paragraph of the Discussion, which suffers from the same issue.

From the Abstract:

"Contrary to models relying on temporally stable networks or bulk-signaling, these results suggest that detection depends on transient activation of selective and dynamic neuronal ensembles."

Reviewer #2:

Single-trial population recordings in behaving animals have the potential to uncover how the dynamics of a network of neurons give rise to perception, decision and behavior. In the context of visual detection, given the activity of a population of neurons, what is the population measure that better relates with the animal detecting or not the stimulus is unknown. This study shows that in L2/3 of primary visual cortex, measures of spread of neural activity are more predictive of the animal's detection than mean-based measures. The authors did a very good job addressing the issues mentioned in the revision. I believe the paper has improved significantly both in the analysis of the data and in the precision with which the claims are expressed.

Response to my prior comments:

1) I had noted that the low performances at full contrast imply mechanisms other than visual detection contributing to the animal's decision (lack of motivation, for example). This means that test contrast trials are probably contaminated with a significant amount of trials (close to 50% for several animals) in which the animal actually detected the stimulus but didn't respond. The authors argue that heterogeneity does not reflect these other mechanisms because it's equal for both behavioral responses at full contrast. I agree with the argument and understand that the low performances might actually be diluting the effect reported in the paper. But I still would like to ask, does the distribution of heterogeneity in "No Resp" trials show any hint of bimodality, reflecting the 50% of trials in which the stimulus was in fact detected?

2) I had requested a quantification of how predictive is the single-trial value of heterogeneity of the animal's behavior. This was added in Figure 3G, H.

3) I had asked whether the reported effect of increased heterogeneity could be an artifact of the presence of complex -but well-defined- patterns of activation orthogonal to the mean activity. The authors developed an elegant new analysis to address this question by mirroring neural responses with respect to the mean and measuring its symmetry. The results show that neural responses are a bit asymmetrical, pointing to the existence of a structured activation related to visual detection, although the effect size is very small. Besides, this analysis leads to the finding that hits are more structured than misses. Finally, removal of the mean, the heterogeneity or both, allows identifying the importance of each property on hit/miss decoding. I consider the point well taken.

4) I had requested more details on the analysis of reoccurring patterns of activity between trials. The authors addressed this question by expanding the analysis of correlations between population patterns and added the corresponding controls.

5) I had asked for a deeper explanation of why they choose this particular mathematical definition for heterogeneity as opposed to others. The authors expanded the analysis of hit/miss difference for other metrics of heterogeneity and found that many lead to the same results. They mention this fact in the revised manuscript, clarifying that the main result is that measures of "spread" of neural responses are more predictive than mean-based ones.
