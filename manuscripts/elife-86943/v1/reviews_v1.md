# Peer review - Round 1

Editors:
- Srdjan Ostojic, Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86943.3.sa0](https://doi.org/10.7554/eLife.86943.3.sa0)

This important work provides evidence that artificial recurrent neural networks can be used to investigate neural mechanisms underlying reversible remapping of spatial representations. Authors perform convincing state of the art analyses showing how population activity preserves the encoding of spatial position despite remappings due to the tracking of an internal variable. This paper will be of interest to neuroscientists studying contextual computations, neural representation of space and links between artificial neural networks and the brain.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.86943.3.sa1](https://doi.org/10.7554/eLife.86943.3.sa1)

Based on a recent report of spontaneous and reversible remapping of spatial representations in the enthorhinal cortex (Low et al 2021), this study sets out to examine possible mechanisms by which a network can simultaneously represent a positional variable and an uncorrelated binary internal state. To this end, the authors analyse the geometry of activity in recurrent neural networks trained to simultaneously encode an estimate of position in a one-dimensional track and a transiently-cued binary variable. They find that network activity is organised along two separate ring manifolds. The key result is that these two manifolds are significantly more aligned than expected by chance, as previously found in neural recordings. Importantly, the authors show that this is not a direct consequence of the design of the model, and clarify scenarios by which weaker alignment could be achieved. The model is then extended to a two-dimensional track, and to more than two internal variables. The latter case is compared with experimental data that had not been previously analysed.

Strengths:

rigorous and careful analysis of activity in trained recurrent neural networks

particular care is taken to show that the obtained results are not a necessary consequence of the design of the model

the writing is very clear and pleasant to read

close comparison with experimental data

extensions beyond the situations studied in experiments (two-dimensional track, more than two internal states)

Weaknesses:

no major weaknesses

(minor) the comparison with previous models of remapping could be expanded

Altogether the conclusions claimed by the authors seem to be strongly supported and convincing.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.86943.3.sa2](https://doi.org/10.7554/eLife.86943.3.sa2)

This important work presents an example of a contextual computation in a navigation task through a comparison of task driven RNNs and mouse neuronal data. Authors perform convincing state of the art analyses demonstrating compositional computation with valuable properties for shared and distinct readouts. This work will be of interest to those studying contextual computation and navigation in biological and artificial systems.

This work advances intuitions about recent remapping results. Authors trained RNNs to output spatial position and context given velocity and 1-bit flip-flops. Both of these tasks have been trained separately, but this is the first time to my knowledge that one network was trained to output both context and spatial position. This work is also somewhat similar to previous work where RNNs were trained to perform a contextual variation on the Ready-Set-Go with various input configurations (Remington et al. 2018). Additionally findings in the context of recent motor and brain machine interface tasks are consistent with these findings (Marino et al in prep). In all cases contextual input shifts neural dynamics linearly in state space. This shift results in a compositional organization where spatial position can be consistently decoded across contexts. This organization allows for generalization in new contexts. These findings in conjunction with the present study make a consistent argument that remapping events are the result of some input (contextual or otherwise) that moves the neural state along the remapping dimension.

The strength of this paper is that it tightly links theoretical insights with experimental data, demonstrating the value of running simulations in artificial systems for interpreting emergent properties of biological neuronal networks. For those familiar with RNNs and previous work in this area, these findings may not significantly advance intuitions beyond those developed in previous work. It's still valuable to see this implementation and satisfying demonstration of state of the art methods. The analysis of fixed points in these networks should provide a model for how to reverse engineer and mechanistically understand computation in RNNs.

I'm curious how the results might change or look the same if the network doesn't need to output context information. One prediction might be that the two rings would collapse resulting in completely overlapping maps in either context. I think this has interesting implications about the outputs of the biological system. What information should be maintained for potential readout and what information should be discarded? This is relevant for considering the number of maps in the network. Additionally, I could imagine the authors might reproduce their current findings in another interesting scenario: Train a network on the spatial navigation task without a context output. Fix the weights. Then provide a new contextual input for the network. I'm curious whether the geometric organization would be similar in this case. This would be an interesting scenario because it would show that any random input could translate the ring attractor that maintains spatial position information without degradation. It might not work, but it could be interesting to try!

I was curious and interested in the authors choice to not use activity or weight regularization in their networks. My expectation is that regularization might smooth the ring attractor to remove coding irrelevant fluctuations in neural activity. This might make Supplementary Figure 1 look more similar across model and biological remapping events (Line 74). I think this might also change the way authors describe potential complex and high dimensional remapping events described in Figure 2A.

Overall this is a nice demonstration of state-of-the-art methods to reverse engineer artificial systems to develop insights about biological systems. This work brings together concepts for various tasks and model organisms to provide a satisfying analysis of this remapping data.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.86943.3.sa3](https://doi.org/10.7554/eLife.86943.3.sa3)

This important work provides convincing evidence that artificial recurrent neural networks can be used to model neural activity during remapping events while an animal is moving along a one-dimensional circular track. This will be of interest to neuroscientists studying the neural dynamics of navigation and memory, as well as the community of researchers seeking to make links between artificial neural networks and the brain.

Low et al. trained artificial recurrent neural networks (RNNs) to keep track of their location during a navigation task and then compared the activity of these model neurons to the firing rates of real neurons recorded while mice performed a similar task. This study shows that a simple set of ingredients, namely, keeping track of spatial location along a one-dimensional circular track, along with storing the memory of a binary variable (representing which of the two spatial maps are currently being used), are enough to obtain model firing rates that reproduce features of real neural recordings during remapping events. This offers both a normative explanation for these neural activity patterns as well as a potential biological implementation.

One advantage of this modeling approach using RNNs is that this gives the authors a complete set of firing rates that can be used to solve the task. This makes analyzing these RNNs easier, and opens the door for analyses that are not always practical with limited neural data. The authors leverage this to study the stable and unstable fixed points of the model. However, in this paper there appear to be a few places where analyses that were performed on the RNNs were not performed on the neural data, missing out on an opportunity to appreciate the similarity, or identify differences and pose challenges for future modeling efforts. For example, in the neural data, what is the distribution of the differences between the true remapping vectors for all position bins and the average remapping vector? What is the dimensionality of the remapping vectors? Do the remapping vectors vary smoothly over position? Do the results based on neural data look similar to the results shown for the RNN models (Figures 2C-E)?

There are many choices that must be made when simulating RNNs and there is a growing awareness that these choices can influence the kinds of solutions RNNs develop. For example, how are the parameters of the RNN initialized? How long is the RNN trained on the task? Are the firing rates encouraged to be small or smoothly varying during training? For the most part these choices are not explored in this paper so I would interpret the authors' results as highlighting a single slice of the solution space while keeping in mind that other potential RNN solutions may exist. For example, the authors note that the RNN and biological data do not appear to solve the 1D navigation and remapping task with the simplest 3-dimensional solution. However, it seems likely that an RNN could also be trained such that it only encodes the task relevant dynamics of this 3-dimensional solution, by training longer or with some regularization on the firing rates. Similarly, a higher-dimensional RNN solution may also be possible and this would likely be necessary to explain the more variable manifold misalignment reported in the experimental data of Low et al. 2021 as opposed to the more tightly aligned distribution for the RNNs in this paper. However, thanks to the modeling work done in this paper, the door has now been opened to these and many other interesting research directions.
