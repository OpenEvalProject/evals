# Peer review - Round 1

Editors:
- SP Arun, https://ror.org/04dese585 Indian Institute of Science Bangalore India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81701.sa0](https://doi.org/10.7554/eLife.81701.sa0)

In this study, the authors investigate whether neurons in the inferior temporal (IT) cortex encode features relative to the absolute gravitational vertical, by recording responses to objects in varying orientations while monkeys viewed them sitting in physically rotated chairs. They find surprising and compelling evidence that neural tuning is unaffected by physical whole-body tilt, which cannot be explained by any compensatory torsional rotations of the eyes. These findings are of fundamental importance because they indicate that IT neurons may play a role not only in object recognition but more broadly in physical scene understanding.


---

# Peer review - Round 1

Editors:
- SP Arun, https://ror.org/04dese585 Indian Institute of Science Bangalore India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81701.sa1](https://doi.org/10.7554/eLife.81701.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Object representation in a gravitational reference frame" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Tirin Moore as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The high tuning correlation between the whole-body tilt conditions could also occur if IT neurons encoded the angle between the horizon and the object in the object-with-horizon experiment, and/or the angle between the object and the frame of the computer monitor which may potentially be visible in the object-alone conditions. The authors will need to think carefully about how to address this confound, or acknowledge clearly that this is an alternate explanation for their findings, which would also dilute the overall novelty of the results. One possibility could be to perform identical analyses on pre-trained deep neural networks. Another could be to quantify the luminance of the monitor, and maybe also how brightly lit other objects are by the monitor in their setup. Finally, object-orientation tuning could be compared in the object-alone and object-in-scene conditions.

2) The authors should provide more details about the torsional eye movements they have measured in each animal. For instance, have the authors measured torsional eye rotations on every trial? Is it fixed always at {plus minus}6{degree sign} or does it change from trial to trial? If it changes, then could the high tuning correlation between the whole-body rotations be simply driven by trials in which the eyes compensated more?

3) A lot of details are dense in the manuscript. The authors should clearly present their control analyses and also the correlation analyses reported in the main figures. Please refer to the specific comments in the individual reviews for details.

Reviewer #1 (Recommendations for the authors):

In addition to the comments in the public review, It would also be good if the authors can quantify the overall tendency of the population in some way, rather than reporting the proportions of neurons that show a high correlation in the two reference frames. For instance, is the average tuning correlation in the absolute gravitational reference frame stronger than the average tuning correlation for the retinal reference frame? Are the proportions of neurons encoding the two reference frames different in the two experiments?

Specific comments:

In Figure 1a, the object orientations given are -50{degree sign}, 0{degree sign}, and +50{degree sign}, but in figures 1c and 1d, we can see that orientations go up to 100{degree sign}, in both directions. For these bigger rotations, do the objects penetrate the ground surface? Can the authors show more object orientations?

Figure 1a: please rearrange the columns to show the object rotating consistently in one direction (CW or CCW). For instance, swap the leftmost and rightmost columns in the stimuli.

Figure 1e, f – Can the authors quantify the shift from 1c and 1d explicitly? In line 102, it says the shift is about 20o. Is there any variability in the magnitude of shift across trials/neurons etc? If so, can the authors explain it clearly?

Figure 1,3: The Cyan and pink triangles are not explained clearly at all. The authors should elaborate on this in the Results and in the figure legends.

Figure 1e, f, i, j – We understand that x-axis values are estimated from monkey tilt and torsional rotation. Can authors show some details on torsional rotation, as in is this observed for every trial? Is there trial-to-trial variability here? Are there any trials, for which there is complete compensation by ocular counter-rolling? Though it is mentioned in the supplementary section (line 548), it is not very clear, what is meant by the comment "For all the data from both monkeys".

Figure 2c, d – I suggest the authors move panels c and d to supplementary material, as it is not central to the arguments. Can the authors explain the matched analysis in detail on how it was done?

Line 135 – It says a sample of 99 neurons, but in lines 136-138 while giving the % of each set of neurons, the denominator is 53. Please clarify.

Figure 3: Since there are two neurons shown in this figure, label them as Cell 1 and Cell 2 in the figure itself. Also, it would be better to explicitly mention, which one of the figures 3c or 3e, has the x-axis inferred.

Line 476: Materials and methods: Provide the details of recording sites – left/right hemisphere, probe, and data acquisition process.

Methods: Can the authors show one full set of example stimuli indicating all object orientations used in each experiment?

Reviewer #2 (Recommendations for the authors):

– The data is presented in a very compact form right now. For both Figure 1 and Figure 3, I would have found helpful a figure showing the responses of a cell to the 5 repeated presentations and showing 'each of the stimuli' (and monkey physical orientation) presented for each condition in the gravitational and retinal reference frame comparisons.

And to show such a plot (possibly in Supplementary data) for more example cells. A huge amount of work went into collecting this data, and I think it would really help to bring readers closer to the raw data through more examples and a complete and hand-holding presentation format (even if takes up more pdf pages).

– For plots of single-cell tuning curves, error bars indicating SEM would be helpful.

– The result of the decoding analysis, that one can build decoders for both the gravitational reference frame and the retinal reference frame same-different task, is interesting. To what extent does this depend on specialized mechanisms? If one were to attempt the same decoding using a deep neural network trained on classification by presenting the same images presented to the monkey in the experiment, could one achieve similar decoding for the gravitational frame same/different task? Or would it completely fail?

– Additional discussion of the relation of current findings to known functional architecture of IT would be helpful. For example, the recordings were from AP5 to AP25. Were any differences observed across this span? Were cells recorded in object or scene regions of IT (cf. Vaziri and Connor)?

– Also, how do results relate to the notion of IT cells generating an invariant representation? If IT cells were completely rotation invariant, then all the points should cluster in the top right in their scatter plots, and that is clearly not the case. Is the suggestion then that in general IT cells are less invariant to rotations than to translations, scalings, etc., and furthermore that this selectivity for rotation angle is represented in a mixed reference frame, enabling robust decoding of identity and orientation in retinal and gravitational coordinates? A more explicit statement on the relation of the findings to the idea of IT encoding a hierarchy of increasingly invariant representations would be helpful.

Reviewer #3 (Recommendations for the authors):

1. The authors employ a correlation analysis to examine quantitatively the effect of tilt on orientation tuning. However, it is not clear to me how well the correlation analysis can distinguish the two reference frames (retinal versus gravitational). For instance, for the data in Figure 1, I expect that the retinal reference frame also would have provided a positive correlation although the orientation tuning shifted as predicted in retinal coordinates. Furthermore, a lack of correlation can reflect an absence of orientation tuning. Therefore, I suggest that the authors select first those neurons that show a significant orientation tuning for at least one of the two tilts. For those neurons, they can determine for each tilt the preferred orientation and examine the difference in preferred orientation between the two tilts. Each of the two reference frames provides clear predictions about the expected (absence of) difference between the preferred orientations for the two tilts. Using such an analysis they can also determine whether neurons tested with and without a scene background show effects of tilt on orientation preference that are consistent across the scene manipulation (i.e. without and with scene background). Then the scene data would be useful.

2. I have two issues with the population decoding analysis. First, the authors should provide a better description of the implementation of the decoding analysis. It was unclear to me how the match-nonmatch task was implemented. Second, they should perform this analysis for the object without scene background data, since as I discussed above, the scene data are difficult to interpret.

3. The authors pooled the data of the two monkeys. They should provide also individual monkey data so that the reader knows how consistent the effects are for the two animals.
