# Peer review - Round 1

Editors:
- Roshan Cools, Donders Institute for Brain, Cognition and Behaviour, Radboud University Nijmegen Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101371.3.sa0](https://doi.org/10.7554/eLife.101371.3.sa0)

This important work describes results from a set of simulation and empirical studies of a set-up assessing exploratory behavior in a potentially rewarding environment that contains danger. The core idea is that an instrumental agent can be helped to be both effective and safe, thus avoiding excessive danger, during exploratory behavior, if the influence of an independent Pavlovian fear is flexibly gated based on uncertainty. This work is grounded in previous foundational work on Pavlovian control of instrumental choice, and significantly extends prior work showing that the impact of Pavlovian reward biases can be flexibly gated. The conclusion that safe but effective exploration can be achieved based on a flexibly weighted combination of a Pavlovian and an instrumental agent is convincing.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101371.3.sa1](https://doi.org/10.7554/eLife.101371.3.sa1)

Summary:

This paper provides a computational model of a synthetic task in which an agent needs to find a trajectory to a rewarding goal in a 2D-grid world, in which certain grid blocks incur a punishment. In a completely unrelated setup without explicit rewards, they then provide a model that explains data from an approach-avoidance experiment in which an agent needs to decide whether to approach, or withdraw from, a jellyfish, in order to avoid a pain stimulus, with no explicit rewards. Both models include components that are labelled as "Pavlovian"; hence the authors argue that their data show that the brain uses a "Pavlovian" fear system in complex navigational and approach-avoid decisions.

In the first setup, they simulate a model in which a "Pavlovian" component learns about punishment in each grid block, where as a Q-learner learns about the optimal path to the goal, using a scalar loss function for rewards and punishments. "Pavlovian" and Q-learning components are then weighed at each step to produce an action. Unsurprisingly, the authors find that including the "Pavlovian" component into the model reduces the cumulative punishment incurred, and this increases as the weight of the "Pavlovian" system increases. The paper does not explore to what extent increasing the punishment loss (while keeping reward loss constant) would lead to the same outcomes with a simpler model architecture.

In the second setup, an agent learns about punishments alone. So-called "Pavlovian biases" have previously been demonstrated in this task (i.e. an over avoidance when the correct decision is to approach). The authors explore several models to account for the Pavlovian biases.

Strengths:

Overall, the modelling exercises are interesting and relevant and incrementally expand the space of existing models.

Weaknesses:

For the first task, the simulation results are not compared to a simple Q-learning model. The second task is somewhat artificial, a problem compounded by the virtual reality setup. According to the cover story, participants get "stung by a jellyfish" on average 88 times during the experiment. In one condition, withdrawal from a jelly fish lead to a sting.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101371.3.sa2](https://doi.org/10.7554/eLife.101371.3.sa2)

Summary:

The authors tested the efficiency of a model combining Pavlovian fear valuation and instrumental valuation. This model is amenable to many behavioral decision and learning setups - some of which have been or will be designed to test differences in patients with mental disorders (e.g., anxiety disorder, OCD, etc.).

Strengths:

(1) Simplicity of the model which can at the same time model rather complex environments.

(2) Introduction of a flexible omega parameter.

(3) Direct application to a rather advanced VR task.

(4) The paper is extremely well written. It was a joy to read.

Weaknesses:

Almost none! In very few cases, the explanations could be a bit better.

Comments on revised version:

No further comments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101371.3.sa3](https://doi.org/10.7554/eLife.101371.3.sa3)

Summary:

This paper aims to address the problem of exploring potentially rewarding environments that contain danger, based on the assumption that an independent Pavlovian fear learning system can help guide an agent during exploratory behaviour such that it avoids severe danger. This is important given that otherwise later gains seem to outweigh early threats, and agents may end up putting themselves in danger when it is advisable not to do so.

The authors develop a computational model of exploratory behaviour that accounts for both instrumental and Pavlovian influences, combining the two according to uncertainty in the rewards. The result is that Pavlovian avoidance has a greater influence when the agent is uncertain about rewards.

Strengths:

The study does a thorough job of testing this model using both simulations and data from human participants performing an avoidance task. Simulations demonstrate that the model can produce "safe" behaviour, where the agent may not necessarily achieve the highest possible reward but ensures that losses are limited. Interestingly, the model appears to describe human avoidance behaviour in a task that tests for Pavlovian avoidance influences better than a model that doesn't adapt the balance between Pavlovian and instrumental based on uncertainty. The methods are robust, and generally there is little to criticise about the study.

Weaknesses:

The methods are robust, and generally there is little to criticise about the study. The extent of the testing in human participants is fairly limited, but goes far enough to demonstrate that the model can account for human behaviour in an exemplar task. There are, however, some elements of the model that are unrealistic (for example, the fact that pre-training is required to select actions with a Pavlovian bias would require the agent to explore the environment initially and encounter a vast amount of danger in order to learn how to avoid the danger later), although this could simply reflect a lengthy evolutionary process.
