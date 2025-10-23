# A flexible framework for simulating and fitting generalized drift-diffusion models

## Authors

- Maxwell Shinn<sup>1</sup> ([ORCID: 0000-0002-7424-4230](https://orcid.org/0000-0002-7424-4230))
- Norman H Lam<sup>2</sup>
- John D Murray<sup>3</sup> ([ORCID: 0000-0003-4115-8181](https://orcid.org/0000-0003-4115-8181)) †

### Affiliations

1. Department of Psychiatry Yale University New Haven United States
2. Department of Physics Yale University New Haven United States
3. Psychiatry, Neuroscience, and Physics Yale University New Haven United States

† Corresponding author

## Abstract

The drift-diffusion model (DDM) is an important decision-making model in cognitive neuroscience. However, innovations in model form have been limited by methodological challenges. Here, we introduce the generalized drift-diffusion model (GDDM) framework for building and fitting DDM extensions, and provide a software package which implements the framework. The GDDM framework augments traditional DDM parameters through arbitrary user-defined functions. Models are solved numerically by directly solving the Fokker-Planck equation using efficient numerical methods, yielding a 100-fold or greater speedup over standard methodology. This speed allows GDDMs to be fit to data using maximum likelihood on the full response time (RT) distribution. We demonstrate fitting of GDDMs within our framework to both animal and human datasets from perceptual decision-making tasks, with better accuracy and fewer parameters than several DDMs implemented using the latest methodology, to test hypothesized decision-making mechanisms. Overall, our framework will allow for decision-making model innovation and novel experimental designs.
