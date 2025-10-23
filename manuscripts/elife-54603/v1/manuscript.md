# Coverage-dependent bias creates the appearance of binary splicing in single cells

## Authors

- Carlos F Buen Abad Najar<sup>1</sup>
- Nir Yosef<sup>2</sup> ([ORCID: 0000-0001-9004-1225](https://orcid.org/0000-0001-9004-1225)) †
- Liana F Lareau<sup>3</sup> ([ORCID: 0000-0003-3223-3426](https://orcid.org/0000-0003-3223-3426)) †

### Affiliations

1. Center for Computational Biology University of California, Berkeley Berkeley United States
2. Department of Electrical Engineering and Computer Science and the Center for Computational Biology University of California, Berkeley Berkeley United States
3. Department of Bioengineering University of California, Berkeley Berkeley United States

† Corresponding author

## Abstract

Single cell RNA sequencing provides powerful insight into the factors that determine each cell's unique identity. Previous studies led to the surprising observation that alternative splicing among single cells is highly variable and follows a bimodal pattern: a given cell consistently produces either one or the other isoform for a particular splicing choice, with few cells producing both isoforms. Here we show that this pattern arises almost entirely from technical limitations. We analyze alternative splicing in human and mouse single cell RNA-seq datasets, and model them with a probabilistic simulator. Our simulations show that low gene expression and low capture efficiency distort the observed distribution of isoforms. This gives the appearance of binary splicing outcomes, even when the underlying reality is consistent with more than one isoform per cell. We show that accounting for the true amount of information recovered can produce biologically meaningful measurements of splicing in single cells.
