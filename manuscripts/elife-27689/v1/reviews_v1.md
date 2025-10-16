# Peer review - Round 1

Editors:
- Naoshige Uchida, Harvard University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27689.015](https://doi.org/10.7554/eLife.27689.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Causal role for the subthalamic nucleus in interrupting behavior" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Summary:

The authors have tested the idea that subthalamic nucleus (STN) plays an important role in interrupting or pausing on-going behavior by a surprising stimulus or threat. The authors first developed a task using self-initiated licking behavior. The authors first show that optogenetic activation of STN neurons was sufficient to pause a bout of licking. Furthermore, optogenetic inhibition of STN neurons reduced the disruptive effect of a salient light/sound stimulus on licking behavior, effectively lengthening lick bouts.

The reviewers thought that the task is a naturalistic behavior and simple yet elegant. Although the role of STN in interrupting behaviors is not very novel, it is important to test this idea experimentally. Overall, the reviewers thought that this study is important and potentially warrant publication in eLife.

However, the reviewers raised a number of concerns. In particular, it is important to quantify how halorhodopsin-mediated inhibition affected the spiking of STN neurons. Since this experiment will likely take >2 months, we reject this manuscript at least in its current form. However, if the authors can address the following essential points, we are happy to reconsider a new submission of this work.

Essential points:

1) Although the authors confirmed the effect of optogenetic activations via channelrhodopsin-2 (ChR2), they do not show any demonstration that halorhodopsin inhibited the activity of neurons in the subthalamic nucleus (STN). This is an important point to demonstrate in order to interpret the data. Were STN neurons purely inhibited? What about rebound excitations? Please address this issue by in vivo recording.

2) In Figure 1C, the authors show the effect ChR2 stimulation in the STN. Spiking of the STN neurons seems essentially continuous during the stimulation train. Does this indicate that synchronous activation of STN neurons caused persistent reverberatory activity? Please show the data after the last pulse as well so that we can see the extent at which the effect of stimulation lasts after the termination of the stimulation.

3) Figure 1H-J. If the idea is that STN can rapidly arrest behavior, why show target firing rate averaged over a 5s stimulation period? Presumably any relevant effect on target firing must be occurring within less than ~50ms or so – please show the time courses of target firing shortly after light onset instead.

4) In general, it would be important to show less processed behavioral data, which may give a clearer view of what is going on. For instance, in Figure 2, the authors show an idealized schematic of a regular lick bout, and then information on lick bout length. Please show actual lick bout timing. Examples of real bouts may be helpful, and also simply rasters and histograms of lick density over time (as if licks were spikes). Also, are the bouts very distinct from each other or is the mouse essentially licking all the time with occasional >750ms gaps that define bout boundaries?

5) Figure 3. For the surprise experiment, why use such a long laser stimulation pulse (1s) given that any relevant neural effects must be much faster? Is this related to the definition of a "bout" as involving <750ms inter-lick-intervals? In addition, it seems that it took a long time for STN neurons to be inhibited by the halorhodopsin-based inhibition, compared with the excitation by ChR2-based stimulation. This also points to the importance of characterizing the effect of halorhodopsin-based inhibition on STN neurons (point #1).

6) Figure 2—figure supplement 1B and C. Why would green light alone (YFP group) tend to interrupt behavior when such an effect was not seen for blue light alone (YFP group) in the previous experiment?

7) Halo and YFP animals showed different lengths of lick bouts in the baseline (no surprise, no laser condition, although the difference was not significant) (Figure 3D). Although surprise resulted in similar lick bout lengths in Halo and YFP mice (Figure 3E), the difference in the baseline might be problematic. Combining these results, the main result in Figure 3F could be explained by a mixture of laser itself, individual biases, and the effect that the authors are looking for (the role of STN). The authors must discuss this.

Reviewer #1:

The authors examined behavioral effects of stimulating or blocking the subthalamic nucleus (STN) activity by applying optogenetics to mice. They found (1) STN activation interrupted or paused a self-initiated licking, and (2) STN silencing reduced the disruptive effect of surprise.

1) The authors only examined the effect of STN optogenetic activation by in vitro recording and c-fos immunohistochemistry. Results of in vivo electrophysiological recordings, how STN neurons and their targets are activated by light through the fiber optics placed above the STN, are necessary.

2) Moreover, they did not show any in vivo and in vitro electrophysiological results during STN silencing by Halorhodopsin. These data are indispensable.

3) How effective is the activation or inhibition of STN neurons? Silencing of the STN induces motor abnormal behaviors such as hemiballism. Did animals show abnormal behaviors, such as hemiballism or rotational behaviors during strong silencing of the STN?

4) Why did authors use different vectors between behavioral experiments and in vitro electrophysiological experiments? They should use the same vectors and examine the effectiveness by electrophysiological methods.

Reviewer #2:

To study the function of STN, the authors used a self-initiated bout of licking as an ongoing behavior that may be modulated by STN. This is a great choice because the behavior is natural and repeatable without any learning. The role of STN was examined by local activation and inactivation of STN neurons using optogenetic stimulation. Both of the data are critical for the conclusion that "STN is both necessary and sufficient for such forms of behavioral response suppression." The effects of STN activation are clear and convincing, but I have a question about the effects of STN inactivation, as shown below.

There is no clear evidence that photostimulation of STN in Halo-expressing mice inactivated STN neurons or their target neurons (GPe/EP/SNr), unlike the data shown for ChR2-expressing mice shown in Figure 1. This may be a bit tricky because STN neurons must be spontaneously active to see any effect on the target neurons. But if a prolonged stimulation (e.g., 1 s) is used (as in the behavioral experiment shown in Figure 3), the firing rates of the target neurons should decrease. Such data are important to proceed to the behavioral experiment.

I have two specific questions.

First, how quickly can STN neurons suppress ongoing behavior? This is important to adapt to the rapidly changing environment. To address this question, I have been checking the data in Figure 2I. I assume that the blue window indicates the stimulation period. The effect of ChR2-laser diverged from the control around 100 ms after the onset of the stimulation. This looks explicit, but I am not convinced. My understanding is that the data lines are shown relative to the total number of licks within a bout of licks. Since the number of licks was smaller in ChR2-laser trials, the data lines are not presented based on the actual frequency of licks. I would simply show the cumulative number of clicks. Then, the blue line (ChR2-laser) would be lower, and the differentiation latency may be shorter than 100 ms. Another reason for asking this question is that the effects of the photostimulation on the STN-target neurons in GPe, EP, and SNr are fairly quick (Figure 1E-G) (although I cannot see the actual latencies). If these target neurons respond, say, in 2-3 ms, I expect that the behavior would be suppressed much earlier than 100 ms.

Second, I have some questions about the data showing the effect of the inactivation of STN neurons (Figure 3). According to my understanding, the photostimulation started simultaneously with the 2nd lick, and then the surprising event started after 50 ms. Is this because the authors had tried several versions and found that this temporal order was most effective? Apparently, it took a long time for STN neurons to be inhibited by this Halo-based stimulation, compared with the excitation by ChR2-based stimulation. Relevant to this question: What was the latency of the behavioral suppression in response to the surprising event?

Other specific questions and comments:

Subsection “Optogenetic activation of STN excites output nuclei”, last paragraph: How did you define 'postsynaptic cells'?

In Figure 1E-G, please indicate the time and EPSC amplitude for the example data. What was the latency of EPSC in response to the stimulation?

In Figure 1—figure supplement 1, does 'ChR2 excluded' mean that the data obtained with these stimulation sites were excluded? I presume that the stimulation effect was absent or weaker than the others. Such data may be important to support the conclusion: the stimulation affected STN, not other areas.

Data in Figure 1—figure supplement 2. Was the stimulation intensity 0.5mW or 10mW? There are some c-Fos labeled cells outside the presumed target areas. For example, I wonder if labeled cells outside SNr (K) are located in VTA.

Please indicate how many animals were used for each experiment.

Figure 2E and H indicate that the total number of bouts increased in ChR2-laser condition. Does this mean that the total number of licks increased? Any interpretation?

Figure 2—figure supplement 1 shows that the bilateral stimulation was less effective. Any reason?

Figure 3—figure supplement 1 suggests the non-selective effect of photostimulation which seems to act as another surprising event. Is it difficult to block the light from the head cap?

Figure 3—figure supplement 2 indicates that the behavioral suppression became weaker as the surprising event was repeated. I wonder if this is caused by the decrease in the sensitivity of STN neurons to the surprising event.

Was the experiment shown in Figure 3 started after the habituation shown in Figure 3—figure supplement 2? If so, why?

"Importantly, in the absence of the sound/light event we found that STN inhibition did not alter licking behavior compared to the YFP controls."

This is important, but I cannot find data.

While reading the manuscript, I had a difficulty in finding which video I should check.

Reviewer #3:

In this brief report Fife et al. present optogenetic results supporting the idea that the STN is involved in interrupting ongoing behavior; activation of STN tends to interrupt bouts of licking, while suppression of STN tends to prevent interruption of licking by surprising cues. Though limited in scope these results based on manipulations are a useful complement to the extensive literature on STN & stopping based on correlations. But it would be good to show less processed behavioral data, which may give a clearer view of what is going on.

1) (Figure 1C) Spiking of the STN neurons seems essentially continuous during the stimulation train. This seems a bit strange – is synchronous stimulation of STN neurons causing persistent reverberatory activity? Please show us when it stops after the last pulse. In any case "spikes/stimulus" seems like an inappropriate measure, since it's not clear which spikes are being evoked by which stimulus.

2) (Figure 1H-J). If the idea is that STN can rapidly arrest behavior, why show target firing rate averaged over a 5s stimulation period? Presumably any relevant effect on target firing must be occurring within less than ~50ms or so – please show the time courses of target firing shortly after light onset instead.

3) (More on Figure 1). Figure 1A: probably unnecessary these days. Figure 1B: not clear what is being shown – is this supposed to be ChR2 expression in STN cell bodies and in fibers (only) within STN targets? Probably better just to use Figure 1—figure supplement 1 as a main figure instead. Figure 1E-G: scale bar scales are not shown or given in caption.

4) (Figure 2) We are shown an idealized schematic of a regular lick bout, and then information on lick bout length, but please show actual lick bout timing. Examples of real bouts may be helpful, and also simply rasters and histograms of lick density over time (as if licks were spikes). Also, are the bouts very distinct from each other or is the mouse essentially licking all the time with occasional >750ms gaps that define bout boundaries?

5) (Figure 2) If STN arrests licking, but mice adjust by increasing the number of bouts, how long does the arrest last?

6) (Figure 2) How fast is the closed-loop control? I.e. what is the time from 2nd lick onset to laser pulse onset?

7) (Figure 3) For the surprise experiment, why use such a long laser stimulation pulse (1s) given that any relevant neural effects must be much faster? Is this related to the definition of a "bout" as involving <750ms inter-lick-intervals?

8) (Figure 3B) Schematic – it's not very clear what is what.

9) (Figure 2—figure supplement 1B and C) Why would green light alone (YFP group) tend to interrupt behavior when such an effect was not seen for blue light alone (YFP group) in the previous experiment?

10) Discussion is a bit cursory. For example it would have been helpful to discuss the fact that the results here are based on interrupting an already-started action (if this is a fair description) compared to canonical results based on preventing action initiation at all.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Causal role for the subthalamic nucleus in interrupting behavior" for further consideration at eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom, Naoshige Uchida, is a member of our Board of Reviewing Editors.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Essential points:

1) Figure 1A: It's not entirely clear what point is being made with the zoomed-in insets, and what the nuclear marker is in the YFPctrl inset.

2) Figure 1—figure supplement 1D not referenced in text?

3) Figure 2A. The illustration of blue light coming out of fibers to interrupt licking is pretty, but better would be an unequivocal mark of exactly the period of blue light illumination.

4) Figure 3C. The explanation for using "% 3-lick-bouts", rather than 2-lick-bouts as examined in prior figures, needs to be provided the first time this figure is referenced in the text rather than later.

5) Figure 3D, as above a simpler indicator of light onsets and offsets would be better than the bulb/fiber illustrations.

6) Blocking of STN activity should induce involuntary movements. Did Halo-expressing mice show any abnormal behaviors?

7) Optogenetic activation of STN neurons interrupted bout of licking. Did it interrupt other behaviors?

For the points #6 and 7, we would like to see the authors' response if the authors already have a relevant data.

The original review comments from each reviewer are appended below:

Reviewer #1:

The authors have addressed most of the previous concerns. To confirm the effect of Arch-mediated inhibition of subthalamic nucleus neurons, the authors performed in vitro experiments. Although the data in vivo is still missing, this is an important addition.

Reviewer #2:

The manuscript has been greatly improved by additional data, analysis, and figures and is an important contribution to the literature on STN and behavioral inhibition.

Reviewer #3:

The authors examined self-initiated licking behaviors of mice during optogenetic activation or inhibition of the subthalamic nucleus (STN). They used mice whose STN neurons expressed specifically channelrhodopsin (ChR2) or halorhodopsin (Halo). Optogenetic activation of STN neurons interrupted bout of licking. Inhibition of STN neurons decreased interruption of liking by surprise stimuli. They consider that the STN is necessary and sufficient for suppression of behaviors.

1) The authors did not show any clear evidence that yellow laser inhibited STN neurons or their targets in vivo.

2) Blocking of STN activity should induce involuntary movements. Did Halo-expressing mice show any abnormal behaviors?

3) Optogenetic activation of STN neurons interrupted bout of licking. Did it interrupt other behaviors?
