# A model of hippocampal replay driven by experience and environmental structure facilitates spatial learning

## Authors

- Nicolas Diekmann<sup>1</sup> ([ORCID: 0000-0003-3638-7617](https://orcid.org/0000-0003-3638-7617))
- Sen Cheng<sup>1</sup> ([ORCID: 0000-0002-6719-8029](https://orcid.org/0000-0002-6719-8029)) †

### Affiliations

1. Faculty of Computer Science Ruhr University Bochum Bochum Germany

† Corresponding author

## Abstract

Replay of neuronal sequences in the hippocampus during resting states and sleep play an important role in learning and memory consolidation. Consistent with these functions, replay sequences have been shown to obey current spatial constraints. Nevertheless, replay does not necessarily reflect previous behavior and can construct never-experienced sequences. Here we propose a stochastic replay mechanism that prioritizes experiences based on three variables: 1. Experience strength, 2. experience similarity, and 3. inhibition of return. Using this prioritized replay mechanism to train reinforcement learning agents leads to far better performance than using random replay. Its performance is close to the state-of-the-art, but computationally intensive, algorithm by Mattar & Daw (2018). Importantly, our model reproduces diverse types of replay because of the stochasticity of the replay mechanism and experience-dependent differences between the three variables. In conclusion, a unified replay mechanism generates diverse replay statistics and is efficient in driving spatial learning.
