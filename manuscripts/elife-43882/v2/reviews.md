# Peer review - Round 1

Editors:
- Edward Morrisey, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.43882.060](https://doi.org/10.7554/eLife.43882.060)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Single-cell expression profiling reveals dynamic flux of cardiac stromal, vascular and immune cells in health and injury" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Harry Dietz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All of the reviewers as well as the editor believe that your study has merit. The reviewers felt that a better synopsis of the informatic analysis that would both simplify and better illustrate the findings would be beneficial to the report. There were also multiple instances where additional data including gene/protein expression, positional information of cell types identified, and confirmation of gene expression differences reported in the scRNA-seq analysis are required. Additional textual revisions are also requested and outlined below.

Reviewer #1:

The authors report on a new fibroblast type/state which is enriched for Wnt inhibition through increased expression of Wnt inhibitors, in particular Wif1. While the data is undoubtedly important and useful for the cardiac repair field, there are several notable issues that limit the impact of this report.

1) The data analysis as presented is confusing and does not lend itself to easy interpretation. If one of the main points to focus on is the Wntx cell type/state, then this should be much more clearly presented in the figures. This should include a clear assessment by GO category or other statistically significant methods to show that this cell cluster is enriched in expression of Wnt inhibitors.

2) In relation to point 1, if the Wntx cell type is enriched in expression of secreted Wnt inhibitors, then these cells could act on a neighboring cell type rather than in a cell autonomous manner. The authors should provide data on whether the Wntx cell is located in any specific relationship to other cardiac cells types. The current data in Figure 5 are at too low a resolution to define cell-cell relationships as Wif1 could be acting at short range.

3) A weakness of these studies is that there is no clear integration across the 3 different time frames examined i.e. 0, 3, and 7 days. To assess true relationships and how cells change after injury, a pseudotime analysis combining the 3 times points could help define what basal homeostatic fibroblast population gives rise to the Wntx and other cell types found at days 3 and 7.

Reviewer #2:

This is a well-written paper that concentrates on delineating the distinct immune and fibrotic signatures present in the acute and reparative phases post cardiac injury. The data presented here give insight into the different subtypes of immune and fibrotic cells in the heart, which have otherwise been hard to identify in bulk cellular and transcriptomic studies. Although this is a largely descriptive study, it provides a wealth of information that will be useful in the future to garner mechanistic insights into the signaling networks involved during cardiac injury and repair.

1) The authors mention the presence of a small percentage of hybrid endothelial cells which display both endothelial and fibroblast markers. To exclude the possibility that this population arises due to captured cell doublets, the authors should perform co-immunostaining for these markers to determine if this intermediate cell type exists in the heart. Immunostaining will also provide important spatial information regarding the location of this cell type in the heart.

2) Similarly, the authors mention that a significant proportion of the M2-macrophage population expressed endothelial markers, suggesting their ability to transdifferentiate into endothelial cells. This conclusion would also be more compelling if coupled with some spatial information. Are these cells prevalent in the areas near the site of injury?

3) In the differential proportion analysis in Figure 1E, the authors should indicate the changes in the total fibroblast population along with the subtypes already shown. There appears to be a significant decrease in the F-SH and F-SL populations at MI-day3 and this not very clearly indicated. In the latter half of the paper, the authors attribute this to the conversion of these fibroblast types to F-Act. However, the FACS data presented in the supplement do not entirely support this conclusion. This should be addressed.

4) Parts of the Discussion section simply reiterate the results. It might be more useful if the provided a more in-depth discussion regarding the implications of the different immune signatures observed post injury in the context of the known literature.

5) The authors need to cite and discuss in some detail the recently published, related findings of Epelman and coworkers "Self-renewing resident cardiac macrophages limit adverse remodeling following myocardial infarction" Nature Immunology 20, 29-39 (2019).

Reviewer #3:

The authors have performed an interesting single cell RNA-seq using the widely used 10X platform on adult ventricular murine cardiac tissue with or without myocardial infarction (MI). The authors focused their study on non-cardiomyocytes (TIP cells) with an emphasis on the fibroblast lineage. Moreover, they extensively describe a population of fibroblasts that express high levels of Wnt signaling-associated transcripts like Wif1.

Overall, while the work is very solid and interesting, it would be improved by further validation experiments and functional data to support the profiling data, which is predictive. The data analysis is of good quality, however, there are several technical issues as discussed below.

1) The authors include and present what appear to be obvious cell doublets in their final data set as EC-L1, EC-L2, and F-EC clusters (Figure 1). Doublets are expected on the 10X platform at a certain percentage which can be as high as ~5%, depending on the number of cells loaded. Without validation, these clusters that are suspected to be doublets should be removed and information regarding their identities and reasons for removal be added to the Materials and methods section. Moreover, the M2MΦ cluster which "expressed canonical endothelial markers" is partly composed of MΦ-endothelial cell doublets. This is obvious given that the endothelial-like "~29%" separates clearly from the main myeloid cluster (Figure 1D). The clustering parameter therefore is inadequate and unable to separate this issue and should be corrected. Finally, suggestions of a connection to trans-differentiation of myeloid cells into the endothelial cells and the contributions of embryonic EMPs to cardiac vessels should be removed from the manuscript to avoid confusion or more experimental data must be presented.

2) Based on the methods described in this study, it is unclear why epicardial and endocardial cells were not detected in the analysis shown in Figure 1. Even single nucleus RNA-seq studies, which are much less powerful, can detect these rare cell types in the heart (Hu et al., 2018). Please clarify in the writing.

3) The authors use the M1 and M2 classifications of macrophages and monocytes throughout their manuscript. Recent publications (that have been accurately referenced in the manuscript) have detailed the transcriptional responses of myeloid cells after MI (King et al., 2017) and after ischemia-reperfusion (IR) injury (Bajpai et al., 2018) using high throughput single cell RNA-sequencing. The authors should consider using nomenclature conventions more consistent with these previous reports.

4) Results from ligand-receptor analysis would greatly benefit from validation at the protein level.

5) It is unclear why the authors performed additional scRNA-seq on Pdgfra lineage cells, and what information was gained from these experiments. Please clarify in the writing. Similarly, what were the findings from the Fluidigm scRNA-seq experiments? Did they differ from or confirm the droplet-based scRNA-seq results? Please clarify in the writing.

6) It is unclear if the authors are claiming that the F-SH cells, which they additionally denote as CFU-Fs are cardiac mesenchymal stem cells (MSCs)? This section of the Results needs to be more clearly written.

7) In Figure 5, no strong evidence is provided that the indicated images are in the borderzone. Please clarify.
