# Peer review - Round 1

Editors:
- Ranulfo Romo, Universidad Nacional Autónoma de México Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29226.020](https://doi.org/10.7554/eLife.29226.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cortical response states for enhanced sensory discrimination" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and coordindated by myself as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Alfonso Renart (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this letter to offer you an opportunity to respond to the serious issues identified by the reviewers. At this point, we ask that you write back with a detailed plan to address the essential points raised below and provide a time frame for the completion of these tasks. Your response will then be considered by the Board and the reviewers who will the issue a binding recommendation.

The reviewers found your research topic of interest for understanding the roles of variability of neural activity in sensory encoding and perception. That said, the reviewers and I found the way this was addressed was not especially novel: there was a general lack of depth in the analysis surrounding variability aspects. The reviewers and I would have liked to see a deeper connection between how variability shifted with high/low activity and the decoding performance. At this stage of your work, I am not sure of whether you would be able to address the reviewers' concerns. However, given the interest in the topic, we wish to learn how you could satisfy the reservations of the reviewers.

Essential revisions:

1) Baseline subtraction. Responses in the low pre-stimulus condition (LPSC) are stated to be smaller than in the HPSC. The rasters in Figure 1BC show a moderate effect of the stimulus in shaping the activity of the neurons, compared to spontaneous fluctuations. The higher rates in the HPSC can thus be due to higher activity in the baseline (by construction). It would be nice to know:a) What is the magnitude of baseline-corrected evoked responses.b) What is the relative magnitude of (baseline-subtracted) evoked responses compared to spontaneous fluctuations.

The decoding analysis in Figures 4 and 5 could also be done with baseline-subtracted responses.

General point being that since activity changes quite a bit in the absence of the stimulus, a simple way to understand what is the responsibility of the stimulus over the evoked responses is to baseline subtract.

2) Dependence of the effect on difficulty. There are two things that shape performance: stimulus difficulty and, as shown by the authors, pre-stimulus activity (PSA). What is the relative contribution of each?

The authors provide very little information on this issue. In Figure 3B,D we see an example of a session with lower performance for 10° than for 5°. We assume this is not a representative session. And then when combining across sessions, the overall performance is normalised away. It would be useful to know just performance depends on difficulty.

The effect of PSA is presumably added on top of this. But does its magnitude change for the two difficulties. We currently can't tell because we only see normalised performance. For this quantity, the effect of PSA is smaller for 10°. Is it really smaller, or is it only smaller relative to the increased performance for easier trials?

3) Decoding accuracy vs performance. In Figure 5A, we see that performance of the decoder, even with only 1 neuron (I'm guessing averaged across sessions/monkeys?) is ~ 0.82. That's quite high. Again, the limited info we are given is that the monkey performs at ~ 70%? Is this really true that a single neuron does consistency better than the animal?

4) Shuffling the data (removing correlations) leads to an overall decrease in performance. This is interesting, but not really explored. It suggests that the neurons that authors are simultaneously recording have typically negative signal correlations. Is this really true? This is surprising because in primate V1, one might assume that nearby cells would have similar tuning curves, which, in the presence of net positive correlations (Figure 5B) would presumably have led to a situation where correlations were detrimental. Can the authors clarify what's going on?

5) LFP analysis. Seems puzzling to look at power in different bands on a phenomenon that appears intrinsically transient (brief evoked responses). Can the authors just look at changes in evoked LFP? Both PSA and evoked responses can be evaluated at the level of the LFP. It would be interesting to do so. Furthermore, it appears to be the only 'global' (or at least more global than the single spikes) signal that the authors record, so it can help clarify some of their claims (see below) on the spontaneous fluctuations being locally generated. Related to this, concerning the Crist-grid arrays, how far are the tips? Can we learn something about the local/global nature of the signal by comparing LFP across electrodes?

6) Local/Global fluctuations. Several places (Discussion section), the authors make a contrast between the type of fluctuations that they analyse (which they say are local, and even that they originate in the local circuit!!) and 'global' up/down fluctuations. But what is the evidence behind these local/global claims? One would need to record a 'global signal' (either a local ePhys signal at different distant locations, or wide-field imaging) and show that it is weakly correlated with a particular local signal to make these claims. Do we have any information about the global state of the cortex, or at least the visual cortex? How do we know the global (in the sense of being correlated across the recorded neurons) signal the authors record and analyse, is not correlated with a similar signal a few mm away? Unless some evidence is provided, the statements about local/global nature and origin of the signal analysed seem unfounded.

7) Last paragraph of the Discussion section: The authors write: "Altogether, our results demonstrate that the variability in pre-stimulus cortical activity is not simply noise but has a dynamic structure that controls how incoming sensory information is optimally integrated with ongoing processes to guide network coding and behavior." This statement is puzzling. What does it mean it is not simply noise? A starting point would be to show that it cannot be predicted by anything, but the authors do not do any analysis of this type. Maybe they mean that the fluctuations are not uncorrelated across cells? The authors should either be more accurate/explicit, or remove this sentence. It's a not-so-good ending for a nice study!)

8) The changes in the probability of correct detection (PCD, Figure 5A) are very modest, especially compared to the actual conditioned (high vs low) performance of the animal in the detection task (Figure 3). This is sort of a letdown, perhaps suggesting that FLD is insufficient to capture the main effects, or that simply the number of neurons are too small. In any event, while the effects are certainly statistically significant the take home message from Figure 5 is not overly impressive.

9) The noise correlation vs coding results are puzzling. The noise correlations are higher in the high state than the low state (Figure 5B), and the PCD is higher in the low state than the high state (Figure 5C, left). This seems ok However, when the spike trains are trial shuffled, artificially removing the noise correlations, then PCD (as computed from the Fisher linear estimate) actually decreases. Thus, the excess noise correlations in the high state are deleterious to coding (Figure 5C, left, red vs. blue), yet the complete absence of correlations is also deleterious to coding (Figure 5C, blue, right vs left). This suggests that either how the structure of the covariance changes is very important, and shuffling trials is very different than the decorrelation from high to low, or the shift in response gain is more impressive than any correlation change.

The authors are completely aware of this (subsection “Cortical state influences encoded information”) and they conclude that the main effect is that the low state has a higher gain/sensitivity (Figure 5D). That is fine, except then the whole paper now loses steam. The higher sensitivity to punctate inputs in the low state compared to the high state has been shown in the somatosensory system (Fanselow and Nicolelis 1999; Sachdev, Ebner, and Wilson, 2004). Further, the authors recently published a related manuscript in cerebral cortex (2016) that dissected coding in terms of up and down states, and gain changes were critical there also. But those results were in cat and did not consider animal behavior during a task. The current manuscript may be the first demonstration of this in awake primate V1.

In the end, while the correlation and variability analysis is important for the evaluation of the FLD, the state dependent changes in variability seem less important for the ultimate shift in discrimination.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for sending your article entitled "Cortical response states for enhanced sensory discrimination" for peer review at eLife. Your article is being evaluated by two peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Richard Ivry as the Senior Editor.

The reviewers had a favorable response to the revision. There were a few, relatively minor raised by one of the reviewers that I think should be addressed.

1) There are no labels in the Supplementary figures which allows one to identify them

2) Although it is a good idea to do the pupil analysis, I don't think that showing the (lack of) relationship between the pipil diameter and the pre-stim baseline is good enough evidence that the changes pre-stim activity are local. Pre-stim baseline and pupil diameter are two different signals with presumably different time-constants etc. I think it is fair to conclude that changes in arousal as indexed by pupil diameter do not seem to explain the changes in pre-stim baseline. However, in order to conclude that the pre-stim signal is local one would have to measure it at distant cortical locations and show that as distance grows, the correlation between the different pre-stim baselines decreases. I would thus suggest that the authors re-phrase the last sentence of subsection “Pooling neurons improves the predictability of behavioral responses” and first sentence of the eleventh paragragh of the Discussion section. Sorry for being picky but the local-global nature of this signals is quite important and I don't think sloppy statements in this regards have room here.

3) Discussion section. I don't think the authors can say this, as attention in their task is uncontrolled.

4) Results section. I may be missing something, but in my opinion what Figure 1—figure supplement 4 shows is that the baseline subtracted evoked response is larger with low pre-stim activity than with high pre-stim activity, NOT that stim-driven fluctuations are smaller than evoked fluctuations (and in any event this last finding would not imply non-linearity…).
