# Discovering and deciphering relationships across disparate data modalities

## Authors

- Joshua T Vogelstein<sup>1</sup> ([ORCID: 0000-0003-2487-6237](https://orcid.org/0000-0003-2487-6237)) †
- Eric W Bridgeford<sup>2</sup>
- Qing Wang<sup>3</sup>
- Carey E Priebe<sup>4</sup>
- Mauro Maggioni<sup>5</sup>
- Cencheng Shen<sup>4</sup>

### Affiliations

1. Department of Biomedical Engineering Johns Hopkins University Baltimore United States
2. Department of Biostatistics Johns Hopkins University Baltimore United States
3. Department of Oncology Johns Hopkins University Baltimore United States
4. Department of Applied Mathematics and Statistics Johns Hopkins University Baltimore United States
5. Department of Mathematics Johns Hopkins University Baltimore United States

† Corresponding author

## Abstract

Understanding the relationships between different properties of data, such as whether a genome or connectome has information about disease status, is increasingly important. While existing approaches can test whether two properties are related, they may require unfeasibly large sample sizes and often are not interpretable. Our approach, 'Multiscale Graph Correlation' (MGC), is a dependence test that juxtaposes disparate data science techniques, including k-nearest neighbors, kernel methods, and multiscale analysis. Other methods may require double or triple the number of samples to achieve the same statistical power as MGC in a benchmark suite including high-dimensional and nonlinear relationships, with dimensionality ranging from 1 to 1000. Moreover, MGC uniquely characterizes the latent geometry underlying the relationship, while maintaining computational efficiency. In real data, including brain imaging and cancer genetics, MGC detects the presence of a dependency and provides guidance for the next experiments to conduct.
