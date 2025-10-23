# Peer review - Round 1

Editors:
- Lisa M Giocomo, Stanford School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88053.3.sa0](https://doi.org/10.7554/eLife.88053.3.sa0)

This is an important theoretical study providing insight into how fluctuations in excitability can contribute to gradual changes in the mapping between population activity and stimulus, commonly referred to as representational drift. The authors provide convincing evidence that fluctuations can contribute to drift. Overall, this is a well-presented study that explores the question of how changes in intrinsic excitability can influence distinct memory representations.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88053.3.sa1](https://doi.org/10.7554/eLife.88053.3.sa1)

Summary of the findings:

The authors explore an important question concerning the underlying mechanism of representational drift, which despite intense recent interest remains obscure. The paper explores the intriguing hypothesis that drift may reflect changes in the intrinsic excitability of neurons. The authors set out to provide theoretical insight into this potential mechanism.

They construct a rate model with all-to-all recurrent connectivity, in which recurrent synapses are governed by a standard Hebbian plasticity rule. This network receives a global input, constant across all neurons, which can be varied with time. Each neuron also is driven by an "intrinsic excitability" bias term, which does vary across cells. The authors study how activity in the network evolves as this intrinsic excitability term is changed.

They find that after initial stimulation of the network, those neurons where the excitability term is set high become more strongly connected and are in turn more responsive to the input. Each day the subset of neurons with high intrinsic excitability is changed, and the network's recurrent synaptic connectivity and responsiveness gradually shift, such that the new high intrinsic excitability subset becomes both more strongly activated by the global input and also more strongly recurrently connected. These changes result in drift, reflected by a gradual decrease across time in the correlation of the neuronal population vector response to the stimulus.

The authors are able to build a classifier that decodes the "day" (i.e. which subset of neurons had high intrinsic excitability) with perfect accuracy. This is despite the fact that the excitability bias during decoding is set to 0 for all neurons, and so the decoder is really detecting those neurons with strong recurrent connectivity, and in turn strong responses to the input. The authors show that it is also possible to decode the order in which different subsets of neurons were given high intrinsic excitability on previous "days". This second result depends on the extent by which intrinsic excitability was increased: if the increase in intrinsic excitability was either too high or too low, it was not possible to read out any information about the past ordering of excitability changes.

Finally, using another Hebbian learning rule, the authors show that an output neuron, whose activity is a weighted sum of the activity of all neurons in the network, is able to read out the activity of the network. What this means specifically, is that although the set of neurons most active in the network changes, the output neuron always maintains a higher firing rate than a neuron with randomly shuffled synaptic weights, because the output neuron continuously updates its weights to sample from the highly active population at any given moment. Thus, the output neuron can read out a stable memory despite drift.

Strengths:

The authors are clear in their description of the network they construct and in their results. They convincingly show that when they change their "intrinsic excitability term", upon stimulation, the Hebbian synapses in their network gradually evolve, and the combined synaptic connectivity and altered excitability result in drifting patterns of activity in response to an unchanging input (Fig. 1, Fig. 2a). Furthermore, their classification analyses (Fig. 2) show that information is preserved in the network, and their readout neuron successfully tracks the active cells (Fig. 3). Finally, the observation that only a specific range of excitability bias values permits decoding of the temporal structure of the history of intrinsic excitability (Fig. 2f and Figure S1) is interesting, and as the authors point out, not trivial.

Weaknesses:

1. The way the network is constructed, there is no formal difference between what the authors call "input", Δ(t), and what they call "intrinsic excitability" Ɛ_i(t) (see Equation 3). These are two separate terms that are summed (Eq. 3) to define the rate dynamics of the network. The authors could have switched the names of these terms: Δ(t) could have been considered a global "intrinsic excitability term" that varied with time and Ɛ_i(t) could have been the external input received by each neuron in the network. In that case, the paper would have considered the consequence of "slow fluctuations of external input" rather than "slow fluctuations of intrinsic excitability", but the results would have been the same. The difference is therefore semantic. The consequence is that this paper is not necessarily about "intrinsic excitability", rather it considers how a Hebbian network responds to changes in excitatory drive, regardless of whether those drives are labeled "input" or "intrinsic excitability".

A revised version of the manuscript models "slope-based" excitability changes in addition to "threshold-based" changes. This serves to address the above concern that as constructed here changes in excitability threshold are not distinguishable from changes in input. However, it remains unclear what the model would do should only a subset of neurons receive a given, fixed input. In that case, are excitability changes sufficient to induce drift? This remains an important question that is not addressed by the paper in its current form.

1. Given how the learning rule that defines the input to the readout neuron is constructed, it is trivial that this unit responds to the most active neurons in the network, more so than a neuron assigned random weights. What would happen if the network included more than one "memory"? Would it be possible to construct a readout neuron that could classify two distinct patterns? Along these lines, what if there were multiple, distinct stimuli used to drive this network, rather than the global input the authors employ here? Does the system, as constructed, have the capacity to provide two distinct patterns of activity in response to two distinct inputs?

A revised version of the manuscript addresses this question, demonstrating that the network is capable of maintaining two distinct memories.

Impact:

Defining the potential role of changes in intrinsic excitability in drift is fundamental. Thus, this paper represents an important contribution. What we see here is that changes in intrinsic excitability are sufficient to induce drift. This raises the question for future work of the specific contributions of changing excitability from changing input to representational drift.
