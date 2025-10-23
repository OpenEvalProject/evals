# Peer review - Round 1

Editors:
- Yoshinao Kajikawa, The Nathan S. Kline Institute for Psychiatric Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29086.024](https://doi.org/10.7554/eLife.29086.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The rate of transient beta frequency events predicts impaired function across tasks and species" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Sabine Kastner as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study shows that beta band signals appear as short beta events using human MEG and mouse LFP in barrel cortex, and investigates how apparent change in beta band power and somatosensory detection/attention relate to the event features (i.e. event rate, duration, spectral width, amplitude and timing) within individual trials of tasks. Results show that the event rate of beta consistently correlates with sensory outcome and beta power, and particularly recent events are the strongest predictors.

All reviewers agree with the novelty and potential importance of findings documented in the manuscript. Though well written, there are many issues that need clarification, and there are several concerns that should be addressed.

Essential revisions:

1) The study's conclusions are not constrained as long as it is not documented from which neural populations beta events are measured. Enhanced transient beta event rates in a neural population that is not relevant for the near threshold sensory detection would have a fundamentally different functional meaning than a reduced event rate in a neural population that is essentially encoding task relevant information. But the current manuscript version does not disambiguate from which neural populations these events were measured. It is unclear from which sensor level or deep sources the beta events in the human datasets originate, nor is it reported whether the beta events in barrel cortex stem from neural recording sites that were overlapping the stimulation site or not, or from sites with evoked responses to the stimulation.

Since there are more than 300 sensors measured in the human datasets it might be safe to assume that only a very small portion of them are measuring activity from neural circuits necessary for efficient preparation of the detection response. The enhanced beta event rate may thus be dominated by activity from neural populations that interfere with the task, including from sensory or language related areas, from motor related areas or from prefrontal areas where beta activity may signify activation rather than inhibition. In this situation, it seems necessary that the authors report whether event rates changes were differentially observed in those recording/measurement sites that are apparently task modulated as opposed to those not task modulated.

Thus, the manuscript should show information about locations of MEG sources and LFP recordings. If signals were from the hand area of somatosensory cortex and barrel cortex, then somatosensory responses to finger taps and whisker deflections are expected. Additionally, those sensory neuronal responses could be susceptible to prior beta events, similarly to behaviorally-indicated sensory detection. In human attention tasks, it is also possible to see beta band of dipole in foot area acting differently from beta band in hand area depending on the cue in each trial.

In a similar vein, it would be helpful to know whether the beta event rate enhancement was more a frontal / motor preparation related effect, or a sensory association cortex effect.

2) While the unconventional analysis approach to beta events is timely and interesting, it comes with the risk of "relabeling" something we already know with novel terminology.

The starting point of the manuscript is the hypothesis that neural activity in the beta frequency band is best described as bursts. While there is certainly some evidence that supports this assumption, it would be good if the authors could also provide some key evidence for this in the current manuscript. Whereas the (implicit) alternative model used by the authors appears to be a model with stationary oscillatory amplitude, it may be more useful here to consider an alternative oscillation-based model with dynamic amplitude modulations.

There are at least two further analyses that may adjudicate burst vs. dynamic amplitude accounts. First, the authors could provide histograms of Hilbert-transformed amplitude envelope data. If there are two regimes ([no-bursts + noise] and [bursts+noise]), then this should result in amplitude distributions (histograms) with bimodal features (in the clearest case: a separate 'bump' at the participant-specific burst amplitude). Second, the authors may look at the degree of phase-preservation between successive time points as well as between successive bursts. Under a dynamic amplitude account, one would expect consistent phase relations between successive time points / successive "bursts". In contrast, the bursting account, as far as I understand it, would predict phase independence between beta "oscillations" at successive time points and bursts.

3) A related issue regards the concern that epochs with prominent (and largely sustained) beta oscillations may be wrongfully classified as epochs with high burst rate. Noise (as well as dynamic amplitude fluctuations) may tip the beta estimates above and below threshold, resulting in multiple "bursts" (e.g., high burst rate) in the authors' analysis. This appears particularly a concern given that most inter-burst-intervals (Figure 9) indeed appear to occur within the range of few millisecond only. Have the authors considered imposing a minimum interval between successive bursts (and/or a minimal amplitude relaxation between successive bursts)? Would the same results be obtained?

Figures 5 and 9 (duration ~ 100 ms and intervals of <50 ms) together suggest that many bursts occur as doublets of about 250 ms, or triplets. Is that so? If yes, there should be more to characterize, like the timing of doublets. It may be noted that 250 ms or less is about the duration of the prestimulus period described as when beta events are effective in modulating sensory detection.

In addition, Figure 9 shows the interval distributions do not differ between behavioral outcomes. It looks inconsistent with that more beta events occur in miss trials than hit trials.

4) For comparison, it appears key to also include outcomes of regular power analyses when relating neural activity to behavioral performance, as in Figure 7 (for the 1s pre-stimulus epoch) and Figure 8 (power as a function of time). Are events features (rate) really better predictors of performance than conventional power estimates?

5) The authors limit analysis to the beta frequency range, but in the discussion mention alpha and gamma bands. One might expect these frequency ranges to be modulated as well at least in a fraction of sensors and recording sites. Why did the authors not add a brief summary analysis on whether similar findings as the beta event rate changes might be obtained with alpha and gamma ? In that way one immediately can discern whether the findings have clear frequency specificity, or whether similar effects can be expected in other bands with clear power spectral peaks. Either of these results would be highly informative.

If the authors find this analysis would exceed the scope of the study, the discussion on alpha and gamma should be shortened and instead a discussion of the possibly different functional roles of the beta frequency (sub)ranges is included to discern better why the analysis concentrates on this band and whether the authors suggest that the band represents some homogeneous underlying sources (or not).

Also, there is evidence that rolandic alpha oscillations also predict somatosensory performance and are modulated by somatosensory attention. Have the authors considered extending their analyses to this frequency range?

6) What was the proportion of trials in each dataset with at least one event (the inclusion criteria) in correct and error trials? Without this information, it is difficult to discern how important the beta events would be to predict trial-by-trial performance. A discussion of the overall effect size considering this number would be very interesting to readers – this is particularly relevant with regard to the stimulation approaches that would want to utilize event like stimulation protocols.

Do the curves in Figure 8 (i) derived from all trials or a fraction of trials that had beta events? Event rate can be derived in both ways. Blue and red curves in the figure should be derived from all detected and non-detected trials respectively.

Which trials were used to derive the threshold in Figure 4? All Hit, Miss, FA, and catch trials?

Would the strength of the correlations look very different when including these zero event trials as zero's and using Spearman instead of Pearson correlations?
