# Peer review - Round 1

Editors:
- Howard Eichenbaum, Boston University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.01982.018](https://doi.org/10.7554/eLife.01982.018)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “CA1 cell activity sequences emerge after reorganization of network correlation structure during associative learning” for consideration at eLife. Your article has been favorably evaluated by a Senior editor (Eve Marder) and 3 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments from the three reviews to help you prepare a revised submission.

This manuscript uses imaging to examine activity dynamics generated in area CA1 of the hippocampus while animals learn a conditioned eyeblink response. Since the US and CS are separated in time, they must be linked by neural activity in the intervening period. The authors find that relatively uncoordinated activity in CA1 reorganizes into a reliable sequential firing pattern that spans the time between CS and US, which they propose bridges this time interval. This paper offers two main contributions. First, observing these firing patterns during eyeblink conditioning expands the range of behavioral paradigms where sequences are observed, emphasizing their generality and hippocampal involvement in linking time-separated events. Second, the authors directly observe how sequential activity emerges over training. They find parallel changes in the structure of spontaneous correlations, implying changes in functional connectivity of the hippocampal network. While as the authors note, correlations do not definitively establish the nature of these changes, it does point towards redistributed functional interactions.

There were, however, several concerns and recommendations by the reviewers that should each be addressed in a revision:

1) The measure of learning – the trial on which the peak conditioned eyelid response is observed – is not intuitive and crude. It might be expected that the magnitude of the eyelid response might continue to grow long after learning, so a measure of when the first reliable CRs occur likely provides a more sensitive measure of initial learning. An even better approach would incorporate the sophisticated learning curve analysis used by Wirth et al. (Science, 2003) which tracks correct learning responses and would likely allow you to use eyeblink magnitude directly without setting an arbitrary threshold for CR or no-CR. This is viewed as important because you use the trial on which learning occurs to make conclusions about whether time cells precede or follow learning.

2) The reliability and temporal decoder scores are not intuitive. Reviewers had no idea whether a score of “3” is highly reliable or just statistically significant but a small effect. And it's not clear what statistical tests were used to generate p-values shown for these findings.

3) Why did the K-means analysis only test 2-4 clusters? Perhaps there are many?

4) It is not clear what the analyses of inter-trial-interval (ITI) correlations mean. Is this aimed to test whether time cell firing sequences are a “synfire” chain? How does correlation during the ITI imply anything about firing chains during the trace interval? A closer connection between connectivity and time cell sequences might be made if they were able to show that high ITI correlations occur only in strong time cells and not in other cells that do not exhibit temporally specific trace period firing.

5) A major strength of the paper is that it follows changes through training. These data could help address whether learning increases reliability of pre-existing responses already tied to specific time points (i.e., reinforces a pre-existing sequence), vs reconfigures activity by shifting peaks in time or generating new responses. The data point strongly to reconfiguration but some more in-depth analysis addressing this could be a nice addition. For example: Figure 3A shows an interesting single-cell example where firing occurs at similar times across trials, but more reliably after learning. The reliability score will tend to collapse differences in probability at the same time, vs changes in timing (or reliability of timing) of peaks, into a single number. It would be useful to address these separately – e.g., comparing the variability in peak times for each neuron across trials, before and after training and/or comparing the change in peak time. Does learning primarily affect mean timing of activity, variability of timing across trials, or reliability at a specific time point?

6) A central focus of the manuscript is changes in activity dynamics before and after learning. Figures 2B and 2D show clear strong peaks sequentially ordered across the CS-US interval. The heading of section 3 could be taken to mean that this structure is absent before learning. However, the data in Figure 3—figure supplement 1 shows clearly observable, albeit less complete, activity sequences. A side-by-side comparison of these data could help the reader evaluate the strength of learning-dependent effects. The reordering shown in supplemental panels A/B is a particularly striking learning outcome.

7) The authors have a substantial dataset of spontaneous activity, analyzed for noise correlations but not temporal structure. Depending on strength and timing of events, sorting by peak response could lead to apparent ordering of even randomly occurring activity. As a baseline, it would be useful to know the results of using the same sorting analysis for epochs of spontaneous data. Beyond this, it may even be possible to ask whether spontaneous activity gains any temporal structure resembling the stimulus-triggered sequences after training.

8) The authors describe the emergence of novel temporal sequences starting at the beginning of the CS (tone presentation) and evolving in time in the “learner” group and relate them to learning. For comparison, they use a control group that underwent a “pseudo-conditioning”. However, if one of the main goals is to investigate the neuronal dynamics underlying learning, the best control for the learner group should be the non-learner group that underwent the exact training protocol, but failed to learn the association. The authors should include the non-learner group in all of the relevant analyses and in the comparisons with the learner group. This could get them one step closer to understanding the neuronal correlates of learning.

9) The cellular activity was imaged at 11-16 Hz resulting in 70-90 ms-long frames. This is a quite large time interval for cellular physiology. How do the authors relate the long calcium transients to the spiking activity of the neurons occurring within such transients? Many possible different neuronal sequences can occur within each of the 7-8 frames composing the 600 ms interval between CS and US. For instance in Figure 2D frames 5 and 6 contain neurons 25-35 and 36-52, respectively which can fire in multiple different sequences within frames 5 and 6, across trials undetectably. Also, scale and units should be added to the x-axis (Time) in Figure 2D.

10) Were the neurons that were active during the tone after training also active during the tone in the pre-training? How do we know the neuronal sequences in CA1 bear any meaning to this task? Does the non-learner group also exhibit neuronal sequences bridging the CS and US?

11) How do the authors explain that the noise correlations (NC) declined toward the end of the session? Were the animals maintaining equal attention to the task toward the end? The authors should also refer and relate to the trial by trial correlations in spiking activity of place cells in spatial environments that show steady increases with more training (e.g., Dragoi and Tonegawa, 2013, eLife; Cheng and Frank, 2008, Neuron).

12) In Figure 3D, the Trace group shows average Reliability Score values around 3. In Figure 3F, the same variable ranges from a minimum of ∼1 in early trials to a maximum of ∼1.4. The numbers in 3D and 3F don't match. Please explain the difference.

13) What is being displayed in Figure 5A? Please explain in more detail. In Figure 7A, spikes should not go in time beyond the time of air puff delivery as they could by emitted in response to the air puff. In Figure 7B, late in the training session (bottom), if increased correlations should be considered a mark of learning, why do they decline with more training? Please explain. Figure 6–figure supplement 1; why are NC values in trace conditioning group of mice that fail to learn in the beginning as high as the maximum NC values of learners later during training? Figure 3H; color coding and labeling is not entirely clear. Are these different image frames at which the cell responded?

Also panels D and E in Figure 3–figure supplement 1 have no legend. These appear to show the number of cells active for each time epoch before learning. Again a direct side-by-side comparison of this data before and after learning could be valuable.
