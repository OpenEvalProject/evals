# Peer review - Round 1

Editors:
- Rui Ponte Costa, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.103660.3.sa0](https://doi.org/10.7554/eLife.103660.3.sa0)

The findings of this study are valuable, offering insights into the neural representation of reversal probability in decision-making tasks, with potential implications for understanding flexible behavior in changing environments. The study contains interesting comparisons between neural data and models, including evidence for partial consistency with line attractor models in this probabilistic reversal learning task. However, it remains incomplete due to issues related to how the RNN training and the analysis of its dynamics, which renders the evidence as not complete.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103660.3.sa1](https://doi.org/10.7554/eLife.103660.3.sa1)

The authors aimed to investigate how the probability of a reversal in a decision-making task is computed in cortical neurons. They analyzed neural activity in the prefrontal cortex of monkeys and units in recurrent neural networks (RNNs) trained on a similar task. Their goal was to understand how the dynamical systems that implement computation perform a probabilistic reversal learning task in RNNs and nonhuman primates.

Major strengths and weaknesses:

Strengths:

(1) Integrative Approach: The study exemplifies a modern approach by combining empirical data from monkey experiments with computational modeling using RNNs. This integration allows for a more comprehensive understanding of the dynamical systems that implement computation in both biological and artificial neural networks.

(2) The focus on using perturbations to identify causal relationships in dynamical systems is a good goal. This approach aims to go beyond correlational observations.

(3) The revised manuscript provides a more nuanced interpretation of the dynamics, reconciling the observations with aspects of line attractor models.

Weaknesses:

(1) The use of targeted dimensionality reduction (TDR) to identify the axis determining reversal probability may not necessarily isolate the dimension along which the RNN computes reversal probability. This should be computed from the RNN update itself rather than through a readout of network variance. Depending on how this is formulated, it could be something like the Jacobian of the state update with respect to inputs at input onset and with respect to the state during relaxation dynamics. This is worth thinking through further. It's important to try to take advantage of access afforded by using RNNs rather than solely relying on analyses available to us in neural data.

Appraisal of aims and conclusions:

The authors have substantially revised their interpretation of the results to reconcile their findings with line attractor models. They now acknowledge that their observation of reward integration explaining reversal probability activity (x_rev) is compatible with line attractor models, which addresses one of my main concerns.

Their expanded analysis now differentiates between two activity modes: (1) substantial non-stationary dynamics during a trial (incompatible with line attractors) and (2) stationary and stable dynamics at trial start (compatible with point attractors and line attractor models). This dual characterization provides a more complete picture of the dynamical system and highlights the composability of dynamical features.

Likely impact and utility:

This work makes a stronger contribution to our understanding of how probabilistic information is represented in neural circuits with intervening behaviors. The augmented model that combines elements of attractor dynamics with non-stationary trajectories offers a more comprehensive framework for understanding neural computations in decision-making tasks.

The data and methods could be useful to the community. While the authors have improved their analysis of network dynamics, additional reverse engineering that takes full advantage of access to the RNN's update equations could further strengthen the work.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103660.3.sa2](https://doi.org/10.7554/eLife.103660.3.sa2)

Summary:

In this work the authors trained RNN to perform a reversal task also performed by animals while PFC activity is recorded. The authors devised a new method to train RNN on this type of reversal task, which in principle ensures that the behavior of the RNN matches the behavior of the animal. They then performed some analysis of neural activity, both RNN and PFC recording, focusing on the neural representation of the reversal probability and its evolution across trials. Given the analysis presented, it has been difficult for me to asses at which point RNN can reasonably be compared to PFC recordings.

Strengths:

Focusing on a reversal task, the authors address a challenge in RNN training, as they do not use a standard supervised learning procedure where the desired output is available for each trial. They propose a new way of doing that.

They attempt to confront RNN and neural recordings in behaving animals.

Weaknesses:

It would be nice to better articulate the analysis results of the two training set-ups (with and without 0 response during fixation). The dynamical system analysis is confusing, the notions of stationary and non-stationary dynamics and its relationship with attractors are puzzling. Is there a line attractor in one case (with inputs orthogonal to the integration direction being called back to the attractor, and reward input aligned with the stable direction)? In the other case, do we have a cylindrical attracting manifold on which activity circles around and is pushed along the axis of the cylinder by reward inputs? Which case is closest to the PFC recordings?


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103660.3.sa3](https://doi.org/10.7554/eLife.103660.3.sa3)

Summary:

Kim et al. present a study of the neural dynamics underlying reversal learning in monkey PFC and neural networks. Their main finding is that neural activity during fixation resembles a line attractor storing the current belief of the reversal state of the task. This is followed by richer dynamics unfolding throughout the remainder of the trial, which eventually converge to a new point on the line attractor by the start of the next trial. The idea of studying neural dynamics throughout the task (including intervening behaviour) is interesting, and the data provides some insights into the neural dynamics driving reversal learning. The modelling seems to support the analyses, but both the modelling and analyses also leave several open questions.

Strengths:

The paper addresses an interesting topic of the neural dynamics underlying reversal learning in PFC, using a combination of biological and simulated data. Reversal learning has been studied extensively in neuroscience, but this paper takes a step further by analysing neural dynamics throughout the trials instead of focusing on just the evidence integration epoch.

The authors show some close parallels between the experimental data and RNN simulations, both in terms of behaviour and neural dynamics. The analyses of how rewarded and unrewarded trials differentially affect dynamics throughout the trials in RNNs and PFC were particularly interesting. This work has the potential to provide new insights into the neural underpinnings of reversal learning.

Weaknesses:

Data analyses:

While the analyses seem mostly sound, one shortcoming is that they are all aligned to the inferred reversal trial rather than the true experimental reversal trial. For example, the analyses showing that 'x_rev' decays strongly after the reversal trial, irrespective of the reward outcome, seem like they are true essentially by design. The choice to align to the inferred reversal trial also makes this trial seem 'special' (e.g. in Fig 2 & Fig 6A), but it is unclear whether this is a real feature of the data or an artifact of effectively conditioning on a change in behaviour. It would be useful to investigate whether any of these analyses differ when aligned to the true reversal trial. It is also unsurprising that x_rev increases before the reversal and decreases after the reversal (it is hard to imagine a system where this is not the case), yet all of Fig 6 and several other analyses are devoted to this point.

Most of the analyses focus on the dynamics specifically in the x_rev subspace, but a major point of the paper is to say that biological (and artificial) networks may also have to do other things at different times in the trial. If that is the case, it would be interesting to also ask what happens in other subspaces of neural activity, which are not specifically related to evidence integration or choice - are there other subspaces that explain substantial variance? Do they relate to any meaningful features of the experiment?

This is especially important when considering analyses trying to establish the presence (or absence) of attractor dynamics in the circuit. In particular, activity in the x_rev subspace both affects and depends on other subspaces of neural activity, so it is not as meaningful to analyse the dynamics of this subspace in isolation. It would e.g. have been preferable to analyse the early-trial dynamics in the full state space and then possibly projecting onto x_rev, rather than first projecting activity onto x_rev and then fitting a linear autoregressive model.

Modelling:

There are a number of surprising and non-standard modelling choices made in this paper. For example, the choice to only use inhibitory neurons is non-conventional and it is not clear whether and how this impacts the results. The inputs are also provided without any learnable input weights, which makes it harder to interpret the input-driven dynamics during the different phases of a trial.

It is surprising that the RNN is "trained to flip its preferred choice a few trials after the inferred scheduled reversal trial", with the reversal trial inferred by an ideal Bayesian observer. A more natural approach would be to directly train the RNN to solve the task (by predicting the optimal choice) and then investigating the emergent behaviour & dynamics. If the authors prefer their imitation learning approach, it is also surprising that the network is trained to predict the reversal trial inferred using Bayesian smoothing instead of Bayesian filtering.

Finally, it was surprising that the network is trained and tested with different block lengths (24 & 36 trials, respectively), and it is not mentioned whether or how this affects behaviour.
