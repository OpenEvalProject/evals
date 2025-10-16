# Peer review - Round 1

Editors:
- Douglas Portman, University of Rochester United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.104972.4.sa0](https://doi.org/10.7554/eLife.104972.4.sa0)

This valuable paper uses a quantitative modeling approach to explore a well-studied transition in motor behavior in the nematode C. elegans. The authors provide convincing evidence that this transition, which has been interpreted as a two-state behavior, can instead be described as a process whose parameters are smoothly modulated within a single state. This finding provides insight into the relationships between latent internal states and observable behavioral states, and suggests that relatively simple neuronal mechanisms can drive behavioral sequences that appear more complex.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104972.4.sa1](https://doi.org/10.7554/eLife.104972.4.sa1)

This paper concerns mechanisms of foraging behavior in C. elegans. Upon removal from food, C. elegans first executes a stereotypical local search behavior in which it explores a small area by executing many random, undirected reversals and turns called "reorientations." If the worm fails to ﬁnd food, it transitions to a global search in which it explores larger areas by suppressing reorientations and executing long forward runs (Hills et al., 2004). At the population level, reorientation rate declines gradually. Nevertheless, about 50% of individual worms appear to exhibit an abrupt transition between local and global search, which is evident as a discrete transition from high to low reorientation rate (Lopez-Cruz et al., 2019). This observation has given rise to the hypothesis that local and global search correspond to separate internal states with the possibility of sudden transitions between them (Calhoun et al., 2014). The objective of the paper is to demonstrate that is not necessary to posit distinct internal states to account for discrete transitions from high to low reorientation rate. On the contrary, discrete transitions can occur simply because of the stochastic nature of the reorientation behavior itself.

Major strengths and weaknesses of the methods and results

The model was not explicitly designed to match the sudden, stable changes in reorientation rates observed in the experimental data from individual worms. Kinetic parameters were simply chosen to match the average population behavior. Nevertheless, many sudden stable changes in reorientation rates occurred. This is a strong argument that apparent state changes can arise as an epiphenomenon of stochastic processes.

The new stochastic model is more parsimonious than reorientation-state change model because it posits one state rather than two.

A prominent feature of the empirical data is that 50% of the worms exhibit a single (apparent) state change and the rest show either no state changes or multiple state changes. Does the model reproduce these proportions? This obvious question was not addressed.

There is no obvious candidate for the neuronal basis of the decaying factor M. The authors speculate that decreasing sensory neuron activity might be the correlate of M but then provide contradictory evidence that seems to undermine that hypothesis. The absence of a plausible neuronal correlate of M weakens the case for the model.

Appraisal of whether the authors achieved their aims, and whether the results support their conclusions

The authors have made a convincing case that is not necessary to posit distinct internal states to account for discrete transitions from high to low reorientation rate. On the contrary, discrete transitions can occur simply because of the stochastic nature of the reorientation behavior itself.

Impact of the work on the field, and the utility of the methods and data to the community

Posting hidden internal states to explain behavioral sequences is gaining acceptance in behavioral neuroscience. The likely impact of the paper is to establish a compelling example of how statistical reasoning can reduce the number of hidden states to achieve models that are more parsimonious.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104972.4.sa2](https://doi.org/10.7554/eLife.104972.4.sa2)

Summary:

In this study, the authors build a statistical model that stochastically samples from a time-interval distribution of reorientation rates. The form of the distribution is extracted from a large array of behavioral data, is then used to describe not only the dynamics of individual worms (including the inter-individual variability in behavior), but also the aggregate population behavior. The authors note that the model does not require any assumptions about behavioral state transitions, or evidence accumulation, as has been done previously, but rather that the stochastic nature of behavior is "simply the product of stochastic sampling from an exponential function".

Strengths:

This model provides a strong juxtaposition to other foraging models in the worm. Rather than evoking a behavioral transition function (that might arise from a change in internal state or the activity of a cell type in the network), or evidence accumulation (which again maps onto a cell type, or the activity of a network) - this model explains behavior via the stochastic sampling of a function of an exponential decay. The underlying model and the dynamics being simulated, as well as the process of stochastic sampling are well described, and the model fits the exponential function (equation 1) to data on a large array of worms exhibiting diverse behaviors (1600+ worms from Lopez-Cruz et al). The work of this study can explain or describe the inter-individual diversity of worm behavior across a large population. The model is also able to capture two aspects of the reorientations, including the dynamics (to switch or not to switch) and the kinetics (slow vs fast reorientations). The authors also work to compare their model to a few others including the Levy walk (whose construction arises from a Markov process) to a simple exponential distribution, all of which have been used to study foraging and search behaviors.

Weaknesses:

The weaknesses are one of framework, which may nonetheless stir discussion and motivate new ideas based on these results.

First, the examples the authors cite where a Gillespie algorithm is used to sample from a distribution, be it the kinetics associated with chemical dynamics, or a Lotka-Volterra Competition Model, there are underlying processes that govern the evolution of the dynamics, and thus the sampling from distributions. In one of their references for instance, the stochasticity arises from the birth and death rates, thereby influencing the genetic drift in the model. In these examples, the process governing the dynamics (and thus generating the distributions from which one samples) are distinct from the behavior being studied. In this manuscript, the distribution being sampled from is the exponential decay function of the reorientation rate. That the model performs well, and matches the data is commendable, but it is unclear how that could not be the case if the underlying function generating the distribution was fit to the data.

The second weakness is related to the first, in that absent an underlying mechanism or framework, one is left wondering what insight the model provides. Stochastic sampling a function generated by fitting the data to produce stochastic behavior is where one ends up in this framework. But if that is the case, what do we learn about how the foraging is happening. The authors suggest that the decay parameter M can be considered a memory timescale, which offers some suggestion, but then go on to say that the "physical basis of M can come from multiple sources". Here is where one is left for want: Molecular dynamics models that generate distributions can point to certain properties of the model, such as the binding kinetics (on and off rates, etc.) as explanations for the mechanisms generating the distributions, and therefore point to how a change in the biology affects the stochasticity of the process. It is unclear how this model provides such a connection.

The authors provide possible roadmaps, but where they lead and how to relate that back to testable mechanistic studies remains unclear. Weighing the significance of the finding relative to the weaknesses appears to depend on how one feels about the possible mechanisms the authors identify in their responses.
