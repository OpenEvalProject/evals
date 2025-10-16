# Peer review - Round 1

Editors:
- David Knowles, Department of Computer Science and Department of Systems Biology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.100949.3.sa0](https://doi.org/10.7554/eLife.100949.3.sa0)

This work provides an important framework for understanding the primary causes of disease. While the theoretical results rely on strong assumptions about the underlying causal mechanisms, the authors provide solid empirical evidence that the framework is robust to modest violations of these assumptions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100949.3.sa1](https://doi.org/10.7554/eLife.100949.3.sa1)

Summary:

This manuscript seeks to estimate the causal effect of genes on disease. To do so, they introduce a novel algorithm, termed the Root Causal Strength using Perturbations (RCSP) algorithm. RCSP uses perturb-seq to first estimate the gene regulatory network structure among genes, and then uses bulk RNA-seq with phenotype data on the samples to estimate causal effects of genes on the phenotype conditional on the learned network structure. The authors assess the performance of RCSP in comparison to other methods via simulation. Next, they apply RCSP to two real human datasets: 513 individuals age-related macular degeneration and 137 individuals with multiple sclerosis.

Strengths:

The authors tackle an important and ambitious problem - the identification of causal contributors to disease in the context of a causal inference framework. As the authors point out, observational RNA-seq data is insufficient for this kind of causal discovery, since it is very challenging to recover the true underlying graph from observational data; interventional data are needed. However, little perturb-seq data has been generated with annotated phenotype data, and much bulk RNA-seq data has already been generated, so it is useful to propose an algorithm to integrate the two as the authors have done.

The authors also offer substantial theoretical exposition for their work, bringing to bear both the literature on causal discovery as well as literature on the genetic architecture of complex traits. They also benchmark RCSP under multiple challenging simulation settings, including an analysis of RCSP when the underlying graph is not a DAG.

Weaknesses:

The notion of a "root" causal gene - which the authors define based on a graph theoretic notion of topologically sorting graphs - requires a graph that is directed and acyclic. It is the latter that constitutes an important weakness here - it simply is a large simplification of human biology to draw out a DAG including hundreds of genes and a phenotype Y and to claim that the true graph contains no cycles. For example - consider the authors' analysis of T cell infiltration in multiple sclerosis (MS). CD4+ effector T cells have the interesting property that they are stimulated by IL2 as a growth factor; yet IL2 also stimulates the activation of (suppressive) regulatory T cells. What does it mean to analyze CD4+ regulation in disease with a graph that does not consider IL2 (or other cytokine) mediated feedback loops/cycles? To the authors' credit, in the supplementary materials they do consider a simulated example with a cyclic underling causal graph, finding that RCSP performed well comparison to an implementation of the additive noise model (ANM), LiNGAM, CausalCell, and two simpler approaches based on linear regression.

I also encourage the authors to consider more carefully when graph structure learned from perturb-seq can be ported over to bulk RNA-seq. Consider again the MS CD4+ example - the authors first start with a large perturb-seq experiment (Replogle et al., 2022) performed in K562 cells. To what extent are K562 cells, which are derived from a leukemia cell line, suitable for learning the regulatory structure of CD4+ cells from individuals with an MS diagnosis? Presumably this structure is not exactly correct - to what extent is the RCSP algorithm sensitive to false edges in this graph? The authors perform an analysis of this scenario in Supplementary Figure 4, which shows that RCSP is robust to some degree of departure from the underlying true structure. And although challenging - it would be ideal for the RCSP to model or reflect the challenges in correctly identifying the regulatory structure.

It should also be noted that in most perturb-seq experiments, the entire genome is not perturbed, and frequently important TFs (that presumably are very far "upstream" and thus candidate "root" causal genes) are not expressed highly enough to be detected with scRNA-seq. In that context - perhaps slightly modifying the language regarding RCSP's capabilities might be helpful for the manuscript - perhaps it would be better to describe it has an algorithm for causal discovery among a set of genes that were perturbed and measured, rather than a truly complete search for causal factors. Perhaps more broadly - it would also benefit the manuscript to devote slightly more text to describing the kinds of scenarios where RCSP (and similar ideas) would be most appropriately applied - perhaps a well-powered, phenotype annotated perturb-seq dataset performed in a disease relevant primary cell.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100949.3.sa2](https://doi.org/10.7554/eLife.100949.3.sa2)

Summary:

This paper presents a very interesting use of a causal graph framework to identify the "root genes" of a disease phenotype. Root genes are the genes that cause a cascade of events that ultimately leads to the disease phenotype, assuming the disease progression is linear.

Strengths:

- The methodology has a solid theoretical background.

- This is a novel use of the causal graph framework to infer root causes in a graph

Comments on revisions:

The authors addressed all of my comments.
