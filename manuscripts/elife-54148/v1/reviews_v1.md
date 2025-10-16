# Peer review - Round 1

Editors:
- Inna Slutsky, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54148.sa1](https://doi.org/10.7554/eLife.54148.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In many brain areas, mean firing rates of neurons are regulated by sleep-wake cycle. However, how this local homeostatic regulation is linked to a global homeostatic process determining sleep pressure remains unknown. Based on empirical and modeling work, the authors propose that global sleep homeostasis arises from a spatial and temporal integration of local activities at the level of microcircuits. This study implies that homeostatic processes, integrating the history of activity at the level of local networks, may provide intrinsic time-keeping signals that can be used to calculate global sleep need.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Sleep homeostasis reflects temporally integrated local cortical neuronal activity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. While all the reviewers appreciate the high quality of the data, they think that the findings are not conceptually new. The results are not qualitatively different from the established state-dependent regulation of mean firing rates and model-based predictions are not proposed.

Reviewer #1:

The paper focuses on the neuronal mechanisms that underlie sleep homeostasis. It proposes that the process which determines the need for sleep, so called process S, is not affected directly by sleep or wakefulness, but rather by deviations of local neuronal activity from a set point. The paper presents concrete mathematical models for the dynamics of process S in terms of neuronal firing rates and off periods, and shows that they could account for vigilance states and electrophysiological data collected from 6 mice over 48 hours (including a period of sleep deprivation). Thus, the paper suggests that sleep homeostasis is directly determined by intrinsic neuronal mechanisms, rather than by external cues. The proposed model for sleep homeostasis could have important implications and novel predictions for future studies on sleep regulation. Nevertheless, the fact that a model based on firing rate deviations could fit the data is not very surprising, and unexpected observations or predictions are not described, limiting the significance of the work for a wide audience. My comments relate more to the level of interpretation and predictions.

1) Although the proposed model works well, the evidence is correlational in nature rather than causal (as also mentioned in the Discussion). I would not ask for new experiments, but some non-trivial predictions regarding the effect of causal interventions should be explicitly discussed. For example, optogenetic intervention to manipulate the firing rates, even locally, is expected to affect process S in a predicted manner and provide more support for the model if the results would be consistent.

2) The paper suggests that sleep homeostasis involves multiple spatial and temporal scales. A unifying framework that could be interesting for describing this is that of critical brain dynamics, which suggests self-similarity across different spatial and temporal scales. Criticality was hypothesized in the past to in the context of sleep homeostasis [1]. Furthermore, changes in measures of criticality during sleep deprivation were described in a paper [2], on which one of the co-authors of the present paper (Achermann) is the last author. To be more specific, measures of the proximity to critical dynamics, derived from the population activity, could in principle replace the deviation of the firing rate from a set point in the proposed mathematical models. The network would be subcritical during wakefulness and supercritical during slow wave activity. One advantage of this model would be that it does not require fitting a parameter for the firing rate set point.

References:

1) Pearlmutter, B. A., and Houghton, C. J. (2009). A new hypothesis for sleep: tuning for criticality. Neural computation, 21(6), 1622-1641.

2) Meisel, C., Olbrich, E., Shriki, O., and Achermann, P. (2013). Fading signatures of critical brain dynamics during sustained wakefulness in humans. Journal of Neuroscience, 33(44), 17363-17372.

Reviewer #2:

Sleep is hypothesized to be regulated by a homeostatic sleep pressure process (and by the circadian rhythm, which is not considered in the present research). It is widely believed that this process ("process S") manifests itself in slow waves. Hence, changes in the strength of process S can be quantified by the power of slow wave activity (SWA) in segments of a few seconds in duration. This empirical behavior is traditionally approximated analytically by an exponential decay towards an asymptotic value during sleep and an inverse behavior (with a potentially different time constant and asymptote) during wakefulness. Here the authors suggest to quantify process S through the instantaneous multiunit firing rate: at any point in time where firing rate is below a certain threshold, process S decays (as during sleep) and when firing rate is above it, process S grows (as during wakefulness). A variant of the model described by an equation taking firing rates and DOWN states into consideration was also considered.

The paper shows that such quantification of process S produces trajectories that are similar to the traditional model. The question addressed by this work has a clear motivation, as firing rate level is likely more closely related to the biophysical mechanisms of process S than the EEG slow waves (for all we know EEG is an epiphenomenon). In my opinion, the result is of confirmatory nature rather than any conceptually new finding, as I do not see how any result that is qualitatively different from what is shown could have been observed, given the established finding that MUA firing rates in wakefulness are on average higher than during sleep. If the very idea that the evolution of process S can be expressed through changes in firing rate is thought to be novel and important, the paper would benefit from making this point in a concise way, using only one variant of the model.

1) I would have liked to see some form of cross-validation, e.g., by inferring the parameters separately from different portions of the data, and showing them to be in close agreement with each other. If this is not the case, the analytical model has too many parameters, which need not correspond to any biophysical processes.

2) Subsection “Data collection and pre-processing”: Some channels had an unstable MUA or had low firing rates and were excluded. The exclusion criteria seem to be subjective (no objective criteria are provided). This introduces a potential subjective bias into the findings and could preclude replication.

3) Zucca et al., 2019, demonstrate that some PV cells fire during DOWN states. This is a potential confound of defining DOWNs based on ISIs of individual channels.

4) A justification for a set point for MUA firing rate should be discussed, as different neurons can behave differently with respect to their individual set point (e.g. see Watson and Buzsaki, Neuron 2016).

Reviewer #3:

Thomas et al. present scientifically rigorous manuscript. The authors develop a novel means of modeling "process S" that is derived from the deviation of cortical firing rates from set points. The authors rigorously compare this approach to the classical model and demonstrate high agreement. The data used in this manuscript are of high spatial resolution and reveal significant differences in process S between recording channels within an animal. The work is statistically robust, and quite technical. This manuscript adds evidence to a series of papers that describe firing rate changes as a function of sleep and wake state, but makes no attempt to suggest a mechanism by which firing rates deviate or are restored. My concern with the paper is related primarily to its general interest and novelty. While the work is clearly rigorous and well executed, this study may be more appropriate for a specialized journal.

1) The findings presented in this manuscript are derived from primary motor cortex, whose activity has long been described as strongly positively related to arousal state and movement (e.g. Evarts, 1964, Sreenivasan, 2016, the Vyazovskiy group's 2016 paper by Fisher). Given evidence that, for example, visual cortical areas show less or no modulation of rate during sleep versus wake (e.g. Durkin 2016; Hengen et al. 2016), it's unclear how universalizable rules/models will be across regions. That these data and conclusions may be specific to the circuit in M1 should be made clear throughout the manuscript and explicitly addressed as a key point of interest in the Discussion.

2) One of the major speculative points in the manuscript is that the results support a model in which Process S is a time-keeping mechanism that maintains a sleep quota. The data presented seem to also be entirely consistent with a model in which waking experience-dependent alterations in neuronal physiology drive deviations in firing rates which require a homeostatic regulation of this (unidentified) physiological variable. Perhaps I have missed a key differentiator between these – if so, this should be clarified for the reader. Otherwise, the speculative model should be minimized.

3) Much of the Discussion comes across as highly speculative.
