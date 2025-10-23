# Peer review - Round 1

Editors:
- Laura Colgin, The University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38471.040](https://doi.org/10.7554/eLife.38471.040)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Unsupervised discovery of temporal sequences in high-dimensional datasets, with applications to neuroscience" for peer review at eLife. Your article is being evaluated by Timothy Behrens as the Senior Editor, a Reviewing Editor, and three reviewers.

While the reviewers were generally enthusiastic about the work, major concerns were brought up that raise the question of whether this work is appropriate for the general readership of eLife. All reviewers agreed that these major concerns require essential revisions and thus would like to see an action plan that addresses these concerns before they issue a formal decision. In particular, the reviewers were not convinced that this method constitutes a major advance over current state-of-the-art methods in the field. Also, the selection of hyperparameters was not convincingly justified. The reviews are included below in their entirety.

Reviewer #1:

This paper introduces a matrix factorization-based method, seqNMF, for extracting temporal sequences from high-dimensional data. The authors convincingly demonstrate that seqNMF performs well in artificial and real datasets. I believe seqNMF will be a useful tool for a wide range of applications. After its appearance at COSYNE, the tool has already created considerable excitement in the computational and systems neuroscience community.

I found the paper to be very well written and the results clearly presented. However, some points need improvement:

1) While Type 1, 2, and 3 errors are clearly explained, I thought better naming could improve the readability of the paper a lot.

2) Building into equation 6, the authors discuss two alternative regularizers, and claim that they would fail at preventing Type 1, 2 and 3 errors simultaneously. While the arguments are clear, an experimental demonstration would be more convincing.

3) In subsection “SeqNMF: A constrained convolutional non-negative matrix factorization”, authors call ||M||1,i≠j a norm on M, which technically isn't correct (Under this definition, a diagonal matrix would have a zero norm).

4) I have trouble with understanding the first method of choosing λ. Is this method only applicable to data for which ground-truth is known? Or are the authors suggesting to choose λ between 2λ0 and 5λ0 for any dataset? Please clarify what the suggested method is.

Reviewer #2:

This paper describes a targeted dimensionality reduction approached, called seqNMF, to identify sequences in neural data. The approach is an improvement on previously published methods. The method will be of interest to its target audience. Also, the method is well described in straightforward terms, and the authors do a great job of describing how to use the method. They provide good examples, both from simulated data and multiple types of real data. They also give a good understanding of how the method can be tuned, such as using the λ value, to explore sequences with different levels of granularity or to test different ideas about the data. The paper is well written and is presented in a fair manner. I am therefore supportive of this paper and suggest publication.

Reviewer #3:

Overview: This manuscript aims to address the problem of automated discovery of temporal sequences from neural data. The authors report on a modification (seqNMF) of the convolutional non-negative matrix factorization (convNMF) algorithm targeted to address purported issues in the base method. The fundamental issue that seqNMF attempts to address is the redundancy/replication of learned bases by the vanilla convNMF algorithm. The authors use extensive numerical studies to characterize the performance of their algorithm. The target biological datasets are neural activity (spike trains and calcium signals) from hippocampus and nucleus HVC of the zebra finch. This paper is generally well written, though it could be streamlined substantially to accelerate the reader through the manuscript. However, for reasons elaborated below, it is unclear how much of an advance the reported method is over the current state of the art in the field. Most importantly, the authors seem unaware of recent advances in the statistical-machine learning literature that aim at addressing the issue of non-redundant bases learning by NMF algorithms. Furthermore, the heuristic used for selection of the penalty hyperparameter is not adequately justified. As such, the impact/novelty of the proposed algorithm has not been evaluated or demonstrated: quantitative comparisons to the state-of-the-art is required for evaluation of proposed new analytic methods. While these issues could potentially be addressed, in my opinion, this work does not present a clear major improvement over existing methods and thus belongs in a much more specialized venue.

Major Critiques:

1) Insufficient comparison to state-of-the-art methods. The central issue that the seqNMF algorithm attempts to solve is "To reduce the occurrence of redundant factors in convNMF […]". The authors identify three types of bases learning consistency errors. To address these errors, the authors augment an existing penalty on the reconstruction cost function to encourage uncorrelated bases and loadings. This is a reasonable strategy but is by no means the only approach. Indeed, as mentioned by the authors:

-Direct selection of the rank K vs. hyperparameter strength (λ)

-Use of a sparsity penalty (e.g., L1-regularization)

While these approaches are mentioned, and sometimes examined, the benefit of the proposed method over these approaches has not been demonstrated in either synthetic or neurobiological data. For example, if one were to attempt to optimize the number of bases (K) and the regularization strength (λ) in a sparse convNMF, how do the performance measures on the synthetic data sets with various noise levels stack up? Note that the results of Figure 2C,D in this regard are not at all convincing, as the rank K of the factorization of convNMF is not optimized: indeed, I find this figure to be misleading, as it is not an 'apples-to-apples' comparison (also, I believe there is a mislabeling of convNMF vs. seqNMF in this figure).

More seriously, the authors seem unaware of recent advances in the statistical-machine learning community which directly address the issue of learning non-redundant bases. For example, the 'stability NMF' algorithm (Wu et al., 2016) was recently successfully applied to extract biologically meaningful patterns from diverse data sets. More recently, the UoI-NMFcluster algorithm (Ubaru et al., 2018) has been shown to extract the precise generative bases, and assign sparse reconstruction weights to those bases, from noisy synthetic and neurobiological data. Both of these methods aim to select bases that are minimally correlated with each other. While these methods have not been applied to sequences per se, there is no conceptual reason why they could not be. For example, if one allows for a sliding cross-correlation, it is likely that both stability NMF and UoI-NMF could deal with temporal jitter. Can these methods be modified to provide even greater robustness for learning non-redundant bases for sequences?

In summary, the authors have not demonstrated the broad and robust improvement of the proposed algorithm relative to other methods in the field.

2) Method for selecting regularization parameters. In the seqNMF algorithm, the balance between reconstruction and un-correlated bases is modulated by the λ hyperparamter. The authors provide various heuristics for choosing λ to find the correct bases. The main heuristic used for the main figure use a heuristic of 2-5x of the λ value that gives the cross-over in normalized reconstruction vs. correlation costs (λ0). The authors justify this as giving good results in the synthetic data sets and having a reasonable overlap with cross-validated reconstruction error. However, for many of the synthetic and real data sets, lambda0 also lies at the most sensitive part of the range, and small modulations lead to large changes in the trade-off of reconstruction vs. correlation. That is, the results are likely to be very sensitive to this selection. Furthermore, the selected values often result in very poor data reconstruction (e.g., Figure 6C,D and Figure 7B,F). As quantified, this is a big problem for 'interpretability', as it is very hard to interpret the results of a method that does not have good data prediction quality. In science, ground-truth is not known, and a major metric we have to quantitatively evaluate methods is reconstruction error/parsimony. If the authors could show that, something like cross-validated Bayesian Information Criterion, was optimized for the selected values of λ, that would be much more convincing.

In summary, the heuristic method used to select the regularization strength, which is a major component of the reported work, is not sufficiently justified from a statistical-machine learning perspective.
