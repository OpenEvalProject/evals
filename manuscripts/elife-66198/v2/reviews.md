# Peer review - Round 1

Editors:
- C Daniela Robles-Espinoza, International Laboratory for Human Genome Research Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66198.sa1](https://doi.org/10.7554/eLife.66198.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript is of interest for researchers in the cancer genomics and telomere maintenance fields. Telomere maintenance is critical in tumour development as it allows cells to divide indefinitely. By studying a large collection of cell lines, the authors have identified genomic features broadly correlated with telomere content, including telomerase expression and mutation, as well as differences between tissues of origin, dependencies among different telomere maintenance genes, and correlations with region-specific methylation patterns. Overall, its value lies in the novel biological insights it provides regarding telomere maintenance and the massive resource it provides to the scientific community.

Decision letter after peer review:

Thank you for submitting your article "Integrated evaluation of telomerase activation and telomere maintenance across cancer cell lines" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including C Daniela Robles-Espinoza as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Maureen Murphy as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Floris Barthel (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

In this manuscript, Hu, Ghandi and Huang describe a number of genomic features that are correlated with telomere content, and focus on the study of cancer cell lines from two different sources (the Cancer Cell Line Encyclopedia, CCLE) and the Genomics of Drug Sensitivity in Cancer (GDSC). They describe genomic alterations, gene dependencies, telomerase (TERT) expression and promoter mutation, and methylation patterns both in the TERT locus and beyond. The study is impressive in scope, as putting together data from distinct cell lines from different batches and sources is not an easy task.

However, the reviewers have a number of suggestions to improve the conclusions and readability of the manuscript.

Essential revisions

1. About the structure of the manuscript.

Two reviewers commented that the manuscript is at times hard to understand due to it covering a large number of observations that not always follow logically from each other. Specifically, it was mentioned that the ATRX/DAXX section does not add much to the paper, and that a substantial part of analyses and supplementary data are not mentioned (e.g., What is CERES and DEMETER2 dependency, in Figure S6c and d?). Please re-check these issues, and if possible, simplify the paper to convey a clear message.

2. About cell lines.

Please answer the following questions.

a. Does the CCLE provide any information on cell line source? Do the authors have any cell lines with biological replicates from different sources that could determine how this affects telomere length, as in eg. PMID 30089904? Also, are there any technical replicates derived from unique libraries prepared from the same cell line to establish that these show similar measurements?

b. Do the authors think their conclusions are affected by the fact that cell lines are immortalised, and this process in many cases includes the activation of TERT? Can their conclusions be extended to living tissues?

c. Can the number of cell lines from both sets that were taken forward for downstream analyses be specified in the main text?

3. About telomere measurements and correlations.

a. The raw telomere content measurements from WGS are not discussed much and quickly discarded in favor of normalized estimates. Looking at the supplementary table these look to be all on a similar and comparable scale for WGS. It strikes me that WGS-based estimates are much more reliable, and some associations may be stronger using these numbers despite being limited to a much smaller sample size. Can the authors show the overlap between WGS/WXS and associated data (CRISPR screens, RNAseq, etc)? Do the described findings hold when limited to WGS raw estimates or is there insufficient power? Also, an explanation of why correlation is higher between WES and WGS of different datasets than with those of the same dataset would be welcome.

b. While the authors look at the patients age at tissue extraction and find a correlation between estimated telomere content and age, one wonders if cell culture specific parameters could not be even stronger determinants. Have the authors looked at time in culture, passage number and population doubling level (PDL) in relation to telomere length?

c. Could the authors infer ALT status for a large number of cell lines from other resources? Capital Biosciences was awarded NIH SBIR funding several years ago specifically to determine the ALT status of all cell lines in the ATCC.

See for example:

1. https://www.eposters.net/pdfs/identification-of-new-alternative-lengthening-of-telomeres-positive-cancer-cell-lines-using-the-c.pdf

2. https://www.atcc.org/~/media/PDFs/Presentations/HOC%20poster%20ALT.ashx

At a minimum, perhaps the authors could annotate lines known to exhibit ALT as ALT+ and others as ALT unknown?

d. It is slightly surprising there is a positive correlation between telomere content and TERT mRNA in CNS since CNS tumors are often ALT+ (and telomerase-). Possibly none of the CNS lines assayed were ALT+? Perhaps the correlation between TERT mRNA and telomere content needs to be adjusted for ALT status because of the presumed interaction. Could the authors incorporate multiple correlates of telomere content in a model and determine their independent contributions and interactions? Perhaps this could be limited to WGS and using the raw measurements.

e. Some correlations with TC (for example all Figure S3) are likely to be biased by the important TC differences between tissue types. Can the authors perform this analysis on each tissue separately, or normalize TC to use relative TC within a tissue type?

4. About figures.

a. Figure 1.

– This is an informative figure. Can a clarification of the total number of cell lines be added?

– It says it is 683 but from the main text it seems that many more were taken forward for analysis (1,056 GDSC with WES and 329 WGS CCLE, with only 286 overlapping)? Why are the others not depicted here?

– If the outlier U2-OS cell line is removed from the 44 bone cell lines, is the bone cell line average still the highest?

– Can the ATRX/DAXX expression be included?

b. Figure 2.

– Figure 2a-b: the authors claim that dependency toward TRF1 and the CST complex is higher in cells with short telomeres. However, they show a positive correlation between TC and AVANA dependency. This may be interpreted that cells with longer telomeres are more sensitive to loss of TRF1 or the CST complex. That could be explained by their role during telomere replication, and the likely higher replication stress at longer telomeres. If this is not the correct explanation, can the explanation be reworded, as it is confusing?

– Figure 2d-e: Does each dot represent a cell line? If so, are the conclusions (model in 2f) drawn out of only 1 cell with a mutation in a hotspot?

c. Figure 3a.

– Here, it seems that cells with lower PML expression are more sensitive to DAXX suppression. Could the analysis be done with telomerase positive cells only? Similarly, cells with higher levels of ZMYM3 are more sensitive to DAXX suppression. What does that mean biologically? Can you please specify what are the dots?, do they refer to cell lines? So these all represent the top score of their corresponding cell line?

5. Other points

a. The introduction and the narrative tell us that telomerase is activated, that telomeres are usually longer in cancer, etc. Therefore, the phrase "The 55 non-cancerous samples profiled as part of the GDSC also displayed relatively high telomere contents (P = 5.9×10-4, two sided Mann-Whitney U test), consistent with previous reports of widespread telomere shortening in cancer (Barthel et al., 2017)." seems to contradict what has been said. So, is it expected that the normal samples would have long telomeres? Would this be expected physiologically or is it an effect from these being cell lines? Also – is the information for these normal cell lines displayed in Figure 1? Reviewers recommend to add the normals to this figure so it is easier to compare between normal and cancer tissues.

b. Could the definition of what a dependency means, exactly, be included? Does it assess correlated gene expression? Does it assess activation of one gene upon knockout of the other? It would be helpful to spell this out in the main text. This may help understand the observed dependencies between the members of the shelterin complex and those of the CST complex.

c. Page 6 says "increased sensitivities to knockout of the CST complex components, which are key mediators of telomere capping and elongation termination (Chen et al., 2012), were correlated with lower telomere content." However, it seems that supplementary figure 3b indicates that the CST genes are positively correlated with telomere content? If this is an index of sensitivity, could this be indicated somewhere? (At the moment it seems similar to the TERT figure, so readers may read it in the same way which may be confusing). Could TERF1 be highlighted in Figure S3b please, DRIVE dependencies?

d. About methylation studies. In page 11 it says "TERTp mutants exhibited strong and significant (P < 0.01) increases in ASM (allele-specific CpG methylation) in the promoter (n = 485), remaining gene body (n = 493), and exon 1 (n = 478) regions", but then in page 12, line 292 it says "The observation that TERT promoter mutants display a hypomethylated TERT locus…" – does this not directly contradict the statement above? Or is it referring to methylation on a specific region? Could this be clarified please?

Reviewer #1:

In this manuscript, Hu, Ghandi and Huang describe a number of genomic features that are correlated with telomere content, and focus on the study of cancer cell lines from two different sources (the Cancer Cell Line Encyclopedia, CCLE) and the Genomics of Drug Sensitivity in Cancer (GDSC). They describe genomic alterations, gene dependencies, telomerase (TERT) expression and promoter mutation, and methylation patterns both in the TERT locus and beyond. The analyses are carefully done and largely convincing, and impressive in scope as putting together data from distinct cell lines from different batches and sources is not an easy task.

Their major claims are that:

– TERT expression correlates with telomere content in lung, central nervous system, and leukemia cell lines. This claim is supported by their analyses of telomere tract quantification and TERT mRNA levels in the same cell lines (Figure S4). However, some negative correlations in other cell lines were also found, which are currently unexplained.

– Lower telomeric content is associated with dependency of CST telomere maintenance components. This is supported by an analysis of the Avana dependency dataset, which has been previously published. This makes sense biologically and is clear in Figure S3.

– Increased dependencies of shelterin member genes are associated with wild-type TP53 status. An extended analysis as the one before in the Avana and DRIVE dependency datasets support this claim. This would mean that cells are less sensitive to shelterin depletion when they are mutated in TP53, which makes sense biologically.

– Monoallelic expression in TERT promoter-mutant contexts. The analysis behind this claim, based on alignment of RNA reads to heterozygous regions and the subsequent counting of reads mapping to each allele, seems robust, although it would have been nice to see a few more details (for example, what is the measure of linkage disequilibrium between the TERT promoter mutations and these anchor SNPs).

– TERT promoter-mutant cell lines show hypomethylation at PRC2-repressed regions. This claim is based on an analysis of genome-wide reduced representation bisulfite sequencing (RRBS) data in nearly 1000 cell lines, and the finding of associations between TERT promoter mutation and CpG methylation of different regions of the TERT gene and other loci. An overlap analysis showed that these methylated regions were enriched for PRC2-repressed regions.

All in all, I believe the claims in this study are well supported. This work constitutes a valuable resource for the scientific community, and has made new observations that contribute to the elucidation of telomere maintenance mechanisms.Reviewer #2:

Kevin Hu, Mahmoud Ghandi and Franklin W. Huang present their important work on determining telomere content across > 1000 cancer cell lines. In addition to this highly valuable dataset, the authors present several scientific vignettes wherein various questions are addressed using their curated resource. Using CRISPR/Cas9 screening data from the same set of cell lines, they find that sensitivity to CST (CTC1, STN1, TEN1) knockout was associated with telomere content and that cell lines sensitive to CST knockout demonstrated lower telomere content. Shelterin complex members (ACD, POT1, TERF1, TERF2, TINF2) were further identified as co-dependencies to CST knockout.

They find that cell lines with monoallelic expression, as in a TERT promoter mutant setting, also demonstrate allele-specific methylation. Interestingly, TERT promoter mutant demonstrated gene body hypomethylation not observed in other monoallelic TERT expressors. Moreover, this hypomethylation was found to be genome-wide and not restricted to the TERT locus. Finally, nearly all of this hypomethylation was localized in PRC2-repressed regions.

The hypothesis-driven vignettes are clearly of interest in providing correlative insights that could fuel future mechanistic studies. More importantly, they exemplify the strengths of the resource. Nevertheless, the primary value of the manuscript in my opinion is the enormous resource of telomere content estimates for cell lines widely used in biomedical research. The authors can do a more thorough job showing the reader that their measurements are reliable and whether or not they would be generally applicable to fresh cell lines purchased from a vendor.

1. WGS-based telomere content estimates are likely much more reliable than WXS-based estimates. The authors do not comment on this.

2. Cell lines from different sources can vary substantially. For example, HeLa strains from different laboratories can show vastly different karyotypes (PMID 30778230). These caveats are not currently discussed.

3. Telomere length attrition is replication dependent, however the authors have not looked at whether their measurements are associated with population doublings in individual samples or across multiple samples taken at different PDLs.

4. ALT status is an important confounder of telomere content. The authors hint at ALT status in their manuscript at various points, but do not incorporate ALT status into their analyses.

5. The combination of a number of parameters is going to determine telomere content in cell lines. It would be helpful to understand the combined contribution of multiple parameters.Reviewer #3:

In this manuscript, Huang and colleagues used public whole genome or whole exome sequencing datasets to establish telomere content in over a thousand cancer cells lines. Once telomere content was established, they linked it to other available sets of analysis, including RNAseq libraries and genome-wide CRISPR or RNAi screens.

First, they found that telomere content is highly variable among tissue types, with highest telomere content (TC) in tissues that have higher frequencies of ALT activation. They also found weak correlation with TERT or TERC expression. They then analyzed the correlation between telomere content and gene dependencies and found that dependencies to TRF1 and the CST correlates with TC. Independently of TC, they analyzed correlations between gene dependency of telomeric proteins or ATRX and DAXX with mutations or transcriptomic and proteomic profiles. Finally, they analyzed the link between TERT allelic expression and epigenetic marks on TERT promoter.

Although such broad analysis of telomere length or telomere proteins / TERT dependencies is interesting, it appears hard to really see the biological significance of certain correlations or the novelty of the findings.
