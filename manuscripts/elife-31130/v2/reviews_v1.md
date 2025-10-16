# Peer review - Round 1

Editors:
- Gustavo Deco, Universitat Pompeu Fabra Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31130.016](https://doi.org/10.7554/eLife.31130.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The modulation of neural gain facilitates a transition between functional segregation and integration in the brain" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and three reviewers, one of whom, Gustavo Deco (Reviewer #1), is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Tobias H Donner (Reviewer #2); Maxwell Bertolero (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Your paper presents a very useful integration a modeling framework and graph theoretical analysis, providing a mechanistic explanation of how neuromodulation balances the equilibrium between segregation and integration of functional information. All reviewers found the paper to be well written and the results to be relevant for the broader neuroscience community. All reviewers support the publication of the paper in eLife, provided that you address the following issues in your revision.

1) Additional analyses:

1a) The participation coefficient is a great measure of integration, but it needs to be supplemented with other measures. You should test the integration hypotheses with the participation coefficient, Q (inverse), and efficiency, and more carefully lay out why these measures make sense for testing the hypotheses regarding integration and segregation.

Moreover, the participation coefficient is a nodal measure, but you only report the mean – are all nodes equally increasing their participation coefficients? Are low or high nodes increasing their participation coefficients? These analyses will give more insight into exactly what is occurring in the network as a result of neural gain.

Rationale behind this request: The participation coefficient is a relative measure of the diversity a node's connections across communities. Thus, consider a node with strong connectivity to community A and weak connectivity to communities B-F. If the node simply decreases connectivity to community A, its participation coefficient increases. While this is likely rare, it can occur, and this might not capture the intuition of increased integration. On the other hand, perhaps it does, as the node is interacting with communities in a more equal fashion. Moreover, if other nodes from community A shift to community B, the participation coefficient of the node will increase, even if none of its connections did. Because of these ambiguities, supplementing the mean participation coefficient with Q and efficiency (the inverse of the sum of shortest paths) would be ideal. While Q is used as a measure of segregation, which is appropriate, the reasoning behind this is not laid out. It should be.

1b) You show that the profile for global phase synchrony (computed from the regional membrane potentials) is very similar to the profiles for the graph-theoretical measures that are based on the correlations of (much slower) local BOLD time series (Figure 2A and B). This observation is non-trivial. It should be complemented by an analysis of a measure of the dynamics of global phase synchrony – for instance, the standard deviation of global phase synchrony, which has been used to quantify metastability. Does this measure exhibit the same profile as those in Figure 2A and B? Along that line, please discuss why the similarity between BOLD correlation topology and global phase synchrony emerges. Do you have an intuition for this?

1c) The "Gain mediated integration is maximal in frontoparietal hub regions" findings should be complemented by analyzing the "diverse club" or the regions with high participation coefficients (Bertolero et al., 2017), which was found to be more highly interconnected than the rich club in the macaque.

2) Discussion, embedding of the present results into the existing literature.

2a) The Discussion should elaborate on the facts that (i) several of the results are motivated and expected from previous work, and (ii) the excitability parameter in your model is analogous to the global coupling, which has been used as control parameter in previous studies. The main new contribution here seems to be the addition of a second control parameter, the global gain.

Please note that, all reviewers appreciate the need of implementing the effects of neuromodulation effect explicitly, but they feel that the readership would benefit from a more balanced discussion of the context.

Rationale behind this request: Several previous studies have shown that networks of oscillators reach a balance between integration and segregation, a maximal complexity, and the largest variability of temporal networks at the critical point separating the asynchronous and synchronous phases (e.g., Schmidt et al., 2015; Zamora-Lopez et al. 2016; Deco et al. 2017). These studies also showed that rich clubs have a leading role concerning integration/segregation and complexity. The network can be displaced from one phase to the other by changing a control parameter, which is usually chosen to be the global coupling or connectivity strength – analogous to the excitability parameter used in your model. In addition, you manipulate a second control parameter, namely the slope of the transfer function that converts inputs into firing rates. Increasing the slope brings the system from asynchronous state to the synchronous state, and, as shown in Equation [3], has the same effect than a global coupling.

2b) Changes in both parameters (gain and excitability) are necessary for producing the effects of interest in your model. In particular, the graph-theoretical measures show a non-monotonic (inverted U) dependency on excitability, but not on gain. Still, the title and much of your Discussion focusses on gain only, drawing firm links to the Astone-Jones and Cohen Adaptive Gain Theory. Please discuss more explicitly the interesting effects of excitability. Specifically: How can you reconcile the predominance of inverted U patterns for excitability but not gain, with the Aston-Jones and Cohen framework.

2c) Previous work by the labs of Ken Harris and Stefano Panzeri has also used the FitzHugh-Nagumo model to characterise the effects of state/neuromodulation on cortical dynamics – but by modulating the dynamics of the 2D-oscillator itself (Curto et al., 2009; Safaai et al., PNAS, 2015). This work should be discussed and related to your current approach.

3) Clarifications

3a) In general, all reviewers appreciate that the paper was written for a general audience. However, please include all equations and note in the main text where they exist. For example, please include the equation for Communicability and expand the explanation – is it all walks, or all walks that are part of all shortest walks between all nodes? It is not clear in the Results or Materials and methods section.

3b) Please unpack the rationale behind using the correspondence between structural and functional connectivity as criterion for delineating the "plausible" sub-space of parameter combinations. This is important because work into neuromodulation in small circuits shows that neuromodulation can reconfigure circuits, thus overriding the structural connectome (Marder, Neuron, 2012).

3c) It seems that Vi is used for the computation of phase synchrony (i.e., not the neural activity passed through the hemodynamics). This should be made explicit in the Materials and methods. (Terms like "raw signal" or "neural data" are ambiguous.)

3d) Figure 2D is described as inverted U relationship, a description that glosses over the left flank of this plot. The relationship clearly is monotonic, but not an inverted U.

3e) Figure 2—figure supplement 3 is missing axis labels and won't be understandable for a broad audience. Please explain what it shows and what that means.
