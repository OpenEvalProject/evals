# Lack of evidence for increased transcriptional noise in aged tissues

## Authors

- Olga Ibañez-Solé<sup>1</sup> ([ORCID: 0000-0002-0552-9793](https://orcid.org/0000-0002-0552-9793))
- Alex M Ascensión<sup>1</sup>
- Marcos J Araúzo-Bravo<sup>1</sup> †
- Ander Izeta<sup>2</sup> ([ORCID: 0000-0003-1879-7401](https://orcid.org/0000-0003-1879-7401)) †

### Affiliations

1. Computational Biology and Systems Biomedicine Group Biodonostia Health Research Institute San Sebastian Spain
2. Tissue Engineering Laboratory Biodonostia Health Research Institute San Sebastian Spain

† Corresponding author

## Abstract

Aging is often associated with a loss of cell type identity that results in an increase in transcriptional noise in aged tissues. If this phenomenon reflects a fundamental property of aging remains an open question. Transcriptional changes at the cellular level are best detected by single-cell RNA sequencing (scRNAseq). However, the diverse computational methods used for the quantification of age-related loss of cellular identity have prevented reaching meaningful conclusions by direct comparison of existing scRNAseq datasets. To address these issues we created Decibel, a Python toolkit that implements side-to-side four commonly used methods for the quantification of age-related transcriptional noise in scRNAseq data. Additionally, we developed Scallop, a novel computational method for the quantification of membership of single cells to their assigned cell type cluster. Cells with a greater Scallop membership score are transcriptionally more stable. Application of these computational tools to seven aging datasets showed large variability between tissues and datasets, suggesting that increased transcriptional noise is not a universal hallmark of aging. To understand the source of apparent loss of cell type identity associated with aging, we analyzed cell type-specific changes in transcriptional noise and the changes in cell type composition of the mammalian lung. No robust pattern of cell type-specific transcriptional noise alteration was found across aging lung datasets. In contrast, age-associated changes in cell type composition of the lung were consistently found, particularly of immune cells. These results suggest that claims of increased transcriptional noise of aged tissues should be reformulated.
