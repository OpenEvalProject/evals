# Peer review - Round 1

Editors:
- Neil A Hanley, University of Manchester , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27564.023](https://doi.org/10.7554/eLife.27564.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Reconstructing human pancreatic organogenesis by mapping specific cell populations during development" for consideration by eLife. Your article has been favorably evaluated by Mark McCarthy (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Susana Chuva de Sousa Lopes (Reviewer #2); Timo Otonkoski (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors have undertaken a cellular deconstruction of how the human pancreas develops by studying the expression dynamics of several surface markers between 7 and 12 weeks of development. There is particular focus on the insulin-producing β cells. The evolution of these cell populations was very dynamic during the developmental stages studied, demonstrating that endocrine cells arise in the population that down-regulates both ECAD and GP2 expression. Further refinement of the characterization was achieved by including the cell surface marker SUSD2. Finally, human pluripotent stem cells undergoing pancreatic differentiation were analysed by the same parameters, demonstrating that in vitro development followed the same principles identified in vivo.

Essential revisions:

The three referee reports are included as all raise important points that should be addressed (and would improve the manuscript). The major request focuses on more detailed analysis and reporting of existing data (and not the acquisition of new 'wet lab' data). While all individual points should to be addressed in a revised manuscript and / or the accompanying rebuttal letter, there are some common themes to the referee reports:

1) There is a need to improve the detail of the computational and statistical analyses. There would be benefit from incorporating existing datasets on other pancreatic cell-types into some of the analyses (as highlighted by reviewer 2). This would then assist in commenting on other endocrine cell-types (as requested by reviewer 3) and examining other important genes (PAX4 is mentioned by reviewer 1).

2) There is scope to include more information on specific genes, for instance underlying the GO terms, either as part of the figures or as additional supplementary tables.

3) All the data should be made freely available for download.

4) The Materials and methods need far more detail to enable others to follow the work.

Reviewer #1:

Thank you very much for letting me review this manuscript. The major novelty is in the cellular deconstruction of how a human organ (the pancreas) develops. This has not been undertaken before and is challenging for a solid organ (e.g. compared to the haematopoietic system). The data have direct translational benefit for stem cell researchers. I make comments to try and improve the manuscript.

1) Figure 1. The data imply that a considerable number, 45% if I interpret the data correctly in Figure 1E, of EpCAM+ cells either lack or (more likely) have lower levels of PDX1 and NKX6.1. These are then excluded from downstream analyses. The immunohistochemistry and text imply that all EpCAM+ cells possess PDX1, i.e. these cells are pancreatic progenitors. What do the authors think these cells EpCAM+ / low PDX1/low NKX6.1 cells are? How do these cells fit with the notion of NKX6.1 'low' cells as described by the authors in their recent Cell Reports paper, Ameri et al.? In that study on differentiating hPSCs, these cells were argued to be earlier stage pancreatic progenitors with higher levels of cell proliferation. Perhaps the authors could integrate their thoughts on this topic into the current manuscript?

2) At several places in the manuscript, there is mention of very precise timing, e.g. '7.4 WD'. What does this mean? How was such accuracy determined over and above 7WD or 8WD? Moreover, the authors described triplicate experiments: are these biological replicates at this very precise time point? Or technical replicates from a single human embryonic pancreas. The manuscript would benefit on full detail regarding human tissue use, perhaps as a supplementary table.

3) Computational analyses. A number of improvements should be made to allow others to gain maximum benefit from the data.a) For instance, in the subsection “GP2 and ECAD define 4 populations in the human fetal pancreatic epithelium that develop sequentially” (and elsewhere) (unless I missed it) it is not clear what cut-offs were applied to define particular genes as enriched. I don't think this detail was in the Materials and methods. b) The genes underlying all the GO terms should be listed, perhaps as a supplementary table as this would help the reader interpret the data. c) 'We correlated these signatures with RNAseq Single Cell data'. How were these correlations undertaken? d) The heatmaps in Figure 4 refer to very few genes. Why? And if selected, why were these particular genes chosen and (presumably) others overlooked?

4) Subsection “Acinar and endocrine functions segregate within the GP2 and ECAD populations”, end of first paragraph and elsewhere (e.g. subsection “CD142 and SUSD2 reveal heterogeneity within the GP2- and Elow populations during development”, last paragraph): I would encourage the authors to avoid 'data not shown'. Either include the data or remove the interpretation.

5) I did not follow the text in the last paragraph of the subsection “CD142 and SUSD2 reveal heterogeneity within the GP2- and Elow populations during development” referring to Figure 2—figure supplement 2A, B. This figure supplement does not detail SUSD2 or CD142?

6) The broad transcriptomics data are useful but at present only a limited number of key genes are discussed. Would it be possible to describe some additional key factors, some of which have been notoriously difficult to track down accurately in native human embryonic/fetal pancreas, such as PAX4? The precision with which the authors have picked apart human pancreatic differentiation should offer an opportunity to narrow down when PAX4 becomes expressed and in which precise cell-type.

7) Figure 6A-B. In the subsection “Endocrine progenitors develop in the GP2- CD142- SUSD2- subset and mature within the ElowSUSD2+ subset” the authors describe two different cell populations in which insulin is expressed in the earlier fetal pancreas at 8.6WD: an Elow/CD142-/SUSD2+ population but not in the Elow/CD142-/SUSD2- population; and then the converse in older fetal pancreas at 10-12WD, namely in the Elow/CD142-/SUSD2- population but now not in the Elow/CD142-/SUSD2+ population. At least to me, this is surprising as β cell differentiation operates over a window, i.e. β-cells are serially differentiating over time. Morphologically, there are differences-at the earlier time point β-cells tend to be scattered whereas at the later time point β-cells are more clustered. Therefore, my question is whether the authors have unearthed two distinct populations of β-cells?

Reviewer #2:

The authors have studied the expression dynamics of several surface markers in human pancreas from 7-12 weeks of development, mainly by FACS; and suggest an order of events during the differentiation of several lineages in the human pancreas.

1) The authors used single cell transcriptomics data from Segerstolpe et al. to generate Figure 3—figure supplement 1A, B, but I don't understand what values were used to generate the heatmap. I assume they used RPKM values, but the legend goes from -1 to 1, so I am confused. I suggest that figure is replaced by heatmaps for the selected genes showing all individual cells instead of using averages (?) and using RPKM values.

2) For robustness, the set of cells from Muraro et al., 2016, Cell Systems, 3:385 should also be included in two extra independent heatmaps in Figure 3—figure supplement 1A, B. The authors should also include not only acinar, ductal, α and β, but also the mesenchymal, δ, ε and pp cells.

3) The authors should use more than one HKG to normalize the QPCR results, the probes used are stable they could use bactin, HPRT and PPIA instead of just one of those (they already have the 3 probes in house).

4) The authors differentiate hPSCs into pancreas progenitors, but from the results it is unclear which of the 3 different lines mentioned were used and for what experiments. Can this be clarified in the Results and figures? Were the 3 lines used for the same experiments? And are the results comparable? In Figure 7: Could you specify what hPSCs were used for what experiments?

5) Discussion: you mention that culture of pancreatic cells have failed: could you be more specific about the reason for failure (cells don't attach; cells die; which conditions have you tried? What are the culture periods tried, etc.)?

6) The authors mention in the Discussion Ptf1, Cpa1 and cMyc as marking multipotent progenitors in mice. These genes were not analysed in the human data set. Were they expressed (and if yes, in what cells)? Could you include those genes in the heatmap in Figure 4B?

7) I don't understand what the samples with "statistical significance" in all QPCR graphs were compared to? Could you clarify that in the figures?

8) Figure 2A: the authors show the cells in the blue square stained with GP2 and ECAD. Could the authors also present the other 2 populations (in the two black squares) for the markers GP2 and ECAD? You should have that data acquired.

9) Figure 3A, C: If the authors want to present PCA in 3D, they have to provide lines projecting each dot into the lower area. The plots as presented are 2D…

Reviewer #3:

In this study Ramond et al. have aimed to understand the sequential development of epithelial cell populations in the human fetal pancreas, focusing particularly on the emergence of the insulin-producing β cells. For this purpose, they have identified cell surface markers that were used to sort the cell populations between developmental stages estimated to represent 7-12 weeks. They identify a CD45-CD31-EPCAM+ population that includes the pancreatic progenitors. This population was then found to contain 4 subpopulations based on the expression of GP2 and E-Cadherin. The evolution of these cell populations was very dynamic during the developmental stages studied, demonstrating that endocrine cells arise in the population that downregulates both ECAD and GP2 expression. Further refinement of the characterization was achieved by including the cell surface marker SUSD2. Finally, human pluripotent stem cells undergoing pancreatic differentiation were analysed by the same parameters, demonstrating that the in vitro development follows the same principles identified in vivo.

Overall, the study represents an impressive amount of flow cytometry analysis in human fetal pancreas, taking into account the scarcity of this research material. These results contribute to the understanding of human pancreatic development and provide surface markers that could be utilized to isolate bona fide pancreatic endocrine progenitors. The novelty of the study relies in the combined used of previously reported and novel surface marker to delimit the target cell population, both in human fetal pancreas samples and stem cell derived cells. However, the novelty is decreased by the recent report by the same investigators (Ameri et al., Cell Reports 2017) in which GP2 was characterized as a surface marker for pancreatic endocrine progenitors in the human fetal pancreas and hPSCs.

The value of the study would be increased by adding the following analyses:

1) Out of all endocrine cells, the analysis focuses only on β cells. In which populations do the other major endocrine cell populations reside? It would be interesting to see at which stage and in which population within the GP2- ECADlow SUSD2+ are other endocrine cell hormones than insulin expressed: is the GCG+ population in SUSD2+ or SUSD2-? What is the distribution of hormone+ endocrine cells in the single cell samples (6D and 6E)? Are there polyhormonal cells, as is often seen in hPSC differentiation?

2) In the fourth paragraph of the Discussion the authors describe the GP2+ cell population to represent the multipotent "tip" cells described in the mouse embryo to express PTF1a, Cpa1 and c-Myc. Are these markers expressed in the human GP2+ cells?

The quality of the presentation and the statistical analysis should be improved:

1) Many of the figures are difficult to interpret. In general, it would be advisable to present as much as possible of the results as the quantitative summary of all experiments (as in Figure 2D), and also include statistical comparison of the changes.

2) The immunofluorescent image in Figure 1B should be made larger and clearer.

3) The methods in general are only superficially described and there are no detailed supplementary methods.
