# Predicting non-linear dynamics by stable local learning in a recurrent spiking neural network

## Authors

- Aditya Gilra<sup>1</sup> ([ORCID: 0000-0002-8628-1864](https://orcid.org/0000-0002-8628-1864)) †
- Wulfram Gerstner<sup>1</sup>

### Affiliations

1. School of Computer and Communication Sciences Ecole Polytechnique Federale de Lausanne Lausanne Switzerland

† Corresponding author

## Abstract

The brain needs to predict how the body reacts to motor commands, but how a network of spiking neurons can learn non-linear body dynamics using local, online and stable learning rules is unclear. Here, we present a supervised learning scheme for the feedforward and recurrent connections in a network of heterogeneous spiking neurons. The error in the output is fed back through fixed random connections with a negative gain, causing the network to follow the desired dynamics. The rule for Feedback-based Online Local Learning Of Weights (FOLLOW) is local in the sense that weight changes depend on the presynaptic activity and the error signal projected onto the postsynaptic neuron. We provide examples of learning linear, non-linear and chaotic dynamics, as well as the dynamics of a two-link arm. Under reasonable approximations, we show, using the Lyapunov method, that FOLLOW learning is uniformly stable, with the error going to zero asymptotically.
