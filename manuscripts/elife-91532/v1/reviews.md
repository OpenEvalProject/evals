# Peer review - Round 1

Editors:
- Sacha B Nelson, Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91532.3.sa0](https://doi.org/10.7554/eLife.91532.3.sa0)

This is an important computational study that applies the machine learning method of bilinear modeling to the problem of relating gene expression to connectivity. Specifically, the author attempts to use transcriptomic data from mouse retinal neurons to predict their known connectivity with promising results. On revision, the approach was tested against a second data set from C. elegans. A limited number of genes studied in this second dataset may have resulted in performance that matched but did not exceed prior models. However, taken together, the results were felt to provide solid evidence for the value of the approach.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91532.3.sa1](https://doi.org/10.7554/eLife.91532.3.sa1)

Summary:

In this study, the author aimed to develop a method for estimating neuronal-type connectivity from transcriptomic gene expression data. They sought to develop an interpretable model that could be used to characterize the underlying genetic mechanisms of circuit assembly and connectivity in various neuronal systems.

Strengths:

Many of the proposed suggestions were addressed by the author from the initial review. In general the claims made by the author are more strongly supported by the data and better situated in the literature. A major improvement includes the application of the model to the C. elegans gap junction neuronal system. Despite several key differences in the dataset as compared to the mouse retina data, the proposed model performs comparably to the SCM model currently considered state of the art in the literature (the author should remain cautious about claiming better performance given extremely marginal differences). In section 7.2, the author clearly outlines additional advantages of the proposed model including superior time and space complexity. The overall model performance remains modest, but it learns the same rules as the SCM model as well as other candidate patterns.

As in the initial submission, the bilinear model recapitulates key connectivity motifs for the mouse dataset. The algorithm is shown to converge across several runs affirming its stability/replicability. The model is also extended to predict connectivity on unknown RGC-BC cell type pairs. Without ground truth, the author posits how it should perform based on known functional properties of the RGC type. The hypotheses are confirmed for 8/10 neuronal types with unknown connectivity. The author more clearly describes how this model can be used experimentally for hypothesis testing and presents a more comprehensive future roadmap regarding validation, avenues for improving the model, and incorporation of growing datasets.

Weaknesses:

While the C Elegans dataset is useful because it enables benchmarking to existing models, the dataset is quite different. The gene expression dimensionality is 18 genes as opposed to over 3000 genes in the mouse dataset. It is a strength that the model still works as intended, but a weakness that the bilinear model could not be tested on a similar mouse dataset. This distinction matters because it remains an open question if the PCA methodology would hold up in a dataset with varied distributions of gene expression. Variations of the PCA methodology could be evaluated further with the present dataset to make the generalizability of the model more convincing.

The Gene Ontology analysis requires more methodological explanation. The author claims, "(the linear nature of the model) enables the direct interpretation of gene expressions by examining their associated weights in the model. These weights signify the importance of each gene in determining the connectivity motifs between the BC and RGC types." If I am correctly understanding the methods, the model weights in each dimension are indexing the importance of a gene expression feature as opposed to the importance of a single gene alone, "the gene expression of the BCs in X and the RGCs in Y were featurized by their respective PCs, resulting in matrices of dimensions 22453 × 11323 and 3779 × 3142, respectively." It would be helpful to explain how gene weights are extracted from a gene expression feature once highlighted.

There could be a more rigorous analysis of the predictive capacity of the model even with the current data. The model recapitulates connectivity patterns from the full dataset and a prediction is demonstrated for unknown data. The model is thus championed as a useful tool for predicting how genetic modifications will influence connectivity, but this is not empirically evaluated.

Appraisal of whether the author achieved their aims, and whether results support their conclusions:

In line with the aims of the paper, the author proposed an interpretable bilinear model to learn a shared latent feature space derived from gene expression profiles to predict synaptic connectivity between various neuron types. The model was shown to generalize to two distinct neuronal systems with varying levels of genomic and cellular resolution. While the performance remains modest, the model performs comparably to the existing state of the art despite improved computational complexity.

Discussion of likely impact of the work on the field, and utility of methods and data to the community:

The author has elaborated substantially on the impact of this work, particularly how it could be leveraged in experimental settings. The clear methodology could be implemented by other researchers to test the model on new datasets and for benchmarking novel methods.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91532.3.sa2](https://doi.org/10.7554/eLife.91532.3.sa2)

Summary:

In this study, Mu Qiao employs a bilinear modelling approach, commonly utilised in the recommendation systems, to explore the intricate neural connections between different pre- and post-synaptic neuronal types. This approach involves projecting single-cell Transcriptomic datasets of pre- and post-synaptic neuronal types into a latent space through transformation matrices. Subsequently, the cross-correlation between these projected latent spaces is employed to estimate neuronal connectivity. To facilitate the model training, Connectomic data is used to estimate the ground-truth connectivity map. This work introduces a promising model for the exploration of neuronal connectivity and its associated molecular determinants. In the revised version of the manuscript, the author has applied and validated the model in both C. elegans gap junction connectivity and the retina neuron connectivity conditions.

Strengths:

This study introduces a succinct yet promising computational model for investigating connections between neuronal types. The model, while straightforward, effectively integrates single-cell transcriptomic and connectomic data to produce a reasonably accurate connectivity map, particularly within the context of retinal connectivity. Furthermore, it successfully recapitulates connectivity patterns and helps uncover the genetic factors that underlie these connections.

Weaknesses:

(1) When compared with the previous method - SCM, the new model shows a similar performance level. This may be due to the limitation of the dataset itself, as it only has the innexin expression data. Is it possible to apply the SCM model to the more complete retina dataset and compare the performance with the proposed bilinear modelling approach?

Minor Weakness:

(1) The study lacks experimental validation of the model's prediction results.
