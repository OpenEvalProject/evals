# Peer review - Round 1

Editors:
- Peter Latham, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50804.sa1](https://doi.org/10.7554/eLife.50804.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors investigate the issue of energy consumption in synapses. They show that under a strategy in which much of the information about weights is kept in temporary storage while permanent weight changes are rare, energy consumption can be reduced by an order of magnitude. There has been a great deal of work on energy consumption associated with action potentials and synaptic plasticity, but this is, to our knowledge, the first to consider energy efficiency in the context of learning. As such it fills an important gap in our understanding of synaptic plasticity. This paper should appeal to anybody who is interested either in synaptic plasticity or energy efficiency in the brain. It may also be important for learning in artificial systems, where energy costs for training networks that are small by brain standards can exceed millions of kilowatt-hours.

Decision letter after peer review:

Thank you for submitting your article "Energy efficient synaptic plasticity" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Walter Senn (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors investigate the issue of energy consumption in synapses. They show that under a strategy in which much of the information about weights is kept in temporary storage while permanent weight changes are rare, energy consumption can be reduced by an order of magnitude.

This is an interesting paper that formalizes the concept of energy efficiency in learning. While work exists that considers the energy consumption of action potentials and synaptic plasticity, the formalization of energy efficiency in the context of learning is new, and worth a publication. The paper is well written and the math seems to be sound.

Essential revisions:

1) The authors introduce two components of the synaptic strength, a quickly decaying component that is transcribed into a long-lasting component when a threshold is crossed. The quickly decaying component requires less energy, and thus learning becomes a trade-off between energy efficient storage in the decaying component and energy costly storage in the sustained component.

The decay will lead to forgetting of unconsolidated memories and to a slow-down of learning, together with an increase of energy. As far as we could tell, the paper does not consider the speed of learning, and instead only asks for an energy efficient learning up to a certain degree of accuracy. The authors should provide learning curves for different consolidation thresholds and decay rates. Ideal would be a plot of energy versus learning time – presumably the lower the energy, the longer it takes to achieve a given set of accuracy, although we admit that's only a guess. On the other hand, there may be an optimal threshold.

2) Previous work [e.g., Ziegler, Zenke,.…, Gerstner, 2015, "From synapses to behavioural modelling"; Zenke et al., 2017, "Continual Learning Through Synaptic Intelligence"] has shown a benefit for the 2-stage synapses model in terms of learning and forgetting. Is there a similar benefit for this 2-stage model? This may simply be a Discussion point, referring to the analysis asked in the point (1) above.

3) From a biological point of view, it is clear that the change as well as the maintenance of synaptic weight can cost energy. Nevertheless, we find it strange that the authors analyze the perceptron learning rule according to a change-only energy cost function while the synaptic caching rule is analyzed by a combination of change (late-phase) and maintenance (early-phase) cost function. How critical is the phase-cost relation? Is it also efficient if the late-phase costs maintenance (e.g., by having a larger synaptic apparatus) and the early-phase costs energy dependent on its change? What is the energy consumption of the perceptron learning rule considering the maintenance cost function?

4) Please test for comparison the energy consumption of other learning rules performing perceptron learning (e.g., D’Souza et al., 2010).
