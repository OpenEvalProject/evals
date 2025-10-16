# Peer review - Round 1

Editors:
- Warren Andrew Andayi, Murang'a University of Technology Kenya

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95595.3.sa0](https://doi.org/10.7554/eLife.95595.3.sa0)

The study provides a valuable showcase of a workflow to perform large-scale characterization of drug mechanisms of action using proteomics in which on-target and off-targets of 166 compounds using proteome solubility analysis in living cells and cell lysates were determined. The evidence supporting the claims of the authors is solid, however, the inclusion of more replicate experiments and more statistical rigor would have strengthened the study. This will be of broad interest to medicinal chemists, toxicologists, computational biologists and biochemists.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95595.3.sa1](https://doi.org/10.7554/eLife.95595.3.sa1)

This paper describes proteome solubility analysis (PISA) of 96 compounds in living cells and 70 compounds in cell lysates. A wealth of information related to on- and off-target engagement is uncovered. This work fits well the eLife profile, will be of interest to a large community of proteomics researchers, and thus is likely to be reasonably highly cited.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95595.3.sa2](https://doi.org/10.7554/eLife.95595.3.sa2)

Summary:

This work aims to demonstrate how recent advances in thermal stability assays can be utilised to screen chemical libraries and determine compound mechanism of action. Focusing on 96 compounds with known mechanisms of action, they use the PISA assay to measure changes in protein stability upon treatment with a high dose (10uM) in live K562 cells and whole cell lysates from K562 or HCT116. They intend this work to showcase a robust workflow which can serve as a roadmap for future studies.

Strengths:

The major strength of this study is the combination of live and whole cell lysates experiments. This allows the authors to compare the results from these two approaches to identify novel ligand-induced changes in thermal stability with greater confidence. More usefully, this also enables the authors to separate primary and secondary effects of the compounds within the live cell assay.

The study also benefits from the number of compounds tested within the same framework, which allows the authors to make direct comparisons between compounds.

These two strengths are combined when they compare between CHEK1 inhibitors and suggest that AZD-7762 likely induces secondary destabilisation of CRKL through off-target engagement with tyrosine kinases.

Weaknesses:

One of the stated benefits of PISA compared to the TPP in the original publication (Gaetani et al 2019) was that the reduced number of samples required allows more replicate experiments to be performed. Despite this, the authors of this study performed only duplicate experiments. They acknowledge this precludes use of frequentist statistical tests to identify significant changes in protein stability. Instead, they apply an 'empirically derived framework' in which they apply two thresholds to the fold change vs DMSO: absolute z-score (calculated from all compounds for a protein) > 3.5 and absolute log2 fold-change > 0.2. They state that the fold-change threshold was necessary to exclude non-specific interactors. While the thresholds appear relatively stringent, this approach will likely reduce the robustness of their findings in comparison to an experimental design incorporating more replicates. Firstly, the magnitude of the effect size should not be taken as a proxy for the importance of the effect. They acknowledge this and demonstrate it using their own data for PIK3CB and p38α inhibitors (Figure 2B-C). They have thus likely missed many small, but biological relevant changes in thermal stability due to the fold-change threshold. Secondly, this approach relies upon the fold-changes between DMSO and compound for each protein being comparable, despite them being drawn from samples spread across 16 TMT multiplexes. Each multiplex necessitates a separate MS run and the quantification of a distinct set of peptides, from which the protein-level abundances are estimated. Thus, it is unlikely the fold-changes for unaffected proteins are drawn from the same distribution, which is an unstated assumption of their thresholding approach. The authors could alleviate the second concern by demonstrating that there is very little or no batch effect across the TMT multiplexes. However, the first concern would remain. The limitations of their approach could have been avoided with more replicates and use of an appropriate statistical test. It would be helpful if the authors could clarify if any of the missed targets passed the z-score threshold but fell below the fold-change threshold.

The authors use a single, high, concentration of 10uM for all compounds. Given that many of the compounds may have low nM IC50s, this concentration could be orders of magnitude above the one at which they inhibit their target. This makes it difficult to assess the relevance of the off-target effects identified to clinical applications of the compounds or biological experiments. The authors acknowledge this and use ranges of concentrations for follow-up studies (e.g. Figure 2E-F). Nonetheless, this weakness is present for the vast bulk of the data presented.

Aims achieved, impact and utility:

The authors have achieved their main aim of presenting a workflow which serves to demonstrate the potential value of this approach. However, by using a single high dose of each compound and failing to adequately replicate their experiments and instead applying heuristic thresholds, they have limited the impact of their findings. Their results will be a useful resource for researchers wishing to explore potential off-target interactions and/or mechanisms of action for these 96 compounds but are expected to be superseded by more robust datasets in the near future. The most valuable aspect of the study is the demonstration that combining live cell and whole cell lysate PISA assays across multiple related compounds can help to elucidate the mechanisms of action.
