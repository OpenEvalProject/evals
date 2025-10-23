# Author response - Round 1

Authors:
- Andrea Santeford ([ORCID: 0000-0002-7691-6213](https://orcid.org/0000-0002-7691-6213))
- Aaron Y Lee
- Abdoulaye Sene
- Lynn M Hassman
- Alexey A Sergushichev
- Ekaterina Loginicheva
- Maxim N Artyomov
- Philip A Ruzycki
- Rajendra S Apte ([ORCID: 0000-0003-2281-2336](https://orcid.org/0000-0003-2281-2336))

## Response text

DOI: [10.7554/eLife.66703.sa2](https://doi.org/10.7554/eLife.66703.sa2)

Essential revisions:

1) The authors use a type of "elicited" macrophages, Thioglycollate-elicited macrophages (TGEMs), which do not represent a naive state, but an activated/recruited state. However, this information is only included in the material and methods, and not discussed in the rest of the manuscript. Since this could have a great impact on the results, the three reviewers agreed that it is essential that authors explicitly address the use of TGEMs, (even if only textually), including in the title, abstract and main text, to make sure that the narrower scope of findings is clear to readers without needing to read the material and methods. If possible (maybe for future studies), similar analyses of other macrophage types would help understand the general relevance of the finding on the impact of miR-146b on inflamm-aging.

Use of Thioglycollate-elicited macrophages (TGEMs) has been has been explicitly highlighted throughout the manuscript, and we have included this detail in the revised manuscript title.

2) Since the authors opted for an adherence-only method of purification for the TGEMs, it is crucial that some measurement of the purity of the macrophage population be provided to make sure that the purity of TGEMs by adherence is not affected by aging. An F4/80 and Cd11b flow cytometry staining on cells purified similarly from the same ages and sexes would be the ideal method for this.

In our previous studies, we have established that aging does not affect the purity of the TGEM population selected by adherence (Lin JB, Sene A, Santeford A, et al. Oxysterol Signatures Distinguish Age-Related Macular Degeneration from Physiologic Aging. EBioMedicine. 2018;32:9-20. doi:10.1016/j.ebiom.2018.05.035). Using a flow cytometry approach, as was also suggested by reviewers here, we harvested TGEMs from female C57Bl/6 mice at approximately 3 and 18 months of age and stained for macrophage markers F4/80 (clone BM8) and CD64 (clone x54-5/7.1). We acquired data on a BD LSR II flow cytometer and used FlowJo v10 software to visualize and analyze data. No difference in the macrophage population was noted with either marker, and the overall percentages of cells positive for both macrophage markers (and therefore identified as macrophages) was consistently 94-96% in both old and young. Author response image 1 contains representative dot plots from TGEM samples from a young and an old mouse, each gated for live single cells and double positive for F4/80 and CD64, as well as normalized univariate histogram displays for each marker.

3) The authors need to carefully edit the manuscript to include all relevant and necessary methodological details (e.g. sex of used mice in general and by panel, a systematic clarification of the use of technical vs. biological replicates, etc.). The authors also should refer to the individual reviewer comments for the points needed clarification in the revised manuscript on this point.

Methodological details, including clarification of mouse sexes and ages and use of biological vs. technical replicates, have been extensively added throughout the manuscript for each experiment. This includes the Methods section as well as main text and figure legends.

4) Generally, the authors need to improve and amend their statistical analyses. This includes (i) providing more information on the analysis leading to only miR-146b (since referees note that other miRs look significant in the analysis), (ii) removal of all t-tests since there is no power to test for data normality, removal of statistical tests when the authors only have n = 2, etc.

We have added additional rationale regarding our identification of and focus on miR-146b, and acknowledged that other miRs were identified whose expression may change with mouse age and possibly warrant future investigation. In particular, reviewers noted that miR-15a levels represented in heatmap format in Supplemental Figure 1A look similar to those of miR-146b. Indeed, in this graphical representation pattern coloring does appear similar, particularly in small format. However, when we look directly at the numerical expression data, we can see that the decrease in expression from 3 months to 30 months in not unidirectional, as was seen with miR-146b and that may be expected as a result of the natural aging process. In fact, miR-15a expression actually increases by more than 10% between two separate consecutive time points (12 months to 18 months and 24 months to 30 months, respectively), thereby failing our criterion threshold.

We have also presented experiments throughout the manuscript that include a greater number of replicates, when possible, and amended our statistical analyses of all experiments in accordance with the recommendation to remove all t-test. For instances when comparison between two groups is necessary, we have utilized the non-parametric Mann-Whitney U-test. In addition, for discussion of cytokine gene expression in Figures 2C and F, we removed statistical analysis and referred only to trends in the data, while also providing additional data points from independent experiments.

5) Finally, potentially contradictory findings between figures need to be reconciled or explicitly discussed by the authors. (e.g. Reviewer #2 point 4)

We have amended the text to address the contradictory findings noted by the reviewers. Namely, we have addressed the discrepancy between in vitro knockdown and in vivo knockout of miR-146b in regards to cytokine gene expression levels. One potential explain of the differential patterns that we observed may be caused by the dramatic long-term (life-long) absence of miR-146b in conditional knockout macrophages vs. the short-term, partial reduction achieved through in vitro transfection.

We have also expanded our discussion of Lyz1 data obtained through bulk RNA-seq and scRNA-seq. Lyz1 was found to be the only gene significantly increasing as a result of miR-146b deletion in TGEMs in our bulk RNAseq analysis. Deeper analysis using scRNA-seq also found this target to be increased across all clusters between miR-146b and littermate controls at both young (3 months old) and old (17 months old) time points. However, as noted by Reviewer #2, we did not observe an increase in Lyz1 when comparing old control TGEMs to young controls. As we have established that miR-146b expression is decreased with age in TGEMs, one may anticipate that expression of Lyz1 should thereby increase. An important consideration is that the natural aging process leads to a slow and steady decline of miR-146b, though not a full obliteration of expression, whereas TGEMs from our conditional knockout mouse model show a persistent, near complete miR-146b loss. The continued expression of miR-146b, though lesser with age, in control/wildtype TGEMs may either be enough to continue regulating Lyz1 and/or the slow decline in miR146b with aging may allow for additional, indirect compensatory regulation through other targets. These data illustrate in our opinion an important point about macrophage aging.

Reviewer #1:

1) Methodological details need to be included or revised for consistency reproducibility.

a. Please include a table with the sequences of all used qPCR and genotyping primers.

The list of qPCR probe sets and manufacturer ID/catalogue number has been presented in lieu of specific sequences. Each of the products used within this manuscript are commercially available. The manufacturers from which we obtained Taqman probes (Life Technologies) or LNA primers (Qiagen) do not disclose specific product sequences. However, utilizing the provided manufacturer assay IDs will allow other investigators to easily find these products should they choose to replicate these studies in their own hands.

All genotyping PCR sequences are presented in Supplemental Table 2 and the Key Resources table.

b. Some analyses are performed on the mm9 mouse genome build (e.g. small RNA-seq seq, line 449) and some on the mm10 genome build (e.g. RNA-seq of KO TGEMs line 591). Since this could lead to differences in results, please harmonize analyses so they are all performed on the same genomic build.

c. Please include all code/scripts used for the analysis in a supplementary document or deposit them to a Github repository as per the journal policy.

References to GitHub depository have been moved to the Data Availability section for greater visibility and included in the Key Resources table.

Reviewer #2:

1. The cytokine panel in Figure 2C (miR-146b knockdown) does not include some cytokines in 2F (miR-146b knockout) – were they measured? Also, please comment on the Mmp9 expression, which is decreased in 2C but increased in 2F.

In adding additional samples to our analyses, we have amended the list of cytokines to include targets measured for both knockdown and knockout, including some targets that may not be significantly changed. We have discussed any discrepancies within the text and noted possible rationale for differences noted in transgenic knockout vs. in vitro knockdown scenarios.

2. It would strengthen the paper if the levels of secreted cytokines (proteins) upon loss of miR-146b were measured.

We agree that protein levels often provide interesting insight to a cell’s biology. Our previous studies have shown that gene expression data provides a strong picture of the cell’s status. As our experiments did not utilize additional activators, such as INFγ + LPS or IL4, the greater sensitivity of qPCR over protein assays like ELISAs is capable of more accurately measuring differences here at baseline that may be otherwise less-reliably detectable due to the experimental limits of protein measuring.

3. In figure 3, the authors overexpress miR-146b and show increased mitochondrial respiration. Does this also alter the expression of cytokines measured in Figure 2?

The effects of miR-146b overexpression on TGEM cytokine or mitochondria-related gene expression have not yet been examined. These are interesting questions which certainly warrant follow-up studies, with both in vitro and possibly mouse models.

4. The miR-146b-dependent metabolic shift may result from alterations of multiple metabolic pathways that consequently affect OCR/ECAR, such as glucose metabolism. Were there metabolic genes that changed in the RNA-seq? If so, is/were there a coherent metabolic pathway(s) that is/are highlighted? If possible, quantifying metabolites that are highly relevant to macrophage function would provide further insight.

RNA-seq revealed statistically significant decreases in several genes involved in mitochondrial morphology and respiration, as noted in lines 342-3. However, no one pathway in particular seems to be targeted, though pathway analysis without a large number of genes can be limiting. Metabolomics analysis is great idea for future follow up studies, but is beyond the scope of the current project.

5. Are the cytokines measured in Figure 2 reflected in the scRNA-seq of Lyz2; miR-146bM-/M- mice?

Most of the cytokines measured in Figure 2 do appear in the scRNA-seq data set, as shown in Author response image 3. As many of the reads are scant, however, it is difficult to make broad assumptions regarding these targets in this context. For this reason, we did not include the data within the manuscript.

6. As the authors state, peritoneal macrophages consist of a heterogeneous population of resident and recruited (monocyte-derived) macrophages. Further, monocyte-derived macrophages may not display age-dependent loss of miR-146b (Figure 1C). The authors may want to add some discussion on the potentially differential role of resident vs recruited macrophages in inflammaging. Further, have the authors tried to compare resident vs recruited macrophages in the scRNA-seq on peritoneal macrophages in addition to the 3 clusters (it is not clear whether the largest cluster 1 is a mix of both populations)?

BMDMs indeed exhibit age-related loss of miR-146b, though perhaps not as dramatically as noted in TGEMs. The levels of miR-146b even in BMDMs from young mice however is only ~30% that of TGEMs from age-matched mice. In the scRNA-seq, the majority of cells expressing markers or resident peritoneal macs map to cluster 2. However, the vast majority of cells map to cluster 1, as noted in Supplemental B, and as such would be anticipated to contribute most to the phenotypes we observed.

Reviewer #3:

1) Figure 1A, please clarify the units on the Y axis.

Y axis units of Figure 1A have been amended to “Normalized Expression (RPM)”. Units represent the normalized expression value of reads per million mapped to the mouse genome.

2) Typo pg 5, line 86, add space between number and months.

Spacing between number and months has been added to p5 line 86.

3) Figure 4D, clearly label what are resident vs non-resident markers.

Labels have been added to Figure 4D indicating resident vs recruited markers.

4) Figure 4A and 4E, please list the genes in the same order and provide the same genes in each experiment.

Gene listings for Figures 4A and 4E have been harmonized to list genes in the same order.

5) Figure 4F, please label on graph what each Pattern represents, clearly state genes in each Pattern and if possible show data for each gene in supplemental space.

For Figure 4F, the main text and figure legend has been expanded to more clearly explain that each row represents the mean z score for that hierarchically defined cluster of genes from the heatmap in Supplemental Figure 3. This was used to convey the various expression patterns across our four samples, and to interpret the GO categories and functions of the groups of genes with these patterns. All genes from Patterns a-e are noted in Supplemental Figure 3, along with their individual expression patterns across each sample, as well as listed Supplemental Table 1 for additional clarity.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

The reviewers have discussed your revised submission, and found that crucial issues had not been addressed, as outlined below:

1. The purity panel needs to be more than n = 1 per age, and should be included in the manuscript, not just in the rebuttal letter. All reviewers were disappointed that this major point was not satisfactorily addressed.

2. In general, the authors should address all previous concerns raised in the first round of reviews that were not addressed, including:

– a number of the methodological points we raised (for instance the mix and match approach on genome reference usage mm9/mm10) are not at all addressed, not even textually in the revised manuscript.

– regarding the uniqueness of the miR-146B pattern, reviewers are not convinced. For instance, the authors do not attempt to look at other micro RNAs as controls to test their hypothesis that miR-146B is the only micro RNA whose expression is regulated during aging.

– information about biological vs. technical replication is still lacking in the revised manuscript.

1. We have included flow cytometry analysis of both young (3 month old, n=5 biological replicates/individual mice) and old (20+ month old, n=5 biological replicates/individual mice) TGEMs using the macrophage markers CD11b and F4/80 to validate the purity of the macrophage population utilizing the adherence selection method employed throughout this study. Approximately 95% of all cells, in both young and old samples, were double positive for both markers, indicating not only a high level of macrophage purity, but also demonstrating that there is no purity difference due to age. This data has been included as Figure 1—figure supplement 1 and Figure 1—figure supplement 1 source data. Dr. Lynn Hassman contributed to this effort and has been included as an author on the revised manuscript.

2. We have evaluated the miRNA expression patterns for a number of additional miRNAs in TGEMs. Here we further investigated microRNAs identified in our original dataset to have overall decreased expression with age, but which were not noted to decline in quite the linear fashion with each age point, we observed Mir146b. Based on values from our original small RNA-seq, we have evaluated the expression of Mir15a, Mir22, Mir423, Mir29a, Mir146a, and Mir18a along with Mir146b. We also attempted to analyze Mir362, but found its expression below the limit of detection for nearly half of our samples, regardless of age, and therefore did not include it in this manuscript. While our original experiment was able to utilize mice as old as 30 months of age, 20 month old mice is the oldest time point that we are able to presently acquire. We have noted this caveat within the manuscript. This new validation using mice using 7-9 individual mice at 3, 12, and 20 months of age again demonstrated decline in Mir146b from 3 to 20 months. In addition, Mir22 was observed to decline between these time points as well. Our RNA-seq data indicates that while there may be decreases in expression between 3 and 18-24 months, expression may actually increase again from 24-30 months. We have included the graph of normalized expression values for Mir22 obtained from our small RNA-seq data, but we cannot presently validate this potential increase in TGEMs from 30 month mice, and as such, do not comment on this pattern within the manuscript. We do however note that the level of reads for Mir146b is more than 3 fold higher than that of Mir22, keeping Mir146b an attractive target for our study, but also note the need for future studies of Mir22 in the aging macrophage.

3. We have explicitly highlighted and discussed that our original small RNA-seq data, which helped us to identify Mir146b as a microRNA of interest, was aligned to the mm9 version of the mouse genome. We understand that re-analysis of the data using a newer version may reveal different patterns of expression for some miRNAs, revealing additional miRNAs of interesting in aging. However, due to the changes in raw data file types and programs that have occurred in the time period since this data was originally procured, conversion has been technically challenging at this point, and as such we are currently unable to realign these files. Importantly though, our qPCR of miRNA expression and additional experiments validates our initial findings from this RNAseq data set—Mir146b progressively declines with aging in murine TGEMs.

4. We have reviewed details in both the manuscript body as well as figure legends to ensure that we have explicitly indicated the use of biological vs technical replicates of each experiment and added additional methodological details within both the results and Materials and methods sections as well as in the figure legends.

5. Use of Thioglycollate-elicited macrophages (TGEMs) has been has been explicitly highlighted throughout the manuscript, and we have included this detail in the revised manuscript title.

6. We have presented experiments throughout the manuscript that include a greater number of replicates, when possible, and amended our statistical analyses of all experiments in accordance with the recommendation to remove all t-test. For instances when comparison between two groups is necessary, we have utilized the non-parametric Mann-Whitney U-test. In addition, for discussion of cytokine gene expression in Figures 2C and F, we removed statistical analysis and referred only to trends in the data, while also providing additional data points from independent experiments.

7. We have amended the text to address the contradictory findings noted by the reviewers. Namely, we have addressed the discrepancy between in vitro knockdown and in vivo knockout of miR-146b in regards to cytokine gene expression levels. One potential explain of the differential patterns that we observed may be caused by the dramatic long-term (life-long) absence of miR-146b in conditional knockout macrophages vs. the short-term, partial reduction achieved through in vitro transfection.

We have also expanded our discussion of Lyz1 data obtained through bulk RNA-seq and scRNA-seq. Lyz1 was found to be the only gene significantly increasing as a result of miR-146b deletion in TGEMs in our bulk RNAseq analysis. Deeper analysis using scRNA-seq also found this target to be increased across all clusters between miR-146b and littermate controls at both young (3 months old) and old (17 months old) time points. However, as noted by Reviewer #2, we did not observe an increase in Lyz1 when comparing old control TGEMs to young controls. As we have established that miR-146b expression is decreased with age in TGEMs, one may anticipate that expression of Lyz1 should thereby increase. An important consideration is that the natural aging process leads to a slow and steady decline of miR-146b, though not a full obliteration of expression, whereas TGEMs from our conditional knockout mouse model show a persistent, near complete miR-146b loss. The continued expression of miR-146b, though lesser with age, in control/wildtype TGEMs may either be enough to continue regulating Lyz1 and/or the slow decline in miR146b with aging may allow for additional, indirect compensatory regulation through other targets. These data illustrate in our opinion an important point about macrophage aging.
