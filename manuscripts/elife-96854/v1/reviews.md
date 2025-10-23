# Peer review - Round 1

Editors:
- Jörn Diedrichsen, Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96854.3.sa0](https://doi.org/10.7554/eLife.96854.3.sa0)

This valuable paper presents convincing evidence that changing the constraint of how long to stop at an intermediate target significantly influences the degree of coarticulation of two sequential reaching movements, as well as their response to mechanical perturbations. Using an optimal-control framework, the authors offer a normative explanation of how both co-articulated and separated sequential movement can be understood as an optimal solution to the task requirements.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96854.3.sa1](https://doi.org/10.7554/eLife.96854.3.sa1)

In their paper, Kalidini et al. investigate why the motor system sometimes coarticulates movements within a sequence. They begin by examining this phenomenon in an optimal feedback controller (OFC) that performs reaching movements to two targets (T1 and T2). They show that coarticulation occurs only when the controller is not required to slow down at T1. When the controller must decelerate at T1, coarticulation does not occur. This observation holds true even though the controller has information about both targets in both scenarios. They test the same experiment on human participants and show that humans also coarticulate the reaches only when they are instructed to treat the first target as a via point. Both in human participants and OFC simulations, whenever the coarticulation is present, the long-latency response to perturbations during the first reach is also informed by the second target- suggesting that the information about the second target is already present in the circuitry that control the long-latency reflex.

All experiments and analyses are standard and clearly explained. Their analysis of long-latency as a measure of coarticulation of sequence items is highly interesting and broadly useful for future experiment design. They successfully demonstrate that one reason the motor system sometimes coarticulates movements is due to high-level instructions on how to execute the sequence. These high-level instructions can, in turn, determine how and to what extent information about future sequence items is utilized by the low-level controller that governs muscle activity. However, the precise interaction between high-level task demands and low-level controllers at the neural tissue level remains an open question.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96854.3.sa2](https://doi.org/10.7554/eLife.96854.3.sa2)

Summary:

In this manuscript the authors examine the question of whether discrete action sequences and coarticulated continuous sequential actions can be produced from the same controller, without having to derive separate control policies for each sequential movement. Using modeling and behavioral experiments, the authors demonstrate that this is indeed possible if the constraints of the policy are appropriately specified. These results are of interest to those interested in motor sequences, but it is unclear whether these findings can be interpreted to apply to the control of sequences more broadly (see weaknesses below).

Strengths:

The authors provide an interesting and novel extension of the stochastic optimal control model to demonstrate how different temporal constraints can lead to either individual or coarticulated movements. The authors use this model to make predictions about patterns of behavior (e.g., in response to perturbations), which they then demonstrate in human participants both by measuring movement kinematics as well as EMG. Together this work supports the authors' primary claims regarding how changes in task instructions (i.e., task constraints) can result in coarticulated or separated movement sequences and the extent to which the subsequent movement goal affects the planning and control of the previous movement.

Weaknesses:

Although this work is quite interesting, it remains unknown whether there is a fundamental distinction between a coarticulated sequence and a single movement passing through a via point (or equivalently, avoiding an obstacle). The notion of a coarticulated sequence brings with it the notion of sequential (sub)movements and temporal structure, whereas the latter can really be treated as more of a constraint on the production of a single continuous movement. The authors suggest that these are not truly different kinds of movements at the level of a control policy, but this remains to be tested experimentally.

It also remains unclear for the theory of optimal feedback control as a whole where and how the cost function and constraints are specified to guide the optimization process. That is, presumably there is the ability for higher-level or explicit description of these constraints, but how they then become incorporated into a control policy remains unclear. With regard to the kind of multi-target constraints proposed here, in typical sequence tasks, while some movements become coarticulated, people also tend to form chunks with distinct chunk boundaries. This presumably means that there is at least some specification of the sequential ordering of these chunks that must exist beyond the control policy and that multiple control policies may still be warranted to execute an entire sequence (otherwise the authors' model might suggest that people can coarticulate forever without needing to exhibit any chunk boundaries). Hence, while the authors fairly convincingly show that a single control policy can lead to separated or coarticulated movements given an appropriate set of constraints, their work does not speak to where or how those constraints are specified, nor to how longer sequences are controlled.
