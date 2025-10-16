# Graphical-model framework for automated annotation of cell identities in dense cellular images

## Authors

- Shivesh Chaudhary<sup>1</sup>
- Sol Ah Lee<sup>1</sup>
- Yueyi Li<sup>1</sup>
- Dhaval S Patel<sup>1</sup>
- Hang Lu<sup>2</sup> ([ORCID: 0000-0002-6881-660X](https://orcid.org/0000-0002-6881-660X)) †

### Affiliations

1. Chemical & Biomolecular Engineering Georgia Institute of Technology Atlanta United States
2. Chemical & Biomolecular Engineering Georgia Institute of Technology Atlanta, GA United States

† Corresponding author

## Abstract

Although identifying cell names in dense image stacks is critical in analyzing functional whole-brain data enabling comparison across experiments, unbiased identification is very difficult, and relies heavily on researchers' experiences. Here we present a probabilistic-graphical-model framework, CRF_ID, based on Conditional Random Fields, for unbiased and automated cell identification. CRF_ID focuses on maximizing intrinsic similarity between shapes. Compared to existing methods, CRF_ID achieves higher accuracy on simulated and ground-truth experimental datasets, and better robustness against challenging noise conditions common in experimental data. CRF_ID can further boost accuracy by building atlases from annotated data in highly computationally efficient manner, and by easily adding new features (e.g. from new strains). We demonstrate cell annotation in C. elegans images across strains, animal orientations, and tasks including gene-expression localization, multi-cellular and whole-brain functional imaging experiments. Together, these successes demonstrate that unbiased cell annotation can facilitate biological discovery, and this approach may be valuable to annotation tasks for other systems.
