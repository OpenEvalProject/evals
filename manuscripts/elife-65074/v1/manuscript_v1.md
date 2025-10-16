# Likelihood approximation networks (LANs) for fast inference of simulation models in cognitive neuroscience

## Authors

- Alexander Fengler<sup>1</sup> †
- Lakshmi N Govindarajan<sup>1</sup> ([ORCID: 0000-0002-0936-2919](https://orcid.org/0000-0002-0936-2919))
- Tony Chen<sup>2</sup>
- Michael J Frank<sup>1</sup> ([ORCID: 0000-0001-8451-0523](https://orcid.org/0000-0001-8451-0523)) †

### Affiliations

1. Robert J and Nancy D Carney Institute for Brain Science; Cognitive, Linguistic & Psychological Sciences Brown University Providence United States
2. Psychology and Neuroscience Boston College Boston United States

† Corresponding author

## Abstract

In cognitive neuroscience, computational modeling can formally adjudicate between theories and affords quantitative fits to behavioral/brain data. Pragmatically, however, the space of plausible generative models considered is dramatically limited by the set of models with known likelihood functions. For many models, the lack of a closed-form likelihood typically impedes Bayesian inference methods. As a result, standard models are evaluated for convenience, even when other models might be superior. Likelihood-free methods exist but are limited by their computational cost or their restriction to particular inference scenarios. Here, we propose neural networks that learn approximate likelihoods for arbitrary generative models, allowing fast posterior sampling with only a one-off cost for model simulations that is amortized for future inference. We show that these methods can accurately recover posterior parameter distributions for a variety of neurocognitive process models. We provide code allowing users to deploy these methods for arbitrary hierarchical model instantiations without further training.
