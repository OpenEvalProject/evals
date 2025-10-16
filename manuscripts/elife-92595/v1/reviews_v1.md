# Peer review - Round 1

Editors:
- Peter Latham, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92595.3.sa0](https://doi.org/10.7554/eLife.92595.3.sa0)

This important study provides deep insight into a ubiquitous, but poorly understood, phenomenon: synaptic noise (primarily due to failures). Through a combination of theoretical analysis, simulations, and comparison to existing experimental data, this paper makes a compelling case that synapses are noisy because reducing noise is expensive. It touches on probably the most significant feature of living organisms -- their ability to learn -- and will be of broad interest to the neuroscience community.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92595.3.sa1](https://doi.org/10.7554/eLife.92595.3.sa1)

Summary:

Given the cost of producing action potentials and transmitting them along axons, it has always seemed a bit strange that there are synaptic failures: when a spike arrives at a synapse, about half the time nothing happens. This paper proposes a perfectly reasonable explanation: reducing failures (or, more generally, reducing noise) is costly. Four possible mechanisms are proposed, each associated with a different cost, with costs of the form 1/sigma_i^rho where sigma_i is the failure-induced variability at synapse i and rho is an exponent. The four different mechanisms produce four different values of rho.

What is interesting about the study is that the model makes experimental predictions about the relationship between learning rate, variability and presynaptic firing rate. Those predictions are consistent with experimental data, making it a strong candidate model. The fact that the predictions come from reasonable biological mechanisms make it a very strong candidate model and suggest several experiments to test it further.

Interestingly, the predictions made by this model are nearly indistinguishable from the predictions made by a normative model Synaptic plasticity as Bayesian inference. Aitchison it al., Nature Neurosci. 24:565-571 (2021). As pointed out by the authors, working out whether the brain is using Bayesian inference to tune learning rules, or it just looks like it's Bayesian inference but the root cause is cost minimization, will be an interesting avenue for future research.

Finally, the authors relate their cost of reliability to the cost used in variational Bayesian inference. Intriguingly, the biophysical cost provides an upper bound on the variational cost. This is intellectually satisfying, as it answers a "why" question: why would evolution evolve to produce the kind of costs seen in the brain?

Strengths:

This paper provides a strong mix of theoretical analysis, simulations and comparison to experiments. And the extended appendices, which are very easy to read, provide additional mathematical insight.

Weaknesses:

None.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92595.3.sa2](https://doi.org/10.7554/eLife.92595.3.sa2)

Summary

This manuscript argues about the similarity between two frameworks describing synaptic plasticity. In the Bayesian inference perspective, due to the noise and the limited available pre- and postsynaptic information, synapses can only have an estimate of what should be their weight. The belief about those weights is described by their mean and variance. In the energy efficient perspective, synaptic parameters (individual means and variances) are adapted such that the neural network achieves some task while penalizing large mean weights as well as small weight variances. Interestingly, the authors show both numerically and analytically the strong link between those two frameworks. In particular, both frameworks predict that (a) synaptic variances should decrease when the input firing rate increases and (b) that the learning rate should increase when the weight variances increase. Both predictions have some experimental support.

Strengths

(1) Overall, the paper is very well written and the arguments are clearly presented.

(2) The tight link between the Bayesian inference perspective and the energy efficiency perspective is elegant and well supported, both with numerical simulations as well as with analytical arguments.

(3) I also particularly appreciate the derivation of the reliability cost terms as a function of the different biophysical mechanisms (calcium efflux, vesicle membrane, actin and trafficking). Independently of the proposed mapping between the Bayesian inference perspective and the energy efficiency perspective, those reliability costs (expressed as power-law relationships) will be important for further studies on synaptic energetics.

Weaknesses

(1) As recognised by the authors, the correspondence between the entropy term in the variational inference description and the reliability cost in the energetic description is strong, but not perfect. Indeed, the entropy term scales as -log(sigma) while reliability cost scales as sigma^(-rho).

(2) Even though this is not the main point of the paper, I appreciate the effort made by the authors to look for experimental data that could in principle validate the Bayesian/energetic frameworks. A stronger validation will be an interesting avenue for future research.
