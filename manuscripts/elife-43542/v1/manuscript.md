# Automated cryo-EM structure refinement using correlation-driven molecular dynamics

## Authors

- Maxim Igaev<sup>1</sup> ([ORCID: 0000-0001-8781-1604](https://orcid.org/0000-0001-8781-1604)) †
- Carsten Kutzner<sup>1</sup>
- Lars V Bock<sup>1</sup>
- Andrea C Vaiana<sup>1</sup> ([ORCID: 0000-0002-8865-0651](https://orcid.org/0000-0002-8865-0651)) †
- Helmut Grubmüller<sup>1</sup> ([ORCID: 0000-0002-3270-3144](https://orcid.org/0000-0002-3270-3144)) †

### Affiliations

1. Department of Theoretical and Computational Biophysics Max Planck Institute for Biophysical Chemistry Göttingen Germany

† Corresponding author

## Abstract

We present a correlation-driven molecular dynamics (CDMD) method for automated refinement of atomistic models into cryo-electron microscopy (cryo-EM) maps at resolutions ranging from near-atomic to subnanometer. It utilizes a chemically accurate force field and thermodynamic sampling to improve the real-space correlation between the modeled structure and the cryo-EM map. Our framework employs a gradual increase in resolution and map-model agreement as well as simulated annealing, and allows fully automated refinement without manual intervention or any additional rotamer- and backbone-specific restraints. Using multiple challenging systems covering a wide range of map resolutions, system sizes, starting model geometries and distances from the target state, we assess the quality of generated models in terms of both model accuracy and potential of overfitting. To provide an objective comparison, we apply several well-established methods across all examples and demonstrate that CDMD performs best in most cases.
