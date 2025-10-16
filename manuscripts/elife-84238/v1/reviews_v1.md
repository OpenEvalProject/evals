# Peer review - Round 1

Editors:
- Bérénice A Benayoun, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84238.sa0](https://doi.org/10.7554/eLife.84238.sa0)

Rossi et al. carry out a valuable characterization of the molecular circuitry connecting the immunomodulatory cytokine BAFF (B-cell activating factor) in the context of cellular senescence. They present solid evidence that BAFF is upregulated in response to senescence, and that this upregulation is partially driven by the immune response-regulating transcription factor (TF) IRF1, with potential cell type-specific effects during senescence. Ultimately, these results strongly suggest that BAFF plays a senomorphic role in senescence, modulating downstream senescence-associated phenotypes, and may be an interesting candidate for senomorphic therapy.


---

# Peer review - Round 1

Editors:
- Bérénice A Benayoun, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84238.sa1](https://doi.org/10.7554/eLife.84238.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Pleiotropic effects of BAFF on the senescence-associated secretome and growth arrest" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Satyajit Rath as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers discussed the manuscript, and believe the study is interesting but has some concerns of a technical and methodological nature that they believe need to be addressed. Specifically:

1. Some specificity and technical controls are currently missing:

– Technical controls: validating siRNA specificity/efficiency by Western, antibody specificity, consistency between panels.

– Biological control: changes in aging tissues, specificity to senescence vs. quiescence, degree of senescence induction, cell type specificity vs. primary/cancer specificity (i.e. also include primary monocytes).

2. There also are some methodological issues to be cleared up to ensure data robustness.

– See comments on issues with the RNAseq analysis pipeline as currently implemented

– See comments on the need to use at least 2 independent siRNA to exclude that observed phenotypes may be due to off-target effects.

– See comments on the need to use 2-3 RT-qPCR normalizing amplicons to avoid noise due to housekeeping genes not being constant across conditions

Reviewer #1 (Recommendations for the authors):

1. The model proposed by the authors, as currently illustrated in Figure 7, is too general to be supported by the data. While this reviewer agrees that the contributions of BAFF to senescence responses are likely to be cell-type specific, it is unclear that p53 and NF-κB actually play differential roles in senescent fibroblasts and senescent monocytes. For the series of monocyte experiments, cancerous THP-1 cells were used which, as stated by the authors, harbor mutations in p53 that prevent its expression. Thus, it is unclear whether the p53 response is specific to fibroblasts, or whether the lack of a p53 response is an artifact/feature of this specific cancer monocytic cell line. That is, it is still within the realm of possibility that the p53 response may be influenced by BAFF in non-cancerous, senescent monocytes with intact p53. This remains an open question. Since the authors have access to mice based on some of the analyses, a relatively easy source of monocytes with intact p53 can be from bone marrow, which would help strengthen the point they make on the impact of NF-κB. The model, and its discussion, should be revised to take this caveat into account (or additional experiments in WT/primary cells should be added).

2. Currently, RT-qPCR data is normalized to a single reference gene (ACTB or GAPDH), e.g. in Figure 1G. However, results using a single reference gene are often unstable, since no gene is truly ever impacted by outside stimuli. It is considered a best practice to include multiple reference genes when conducting this type of analysis [PMID: 19246619], for instance using the geometric mean of the Cts of 3+ normalizing amplicons. Although control using 18s rRNA is mentioned in Figure legend, it does not seem like it was used to perform normalization of the RT-qPCR results shown in Figure 1G.

2.1. Importantly, the cytoskeleton is known to be broadly impacted by senescence [PMID: 15742196], which makes ACTB a poor choice for a normalizing amplicon. Consistent with using ACTB as the single "housekeeping" gene being an issue, ACTB protein levels are highly variable in the spleens of Dox-treated mice in Figure 1H, suggesting that mRNA levels may also be highly variable. Thus, presented RT-qPCR data should be revised or re-run accordingly using a panel of normalizing amplicons (unless RNA-seq has been performed for the same/similar samples and the RNA-seq results can be shown as well for discussed genes, as RNA-seq normalization bypasses housekeeping gene-related issues).

2.2. In addition, if different normalizing amplicons are used for different panels, please make sure to note which were used for which, as well as a rationale for using different ones for different analyses.

3. The authors state that DEGs were defined as those genes with padj < 0.05 and absolute log2 fold change > 1. However, it is unclear how fold change filtering was implemented. Fold-change filtering, if not implemented into the statistical model used to identify DEGs, can lead to poor FDR control and is not appropriate (see PMC2654802). Wald tests in DESeq2 can be constructed with thresholds; please run the analysis in this manner if fold change filtering is currently carried out post hoc using the default settings. Alternatively, DESeq's default settings can be used without fold change filtering – if the number of DEGs is the issue, a smaller FDR threshold can be used (e.g. FDR < 0.01). Additionally, please ensure that DEGs are called uniformly throughout the manuscript (or explicitly justify differences between panels). In contrast to the methods section, Figure 3B implements an abs (fold change) > 1.3 thresholds.

4. Experimental groups were statistically analyzed using unpaired Student's t-tests. Though the data were tested for normality, it is difficult to say whether a sample size of 3 actually came from a normal distribution. To avoid making normality assumptions, analyses should be carried out using non-parametric tests instead, such as Wilcoxon tests. Most effects identified in the manuscript will likely be robust enough to this change.

5. For reproducibility of code and analyses, all analytical scripts for this study should be deposited in a repository such as GitHub or made available as a Supplementary file.

Reviewer #2 (Recommendations for the authors):

While we believe, the manuscript as a whole is close to publication quality, one of the major concerns is the reliance on cell lines as the major model system used, as opposed to primary cells and more in-depth in vivo analysis to strengthen the relevance of BAFF in aging. Please see our comments and concerns below:

1) The amount of DNA damaging stimuli seems fairly weak (5gy IR and 10nM Doxo). Can the authors determine via cell cycle analysis or some other assay, what percent of cells are undergoing cell cycle arrest?

2) Likewise, in Figure 1 the SA-B-GAL staining in THP-1 cells seems to be only in a small subset of cells, can the authors also quantify the staining perhaps via the use of C12FDG using a plate reader or preferably flow cytometry?

3) Figure 1: In addition to doxo-treated mice, can the authors also measure BAFF expression in old vs young tissues?

4) Pg 6: "In all cases, BAFF mRNA levels increased during senescence (Figure 1—figure supplement 1E) and secreted BAFF was generally elevated with senescence, although it was undetectable in hVSMCs, and the levels were overall higher in THP-1 cells (Figure 1D and Figure 1—figure supplement 1F)." The total BAFF in the ELISA experiments in THP-1 and WI-38 cells is equivalent, in fact, the irradiated WI-38 cells have more expression than the irradiated THP-1 cells.

5) Pg 6: "Next, we investigated if the rise in BAFF mRNA with senescence in THP-1 cells was the result of transcriptional or posttranscriptional regulatory mechanisms" Please explain the rationale for asking this question.

6) Figure 2G: The authors show that IRF1 and IRF2 are induced during senescence and may drive BAFF expression. Thus, in addition to IRF1 can the authors also silence IRF2 to test its effect on BAFF mRNA expression.

7) In Figures 4B and 4C, can the cell viability and cell proliferation be measured via flow cytometry which is more quantitative?

8) Figure 5: To further define the BAFF signaling mechanism, can the authors also silence or KO the different BAFF receptors to determine which is the major receptor necessary for BAFF signaling in senescent THP-1 and fibroblast?

9) Figure 5: We suggest the authors perform an NFkB luciferase assay to confirm BAFF silencing impacts NFkB gene expression.

10) Pg 12 Figure 6: "To gain a more complete understanding of the role of BAFF in senescence, we investigated its function in primary fibroblasts, which are well-established models for senescence and express the senescence-relevant protein p53" The subsequent experiments were not performed in primary fibroblast.

11) Lastly, as mentioned above the paper would be strengthened if some of the key experiments can be performed in primary mouse or human monocytes and fibroblast to confirm BAFF regulates senescence in cells that are more relevant to normal physiology.

Reviewer #3 (Recommendations for the authors):

1. Figure 1. Test whether the upregulation of BAFF is specific to senescence, or also in reversible quiescence arrest.

2. Figure 1, Supplement 1G. Show negative control IgG for immunofluorescence.

3. All results with siRNA should be validated with at least 2 individual siRNAs to eliminate the possibility of off-target effects.

4. To confirm a role for IRF1 in the activation of BAFF, the authors should confirm the binding of IRF1 to the BAFF promoter by ChIP or ChIP-seq.

5. Key antibodies should be validated by siRNA knockdown of their targets, for example, TACI, BCMA, and BAFF-R in Figure 5. Note that there is an apparent discrepancy between BCMA data in Figure 5B vs 5C.

6. Figure 5E. Negative/specificity controls for this assay should be shown.

7. Hybridization arrays such as Figure 5H, Figure 6 – Supplement 1I, and Figure 6H should be shown as quantitated, normalized data with statistics from replicates.

8. Figure 6B – Supplement 1. Controls to confirm fractionation (i.e., non-contamination by cytosolic and nuclear proteins) should be shown.

9. Figure 6A. Knockdown of BAFF should be shown by western blot.

10. Figure 6G. Although BAFF knockdown decreases the expression of p53, p21 increases. How do the authors explain this?
