# Neural population dynamics of computing with synaptic modulations

## Authors

- Kyle Aitken<sup>1</sup> ([ORCID: 0000-0003-0207-5885](https://orcid.org/0000-0003-0207-5885)) †
- Stefan Mihalas<sup>1</sup> ([ORCID: 0000-0002-2629-7100](https://orcid.org/0000-0002-2629-7100))

### Affiliations

1. MindScope Program Allen Institute Seattle United States

† Corresponding author

## Abstract

In addition to long-timescale rewiring, synapses in the brain are subject to significant modulation that occurs at faster timescales. These modulations vary widely in underlying biological mechanisms as well as the timescales over which they occur, yet they all endow the brain with additional means of processing information. Despite this, models of the brain like recurrent neural networks (RNNs) often have their weights frozen after training, relying on an internal state stored in neuronal activity to hold temporal information over task-relevant timescales. Although networks with dynamical synapses have been explored previously, often said modulations are added to networks that also have recurrent connections and thus the computational capabilities and dynamical behavior contributed by the synapses remain unclear. In this work, we study the computational potential and resulting dynamics of a network that relies solely on synapse dynamics to process temporal information, the multi-plasticity network (MPN). Unlike traditional RNNs, the weights in the MPN are modulated during inference. The generality of the MPN allows for our results to apply to synaptic modulation mechanisms ranging from short-term synaptic plasticity (STSP) to slower modulations such as spike-time dependent plasticity (STDP). We thoroughly examine the neural population dynamics of the MPN trained on integration-based tasks and compare it to known RNN dynamics, finding the two to have fundamentally different attractor structure. We find said differences in dynamics allow the MPN to outperform its RNN counterparts on several neuroscience-relevant tests. Training the MPN across a battery of neuroscience tasks, we find its computational capabilities in such settings is comparable to networks that compute with recurrent connections. Altogether, we believe this works demonstrates the computational possibilities of computing with synaptic modulations and highlights important motifs of these computations so that they can be identified in brain-like systems.
