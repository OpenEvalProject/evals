# Peer review - Round 1

Editors:
- Ranulfo Romo, Universidad Nacional Autonoma de Mexico , Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.02670.018](https://doi.org/10.7554/eLife.02670.018)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Contribution of correlated noise and selective decoding to choice probability measurements in extrastriate visual cortex” for consideration at eLife. Your article has been favorably evaluated by Eve Marder (Senior editor) and 3 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission. Your manuscript occasioned a significant discussion among the reviewers, largely around the issue of whether your paper makes a general contribution or whether it deals with a relatively narrow set of issues. Therefore, in preparing your revision, please think about any generalizations of the work that might make this more salient to people working on associated problems. Minimally, these issues should be confronted squarely in the revised Discussion.

General:

This paper focuses on the nature of choice probabilities (CPs). CPs is a measure of the covariation, in trial-by-trial-basis, between neural activity and behavior, typically in a decision task. As is well explained by the authors, the origins of CPs could originate from pure correlated noise of pairs of neurons as estimates of a neuronal population or by selective decoding, the neural response to a stimulus parameter(s) and its relation to behavior. According to the authors there is an historical debate of whether CPs, originate from pure correlated noise from neurons or by the selective decoding in a neuronal population. Here the authors use both simulations in artificial neurons biologically constrained and then tested the simulated results from real data of MSTd neurons, which are known by the authors; these neurons are associated with heading responses to visual flow and vestibular perturbations. The results of both simulations and real data are that MSTs neurons best conform to a selective decoding computation, although pure correlated noise contributes to selectivity.

Reviewer #1:

Found that the conclusions do not appear quite categorical since the authors claim that correlated noise is important but also cannot be excluded the selectivity decoding hypothesis. Curiously, cells in second somatosensory cortex have opposite tuning properties to the same stimulus, but that shared correlated noise has beneficial effect for improving the neurometric function and correlates with the psychometric performance (Romo et al., Neuron 2003). The beneficial effect came from a subtraction operation between the opposite tuning and correlated noise. Is this the case for congruent cells? In other words, for pool 2 neurons that carry the decision, she/he suspects that another group of neurons doing the opposite and very likely by subtracting noise and not a simple cancellation.

Reviewer #2:

As the authors acknowledge, the idea that all MSTd neurons are decoded according to their vestibular tuning preferences is a bit counterintuitive. He/she wonders whether the same simulations could be used to test the implications of this sort of decoding on the amount of information extracted about the stimulus. That is, does decoding only according to vestibular preference account for any sub-optimalties in the monkey's behavior? Such a result would provide more evidence for this decoding algorithm.

Reviewer #3:

This reviewer considers that the clear cut difference between the two models can only be formulated within the context of the Shadlen et al 96 model (recently revised by Haeffner et al), which the authors seem to take a ground truth, but which is itself a useful but fairly crude and simplistic picture of how the decision is being made), i.e. totally feedforward, no dynamics, etc).

Secondly even if one accepted that the decision making model is valid, the analysis does not allow the authors to draw general enough conclusions. Conceivably, one would set oneself to answer the question of whether it is possible to rule out the possibility than incongruent neurons do not contribute at all to the decision, regardless of all other modeling choices. The reviewer wasn't convinced by the analysis that this is the case. There are 3 main pieces of evidence: the patterns of CCs in Figure 3, the patterns of CPs in Figure 5 and the psychophysical data in Figure 6. In Figure 3, using an all-or-none approach where r_noise is ‘only’ a function of vestibular r signal, the data seems to favor the selective decoding model. However, (a) there are only 10 mixed pairs and (b) it is not at all clear that having r_noise be ‘mainly’ due to vestibular r_signal but with some contribution from visual r_signal, the two models would not look more similar to themselves and to data. This is a general concern: Even assuming the framework is valid, a simplified situation (in term of model parameters) is used to make categorical distinctions, and so it's not clear whether the conclusions are generic or if they only applied to the simplified situation.

The evidence from Figure 5 is also not shown to be conclusive/generic. The bi-modality in Figure 5b is not explained clearly and so it's not clear what exactly is necessary to obtain bi-modality. Is there no model with zero weights from incongruent neurons able to show unimodal CPs? Are there no parameters from the selective decoding model which would result in bi-modality? To make things worse, the selective decoding model seems to have one more degree of freedom (Readout Index). Similar concerns of generality apply to the analysis in Figure 6.

The authors conclude that both noise correlations and selective weighting probably contribute to the measured CPs. But this is hardly surprising (again, even assuming the whole framework is valid)!

In summary, the paper attempts to make a relatively minor distinction (i.e., to refute a model that represents a small region of parameter space (CPs are a result of only CCs) compared to the alternatives (CPs are a result of both CCs and weights)) and it does so it not in general terms, which limits the potential impact of the work.
