# DeepFly3D, a deep learning-based approach for 3D limb and appendage tracking in tethered, adult Drosophila

## Authors

- Semih Günel<sup>1</sup> †
- Helge Rhodin<sup>1</sup> ([ORCID: 0000-0003-2692-0801](https://orcid.org/0000-0003-2692-0801))
- Daniel Morales<sup>2</sup> ([ORCID: 0000-0002-7469-0898](https://orcid.org/0000-0002-7469-0898))
- João H Campagnolo<sup>2</sup>
- Pavan Ramdya<sup>2</sup> ([ORCID: 0000-0001-5425-4610](https://orcid.org/0000-0001-5425-4610)) †
- Pascal Fua<sup>1</sup>

### Affiliations

1. School of Computer and Communication Sciences, Computer Vision Laboratory EPFL Lausanne Switzerland
2. School of Life Sciences, Brain Mind Institute and Interfaculty Institute of Bioengineering, Neuroengineering Laboratory EPFL Lausanne Switzerland

† Corresponding author

## Abstract

Studying how neural circuits orchestrate limbed behaviors requires the precise measurement of the positions of each appendage in 3-dimensional (3D) space. Deep neural networks can estimate 2-dimensional (2D) pose in freely behaving and tethered animals. However, the unique challenges associated with transforming these 2D measurements into reliable and precise 3D poses have not been addressed for small animals including the fly, Drosophila melanogaster. Here we present DeepFly3D, a software that infers the 3D pose of tethered, adult Drosophila using multiple camera images. DeepFly3D does not require manual calibration, uses pictorial structures to automatically detect and correct pose estimation errors, and uses active learning to iteratively improve performance. We demonstrate more accurate unsupervised behavioral embedding using 3D joint angles rather than commonly used 2D pose data. Thus, DeepFly3D enables the automated acquisition of Drosophila behavioral measurements at an unprecedented level of detail for a variety of biological applications.
