# Peer review - Round 1

Editors:
- Paschalis Kratsios, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78345.sa0](https://doi.org/10.7554/eLife.78345.sa0)

This study provides the genome of the little skate Leucoraja erinacea, a cartilaginous fish that displays pelvic fin-driven walking-like behavior. Leveraging this genomic resource, the authors compare gene expression and chromatin accessibility profiles in motor neurons of the little skate and other species (e.g., mouse, chicken), aiming to predict conserved and divergent gene regulatory mechanisms underlying motor neuron development. The work represents an important contribution to the field of comparative genomics and evolutionary biology.


---

# Peer review - Round 1

Editors:
- Paschalis Kratsios, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78345.sa1](https://doi.org/10.7554/eLife.78345.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Little skate genome exposes the gene regulatory mechanisms underlying the evolution of vertebrate locomotion" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Catherine Dulac as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you plan the next steps. The reviewers agree that the paper has potential, but extensive revision and new data are needed.

Essential revisions:

1. The authors report the identification of conserved and divergent molecular markers across multiple species with RNA-Seq, but they do not validate the expression of novel markers in either category with an independent method (e.g. in situ or antibody staining).

Such validation is needed to substantiate the authors' conclusions.

2. The reviewers do recognize that functional analyses are not feasible in the little skate. However, to substantiate the claim that more complex regulatory mechanisms have evolved in tetrapods to accommodate sophisticated motor behaviors, the authors should conduct additional gene expression experiments. For example, as pointed out by reviewer 1, the authors can focus on Foxp1 and Snail.

3. Reviewers 1 and 3 raised a number of important issues regarding the bioinformatic comparisons (e.g., completeness of datasets, quality control, introduction of bias) that must be carefully addressed. First, the authors must show validation of their RNA-Seq method in chick, as suggested by reviewer 1. Second, the reviewers would like to see a re-analysis of the RNA-Seq datasets in an unbiased manner, for example, by directly comparing MN expression of orthologous genes in the different species (e.g., compare highly expressed genes in MNs of the different species). Two reviewers stressed that comparing a pure MN population to tail tissue in the skate and DRGs in the mouse was not an appropriate comparison. Third, comparisons of mouse and skate-accessible chromatin regions should be done without biasing first to DEX genes. Lastly, additional key aspects of evolution, such as paralogue substitution or expression of species-specific genes should also be considered. Authors could follow comparisons similar to: 10.1038/s41559-021-01580-3.

4. The reviewers agree that a significantly improved version of the little skate genome is an important contribution. In the first part of the manuscript, the authors should mention the work by Marletaz et al. (bioRxiv) that also provides a new little skate sequenced genome.

5. There is a propensity to overstate claims throughout the manuscript. For example, without functional data in little skate, the claim that the TF networks are much simpler is not substantiated simply by ATACseq and predicted binding sites. The authors should tone down statements in Abstract and Discussion (as indicated by the reviewers) and always make it very clear that they are simply predicting regulatory connections between all these genes.

Reviewer #1 (Recommendations for the authors):

1) Based on the low convergence of mouse, skate and chick MN transcriptomes it may be a possibility that one of the datasets is incomplete. The authors should go back to their RNAseq datasets and check for the expression of known MN markers that are conserved in the 3 species to identify where this inconsistency arises. It would also be helpful to show validation of their chick RNAseq method, for example, show the efficiency and specificity of GFP expression in MNs, and what % of MNs were electroporated and sorted before sequencing.

2) Another surprising finding is that a higher number of putative TF binding sites are found in the tail-SC-specific ACRs for pectoral MNs and that the expression levels of these TFs do not correlate with this trend. The authors should comment on this discrepancy. Similarly, while they were found to be highly expressed in pectoral MNs, 5 genes including Isl1, show no associated ACR (Figure 5C). Do the authors think that this is due to long-range regulation of those genes? Some discussion of this would be clarifying.

Reviewer #2 (Recommendations for the authors):

As already stated, the main limitation of the study seems to be the strategy followed for the RNAseq and ATACseq comparative analysis. The use of a prior intra-species comparison with heterogeneous criteria is not well-justified, it is a potential source of bias and should be avoided. Why authors do not directly compare MN expression and ATACseq of orthologous genes in the different species? In addition, it is known that there are extensive paralogue substitutions that indicate common regulatory mechanisms but might be missed if not analysed directly. Authors could follow comparisons similar to previously published articles: 10.1038/s41559-021-01580-3.

Comments on each section:

1) Abstract:

Several statements are not strongly supported by data:

"Conserved MN genes were enriched for early-stage nervous system development."

"conservation of the potential regulators with divergent transcription factor (TF) networks through which expression of MN genes is differentially regulated."

"TF networks in little skate MNs are much simpler than those in mouse MNs."

2) Figure 1 data:

In the first part of the manuscript, the authors should mention biorxiv Marletaz et al.'s work which also provides a new little skate sequenced genome and analysis, with a higher number of identified coding genes compared to this work and also with 3D chromatin structure data that identifies TAD boundaries that coincide with CTCF sites in Hoxa and Hoxd clusters mentioned in Baek et al.

3) Figure 2 data:

(3.1) The comparison of Pectoral MN with tail SC, compares a purified population with a mix of cell types including MN. This unbalanced comparison could explain why tail SC shows 3 times more DEX genes than pec-MN.

(3.2) In the previous analysis published by the group, 592 genes were identified as 2 fold enriched in pectoral MN, why the new analysis retrieves only 135 genes? This should be clarified for the reader.

(3.3) Also from previous work of the authors several genes were determined to be expressed in little skate MN (HB9, lhx3, lhx1, Ephs, Ephrins, slit3, onecut1, nell2, nrcam, ngfr, pappa2, cdh7, amigo1, unc5c, lrx5, lrp1b, Zfp804a, etc), which of these genes are predicted to be enriched (or expressed at least) in the Pec-MN data set? Were all the genes found? This could be used as quality control of the data set or data set analysis.

4) Figure 3 data:

(4.1) Compares "Highly expressed genes in pec-MN". What are the criteria followed to assigned "highly expressed genes"?

(4.2) This data set is now compared with DEX of mouse embryonic MN compared to sensory neurons. Which type of mouse MN? at what A-P level?

(4.3) If skate genes are selected by high expression, why do mouse MN not follow the same criteria to avoid bias of comparison? As a control for bias in the criteria: What is the overlap of mouse highly expressed genes (with similar criteria to skate gene selection) with the data set of mouse MN DEX compared to sensory mouse neuron?

(4.4) Same for chick data, how equivalent are brachial MN to mouse MN dataset? Why select DEX compared to the brachial spinal cord and not sensory neurons as in mouse.

Without any justification for the followed strategy, it seems different populations and comparisons will introduce important biases that limit the conclusions.

The best strategy would be to compare highly expressed genes in MN in the different species and clarify if used populations are really "homologous" cell types in the different species.

(4.5) The variability of sampled populations or the biases introduced in the analysis might explain the low overlap found among the 3 species (Figure 3A). For the Venn diagram, is the overlap among categories higher/lower/equal to what would be expected by chance?

5) Figure 4 data:

(5.1) Similar to previous comments: Why limit TF motif enrichment of ACRs to only DEXs in pec-MN and tail-SC that (1) highly reduced the number of ACRs and (2) Induces a bias in the analysis? Analysis should be performed with all MN ACRs.

(5.2) Line 224: On the other hand, the tail-SC-specific ACRs in the pec-MN DEGs were enriched with the binding sites of Hoxa9, Hoxa11, Hoxd10 and Hoxd11, most of which are expressed in fin-MNs of little skate.

Could the authors provide a sentence to try to explain this observation? I found confusing that this is mentioned without providing more context.

6) Figure 5 data:

(6.1) Similar to previous comments, conclusions driven by this analysis might be biased by wrong comparative strategies to start with, thus conclusions are not well supported. Comparative of mouse and skate ACRs should be done without biasing first to DEX genes, which highly reduced the number of analysed ACRs, particularly to shared genes that are only 40.

(6.2) MN TF enrich motifs are broadly found in mouse sensory and skate tail DEX genes, which might be a strong indication that the strategy used in the analysis is not suitable for the identification of MN gene regulatory networks.

(6.3) Figure 5C: Most TF binding motifs in databases are built with experimental data from mouse or human TFs. Although core sequences for TF binding sites in the same families are conserved, small differences arise in individual members or between species. Could this explain why there is a higher number of motifs found in mouse than in skate? In addition, is the number of motifs in mouse and skate normalized by the size of analysed sequence?

7) General comments on format:

(7.1) Figures 3-5: differences among circles sizes are difficult to appreciate, maybe color heatmaps would be more informative.

(7.2) Figure 4 B, C could be included in supplementary.

Reviewer #3 (Recommendations for the authors):

The authors should be careful in their phrasing so as to always make it clear that they are simply predicting regulatory connections between all these genes.

For instance, on Page 3, line 29:

"Comparison of accessible chromatin regions between mouse and skate MNs revealed conservation of the potential regulators with divergent transcription factor (TF) networks through which expression of MN genes is differentially regulated. TF networks in little skate MNs are much simpler than those in mouse MNs, suggesting a more fine-grained control of gene expression operates in mouse MNs."

As one can see, without functional data in little skate, the claim that the TF networks are much simpler is not substantiated simply by ATACseq and predicted binding sites.

A similar claim on Page 17, line 338 indicates the same propensity to overstate these claims:

"As illustrated in the Figure 5C, a greater number of shared TFs binds to their downstream TFs in mouse MNs than in skate pec-MNs, allowing an intricate control of gene expression and thus the more complex nervous system of mouse compared to that of skate"

Again, there was no demonstration of little skate TFs binding to any downstream TF genes, only predicted binding sites. Thus, the claim is unsubstantiated.

These examples indicate an overall propensity by the authors to gloss over the fact that no functional connections between any TFs or genes were experimentally demonstrated in little skate. I do not believe it is appropriate to substitute binding motif enrichment for experimentally determined regulatory connections when inferring gene regulatory networks in something as complex as vertebrate development. There are a number of reasons why this is problematic.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Little skate genome exposes the gene regulatory mechanisms underlying the evolution of vertebrate locomotion" for further consideration by eLife. Your revised article has been evaluated by Catherine Dulac (Senior Editor), myself (reviewing editor), and 3 reviewers.

The revised manuscript has been significantly improved by the validation of RNA-Seq findings, the re-analysis of RNA-Seq and ATAC-Seq datasets, and the requested text changes. However, there are some remaining issues that need to be addressed, as outlined below (please see detailed comments by reviewers #1 and #3):

Essential revisions:

1. Please clarify whether you performed ATAC-seq from mouse MNs.

2. The findings on Snail1 are not described, and this part should be removed.

3. Please address the concerns raised by reviewer #3 about Figure 5.

4. We acknowledge that the revised version has toned down most claims on gene regulatory mechanisms, but we further suggest toning down the claim made in the title of the paper.

5. The manuscript should be edited for language and grammatical errors and carefully proofread.

Because your manuscript provides valuable datasets (e.g., little skate genome, new RNA-Seq data, new ATAC-Seq data), myself and all reviewers agree that your manuscript should be considered under the "Tools and Resources" article type.

Reviewer #1 (Recommendations for the authors):

The manuscript is much improved, as the authors have addressed a number of the major previous concerns, including re-analyzing RNA-seq data, generating a new set of mouse RNA-seq data, and validating their results with in situ hybridization. The new analysis seems much more convincing than the previous one. Some lingering concerns remain, mostly regarding figure 5 and the central claim of the paper, which is still not functionally supported. The authors did however tone down their claims and pointed out the limitations of the study.

(1) Did the authors perform ATAC-seq from mouse MNs? They show some data in figure 5 but it was not clear from the description of the methods or the results whether they performed the experiment.

(2) It seems that repeating the motif analysis of the ATAC-seq data gave completely new regulatory factors for FoxP1, even though the same regions as in the original manuscript are shown. It appears that Snai1 is no longer on the list so the experiment in the supplemental figures testing its function is somewhat moot. The authors also do not describe the experiment at all in the Results section so it should be taken out.

Reviewer #3 (Recommendations for the authors):

The revised manuscript has made important efforts in answering some of the raised concerns but did not address other key issues, particularly at the end of the manuscript.

The description of the little skate genome is, with no doubt, useful for the field of Evolutionary Biology. Then authors, re-analyse previously published experimental data and compare differential gene expression between isolated pectoral motorneurons and a mixed population of the tail spinal cord of little skate (Figure 2) and differential accessible chromatin regions between Fin motorneurons (Pectoral+pelvic) compared to a mixed population of the tail spinal cord (Figure 4). These two figures are descriptive and it is unclear what insights are provided by the comparison of these heterogeneous populations of cells. Thus do not seem to constitute a great advancement in the understanding of gene regulatory networks present in the little skate or their evolution.

In the new version of the manuscript authors now compared homologous motorneuron populations of the little skate, mouse, and chick, which reveals a remarkable degree of conservation of the transcriptomes in the 3 species (Figure 3), which is even higher when considering possible paralog substitutions in the few divergently expressed genes. This is radically different from the initial version of the manuscript and I think is an important observation.

Finally, the authors attempt to describe and compare motorneuron gene regulatory networks in mouse and skate in Figure 5. I think this is the weakest part of the manuscript, not only I found it hard to follow, not clearly explained, and using vague terms and overstatements but in addition the methodology and strategy for the analysis seem incorrect, leading to potentially wrong conclusions.

To start, it is unclear to me what is exactly the mouse motorneuron population that is being compared and how equivalent it is to the mixed Pectoral and pelvic motorneuron population from the little skate.

More importantly, Figure 5A: authors describe 18 TF motifs commonly enriched in mouse and skate MN ACRs, among which 6 TFs predicted to bind those motifs are expressed both in mouse and skate. What does this mean? Is this overlap biologically meaningful? How many would overlap if enriched motifs in skate ACRs are compared to motifs in mouse ACRs of a non-related neuron type at a similar developmental stage, such as cortical interneurons cortical projection neurons? Less? More? similar number?

Authors then look for motif enrichment of these 6 common motif/TFs in ACRs of other expressed TFs (either expressed both in mouse and skate or only in one of them). It is unclear why TFs with enriched motifs in mouse and skate should be upstream of the other TFs, it is equally possible that the 6 common motif/TFs are downstream of the expressed TFs. In addition, using the term "interactions" for motif enrichment of one TF in the ACRs of another TF is an overstatement.

It is also striking that "interactions" of the 6 mouse common motif/TFs seem equally prevalent within ACRs of mouse-expressed TFs compared to ACRs of TFs expressed in skate but not in mouse. Similarly, for the skate data, motif enrichment in ACRs of commonly expressed TFs or TFs only expressed in the skate is not higher than in ACRs of TF expressed in mouse only. These results again raise doubts if this analysis is meaningful at all. Would it be different using just randomly picked ACRs from other TFs not expressed in MN? Finally, as already mentioned in the first review, the increasing number of motifs for mouse TFs could be again due to methodological limitations (based on known motifs in mouse compared to skate, etc) but not biologically meaningful, it should be stated right away when described and not as a separate paragraph in the section of limitations for the study.

Considering all these methodologic concerns, together with the lack of any experimental validation of predicted binding sites for any of the TFs, it would be advisable to completely remove that figure.

In summary, the manuscript has valuable information, namely the description of the little skate genome and the comparison of mouse, chick, and little skate MN transcriptome. It also provides a description and comparison of some heterogeneous populations of neurons in little skate which provide limited insights into gene regulation in skate motorneurons. Most importantly, I think the last part of the manuscript (Figure 5) is below the standards required for a journal such eLife. Unfortunately, I don´t think the paper, in its current revised format, provides any mechanism underlying the evolution of vertebrate locomotion as stated in the title.

Other comments:

Authors constantly use the term "MN genes" or similar expressions when should be referring to "MN expressed genes" or "MN enriched genes". Other non-accurate expressions:

"Number of predicted TFs enriched" when it refers to TF motif predictions, "expression of each predicted TF" when meaning "TF expression for the corresponding TF enriched motif ", "predicted shared TFs found in MN ACRs" meaning " predicted shared enriched TF motifs found in MN ACRs", etc.

This lack of accuracy makes it harder for the reader to follow the text.

Methods include snail cDNA electroporation, but I don't think those results are included in the manuscript.

In figure 4D, the legend states ACR group but would be clearer to label as Motif category or Motif distribution in ACR categories.

Line 251: "Together with the predicted binding sites of the Hox proteins, the binding sites of Foxp1 and Pbx1 and Lhx3, which are well-known regulators in MN(31-33), were enriched in shared ACRs and fin-MN-specific and tail-SC-specific ACRs, respectively (Figure 4D)"

However in the figure Pbx1 is also in the shared category as Foxp1, not in fin-MN specific, correct?

Why Figure 5 shows common TFs only 16 TFs, if figure 3 shows many more?
