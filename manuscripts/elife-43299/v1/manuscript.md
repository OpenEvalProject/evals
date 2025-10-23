# Local online learning in recurrent networks with random feedback

## Authors

- James M Murray<sup>1</sup> ([ORCID: 0000-0003-3706-4895](https://orcid.org/0000-0003-3706-4895)) †

### Affiliations

1. Zuckerman Mind, Brain, and Behavior Institute Columbia University New York United States

† Corresponding author

## Abstract

Recurrent neural networks (RNNs) enable the production and processing of time-dependent signals such as those involved in movement and working memory. Classic gradient-based algorithms for training RNNs have been available for decades, but are inconsistent with biological features of the brain, such as causality and locality. We derive an approximation to gradient-based learning that comports with these constraints by requiring synaptic weight updates to depend only on local information about pre- and postsynaptic activities, in addition to a random feedback projection of the RNN output error. In addition to providing mathematical arguments for the effectiveness of the new learning rule, we show through simulations that it can be used to train an RNN to perform a variety of tasks. Finally, to overcome the difficulty of training over very large numbers of timesteps, we propose an augmented circuit architecture that allows the RNN to concatenate short-duration patterns into longer sequences.
