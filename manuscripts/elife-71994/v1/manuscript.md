# Signature-scoring methods developed for bulk samples are not adequate for cancer single-cell RNA sequencing data

## Authors

- Nighat Noureen<sup>1</sup>
- Zhenqing Ye<sup>1</sup>
- Yidong Chen<sup>2</sup>
- Xiaojing Wang<sup>1</sup>
- Siyuan Zheng<sup>1</sup> ([ORCID: 0000-0002-1031-9424](https://orcid.org/0000-0002-1031-9424)) †

### Affiliations

1. Greehey Children's Cancer Research Institute The University of Texas Health Science Center at San Antonio San Antonio United States
2. Greehey Children's Cancer Research Institute University of Texas Health Science Center at San Antonio San Antonio United States

† Corresponding author

## Abstract

Quantifying the activity of gene expression signatures is common in analyses of single-cell RNA sequencing data. Methods originally developed for bulk samples are often used for this purpose without accounting for contextual differences between bulk and single-cell data. More broadly, these methods have not been benchmarked. Here we benchmark five such methods, including single sample gene set enrichment analysis (ssGSEA), Gene Set Variation Analysis (GSVA), AUCell, Single Cell Signature Explorer (SCSE), and a new method we developed, Jointly Assessing Signature Mean and Inferring Enrichment (JASMINE). Using cancer as an example, we show cancer cells consistently express more genes than normal cells. This imbalance leads to bias in performance by bulk-sample-based ssGSEA in gold standard tests and down sampling experiments. In contrast, single-cell-based methods are less susceptible. Our results suggest caution should be exercised when using bulk-sample-based methods in single-cell data analyses, and cellular contexts should be taken into consideration when designing benchmarking strategies.
