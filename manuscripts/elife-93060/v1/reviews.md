# Peer review - Round 1

Editors:
- Tatyana O Sharpee, Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.93060.3.sa0](https://doi.org/10.7554/eLife.93060.3.sa0)

This work provides an important and novel framework for interpreting the interactions between recurrent dynamics across stages of neural processing. The authors report that two different kinds of dynamics exist in recurrent networks differing in the extent to which they align with the output weights. The authors also present convincing evidence that both types of dynamics exist in the brain.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93060.3.sa1](https://doi.org/10.7554/eLife.93060.3.sa1)

Summary:

In this work, authors utilize recurrent neural networks (RNNs) to explore the question of when and how neural dynamics and the network's output are related from a geometrical point of view. The authors found that RNNs operate between two extremes: an 'aligned' regime in which the weights and the largest PCs are strongly correlated and an 'oblique' regime where the output weights and the largest PCs are poorly correlated. Large output weights led to oblique dynamics, and small output weights to aligned dynamics. This feature impacts whether networks are robust to perturbation along output directions. Results were linked to experimental data by showing that these different regimes can be identified in neural recordings from several experiments.

Strengths:

Diverse set of relevant tasks

Similarity measure well chosen

Explored various hyperparameter settings

Weaknesses:

One of the major connections to found BCI data with neural variance aligned to the outputs. Maybe I was confused about something, but doesn't this have to be the case based on the design of the experiment? The outputs of the BCI are chosen to align with the largest principal components of the data.

Proposed experiments maybe have already been done (New neural activity patterns emerge with long-term learning, Oby et al. 2019). My understanding of these results is that activity moved to be aligned as the manifold changed, but more analyses could be done to more fully understand the relationship between those experiments and this work.

Analysis of networks was thorough, but connections to neural data were weak. I am thoroughly convinced of the reported effect of large or small output weights in networks. I also think this framing could aid in future studies of interactions between brain regions.

This is an interesting framing to consider the relationship between upstream activity and downstream outputs. As more labs record from several brain regions simultaneously, this work will provide an important theoretical framework for thinking about the relative geometries of neural representations between brain regions.

It will be interesting to compare the relationship between geometries of representations and neural dynamics across connected different brain areas that are closer to the periphery vs. more central.

Exciting to think about the versatility of the oblique regime for shared representations and network dynamics across different computations.

Versatility of oblique regime could lead to differences between subjects in neural data.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93060.3.sa2](https://doi.org/10.7554/eLife.93060.3.sa2)

Summary:

This paper tackles the problem of understanding when the dynamics of neural population activity do and do not align with some target output, such as an arm movement. The authors develop a theoretical framework based on RNNs showing that an alignment of neural dynamics to an output can be simply controlled by the magnitude of the read-out weight vector while the RNN is being trained: small magnitude vectors result in aligned dynamics, where low-dimensional neural activity recapitulates the target; large magnitude vectors result in "oblique" dynamics, where encoding is spread across many dimensions. The paper further explores how the aligned and oblique regimes differ, in particular that the oblique regime allows degenerate solutions for the same target output.

Strengths:

- A really interesting new idea that different dynamics of neural circuits can arise simply from the initial magnitude of the output weight vector: once written out (Eq 3) it becomes obvious, which I take as the mark of a genuinely insightful idea

- The offered framework potentially unifies a collection of separate experimental results and ideas, largely from studies of motor cortex in primate: the idea that much of the ongoing dynamics do not encode movement parameters; the existence of the "null space" of preparatory activity; and that ongoing dynamics of motor cortex can rotate in the same direction even when the arm movement is rotating in opposite directions.

- The main text is well written, with a wide-ranging set of key results synthesised and illustrated well and concisely

- Shows the occurrence of the aligned and oblique regimes generalises across a range of simulated behavioural tasks

- A deep analytical investigation of when the regimes occur and how they evolve over training

- Shows where the oblique regime may be advantageous: allows multiple solutions to the same problem; and differs in sensitivity to perturbation and noise

- An insightful corollary result that noise in training is needed to obtain the oblique regime

- Tests whether the aligned and oblique regimes can be seen in neural recordings from primate cortex in a range of motor control tasks

- The revised text offers greater clarity and precision about when the aligned and oblique regimes occur and in the interpretation of the analyses of neural data

Weaknesses:

- The depth of analytical treatment in the Methods is impressive; however, the paper and the Methods analyses are largely independent, with the numerous results in the latter not being mentioned in the Results or Discussion. It in effect operates as two papers.
