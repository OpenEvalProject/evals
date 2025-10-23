# SynEM, automated synapse detection for connectomics

## Authors

- Benedikt Staffler<sup>1</sup>
- Manuel Berning<sup>1</sup> ([ORCID: 0000-0002-3679-8363](https://orcid.org/0000-0002-3679-8363))
- Kevin M Boergens<sup>1</sup>
- Anjali Gour<sup>1</sup>
- Patrick van der Smagt<sup>2</sup>
- Moritz Helmstaedter<sup>1</sup> ([ORCID: 0000-0001-7973-0767](https://orcid.org/0000-0001-7973-0767)) †

### Affiliations

1. Department of Connectomics Max Planck Institute for Brain Research Frankfurt Germany
2. Data Lab Volkswagen Group Munich Germany

† Corresponding author

## Abstract

Nerve tissue contains a high density of chemical synapses, about 1 per µm 3 in the mammalian cerebral cortex. Thus, even for small blocks of nerve tissue, dense connectomic mapping requires the identification of millions to billions of synapses. While the focus of connectomic data analysis has been on neurite reconstruction, synapse detection becomes limiting when datasets grow in size and dense mapping is required. Here, we report SynEM, a method for automated detection of synapses from conventionally en-bloc stained 3D electron microscopy image stacks. The approach is based on a segmentation of the image data and focuses on classifying borders between neuronal processes as synaptic or non-synaptic. SynEM yields 97% precision and recall in binary cortical connectomes with no user interaction. It scales to large volumes of cortical neuropil, plausibly even whole-brain datasets. SynEM removes the burden of manual synapse annotation for large densely mapped connectomes.
