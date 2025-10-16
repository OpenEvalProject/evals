# Author response - Round 1

Authors:
- Carly Boye ([ORCID: 0000-0002-9142-0240](https://orcid.org/0000-0002-9142-0240))
- Cynthia A Kalita
- Anthony S Findley ([ORCID: 0000-0001-9922-3076](https://orcid.org/0000-0001-9922-3076))
- Adnan Alazizi
- Julong Wei
- Xiaoquan Wen
- Roger Pique-Regi ([ORCID: 0000-0002-1262-2275](https://orcid.org/0000-0002-1262-2275))
- Francesca Luca ([ORCID: 0000-0001-8252-9052](https://orcid.org/0000-0001-8252-9052))

## Response text

DOI: [10.7554/eLife.85235.sa2](https://doi.org/10.7554/eLife.85235.sa2)

Essential revisions:

Please see the reviewer comments below, which elaborate on these overall essential revisions. Importantly, all three reviewers had a productive internal discussion and are in agreement about these revisions.

1. Clarify p-value calculations, N oligos, Figure 2 ambiguities, selection of null SNPs, and method details. Convincingly demonstrate the overall robustness of the underlying data.

We thank the reviewers and editor for these comments which we have addressed as described below:

P-value calculations: Previously, to summarize the DESeq results we had plotted the lowest pvalue per construct (either the p-value for the forward or reverse orientation). By selecting the pvalues this way, the plot seemed to have inflated p-values. Instead, we have changed the plot to show all p-values (for both directions when available).

N oligos and selection of null SNPs: we have clarified the nomenclature used across the manuscript to refer to SNP/direction pairs or SNPs and the number of oligos tested for each analysis. We have also clarified the selection of null SNPs. All these changes were introduced in the “BiT-STARR-Seq Library Design” section of methods and are also copied below:“We designed 43,556 target regulatory regions each containing a SNP in the middle and with a total length of 200 nucleotides. This set of targets corresponds to 87,112 constructs each containing only one of two alleles at the test SNP. Additionally, each construct can be integrated in the forward or reverse orientation, leading to a maximum of 174,224 constructs in either direction. Please also see below for a description of how we use library-related terms throughout the paper. The library used is the same as reported in Kalita et al. (Kalita et al., 2018). Briefly, the library of target regulatory sequences consisted of several categories of regulatory variants, including eQTLs (Innocenti et al., 2011; Wen et al., 2015), SNPs predicted to disrupt transcription factor binding (centiSNPs) (Moyerbrailean et al., 2016a), and SNPs associated with complex traits in GWAS(Pickrell, 2014). Negative controls that were not predicted to have a regulatory effect were also included in the library (Moyerbrailean et al., 2016a). It is important to note that these negative controls are only predicted not to have a regulatory effect via computation annotation (Moyerbrailean et al., 2016b), so they may not be representative of true negative controls. This is why we largely do not utilize these SNPs as negative controls within our analyses. Our predictions of regulatory activity also did not account for environmental context, thus these sequences are also not suited to annotate our cASE results.

SNP (n = 43,556): Refers to a genetic variant tested for allelic effects on gene regulation. Target (n = 43,556): 200 nucleotide-long oligonucleotide sequence that contains the test SNP in the middle of the target.

Construct (n = 87,112): Synthesized 200 nucleotide-long oligonucleotide sequence that contains only one of the two possible alleles at the test SNP. Each target corresponds to two constructs.. Direction: Constructs can integrate in either the forward or reverse direction relative to the direction of transcription in the BiT-STARR-seq plasmid. Therefore two directions are possible for each construct.

SNP/direction pair (n = 87,112): A SNP tested for allelic effects on gene regulation contrasting the expression of two constructs that are integrated in the same direction. All statistical tests are performed at this level, testing in each direction separately.”

Additionally, we now utilize the NULL sequences to annotate our ASE results, and show a depletion for these sequences. See Figure 3A. We have also prepared a plot zoomed-in to show the deviation in the 0-1 region (Author response image 2).

Figure 2 ambiguities: Thanks for pointing out this inconsistency in Supplemental figure 2. We had used the wrong caption by mistake and have now corrected it.Methods: We have added a brief description of pTWAS in the Results section to aid the reader in interpreting the results we present. Since we added additional analyses (INTACT), we have expanded our methods section to include this as well. We have also generally added more detail in the methods section.

2. Show a more convincing locus than the PIP4K2B example, which is only supported by a pTWAS result (with LD contamination issues) with no fine mapping or even nominal p-value evidence.

We agree that a stronger example could be provided. We have utilized INTACT, which identifies putative causal genes, to provide better example variants. This method combines TWAS and colocalization approaches to mitigate issues with LD contamination. We now provide the following 2 examples in the text, and include 8 total examples in supplemental table 6:

rs4938344 is an eQTL regulating the long non-coding RNA AP000892.6. The reference allele at this locus, G, results in decreased expression of AP000892.6. (as measured in GTEx and in the caffeine condition of our assay, Figure 5D and 5E respectively). INTACT associated high expression of AP000892.6 with decreased risk of hypertension and CAD (Figure 5F). This SNP is predicted to modulate binding of GABP (a known repressor of transcription(Genuario and Perry, 1996)) and ETV1 at this site (Figure 5C). These transcription factors are upregulated in caffeine exposed endothelial cells (Findley et al., 2019) (Figure 5B). This increase in expression uncovers allelic differences in gene regulation which are not detected in the absence of caffeine, likely because of the low expression of the repressor. The allelic differences in binding of these factors should lead to allelic differences in expression of AP000892.6. Accordingly, the reference allele for this variant exhibited lower activity in response to caffeine in our BiT-STARR-seq experiments (Figure 5E). This effect is consistent with the GTEx artery eQTL for AP000892.6 (Figure 5D). In summary, caffeine induces higher expression of the ETV1 and GABP transcription factors, which then bind preferentially to the reference allele at rs4938344, this results in lower expression of AP000892.6 and increased risk for CAD and hypertension (Figure 5A). AP000892.6 interacts with the RB1CC1 RNA (Gong et al., 2018), which may play a role in atherosclerosis via its function in forming the autophagosome (Chen et al., 2021).

rs4527034 is an eQTL regulating the KAT8 gene. The reference allele at this locus, A, results in decreased expression of KAT8 (as measured in GTEx and in the control condition of our assay, Figure 6D and 6E respectively). INTACT associated high expression of KAT8 with increased risk of hypertension (Figure 6F). This SNP is predicted to modulate binding of the TERF2IP transcription factor at this site (Figure 6C). TERF2IP is upregulated in caffeine exposed endothelial cells (Findley et al., 2019) (Figure 6B). This increase in expression may saturate all binding sites in the caffeine condition, while the transcription factor may only bind to the preferential allele in the control condition. The allelic differences in binding of these factors should lead to allelic differences in expression of KAT8 in the control condition, which is what we observe both in our BiT-STARR-seq experiments (Figure 6E) and in GTEx artery eQTL for KAT8 (Figure 6D). In summary, in the absence of caffeine, TERF2IP binds preferentially to the reference allele at rs4527034, this results in lower expression of KAT8 and reduced risk for hypertension. In the presence of caffeine, TERF2IP is upregulated, resulting in increased binding and lower expression of KAT8, independently of the genotype, with an expected overall protective effect on hypertension. Confirming this potential mechanism for disease risk, TERF2IP expression levels were found to affect plaque formation in a mouse model (Kotla et al., 2019). High expression of KAT8, a histone acetyltransferase, also coincides with atherosclerotic progression, and histone acetylation increases in plaques within vascular endothelial cells (Greißel et al., 2016; Zhang et al., 2018).
