# Peer review - Round 1

Editors:
- Bruno Lemaître, https://ror.org/02s376052 École Polytechnique Fédérale de Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76132.sa0](https://doi.org/10.7554/eLife.76132.sa0)

Hixson et al. provide a large overview of gene expression level of the mosquito Aedes aegypti through the use of RNA-seq. They analyse gene expression changes in the digestive tract, as well as the 3 body regions and the ovaries in various conditions. These organ-specific transcriptomes fill a hole in our understanding of mosquito vector biology and will be an excellent starting point for many researchers to produce new projects.


---

# Peer review - Round 1

Editors:
- Bruno Lemaître, https://ror.org/02s376052 École Polytechnique Fédérale de Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76132.sa1](https://doi.org/10.7554/eLife.76132.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "A transcriptomic atlas of Aedes aegypti reveals detailed functional organization of major body parts and gut regional specializations in sugar-fed and blood-fed adult females" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Utpal Banerjee as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Emilie Pondeville (Reviewer #2).

All reviewers were quite positive on the findings reported by the manuscript and agree that the paper contains important data that will be of use to the vector biology community. There are however some issues to address (see below) An important one is the lack of clarity/detail in the Materials and methods in regards to how the libraries were constructed and details of how the comparisons across tissues were made. However, collectively they think that the paper is a valuable contribution and if the authors can clarify/revise in regards to those issues it would be a nice paper. We therefore ask you to prepare a revised submission to address the points listed below

Essential revisions:

1. As a dry/wet bioinformatician/molecular biologist, this reviewer acknowledges that this work has been beautifully executed following standard practices for mosquito rearing and following the guidelines of RNA sequencing. Though, data reproducibility is a concern in bioinformatics since different analysis pipelines may lead to dissimilar results from same datasets. While aiming to reach a broad audience of specialists and non-specialists in RNAseq analyses, this reviewer suggests that authors deposit their command lines and scripts (even if only relevant parts) in an open-access repository such as GitHub or equivalent, so others may compare their own data without technical variation. Also, raw tables with normalized gene expression (i.e., outputs of DEseq2) could also be provided for future reference, either deposited in GEO/NCBI or as tables together with the code at GitHub.

2. One major concern relates to the normalization of transcriptomic data presented here. Authors emphasize that data from some tissues such as ovaries or specific midgut regions showed considerably distinct patterns of gene expression. Consequently, such patterns of unbalanced transcriptional levels can skew normalization and could be of concern. The tool used here for normalization of transcript counts, DEseq2, should not be severely impacted by these events since, as mentioned by its author Michael Love, "the median ratio normalization in DESeq2 doesn't have as strong of an assumption that most genes don't change" (see post at https://support.bioconductor.org/p/61604/ for details). This reviewer suggest that the authors provide some data confirming that the normalization is stable enough between samples, hopefully showing that the core of genes that do not change expression reflect the size factors estimated by DEseq2 (a good example of this quality control is given in the blog post above). If some striking differences are seen, I would suggest applying HMM-normalization or other technique to better normalize the data and increase accuracy. Example of normalization methods for such situation are given in this Review by Liu et al. Front. Bioeng. Biotechnol. 2019 – DOI 10.3389/fbioe.2019.00358.

3. A known problem in high-throughput analysis is the establishment of arbitrary thresholds or cutoffs when analyzing differential expression. Here the authors often established arbitrary thresholds/cutoffs without depicting the reason for doing so (e.g., top 20 genes, 5-fold difference or 2-fold difference, etc). This reviewer thinks that it would be of great improvement for this manuscript if authors explain in detail the relevance of their choices and how it impacted their analyses.

4) Although some studies already analysed gene expression in the different organs of Aedes mosquitoes and changes occurring after a blood meal, this study is the first to analyse gene expression in most of female tissues allowing an accurate comparison of profiles between tissues. The analysis of data is very thorough and well described, showing investment (number of transcripts) and output (number of transcripts balanced by total number of transcripts in a specific tissue) of each organ. The putative biological functions of the different organs are not new and surprising, however, the gene expression profiles and conferred biological functions of the different gut regions is original and was not previously assessed. Although this study brings a lot of information and is very valuable for the mosquito research community, it remains a very descriptive study without functional characterization/validation.

Some limits should be taken in consideration when looking at the data for instance to know in which tissue a gene is expressed or not, if a gene promoter could be used for specific gene expression system, e.g., one mosquito strain analysed, immune gene expression profiles (especially in the gut) may be affected by the microbiota, which is known to be different between labs, mating status (not controlled in the study), etc. However, this study is a good start for the creation of an atlas for Aedes aegypti and should constitute the basis for a future and larger deposition of data to complete the picture, e.g., more tissues (hemocytes for instance), more developmental stages, infection with pathogens etc. The creation of an online database is of course positive, but it is regrettable that those data are not integrated in larger databases such as vector base allowing an integrated analysis of data with previous published datasets.

5) The use of cumulative expression values and RNA yield is confusing. There is not an adequate description of library prep to assess the validity of these methods. Typically, libraries are prepped with a subset of the total RNA extracted from a sample. In the manuscript, authors write that they normalized transcript levels by RNA yield, however there is no discussion of whether the volume of tissue for each replicate was standardized. If libraries were prepped with equivalent concentrations of RNA, this normalization is unnecessary. Authors may have used the concentration of RNA used to prepare the RNA-seq libraries for this normalization but the way it is written does not make their methods clear.

6) Additionally, there are points throughout the manuscript that need further explanation to improve clarity and to allow for successful assessment of the methods used. For example, when describing the mosquito equation developed by the authors, a "scaling factor" is mentioned without proper explanation of what this scaling factor is. Furthermore, specifics on the parameters used in the differential expression analysis and the gene ontology enrichment analysis are missing from the methods section.
