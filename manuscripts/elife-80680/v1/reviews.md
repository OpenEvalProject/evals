# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/00hx6zz33 École Normale Supérieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80680.sa0](https://doi.org/10.7554/eLife.80680.sa0)

This important work provides compelling evidence for the biological plausibility of the Successor Representation (SR) algorithm. The SR is a leading computational hypothesis to explore whether neural representations are consistent with the hypothesis that the neural networks in specific brain areas perform predictive computations. Establishing a biologically plausible learning rule for SR representations to form is of high significance in the field of neuroscience.


---

# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/00hx6zz33 École Normale Supérieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80680.sa1](https://doi.org/10.7554/eLife.80680.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Neural learning rules for generating flexible predictions and computing the successor representation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Stefano Recanatesi (Reviewer #1); Arthur Juliani (Reviewer #2); Srdjan Ostojic (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Main Comments:

1) The form of the plasticity rule in Equation 4 is motivated by the requirement that synaptic weights encode a properly normalised transition probability matrix (lines 92-96). But why is the normalisation important? What would change if synaptic weights were simply monotonic functions of transition probabilities, without normalisation? Presumably that would allow for a broader range of plasticity rules.

2) As the results of the paper strongly rely on the normalizing term in Equation 4. One of the reviewers suggests potentially moving upfront part of the discussion of this term, and enlarging the paragraph that discusses the biological plausibility of this specific term. Clearly laying out, for the non-expert reader, why it is biologically plausible compared to other learning rules. Also consider moving the required material to establish the novelty of such term: a targeted review of the relevant literature (current lines 358-366 and 413-433). This would allow the reader to understand immediately the significance and relative novelty of such term. For example, this reviewer personally wondered while reading the paper of how different was such term from the basic idea of Fiete et al., Neuron 2010 (DOI 10.1016/j.neuron.2010.02.003).

3) Related to the first point, the text insists on the fact that \γ is not encoded in the synaptic weights (eg line 89). Again, it is not entirely clear why this is important and justified, since γ is an ad-hoc factor in Equation 2. Presumably the proper normalisation of γ relies on the normalisation of J discussed above? It seems that this constraint could be relaxed.

4) As a consequence of the body of the text being devoted to the analysis of the design choices behind the proposed model, a relatively smaller portion of the work involves direct comparisons with neural data. In these comparisons, while it is apparent that there is a reasonable match between the proposed model and the empirical data, it is difficult to interpret these results. This is because it is unclear what should be expected of a good or bad model given the data being analyzed (TD error and KL divergence), and reasonable baselines to compare against are not presented outside of the traditional TD algorithm, which is shown to be comparable to the proposed RNN based method in a number of cases.

5) It would be useful to have a "limitations" paragraph in the discussion clearly outlining what this learning rule couldn't achieve. For example, Stachenfeld et al., Nat.Neuro. have many examples where the SR is deployed. Does the learning rule suggested by the authors would always work across the board, or are there limitations that could be highlighted where the framework suggested would not work well. No need to perform more experiments/simulations but simply to share insight regarding the results and the capability of the proposed learning rule.

Other comments/suggestions:

– Page 1: The introduction motivates this work with a discussion of hippocampal memory (storage and retrieval), but the work focuses on the SR which is inherently prospective. The first paragraph of the text could be revised to better make this connection beyond simply stating that the hippocampus is involved in both memory and future prediction.

– Page 2: The end of the introduction would be stronger if the motivation for an RNNs usage was tied to the literature on the known recurrent dynamics of the hippocampus. See for example: https://www.frontiersin.org/articles/10.3389/fncel.2013.00262/full

– Page 6: It is not clear the extent to which the FF-TD model differs from a canonical tabular SR algorithm or linear SF algorithm. My understanding is that it is the same, but the presentation in Figure 1i for example makes this somewhat unclear.

– Pages 6 – 11: it may be of benefit to more strongly support the various modifications to the model with connections to known or hypothesized hippocampal neural dynamics.

– Page 14: It states that "We discretize the arena into a set of states and encode each state as a randomly drawn feature ϕ." If I understand correctly, these features are not completely random, and instead follow the distribution described in Section 2.5. As it currently reads, it seems that these features might be drawn from a uniform random distribution, which would be misleading.

– Page 14: In Section 2.6 there is an assumption that a certain level of TD error corresponds to good performance. It is not clear what should objectively be considered a reasonable TD error. This is especially difficult to interpret in the case where both the RNN-S and FF-TD models display comparable performance. Is there perhaps some other baseline you would expect to perform considerably worse?

– Page 17: In Figure 4 it is somewhat confusing that the KL divergence (subplots G and I) has reversed shading (dark for low values) compared to the other subplots. It would be easier to interpret these graphs if their color coding was more consistent.

– Page 18: Similar to the difficulty of interpreting the TD error results, it is not clear what a "good" or "bad" KL divergence from the neural data would be. Any hypotheses on how to ground the numbers provided here would help to improve the quality of the results.

– Page 20: It is mentioned that the predictive timescale may be a separate gain term which the hippocampus takes as input, but there is evidence that different regions of the hippocampus seem to operate on different timescales. See for example: https://www.jneurosci.org/content/42/2/299.abstract. Is there a way to reconcile these ideas?

– Page 23: Section 4.5 describes the procedure for learning the parameters of the weight update rule as CMA-ES. Mentioning the fact that an evolutionary algorithm is used for learning these weights would help to make Section 2.3 more clear.

– Figures 5D-E and similar supplementary figures: if there is a parameter region that is unexplored then the color used for such region should be outside of the colormap. One of the reviewers suggests replacing white with gray for such region in these figures.

– Line 173: the text makes the distinction between an "SR-like" representation, and an "exact SR". What is the difference? Why is it important to have an exact of the SR in the neural activity, rather then eg a monotonic encoding of the SR?

– The RNN described in Equation 2 is not of the standard form (the non-linearity is applied after the connectivity matrix, ie f(J x) instead of Jf(x)). Is this detail important? If not, why not use the more standard form to avoid confusion?

– A line of work in the Fusi lab has examined plasticity rules that lead to the encoding of transition probabilities (eg Fusi et al., Neuron 2007). In particular, a paper by the reviewing editor (Ostojic and Fusi Front Comp Neuro 2013) examined the encoding of transition probabilities using plasticity rules that look similar to this manuscript. This is mentioned just for information, the authors should decide if those papers are relevant.

– Figures 5D-E and similar supplementary figures: if there is a parameter region that is unexplored then the color used for such region should be outside of the colormap. One of the reviewers suggests replacing white with gray for such region in these figures.
