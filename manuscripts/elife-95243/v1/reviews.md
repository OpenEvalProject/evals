# Peer review - Round 1

Editors:
- Julijana Gjorgjieva, https://ror.org/02kkvpp62 Technical University of Munich Munich Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95243.3.sa0](https://doi.org/10.7554/eLife.95243.3.sa0)

This is an important study that investigates how neural networks can learn to stochastically replay presented sequences of activity according to learned transition probabilities. The authors use error-based excitatory plasticity to minimize the difference between internally predicted activity and stimulus-driven activity, and inhibitory plasticity to maintain E-I balance. The approach is solid but the choice of learning rules and parameters is not always always justified, with some unclear aspects to the formal derivation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95243.3.sa1](https://doi.org/10.7554/eLife.95243.3.sa1)

Summary:

This work proposes a synaptic plasticity rule which explains the generation of learned stochastic dynamics during spontaneous activity. The proposed plasticity rule assumes that excitatory synapses seek to minimize the difference between the internal predicted activity and stimulus-evoked activity, and inhibitory synapses try to maintain the E-I balance by matching the excitatory activity. By implementing this plasticity rule in a spiking recurrent neural network, the authors show that the state-transition statistics of spontaneous excitatory activity agrees with that of the learned stimulus patterns, which is reflected in the learned excitatory synaptic weights. The authors further demonstrate that inhibitory connections contribute to well-defined state-transitions matching the transition patterns evoked by the stimulus. Finally, they show that this mechanism can be expanded to more complex state-transition structures including songbird neural data.

Strengths:

This study makes an important contribution to computational neuroscience, by proposing a possible synaptic plasticity mechanism underlying spontaneous generations of learned stochastic state-switching dynamics that are experimentally observed in the visual cortex and hippocampus. This work is also very clearly presented and well-written, and the authors conducted comprehensive simulations testing multiple hypotheses. Overall, I believe this is a well-conducted study providing interesting and novel aspects on the capacity of recurrent spiking neural networks with local synaptic plasticity.

Weaknesses:

This study is very well-thought out and theoretically valuable to the neuroscience community, and I think the main weaknesses are in regard to how much biological realism is taken into account. For example, the proposed model assumes that only synapses targeting excitatory neurons are plastic, and uses an equal number of excitatory and inhibitory neurons.

The model also assumes Markovian state dynamics while biological systems can depend more on history. This limitation, however, is acknowledged in the Discussion.

Finally, to simulate spontaneous activity, the authors use a constant input of 0.3 throughout the study. Different amplitudes of constant input may correspond to different internal states, so it will be more convincing if the authors test the model with varying amplitudes of constant inputs.

Comments on revisions:

The authors have addressed all of the previously raised concerns satisfactorily, by running extra simulations with a biologically plausible composition of excitatory and inhibitory neurons, plasticity assumed for all synapses, and varied amounts of constant inputs representing internal states or background activities. While in some of these cases the stochastic dynamics during spontaneous activity change or do not replicate those of the learned stimulus patterns as well as before, these extended studies provide thorough evaluations of the strengths and limitations of the proposed plasticity rule as the underlying mechanism of stochastic dynamics during spontaneous activity. Overall, the revision has strengthened the paper significantly.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95243.3.sa2](https://doi.org/10.7554/eLife.95243.3.sa2)

Summary:

Asabuki and Clopath study stochastic sequence learning in recurrent networks of Poisson spiking neurons that obey Dale's law. Inspired by previous modeling studies, they introduce two distinct learning rules, to adapt excitatory-to-excitatory and inhibitory-to-excitatory synaptic connections. Through a series of computer experiments, the authors demonstrate that their networks can learn to generate stochastic sequential patterns, where states correspond to non-overlapping sets of neurons (cell assemblies) and the state-transition conditional probabilities are first-order Markov, i.e., the transition to a given next state only depends on the current state. Finally, the authors use their model to reproduce certain experimental songbird data involving highly-predictable and highly-uncertain transitions between song syllables. While the findings are only moderately surprising, this is a well-written and welcome detailed study that may be of interest to experts of plasticity and learning in recurrent neural networks that respect Dale's law.

Strengths:

This is an easy-to-follow, well-written paper, whose results are likely easy to reproduce. The experiments are clear and well-explained. In particular, the study of the interplay between excitation and inhibition (and their different plasticity rules) is a highlight of the study. The study of songbird experimental data is another good feature of this paper; finches are classical model animals for understanding sequence learning in the brain. I also liked the study of rapid task-switching, it's a good-to-know type of result that is not very common in sequence learning papers.

Weaknesses:

One weakness I see in this paper is the derivation of the learning rules, which is semi-heuristic. The paper studies Poisson spiking neurons, for which learning rules can be derived from a statistical objective, typically maximum likelihood, as previously done in the cited literature. The authors provide a brief section connecting the learning rules to gradient descent on objective functions, but the link is only heuristic or at least not entirely presented. The reason is that the neural network state is not fully determined by (or "clamped to") the target during learning (for instance, inhibitory neurons do not even have a target assigned). So, the (total) gradient should take into account the recurrent contributions from other neurons, and equation 13 does not appear to be complete/correct to me. Moreover, the target firing rate is a mixture of external currents with currents arising from other neurons in the recurrent network. The authors ideally should start from an actual distribution matching objective (e.g., KL divergence, and not such a squared error), so that their main claims immediately follow from the mathematical derivations. Along the same line, it would be excellent to get some additional insights on the interaction of the two distinct plasticity rules, one of the highlights of the study. This could be naturally achieved by relating their distinct rules to a common principled objective.

The other major weakness (albeit one that is clearly discussed by the authors) is that the study assumes that every excitatory neuron is directly given its target state when learning. In machine learning language, there are no 'hidden' excitatory neurons. While this assumption greatly simplifies the derivation of efficient and biologically-plausible learning rules that can be mapped to synaptic plasticity, it also limits considerably the distributions that can be learned by the network, more precisely to those that satisfy the Markov property.
