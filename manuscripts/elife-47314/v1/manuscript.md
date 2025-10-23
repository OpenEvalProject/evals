# Brian 2, an intuitive and efficient neural simulator

## Authors

- Marcel Stimberg<sup>1</sup> ([ORCID: 0000-0002-2648-4790](https://orcid.org/0000-0002-2648-4790)) †
- Romain Brette<sup>1</sup> ([ORCID: 0000-0003-0110-1623](https://orcid.org/0000-0003-0110-1623))
- Dan FM Goodman<sup>2</sup> ([ORCID: 0000-0003-1007-6474](https://orcid.org/0000-0003-1007-6474))

### Affiliations

1. Institut de la Vision Sorbonne Université, INSERM, CNRS Paris France
2. Department of Electrical and Electronic Engineering Imperial College London London United Kingdom

† Corresponding author

## Abstract

Brian 2 allows scientists to simply and efficiently simulate spiking neural network models. These models can feature novel dynamical equations, their interactions with the environment, and experimental protocols. To preserve high performance when defining new models, most simulators offer two options: low-level programming or description languages. The first option requires expertise, is prone to errors, and is problematic for reproducibility. The second option cannot describe all aspects of a computational experiment, such as the potentially complex logic of a stimulation protocol. Brian addresses these issues using runtime code generation. Scientists write code with simple and concise high-level descriptions, and Brian transforms them into efficient low-level code that can run interleaved with their code. We illustrate this with several challenging examples: a plastic model of the pyloric network, a closed-loop sensorimotor model, a programmatic exploration of a neuron model, and an auditory model with real-time input.
