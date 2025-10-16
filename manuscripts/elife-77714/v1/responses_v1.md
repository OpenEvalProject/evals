# Author response - Round 1

Authors:
- Ariel Ogran ([ORCID: 0000-0002-9411-3537](https://orcid.org/0000-0002-9411-3537))
- Tal Havkin-Solomon
- Shirly Becker-Herman
- Keren David
- Idit Shachar
- Rivka Dikstein ([ORCID: 0000-0002-6251-4723](https://orcid.org/0000-0002-6251-4723))

## Response text

DOI: [10.7554/eLife.77714.sa2](https://doi.org/10.7554/eLife.77714.sa2)

Essential revisions:

1) It was found that the evidence of expression of putative N-terminally truncated proteins is required to fully support the proposed model. Notwithstanding that the overarching characterization of N-terminally truncated proteins across the proteome may be out of the scope of the paper, it was thought that the authors should at least provide evidence of in-depth-discussed proteins (e.g., chromatin modifiers). Moreover, it was thought that orthogonal techniques (e.g., 5'RACE) should be used to confirm the results of CAGE studies.

As suggested, we now performed 5’ RACE to validate the CAGE results by picking four chromatin modifiers and examining the upregulation of the alternative TSS in Eu-TCl1 mice. The 5’ RACE was done using template switching RT enzyme mix (NEB), Template Switching Oligo (TSO) and a gene-specific reverse primer common to the canonical full-length isoform and the N’ terminally truncated one. In order to compare the transcription level of the truncated isoform between Eu-Tcl1 and WT mice, isoform-specific primers were used in the qPCR assay. The results of the 5’RACE-qPCR authenticate our CAGE-seq results, showing upregulation of the isoforms originating by alternative TSS of the four selected DNMT3a, CHD1, KDM4A and SIRT2 (see Figure 3—figure supplement 1 in the revised manuscript).

Notably, we also confirmed that these isoforms are efficiently translated to proteins by combining CAGE with polysome profiling (Figure 5). Other proteomic approaches such as mass spectrometry (MS) and western blot for detecting the N-terminally truncated/modified proteins are less suitable. With the MS, the peptides derived from N-terminally truncated proteins are shared with the full-length protein. In western blot, there are several limitations that include the finding of high-quality antibodies directed against the C-terminus of the candidate proteins, the ability to distinguish between truncated and proteolytically cleaved protein, and the ability to predict the new translation initiation site accurately, the ORF and the size of the protein isoform. This is particularly challenging since, in most cases, the new promoters are located within an intron. Nevertheless, we performed multiple western blots by purchasing antibodies against the C-terminus of selected proteins, but we could not identify the truncated protein with high certainty.

2) Link between TCL1-dependent alterations in transcription site selection and/or promoter usage and chromatin remodelling was found to be largely correlative. Based on this, it was thought that the authors should provide more mechanistic data to support the role of apparent TCL1-dependent alterations in chromatin factors and perturbations in chromatin structure.

By combining our data with data from the literature, a mechanism by which TCL-1 promotes the activation of cryptic promoters is emerging. We briefly referred to this mechanism in the discussion of the original manuscript. In the revised manuscript, we further expand it with more specific details. Specifically, a previous study reported decreased DNA methylation levels in Eµ-Tcl1 mice and CLL patients and demonstrated an interaction between TCL1 and the de novo DNA methyl transferases DNMT3A and 3B along with inhibition of their enzymatic activity (1), suggesting for direct inhibition of de novo methylation by TCL1 during leukemogenesis. In addition, it was reported that TCL1 promotes the Α Serine/Threonine-Protein Kinase (AKT) activity. As AKT signaling itself reduces Dnmt3a activity (2, 3), over-sensitization of the AKT by the constitutively overexpressed TCL1 is likely to reduce DNMT3A activity further. Our findings complement these observations by uncovering another mechanism of impairment of DNMT3A activity via activation of an internal promoter and generation of large amounts of truncated inactive protein (Figure 5F, left). All these mechanisms inhibit DNMT3A and DNA methylation in these cells in an additive manner. We, therefore, propose that downregulation of DNMT3A directly and indirectly by TCL1 is the initial trigger for the activation of cryptic promoters in Eµ-Tcl1 CLL cells, which is further augmented by the activation of cryptic promoters of other chromatin regulators in a feed-forward loop and by activation of c-myc (see more details in the discussion).

(1) Palamarchuk, A., Yan, P.S., Zanesi, N., Wang, L., Rodrigues, B., Murphy, M., Balatti, V., Bottoni, A., Nazaryan, N., Alder, H. et al. (2012) Tcl1 protein functions as an inhibitor of de novo DNA methylation in B-cell chronic lymphocytic leukemia (CLL). Proceedings of the National Academy of Sciences of the United States of America, 109, 2555-2560.

(2) Yang, Qi, Wei Jiang, and Peng Hou. "Emerging role of PI3K/AKT in tumor-related epigenetic regulation." Seminars in Cancer biology. Vol. 59. Academic Press, 2019.

(3) Popkie, Anthony P., et al. "Phosphatidylinositol 3-kinase (PI3K) signaling via glycogen synthase kinase-3 (Gsk-3) regulates DNA methylation of imprinted loci." Journal of Biological Chemistry 285.53 (2010): 41337-41347.

3) As outlined in the individual reviews, some important issues were observed pertinent to bioinformatic analyses. It was also thought that several important controls were missing. For instance, a more detailed rationale should be provided for cut-offs/thresholds used in bioinformatic approaches.

As suggested, we now provide explicit reasonings for the bioinformatics cut-off/thresholds described in the method paragraph titled “CAGE tag clustering, quantification and analysis<milestone-start />״<milestone-end />. After counting CAGE reads into defined tag clusters (TC), we filtered out TCs with less than one tag per million (TPM) to remove very lowly expressed TC and obtain likely biological relevance. Where eRNA prediction is based on finding two balanced bidirectional (sense and antisense) TCs, we set the threshold of the Bhattacharyya coefficient (BC) to 0.95, where the value of 1 corresponds to perfectly balanced sites. In addition, when we measured the width of TCs of pooled CAGE tags, we used a 10-90% interquartile range (IQR) threshold to dampen the effect of possible straggler tags that can greatly extend the width of a TSS candidate without contributing much to expression. Deseq2-based results of differentially expressed TCs were independently filtered by setting the α argument to 0.05, which is the significance cutoff used for optimizing the independent filtering. For the analysis of differential TSS Usage (DTU) that was done by the diffSpliceDGE method of the edgeR package, we used a subset of genes with more than one TSS to analyze. By considering only TSS that correspond to more than 10% of total gene expression, we guarantee meaningful detection of promoter shifting events during CLL transformation.

The reproducibility of the results between the two CAGE replicates was also not clear.

We have added coefficient scores of CAGE library replicates derived from the RNA samples of Eu-TCL1 and WT, as well as CAGE library replicates from the polysome profiles of Eu-TCL1. (See Figure 1 —figure supplement 1A and Figure 5 – —figure supplement 1A). All replicates have shown high coefficient scores by the Pearson pairwise-correlation test, indicating the high reproducibility of our CAGE results.

An apparent lack of application of unique molecular identifiers in the CAGE approach was also observed.

Indeed, using the unique molecular identifiers (UMI) sequences for removing PCR-originated read duplicates became a gold standard and in 2017, the nanoCAGE protocol introduced the UMIs to the CAGE methodology. However, this method is claimed to be inferior to the classic CAGE method for the following reasons: (a) the template switching method used by nanoCAGE was shown to be sequence-dependent and, therefore, is potentially biased (Tang et al. 2013, Nucleic Acids Res 41: e44 10.1093/nar/gks1128) (b) the nanoCAGE was optimized for the use of a small amount of starting RNA (50 ng) that lead to low-complexity libraries with high levels of duplicates (Cvetesic, Nevena, et al.2018). Also, it was claimed by Cvetesic, Nevena, et al., that the synthesis of truly random UMIs is problematic and subject to variability, thereby obscuring its use. Taking all these into consideration, the sequencing errors of UMI sequences (Smith et al. 2017), our ability to start with a higher amount of 5 ug total RNA to reduce PCR cycles to a minimum of eight, and by that avoid amplification biases, we decided to follow the classic CAGE method.

In addition, concerns were raised regarding the application of log-ratios to calculate translational efficiency.

We wish to clarify that we did not use the log-ratios method for TE calculation as reported in (PMID: 21115840) and noted by Reviewer 1. Briefly, the calculation method we used is based on the ratio of the counts of the polysome fractions to the free fraction (see p. 9)

Finally, there was a lack of loading controls in some of the Western blots.

We have now added the missing loading control using antibodies against GAPDH (see Figure 3B).
