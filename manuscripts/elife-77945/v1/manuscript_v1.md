# Automated hippocampal unfolding for morphometry and subfield segmentation with HippUnfold

## Authors

- Jordan DeKraker<sup>1</sup> ([ORCID: 0000-0002-4093-0582](https://orcid.org/0000-0002-4093-0582)) †
- Roy AM Haast<sup>2</sup>
- Mohamed D Yousif<sup>1</sup>
- Bradley Karat<sup>1</sup> ([ORCID: 0000-0002-6550-1418](https://orcid.org/0000-0002-6550-1418))
- Jonathan C Lau<sup>1</sup>
- Stefan Köhler<sup>3</sup> ([ORCID: 0000-0003-1905-6453](https://orcid.org/0000-0003-1905-6453))
- Ali R Khan<sup>1</sup> ([ORCID: 0000-0002-0760-8647](https://orcid.org/0000-0002-0760-8647)) †

### Affiliations

1. University of Western Ontario London Canada
2. Aix-Marseille University Marseille France
3. Brain and Mind Institute University of Western Ontario london Canada

† Corresponding author

## Abstract

Like neocortical structures, the archicortical hippocampus differs in its folding patterns across individuals. Here, we present an automated and robust BIDS-App, HippUnfold, for defining and indexing individual-specific hippocampal folding in MRI, analogous to popular tools used in neocortical reconstruction. Such tailoring is critical for inter-individual alignment, with topology serving as the basis for homology. This topological framework enables qualitatively new analyses of morphological and laminar structure in the hippocampus or its subfields. It is critical for refining current neuroimaging analyses at a meso- as well as micro-scale. HippUnfold uses state-of-the-art deep learning combined with previously developed topological constraints to generate uniquely folded surfaces to fit a given subject's hippocampal conformation. It is designed to work with commonly employed sub-millimetric MRI acquisitions, with possible extension to microscopic resolution. In this paper we describe the power of HippUnfold in feature extraction, and highlight its unique value compared to several extant hippocampal subfield analysis methods.
