# Overexpression screen of interferon-stimulated genes identifies RARRES3 as a restrictor of Toxoplasma gondii infection

## Authors

- Nicholas Rinkenberger<sup>1</sup>
- Michael E Abrams<sup>2</sup>
- Sumit K Matta<sup>1</sup>
- John W Schoggins<sup>2</sup> ([ORCID: 0000-0002-7944-6800](https://orcid.org/0000-0002-7944-6800))
- Neal M Alto<sup>2</sup> ([ORCID: 0000-0002-7602-3853](https://orcid.org/0000-0002-7602-3853))
- L David Sibley<sup>1</sup> ([ORCID: 0000-0001-7110-0285](https://orcid.org/0000-0001-7110-0285)) †

### Affiliations

1. Department of Molecular Microbiology, Washington University in St. Louis St Louis United States
2. Department of Microbiology, University of Texas Southwestern Dallas United States

† Corresponding author

## Abstract

Toxoplasma gondii is an important human pathogen infecting an estimated one in three people worldwide. The cytokine interferon gamma (IFNγ) is induced during infection and is critical for restricting T. gondii growth in human cells. Growth restriction is presumed to be due to the induction of interferon-stimulated genes (ISGs) that are upregulated to protect the host from infection. Although there are hundreds of ISGs induced by IFNγ, their individual roles in restricting parasite growth in human cells remain somewhat elusive. To address this deficiency, we screened a library of 414 IFNγ induced ISGs to identify factors that impact T. gondii infection in human cells. In addition to IRF1, which likely acts through the induction of numerous downstream genes, we identified RARRES3 as a single factor that restricts T. gondii infection by inducing premature egress of the parasite in multiple human cell lines. Overall, while we successfully identified a novel IFNγ induced factor restricting T. gondii infection, the limited number of ISGs capable of restricting T. gondii infection when individually expressed suggests that IFNγ-mediated immunity to T. gondii infection is a complex, multifactorial process.

## Introduction

Toxoplasma gondii infection is common in humans, and while typically self-limiting in immunocompetent individuals, it can be severe in congenital toxoplasmosis and in immunodeficient individuals (Furtado et al., 2011). Additionally, T. gondii is a leading cause of infectious retinochoroiditis (Weiss and Dubey, 2009). Eye disease is most prominent in Latin America and Africa with approximately one-third of uveitis cases being attributed to ocular toxoplasmosis (Furtado et al., 2013). Although mechanisms of immune control are well studied in the mouse, they are less well understood in humans with currently known mechanisms of restriction observed in a cell type-dependent manner (Fisch et al., 2019b).

In response to pathogen infection, host cells express and secrete interferons (IFNs), which signal in an autocrine or paracrine manner through IFN receptors to induce factors designed to block infection. Interferons fall into three categories: type I (including IFNα and IFNβ), type II (IFNγ), and type III (IFNλ1–4). In general, receptors for type I and type II IFN are ubiquitously expressed whereas type III IFN sensitivity is restricted to epithelial barriers. Conventionally, IFN signaling involves the induction of interferon-stimulated genes (ISGs) involved in host defense via JAK-STAT-mediated signaling (Alspach et al., 2019; Lazear et al., 2019; Schoggins, 2019). Although IFN upregulates the expression of many genes, induction of ISGs is only semi-conserved between cell types, with many ISGs being cell type dependent (Schoggins, 2019). Variability in ISG expression is perhaps due to the induction of noncanonical IFN signaling pathways that have been observed in a cell type-dependent manner (Van Boxel-Dezaire and Stark, 2007; van Boxel-Dezaire et al., 2006). To identify and study the functions of this diverse set of genes, a wide variety of approaches have been utilized including ectopic overexpression, siRNA-mediated knockdown, and more recently CRISPR-Cas9 screening approaches (Schoggins, 2019). For the purpose of our study, several previous overexpression screens have been informative: an ectopic expression-based screen of type II IFN induced genes developed by Abrams et al., 2020, and the prior screen developed by Schoggins et al., 2011, which focused on type I IFN induced genes. These screens utilized a lentiviral-based expression cassette to express a curated library of commonly expressed ISGs in a one gene per well format. Abrams et al., successfully used this approach to identify novel type II IFN induced genes that impact Listeria monocytogenes infection while the screen developed by Schoggins et al., has been used to identify many ISGs impacting a broad range of pathogens, including both bacteria and viruses (Abrams et al., 2020; Schoggins et al., 2011; Schoggins et al., 2014; Perelman et al., 2016). A similar ectopic expression-based screen utilized a large cDNA library to search for enhancers of STAT1-mediated transcription in T. gondii infected cells and successfully identified the orphan nuclear receptor TLX as an enhancer of STAT1-mediated transcription (Beiting et al., 2015).

Interferon gamma (IFNγ) has been known since the 1980s to be expressed during T. gondii infection and to be critical for restricting infection in mice (Suzuki et al., 1988; McCabe et al., 1984; Shirahata and Shimizu, 1980). IFNγ-mediated restriction has been attributed to the expression of a group of ISGs, including immunity-related GTPases (IRGs) and guanylate binding proteins (GBPs) (Gazzinelli et al., 2014; MacMicking, 2012). IRGs and GBPs are recruited to the parasitophorous vacuole membrane (PVM) resulting in a loss of membrane integrity and parasite death (Ling et al., 2006; Martens et al., 2005; Yamamoto et al., 2012). As a defense, type I and type II strains of T. gondii express the Ser/Thr kinase ROP18, which phosphorylates and inactivates IRG proteins to prevent PVM damage (Hunter and Sibley, 2012; Mukhopadhyay et al., 2020). Additionally, increased nitric oxide production due to induction of inducible nitric oxide synthase (iNOS) has also been shown to play a role in restricting T. gondii infection in mice in vivo and in vitro (Khan et al., 1997; Adams et al., 1990; Meisel et al., 2011).

IFNγ is similarly important for T. gondii restriction in human cells in vitro and IFNγ expression has been shown to correlate with disease severity in vivo (Pfefferkorn et al., 1986; Meira et al., 2014). In contrast to the situation in mouse, the reported mechanisms underlying IFNγ-mediated T. gondii restriction in humans tend to be cell-type specific. However, it is important to note here that many of the studies in mice have been conducted in primary cells whereas human studies have mostly relied on immortalized cell lines. This could also be an important factor in the differences between restriction mechanisms observed in mice and humans. Humans possess one truncated IRG that likely lacks GTPase activity and only one nontruncated IRG that is not IFNγ or infection inducible (Bekpen et al., 2005). Hence, it is unlikely IRGs play a role in human resistance to T. gondii infection. Although human GBP1 has been shown to restrict T. gondii infection, it does so in a cell type-dependent manner. GBP1 restricts infection in IFNγ-treated human mesenchymal stromal cells (MSCs) and lung epithelial cells (i.e., A549 cells) but not myeloid-derived cells (i.e., HAP1 cells) (Qin et al., 2017; Ohshima et al., 2014; Johnston et al., 2016). GBP1 is also implicated in an inflammasome pathway that results in host cell death in human macrophages following T. gondii infection (Fisch et al., 2019a). Additionally, GBP5 has been shown to play a role in the clearance of T. gondii from human macrophages in vitro, albeit in an IFNγ independent manner (Matta et al., 2018). Humans also possess an ISG15-dependent, IFNγ inducible, noncanonical autophagy (ATG) pathway that restricts T. gondii growth in human cervical adenocarcinoma cells (HeLa cells) and A549 cells (Bhushan et al., 2020; Selleck et al., 2015). A similar noncanonical ATG dependent pathway has been reported in human umbilical vein epithelial cells (HUVECs), although it differs slightly in culminating in lysosome fusion (Clough et al., 2016). Finally, indoleamine 2,3-dioxygenase (IDO1) has been shown in vitro to restrict T. gondii growth by limiting L-tryptophan availability in human fibroblasts and monocyte-derived macrophages as well as in human-derived cell lines of myeloid, foreskin, liver, or cervix origin (e.g., HAP1s, HFFs, Huh7s, and HeLas) but not in cells lines originating from mesenchymal stem cells, the large intestine, or the umbilical endothelium (e.g., MSCs, CaCO2s, or HUVECs) (Qin et al., 2017; Bando et al., 2018; Pfefferkorn, 1984; Woodman et al., 1991; Dimier and Bout, 1997; Schmitz et al., 1989).

Collectively, the previous studies examining IFNγ-mediated growth restriction in human cells support a model where different mechanisms make variable contributions in distinct lineages. However, the known pathways for restriction only cover a small fraction of the genes that are normally upregulated in different human cell types following treatment with IFNγ (Schoggins, 2019; Rusinova et al., 2013). Hence, there may be additional control mechanisms not yet defined, including either those that are lineage-specific or that operate globally in all cell types. To explore this hypothesis, we screened a library of 414 IFNγ induced ISGs in a one gene per well format to attempt to identify novel human factors with the ability to restrict T. gondii infection.

## Results

To identify novel ISGs that impact T. gondii infection, we employed a library of 414 IFNγ induced ISGs cloned into a lentiviral expression cassette co-expressing tagRFP, as previously described by Abrams et al., 2020. To screen for ISGs that restrict T. gondii infection, we developed a high-throughput method to quantitatively measure infection of GFP-expressing type III strain CTG parasites using automated microscopy. CTG is a type III strain of T. gondii that is avirulent in mice and more susceptible to IFNγ-mediated restriction than other strains thus making it ideal for identifying individual ISGs which can restrict infection (Khaminets et al., 2010; Boothroyd and Grigg, 2002; Saeij et al., 2006). A549 lung epithelial cells were infected with CTG-GFP and the size of individual parasitophorous vacuoles (PVs), the number of vacuoles per field, and the percentage of vacuoles with a size consistent with containing ≥8 parasites were determined after 36 hr of culture (Figure 1A–C). A549 cells were used as they are highly permissive to transduction with our VSV-G pseudotyped lentivirus and readily infected by T. gondii. Cells were transduced with lentivirus in a one gene per well format and challenged with CTG-GFP (Figure 1D). Transduction efficiency was high for most ISGs with 86% (357/414) of ISGs expressed in at least 50% of the cell population and 50% of ISGs (205/414) expressed in 90% of the cell population (Supplementary file 1). Using this approach, we found three ISGs that restricted infection: IRF1, TRIM31, and RARRES3 (Figure 1E, Supplementary file 1). All hits were identified as significant by a two-way ANOVA (p<0.0001). Interestingly, six ISGs significantly promoted parasite growth, including IL7R, IFITM1, MX1, DHX58, RNF19B, and CNDP2. For the purposes of this study, we were interested in investigating ISGs that restricted infection and did not further validate or study any ISGs that promoted parasite growth. We found it curious that IDO1 was not identified by this screen considering its significant impact on infection observed in some but not all cell lines (Qin et al., 2017; Bando et al., 2018; Pfefferkorn, 1984; Woodman et al., 1991; Dimier and Bout, 1997; Schmitz et al., 1989). There have been no previous reports as to the role of IDO1 during infection in A549s and as such we generated an IDO1 deficient A549 cell line and challenged with CTG-GFP in the presence of IFNγ. Consistent with the results of our screen, IDO1 deficiency did not impair IFNγ-mediated restriction of CTG-GFP (Figure 1F). It is worth noting here that the concentration of tryptophan used in the media for these experiments (16 µg/ml) was higher than what has been used previously to observe IDO1-mediated infection restriction, which may prevent IDO1-mediated depletion of tryptophan (Pfefferkorn, 1984). However, in the present study, a much higher dose of IFNγ was also used to induce strong ISG expression and this might be expected to overcome increased tryptophan levels. Collectively, our results suggest that IDO1 does not play a major role in the restriction of T. gondii in A549 cells under the experimental conditions used in this study.

![Figure 1.](https://cdn.elifesciences.org/articles/73137/elife-73137-fig1-v2.jpg)

**Figure 1.:** A549 cells were treated with indicated concentrations of IFNγ for 24 hr and subsequently infected with the type III strain CTG expressing GFP (CTG-GFP) for 36 hr. (A–C) Cells were fixed, stained with anti-GFP and anti-RFP antibodies, and imaged using a Cytation3 Imager. (A–C) Average parasitophorous vacuole (PV) size (A), PVs per field (B), and the percentage of vacuoles containing ≥8 parasites (C) was quantitated for data from 36 hr image sets. (D) Illustration of the method used to conduct the screen presented in (E). (E) A549 cells were transduced with a lentiviral expression cassette co-transcriptionally expressing tagRFP and an ISG of interest in a one gene per well format. After 72 hr, cells were infected with CTG-GFP for 36 hr, fixed, stained with anti-GFP and anti-RFP antibodies, and imaged with a Cytation3 Imager. Statistical significance was determined using a two-way ANOVA with Tukey’s test for post hoc analysis. ISGs enhancing or restricting infection >20% relative to control with p<0.0001 were classified as hits. Hits are shown in red and labeled. (F) WT and IDO1−/− A549 cells were infected with CTG-GFP for 96 hr. Cells were fixed, stained with anti-SAG1 antibody, and imaged with a Cytation3 Imager. Average total infected area per well is shown. Loss of IDO1 in IDO1−/− A549 cells was confirmed via western blot. Briefly, cells were treated with or without 1000 U/ml IFNγ for 24 hr before samples were harvested and IDO1 expression was determined. (A–C, F) Data represent the  deviation of three biological replicates conducted in technical triplicate. (E) Data represent  deviation of two biological replicates conducted in technical duplicate. Statistical significance was determined using two-way ANOVA with Tukey’s test for post hoc analysis. ns, not significant; p>0.05, **p<0.01, ****p<0.0001.

### Validation of screen hits

Cells ectopically expressing IRF1, TRIM31, and RARRES3 expanded normally and showed similar viability compared to a luciferase control when stained with the live-dead stain SYTOX green, suggesting that the overexpression of these genes is not cytotoxic (Figure 2A–B). To confirm that these genes restrict T. gondii infection, we ectopically expressed these genes in A549 cells and challenged with CTG-GFP for 36 or 96 hr. RARRES3 and IRF1 ectopic expression resulted in a reduction in average vacuole size at 36 hr (Figure 2C–D). At 96 hr, the total area infected per well was significantly lower for RARRES3 and IRF1 expressing cells compared to control as was the average size of infection foci (Figure 2E–F). TRIM31 had no significant effect on infection in validation experiments and it was not studied further. IRF1 has a known role in amplifying IFNγ-mediated transcription, and its role relative to IFNγ is further explored below. RARRES3 is a small, 18.2 kDa single domain protein in the HRASLS subfamily (Mardian et al., 2015). RARRES33 has been shown to inhibit immunoproteasome expression in cancer cells (Anderson et al., 2017). It displays phospholipase A1/2 activity in vitro and has been shown to suppress Ras signaling and promote apoptosis (Uyama et al., 2009; Tsai et al., 2007; Han et al., 2010). Although RARRES3 was described by a previous screen to be antiviral (Schoggins et al., 2014), it was not studied further and little is known about its involvement in immunity to other pathogens. In studies described below, we explore its role in restricting the growth of intracellular T.gondii.

![Figure 2.](https://cdn.elifesciences.org/articles/73137/elife-73137-fig2-v2.jpg)

**Figure 2.:** (A, B) Wild-type (WT) A549 cells were either not transduced (NT) or transduced with TRIP.RARRES3 or TRIP.FLUC control and split 48 hr later. After 60 hr, cells were stained with Hoechst 33342, SYTOX green, and imaged with a Cytation3 Imager. As a positive control, cells were permeabilized by treatment with methanol (MeOH) for 5 min prior to staining. Average cell number (A) and the percentage of SYTOX staining cells (B) were determined. (C–F) WT A549 cells were transduced with TRIP.RARRES3 or TRIP.FLUC control and infected 72 hr later with CTG-GFP for 36 (C, D) or 96 (E, F) hr. Cells were fixed, stained with anti-GFP and anti-RFP antibodies, and imaged using a Cytation3 Imager. Average PV number per field (C) and PV size (D) were quantitated for 36 hr infections while total area infected per sample (E) and average foci size (F) were quantitated for 96 hr infections. Data in (A) represent four to seven biological replicates conducted in technical triplicate. Data in (B) represent two to four biological replicates conducted in technical triplicate. Data in (C–F) represent three to four biological replicates conducted in technical triplicate. Statistical significance was determined using a Brown-Forsythe and Welch ANOVA (A, B) or a two-way ANOVA with Tukey’s test for post hoc analysis (C–F). *p≤0.05, **p<0.01.

### IRF1 versus IFNγ induced genes

In mice, Irf1 deficiency has been shown to result in increased susceptibility to T. gondii infection (Khan et al., 1996), consistent with the secondary induction of a broad set of ISGs downstream of IFN dependent STAT-mediated gene expression (Feng et al., 2021). However, it is unknown what subset of IFNγ-induced genes are regulated by IRF1 in A549 cells. To define these two gene sets, we ectopically expressed IRF1 or luciferase control in A549 cells, treated a subset of control cells with IFNγ, and analyzed transcriptional changes by RNA-seq. For both IFNγ and IRF1, the majority of changes were due to upregulation, and we focused our analysis on these genes (Figure 3A and B). We identified 160 genes upregulated by IRF1 and 380 genes upregulated by IFNγ in A549 cells (FDR≤0.05, twofold) (Supplementary file 2). When we compared these gene lists with the ISG library with which we challenged T. gondii infection, we found that 41.1% (86/160) of IFNγ induced genes and 53.8% (156/380) of IRF1 induced genes were represented by the library (Supplementary file 3). Notably, strongly induced ISGs were more commonly represented in the ISG library with 69% of the top 100 strongest induced genes by IFNγ and 67% of those induced by IRF1 being represented (Figure 3C, Supplementary file 3). Gene ontology (GO) analysis for the lists of IRF1 and IFNγ induced genes revealed induction of very similar processes that were grouped into IFN signaling, immune response regulation, host defense, and antigen presentation (Figure 3D–E). Interestingly, RARRES3 was strongly induced by both IRF1 and IFNγ treatment. This is consistent with the previously reported finding that IRF1 expression strongly induces RARRES3 expression in human hepatoma and skin fibroblast derived cell lines (Schoggins et al., 2011).

![Figure 3.](https://cdn.elifesciences.org/articles/73137/elife-73137-fig3-v2.jpg)

**Figure 3.:** Cells were transduced with TRIP.IRF1 or TRIP.FLUC control lentivirus. Cells transduced with FLUC were further treated 72 hr later with or without 1000 U/ml IFNγ for 24 hr. All cell populations were subsequently harvested and analyzed by RNA-Seq. (A, B) Changes in gene expression relative to FLUC control expressing cells for cells treated with IFNγ (A) or ectopically expressing IRF1 (B). Genes upregulated in both IRF1 expressing and IFNγ treated cells are defined as ‘Shared’ while genes only upregulated in one of these two cell populations are defined as ‘Unique.’ (C) Comparison of genes induced ≥2-fold with a false discovery rate cutoff of 0.05 by each condition and their overlap with the ISG library used in the screen described in Figure 1. (D–E) Lists of induced genes were analyzed with PANTHER gene ontology analysis. The top 10 most enriched processes amongst genes induced by IFNγ (D) and IRF1 (E) are shown. Redundant terms were excluded from these lists with only the most enriched version of each term remaining.

### RARRES3 does not affect immune signaling

To determine if the observed reduction in infection with RARRES3 overexpression might also be due to induction of interferon expression and downstream ISG induction, we used CRISPR/Cas9-mediated gene editing to generate a STAT1−/− A549 cell line (Figure 4A–B). We ectopically expressed RARRES3 in these cells and subsequently infected with CTG-GFP parasites. The same phenotypes were observed with RARRES3 ectopic expression irrespective of the presence of STAT1, suggesting that decreased infection on overexpression of RARRES3 is not due to induction of IFNγ signaling (Figure 4C–F). Interestingly, we noticed that RARRES3 ectopic expression resulted in a modest increase in the number of PVs observed at 36 hr in WT cells and was slightly more pronounced in STAT1−/− cells (Figures 2C and 4C). We further tested if ectopic expression of RARRES3 impacted NF-κB or interferon signaling by using κB-, ISRE-, and GAS-luciferase reporter cell lines. RARRES3 did not significantly impact luciferase expression for any of the reporters tested (Figure 4G–J). These findings suggest that RARRES3 does not modulate immune signaling pathways and instead plays a direct role in restricting infection.

![Figure 4.](https://cdn.elifesciences.org/articles/73137/elife-73137-fig4-v2.jpg)

**Figure 4.:** To determine if restriction of T. gondii growth was STAT1 dependent, STAT1−/− A549 cells were generated. To confirm complete insensitivity to interferon treatment, WT or STAT1−/− A549 cells were treated with or without 4000 U/ml IFNγ for 6 hr, fixed, stained with anti-IRF1 antibodies, and imaged with a Cytation3 Imager. (A) Representative images and (B) quantitation are shown. Scale bar=50 µm. (C–F) STAT1−/− A549 cells were transduced with TRIP.RARRES3 or TRIP.FLUC control and infected 72 hr later with CTG-GFP for 36 (C, D) or 96 (E, F) hr. Cells were fixed, stained with anti-GFP and anti-RFP antibodies, and imaged using a Cytation3 Imager. Average PV number per field (C) and PV size (D) were quantitated for 36 hr infections while total area infected per sample (E) and average foci size (F) were quantitated for 96 hr infections. HeLa reporter cell lines expressing GAS-LUC (G), kB-LUC (H), ISRE-GLUC (I), and GFP-LUC (J) were either not transduced (NT) or transduced with TRIP.RARRES3, TRIP.FLUC, or TRIP.GFP. After 72 hr, cells were mock treated or treated with 100 U/ml IFNβ or IFNγ as indicated and infected with CTG-GFP for 36 hr. Cells were harvested for luciferase assay. Data in (B) represent means ± SD of four biological replicates conducted in technical duplicate. Data in (C–F) represent means ± standard deviation of four biological replicates conducted in technical triplicate. Data represent means ± SD of two (G) or three (H–I) biological replicates conducted in technical duplicate. Statistical significance was determined using two-way ANOVA with Tukey’s test for post hoc analysis except for (D) where Mann-Whitney’s U-test was used. *p≤0.05, **p<0.01, ***p<0.001, ****p<0.0001.

### Catalytic activity is required for infection restriction and endogenous RARRES3 can restrict infection

As previously stated, RARRES3 displays phospholipase A1/2 activity in vitro and belongs to the H-RAS suppressor-like (HRASLA) subfamily (Uyama et al., 2009). Phospholipase and acyltransferase activities of HRASLS subfamily enzymes involve the temporary acylation of an active site cysteine residue (Mardian et al., 2015). To determine if the catalytic activity of RARRES3 was required for restriction of infection, we generated two active site point mutants (C113A, C113S) of RARRES3. Cells ectopically expressing mutant or WT RARRES3 were subsequently challenged with CTG-GFP. Although WT RARRES3 restricted infection, neither mutant was able to do so (Figure 5A). Notably, RARRES3 C113A ectopic expression slightly promoted infection. Analysis of protein expression by western blot indicated that both mutants were strongly expressed compared to WT (Figure 5B). These data suggest that the enzymatic activity of RARRES3 is necessary for restriction of infection. To determine if endogenously expressed RARRES3 impacts infection, we next used CRISPR/Cas9-mediated gene editing to generate a RARRES3−/− A549 cell line. Alternatively, cells were transduced with an expression cassette containing Cas9 and a previously used nontargeting sgRNA to serve as a negative control (Doench et al., 2016). RARRES3 deficiency did not alter the susceptibility of quiescent cells to infection (Figure 5C–D). However, RARRES3 deficiency partially alleviated IFNγ-mediated restriction of CTG-GFP infection and this deficiency was complemented with RARRES3 ectopic expression (Figure 5C–D). As previously mentioned, RNA-seq analysis showed that RARRES3 expression was strongly induced by both IRF1 and IFNγ. Since RARRES3 was the only ISG identified by our screen to restrict T. gondii infection, we wanted to determine if the impact of IRF1 on infection was solely due to upregulation of RARRES3 expression. To test this, we ectopically expressed IRF1 or luciferase control in WT and RARRES3−/− A549 cells and challenged them with CTG-GFP. However, loss of RARRES3 did not impact IRF1-mediated restriction of infection (Figure 5E). This suggests that either IRF1-mediated infection restriction is RARRES3 independent or involves multiple factors with RARRES3 playing a redundant role in the process of restricting growth. As previously mentioned, CTG is a type III strain of T. gondii that is less virulent in mice and more susceptible to IFNγ-mediated restriction than other strains (Khaminets et al., 2010; Boothroyd and Grigg, 2002; Saeij et al., 2006). We wanted to determine if RARRES3 also impacts other strains of T. gondii. To test this, we infected A549s ectopically expressing RARRES3 with GFP expressing RH88 (type I) and Me49 (type II). However, RARRES3 had no impact on the infection of either of these two strains (Figure 5—figure supplement 1). Differential expression or polymorphic virulence factors may explain the disparity in susceptibility to RARRES3-mediated restriction between strains (Saeij et al., 2006; Rosowski et al., 2011).

![Figure 5.](https://cdn.elifesciences.org/articles/73137/elife-73137-fig5-v2.jpg)

**Figure 5.:** (A, B) A549s were transduced with V5 tagged WT RARRES3 or the catalytically inactive mutants C113A or C133S for 72 hr. (A) Cells were infected with CTG-GFP for 96 hr. Cells were harvested, stained with anti-GFP and anti-RFP antibodies, and imaged with a Cytation3 Imager. The total area infected per sample is shown. (B) Western blot from lysates prepared with above RARRES3 expressing cells. Membranes were probed with mouse anti-actin and mouse anti-V5 antibodies overnight followed by goat anti-mouse 680RD and imaged with a LI-COR Odyssey scanner. RARRES3−/− A549s or wild-type cells transduced with a nontargeting CRISPR/Cas9 sgRNA were transduced with Cas9 resistant TRIP.RARRES3 or TRIP.FLUC as indicated. After 72 hr, cells were treated with or without 100 U/ml IFNγ for 24 hr as indicated and subsequently infected with CTG-GFP for 96 hr. Cells were harvested, stained with anti-GFP and anti-RFP antibodies, and imaged with a Cytation3 Imager. (C) Representative images and (D) quantitation are shown. Scale bar=500 µm. (E) RARRES3−/− or RARRES3+/+ A549 cells transduced with a nontargeting CRISPR/Cas9 control sgRNA were transduced with TRIP.FLUC or TRIP.IRF1 derived lentivirus. After 72 hr, cells were infected with CTG-GFP for 96 hr, harvested, stained with anti-GFP and anti-RFP antibodies, and imaged with a Cytation3 Imager. Average total infected area per well is shown. Data represent means ± standard deviation of three (A) or four (D, E) biological replicates conducted in technical triplicate. Statistical significance was determined using two-way ANOVA with Tukey’s test for post hoc analysis. ns, not significant; *p>0.05, **p<0.01, ****p<0.0001.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/73137/elife-73137-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** A549 cells were transduced with TRIP.RARRES3 and infected 72 hr later with a type I strain expressing GFP (RH88-GFP) (A, B) or a type II strain expressing GFP (Me49-GFP) (C, D) for 4 or 6 days, respectively. Cells were fixed, stained with anti-GFP and anti-RFP antibodies, and imaged using a Cytation3 Imager. Average total infected area per well (A, C) and average area of infection foci (B, D) are shown. Data represent means ± standard deviation of two to three biological replicates conducted in technical triplicate. Statistical significance was determined using two-way ANOVA with Tukey’s test for post hoc analysis.

### RARRES3 promotes premature egress

We subsequently revisited our previous finding that infection in RARRES3 ectopically expressing cells results in more, smaller PVs at 36 hr than control. This result suggested to us that RARRES3 might be promoting premature egress of the parasite. To test this possibility, we infected A549 cells ectopically expressing RARRES3 with CTG-GFP parasites and measured lactate dehydrogenase (LDH) release (Figure 6A). RARRES3 ectopic expression resulted in increased LDH release in CTG-infected cells compared to control cells (Figure 6A). We next sought to differentiate if the observed LDH release was due to protein kinase G (PKG) dependent, active parasite egress, or a form of induced cell death. To differentiate between these two hypotheses, we treated cells during infection with a trisubstituted pyrrole T. gondii protein kinase G inhibitor known as Compound 1 (Gurnett et al., 2002; Donald et al., 2006). Compound 1 is a potent inhibitor of parasite egress and has also been shown to promote differentiation from tachyzoites to bradyzoites, significantly slowing parasite growth thus also delaying or preventing egress (Nare et al., 2002; Lourido et al., 2012; Radke et al., 2006). Treatment with Compound 1 blocked the LDH release observed during infection and compound 1 treated cells did not stain with propidium iodide, suggesting that host cell death as measured by LDH release was due to parasite egress (Figure 6B, Figure 6—figure supplement 1A). To further confirm that RARRES3 induces premature egress, we directly measured the kinetics of CTG-GFP egress from RARRES3 or FLUC control expressing cells via time-lapse imaging of live cells by video microscopy. Parasites egressed significantly sooner in RARRES3 expressing cells compared to control (two-way ANOVA, p<0.0001), further confirming that RARRES3 induces premature parasite egress (Figure 6C, Videos 1–2).

![Figure 6.](https://cdn.elifesciences.org/articles/73137/elife-73137-fig6-v2.jpg)

**Figure 6.:** A549 cells were transduced with TRIP.RARRES3 or TRIP.FLUC control and infected 72 hr later with CTG-GFP for 36 (A, B, D, F), 50 (C), or 72 (E) hr. Cells were treated with the cell death inhibitors Z-VAD-FMK (50 µM), GSK’963 (1 µM), GSK’872 (5 µM), NSA (10 µM), and Z-YVAD-FMK (10 µM) or the parasite egress inhibitor compound 1 (5 µM) as indicated during infection. (A, B, E, F) Cell supernatant was collected after infection and lactate dehydrogenase (LDH) activity was determined to measure cell lysis. As a control to measure maximal LDH release, cells were lysed before supernatant collection. (C) Live infection was imaged every 15 min starting 2 hr postinfection until 50 hr postinfection. Time of parasite egress was recorded for at least 100 PVs per condition per replicate. Percentage of total parasites egressed by the end of each hour is indicated. (D) Cells were fixed, stained with anti-RFP and anti-GFP antibodies, and imaged with a Cytation3 Imager. Average cells per field are shown. Data represent the means ± standard deviation (A, B, D–F) or standard error of the mean (C) of three to five biological replicates conducted in technical duplicate (A, B, D–F), or singlet (C). Statistical significance was determined using two-way ANOVA with Tukey’s test for post hoc analysis. ns, not significant; P>0.05, *p≤0.05, ***p<0.001, ****p<0.0001.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/73137/elife-73137-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A–C) A549 cells were transduced with TRIP.RARRES3 or TRIP.FLUC control and infected 72 hr later with CTG-GFP for 36 hr (A) or 72 hr (B, C). Cells were stained with Hoechst 33342, propidium iodide, and imaged with a Cytation3 imager. As a positive control, cells were permeabilized by treatment with methanol (MeOH) for 5 min prior to staining. The percentage of propidium iodide staining cells (A, B) and average cell number per field (C) were determined. (D–F) HFF cells were pretreated with or without IFNγ for 24 hr and subsequently infected with CTG-GFP for 36 hr. Cells were stained with Hoechst 33342, propidium iodide, and imaged with a Cytation3 imager. As a positive control, cells were permeabilized by treatment with methanol (MeOH) for 5 min prior to staining. (D) Representative images are shown. Scale bar=50 µm. Average cell number (E) and the percentage of propidium iodide staining cells (F) were determined. Data represent means ± standard deviation of two or three biological replicates conducted in technical duplicate. Statistical significance was determined using two-way ANOVA with Tukey’s test for post hoc analysis. ***p<0.001, ****p<0.0001.

![Video 1.](https://cdn.elifesciences.org/articles/73137/elife-73137-video1.mp4.jpg)

**Video 1.:** A549 cells were transduced with TRIP.FLUC control and infected 72 hr later with CTG-GFP. Live infection was imaged every 15 min starting 12 hr postinfection until 50 hr postinfection.

![Video 2.](https://cdn.elifesciences.org/articles/73137/elife-73137-video2.mp4.jpg)

**Video 2.:** A549 cells were transduced with TRIP.RARRES3 and infected 72 hr later with CTG-GFP. Live infection was imaged every 15 min starting 12 hr postinfection until 50 hr postinfection.

In addition to increased parasite egress, we observed a reduction in host cell number during infection in cells ectopically expressing RARRES3 compared to control at 36 hr postinfection (Figure 6D). Similar to above, this phenotype was blocked by Compound 1 addition. A common trigger of premature egress is the induction of cell death pathways, of which there is a diversity of types controlled by different mechanisms (Yao et al., 2017; Persson et al., 2007; Niedelman et al., 2013; Rosenberg and Sibley, 2021). If induction of host cell death is the trigger for premature egress, we would expect to observe host cell death even when parasite egress is blocked. Hence, we were curious if extending this timepoint further would reveal host cell death even with blockage of parasite egress by Compound 1. However, Compound 1 addition during infection resulted in no significant increase in LDH release or propidium iodide staining even 72 hr after infection (Figure 6E, Figure 6—figure supplement 1B). Meanwhile, in untreated, infected cultures, the cell monolayer was nearly completely lysed and LDH activity was elevated in the supernatant (Figure 6E, Figure 6—figure supplement 1C). Further, we did not observe signs of death such as cell rounding, blebbing, or loss of nuclear integrity prior to parasite egress during live imaging (Videos 1–2). Collectively, these findings suggest that induction of cell death by RARRES3 is not the trigger for promotion of parasite egress. To further test this idea, we treated cells with a panel of established inhibitors of known cell death pathways during infection either individually or in combination as indicated (Figure 6F). These inhibitors included the pan-caspase inhibitor Z-VAD-FMK, which blocks apoptosis; the necroptosis inhibitors GSK’963, GSK’872, and necrosulfonamide (NSA), which block RIP1, RIP3, and MLKL activity, respectively; and the pyroptosis inhibitor Z-YVAD-FMK, which blocks caspase 1. No single drug or combination thereof was capable of inhibiting LDH release during infection except for GSK’872, which partially prevented LDH release in both RARRES3 ectopically expressing and control cells. Overall, we conclude from these experiments that it is unlikely that overexpression of RARRES3 induces cell death and therefore it must trigger premature egress by some other means.

A similar premature egress phenotype to that observed here has previously been identified in HFF cells (Niedelman et al., 2013). We hypothesized that RARRES3 might play a role in this process. To test this possibility, we ectopically expressed RARRES3 in HFF cells and infected with CTG-GFP parasites. RARRES3 ectopic expression was found to restrict CTG infection (Figure 7A–B). We next ablated RARRES3 expression in HFFs using CRISPR/Cas9-mediated gene editing. Loss of RARRES3 resulted in a partial reduction in IFNγ-dependent cell death in RARRES3−/− HFF cells compared to control cells expressing Cas9 and a nontargeting sgRNA (Figure 7C). This finding indicates that RARRES3 plays a role in premature egress but is not the only factor involved in HFF cells. In line with this finding, RARRES3 deficiency in HFF cells partially abrogated IFNγ-mediated restriction of CTG-GFP infection (Figure 7D). Moreover, treatment with Compound 1 completely blocked cell death during infection, suggesting that cell death is caused by PKG-dependent parasite egress (Figure 7E, Figure 6—figure supplement 1D-F). Collectively, this data suggests that RARRES3 overexpression promotes premature parasite egress independently of host cell death pathways in multiple cell lines which presumably stunts parasite growth leading to reduced infection overall.

![Figure 7.](https://cdn.elifesciences.org/articles/73137/elife-73137-fig7-v2.jpg)

**Figure 7.:** (A, B) HFF cells were transduced with TRIP.RARRES3 or TRIP.FLUC control and infected 72 hr later with CTG-GFP for 96 hr. Cells were fixed, stained with anti-GFP and anti-RFP antibodies, and imaged using a Cytation3 Imager. Total infected area per well (A) and average number of infection foci (B) are shown. (C–D) WT HFFs expressing a nontargeting sgRNA control or RARRES3 deficient HFFs were pretreated with or without 1000 U/ml IFNγ for 24 hr. (C) Cells were infected with CTG-GFP for 36 hr. Supernatant was collected and lactate dehydrogenase (LDH) activity was determined. As a control to measure maximal LDH release, cells were lysed before supernatant collection. (D) Cells were infected with CTG-GFP for 96 hr. Samples were treated as in (A). Total infected area per sample is shown. (E) HFFs were infected with CTG-GFP for 36 hr in the presence or absence of 5 µM Compound 1. Supernatant was collected and LDH activity was determined. Data represent means ± standard deviation of three (A, B, D, E) or four (C) biological replicates conducted in technical duplicate (A, B, D, E) or singlet (C). Statistical significance was determined using two-way ANOVA with Tukey’s test for post hoc analysis. *p≤0.05, ***p<0.001, ****p<0.0001.

## Discussion

The major mechanisms of IFNγ-mediated immunity have been shown to be conserved in multiple cell types including embryonic fibroblasts, macrophages, and astrocytes suggesting high conservation of immune mechanisms against T. gondii in mice (Ling et al., 2006; Martens et al., 2005; Yamamoto et al., 2012; Khan et al., 1997; Adams et al., 1990; Meisel et al., 2011). However, the currently known restriction mechanisms in humans show dramatic differences between cell types with no common or widespread restriction mechanism being observed. On the other hand, of the hundreds of ISGs, the vast majority have never been studied in relation to T. gondii, leaving open the possibility of unidentified restriction mechanisms. Herein, we performed a screen of IFNγ induced ISGs to identify novel mechanisms of IFNγ-mediated immunity in humans. Our screen identified RARRES3 and IRF1 as ISGs restrictive to T. gondii infection in human cells. Further study revealed that RARRES3 induced premature egress of T. gondii from host cells in a cell death independent manner. Not unexpectedly, IRF1 induced genes were largely found to be a subset of those induced by IFNγ, including RARRES3. These findings suggest that IRF1 works by the collective action of multiple ISGs. The relative lack of individual ISGs that are active alone also suggests that control mechanisms effective against T. gondii rely on complexes of multiple ISGs or cellular proteins working in concert. Hence, the control of intracellular eukaryotic pathogens contrasts with that of viral pathogens, mirroring differences in their overall biological complexity.

We identified RARRES3 as an ISG promoting premature egress of type III strains of T. gondii in two different human cell lines. This phenotype occurs independently of triggering downstream immune signaling. A common cause of premature egress is the induction of host cell death pathways (Yao et al., 2017; Persson et al., 2007; Niedelman et al., 2013). And indeed, such a mechanism might be suggested due to the fact that RARRES3 ectopic expression has been previously shown to induce apoptosis (Tsai et al., 2007). However, in our system RARRES3 ectopic expression was not found to impact cell death. Additionally, basal levels of LDH release were not increased in cells ectopically expressing RARRES3. Finally, when we blocked cell death pathways individually or in tandem, we did not see a reduction in LDH. The one exception to this pattern was the reduced release of LDH following treatment with GSK’872. We suspect this result is due to RIP3 inhibition mediated induction of apoptosis as has been demonstrated previously with GSK’872 treatment (Tenev et al., 2011). Thus, following treatment with GSK’872 it is likely that infection is hindered by host cell apoptosis and LDH release is not observed since cell membranes remain largely intact. The early egress phenotype observed here was similar to an IFNγ-dependent premature parasite egress observed in HFF cells that was independent of known cell death pathways (Niedelman et al., 2013). We found that ablation of RARRES3 expression partially prevented the IFNγ and infection-dependent cell death phenotype in HFF cells. Furthermore, we observed that LDH release was blocked via Compound 1 mediated inhibition of PKG suggesting that RARRES3 overexpression leads to parasite egress resulting in host cell lysis. Although previous studies using CDPK3 inhibition concluded that blocking egress was not sufficient to prevent cell death, our findings differ from this conclusion, possibly due to the stronger role for PKG in controlling egress (Lourido et al., 2012). It is presently unclear how RARRES3 leads to premature egress, although it is possible that its phospholipase A1/A2 activity may alter cellular lipid pools that could induce premature egress consistent with the requirement for catalytic residues. As an example of the sensitivity of egress to membrane lipid constituents, increases in phosphatidic acid (Bisio et al., 2019), or the activity of lipolytic lecithin: cholesterol acyltransferase Pszenny et al., 2016 have been shown to trigger egress of T. gondii.

Although our studies define a role for RARRES3 in promoting early egress in vitro, they do not address how this outcome impacts parasite infection in vivo. Premature egress prevents further parasite growth and would reduce the maximum number of parasites reduce per round of infection while also incurring additional energy costs of reinvasion. Further, it removes the parasite from its protected intracellular niche, resulting in exposure to the extracellular environment and potential recognition by the immune system. Finally, host cell death that accompanies premature egress is a proinflammatory event that would presumably lead to a heightened immune response (Rock and Kono, 2008). For these reasons, we expect that the early egress induced by RARRES3 would be protective against T. gondii infection in vivo. However, it is possible that rapid egress could result in faster spread to neighboring cells. It is also worth noting premature expulsion by phagocytic cells has been suggested to promote the dissemination of T. gondii and other pathogens such as Cryptococcus neoformans (Seoane and May, 2020; Drewry and Sibley, 2019). Further studies using in vivo models of infection are needed to clarify the role of RARRES3 in control of infection.

In addition to RARRES3, we found that ectopic expression of IRF1 was sufficient to restrict T. gondii infection. It was not surprising to us that we identified IRF1 in this screen considering the well-known role of IRF1 in the secondary induction of ISGs and other protective factors downstream of IFN signaling (Feng et al., 2021). Mice deficient in Irf1 were previously shown to be more susceptible to T. gondii infection (Khan et al., 1996). However, considering the limited number of ISGs found to restrict T. gondii infection in our screen, we were curious as to what genes or pathways were being induced by IRF1 ectopic expression and how this compared to IFNγ-mediated gene expression in A549s. Although few genes were substantially downregulated by IRF1 expression, 160 genes were upregulated ≥2-fold by IRF1 compared to 380 genes with IFNγ treatment. IRF1 induced genes were largely a subset of those IFNγ inducible genes. Notably, this is not always the case with a significant disparity in genes being induced by IRF1 compared to IFNs being reported previously in BEAS-2B cells (Panda et al., 2019). Overall, similar processes were induced by both IRF1 and IFNγ and these were related to antigen processing and presentation, host defense, and immune signaling. We observed that IRF1 and IFNγ both strongly induced the expression of RARRES3 which led us to question if infection restriction by IRF1 was due to the induction of RARRES3 expression. However, we found that this was not the case, suggesting that RARRES3 either does not play a role in IRF1-mediated restriction of T. gondii infection or plays a redundant role. Hence, it is likely that IRF1 leads to overexpression of multiple ISGs that collectively inhibit parasite growth.

Although our study is the first to broadly screen ISGs for anti-protozoal activity, it is curious that we only identified two genes that were inhibitory to T. gondii infection. In contrast, similar screens challenging viruses and bacteria have commonly identified a minimum of 2–3 times this number of gene products that were restrictive to infection (Abrams et al., 2020; Schoggins et al., 2011; Schoggins et al., 2014; Perelman et al., 2016; Dittmann et al., 2015; Kuroda et al., 2020; Kane et al., 2016; Liu et al., 2019). To our knowledge, a total of 30 viruses and two bacterial pathogens have been challenged in similar screens. It is possible that the above observation may not hold as more screens are performed on other pathogens especially intracellular bacteria or parasites. One possible explanation of this difference is that T. gondii separates itself from the host cytoplasm via the host derived PVM that forms a barrier to otherwise harmful ISGs in the cytosol. Another explanation is that a common mechanism of ISG activity is the manipulation or shutdown of host processes required for pathogen infection. Examples include PKR-mediated and IFIT-mediated inhibition of host translation machinery, processes that directly affect viral infection (Schoggins, 2019). In contrast, T. gondii is a relatively autonomous intracellular pathogen with relatively limited need for host machinery for its growth and replication. Hence, the fact that so few genes were identified by this screen may reflect a secluded existence of T. gondii within the PVM and its autonomy of cellular processes relative to viral or bacterial pathogens.

Alternatively, the low number of single genes that restrict the growth of T. gondii in A549 cells suggests that IFNγ-dependent restriction is a complex process requiring the cooperation of multiple host factors at a time. Hence, the expression of single factors may not be sufficient to restrict infection. For example, a requirement for additional factors could explain why ISG15 was not identified by this screen as ISGylation also requires ubiquitin-like conjugation to attach to target proteins (Perng and Lenschow, 2018). ISG15 knockout was previously found to enhance T. gondii growth in A549 cells (Bhushan et al., 2020) and this was attributed to its role in the targeting of autophagy machinery to the PV during infection leading to restriction of parasite growth. Currently, over 200 genes have been found to be involved in autophagy in human cells according to the human autophagy database (HADb, http://autophagy.lu/clustering/index.html). Furthermore, coimmunoprecipitation experiments indicated that ISG15 interacts directly or indirectly with more than 240 proteins (Bhushan et al., 2020). Thus, although ISG15 may be necessary for autophagy-mediated infection restriction as observed with knockout-based studies, its individual ectopic expression may not be sufficient to induce this mechanism of infection restriction. A similar explanation can be made for GBP1 that was shown via knockout experiments to be important for restriction of T. gondii in A549 cells previously (Johnston et al., 2016). Gbp1 recruitment to the PV and parasite clearance in mice has been shown to require the autophagy machinery (Selleck et al., 2013) and the interaction of GBP1 with ATG5 has been reported in a human cell line (Bhushan et al., 2020). In human macrophages, the AIM2 inflammasome has been reported to induce host cell death in a GBP1 dependent manner (Fisch et al., 2019a). Thus, the expression of GBP1 individually may not be sufficient to restrict T. gondii infection. A similar argument is unlikely to explain the lack of a phenotype for IDO1, which is not thought to require any other genes for its function. However, this pathway does not seem to operate in all human cells (Qin et al., 2017; Woodman et al., 1991; Dimier and Bout, 1997). Our findings demonstrate that IDO1 does not impact infection in A549s at least under the conditions used in this study. Finally, it is also possible that ISGs important for T. gondii were missed by this screen as the library used herein is not an exhaustive list of all ISGs expressed in A549 cells. Hence, it is possible that other ISGs that restrict T. gondii infection could be identified using a more focused library or using a similar approach in a different human cell line.

Although we successfully identified a novel anti-parasitic ISG impacting T. gondii infection, the scarcity of ISGs identified with the screening approach used here is also of interest. Our results suggest that immunity to T. gondii is a complex process requiring multiple factors to impact infection. This complexity differs from other intracellular pathogens such as bacteria and viruses, where single ISGs are often sufficient to inhibit infection. As such, a future loss-of-function based screen for ISGs targeting T. gondii infection may reveal additional mechanisms of T. gondii restriction.

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
      <td>Cell line (Homo sapiens)</td>
      <td>A549</td>
      <td>ATCC</td>
      <td>CCL-185; RRID:CVCL_0023</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>293T</td>
      <td>ATCC</td>
      <td>CRL-3216; RRID:CVCL_0063</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>HFF</td>
      <td>ATCC</td>
      <td>SCRC-1041; RRID:CVCL_3285</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>HeLa</td>
      <td>ATCC</td>
      <td>CCL-2; RRID:CVCL_0030</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (H. sapiens)</td>
      <td>HeLa reporter cell line expressing ISRE-GLUC</td>
      <td>PMID:31413201</td>
      <td>11×-ISRE-Gaussia Luciferase reporter line</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (H. sapiens)</td>
      <td>HeLa reporter cell line expressing GAS-FLUC</td>
      <td>PMID:27091930</td>
      <td>HeLa reporter cell line expressing GAS-FLUC</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (H. sapiens)</td>
      <td>RARRES3−/− Lung adenocarcinoma (A549)</td>
      <td>This paper</td>
      <td></td>
      <td>See Materials and methods</td>
    </tr>
    <tr>
      <td>Genetic reagent (H. sapiens)</td>
      <td>IDO1−/− Lung adenocarcinoma (A549)</td>
      <td>This paper</td>
      <td></td>
      <td>See Materials and methods</td>
    </tr>
    <tr>
      <td>Strain, strain background (Toxoplasma gondii)</td>
      <td>RH88</td>
      <td>ATCC</td>
      <td>50853</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (T. gondii)</td>
      <td>Me49</td>
      <td>ATCC</td>
      <td>50611</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (T. gondii)</td>
      <td>CTG</td>
      <td>ATCC</td>
      <td>50842</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (T. gondii)</td>
      <td>RH88-GFP</td>
      <td>This paper</td>
      <td></td>
      <td>See Materials and methods</td>
    </tr>
    <tr>
      <td>Genetic reagent (T. gondii)</td>
      <td>Me49-GFP</td>
      <td>This paper</td>
      <td></td>
      <td>See Materials and methods</td>
    </tr>
    <tr>
      <td>Genetic reagent (T. gondii)</td>
      <td>CTG-GFP</td>
      <td>This paper</td>
      <td></td>
      <td>See Materials and methods</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-RFP (rabbit polyclonal)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#: R10367; RRID:AB_2315269</td>
      <td>(1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GFP (mouse monoclonal)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#: A-11120; RRID:AB_221568</td>
      <td>(1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse Alexa Fluor 488 (goat polyclonal)</td>
      <td>Life Technologies</td>
      <td>Cat#: A-11029; RRID:AB_138404</td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-rabbit Alexa Fluor 568 (goat polyclonal)</td>
      <td>Life Technologies</td>
      <td>Cat#: A-11011; RRID:AB_143157</td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-rabbit Alexa Fluor 488 (goat polyclonal)</td>
      <td>Invitrogen</td>
      <td>Cat#: A-11034; RRID:AB_2576217</td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-V5 (mouse monoclonal)</td>
      <td>Invitrogen</td>
      <td>Cat#: R960-25; AB_2556564</td>
      <td>(1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse 680RD (goat polyclonal)</td>
      <td>LI-COR Biotechnology</td>
      <td>Cat#: 926-68070; RRID:AB_10956588</td>
      <td>(1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-rabbit 800CW(goat polyclonal)</td>
      <td>LI-COR Biotechnology</td>
      <td>Cat#: 926-32211; RRID:AB_621843</td>
      <td>(1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-actin (mouse monoclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#: MAB1501; RRID:AB_2223041</td>
      <td>(1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IDO1 (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#: 86630S; RRID:AB_2636818</td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IRF1 D5E4 (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#: 8478S; RRID:AB_10949108</td>
      <td>(1:500)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Necrosulfonamide; NSA</td>
      <td>Tocris Biotechnology</td>
      <td>Cat#: 5025</td>
      <td>(10 µM)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>GSK’872</td>
      <td>Selleck Chemicals</td>
      <td>Cat#: S8465</td>
      <td>(5 µM)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Z-YVAD-FMK</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#: 218,746</td>
      <td>(10 µM)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Z-VAD-FMK</td>
      <td>R&amp;D Systems</td>
      <td>Cat#: fmk001</td>
      <td>(50 µM)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>GSK’963</td>
      <td>Selleck Chemicals</td>
      <td>Cat#: S8642</td>
      <td>(1 µM)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Compound 1</td>
      <td>MedChemExpress</td>
      <td>Cat#: HY-101525</td>
      <td>(5 µM)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hoechst stain; Hoechst 33342</td>
      <td>Invitrogen</td>
      <td>Cat#: H3570</td>
      <td>(1 µg/ml)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>SYTOX Green</td>
      <td>Invitrogen</td>
      <td>Cat#: S7020</td>
      <td>(5 µM)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>XtremeGene9 DNA Transfection Reagent</td>
      <td>Roche</td>
      <td>Cat#: XTG9-RO</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE NFkB-TA-LUC-UBC-GFP-W (plasmid)</td>
      <td>Addgene</td>
      <td>49,343</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>plentiCRISPRv2 (plasmid)</td>
      <td>Addgene</td>
      <td>52,961</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-Cas9-GFP (plasmid)</td>
      <td>Addgene</td>
      <td>86,145</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pTRIP.RARRES3 (plasmid)</td>
      <td>PMID:21478870</td>
      <td>pTRIP.CMV.IVSb.RARRES3.ires.TagRFP</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pTRIP.V5-RARRES3 WT (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>See Materials and methods</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pTRIP.V5-RARRES3 C113A (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>See Materials and methods</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pTRIP.V5-RARRES3 C113S (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>See Materials and methods</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pDONR221 (plasmid)</td>
      <td>Invitrogen</td>
      <td>Cat#: 12536017</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pTRIP.FLUC (plasmid)</td>
      <td>PMID:21478870</td>
      <td>pTRIP.CMV.IVSb.FLUC.ires.TagRFP</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pTRIP.IRF1 (plasmid)</td>
      <td>PMID:21478870</td>
      <td>pTRIP.CMV.IVSb.IRF1.ires.TagRFP</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pTRIP.GBP2 (plasmid)</td>
      <td>PMID:21478870</td>
      <td>pTRIP.CMV.IVSb.GBP2.ires.TagRFP</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pVSVg (plasmid)</td>
      <td>PMID:21478870</td>
      <td>Plasmid expressing the vesicular stomatitis virus glycoprotein (VSVg)</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pGag-pol (plasmid)</td>
      <td>PMID:21478870</td>
      <td>Plasmid expressing HIV gag-pol</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pGRA1.GFP.GRA2.DHFR (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>See Materials and methods</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>CyQuant LDH Cytotoxicity Assay Kit</td>
      <td>Invitrogen</td>
      <td>Cat#: C20300</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Luciferase cell culture lysis reagent (5×)</td>
      <td>Promega</td>
      <td>Cat#: E1531</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Luciferase Assay System</td>
      <td>Promega</td>
      <td>Cat#: E1500</td>
      <td>For firefly luciferase</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Pierce Gaussia Luciferase Glow Assay Kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#: 16160</td>
      <td>For Gaussia luciferase</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Q5 High Fidelity DNA Polymerase</td>
      <td>NEB</td>
      <td>Cat#: M0491</td>
      <td>Recombinant fragment and plasmid amplification</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>PrimeSTAR GXL DNA Polymerase</td>
      <td>Tocris Biotechnology</td>
      <td>Cat#: R050</td>
      <td>Genomic DNA amplification</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>BsmBI-v2</td>
      <td>NEB</td>
      <td>Cat#: R0739</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>BP Clonase II</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#: 11789-020</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>LR Clonase II</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat#: 11791-020</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CellProfiler</td>
      <td>BROAD Institute</td>
      <td>RRID:SCR_007358</td>
      <td>Version 3.1.9</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism</td>
      <td>GraphPad</td>
      <td>RRID:SCR_002798</td>
      <td>Version 3.1.2</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>National Institutes of Health</td>
      <td>RRID:SCR_003070</td>
      <td>Version 1.53f51</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ZEN Blue</td>
      <td>Zeiss</td>
      <td>RRID:SCR_013672</td>
      <td>Version 2.5</td>
    </tr>
  </tbody>
</table>

### Cell lines and parasites

HeLa adenocarcinoma, A549 lung carcinoma (ATCC #CCL-185), HFF foreskin fibroblast (ATCC #SCRC-1041), and human embryonic kidney-derived 293T cells (ATCC #CRL-3216) were grown in Dulbecco's modified Eagle’s medium (DMEM) supplemented with 10% fetal bovine serum (FBS), 10 mM HEPES (pH 7.5), 2 mM L-glutamine, and 10 µg/ml gentamicin. Cells were grown at 37°C with 5% CO2. T. gondii strains RH88 (type I), Me49 (type II), and CTG (type III) expressing GFP were generated via random insertion of pGRA1.GFP.GRA2.DHFR after electroporation as described previously (Shen et al., 2017). Clonal populations expressing GFP were generated via limiting dilution. T. gondii lines were passaged as described previously in HFFs grown under the conditions listed above (Khan and Grigg, 2017). Parasite and host cell lines were confirmed to be negative for mycoplasma using an e-Myco Plus Kit (Intron Biotechnology).

### Plasmids and cloning

The plasmids TRIP.RARRES3 and control constructs were kindly provided by Neal Alto and John Schoggins. Briefly, the TRIP plasmid encodes an expression cassette flanked by lentiviral LTRs. Expression of a bicistronic transcript including tagRFP and a gene of interest is driven by a CMV promoter. The gene of interest and tagRFP are translated independently via an internal ribosome entry site. Cas9 resistant RARRES3 was generated from the WT TRIP.RARRES3 construct by overlap extension PCR using Q5 high fidelity DNA polymerase (NEB). N-terminally V5 tagged WT, C113A, and C113S RARRES3 were generated from WT by overlap extension PCR. Fragments were cloned into pDONR221 using BP Clonase II (Thermo Fisher Scientific) and subsequently cloned into pTRIP using LR Clonase II (Thermo Fisher Scientific) according to the manufacturer’s protocol. For CRISPR/Cas9 experiments, RARRES3 and nontargeting guides were cloned into plentiCRISPRv2 (Addgene plasmid #52961) (Sanjana et al., 2014). Primers for the above cloning are listed in Supplementary file 4. For IDO1, an IDO1 targeting sgRNA was cloned into pLenti-Cas9-GFP (Addgene plasmid #86145). Briefly, pLenti-Cas9-GFP was digested with BsmBI (New England Biolabs). Primers listed in Supplementary file 4 were annealed and ligated into the digested plasmid using T4 ligase (New England Biolabs). For the generation of pGRA1.GFP.GRA2.DHFR, an expression cassette consisting of the GRA1 5′ UTR (M26007.1, nucleotides 4–615) driving the expression of GFP (MN114103.1, coding sequence) flanked by the GRA2 3′ UTR (XM_002366354.2, nucleotides 997–1114) was cloned into pHL931 along with DHFR (XM_002367211.2, coding sequence) expressed from its native promoter and flanked by its 3′ UTR (L08489.1).

### Lentivirus production and cell line generation

TRIP lentiviruses were produced as previously described (Schoggins et al., 2012). Lentiviruses derived from Lenti-Cas9-GFP, lentiCRISPRv2, and HAGE NFkB-TA-LUC-UBC-GFP-W (Wilson et al., 2013) were produced similarly. Briefly, 293T cells were seeded at 4×105 cells per well into six-well plates. Cells were transfected with 1 µg pTRIP, pLenti-Cas9-GFP, plentiCRISPRv2, or pHAGE NFkB-TA-LUC-UBC-GFP-W, 0.2 µg plasmid expressing VSVg, and 0.8 µg plasmid expressing HIV-1 gag-pol using X-tremeGENE 9 (Sigma-Aldrich). Media were changed 6 hr later and lentivirus containing culture supernatants were collected at 48 and 72 hr post-transfection. Pooled supernatants were clarified by centrifugation at 800×g for 5 min. Polybrene and HEPES were added to a final concentration of 4 µg/ml and 35 mM, respectively. Lentivirus was stored at –80°C until use.

For lentivirus transductions, cells were seeded at 7×104 cells per well in 24-well plates. The next day, media were changed to DMEM supplemented with 4 µg/ml polybrene, 3% FBS, 35 mM HEPES, 2 mM glutamine, and 10 µg/ml gentamicin. Cells were transduced by spinoculation at 800×g, 45 min, 37°C. For the ISG screen, media was changed 6 hr later to normal growth medium. Cells were replated at 48 hr post-transduction for subsequent experimentation.

For knockout cell line generation, cells were transduced with lentiCRISPRv2 or pLenti-Cas9-GFP containing the appropriate sgRNA for Cas9 targeting as above. For lentiCRISPRv2, cells were selected for at least 2 weeks in growth media containing 4 µg/ml puromycin before experimentation. For IDO1−/−, STAT1−/−, and RARRES3−/− A549 cell lines, cells were transduced with a single lentivirus and clonal cell lineages were established through limiting dilution. For HFFs, a heterogeneous bulk population RARRES3 knockout cell line was generated by transducing at a tissue culture infectious dose of 90% (TCID90) with two different lentiCRISPRv2 based lentiviruses expressing separate RARRES3 targeting sgRNAs. Nontargeting control cell lines were generated for use as a control in all experiments involving RARRES3−/− cells. Here, cells were transduced with a single lentiCRISPRv2 based lentivirus containing a single nontargeting guide. For RARRES3 and STAT1, editing was confirmed by PCR amplifying targeted loci using primers listed in Supplementary file 4 and PrimeSTAR GXL DNA polymerase (Tocris) followed by Sanger sequencing. Editing efficiency was quantitated using Synthego ICE analysis (https://ice.synthego.com/#/). For single-cell clones, >90% editing was verified. For HFF bulk population knockout of RARRES3, 68% editing of sequenced alleles was observed. For STAT1, editing was further confirmed functionally via testing the sensitivity of cells to IFN treatment as determined by IRF1 induction. For IDO1, editing was confirmed via loss of protein expression observed by western blot.

### Infections

A549 and HeLa cells were seeded at 1.5×104 in 96-well plates 24 hr prior to infection. HFFs were seeded at 2×104 in 96-well plates 24 hr prior to infection. Cells were infected with parasites diluted in 200 µl normal growth medium for 1 hr at 37°C. Medium was subsequently changed to 300 µl normal growth medium. For single life cycle infections (typically indicated as 36 hr infections), an MOI of 1 was used. For focus forming assays (typically indicated as 96 hr infections), an MOI of 0.03 was used. For LDH assays, media were changed to 200 µl normal growth medium. For experiments involving IFNγ, cells were pretreated with or without IFNγ diluted in normal growth medium as indicated for 24 hr prior to infection. For infections involving cell death inhibitors or Compound 1, drugs were added during the media change after the 1-hr infection period. For imaging-based experiments, cells were fixed in 4% formaldehyde for 10 min after infection and washed with phosphate-buffered saline (PBS) before subsequent experimentation.

### Drugs

Stocks of the cell death inhibitors Z-VAD-FMK (R&D Systems), GSK’963 (Selleck Chemicals), GSK’872 (Selleck Chemicals), NSA (Tocris), and Z-YVAD-FMK (Sigma-Aldrich) as well as Compound 1 (obtained from MERCK & CO., Inc) were prepared in DMSO. For use, the drugs were diluted in normal growth medium to the following working concentrations: Z-VAD-FMK (50 µM), GSK’963 (1 µM), GSK’872 (5 µM), NSA (10 µM), Z-YVAD-FMK (10 µM), and Compound 1 (5 µM). A DMSO control was included in experiments involving these drugs with a final DMSO concentration of 1%.

### LDH assays

LDH assays were performed with the CyQuant LDH Cytotoxicity Assay Kit (Invitrogen) according to the manufacturer’s protocol. Briefly, A549 or HFF cells split in 96-well plates were infected for 1 hr as described above with CTG-GFP at an MOI of 40 or 15, respectively, and subsequently treated with drugs as indicated. After 36 or 72 hr, 20 µl of 10× lysis buffer or PBS was added to each well and incubated at 37°C for 30 min. Afterward, 50 µl of cell supernatant was mixed with 50 µl of assay buffer and substrate for 30 min at room temperature. The reaction was stopped with 50 µl stop solution and absorbance was measured at 490 nm.

### Luciferase assays

Previously generated HeLa cells expressing GAS-FLUC, GFP-FLUC, or ISRE-GLUC reporters were transduced with TRIP.RARRES3 or TRIP.FLUC lentivirus as described above (Bando et al., 2018; Olias and Sibley, 2016). For kB-LUC, HeLa cells were additionally transduced with HAGE NFkB-TA-LUC-UBC-GFP-W lentivirus. After 48 hr, cells were split into 96-well plates at 1.5×104 cells/well. Cells were treated with or without 100 U/ml IFNβ or IFNγ as indicated for 24 hr and subsequently infected as indicated with CTG-GFP at an MOI of 2 for 24 hr. For firefly luciferase assays, cells were lysed in 50 µl of 1× Luciferase Cell Culture Lysis Buffer (Promega). For Gaussia luciferase assays, supernatant was collected. Luciferase assays were conducted using Pierce Gaussia Luciferase Glow Assay Kit (Thermo Fisher Scientific) or Luciferase Assay System Kit (Promega) according to the manufacturer’s protocol.

### Next generation RNA-sequencing sample preparation and analysis

A549 cells transduced with TRIP.IRF1 or TRIP.FLUC derived lentivirus were split at 3.5×106 into 100 mm dishes. After 24 hr, cells were treated with or without IFNγ at 1000 U/ml for an additional 12 hr before harvest with RLT buffer. RNA was isolated with a Qiagen RNeasy Mini Kit according to the manufacturer’s protocol. Prior to sequencing, RNA quality was determined on an Agilent Bioanalyzer to have a RIN>8.0. Libraries prepared from samples were analyzed with an Illumina NovaSeq 6000 S4 generating a minimum of 3×107 reads per sample. Data were analyzed with Partek Flow software. Prior to alignment, 5 bp were trimmed from the 5′ end of transcripts. Only fragments ≥25 bp in length were considered for alignment. Alignment was conducted with the STAR aligner and differential expression analysis was conducted using GSA analysis with recommended settings. Genes were characterized here as induced by IFNγ or IRF1 if they induced gene expression ≥2-fold with an FDR<0.05. Gene lists were compared using GeneVenn (http://genevenn.sourceforge.net/index.htm; Pirooznia et al., 2007). For GO analysis, gene lists were analyzed with the PANTHER classification system using the GO biological process complete data set (Thomas et al., 2003; Thomas et al., 2006). Statistical significance was determined with Fisher’s exact test using the Bonferroni correction for multiple testing. Only processes containing at least 25 total genes with a p-value≤0.05 were considered.

### Immunofluorescence and imaging

Samples were fixed in 4% formaldehyde for 10 min at room temperature. Wash buffer (WB) consisted of 1% FBS, 1% normal goat serum (NGS), and 0.02% Saponin in PBS. Samples were blocked for 30 min with PBS containing 5% FBS, 5% NGS, and 0.02% Saponin. Samples were incubated with 1:2000 anti-RFP antibody (Invitrogen) and 1:2000 anti-GFP (Invitrogen) in WB overnight, washed four times in WB for 5 min each, and probed with 1:1000 goat anti-mouse Alexa Fluor 488 (Life Technologies) and 1:1000 goat anti-rabbit Alexa Fluor 568 (Life Technologies) in WB for 1 hr. For IRF1 staining, 1:500 anti-IRF1 primary antibody (Cell Signaling Technology) and 1:1000 anti-rabbit Alexa Fluor 488 secondary antibody (Life Technologies) were used instead. Samples were washed three times with WB and nuclei were stained for 5 min with Hoechst 33342 (Life Technologies) in WB. Samples were imaged with a Cytation 3 Imager (BioTek) and images were analyzed in CellProfiler v3.1.9.

For live imaging experiments, cells were imaged starting 2 hr postinfection every 15 min for 48 hr at 37°C under 5% CO2. Live imaging was conducted with a Zeiss Observer Z1 inverted microscope (Zeiss) using a Colibri 7 LED light source (Zeiss), ORCA-ER digital camera (Hamamatsu Photonics), Plan-Neofluar 10× (NA 0.3) objective (Zeiss), and ZEN Blue image acquisition software (v2.5). Following acquisition, channel bleed-through was subtracted from GFP channel images and images were contrast enhanced using ImageJ (v1.53f51).

### Western blotting

A549 cells were split at 2.5×105 cells per well into six-well plates in standard growth medium. The following day, media were changed to standard growth medium supplemented with or without 1000 U/ml IFNγ. After 24 hr, cells were washed with PBS, trypsinized with 0.05% trypsin, and spun down at 200×g for 5 min. Cell pellets were washed once with PBS and lysed with CelLytic M (Millipore) supplemented with 20 mM DTT and 125 U/ml benzonase (Millipore). Samples were incubated at room temperature for 20 min, run on a 10%, 37.5:1 polyacrylamide gel, and transferred to nitrocellulose membranes. Membranes were blocked with 0.1% Tween-20 PBS-T containing 5% bovine serum albumin (BSA) for 30 min. Membranes were incubated with 1:1000 rabbit anti-IDO1 (Cell Signaling Technology), 1:5000 mouse anti-V5 (Invitrogen), or 1:5000 mouse anti-actin (Sigma-Aldrich) in 5% BSA PBS-T for 1 hr, washed four times with PBS-T for 3 min each, incubated with 1:5000 goat anti-mouse 680RD (LI-COR) and 1:5000 goat anti-rabbit 800CW (LI-COR) in 5% BSA PBS-T for 30 min, washed four times in PBS-T for 3 min each, and washed two times in PBS. Membranes were imaged with a LI-COR Odyssey scanner.

### Statistical analysis

For most data sets including those normalized to control, statistical significance was determined with a two-way ANOVA and Tukey’s honestly significant difference post hoc test conducted on raw data prior to normalization and considered variance between experimental replicates and variance between experimental conditions. For LDH and luciferase reporter experiments, statistical significance was determined after normalization and considered variance between experimental replicates and variance between experimental conditions. For experiments in Figure 2A and B, statistical significance was determined using a Brown-Forsythe and Welch ANOVA. Specifically for data sets not normalized to control with only two conditions, a Mann-Whitney U-test was used to determine statistical significance. All statistical analyses were conducted using GraphPad Prism (v3.1.2). The term ‘technical replicate’ refers to separate samples derived from the same original source within the same experiment (i.e., wells of a plate) processed on the same day. The term ‘biological replicate’ refers to separate experiments conducted on different dates with different samples.
