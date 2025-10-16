# Peer review - Round 1

Editors:
- Richard Naud, University of Ottawa Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.104101.4.sa0](https://doi.org/10.7554/eLife.104101.4.sa0)

In this important study, the authors model reinforcement-learning experiments using a recurrent neural network. The work examines if the detailed credit assignment necessary for back-propagation through time can be replaced with random feedback. The authors provide solid evidence that the solution is adequate within relatively simple tasks.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104101.4.sa1](https://doi.org/10.7554/eLife.104101.4.sa1)

Summary:

Can a plastic RNN serve as a basis function for learning to estimate value. In previous work this was shown to be the case, with a similar architecture to that proposed here. The learning rule in previous work was back-prop with an objective function that was the TD error function (delta) squared. Such a learning rule is non-local as the changes in weights within the RNN, and from inputs to the RNN depends on the weights from the RNN to the output, which estimates value. This is non-local, and in addition, these weights themselves change over learning. The main idea in this paper is to examine if replacing the values of these non-local changing weights, used for credit assignment, with random fixed weights can still produce similar results to those obtained with complete bp. This random feedback approach is motivated by a similar approach used for deep feed-forward neural networks.

This work shows that this random feedback in credit assignment performs well but is not as well as the precise gradient-based approach. When more constraints due to biological plausibility are imposed performance degrades. These results are consistent with previous results on random feedback.

Strengths:

The authors show that random feedback can approximate well a model trained with detailed credit assignment.

The authors simulate several experiments including some with probabilistic reward schedules and show results similar to those obtained with detailed credit assignments as well as in experiments.

The paper examines the impact of more biologically realistic learning rules and the results are still quite similar to the detailed back-prop model.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104101.4.sa2](https://doi.org/10.7554/eLife.104101.4.sa2)

Summary:

Tsurumi et al. show that recurrent neural networks can learn state and value representations in simple reinforcement learning tasks when trained with random feedback weights. The traditional method of learning for recurrent network in such tasks (backpropogation through time) requires feedback weights which are a transposed copy of the feed-forward weights, a biologically implausible assumption. This manuscript builds on previous work regarding "random feedback alignment" and "value-RNNs", and extends them to a reinforcement learning context. The authors also demonstrate that certain non-negative constraints can enforce a "loose alignment" of feedback weights. The author's results suggest that random feedback may be a powerful tool of learning in biological networks, even in reinforcement learning tasks.

Strengths:

The authors describe well the issues regarding biologically plausible learning in recurrent networks and in reinforcement learning tasks. They take care to propose networks which might be implemented in biological systems and compare their proposed learning rules to those already existing in literature. Further, they use small networks on relatively simple tasks, which allows for easier intuition into the learning dynamics.

Weaknesses:

The principles discovered by the authors in these smaller networks are not applied to larger networks or more complicated tasks with long temporal delays (>100 timesteps), so it remains unclear to what degree these methods can scale or can be used more generally.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104101.4.sa3](https://doi.org/10.7554/eLife.104101.4.sa3)

Summary:

The paper studies learning rules in a simple sigmoidal recurrent neural network setting. The recurrent network has a single layer of 10 to 40 units. It is first confirmed that feedback alignment (FA) can learn a value function in this setting. Then so-called bio-plausible constraints are added: (1) when value weights (readout) is non-negative, (2) when the activity is non-negative (normal sigmoid rather than downscaled between -0.5 and 0.5), (3) when the feedback weights are non-negative, (4) when the learning rule is revised to be monotic: the weights are not downregulated. In the simple task considered all four biological features do not appear to impair totally the learning.

Strengths:

(1) The learning rules are implemented in a low-level fashion of the form: (pre-synaptic-activity) x (post-synaptic-activity) x feedback x RPE. Which is therefore interpretable in terms of measurable quantities in the wet-lab.

(2) I find that non-negative FA (FA with non negative c and w) is the most valuable theoretical insight of this paper: I understand why the alignment between w and c is automatically better at initialization.

(3) The task choice is relevant, since it connects with experimental settings of reward conditioning with possible plasticity measurements.
