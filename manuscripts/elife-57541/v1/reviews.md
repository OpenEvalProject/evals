# Peer review - Round 1

Editors:
- Srdjan Ostojic, Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57541.sa1](https://doi.org/10.7554/eLife.57541.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript explores an excitatory-inhibitory network model to determine the circuit and plasticity mechanisms underlying the generation of neurons coding for prediction errors in the visual cortex. The manuscript demonstrates that negative prediction errors arise naturally if synaptic plasticity acts to produce homeostatic excitation-inhibition balance when the circuit receives both visual inputs and internal predictions thereof. Remarkably, the emergence of prediction error neurons depends on experience of the circuit with coupled visuomotor input, reflecting recent experimental results, and the model provides direction for future optogenetic experiments to disentangle which cell types are targeted by visual or motor input.

Decision letter after peer review:

Thank you for submitting your article "Learning prediction error neurons in a canonical interneuron circuit" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Srdjan Ostojic as the Reviewing Editor, and the evaluation has been overseen by Richard Ivry as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This manuscript models a canonical cortical microcircuit in order to investigate the circuit configurations and plasticity underlying one type of sensorimotor mismatch response identified in visual cortex. The authors show that negative prediction error neurons emerge from the network via plasticity in a set of inhibitory synapses that acts to minimize evoked firing of pyramidal cells. Moreover, the emergence of these response properties is robust to the particular cellular targets of visual and motor input (for PVs and PCs), while the type of prediction error neuron that emerges (positive versus negative) is dependent on how motor and visual inputs target VIPs and SOMs. Very nicely, the emergence of prediction error neurons depends on experience of the circuit with coupled visuomotor input (reflecting recent experimental results), and the model provides direction for future optogenetic experiments to disentangle which cell types are targeted by visual or motor input.

The general topic of microcircuits for predictive coding is very interesting, in direct relationship with experimental work. The manuscript is well written and thorough, and the topic is timely. All reviewers were generally supportive, but some concerns were raised and need to be addressed in the revision.

Essential revisions:

1) The paper focuses on a very homogeneous coding of negative prediction errors, while positive prediction errors appear only in one figure. The authors don't justify their focus on the former over the latter. It would therefore be important to include better the variety of prediction error coding in the model, and discuss its functional implications. Wouldn't it be possible and interesting to compare the distribution of different types of neurons (nPE, pPE, others) between the model and the data? The manuscript states that "nPE neurons represent only a small fraction of neurons in mouse V1". This undercuts somewhat the previous sections, and calls for a more quantitative comparison, in particular with respect to a distribution that would be obtained from random wiring for instance. The predictions for optogenetic inactivations in Figure 3 are very nice, but how do they extend to the heterogeneous case with pPE and other neuron classes (Figure 4) ? Can Equations 8-9 be extended to pPE neurons?

2) In the model, every neuron receives one or two scalar signals representing a one-dimensional visual input and corresponding motor efference copy. The authors should describe how their results would generalize to a situation in which neurons have different selectivities. In particular, there are observations that receptive-field size differs across cell types. More generally, could the circuit the authors describe generalize to neurons with "mixed selectivity" to multiple variables?

3) The paper heavily focuses on a 4 cell-type motif (Pyr, PV, SOM, VIP), but does not provide a clear message on what the functional importance of this motif is. Could PE and nPE neurons emerge in circuits with only 2 or 3 cell types? If so, what computational benefits does the presence of other cell types provide? Along similar lines, how stringent are the conditions on synaptic weights to generate nPE (or pPE) neurons ? A comparison between the number of constraints and the number of variables would be interesting to determine how large the space of solutions is.

4) What is the role of recurrent connections In the model? The argument in terms of pathways (Figure 2) does not take loops into account. The approach taken here should be compared with predictive coding of Deneve and Machens, which relies on recurrent connection.

5) A key point of the paper is the plasticity rule operative at SOM->PV synapses. In the first part of the paper, the authors use a non-local, backpropagation-like rule, and then later show that under certain circumstances this assumption can be relaxed. The fact that the initial learning rule is based on backpropagation becomes apparent only in the first paragraph of the Results, and the reader needs to dig through the Materials and methods and appendix to understand the details of the plasticity rule that is being used throughout the main text. The learning rules need to be explained earlier in the manuscript, e.g. by including, Equations 16, 17, and 19 of the Materials and methods in the main text. We also suggest reorganising the corresponding part of the Materials and methods to clearly separate the two different types of learning used at different points in the Results. More generally, during the discussion of biological plausible plasticity, the reader is left asking why the authors didn't restrict to such plasticity from the beginning. Are the results worsened when using more realistic rules?
