# Peer review - Round 1

Editors:
- Nir Yosef, University of California , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20487.025](https://doi.org/10.7554/eLife.20487.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Dynamics of differentiation inferred from single-cell RNA-seq show a series of transitions through discrete cell states" for consideration by eLife. Your article has been favorably evaluated by Arup Chakraborty (Senior Editor) and three reviewers, one of whom, Nir Yosef (Reviewer #1) served as Guest editor. Jacob H. Hanna (Reviewer #3) agreed to share his identity.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In their manuscript, Jang et al. propose, test, and validate a statistical framework for analyzing single-cell transcriptomics data from mouse embryonic stem (mES) cell differentiation. The first part of the analysis relies on a companion manuscript, which presented a combined method for clustering and lineage inference of single cells. By applying this method on data from multiple mouse ES subject to short inductive differentiation protocols, the authors identify several cell states, the genes that mark these states, and the genes that capture state transitions. Within these clusters of cells, the authors assert there is little variation, thus defining discrete cell states along mES cell differentiation. They then cluster the genes into modules and use the Hopfield model to identify patterns of dependencies between modules that give rise to the observed clusters as steady states. With this analysis they provide and validate three hypotheses about possible "rewiring" at different stages (i.e. when the effect of perturbing gene X on gene Y varies between cell states).

Essential revisions:

Overall, the reviewers find the methodology developed in this paper interesting, and of potential impact. However, there are several key points that need to be addressed in order to fully support the validity of this methodology and to understand its intricacies.

1) Single cell data quality:

1.1) Based on the data in Figure 1—figure supplement 1E, there seems to be a fairly large variation in the percentage of reads aligning to the transcriptome on a cluster to cluster basis. Do any of the lineages correlate with the percentage of transcriptome or genome reads? What is the significance of the differences between the clusters, like C0 and C3 for example?

1.2) More generally, we are missing a description of how was the RNA-seq data normalized. In many cases when scRNA-seq data is not normalized, we see technical factors that confound the data, and library quality can dominate clustering and dimensionality reduction. Please provide evidence that this is not the case or correct accordingly.

2) Clustering and lineage detection algorithm:

2.1) For their clustering analysis, the authors limit their focus to transcription factors. While they provide off-hand reasoning for this, it is insufficient. Transcription factors (TFs), just like any other transcript, undergo stochastic, burst-like kinetics, and are subject to high amount of variation (esp. given their typically moderate expression). Additionally, it is not a given that measuring TF mRNA, rather than a TF's downstream targets, accurately depicts the circuitry involved in cellular response or differentiation. The authors should demonstrate the effects of including genes other than transcription factors on the clustering results. Relatedly, they later include signaling molecules without a rationale for the shift.

2.2) The nature of the clustering method in which only three clusters of cells are considered at a time inherently limits the hierarchy produced by the author's Bayesian framework (see Figure 2—figure supplement 1B, right). In this way, the final lineage tree is limited only to branching into two arms at any given differentiation step. Thus, any differentiation program that produces more than two offspring would not be properly modeled. The authors should address this limitation in their framework.

3) Application to ESC:

3.1) The parameters used for the Bayesian framework from the co-submission are missing. What is the cutoff for a triplet to count as a "transition" event? what is a cutoff for a gene to be defined as a "marker" or "transition" gene? What is the termination/ convergence condition?

3.2) Since the algorithm is iterative, it might be very sensitive to slight variations in initial conditions or the parameters. In standard EM applications, a common practice is to start from many starting conditions. The authors should provide an estimate of how sensitive are the results for the algorithm's parameters (e.g., probability cutoffs) and how sensitive they are for sub-sampling of cells or genes (i.e., going beyond changing the seed set of clusters, which the authors have already done).

3.3) The results in Figure 2B-E, and especially the comparison of 2B vs. 2D are somewhat tautological. It is not clear to me what these figure panels are supposed to show that we don't already know form the definition of the process applied for choosing those genes.

3.4) What is the relationship between the experimental conditions (time/ stimulation; Figure 1—source data 1) and the inferred clusters? This point is potentially crucial for interpreting the meaning of the clusters and should be discussed.

3.5) We are missing a direct and less engineered view that will help evaluate and digest the clustering results. Specifically – please provide a global heat map figure with all gene used for the final clustering (possibly stratified according to their role as transitions or markers in different parts of the tree) vs. all cells (organized by clusters). This will also help support the statement in the first paragraph of the subsection “Differentiation occurs through a series of discrete cell state transitions”.

3.6) The authors claim that gene expression within each cell cluster does not significantly vary. They validate this by comparing the magnitude of the variance explained by the first PC to the that of the first PC from 1000 sets of randomized data (FYI – unclear how 3B shows lack of significance). Why don't the authors compare the percent variance described by the first PC of each cluster to the percent variance described by first PC of randomized data?

3.7) Can the authors identify early primordial germ cell sub-population (e.g. BLIMP1+, T+, TFAP2C+ cells)? Is it discrete or is it perhaps "hiding" in one of their progenitor populations (e.g. mesendodermal cells)?

4) Validation of results:

4.1) The selection of genes in Figure 3D (immunostaining) seem somewhat biased to well-studied markers (shown in Figure 3—figure supplement 1A). Therefore, these results provide a somewhat weak support for the cell states inferred form the single cell data.

4.2) In the subsection “A probabilistic model that replicates the observed discrete cell states predicts state-dependent interpretation of perturbations” the authors mention that they "categorized the 184 marker and transition genes and signaling gene groups into 23 gene modules". However, in Figure 2—figure supplement 2 it seems that the number of transition/ marker genes should be around 800. Also, it is not clear how were the signaling genes selected (since the analysis up to this point focused on transcription factors). Please clarify these points.

5) Network analysis:

5.1) The use of Hopfield model is a nice idea, however the presentation in Figure 4A is somewhat illegible, and it is hard to evaluate the stability of the model (or parts thereof) across the 10k solutions. Please provide a more convenient way to estimate the inferred magnitude and noise for the models parameters. For instance, a scatter plot of parameters showing mean vs. fano factor across the 10,000 solutions; and for a few selected of parameters, the complete empirical distribution.

5.2) How were the gene modules discretized? The explanation in the subsection “1. Determination of gene modules” is insufficient. Specifically – which cutoffs were used? How was gene drop-out taken into account?

5.3) The derivation of the hypotheses (subsection “A probabilistic model that replicates the observed discrete cell states predicts state-dependent interpretation of perturbations”, seventh paragraph) is not defined rigorously. Please describe clearly – what is "effective interaction strength"? How do we decide when "[X] levels are more stable to [Y] overexpression"? Specifically – which statistical cutoffs were used? What is the false discovery rate? How many other, additional hypotheses with a similar FDR can be derived using the same procedure?
