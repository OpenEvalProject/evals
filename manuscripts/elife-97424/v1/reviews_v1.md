# Peer review - Round 1

Editors:
- Mohammad M Karimi, King's College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97424.3.sa0](https://doi.org/10.7554/eLife.97424.3.sa0)

MGPfactXMBD is a novel computational method for investigating cell evolutionary trajectory for scRNA-seq samples. It is important, with several potential future applications. The authors benchmarked this method using synthetic and real-world samples and showed superior performance for some of the tasks in cell trajectory analysis compared to other methods with compelling evidence.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97424.3.sa1](https://doi.org/10.7554/eLife.97424.3.sa1)

Summary:

Ren et al developed a novel computational method to investigate cell evolutionary trajectory for scRNA-seq samples. This method, MGPfact, estimates pseudotime and potential branches in the evolutionary path through explicitly modeling the bifurcations in a Gaussian process. They benchmarked this method using synthetic as well as real world samples and showed superior performance for some of the tasks in cell trajectory analysis. They further demonstrated the utilities of MGPfact using single cell RNA-seq samples derived from microglia or T cells and showed that it can accurately identify the differentiation timepoint and uncover biologically relevant gene signatures.

Strengths:

Overall I think this is a useful new tool that could deliver novel insights for the large body of scRNA-seq data generated in the public domain. The manuscript is written is a logical way and most parts of the method are well described.

Comments on revisions:

In this revision, the authors have sufficiently addressed all of my concerns. I don't have any follow-up comments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97424.3.sa2](https://doi.org/10.7554/eLife.97424.3.sa2)

Summary of the manuscript:

Authors present MGPfactXMBD, a novel model-based manifold-learning framework designed to address the challenges of interpreting complex cellular state spaces from single-cell RNA sequences. To overcome current limitations, MGPfactXMBD factorizes complex development trajectories into independent bifurcation processes of gene sets, enabling trajectory inference based on relevant features. As a result, it is expected that the method provides a deeper understanding of the biological processes underlying cellular trajectories and their potential determinants.

MGPfactXMBD was tested across 239 datasets, and the method demonstrated similar to slightly superior performance in key quality-control metrics to state-of-the-art methods. When applied to case studies, MGPfactXMBD successfully identified critical pathways and cell types in microglia development, validating experimentally identified regulons and markers. Additionally, it uncovered evolutionary trajectories of tumor-associated CD8+ T cells, revealing new subtypes with gene expression signatures that predict responses to immune checkpoint inhibitors in independent cohorts.

Overall, MGPfactXMBD represents a relevant tool in manifold-learning for scRNA-seq data, enabling feature selection for specific biological processes and enhancing our understanding of the biological determinants of cell fate.

Summary of the outcome:

The novel method addresses core state-of-the-art questions in biology related to trajectory identification. The design and the case studies are of relevance.

Comments on revisions:

The authors have addressed all my previous comments to satisfaction.
