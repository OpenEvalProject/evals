# Sparse dimensionality reduction approaches in Mendelian randomization with highly correlated exposures

## Authors

- Vasileios Karageorgiou<sup>1</sup> ([ORCID: 0000-0002-7173-9967](https://orcid.org/0000-0002-7173-9967)) †
- Dipender Gill<sup>2</sup>
- Jack Bowden<sup>1</sup>
- Verena Zuber<sup>2</sup>

### Affiliations

1. University of Exeter Exeter United Kingdom
2. Department of Epidemiology and Biostatistics Imperial College London London United Kingdom

† Corresponding author

## Abstract

Multivariable Mendelian randomization (MVMR) is an instrumental variable technique that generalizes the MR framework for multiple exposures. Framed as a linear regression problem, it is subject to the pitfall of multi-collinearity. The bias and efficiency of MVMR estimates thus depends heavily on the correlation of exposures. Dimensionality reduction techniques such as principal component analysis (PCA) provide transformations of all the included variables that are effectively uncorrelated. We propose the use of sparse PCA (sPCA) algorithms that create principal components of subsets of the exposures with the aim of providing more interpretable and reliable MR estimates. The approach consists of three steps. We first apply a sparse dimension reduction method and transform the variant-exposure summary statistics to principal components. We then choose a subset of the principal components based on data-driven cutoffs, and estimate their strength as instruments with an adjusted F-statistic. Finally, we perform MR with these transformed exposures. This pipeline is demonstrated in a simulation study of highly correlated exposures and an applied example using summary data from a genome-wide association study of 97 highly correlated lipid metabolites. As a positive control, we tested the causal associations of the transformed exposures on CHD. Compared to the conventional inverse-variance weighted MVMR method and a weak-instrument robust MVMR method (MR GRAPPLE), sparse component analysis achieved a superior balance of sparsity and biologically insightful grouping of the lipid traits.
