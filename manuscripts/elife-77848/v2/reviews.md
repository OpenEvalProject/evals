# Peer review - Round 1

Editors:
- Adèle L Marston, https://ror.org/01nrxwf90 University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77848.sa0](https://doi.org/10.7554/eLife.77848.sa0)

This manuscript will be of interest to scientists working on genome organisation and transcriptional control of myelination during mammalian brain development. The authors combine diverse and complementary experimental approaches to generate insights into how DNA looping contributes to transcriptional regulation in functionally specialised cell types. The experiments have been rigorously performed and the main conclusions are justified.


---

# Peer review - Round 1

Editors:
- Adèle L Marston, https://ror.org/01nrxwf90 University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77848.sa1](https://doi.org/10.7554/eLife.77848.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "STAG2 promotes the myelination transcriptional program in oligodendrocytes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Adèle L Marston as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Jessica Tyler as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Andrew J Wood (Reviewer #2); Simone Di Giovanni (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Although the NexCre system is widely used, there is no clear consensus in the literature where the Cre recombinase is expressed. While Giusti et al. 2014 (J. of psychiatric research) reported neuronal and astroglial expression, Goebbels et al. 2006 (Genesis) reported neuronal only expression. A more detailed characterization of the cell type specificity and timing of Stag2 expression and ablation in the NPCs lineage would be useful. This is important to understand whether OLs are particularly sensitive to Stag2 deletion or whether Stag2 has not been deleted in neurons and astrocytes. From Figure 4A and FigS6B, neurons and astrocytes are hardly retrieved from WT brains, so it is difficult to compare Stag2 expression level and ablation in these cells. While it is clear that OLs are affected by Stag2 KO, it is not certain that these are the only and main cell type affected. Along the same lines, since it is difficult to quantify cell composition from the RNAseq, due to different cell survival and purification, a better characterization of cell type numbers on histological section is needed to clarify if Stag2Cre mice have indeed a generally normal neuronal cell differentiation.

2. More details are required for the 3D chromatin structure analysis. Although the data are mainly in line with the literature, opposite to other work (Wutz et al., EMBOJ 2017; Pekowska et al., Nature 2017; Casa et al., Genome Res 2020), the authors did not find any TAD alterations. This might be related to the resolution used; the methods or legends do not state which resolution has been used. Please clarify and include this information in the figure legend, and make sure that at least 25 kb resolution is used for TAD analysis. You should report a summary of the sequencing data including the total reads obtained and, importantly the number of valid cis-pairs in each of their libraries etc.

3. Also for the Hi-C data: from Figure 5F and 5E, the correlation between the 2 biological replicates seems to be not very high; please comment. Since the effect is only on the loops and is quite modest, it is important that you demonstrate that it is reproducible and report whether this effect was seen in independent datasets, and whether the same loops were affected in each case.

4. Regarding the single-cell and purified OL RNAseq, only two biological replicates have been used, but three would be recommended.

5. Please provide a better discussion of what distinguishes genes that are or are not regulated by STAG2. On page 15, you speculate that STAG2 might interact with oligodendrocyte-specific transcription factors and be preferentially recruited to myelination genes. Preferential recruitment to myelination genes should be tested using the existing ChIP-seq data represented in Figure S8.

6. Similarly, all three of the models shown in Figure 7 appear to indicate that STAG2 ordinarily regulates transcription through the formation of promoter-anchored loops, via a mechanism that involves direct binding to the relevant promoter in question. STAG2 binding sites should therefore be enriched at promoters where loops are lost in the STAG2 mutant condition. You should determine whether this is the case and discuss the implications for their models if it is not.

7. Similarly, you hypothesise three possible ways for Stag2 mediated gene expression regulation. One is by assisting enhancer-promoter loops. The authors have generated H3K27ac Chip from purified OLs, and this could be used to map E-P loops and test their hypothesis.

8., Figure 6D – A gene with a better-defined role in myelination than Pls1 would be preferable to use as an exemplar locus here.

8. Please provide the list of DE genes, STAG2 genomic occupancy, or promoters anchored loops as a supplementary file. This will help the readability of the paper and will allow full disclosure of the dataset to the community. Furthermore, please provide the reviewer passkey for the GEO link.

10. The authors are recommended to perform GO and pathway analysis using some other tools in addition to IPA, like GSEA. Also, since the pathways shown in the chart in Fig2Da and 4G are the top enriched pathways, it would be useful if the authors could provide a list of all the enriched pathways. Furthermore, please clarify what you used as background for the enrichment analysis.

11. From the purified OL RNAseq, the authors found 271 down and 292 upregulated genes. Please clarify what these genes are. In Fig4G, you showed a pathway analysis of all the DE, and it is not clear which gene set has been used for FigS7E. It would be useful to characterize the UP and DOWN genes separately.

12. In the single-cell RNAseq, you have used nFeature_RNA(200-9500). This seems to be a very high threshold, with the risk to include cell doublets. Please disclose whether you can reproduce the same analysis using a lower threshold.

13. It would be useful to test using the Stag2 ChIP data in isolated OLs, whether loop loss is observed preferentially on Stag2 occupied sites and how STAg2 occupancy correlates with loop score of up/down/no DE genes.

14. A more detailed Methods section is required: for example, how many replicates for the sequencing, sequencing depth, the sequence of the probes, PCR primers, antibodies (codes and quantity); more details for the OL isolation procedure. Methods for Cas9 mediated KO are missing.

15. Similarly, Figure Legends need more details for clarity

Reviewer #2 (Recommendations for the authors):

(1) Page 8 – the statement " a mild reduction in the number of MOLs" should be changed to "a mild reduction in the proportion of MOLs"

(2) Page 12 contains the statement "Highly expressed genes might be more reliant on these loops for transcription and are preferentially downregulated by Stag2 loss". Please provide a reference to the data which support the second part of this statement.
