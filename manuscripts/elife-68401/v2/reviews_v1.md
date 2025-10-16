# Peer review - Round 1

Editors:
- Nanthia Suthana, University of California, California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68401.sa1](https://doi.org/10.7554/eLife.68401.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Discrete ripples reflect a spectrum of synchronous spiking activity in human association cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. While the reviewers agreed the authors have an opportunity to contribute important findings related to memory, and high-frequency/spiking activity in humans they felt that the claims of ripples as discrete events was not supported. Further, they suggest increased transparency with regards to the possibility that these events may not be ripples but rather high frequency oscillatory events that reflect spiking activity. Further suggestions for revisions are below.

Essential revisions:

1) The results as-is do not support the claim that ripples are discrete events. The reviewers suggest the authors include additional analyses to demonstrate that ripples are discrete events or instead remove these claims and report on the findings/characterization of these high frequency events and their relationship to spiking activity and memory.

2) To unambiguously demonstrate that ripples are discrete events, the authors could generate a plot of the distribution of detection features, such as binned ripple power of the LFP electrodes, which would presumably need to be bimodal. If, as would be expected from the rodent literature and the results of this study, the authors instead observe a long-tailed distribution, the data would clearly demonstrate that these are not discrete events. If so, rather than fighting to prove the "discrete" nature of ripples, it would be more productive to embrace the variability in event sizes and take a more "signal detection" -style approach to this challenge. In line with this approach, methods have been developed which first model the noise of the signal and use this to set a somewhat less arbitrary threshold for event detection (Yu et al., eLife 2017), which demonstrate that events far smaller than would have been detected using traditional thresholds are likely to be biologically meaningful.

3) In addition to using more sensitive detection methods, the authors can ask how results, such as phase coupling or spiking modulation, vary over different sizes of events, and perhaps identify features that can inform less arbitrary detection thresholds for future work. Further, it would be extremely useful to see how the different sizes of LFP events are differentially detectable/reflected in the iEEG signal. For instance, it would be informative to know what proportion of events detected in the iEEG coincide with events in the LFP, and how this varies over a range of detection thresholds applied to each type of recording.

4) The title of Figure 1 would suggest that the authors will demonstrate the discrete nature of ripple events, however, the examples and analyses in this figure do not address this question. Unless the authors can show that there are clearly bimodal distributions underlying ripple events, It would be preferable to set aside the "discrete" claim throughout the manuscript and instead use this figure to address the detection methodology and show the characteristics of ripples in iEEG and LFP over a range of detection thresholds.

5) Also regarding Figure 1, it is unclear how much of the findings showing differential engagement of ripples/HFA on correct vs incorrect retrievals are re-prints of previously published findings, replication of previous findings with new or additional data, or new findings. Please specify.

6) An illustration like Figure 2A with much more detail and quantification would be extremely helpful for developing a better intuition for how to evaluate the resultant data. For instance, is a single iEEG contact consistently directly above, and exactly the same size as, the MEA, as suggested by Figure 2A? Where do the MEA electrode tips tend to lie in relation to cortical layers? Additionally, it would be critical to specify exactly how the spatial layout of electrodes, and the brain areas targeted, varied over the individual patients.

7) Regarding figures 2 and 3, more analyses of how often events detected in the iEEG would coincide with events detected in the LFP and/or cross-correlograms of the time of peak power for each event would be useful instead or in addition to the current approach of applying event detection in one data type and then plotting the continuous measure from the other datatype. In addition, it would be useful if the authors reported, in the text, the amount of variance for each relationship, not just whether a regression is significant. For example, in Figure 2c, the signal from a local LFP electrode captures ~36% of the variance in spiking rate, while the signal from the iEEG electrode captures ~1.4% of the variance. The authors are making claims about iEEG reflecting the LFP or spiking, and it's important that these claims be quantified with the strengths of the relationships, not just whether they are significant or not.

8) Regarding figures 2-4, would it be possible to glean more statistical power by capturing the variability of events within each patient as well as the variability across patients by using linear mixed-effects models for the summary statistics such as those shown in Figure 2D, F, H, etc? These models generally provide a much better way to describe relationships when large data samples have been collected from multiple subjects.

9) With regards to the quantification of the strengths of the relationships, it might be helpful if the authors quantified the same relationships across the spatial extent of the MEA. That might allow them to estimate the fall-off of predictability with distance on short length scales, which would give them a first order prediction of what they might see on the larger scales of the distances from the iEEG contacts to the MEA.

10) Additional raw data examples (similar to Figure 2B or 4A) including the full LFP band signal from several MEA sites (not only the 80-120Hz filtered traces) would be useful to add into the supplementary figures. In particular, it would be informative to be able to compare the full LFP signal to the full 1-200Hz iEEG trace.

11) In the experiment, authors assigned a randomly correct response time to 'pass' trials and categorized these 'pass' trials as incorrect. The randomly assigned response time smear out the effect of vocal-locked responses of incorrect trials. It might be one reason underlying the difference between incorrect and correct trials. Authors perhaps can include only the 'intrusive' trials as incorrect trials and see how the result look like.

12) The authors found that the amplitude of ripple events reflected the local spiking activities which was consistent with results from a study by Logothetis et al. showing that the gamma activity of LFP is related with local single unit activities. How could the authors distinguish the difference between their ripple activity and Logothetis's gamma activity?

13) What is the difference between iEEG ripples and LFP ripples? Do they differ in amplitude? Do they come from the same origin? I suggest adding details as to how they differ.

14) The micro arrays were placed within the expected resection area. I understand the potential damage to the brain if it is placed in a healthy area. However, how do the authors think it affects the results? It perhaps would be difficult to perform any control analyses given the current dataset. Maybe the authors can pay some lines in the discussion.

15) About the criterion of defining ripple events: In the methods part of 493-495, the criterion was already liberal compared to rodent studies. The authors however took an even more liberal criterion in another analysis (line 503-507). Perhaps the authors should call these events gamma bursts instead of ripples.

16) When performing the pairwise phase consistency analysis, they assigned the maximum PPC computed over the duration of each iEEG ripples as the LFP 80-120 Hz PPC for that iEEG ripple. It seems that they have a hypothesis that the PPC of LFP 80-120Hz which does not satisfy as ripple criterions is comparable with PPC of LFP ripples. I however did not find the supporting data.

17) I think the authors should be more transparent about the possibility that a portion of their defined "ripple" events may not in fact be ripples but high frequency activity events that relate to spiking activity. I suggest renaming these events to "ripple-like" and adding relevant discussion on this topic.

18) While the authors acknowledge the limitation of their ripple detection methods, they go on to argue in their conclusions that their results provide evidence that human ripple activity are thus more variable and exist on a "continuum of amplitudes and scales". I was not convinced by this argument since it is also possible that many of these events are simply not ripples and rather could be high frequency events that reflect spiking activity.

19) The statement "neural activity in the human cortex is organized into dynamic, discrete packets of information" seems out of place and not directly related to what the study is attempting to show. I suggest removing it or rephrasing.

20) Very difficult to evaluate Figure 2 since the legend is an exact copy from figure 1. Please revise.

21) It would be nice if the authors can include how many "ripple" events overlapped with IED events.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Ripples reflect a spectrum of synchronous spiking activity in human anterior temporal lobe" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Claims that ripples reflect discrete events should be removed or further analyses should be completed and results included to support this conclusion.

2) Simultaneous recording of LFP and iEEG, and the associated findings are a major strength of the study and should be further highlighted throughout the manuscript.

Reviewer #1 (Recommendations for the authors):

The manuscript is much improved and the authors have done a nice job responding to reviewer concerns. The added analyses, including the investigation of medial temporal and anterior temporal ripples as well as LFP-IEEG ripples are a nice addition. Further the authors have added important language acknowledging the variability in features of human ripples as reported and potential differences between those found in rodents. I think the community would benefit from the revised manuscript and recommend publication.

Reviewer #2 (Recommendations for the authors):

In their revised manuscript, Tong et al. make a solid case to link neural spiking with patterns of oscillatory activity recorded at the local field potential and intracranial EEG levels. They have softened their claims about discrete packets of activity, and instead focus on establishing relationships between the different neural recording approaches over a range of event sizes and detection thresholds. We have two major suggestions to improve the clarity of their manuscript.

First, while the authors have moved away from focusing on whether ripples can be considered discrete events, this claim still comes up in several prominent places (including in the titles of their first Results section and figure) and continues to cause confusion. The authors now claim equally or more strongly that ripples exist on a continuum, which seems contradictory and incompatible with the claim of discreteness. The claim of discreteness is not central to the important message that these events are meaningful, that they can be detected by the various recording modalities, and that they reflect underlying neural spiking activity. Given this, it would likely be best if the authors simply remove all claims of discreteness. However, we also appreciate that the authors have included distributions of ripple features and can show that these can appear bimodal. If the authors truly want to demonstrate discreteness, further explanation of Figure 2-Supplement 4 is needed as well as more prominent positioning of this result in a main figure and further analysis of the events detected by this method. Indeed, if this bimodality is truly robust, then an improved detection method would use the dip in the distribution as the detection threshold for each session/subject for all subsequent analysis. Further, this detection approach could/should then be compared to the more traditional thresholds.

Second, the authors note several times throughout the manuscript that a particular challenge in understanding ripples is the range and variety of detection methods used (for instance, lines 34-36). This is absolutely true, but a perhaps even more critical challenge is the difficulty of comparing ripples detected by the two major recording techniques – LFP for rodent work and iEEG for human work. Critically, the authors are particularly well-positioned to shed light and improve our understanding of how the LFP and iEEG signals relate to each other, and they should incorporate this point as a major strength of their study throughout their manuscript.

Reviewer #3 (Recommendations for the authors):

Thanks for authors' efforts on the revised manuscript. Questions proposed during the first round were carefully taken care of by authors. The manuscript was also properly revised.
