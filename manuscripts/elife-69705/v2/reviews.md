# Peer review - Round 1

Editors:
- Jerry L Workman, https://ror.org/04bgfm609 Stowers Institute for Medical Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69705.sa0](https://doi.org/10.7554/eLife.69705.sa0)

This work will be of wide interest to the transcription community as it is the first evidence that the cofactor, TRRAP, which is known as a transcriptional activator, can also act as a transcriptional repressor. The new experiments added to the revised manuscript further support this conclusion.


---

# Peer review - Round 1

Editors:
- Jerry L Workman, https://ror.org/04bgfm609 Stowers Institute for Medical Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69705.sa1](https://doi.org/10.7554/eLife.69705.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The TRRAP transcription cofactor represses interferon-stimulated genes in colorectal cancer cells" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Jerry L Workman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kevin Struhl as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The manuscript by Detilleux and coworkers continues studies by the Helmlinger group on the conserved TRAPP subunit of the SAGA and TIP60 (NuA4 in yeast) complexes. In this manuscript the authors create auxin-inducible degron allelles of TRAPP and of its TTT chaperone TELO2 in the HCT116 colorectal cancer cell line. In previous work the group showed that the TTT complex stabilizes TRAPP, and indeed degradation of TELO2 reduces nuclear accumulation of TRAPP. As expected direct auxin-induced degradation of TRAPP is more rapid, and inhibits HTC116 cell growth already after one day instead of two days for TELO2. Loss of TRAPP from the SAGA and TIP60 is significant, but not complete. RNAseq analysis showed that reduced TELO2 and TRAPP mostly leads to a reduced expression of genes, including MYC and E2F target genes, which is expected given the documented role of TRAPP as a co-activator for MYC ad E2F.

Unexpected is the increase expression of the interferon type 1 group of genes (ISGs). The authors investigated regulation of the ISG pathway to find that TRAPP depletion mostly affects IRF9 expression at the mRNA and protein levels and to a lesser extent IRF7 expression. IRF9 and IRF7 are critical transcription factors for the ISG pathway and these observations offer an explanation for the induction of interferon type 1 genes after TRAPP depletion. The authors continue to show by 4SU labeling that IRF9 and IRF7 are transcriptionally induced and by CUT&RUN-PCR that TRAPP binds to the promoter regions of these genes. Re-expression of TRAPP reverses these effects. In order to dissect which of the TRAPP containing complexes several SAGA and TIP60 complexes are targeted by siRNA knock-down, but this does not provide clear distinction between SAGA and TIP60. In general, the exact mechanistic details of TRAPP-mediated repression of gene transcription have not been worked out, but the current work provides a strong basis for future studies addressing this.

Major open issues:

1) The reviewers did not think the authors need a detailed understanding of the repression mechanism. However, the basic conclusion has to be correct, and the various models of "indirect effect" such as TRRAP activating a repressor (which are very plausible and even more likely) are inconsistent with the main conclusion. The interest of the paper is that, although TRRAP is well described as a positive factor, it has a direct negative effect on a set of genes. However, the "indirect" models involve TRRAP function in the usual positive manner, which isn't novel or even interesting. Indirect effects happen all the time and are rarely of sufficient interest for a journal like eLife (and this paper is not an exception to this). More generally, reducing the function of a chromatin-modifying activity usually leads to both up- and down-regulation of many genes. So finding genes that behave in the opposite fashion from what is expected happens all the time. Without demonstrating a direct negative effect, we don't see the advance here.

One experiment would greatly help show a direct negative effect. A kinetic experiment where one rapidly deplete TRRAP and simultaneously assays TRRAP association (ChIP) and transcription (Pol II occupancy or better yet (PRO-seq or Net-seq) over multiple time points. For a direct effect, loss of TRRAP occupancy should be concomitant with increased transcription).

A good approach to this would be a time course genome wide CUT and RUN coupled with PRO-seq or Net-seq

2) It is unclear why the authors did not choose to sequence the DNA from the TRAP CUT&RUN experiment, but rather performed (a more cumbersome) PCR analysis. A genome-wide CUT&RUN dataset for TRAPP would have allowed a direct comparison with their TELO2 and TRAPP depletion RNAseq datasets.

3) The experiments implicating both TIP60 and SAGA in the repression of the IRF9 gene are not convincing. This part should be removed from the manuscript as substantial additional work would be required to make this claim convincing. To argue for a direct affect ChIP/PCR experiments on IRF9 are required. Interpretation of the expression changes observed on knock down of SAGA and TIP60 components are complicated by different efficiencies of the knockdowns and by the fact that these components can be components of other complexes and/or function independently in sub-complexes. Finally, different genes require different parts of SAGA for their expression, thus it is likely that different subunits would have different affects on any repression mechanism

4) The authors mention in the methods section that heterologous DNA was used to normalize CUT&RUN experiments but make no reference to this normalization in their figures or explained in the methods. In the presented data it is certainly not explained what "AU" (occupancy levels) corresponds to technically, while IgG controls are seemingly not used as reference point. The numbers presented are extremely variable and it is difficult to judge relative TRRAP binding to the 3 different promoters. If the CUTnRUN works so well, why not performing NGS and get a global view of TRRAP binding on the genome?

5) In addition, a drop in MYC occupancy at MIR17-HG promoter following auxin induction is observed and the authors explain this by a role for TRRAP in stabilizing MYC at its target genes. However, non-specific effects of auxin on CUT&RUN results are not ruled out. Profiling an additional factor that should not be affected by TRRAP depletion would be necessary to validate and increase confidence in the results obtained in Figure 6, where the authors look at the dynamics of ISG regulation by TRRAP over a time course after removing auxin by coupling CUT&RUN to RT-PCR analyses, and to confirm that TRRAP indeed is a direct repressor of IRF9.

Reviewer #1 Recommendations for the authors:

The experiments implicating both TIP60 and SAGA in the repression of the IRF9 gene are not convincing. This part should be removed from the manuscript as substantial additional work would be required to make this claim convincing. To argue for a direct affect ChIP/PCR experiments on IRF9 are required. Interpretation of the expression changes observed on knock down of SAGA and TIP60 components are complicated by different efficiencies of the knockdowns and by the fact that these components can be components of other complexes and/or function independently in sub-complexes. Finally, different genes require different parts of SAGA for their expression, thus it is likely that different subunits would have different affects on any repression mechanism

Reviewer #2 Recommendations for the authors:

An important recommendation on current manuscript is the inclusion of library sequence TRAPP CUT&RUN fragments rather than performing a CUT&RUN-qPCR.
