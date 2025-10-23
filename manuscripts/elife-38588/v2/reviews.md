# Peer review - Round 1

Editors:
- Mary B Kennedy, California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38588.021](https://doi.org/10.7554/eLife.38588.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Inhibition enhances spine-specific calcium encoding of synaptic input patterns in a biologically constrained model" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Mary B Kennedy as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Eve Marder as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Thomas M Bartol (Reviewer #2); Joshua Plotkin (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Dorman et al. describes a biologically grounded compartmental model of a striatal spiny projection neuron developed with the program GENESIS. The authors use the model to examine dendritic synaptic integration and calcium dynamics. The model incorporates channels responsible for the experimentally observed electrical behavior of the neurons. Numbers and locations of membrane channels and pumps have been "tuned" to reproduce observed electrical behavior, as well as observed calcium transients in activated spines. The model includes both excitatory and inhibitory synaptic "inputs".

The authors verify that activation of a cluster of distal, but not proximal, dendritic spines produces a non-linear dendritic plateau potential, as observed experimentally. They then extend these findings to make testable predictions about synaptic cooperativity and heterosynaptic calcium dynamics in stimulated vs. unstimulated dendritic spines. They explore the effects of simultaneous vs. non-simultaneous coordinated stimulation of groups of distal spines on individual dendritic branches. They report that simultaneous coordinated synaptic stimulation evokes enhanced ("supralinear") elevation of calcium in stimulated spines and increases the specificity of the increase for stimulated vs. non-stimulated spines. This effect is specific to distal dendritic spines, suggesting that co-activation of spines on individual branches may lead to the most potent potentiation, and that distal branches may therefore act as relatively independent integrating units.

They also explore the effect of coordinated distal synaptic stimulation onto different, neighboring dendritic branches, finding that the effects of coordinate activation are less pronounced when the inputs are on different branches. The data offer several new insights into these processes, such as the effects of spatial and temporal dispersion of stimulation on calcium summation and the contribution of NMDA receptors vs. VGCCs in mediating spine-specific supralinear calcium responses.

The most novel finding, however, concerns the role of GABAergic inputs in shaping synaptic specificity during multi-synaptic stimulation. The authors show that single GABAergic synaptic inputs to distal dendrites can drastically increase the specificity of intra-spine calcium dynamics by increasing the difference between the sizes of calcium transients in stimulated vs. neighboring unstimulated spines. This has important implications for synaptic plasticity, and helps resolve a paradox of how synapse-specificity may be achieved under conditions where converging synaptic stimulation pushes an entire dendritic region into a depolarized plateau, a scenario that is now appreciated to represent a physiologically meaningful and important event.

Essential revisions:

The work represents the kind of modeling that the reviewers would like to see published in eLife. However, there are major concerns that must be addressed before the manuscript would be suitable for publication. The concerns fall into two categories; the first is the writing style which is, at present, inadequate for the relatively general readership of eLife. The second concern derives from limitations of the model structure that the authors need to address.

Writing:

1) The manuscript is poorly written and must be thoroughly re-written in a less terse and more didactic style to be suitable for the relatively broad audience of eLife. The writing becomes less and less clear as it progresses through the presentation of figures. Here are a few examples:

The title of the section “Cooperative spine calcium exhibits dendritic branch independence” is vague. What is cooperative about the spine calcium? And what is independent about the branches? This ambiguous use of language is present throughout the writing in the paragraphs that follow. A better title would be something like "The supralinear calcium transient in spines that are activated simultaneously is largest when the co-activated spines are on the same dendritic branch."

In the following paragraph, the authors begin using the term "inputs" to mean either synapses themselves or activated synapses. The authors should use the term activation whenever they refer to activated synapses. For example, "To investigate the effect of spatial dispersion of inputs, synaptic inputs were randomly distributed…". This sentence is ambiguous.

It is not clear what the meaning is of "average interstimulus interval of 10 ms per branch with random temporal ordering". The methods do not describe exactly how this stimulation was structured. This leads to several questions about the stimulus itself:

If the "temporal ordering" was random, were there still a certain percentage of spines that were activated simultaneously?

2) The timing of the simulated FSI spike train relative to glutamatergic synaptic stimulation (Figure 6C) should be clarified.

3) The peak spine calcium data shown in Figure 6C is taken only from stimulated spines, correct? What length of dendrite was stimulated (with glutamatergic synapses) for each branch condition tested (1 vs. 2 branches), and was there a distance dependence of the simulated FSI train on the synaptic calcium responses (i.e. location of glutamatergic synapse on the branch, with location of FSI inputs fixed)?

4) In the experiments where distributed non-simultaneous synaptic stimulation was used to induce plateau potentials (e.g. Figure 4), is there a direction dependence (towards vs. away from soma) to stimulation, as shown for other neuron types? If so, does direction affect membrane potential, calcium dynamics or both?

There are many instances of use of jargon and/or ambiguous wording, as well as sentences that are too terse to be clear. The manuscript needs a thorough editing to employ a better organized and more didactic style. One more example, "the duration of proximal spine calcium was prolonged when the proximal spine was stimulated prior to the distal cluster." The authors mean – "the calcium transients in the proximal spines were prolonged when proximal spines were stimulated prior to..." Note that calcium does not have a duration.

The section on the effects of GABA inputs was very difficult to read for all the above reasons. The authors seem to use GABA as a code for "activation of GABAergic inputs". This is an example of lab jargon. The sixth paragraph of the subsection “GABA attenuates stimulated spine calcium but enhances spatial specificity” needs to be re-organized and each individual issue should be discussed in a separate paragraph (for example fast vs. slow GABAergic receptor kinetics.) Briefly define the nature and meaning of a "confusion matrix" for eLife's more general readership.

In the Introduction, and throughout the Results section, the work should be better set into the context of previous work. This will not detract from the significance of the present work, rather it will enhance it. The supralinear response of a calcium transient in spines resulting from activation of NMDA receptors has long been studied in cortical and hippocampal synapses. Earlier hippocampal/cortical papers should be cited; for example, Schiller, Schiller and Clapham, 1998. A good early review is Sjöström and Nelson, 2002. A stochastic computer model of a hippocampal neuron that includes differential contributions to spine calcium from various sources is Bartol et al., 2015.

The Introduction should contain a separate paragraph discussing the key differences between the anatomy and physiology of striatal spiny projection neurons and hippocampal and cortical projection neurons, including the observed synaptic plateau potentials, the up-state and down-state, and the observed differences between proximal and distal spines. In the Introduction and/or Discussion, a separate paragraph on the potential roles of the different sources of inhibitory inputs should be included. The present organization of the manuscript includes this background material interspersed throughout the Introduction, Results and Discussion, which becomes confusing.

Model Structure:

1) GENESIS (and also a recent module added to Neuron) treat the problem of reaction/diffusion between compartments connected by bottlenecks (such as the spine neck connected to the dendritic shaft) as a 1D problem (i.e. diffusion along the axial dimension of a cylinder). It has been shown previously that this treatment greatly underestimates the diffusion flux across the mouth of the bottleneck (see Stiles et al., 1996). The underestimate is due to the formation of a 3D concentration gradient in the neighborhood of the mouth as the diffusing particles enter the larger space. This 3D diffusion gradient greatly increases the apparent flux area of the mouth. Only a full 3D method that captures this fine structure provides an accurate quantitative estimate of diffusion as it occurs in the space and time scales of real dendrites and spines. Because major conclusions of this study concern fluxes and exchange of calcium among clusters of spines on the dendrite, getting the diffusion rate right may be of critical importance to the conclusions. The authors should discuss this aspect of the model explicitly and, at the very least, include information about the sensitivity of the conclusion of the model to the diffusion rate of calcium out of spines into the dendrite. For example, if the diffusion rate were faster, as described in the Stiles paper, would the tuning of channel numbers have to be adjusted to reproduce experimental data? And would the major conclusions of the study regarding size and specificity of calcium fluxes in spines still hold?

2) In computational science and numerical methods, the choice of temporal and spatial discretization of a PDE model is critical to achieve physically accurate results. For this reason, it is customary to validate a model by a test of convergence at ever finer space and time scales and through cross-validation with other simulation methods to demonstrate a robust solution. The authors should test the validity of their model using one or more of these techniques.

3) The boundary conditions in PDE models of reaction/diffusion are also a critical factor to get right. It is very important to account for the localradius of curvature at the boundary in the diffusion and flux terms at the boundary. It is not clear that the PDEs employed in the difshell module of GENESIS account for this curvature. See equation 3 of Rangamani et al., 2013. This could have a significant impact on the inward Ca flux and outward pump fluxes.

4) After addressing points 1-3 the calcium dynamics in the spines and dendrite may very well be different and will require the authors to re-tune the tunable parameters to compensate and restore a good fit to the experimental observations. It is unclear whether the authors' conclusions will hold up or be weakened.
