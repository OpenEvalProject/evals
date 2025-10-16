# Peer review - Round 1

Editors:
- Gordon J Berman, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.102906.3.sa0](https://doi.org/10.7554/eLife.102906.3.sa0)

This important study uses reinforcement learning to study how turbulent odor stimuli should be processed to yield successful navigation. The authors find that there is an optimal memory length over which an agent should ignore blanks in the odor to discriminate whether the agent is still inside the plume or outside of it, complementing recent studies using recurrent neural networks and finite state controllers to identify optimal strategies for navigating a turbulent plume. The strength of evidence is compelling, presenting a novel approach to understanding optimal representations for navigation in stochastic sensory environments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102906.3.sa1](https://doi.org/10.7554/eLife.102906.3.sa1)

Overall I found the approach taken by the authors to be clear and convincing. It is striking that the conclusions are similar to those obtained in a recent study using a different computational approach (finite state controllers), and lends confidence to the conclusions about the existence of an optimal memory duration. There are a few questions that could be expanded on in future studies:

(1) Spatial encoding requirements

The manuscript contrasts the approach taken here (reinforcement learning in a gridworld) with strategies that involve a "spatial map" such as infotaxis. However, the gridworld navigation algorithm has an implicit allocentric representation, since movement can be in one of four allocentric directions (up, down, left, right), and wind direction is defined in these coordinates. Future studies might ask if an agent can learn the strategy without a known wind direction if it can only go left/right/forward/back/turn (in egocentric coordinates). In discussing possible algorithms, and the features of this one, it might be helpful to distinguish (1) those that rely only on egocentric computations (run and tumble), (2) those that rely on a single direction cue such as wind direction, (3) those that rely on allocentric representations of direction, and (4) those that rely on a full spatial map of the environment.

(2) Recovery strategy on losing the plume

The authors explore several recovery strategies upon losing the plume, including backtracking, circling, and learned strategies, finding that a learned strategy is optimal. As insects show a variety of recovery strategies that can depend on the model of locomotion, it would be interesting in the future to explore under which conditions various recovery strategies are optimal and whether they can predict the strategies of real animals in different environments.

(3) Is there a minimal representation of odor for efficient navigation?

The authors suggest that the number of olfactory states could potentially be reduced to reduce computational cost. They show that reducing the number of olfactory states to 1 dramatically reduces performance. In the future it would be interesting to identify optimal internal representations of odor for navigation and to compare these to those found in real olfactory systems. Does the optimal number of odor and void states depend on the spatial structure of the turbulence as explored in Figure 5?


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102906.3.sa2](https://doi.org/10.7554/eLife.102906.3.sa2)

Summary:

The authors investigate the problem of olfactory search in turbulent environments using artificial agents trained using tabular Q-learning, a simple and interpretable reinforcement learning (RL) algorithm. The agents are trained solely on odor stimuli, without access to spatial information or prior knowledge about the odor plume's shape. This approach makes the emergent control strategy more biologically plausible for animals navigating exclusively using olfactory signals. The learned strategies show parallels to observed animal behaviors, such as upwind surging and crosswind casting. The approach generalizes well to different environments and effectively handles the intermittency of turbulent odors.

Strengths:

* The use of numerical simulations to generate realistic turbulent fluid dynamics sets this paper apart from studies that rely on idealized or static plumes.

* A key innovation is the introduction of a small set of interpretable olfactory states based on moving averages of odor intensity and sparsity, coupled with an adaptive temporal memory.

* The paper provides a thorough analysis of different recovery strategies when an agent loses the odor trail, offering insights into the trade-offs between various approaches.

* The authors provide a comprehensive performance analysis of their algorithm across a range of environments and recovery strategies, demonstrating the versatility of the approach.

* Finally, the authors list an interesting set of real-world experiments based on their findings, that might invite interest from experimentalists across multiple species.

Weaknesses:

* Using tabular Q-learning is both a strength and a limitation. It's simple and interpretable, making it easier to analyze the learned strategies, but the discrete action space seems somewhat unnatural. In real-world biological systems, actions (like movement) are continuous rather than discrete. Additionally, the ground-frame actions may not map naturally to how animals navigate odor plumes (e.g. insects often navigate based on their own egocentric frame).
