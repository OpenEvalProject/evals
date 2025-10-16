# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, National Centre for Biological Sciences India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99302.4.sa0](https://doi.org/10.7554/eLife.99302.4.sa0)

This useful modeling study shows how spatial representations similar to experiment emerge in a recurrent neural network trained on a navigation task by requiring path integration and decodability, but without relying on grid cells. The network modeling results are solid, although the link to experimental data may benefit from further development.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99302.4.sa1](https://doi.org/10.7554/eLife.99302.4.sa1)

Summary:

This work studies representations in a network with one recurrent layer and one output layer that needs to path-integrate so that its position can be accurately decoded from its output. To formalise this problem, the authors define a cost function consisting of the decoding error and a regularisation term. They specify a decoding procedure that, at a given time, averages the output unit center locations, weighted by the activity of the unit at that time. The network is initialised without position information, and only receives a velocity signal (and a context signal to index the environment) at each timestep, so to achieve low decoding error it needs to infer its position and keep it updated with respect to its velocity by path integration.

The authors take the trained network and let it explore a series of environments with different geometries while collecting unit activities to probe learned representations. They find localised responses in the output units (resembling place fields) and border responses in the recurrent units. Across environments, the output units show global remapping and the recurrent units show rate remapping. Stretching the environment generally produces stretched responses in output and recurrent units. Ratemaps remain stable within environments and stabilise after noise injection. Low-dimensional projections of the recurrent population activity forms environment-specific clusters that reflect the environment's geometry, which suggests independent rather than generalised representations. Finally, the authors discover that the centers of the output unit ratemaps cluster together on a triangular lattice (like the receptive fields of a single grid cell), and find significant clustering of place cell centers in empirical data as well.

The model setup and simulations are clearly described, and are an interesting exploration of the consequences of a particular set of training requirements - here: path integration and decodability. But it is not obvious to what extent the modelling choices are a realistic reflection of how the brain solves navigation. Therefore, it is not clear whether the results generalize beyond the specifics of the setup here.

Strengths:

The authors introduce a very minimal set of model requirements, assumptions, and constraints. In that sense, the model can function as a useful 'baseline', that shows how spatial representations and remapping properties can emerge from the requirement of path integration and decodability alone. Moreover, the authors use the same formalism to relate their setup to existing spatial navigation models, which is informative.

The global remapping that the authors show is convincing and well-supported by their analyses. The geometric manipulations and the resulting stretching of place responses, without additional training, are interesting. They seem to suggest that the recurrent network may scale the velocity input by the environment dimensions so that the exact same path integrator-output mappings remain valid (but maybe there are other mechanisms too that achieve the same).

The simulations and analyses in the appendices serve as insightful controls for the main results.

The clustering of place cell peaks on a triangular lattice is intriguing, given there is no grid cell input. It could have something to do with the fact that a triangular lattice provides optimal coverage of 2d space? The included comparison with empirical data is valuable as a first exploration, showing a promising example, but doesn't robustly support the modelling results.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99302.4.sa2](https://doi.org/10.7554/eLife.99302.4.sa2)

Summary:

The authors proposed a neural network model to explore the spatial representations of the hippocampal CA1 and entorhinal cortex (EC) and the remapping of these representations when multiple environments are learned. The model consists of a recurrent network and output units (a decoder) mimicking the EC and CA1, respectively. The major results of this study are: the EC network generates cells with their receptive fields tuned to a border of the arena; the decoder develops neuron clusters arranged in a hexagonal lattice. Thus, the model accounts for entrohinal border cells and CA1 place cells. It suggests that the remapping of place cells occurs between different environments through state transitions corresponding to unstable dynamical modes in the recurrent network.

Strengths:

The authors found a spatial arrangement of receptive fields similar to their model's prediction in experimental data recorded from CA1. Thus, the model proposes plausible mechanisms to generate hippocampal spatial representations without relying on grid cells. The model also suggests an interesting possibility that path integration is not the speciality of grid cells.

Weaknesses:

The role of grid cells in the proposed view, i.e., the boundary-to-place-to-grid model, remains elusive. The model can generate place cells without generating entorhinal grid cells. Moreover, the model can generate hexagonal grid patterns of place cells in a large arena. Whether and how the proposed model is integrated into the entire picture of the hippocampal-entorhinal meｍory processing remains elusive.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99302.4.sa3](https://doi.org/10.7554/eLife.99302.4.sa3)

Summary:

The authors used recurrent neural network modelling of spatial navigation tasks to investigate border and place cell behaviour during remapping phenomena.

Strengths:

The neural network training seemed for the most part (see comments later) well-performed, and the analyses used to make the points were thorough.

The paper and ideas were well-explained.

Figure 4 contained some interesting and strong evidence for map-like generalisation as environmental geometry was warped.

Figure 7 was striking and potentially very interesting.

It was impressive that the RNN path-integration error stayed low for so long (Fig A1), given that normally networks that only work with dead-reckoning have errors that compound. I would have loved to know how the network was doing this, given that borders did not provide sensory input to the network. I could not think of many other plausible explanations... It would be even more impressive if it was preserved when the network was slightly noisy.

Update:

The analysis of how the RNN remapped, using a context signal to switch between largely independent maps, and the examination of the border like tuning in the recurrent units of the RNN, were both thorough and interesting. Further, in the updated response I appreciated the additional appendix E which helped substantiate the claim that the RNN neurons were border cells.
