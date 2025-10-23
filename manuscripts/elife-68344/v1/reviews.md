# Peer review - Round 1

Editors:
- Morgan Barense, University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68344.sa1](https://doi.org/10.7554/eLife.68344.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper reports a timely, computationally-inspired fMRI analysis of how hippocampus-dependent memory handles overlap in the timing and visual characteristics of objects we encounter. The elegant experimental approach directly tests the predictions of a theoretical framework by parametrically manipulating visual overlap between associated stimuli. Results showed that within the dentate gyrus of the hippocampus, moderate levels of visual feature similarity led to differentiation following a statistical learning paradigm, but higher and lower levels of visual similarity did not. These findings speak to discrepancies in the field over how the hippocampus responds to similarity in memories and will be of broad interest to memory researchers and computational neuroscientists.

Decision letter after peer review:

Thank you for submitting your article "Increasing stimulus similarity drives nonmonotonic representational change in hippocampus" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Thackery Brown (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1. Provide a clearer theoretical rationale for the focus on the dentate gyrus given extant rodent work, per the detailed comments provided by Reviewer 3.

2. Address the extent to which these findings are dependent on this particular learning paradigm.

3. Clarify the time course of these effects, in particular as they relate to interpreting the pre- to post-learning results.

4. Describe extent to which these neural patterns meaningfully relate to behaviour.

5. Describe the relationship between the effects in the hippocampus and early visual regions.

Reviewer #2 (Recommendations for the authors):

1. Related to point 2 above – it would be helpful to show an analysis of how hippocampal representations change over time. I understand that time is a confound here – representations will drift further from the pre-learning template even with no further learning. However, since all stimuli were presented at all timepoints, adjacent run-to-run similarity values for these pairs could be calculated to establish whether the relative integration/differentiation occurs in a gradual way or as a step function. I leave it up to the authors to decide how to address this, or to provide an explanation for why such an analysis might not be feasible, but this would be helpful in interpreting the pre- to post-learning results.

2. Related to point 3 above – it would be helpful to provide any behavioural measures such as RT that might hint at whether (and how well) the participants learned the links between paired stimuli. Similarly, across the 6 statistical learning runs, did the authors observe RT facilitation for times when the grey square appeared on the second stimulus of a pair (vs. the first one)?

3. Perhaps I'm missing something, but it seems more parsimonious to remove participants who did not have statistical learning data from the templating analyses as well (p. 17). This way, the brain maps and plots are derived from data from the same individuals.

4. Figure 1 is somewhat difficult to follow. The logic is clear, but the lines depicting the information flow between the layers are somewhat difficult to keep in mind – perhaps it would be helpful if the hippocampal and visual layers were displayed in different colours. However, I leave it up to the authors to decide whether to make any changes, this could just be subjective preference. All other figures are exceptionally clear and easy to follow.

Reviewer #3 (Recommendations for the authors):

I am very enthusiastic about this work, and did find it quite well-motivated and designed in the broad strokes. I consider my concerns/comments to be "moderate" and am confident they can be addressed.

Specifics on the concerns and my suggestions:

Thinking about the DG findings, the authors present this as being the predicted locus of their non-monotonic representational relationship. But the justification for that is somewhat brief (limited to P.8) and to be honest not immediately intuitive to me. For one thing, in my view of the rodent literature the data might suggest DG favors differentiation for both low and moderate coactivation of memories on such a task, being highly sensitive to small changes. The authors cite the important Leutgeb 2007 work on this, but it's not clear to me that favors DG for the U-shaped pattern observed. The authors might also consider evidence juxtaposing CA1 and CA3 in a similar manner (Vazdarjanova and Guzowski 2004, J Neurosci). That work and the Leutgeb data would seem to favor CA3 having a "thresholded" representational relationship with contextual similarity, whil also suggesting CA1 may have higher discriminability for moderate levels of overlap. One suggestion is that pattern completion processes in the CA3 subcircuit may resist differention from DG up to an extent as contextual similarity drifts.

A related question on the theoretical side is how the network model is being conceptualized for subfields – for example, the subdivisions of the hippocampus can (ought to?) themselves be seen as layers in a neural network. Are the authors envisioning the context and perceptual conjunction cells as layers equally represented in each subfield tested, and that the transformation in that region alone is what differs? I ask because at least in broad terms the inputs to these regions from each other and the entorhinal cortex are different – DG and CA3 are predominantly targeted by entorhinal layer II, while CA1 is largely the target of entorhinal layer III, and it appears "where" and "what" cortical pathways are more segregated in CA1 than CA3 and DG (Witter et al., 2006 Annals of NYAS), and models of hippocampal circuit-level function often view item-context associations in inter-subregional terms (e.g., Hasselmo and Eichenbaum, 2005).

Thinking about the model –

One interesting assumption, if I read correctly, is that residual firing within the hippocampus during statistical learning (in the conjunction units) is "externally driven" – we see a "moderate" repeated activation of a unit in Figure 1 driven by sustained firing in visual cortex from the preceding trial and repeated firing of the same unit in the context layer. To my eye, this would seem to be a high overlap scenario for such a circuit – why does full context repetition and weak input from the cortex not drive strong activity in that item A cell (plasticity has indeed promoted a strong recurrent connection from prior learning between context and the perceptual layer)? Moreover, why do we assume sustained firing in the conjunctive codes in cortex but not those in the hippocampus?

On a related note, it seems allowing context to drift, as in a temporal context model, would help – the context is likely highly similar, but not identical, between adjacent events, which could somewhat attenuate the coactivation of the past event and facilitate the weakened connections with the perceptual conjunction layer.

Perhaps this is lost in the weeds, somewhat for the overall memory – similarity relationships observed, but I think it's an area where more justification and consideration could help tie the fMRI research here to data in rodents and/or motivate continued research into the circuit level of what is being observed.

Overall, I think a bit more on why the model was conceptualized the way it was and how the predictions (or, if more post-hoc – discover) of DG relate to our understanding of neural population connectivity and behavior from animal work would set the study up to promote even more hypothesis testing in this area.
