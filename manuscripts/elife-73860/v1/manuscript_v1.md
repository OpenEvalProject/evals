# Bayesian machine learning analysis of single-molecule fluorescence colocalization images

## Authors

- Yerdos A Ordabayev<sup>1</sup>
- Larry J Friedman<sup>1</sup> ([ORCID: 0000-0003-4946-8731](https://orcid.org/0000-0003-4946-8731))
- Jeff Gelles<sup>1</sup> ([ORCID: 0000-0001-7910-3421](https://orcid.org/0000-0001-7910-3421)) †
- Douglas L Theobald<sup>1</sup> ([ORCID: 0000-0002-2695-8343](https://orcid.org/0000-0002-2695-8343)) †

### Affiliations

1. Department of Biochemistry Brandeis University Waltham United States

† Corresponding author

## Abstract

Multi-wavelength single-molecule fluorescence colocalization (CoSMoS) methods allow elucidation of complex biochemical reaction mechanisms. However, analysis of CoSMoS data is intrinsically challenging because of low image signal-to-noise ratios, non-specific surface binding of the fluorescent molecules, and analysis methods that require subjective inputs to achieve accurate results. Here, we use Bayesian probabilistic programming to implement Tapqir, an unsupervised machine learning method that incorporates a holistic, physics-based causal model of CoSMoS data. This method accounts for uncertainties in image analysis due to photon and camera noise, optical non-uniformities, non-specific binding, and spot detection. Rather than merely producing a binary 'spot/no spot' classification of unspecified reliability, Tapqir objectively assigns spot classification probabilities that allow accurate downstream analysis of molecular dynamics, thermodynamics, and kinetics. We both quantitatively validate Tapqir performance against simulated CoSMoS image data with known properties and also demonstrate that it implements fully objective, automated analysis of experiment-derived data sets with a wide range of signal, noise, and non-specific binding characteristics.
