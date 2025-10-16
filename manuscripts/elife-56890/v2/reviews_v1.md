# Peer review - Round 1

Editors:
- Emma L Rawlins, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56890.sa1](https://doi.org/10.7554/eLife.56890.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work provides a comprehensive bioinformatic view of the immune cell landscape of the developing mouse lung at an important biological transition from in utero to the neonatal air-breathing period. The data are coupled with well-quantified spatial analysis of some of the most dynamic cell types identified in the analysis. They are also presented clearly in the context of analogous recent studies and provide a biological overview of immune cell evolution in mouse lung perinatal development.

Decision letter after peer review:

Thank you for submitting your article "Diverse homeostatic and immunomodulatory roles of immune cells in the developing mouse lung at single cell resolution" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Tadatsugu Taniguchi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

The present study by Domingo-Gonzales et al. is a comprehensive bioinformatic approach, in which they investigate immune cells in the lung perinatally by characterizing changes in composition, localization, and function before birth and through the first three weeks of life. To this end, they combined a transcriptomic analysis (single cell RNA-seq) with fluorescent in situ hybridization. They clearly identified and characterized the localization and dynamics of five macrophage/monocyte populations with very distinct functions in murine lungs. Moreover, they provide strong data on the abundance and distribution of other important immune cells (e.g. dendritic cells) that are central in lung developmental processes, but also in lung diseases. Overall the manuscript is very well written addressing an highly important and disease-relevant topic that has not been elucidated to this extent yet.

Essential revisions:

These can all be done without additional experiments.

1) The quality of the spatial information describing the location of the macrophages/monocytes needs to be improved. A detailed quantification of the in situ hybridisation images is required for clarifying the distribution of perivascular macrophage/monocytes in the tissues e.g. in Figure 2E, F all Cd68+ cells should be scored as Dab2+, Plac8+, both, or neither. In Figure 3 the % macrophages around the vessels versus scattered should be given, the relative % of type 1 versus IV around the vessels and the % of co-labelling with Mki67. Moreover, clarification of the structures seen in Figure 3 would be helpful – are the macrophages arranged in intermittent circles around the diameter of the vessels? Are they forming lines along their length (if so, from where to where)? If possible, an antibody-based immunofluorescence approach to improve the cellular resolution of the image data would be desirable.

2) The data in Figure 4A and the respective tables are very interesting, providing new insight in the functional role of the macrophages. Pathway analysis using these respective genes in the supplementary tables would give more information of the pathways and functional regulation of the individual macrophage types.

3) Figure 3 and Figure 4 suggest that some macrophage population, e.g. Mac I, might regulate and promote angiogenesis in the lung. These findings coupled with Figure 4 showing genes related to angiogenesis let me query if anti-angiogenic factors might be produced by specific macrophages. That might be of interest in regulating alveolarization, but also in the pathogenesis of lung diseases (PAH or BPD).

4) Did the authors relate macrophages or other immune cells, such as dendritic cells or B cells, to the regulation of stemness or lung progenitor cells? They are crucial in the process of alveolarization.

5) We recommend including Fc receptor data in the main manuscript. They are important in disease development and often a therapeutic target.

6) How do the present mouse data relate to human lung? At birth, murine lungs are in the saccular stage, whereas human lungs are already at the alveolar stage. What might be the main driver of macrophage differentiation: oxygen? mechanical forces? That could be further addressed in the Discussion.

7) Discussion: It would be interesting to discuss more in detail how this precise regulation of immune cell differentiation and distribution in the lung during development could underlie the origins of lung disease. For example, there are data showing that BPD is related to activation of macrophages. Could asthma originate from adverse effects on dendritic and T cells during a critical phase of differentiation? That could be discussed.

8) To make this manuscript more useful to the community further details need to be provided about the bioinformatic analysis:

a) The authors should state exactly how many cells in total were profiled and how many cells passed QC. It will be useful as part of QC metric to see the number of genes per cell state identified.

b) The link to scripts, gene count and metadata table provided in the manuscript was inactive.

c) The authors should state what is actually displayed as gene expression for all figures – is this expression value on log scale? What does min, mod, high e.g. Figure 4A refer to quantitatively?

d) Smart-seq2 is less likely to have doublet contamination but it is not clear if doublet detection and removal during analysis was attempted.

e) Was batch correction methods e.g. Harmony implemented? – this would be helpful to assess if findings were impacted by batch effects.

f) The observation of Mac I that encircles blood vessels prenatally and disappears after birth is interesting. However, the claims based on using inferred trajectory analysis of scRNA-seq data to suggest Mac I transition into Mac II and III needs to be more cautiously made as definitive lineage tracing or fate-mapping experiments were not done to validate the trajectory inference.

g) What pseudotime trajectory method was used?

9) DC nomenclature may be confusing as DC1, DC2 and DC3 are recognised subsets of conventional DCs. DCII described by authors are monocyte-derived DC and DCIII identity is unclear. This should be clarified in the text.

10) Some integration of this dataset with other existing datasets from embryonic, perinatal and adult immune cells would permit harmonization of the cell states described by the various manuscripts and enhancing the value of this manuscript from a biological advancement and resource value of the manuscript.
