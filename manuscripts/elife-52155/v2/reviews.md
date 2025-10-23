# Peer review - Round 1

Editors:
- Helena Pérez Valle, eLife United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52155.sa1](https://doi.org/10.7554/eLife.52155.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "The single-cell eQTLGen Consortium" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by two editors from the eLife Features Team (Helena Pérez Valle and Peter Rodgers). The following individuals involved in review of your submission have agreed to reveal their identity: Stephen B. Montgomery (Reviewer #1); Maud Fagny (Reviewer #2).

The reviewers have discussed the reviews with one another and the editors have drafted this decision to help you prepare a revised submission.

The manuscript introduces the single-cell eQTLGen Consortium, which aims to assess the effect of genetic variants on gene expression at the cell-type level, and describes the goals of the consortium and its plans for data analysis. The authors propose the development of standardized guidelines and pipelines to perform eQTL analyses, as well as a roadmap to perform analyses while preserving anonymity. They highlight the expected results of the Consortium, including a better understanding of the molecular bases of complex diseases and of the cell type involved, and potential clinical applications.

The manuscript is clearly written and interesting, and it outlines a sound an applicable protocol to analyse many cohorts while preserving data privacy. However, it would benefit from addressing a number of issues in greater detail - see below.

Essential revisions:

1. The Consortium does not provide detail of the study design considerations for data producers in any specifics. I.e. how data should be processed, how many cells/individual, how many reads. Minimum number of individuals. Inclusion/exclusion criteria. Further, what type of genotyping will be required for individuals. For example, the authors mention that cells from different individuals can be mixed together and "multiplexed" to reduce cost and avoid confounding, but it would be very useful for the authors to show the mapping power increase obtained from multiplexing. Analyses like this may help researchers decide on their preferred collection design which would allow a better harmonization of data generated from outside the consortium.

2. The analyses proposed are exciting but the specifics of how they will be run are vague. It would be helpful to catalogue existing tools and identify where new tools are needed, highlighting where the code/algorithms will eventually be found.

3. Authors mention gene regulatory networks, when they really plan to study gene co-expression network. "Regulatory" suggests a causal relationship between 2 nodes, while co-expression only relies on correlations. While similar changes in expression levels among cells might suggest a co-regulation, no inference can be made about a regulatory relationship between genes in absence of complementary information such as TF bindings. Some approaches are able to build regulatory networks from expression data, with the addition of prior information (see Sonawane et al., Network Medicine in the age of biomedical big data. 2019. Frontiers in Genetics. doi: 10.3389/fgene.2019.00294).

4. scRNA-seq data has lower power for eQTL mapping than bulk RNA-seq when matched for sample size. It would be informative for the readers and community to get a better sense of the number of eQTLs that we would expect to map based on individual sample size, number of cells captured by experiment, cell-type proportion in PBMC, etc...

5. Many data are mentioned (genomic data, scRNA-seq, scATAC-seq, sc-protein level...), but it is not always clear which ones will be generated, which ones may be generated, and which ones are already existing datasets. Maybe a figure would help?

6. There is limited mention of potential ASE-based or splicing analyses.

7. There is limited mention of how multi-omics from single cell data may improve GRN or other analyses. There are multiple studies that have now obtained different data modalities from the same cells.

8. I would expect some discussion of spatial transcriptomics and its potential.

9. How does the consortium and its work relate to/differ from the following project?

https://chanzuckerberg.com/science/programs-resources/humancellatlas/seednetworks/human-immune-variation-across-genetic-backgrounds-gender-and-time/

10. Please outline the deliverables proposed for the consortium (including a timeline for when they will be available).

11. Aspects of future data sharing and accessibility are essential to address.

12. Please explain how new individuals can become members of the consortium.

13. Please explain the consortium will be funded.
