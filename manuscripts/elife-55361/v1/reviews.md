# Peer review - Round 1

Editors:
- Shahragim Tajbakhsh, Institut Pasteur France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55361.sa1](https://doi.org/10.7554/eLife.55361.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your study describes bi-fated cells at the murine tendon-to-bone attachment, namely with activation of a mixture of chondrocyte and tenocyte transcriptomes, under the regulation of shared regulatory elements and KLF transcription factors, notably KLF2 and KLF4. The report provides novel insights into the yet unknown molecular and cellular architecture of the tendon-to-bone attachments, and hence is seen to be both novel and medically relevant.

Decision letter after peer review:

Thank you for submitting your article "Bi-fated tendon-to-bone attachment cells are regulated by shared enhancers and KLF transcription factors" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Clifford Rosen as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

The manuscript from Kult and colleagues focuses on the transcriptional regulation of a unique set of cells located between bone and tendon known as the attachment unit. Using RNA-seq and ATAC-seq, the authors investigate shared and unique transcriptional programs and accessible genomic regions. The ATACseq and epigenome profiling reveals transcriptional enhancers, with overlapping intergenic areas between bifated and both fates. Transgenic enhancer reporters expose common enhancers for tenocytes and chondrocytes. Klf2 and Klf4 were identified as critically required for differentiation. These findings lead the authors to propose that bi-fated attachment cells that connect tendon to bone. Previous studies showed that these cells express cartilage and tendon markers so the present study would need to clearly highlight the advances made compared to previous work. As a general note for example, the co-option of existing enhancers does not rule out the existence of de novo ones. This needs to be addressed clearly in the study.

Essential revisions:

1) The test of enhancers by transgenesis is somewhat limited in scope (only 8 tested) and yields some surprising results that can be explored further. An important request would be to make sure of the reproducibility of experiments. It is said that 5 out of 8 selected elements drove expression in the forelimb, but not how many attempts were done for the negative ones. Moreover, as reported in the transparent report form, N=1 for Col1a1 element, N=3 for Klf2 element, N=2 for Sox9 element, N=3 for Mgp element, N=4 for Col11a1. The reviewers understand that a site-directed approach is likely to be more reproducible that random insertion, it is recommended to examine at least 3 instances per element, to be certain of some surprising results. For example, although Sox9 is not expressed in hypertrophic chondrocytes, the Sox9 element drives expression in hypertrophic chondrocytes. Moreover, Sox9 and Klf2 elements drive expression in hypertrophic chondrocytes but not in AU cells. If these results are confirmed, they may cast doubt on the conclusion that co-option of enhancers is the (only) mechanism that regulates expression in AU cells.

2) The authors have not systemically looked for AU enhancers that are not shared with tenocytes or chondrocytes. Combined ATAC-seq dataset and published ChIP-seq of histone marks can potentially identify new enhancers. The authors could speculate or assess if those enhancers were acquired de novo and exclusive of AU cells.

3) Figure 1A, the authors present a PCA biplot : Can they be more specific on how the data were transformed prior the dimension reduction (FPKM, VST, Log transformed, CPM…?). How many genes were taken into account in the PCA; All or as it is more commonly done on the 500 most variant ones ?

4) Figure 1 C – GO terms found are very generic, this information does not really seem to be useful. Can the authors can be more specific on the parameters they used in their GSEA analysis : test used and p-value correction (FDR q-value suggests a Benjamin and Hochberg correction, it that right ?

5) In general, one has to give the detail on the software version (including package version) and OS type used for the bioinformatic analysis, these informations are missing from the manuscript.

6) In the sentence: "This suggests that the attachment cell transcriptome is largely shared with both chondrocytes and tenocytes (Figure 1A, PC1 52.47%)", the word largely is misleading.

7) The authors do not discuss the variation both on the first and the second PC and of the attachment samples. This is a big issue because there are only 2 samples for this category of cells in which the intra-group variability is very high. This leads to a poor statistical parameter estimation giving rise to poor statistical test outcome.

8) Legend of Figure 1: The term MARS-Seq is slightly misleading as it is usually associated with single cell RNAseq analysis. For clarity, please write instead bulk-MARS-Seq.

9) "To further support our initial observation that the transcriptome of the attachment cells is a mixture of chondrocyte and tenocyte transcriptomes, we clustered the statistically significant differentially expressed genes between all samples into 5 clusters, using CLICK". Same remark as the use of contrasts in DESeq2.

10) In the sentence : "From these two clusters, 374 genes, 320 of them tenogenic and 54 chondrogenic, were also found to be expressed by attachment cells." It is unclear what "so found to be expressed by attachment cells" mean? For instance, for the tenogenic markers, does this mean that in the attachment vs. chondrocytes comparison these genes are up-regulated in the attachment cells? In that case, how are the tenogenic markers defined, using the tenocytes vs chondrocytes comparison? Would it be possible to have a Venn diagram to help follow the process to define the different marker identifications? Has a simpler method using contrasts in DESeq2 been tested? If yes, do the results converge with the ones presented here? Are these "statistically significant differentially expressed genes between all samples" coming from a pairwise wald-test or a likelihood ratio test? the Materials and methods suggest that the wald-test was used. Please clarify.

11) In a previous study the authors investigated the emergence of the attachment unit (AU) with focus on bone eminence progenitors (co-expressing Sox9 and SCX up to E12.5 and expressed Col2 after E12.5 according to Col2a1CreERT2 lineage tracing). Here, they focus on the transcriptome of E14.5 attachment cells from the deltoid tuberosity, however these appear to be different from tuberosity progenitors (adjacent chondrocytes) as described in Figure 1—figure supplement 1. A better definition of what is defined as attachment unit in this paper vs previous papers and/or the AU subcompartments would help clarify the populations that are being examined.

12) Moreover, as the constitutive Col2a1Cre did not label the AU, but in the previous study did label the AU/bone eminence progenitors, it is unclear what the exact definition of AU is.

13) When using the Col2a1-Cre, R26R-tdTomato and Scx-GFP, the authors mention : Unexpectedly, the two reporters failed to label the attachment cells that were located in between these two populations. This failure might be due to a missing regulatory element in one of the constructs that was used to produce each transgenic reporter. However, in Figure 1—figure supplement 1, subpopulation 5 seems to have SCX+ cells. Is this an error of labelling? What is the orientation of this section?

14) For FACS and ATACseq analysis the authors use Sox9CreERT2;tdTomato;SCX-GFP and Col2CreERT2;tdTomato;SCX-GFP. It is not clear why for FACS the Col2CREERT2 line is used while for LCM the constitutive one is used. Moreover, as previously reported, they isolate attachment cells as double positive SOX9/SCX cells. Here again, do the cells taken for analysis include those of the tuberosity itself? Col2CreERT2 with Tamox at E12.5 should be labeling the tuberosity too. It is unclear which cells from which Cre/reporter combination have been used for the ATACseq experiments of Figure 3.

15) For Figure 2, a scheme showing where exactly in the bone we are located and how it has been sectioned would be helpful. Also, it would be nice to perform single molecule FISH on top of Col2Cre:R26TOM:SCX lineage tracing to show the specificity of the colocalization in the "double reporter-negative" area. Also, including the KLF2/4 FISH at this point would help visualize distinctions between genes belonging to cluster 5 (unique to AU) vs genes referred as mixed transcriptome (Wwp2, Bgn).

16) The authors propose a role of Klf2/4 in attachment differentiation. What is the temporality in expression of Klf2/4 vs the putative downstream factors such as Gli1, Col5a1?

17) In ISH figures, some cells in the cartilage compartment also seem to coexpress tenocyte/cartilage markers. Can the authors comment on that?

18) How did the authors adapt MARS-Seq (a single cell RNA seq pipeline taking advantage of cell sorting) to a bulk analysis? More specifically, it isn't clear how laser capture technique was combined with the MARS-seq protocol.

19) The resolution on the single molecule FISH does not allow to really appreciate a large coexpression of the presented markers in the area.

20) Figure 4: Could the authors indicate more clearly the demarcation between cartilage and connective tissue where double labeling is found?

21) It would be interesting to know if the loss of the gene expression in Figure 5 results in a morphological abnormal attachment at later postnatal stages. If the authors have looked, it would be helpful to comment in the Discussion or include the data. How much of the intermediate gene expression program in the attachment site is dependent upon Klf regulation?

22) Is this transcriptional state-sharing permanent or transitional? Their work could be nicely contrasted and compared with some studies examining transcriptional heterogeneity/the co-expression of multiple cell fates as a mechanism cells used to transition from (multipotent) progenitor states to committed fates. Enthesis tissue would be an interesting and unique situation where possibly this intermediate shared transcriptional state is maintained to generate a new cell type. Possible references for transcriptional heterogeneity in progenitors include: Soldatov et al., 2019 and Johnson et al., 2015.

23) The section on the AEG/esophagus-stomach boundary should be better integrated with their own data or removed from the Discussion. It was not clearly stated how these two tissues are similar other than being border tissues. It is recommended to expand this section to include more specific examples how these regions (enthesis and esophagus) are related. Perhaps this esophageal boundary has also been shown to have a shared transcriptional/epigenetic state with neighboring tissues?
