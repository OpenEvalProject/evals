# Peer review - Round 1

Editors:
- Joon-Yong An, Korea University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90214.3.sa0](https://doi.org/10.7554/eLife.90214.3.sa0)

This paper reports a useful finding on the impact of choices of quality control and differential analysis methods on the discovery of disease-associated gene expression signatures. The study provides a solid comparison of the data process by re-analysis of a large-scale snRNA-seq dataset for Alzheimer's disease. This paper would be of interest to the community as to rigorous analyses for large-scale single-cell datasets.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90214.3.sa1](https://doi.org/10.7554/eLife.90214.3.sa1)

Murphy, Fancy and Skene performed a reanalysis of snRNA-seq data from Alzheimer Disease (AD) patients and healthy controls published previously by Mathys et al. (2019), arriving at the conclusion that many of the transcriptional differences described in the original publication were false positives. This was achieved by revising the strategy for both quality control and differential expression analysis. With this re-analysis, the authors aim to raise awareness of the impact of data analysis choices for scRNA-seq data and to caution focus on putatively wrongly identified genes in the AD research community. The revised manuscript has been improved by separating QC and DE analysis, which makes interpretation of both steps more straightforward.

STRENGTHS:

The authors demonstrate that the choice of data analysis strategy can have a vast impact on the results of a study, which in itself may not be obvious to many researchers.

The authors apply a pseudobulk-based differential expression analysis strategy (essentially, adding up counts from all cells per individual and comparing those counts with standard RNA-seq differential expression tests), which is (a) in line with latest community recommendations, (b) different from the "default options" in most popular scRNA-seq analysis suites, and (c) explains the vastly different number of DEGs identified by the authors and the original publication. The recommendation of this approach together with a detailed assessment of the DEGs found by both methodologies could potentially be a useful finding for the research community. Unfortunately, it is currently not sufficiently substantiated.

All code and data used in this study are publicly available to the readers.

WEAKNESSES:

The authors interpret the fact that they found fewer DEGs with their method than the original paper as a good thing by making the assumption that all genes that were not found were false positives. However, they do not prove this, and it is likely that at least some genes were not found due to a lack of statistical power and not because they were actually "incorrect". The original paper also had performed independent validations of some genes that were not found here. I had raised this weakness in my first review, but it was not explicitly addressed and still pertains to the revised manuscript. The authors have added an analysis that shows that "pseudoreplication" is prone to false positive (FP) discoveries for high cell numbers (Fig. 1f), but this does not prove that all of Mathys' DEGs were wrong.

I am concerned that almost all DEGs found by the authors are in the rare cell types, foremost the rare microglia (see Fig. 1e). Indeed, there is a weak negative correlation between cell counts and numbers of DEGs (Fig. 1e), if the correlation analysis is to be believed (see next point). It is unclear to me how many cells the pseudo-bulk counts were based on for these cell types, but it seems that (a) there were few and (b) there were quite few reads per cells. If both are the case, the pseudobulk counts for these cell populations might be rather noisy and the DEG results liable to outliers with extreme fold changes. Supp. Fig. 3b now shows three examples of DEGs, of which one (EGR1) looks like the DE call is indeed largely driven by four outliers, while Supp. Fig 3a shows at least one gene (BEX1) that could be FP of the pseudobulk approach due to insufficient statistical power. The authors go on to cite two papers (one is their own, published in a journal with suspected lack of appropriate quality assurance measures https://predatoryreports.org/the-predatory-journals-1), to support that the finding of DEGs in microglia "makes more sense" (l. 127). In summary, neither the presented examples nor the supporting literature are convincing. Lastly, the authors even show themselves that their approach is liable to FPs if applied with very low cell numbers in the range of those for microglia and OPCs (Fig. 1g).

The correlation analysis between cell counts and number of DEGs found is weak. In all three cases (Fig. 1c, d, e) the correlation is largely driven by a single outlier data point.

The authors claim they improved the quality control of the dataset but offer no objective metric to assess this putative improvement. The authors' QC procedure removes some 20k cells that had not been filtered out by Mathys' et al. As the authors state themselves, this difference is mostly due to the removal of cells with a high mitochondrial read content. Murphy et al use a fixed threshold for the mitochondrial percentage of reads, while the original paper had removed cell clusters with an "abnormally high" mitochondrial read fraction. That also seems reasonable, given that some cells might have a higher mitochondrial read content for reasons other than being "low quality". Simply stating that Mathys' approach was ineffective at removing cells with high mitochondrial read content is a self-fulfilling prophecy given the difference in approach, and itself not proof that the original QC procedure was inferior.

Batch correction: "Dataset integration has become a common step in single-cell RNA-Seq protocols and is recommended to remove confounding sources of variation" (l. 38). While it is true that many authors now choose to perform an integration step as part of their analysis workflow, this is by no means uncontroversial as there is a risk of "over-integration" and loss of true biological differences. I had raised this point previously, but the authors chose not to address it (quoted text and line numbers updated). Given that there is controversy in the literature and "community opinion" on the topic of data integration, this is another example of the authors claiming superiority in analysis without showing proof.

Due to a lack of comparison with other methods and due to the fact that the author's methodology was only applied to a single dataset, the paper presents merely a case study, which could be useful but falls short of providing a general recommendation for a best practice workflow.

APPRAISAL:

The manuscript could help to increase awareness of data analysis choices in the community, but only if the superiority of the methodology was clearly demonstrated. However, the authors only show that there are differences but have no convincing (orthogonal) evidence that their methodology was indeed better. This applies to both QC and DE analysis.
