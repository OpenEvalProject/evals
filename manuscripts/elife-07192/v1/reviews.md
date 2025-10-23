# Peer review - Round 1

Editors:
- Marlene Bartos, Albert-Ludwigs-Universität Freiburg , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07192.026](https://doi.org/10.7554/eLife.07192.026)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Optogenetic feedback control of neural activity” for consideration at eLife. Your article has been favorably evaluated by Eve Marder (Senior editor) and two reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewer discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The overall statements of both reviewers were positive. Indeed, the novelty of the technique for reading out and controlling the activity of neuronal networks, was positively valued. However, both reviewers formulated several main concerns, of which two are most salient.

1) The mechanisms underlying the light-mediated alternation or clamp of neuron excitability are highly dependent on various factors including neuron types expressing ChR2, their cellular and synaptic properties and interconnectivity. It was unclear how these factors may influence the speed and quality of clamping neuronal excitability.

2) One reviewer pointed out that it is unclear how the activity spreads through the network and how it may change the input. Finally, the reviewer pointed out that the speed of the system is a limiting factor in a fast control of network excitability. The question is whether the speed can be improved. In general, a more thorough discussion of the limitations of the techniques should be discussed. Below you will find the major and minor criticism of the two reviewers.

Reviewer #1:

Major criticism:

By comparing sinusoidal light application to ChR2 expressing cell populations in comparison to rectangular or triangular light application, the authors observed differences in spike correlations and synchrony in some of the applied light protocols. The problem with this approach is that the resonance behavior of neurons is highly diverse and depends on the intrinsic membrane properties. Thus, any interpretations on the population behavior will depend on the nature of the cells expressing ChR2 and the percent of the contributing neuron types expressing CR2. Thus, the mentioned 'systematic modulation' of neuronal networks at the end of the subsection headed “Proportional-integral control of network firing” is very much dependent on various factors such as cell types, percent of neuron types expressing Chr2, brain area under investigation. This should be discussed in the manuscript.

Minor criticism:

At the end of the first paragraph of the subsection headed “Multi-hour control of firing rates” I would propose to replace the wording 'network plasticity' by 'changes in neuronal network dynamics'.

Reviewer #2:

In this manuscript the authors propose a way to measure the input into a neuronal population by quantifying the optogenetic current which is required to keep those cells at a constant firing rate level. They use eNpHR3.0 to balance the lack of inhibition and ChR2 to counteract the lack of excitation in vitro and in vivo. With this method, the authors approximate the input to the neuronal population by the power of the yellow light minus the power of the blue light. Since the study controls for the neuronal firing, the clamp can be used to cancel slow components for several seconds. This was used to keep the neuronal firing rate constant in order to show that the synaptic homeostasis is not dependent on neuronal firing rate. This is a nice application of the method. Overall the paper is well written and the figures are clear. What is missing is a discussion and data about how this method differs from classic patch clamp and how one can deal with the differences. The patch clamp is an important reference since it is relatively easy to understand its advantages and disadvantages.

While it is tempting to find a network correspondence with a single cell patch clamp, it might be difficult for at least two reasons: indirect network effects and speed. First, the advantage with single cell patch clamp is that there is a minimal impact on the remaining network since only one cell is modified. Here a whole population is modulated. Therefore a crucial question is how this modulation spreads through the network, how this spread changes the processing, and how this spread even will change the input that should be measured in the first place. Second, the main output of the classic voltage clamping is the amount of current that is required to compensate for various currents into a neuron. It is important that the compensation is complete, otherwise the injected current cannot be interpreted easily. This requires the regulator to be very fast. This is relatively easy with the membrane potential and currents for a patched cell, but not for a population of heterogeneously firing cells. It would be even more difficult to control for the firing of an individual neuron. This might explain why the controller needs some time to accumulate the spikes (tau=0.16s). This will unfortunately not be fast enough to follow the very fast transients caused by vibrissa stimulation (see Figure 8A). Since the control feedback speed probably depends on the temporal resolution of the neuronal signal, it would be interesting to study what happens when the temporal resolution is increased by taking more and more neurons into account. In this case it may be possible to decrease the time constant such that fast network dynamics can be studied.
