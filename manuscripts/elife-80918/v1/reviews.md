# Peer review - Round 1

Editors:
- Louis K Scheffer, https://ror.org/006w34k90 Howard Hughes Medical Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80918.sa0](https://doi.org/10.7554/eLife.80918.sa0)

This paper marks a fundamental advance in reconstruction of volume EM images, by introducing the automatic assignment of cell types and tissues. This task has previously been done manually, resulting in a serious bottleneck in reconstruction, but the authors present compelling evidence that in at least some cases, automatic and semi-automatic techniques can match or better human assignment of cell and tissue types. These results will be of interest to almost all groups doing EM reconstruction, as they can speed up cell type assignment when the cell types are known, and provide an initial cell type and tissue classification when they are not.


---

# Peer review - Round 1

Editors:
- Louis K Scheffer, https://ror.org/006w34k90 Howard Hughes Medical Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80918.sa1](https://doi.org/10.7554/eLife.80918.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "MorphoFeatures: unsupervised exploration of cell types, tissues and organs in volume electron microscopy" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Louis K Scheffer as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Claude Desplan as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jan Funke (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) What happens when there are errors in segmentation? This can easily lead to shapes which are different from any legitimate cell type, and could result in an erroneous cell type being created. On the other hand, these shapes are not likely reproduced, and so would likely result in a cluster of a single cell, which would be suspicious (at least in bilaterally symmetric creatures) as every cell type should have at least two examples.

It would be good to show the results of an existing merge error (or induce one if necessary) and report the results.

2) Along similar lines, the paper should report the used (or potential) cell-typing flow when using this method. In the paper it speaks of manually correcting the segmentation. But how do you know which cells are wrong? If you need to examine each cell manually, there will not be much time savings. So possibly you segment, then run the algorithms of this paper. Then you look for clusters of size 1, which (assuming bilateral symmetry) are likely a mistake. Then you fix those cells and iterate. It would be great to know if this approach was used, and if so how fast it converges.

3) In the section on "visually interpretable" features, you should provide a more quantitative idea of how many features are considered meaningful, and how those can be found. For example, are the six features shown in Figure 3 particularly meaningful, or were they chosen among many? A discussion of the feature selection protocol would be useful for replicating the method on new data. Furthermore, a supplementary figure with some of the features which are not meaningful would give the reader a better idea of the range of interpretability to expect.

4) The section on MorphoContextFeatures is missing a comparison with the MorphoFeatures. This made it unclear to me whether adding the neighborhood information is necessary for the discovery of tissues and organs. This could be remedied with a supplementary figure showing the same analysis as in figures 7 and 8 on the MorphoFeatures without the additional neighborhood information. Alternatively, since the MorphoFeatures are a subset of the MorphoContextFeatures, the authors could run a post-hoc analysis of whether the MorphoFeatures or the neighborhood features best explain the inter-class variance.

5) Finally, some extra guidance is needed to replicate this work on new data. In particular the following points could use more discussion:

5.1. How to choose the size of the MorphoFeatures vector – did the authors attempt a number other than 80 and if so, what was affected by this choice?

5.2. The protocol for when and how to define sub-clusters – were the chosen thresholds based on prior knowledge such as known tissues/organs? What do the authors suggest if this kind of information is missing?

5.3 How to link the obtained clusters back to specific, potentially meaningful, MorphoFeatures. For example, does the distinctive shape of the enteric neurons in cluster 8.3 of figure 5 correspond to an extreme of the cytoplasm shape feature described in figure 3 (lower left)?

6) In figure 1 b/c: The difference between B and lower part of C is unclear. If seen as a description of the two losses, the fact that the contrastive loss is shown twice is confusing. If seen as a description of the whole training setup, the omission of the fine-grained features is the issue.

7) In figure 2: It would be interesting to find out which subset of features correlates with which class, and whether those are meaningful. At minimum, knowing whether a shape, coarse texture, and fine texture are all involved in predictions.

8) In figure 2: The legend on the scale bars says 'mkm', which is not an abbreviation of micrometers that I am used to. Perhaps μm instead? The legend is also difficult to see (see pt. 11).

9) In figure 5: the scale bar legend is too small to see. Also, putting it above the scale bar might improve readability.

10) In Figure 7 + text: the text suggests that the clusters have been chosen manually, rather than using community detection as in the other figures. This should be justified if true.

11) In figure 8B + text (p.14): There isn't much said about the cells that are misclassified in the MorphoContextFeatures, i.e. where both manual segmentation and gene clusters agree, but MorphoContextFeatures does not. For example: green cell among the brown, or yellow cells just right of the central line of the organism, top. A justification similar to the explanations of misclassification in Figure 2 would help strengthen the argument.

For future work: Currently many EM reconstructions are nervous systems of somewhat higher animals (Drosophila and small portions of mammal brains). The shapes of these cells are very complex, and it would be interesting to see if the morphology features will continue to work on such complex cells. Drosophila could be a good example.

There is a question (line 409) of how well patch characteristics will correspond when comparing different samples. This could be tested, at least in part, by applying different image normalizations to the same sample, then treating them as two separate samples.

Reviewer #1 (Recommendations for the authors):

I have two main technical concerns. The first is what happens when there are errors in segmentation. This can easily lead to shapes which are different from any legitimate cell type, and could result in an erroneous cell type being created. On the other hand, these shapes are not likely reproduced, and so would likely result in a cluster of a single cell, which would be suspicious (at least in bilaterally symmetric creatures) as every cell type should have at least two examples. It would be good to induce a (for example) merge error between two cells and see what happens.

I would be very interested in the cell-typing flow using this method. In the paper it speaks of manually correcting the segmentation. But how do you know which cells are wrong? If you need to examine each cell manually, there will not be much time savings. So I could imagine a flow where you segment, then run the algorithms of this paper. Then you look for clusters of size 1, which (assuming bilateral symmetry) are likely a mistake. Then you fix those cells and iterate. It would be great to know if this approach was used, and if so how fast it converges.

For future work: Currently many EM reconstructions are nervous systems of somewhat higher animals (Drosophila and small portions of mammal brains). The shapes of these cells are very complex, and it would be interesting to see if the morphology features will continue to work on such complex cells. Drosophila could be a good example.

There is a question (line 409) of how well patch characteristics will correspond when comparing different samples. This could be tested, at least in part, by applying different image normalizations to the same sample, then treating them as two separate samples.

Reviewer #2 (Recommendations for the authors):

1. In figure 1 b/c: The difference between B and lower part of C is unclear. If seen as a description of the two losses, the fact that the contrastive loss is shown twice is confusing. If seen as a description of the whole training setup, the omission of the fine-grained features is the issue.

2. In figure 2: It would be interesting to find out which subset of features correlates with which class, and whether those are meaningful. At minimum, knowing whether a shape, coarse texture, and fine texture are all involved in predictions.

3. In figure 2: The legend on the scale bars says 'mkm', which is not an abbreviation of micrometers that I am used to. Perhaps μm instead? The legend is also difficult to see (see pt. 4).

4. In figure 5: the scale bar legend is too small to see. Also, putting it above the scale bar might improve readability.

5. In Figure 7 + text: the text suggests that the clusters have been chosen manually, rather than using community detection as in the other figures. This should be justified if true.

6. In figure 8B + text (p.14): There isn't much said about the cells that are misclassified in the MorphoContextFeatures, i.e. where both manual segmentation and gene clusters agree, but MorphoContextFeatures does not. For example: green cell among the brown, or yellow cells just right of the central line of the organism, top. A justification similar to the explanations of misclassification in Figure 2 would help strengthen the argument.
