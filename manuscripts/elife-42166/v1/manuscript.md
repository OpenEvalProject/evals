# New tools for automated high-resolution cryo-EM structure determination in RELION-3

## Authors

- Jasenko Zivanov<sup>1</sup>
- Takanori Nakane<sup>1</sup> ([ORCID: 0000-0003-2697-2767](https://orcid.org/0000-0003-2697-2767))
- Björn O Forsberg<sup>2</sup>
- Dari Kimanius<sup>2</sup>
- Wim JH Hagen<sup>3</sup> ([ORCID: 0000-0001-6229-2692](https://orcid.org/0000-0001-6229-2692))
- Erik Lindahl<sup>2</sup> ([ORCID: 0000-0002-2734-2794](https://orcid.org/0000-0002-2734-2794)) †
- Sjors HW Scheres<sup>1</sup> ([ORCID: 0000-0002-0462-6540](https://orcid.org/0000-0002-0462-6540)) †

### Affiliations

1. MRC Laboratory of Molecular Biology Cambridge United Kingdom
2. Department of Biochemistry and Biophysics, Science for Life Laboratory Stockholm University Stockholm Sweden
3. Structural and Computational Biology Unit European Molecular Biology Laboratory Heidelberg Germany

† Corresponding author

## Abstract

Here, we describe the third major release of RELION. CPU-based vector acceleration has been added in addition to GPU support, which provides flexibility in use of resources and avoids memory limitations. Reference-free autopicking with Laplacian-of-Gaussian filtering and execution of jobs from python allows non-interactive processing during acquisition, including 2D-classification, de novo model generation and 3D-classification. Per-particle refinement of CTF parameters and correction of estimated beam tilt provides higher-resolution reconstructions when particles are at different heights in the ice, and/or coma-free alignment has not been optimal. Ewald sphere curvature correction improves resolution for large particles. We illustrate these developments with publicly available data sets: together with a Bayesian approach to beam-induced motion correction it leads to resolution improvements of 0.2-0.7 Å compared to previous RELION versions.
