# Peer review - Round 1

Editors:
- C Brandon Ogbunugafor, Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87895.3.sa0](https://doi.org/10.7554/eLife.87895.3.sa0)

This important study describes a high performance computational approach to interrogate how microscopic epistasis and clonal interference affect evolutionary dynamics in a spin glass model of microbial evolution. The study offers several insights that can aid in our understanding of the forces that operate in adaptive evolution. The evidence provided is compelling, with its rigorous use of models and analytical descriptions of how these forces manifest in evolution.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87895.3.sa1](https://doi.org/10.7554/eLife.87895.3.sa1)

This paper presents extensive numerical simulations using a model that incorporates up to second-order epistasis to study the joint effects of microscopic epistasis and clonal interference on the evolutionary dynamics of a microbial population. Previous works that explicitly modeled microscopic epistasis typically assumed strong selection & weak mutation (SSWM), a condition that is generally not met in real-life evolutionary processes. Alternatively, another class of models coarse-grained the effects of microscopic epistasis into a generic distribution of fitness effects. The framework introduced in this paper represents an important advance with respect to these previous approaches, allowing for the explicit modeling of microscopic epistasis in non-SSWM scenarios. The modeling framework presented promises to be a valuable tool to study microbial evolution in silico.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87895.3.sa2](https://doi.org/10.7554/eLife.87895.3.sa2)

This paper presents an extensive numerical study of microbial evolution using a model of fitness inspired by spin glass physics. It places special emphasis on elucidating the combined effects of microscopic epistasis, which dictates how the fitness effect of a mutation depends on the genetic background on which it occurs, and clonal interference, which describes the proliferation of and competition between multiple strains. Both microscopic epistasis and clonal interference have been observed in microbial evolution experiments, and are chief contributors to the complexity of evolutionary dynamics. Correlations between random mutations and nonlinearities associated with interactions between sub-populations consisting of competing strains make it extremely challenging to make quantitative theoretical predictions for evolutionary dynamics and associated observables such as the mean fitness. While the body of theoretical and computational research on modeling evolutionary dynamics is extensive, most theoretical efforts rely on making simplifications such as the strong selection weak mutation (SSWM) limit, which neglects clonal interference, or assumptions about the distribution of fitness effects that are not experimentally verifiable.

The authors have addressed this challenge by running a numerical microbial evolution experiment over realistic population sizes (~ 100 million cells) and timescales (~ 10,000 generations) using a spin glass model of fitness that considers pairwise interactions between mutations on distinct genetic loci. By independently tuning mutation rate as well as the strength of epistasis, the authors have shown that epistasis generically slows down the growth of fitness trajectories regardless of the amount of clonal interference. On the other hand, in the absence of epistasis, clonal interference speeds up the growth of fitness trajectories, but leaves the growth unchanged in the presence of epistasis. The authors quantitatively characterize these observations using asymptotic power law fits to the mean fitness trajectories. Further, the authors employ more simplified macroscopic models that are informed by their empirical findings, to reveal the mechanistic origins of the epistasis mediated slowing down of fitness growth. Specifically, they show that epistasis leads to a broadening of the distribution of fitness increments, leading to the fixation of a large number of mutations that confer small benefits. Effectively, this leads to an increase in the number of fixed mutations required to climb the fitness peak. This increased number of required beneficial mutations together with the decreasing availability of beneficial mutations at high fitness lead to the slowdown of fitness growth. The authors' data analysis is quite solid and their conclusions are well supported by quantitative macroscopic models. The paper also includes an interesting analysis of dynamical correlations between mutations, using tools developed in the spin glass literature.

One of the highlights of this paper is the author's astute choice of model, which strikes an impressive balance between complexity, flexibility, and numerical accessibility. In particular, the authors were able to achieve results over realistic population sizes and timescales largely because of the amenability of the model to the implementation of an efficient simulation algorithm. At the same time, the strength of epistasis and clonal interference can be tuned in a facile manner, enabling the authors to map out a phase diagram spanning these two axes. One could argue that the numerical scheme employed here would only work for a specific class of models, and is therefore not generalizable to all models of evolutionary dynamics. While this is likely true, the model is capable of recapitulating several complex aspects of microbial evolution, and is therefore not unduly restrictive.

Spin glass physics has already provided significant insights into a wide range of topics in the life sciences including protein folding, neuroscience, ecology and evolution. The present work carries this approach forward, with immediate implications for microbial evolution, and potential implications in related areas of research such as microbial ecology. In addition to the theoretical value of spin glass physics, the high performance algorithm developed in this work lays the foundation for formulating data driven approaches aimed at understanding evolutionary dynamics. In the future, there is considerable scope for utilizing data generated by such models to train machine learning algorithms for quantifying parameters associated with epistasis, clonal interference, and the distribution of fitness effects in laboratory experiments.
