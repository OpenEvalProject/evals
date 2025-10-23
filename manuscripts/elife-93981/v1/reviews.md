# Peer review - Round 1

Editors:
- Adrien Peyrache, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.93981.3.sa0](https://doi.org/10.7554/eLife.93981.3.sa0)

This study presents an important finding on the spontaneous emergence of structured activity in artificial neural networks endowed with specific connectivity profiles. The evidence supporting the claims of the authors is convincing, providing direct comparison between the properties of the model and neural data although investigating more naturalistic inputs to the network would have strengthened the main claims. The work will be of interest to systems and computational neuroscientists studying the hippocampus and memory processes.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93981.3.sa1](https://doi.org/10.7554/eLife.93981.3.sa1)

Summary:

An investigation of the dynamics of a neural network model characterized by sparsely connected clusters of neuronal ensembles. The authors found that such a network could intrinsically generate sequence preplay and place maps, with properties like those observed in the real-world data.

Strengths:

Computational model and data analysis supporting the hippocampal network mechanisms underlying sequence preplay of future experiences and place maps.

The revised version of the manuscript addressed all my comments and as a result is significantly improved.

Weaknesses:

None noted


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93981.3.sa2](https://doi.org/10.7554/eLife.93981.3.sa2)

Summary:

The authors show that a spiking network model with clustered connectivity produces intrinsic spike sequences when driven with an ramping input, which are recapitulated in the absence of input. This behavior is only seen for some network parameters (neuron cluster participation and number of clusters in the network), which correspond to those that produce a small world network. By changing the strength of ramping input to each network cluster, the network can show different sequences.

Strengths:

A strength of the paper is the direct comparison between the properties of the model and neural data.

Weaknesses:

My main critique of the paper relates to the form of the input to the network. Specifically, it's unclear how much the results depend on the choice of a one-dimensional environment with ramping input. While this is an elegant idealization that allows the authors to explore the representation and replay properties of their model, it is a strong and highly non-physiological constraint. In order to address this concern, the authors would need to test the spatial tuning of their network in 2-dimensional environments, and with different kinds of input from a population of neurons that have a range of degree of spatial tuning and physiological plausibility. A method for systematically producing input with varying degrees of spatial tuning in both 1D and 2D environments has been previously used in (Fang et al 2023, eLife, see Figures 4 and 5), which could be readily adapted for the current study; and behaviorally plausible trajectories in 2D can be produced using the RatInABox package (George et al 2022, bioRxiv), which can also generate e.g. grid cell-like activity that could be used as physiologically plausible input to the network.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93981.3.sa3](https://doi.org/10.7554/eLife.93981.3.sa3)

This work offers a novel perspective to the question of how hippocampal networks can adaptively generate different spatial maps and replays of the corresponding place cells, without any such maps pre-existing in the network architecture or its inputs. And how can these place cells preplay their sequences even before the environment is experienced? Previous models required pre-existing spatial representations to be artificially introduced, limiting their adaptability to new environments. Others depended on synaptic plasticity rules which made remapping slower that what is seen in recordings. In contrast, this modeling study proposes that quickly-adaptive intrinsic spiking sequences (preplays) and spatially tuned spiking (place cells) can be generated in a network through randomly clustered recurrent connectivity. By simulating spatial exploration through border-cell-like synaptic inputs, the model generates place cells for different "environments" without the need to reconfigure its synaptic connectivity or introduce plasticity. By simulating sleep-like random synaptic inputs, the model generates sequential activations of cells, mimicking preplays. These "preplays" require small-world connectivity, so that cell clusters are activated in sequence. Using a set of electrophysiological recordings from CA1, the authors confirm that the modeled place cells and replays share many features with recorded ones.

Many features of the model are thoroughly examined, and conclusions are overall convincing (within the simple architecture of the model). Even though the modeled connectivity applies more closely to CA3, it remains unclear whether CA3 recapitulates the proposed small world architecture.

In any case, the proposal that a small-world-structured, clustered network can generate flexible place cells and replays without the need for pre-configured maps is novel and of potential interest to a wide computational and experimental community.
