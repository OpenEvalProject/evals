# Bayesian inference of kinetic schemes for ion channels by Kalman filtering

## Authors

- Jan L Münch<sup>1</sup> ([ORCID: 0000-0002-9177-6466](https://orcid.org/0000-0002-9177-6466)) †
- Fabian Paul<sup>2</sup>
- Ralf Schmauder<sup>1</sup>
- Klaus Benndorf<sup>1</sup> †

### Affiliations

1. Institut für Physiologie II Friedrich Schiller University Jena Jena Germany
2. Department of Biochemistry and Molecular Biology University of Chicago Chicago United States

† Corresponding author

## Abstract

Inferring adequate kinetic schemes for ion channel gating from ensemble currents is a daunting task due to limited information in the data. We address this problem by using a parallelized Bayesian filter to specify hidden Markov models for current and fluorescence data. We demonstrate the flexibility of this algorithm by including different noise distributions. Our generalized Kalman filter outperforms both a classical Kalman filter and a rate equation approach when applied to patch-clamp data exhibiting realistic open-channel noise. The derived generalization also enables inclusion of orthogonal fluorescence data, making unidentifiable parameters identifiable and increasing the accuracy of the parameter estimates by an order of magnitude. By using Bayesian highest credibility volumes, we found that our approach, in contrast to the rate equation approach, yields a realistic uncertainty quantification. Furthermore, the Bayesian filter delivers negligibly biased estimates for a wider range of data quality. For some data sets it identifies more parameters than the rate equation approach. These results also demonstrate the power of assessing the validity of algorithms by Bayesian credibility volumes in general. Finally, we show that our Bayesian filter is more robust against errors induced by either analog filtering before analog-to-digital conversion or by limited time resolution of fluorescence data than a rate equation approach.
