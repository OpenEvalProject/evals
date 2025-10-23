# Author response - Round 1

Authors:
- Prashant Rajbhandari
- Douglas Arneson
- Sydney K Hart
- In Sook Ahn
- Graciel Diamante
- Luis C Santos
- Nima Zaghari
- An-Chieh Feng
- Brandon J Thomas
- Laurent Vergnes
- Stephen D Lee
- Abha K Rajbhandari
- Karen Reue
- Stephen T Smale
- Xia Yang
- Peter Tontonoz ([ORCID: 0000-0003-1259-0477](https://orcid.org/0000-0003-1259-0477))

## Response text

DOI: [10.7554/eLife.49501.021](https://doi.org/10.7554/eLife.49501.021)

The reviewers all agree that your work addresses an important issue, and that the manuscript advances our understanding of the role of IL10 and its receptor in adipose biology and systemic metabolism. Your nuclei scSeq method indicates substantial adipocyte heterogeneity, a most interesting observation that will be of importance to the field. However, prior to publication, a few substantive issues need clarification:

1) Has the food intake of the IL10Rα KO mice and calorie excretion been taken into account? Is it possible that much of the phenotype of these animals is simply weight loss due to less caloric input (either less intake or less retention through the gut)?

Food consumption was not different between the genotypes. This data is included in Figure 1—figure supplement 1.

2) Analysis of an important control strain mouse carrying the adiponectin-Cre driver but Il10rα-/- rather than IL10rαFL/FL is lacking. There are many instances of Cre drivers having toxic effects in particular cell types. Feyerabend et al. Immunity 2011 is one example. Perhaps this issue can be raised as a caveat and/or citing some other study's performance of this control with the same Cre driver line.

As suggested, we have referenced studies using these control mice. It would not be feasible for us to repeat studies with an additional control strain within the time frame of an eLife revision.

3) CD36 and FABP4 are also expressed in SVF, and adipocytes are sticky-how do we know these are really adipocyte populations? It is by now standard in the field to provide some independent validation of clusters defined by scRNA-seq as tSNE plots are rather artistic and vary according to chosen parameters. One approach is to use a completely different scRNA-seq platform on a replicate cohort. Immuno-histochemistry of whole adipose tissue mounts would also work, The authors should at least confirm major findings concerning population 9.

Thank you for this suggestion. We have confirmed single cell transcriptomics from Cluster 9 using RNAScope in situ hybridization (FISH) from iWAT of saline or CL treated mice (new Figure 4F). This data directly confirms the existence and co-expression of thermogenic genes in cluster 9.

To address possible SVF contamination, we cross-matched SVF and adipocyte single cell/nuclei data (new Figure 3—figure supplement 1). A Fisher’s exact test was conducted between pairwise sets of cell type marker genes (determined by adjusted p-value < 0.05) to find cell types which had significant overlaps in their marker genes denoting transcriptional similarity. Cell types from both mature adipocyte nuclei and SVF single cells were used in this analysis and they were grouped using hierarchical clustering with tiles colored by -Log10 Bonferroni adjusted p-values. Adjusted p-values were thresholded to aid in visualization with values less than 10-5 set to 10-5. We did not find high degree of transcriptional similarity between SVF and adipocyte clusters (top). However, under stringent p-value adjustment, the transcriptomic state of adipocyte clusters 12 and 14 correlated with markers of adaptative immune cells (bottom). Thus, we cannot exclude the possibility that clusters 12 and 14 may be contaminated with immune cells.
