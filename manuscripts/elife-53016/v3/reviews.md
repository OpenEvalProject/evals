# Peer review - Round 1

Editors:
- Floris P de Lange, Radboud University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53016.sa1](https://doi.org/10.7554/eLife.53016.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

There has been much interest in how stimulus processing depends on the phase and amplitude of pre-stimulus oscillatory activity. Using sophisticated computational modeling, this paper demonstrates that near-criticality is required to enable the ability of networks to regulate stimulus response based on pre-stimulus activity. This highlights a potential functional role for the critical state in allowing pre-stimulus states to influence sensory information processing.

Decision letter after peer review:

Thank you for submitting your article "Versatility of neuronal network function is maximized in the critical state" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Floris de Lange as the Senior Editor and Reviewing Editor. The reviewers have opted to remain anonymous.

Summary:

The authors study the stimulus-evoked responses in a previously published model (from the same group), which generates alpha oscillations and long-range temporal correlations. Previous results have shown that this model can exhibit critical dynamics depending on the connection probabilities of excitation and inhibition. The main novel contribution of this work is that it shows that the pre-stimulus biases (alpha frequency amplitude and phase) of the stimulus-evoked responses only occur in networks close to criticality. In particular, they found a strong negative correlation between pre-stimulus alpha amplitude and phase-locking response to stimulus in critical networks. This is consistent with experimental results that show higher alpha activity is correlated with decreased stimulus detection. This result also suggests that attention can modulate the network from the supercritical state where it ignores stimulus to the subcritical state where it reliably responds to stimulus.

In addition, the authors also show that networks at critical state have the largest dynamic range of phase-locking responses to stimulus. However, similar result has been shown in previous work for the dynamic range of firing rate responses.

Essential revisions:

1) Physiological realism.

Please report how the firing rates of excitatory and inhibitory neurons depend on E-I ratio (analog figure to e.g. 1E, but displaying the firing rates).

Please show raster plots of spiking for e.g. 100 randomly chosen neurons; a 250-500 ms window would be good to see; in addition, show population rates for a few seconds; both for the three examples (sub/super/critical).

"E-I balance" in the strict sense refers to excitatory and inhibitory currents within a single neuron canceling each other. Does the model show that?

2) Robustness.

You modified parameters with respect to the first version of the model. Ideally, the effects you show do not depend on these parameter modifications. Could you demonstrate that?

Likewise, would you expect that other models, like Levina, Hermann and Geisel, 2007, or del Papa, Priesemann and Triesch, 2017, would show similar types of effects, even in the absence of oscillations, thus at the transition between absorbing/sustained activity?

3) Dynamic Range.

The dynamic range at criticality is larger than at sub/supercritical models. However, the "working point" or response range also changes considerably. This is in analogy to Zierenberg et al., 2020. How do your results relate on the systematic change of the response range, and to their ideas that combining networks of different distances to criticality would greatly enhance the dynamic range?

4) Writing.

As to the writing, I think this paper is too concise and requires prior knowledge of the previously published papers from this group. I would appreciate more explanations in the main text about the key terminologies and concepts, such as "critical oscillation", "Long-range temporal correlations", "Detrended fluctuation analysis".

5) Data and code sharing.

The raw spike data for the three states (sub/super/critical) should be made available, so that everyone can re-analyse them. The code should be made available as well. Please share the code before acceptance.

6) I didn't find a clear definition of the stimulus input? What's the duration and magnitude? Is it a constant current in time? Why is the stimulus strength defined as the number of stimulated neurons? Would results be similar if stimulus strength is modeled as the magnitude of input current?

7) Figure 1D, if input current is larger, does it expand the dynamic range of the supercritical networks?

8) Figure 1C, Is the phase-locking response related to the onset increase of firing rate? If the network shows onset response in rate, it would result in more rising phases, right? Since previous work has shown criticality maximizes dynamic range of evoked rate responses, how is this result different from previous work?

9) Figure 3D, Similar to my comments above about the dynamics range, I wonder if the range of pre-stimulus regulation depends on the magnitude of input current. If you drive the supercritical network with stronger input for each neuron, does it expand the region of significant regulation.

10) About the balance between excitation and inhibition: I think it should be the product of synaptic weight and connection probability that determines the network dynamics. Why is the critical transition at approximately when excitatory connectivity percentage equals inhibitory connectivity percentage? How does the transition depend on the recurrent weights?
