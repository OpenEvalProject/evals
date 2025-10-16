# A Bayesian approach to single-particle electron cryo-tomography in RELION-4.0

## Authors

- Jasenkio Zivanov<sup>1</sup> ([ORCID: 0000-0001-8407-0759](https://orcid.org/0000-0001-8407-0759)) †
- Joaquín Otón<sup>2</sup> ([ORCID: 0000-0002-2195-4730](https://orcid.org/0000-0002-2195-4730))
- Zunlong Ke<sup>1</sup> ([ORCID: 0000-0002-8408-850X](https://orcid.org/0000-0002-8408-850X))
- Andriko von Kügelgen<sup>1</sup> ([ORCID: 0000-0002-0017-2414](https://orcid.org/0000-0002-0017-2414))
- Euan Pyle<sup>3</sup> ([ORCID: 0000-0002-4633-4917](https://orcid.org/0000-0002-4633-4917))
- Kun Qu<sup>1</sup>
- Dustin Morado<sup>1</sup>
- Daniel Castaño-Díez<sup>4</sup>
- Giulia Zanetti<sup>3</sup> ([ORCID: 0000-0003-1905-0342](https://orcid.org/0000-0003-1905-0342))
- Tanmay AM Bharat<sup>1</sup> ([ORCID: 0000-0002-0168-0277](https://orcid.org/0000-0002-0168-0277))
- John AG Briggs<sup>1</sup> ([ORCID: 0000-0003-3990-6910](https://orcid.org/0000-0003-3990-6910))
- Sjors HW Scheres<sup>1</sup> ([ORCID: 0000-0002-0462-6540](https://orcid.org/0000-0002-0462-6540)) †

### Affiliations

1. MRC Laboratory of Molecular Biology Cambridge United Kingdom
2. ALBA Synchrotron Cerdanyola del Vallès Spain
3. Institute of Structural and Molecular Biology Birkbeck, University of London London United Kingdom
4. University of Basel Basel Switzerland

† Corresponding author

## Abstract

We present a new approach for macromolecular structure determination from multiple particles in electron cryo-tomography (cryo-ET) data sets. Whereas existing subtomogram averaging approaches are based on 3D data models, we propose to optimise a regularised likelihood target that approximates a function of the 2D experimental images. In addition, analogous to Bayesian polishing and contrast transfer function (CTF) refinement in single-particle analysis, we describe approaches that exploit the increased signal-to-noise ratio in the averaged structure to optimise tilt series alignments, beam-induced motions of the particles throughout the tilt series acquisition, defoci of the individual particles, as well as higher-order optical aberrations of the microscope. Implementation of our approaches in the open-source software package RELION aims to facilitate their general use, in particular for those researchers who are already familiar with its single-particle analysis tools. We illustrate for three applications that our approaches allow structure determination from cryo-ET data to resolutions sufficient for de novo atomic modelling.
