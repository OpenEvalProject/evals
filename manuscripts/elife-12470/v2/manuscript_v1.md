# Registered report: Coding-independent regulation of the tumor suppressor PTEN by competing endogenous mRNAs

## Authors

- Mitch Phelps<sup>1</sup>
- Chris Coss<sup>1</sup>
- Hongyan Wang<sup>1</sup>
- Matthew Cook<sup>2</sup>

### Affiliations

1. Pharmacoanalytic Shared Resource The Ohio State University Columbus United States
2. University of California San Francisco San Francisco United States

† Corresponding author

## Abstract

10.7554/eLife.12470.001 The Reproducibility Project: Cancer Biology seeks to address growing concerns about reproducibility in scientific research by conducting replications of selected experiments from a number of high-profile papers in the field of cancer biology. The papers, which were published between 2010 and 2012, were selected on the basis of citations and Altmetric scores ( Errington et al., 2014 ). This Registered Report describes the proposed replication plan of key experiments from “Coding-Independent Regulation of the Tumor Suppressor PTEN by Competing Endogenous 'mRNAs' by Tay and colleagues, published in Cell in 2011 ( Tay et al., 2011 ). The experiments to be replicated are those reported in Figures 3C, 3D, 3G, 3H, 5A and 5B, and in Supplemental Figures 3A and B. Tay and colleagues proposed a new regulatory mechanism based on competing endogenous RNAs (ceRNAs), which regulate target genes by competitive binding of shared microRNAs. They test their model by identifying and confirming ceRNAs that target PTEN . In Figure 3A and B, they report that perturbing expression of putative PTEN ceRNAs affects expression of PTEN. This effect is dependent on functional microRNA machinery (Figure 3G and H), and affects the pathway downstream of PTEN itself (Figures 5A and B). The Reproducibility Project: Cancer Biology is a collaboration between the Center for Open Science and Science Exchange , and the results of the replications will be published by eLife . DOI: http://dx.doi.org/10.7554/eLife.12470.001

## Introduction

microRNAs are one of the first identified classes of non-coding RNAs that can modulate the expression of mRNA-coding transcripts by binding to complementary regions in a target gene’s sequence and repressing its expression. Thus, expression levels and availability of these microRNAs can influence gene expression, and there is growing evidence that misregulation of microRNAs is correlated with some forms of cancer (Sen et al., 2014). Naturally occurring microRNA 'sponges' have been shown to be effective in regulating gene expression by altering the levels of their cognate microRNAs (Choi et al., 2007; Karreth and Pandolfi 2013). Poliseno and colleagues proposed that pseudogenes, long non-coding RNAs with strong homology to coding sequences, could act as the modulators of gene expression as microRNA sponges (Poliseno et al., 2010). They demonstrated that the pseudogene PTENP1 could regulate the expression levels of PTEN via their cognate microRNAs miR-19b and miR-20a (Poliseno et al., 2010).

In this study, Tay and colleagues expanded upon the previous work to propose a unifying hypothesis of regulatory networks composed of competing endogenous RNAs (ceRNAs) (Karreth and Pandolfi 2013; Sen et al., 2014; Kartha and Subramanian, 2014). They suggest that protein-coding RNAs, not just non-coding RNAs, can cross-regulate each other based on competition for shared microRNA regulators; ceRNAs can titrate microRNAs from their target genes (Tay et al., 2011). Continuing their focus on the regulation of PTEN, one of the most frequently mutated genes in cancer (Song et al., 2012), Tay and colleagues propose a computational model to identify ceRNAs de novo, termed MuTaME. Using MuTaME, they identified potential ceRNA regulators of PTEN, and validated if these candidate ceRNAs could modulate PTEN expression in a microRNA-dependent manner (Tay et al., 2011).

In Figure 3C, Tay and colleagues examine if silencing ceRNAs targeting PTEN would affect the expression levels of a luciferase construct carrying the 3’UTR of PTEN. They co-transfected DU145 cells with siRNAs against the candidate PTEN ceRNAs along with a luciferase-PTEN 3’UTR construct and measured luciferase activity. After confirming knockdown of each target ceRNA (Supplemental Figure 3A), they reported that the loss of three of their candidate ceRNAs - SERINC1, VAPA and CNOT6L, but not ZNF460 - reduced the luciferase activity of the PTEN 3’UTR construct. This experiment will be replicated in Protocol 1.

In Figure 3D, they demonstrated that only the 3’UTRs of the candidate ceRNAs were required to affect changes in the luciferase activity of the PTEN 3’UTR construct. Ectopic overexpression of the 3’UTRs of the three candidate ceRNAs relieved inhibition of the PTEN 3’UTR, as evidenced by increased luciferase activity as compared to controls. This experiment will be replicated in Protocol 2.

To test if this effect was dependent on microRNAs, Tay and colleagues repeated these experiments in DICER1 mutant HCT116 cells, in which the machinery required for microRNA function is abrogated. Transfection of wild type HCT116 cells with siRNAs targeting the candidate ceRNAs showed a marked reduction in PTEN protein levels, an effect that was not seen in the DICER1 mutant HCT116 cells (Figures 3G and H). Knockdown of the candidate ceRNAs was confirmed by RT-PCR (Supplemental Figure 3B). This experiment will be replicated in Protocol 3.

PTEN negatively regulates the PI3K/AKT pathway (Stambolic et al., 1998), so Tay and colleagues examined if ceRNA modulation affected the phosphorylation of AKT. Loss of CNOT6L and VAPA in DU145 cells elevated pAKT levels after serum stimulation, an effect that was also observed in wild-type HCT116 cells (Figure 5A). However, this effect was abrogated in DICER1 mutant HCT116 cells (Figure 5A). They also examined the effect of ceRNAs on the tumorigenic properties conferred by loss of PTEN. Silencing of the ceRNAs CNOT6L and VAPA increased cell proliferation of DU145 cells and wild-type HCT116 cells, similar to silencing of PTEN directly (Figure 5B). This effect was less pronounced in DICER1 mutant HCT116 cells (Figure 5B). These experiments will be replicated in Protocol 4 and 5.

Two papers published simultaneously provide support for the actions of ceRNA regulatory networks. Karreth and colleagues, from the same lab as Tay and colleagues, demonstrated in vivo evidence for the actions of ceRNA regulation using the sleeping beauty transposase system in a mouse model of melanoma to identify and confirm putative PTEN ceRNAs (Karreth et al., 2011). Karreth and colleagues identified CNOT6L as a putative PTEN ceRNA through the sleeping beauty transposase system, providing further evidence that CNOT6L is indeed involved in PTEN regulation. Karreth and colleagues focused on ZEB2; using siRNA silencing, they reported that the loss of ZEB2 reduced PTEN protein levels, and affected downstream phosphorylation of AKT (Karreth et al., 2011). As seen in Tay and colleagues, these effects were dependent on functional microRNA processing; ZEB2 depletion did not affect PTEN levels in DICER1 mutant HCT116 cells (Karreth et al., 2011). Sumazin and colleagues used a bioinformatics approach to identify post-translational regulation and elucidated over 7,000 genes they proposed acted as miRNA sponges. By comparing the miRNA programs of genes, they could identify genes with common miR programs, indicating the potential for miRNA-mediated crosstalk between those two genes (Sumazin et al., 2011). They tested their findings by exploring the regulation of PTEN, demonstrating that silencing of putative miRNA program-mediated regulators (mPRs) of PTEN decreased PTEN expression, and, conversely, that the perturbation of PTEN levels could inversely affect the expression of its mPRs. These manipulations also affected tumor cell growth rates, indicating potential in vivo effects of changes to mPR regulatory networks (Sumazin et al., 2011). Since the publication of these three papers, numerous other examples of ceRNA regulation have been reported in muscle differentiation (Cesana et al., 2011), human embryonic stem cell renewal (Wang et al., 2013), regulation of sex determination by SRY (Granados-Riveron and Aquino-Jarquin 2014), breast cancer (Yang et al., 2014; Zheng et al., 2015a; 2015b), lymphoma (Karreth et al., 2015) and the regulation of the tumor-related HMGA1 (Esposito et al., 2014).

The Pandolfi group followed up on their 2011 paper by generating a mathematical model to predict optimal conditions for ceRNA activity, based on a molecular titration mechanism whose effects were correlated to the relative levels of the ceRNA and its target (Ala et al., 2013). They then tested their in silico predictions by experimentally exploring the effect of VAPA on PTEN expression. While silencing of VAPA did decrease PTEN expression in all five cell lines tested, they noted that the amount of silencing was correlated with the initial VAPA:PTEN expression ratio (Ala et al., 2013). However, Denzler and colleagues challenge the notion that perturbations in ceRNA expression levels could affect target genes at all (Denzler et al., 2014). Denzler and colleagues and Ala and colleagues both state that ceRNA effects are dependent on the kinetics of binding, which in turn relies upon the ratio of microRNAs to target sites; increasing the number of target sites through expression of ceRNAs is postulated to affect target gene repression. By quantifying the absolute copy number of the well-studied highly abundant miR-122 and its target sites, Denzler and colleagues showed that large, physiologically unlikely changes in ceRNA expression levels would be required to alter the microRNA: target site ratio enough to perturb target gene expression, casting doubt on the ability of these putative ceRNAs to affect changes in target gene expression levels (Broderick and Zamore 2014; Denzler et al., 2014). This view was contradicted by Bosson and colleagues, who identified over 3,000 high affinity target sites they claimed could be affected by ceRNAs due to low endogenous microRNA: target site ratios (Bosson et al., 2014). The activity and impact of potential ceRNA networks is an area of active interest (for review, see de Giorgio et al., 2013).

## Materials and methods

Unless otherwise noted, all protocol information was derived from the original paper, references from the original paper, or information obtained directly from the authors. An asterisk (*) indicates data or information provided by the Reproducibility Project: Cancer Biology core team. A hashtag (#) indicates information provided by the replicating lab.

## Protocol 1: Knock-down of ceRNA network genes results in decreased PTEN-3’UTR luciferase expression

This protocol describes how to silence expression of ceRNA network genes and measure effects on PTEN expression by measuring PTEN 3’UTR luciferase activity, as seen in Figures 3C and Supplementary S3A.

## Sampling

## Materials and reagents

## Procedure

Notes:

## Deliverables

## Confirmatory analysis plan

## Known differences from the original study

All known differences are listed in the materials and reagents section above with the originally used item listed in the comments section. All differences have the same capabilities as the original and are not expected to alter the experimental design.

## Provisions for quality control

Extracted RNA integrity will be reported with A260/280 and A260/230 absorbance ratios, and transfection efficiency will be checked using the siGLO control. qRT-PCR will be performed to confirm the silencing of ceRNA expression. The cells will be sent for mycoplasma testing confirming lack of contamination and STR profiling confirming cell line authenticity. Transfection efficiency will be recorded for each replicate and any transfection that does not contain >90% efficiency will be excluded and not continue through the rest of the procedure. Any modifications to the transfection protocol will be recorded, and the procedure will be maintained for the remaining replicates. All data obtained from the experiment - raw data, data analysis, control data and quality control data - will be made publicly available, either in the published manuscript or as an open access dataset available on the Open Science Framework (https://osf.io/oblj1/).

## Protocol 2: Overexpression of PTEN ceRNA 3’UTRs network genes results in upregulation of PTEN3’UTR luciferase activity

This protocol describes how to measure the effect of ectopic overexpression of PTEN ceRNA 3’UTRs in DU145 cells on Luc-PTEN 3’UTR levels. This protocol replicates Figures 3D.

## Sampling

## Materials and reagents

## Procedure

Notes:

## Deliverables

## Confirmatory analysis plan

## Known differences from the original study

All known differences are listed in the materials and reagents section above with the originally used item listed in the comments section. All differences have the same capabilities as the original and are not expected to alter the experimental design.

## Provisions for quality control

The cells will be sent for mycoplasma testing confirming lack of contamination and STR profiling confirming cell line authenticity. All data obtained from the experiment - raw data, data analysis, control data and quality control data - will be made publicly available, either in the published manuscript or as an open access dataset available on the Open Science Framework (https://osf.io/oblj1/).

## Protocol 3: Knock-down of ceRNA network genes results in decreased PTEN protein that is dependent on microRNA functioning

This protocol describes how to test the effects of siRNA-mediated depletion of SERINC1, VAPA, or CNOT6L expression on PTEN protein expression in wild-type HCT116 colon cancer cells. It also tests whether these effects are dependent on mature microRNA using Dicer mutant (DICEREx5) HCT116 cells. It replicates Figures 3G,H, and Supplementary Figure 3B.

## Sampling

## Materials and reagents

## Procedure

Notes

## Deliverables

## Confirmatory analysis plan

## Known differences from the original study

All known differences are listed in the materials and reagents section above with the originally used item listed in the comments section. All differences have the same capabilities as the original and are not expected to alter the experimental design.

## Provisions for quality control

Extracted RNA integrity will be reported with A260/280 and A260/230 absorbance ratios, and transfection efficiency will be checked using the siGLO control. The cells will be sent for mycoplasma testing confirming lack of contamination and STR profiling confirming cell line authenticity. Transfection efficiency will be recorded for each replicate and any transfection that does not contain >90% efficiency will be excluded and not continue through the rest of the procedure. If the efficiency does not reach >90%, then any modifications to the transfection protocol will be recorded. qRT-PCR will be performed to confirm silencing of mRNA expression. Images of Ponceau staining to confirm protein transfer. All data obtained from the experiment - raw data, data analysis, control data, and quality control data - will be made publicly available, either in the published manuscript or as an open access dataset available on the Open Science Framework (https://osf.io/oblj1/).

## Protocol 4: Effect of knock-down of ceRNA network genes on cell proliferation

This experiment tests the effects of siRNA-mediated depletion of PTEN, CNOT6L, and VAPA expression on cell proliferation in DU145, HCT116 WT, and HCT116 DICEREx5 cells. It replicates Figure 5B.

## Sampling

## Materials and reagents

## Procedure

Notes:

## Deliverables

## Confirmatory analysis plan

## Known differences from the original study

All known differences are listed in the materials and reagents section above, with the originally used item listed in the comments section. All differences have the same capabilities as the original and are not expected to alter the experimental design.

## Provisions for quality control

Extracted RNA integrity will be reported with A260/280 and A260/230 absorbance ratios, and transfection efficiency will be checked using the siGLO control. Cells will be sent for mycoplasma testing confirming lack of contamination and STR profiling confirming cell line authenticity. Transfection efficiency will be recorded for each replicate and any transfection that does not contain >90% efficiency will be excluded and not continue through the rest of the procedure. Any modifications to the transfection protocol will be recorded and the procedure will be maintained for the remaining replicates. All data obtained from the experiment - raw data, data analysis, control data and quality control data - will be made publicly available, either in the published manuscript or as an open access dataset available on the Open Science Framework (https://osf.io/oblj1/).

## Protocol 5: Knock-down of ceRNA network genes results in AKT activation

This experiment tests the effects of siRNA-mediated depletion of PTEN, CNOT6L, and VAPA expression on AKT activation in DU145, HCT116 WT, and HCT116 DicerEx5 cells. It replicates Figure 5A.

## Sampling

## Materials and reagents

## Procedure

## Notes:

## Deliverables

## Confirmatory analysis plan

## Known differences from the original study

All known differences are listed in the materials and reagents section above, with the originally used item listed in the comments section. All differences have the same capabilities as the original and are not expected to alter the experimental design.

## Provisions for quality control

The cells will be sent for mycoplasma testing confirming lack of contamination and STR profiling confirming cell line authenticity. Transfection efficiency will be recorded for each replicate and any transfection that does not contain >90% efficiency will be excluded and not continue through the rest of the procedure. Any modifications to the transfection protocol will be recorded, and the procedure will be maintained for the remaining replicates. Images of Ponceau staining to confirm protein transfer. All data obtained from the experiment - raw data, data analysis, control data, and quality control data - will be made publicly available, either in the published manuscript or as an open access dataset available on the Open Science Framework (https://osf.io/oblj1/).

## Power calculations

For additional details on power calculations, please see analysis scripts and associated files on the Open Science Framework:

https://osf.io/c8hb5

## Protocol 1

Summary of original luciferase activity data:

## Test family

Power Calculations performed with G*Power software, version 3.1.7 (Faul et al., 2007).

## Test family

## Power calculations

## Test family

## Power calculations

Summary of original qPCR gene expression data:

## Test family

Power Calculations performed with G*Power software, version 3.1.7 (Faul et al., 2007).

## Test family

## Power calculations

## Protocol 2

Summary of original Luciferase data:

## Test family

Power Calculations performed with G*Power software, version 3.1.7 (Faul et al., 2007).

## Test family

## Power calculations

## Test family

## Power calculations

## Protocol 3

Summary of original Western blot data:

## Test family

Power Calculations performed with G*Power software, version 3.1.7 (Faul et al., 2007).

## Test family

## Power calculations

## Test family

## Power calculations

Summary of original mRNA expression data:

## Test family

## Power calculations

## Test family

## Power calculations

## Protocol 4

Summary of original cell proliferation data:

## DU145 cells

## Test family

Power Calculations performed with G*Power software, version 3.1.7 (Faul et al., 2007).

## Test family

## Power calculations

## Test family

## Power calculations

## HCT116 cells

## Test family

Power Calculations performed with G*Power software, version 3.1.7 (Faul et al., 2007).

## Test family

## Power calculations

## Test family

## Power calculations

## Protocol 5

Summary of original AKT Activation data

## DU145 cells

Note: The original data does not indicate the error associated with multiple biological replicates. To identify a suitable sample size, power calculations were performed using different levels of relative variance.

## Test family

## Power calculations

## Test family

## Power calculations

## HCT 116 cells

Note: The original data do not indicate the error associated with multiple biological replicates. To identify a suitable sample size, power calculations were performed using different levels of relative variance.

## Test family

## Power calculations

## Test family

## Power calculations

In order to produce quantitative replication data, we will run the experiment seven times. Each time we will quantify band intensity. We will determine the standard deviation of band intensity across the biological replicates and combine this with the reported value from the original study to simulate the original effect size. We will use this simulated effect size to determine the number of replicates necessary to reach a power of at least 80%. We will then perform additional replicates, if required, to ensure that the experiment has more than 80% power to detect the original effect.
