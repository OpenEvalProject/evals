# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, https://ror.org/03ht1xw27 Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77603.sa0](https://doi.org/10.7554/eLife.77603.sa0)

This is an important paper that describes and models an inhibitory pathway that mediates delay conditioning using cerebellar mechanisms in mice and rabbits. The manuscript provides convincing evidence for the proposed mechanisms, further supported by models.


---

# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, https://ror.org/03ht1xw27 Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77603.sa1](https://doi.org/10.7554/eLife.77603.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Feedback Inhibition Underlies New Computational Functions of Cerebellar Interneurons" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Christian Hansel (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Can the authors make the manuscript more concise, in particular, to better explain the functional role of PC-MLI interactions?

2. It would be helpful to see more comparisons between the experiments and simulation outcomes. Some have been suggested in the detailed comments.

3. The paired recordings are few in number. Can the authors specifically discuss the caveats from this?

4. Can the authors better substantiate the temporal order of PC and PC-MLI firing during CRs?

5. The methods section lacks details, even if parts have been published, there should be a summary. Some points are mentioned by the reviewers. Additionally, can the authors provide a schematic of the simulation?

6. It is journal policy to provide the entire simulation source code and configuration files on an open-source public platform, such as ModelDB, GitHub, or OpenSourceBrain. This should be done at submission time so that the reviewers can see it.

Reviewer #1 (Recommendations for the authors):

Specific comments:

Given the variability in IPSC amplitudes, how variable are the maps (Figure 3) from trial to trial? How were presynaptic PC somata located (Figure 3f)? If somata could be located, was the estimate of 1-2 PCs impinging on one MLI tested via somatic stimulation?

Figure 1c, bottom, and Figure 2c: Are the averages shown from different trials in the same cell or in different cells?

Figure 2a,b: Show representative traces for different frequencies of stimulation.

Figure 2 title: Can this be called 'Frequency-independent depression' when the extent of depression is maintained by frequency-dependent mobilization?

Figure 2e: Need a statistical test for a slope of 0.

Page 9: '…but this variability was not due to variations in photostimulation of presynaptic PCs' – This needs to be substantiated with AP probability data from light-stimulated PCs.

Page 11: Non-reciprocal connections- how many PC somata were located within the light spot that evoked IPSCs? The paired recordings are technically very challenging, yet, a sample size of 6 is too small to conclude that reciprocal connections do not exist, especially since PC-MLIs are also a small fraction.

Figure 4e: Was this analysis done on evoked or spontaneous spikes in PCs?

Figure 5b: What are the light grey and black bars?

Figure 5g and S3: The dip in MLI firing is symmetrical at about 0. This is not the case for the simulation.

Figure 5i,h: Are the curves showing averages of all the PC-MLIs recorded? If yes, show the error as well.

Figure 6: Wouldn't these results be expected given that PC-MLIs are identified based on a strong correlation to CR kinematics?

Figure 7: all data in this figure are representative. Need group data with appropriate statistics.

Page 23: "These comparisons indicate that the anti-correlated activity of eyelid PCs and putative PC-MLI arises from inhibitory feedback from PCs to PC-MLI."

This is a strong statement. Data in Supp. Figure 4 are consistent with this interpretation but they do not indicate it.

Page 23: "For trials with CRs, PCs reached 50% of their maximum response before PC-MLIs did" – Why is this indicative of earlier PC response? Responses seem to start at about the same time, with similar slopes, but MLIs show a bigger modulation than PCs. Consequently, 50% max response occurs later in MLIs compared to PCs.

Figure 9: How does the presence of PC to MLI synapses lead to lesser overall plasticity between PFs and PCs?

Reviewer #2 (Recommendations for the authors):

1) In the recordings from connected PC-MLI pairs, some parameters are pulled from very low numbers of recordings (n<10). For example, conclusions discussed on p. 5 and illustrated in Figure 1d (and following panels) are based on 7 recordings. It is understandable that it is difficult to find connected pairs, yet as a result, the statistical power is low. This should at least be discussed as a caveat.

2) Figure 5: can the computer simulation predict how many PC-modulated MLIs need to be involved to enable optimal functioning of the feedback circuit (e.g. for one target PC)?

3) Figure 5b3: how is the Gaussian distribution peaking at an x-axis value of 0.5 determined? It seems that there is a separate, distinct peak at about 0.3.

4) Figure 7: This is a very interesting figure that shows that the onset of the PC pause occurs before the peak of MLI activity. If we assume that MLI firing contributes to prolonging the pause, what then mediates the early pause component? Is that PF-PC LTD? Along those lines, is there a necessity/involvement of LTP?

5) On p. 31, last paragraph, the authors state that '…..suggested by our simulations is to require a smaller net change in excitatory synaptic input for PCs to decrease their activity to the level required to produce a well-timed CR during the CS'. This observation resonates well with the recent finding that under realistic [ca2+]o and [Mg2+]o conditions (1.2mM/1mM instead of the more classically used, but incorrect 2mM/2mM) plasticity conditions are less permissive for LTD (Titley et al., J. Physiol. 597, 2019). If correct, those findings suggest that there are plenty of activity conditions under which LTP is induced, but LTD requires a narrow range of specific temporal activity signatures. In light of this, the findings from the computer simulation are particularly meaningful. The authors might want to add this aspect to their discussion.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Feedback Inhibition Underlies New Computational Functions of Cerebellar Interneurons" for further consideration by eLife. Your revised article has been evaluated by Ronald Calabrese (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The reviewers agree that the revision has been done well and most key aspects have been addressed.

2. There are a few small changes that the reviewers suggest to improve clarity and improve the discussion.

3. The provided GitHub link provides a source dump, which is good, but as presented does not make it easy for a reader to replicate or understand the analysis or figures. It needs documentation. Can the authors provide a systematic README which explains how a user may use their code to replicate their results? Ideally this should provide scripts and how they are invoked to replicate the relevant figures.

Reviewer #2 (Recommendations for the authors):

The revised version is a delight to read. Though longer than the original submission, the authors have done a fantastic job in interconnecting the various elements (slice physiology, in vivo physiology and computational simulations) and motivating one with the other. This manuscript is a rigorous and exciting dissection of the PC to PC-MLI pathway and its role in motor learning. This manuscript will be an important addition to the cerebellar circuits literature. The authors have addressed most of my comments to my complete satisfaction.

A few issues remain and once addressed, these can be checked at the editorial level for faster acceptance:

1. Line 326 – "…timing of CRs (Figure 5b3)" – but Figure 5b shows correlations with eyelid position and not with CR timing?

2. Figure 8a and corresponding results text – line 379 – the very small suppression window in vivo during conditioning is at odds with the other results (slice, simulation, in vivo intertrial intervals). Is this window in 8a wider than the duration of the merged signal at time 0?

3. Lines 401-406: This part is a little confusing as the authors state that the intertrial intervals were analyzed to avoid large changes in activity during conditioning. Then they also state that large changes in activity during pauses and bursts show the suppression. So why wouldn't that be seen during conditioning as well? Are pauses and bursts seen during the intertrial interval similar to those during the conditioning?

4. I couldn't locate the n for the number of PC-PC-MLI pairs analysed.

5. Figure colors: Perhaps indicate the CS window with a different color since the grey masks the grey of SEM in some cases (Figure 9-Figure suppl. 1 is one example). Also, in Figure 10, it is difficult to discern the dark blue and black. Red and green are not color-blind friendly.

Reviewer #3 (Recommendations for the authors):

The authors have only partially addressed my prior concerns and referred to potential future work when at least some discussion of these points would have been appropriate.
