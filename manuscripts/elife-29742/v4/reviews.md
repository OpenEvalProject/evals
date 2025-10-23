# Peer review - Round 1

Editors:
- Peter Latham, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29742.sa1](https://doi.org/10.7554/eLife.29742.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Paradoxical response reversal of top-down modulation in cortical circuits with three interneuron types" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript presents some important insights into the diverse, counterintuitive behaviors of circuits with interacting inhibitory neuron populations. The authors show that, in a circuit with three types of interneuron, the functional sign of interactions can change depending on the exact activity level of the different cell types in the network – a population that inhibits another in one regime may suppress it in another regime. The essential features to enable this are: 1) more than one type of interneuron, 2) with diverse thresholds/nonlinearities. They relate this result to the experimental literature through citations, and directly compare their model results to data figures from other authors. In the discussion, they give testable predictions.

Essential revisions:

1) In the standard mode (van Vreeswijk and Sompolinsky, Neural Computation 1998), connectivity is high, and so the diagonal terms, di, are large. In this regime, there is no response reversal. It's an open question exactly how high connectivity is; it certainly isn't infinity, which is what physicists would like it to be, and the effective strength of the connectivity drops as the firing rate drops. However, when firing rates drop, fluctuations become important, and firing rate models become less believable. We're not asking the authors to do full network simulations (although we would suggest that it would be an interesting avenue for future research). However, they should at least comment on this. Even better would be a back of the envelope calculation showing that the connection strengths between populations are in the right range.

2) The authors do a good job citing the relevant literature. However they avoid framing their work in the context of inhibitory stabilized networks (ISNs). ISNs have very strong recurrent excitation that needs to be stabilized by recurrent inhibition (Ozeki et al.), and show the signature of a complex transient before settling in the equilibrium state – reminiscent of the author's Figure 1D. As remarked in the manuscript the sign flip of MSV requires wEE to be sufficiently large. Is the network an ISN? Figure 2 of Litwin-Kumar et al. (2016) extends ISNs to circuits with multiple interneurons subtypes, and they show that if the total inhibition received by E cells reduces under VIP stimulation then the network is an ISN. What regime is the author's model in? Is this a useful label for their network?

3) In Figure 2D, MEE is negative (-0.35), and if we understand things correctly, it's always negative in the high gain regime. Thus, in the high baseline activity state, an input to the pyramidal neuron population will result in a decrease of pyramidal neuron firing rates. This is at odds with most (all?) data sets. The authors remark on this feature in the last paragraph of the subsection “Circuit behavior explained by response matrix”, but do not address the plausibility of this prediction. Do the authors think this result is a problem for their model? More generally, with new parameters can the authors explain the sign flip in MSV without a sign flip in MEE or are these tethered together somehow?

4) Dipoppa et al. 2016 is important for justifying the model and the authors cite it frequently (and even republish some of its figures). But this paper has not been peer-reviewed (it's a Biorxiv report), giving it the same veridical status as a personal communication or SFN abstract. It's not appropriate for a peer-reviewed manuscript to depend on data that has not been reviewed. In addition, we're not sure how this will affect Dipoppa et al.'s attempts to get their work published. eLife is peer reviewed, and many journals won't let you republish work that's already published in a peer reviewed journal. In this manuscript, the authors actually take figures out of the other group's non-reviewed preprint and publish them in their own paper.

It seems to us that Dipoppa et al. is not absolutely essential; Figure 4E could be dropped without affecting the paper much. If the authors do want to include it, they should do two things. First, they should make it crystal clear that Dipoppa et al. is not peer-reviewed, every single time the citation is made. They can leave no doubt in the readers' minds that data is not yet part of the scientific literature. Second, they should get permission from Dipoppa et al. before publishing their data. We're guessing eLife requires this, but even if it doesn't, it's not worth irritating one's colleagues for something that is not essential to one's story.
