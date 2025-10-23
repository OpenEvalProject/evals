# Peer review - Round 1

Editors:
- Michael R Green, Howard Hughes Medical Institute, University of Massachusetts Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.45672.024](https://doi.org/10.7554/eLife.45672.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Tumor suppressor SMARCB1 suppresses super-enhancers to govern hESC lineage determination" for consideration by eLife. Your article has been reviewed by Jessica Tyler as the Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study addresses the role of the SMARCB1 subunit of the ATP-dependent SWI/SNF chromatin remodeling complex in regulating gene expression in human embryonic stem cells (hESCs) before and after differentiation. Study of SMARCB1 is particularly important, because mutations in this subunit are strongly associated with pediatric neural tumors. The authors compare gene expression (RNA-seq) and chromatin accessibility (ATAC-seq) in control and SMARCB1 knockdown (KD) hESCs made using a lentivirus carrying a dox-inducible shRNA. The effects of initiating differentiation into neural cells, endoderm or mesoderm are also assessed using the same methods.

In undifferentiated hESCs, many genes are activated in response to knockdown, whereas only a few are repressed, indicating that SMARCB1 has a primarily repressive role. This observation is particularly true of genes with bivalent chromatin marks. Changes in chromatin accessibility occur primarily at enhancers: the accessibility of active enhancers decreases in KD cells (LA peaks), indicating that SMARCB1 promotes accessibility at active enhancers. In contrast, super-enhancers show the opposite trend, indicating that SMARCB1 represses their function (HA peaks). They find that SMARCB1 KD hESCs can be differentiated into mesoderm or endoderm but not neural cells. In the latter case, only some neural genes are induced and many genes characteristic of stem cells remain active. They conclude that SMARCB1 is needed for the initial stages of neural induction, but not for mesoderm or endoderm induction. In particular, the hESC super-enhancers remain accessible in neurally induced KD cells.

Overall, the reviewers found the study to be interesting and felt that the major claims were supported by the presented results. The reviewers did express some difficulty in following the text in places and requested that more explanation of the analyses be included in the text.

Essential revisions:

1) In Figure 2B, the aim appears to be to correlate changes in ATAC-peaks with changes in gene expression. This is tricky because the target genes of specific enhancers are unknown and difficult to infer because they are often separated by large genomic distances. The reviewer did not understand the method used in Figure 2B to calculate the probability of association – what assumptions underlie this analysis? Detailed explanation in the text is needed.

2) The reviewer also found the "dot plots" such as those in Figure 2C/D difficult to understand. In Figure 2C, I think they have calculated the probability of low (LA) and high (HA) accessibility ATAC-peaks coinciding with enhancers and super-enhancers found in 98 human cells using data from other papers (subsection “SMARCB1 KD differentially affects chromatin accessibility at key regions associated with hESC identity”). Some significant dots in Figure 2C are labeled – but what cell type do they belong to? Presumably the current experiments. The reviewer was not sure why they did this analysis. Isn't it sufficient to examine the correlations between enhancer types and LA/HA peaks in the cells used here? The justification for this analysis seems obscure, but perhaps I'm missing something. More explanation is needed in the text.

3) What about the promoters of differentially expressed genes? Do their accessibilities change as expected from the RNA-seq data?

4) Figure 1F shows the significance of overlap between up- or down-regulated genes and the genomic binding sites of numerous regulatory proteins or histone modifications. In this figure, it would be reasonable to include the binding sites of any SWI/SNF subunits for which ChIP-seq data are available to better assess the extent to which the gene expression changes are direct.

5) In hESCs, many more genes go up than down in SMARCB1 KD cells, suggesting SMARCB1 largely represses (or at least limits) gene expression. On the other hand, many more regions become less accessible than more accessible in SMARCB1 KD hESCs, which suggests a greater role in activation of transcription. How do the authors explain these phenotypes?

6) Figure 2B, Figure 4D, and Figure 5C seem strange in that no matter how large the bin size surrounding a region of interest (e.g., differential ATAC peaks), the association with differentially expressed genes is statistically significant. For lower accessibility peaks in Figure 2B, significance actually increases as the bin size increases from 300 to 500 kb from the aggregate ATAC-seq peak center. This seems unlikely. Furthermore, Figures 4D and Figure 5C seem to flatten out on the right as bin size gets very large, but they seem to approach an asymptote of -log10(p) = 2-3 (e.g., p = 0.01-0.001). Shouldn't they approach -log10(p) = 0? How might a set of "peaks" consisting of random locations in the genome (with the number of different random locations equal to the number of real peaks) look when subjected to the same analysis? This comparison could be added to these figures.

7) Subsection “SMARCB1 is required for the initial stages of neural induction but is dispensable for endodermal and mesodermal induction”: "In contrast, some of the genes with the highest expression in SMARCB1 KD vs. control cells included the neural differentiation markers FOXG1 (FD = -28.2), DLK (FD = -25.9), and LHX2 (FD = -14.2) (Supplementary file 3) (Watanabe et al., 2005, Porter, 1997, Tedeschi and Bradke, 2013)." Here, I think "highest" should be either "lowest" or "most strongly repressed".
