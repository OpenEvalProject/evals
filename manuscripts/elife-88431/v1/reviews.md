# Peer review - Round 1

Editors:
- Luca Pinello, Massachusetts General Hospital United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88431.3.sa0](https://doi.org/10.7554/eLife.88431.3.sa0)

This study makes a valuable contribution to spatial transcriptomics by rigorously benchmarking cell-type deconvolution methods, assessing their performance across diverse datasets with a focus on biologically relevant, previously unconsidered aspects. The authors demonstrate the strengths of RCTD, cell2location, and SpatialDWLS for their performance, while also revealing the limitations of many methods when compared to simpler baselines. By implementing a full Nextflow pipeline, Docker containers, and a rigorous assessment of the simulator, this work offers robust insights that elevate the standards for future evaluations and provides a resource for those seeking to improve or develop new deconvolution methods. The thorough comparison and analysis of methods, coupled with a strong emphasis on reproducibility, provide solid support for the findings.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88431.3.sa1](https://doi.org/10.7554/eLife.88431.3.sa1)

Cell type deconvolution is one of the early and critical steps in the analysis and integration of spatial omic and single cell gene expression datasets, and there are already many approaches proposed for the analysis. Sang-aram et al. provide an up-to-date benchmark of computational methods for cell type deconvolution.

In doing so, they provide some (perhaps subtle) additional elements that I would say are above the average for a benchmarking study: (i) a full Nextflow pipeline to reproduce their analyses; (ii) methods implemented in Docker containers (which can be used by others to run their datasets); (iii) a fairly decent assessment of their simulator compared to other spatial omics simulators. A key aspect of their results is that they are generally very concordant between real and synthetic datasets. And, it is important that they authors include an appropriate "simpler" baseline method to compare against and surprisingly, several methods performed below this baseline. Overall, this study also has the potential to also set the standard of benchmarks higher, because of these mentioned elements.

The only weakness of this study that I can readily see is that this is a very active area of research and we may see other types of data start to dominate (CosMx, Xenium) and new computational approaches will surely arrive. The Nextflow pipeline will make the the prospect of including new reference datasets and new computational methods easier.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88431.3.sa2](https://doi.org/10.7554/eLife.88431.3.sa2)

In this manuscript Sangaram et al provide a systematic methodology and pipeline for benchmarking cell type deconvolution algorithms for spatial transcriptomic data analysis in a reproducible manner. They developed a tissue pattern simulator that starts from single-cell RNA-seq data to create silver standards and used spatial aggregation strategies from real in situ-based spatial technologies to obtain gold standards. By using several established metrics combined with different deconvolution challenges they systematically scored and ranked 12 different methods and assessed both functional and usability criteria. Altogether, they present a reusable and extendable platform and reach very similar conclusions to other deconvolution benchmarking paper, including that RCTD, SpatialDWLS and Cell2location typically provide the best results. Major strengths of the simulation engine include the ability to downsample and recapitulate several cell and tissue organization patterns.

More specifically, the authors of this study sought to construct a methodology for benchmarking cell type deconvolution algorithms for spatial transcriptomic data analysis in a reproducible manner. The authors leveraged publicly available scRNA-seq, seqFISH, and STARMap datasets to create synthetic spatial datasets modeled after that of the Visium platform. It should be noted that the underlying experimental techniques of seqFISH and STARMap (in situ hybridization) do not parallel that of Visium (sequencing), which could potentially bias simulated data. Furthermore, to generate the ground truth datasets cells and their corresponding count matrix are represented by simple centroids. Although this simplifies the analysis it might not necessarily accurately reflect Visium spots where cells could lie on a boundary and affect deconvolution results.

The authors thoroughly and rigorously compare methods while addressing situational discrepancies in model performance, indicative of a strong analysis. The authors make a point to address both inter- and intra- dataset reference handling, which has a significant impact on performance, as the authors note in the text and conclusions. Indeed, supplying optimal reference data is - potentially most - important to achieve the best performance and hence it's important to understand that experimental design or sample matching is at least equally important to selecting the ideal deconvolution tool.

Similarly, the authors conclude that many methods are still outperformed by bulk deconvolution methods (e.g. Music or NNLS), however, it needs to be noted that these 'bulk' methods are also among the most sensitive when using an external (inter) dataset (S10), which likely resembles the more realistic scenario for most labs.

As the authors also discuss it's important to realize that deconvolution approaches are typically part of larger exploratory data analysis (EDA) efforts and require users to change parameters and input data multiple times. Thus, running time, computing needs, and scalability are probably key factors that researchers would like to consider when looking to deconvolve their datasets.

The authors achieve their aim to benchmark different deconvolution methods and the results from their thorough analysis support the conclusions that creating cell type deconvolution algorithms that can handle both cell abundance and rarity throughout a given tissue sample are challenging.

The reproducibility of the methods described will have significant utility for researchers looking to develop cell type deconvolution algorithms, as this platform will allow simultaneous replication of the described analysis and comparison to new methods.
