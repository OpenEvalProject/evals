# Peer review - Round 1

Editors:
- Babak Momeni, https://ror.org/02n2fzt79 Boston College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81464.sa0](https://doi.org/10.7554/eLife.81464.sa0)

This manuscript presents an important tool for causal inference intended for the analysis of single cell datasets but possibly with broader applications. It compares several algorithms and incorporates a number of them in the platform and offers convincing evidence of its usefulness. With the rapid expansion of large datasets, this tool is beneficial in offering several causal inference analysis options and expediting the interpretation of data.


---

# Peer review - Round 1

Editors:
- Babak Momeni, https://ror.org/02n2fzt79 Boston College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81464.sa1](https://doi.org/10.7554/eLife.81464.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "CausalCell: applying causal discovery to single-cell analyses" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Anna Akhmanova as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

This manuscript presents a tool for causal inference intended to be used for the analysis of single-cell datasets. The tool, named CausalCell, attempts to address a quite important question in the network biology field. That is how to infer a directed gene network to reveal causal relationships among genes. Given scRNA-seq data and a set of genes of interest, CausalCell is potentially useful for inferring cell type-specific intracellular causal networks among genes. Although in principle this can be a very helpful tool, the evidence that the incorporated algorithms are the most suitable for the proposed applications is inadequate. Data preprocessing, result illustration, and validation should be substantially strengthened.

1) The authors need to either justify their choice of algorithms in the paper or expand the work to include other important algorithms.

2) Throughout the paper, the authors need to be more explicit about the description of preprocessing as well as the quantification of stated claims.

3) Stronger validation is needed to support and clarify the usefulness of the proposed tool.

Reviewer #1 (Recommendations for the authors):

1. There seem to be three general categories of causal inference algorithms: constraint-based, score-based, and hybrid (see for example, https://proceedings.neurips.cc/paper/2017/file/275d7fb2fd45098ad5c3ece2ed4a2824-Paper.pdf).

This paper appears to focus only on different implementations of constraint-based algorithms; however, it appears that score-based algorithms in general produce better results for complex biologically-driven datasets. I have checked this with experts since this is a little outside of my field. In my opinion, this is a major shortcoming that significantly reduces the impact of the current manuscript. In other words, the authors need to justify that the algorithm (or group of algorithms) they have picked is the best option for single-cell analyses (in doing so, the existing efforts and literature should be addressed). Alternatively (and especially if there is no consensus about what algorithm works best), they should incorporate other options into the tool.

2. Some statements in the comparison section need clarification. For example, in Table 1, the authors mention that "Both ExtraTrees and RandomForest perform well, but XGBoost does not." I believe it is necessary to state more details about what the context/condition is, in order to justify such claims.

3. Figure 2: The comparison shows a relatively poor similarity between different algorithms. What is the reason for this?

4. In Discussions, the authors state that kernel-based CI tests perform better than faster methods that make additional assumptions. I am not sure if I see the evidence for this. Especially when different kernel-based algorithms poorly agree with each other, it is unclear how a case can be made. Ideally, this issue can be addressed with a "mock" dataset in which the causal links are already known. In the absence of a known "ground truth" or a "gold standard", their arguments about accuracy and performance are in general less convincing.

5. Line 353: The authors make a statement about the dataset being "large enough". I'd suggest including a formal treatment, in which the causal inference results are compared as the number of data points increases (for example by sub-sampling one of the existing datasets). I believe this will provide more convincing evidence for how many data points are required and what to expect as that number increases/decreases.

Reviewer #2 (Recommendations for the authors):

1) Reactome and KEGG databases curated directed links between genes or proteins, which is suitable for result evaluation.

2) 50 feature genes represent a small fraction of the whole genome. This means CausalCell cannot fully take advantage of the high-throughput feature of current scRNA-seq technologies. Any suggestions to deal with this concern?

3) What techniques do the authors use to generate the consensus network?

4) On lines 68-70, what are the differences among regulatory networks, causal networks, (ordinary) networks, and gene networks? Readers could be confused by such an introduction.

5) Figure 4 and other causal network plots should have a legend to indicate the color scheme for the upregulation or downregulation of gene expression.

6) Volume and page information of Reference [49] are missing.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Applying causal discovery to single-cell analyses using CausalCell" for further consideration by eLife. Your revised article has been evaluated by Anna Akhmanova (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The need to include more recent advances in causal discovery, such as continuous optimization-based, neural network-based methods is brought up by the reviewers again. There is a need to either include these approaches or offer concrete evidence that the PC algorithm works better (or at least equally well) for the type of biological questions the tool is addressing. This is perhaps best done by a direct comparison of results between the methods included in CausalCell and some other representatives such as Notears, Golem, DAG-GNN, lingam, and Dlingam.

2. A more thorough comparison of independence/CI tests with more recent methods such as regression-based, ranking-based, and deep neural network-based CI tests (e.g., MLP-based and GAN-based) needs to be included.

Additionally, please address the more detailed issues raised by Reviewer #3 below.

Reviewer #3 (Recommendations for the authors):

This work developed a workflow and platform for effectively performing causal discovery from scRNA‐seq data. The workflow/platform is developed upon the benchmark of 9 feature selection algorithms, 3 causal discovery methods, 9 CI tests, and the analyses of multiple datasets. The authors suggest that kernel-based conditional independence tests generate reliable results. Some key issues are discussed, and tips for best practices are provided. In my opinion, this work has the potential to help biologists discover some causal relationships among single-cell data, but the main drawback of this approach is the lack of new technologies on causal discovery as well as CI tests, and the biological significance of the work is not quite clear. Following are some of my concerns or questions about this work:

1. In recent years, continuous optimization-based methods have become the most popular method for causal discovery, which yield much better performance than the PC algorithm, I think this work should discuss and take some representative continuous optimization-based methods into account, such as Notears, Golem, DAG-GNN. There are also some causal functional model-based methods such as lingam and Dlingam should be discussed.

2. The 9 independence/CI tests might not stand for the state-of-the-art, more kinds of, and more recent methods should be taken into account, such as regression-based, ranking-based, and deep neural network-based CI tests (e.g., MLP-based & GAN-based).

3. Theoretically, not all causal directions can be discovered by the orientation step of the PC algorithm, how to address the Markov equivalence classes in this paper? And there are also some other constraint-based methods, why choose PC?

4. I suggest the author present the time complexity of each method not just 'time consumption', as it seems a little bit confusing. For example, HSIC.gmma should work much faster than HSIC.perm, but they are both '*' at 'time consumption'.

5. How to perform PC with HSIC? only 0-order CI test?

6. See "……However, because most algorithms have been designed for handling limited variables and few algorithms have been evaluated using real data, applying causal discovery to single-cell data remains challenging……". I don't quite agree with this statement, because there are lots of constraint-based methods (or combining with feature selections as dimension reduction step) with different CI tests for causal discovery on RNA-sq/Microarray, and this work also does a similar or same job.

7. See "……These features of CI tests enable causation between any genes and molecules to be inferred……". It should be noted that not all causation between them can be inferred by CI tests.

8. " ……the time consumption of kernel-based CI tests disallows large-scale network inference……", how about the parallel PC? And sometimes one can limit the size of the conditional set.

9. Actually, I wonder whether this workflow/platform can find some interesting biological results (say biomarkers) from the data. This is related to the biological significance of the work. Computational results in the paper do not provide convincing support for this point.
