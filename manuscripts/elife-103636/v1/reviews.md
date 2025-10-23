# Peer review - Round 1

Editors:
- Srdjan Ostojic, École Normale Supérieure - PSL France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.103636.3.sa0](https://doi.org/10.7554/eLife.103636.3.sa0)

This study provides an important set of analyses and theoretical derivations to understand the mechanisms used by recurrent neural networks (RNNs) to perform context-dependent accumulation of evidence. The results regarding the dimensionality and neural dynamical signatures of RNNs are convincing and provide new avenues to study the mechanisms underlying context-dependent computations. This manuscript will be of interest to a broad audience in systems and computational neuroscience.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103636.3.sa1](https://doi.org/10.7554/eLife.103636.3.sa1)

Summary:

This paper investigates how recurrent neural networks (RNNs) can perform context-dependent decision-making (CDM). The authors use low-rank RNN modeling and focus on a CDM task where subjects are presented with sequences of auditory pulses that vary in location and frequency, and they must determine either the prevalent location or frequency based on an external context signal. In particular, the authors focus on the problem of differentiating between two distinct selection mechanisms: input modulation, which involves altering the stimulus input representation, and selection vector modulation, which involves altering the "selection vector" of the dynamical system.

First, the authors show that rank-one networks can only implement input modulation, and that higher-rank networks are required for selection vector modulation. Then, the authors use pathway-based information flow analysis to understand how information is routed to the accumulator based on context. This analysis allows the authors to introduce a novel definition of selection vector modulation that explicitly links it to changes in the effective coupling along specific pathways within the network.

The study further generates testable predictions for differentiating selection vector modulation from input modulation based on neural dynamics. In particular, the authors find that: (1) A larger proportion of selection vector modulation is expected in networks with high-dimensional connectivity. (2) Single-neuron response kernels exhibiting specific profiles (peaking between stimulus onset and choice onset) are indicative of neural dynamics in extra dimensions, supporting the presence of selection vector modulation. (3) The percentage of explained variance (PEV) of extra dynamical modes extracted from response kernels at the population level can serve as an index to quantify the amount of selection vector modulation.

Strengths:

The paper is clear and well written, and it draws bridges between two recent important approaches in the study of CDM: circuit-level descriptions of low-rank RNNs, and differentiation across alternative mechanisms in terms of neural dynamics. The most interesting aspect of the study involves establishing a link between selection vector modulation, network dimensionality and dimensionality of neural dynamics. The high correlation between the networks' mechanisms and their dimensionality (Fig. 7d) is surprising since differentiating between selection mechanisms is generally a difficult task, and the strength of this result is further corroborated by its consistency across multiple RNN hyperparameters (Figure 7-figure supplement 1 and Figure 7-figure supplement 2). Interestingly, the correlation between the selection mechanism and the dimensionality of neural dynamics is also high (Fig. 7g), potentially providing a promising future avenue for the study of neural recordings in this task.

Weaknesses:

As acknowledged by the authors, the results linking selection vector modulation and dimensionality might not generalize to neural representations where a significant fraction of the variance encodes information unrelated to the task. Therefore, these tools might not be applicable to neural recordings or to artificial neural networks with additional high-dimensional activity unrelated to the task (e.g. RNNs trained to perform many other tasks).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103636.3.sa2](https://doi.org/10.7554/eLife.103636.3.sa2)

This manuscript examines network mechanisms that allow networks of neurons to perform context-dependent decision-making.

In a recent study, Pagan and colleagues identified two distinct mechanisms by which recurrent neural networks can perform such computations. They termed these two mechanisms input-modulation and selection-vector modulation. Pagan and colleagues demonstrated that recurrent neural networks can be trained to implement combinations of these two mechanisms, and related this range of computational strategies with inter-individual variability in rats performing the same task. What type of structure in the recurrent connectivity favors one or the other mechanism however remained an open question.

The present manuscript addresses this specific question by using a class of mechanistically interpretable recurrent neural networks, low-rank RNNs.

The manuscript starts by demonstrating that unit-rank RNNs can only implement the input-modulation mechanism, but not the selection-vector modulation. The authors then build rank three networks which implement selection-vector modulation, and show how the two mechanisms can be combined. Finally, they relate the amount of selection-vector modulation with the effective rank, ie the dimensionality of activity, of a trained full-rank RNN.

Strength:

- The manuscript is written in an obvious manner

- The analytic approach adopted in the manuscript is impressive

- Very clear identification of the mechanisms leading to the two types of context-dependent modulation

- Altogether, this manuscript reports remarkable insights on a very timely question
