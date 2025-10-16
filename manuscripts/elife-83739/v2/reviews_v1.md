# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/05a0dhs15 Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83739.sa0](https://doi.org/10.7554/eLife.83739.sa0)

This important work demonstrates a significant asymmetry between the connectivity statistics of the left and right hemispheres of the Drosophila larva brain. The evidence supporting the conclusions is compelling and represents a first step toward the development of statistical tests for comparing pairs of connectomes more generally. This work will therefore be of interest to the broad neuroscience community.


---

# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/05a0dhs15 Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83739.sa1](https://doi.org/10.7554/eLife.83739.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Generative network modeling reveals quantitative definitions of bilateral symmetry exhibited by a whole insect brain connectome" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another. Both reviewers are very enthusiastic about the paper and have minor comments that should be easy to address (see below).

Reviewer #1 (Recommendations for the authors):

This study is very clear and well-presented both at the level of the writing and the figures. I only have a couple of questions/recommendations for the authors:

1) In the stochastic block model approach, the authors find differences in 6 group-to-group connections (that all showed higher probabilities in the right hemisphere consistent with the higher density of the right hemisphere). After adjusting for density, they found two group-to-group connections that remain different. When doing this, their assumption is that the density is uniform across the brain hemisphere. However, it is also possible that the density of the network varies to some degree depending on brain areas and neuron types. Could the authors compute the density for subnetworks or groups of neurons within the hemispheres to determine whether the density is relatively constant within a given hemisphere? For example, removing KC slightly decreased the densities in both hemispheres and slightly increased the difference in densities between the left and the right hemispheres (0,91 versus 0.93 ratios). Having a subnetwork with different trends in density (no difference between left and right or higher density on the left) could potentially introduce a bias when comparing group-to-group probabilities adjusted by density.

2) When exploring the definitions of an edge the authors found that using a threshold to only compare stronger connections and also when using input percentage rather than synaptic count, they were less likely to find differences between the compared network. Did the authors try to compare the connectivity involving KC (they found were different between the hemispheres using SBM) using these edge definitions and thresholds? Do they still find differences?

Reviewer #2 (Recommendations for the authors):

My suggestions mainly involve justifying and simplifying assumptions of the approach and discussing how the results could be generalized beyond simple tests of connection density.

Regarding the Erdos-Renyi independent edge weight assumption, I would be curious to see whether the in- and out-degree distributions of the network models (e.g. the SBM) the authors construct are consistent with the empirical data, and if not, a discussion of alternative network models that can match this feature of the data better.

Regarding the observation of KC connectivity being significantly different from the SBM, could this be due to a sample size issue? The inclusion of the number of neurons belonging to each group and/or edges belonging to each comparison would be valuable, and it would also be helpful if the authors could discuss how to deal with issues of statistical power within the SBM.

Finally, I would be interested if the authors could motivate and comment on their focus on connection density as the measure of bilateral symmetry. Certainly, many graph properties may differ between connectomes, connection density being a straightforward one to quantify. It's not clear that the authors' motivating example of comparing the connectome of an organism that has undergone a learning procedure and one that hasn't would be best served by a test of connection density versus something else (like the number of reciprocal connections, degree of convergence, etc.).
