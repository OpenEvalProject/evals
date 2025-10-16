# Peer review - Round 1

Editors:
- Richard Naud, University of Ottawa Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99545.4.sa0](https://doi.org/10.7554/eLife.99545.4.sa0)

This study offers a valuable treatment of how the population of excitatory and inhibitory neurons integrates principles of energy efficiency in their coding strategies. The convincing analysis provides a comprehensive characterisation of the model, highlighting the structured connectivity between excitatory and inhibitory neurons. The role of the many free parameters are discussed and studied in depth.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99545.4.sa1](https://doi.org/10.7554/eLife.99545.4.sa1)

Koren et al. derive and analyse a spiking network model optimised to represent external signals using the minimum number of spikes. Unlike most prior work using a similar setup, the network includes separate populations of excitatory and inhibitory neurons. The authors show that the optimised connectivity has a like-to-like structure, which leads to the experimentally observed phenomenon of feature competition. The authors also examine how various (hyper)parameters-such as adaptation timescale, the excitatory-to-inhibitory cell ratio, regularization strength, and background current-affect the model. These findings add biological realism to a specific implementation of efficient coding. They show that efficient coding explains, or at least is consistent with, multiple experimentally observed properties of excitatory and inhibitory neurons.

As discussed in the first round of reviews, the model's ability to replicate biological observations such as the 4:1 ratio of excitatory vs. inhibitory neurons hinges on somewhat arbitrary hyperparameter choices. Although this may limit the model's explanatory power, the authors have made significant efforts to explore how these parameters influence their model. It is an empirical question whether the uncovered relationships between, e.g., metabolic cost and the fraction of excitatory neurons are biologically relevant.

The revised manuscript is also more transparent about the model's limitations, such as the lack of excitatory-excitatory connectivity.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99545.4.sa2](https://doi.org/10.7554/eLife.99545.4.sa2)

Summary:

In this work, the authors present a biologically plausible, efficient E-I spiking network model and study various aspects of the model and its relation to experimental observations. This includes a derivation of the network into two (E-I) populations, the study of single-neuron perturbations and lateral-inhibition, the study of the effects of adaptation and metabolic cost, and considerations of optimal parameters. From this, they conclude that their work puts forth a plausible implementation of efficient coding that matches several experimental findings, including feature-specific inhibition, tight instantaneous balance, a 4 to 1 ratio of excitatory to inhibitory neurons, and a 3 to 1 ratio of I-I to E-I connectivity strength.

Strengths:

While many network implementations of efficient coding have been developed, such normative models are often abstract and lacking sufficient detail to compare directly to experiments. The intention of this work to produce a more plausible and efficient spiking model and compare it with experimental data is important and necessary in order to test these models. In rigorously deriving the model with real physical units, this work maps efficient spiking networks onto other more classical biophysical spiking neuron models. It also attempts to compare the model to recent single-neuron perturbation experiments, as well as some long-standing puzzles about neural circuits, such as the presence of separate excitatory and inhibitory neurons, the ratio of excitatory to inhibitory neurons, and E/I balance. One of the primary goals of this paper, to determine if these are merely biological constraints or come from some normative efficient coding objective, is also important. Lastly, though several of the observations have been reported and studied before, this work arguably studies them in more depth, which could be useful for comparing more directly to experiments.

Weaknesses:

This work is the latest among a line of research papers studying the properties of efficient spiking networks. Many of the characteristics and findings here have been discussed before, thereby limiting the new insights that this work can provide. Thus, the conclusions of this work should be considered and understood in the context of those previous works, as the authors state. Furthermore, the number of assumptions and free parameters in the model, though necessary to bring the model closer to biophysical reality, make it more difficult to understand and to draw clear conclusions from. As the authors state, many of the optimality claims depend on these free parameters, such as the dimensionality of the input signal (M=3), the relative weighting of encoding error and metabolic cost, and several others. This raises the possibility that it is not the case that the set of biophysical properties measured in the brain are accounted for by efficient coding, but rather that theories of efficient coding are flexible enough to be consistent with this regime. With this in mind, some of the conclusions made in the text may be overstated and should be considered in this light.

Conclusions, Impact, and additional context:

Notions of optimality are important for normative theories, but they are often studied in simple models with as few free parameters as possible. Biophysically detailed and mechanistic models, on the other hand, will often have many free parameters by their very nature, thereby muddying the connection to optimality. This tradeoff is an important concern in neuroscientific models. Previous efficient spiking models have often been criticized for their lack of biophysically-plausible characteristics, such as large synaptic weights, dense connectivity, and instantaneous communication. This work is an important contribution in showing that such networks can be modified to be much closer to biophysical reality without losing their essential properties. Though the model presented does suffer from complexity issues which raise questions about its connections to "optimal" efficient coding, the extensive study of various parameter dependencies offers a good characterization of the model and puts its conclusions in context.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99545.4.sa3](https://doi.org/10.7554/eLife.99545.4.sa3)

Summary:

In their paper the authors tackle three things at once in a theoretical model: how can spiking neural networks perform efficient coding, how can such networks limit the energy use at the same time, and how can this be done in a more biologically realistic way than previous work.

They start by working from a long-running theory on how networks operating in a precisely balanced state can perform efficient coding. First, they assume split networks of excitatory (E) and inhibitory (I) neurons. The E neurons have the task to represent some lower dimensional input signal, and the I neurons have the task to represent the signal represented by the E neurons. Additionally, the E and I populations should minimize an energy cost represented by the sum of all spikes. All this results in two loss functions for the E and I populations, and the networks are then derived by assuming E and I neurons should only spike if this improves their respective loss. This results in networks of spiking neurons that live in a balanced state, and can accurately represent the network inputs.

They then investigate in depth different aspects of the resulting networks, such as responses to perturbations, the effect of following Dale's law, spiking statistics, the excitation (E)/inhibition (I) balance, optimal E/I cell ratios, and others. Overall, they expand on previous work by taking a more biological angle on the theory and show the networks can operate in a biologically realistic regime.

Strengths:

* The authors take a much more biological angle on the efficient spiking networks theory than previous work, which is an essential contribution to the field

* They make a very extensive investigation of many aspects of the network in this context, and do so thoroughly

* They put sensible constraints on their networks, while still maintaining the good properties these networks should have

Weaknesses:

* One of the core goals of the paper is to make a more biophysically realistic network than previous work using similar optimization principles. One of the important things they consider is a split into E and I neurons. While this works fine, and they consider the coding consequences of this, it is not clear from an optimization perspective why the split into E and I neurons and following Dale's law would be beneficial. This would be out of scope for the current paper however.

* The theoretical advances in the paper are not all novel by themselves, as most of them (in particular the split into E and I neurons and the use of biophysical constants) had been achieved in previous models. However, the authors discuss these links thoroughly and do more in-depth follow-up experiments with the resulting model.

Assessment and context:

Overall, although much of the underlying theory is not necessarily new, the work provides an important addition to the field. The authors succeeded well in their goal of making the networks more biologically realistic, and incorporate aspects of energy efficiency. For computational neuroscientists this paper is a good example of how to build models that link well to experimental knowledge and constraints, while still being computationally and mathematically tractable. For experimental readers the model provides a clearer link of efficient coding spiking networks to known experimental constraints and provides a few predictions.
