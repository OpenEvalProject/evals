# Inducible and reversible inhibition of miRNA-mediated gene repression in vivo

## Authors

- Gaspare La Rocca<sup>1</sup> ([ORCID: 0000-0003-1277-0566](https://orcid.org/0000-0003-1277-0566)) †
- Bryan King<sup>1</sup>
- Bing Shui<sup>2</sup> ([ORCID: 0000-0002-5956-130X](https://orcid.org/0000-0002-5956-130X))
- Xiaoyi Li<sup>1</sup>
- Minsi Zhang<sup>1</sup>
- Kemal M Akat<sup>4</sup> ([ORCID: 0000-0002-9012-3551](https://orcid.org/0000-0002-9012-3551))
- Paul Ogrodowski<sup>1</sup>
- Chiara Mastroleo<sup>1</sup>
- Kevin Chen<sup>1</sup> ([ORCID: 0000-0002-0674-1411](https://orcid.org/0000-0002-0674-1411))
- Vincenzo Cavalieri<sup>5</sup>
- Yilun Ma<sup>6</sup>
- Viviana Anelli<sup>7</sup>
- Doron Betel<sup>8</sup>
- Joana Vidigal<sup>9</sup>
- Thomas Tuschl<sup>4</sup>
- Gunter Meister<sup>10</sup> ([ORCID: 0000-0002-2098-9923](https://orcid.org/0000-0002-2098-9923))
- Craig B Thompson<sup>1</sup> ([ORCID: 0000-0003-3580-2751](https://orcid.org/0000-0003-3580-2751))
- Tullia Lindsten<sup>11</sup>
- Kevin Haigis<sup>2</sup>
- Andrea Ventura<sup>1</sup> ([ORCID: 0000-0003-4320-9907](https://orcid.org/0000-0003-4320-9907)) †

### Affiliations

1. Cancer Biology and Genetics Program, Memorial Sloan Kettering Cancer Center New York United States
2. Department of Cancer Biology, Dana Farber Cancer Institute Boston United States
3. Louis V. Gerstner Jr. Graduate School of Biomedical Sciences, Memorial Sloan Kettering Cancer Center New York United States
4. Laboratory of RNA Molecular Biology, The Rockefeller University New York United States
5. Department of Biological, Chemical and Pharmaceutical Sciences and Technologies, University of Palermo Palermo Italy
6. Weill Cornell/Rockefeller/Sloan-Kettering Tri-Institutional MD-PhD Program New York United States
7. Center of Integrative Biology, University of Trento Trento Italy
8. Hem/Oncology, Medicine and Institution for Computational Biomedicine, Weill Cornell Medical College New York United States
9. Laboratory of Biochemistry and Molecular Biology, National Cancer Institute Bethesda United States
10. Regensburg Center for Biochemistry, University of Regensburg Regensburg Germany
11. Immunology Program, Memorial Sloan Kettering Cancer Center New York United States

† Corresponding author

## Abstract

Although virtually all gene networks are predicted to be controlled by miRNAs, the contribution of this important layer of gene regulation to tissue homeostasis in adult animals remains unclear. Gain and loss-of-function experiments have provided key insights into the specific function of individual miRNAs, but effective genetic tools to study the functional consequences of global inhibition of miRNA activity in vivo are lacking. Here we report the generation and characterization of a genetically engineered mouse strain in which miRNA-mediated gene repression can be reversibly inhibited without affecting miRNA biogenesis or abundance. We demonstrate the usefulness of this strategy by investigating the consequences of acute inhibition of miRNA function in adult animals. We find that different tissues and organs respond differently to global loss of miRNA function. While miRNA-mediated gene repression is essential for the homeostasis of the heart and the skeletal muscle, it is largely dispensable in the majority of other organs. Even in tissues where it is not required for homeostasis, such as the intestine and hematopoietic system, miRNA activity can become essential during regeneration following acute injury. These data support a model where many metazoan tissues primarily rely on miRNA function to respond to potentially pathogenic events.

## Introduction

MicroRNAs (miRNAs) are short non-coding RNAs that in Metazoa repress gene expression at the post-transcriptional level by binding to partially complementary sequences on target mRNAs (Bartel, 2009; Bartel, 2018; Eichhorn et al., 2014; Izaurralde, 2015).

miRNAs act as part of a large ribonucleoprotein complex known as the miRNA-induced silencing complex (miRISC). In mammals, the Argonaute protein family (AGO1-4) and the trinucleotide repeat-containing gene 6 protein family (TNRC6A/GW182, TNRC6B and TNRC6C) are the core components of the miRISC. AGO binds to the miRNA and facilitates its interaction with target mRNAs (Schirle et al., 2014). In turn, TNRC6 binds to AGO and recruits the decapping and deadenylation complexes, leading to degradation of target mRNAs (Braun et al., 2011; Chekulaeva et al., 2011; Chen et al., 2009; Chen et al., 2014; Fabian et al., 2011; Guo et al., 2010a; Huntzinger et al., 2013; Lazzaretti et al., 2009; Nishihara et al., 2013; Rehwinkel et al., 2005; Till et al., 2007).

Although miRNAs are abundantly expressed in embryonic and adult mouse tissues, and computational and experimental analyses indicate that they target components of virtually every cellular process (Flynt and Lai, 2008), animals harboring targeted deletion of single miRNA genes are often indistinguishable from their wild-type counterparts (Abdellatif, 2012; Chivukula et al., 2014; Cimmino et al., 2005; Liu et al., 2008; Park et al., 2010; van Rooij et al., 2007; Vechetti et al., 2019; Williams et al., 2009). One explanation for these observations is that the redundant functions of related miRNAs may buffer the emergence of obvious phenotypes in mutant animals (Bartel, 2009; Bartel, 2018). Interestingly, however, clear phenotypes often emerge in mutant adult animals when exposed to external or internal perturbations (Chivukula et al., 2014; Mendell and Olson, 2012; van Rooij et al., 2007). These observations suggest that, at least in some contexts, miRNA function is conditionally, rather than constitutively, required to carry on cellular processes.

Previous efforts to investigate the consequences of global inhibition of miRNA function have relied upon the targeted deletion of the core miRNA biogenesis factors DICER, DROSHA, and DGCR8 (Treiber et al., 2019). Several animal models harboring conditional or constitutive knockout alleles of these genes have been generated (Bernstein et al., 2003; Chong et al., 2008; Hebert et al., 2010; Huang et al., 2012; JnBaptiste et al., 2017; Kanellopoulou et al., 2005; Kobayashi et al., 2015; Kumar et al., 2007; Wang et al., 2007). Although these strategies have provided important insights into miRNA biology, they suffer from several limitations.

First, inactivation of these gene products is known to have other consequences in addition to impairing miRNA biogenesis. For instance, DICER is involved in epigenetic regulation in the nucleus in a miRNA-independent manner (Fukagawa et al., 2004; Giles et al., 2010; Gullerova and Proudfoot, 2012; Okamura and Lai, 2008; Song and Rossi, 2017; Tam et al., 2008) and is essential to metabolize transcripts from short interspersed nuclear elements, predominantly Alu RNAs in humans and B1 and B2 RNAs in rodents (Kaneko et al., 2011). DROSHA, on the other hand, regulates the expression of several coding and non-coding RNAs by directly cleaving stem–loop structures embedded within the transcripts (Chong et al., 2010). Furthermore, DICER and DROSHA are also involved in the DNA-damage response (Francia et al., 2012; Michelini et al., 2017), and DGCR8 regulates the maturation of small nucleolar RNAs and of some long non-coding RNAs (Cirera-Salinas et al., 2017; Macias et al., 2015). Consequently, the phenotypes observed in these models cannot be solely attributed to inhibition of miRNA activity.

Another limitation of conditional ablation of miRNA biogenesis genes in vivo is that due to their high stability mature miRNAs can persist for several days after their biogenesis is inhibited. For example, 4 weeks after near complete conditional ablation of Dicer1 in the muscle, the levels of the highest expressed miRNAs were found to be only reduced by 30–40% and their expression remained substantial even 18 months later (Vechetti et al., 2019). This complicates the interpretation of experiments based on temporally controlled conditional ablation of these biogenesis factors, especially in non-proliferating tissues.

Third, a subset of mammalian miRNAs does not rely on the canonical biosynthesis pathway, and therefore their expression and activity are not affected by inactivation of the core miRNA biogenesis factors (Cheloufi et al., 2010; Chong et al., 2010; Cifuentes et al., 2010; Kim et al., 2016; Okamura et al., 2007; Ruby et al., 2007; Yang and Lai, 2011).

Finally, these genetic approaches are not reversible and therefore these animal models cannot be used to study the effects of transient inhibition of miRNA function.

To circumvent these limitations, we have generated a novel genetically engineered mouse strain that allows inducible and reversible disassembly of the miRISC, thereby achieving controllable inhibition of miRNA-mediated gene repression in vivo without affecting small RNA biogenesis. To address the reliance of adult tissues on miRNA-mediated gene repression, we have used this novel strain to investigate the consequences of acute inhibition of the miRISC under homeostatic conditions, and during tissue regeneration.

## Results

### Inhibition of the miRNA pathway through peptide-mediated disruption of the miRISC

Multiple motifs within the N-terminal domain of TNRC6 proteins contain regularly spaced tryptophan residues that mediate the interaction between AGO and TNRC6 by inserting into conserved hydrophobic pockets located on AGO’s Piwi domain (Lian et al., 2009; Sheu-Gruttadauria and MacRae, 2018).

A peptide encompassing one of the AGO-interacting motifs of human TNRC6B has been previously employed as an alternative to antibody-based approaches to efficiently pull down all AGO family members from cell and tissue extracts (Hauptmann et al., 2015; Pfaff et al., 2013). This peptide, named T6B, competes with endogenous TNRC6 proteins for binding to AGOs. However, as it lacks the domains necessary for the recruitment of decapping and deadenylation factors, it prevents the assembly of the full miRISC, thus resulting in effective inhibition of miRISC-mediated gene repression in cells (Danner et al., 2017; Hauptmann et al., 2015).

Based on these results, we reasoned that temporally and spatially controlled expression of a T6B transgene in animals would offer the unprecedented opportunity to study the consequences of acute and reversible inhibition of miRNA function in vivo without interfering with miRNA biogenesis or abundance (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig1-v2.jpg)

**Figure 1.:** T6B fusion protein prevents miRNA-induced silencing complex (miRISC) assembly and impairs microRNA (miRNA) activity in vitro.
(A) Schematics of T6B action: T6B competes with TNRC6 for binding to AGO proteins preventing miRISC assembly. (B) Schematics of the size-exclusion chromatography (SEC) assay for the fractionation of AGO-containing complexes according to their molecular weight. (C) SEC profiling of miRISC components upon T6B expression: total lysates from HCT116 cells expressing no fusion protein (upper panel), T6B (middle panel), or T6BMut (lower panel) were fractionated as described in (B) and immunoblotted to detect AGO2, TNRC6A, T6B, and PABP1. For each blot, the relative signal intensity was assessed by densitometric analysis. (D) RNAseq analysis of total and small RNAs isolated from mouse embryo fibroblasts (MEFs) cell lines expressing either no fusion protein, T6B, or T6BMut (n = 3 for each cell line). Upper panel: bubble plot of target de-repression against miRNA abundance. The mean log2-fold change (T6B or T6BMut vs. control) of predicted targets for each conserved miRNA family was calculated, converted to a z-score and is plotted on the x-axis against the miRNA family abundance (log of the sum of read counts for each member of the family). The size of each circle is proportional to the number of predicted targets. A positive z-score indicates that the targets for that family are preferentially upregulated upon T6B expression, while a negative score would indicate preferential downregulation. Expression of T6B, but not of T6BMut, causes preferential upregulation of miRNA targets of the most miRNA families and the effect is roughly proportional to each miRNA family abundance. Lower panel: cumulative distribution plot of predicted let-7 targets compared to background in T6B-expressing MEFs. (E) Scatter plots of miRNA abundance as determined by small-RNAseq of total RNA extracted from MEFs expressing either T6B or T6BMut (n = 3 for each cell line). Each dot represents a miRNA in miRbase. (F) Effect of T6B expression on AGO2 slicing activity. MEFs expressing either T6B or T6BMut were transfected with siRNAs targeting GAPDH mRNA (siGAPDH) or with scramble siRNA (siCTL). Levels of GAPDH, T6B, and tubulin were assessed by immunoblot 72 hr post-transfection. T6B and T6BMut have slightly different migration on PAGE, as previously observed by Hauptmann et al., 2015.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Sequence and properties of the FH-T6B-YFP fusion protein.
(A) HCTT116 cells transduced with retroviral vectors expressing a doxycycline-inducible T6B or T6BMut transgene (FH-T6B-YFP) were cultured in the presence of doxycycline for 48 hr. Whole-cell lysates were probed with an anti-HA antibody. (B) Lysates from (A) were immunoprecipitated with the indicated antibodies and blotted against AGO2, FH-T6B-YFP (anti-HA), and GAPDH. Note that the T6B fusion protein, but not its mutant version (T6BMut), binds to AGO proteins. Lower panel: amino acid sequence of the T6B and T6BMut fusion proteins. Both T6B versions have HA and FLAG tags at the N termini and are fused to the yellow fluorescent protein (YFP) at the C-termini. In T6BMut, all tryptophan residues (red) are mutated to alanine to prevent interaction with AGO proteins. Blue: FLAG-tag; light blue: HA-tag; bold black: T6B; green: YFP.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Size-exclusion chromatography was performed on whole-cell lysates from mouse embryo fibroblasts transduced with retroviral vectors expressing a doxycycline-inducible T6B or T6BMut transgene and cultured in the presence of doxycycline for 48 hr.
Eluted fractions were probed with the anti-AGO2 or anti-HA antibodies to determine the elution profile of AGO2 and T6B, respectively.

To test the suitability of this approach, we first investigated the dynamics of interaction between T6B and the miRISC in mouse and human cell lines. We employed a previously reported size-exclusion chromatography (SEC)-based assay (La Rocca et al., 2015; Olejniczak et al., 2013) to analyze the molecular weight of AGO-containing complexes in lysates from cells expressing either a doxycycline-inducible FLAG-HA-T6B-YFP fusion protein (hereafter referred to as T6B) or a mutant version (hereafter referred to as T6BMut) incapable of binding to AGO (Figure 1—figure supplement 1). We reasoned that if T6B expression prevents AGO from stably binding to TNRC6 and its targets, AGO proteins should be detected in fractions corresponding to ~120–130 kDa, the sum of the molecular weights of AGO (~95 kDa) and the T6B fusion protein (~30 kDa). In contrast, unperturbed AGO complexes that are part of the fully assembled miRISC bound to mRNAs should elute in the void of the column, which contains complexes larger than 2 MDa (Figure 1B).

As expected, in lysates from cells expressing no T6B or T6BMut, AGO2 and TNRC6A were mostly detected in the high-molecular-weight fractions, indicating the presence of target-bound miRISC (Figure 1C). In contrast, AGO2 and TNRC6A were nearly completely depleted from the high-molecular-weight fractions in lysates from cells expressing T6B (Figure 1C). Moreover, while AGO2, TNRC6A, and the polyA-binding protein 1 (PABP1) co-fractionated in lysates from control cells, they eluted in different fractions in lysates from T6B-expressing cells (Figure 1C), indicating that T6B leads to loss of interactions between the miRISC components and mRNAs. As expected based on the strong evolutionary conservation of human and mouse AGO and TNRC6 proteins (Pfaff et al., 2013; Zielezinski and Karlowski, 2015; Zipprich et al., 2009), we obtained identical results when human T6B was expressed in mouse embryo fibroblasts (MEFs; Figure 1—figure supplement 2).

To test whether the redistribution of AGO-containing complexes induced by T6B expression was mirrored by a loss of miRNA-mediated gene repression, we performed RNAseq analysis on MEFs expressing T6B or T6BMut. Cells expressing T6B displayed marked and selective de-repression of predicted mRNA targets for expressed miRNAs (Figure 1D). The extent of de-repression was roughly proportional to the abundance of individual miRNA families, with predicted targets of poorly expressed miRNAs collectively showing modest de-repression compared to targets of more abundantly expressed miRNA families (Figure 1D). Importantly, de-repression of miRNA targets was not accompanied by a global change in mature miRNAs levels (Figure 1E), consistent with the role of T6B in perturbing the effector step of the miRNA pathway, without affecting miRNA processing.

Of the four mammalian AGO proteins, AGO2 is the only one that has endo-ribonucleolytic activity, which does not require TNRC6 (Liu et al., 2019) and is triggered when the AGO2-loaded small RNA and the target are perfectly complementary (Doench et al., 2003; Liu et al., 2004; Zeng et al., 2003). AGO2’s catalytic activity is essential for gene regulation in the germline. For example, in mouse oocytes, AGO2 loaded with endogenous small-interfering RNAs (endo-siRNAs) mediates the cleavage of coding and non-coding transcripts bearing perfectly complementary sequences (Stein et al., 2015; Tam et al., 2008). In metazoan somatic tissues, in contrast, AGO2 catalytic activity is mainly involved in the biogenesis of miR-486 and miR-451 in the hematopoietic system (Cheloufi et al., 2010; Jee et al., 2018), and in occasional instances of miRNA-directed cleavage of mRNAs (Yekta et al., 2004).

Importantly, T6B expression does not interfere with the ability of synthetic siRNAs to cleave perfectly complementary endogenous targets (Figure 1F), indicating that AGO2’s catalytic function is not affected by the binding of T6B, and implying that the loading of small RNAs onto AGOs is also not perturbed by T6B.

Collectively these results demonstrate that ectopic T6B expression in mammalian cells causes global inhibition of miRISC function with minimal perturbation of the expression of mature miRNAs, and with preservation of AGO2’s endo-nucleolytic activity.

### Generation of a mouse strain with inducible expression of a T6B transgene

To apply this general strategy to an in vivo setting, we next generated mouse embryonic stem cells (mESCs) expressing a doxycycline-inducible T6B transgene. We used a knock-in approach in which the doxycycline-inducible transgene is inserted into the Col1a1 locus of mESC expressing the reverse tetracycline-controlled transactivator (rtTA) under the control of the endogenous Rosa26 promoter (Beard et al., 2006; Figure 2A). Targeted mESCs were tested for the ability to express the T6B transgene in response to doxycycline (Figure 2—figure supplement 1) and then used to generate mice with genotype Rosa26rtTA/rtTA; Col1a1T6B/T6B
 (hereafter R26T6B). Rosa26rtTA/rtTA; Col1a1+/+
 mice, with untargeted Col1a1 loci but expressing rtTA served as negative controls (hereafter R26CTL).

![Figure 2.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig2-v2.jpg)

**Figure 2.:** Expression of T6B reversibly blocks miRNA-induced silencing complex (miRISC) assembly and inhibits microRNA (miRNA) function in vivo.
(A) Schematic of the targeting strategy to generate the T6B mouse. The construct contains a flippase recognition target site (frt) that allows homing into the Col1a1 locus when electroporated together with a vector expressing the Flippase recombinase into KH2 (Col1a1-frt/Rosa26-rtTA) murine embryonic stem cells. KH2 also express the rtTA trans-activator driven by the endogenous Rosa26 (R26) promoter. (B) Immunofluorescence imaging performed using an anti-YFP antibody, showing T6B expression in a panel of tissues of adult R26T6B mice fed doxycycline for 7 days. Tissues from R26CTL (carrying the rtTA allele but not the T6B allele) were used as negative controls. (C) Protein lysates from the liver of R26T6B mice on or off doxycycline-containing chow for the indicated number of days were resolved by SDS-PAGE and western blotting was performed with anti-HA antibody to detect expression of the T6B transgene. (D) Co-IP experiments using an anti-YFP antibody showing interaction between AGO and T6B in total liver extracts from T6B mice on doxycycline-containing chow. (E) Size-exclusion chromatography (SEC) elution profile of AGO2-containing complexes in liver lysates from T6B mice euthanized at the indicated time points after doxycycline administration. Notice the shift of AGO2 from the high-molecular-weight fractions to the low-molecular-weight fractions after 5 days of doxycycline treatment and the reconstitution of the full miRISC after removal of doxycycline from the diet. (F, G) Total RNA extracted from the large intestine (F) and the liver (G) of R26CTL and R26T6B mice was subjected to RNAseq (n = 3 for each strain). Left panel: scatter plot showing the effect of T6B expression on targets of all miRNA families was generated as described in Figure 1D. The abundance of each miRNA family was calculated using dataset from Isakova et al., 2020. Right panel: representative cumulative distribution plot of log2-fold changes in expression of predicted targets of the indicated miRNA families.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Expression of FH-T6B-YFP fusion protein in targeted ES clones.
(A) Two independent targeted ES clones were cultured in the presence or absence of doxycycline for 48 hr and examined by epifluorescence microscopy to detect FH-T6B-YFP expression. The same exposure was used for all images. Bright-field images are also shown for each clone. (B) Whole-cell lysates from the clones shown in (A) were probed with an anti-HA antibody to detect expression of the T6B fusion protein.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Immunofluorescence imaging using a YFP-specific antibody, showing T6B expression in a panel of tissues of adult R26T6B mice (second column) and CAGT6B mice (third column) fed doxycycline-containing diet for 7 days.
Tissues from R26CTL (first column) mice fed doxycycline-containing diet for 7 days were included as negative controls.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Total extracts from the colon of R26T6B mice kept on doxycycline-containing diet for 1 week were immunoprecipitated using an anti-YFP antibody and probed with the indicated antibodies to measure the interaction between the T6B fusion protein and AGO2 in vivo.
An anti-HA antibody was used to detect T6B.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** Size-exclusion chromatography (SEC) fractionation followed by western blotting of total extracts from the liver and large intestine of control and R26T6B mice treated with doxycycline-containing chow for 7 days.
The shift of AGO2 from high-molecular-weight to low-molecular-weight complexes confirms disruption of the miRNA-induced silencing complex.

Upon doxycycline administration, we observed strong expression of T6B in R26T6B mice and across most adult tissues (Figure 2B). Notable exceptions were the central nervous system (Figure 2B, Figure 2—figure supplement 2), probably due to low blood–brain barrier penetration of doxycycline, and the skeletal muscle and the heart, most likely due to low expression of the rtTA transgene in these tissues (Premsrirut et al., 2011).

When doxycycline was administered in the diet, T6B became detectable after 24 hr, reached a plateau after 3 days, and completely disappeared 4 days after doxycycline removal from the diet (Figure 2C).

Because colon and liver expressed uniformly high levels of T6B in response to doxycycline, we used these tissues to test the effects of T6B expression on miRISC activity in vivo. Co-IP experiments using antibodies directed to T6B confirmed the interaction between AGO and T6B in these tissues (Figure 2D, Figure 2—figure supplement 3). Expression of T6B resulted in nearly complete disassembly of the miRISC, as indicated by the elution shift of AGO from the high-molecular-weight to low-molecular-weight fractions in both tissues (Figure 2E, Figure 2—figure supplement 4). Importantly, doxycycline removal from the diet led to a complete reconstitution of the miRISC, as indicated by the reappearance of AGO2 in the high-molecular-weight fractions (Figure 2E).

To test whether T6B expression also resulted in inhibition of miRNA-mediated gene repression in vivo, we performed RNAseq on total RNAs extracted from the liver and colon of R26T6B and R26CTL mice kept on doxycycline-containing diet for 1 week. As shown in Figure 2F, T6B expression resulted in marked de-repression of miRNA targets in both tissues.

Based on these results,we conclude that T6B expression allows acute and reversible disruption of the miRISC, and concomitant inhibition of miRNA function in vivo.

### Consequences of miRISC disruption in adult tissues under homeostatic conditions

Given the central role of miRNAs in gene regulatory networks, one might expect widespread phenotypes emerging when miRISC function is systemically inhibited. Consistent with this hypothesis, inhibition of miRISC starting either at conception (Figure 3A) or at mid-gestation caused developmental defects and perinatal lethality in R26T6B mice (Figure 3B, Figure 3—figure supplement 1). Histological examination of hematoxylin-eosin-stained sections of P0 R26T6B pups treated with doxycycline starting at mid-gestation confirmed a general delay in development and reduced growth, but no specific organ defects. Surprisingly, however, adult R26T6B mice kept on doxycycline diet for up to 2 months remained healthy and appeared normal upon macroscopic and histopathological examination.

![Figure 3.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig3-v2.jpg)

**Figure 3.:** Phenotypic analysis of R26T6B mice during homeostasis.
(A) Rosa26+/+; Col1a1T6B/T6B
 females were crossed with Rosa26rtTA/+; Col1a1T6B/T6B
 males and doxycycline was administered by chow starting at 0.5 d.p.c. No viable pups positive for both the rtTA and T6B allele were observed (n = 15, p-value = 0.002, Fisher’s exact test). (B) Pregnant females were kept on doxycycline diet from E13.5 to E18.5 and the pups delivered on E18.5 by c-section. Note the significantly smaller size of Rosa26rtTA/rtTA; Col1a1T6B/T6B
 embryos relative to Rosa26rtTA/rtTA;Col1a1+/+
 control littermates. Lower row: YFP detection by epifluorescence in E18.5 pups of the indicated genotypes. (C) Comparison of intestine architecture in H&E sections from R26T6B and R26CTL mice (n = 3 for each genotype) maintained on doxycycline for 2 months. (D) Immunofluorescence imaging of the small intestine of R26T6B and R26CTL mice (n = 3–5 for each genotype) kept on doxycycline diet for a month (upper row), showing a reduction in lysozyme expression in Paneth cells in the crypts. Lysozyme expression in R26T6B mice returned to normal levels upon removal of doxycycline from the diet (lower row). (E) Peripheral blood analysis conducted in R26T6B and R26CTL mice (R26CTL n = 4; R26T6B n = 5). (F) Flow cytometric analysis of bone marrow of R26T6B and R26CTL mice kept on doxycycline diet for 3 weeks showing developmental block at the Pro-B to Pre-B. p-Values (from left to right): *p=0.0348, **p=0.0023, *p=0.0340, **p=0.0004, unpaired t-test. R26CTL n = 4; R26T6B n = 5. (G) Flow cytometry analysis of the bone marrow of control and R26T6B mice kept on doxycycline diet for 3 weeks. p-Values (from left to right): p=0.0994, **p=0.0092, **p=0.0085, *p=0.0312, unpaired t-test. R26CTL n = 4; R26T6B n = 5.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Effects of FH-T6B-YFP fusion protein expression during development.
(A) Litter obtained by c-section from a pregnant Rosa26rtTA/rtTA; Col1a1T6B/+
 female crossed to a Rosa26rtTA/rtTA; Col1a1T6B/+
 male and maintained on doxycycline from d.p.c. 13.5 to d.p.c. 18.5. (B) Pups from (A) were weighted and genotyped and the results plotted. p-Value: two-tailed unpaired t-test.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Immunofluorescence imaging of the small and large intestine of R26T6B and R26CTL mice kept on doxycycline diet for a month.
An antibody against YFP was used to detect the T6B fusion protein.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Sections from the colon and small intestine sections of R26T6B and control mice kept on doxycycline-containing diet for 2 months were probed by immunohistochemistry with an anti-Ki67 antibody.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** Detection of goblet cells by staining of acidic and neutral mucins in intestine sections from R26T6B and control mice kept on doxycycline diet for 2 months.
Neutral mucins are stained with periodic acid-Shiff, whereas acidic mucins are stained with Alcian blue.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** Body weight of R26T6B (n = 5) and control (n = 8) female mice was assessed after 2-month administration of doxycycline-containing chow.
ns, not significant (p=0. 6264, unpaired t-test).

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** Representative flow cytometry plots showing the gating strategy for the identification of hematopoietic stem and progenitor cells from whole bone marrow harvested from R26T6B and R26CTL mice maintained on doxycycline diet for 3 weeks.
LT-HSC: Lin- Kit+ Sca1+ CD150+ CD48-; ST-HSC: Lin- Kit+ Sca1+ CD150- CD48-; MPP2: Lin- Kit+ Sca1+ CD150+ CD48+; MPP3/4: Lin- Kit+ Sca1+ CD150 CD48+.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig3-figsupp7-v2.jpg)

**Figure 3—figure supplement 7.:** Representative flow cytometry plots showing the gating strategy for the identification of B cell lineage populations from whole bone marrow harvested from R26T6B and R26CTL mice maintained on doxycycline diet for 3 weeks.
Pro-B: B220+ CD19+ IgD-IgM-CD25-Kit+; Pre-B: B220+ CD19+ IgD-IgM-CD25+; Imm B: B220+ CD19+ IgD-IgM+; Mat B: B220+ CD19+ IgD + IgM+/lo.

Detailed examination of the intestine confirmed extensive T6B expression in the epithelium and in the mesenchymal compartment (Figure 3—figure supplement 2), but no architectural abnormalities were observed (Figure 3C). Cells in the crypts showed no significant changes in expression pattern of Ki67 protein (Figure 3—figure supplement 3), suggesting that the proliferation and turnover of the epithelium are maintained even in the absence of a functional miRISC. No significant change in the number of goblet cells was detected throughout the intestine (Figure 3—figure supplement 4), and mice maintained normal body mass throughout the period of doxycycline treatment (Figure 3—figure supplement 5), suggesting that general intestinal functions were not affected.

Although no obvious macroscopic, functional, or architectural abnormalities were caused by T6B expression in the intestine, we observed a reduction in lysozyme expression in Paneth cells in the crypts (Figure 3D, upper row). However, this phenotype was reversible as lysozyme signal in the crypts returned to normal levels when doxycycline was removed from the diet (Figure 3D, lower row), suggesting that T6B expression did not affect neither the viability of intestinal stem cells nor their self-renewal ability.

Complete blood counts showed a modest, but significant, decrease in erythrocytes volume (MCV) and hemoglobin content (MCH) in R26T6B RBCs (Figure 3E, Figure 3—source data 1), analogously to what was reported in mice harboring targeted deletion of miR-451 (Patrick et al., 2010). Flow cytometric analysis of bone marrow showed a threefold depletion in Pre-B cells as well as a significant decrease in immature and mature circulating B cells in R26T6B mice. We also observed a reciprocal increase in the frequency of Pro-B cells in the bone marrow of these animals (Figure 3F, Figure 3—figure supplement 6). These results are reminiscent of the partial block in B cell differentiation observed upon deletion of the miR-17–92 cluster (Ventura et al., 2008).

Further characterization of hematopoietic stem cells (HSCs) showed that the number of long-term repopulating hematopoietic stem cells (LT-HSC) was unaffected after 3 weeks of doxycycline exposure. However, we observed a modest decrease in short-term repopulating HSCs (ST-HSCs) and a concomitant increase in multipotent progenitors (MPPs) relative to controls (Figure 3G, Figure 3—figure supplement 7).

Collectively, these data suggest that in a subset of adult tissues miRISC function can be suppressed with minimal or no consequences on the ability of these tissues to maintain homeostasis.

### miRISC disruption impairs the regeneration of injured colon epithelium

Several studies have shown that the phenotype caused by targeted deletion of individual miRNAs often manifests only after the mutant animals are subjected to ‘stress’ (Chivukula et al., 2014; Leung and Sharp, 2010; Mendell and Olson, 2012; van Rooij et al., 2007). For example, ablation of miR-143/145 causes no apparent phenotype under homeostasis but severely impairs the ability of the mutant animals to respond to acute damage to the intestinal epithelium (Chivukula et al., 2014).

Prompted by these reports, and by our initial observation that prolonged T6B expression does not substantially affect intestinal homeostasis, we tested the consequences of miRISC disruption on the regenerating intestine. A cohort of R26T6B and R26CTL mice were kept on doxycycline-containing diet for 10 days, after which they were treated with dextran sulfate sodium (DSS), which induces severe colitis in mice (Chivukula et al., 2014; Okayasu et al., 1990).

A significant and progressive loss of body mass was observed in both groups during DSS treatment and 2 days following DSS removal (Figure 4A). However, R26T6B mice lost body mass more rapidly than controls and reached critical health conditions 7 days after DSS removal. Three days after DSS removal, control animals started to regain weight, reaching the initial body mass within 5 days after DSS removal (Figure 4A). In contrast, R26T6B mice failed to fully recover (Figure 4A), and all reached a humane endpoint within 5 days after DSS removal from the diet (Figure 4B).

![Figure 4.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig4-v2.jpg)

**Figure 4.:** T6B-induced block of miRNA-induced silencing complex (miRISC) assembly leads to impaired intestinal regeneration.
(A) R26T6B and R26CTL mice (n = 6 for each genotype) kept on doxycycline diet were treated with dextran sulfate sodium (DSS) for 5 days to induce inflammatory colitis and their weight was monitored daily. Data are presented as mean ± SD. p-Values (from left to right): *p=0.034, *p=0.005, *p=0.029, *p=0.024, *p=0.011, from unpaired t-test. (B) Kaplan–Meier curves of animals treated with DSS as described in panel (A). p-Value from log-rank test (C) Representative hematoxylin-eosin-stained sections of intestine of R26T6B and R26CTL mice (n = 3 for each genotype) at different time points pre- and post-DSS treatment. (D) Ki67 immunostaining of section of intestine at the indicated time points. (E) Sections from the large intestine of control and T6B mice euthanized at day 13 were subjected to RNA in situ hybridization with a probe against the IGFBP5 transcript. The results show increased levels of IGFBP5 mRNA in ulcerated areas of R26T6B as compared to controls (n = 4 for each genotype).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Bar plots showing measurement of colon length, aggregated length of ulcers, percentage of colon with ulcers, area of ulcers, number of immune nodules, and the area of immune nodules performed on H&E longitudinal sections of colon from R26CTL and R26T6B mice 5 days post-dextran sulfate sodium (DSS) treatment.
Measurements of these parameters were obtained using OMERO (https://www.openmicroscopy.org/omero/) and used to estimate the extent of damage and colitis induced by DSS treatment. Plots show that no significant differences between R26CTL and R26T6B mice were observed, suggesting that both groups experienced similar level of DSS-induced colitis.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Representative immunohistochemistry image showing Ki67 signal in control mice (n = 3) 5 days after dextran sulfate sodium (DSS) treatment was discontinued.
The presence of highly proliferating cells indicates residual dysplasia.

Histological analysis confirmed that DSS treatment induced the disruption of the architecture of the epithelium and the appearance of ulcerative areas to a similar extent in both R26T6B and R26CTL control mice (Figure 4C, Figure 4—figure supplement 1). In contrast, although 5 days after DSS removal the integrity of the colonic epithelium of control mice was largely reestablished with the exception of isolated dysplastic areas (Figure 4—figure supplement 2), extensive ulcerated regions persisted in the colon of R26T6B mice (Figure 4C). Importantly, we observed the presence of dysplastic epithelium in R26T6B mice during and after DSS treatment, indicating that miRISC disruption does not completely abolish the potential of cells to proliferate, as also confirmed by Ki67 staining (Figure 4D). Therefore, we speculate that other factors, such as impaired stem cell maintenance or differentiation, may be responsible for the increased susceptibility of T6B-expressing colon to DSS treatment.

Chivukula and colleagues have shown that defective intestinal regeneration in the colon of miR-143/145-deficient mice is associated with upregulation of the miRNA-143 target IGFBP5 in the mesenchymal compartment. The increased levels of IGFBP5 protein cause the inhibition of IGF1R signaling in the epithelium through a non-cell-autonomous mechanism, which ultimately prevented epithelial regeneration (Chivukula et al., 2014). Consistent with their findings, in situ hybridization analyses in the colon of DSS-treated R26T6B mice showed a significant upregulation of IGFBP5 mRNA in the mesenchymal compartment compared to controls (Figure 4E). The extent of de-repression of IGFBP5 was comparable to that previously observed in miRNA-143/145 knockout mice (Chivukula et al., 2014), providing further evidence that T6B-mediated miRISC disassembly is an effective strategy to globally inhibit miRNA function in vivo.

Collectively, these results support a model whereby miRNA-mediated gene regulation, while dispensable to maintain normal colon homeostasis, becomes critical for its regeneration following acute damage.

### miRISC disruption impairs regeneration of the hematopoietic system

To further characterize the consequences of miRISC inhibition during tissue regeneration, we explored the possibility that other tissues may adopt a similar dynamic reliance on miRNA function.

Along with the intestinal epithelium, blood is one of the most rapidly turned over tissues in mice. HSCs reside as a predominantly quiescent population in the bone marrow and are rapidly induced to re-enter the cell cycle in response to external cues, such as infection or injury (Ng and Alexander, 2017). Furthermore, HSCs can be readily isolated by flow cytometry and transplanted, allowing the study of mechanisms underlying regeneration at the single-cell level.

To test the consequences of miRISC disruption in the regenerating hematopoietic system, we treated R26T6B and R26CTL mice on doxycycline-containing diet with a single dose of the cytotoxic drug 5-fluorouracil (5FU). 5-FU selectively depletes rapidly proliferating hematopoietic progenitors and leads to a compensatory increase in LT-HSC proliferation. Flow cytometry analysis of the bone marrow 7 days after 5FU-injection showed that T6B expression prevented this compensatory increase in LT-HSC. We observed an identical phenotype when R26T6B and R26CTL mice were bled repeatedly over a 3-week period to induce LT-HSC to re-enter the cell cycle (Figure 5A).

![Figure 5.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig5-v2.jpg)

**Figure 5.:** T6B-induced block of miRNA-induced silencing complex (miRISC) assembly impairs the regeneration of the hematopoietic system.
(A) Long-term hematopoietic stem cell (HSC) in the bone marrow of R26T6B and R26CTL mice treated with 5-fluorouracil (5-FU) or subjected to repeated bleeding (n = 5 for each genotype). Mice were maintained on doxycycline-containing diet throughout the experiment. (B) Kaplan–Meier plots of R26T6B (n = 5) and R26CTL (n = 5) mice treated weekly with 5-FU for 7 weeks. (C) Schematic of the bone marrow transplantation experiments: T6B was induced at different time points post-transplantation, and multilineage reconstitution was assessed at the indicated time points by FACS. (D) FACS analysis conducted on the peripheral blood of irradiated recipients transplanted 1:1 with T6B-expressing and wild-type bone marrow, and maintained on doxycycline diet according to scheme shown in panel (C). Data are presented as mean ± SD. *p<0.05, **p<0.01, ***p<0.001, one-way ANOVA. off > off, n = 9; off > on, n = 10; on > off, n = 8; on > on, n = 8. (E) FACS analysis showing the frequency of T6B-extressing HSCs in the bone marrow of transplanted recipient mice kept on doxycycline diet according to scheme shown in panel (C). off > off, n = 5; off > on, n = 5; on > off, n = 4; on > on, n = 5, one-way ANOVA.

The decreased number of HSCs in the bone marrow of R26T6B mice after a single 5-FU challenge compared to controls suggested that miRISC disruption impaired HSCs’ ability to re-enter the cell cycle and regenerate the hematopoietic compartment. Consistent with this hypothesis, when injected with repetitive 5-FU doses, R26T6B mice showed significantly shorter survival compared to controls (Figure 5B).

To measure the regenerative capacity of HSCs more directly in a context where T6B would only be expressed in hematopoietic cells, we performed competitive transplantation of T6B-expressing (CD45.2+) and wild-type (CD45.1+) bone marrows (1:1 ratio) into lethally irradiated hosts. The recipient animals were divided into four groups as shown in Figure 5C: (1) a control group that was never administered doxycycline; (2) a group maintained on a doxycycline-containing diet throughout the duration of the experiment (8 weeks); (3) a group treated with doxycycline starting 4 weeks after transplant; and (4) a group that was on doxycycline for only the first 4 weeks after transplant. Blood samples were taken at 4 and 8 weeks following the start of the experiment for analysis (Figure 5C). This experiment was designed to test the prediction that expression of T6B during the first 4 weeks following transplant, when the regenerative demand is highest and when we hypothesize miRNA-mediated gene repression is required, would more severely affect the ability of donor cells to contribute to the recipient hematopoietic reconstitution compared to T6B expression after homeostasis is reestablished.

Consistent with this prediction, mice that were administered doxycycline in the first 4 weeks post-transplant had significantly fewer CD45.2+ peripheral blood mononuclear cells (PBMCs; Figure 5D). Contribution to the B cell population was particularly impaired by T6B expression, but this was reversed once the recipients were taken off of doxycycline, consistent with the developmental block described earlier (Figure 3D, Figure 3—figure supplement 6). Interestingly, the decrease in total CD45.2+ PBMCs and CD45.2+ myeloid cells was not reversed by doxycycline withdrawal, which suggested that the T6B-expressing CD45.2+ HSCs might have been outcompeted by wild-type CD45.1+ HSCs in these recipients (Figure 5D). Consistent with this hypothesis, we observed a significant reduction in CD45.2+ HSCs only in the bone marrow of recipient animals that were fed a doxycycline-containing diet in the first 4 weeks post-transplant (Figure 5E).

Taken together, these results support a model where the miRNA-mediated gene regulation is conditionally essential for the maintenance of HSCs during acute regeneration but is largely dispensable under homeostasis.

### An essential role for miRNA-mediated gene repression in the skeletal muscle and in the heart

As previously discussed, we observed low or no expression of T6B in the heart and skeletal muscle of R26T6B mice treated with doxycycline (Figure 2—figure supplement 2), consistent with previous reports indicating that rtTA expression from the endogenous Rosa26 promoter is tissue restricted (Premsrirut et al., 2011). To extend the analysis of the phenotype caused by the loss of miRISC activity to these tissues, we crossed T6B transgenic mice with the Rosa26-CAGs-rtTA3 strain (Dow et al., 2014) in which the modified chicken beta-actin with CMV-IE enhancer (CAG) promoter (Niwa et al., 1991) drives a more ubiquitous expression of the rtTA variant rtTA3 (hereafter CAGT6B). As expected, the pattern and intensity of T6B expression upon dox administration in CAGT6B mice and R26T6B mice were largely overlapping, except for the heart and the skeletal muscle, for which significant T6B expression was only observed in CAGT6B mice (Figure 6A, Figure 2—figure supplement 2). RNAseq analyses confirmed inhibition of miRNA function in both heart and skeletal muscle of CAGT6B mice upon dox administration (Figure 6B).

![Figure 6.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig6-v2.jpg)

**Figure 6.:** The microRNA (miRNA) pathway is essential in heart and skeletal muscle during homeostasis.
(A) Detection of T6B expression with an anti-YFP antibody in the heart and skeletal muscle of R26T6B, CAGT6B, and R26CTL mice maintained on doxycycline-containing diet for 7 days. (B) Total RNA extracted from the heart (upper panel) and the skeletal muscle (lower panel) of CAGCTL and CAGT6B mice (n = 3 for each strain) maintained on dox for 7 days was analyzed by RNAseq. Left panels: scatter plot showing the effect of T6B expression on targets of conserved miRNA families was generated as described in Figure 1D. The abundance of each miRNA family was calculated using dataset from Isakova et al., 2020. Right panels: representative cumulative distribution plot of log2-fold changes in expression of predicted targets of the indicated miRNA families. (C) Kaplan–Meier curves of CAGT6B and CAGCTL mice (n = 8 for each genotype) maintained on doxycycline throughout the duration of the experiment. p-Value from log-rank test. (D) Upper row: representative H&E staining showing marked dilation of the four cardiac chambers in hearts of CAGT6B mice compared to controls (n = 9 for each genotype). Despite having thinner walls, the histomorphology of ventricular cardiomyofibers was within normal limits. Bottom row: representative H&E staining showing degenerative and regenerative changes in the skeletal muscle of the hind limbs of CAGT6B mice compared to controls (n = 9 for each genotype).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Body weight of CAGT6B and control mice maintained on doxycycline for up to 45 days was assessed the day on which euthanasia was performed.
n = 8 (four females and four males) for each genotype (age and sex matched). Mice were kept on doxycycline diet throughout the duration of the experiment, and control mice were euthanized at day 45. P-values: unpaired t-test.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Representative H&E staining showing vasculitis of the pulmonary veins as revealed by inflammatory immune cell infiltration of the vessel wall (arrows).

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/70948/elife-70948-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** T6B blocks miRNA activity in sea urchins and zebrafish.
(A) Left panel: representative examples of Mediterranean sea urchin (Paracentrotus lividus) zygotes injected with 1 pg of in vitro-transcribed mRNA coding for either T6B or T6BMut proteins and observed under DIC optics at 48 hr post-fertilization. Both embryos are oriented in a vegetal view. T6B-expressing embryos displayed severe developmental aberrations ranging from the failure to form a proper archenteron and skeletal structures, to overall delay in development and embryonic lethality. By contrast, control T6BMut-expressing embryos observed at the same developmental stage went through embryogenesis normally and exhibited the characteristic easel-like shape of the echinoid pluteus larva. Right panel: quantitative PCR showing dysregulation of territorial marker genes involved in the developmental gene regulatory network of the sea urchin (Cavalieri and Spinelli, 2015a, Cavalieri and Spinelli, 2015b) upon T6B expression. Data are indicated as fold difference in transcript abundance with respect to control T6BMut-expressing embryos at the same stage of development. The gray region represents changes in mRNA abundance corresponding to less than threefold difference, while error bars are standard errors for the qPCR replicates. PMCs: primary mesenchyme cells; SMCs: secondary mesenchyme cells. (B) Zebrafish (Danio rerio) fertilized eggs were injected with 75 pg of in vitro-transcribed mRNA coding for either T6B or T6BMut fusion proteins. While T6BMut-expressing embryos developed normally, the majority of T6B-expressing embryos underwent severe developmental defects.

In contrast to R26T6B mice, CAGT6B mice fed a doxycycline-containing diet showed a progressive decline in body mass (Figure 6—figure supplement 1) and died or reached a humane endpoint within 4–6 weeks (Figure 6C). The decrease in body mass was not caused by intestinal malabsorption as, similarly to what was observed in R26T6B mice, we found no evidence of architectural defects throughout the intestine. In contrast, histopathological examination of heart and skeletal muscle showed severe alterations in both organs, including dilated cardiomyopathy and diffuse muscular degeneration (Figure 6D). All mice also showed necro-inflammatory changes in the liver, variable alterations in the pancreas, and increased urea nitrogen and alanine aminotransferase levels in the serum. Such alterations are likely secondary to congestive heart failure and/or to severe muscle catabolism as they were not observed in R26T6B mice. Another phenotype that distinguished the R26T6B strain from the CAGT6B strain was the presence in the latter of vasculitis of pulmonary veins (Figure 6—figure supplement 2). A likely explanation is that these lesions are caused by increased pressure in the pulmonary veins secondary to congestive heart failure, but we cannot exclude that they reflect a direct effect of T6B expression on the pulmonary vasculature. Discriminating between these two possibility will require the use of transgenic mice harboring tissue-restricted rtTA transgenes.

The emergence of severe cardiac and skeletal muscle phenotypes, as opposed to the lack of obvious structural and functional abnormalities in most T6B-expressing tissues, points toward the existence of significant differences among adult tissues in their reliance on the miRNA pathway during homeostasis.

## Discussion

We report the generation of a novel genetically engineered mouse strain in which miRISC assembly and function can be temporally and spatially controlled in a reversible manner by a doxycycline-inducible transgene encoding a T6B-YFP fusion protein to address the role(s) miRNA-mediated gene regulation plays in vivo in adult tissues.

Surprisingly, in most adult tissues, we do not find an essential role for miRNA-mediated gene repression in organ homeostasis. A notable exception are the heart and the skeletal muscle, where miRISC inactivation in adult mice results in acute tissue degeneration and death even in the absence of tissue damage or exogenous stress.

Even though miRISC function is not overtly required for the homeostasis of other tissues, we have investigated the consequences of miRNA inhibition in the intestine and in the hematopoietic system of adult mice under homeostatic conditions and during tissue regeneration. These are tissues that periodically respond to external/internal stresses. In both tissues, we have found that miRISC activity is dispensable for homeostasis. However, miRNA function becomes essential during tissue regeneration following acute injury. These results lend experimental support to the hypothesis that a major role for miRNA-mediated gene repression is to support tissue adaptation to stress.

In previous studies where Dicer1 was conditionally ablated in the skeletal muscle of adult mice, muscle regeneration was impaired after acute injury, but no effect on muscle morphology or function was observed during homeostasis (Oikawa et al., 2019a; Oikawa et al., 2019b; Vechetti et al., 2019). An explanation for this difference is that in the Dicer1 conditional knockout experiments miRNA levels were only partially reduced even weeks after Dicer1 ablation, likely reflecting the high stability of these short non-coding RNAs. The T6B mouse strain we describe here overcomes this major limitation and allows the rapid and effective inhibition of miRNA activity independently from the half-life of these molecules.

In this article, we have focused on the role of miRNA-mediated gene repression in adult mice. The same strategy for the acute inhibition of miRISC activity can in principle be applied to other organisms. We have found that expression of T6B in embryos of both sea urchin (Paracentrotus lividus) and zebrafish (Danio rerio) induces developmental defects and gene expression changes consistent with the essential role of the miRNA pathway during development (Ambros and Horvitz, 1984; Chalfie et al., 1981; Lee et al., 1993; Reinhart et al., 2000; Song et al., 2012; Wienholds et al., 2003; Wightman et al., 1993, Figure 6—figure supplement 3). Considering that in vitro T6B efficiently binds to AGO proteins from different non-mammalian organisms (Hauptmann et al., 2015), these findings are not unexpected, yet they highlight the usefulness of the T6B system for dissecting the miRNA pathway in a variety of animal models.

Despite its many advantages, the T6B mouse strain has also some unique limitations that need to be considered when designing and interpreting experiments.

First, although our biochemical and computational analysis of cells and tissues expressing T6B indicates that the peptide can effectively impair miRISC function, we cannot exclude some residual miRISC activity even in cells expressing high levels of the T6B transgene. The observation that we can recapitulate phenotypes observed in mice harboring complete targeted deletion of miR-143/145 miRNAs in the intestine (Chivukula et al., 2014) and of miR-17–92 and miR-451 in the hematopoietic system (Koralov et al., 2008; Patrick et al., 2010; Ventura et al., 2008) is reassuring in this respect. For example, consistent with observations made in the regenerating intestine of miRNA-143/145 knockout mice (Chivukula et al., 2014), we did not record any abnormalities or toxicity during the normal intestinal homeostasis of R26T6B mice, whereas T6B expression became lethal during intestinal regeneration. Moreover, in the hematopoietic system, abnormalities were mostly restricted to B cell maturation, which are consistent with a developmental block at the Pro-B to Pre-B transition found in mir17–92 knockout mice (Ventura et al., 2008). Finally, we also observed a statistically significant decrease in hematocrit, erythrocyte volume, and hemoglobin content in adult T6B-expressing mice, analogous to what was reported in mice harboring targeted deletion of miR-451 (Patrick et al., 2010).

In contrast, some of our results markedly differ from the results obtained by conditional ablation of Dicer1 in mice. For example, conditional knockout of Dicer1 in the hematopoietic system has been reported to result in the rapid depletion of HSCs (Guo et al., 2010b). Furthermore, the lack of an overt phenotype in the intestine contrasts with previous reports showing that postnatal, conditional deletion of Dicer1 results in depletion of goblet cells (Biton et al., 2011; McKenna et al., 2010), in addition to abnormal vacuolation and villous distortion in the small intestine (Huang et al., 2012; McKenna et al., 2010). We cannot exclude that these differences are due to an incomplete inactivation of the miRNA pathway in T6B mice, but an alternative explanation is that they reflect the well-characterized miRNA-independent functions of DICER.

Another limitation to be considered is the possibility that T6B expression impairs the activity of other complexes in addition to the miRISC. Although RNAseq analysis of cells expressing T6B has not revealed changes that are not explained by loss of miRNA-mediated gene repression and the phenotypes observed are consistent with loss of miRNA activity, this possibility cannot be formally excluded at this time. Further studies to experimentally identify T6B interactors in cells and tissues will be important to formally address this possibility.

In conclusion, we have developed a novel mouse strain that enables investigating the role of miRNA-mediated gene repression in adult organisms. The body of data presented here suggests that in adult animals miRNAs primarily provide for the ability to adaptively change gene expression in response to the physiological and pathological stresses that accompany metazoans’ life. It is likely that the specific miRNAs and stresses differ based on the adult organ or tissue being studied, and the model we have generated will be useful to address these important aspects of miRNA biology.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Strain, strain background(Mus musculus)</td>
      <td>T6B</td>
      <td>This paper</td>
      <td>Stock #036470</td>
      <td>The T6Bwt allele is integrated in the Col1a1 locus</td>
    </tr>
    <tr>
      <td>Strain, strain background(M. musculus)</td>
      <td>CD45.1+ C57BL/6 (BoyJ)</td>
      <td>Jackson Laboratory</td>
      <td>RRID:IMSR_JAX:002014</td>
      <td>Carries the differential Ptprca
 pan leukocyte marker</td>
    </tr>
    <tr>
      <td>Strain, strain background(M. musculus)</td>
      <td>C57BL/6J</td>
      <td>Jackson Laboratory</td>
      <td>RRID:IMSR_JAX:000664</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background(M. musculus)</td>
      <td>Rosa26-CAGs-rtTA3</td>
      <td>Jackson Laboratory</td>
      <td>RRID:IMSR_JAX:029627</td>
      <td>The CAG promoter drives the expression of rtTA3</td>
    </tr>
    <tr>
      <td>Cell line (M. musculus)</td>
      <td>KH2</td>
      <td>PMID:16400644</td>
      <td>RRID:CVCL_C317</td>
      <td>Embryonic stem cells</td>
    </tr>
    <tr>
      <td>Cell line (M. musculus)</td>
      <td>DR4</td>
      <td>ATCC</td>
      <td>RRID:CVCL_VK72</td>
      <td>Irradiated feeder cells</td>
    </tr>
    <tr>
      <td>Transfected construct(M. musculus)</td>
      <td>Silencer GAPDH siRNA</td>
      <td>Thermo Fisher</td>
      <td>#AM4624</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct(M. musculus)</td>
      <td>Negative Control 1 siRNA</td>
      <td>Thermo Fisher</td>
      <td>#AM4611</td>
      <td>Nontargeting control</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-E-cadherin(mouse monoclonal)</td>
      <td>BD</td>
      <td>#610181</td>
      <td>IF: (1:750)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-lysozyme(rabbit polyclonal)</td>
      <td>Thermo Fisher</td>
      <td>#RB-372-A1</td>
      <td>IF: (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-PH3(mouse monoclonal)</td>
      <td>Cell Signaling</td>
      <td>#970</td>
      <td>IF: (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-YFP(rabbit polyclonal)</td>
      <td>Invitrogen</td>
      <td>#A11122</td>
      <td>IF: (1:250)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Ki67(rabbit monoclonal)</td>
      <td>Cell Signaling</td>
      <td>#12202</td>
      <td>IF: (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Rabbit IgG, Alexa Fluor 488(goat polyclonal)</td>
      <td>Thermo Fisher</td>
      <td>#A11034</td>
      <td>IF: (1:250)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse IgG2a, Alexa Fluor 594(goat polyclonal)</td>
      <td>Thermo Fisher</td>
      <td>#A-21135</td>
      <td>IF: (1:250)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GFP(chicken polyclonal)</td>
      <td>Abcam</td>
      <td>#ab13970</td>
      <td>IF: (1:250)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat IgG(rat polyclonal)</td>
      <td>Sigma</td>
      <td>#I-8015</td>
      <td>IF: (1:250)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GW182(rabbit polyclonal)</td>
      <td>Bethyl</td>
      <td>#A302-329A</td>
      <td>WB: (1:1000, in 5% milk)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Ago2(rabbit monoclonal)</td>
      <td>Cell Signaling</td>
      <td>#2897</td>
      <td>WB: (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-RPL26(rabbit polyclonal)</td>
      <td>Bethyl</td>
      <td>#A300-686A</td>
      <td>WB: (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GAPDH(mouse monoclonal)</td>
      <td>Sigma</td>
      <td>#G8795</td>
      <td>WB: (1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-β-actin(mouse monoclonal)</td>
      <td>Sigma</td>
      <td>#A2228</td>
      <td>WB: (1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-tubulin(mouse monoclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>#T9026</td>
      <td>WB: (1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-HA(rabbit monoclonal)</td>
      <td>Cell Signaling</td>
      <td>#C29F4</td>
      <td>WB: (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-rabbit IgG, HRP-conjugated(donkey polyclonal)</td>
      <td>GE Healthcare</td>
      <td>#NA934</td>
      <td>WB: (1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse IgG, HRP-conjugated(sheep polyclonal)</td>
      <td>GE Healthcare</td>
      <td>#NA931</td>
      <td>WB: (1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-AGO2(mouse monoclonal)</td>
      <td>WAKO</td>
      <td>#011-22033</td>
      <td>IP: (1 µg/100 µl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-AGO1-4(mouse monoclonal)</td>
      <td>EMD Millipore</td>
      <td>#MABE56</td>
      <td>IP: (1 µg/100 µl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-FLAG(mouse monoclonal)</td>
      <td>Cell Signaling</td>
      <td>#8146S</td>
      <td>IP: (1 µg/100 µl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-HA(mouse monoclonal)</td>
      <td>Cell Signaling</td>
      <td>#2367S</td>
      <td>IP: (1 µg/100 µl)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IgG1 isotype(mouse monoclonal)</td>
      <td>Cell Signaling</td>
      <td>#5415</td>
      <td>IP: (1 µg/100 µl)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCAGGS-flpE-puro (plasmid)</td>
      <td>Addgene</td>
      <td>RRID:Addgene_20733</td>
      <td>Flippase recombinase-expressing vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pgk-ATG-frt plasmid</td>
      <td>Addgene</td>
      <td>RRID:Addgene_20734</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Col1a1 common _F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AATCATCCCAGGTGCACAGCATTGCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Col1a1 wildtype _R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CTTTGAGGGCTCATGAACCTCCCAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Col1a1 mutant _R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>ATCAAGGAAACCCTGGACTACTGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>R26_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AAAGTCGCTCTGAGTTGTTAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>R26a_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GCGAAGAGTTTGTCCTCAACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>R26b_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CCTCCAATTTTACACCTGTTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>T6B-YFP_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GACTACAAGGACGACGATGACAAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>T6B-YFP_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GTTACTTGTACAGCTCGTCCATG</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNAscope 2.5 HD Detection Reagent, BROWN</td>
      <td>ACD</td>
      <td>#320771</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNAScope Igfbp5 Probe</td>
      <td>ACD</td>
      <td>#425738</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Superose 6 10/300 GL</td>
      <td>Cytiva</td>
      <td>#GE17-5172-01</td>
      <td>Now available as Increase 10/300 GL,Cytiva #GE29-0915-96</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Novex NuPAGE SDS/PAGE gel system</td>
      <td>Thermo Fisher</td>
      <td>#NP0321</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>EnVision + HRP</td>
      <td>DAKO, Glostrup, Denmark</td>
      <td>#K401111-2, RRID:AB_2827819</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>GFP-trap</td>
      <td>Chromotek</td>
      <td>#gtma-10RRID:AB_2827592</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TruSeq Stranded mRNA LT Kit,</td>
      <td>Illumina</td>
      <td>#RS-122-2102</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>OMERO</td>
      <td>PMID:22373911</td>
      <td>RRID:SCR_002629</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STAR v2.5.3a</td>
      <td>PMID:23104886</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq2</td>
      <td>PMID:25516281</td>
      <td>RRID:SCR_015687</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>miRbase version 21</td>
      <td>https://www.mirbase.org/</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>TargetScan</td>
      <td>PMID:26267216</td>
      <td>RRID:SCR_010845</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Doxycyline-containingRodent diet</td>
      <td>Envigo</td>
      <td>#TD01306</td>
      <td>625 mg/kg doxycycline</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dextran sulfate sodium (DSS)</td>
      <td>Cayman Chemical</td>
      <td>#23250</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Surgipath Decalcifier I</td>
      <td>Leica Biosystems</td>
      <td>#3800400</td>
      <td>Formic acid solution</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>EDTA-free complete protease inhibitors</td>
      <td>Sigma-Aldrich</td>
      <td>#11836170001</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>KnockOut DMEM</td>
      <td>GIBCO</td>
      <td>#10829018</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Phosphate inhibitors</td>
      <td>Roche</td>
      <td>#04906837001</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>TRIzol Reagent</td>
      <td>Thermo Fisher</td>
      <td>#15596026</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DAPI stain</td>
      <td>Sigma-Aldrich</td>
      <td>#62248</td>
      <td>5 μg/ml</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Mowiol 4-88</td>
      <td>Calbiochem</td>
      <td>#475904100 GM</td>
      <td>Mounting media</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>GlutaMax</td>
      <td>GIBCO</td>
      <td>#35050061</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>A/G PLUS-Agarose beads</td>
      <td>Santa Cruz</td>
      <td>#2003</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>RIPA buffer</td>
      <td>Sigma-Aldrich</td>
      <td>#R0278</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Lipofectamine RNAiMAX</td>
      <td>Thermo Fisher</td>
      <td>#13778100</td>
      <td>Transfection reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Alexa Fluor 488 tyramide signal amplification reagent</td>
      <td>Life Technologies</td>
      <td>B40953</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Animal models

The Rosa26rtTA/rtTA; Col1a1T6B/T6B
 (R26T6B) mice were generated by site-specific integration of the transgene coding for the FLAG-HA-T6B-YFP fusion protein within the Col1a1 locus of KH2 embryonic stem cells (Col1a1-frt/Rosa26 rtTA; Beard et al., 2006). Briefly, the FLAG-HA-T6B-YFP (FH-T6B-YFP) DNA fragment was subcloned into the targeting vector, as described in ‘Vectors and molecular cloning.’ A mixture of 5 µg of the targeting vector and 2.5 µg of the pCAGGS-flpE-puro (Addgene #20733), Flippase recombinase-expressing vector was electroporated into KH2 cells, using 4D-Nucleofector core unit (Lonza), following the manufacturer’s ‘primary cells P3’ protocol. Selection of targeted clones was initiated 48 hr after electroporation, using 150 µg hygromycin per ml of culture medium. 10 days later, individual hygromycin-resistant ES cell clones were analyzed by PCR to confirm correct integration of the knock-in allele. Clones carrying the correctly integrated knock-in allele were genotyped using a three-primer PCR, with the following primers: (1) 5′-AATCATCCCAGGTGCACAGCATTGCGG-3′; (2) 5′-CTTTGAGGGCTCATGAACCTCCCAGG-3′; and (3) 5′-ATCAAGGAAACCCTGGACTACTGCG-3′. A 287-bp-long PCR product indicates successful integration of the transgene into the Col1a1 locus, while a 238-bp-long PCR product indicates a wild-type, untargeted locus. Two independent ES clones were injected into C57BL/6J albino blastocysts and backcrossed the resulting chimeras to C57BL/6J mice to achieve germline transmission of the recombinant allele. F1 animals were then intercrossed to generate animals expressing rtTA from the Rosa26 locus under control of the Rosa26 endogenous promoter, while expressing the T6B fusion protein from the Col1a1 locus under control of the tetracycline-responsive element (TRE) and the minimal CMV promoter. Animals were genotyped as follows: to assess the presence of the transgene in the Col1a1 locus, PCR was carried out as for the genotyping of KH2 cells. To assess the presence of the rtTA transgene in the Rosa26 locus, a three-primer PCR was performed, with the following primers: (1) 5′-AAAGTCGCTCTGAGTTGTTAT-3′; (2) 5′-GCGAAGAGTTTGTCCTCAACC-3′; and (3) 5′-CCTCCAATTTTACACCTGTTC-3′. A 350-bp-long PCR product indicates the presence of the rtTA transgene into the Rosa26 locus, while a 297-bp-long PCR product indicates the presence of a wild-type locus. CAGrtTA/rtTA; Col1a1T6B/T6B
 (CAGT6B) mice were generated by backcrossing R26T6B mice with Rosa26-CAGs-rtTA3 mice (a gift from Scott Lowe, MSKCC). In the Rosa26-CAGs-rtTA3 mice, the knock-in allele has the CAG promoter driving the expression of the third-generation reverse tetracycline-regulated transactivator gene (rtTA3), all inserted into the Gt(ROSA)26Sor locus. In vivo doxycycline-dependent expression of the FLAG-HA-T6B-YFP transgene was achieved by feeding mice chow that contained doxycycline at the concentration of 625 mg/kg (Envigo #TD01306). Mice were maintained and euthanized in accordance with a protocol approved by the Memorial Sloan Kettering Cancer Center Institutional Animal Care and Use Committee. The T6B transgenic strain has been deposited at the Jackson Laboratory (JAX stock #036470).

### Necropsy, staining, and histopathology

Mice were euthanized with CO2. Following gross examination, all organs were fixed in 10% neutral buffered formalin, followed by decalcification of bone in a formic acid solution (Surgipath Decalcifier I, Leica Biosystems). Tissues were then processed in ethanol and xylene and embedded in paraffin in a Leica ASP6025 tissue processor. Paraffin blocks were sectioned at 5 µm, stained with hematoxylin and eosin (H&E), and examined by a board-certified veterinary pathologist. The following tissues were processed and examined: heart, thymus, lungs, liver, gallbladder, kidneys, pancreas, stomach, duodenum, jejunum, ileum, cecum, colon, lymph nodes (submandibular, mesenteric), salivary glands, skin (trunk and head), urinary bladder, uterus, cervix, vagina, ovaries, oviducts, adrenal glands, spleen, thyroid gland, esophagus, trachea, spinal cord, vertebrae, sternum, femur, tibia, stifle join, skeletal muscle, nerves, skull, nasal cavity, oral cavity, teeth, ears, eyes, pituitary gland, and brain. To detect goblet cells in the intestine, the AB/PAS kit (Thermo Fisher #87023) was used according to the manufacturer’s instructions.

### Immunofluorescence

For the staining of intestine sections shown in Figure 3 and Figure 3—figure supplement 2, formalin-fixed, paraffin-embedded (FFPE) slides were deparaffinized and rehydrated according to a standard xylene/ethanol series. After heat-induced epitope retrieval in sodium citrate (pH 6), tissue sections were permeabilized in triton X-100, blocked, and incubated with the following 1° antibodies: PH3 (Cell Signaling #970) at 1:200 dilution; lysozyme (Thermo Fisher #RB-372-A1) at 1:200 dilution; E-cadherin (BD #610181) at 1:750 dilution; YFP (Invitrogen #A11122) at 1:250 dilution; and Ki67 (Cell Signaling #12202) at 1:400 dilution. Next, cells were washed with PBS containing 0.05% Triton X and incubated with the following 2° antibodies: goat anti-rabbit IgG, Alexa Fluor 488 (Thermo Fisher #A11034) at 1:250 dilution; goat anti-mouse IgG2a, Alexa Fluor 594 (Thermo Fisher #A11029) at 1:250 dilution. For the staining of tissue sections shown in Figures 2 and 4 and Figure 2—figure supplement 2, FFPE tissue sections were cut at 5 μm and heated at 58°C for 1 hr. The antibody against GFP (Abcam, ab13970, 2 µg/ml) was incubated for 1 hr and detected with Leica Bond RX. Appropriate species-matched secondary antibody and Leica Bond Polymer anti-rabbit HRP were used, followed by Alexa Fluor 488 tyramide signal amplification reagent (Life Technologies, B40953). After staining, slides were washed in PBS and incubated in 5 μg/ml 4′,6-diamidino-2-phenylindole (DAPI; Sigma-Aldrich) in PBS (Sigma-Aldrich) for 5 min, rinsed in PBS, and mounted in Mowiol 4-88 (Calbiochem). Slides were kept overnight at –20°C before imaging.

### Immunohistochemistry

For immunohistochemistry, deparaffinized sections were subjected to antigen retrieval and processed with the EnVision + HRP kit (K401111-2, DAKO, Glostrup, Denmark) according to the manufacturer’s instructions. A primary polyclonal antibody against Ki67 (Cell Signaling #12202) at 1:400 dilution was diluted in Antibody Diluent (DAKO #S0809) and incubated overnight at 4°C. Next, sections were incubated in the provided anti-rabbit HRP-labeled polymer reagent, and detection was performed according to the manufacturer’s protocol. Images were acquired using an Olympus BX-UCB slide scanner.

### RNA in situ hybridization

5 μm sections were obtained from FFPE colons from age/sex-matched mice. Before staining, tissue slides were deparaffinized, rehydrated, and permeabilized according to standard procedures. Detection was carried out using RNAscope 2.5 HD Detection Reagent, BROWN (ACD # 320771), with a specific RNAScope Igfbp5 Probe (ACD #425738), according to the manufacturer’s instructions.

### Serum chemistry and hematology

For serum chemistry, blood was collected into tubes containing a serum separator, the tubes were centrifuged, and the serum was obtained for analysis. Serum chemistry was performed on a Beckman Coulter AU680 analyzer, and the concentration of the following analytes was determined: alkaline phosphatase, alanine aminotransferase, aspartate aminotransferase, creatine kinase, gamma-glutamyl transpeptidase, albumin, total protein, globulin, total bilirubin, blood urea nitrogen, creatinine, cholesterol, triglycerides, glucose, calcium, phosphorus, chloride, potassium, and sodium. Na/K ratio and albumin/globulin ratio were calculated. For hematology, blood was collected retro-orbitally into EDTA microtainers. Automated analysis was performed on an IDEXX Procyte DX hematology analyzer.

### DSS treatment and post-DSS treatment quantitative analyses

Mice kept in doxycycline-containing chow were treated for 5 days with 4% w/v DSS (FW 40.000; Cayman Chemical #23250) dissolved in drinking water. Body mass was monitored daily. Measurements of colon length, aggregated length of ulcers, percentage of colon with ulcers, area of ulcers, the number of immune nodules, and the area of immune nodules were obtained using OMERO (https://www.openmicroscopy.org/omero/). Measurements of these parameters were used to estimate the extent of damage and colitis induced by DSS treatment. All measurements were acquired from H&E-stained colon sections. Ulcer was defined as regions of colon with complete/partial loss of epithelial structure, accompanied by massive immune infiltrates. Colon length was measured by tracing the length of muscular layer of each colon. Length of ulcer was measured as the added length of each ulcerated region along the colon. Ulcer percentage was calculated as the length of ulcer/length of colon. The area of each individual ulcer was also measured and summed for each animal. Clear immune nodules are visible, showing aggregates of immune cells with high nucleus/cytoplasm ratio. Number and area of the immune nodules were summarized for each animal.

### Tissue isolation and total lysates preparation

Organs extracted from 8- to 12-week-old mice, perfused with PBS, were snap-frozen in liquid nitrogen and stored at −80°C until further processing. To prepare total extract from solid tissues, tissues were pulverized using a mortar, resuspended in 1 ml of lysis buffer per cm3 of tissue, and dounce-homogenized with a tight pestle until completely homogenized. Next, extracts were cleared by centrifugation at 20,000× g for 5 min followed by a second step of centrifugation at 20,000× g for 5 min. To prepare total extracts from cultured cells, pelleted cells were snap frozen in liquid nitrogen and stored at −80°C until further processing. Pellets were then resuspended in lysis buffer, incubated for 10 min on ice, and cleared by centrifugation at 20,000× g. Two different lysis buffers were used, depending on the specific downstream application. For IP and SEC, lysates were prepared in SEC buffer (150 mM NaCl, 10 mM Tris-HCl pH 7.5, 2.5 mM MgCl2, 0.01% Triton X-100). For western blotting applications, lysates were prepared in RIPA buffer (Sigma-Aldrich #R0278). Upon usage, both buffers were supplemented with the addition of EDTA-free complete protease inhibitors (Sigma-Aldrich #11836170001), phosphate inhibitors (Roche #04906837001), and 1 mM DTT.

### Cell lines and culture conditions

Cell lines were maintained in log-phase growth in a humidified incubator at 37°C, 5% CO2 prior to experimental manipulation. HCT116 colorectal adenocarcinoma cells were obtained from ATCC prior to this study and tested negative for Mycoplasma and were maintained in McCoy’s medium supplemented with 10% heat-inactivated fetal calf serum (FCS, GIBCO, Cat#16141079), 10 U/ml penicillin/streptomycin, and 2 mM L-glutamine. MEFs were grown in Dulbecco’s Modified Eagle Medium (DMEM) supplemented with 10% heat-inactivated FCS (GIBCO), 10 U/ml penicillin/streptomycin, and 2 mM L-glutamine. KH2 embryonic stem cells were cultured in gelatin-coated plates in the presence of irradiated DR4 Mouse Embryonic Fibroblasts (Thermo Fisher #A34966), and maintained in KnockOut DMEM (GIBCO, Cat#10829018), supplemented with 15% FCS (GIBCO), GlutaMax (GIBCO Cat#35050061), 100 µM non-essential amino acids (Sigma-Aldrich Cat#M7145), 1000 U/ml leukemia inhibitory factor (LIF, Millipore Cat#ESG1107), 10 U/ml penicillin/streptomycin (GIBCO Cat#15070063), 100 mM 2-mercaptoethanol (Bio-Rad Cat#1610710), and nucleosides (Millipore Cat#ES-008-D).

### Flow cytometry

Analysis of bone marrow populations was performed by harvesting femurs and tibiae from euthanized mice. Bone marrow was isolated by centrifugation, resuspended in FACS buffer (PBS with 2% FCS), and passed through a 40 µm cell strainer to make a single-cell suspension. Nonspecific antibody binding was blocked by incubation with 10 µg/ml rat IgG (Sigma #I-8015) for 15 min on ice. Antibodies used to identify HSCs included a cocktail of biotinylated lineage antibodies (Gr1, CD11b, TER119, B220, CD3, CD4, CD8), CD117 (c-kit) APC (2B8), Sca-1 (D7) PE-cy7, CD150 PE, and CD48 Pacific Blue. B cell progenitors were identified with the following antibodies: B220, CD19, CD25, CD43, IgM, IgD, and c-kit. For analysis of PBMCs, blood was collected retro-orbitally from live mice into EDTA microtainers. Whole blood was lysed in ACK buffer for 5 min at room temperature, washed with FACS buffer, and pelleted prior to antibody staining. Mature blood populations were identified with the following antibodies: CD45.1, CD45.2, Gr1, CD11b, B220, and CD3. Cells were incubated with primary antibodies for 45 min, washed once with FACS buffer, and incubated with BV711 streptavidin conjugate for 15 min. All incubations were carried out on ice and protected from light. Antibodies were purchased from BioLegend or eBioscience.

### Bone marrow transplantation

8- to 12-week-old CD45.1+ C57BL/6 (BoyJ) mice (JAX) were lethally irradiated by exposure to 1100 cGy of gamma irradiation from a cesium source, administered in two doses, split 4 hr apart. Bone marrow suspensions from CAGT6B (CD45.2+) and BoyJ mice were counted, mixed 1:1, and transferred intravenously by retro-orbital injection into isofluorane-anesthetized, irradiated recipients.

### Size-exclusion chromatography (SEC)

SEC was performed using a Superose 6 10/300 GL prepacked column (GE Healthcare) equilibrated with SEC buffer essentially as previously described (La Rocca et al., 2015; Olejniczak et al., 2013). Briefly, 400 μl (1.5–2 mg) of total extracts precleared by centrifugation were run on the SEC column at a flow rate of 0.3 ml/min. 1 ml fractions were collected. Proteins were extracted from each fraction by TCA precipitation following standard procedures and run on SDS-PAGE gels for western blotting analysis.

### Western blotting and antibodies

Western blotting was performed using the Novex NuPAGE SDS/PAGE gel system (Invitrogen). Total cell lysates were run either on 3–8% Tris-acetate or 4–12% Bis-Tris precast gels, transferred to nitrocellulose membranes, and probed with antibodies specific to proteins of interest. Detection and quantification of blots were performed on Amersham hyperfilm ECL (Cytiva #28906839) and developed on film processor SRX-101A (Konica). Antibodies used for western blots were obtained from commercial sources as follows: anti-GW182 (Bethyl #A302-239A), anti-Ago2 (Cell Signaling #2897), anti-PABP1 (Cell Signaling #4992), anti-RPL26 (Bethyl #A300-686A), anti-GAPDH (Sigma #G8795), anti-β-actin (Sigma #A2228), anti-GFP (Roche #11814460001), anti-tubulin (Sigma-Aldrich #T9026), anti-HA (Cell Signaling #C29F4), anti-rabbit IgG, HRP-conjugated (GE Healthcare #NA934), and anti-mouse IgG, HRP-conjugated (GE Healthcare #NA931).

### Immunoprecipitation (IP)

For IP of AGO-T6B complexes from human HCT116 cells, 500 μg of lysates in 500 μl of SEC buffer were incubated for 3 hr with primary antibodies directed to either AGO proteins (WAKO anti-AGO2 #011-22033, EMD Millipore anti-panAGO #MABE56) or directed to T6B-fusion protein (Cell Signaling anti-FLAG #8146S, Cell Signaling anti-HA #2367S) or mouse IgG1 isotype control (Cell Signaling #5415). Next, lysates were incubated with 20 µl of protein A/G PLUS-Agarose beads (Santa Cruz #2003) for 1 hr. For IP of AGO-T6B complexes from mouse tissues, 500 μg of lysates in 500 μl of SEC buffer were incubated for 2 hr with GFP-trap magnetic agarose beads (Chromotek #gtma-10) or binding control beads (Chromotek #bmab-20). The immune complexes were run on SDS-PAGE and analyzed by western blotting.

### Vectors and molecular cloning

The targeting vector expressing the FH-T6B-YFP under control of TRE and CMV minimal promoter was generated from a modified version of the pgk-ATG-frt plasmid (Addgene plasmid #20734), in which the region of pgk-ATG-frt comprised between the EcoRI site and the PciI site was substituted with the rabbit β-globin polyadenylation signal (RBG pA). The FH-T6B-YFP DNA insert was generated by PCR using the plasmid pIRES-Neo-FH-T6B-YFP58 as a template. PCR was carried out using the following primers: forward: 5′-GACTACAAGGACGACGATGACAAG-3′, reverse: GTTACTTGTACAGCTCGTCCATG. Next, the modified pgk-ATG-frt was cut with NcoI, filled-in to produce blunt ends, dephosphorylated, and ligated to the PCR-generated FH-T6B-YFP DNA fragment according to standard subcloning procedures. A scheme of the cloning strategy is shown as follows:

![Scheme 1.](https://cdn.elifesciences.org/articles/70948/elife-70948-scheme1-v2.jpg)

**Scheme 1.:** Cloning strategy for the generation of the targeting vector expressing the FH-T6B-YFP transgene.

To generated cell lines expressing either FH-T6B-YFP or FH-T6BMut-YFP fusion proteins in a doxycycline-inducible manner, a modified version of the retroviral vector pSIN-TREtight-HA-UbiC-rtTA3-IRES-Hygro (hereafter TURN vector, a gift from Scott Lowe) was used to transduce commercially available HCT116 and MEFs cell lines. TURN is an all-in-one Tet-on vector that includes (1) the rtTA3 gene under the human ubiquitin C promoter and (2) the transgene of interest driven by a TRE/CMV promoter. We used the pIRES-Neo-FH-T6B-YFP described in Hauptmann et al., 2015 as a template to generate by PCR the DNA fragments coding either for FH-T6B-YFP or for FH-T6BMut-YFP fusion proteins. DNA fragments were then inserted into the XhoI/EcoRI-digested TURN vector to generate TURNT6B and TURNT6Bmut vectors used for the transduction of parental HCT116 and MEFs.

### Small RNA transfection

Silencer GAPDH siRNA (Thermo Fisher AM4624) and Silencer Select Negative Control 1 siRNA (Thermo Fisher AM4611) small RNAs were transfected at 10 pM per 1 × 106 cells. MEFs were reverse transfected using Lipofectamine RNAiMAX. Lipofectamine RNAiMAX was combined with 20 µM small RNAs at a 4:3 ratio (vol:vol) in Opti-MEM and incubated for 20 min at room temperature. Trypsinized cells were added to culture dishes containing siRNAs and Lipofectamine RNAiMAX at 3.8 × 104 cells per cm2. Three volumes of complete medium were added to culture dishes, and cells were incubated for 2–3 days before further processing.

### Small RNA sequencing

Total RNA was extracted from MEFs transduced with the retroviral vectors encoding a doxycycline-inducible T6B or T6Bmut transgene and cultured in the presence or absence of doxycycline. Small RNA-seq library preparation was as described in Hafner et al., 2011. Briefly, 1 µg total RNA was ligated to nine distinct pre-adenylated 26-nt 3′-adapters with a 5-nt barcode using a mutated and truncated Rnl2 followed by urea gel purification and size selection and 5′-adapter ligation with Rnl1. This ligation reaction was again gel-purified and size-selected for fully ligated product and reverse-transcribed using SuperScript III RT followed by PCR amplification using Taq polymerase for 25 cycles. The final PCR product was separated on a 2% agarose gel in TBE buffer and extracted using the QIAgen gel extraction kit according to the manufacturer’s instructions including all optional steps. After high-throughput sequencing, small RNA reads were aligned to a miRNA genome index built from 1915 murine pre-miRNA sequences from miRbase version 21 (Kozomara et al., 2019; ftp://mirbase.org/pub/mirbase/21/) using Bowtie v2.4.296. Mature miRNA abundance was calculated by counting reads falling within 4 bps at each of the 5′ and 3′ end of the annotated mature miRNAs. miRNA seed family data were downloaded from the TargetScan website at http://www.targetscan.org/cgi-bin/targetscan/data_download.cgi?db=mmu_71. For miRNA family-level analysis, read counts mapping to members of the same miRNA family were summed up.

### RNAseq analysis

Total RNA from heart, skeletal muscle, colon, and liver of sex-matched littermate animals, and total RNA from cell lines were extracted using TRIzol Reagent (Invitrogen) according to the manufacturer’s instructions and subjected to DNase (QIAGEN) treatment. After RiboGreen quantification and quality control by Agilent BioAnalyzer, 500 ng of total RNA with RIN values of 7.0–10 underwent polyA selection and TruSeq library preparation according to the instructions provided by Illumina (TruSeq Stranded mRNA LT Kit, Cat#RS-122-2102), with eight cycles of PCR. Samples were barcoded and run on a HiSeq 4000 in a PE50/50 run using the HiSeq 3000/4000 SBS Kit (Illumina). An average of 34 million paired reads was generated per sample. The percent of mRNA bases averaged 60% over all samples. Reads were aligned to the standard mouse genome (mm10) using STAR v2.5.3a (Dobin et al., 2013). RNA reads aligned were counted at each gene locus. Expressed genes were subjected to differential gene expression analysis using DESeq2 (Love et al., 2014), and log2-fold changes were determined comparing T6B-expressing tissues to controls.

### Z-score calculation

For each conserved miRNA families, the mean log2-fold change of predicted targets, as defined by TargetScan, compared to the rest of the transcriptome (background), was calculated. The means were converted to z-scores as described by Kim and Volsky, 2005: Z-score = (Sm - µ)*m1/2*∂–1, where Sm is the mean of log2-fold changes of genes for a given gene set, m is the size of the gene set, and µ and ∂ are the mean and the standard deviation of background log2-fold change values.

### Real-time quantitative PCR

Real-time quantitative PCR analysis to assess the expression levels of the territorial marker genes involved in the developmental gene regulatory network of the sea urchin was conducted as previously described by Cavalieri et al., 2009. Briefly, total RNA from batches of 150 microinjected embryos was extracted by using the High Pure RNA Isolation kit (Roche). RNA samples were treated with reagents provided by the Turbo DNA-free kit (Ambion) and resuspended in a final volume of 30 µl. Reverse transcription into cDNA was performed in an 80 µl reaction using random hexamers and the TaqMan Reverse Transcription Reagents kit (Applied Biosystems). The resulting cDNA sample was further diluted, and the equivalent amount corresponding to one embryo was used as template for Q-PCR analysis. Q-PCR experiments were performed from two different batches, and all reactions were run in triplicate on the 7300 Real-Time PCR system (Applied Biosystems) using SYBR Green detection chemistry (Applied Biosystems). ROX was used as a measure of background fluorescence, and MBF-1 and z12 mRNAs were used as internal controls. At the end of the amplification reactions, a ‘melting-curve analysis’ was run to confirm the homogeneity of all Q-PCR products. Calculations from Q-PCR raw data were performed by the RQ Study software version 1.2.3 (Applied Biosystems) using the comparative Ct method (Ct). Oligonucleotide primer pairs used for qPCR reactions and amplicon lengths have been described previously (Cavalieri et al., 2008, Cavalieri et al., 2011, Cavalieri and Spinelli, 2014, Cavalieri et al., 2017, Turturici et al., 2018).
