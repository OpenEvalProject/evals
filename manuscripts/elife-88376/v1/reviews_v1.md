# Peer review - Round 1

Editors:
- Panayiota Poirazi, FORTH Institute of Molecular Biology and Biotechnology Greece

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88376.3.sa0](https://doi.org/10.7554/eLife.88376.3.sa0)

This valuable study combines experiments and modelling to advance our understanding of the nonlinear nature of homeostatic structural plasticity and its interaction with synaptic scaling. The methodology and findings are solid, although additional work is needed to better link models with experiments and support some of the conclusions drawn. This study will be of interest to theoretical and experimental neuroscientists working in homeostatic plasticity.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88376.3.sa1](https://doi.org/10.7554/eLife.88376.3.sa1)

This manuscript investigates homeostatic structural plasticity and its interplay with synaptic scaling. It uses an integrated approach with models and experiments.

First, electrophysiology and chronic imaging are used to investigate the influence of different levels of AMPA-receptor antagonist NBQX, which allows for gradual activity reduction. Low levels of NBQX lead to a decrease of activity and a homeostatic increase of synapse density, whereas high levels block neural activity and lead to a reduced number of synapses after 3 days. The authors conclude that there must be a non-linear dependency between neuronal activities and rewiring. As a mathematical model for this, a biphasic structural plasticity rule is used, which, for increasing neural activities, switches from net synapse removal to growth and back, yielding two stable states at zero activity and the homeostatic target.

This rule is tested in various situations in silico, yet without attempting to reproduce the experiment. First, in network development, the biphasic rule generates a lot of unconnected silent neurons and a reasonable network structure only emerges when the neurons are additionally supported by a facilitating input current. For comparison, a linear and a simpler nonlinear homeostatic plasticity model, which had been ruled out by the experimental data, need no external drive. Second, the consequences of lasting, altered stimulation in a subgroup of neurons is explored. As expected by the design of the rule, a small increase and decrease in stimulation leads to a decrease and increase of synaptic connectivity, respectively, and stimulation silencing led to a complete disconnection of the sub-population with restoration of activity. Unlike in previous studies, an asymmetry of pre- and postsynaptic plasticity mechanisms cannot rescue this. Third, silencing only for a short time period and then overstimulating the network led to overly strong activity, which may, however, also hold without silencing. For a transiently silenced stimulation, recovery is possible, but only when there is enough recurrent excitation from the rest of the network.

Following this, the second part of the manuscript explores whether synaptic scaling may adapt and up-regulate the recurrent excitation, such that activity in a normally silenced subpopulation can be restored. Indeed, fast enough synaptic scaling leads to a recovery of neuronal activity in simulations, but leads to highly synchronous activity. A systematic model analysis shows at which scaling and rewiring speeds the activity and connectivity for a silenced sub-population can be restored. In between, however, the authors analyze spine sizes and changes in their whole population AMPAR-blocking experiments that demonstrate synaptic scaling and that structural plasticity and scaling effects may be jointly regulated. This experimental "break" between a simulation and its systematic analysis makes the paper harder to read and seems unnecessary as the analyses from the experiments are not repeated for the model.

Overall, the combination of experiments and simulations is a promising approach to investigate network self-organization. Especially the gradual blocking of activity is very valuable to inform mathematical models and distinguish them from alternatives. However, it remains unclear whether the model would actually reproduce the experiment. When switching from one to the other, this entails a detour to the conceptual level which makes the narrative sometimes hard to follow.

In summary, this manuscript makes a valuable contribution to discern the mathematical shape of a homeostatic structural plasticity model and understanding the necessity of synaptic scaling in the same network. Both experimental and computational methods are solid and well described. Yet, both parts could be linked better in order to obtain conclusions with more impact and generality.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88376.3.sa2](https://doi.org/10.7554/eLife.88376.3.sa2)

This manuscript by Lu et al addresses the understudied interplay between structural and functional changes underlying homeostatic plasticity. Using hippocampal organotypic slice cultures allowing chronic imaging of dendritic spines, the authors showed that a partial or complete inhibition of AMPA-type glutamate receptors differentially affects spine density, respectively leading to an increase or decrease. Based on that dataset, they built a model where activity-dependent synapse formation is regulated by a biphasic rule and tested it in stimulation- or deprivation-induced homeostatic plasticity. The model matches experimental data (from the authors and the literature) quite well, and provides a framework within which functional and structural changes coexist to regulate firing rate homeostasis.

While the correlation between changes in AMPAR numbers and in spine number/size has been well characterized during Hebbian plasticity, the situation is much less clear in homeostatic plasticity due to multiple studies yielding diverging results. This manuscript adds new experimental results to the existing data and presents a valuable effort to generate a model that can explain these divergences in a unifying framework.

The model and its successive implantation steps are well presented along a clear thread. However, the manuscript would benefit from clarifications at several key points (Hebbian vs homeostatic timeline).

First of all, it would have benefited from having an actual timeline of structural changes throughout the three days of AMPAR inhibition, especially as their experimental model allows it. This would have provided much-needed and otherwise entirely lacking information on spine dynamics (especially on transient spines) and on the respective timescale of the structural and functional changes, instead of modelling an entire timeline based solely on an experimental endpoint.

Additionally, the model would have been strengthened by an experimental dataset with homeostatic plasticity induced by higher activity (e.g. with bicuculline). To the best of my knowledge, there is currently no data on structural plasticity following scaling down, and it is also known that scaling up and down are mediated by different molecular pathways. The extension of the model from scaling up (in response to silencing) to scaling down (in response to increased activity) offers an interesting perspective, but its biological relevance is limited as there is no experimental data to support it.

Finally, the difference between weak and complete inhibition could have been more extensively characterized. The authors focus indeed on the effects of either condition on spine number, but only integrate synaptic weights following complete inhibition. This is a pity, as they show some intriguing data suggesting a differential effect on spine size by partial or complete AMPAR inhibition (although further work is required to support some of their interpretations). Since the model aims at correlating structural and functional homeostatic plasticity, the fact that it is only demonstrated for one of the two conditions tested severely undermines the claims of the authors in the discussion that the model tackles that question.
