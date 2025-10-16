# Peer review - Round 1

Editors:
- Frances K Skinner, University Health Network , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.17267.025](https://doi.org/10.7554/eLife.17267.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Repeating circular waves enable strengthening of large-scale neural assemblies during sleep spindles in human cortex" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This work is an analysis of spindle oscillations recorded from human subdural grids placed for the purpose of localizing epileptic seizures. The authors examine the spatio-temporal structures of spindles during sleep in human, and their possible role in memory consolidation. The techniques used are developed from their earlier work where waves were found in monkey visual cortex. Used here in considering both amplitude and phase information, the authors show that spindles exhibit a sophisticated spatio-temporal structure, with the majority of spindles traveling from temporal to parietal to frontal (TPF) cortex. The authors suggest that such traveling waves could serve to facilitate spike-timing dependent plasticity between anatomically remote areas, which would otherwise be difficult due to long axonal delays. The analysis is rigorous and the application of methods to detect propagating waves to spindles is novel. Spindles are of high interest for memory consolidation, and this dataset is highly valuable.

The revision requirements are three-fold.

1) An expansion and clarification of methodological aspects is needed in various places. Specific points are as follows.

a) Rotating spindle waves: The presented data and analyses on spindle oscillations are clear. They rely on a large dataset of spindle oscillations and the provided movies give a good sense of the observations made. However, clarifications are needed. First, the authors should incorporate a definition of what they consider as rotating and expanding waves, as well as the specific criterion used to distinguish these. Definitions should appear in the main text, and the supplementary material should include the specific criteria used for the classification of spatio-temporal patterns of activity. In the absence of this, it remains quite difficult to validate the method.

The methods present clearly the identification of the center point of the oscillation, important to perform a polar parameterization, thus essential to extract rotating or expanding waves. This step is well described and the method relies on the computation of gradients and curl. It would be important to know:

i) If the authors pre-processed the data and if smoothing occurred to compute these differential elements. In particular, filtering is indicated in Figure 1—figure supplement 8. Was a similar filtering used in the identification of waves? If this was not the case, how did the authors correct high frequency signals that may be amplified in the computation of differential quantities?

ii) Once the polar coordinate system has been derived and the phase map computed, how did the classification take place and what were the error rates accepted for this classification? The statement about the proportion of spindle oscillations classified as rotating waves of ~50% remains a little bit hard to appreciate since there are only 2 classes (plus "complex" waves that are those not satisfying their criteria of rotating or expanding wave). Moreover, the analysis of Figure 1—figure supplement 7 provides a more contrasted view of this result: rotational waves are not necessarily the leading form of oscillation, except for subject 1 (for other subjects, spindles were generally classified as complex).

iii) The authors indicate that among the rotating waves, they identified a clear bias towards TPF direction of rotation. Was this observation supported by a statistical test?

iv) The waves observed indeed reflect a peak between 3-5 m/s, but also a very high variance. From the individual curves, it seems that we see the superposition of two speed distributions centered at distinct values. Could the authors comment on the variations of the speed value provided?

b) The analysis of intra-class similarity is nicely developed. However, for the level of synchronization, it was unclear how the millisecond precision was computed. Particularly, it was unclear what was meant by "in two cycles with the highest similarity". Could the authors elaborate in the Methods or in the text on this choice?

c) A rigorous demonstration that spindles are waves would be a highly novel finding. However, given the limited size of the dataset, and the relationship of spindles to the underlying anatomy being unclear, additional analyses and explanations are needed.

i) Discrepancy with "local spindles", different frequencies of controparietal/frontal spindles finding, and relationship to underlying anatomy. Much previous work concludes that human spindles are "local" and that spindle frequencies vary between areas (i.e. Andrillon et al. 2011, Peter-Derex et al. 2012, Nir et al. 2014). However, here the statement is made that this is in fact not so and the explanation is provided that this might be due to using a threshold for detection. It is unclear how this analysis supports this statement. What would the wave-detection approach show if these spindles would in fact be local? All that is done here is to fit a field of vectors in 2D space and then to see if a curl can be fit. No goodness of fit is assessed (only that it is significant). But presumably this would also work for fields where only subsets of the vectors are fit, with the others random. Also, spindles have different frequencies depending on anatomical origin as well as in time relative to spindle onset. Could these frequency changes "generate" the appearance of waves (or vice-versa)?

ii) Structure of waves. It was unclear whether the origin (center) of waves remained constant, changed wave-by-wave or changed slowly. Figures are shown "re-centered", so it isn't apparent where the actual center was. Also, how sensitive is this method to edge effects, i.e., is it equally sensitive to detect centers everywhere on the array or only in the center? Overall, the location of the centers and the underlying anatomy should be clarified. The authors suggest a TPF direction of spread, so does this indicate center preferentially in temporal lobe?

2) A toning down of interpretation and claims and situating the work more appropriately. That is, STDP and memory consolidation aspects aren't actually measured. Specifically:

a) The authors should consider adjusting their title somewhat in toning down the claims (i.e., "… enable strengthening of large-scale neural assemblies…") to more appropriately reflect the main aspects of the paper.

b) Mechanistic interpretation is not supported. The Abstract talks extensively about synapses and STDP, neither of which is measured here. This should be clarified (e.g., interesting suggestions, but cannot be assessed using this data). Same for "spiking activity" – all that is measured is γ band power. Statements such as "groups of spikes" are not supported by this data. Others have measured spindles and spikes simultaneously in humans (i.e. Andrillon et al., as cited), showing a complex relationship.

c) Another suggestion is that the authors expand on their Figure 2 description/illustration. For example, could the authors say something about spindle mechanisms (RT cells and mutual inhibition etc.), and how such spikings illustrated in Figure 2 translate to EPSPs (IPSPs?). Haider et al. is cited to justify LFP and synaptic current tight couplings, but this includes IPSPs. Related to this is the consideration of different STDP rules for different cell types (e.g., see Abbott and Nelson, Nature Neuroscience 2000).

In essence, since much has been published regarding STDP, spindling mechanisms, memory consolidation etc., it would be good for the authors to put these various pieces together in their suggestions for the general reader to appreciate more fully, and so that interpretations/limitations/assumptions are clear in what is being said. As it stands, it comes across as overly simplistic regarding the timing relationships and LTP/LTD (Figure 2) and traveling waves with STDP aspects and so on.

3) Clearly describing/demonstrating that a differentiation between the two types of 'waves' is possible along with what is the current consensus in the literature – 'local spindles' and how it was ruled out with their analyses. This is unclear at present. Perhaps some of the unclassified waves are of that nature? That is statistics and classification are not always clear [see point (1) above].

Additional points to address:

i) In general, please provide more statistical support and more information on the statistical tests and the data analysis procedures used. It is stated that the code is available on bitbucket, but when looked for by one of the reviewers, access was not possible, thus preventing a better understanding of the types of tests used.

ii) How were the recordings referenced? Phase analysis is highly sensitive to this.

iii) What Figure 4C quantifies is unclear – please clarify how this is calculated. Can one show the same data for expanding waves and show this critical analysis for multiple patients?
