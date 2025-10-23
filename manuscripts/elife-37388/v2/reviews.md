# Peer review - Round 1

Editors:
- Mark CW van Rossum, University of Nottingham United Kingdom

Reviewers:
- Maxim Bazhenov, University of California, San Diego United States

## Review text

DOI: [10.7554/eLife.37388.032](https://doi.org/10.7554/eLife.37388.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Theta-modulation drives the emergence of connectivity patterns underlying replay in a network model of place cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Overall the reviewers thought that this was an interesting study. However, a substantial number of issues were identified, and in subsequent discussions all reviewers thought each other's revision requests were valid and important.

We believe that it should be manageable to address them within a reasonable time.

Essential revisions:

Here is the summary of the essential revisions. These are just summaries, for the full comments see below.

- Discuss, and ideally simulate, the effect of phase precession.

- More clearly discuss the requirement that STDP rule cannot be frequency dependent, as well as the exact prediction regarding the optimal frequency.

- Extend the discussion of the result of Equation 5 and its predictions.

- Discuss, and ideally simulate, reverse replay in the model.

- Clarify the brain region which is modeled from the outset.

Reviewer #1:

In this study the authors present a rate based network model representing the place field activity in rodents on a periodic track. An external input activates place cells according to their preferred position and an asymmetric learning rule strengthens the recurrent excitatory synaptic weights such that during bursts in a quiet period (no place cell input) replay of the place cell sequence occurs. This learning is accelerated by theta oscillations. Over all, this is a well done study, consisting of computer simulations, analytical derivations and the analysis of electrophysiological data. However there are a few comments that should be addressed.

The model assumes a Poisson-rate for each neuron. However, it has been shown that place cells phase precess during theta oscillations which leads to a sequential organization of spiking during the theta cycle. This phenomenon is not mentioned at all. What effect does phase precession have on the presented results?

In this model the growth rate of the symmetric mode, which governs the learning process, depends on the auto-correlation and the plasticity rule. But the auto-correlation itself depends on the firing rate of the place cell. What happens with heterogeneous peak rates as shown in Figure 7A? Does this framework still hold?

I wonder whether the muscimol experiments are sufficient to claim the importance of theta oscillations for the learning process. A counter-example for place cell activity in the absence of theta oscillations has been demonstrated in bats (Yartsev and Ulanovsky, 2013), which should be mentioned. Yes, silencing the medial septum largely abolishes theta oscillations, however, it might be a stretch to reduce the medial septum to its pace making function.

Reviewer #2:

Summary:

The authors describe a spiking neural network model of place cells using what seems to be a variation of Linear-Nonlinear-Poisson (LNP) neurons equipped with a temporally asymmetric Spike-Timing-Dependent Plasticity (STDP) rule and externally oscillatory modulation. The network is capable of giving rise to spontaneous replay following simulated exploration, and its learning rate is optimized by external modulation in the Theta range. Moreover, the authors performed an analytical treatment of a simplified version of the network model to derive a formal description of how the robustness of and timescale in which replay emerging from repeated pre-post spike pairings is modulated by oscillatory activity at various frequencies.

The science behind the paper is very solid, and the analytical treatment in addition to the numerical simulations make this a very thorough, impressive modeling paper. The major criticisms revolve around how the authors chose to present some of their findings. Certain claims and findings are very exaggerated or misleading (see Major Critiques 1-3), and it is unclear what brain region are actually modeled (see Major Critique 4). Finally, there is an unsubstantiated claim about the model and oversight of extremely similar previously published work in the Discussion.

Major Critiques:

1) The authors consistently refer to the frequency band which optimizes the learning rate in the model as "theta", which is typically referred to as a hippocampal oscillation within the 8-12 Hz range. However, Figure 4A appears to show that optimal synaptic weight changes occur over a much broader frequency range, and Figure 4B specifically shows that optimal replay occurs within the 2-8 Hz range. The authors should be clear in the introduction about what is typically considered the theta range, and that, while their model does demonstrate the utility of oscillations within the theta range, the effect they observe is not limited to theta.

2) The authors should spend some time interpreting the analytical result from Equation 5 which demonstrates that "the growth rate of the even mode is found by multiplying the AC of place-cell activity by the window for plasticity, and integrating." No real physiological/functional interpretations/implications of this result are mentioned (which should always be done), and this leaves it unclear to readers (particularly ones without a rigorous computational background) how impactful this result actually is. It is unsurprising that integrating the autocorrelation of place-cell activity multiplied by the plasticity window provides the expected growth rate. This is essentially saying that by considering all of the place-cell activity which occurs regularly, and the corresponding weight change given by STDP, while ignoring the noisy activity (which would tend to cancel out on average from this type of unsupervised learning rule) it is possible to estimate the growth rate of the even mode (i.e. the one relevant to learning and which governs replay). The straightforward intuition of this result should be discussed both so that less computationally inclined readers can appreciate the result, and so that it does not mistakenly get taken to be predictive of a novel interpretation of how STDP leads to learning.

3) The authors propose an unsubstantiated mechanism for how their network could also generate reverse replay in addition to the more commonly studied forward replay. They should either provide supporting data for this claim or go into a much more detailed explanation of their proposed mechanism. To begin with, it is unclear what exactly is meant by "synapses to downstream neurons become rapidly depressed". Is this referring to long-term depression, short-term presynaptic depression, etc.? Assuming short-term presynaptic depression (as it has the appropriate timescale) this mechanism would only make sense if the same place-cell sequences were activated during the theta cycle as those immediately reactivated in during sharp-wave replay. However, as far as I know, no such tight temporal correlation has been observed.

4) The authors need to be clearer from the beginning which region of the brain is modeled. The paper does not spend any time on this or the general architecture of the network model in the Introduction. The constant reference to "place-cells" implies that this is a model of CA1, however the connectivity of the model makes this more likely to reflect CA3; a fact which the authors bring up themselves in the Discussion. Their defence of how these results can still apply to learning and replaying place-cell sequences is solid, and I would recommend the authors take this approach from the start. Bringing it up at the end of the paper seems somewhat misleading and could potentially turn off readers and make them dismissive of the interesting findings reported in the paper.

Reviewer #3:

This paper presents a theoretical study how STDP together with short-term synaptic depression and correctly tuned oscillation leads to replay like activity of hippocampal place cells. I think that none of the particular mechanisms are new, but the combination and its application to hippocampal sequences is and the analysis of the complete system is nice.

- Were any special settings needed to make sure the rotation of the attractor stopped (Figure 2C bottom), and did not continue rotating? Or would sufficient experience lead to longer and longer sequences?

- The maximum in Figure 4A hinges on the lack of frequency dependence in the STDP rule. The problem is that, AFAIK, STDP always has shown frequency dependence (more LTP at higher frequencies) and it is hard to imagine how biophysically a precise balanced STDP model could be constructed.

Currently it is written as if this is a minor issue, and that STDP needs some stabilization anyway. That might be true but the maximum might be lost. I think this weakness of the model needs to be exposed more.

Secondly, related but a bit less important, I would expect that even with balanced STDP the weights diverge due to the correlation contribution to LTP.
