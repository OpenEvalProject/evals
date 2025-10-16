# Peer review - Round 1

Editors:
- Jing Sui, Beijing Normal University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101069.3.sa0](https://doi.org/10.7554/eLife.101069.3.sa0)

The authors proposed an important novel deep-learning framework to estimate posterior distributions of tissue microstructure parameters. The method shows superior performance to conventional Bayesian approaches and there is convincing evidence for generalizing the method to use data from different protocol acquisitions and work with models of varying complexity.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101069.3.sa1](https://doi.org/10.7554/eLife.101069.3.sa1)

The authors proposed a framework to estimate the posterior distribution of parameters in biophysical models. The framework has two modules: the first MLP module is used to reduce data dimensionality and the second NPE module is used to approximate the desired posterior distribution. The results show that the MLP module can capture additional information compared to manually defined summary statistics. By using the NPE module, the repetitive evaluation of the forward model is avoided, thus making the framework computationally efficient. The results show the framework has promise in identifying degeneracy. This is an interesting work.

Comment on revised version:

The authors have addressed all the raised concerns and made appropriate modifications to the manuscript. The changes have improved the clarity, methodology, and overall quality of the paper. Given these improvements, I believe the paper now meets the standards for publication in this journal.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101069.3.sa2](https://doi.org/10.7554/eLife.101069.3.sa2)

Summary:

The authors improve the work of Jallais et al. (2022) by including a novel module capable of automatically learning feature selection from different acquisition protocols inside a supervised learning framework. Combining the module above with an estimation framework for estimating the posterior distribution of model parameters, they obtain rich probabilistic information (uncertainty and degeneracy) on the parameters in a reasonable computation time.

The main contributions of the work are:

(1) The whole framework allows the user to avoid manually defining summary statistics, which may be slow and tedious and affect the quality of the results.

(2) The authors tested the proposal by tackling three different biophysical models for brain tissue and using data with characteristics commonly used by the diffusion-MR-microstructure research community.

(3) The authors validated their method well with the state-of-the-art.

(4) The methodology allows the quantification of the inherent model's degeneration and how it increases with strong noise.

The authors showed the utility of their proposal by computing complex parameter descriptors automatically in an achievable time for three different and relevant biophysical models.

Importantly, this proposal promotes tackling, analyzing, and considering the degenerated nature of the most used models in brain microstructure estimation.
