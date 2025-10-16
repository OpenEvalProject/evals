# Peer review - Round 1

Editors:
- Dane Taylor, University of Buffalo United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41690.029](https://doi.org/10.7554/eLife.41690.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Discovering and Deciphering Relationships Across Disparate Data Modalities" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor, Dane Taylor, and a Senior Editor, Joshua Gold. The following individual involved in the review of your submission has agreed to reveal their identity: James D Wilson (Reviewer #2).

The Reviewers and Reviewing Editor have discussed the reviews with one another and generally found the paper to be well written, clearly organized, and an important advancement to the data-analytics community. While we do not accept the article for publication in its current form, we invite you to resubmit the manuscript after taking the following issues into consideration.

Summary:

In this work, the authors Vogelstein et al. introduce a new technique called Multiscale Graph Correlation (MGC) to discover (i.e., statistically infer using locally biased, distance-based hypothesis testing) and decipher (e.g., study the geometry of) pairwise relationships between different modalities of a dataset. Their approach is straightforward, principled, and computationally reasonable. It improves upon widely used relationship-inference techniques including test statistics for detecting linear relationships (e.g., Pearson's correlation coefficient) and nonlinear relationships (e.g., distance-correlation-based analyses including kNN-based methods, kernel-based methods and Mantel's test). Specifically, it provides an improved null-hypothesis relationship-test statistic that requires fewer samples and can be implemented at a marginal increase in computational cost [the algorithm scales as O(n2log n) for n data points. The authors study the MGC approach using a synthetic dataset comprised on 20 models, finding MGC to typically outperform competing approaches. In addition to identifying pairwise relationships between datasets, the MGC approach is a multiscale analysis and identifies the spatial scale at which the relationship's inference is most powerful. In doing so, the approach yields an MGC-map that provides rich insight into the nature of the relationship (particularly its geometry). To conclude, the authors apply the MGC test statistic to explore relationships for three biological datasets: brain activity and personality, brain connectivity and creativity, and proteomic biomarkers and cancers.

Essential revisions:

1) The experimental section is lacking sufficient discussion and citation to the literature on related scientific studies. For example, there are several statements in paragraph 2 of subsection “MGC Identifies Potential Cancer Proteomics Biomarkers” that need citation. (Discussion and citations for the brain study also appear to be missing.)

2) The authors should provide more detail about how this method scales up to larger datasets. It should be noted that the provided examples are restricted to small datasets, n\le1000. What are the practical limitations on how you might adapt your algorithm to larger data? It would be helpful to provide further results on computational time, similar to Table 4 in the Appendix. In particular, can the authors provide numerical support for their O(n2log n) scaling result.

3) The proteomics study and discussion is lacking exploration. For example: Were any biomarkers besides neurogranin identified as significant and biologically relevant? What are some of the top hits in Panc vs All and Panc VS norm individually? Also, what are some of the top hits for both of these comparisons? Do these top hits also make sense biologically? Also, you mention that "the rest of the global methods did not identify any markers." Even if no markers were identified to be statistically significant with other methods, could you still consider their relative ranking? In particular, does neurogranin appear in other methods as one of the more important biomarkers? What are the other additional top hits identified by other methods? Where do those hits appear on the scatter plot in Figure 4C?

4) Step 3 of the MGC algorithm (see subsection “The Multiscale Graph Correlation Procedure”) could use further discussion/motivation. First, the local generalized correlation is normalized in the Appendix but not in the subsection “The Multiscale Graph Correlation Procedure”, which is confusing. Second, the local generalized distance correlations are computed using the intersection of the two graphs (the k-nn and the l-nn graphs). That is, the product of terms A(i,j) Gk(i,j) B(i,j) Hl(i,j) is nonzero if (i,j) are in the "closest" neighborhood for both the graph associated with adjacency matrix Gk as well as that associated with Hl. Could this be too stringent? That is, couldn't there be a significant correlation between two data sets where only one of the data modality coordinates is in the nearest neighbors? In particular, an entry

A(i,j) Gk(i,j) B(i,j) Hl(i,j)

is treated as the same in the following 3 situations:

a) Gk(i,j) = Hl(i,j) = 0

b) Gk(i,j) = 0, Hl(i,j) = 1

c) Gk(i,j) = 1, Hl(i,j) = 0

Shouldn't case (a) be treated differently than cases (b) and (c)? It may be useful for the authors to discuss this and explain their choice.

5) For the original choice of k-nearest neighbors, in practice, how does one choose the distance metric (of course Euclidean is often selected by default)? I know it is context dependent, but is there any general data driven advice for this? The reason why I state this is that one could, if they wanted, basically p-value hunt by choosing the right metric to give a small p-value.
