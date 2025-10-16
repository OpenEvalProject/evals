# Rapid, reference-free human genotype imputation with denoising autoencoders

## Authors

- Raquel Dias<sup>1</sup>
- Doug Evans<sup>2</sup>
- Shang-Fu Chen<sup>2</sup>
- Kai-Yu Chen<sup>2</sup>
- Salvatore Loguercio<sup>2</sup>
- Leslie Chan<sup>2</sup>
- Ali Torkamani<sup>2</sup> ([ORCID: 0000-0003-0232-8053](https://orcid.org/0000-0003-0232-8053)) †

### Affiliations

1. Department of Microbiology and Cell Science University of Florida Gainesville United States
2. Scripps Research Translational Institute Scripps Research Institute La Jolla United States

† Corresponding author

## Abstract

Genotype imputation is a foundational tool for population genetics. Standard statistical imputation approaches rely on the co-location of large whole-genome sequencing-based reference panels, powerful computing environments, and potentially sensitive genetic study data. This results in computational resource and privacy-risk barriers to access to cutting-edge imputation techniques. Moreover, the accuracy of current statistical approaches is known to degrade in regions of low and complex linkage disequilibrium. Artificial neural network-based imputation approaches may overcome these limitations by encoding complex genotype relationships in easily portable inference models. Here we demonstrate an autoencoder-based approach for genotype imputation, using a large, commonly used reference panel, and spanning the entirety of human chromosome 22. Our autoencoder-based genotype imputation strategy achieved superior imputation accuracy across the allele-frequency spectrum and across genomes of diverse ancestry, while delivering at least 4-fold faster inference run time relative to standard imputation tools.
