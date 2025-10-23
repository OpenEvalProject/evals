# Peer review - Round 1

Editors:
- Tatyana O Sharpee, Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96566.3.sa0](https://doi.org/10.7554/eLife.96566.3.sa0)

This work is an important contribution to the development of a biologically plausible theory of statistical modeling of spiking activity. The authors convincingly implemented the statistical inference of input likelihood in a simple neural circuit, demonstrating the relationship between synaptic homeostasis, neural representations, and computational accuracy. This work will be of interest to neuroscientists, both theoretical and experimental, who are exploring how statistical computation is implemented in neural networks.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96566.3.sa1](https://doi.org/10.7554/eLife.96566.3.sa1)

Summary

A novel statistical model of neural population activity called the Random Projection model has been recently proposed. Not only is this model accurate, efficient, and scalable, but also is naturally implemented as a shallow neural network. This work proposes a new class of RP model called the reshaped RP model. Inheriting the virtue of the original RP model, the proposed model is more accurate in terms of data fitting and efficient in terms of lower firing rate than the original, as well as compatible with various biological constraints. In particular, the authors have demonstrated that normalizing the total synaptic input in the reshaped model has a homeostatic effect on the firing rates of the neurons, resulting in even more efficient representations with equivalent accuracy. These results suggest that synaptic normalization contributes to synaptic homeostasis as well as efficiency in neural encoding.

Strength

This paper demonstrates that the accuracy and efficiency of the random projection models can be improved by extending the model with reshaped projections. Furthermore, it broadens the applicability of the model under biological constraints of synaptic regularization. It also suggests the advantage of the sparse connectivity structure over the fully connected model for modeling spiking statistics. In summary, this work successfully integrates two different elements, statistical modeling of the spikes and synaptic homeostasis in a single biologically plausible neural network model. The authors logically demonstrate their arguments with clear visual presentations and well-structured text, facilitating an unambiguous understanding for readers.

Discussions

The authors have clearly responded to most of our questions in the revised manuscript and we are happy to recommend publishing the final version of the article as it is. Below, we would like to present some alternative interpretations of the results. These comments are not exclusive with the claims made in the articles; it is rather intended to enhance the understanding of readers by providing additional perspectives.

As summarized above, the main contribution of the work consists of two parts; (1) the reshaped RP model achieved higher performance in explaining the statistics of the spiking activity of cortical neurons with more efficient representations (=lower firing rate), (2) synaptic homeostatic normalization in the reshaped RP model yields even more efficient representations without impairing the fitting performance.

For part (1),

Suppl. Fig. 1B compares reshaped RP models with RP and RP with pruning and replacement (R&P). The better performance of RP with P&R might imply the advantage of pruning over gradient descent in this setting, reflecting the non-convexities of the problem. Alternatively, it might suggest the benefit of the increased number of parameters, since pruning allows the network to explore the broader parameter space during the learning process. This latter view might partially explain the superiority of the reshaped RP model over the original RP model.

It is interesting that the backprop model has higher firing rate than the reshaped model (Fig. 1D). This trend is unchanged when optimization of the neural threshold is also allowed (Supp. Fig. 2A). Since backprop model overperforms reshaped model slightly but robustly, high firing rates in the backprop model might be a genuine feature of the spike statistics.

For part (2),

We note that λ regulates the average firing rate, since maximizing the entropy <-ln p(x)> with a regularization term -λ <Σi f(xi)> results in λi = λ for all i in the Boltzmann distribution of eq. 2. Suppl. Fig. 2B could be understood as demonstrating this "homeostatic" effect of λ.

Suppl. Fig. 3 could be interpreted as demonstrating the interaction of two different homeostatic mechanisms: one at the firing-rate level (as regulated by λ) and the other at the synaptic level (as regulated by φ). It shows that the range of synaptic constraints where the fitting performance is not impaired differs by the value of λ. For example, if lambda is small (λ = 0.25), synaptic constraint can easily deteriorate the performance; on the other hand, if lambda is large (λ = 4), performance remains unchanged under strict synaptic constraint. Considering that practically we are most interested in the regime where the model performs best (λ = 2.0), an advantageous feature of the homeostatic model is that homeostatic constraint is harmless at λ=2.0 for the wide range of constraints.
