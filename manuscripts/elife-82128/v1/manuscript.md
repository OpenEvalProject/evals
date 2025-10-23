# Generating colorblind-friendly scatter plots for single-cell data

## Authors

- Tejas Guha<sup>1</sup>
- Elana J Fertig<sup>2</sup> ([ORCID: 0000-0003-3204-342X](https://orcid.org/0000-0003-3204-342X)) †
- Atul Deshpande<sup>2</sup> ([ORCID: 0000-0001-5144-6924](https://orcid.org/0000-0001-5144-6924)) †

### Affiliations

1. Department of Electrical and Computer Engineering University of Maryland, College Park College Park United States
2. Department of Oncology Johns Hopkins University Baltimore United States

† Corresponding author

## Abstract

Reduced-dimension or spatial in situ scatter plots are widely employed in bioinformatics papers analyzing single-cell data to present phenomena or cell-conditions of interest in cell groups. When displaying these cell groups, color is frequently the only graphical cue used to differentiate them. However, as the complexity of the information presented in these visualizations increases, the usefulness of color as the only visual cue declines, especially for the sizable readership with color-vision deficiencies (CVDs). In this paper, we present scatterHatch, an R package that creates easily interpretable scatter plots by redundant coding of cell groups using colors as well as patterns. We give examples to demonstrate how the scatterHatch plots are more accessible than simple scatter plots when simulated for various types of CVDs.
