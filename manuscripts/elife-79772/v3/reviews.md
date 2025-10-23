# Peer review - Round 1

Editors:
- Damon A Clark, https://ror.org/03v76x132 Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79772.sa0](https://doi.org/10.7554/eLife.79772.sa0)

This valuable article will be of interest to neuroscientists who study visual processing or are interested in dendritic integration. The authors used calcium imaging, pharmacology, and electrophysiology to investigate how a large, loom-sensitive neuron in grasshoppers integrates visual input to respond to both light and dark looming objects. These experiments convincingly support the finding that the integration is done by two distinct arbors of the neuronal dendritic tree, one of which loses retinotopic information. The authors suggest energetic advantages of this dendritic arrangement.


---

# Peer review - Round 1

Editors:
- Damon A Clark, https://ror.org/03v76x132 Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79772.sa1](https://doi.org/10.7554/eLife.79772.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Contrast-polarity specific mapping optimizes neuronal computation for collision detection" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tiago Branco (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers agreed that this manuscript would be suitable for publication in eLife if the authors address the points below.

1) Retinotopic mapping in field C: It remains unclear how the columnar organization of the lobula could relate to the proposed lack of retinotopy in field C. Similarly, the ROI based retinotopic analysis should be related to this anatomy. Both of these issues should be addressed.

2) Modeling: A detailed modeling section is required in the methods, including how excitation and inhibition are included.

3) Energetics: These claims need to be better supported by direct calculations and clear comparisons.

4) Optimizing claims: These must be better supported if they are to be included in the manuscript and title. As it stands, the claim is not backed up with concrete evidence that this anatomical organization optimizes the computation.

5) Inhibition: The contribution of inhibition should be considered when interpreting data and expanded on in the discussion.

6) Claims: Several smaller claims should be softened, as indicated in the detailed comments.

Reviewer #1 (Recommendations for the authors):

There were a few items that seemed incomplete in the manuscript:

1) There were a few places where claims were perhaps a little too strong:

a. Lines 152-161: Ach experiments. In principle, all these results are also consistent with an upstream neuron being excited by ach and using a different neurotransmitter to get the excitation to the LGMD. One solution is to simply adjust text. Or could one show that puffing a different excitatory neurotransmitter doesn't cause this?

b. Figure 4I: The authors say flatly that there is no retinotopic mapping in field C (line 191) and that the input locations are not different from random, but 4I shows that's not true along 1 axis in field C, even if the effect is small. (Or at least, n.s. is only marked for one of two axes in this panel.)

c. The authors assume that LGMD is mediating behavioral responses to ON looms. Is that proven or could it be here? If not, a caveat might be warranted.

2) There were two particular results that I thought deserved more explanation:

a. Field C really responds reasonably to the OFF loom. It's a little hard to reconcile this with treating it as the ON loom responsive field. Relatedly, on line 356: Incomplete rectification doesn't seem like it could explain the lack of selectivity in these fields. Incompletely rectified ON neurons would not also depolarize in response to contrast decrements, for instance. It seems like there would need to be a different parsimonious explanation.

b. Why does mecamylamine application to field C reduce the field A ON response?

3) The modeling and energetics arguments need substantially more detail to be convincing.

a. The authors should provide some details of the model in the methods. It would be helpful to have the basics of the model here; right now, there is nothing. Particularly important are the input transformations used to create the ON and OFF signals for the two fields – are these tonic or transient inputs? It could make a large difference to the energetics of the system.

b. Figure 7D: I would call 'clustered' 'retinotopic' if I'm understanding this correctly.

c. The noise in several modeling traces seems to be the same, which suggests this hasn't been averaged over noise (if there's noise in the model) or averaged over looms at different spatial locations. In particular, the noise in traces appears the same in the red and blue traces in 7B. But also in the black and gray traces in 7D. Is the gray really less than the black? The noise appears the same in these two traces (around t = -1), which suggests that this simulation is not averaging over noise instantiations or stimuli as it probably should. If this figure is the argument for why evolution dropped retinotopy to Field C, it's interesting, but it should be made stronger, perhaps with error bars or confidence intervals.

d. The energetics arguments should be spelled out more clearly:

i. When the authors write that there would be X savings for the ON Field C arrangement, they need to be clear about what the comparison is to. What is the alternative arrangement they're considering? ON and OFF retinotopic inputs to Field A? No ON inputs at all? I did not find this clear.

ii. There's a mix of detailed biophysical modeling and back-of-the-envelope style reasoning to come up with various numbers for the savings (in percents and in ATP). Doesn't the biophysical model allow one to compute the energy requirements directly and precisely?

Reviewer #2 (Recommendations for the authors):

1. Polarity does not reduce jump probability (Line 91):

a. The data in figure 1B show a trend towards a reduction in jump probability to white vs dark looms. Lower response rates to white vs dark stimuli have been documented across animals (Yilmaz and Meister 2013, Holmqvist and Srinivasan 1991, etc.), and figure 5G, at 100% coherence, seems to support this, with a >60% response rate for black and ~40% response rate for white looming stimuli. How do the Figure 1B data appear when using paired, individual animal probabilities as the data points, instead of 263 trials from 7 grasshoppers? Are the trials evenly distributed across the 7 grasshoppers?

2. The contribution of off inhibition for dendrite field C:

a. Dendrite field C, in addition to receiving on excitation, has been documented to receive OFF inhibition. Could a release of OFF inhibition (inhibitory rebound, for example) also be contributing to the response observed in dendrite C during white loom presentations? The authors should comment on this in the discussion. Additionally, why would off inhibition and on excitation be converging onto this particular dendrite field?

3. Lack of retinotopy for excitatory on inputs to dendrite field C:

a. How are the branches of dendrite field C arranged with respect to the columnar structure of the lobula? Dendrite field A spans across the lobula columns so adjacent areas in space are mapped to adjacent areas on the dendrite. In comparison, does the anatomy of dendrite field C provide insight into why an absence of retinotopic arrangement is observed? Are there substructures in the locust lobula where the different dendrite fields reside (Rosner 2017)? Can the authors expand on this, including what has been observed in past anatomical investigations?

b. Additionally, in analyzing the retinotopy with calcium imaging, can the ROIs for dendrite field C (Figure 4A) be drawn to match the columnar structure of the lobula as in field A, and/or drawn to follow the individual branches instead of combining multiple primary and secondary branches that may result in averaging the signal across multiple regions? The authors note they employed different strategies for drawing the ROI and witnessed similar results, but it would be helpful to include the ROI data that follow the analysis for dendrite field A. Finally, does the smaller size and location of dendrite field C suggest it samples from a much smaller (or different) receptive field than dendrite A? This relates back to (3) where it would be helpful to expand the introduction of the anatomy for the three dendrite fields, and expand on how it aligns or does not align with the ca2+ imaging results in the Discussion section.

4. Modeling synapse numbers as a proxy for energetic cost:

a. There is not a modeling section in the methods. The authors need to recap the methods for the published model and then describe in detail what changes/additions were made for the current manuscripts.

b. It is indeed interesting that the same firing rate can be achieved after removing 60% of dendrite field C's input, and that this may reduce energetic costs for the LGMD. However, are the starting number of synapses anatomically relevant?
