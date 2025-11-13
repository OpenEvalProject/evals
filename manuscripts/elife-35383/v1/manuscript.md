# cisTEM, User-friendly software for single-particle image processing

## Authors

- Timothy Grant<sup>1</sup> †
- Alexis Rohou<sup>1</sup> ([ORCID: 0000-0002-3343-9621](https://orcid.org/0000-0002-3343-9621)) †
- Nikolaus Grigorieff<sup>1</sup> ([ORCID: 0000-0002-1506-909X](https://orcid.org/0000-0002-1506-909X)) †

### Affiliations

1. Janelia Research Campus, Howard Hughes Medical Institute Ashburn United States

† Corresponding author

## Abstract

We have developed new open-source software called cisTEM (computational imaging system for transmission electron microscopy) for the processing of data for high-resolution electron cryo-microscopy and single-particle averaging. cisTEM features a graphical user interface that is used to submit jobs, monitor their progress, and display results. It implements a full processing pipeline including movie processing, image defocus determination, automatic particle picking, 2D classification, ab-initio 3D map generation from random parameters, 3D classification, and high-resolution refinement and reconstruction. Some of these steps implement newly-developed algorithms; others were adapted from previously published algorithms. The software is optimized to enable processing of typical datasets (2000 micrographs, 200k - 300k particles) on a high-end, CPU-based workstation in half a day or less, comparable to GPU-accelerated processing. Jobs can also be scheduled on large computer clusters using flexible run profiles that can be adapted for most computing environments. cisTEM is available for download from cistem.org.
