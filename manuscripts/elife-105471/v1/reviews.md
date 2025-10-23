# Peer review - Round 1

Editors:
- Thierry Mora, https://ror.org/05a0dhs15 École Normale Supérieure - PSL France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105471.3.sa0](https://doi.org/10.7554/eLife.105471.3.sa0)

This study provides an important method to model the statistical biases of hypermutations during the affinity maturation of antibodies. The authors show convincingly that their model outperforms previous methods with fewer parameters; this is made possible by the use of machine learning to expand the context dependence of the mutation bias. They also show that models learned from nonsynonymous mutations and from out-of-frame sequences are different, prompting new questions about germinal center function. Strengths of the study include an open-access tool for using the model, a careful curation of existing data sets, and a rigorous benchmark; it is also shown that current machine-learning methods are currently limited by the availability of data, which explains the only modest gain in model performance afforded by modern machine learning.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105471.3.sa1](https://doi.org/10.7554/eLife.105471.3.sa1)

Summary:

This paper introduces a new class of machine learning models for capturing how likely a specific nucleotide in a rearranged IG gene is to undergo somatic hypermutation. These models modestly outperform existing state-of-the-art efforts, despite having fewer free parameters. A surprising finding is that models trained on all mutations from non-functional rearrangements give divergent results from those trained on only silent mutations from functional rearrangements.

Strengths:

* The new model structure is quite clever and will provide a powerful way to explore larger models.

* Careful attention is paid to curating and processing large existing data sets.

* The authors are to be commended for their efforts to communicate with the developers of previous models and use the strongest possible versions of those in their current evaluation.

Weaknesses:

* No significant weaknesses noted


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105471.3.sa2](https://doi.org/10.7554/eLife.105471.3.sa2)

This work offers an insightful contribution for researchers in computational biology, immunology, and machine learning. By employing a 3-mer embedding and CNN architecture, the authors demonstrate that it is possible to extend sequence context without exponentially increasing the model's complexity. Key findings include:

• Efficiency and Performance: Thrifty CNNs outperform traditional 5-mer models and match the performance of significantly larger models like DeepSHM.

• Neutral Mutation Data: A distinction is made between using synonymous mutations and out-of-frame sequences for model training, with evidence suggesting these methods capture different aspects of SHM, or different biases in the type of data.

• Open Source Contributions: The release of a Python package and pretrained models adds practical value for the community.

However, readers should be aware of the limitations. The improvements over existing models are modest, and the work is constrained by the availability of high-quality out-of-frame sequence data. The study also highlights that more complex modeling techniques, like transformers, did not enhance predictive performance, which underscores the role of data availability in such studies.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105471.3.sa3](https://doi.org/10.7554/eLife.105471.3.sa3)

Summary:

Modeling and estimating sequence context biases during B cell somatic hypermutation is important for accurately modeling B cell evolution to better understand responses to infection and vaccination. Sung et al. introduce new statistical models that capture a wider sequence context of somatic hypermutation with a comparatively small number of additional parameters. They demonstrate their model's performance with rigorous testing across multiple subjects and datasets. Prior work has captured the mutation biases of fixed 3-, 5-, and 7-mers, but each of these expansions has significantly more parameters. The authors developed a machine-learning-based approach to learn these biases using wider contexts with comparatively few parameters.

Strengths:

Well motivated and defined problem. Clever solution to expand nucleotide context. Complete separation of training and test data by using different subjects for training vs testing. Release of open-source tools and scripts for reproducibility.

The authors have addressed my prior comments.
