# ProteInfer, deep neural networks for protein functional inference

## Authors

- Theo Sanderson<sup>1</sup> ([ORCID: 0000-0003-4177-2851](https://orcid.org/0000-0003-4177-2851)) †
- Maxwell L Bileschi<sup>2</sup>
- David Belanger<sup>2</sup>
- Lucy J Colwell<sup>2</sup>

### Affiliations

1. The Francis Crick Institute London United Kingdom
2. Google AI Boston United States

† Corresponding author

## Abstract

Predicting the function of a protein from its amino acid sequence is a long-standing challenge in bioinformatics. Traditional approaches use sequence alignment to compare a query sequence either to thousands of models of protein families or to large databases of individual protein sequences. Here we introduce ProteInfer, which instead employs deep convolutional neural networks to directly predict a variety of protein functions - EC numbers and GO terms - directly from an unaligned amino acid sequence. This approach provides precise predictions which complement alignment-based methods, and the computational efficiency of a single neural network permits novel and lightweight software interfaces, which we demonstrate with an in-browser graphical interface for protein function prediction in which all computation is performed on the user's personal computer with no data uploaded to remote servers. Moreover, these models place full-length amino acid sequences into a generalised functional space, facilitating downstream analysis and interpretation. To read the interactive version of this paper, please visit https://google-research.github.io/proteinfer/.
