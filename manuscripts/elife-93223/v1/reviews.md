# Peer review - Round 1

Editors:
- Rosana Collepardo, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.93223.3.sa0](https://doi.org/10.7554/eLife.93223.3.sa0)

This important work significantly advances the field of computational modeling of genome organization through the development of OpenNucleome. The evidence supporting the tool's effectiveness is compelling as the authors compare their predictions with experimental data. It is anticipated that OpenNucleome will attract significant interest from the biophysics and genomics communities.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93223.3.sa1](https://doi.org/10.7554/eLife.93223.3.sa1)

Summary:

In this paper the authors develop a comprehensive program to investigate the organization of chromosome structures at 100 kb resolution. It is extremely well executed. The authors have thought through all aspects of the problem. The resulting software will be most useful to the community. Interestingly they capture many experimental observations accurately. I have very little complaints.

Strengths:

A lot of details are provided. The success of the method is well illustrated. Software is easily available,

Weaknesses:

The number of parameters in the energy function is very large. Any justification? Could they simply be the functions?

What would the modification be if the resolution is increased?

They should state that the extracted physical values are scale dependent. Example, viscosity.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93223.3.sa2](https://doi.org/10.7554/eLife.93223.3.sa2)

Summary:

In this work, Lao et al. develop an open-source software (OpenNucleome) for GPU-accelerated molecular dynamics simulation of the human nucleus accounting for chromatin, nucleoli, nuclear speckles, etc. Using this, the authors investigate the steady-state organization and dynamics of many of the nuclear components.

Strengths:

This is a comprehensive open-source tool to study several aspects of the nucleus, including chromatin organization, interactions with lamins and organization, and interactions with nuclear speckles and nucleoli. The model is built carefully, accounting for several important factors and optimizing the parameters iteratively to achieve experimentally known results. Authors have simulated the entire genome at 100kb resolution (which is a very good resolution to simulate and study the entire diploid genome) and predict several static quantities such as the radius of gyration and radial positions of all chromosomes, and time-dependent quantities like the mean-square displacement of important genomic regions.

Weaknesses:

One weakness of the model is that it has several parameters. Some of them are constrained by the experiments. However, the role of every parameter is not clear in the manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93223.3.sa3](https://doi.org/10.7554/eLife.93223.3.sa3)

Summary:

The authors present OpenNucleome, a computational tool for simulating the structure and dynamics of the human nucleus. The software models nuclear components, including chromosomes and nuclear bodies, and incorporates GPU acceleration for potential performance gains. The authors aim to advance the understanding of nuclear organization by providing a tool that aligns with experimental data and is accessible to the genome architecture research community.

Strengths:

OpenNucleome provides a model of the nucleus, contributing to the advancement of computational biology.

Utilizing GPU acceleration with OpenMM may offer potential performance improvements.

Weaknesses:

It could still take advantage of clearer explanations regarding the generation and usage of input and output files and compatibility with other tools.
