# Peer review - Round 1

Editors:
- Jenny Tung, Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89594.3.sa0](https://doi.org/10.7554/eLife.89594.3.sa0)

This is an important study that leverages a human-chimpanzee tetraploid iPSC model to test whether cis-regulatory divergence between species tends to be cell type-specific. The evidence supporting the study's primary conclusions together provide convincing evidence for enrichment of species differences in gene regulation in cell type-specific genes and regulatory elements, motivating future work with larger sample sizes of cell lines. This work will be of broad interest in evolutionary and functional genomics.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89594.3.sa1](https://doi.org/10.7554/eLife.89594.3.sa1)

This study aims to identify gene expression differences exclusively caused by cis-regulatory genetic changes by utilizing hybrid cell lines derived from human and chimpanzee. While previous attempts have focused on specific tissues, this study expands the comparison to six different tissues to investigate tissue specificity and derive insights into the evolution of gene expression.

One notable strength of this work lies in the use of composite cell lines, enabling a comparison of gene expression between human and chimpanzee within the same nucleus and shared trans factors environment. However, a potential weakness of the methodology is the use of bulk RNA-seq in diverse tissues, which limits the ability to determine cell-type-specific gene expression and chromatin accessibility regions. Their approach, using hybrid lines, naturally accounts for cell type heterogeneity avoiding the risk of false positives introduced by the otherwise confounding differences in cell type abundances between species, albeit the challenge of false negatives remains an issue. The authors now dully acknowledge this limitation in the manuscript.

Another concern is the use of two replicates derived from the same pair of individuals. While the authors produced cell lines from two pairs of individuals in a previous study (Agloglia et al., 2021). The reason for this experimental design is cost limitations. The authors now acknowledge that the use of replicates could enhance the ability to detect "more" species-specific changes in expression and chromatin accessibility. I would emphasize that replicates would increase robustness to the present findings, given that they are derived from a single pair of individuals.

Furthermore, the study offers the opportunity to relate inter-species differences to trends in molecular evolution. The authors discovered that expression variance and haploinsufficiency score do not fully account for the enrichment of divergence in cell-type-specific genes. The reviewer suggested exploring this further by incorporating external datasets that bin genes based on interindividual transcriptomics variation as a measure of extant transcriptomics constraint (e.g., GTEx reanalysis by Garcia-Perez et al., 2023 -- PMID: 36777183). The authors considered this question to be out of the scope of the paper, yet in my opinion this would enhance one of the main findings of this study.

Additionally, stratifying sequence conservation on ASCA regions, which exhibit similar enrichment of cell-type-specific features, using the Zoonomia data mentioned also in the text (Andrews et al., 2023 -- PMID: 37104580) could provide valuable insights. While the author did not find Zoonomia Phastcons values available, they used PhastCons derived from a 470-way alignment of mammals. I commend the authors for their diligent efforts, which undoubtedly bolster their findings that an enrichment in ASCA is evident across all levels of sequence conservation. However, this recent analysis indicates the presence of a potential relationship between sequence conservation and ASCA. It may be advantageous to consider evaluating more quantile subdivisions of maxZ values and pPhastCons values, with the inclusion of these results in the supplementary materials. This approach would be preferable, even if the precise reasons behind the observed discrepancy are not fully elucidated.

Another potential strength of this study is the identification of specific cases of paired allele-specific expression (ASE) and allele-specific chromatin accessibility (ASCA) with biological significance. Prioritizing specific variants remains a challenge, and the authors apply a machine learning approach to identify potential causative variants that disrupt binding sites in two examples (FABP7 and GAD1 in motor neurons). However, additional work is needed to convincingly demonstrate the functionality of these selected variants. Strengthening this section with additional validation of ASE, ASCA, and the specific putative causal variants identified would enhance the overall robustness of the paper. The authors have opted to defer these validations to future studies.

Additionally, the authors support the selected ASE-ASCA pairs by examining external datasets of adult brain comparative genomics (Ma et al., 2022) and organoids (Kanton et al., 2019). While these resources are valuable for comparing observed species biases, the analysis is not systematic, even for the two selected genes. For example, it would be beneficial to investigate if FABP7 exhibits species bias in any cell type in Kanton et al.'s organoids or if GAD1 is species-biased in adult primate brains from Ma et al. Comparing these datasets with the present study, along with the Agoglia et al. reference, would provide a more comprehensive perspective. In the revised version of the manuscript the authors have evaluated the expression of GAD1 in Ma et al, and FABP7 in Sousa et al 2017. For instance, GAD1 show cell type specific species biases in the later. The authors opted for not showing this in the manuscript, However, it remains unclear why certain datasets were favored over others, or why FABP7 should not be evaluated in Kanton et al.

The use of the term "human-derived" in ASE and ASCA has now been avoided.

Finally, throughout the paper, the authors refer to "hybrid cell lines." It has been suggested to use the term "composite cell lines" instead to address potential societal concerns associated with the term "hybrid," which some may associate with reproductive relationships (Pavlovic et al., 2022 -- PMID: 35082442). The authors have presented an eloquent and persuasive explanation that I found to be highly informative.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89594.3.sa2](https://doi.org/10.7554/eLife.89594.3.sa2)

The authors utilize chimpanzee-human hybrid cell lines to assess cis-regulatory evolution. These hybrid cell lines offer a well-controlled environment, enabling clear differentiation between cis-regulatory effects and environmental or other trans effects.

In their research, Wang et al. expand the range of chimpanzee-human hybrid cell lines to encompass six new developmental cell types derived from all three germ layers. This expansion allows them to discern cell type-specific cis-regulatory changes between species from more pleiotropic ones. Although the study investigates only two iPSC clones, the RNA- and ATAC-seq data produced for this paper is a valuable resource.

The authors begin their analysis by examining the relationship between allele-specific expression (ASE) as a measure of species divergence and cell type specificity. They find that cell-type-specific genes exhibit more divergent expression. By integrating this data with measures of constraint within human populations, the authors conclude that the increased divergence of tissue-specific genes is, at least in part, attributable to positive selection. A similar pattern emerges when assessing allele-specific chromatin accessibility (ASCA) as a measure of divergence of cis-regulatory elements (CREs) in the same cell lines.

By correlating these two measures, the authors identify 95 CRE-gene pairs where tissue-specific ASE aligns with tissue-specific ASCA. Among these pairs, the authors select two genes of interest for further investigation. Notably, the authors employ an intriguing machine learning approach in which they compare the inferred chromatin state of the human sequence with that of the chimpanzee sequence to pinpoint putatively causal variants.

Overall, this study delves into the examination of gene expression and chromatin accessibility within hybrid cell lines, showcasing how this data can be leveraged to identify potential causal sequence differences underlying between-species expression changes.

All in all most conclusions appear solid, with the exception of the interpretation of a cell type/state identification machine learning model to pinpoint putatively causal variants. The described variants lack any functional validation and there is no data that measure the certainty of the results.
