# Locating Macromolecular Assemblies in Cells by 2D Template Matching with cisTEM

## Authors

- Bronwyn A Lucas<sup>1</sup>
- Benjamin A Himes<sup>2</sup> ([ORCID: 0000-0001-7777-0298](https://orcid.org/0000-0001-7777-0298))
- Liang Xue<sup>3</sup> ([ORCID: 0000-0003-4368-2526](https://orcid.org/0000-0003-4368-2526))
- Tim Grant<sup>1</sup> ([ORCID: 0000-0002-4855-8703](https://orcid.org/0000-0002-4855-8703))
- Julia Mahamid<sup>4</sup> ([ORCID: 0000-0001-6968-041X](https://orcid.org/0000-0001-6968-041X))
- Nikolaus Grigorieff<sup>2</sup> ([ORCID: 0000-0002-1506-909X](https://orcid.org/0000-0002-1506-909X)) †

### Affiliations

1. Janelia Research Campus Howard Hughes Medical Institute Ashburn United States
2. RNA Therapeutics Institute University of Massachusetts Medical School Worcester United States
3. Structural and Computational Biology Unit EMBL Heidelberg Germany
4. European Molecular Biology Laboratory Heidelberg Germany

† Corresponding author

## Abstract

For a more complete understanding of molecular mechanisms, it is important to study macromolecules and their assemblies in the broader context of the cell. This context can be visualized at nanometer resolution in three dimensions (3D) using electron cryo-tomography, which requires tilt series to be recorded and computationally aligned, currently limiting throughput. Additionally, the high-resolution signal preserved in the raw tomograms is currently limited by a number of technical difficulties, leading to an increased false-positive detection rate when using 3D template matching to find molecular complexes in tomograms. We have recently described a 2D template matching approach that addresses these issues by including high-resolution signal preserved in single-tilt images. A current limitation of this approach is the high computational cost that limits throughput. We describe here a GPU-accelerated implementation of 2D template matching in the image processing software cisTEM that allows for easy scaling and improves the accessibility of this approach. We apply 2D template matching to identify ribosomes in images of frozen-hydrated Mycoplasma pneumoniae cells with high precision and sensitivity, demonstrating that this is a versatile tool for in situ visual proteomics and in situ structure determination. We benchmark the results with 3D template matching of tomograms acquired on identical sample locations and identify strengths and weaknesses of both techniques, which offer complementary information about target localization and identity.
