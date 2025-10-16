# Peer review - Round 1

Editors:
- K VijayRaghavan, National Centre for Biological Sciences, Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.102019.3.sa0](https://doi.org/10.7554/eLife.102019.3.sa0)

This is an important study that generates an inventory of accessible genomic regions bound by a transcription factor ZFHX3 within the suprachiasmatic nucleus in the hypothalamus and details the impact of its depletion on daily rhythms in behaviour and gene expression patterns. Analysis using circadian phase-estimation algorithms makes the argument that gene regulatory networks are at play and changes in gene expression of a few clock genes cannot account for the observed animal behaviour. While the transcriptome analysis is compelling, the data on the activity of the TF in rhythmic gene expression is solid, and interpretations that allow for direct and/or indirect roles have been incorporated.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102019.3.sa1](https://doi.org/10.7554/eLife.102019.3.sa1)

Summary:

Authors of this article have previously shown the involvement of the transcription factor Zinc finger homeobox-3 (ZFHX3) in the function of the circadian clock and the development/differentiation of the central circadian clock in the suprachiasmatic nucleus (SCN) of the hypothalamus. Here, they show that ZFHX3 plays a critical role in the transcriptional regulation of numerous genes in the SCN. Using inducible knockout mice, they further demonstrate that the deletion Of Zfhx3 induces a phase advance of the circadian clock, both at the molecular and behavioral levels.

Strengths:

- Inducible deletion of Zfhx3 in adults

- Behavioral analysis

- Properly designed and analyzed ChIP-Seq and RNA-Seq supporting the conclusion of the behavioral analysis

Comments on revisions:

The authors have properly addressed reviewers' issues.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.102019.3.sa2](https://doi.org/10.7554/eLife.102019.3.sa2)

Summary

ZFHX3 is a transcription factor expressed in discrete populations of adult SCN and was shown by the authors previously to control circadian behavioral rhythms using either a dominant missense mutation in Zfhx3 or conditional null Zfhx3 mutation using the Ubc-Cre line (Wilcox et al., 2017). In the current manuscript, the authors assess the function of ZFHX3 by using a multi-omics approach including ChIPSeq in wildtype SCNs and RNAseq of SCN tissues from both wildtype and conditional null mice. RNAseq analysis showed a loss of oscillation in Bmal1 and changes in expression levels of other clock output genes. Moreover, a phase advance gene transcriptional profile using the TimeTeller algorithm suggests the presence of a regulatory network that could underlie the observed pattern of advanced activity onset in locomotor behavior in knockout mice.

In Figure 1, the authors identified the ZFHX3 bound sites using ChIPseq and compared the loci with other histone marks that occur at promoters, TSS, enhancers and intergenic regions. And the analysis broadly points to a role for ZFHX3 in transcriptional regulation. The vast majority of nearly 40000 peaks overlapped H3K4me3 and K27ac marks, active promoters which also included genes falling under the GO category circadian rhythms. However, no significant differential ZFHX3 bound peaks were detected between ZT3 and ZT15. In these experiments, it is not clear if and how the different ChIP samples (ZFHX3 and histone PTM ChIPs) were normalized/downsampled for analysis. Moreover, it seems that ZFHX3 binding or recruitment has little to do with whether the promoters are active.

Based on an enrichment of ARNT domains next to K4Me3 and K27ac PTMs, the authors propose a model where the core-clock TFs and ZFHX3 interact. If the authors develop other assays beyond just predictions to test their hypothesis, it would strengthen the argument for a role in circadian transcription in the SCN. It would be important in this context to perform a ChIP-seq experiment for ZFHX3 in the knockout animal (described from Figure 2 onwards) to eliminate the possibility of non-specific enrichment of signal from "open chromatin'. Alternatively, a ChIPseq analysis for BMAL1 or CLOCK could also strengthen this argument to identify the sites co-occupied by ZFHX3 and core-clock TFs.

Next, they compared locomotor activity rhythms in floxed mice with or without tamoxifen treatment. As reported before in Wilcox et al 2017, the loss of ZFHX3 led to a shorter free running period and reduced amplitude and earlier onset of activity. Overall, the behavioral data in Figure 2 and supplementary figure 2 has been reported before and are not novel.

Next, the authors performed RNAseq at 4hr intervals on wildtype and knockout animals maintained in light/dark cycles to determine the impact of loss of ZFHX3. Overall transcriptomic analysis indicated changes in gene expression in nearly 36% of expressed genes, with nearly half being upregulated while an equal fraction was downregulated. Pathways affected included mostly neureopeptide neurotransmitter pathways. Surprisingly, there was no correlation between the direction in change in expression and TF binding since nearly all the sites were bound by ZFHX3 and the active histone PTMs. The ChIP-seq experiment for ZFHX3 in the UBC-Cre+Tam mice again could help resolve the real targets of ZFHX3 and the transcriptional state in knockout animals.

To determine the fraction of rhythmic transcripts, Using dryR, the authors categorise the rhythmic transcriptome (about 7% in all) into modules that include genes that lose rhythmicity in the KO, gain rhythmicity in the KO or remain unaffected or partially affected. The analysis indicates that a large fraction of the rhythmic transcriptome is affected in the KO model. However, among core-clock genes only Bmal1 expression is affected showing a complete loss of rhythm. The authors state a decrease in Clock mRNA expression (line 294) but the panel figure 4A does not show this data. Instead it depicts the loss in Avp expression - {{ misstated in line 321 we noted severe loss in 24-h rhythm for crucial SCN neuropeptides such as Avp (Fig. 3a).}}

However, core-clock genes such as Pers and Crys show minor or no change in expression patterns while Per2 and Per3 show a ~2hr phase advance. While these could only weakly account for the behavioral phase advance, the authors used TimeTeller to assess circadian phase in wildtype and ZFHX3 deficient mice. This approach clearly indicated that while the clock is not disrupted in the knockout animals, the phase advance can be correctly predicted from a network of gene expression patterns.

Strengths

The authors use a multiomic strategy in order to reveal the role of the ZFHX3 transcription factor with a combination of TF and histone PTM ChIPseq, time-resolved RNAseq from wildtype and knockout mice and modeling the transcriptomic data using TimeTeller. The RNAseq experiments are nicely controlled and the analysis of the data indicates a clear impact on gene-expression levels in the knockout mice and the presence of a regulatory network that could underlie the advanced activity onset behavior.

Weaknesses

It is not clear whether ZFHX3 has a direct role in any of the processes and seems to be a general factor that marks H3K4me3 and K27ac marked chromatin. Why it would specifically impact the core-clock TTFL clock gene expression or indeed daily gene expression rhythms is not clear either. Details for treatment of different ChIP samples (ZFHX3 and histone PTM ChIPs) on data normalization for analysis are needed. The loss of complete rhythmicity of Avp and other neuropeptides or indeed other TFs could instead account for the transcriptional deregulation noted in the knockout mice.

Comments on revisions:

The authors addressed the majority of my criticisms. They also explained that some requested experiments are beyond the scope of the current manuscript, while others are technically not feasible. I do not have any further concerns.
