# Peer review - Round 1

Editors:
- Timothy O'Leary, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66804.sa1](https://doi.org/10.7554/eLife.66804.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Grid cells in the rodent entorhinal cortex are believed to contribute to internal representations of space and other continuous quantities via periodic firing patterns. Using extensive simulations, Mittal and Narayanan show that a leading continuous attractor model of how such patterns emerge is fragile to biologically relevant heterogeneities. The authors show how this fragility is rescued by introducing intrinsic resonance in the dynamics of cells in the network. Such resonance is widely observed the entorhinal system. This work therefore shows an important potential role for single cell properties in regulating network-level computations.

Decision letter after peer review:

Thank you for submitting your article "Resonating neurons stabilize heterogeneous grid-cell networks" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alessandro Treves (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Address the reviewer's questions about the causal role of resonance in stabilising grid patterns in this specific continuous attractor model. Provide a clearer and more complete description of the single-neuron dynamics.

2) Substantiate the results with more systematic modelling or mathematical analysis, possibly in a simplified model, to provide intuition or demonstrate the mechanism underpinning the observed stabilisation of grid fields. How specific are these effects to the CAN model architecture and/or grid fields?

Reviewer #1 (Recommendations for the authors):

The authors succeed in conveying a clear and concise description of how intrinsic heterogeneity affects continuous attractor models. The main claim, namely that resonant neurons could stabilize grid-cell patterns in medial entorhinal cortex, is striking.

I am intrigued by the use of a nonlinear filter composed of the product of s with its temporal derivative raised to an exponent. Why this particular choice? Or, to be more specific, would a linear bandpass filter not have served the same purpose?

The magnitude spectra are subtracted and then normalized by a sum. I have slight misgivings about the normalization, but I am more worried that , as no specific formula is given, some MATLAB function has been used. What bothers me a bit is that, depending on how the spectrogram/periodogram is computed (in particular, averaged over windows), one would naturally expect lower frequency components to be more variable. But this excess variability at low frequencies is a major point in the paper.

Which brings me to the main thesis of the manuscript: given the observation of how heterogeneities increase the variability in the low temporal frequency components, the way resonant neurons stabilize grid patterns is by suppressing these same low frequency components.

I am not entirely convinced that the observed correlation implies causality. The low temporal frequency spectra are an indirect reflection of the regularity or irregularity of the pattern formation on the network, induced by the fact that there is velocity coupling to the input and hence dynamics on the network. Heterogeneities will distort the pattern on the network, that is true, but it isn't clear how introducing a bandpass property in temporal frequency space affects spatial stability causally.

Put it this way: imagine all neurons were true oscillators, only capable of oscillating at 8 Hz. If they were to synchronize within a bump, one will have the field blinking on and off. Nothing wrong with that, and it might be that such oscillatory pattern formation on the network might be more stable than non-oscillatory pattern formation (perhaps one could even demonstrate this mathematically, for equivalent parameter settings), but this kind of causality is not what is shown in the manuscript.

Reviewer #2 (Recommendations for the authors):

I believe in self-organization and NOT in normative recommendations by reviewers: do this, don't do that. Everybody should be able to publish, in some form, what they feel is important for others to know; so I applaud the new open reviews in eLife. Besides, this manuscript is written very well, clearly, I would say equanimously, and I do not have other points to raise beyond what I observed in the open review. The figures are attractive, maybe a bit too many and too rich, but clear and engaging. My only suggestion would be, take your band-pass units, and show that they produce grids without any recurrent network. It will be fun.
