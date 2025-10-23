# Peer review - Round 1

Editors:
- Silke Hauf, Virginia Tech United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101579.3.sa0](https://doi.org/10.7554/eLife.101579.3.sa0)

This valuable paper reports machine learning-based image analysis pipelines for the automated segmentation of micronuclei and the detection and sorting of micronuclei-containing cells. These are powerful new tools for researchers who study micronuclei and their physiologic consequences. The analysis of the new tools and their benchmarking is rigorous and convincing; applications and remaining limitations are well explained in the paper.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101579.3.sa1](https://doi.org/10.7554/eLife.101579.3.sa1)

DiPeso et al. develop two tools to (i) classify micronucleated (MN) cells, which they call VCS MN, and (ii) segment micronuclei and nuclei with MNFinder. They then use these tools to identify transcriptional changes in MN cells.

The strengths of this study are:

- Developing highly specialized tools to speed up the analysis of specific cellular phenomena such as MN formation and rupture is likely valuable to the community and neglected by developers of more generalist methods.

- A lot of work and ideas have gone into this manuscript. It is clearly a valuable contribution.

- Combining automated analysis, single-cell labeling, and cell sorting is an exciting approach to enrich for phenotypes of interest, which the authors demonstrate here.

The authors addressed my original concerns related to the first version of this manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101579.3.sa2](https://doi.org/10.7554/eLife.101579.3.sa2)

Summary:

Micronuclei are aberrant nuclear structures frequently seen following the missegregation of chromosomes. The authors present two image analysis methods, one robust and another rapid, to identify micronuclei (MN) bearing cells. To analyse their software efficacy, the authors study images of cells treated with MPS1 inhibitor to induce chromosome missegregation. Next, the authors use RNA-seq to assess the outcomes of their MN-identifying methods: they do not observe a transcriptomic signature specific to MN but find changes that correlate with aneuploidy status. Overall, this work offers new tools to identify MN-presenting cells, and it sets the stage with clear benchmarks for further software development.

Strengths:

Currently, there are no robust MN classifiers with a clear quantification of their efficiency across cell lines (mIoU score). The software presented here tries to address this gap. GitHub material (images, ground truth labels, tools, protocols, etc.) provided is a great asset to computational biologists. The method has been tested in more than one cell line. This method can help integrate cell biology and 'omics' data, making it suitable for multimodal studies.

Weaknesses:

Although the classifier outperforms available tools for MN segmentation by providing mIoU, it's not yet at a point where it can be reliably applied to functional genomics assays where we expect a range of phenotypic penetrance in most cell lines (e.g., misshapen, multinucleated, and lagging DNA in addition to micronucleated cells). The discussion considers the nature and proportion of MN in RPE1 cells, and how the classifier is well-suited for RPE1 that predominantly display MN structures. Whether the classifier can rigorously assign MN-presenting cells amidst drastic nuclear aberrancies following a spindle checkpoint loss needs to be tested in the future.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101579.3.sa3](https://doi.org/10.7554/eLife.101579.3.sa3)

Summary:

The authors develop automated methods to visually identify micronuclei (MN) and MN-containing cells. The authors then use these methods to isolate MN-containing RPE-1 cells post-photoactivation and analyze transcriptional changes in cells with and without micronuclei. The authors find that RPE-1 cells with MN have similar transcriptomic changes as aneuploid cells and that MN rupture does not lead to vast changes in the transcriptome.

Strengths:

The authors develop a method that allows for automating measurements and analysis of micronuclei. This has been something that the field has been missing for a long time. Using such a method has the potential to greatly enhance the field's ability to analyze micronuclei and understand the downstream consequences. The authors also develop a method to identify cells with micronuclei in real-time, mark them using photoconversion, and then isolate them via cell sorting, which could change the way we isolate and study MN-containing cells, and the scale at which we do it. The authors use this method to look at the transcriptome. This method is very powerful as it can allow for the separation of a heterogenous population and subsequent analysis with a much higher sample number than previously possible.

Weaknesses:

The major weakness of this paper is the transcriptomic analysis of MN. There is in general large variance between replicates in experiments looking at cells with ruptured versus intact micronuclei. This limits our ability to assess if lack of changes are due to truly not having changes between these populations or experimental limitations. More transcriptomic analysis will be necessary to fully understand the downstream consequences of MN rupture.
