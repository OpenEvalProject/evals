# Peer review - Round 1

Editors:
- Jörn Diedrichsen, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83196.sa0](https://doi.org/10.7554/eLife.83196.sa0)

This valuable and technically highly demanding paper combines intra-cortical stimulation and large-field-of view optical imaging to study the forelimb representation in two macaque monkeys. The authors provide convincing evidence that reach-to-grasp and reach-only tasks only activated restricted subset of the forelimb area (as revealed through stimulation). While these results are consistent with the idea of clusters of neural activity that correspond to different forelimb actions, the evidence that this particular claim, as the discussion points out, remains incomplete.


---

# Peer review - Round 1

Editors:
- Jörn Diedrichsen, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83196.sa1](https://doi.org/10.7554/eLife.83196.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Neural activity is spatially clustered in motor and dorsal premotor cortex" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Wim Vanduffel (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The evidence for "clustered" activity is incomplete. It is not clear whether there is convincing evidence that only a small part of the arm/hand representation is activated. Showing that the non-active regions can be activated by other actions would have been the most direct and convincing evidence here (see main comment 1. from both reviewers 1 and 2).

2) Both reviewers also point out that the comparison between activation and stimulation data (which is the unique feature of this dataset) is rather superficial and both reviewers saw a lot of potential here.

Reviewer #1 (Recommendations for the authors):

This paper describes the neural activity, measured by intrinsic optical imaging in reach-to-grasp, and reach-only conditions in relation to the Intra-cortical micro stimulation maps. The paper mostly describes a relatively unique and potentially useful data set. However, in the current version, no real hypotheses about the organization of M1 and PMd are tested convincingly. For example, the claim of "clustered neural activity" is not tested against any quantifiable alternative hypothesis of non-clustered activity, and support for this idea is therefore incomplete.

The combination of intrinsic optical imaging and intra-cortical micro-stimulation of the motor system of two macaque monkeys promised to be a unique and highly interesting dataset. The experiments are carefully conducted. In the analysis and interpretation of the results, however, the paper was disappointing to me. The two main weaknesses in my mind were:

The alternative hypotheses depicted in Figure 1B are not subjected to any quantifiable test. When is an activity considered to be clustered and when is it distributed? The fact that the observed actions only activate a small portion of the forelimb area (Figure 5G, H) is utterly unconvincing, as this analysis is highly threshold-dependent. Furthermore, it could be the case that the non-activated regions simply do not give a good intrinsic signal, as they are close to microvasculature (something that you actually seem to argue in Figure 6b). Until the authors can show that the other parts of the forelimb area are clearly activated for other forelimb actions (as you suggest on line 625), I believe the claim of cluster neural activity stands unsupported.

The most interesting part of the study (which cannot be easily replicated with human fMRI studies) is the correspondence between the evoked activity and intra-cortical stimulation maps. However, this is impeded by the subjective and low-dimensional description of the evoked movement during stimulation (mainly classifying the moving body part), and the relatively low-dimensional nature (4 conditions) of the evoked activity.

Many details about the statistical analysis remain unclear and seem not well motivated.

Figure 1B: What does FL (gray area, caption) stand for? I can't see that the term is defined.

Line 158: I gather that unsuccessful trials were repeated. What were the repetition rates in the three conditions? Was the big and small sphere (here listed as one condition) also varied in a pseudorandom manner?

Line 223: I gather from this that the movement elicited in the ICMS was judged qualitatively by the two experimenters, but no EMG / movement kinematics was recorded as in the overt behavior. Did you make any attempts to validate the experimenter's judgement against objective recordings? Could you calculate inter-rater reliability or did the two experimenters interact with each other during the judgement?

Line 260: The baseline was either the first frame or the initial first four frames. How did you decide when to use which method? The statement "to increase signal-to-noise ratio" is somewhat cryptic. Increase in respect to what? Baseline subtraction clearly needs to be done in some form or the other. If you wanted a stable baseline, why not take the entire period before cue appearance?

Line 264-266. When you state: kernel = 250 or 550 pixels and low pass filer 5 or 15 pixels does this refer to the data from the two different monkeys? How were these values decided?

Line 278: If you do another baseline subtraction here, is the baseline subtraction on line 260 not superfluous? When did you use 5 and when 9 frames?

For the fMRI crowd, could you add here how pixel darkening and brightening relate to blood flow changes and blood oxygenation changes?

Line 305: Your nomenclature of cells / ROIs is somewhat confusing. What was the motivation to spatially average pixels across each cell/ROI instead of entering all pixels into the clustering analysis? What do mean by "Spatially matched cells"? Was co-registering not something that was done on the entire window?

Line 312: How big was the grid in horizontal and vertical dimensions for each monkey? Is this where the 1700 / 2249 numbers come from?

Line 313: A distances metric is defined to be zeros to itself, dist(A,A) = 0. The correlation of A with itself is 1. Do you mean to say that you used 1-max_correlation, or that you used the correlation as a similarity metric?

Line 323: My guess the point of this analysis is that the total distances decrease with an increasing number of clusters (and the correlation increases with an increasing number of clusters). So, fitting a line assumes a linear relationship between these two variables. When you say "The longest of those orthogonal lines identified the optimal number of clusters" why are the lines orthogonal? By longest – do you mean the largest deviation between the linear fit either above or below the line? This would pick either an especially good or bad parcellation. Or did you look at deviations above or below only?

Line 327: In the methods, we have 3 conditions – in the results 4. Which one is correct?

Line 370: Is the darkening appearing at 1s an artifact of the measurement or real? At least for the posterior border, it looks like it follows exactly the border of the window.

Line 451: "that shifted and expanded across the time series" – is there a statistical test for the claim that the activity region shifted?

Line 462: To what degree is the fact the activity averaged over the entire window remains stable simply a consequence of the high-pass filtering applied to each image? High-pass filtering basically removes the mean across the entire window, no?

Line 466: What is meant by "domains"? Activity clusters?

Line 5E: The analysis here involves statistical testing within each session, and then averaging activity estimates across sessions, subject to an arbitrary 50% threshold for statistical significance within the session. I cannot see a good motivation for this awkward type of analysis. If you want to consider trials a random effect, I would recommend calculating a statistical test for all trials across sessions combined. If you want to consider sessions as a random effect, then calculate a t-test across the 8 repeated activity estimates per session – this analysis also automatically takes the variability across trials into account. Or is there another reason why you chose this baroque style of analysis that is mentioned?

Line 474: "organization of domains was more similar across conditions within an animal than for the same condition across animals". See Ejaz et al. (2015). Nature Neuroscience, for a similar observation in human fMRI motor maps.

Line 483: The overlap analysis is unfortunately quite dependent on the threshold.

Line 494: form → from?

I am not sure what I am supposed to learn from the cluster analysis. It is entitled "Clustering time courses recapitulates spatial patterns of activity" – likely referring to the similarity between Figure 6a and 6b. As the clustering partly depends on the magnitude of the signal at the time points presented in Figure 6a, what is the alternative? Is this similarity more than expected by chance?

Line 527-546. The overlap between the maps is very hard to interpret, as it is highly dependent on the threshold procedure applied, which is somewhat arbitrarily chosen (see above). Even random maps of a certain size would overlap to some degree, and even identical "true" maps don't overlap completely due to measurement error. An overlap of 0.5 has no intrinsic meaning. It would probably be more informative to report the correlation between unthresholded maps, and compare this to a noise ceiling, where you correlate the maps of one condition across sessions.

Reviewer #2 (Recommendations for the authors):

Chehade and Gharbawie investigated motor and premotor cortex in macaque monkeys performing grasping and reaching tasks. They used intrinsic signal optical imaging (ISOI) covering an exceedingly large field-of-view extending from the IPS to the PS. They compared reaching and fine/power-grip grasping ISOI maps with "motor" maps which they obtained using extensive intracranial microstimulation. The grasping/reaching-induced activity activated relatively isolated portions of M1 and PMd, and did not cover the entire ICM-induced 'motor' maps of the upper limbs. The authors suggest that small subzones exist in M1 and PMd that are preferentially activated by different types of forelimb actions. In general, the authors address an important topic. The results are not only highly relevant for increasing our basic understanding of the functional architecture of the motor-premotor cortex and how it represents different types of forelimb actions, but also for the development of brain-machine interfaces. These are challenging experiments to perform and add to the existing yet complementary electrophysiology, fMRI, and optical imaging experiments that have been performed on this topic – due to the high sensitivity and large coverage of the particular IOSI methods employed by the authors. The manuscript is generally well written and the analyses seem overall adequate – but see below for some additional analyses that should be done. Although I'm generally enthusiastic about this manuscript, there are two major issues that should be clarified. These major questions relate mainly to potential thresholding issues and clustering issues.

1) The main claim of the authors is that specific forelimb actions activate only a small fraction of what they call the motor map (i.e., those parts of M1/PMd that evoke muscle contractions upon ICM). The action-related activity is measured by ISOI. When looking a the 'raw' reflectance maps, it is rather clear that relatively wide portions of the exposed cortex are activated by grasping/reaching, especially at later time points after the action. In fact, another reading of the results may be that there are two zones of 'deactivation' that split a large swath of motor-premotor cortex being activated by the grasping/reaching actions. (e.g. at 6 seconds after the cue in Figure 3A, 5A). At first sight, the 'deactivated' regions seem to be located in the cortex representing the trunk/shoulder/face – hence regions not necessarily activated (or only weakly) during the grasping/reaching actions. If true, this means that most of the relevant M1/PMd cortex IS activated during the latter actions – opposing the 'clustering' claims of the authors. This raises the question of whether the 'granularity' claimed by the authors is:

Threshold dependent. In this context, the authors should provide an analysis whereby 'granularity' is shown independent of statistical thresholds of the ISOI maps.

Dependent on the time-point one assesses the maps. Given the sluggish hemodynamic responses, it is unclear which part of the ISOI maps conveys the most information relative to the cue and arm/hand movements. I suspect that timepoints > 6 s will reveal even larger 'homogeneous' activations compared to the maps < 6s.

In fact, Figure 5F (which is highly thresholded) shows a surprisingly good match between the different forelimb actions, which argues against the existence of small subzones that are preferentially activated by different types of forelimb actions -the main claim of the authors.

2) Related to the previous point, the ROI selections/definitions for the time course analyses seem highly arbitrary. As indicated in the introduction, the clustering hypothesis dictates that "an arm function would be concentrated in subzones of the motor arm zones. Neural activity in adjacent subzones would be tuned for other arm functions." To test this hypothesis directly in a straightforward manner, the authors could use the results from the ICM experiment to construct independent ROIs and to evaluate the ISOI responses for the different actions. In that case, the authors could do a straightforward ANOVA (if the data permits parametric analyses) with ROI, action, and time point (and possibly subject) as factors.

3) More details about the transparent silicone membrane should be provided: How implanted? How maintained? Please provide pictures at the end of the 9 and 22months periods.

4) Figure 1D: Are the yellow circles task cues that the monkeys saw? If not, what were the different cues (Reach, Grasp, Withhold)? Were precision and power grip (and reach?) trials similarly cued?

5) For the MEG activity a total of 14 27gauge wires were inserted in 7 muscles. This sounds rather invasive. Did monkeys tolerate this easily? Were local anesthetics used? How deep were the wires inserted in the muscle? How did one prevent the monkeys grabbing these wires?

6) The large FOV was illuminated using 2-3 LEDs. Was illumination uniform throughout the FOV? If not, can this lead to inhomogeneous sensitivity?

7) Pixel values were clipped, if I understood correctly, at either 0.3 SD or 1 SD from the mean. This significantly changes the dynamic range of these pixel values. Are results different without clipping?

8) An arbitrarily p<0.0001 statistical threshold was used. Why was no correction for multiple correspondence performed as one collects data from ~ 600k-1400k pixels (yet without considering the masks)?

9) What is the reason for obvious edge effects in the withhold condition (Figure 3A, 3F) and apparently also the precision grip condition (Figure 5A: 1.1-3.5sec)? Is this artifactual?

10) How are the ROIs defined (cfr major point 2)? They differ in size and location between analyses (e.g. Figure 3 vs Figure 5/S1). Please discuss.

11) I find it a bit counter-intuitive that the same color-code (i.e. black values) is given for 'activations' in panel 3G and 'deactivations' in panel 3H. Why not using red and blue instead? Along the same vein: activations in the time-courses are negative (reflecting the darkening). It would be instructive for the non-experienced reader to either add activation/ suppression on the figures (above and below zero in Figures 3I and J and 5C), or to invert the Y-axis.

12) Line 426: Figure 5K does not exist.

13) Line 520: It is argued that the unsupervised cluster analysis, which is quite interesting, is similar in both monkeys. However, this is not obvious from the data: neither in the spatial domain (Figure 6B vs S2B) nor in the temporal domain Figure 6C and S2 C, especially the blue plots. In fact, the clustering data from monkey G reveal a rather widespread, uninterrupted pattern arguing against the 'cluster hypothesis' of the authors. This should be discussed in more depth.

14) Figure 7A: It is unclear which analysis was done. Is this simply giving 3 different colors to each pixel – indicating 1) precision > baseline; 2) reach > baseline 3) both > baseline (for the left panel)? Why not performing straight (pair-wise) subtractions?
