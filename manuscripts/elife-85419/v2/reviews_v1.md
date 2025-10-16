# Peer review - Round 1

Editors:
- Jeremy J Day, https://ror.org/008s83205 University of Alabama at Birmingham United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85419.sa0](https://doi.org/10.7554/eLife.85419.sa0)

This manuscript describes a valuable new circuit mapping and profiling technique called Multiplexed projEction neuRons retrograde barcodE (MERGEseq) that combines transcriptome and projectome data at a single-cell resolution. The authors provide solid evidence that MERGEseq can be used to identify projection targets and cell type/layer/transcriptome differences of projection neurons in the mouse prefrontal cortex, and validation experiments are rigorous. While this report is a proof-of-principle that MERGEseq is useful for circuit mapping and profiling and many potential details will influence conclusions, this technique could easily be adapted to other regions with known projection targets and adds to a growing arsenal of combinatorial circuit mapping and profiling tools.


---

# Peer review - Round 1

Editors:
- Jeremy J Day, https://ror.org/008s83205 University of Alabama at Birmingham United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85419.sa1](https://doi.org/10.7554/eLife.85419.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "High-throughput mapping of single-neuron projection and molecular features by retrograde barcoded labelling" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Kate Wassum as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Please accompany your revision with a point x point response to each point raised by the reviewers in the public and private reviews, paying special attention to the essential revisions noted below.

Essential revisions:

1) The manuscript builds upon several prior approaches, only some of which are discussed and cited. The scholarship of the manuscript needs to be improved by incorporating a more robust review of other approaches, as suggested by reviewers to place these findings in context. The scholarship of the manuscript should also be improved by including a more transparent discussion of the limitations of MERGE-seq relative to other approaches.

2) Reviewers raised several issues related to the efficiency of retrograde labeling and barcode recovery that have the potential to affect the conclusions reached in the manuscript. These issues should be addressed in the manuscript with new data and/or analysis.

3) A revision should incorporate requested information to provide clarity about the experimental details and analysis methods.

4) Please ensure your manuscript complies with the eLife policies for statistical reporting: https://reviewer.elifesciences.org/author-guide/full "Report summary statistics (e.g., t, F values) and degrees of freedom, exact p-values, and 95% confidence intervals wherever possible. These should be reported for all key questions and not only when the p-value is less than 0.05.

5) Please include a key resource table.

Reviewer #1 (Recommendations for the authors):

1. The introduction discusses current techniques like BARseq but makes no mention of the current retrograde tracing and sequencing techniques which is what MERGEseq is actually improving upon. While these retro techniques are discussed in detail in the discussion, it seems odd that they are left out of the introduction as MERGEseq is really an extension of these techniques rather than MAPseq/BARseq.

2. Figure 1 – Supplement 1 shows that very different UMI cutoffs were used to call a cell "positive" for each barcode index. This would presumably preclude direct comparison across regions with different barcodes, at least for purposes of determining the density of projections (since a different degree of projections will be excluded for each virus region). This should be mentioned more explicitly in the manuscript.

3. Lines 170-171 note that "stressed" 637 neurons were filtered out from the Slc17a7 population. It is not clear what this means, and Figure 2 – Supplement 1A does not explain this. This should be clarified.

4. In the discussion, authors might comment on the added value of capturing the "full" transcriptome at the cost of spatial resolution.

5. It may be good to mention that retro-AAV2 has not been reported to infect fibers of passage.

6. Please include a color scale for Figure 5a.

7. Please include axis labels for Figure 5c.

8. Figure 5F shows the DMS+LH Pou3f+ cells, what about the DMS only and LH only? Are there any Pou3f+ cells that lack fluorescence?

9. Please enlarge Figure 3e.

10. For scRNA-seq, please provide detail on the depth of sequencing, the number of GEMwells used, and the number of technical or biological replicates.

11. Please include a color scale for Figure 6e-f.

12. Typo, line 536 "despite of chosen"; should be "in spite of chosen" or "despite chosen".

13. Supplemental Figure 2 panel E, missing cell type labels going across.

14. Please cite the original retro seq paper (Tasic, 2018, PMCID: PMC6456269).

Reviewer #2 (Recommendations for the authors):

Based on their detection of barcodes in single-cell RNA-sequencing, the authors conclude that "about 74% of barcoded vmPFC neurons projected to one of these five targets (dedicated projection) and 26% of barcoded vmPFC neurons sent collateral projections to multiple brain regions…" (lines 92-94 in Introduction, lines 242-244 in Results). These conclusions are contingent upon 100% of neurons that project to a specific region being labeled by retrograde barcoded viruses and barcodes are detected at 100% efficiency. The authors did not provide an estimation of either efficiency. In the penultimate paragraph of the Discussion, the authors raised this as "A potential technical concern" but conclude that "the overall dedicated and collateral projection pattern…will not be greatly affected by the labeling efficiency or recovery rate."

I disagree with the authors' conclusion. Suppose that retrograde labeling efficiency is 70%, and the barcode recovery rate is also 70% (both very optimistic estimates). Suppose further that all neurons of a particular type send collateral branches to two target regions, X and Y. The experiment will yield the results that 25% of the neurons will be labeled by barcodes injected at X only, 25% by barcodes injected at Y only, 25% labeled by both barcodes, and 25% labeled by neither. The conclusion from the above experiment would be that 2/3 of neurons are "dedicated" to either X or Y, and 1/3 of the neurons send axons to both regions. This simple back-of-the-envelope calculation reveals how much collateralization is underestimated by incomplete retrograde labeling!

Without reading the penultimate Discussion paragraph, readers will be misled twice about the fraction of "dedicated projection." Even after reading it, the readers will still be misled by the authors' conclusions.

If the authors wish to make a quantitative conclusion about the true "dedicated" vs. "collateral" projections, they must determine the efficiency of retrograde barcoding. They can inject AAVretro carrying two different types of barcodes into the same region (via two separate injections, rather than injecting a mixture, which will artificially raise the co-transduction efficiency) and quantify individual cells that are labeled by both types of barcodes. They can then use such efficiency to calibrate their estimation of "dedicated" vs. "collateral" projections. (Note that retrograde labeling efficiency may differ for different sites.) Without such calibration, the authors should caution the readers about the (likely large) underestimation of true collateralization whenever such data are presented and discussed.

Another issue with "dedicated" projections: the authors only examined 5 targets. Each of the "dedicated" projections is true within these 5 targets, these neurons can send collateralized axons to other, unstudied targets.

Reviewer #3 (Recommendations for the authors):

1) Please provide a better context for the presented method. Clarify how the transcriptomic cell type definition in this paper corresponds to previous papers and clarify how the presented method differs from previous methods and what the advantages and disadvantages are. Please cite other papers that have employed single-cell Retro-seq: Tasic et al. 2016 (https://doi.org/10.1038/nn.4216), Tasic et al. 2018 (https://doi.org/10.1038/s41586-018-0654-5) , Yao et al. 2021, https://doi.org/10.1016/j.cell.2021.04.021, Zhang et al. 2021 https://doi.org/10.1038/s41586-021-03223-w )

2) Line 171: How were 'stressed' neurons defined? Please explain.

3) Please mention which 10x Genomics chemistry version (e.g., v2, v3, v3.1) you use in the main text and criteria for QC (lowest acceptable UMI or gene detection level, as well as median gene detection for different cell classes: excitatory, inhibitory and non-neuronal).

4) Figure 1E: The figure shows a correlation between two studies at a resolution that is not appropriate – too low to be informative except for QC. Please move this to supplement.

5) Cell type identity definition: I suggest performing data integration (for example using Seurat) with Bhattacherjee et al., 2019, Liu et al. 2021 and with Yao et al. 2021 (see above) to give more updated names to cell types. The paper should start with cell type definition and present consistent nomenclature from the beginning.

6) Caution should be exercised when interpreting under-represented cell types in MERGE-seq. Figure 2 shows that only 8 neurons of the L5-Htr2c subtype were validly barcoded. However, in addition to the possibility that this subtype does not project to the five targets included in this study, the small number of barcoded L5-Htr2c subtype could also be caused by the tropism of AAV2-Retro viruses, or the selective loss of L5-Htr2c neurons in tissue processing due to cell death. Comparison with the in situ hybridization patterns of marker genes in Supplementary Figure 2 and the proportions of neuronal subtypes in Figure 2b suggests bias in sampling of cell subtypes by scRNA-seq. Therefore, independent approaches should be utilized to further investigate the projection targets of L5-Htr2c neurons before reaching a conclusion.

7) We suggest replacing "unbarcoded" with "non-barcoded". "Un-barcoded" sounds like the cells were barcoded and then the barcode was removed. The more appropriate term is "non-barcoded".

8) Figure 2 (and others): Please state how many cells are represented in each panel of the figure.

9) Figure 2 E and F – Not the most straightforward and informative representation: We suggest converting these to bar plots per area and per type. It is good to see that the authors kept the colors introduced in this figure in Figure 3. We suggest wherever the color code can be kept consistent, to do so.

10) Figure 3. MERGE-seq reveals hidden projection diversity within the vmPFC – please remove 'hidden'.

11) Figure 6E/F – How many neurons and which types are shown? Every figure should state which single-cell transcriptomes were included and the labeling should be consistent with the previous figures. For example, please show the PC1/PC2 scatter plot in E and F next to the same cells labeled with their cell type assignments + colors. This allows the reader to connect the information from previous figures to these.

12) Line 490/491 Please include these references when referring to Retro-seq: Tasic et al. 2016 (https://doi.org/10.1038/nn.4216), Tasic et al. 2018 (https://doi.org/10.1038/s41586-018-0654-5), Yao et al. 2021, https://doi.org/10.1016/j.cell.2021.04.021, Zhang et al. 2021 https://doi.org/10.1038/s41586-021-03223-w )

13) Completeness and sensitivity of barcode recovery of the approach: The authors recovered 1791 EGFP-positive cells undergoing fluorescence-activated cell sorting (FACS) from three mice and 19,470 single cells without sorting from the other three mice. Using thresholds calculated based on barcode counts in non-neurons, they found that the percentage of barcoded cells in FACS sorted or unsorted groups are 54% and 12%, respectively. Given that almost all cells sorted by FACS should have been infected with the barcoded GFP AAV viruses, the recovery rate for barcodes is low. Therefore, labeling neurons as barcoded and unbarcoded based on the detection of barcodes will create false negatives, that is, classifying many retrograded labeled neurons as "unbarcoded" (we suggest changing this to "non-barcoded"). It seems that the projectomes of neurons cannot be simply derived from barcode detection through sequencing. Many "unbarcoded" projection neurons were in fact retrogradely labeled by AAV viruses injected into a specific target but were negative for barcodes due to technical limitations.

One immediate issue caused by the false negative rate of barcode detection is whether the machine learning-based modeling is provided with the right training data (Figure 6). For this model to predict projectomes based on transcriptomes, it first requires a good correlation between barcoding and projectome.

More discussion should be given to the recovery rate of barcodes, and its potential impact on data analysis.

14) Additional analysis and control experiments related to barcode detection:

The low barcode recovery rate could be due to the low number of copies for AAV-encoded transcripts in the transcriptome of single cells, or it is specific for the detection of short barcode sequences. With the current scRNAseq data, one additional analysis is to measure the percentage of neurons positive for GFP transcripts from both FAC-sorted and non-sorted samples and compare the GFP+ neuron frequency to barcode+ neuron frequency.

15) To enrich cDNA fragments composed of the barcode index, unique molecular identifiers (UMIs), and the barcode, the authors prepared expressed virus barcode libraries with special primers. The authors also tried to detect barcodes directly in single-cell transcriptional libraries. What was the barcode detection frequency without this additional amplification, that is, in regular single-cell transcriptional libraries? It would be good to comment on how much this approach (we assume) improves barcode detection compared to the regular 10x single-cell libraries without additional barcode amplification.

16) The authors hypothesized that the non-neuronal cells would not be transduced by rAAV2-retro. The barcode counts in these non-neuronal cells were used to generate the thresholds for projection neurons. However, such cells, especially microglia, could be positive for AAV transcripts perhaps by phagocytosing dying infected neurons. A better control cell population could be cells negative for GFP after FACS. If sequencing data are available for such GFP-negative cells, it would be useful to examine the detection of barcodes in these cells and use them as the negative control for thresholding.

17) In the section on Projection barcode FASTQ alignment, the authors stated that deMULTIplex R package (v1.0.2) (https://github.com/chris-mcginnis-ucsf/MULTI-seq) was used to count UMIs associated with barcodes. This method was designed to detect the Sample index and needs to be further adjusted for barcode reading. The current method did not reveal the fact that a single UMI could be associated with multiple barcodes, which could raise the need for thresholding at this stage.

MULTIseq.preProcess was used to identify the barcode sequence based on its position relative to the P7 primer. The result is a readTable with each row showing the Cell ID, UMI, and barcode sequence. The same UMI appeared in multiple rows and could have different barcodes.

MULTIseq.align function was used to match the barcode sequence in each row of readTable to the 5 barcodes, and to find the numbers of UMI associated with each barcode in each sample. This function utilizes a minimal Hamming distance of 1 to call a match between barcodes detected in the sequencing samples and the list of designed barcodes. We would suggest a minimal hamming distance of 2. Many of the sequences with a minimal Hamming distance of 2 have a frameshift of 1 nucleotide as compared to the designed barcodes. If the parameter of MULTIseq.preProcess is adjusted to change the position of the expected barcode, we would expect to find the full-length barcode. A specific example is:

"AAGGCACAGACTTTG" has a Hamming distance of 2 as compared to barcode 2 "GAAGGCACAGACTTT", and should also be considered as a match.

More importantly, MULTIseq.align does not consider the complication that multiple barcodes could be detected for the same UMI, and simply uses the barcode of the first duplicated UMI. Taking the FAC-sorted pfc_4 dataset as an example, the readTable generated using this dataset contains 30272582 rows. The third column represents sequences detected at the specified barcode position.

After aligning to the 5 barcodes with a max hamming distance of two, 26443131 of the sequences detected at the specified barcode position can be matched, leading to 474012 unique combinations of Cell/UMI, each combination with a set of detected barcodes.

Many of the UMIs are associated with multiple barcodes. In the pfc_4 dataset, 68955 of the 474012 unique combinations of Cell/UMI are associated with multiple barcodes (14.5%).

When we used the data above to compare the density distributions of barcode counts per UMI per cell for the pfc_4 dataset and that of non-neuronal cells, we find that low barcode counts may not be specific. The best negative control here would be to use GFP-negative cells after FACS.

Depending on the threshold values to eliminate these false barcode counts, we reached an even smaller number of barcoded neurons at the end of the analysis.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "High-throughput mapping of single-neuron projection and molecular features by retrograde barcoded labeling" for further consideration by eLife. Your revised article has been evaluated by Kate Wassum (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The reviewers have outlined a couple of additional changes that are needed to fully respond to the prior critiques. These represent small changes in the text and, thus, should not present a significant difficulty. Please address these comments in a revised manuscript.

Reviewer #2 (Recommendations for the authors):

The revised manuscript has improved. However, the authors still did not address my concern about determining "dedicated" vs. "collateralized" projections. The authors put those numbers in the Introduction and Results without doing the control experiment I suggested (to determine retrograde labeling efficiency) and without mentioning the caveats. The caveat is only mentioned in Discussion (lines 499-500). Readers who missed this sentence will be misled.

Adding a comparison between MERGE-seq and fMOST tracing (the new Figure 3C) is an improvement. As can be seen from the graph, there is a higher percentage of collateralized axons in fMOST compared to MERGE-seq in multiple categories, confirming that MERGE-seq underestimates the fraction of collateralized axons (though to my relief there is not an order-of-magnitude difference).

The authors should add the number of neurons included in the fMOST dataset in the Figure 3C legend.

Reviewer #4 (Recommendations for the authors):

This manuscript introduces MERGE-seq, a multiplexed method for profiling transcriptional features of individual neurons projecting to specific targets. The approach involves multiplexed retrograde tracing by injecting distinctly barcoded rAAV-retro viruses into different target areas, followed by scRNAseq of neurons in the source area on the 10xGenomics platform. The projection targets of barcoded neurons in the source area can be inferred by matching the detected barcodes to the barcode sequences to of rAAV-retro viruses injected into the target areas.

Validation of this approach was conducted by injecting rAAVs carrying five distinct 15-nt barcodes to five known ventromedial prefrontal cortex (vmPFC) targets. This revised version has performed integration analysis with previously existing vmPFC scRNA-seq and MERFISH dataset, and compared vmPFC scRNA clusters and the 7 excitatory neuron subtypes analyzed in this study with those in prior datasets. MERGEseq facilitated the identification of vmPFC cell types projecting to distinct areas, revealing that each of the seven identified excitatory neuron subtypes projects to multiple targets, and the five targets receive projections from multiple transcriptomic types. MERGE-seq derived projection patterns were validated through dual-color retro-AAV tracing and were correlated successfully with fMOST-based single-neuron tracing data. Additionally, marker genes for projection-specific cell subclasses were validated in retrogradely labeled vmPFC using RNA FISH for marker detection.

This revised version has effectively tackled the previously raised concerns. Significant efforts have been dedicated to performing an integrated analysis with existing datasets, enhancing the data analysis methodology, and imposing more stringent criteria for barcode determination. The revised manuscript places greater emphasis on acknowledging and incorporating several prior approaches that influenced the development of the MERGE-seq concept. While the efficiency of retrograde barcoding wasn't experimentally addressed by injecting rAAV-retro viruses with different barcodes into the same region, the limitations and potential concerns of MERGE-seq are now explicitly discussed. Additionally, the revised manuscript provides clarity on essential technical aspects, including QC criteria and parameters for evaluating scRNA data quality. In sum, this manuscript is rigorous and thorough, offering a valuable approach for the multiplexed investigation of neuronal transcriptomics and projection targets.

In addition, I suggest that QC criteria should be explicitly listed in the main text. The number of cells passing each QC step should also be listed either in the main text or in the related figures. My understanding is that there is a general QC step for scRNAseq quality based on gene count, total UMI count, and mitochondrial gene expression and that there is another step to identify low-quality cells and contaminated non-neuron cells. It would be very helpful that such information is readily available in the main text.
