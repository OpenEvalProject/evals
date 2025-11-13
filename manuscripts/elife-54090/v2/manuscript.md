# Bmal1 integrates mitochondrial metabolism and macrophage activation

## Authors

- Ryan K Alexander<sup>1</sup> ([ORCID: 0000-0002-9204-9586](https://orcid.org/0000-0002-9204-9586))
- Yae-Huei Liou<sup>1</sup>
- Nelson H Knudsen<sup>1</sup>
- Kyle A Starost<sup>1</sup>
- Chuanrui Xu<sup>1</sup> ([ORCID: 0000-0003-3225-4083](https://orcid.org/0000-0003-3225-4083))
- Alexander L Hyde<sup>1</sup>
- Sihao Liu<sup>1</sup>
- David Jacobi<sup>1</sup>
- Nan-Shih Liao<sup>3</sup>
- Chih-Hao Lee<sup>1</sup> ([ORCID: 0000-0002-6090-0786](https://orcid.org/0000-0002-6090-0786)) †

### Affiliations

1. Department of Molecular Metabolism, Division of Biological Sciences, Harvard TH Chan School of Public Health Boston United States
2. School of Pharmacy, Tongji Medical College, Huazhong University of Science and Technology Wuhan China
3. Institute of Molecular Biology, Academia Sinica Taiwanese China

† Corresponding author

## Abstract

Metabolic pathways and inflammatory processes are under circadian regulation. Rhythmic immune cell recruitment is known to impact infection outcomes, but whether the circadian clock modulates immunometabolism remains unclear. We find that the molecular clock Bmal1 is induced by inflammatory stimulants, including Ifn-γ/lipopolysaccharide (M1) and tumor-conditioned medium, to maintain mitochondrial metabolism under metabolically stressed conditions in mouse macrophages. Upon M1 stimulation, myeloid-specific Bmal1 knockout (M-BKO) renders macrophages unable to sustain mitochondrial function, enhancing succinate dehydrogenase (SDH)-mediated mitochondrial production of reactive oxygen species as well as Hif-1α-dependent metabolic reprogramming and inflammatory damage. In tumor-associated macrophages, aberrant Hif-1α activation and metabolic dysregulation by M-BKO contribute to an immunosuppressive tumor microenvironment. Consequently, M-BKO increases melanoma tumor burden, whereas administering the SDH inhibitor dimethyl malonate suppresses tumor growth. Therefore, Bmal1 functions as a metabolic checkpoint that integrates macrophage mitochondrial metabolism, redox homeostasis and effector functions. This Bmal1-Hif-1α regulatory loop may provide therapeutic opportunities for inflammatory diseases and immunotherapy.

## Introduction

Inflammation and host defense are energetically costly processes that must balance the use of host resources with an efficient containment of infection or injury. This is underpinned by the dynamic regulation of energy metabolism in immune cells in response to extrinsic signals, including cytokines, pathogen- and damage-associated molecular patterns, and tumor-derived metabolites (Andrejeva and Rathmell, 2017; Buck et al., 2017; Ganeshan and Chawla, 2014; Hotamisligil, 2017; O'Neill et al., 2016). For instance, activation of macrophages by bacterial products, such as lipopolysaccharide (LPS) from gram-negative bacteria, shifts core metabolic function towards increased reliance on aerobic glycolysis, with concomitant inhibition of mitochondrial respiration (Fukuzumi et al., 1996; Rodríguez-Prados et al., 2010; Tannahill et al., 2013). This depressed mitochondrial function appears to be by design, as this process serves multiple purposes. It leads to the so-called ‘broken TCA cycle’ that results, in part, from the shunting of citric acid to lipid synthesis (Andrejeva and Rathmell, 2017). Itaconate, also derived from citrate/aconitate, can modulate macrophage immune response through different mechanisms (Lampropoulou et al., 2016; Mills et al., 2018). By contrast, succinate accumulates through anaplerotic reactions, notably glutaminolysis (Tannahill et al., 2013). Succinate oxidation to fumarate, mediated by succinate dehydrogenase (SDH)/ETC complex II activity, is a primary source of mitochondrial reactive oxygen species (mROS) in inflammatory macrophages that are involved in bactericidal activity (Mills et al., 2016; West et al., 2011). Succinate/SDH is believed to trigger mROS production through accumulation of reduced coenzyme Q leading to reverse electron transfer to ETC complex I (Chouchani et al., 2014; Robb et al., 2018). These findings demonstrate a well-orchestrated metabolic signaling event that occurs at the expense of reduced fuel economy and compromised mitochondrial function in macrophages.

In addition to their bacteria-killing effect, mROS stabilize hypoxia-inducible factor (Hif)-1α through inhibition of prolyl-hydroxylase enzymes that target Hif-1α for ubiquitination by the von Hippel–Lindau (Vhl) E3 ubiquitin ligase and subsequent proteasomal degradation (Bell et al., 2007; Jaakkola et al., 2001). Hif-1α is a master transcriptional regulator of genes involved in glycolysis and anabolic metabolism, thereby supplementing the energetic needs of the broken TCA cycle (Cramer et al., 2003; Masson and Ratcliffe, 2014; Semenza et al., 1994). Hif-1α is also required for the expression of the urea cycle enzyme arginase-1 (Arg1). Arg1 and nitric oxide synthase 2 were initially designated as markers for M2 and M1 macrophages, as these two enzymes convert the amino acid arginine to citrulline and nitric oxide, respectively. However, M1 activation also upregulates Arg1 through Hif-1α. Similarly, in the nutrient-deprived tumor microenvironment, tumor-derived lactate has been proposed to increase Hif-1α activity in tumor-associated macrophages (TAMs) and thus to upregulate Arg1 (Colegio et al., 2014). Aberrant expression of Arg1 in TAMs results in local arginine depletion that inhibits antitumor immunity mediated by cytotoxic T cells and natural killer (NK) cells (Doedens et al., 2010; Steggerda et al., 2017). Accordingly, myeloid-specific deletion of Hif1a or Arg1 suppresses tumor growth in mice (Colegio et al., 2014; Doedens et al., 2010). These observations suggest that the distinction between M1 and M2 activation may not be as clear in vivo and highlight the importance of energetic regulation in immune cell activation.

The circadian rhythm has been implicated in many biological and pathological processes, including the immune response and tumor progression (Hardin and Panda, 2013; Nguyen et al., 2013; Papagiannakopoulos et al., 2016). The molecular clock includes the master regulator Bmal1 (or Aryl hydrocarbon receptor nuclear translocator-like protein 1, Arntl) and its transcriptional partner Clock, as well as the negative regulatory loop that includes Nr1d1, Nr1d2, period (Per1/2/3) and cryptochrome (Cry1/2) proteins, and the positive regulator loop that includes Rorα/β/γ (Hardin and Panda, 2013). Several nuclear receptors, such as the peroxisome proliferator-activated receptors, Pparα, Pparδ/β and Pparγ, are downstream of Bmal1/Clock and control the expression of clock output genes (Canaple et al., 2006; Liu et al., 2013; Yang et al., 2006). The circadian clock is both robust and flexible. It has been demonstrated that time-restricted feeding in mice can synchronize the peripheral clock separately from the central clock (Damiola et al., 2000), suggesting that a primary function of circadian rhythm is to maximize metabolic efficiency. In concert, we and others have shown that hepatic Bmal1 regulates rhythmic mitochondrial capacity in anticipation of nutrient availability (Jacobi et al., 2015; Peek et al., 2013). Prior studies have implicated the circadian oscillator in regulating macrophage inflammatory function. Notably, myeloid-specific Bmal1 deletion disrupts diurnal monocyte trafficking and increases systemic inflammation and mortality in sepsis mouse models (Nguyen et al., 2013). Whether and how the circadian clock controls the metabolism of immune cells to modulate their effector functions remains unclear.

In the present study, we describe a cell-autonomous role for Bmal1 in macrophage energetic regulation. Bmal1 is induced following macrophage inflammatory stimulation. Its loss-of-function exacerbates mitochondrial dysfunction, energetic stress and Hif-1α-dependent metabolic reprogramming. By using the B16-F10 melanoma model, we obtained results that demonstrate that the regulatory axis between Bmal1 and Hif-1α dictates macrophage energy investment that is relevant for discrete activation or polarization states, including activation of M1 and tumor-associated macrophages.

## Results

### The circadian clock is a transcriptional module induced by M1 activation

To assess transcriptional regulators that modulate the energetics and inflammatory function of macrophages, we performed RNA sequencing (RNA-seq) comparing interferon-γ (Ifn-γ) primed bone-marrow-derived macrophages (BMDM) without or with LPS stimulation (10 ng/mL for 8 hr, referred to as M1 activation). Gene ontology analysis using the DAVID platform was performed to identify clusters of transcription factors that were up- or downregulated in inflammatory macrophages, which were used to generate a protein–protein interaction map using STRING (Table 1 and Figure 1—figure supplement 1A). Several activators of mitochondrial function or biogenesis were repressed, including Myc (Li et al., 2005), Pparg, Pparg co-activator 1 beta (Ppargc1b), and the mitochondrial transcription factor B1 (Tfb1m) and Tfb2m. On the other hand, the canonical inflammatory (e.g., Nfkb1/2, Rela/b, Hif1a, interferon regulatory factor 7 (Irf7) and Irf8) and stress response (e.g., Atf3, Atf6b and Nfe2l2) transcriptional modules were upregulated. Interestingly, clusters of circadian oscillator components (e.g., Per1, Cry1, Nr1d1, Nr1d2 and Rora), as well as nuclear receptors downstream of the molecular clock (e.g., Ppard and its heterodimeric partner Rxra) (Liu et al., 2013), were also induced.

**Table 1.**
 Transcriptional regulators that are differentially regulated in M1-activated macrophages.Genes encoding transcriptional regulators that were significantly induced or repressed by 8h M1 stimulation (p<0.05, false discovery rate [FDR] <0.05, |F.C.| >1.5) in WT bone-marrow-derived macrophages (BMDM) were identified by gene ontology analysis using the DAVID platform. F.C., fold change. Differentially regulated genes that matched the Transcription GO term in the Biological Processes GO database (accession GO:0006350) were used to generate a protein–protein interaction map using String (Figure 1—figure supplement 1). Uncharacterized zinc-finger proteins (ZFPs) were omitted from analyses by String.


<table>
  <tbody>
    <tr>
      <td colspan="8">Induced (278 genes)</td>
    </tr>
    <tr>
      <td>ADAR</td>
      <td>CRY1</td>
      <td>GTF2A1</td>
      <td>KDM4B</td>
      <td>MNT</td>
      <td>PPP1R10</td>
      <td>Snapc1</td>
      <td>Zkscan17</td>
    </tr>
    <tr>
      <td>AFF1</td>
      <td>CRY2</td>
      <td>GTF2E2</td>
      <td>KDM5B</td>
      <td>MXD1</td>
      <td>PPP1R13L</td>
      <td>SNAPC2</td>
      <td>ZMIZ1</td>
    </tr>
    <tr>
      <td>AFF4</td>
      <td>CSRNP1</td>
      <td>GTF2F1</td>
      <td>KDM5C</td>
      <td>MXI1</td>
      <td>PTOV1</td>
      <td>SOX5</td>
      <td>ZSCAN2</td>
    </tr>
    <tr>
      <td>AHR</td>
      <td>CSRNP2</td>
      <td>HBP1</td>
      <td>KEAP1</td>
      <td>MYB</td>
      <td>PTRF</td>
      <td>SPEN</td>
      <td>ZSCAN29</td>
    </tr>
    <tr>
      <td>AKNA</td>
      <td>DAXX</td>
      <td>HDAC1</td>
      <td>KLF11</td>
      <td>NAB2</td>
      <td>PURA</td>
      <td>SPIC</td>
      <td>ZXDB</td>
    </tr>
    <tr>
      <td>ANP32A</td>
      <td>DDIT3</td>
      <td>HES1</td>
      <td>KLF16</td>
      <td>NACC1</td>
      <td>RBPJ</td>
      <td>SREBF1</td>
      <td></td>
    </tr>
    <tr>
      <td>ARHGAP22</td>
      <td>DDX54</td>
      <td>HES7</td>
      <td>KLF4</td>
      <td>NCOA5</td>
      <td>RCOR2</td>
      <td>SRF</td>
      <td></td>
    </tr>
    <tr>
      <td>ARID3A</td>
      <td>DEDD2</td>
      <td>HEXIM1</td>
      <td>KLF7</td>
      <td>NCOA7</td>
      <td>REL</td>
      <td>ST18</td>
      <td></td>
    </tr>
    <tr>
      <td>ARID5A</td>
      <td>DNMT3A</td>
      <td>HIC1</td>
      <td>KLF9</td>
      <td>NCOR2</td>
      <td>RELA</td>
      <td>STAT2</td>
      <td></td>
    </tr>
    <tr>
      <td>ARNT2</td>
      <td>DPF1</td>
      <td>HIC2</td>
      <td>LCOR</td>
      <td>NFAT5</td>
      <td>RELB</td>
      <td>STAT3</td>
      <td></td>
    </tr>
    <tr>
      <td>ASF1A</td>
      <td>DRAP1</td>
      <td>HIF1A</td>
      <td>LCORL</td>
      <td>NFE2L2</td>
      <td>REST</td>
      <td>STAT4</td>
      <td></td>
    </tr>
    <tr>
      <td>ATF3</td>
      <td>E2F5</td>
      <td>HIF3A</td>
      <td>LHX2</td>
      <td>NFIL3</td>
      <td>RFX1</td>
      <td>STAT5A</td>
      <td></td>
    </tr>
    <tr>
      <td>ATF4</td>
      <td>E4F1</td>
      <td>HINFP</td>
      <td>LIN54</td>
      <td>NFKB1</td>
      <td>RING1</td>
      <td>TAF1C</td>
      <td></td>
    </tr>
    <tr>
      <td>ATF6B</td>
      <td>EAF1</td>
      <td>HIVEP1</td>
      <td>LITAF</td>
      <td>NFKB2</td>
      <td>RNF2</td>
      <td>TAF7</td>
      <td></td>
    </tr>
    <tr>
      <td>ATXN7L3</td>
      <td>EDF1</td>
      <td>HIVEP2</td>
      <td>LMO4</td>
      <td>NFKBIZ</td>
      <td>RORA</td>
      <td>TAL1</td>
      <td></td>
    </tr>
    <tr>
      <td>BANP</td>
      <td>EGR2</td>
      <td>HIVEP3</td>
      <td>MAF</td>
      <td>NOTCH1</td>
      <td>RREB1</td>
      <td>TBL1X</td>
      <td></td>
    </tr>
    <tr>
      <td>BATF</td>
      <td>EID3</td>
      <td>HLX</td>
      <td>MAFF</td>
      <td>NPTXR</td>
      <td>RSLCAN18</td>
      <td>TCEB2</td>
      <td></td>
    </tr>
    <tr>
      <td>BCL3</td>
      <td>EIF2C1</td>
      <td>HMG20B</td>
      <td>MAFG</td>
      <td>NR1D1</td>
      <td>RUNX2</td>
      <td>TCF4</td>
      <td></td>
    </tr>
    <tr>
      <td>BCL6</td>
      <td>ELK1</td>
      <td>HMGA1</td>
      <td>MAFK</td>
      <td>NR1D2</td>
      <td>RUNX3</td>
      <td>TGIF1</td>
      <td></td>
    </tr>
    <tr>
      <td>BCORL1</td>
      <td>ELL</td>
      <td>HMGA1-RS1</td>
      <td>MAML1</td>
      <td>NR1H2</td>
      <td>RUVBL2</td>
      <td>THAP7</td>
      <td></td>
    </tr>
    <tr>
      <td>BHLHE40</td>
      <td>ELL2</td>
      <td>HMGN5</td>
      <td>MAX</td>
      <td>NR1H3</td>
      <td>RXRA</td>
      <td>TLE2</td>
      <td></td>
    </tr>
    <tr>
      <td>BHLHE41</td>
      <td>ELL3</td>
      <td>HOPX</td>
      <td>MBD2</td>
      <td>NR2F6</td>
      <td>RYBP</td>
      <td>TLE3</td>
      <td></td>
    </tr>
    <tr>
      <td>BRWD1</td>
      <td>EPAS1</td>
      <td>HSF4</td>
      <td>MDFIC</td>
      <td>NR4A1</td>
      <td>SAFB2</td>
      <td>TRERF1</td>
      <td></td>
    </tr>
    <tr>
      <td>BTG2</td>
      <td>ERF</td>
      <td>IFI205</td>
      <td>MECP2</td>
      <td>NR4A2</td>
      <td>SAP130</td>
      <td>TRIB3</td>
      <td></td>
    </tr>
    <tr>
      <td>CAMTA2</td>
      <td>ERN1</td>
      <td>IFT57</td>
      <td>MED13</td>
      <td>NR4A3</td>
      <td>SAP30</td>
      <td>TRRAP</td>
      <td></td>
    </tr>
    <tr>
      <td>CASZ1</td>
      <td>ESRRA</td>
      <td>ILF3</td>
      <td>MED13L</td>
      <td>PAF1</td>
      <td>SBNO2</td>
      <td>TSC22D4</td>
      <td></td>
    </tr>
    <tr>
      <td>CBX4</td>
      <td>ETS1</td>
      <td>ING2</td>
      <td>MED15</td>
      <td>PAX4</td>
      <td>SCAF1</td>
      <td>TSHZ1</td>
      <td></td>
    </tr>
    <tr>
      <td>CCDC85B</td>
      <td>ETV3</td>
      <td>IRF2BP1</td>
      <td>MED25</td>
      <td>PCGF3</td>
      <td>SEC14L2</td>
      <td>USP49</td>
      <td></td>
    </tr>
    <tr>
      <td>CDKN2A</td>
      <td>FIZ1</td>
      <td>IRF4</td>
      <td>MED26</td>
      <td>PCGF5</td>
      <td>SERTAD1</td>
      <td>VPS72</td>
      <td></td>
    </tr>
    <tr>
      <td>CEBPB</td>
      <td>FLII</td>
      <td>IRF7</td>
      <td>MED28</td>
      <td>PER1</td>
      <td>SETD8</td>
      <td>WHSC1L1</td>
      <td></td>
    </tr>
    <tr>
      <td>CEBPD</td>
      <td>FOXP1</td>
      <td>IRF8</td>
      <td>MED31</td>
      <td>PER2</td>
      <td>SFPI1</td>
      <td>ZBTB17</td>
      <td></td>
    </tr>
    <tr>
      <td>CITED4</td>
      <td>FOXP4</td>
      <td>JARID2</td>
      <td>MEF2D</td>
      <td>PHF1</td>
      <td>SIN3B</td>
      <td>ZBTB24</td>
      <td></td>
    </tr>
    <tr>
      <td>CREB5</td>
      <td>GATA2</td>
      <td>JDP2</td>
      <td>MIER2</td>
      <td>PHF12</td>
      <td>SIX1</td>
      <td>ZBTB46</td>
      <td></td>
    </tr>
    <tr>
      <td>CREBBP</td>
      <td>GATAD2A</td>
      <td>JMJD6</td>
      <td>MIER3</td>
      <td>PIAS4</td>
      <td>SIX5</td>
      <td>ZBTB7A</td>
      <td></td>
    </tr>
    <tr>
      <td>CREBL2</td>
      <td>GATAD2B</td>
      <td>JUN</td>
      <td>MITF</td>
      <td>PML</td>
      <td>SLC30A9</td>
      <td>ZBTB7B</td>
      <td></td>
    </tr>
    <tr>
      <td>CREBZF</td>
      <td>GFI1</td>
      <td>JUNB</td>
      <td>MIXL1</td>
      <td>POU2F2</td>
      <td>SMAD3</td>
      <td>ZEB1</td>
      <td></td>
    </tr>
    <tr>
      <td>CREM</td>
      <td>GLIS3</td>
      <td>JUND</td>
      <td>MKL1</td>
      <td>POU3F1</td>
      <td>SMAD4</td>
      <td>ZFHX4</td>
      <td></td>
    </tr>
    <tr>
      <td>CRTC2</td>
      <td>GPBP1</td>
      <td>KDM3A</td>
      <td>MLL1</td>
      <td>POU6F1</td>
      <td>SMAD7</td>
      <td>ZGPAT</td>
      <td></td>
    </tr>
    <tr>
      <td>CRTC3</td>
      <td>GRHL1</td>
      <td>KDM4A</td>
      <td>MNDA</td>
      <td>PPARD</td>
      <td>SMYD1</td>
      <td>ZHX2</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="8"></td>
    </tr>
    <tr>
      <td colspan="8">Repressed (195 genes)</td>
    </tr>
    <tr>
      <td>ACTL6A</td>
      <td>ELK3</td>
      <td>IRF2</td>
      <td>NAA15</td>
      <td>SAP18</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AHRR</td>
      <td>ELP2</td>
      <td>ITGB3BP</td>
      <td>NCOA1</td>
      <td>SAP25</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AI987944</td>
      <td>ELP3</td>
      <td>KDM2B</td>
      <td>NCOA3</td>
      <td>SETD7</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ANG</td>
      <td>ELP4</td>
      <td>KLF10</td>
      <td>NFATC1</td>
      <td>SETDB1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ASCC1</td>
      <td>ENY2</td>
      <td>KLF13</td>
      <td>NFATC2</td>
      <td>SNAPC5</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ASF1B</td>
      <td>ERCC8</td>
      <td>KLF2</td>
      <td>NFIA</td>
      <td>SP3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ATAD2</td>
      <td>ESR1</td>
      <td>KLF8</td>
      <td>NKRF</td>
      <td>SSBP2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AW146154</td>
      <td>ETOHI1</td>
      <td>L3MBTL2</td>
      <td>NPAT</td>
      <td>SSRP1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>BCL9L</td>
      <td>ETV1</td>
      <td>LBH</td>
      <td>NPM3</td>
      <td>STAT1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CBFA2T3</td>
      <td>EYA1</td>
      <td>LRPPRC</td>
      <td>NR2C1</td>
      <td>SUV39H1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CBX3</td>
      <td>EYA4</td>
      <td>LYL1</td>
      <td>NRIP1</td>
      <td>SUV39H2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CBX6</td>
      <td>EZH2</td>
      <td>MAFB</td>
      <td>OVOL2</td>
      <td>SUV420H2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CBX8</td>
      <td>FLI1</td>
      <td>MARS</td>
      <td>PA2G4</td>
      <td>TADA1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CCNH</td>
      <td>FNTB</td>
      <td>MBTPS2</td>
      <td>PHF19</td>
      <td>TADA2A</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CDCA7</td>
      <td>FOXM1</td>
      <td>MCM2</td>
      <td>PHTF2</td>
      <td>TAF4B</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CDCA7L</td>
      <td>GTF2H2</td>
      <td>MCM3</td>
      <td>PNRC2</td>
      <td>TAF9B</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CEBPA</td>
      <td>GTF2I</td>
      <td>MCM4</td>
      <td>POLR1B</td>
      <td>TBX6</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CEBPG</td>
      <td>GTF2IRD1</td>
      <td>MCM5</td>
      <td>POLR2G</td>
      <td>TCEA3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CEBPZ</td>
      <td>GTF3A</td>
      <td>MCM6</td>
      <td>POLR2I</td>
      <td>TCEAL8</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CHAF1A</td>
      <td>GTF3C5</td>
      <td>MCM7</td>
      <td>POLR3B</td>
      <td>TCF7L2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CHAF1B</td>
      <td>HABP4</td>
      <td>MCM8</td>
      <td>POLR3H</td>
      <td>TFB1M</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CHD9</td>
      <td>HDAC10</td>
      <td>MCTS1</td>
      <td>POLR3K</td>
      <td>TFB2M</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CHURC1</td>
      <td>HDAC11</td>
      <td>MED14</td>
      <td>PPARG</td>
      <td>TFDP2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CIITA</td>
      <td>HDAC2</td>
      <td>MED18</td>
      <td>PPARGC1B</td>
      <td>THOC1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CIR1</td>
      <td>HDAC6</td>
      <td>MED22</td>
      <td>PRIM1</td>
      <td>TLE1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CREB3</td>
      <td>HDAC7</td>
      <td>MED27</td>
      <td>PRIM2</td>
      <td>TRAPPC2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CREB3L1</td>
      <td>HDAC8</td>
      <td>MEF2A</td>
      <td>PRMT7</td>
      <td>TRIM24</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CREB3L2</td>
      <td>HDAC9</td>
      <td>MEF2C</td>
      <td>PROX2</td>
      <td>TWISTNB</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CTNND1</td>
      <td>HELLS</td>
      <td>MEIS1</td>
      <td>PSPC1</td>
      <td>TXNIP</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CUX1</td>
      <td>HHEX</td>
      <td>MLF1IP</td>
      <td>RAD54B</td>
      <td>UHRF1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>DDI2</td>
      <td>HIP1</td>
      <td>MLL3</td>
      <td>RB1</td>
      <td>USF1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>DNMT1</td>
      <td>HIRA</td>
      <td>MLLT3</td>
      <td>RBAK</td>
      <td>VGLL4</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>DR1</td>
      <td>HMBOX1</td>
      <td>MNAT1</td>
      <td>RCBTB1</td>
      <td>VPS36</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E2F1</td>
      <td>HMGA2</td>
      <td>MPV17</td>
      <td>RCOR3</td>
      <td>WTIP</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E2F2</td>
      <td>HOXA1</td>
      <td>MXD3</td>
      <td>RERE</td>
      <td>ZBTB3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E2F6</td>
      <td>HTATSF1</td>
      <td>MXD4</td>
      <td>RFC1</td>
      <td>ZBTB8A</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E2F7</td>
      <td>IKBKAP</td>
      <td>MYBL2</td>
      <td>RPAP1</td>
      <td>ZHX1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>E2F8</td>
      <td>IKZF2</td>
      <td>MYC</td>
      <td>RSC1A1</td>
      <td>ZIK1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>EGR3</td>
      <td>IL16</td>
      <td>MYCBP2</td>
      <td>RSL1</td>
      <td>ZKSCAN4</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

We examined the expression of Bmal1, the non-redundant master regulator of circadian rhythm, and found that M1 activation (Figure 1A) or LPS treatment without Ifn-γ priming (Figure 1B) induced its mRNA and protein levels, which peaked at 12 hr after the stimulation. Because LPS was directly added to the cell culture without changing the medium, the induction of Bmal1 was not due to serum shock (Tamaru et al., 2003). In fact, a one-hour LPS treatment in culture medium with 2% serum was sufficient to reset Bmal1 expression (Figure 1C) in a manner resembling serum shock (which requires a much higher serum concentration). Similar results were observed in mouse embryonic fibroblasts (MEFs), suggesting that the inflammatory regulation of Bmal1 was not macrophage-specific (Figure 1—figure supplement 1B).

![Figure 1.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig1-v2.jpg)

**Figure 1.:** (A–C) Bmal1 protein levels (top) and relative gene expression determined by qPCR (bottom) in bone-marrow-derived macrophages (BMDM) during a 24-hr time course of M1 activation (10 ng/ml Ifn-γ overnight priming + 10 ng/ml LPS) (A), treatment with LPS alone (100 ng/ml) (B), or acute LPS treatment for 1 hr (100 ng/mL) (C). For M1- and LPS-only treatments, LPS was spiked in at time zero without medium change. For acute LPS treatment, cells were grown with LPS for one hour followed by culture in DMEM, 2% FBS without LPS (time zero indicates medium change). N = 3 biological replicates were used for qPCR. (D) Relative expression of circadian clock and inflammatory transcriptional regulators in M1-activated macrophages, as determined by qPCR. N = 3 biological replicates, statistical analysis performed using two-way ANOVA for WT vs M-BKO across the time course. Data are presented as mean ± S.E.M. *, p<0.05. Experiments were repeated at least twice.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Annotated protein–protein interaction maps generated by STRING of transcriptional regulators that were significantly induced (left) or repressed (right) in WT macrophages by 8 hours M1 activation (Ifn-γ priming followed by stimulation with 10 ng/mL LPS) compared to time-matched controls (Ifn-γ priming without LPS), determined by RNA-seq (p<0.05, FDR <0.05, |F.C.|>1.5). N = 3 biological replicates. F.C., fold change. See Table 1 for the complete gene list. (B) Bmal1 protein levels (top panels) and relative gene expression determined by qPCR (bottom panels) in mouse embryonic fibroblasts during a 24-hr time course of M1 activation (10 ng/ml Ifn-γ overnight priming + 10 ng/ml LPS, left panels), treatment with LPS only (100 ng/ml, middle panels), or 1 hr acute LPS treatment (100 ng/mL, right panels). For M1- and LPS-only treatments, LPS was spiked in at time zero without medium change. For acute LPS treatment, cells were grown with LPS for one hour followed by culture in DMEM, 2% FBS without LPS (time zero indicates medium change). N = 3 biological replicates for qPCR. (C) Gene expression during a 24-hr time course of Il-4 treatment in WT and M-BKO macrophages determined by qPCR. N = 3 biological replicates. Data are presented as mean ± S.E.M. *, p<0.05. Cell culture experiments were repeated at least twice.

Myeloid-specific Bmal1 knockout (M-BKO, Bmal1f/f crossed to Lyz2-Cre) mice were generated to determine the role of the circadian clock in macrophage function. Bmal1f/f was used as the wild-type control (WT). M-BKO did not affect M1 induction of canonical inflammatory regulators, such as Nfkb1, Stat3, Hif1a and Myc (Figure 1D). The expression of genes downstream of Bmal1, including Nr1d2, Cry1 and Ppard, was dysregulated, and there was a further reduction of Pparg expression by M1 activation in M-BKO macrophages compared to WT cells (Figure 1D). By contrast, M2 activation by Il-4 did not regulate Bmal1 mRNA levels, and Il-4-induced expression of Arg1 and Mgl2 was not altered by M-BKO (Figure 1—figure supplement 1C). These results suggest that the circadian clock may function as a downstream effector of M1 stimulation in a cell-autonomous manner.

### Bmal1 promotes mitochondrial metabolism in inflammatory macrophages

Because Pparδ/Pparγ are known regulators of mitochondrial function and energy substrate utilization in macrophages (Dai et al., 2017; Kang et al., 2008; Lee et al., 2006; Odegaard et al., 2007), we sought to determine the role of Bmal1 in macrophage bioenergetic control. In WT macrophages, M1 activation caused a progressive decrease in mitochondrial content, which was more pronounced in M-BKO macrophages (Figure 2A). The reduced mitochondrial content was accompanied by elevated protein levels of the mitophagy receptor Bnip3 (Figure 2—figure supplement 1A). The Seahorse Mito Stress test also showed a steeper decline in oxygen consumption rate (OCR) following M1 treatment in M-BKO macrophages, compared to WT cells (Figure 2B and Figure 2—figure supplement 1B). Measurement of ETC complex activity in isolated mitochondria indicated that M-BKO caused a significant reduction in the activities of complexes II and III, given an equal amount of mitochondrial protein, 6 hr after M1 stimulation (Figure 2C). This suggests that macrophage Bmal1 gene deletion also worsened M1-mediated suppression of mitochondrial function. To determine whether M-BKO affected the basal respiration and/or the recovery of mitochondrial homeostasis following inflammatory insults, we performed Mito Stress tests 24 hr after acute serum shock or LPS treatment, both of which synchronized Bmal1 gene expression (Tamaru et al., 2003 and Figure 1C). There was no genotypic difference in the OCR at the resting state, and serum shock did not affect respiration in WT and M-BKO macrophages (Figure 2—figure supplement 1C). By contrast, the basal OCR of M-BKO macrophages remained suppressed 24 hr following acute LPS treatment, whereas the basal OCR was completely recovered in WT macrophages (Figure 2—figure supplement 1D). Thus, Bmal1 gene deletion impacts macrophage mitochondrial respiration both during inflammatory stimulations and during the subsequent recovery phase.

![Figure 2.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig2-v2.jpg)

**Figure 2.:** (A) Assessment of mitochondrial mass in macrophages throughout a time course of M1 activation using Mitotracker Green (mean fluorescence intensity, MFI) determined by flow cytometry. N = 3 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-BKO across the time course. (B) Basal oxygen consumption rate (OCR) in Ifn-γ-primed macrophages pretreated without or with LPS (10 ng/mL) for 2 or 6 hr before the assay. See Figure 2—figure supplement 1B for the full assay results. The assay medium contained minimal DMEM with 5 mM glucose and 1 mM sodium pyruvate, pH 7.4. N = 5 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-BKO across the time course. (C) Activities of ETC complexes in isolated mitochondria from WT and M-BKO macrophages after 6 hours M1 stimulation. N = 3 biological replicates, statistical analysis was performed using Student’s T test. (D) Extracellular flux analysis in Ifn-γ-primed macrophages measuring the changes in extracellular acidification rate (ECAR, left panel) and oxygen consumption rate (OCR, right panel) following LPS injection (100 ng/mL). The assay medium contained 5 mM glucose and 1 mM pyruvate in minimal DMEM with 2% dialyzed FBS, pH 7.4. N = 5 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-BKO across the time course. (E) Glycolytic stress test in Ifn-γ-primed macrophages measuring ECAR following glucose (25 mM) injection, with or without LPS (100 ng/mL). Maximal glycolytic rate was determined by injection of oligomycin (OM, 2 μM), and glycolysis-dependent ECAR was determined by injection of 2-deoxyglucose (2-DG, 50 mM). The assay medium contained minimal DMEM with 2% dialyzed FBS, pH 7.4. N = 5 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-BKO across the time course. Data are presented as mean ± S.E.M. *, p<0.05. Experiments were repeated at least twice.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Immunoblot of the mitophagy regulator Bnip3 in M1-activated WT and M-BKO BMDMs. (B) Mitostress test measuring oxygen consumption rate (OCR) in Ifn-γ-primed macrophages pretreated without or with LPS (10 ng/mL) for 2 or 6 hr before the assay. Following three measurements of basal respiration, sequential injections of oligomycin (OM, 2 μM), carbonyl cyanide-4-phenylhydrazone (FCCP, 0.5, μM) and rotenone and antimycin A (rot/AA, 1 μM) were carried out to determine uncoupled respiration, spare respiratory capacity, and non-mitochondrial respiration, respectively. The assay medium contained minimal DMEM with 5 mM glucose and 1 mM sodium pyruvate, pH 7.4. N = 5 biological replicates. (C) Mitostress test measuring OCR in macrophages without (control, Ctl) or with serum shock resulting from treatment with 50% FBS for 2 hr to synchronize the circadian clock (Synchronized). Cells were recovered in fresh growth medium containing 10% FBS and the assay was performed 16 hr after the serum shock treatment. N = 5 biological replicates. (D) Mitostress test measuring OCR in macrophages without or with acute LPS treatment. Cells were cultured in growth medium with 2% FBS without (Ctl) or with 100 ng/mL LPS for 2 hr (LPS recovery), followed by recovery in fresh growth medium with 2% FBS for 24 hr prior to the assay. N = 5 biological replicates, statistical analysis was performed using two-way ANOVA for Ctl vs LPS recovery across the time course. (E) Extracellular flux analysis of thioglycollate-elicited peritoneal macrophages measuring the changes in ECAR (left panel) and OCR (right panel) following LPS injection (final concentration 1 μg/mL). The assay medium contained 5 mM glucose and 1 mM pyruvate in minimal DMEM with 2% dialyzed FBS, pH 7.4. N = 5 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-BKO across the time course. (F) Bmal1 mRNA expression determined by qPCR (left) and protein levels (right) in RAW264.7 macrophage stable lines. Bmal1-OE, Bmal1 overexpressing stable line. Cells that were transduced with empty vector were used as the control. N = 3 biological replicates for qPCR, statistical analysis was performed using Student’s T test. V, vector control; OE, Bmal1 overexpression. (G) Measurement of the changes in ECAR (left) and OCR (right) in Ifn-γ-primed RAW264.7 stable lines after injection with LPS (final concentration 100 ng/mL). The assay medium contained 25 mM glucose and 1 mM pyruvate in minimal DMEM with 2% dialyzed FBS, pH 7.4. N = 5 biological replicates, statistical analysis was performed using two-way ANOVA for control vs Bmal1 OE across the time course. (H) Blood glucose levels in 4-month-old WT and M-BKO male mice before and 6 hr after i.p. injection with 10 μg LPS per g body weight. N = 10 mice, statistical analysis was performed using Student’s T test. (I) Glycolytic stress test in splenic macrophages isolated from mice in panel (D) that were sacrificed 6 hr after LPS injection. ECAR was measured before and after injection with glucose (25 mM). Maximal glycolytic rate was determined by injection of oligomycin (OM, 2 μM). Glycolysis-dependent ECAR was determined by injection of 2-deoxyglucose (2-DG, 50 mM). The assay medium contained minimal DMEM, pH 7.4. N = 10 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-BKO across the time course. Data are presented as mean ± S.E.M. *, p<0.05. Experiments were repeated at least twice.

Seahorse extracellular flux analysis showed that LPS injection increased the extracellular acidification rate (ECAR, indicative of lactic acid secretion) and decreased the oxygen consumption rate (OCR) of WT macrophages, as expected from aerobic glycolysis (Figure 2D). The ECAR and OCR were further enhanced and suppressed, respectively, in M-BKO macrophages. Similar results were obtained in thioglycollate-elicited peritoneal macrophages isolated from WT and M-BKO mice (Figure 2—figure supplement 1E). By contrast, stable overexpression of Bmal1 (Bmal1-OE) in RAW264.7 macrophages resulted in higher OCR and lower ECAR after LPS stimulation, compared to control cells (Figure 2—figure supplement 1F-G). To examine aerobic glycolysis directly, glucose was injected during the extracellular flux assay with or without co-injection of LPS. There was no difference in the basal glycolytic rate between WT and M-BKO macrophages (Figure 2E). LPS increased ECAR in both genotypes and to a greater extent in M-BKO macrophages. The induced ECAR could be blocked by injection of 2-deoxyglucose (2-DG), confirming that the acidification was caused by aerobic glycolysis. Furthermore, an increase in the glycolytic rate was observed in splenic macrophages from M-BKO mice isolated 6 hr after i.p. injection of LPS, which was accompanied by lowered circulating glucose levels, indicative of increased glucose consumption by inflammatory myeloid cells in M-BKO mice when compared to WT animals (Figure 2—figure supplement 1H-I).

To further assess the metabolic state, metabolomics analyses were employed to compare the cellular metabolite levels of WT and M-BKO macrophages 0, 6 and 12 hr after M1 activation (Figure 3A–B and Figure 3—source data 1). As has been reported (Tannahill et al., 2013), M1 activation caused accumulation of glycolytic intermediates (glucose-6-phosphate, fructose-6-phosphate and lactic acid) and depletion of TCA metabolites (e.g. citrate) but accumulation of succinate. Glycolytic metabolites and succinate were significantly higher in M-BKO macrophages than in WT cells. M-BKO cells also showed accumulation of several amino acids and intermediates of the urea cycle (which detoxifies ammonia released from amino-acid deamination) (Figure 3A and Figure 3—source data 1). Consistent with the increased glycolytic metabolites, M1-stimulated glucose uptake and lactate production were higher in M-BKO macrophages than in WT cells (Figure 3C–D). These results suggest that Bmal1 loss-of-function leads to metabolic dysregulation in M1-stimulated macrophages.

![Figure 3.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig3-v2.jpg)

**Figure 3.:** (A) Summary of steady-state metabolomics data for differentially regulated metabolites from WT and M-BKO macrophages throughout a 12-hour M1 activation time course. Data are presented as heat maps (normalized to WT control for each metabolite, each panel is the average of four biological replicates). Statistical analysis was performed using two-way ANOVA for WT vs M-BKO across the time course. (B) Box plots of the relative abundances of select metabolites in panel (A). (C, D) Uptake of [3H]−2-deoxyglucose (C) and lactate secretion (D) in control or M1-activated macrophages. N = 3 biological replicates, statistical analysis was performed using Student’s T test. Cell culture assays were repeated at least twice.

### Bmal1–Hif-1α crosstalk regulates macrophage energy metabolism

As mentioned earlier, Hif-1α is a primary regulator of glucose metabolism in inflammatory macrophages. The enhanced aerobic glycolysis in M-BKO macrophages prompted us to examine whether Hif-1α activity was aberrantly elevated in these cells. Western blot analyses revealed that M1 activation led to a several-fold induction of Hif-1α protein levels in M-BKO macrophages compared to WT cells (Figure 4A), whereas Bmal1-OE RAW264.7 macrophages showed reduced Hif-1α protein (Figure 4—figure supplement 1A). The expression of Hif-1α targets, such as lactate dehydrogenase A (Ldha), Arg1 and Il1b, was enhanced by M-BKO and blocked by myeloid Hif1a knockout (M-HKO, Figure 4B). Hif-1α gene expression did not differ between WT and M-BKO cells (Figure 1D). mROS derived from increased succinate oxidation has previously been demonstrated to stabilize Hif-1α protein in inflammatory macrophages (Mills et al., 2016). Metabolite analyses showed accumulation of succinate in M-BKO macrophages, suggesting that elevated mROS may be the cause of the increased Hif-1α protein. In fact, levels of mROS were higher in isolated mitochondria from M-BKO macrophages at 1 hr and 4 hr of M1 activation than in WT macrophages (Figure 4C). The addition of succinate increased mROS production in mitochondria from both WT and M-BKO macrophages. An additional two-fold induction of mROS was detected in mitochondria from 4-hr M1-stimulated M-BKO, but not in those from WT macrophages. Hif-1α protein accumulation could be normalized between genotypes by co-treatment with the antioxidant N-acetylcysteine (N-AC) or the competitive complex II inhibitor dimethylmalonate (DMM), which blocks mROS production (Figure 4D). Furthermore, M1-stimulated glucose uptake, lactate release and aerobic glycolysis were attenuated in myeloid-specific Bmal1 and Hif1a double knockout macrophages (M-BHdKO; Figure 4—figure supplement 1B-D), indicating that the increased glucose utilization in M-BKO was Hif-1α-dependent.

![Figure 4.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig4-v2.jpg)

**Figure 4.:** (A) Immunoblots of Hif-1α and Bmal1 protein levels in WT and M-BKO macrophages during a 24-hr time course of M1 activation. (B) Relative expression of Hif-1α target genes in WT, M-BKO and M-HKO macrophages determined by qPCR. N = 3 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-BKO or WT vs M-HKO across the time course. (C) Measurement of mROS using MitoSox Red (mean fluorescence intensity, MFI) in mitochondria isolated from control or M1-activated macrophages. Succinate (Suc, 10 mM) was included during MitoSox Red staining where indicated. N = 3 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-BKO across the time course. (D) Hif-1α protein levels in control or 8-hr M1-activated macrophages co-treated with or without N-acetylcysteine (NAC) or 10 mM dimethylmalonate (DMM). Data are presented as mean ± S.E.M. *, p<0.05 for WT vs M-BKO and p<0.05 for WT vs M-HKO. Experiments were repeated at least twice.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Hif-1α protein levels in M1-activated (primed with 10 ng/mL Ifn-γ and stimulated with 50 ng/mL LPS) control and Bmal1-OE RAW264.7 stable lines. (B, C) Uptake of [3H]−2-deoxyglucose and lactate secretion in control or M1-activated macrophages. N = 3 biological replicates, statistical analysis was performed using Student’s T test. M-BHdko: myeloid-specific Bmal1 and Hif1a double knockout. (D) Glycolytic stress test in Ifn-γ-primed macrophages measuring ECAR following glucose (25 mM) injection without or with LPS (100 ng/mL). Maximal glycolytic rate was determined by injection of oligomycin (OM, 2 μM), and glycolysis-dependent ECAR was determined by injection of 2-deoxyglucose (2-DG, 50 mM). The assay medium contained minimal DMEM with 2% dialyzed FBS, pH 7.4. N = 5 biological replicates. The difference between LPS-treated WT and M-BHdKO macrophages was determined by two-way ANOVA across the time course. (E) Expression of Nrf2 target genes determined by qPCR throughout a 24-hr time course following M1 stimulation. N = 3 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-BKO across the time course. Data are presented as mean ± S.E.M. *, p<0.05. Experiments were repeated at least twice.

A previous study suggests that Bmal1 deletion impairs the expression of Nfe2l2 (which encodes Nrf2) and its downstream antioxidant genes, thereby increasing oxidative stress (Early et al., 2018). However, we found that expression of Nfe2l2- and Nrf2-induced oxidative stress responsive genes, such as NAD(P)H quinone dehydrogenase 1 (Nqo1; Figure 4—figure supplement 1E), were upregulated in M-BKO macrophages upon M1 stimulation, suggesting that increased mROS associated with M-BKO was the cause rather than the consequence of dysregulated Nrf2 signaling. Collectively, these data indicate that Bmal1 and Hif-1α regulate opposing metabolic programs and that Bmal1-mediated mitochondrial metabolism serves to fine-tune Hif-1α activity by modulating oxidative stress.

### Bmal1 loss-of-function induces metabolic reprogramming toward amino-acid catabolism

To characterize fully metabolic programs that were impacted by Bmal1 loss of function, we compared RNA-seq data from control and M1-activated WT and M-BKO macrophages. These analyses revealed that the majority of M1-induced or -suppressed genes were regulated in a similar manner in WT and M-BKO macrophages, suggesting that Bmal1 gene deletion affected specific inflammatory processes (Figure 5—figure supplement 1A and Figure 5—source data 1) and in line with the intact expression pattern of Nfkb1 in M-BKO macrophages (Figure 1D). Gene ontology analyses indicated that the most enriched categories of M1-upregulated genes shared by both genotypes included regulation of apoptosis, response to stress and cytokine production. Among the top categories of suppressed genes were the cell cycle, DNA repair and carbohydrate metabolism. In the carbohydrate metabolism category, most TCA cycle enzymes were downregulated by M1 activation (Figure 5A).

![Figure 5.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig5-v2.jpg)

**Figure 5.:** (A) Schematic representation of M1-regulated genes involved in amino-acid and TCA metabolism determined by RNA-seq. Genes in blue are downregulated whereas genes in red are upregulated by 8 hours M1 activation in both WT and M-BKO macrophages. Genes that are differentially regulated in these two genotypes are displayed in heat maps on the right. F.C., fold change. N = 3 biological replicates. BCAAs, branch chain amino acids; Keto AAs, ketogenic amino acids; Cic, mitochondrial citrate carrier. (B) Relative expression of differentially regulated genes identified by RNA-seq and validated by qPCR in a 24-hr time course of M1 activation. N = 3 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-BKO across the time course. (C) Hif-1α protein levels in control or 6-hr M1-activated macrophages with or without co-treatment of the neutral amino-acid transport inhibitor 2-amino-2-norbornanecarboxylic acid (BCH, 10 mM). (D) Gene expression in control or 6-hr M1-activated macrophages with or without co-treatment of 10 mM BCH and/or the complex II inhibitor dimethyl malonate (DMM, 10 mM) determined by qPCR. N = 3 biological replicates, statistical analysis was performed using Student’s T test. Data are presented as mean ± S.E.M. *, p<0.05. Cell culture experiments were repeated at least twice.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Functional annotation clustering by biological process and Venn diagram of genes identified by RNA-seq that are mutually induced (2379 genes, left) or suppressed (2644 genes, right) by 8-h M1 activation in WT and M-BKO macrophages. N = 3 biological replicates. F.C., fold change. (B) Enriched biological processes associated with genes that are differentially expressed in M1-activated WT and M-BKO macrophages. (C) Relative expression of the neutral amino-acid transporter Slc7a8 (Lat2) in WT and myeloid Hif1a knockout (M-HKO) macrophages as determined by qPCR. WT samples were from Figure 5B. N = 3 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-HKO across the time course. (D) Determination of glutamine utilization by extracellular flux analysis. OCR was measured before and after LPS injection (final concentration 1 μg/mL), and the assay medium contained 5 mM glutamine in minimal DMEM with 2% dialyzed FBS, pH 7.4. N = 5 biological replicates, statistical analysis was performed using two-way ANOVA for WT vs M-BKO and for WT or M-BKO vs M-BKO cells co-treated with the neutral amino-acid transport inhibitor 2-amino-2-norbornanecarboxylic acid (BCH, 10 mM) across the time course. Data are presented as mean ± S.E.M. *, p<0.05. Cell culture experiments were repeated at least twice.

Direct comparison between M1-stimulated WT and M-BKO macrophages identified 419 genes that are more highly expressed in M1-activated M-BKO macrophages (FDR < 0.05, p<0.05, Figure 5—figure supplement 1B and Figure 5—source data 1). Most-enriched categories included stress and inflammatory responses that contained Il1b and other Hif-1α target genes, such as S100a8/S100a9 (Grebhardt et al., 2012). Other top enriched pathways were protein catabolism and amino-acid transport. These pathways included genes encoding plasma membrane amino-acid transporters (e.g., Slc7a2, Slc7a8, Slc7a11, Slc38a2 and Slc38a7) as well as ubiquitin-activating, -conjugating and -ligating enzymes that target proteins for proteasomal degradation (e.g., ubiquitin-like modifier-activating enzyme 6 [Uba6], ubiquitin conjugating enzymes [Ube2q2 and Ube2e3], ring finger proteins [Rnf12, Rnf56, Rnf128, and Rnf171], cullin 3 [Cul3] and Cul5, and ubiquitin protein ligase e3a [Ube3a]) (Figure 5A–B). The expression of enzymes that are involved in the breakdown of branched-chain amino acids was also higher in M1-activated M-BKO cells, including branched-chain keto acid dehydrogenase E1 subunit beta (Bckdhb) and methylmalonate semialdehyde dehydrogenase (Mmsdh). These results are consistent with the increased amino-acid catabolism that was observed in metabolite assays (Figure 3A). Interestingly, certain genes described above, notably Slc7a8, appeared to be counter-regulated by Hif-1α, as their induction by M1 stimulation was blunted in M-HKO macrophages (Figure 5—figure supplement 1C).

Slc7a8, also called L-type amino-acid transporter 2 (Lat2), transports neutral amino acids that could be converted to succinate and could potentially contribute to Hif-1α protein stabilization. In line with increased amino acid-metabolism, extracellular flux analysis showed that M-BKO macrophages showed enhanced glutamine utilization compared to WT cells, which was blocked by 2-amino-bicyclo-(2,2,1)-heptane-2-carboxylate (BCH), an L-type amino-acid transporter inhibitor (Christensen et al., 1969; Segawa et al., 1999; Figure 5—figure supplement 1D). BCH decreased and normalized levels of Hif-1α protein between WT and M-BKO macrophages (Figure 5C). In addition, treatment with either BCH or DMM suppressed the expression of Il1b, Slc7a8 and Slc7a11 induced by M1 stimulation (Figure 5D). The combination of BCH and DMM did not exert a greater effect over that of DMM alone. Thus, amino-acid metabolism is upregulated in response to dysregulated energy metabolism in M-BKO macrophages, which contributes to increased oxidative stress and Hif-1α activation.

### Macrophage Bmal1 gene deletion promotes an immune-suppressive tumor-associated macrophage phenotype and enhances tumor growth

It has been suggested that myeloid-specific Bmal1 deletion disrupts diurnal monocyte trafficking, thereby increasing sepsis-induced systemic inflammation and mortality (Nguyen et al., 2013). Our results suggest that the cell-autonomous function of Bmal1 on macrophage metabolism and Hif-1α activation may contribute to the reported phenotype. Hif-1α regulates the polarization of M1 and tumor-associated macrophages, both of which are under energetically challenged conditions. We sought to determine whether Bmal1–Hif-1α crosstalk plays a role in modulating TAM activation through a mechanism similar to that in M1 stimulation. Treatment of macrophages with conditioned medium from primary B16-F10 tumors (T-CM) increased the expression of both Bmal1 mRNA and Bmal1 protein (Figure 6A). When compared to WT macrophages, M-BKO macrophages showed enhanced mROS production and Hif-1α protein induced by T-CM (Figure 6B–C). Tracking with Hif-1α stabilization, aerobic glycolysis was upregulated by T-CM pretreatment in WT and to a greater extent in M-BKO macrophages (Figure 6D). T-CM elicited an energetic stress gene expression signature resembling that of M1 stimulation, which included upregulation of amino acid metabolism (Arg1, Slc7a8 and Bckdhb) and oxidative stress (Slc7a11 and Nqo1) pathways in WT macrophages that were further induced by M-BKO (Figure 6E).

![Figure 6.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig6-v2.jpg)

**Figure 6.:** (A) Bmal1 gene expression (left panel) and protein levels (right panel) in WT macrophages treated with control medium or increasing doses of B16-F10 tumor-conditioned medium (T-CM, diluted 1:3 or 1:1 with control medium) for 8 hr. N = 3 biological replicates for qPCR, statistical analysis was performed using Student’s T test. (B) Measurement of mROS using MitoSox Red (mean fluorescent intensity, MFI) in mitochondria from macrophages treated with control medium or T-CM diluted 1:1 with control medium for 1 hr. N = 3 biological replicates, statistical analysis was performed using Student’s T test. (C) Hif-1α protein levels in WT and M-BKO macrophages treated with control medium, T-CM diluted 1:1 with control medium, or undiluted T-CM for 4 hr. (D) Glycolytic stress test in macrophages pretreated with control medium or T-CM diluted 1:1 with control medium for 4 hr. N = 5 biological replicates. Statistical analysis was performed using two-way ANOVA comparing T-CM-treated M-BKO with WT cells across the time course. (E) Relative expression of genes involved in amino-acid metabolism and oxidative stress response in macrophages treated with control medium or T-CM diluted 1:3 with control medium for 8 hr, as determined by qPCR. N = 3 biological replicates, statistical analysis was performed using Student’s T test. (F) Tumor volume in male (left) and female (right) WT and M-BKO mice. 300,000 B16-F10 cells were injected subcutaneously into the right flank. N = 18 (male) and 8 (female) mice, statistical analysis was performed using two-way ANOVA for WT vs M-BKO mice across the time course. (G) Gene expression for F4/80+ cells isolated from B16-F10 tumors or spleens of female mice 14 days after injection. Tissues from six mice per genotype were pooled into three groups for leukocyte isolation. Statistical analysis was performed using Student’s T test. Data are presented as mean ± S.E.M. *, p<0.05. Experiments were repeated at least twice.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Tumor volumes of B16-F10 subcutaneous allografts in 3-month-old female WT and M-BKO mice 14 days after tumor cell injection. Each mouse was injected with 500,000 B16-F10 cells in the right and left flanks, and tumors from each mouse were pooled for immune cell isolation and flow cytometry. N = 4 mice, with two tumors per mouse. (B, C) mROS production and glucose uptake by tumor-associated CD45+F4/80+ cells determined by flow cytometry (mean fluorescent intensities) of Mitosox Red and 2-NBDG staining, respectively. N = 4. Statistical analysis was performed using Student’s T test. Data are presented as mean ± S.E.M. *, p<0.05.

Subsequently, we employed a mouse model of melanoma through subcutaneous injection of B16-F10 melanoma cells to assess the impact of myeloid Bmal1 deletion on tumor growth. Tumor volume was increased in both male and female M-BKO mice compared to WT controls (Figure 6F). Furthermore, the expression of Arg1, Slc7a8 and Slc7a11 was upregulated in F4/80+ cells isolated from tumors but not spleens of M-BKO mice compared to WT animals (Figure 6G). Of note, the mRNA levels of Arg1, Slc7a8 and Slc7a11 were substantially higher in tumor than in splenic F4/80+ cells. Flow cytometry analyses of F4/80+ cells from primary tumors stained with Mitosox Red and 2-deoxy-2-[(7-nitro-2,1,3-benzoxadiazol-4-yl)amino]-D-glucose (2-NBDG) were employed to assess mROS production and glucose uptake, respectively. M-BKO TAMs exhibited a trend towards increased mROS and significantly higher glucose uptake, compared to WT TAMs (Figure 6—figure supplement 1A-C). These results demonstrate that the metabolic reprogramming observed in T-CM-primed BMDM is shared by TAMs.

To confirm that macrophage Bmal1 modulates tumor growth cell-autonomously and to assess the effect of TAMs on anti-tumor immune response within the same host environment, we co-injected B16-F10 cells with either WT or M-BKO macrophages into the right or left flanks, respectively, of WT mice. Tumor growth rate was substantially higher when the tumor cells were co-injected with M-BKO macrophages than when co-injected with WT cells (Figure 7A). In concert, co-injection with M-BKO macrophages led to a reduction in the CD8+ T cell population among tumor-infiltrating CD45+ leukocytes, as well as to functionally primed CD8+ T and NK cells that expressed Ifn-γ protein following stimulation with phorbol myristate acetate and ionomycin ex vivo (Figure 7B). Similar results were obtained when the co-injections were performed in M-BKO mice (Figure 7—figure supplement 1A, B).

![Figure 7.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig7-v2.jpg)

**Figure 7.:** (A) Tumor volume in WT male mice co-injected with 500,000 B16-F10 cells and either 500,000 WT or M-BKO macrophages as indicated. N = 22 mice, statistical analysis was performed using two-way ANOVA to compare WT vs M-BKO macrophage co-injection across the time course. (B) Flow cytometric analysis of tumor-infiltrating CD8+ T cells (CD45+CD3+CD8a+ cells, left panel) and NK cells (CD45+CD3–NK1.1+ cells, right panel) stimulated ex vivo with phorbol 12-myristate 13-acetate and ionomycin for Ifn-γ co-staining. Tumors represented in panel (A) were pooled into three groups prior to isolation of infiltrating leukocytes for flow cytometry. Statistical analysis was performed using Student’s T test. (C) Tumor volume in WT male mice co-injected with 500,000 B16-F10 cells and either 500,000 WT or M-BKO macrophages, supplemented without or with dimethylmalonate (DMM, approximately 150 mg/kg body weight per day in mouse diet). N = 8 mice, statistical analysis was performed using two-way ANOVA to compare WT vs M-BKO macrophage co-injection on control diet, or to compare WT macrophage co-injection on the control diet vs WT or M-BKO macrophage co-injection on the DMM-supplemented diet across the time course. Data are presented as mean ± S.E.M. *, p<0.05. Experiments were repeated at least twice.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/54090/elife-54090-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Tumor volume in M-BKO male mice co-injected with 500,000 B16-F10 cells and either 500,000 WT or M-BKO macrophages as indicated. N = 6 mice, statistical analysis was performed using two-way ANOVA to compare WT vs M-BKO macrophage co-injection across the time course. (B) Flow cytometric analyses of tumor-infiltrating CD8+ T cells (CD45+CD3+CD8a+ cells, left panel) and NK cells (CD45+CD3–NK1.1+ cells, right panel) stimulated ex vivo with phorbol 12-myristate 13-acetate and ionomycin for Ifn-γ co-staining. Tumors that are represented in panel (A) were pooled into three groups prior to isolation of infiltrating leukocytes for flow cytometric analyses. Statistical analysis was performed using Student’s T test. Data are presented as mean ± S.E.M. *, p<0.05. (C) Hif-1α protein levels in WT macrophages treated with (from left to right) control medium or B16-F10 tumor-conditioned medium (T–CM) diluted 1:1 with control medium without or with co-treatment with 10 mM dimethyl malonate (DMM) for 4 hr. (D) Arg1 gene expression in WT macrophages treated as in panel (C) for 8 hr. N = 3 biological replicates. Statistical analysis was performed using Student’s T test. Experiments were repeated at least twice. (E) Schematic showing the working model for Bmal1–Hif-1α crosstalk in the regulation of macrophage bioenergetics and effector functions. Both M1 and tumor-associated macrophages share similar energetically stressed states. Bmal1 preserves mitochondrial oxidative metabolism while reducing oxidative stress to modulate Hif-1α activity and support proper effector functions. Deletion of Bmal1 in the macrophage leads to reliance on glycolytic metabolism and alternative fuel utilization, notably amino-acid metabolism, which further promotes mROS production and Hif-1α protein stabilization. Increased amino-acid utilization by M-BKO macrophages may lead to depletion of amino acids that are critical for lymphocyte activation and cytotoxic function, thereby suppressing anti-tumor immunity in the tumor microenvironment.

We next sought to address the importance of oxidative stress in TAM activation. Similar to M1 macrophages, DMM blocked Hif-1α protein accumulation and attenuated Arg1 upregulation in T-CM-treated macrophages (Figure 7—figure supplement 1C-D). Administering DMM (~150 mg/kg body/day) at the time of macrophage-tumor cell co-inoculation effectively suppressed melanoma tumor growth and normalized the difference in tumor promoting effects between WT and M-BKO macrophages (Figure 7C). These results reveal a unifying mechanism by which Bmal1 controls macrophage effector functions through bioenergetic regulation, and suggest that targeting oxidative stress may provide a means to modulate the anti-tumor activity of TAMs.

## Discussion

It has been reported that sepsis exerts a long-lasting effect on circadian rhythm alteration in mice (Marpegán et al., 2005; O'Callaghan et al., 2012). In the current study, we show that inflammatory stimulants, including Ifn-γ/LPS and tumor-derived factors, control the expression of the circadian master regulator Bmal1 in the macrophages. Our data further demonstrate that Bmal1 is an integral part of the metabolic regulatory network and modulates macrophage activation, in part through crosstalk with Hif-1α. The Bmal1–Hif-1α regulatory loop regulates the balance between oxidative and glycolytic metabolism in energetically stressed macrophages that have distinct effector functions. Bmal1 loss-of-function in M1-activated macrophages causes mitochondrial dysfunction, thereby potentiating mROS production and Hif-1α protein stabilization, which probably contributes to the increased sepsis-induced inflammatory damage reported for M-BKO mice (Nguyen et al., 2013). Within the tumor microenvironment, macrophage Bmal1 gene deletion leads to compromised anti-tumor immunity and accelerated tumor growth in a mouse melanoma model. Therefore, the Bmal1–Hif-1α nexus serves as a metabolic switch that may be targeted to control macrophage effector functions.

Much attention has been focused on how inflammatory stimuli disrupt mitochondrial metabolism as a means to generate signaling molecules, including TCA metabolites and mROS. The analysis of transcriptional modules that are involved in macrophage inflammatory response reveals a coordinated effort in the control of mitochondrial activity. The expression of several regulators of mitochondrial biogenesis (e.g., Pparg) is downregulated rapidly after M1 stimulation and rebounds after between 8–12 hr, when Bmal1 and Ppard expression is induced (Figure 1). Several lines of evidence indicate that Bmal1 plays a key role in restoring mitochondrial function and in modulating a Hif-1α-mediated inflammatory response. The expression of transcription factors that are known to control mitochondrial bioenergetics (i.e., Pparγ and Pparδ) is downregulated by M-BKO. Macrophages that are deficient in Bmal1 are unable to sustain mitochondrial function upon M1 stimulation and fail to recover from suppressed mitochondrial respiration 24 hr following acute LPS treatment. By contrast, Bmal1 gain-of-function in RAW 246.7 macrophages promotes oxidative metabolism. It is interesting to note that the dysregulated mitochondrial respiration phenotype of M-BKO macrophages occurs as early as 2 hr after M1 activation, whereas Bmal1 protein accumulation peaks at 12 hr. This early phase of regulation could be mediated by downstream pathways of the circadian regulatory network. RNA-seq analyses reveal that components of the molecular clock are induced by M1 (Figure 1—figure supplement 1A). Notably, Nr1d1/Nr1d2 have been shown to regulate macrophage inflammatory gene expression negatively (Lam et al., 2013) and promote mitochondrial function in skeletal muscle (Woldt et al., 2013). The induction of Nr1d2 by M1 was almost completely abolished in M-BKO macrophages (Figure 1D). In concert, the expression of Cx3cr1, a direct target suppressed by Nr1d1/Nr1d2 (Lam et al., 2013), is higher in M1-activated M-BKO macrophages than in WT cells (Figure 5—source data 1). This suppressive effect of Nr1d1/Nr1d2 may dampen the inflammatory damage to mitochondrial function at the initial stage of M1 activation. Another potential mechanism is through enhanced Hif-1α activity by M-BKO, which is evident after 4 hr of M1 activation (Figure 4A). Hif-1α suppresses mitochondrial respiration through multiple mechanisms (Thomas and Ashcroft, 2019). For instance, it regulates the glycolytic program favoring lactate production and controls the expression of Bnip3 to promote mitophagy. M-BKO macrophages exhibit a higher lactate production rate 4 hr after M1 stimulation (Figure 3D) and this phenotype was observed as early as 2 hr after M1 stimulation (data not shown). Bnip3 protein accumulation is also increased, although appreciable amounts of Bnip3 protein could only be detected at 8 hr after M1 treatment (Figure 2—figure supplement 1A). Bmal1 is best known for its role in circadian regulation and has been shown to control rhythmic monocyte recruitment, which plays a key role in the immune response against pathogens and in limiting infection-associated inflammatory damage (Nguyen et al., 2013). Our data suggest that LPS or M1 stimulation could ‘reset the clock’ by inducing/resynchronizing the expression of Bmal1. In this context, Bmal1 may regulate energy metabolism to support diurnal monocyte trafficking, and may control the timing of glycolytic to oxidative metabolism transition during M1 activation that dictates the extent of Hif-1α activation and the associated inflammatory response.

Both Bmal1 and Hif-1α belong to the basic helix-loop-helix (bHLH) transcription factor family and have similar domain structures. However, they appear to regulate opposing metabolic programs, with Hif-1α serving as a master regulator of aerobic glycolysis and Bmal1 as a positive regulator of oxidative metabolism (Figure 7—figure supplement 1E). The crosstalk between these two bHLH transcription factors is in part mediated by succinate and SDH/complex II-facilitated mROS production. Succinate is one of the entry points for anerplerosis that attempts to replenish the TCA cycle metabolites that are depleted by disruption of mitochondrial oxidative metabolism. Increased protein or amino-acid catabolism provides a source of anerplerotic reactions. Succinate accumulation and the subsequent oxidation to fumarate, however, generate mROS, which stabilize Hif-1α protein and thus drive aerobic glycolysis. Our data suggest that amino-acid metabolism appears to be down- and upregulated by Bmal1 and Hif-1α, respectively, as demonstrated by the regulation of Arg1 and Slc7a8 gene expression. As described above, Hif-1α has also been shown to regulate Bnip3-mediated mitophagy that reduces mitochondrial oxidative capacity (Zhang et al., 2008). Therefore, Bmal1-controlled mitochondrial metabolism provides a break to this feedforward cycle that limits inflammatory damage. In line with this, previous work has demonstrated that myeloid Bmal1 knockout mice have reduced survival rate upon L. monocytogenes infection (Nguyen et al., 2013). These observations indicate a tightly regulated metabolic program in the macrophage that executes effector functions and places Bmal1-regulated mitochondrial metabolism at the center of an orderly and balanced immune response.

Despite being characterized as M2-like, TAMs share several common features with M1-activated macrophages: both function under nutrient-restricted conditions and Hif-1α is required for their activation. Previous studies implicate a glycolytic preference for TAMs in breast, thyroid, and pancreatic cancer (Arts et al., 2016; Liu et al., 2017; Penny et al., 2016). Our data confirm that T-CM treatment enhances glycolysis in the macrophage accompanied by increased Hif-1α protein (Figure 6C, D). Arg1, originally defined as an M2 marker, is a bona fide target of Hif-1α that is upregulated in TAMs and M1 macrophages. Arg1 is involved in the urea cycle that detoxifies ammonia, and its induction supports the upregulation of amino-acid catabolism. M-BKO macrophages show increased mROS, glycolytic metabolism, Hif-1α stabilization and upregulation of Arg1 and Slc7a8 upon treatment with T-CM. Dysregulated amino-acid metabolism has been shown to impact immune cell activation. Arginine depletion impairs lymphocyte function, as arginine is required for effector T cell and NK cell proliferation and maintenance (Geiger et al., 2016; Lamas et al., 2012; Steggerda et al., 2017). Slc7a8 transports neutral amino acids, including branched-chain amino acids that are essential for lymphocyte activation and cytotoxic function (Sinclair et al., 2013; Tsukishiro et al., 2000). Therefore, the increased amino-acid utilization by M-BKO macrophages may contribute to the observed reduction in populations of Ifn-γ-producing CD8+ T and NK cells in tumor-infiltrating CD45+ leukocytes (Figure 7B and Figure 7—figure supplement 1B). The fact that amino-acid or protein metabolism and oxidative stress genes (Arg1, Slc7a8 and Slc7a11) are upregulated in TAMs, compared to splenic macrophages (Figure 6G), supports the notion that energetic stress is also a key determinant of TAM polarization. As a proof-of-principle approach, we show that DMM treatment blocks T-CM induced Hif-1α protein stabilization in vitro and suppresses tumor growth in vivo. Thus, M1 macrophages opt for an inefficient way to produce ATP, whereas TAMs are limited in energy allocations. Both of these processes result in an energetically challenged state in which Bmal1–Hif-1α crosstalk controls the metabolic adaptation that shapes macrophage polarization. Future studies investigating mechanisms that harness this energetic stress may identify means to modulate immune cell functions effectively.

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
      <td>Strain, strain background (Mus musculus)</td>
      <td>B6.129S4(CG)-Arntltm1Weit/J</td>
      <td>The Jackson Laboratory</td>
      <td>JAX: 007668</td>
      <td>Carry loxp sites flanking exon 8 of the Bmal1 gene</td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>B6.129-Hif1atm3Rsjo/J</td>
      <td>The Jackson Laboratory</td>
      <td>JAX: 007561</td>
      <td>Carry loxp sites flanking exon 2 of the Hif1a gene</td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>B6.129P2-Lyz2tm1(cre)lfo/J</td>
      <td>The Jackson Laboratory</td>
      <td>JAX: 004781</td>
      <td>Myeloid-specific Cre recombinase expression</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-Bmal1 (clone B-1)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat# sc365645; RRID:AB_10841724</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-Hif-1α</td>
      <td>Novus Biologicals</td>
      <td>Cat# NB100-449; RRID:AB_10001045</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-Bnip3 (clone EPR4034)</td>
      <td>Abcam</td>
      <td>Cat# ab109362; RRID:AB_10864714</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-β-tubulin</td>
      <td>Cell Signaling Technology</td>
      <td>Cat# 2146; RRID:AB_2210545</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-β-Actin (clone 13E5)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat# 4970; RRID:AB_2223172</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat monoclonal anti-CD45 (clone 30-F11), PerCP/Cy5.5-conjugated</td>
      <td>Biolegend</td>
      <td>Cat# 103132; RRID:AB_893340</td>
      <td>Flow cytometry (1 μL per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Armenian hamster monoclonal anti-CD3ε (clone 145–2 C11), PE/Cy7-conjugated</td>
      <td>Biolegend</td>
      <td>Cat# 100320; RRID:AB_312685</td>
      <td>Flow cytometry (2.5 μL per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat monoclonal anti-CD8a (clone 53–6.7), Alexa Fluor 700-conjugated</td>
      <td>Biolegend</td>
      <td>Cat# 100730; RRID:AB_493703</td>
      <td>Flow cytometry (0.5 μL per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-NK1.1 (clone PK136), APC-conjugated</td>
      <td>Biolegend</td>
      <td>Cat# 108710</td>
      <td>Flow cytometry (5 μL per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat monoclonal anti-F4/80 (clone BM8), Alexa Fluor 488-conjugated</td>
      <td>Biolegend</td>
      <td>Cat# 123120; RRID:AB_893479</td>
      <td>Flow cytometry (5 μL per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat monoclonal anti-F4/80 (clone BM8), APC-conjugated</td>
      <td>Biolegend</td>
      <td>Cat# 123115; RRID:AB_893493</td>
      <td>Flow cytometry (2.5 μL per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat monoclonal anti-Ifn-γ (clone XMG1.2), PE-conjugated</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# 12-7311-81, RRID:AB_466192</td>
      <td>Flow cytometry (1 μL per test)</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Recombinant murine interferon-γ</td>
      <td>Peprotech</td>
      <td>Cat# 315–05</td>
      <td>Used 10 ng/mL final concentration</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Recombinant murine interleukin-4</td>
      <td>Peprotech</td>
      <td>Cat# 214–14</td>
      <td>Used 10 ng/mL final concentration</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>36b4_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>AGATGCAGCAGATCCGCAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>36b4_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GTTCTTGCCCATCAGCACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Arg1_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CGTAGACCCTGGGGAACACTAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Arg1_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>TCCATCACCTTGCCAATCCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Bckdhb_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>TGGGGCTCTCTACCATTCTCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Bckdhb_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GGGGTATTACCACCTTGATCCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Bmal1_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>AGGATCAAGAATGCAAGGGAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Bmal1_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>TGAAACTGTTCATTTTGTCCCGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cMyc_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CAGCGACTCTGAAGAAGAGCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cMyc_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GACCTCTTGGCAGGGGTTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Cry1_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CACTGGTTCCGAAAGGGACTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Cry1_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CTGAAGCAAAAATCGCCACCT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Gclc_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CATCCTCCAGTTCCTGCACA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Gclc_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>ATGTACTCCACCTCGTCACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Hif1a_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GAACGAGAAGAAAAATAGGATGAGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Hif1a_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>ACTCTTTGCTTCGCCGAGAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Hmox1_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CAGAGCCGTCTCGAGCATAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Hmox1_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CAAATCCTGGGGCATGCTGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Il1b_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>AGCTTCAGGCAGGCAGTATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Il1b_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>AAGGTCCACGGGAAAGACAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Ldha_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GCGTCTCCCTGAAGTCTCTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Ldha_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GCCCAGGATGTGTAACCTTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mgl2_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>ccttgcgtttgtcaaaacatgac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mgl2_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>ctgaggcttatggaactgaggc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mmsdh_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GAGGCCTTCAGGTGGTTGAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mmsdh_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GATAGATGGCATGGTCTCTCCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Nfe2l2_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GGTTGCCCACATTCCCAAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Nfe2l2_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GCAAGCGACTCATGGTCATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Nfkb1_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CCTGCTTCTGGAGGGTGATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Nfkb1_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GCCGCTATATGCAGAGGTGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Nqo1_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>TCTCTGGCCGATTCAGAGTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Nqo1_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>TGCTGTAAACCAGTTGAGGTTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Nr1d2_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>TCATGAGGATGAACAGGAACCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Nr1d2_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CGGCCAAATCGAACAGCATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Ppard_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CAGCCTCAACATGGAATGTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Ppard_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>TCCGATCGCACTTCTCATAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Pparg_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CAGGAGCCTGTGAGACCAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Pparg_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>ACCGCTTCTTTCAAATCTTGTCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Slc7a2_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CCCGGGATGGCTTACTGTTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Slc7a2_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>AGGCCATCACAGCAGAAATGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Slc7a8_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GAACCACCCGGGTTCTGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Slc7a8_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>TGATGTTCCCTACAATGATACCACA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Slc7a11_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>ATCTCCCCCAAGGGCATACT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Slc7a11_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>GCATAGGACAGGGCTCCAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Stat3_F</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>TGGCAGTTCTCGTCCAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Stat3_R</td>
      <td>This paper</td>
      <td>qPCR primer</td>
      <td>CCAGCCATGTTTTCTTTGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Bmal1_F</td>
      <td>This paper</td>
      <td>Cloning primers</td>
      <td>GGCGAATTCGCGGACCAGAGAATGGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Bmal1_R</td>
      <td>This paper</td>
      <td>Cloning primers</td>
      <td>GGGCTCGAGCTACAGCGGCCATGGCAA</td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>RAW264.7 macrophages</td>
      <td>ATCC</td>
      <td>qPCR primer</td>
      <td>TIB-71</td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>B16-F10 melanoma cells</td>
      <td>ATCC</td>
      <td>qPCR primer</td>
      <td>CRL-6475</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pBABE-puro retroviral expression vector (plasmid)</td>
      <td>Addgene</td>
      <td>Plasmid #1764</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pBABE-Bmal1 (plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>For stable overexpression of mouse Bmal1</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Lipopolysaccharides from Escherichia coli K-235</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# L2143</td>
      <td>Final concentration used varied as indicated</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dimethyl malonate</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# 136441; CAS: 108-59-8</td>
      <td>Used 10 mM final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium succinate dibasic</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# 14160; CAS: 150-90-3</td>
      <td>Used 10 mM final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>N-acetyl-L-cysteine</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# A9165; CAS: 616-91-1</td>
      <td>Final concentration used varied as indicated.</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>2-deoxy-D-glucose</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# D8375; CAS: 154-17-6</td>
      <td>Used 50 mM final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Quant-iT ribogreen RNA reagent</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# R11491</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Mitotracker green FM</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# M7514 CAS: 201860-17-5</td>
      <td>Used 100 nM final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Mitosox red superoxide indicator</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# M36008</td>
      <td>Used 5 μM final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>2-NBDG</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# N13195</td>
      <td>Used 10 μM final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Fixable viability dye eFluor 455uv</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# 65-868-14</td>
      <td>Flow cytometry (0.5 μL per test)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Fixable viability dye eFluor 506</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# 65-0866-14</td>
      <td>Flow cytometry (0.5 μL per test)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Oligomycin</td>
      <td>Abcam</td>
      <td>Cat# ab141829; CAS: 1404-19-9</td>
      <td>Used 2 μM final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Rotenone</td>
      <td>Abcam</td>
      <td>Cat# ab143145 CAS: 83-79-4</td>
      <td>Used 1 μM final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Antimycin A</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# A8674; CAS: 1397-94-0</td>
      <td>Used 1 μM final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Carbonyl cyanide-4-(trifluoromethoxy)phenylhydrazone (FCCP)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat# sc203578 CAS: 370-86-5</td>
      <td>Used 0.5 μM final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Phorbol 12-myristate 13-acetate (PMA)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# P8139; CAS: 16561-29-8</td>
      <td>Used 20 ng/mL final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ionomycin calcium salt from Streptomyces conglobatus</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# I0634; CAS: 56092-82-1</td>
      <td>Used 1 μg/mL final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Brefeldin A</td>
      <td>Cell Signaling Technology</td>
      <td>Cat# 9972S; CAS: 20350-15-6</td>
      <td>Used 10 μg/mL final concentration</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>BCA protein assay kit</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# 23227</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Seahorse XF24 FluxPak</td>
      <td>Agilent</td>
      <td>Cat# 102070–00</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Foxp3/Transcription factor staining buffer set</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# 00-5523-00</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TruSeq stranded mRNA library prep kit</td>
      <td>Illumina</td>
      <td>Cat# RS-122–2101</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dynabeads sheep anti-rat IgG</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat # 11035</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STRING</td>
      <td>von Mering, 2004</td>
      <td>https://string-db.org/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DAVID</td>
      <td>Huang et al., 2009</td>
      <td>https://david-d.ncifcrf.gov/</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Thioglycollate medium</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# T9032</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Bovine serum albumin, fatty acid free</td>
      <td>Gemini Bio-Products</td>
      <td>Cat# 700–107P</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Collagen I protein, rat tail</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# A1048301</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Collagenase type IV</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# 17104019</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Recombinant DNase I, RNase-free</td>
      <td>Affymetrix</td>
      <td>Cat# 78411</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Reagents

Lipopolysaccharide (LPS) from Escherichia coli strain K-235 (L2143) was from Sigma-Aldrich. Recombinant murine Ifn-γ (315-05) and Il-4 (214–14) were from Peprotech. The ETC complex II inhibitor dimethyl malonate (136441) and the L-type amino acid transport inhibitor 2-amino-2-norbornanecarboxylic acid, or BCH, (A7902) were from Sigma-Aldrich.

### Animals

All animal studies were approved by the Harvard Medical Area Standing Committee on Animal Research. Animals were housed in a pathogen-free barrier facility at the Harvard T.H. Chan School of Public Health. Bmal1fl/fl (stock # 007668), Hif1a fl/fl (stock # 007561), and Lyz2-Cre (stock # 004781) mice in the C57BL/6J background were obtained from Jackson laboratories and were originally contributed by Drs Charles Weitz, Dmitriy Lukashev, and Irmgard Foerster, respectively. Floxed mice were crossed with Lyz2-Cre mice to generate myeloid-specific Bmal1 and Hif1a knockout mice. Myeloid-specific Bmal1 knockout mice were crossed with Hif1afl/fl mice, and the resulting heterozygotes were crossed to generate myeloid-specific Bmal1 and Hif1a double-knockout mice. The genotypes were validated by both DNA genotyping and mRNA expression. Gender- and age-matched mice of between 8–24 weeks of age were used for experiments. Similar results were obtained from male and female mice.

### Bone marrow-derived macrophage (BMDM) differentiation and cell culture

Macrophages were differentiated from primary mouse bone marrow from the femur and tibia using differentiation medium containing 30% L929-conditioned medium, 10% FBS, and pen-strep solution in low-glucose DMEM in 15-cm Petri dishes. Media were changed every three days, and cells were lifted, counted, and plated in final format in tissue culture plates on days 7–8 of differentiation. For experiments, primary macrophages were maintained in low glucose DMEM containing 10% FBS and pen-strep. For M1 activation, macrophages were primed with 10 ng/mL Ifn-γ for 10–12 hr and subsequently stimulated with 10 ng/mL of E. coli LPS at the start of each experiment. Macrophages with Ifn-γ priming but without LPS were used as the control for M1 activation.

### Peritoneal and splenic macrophage isolation and culture

For peritoneal macrophage isolation, mice aged 2–4 months were i.p. injected with 3 mL of 3% thioglycollate (Sigma-Aldrich, T9032). After 3 days, mice were euthanized, and peritoneal cells were recovered by lavage. For isolation of splenic macrophages, mice were euthanized and spleens were dissected and mashed in growth medium (high glucose DMEM with 10% FBS) and passed through a 70 μm strainer. Cells were pelleted and resuspended in red blood cell lysis buffer. Monocytes and lymphocytes were recovered using Ficoll-Paque Plus density gradient medium (GE Healthcare Life Sciences, 17144002) according to the manufacturer’s instructions, and suspension cells (lymphocytes) were washed away prior to experiments.

### LPS synchronization of Bmal1 expression

To synchronize Bmal1 gene and protein expression with LPS (or LPS shock), BMDMs or mouse embryonic fibroblasts (MEFs) were given fresh culture medium with 2% FBS and 100 ng/mL LPS for 1 hr and then given fresh medium with 2% FBS without LPS. Bmal1 expression was tracked following LPS removal. For M1 or LPS induction of Bmal1 expression, cells were primed with or without 10 ng/mL Ifn-γ for 10–12 hr in DMEM, 10% FBS and subsequently stimulated with 10 ng/mL of LPS without changing the medium (time zero).

### Cell lines

MEFs were isolated from WT C57/BL6J mouse embryos and immortalized using the 3T3 protocol as previously described (Xu, 2005). For experiments, immortalized MEFs were maintained in growth medium containing high glucose DMEM, 10% FBS. RAW264.7 mouse macrophages (TIB-71) and B16-F10 mouse melanoma cells (CRL-6475) were purchased from ATCC and experiments were conducted using early passages. Mycoplasma contamination was monitored using PCR-based methods. For generation of stable Bmal1-overexpressing RAW264.7 cells, the Bmal1 coding sequence was cloned from mouse embryonic cDNA (forward primer: 5′ GGCGAATTCGCGGACCAGAGAATGGAC 3′; reverse primer: 5′ GGGCTCGAGCTACAGCGGCCATGGCAA 3′) and subcloned into the pBABE retroviral expression vector (Addgene, 1764). Retroviral vectors were transfected into Phoenix packaging cells, followed by collection of supernatants containing retroviruses. RAW264.7 macrophages were incubated with retroviral supernatants with 4 µg/mL polybrene, and infected cells were selected with 4 µg/mL puromycin. Control cells were transduced with the empty pBABE vector.

### Syngeneic tumor model and tumor measurement

Male and female WT and M-BKO mice aged 10–12 weeks were subcutaneously injected in the right flank with 300,000 B16-F10 mouse melanoma cells. For co-injection experiments, 500,000 B16-F10 cells were mixed with either 500,000 WT or M-BKO BMDMs (differentiation for 6 day) in the right and left flanks, respectively. Tumor dimensions were measured every two days by caliper after all mice had palpable tumors, and tumor volume was calculated as LxWxWx0.52 as previously described (Colegio et al., 2014). For DMM treatment, mice were switched to a soft pellet, high fat diet (Bio-Serv, F3282) so that DMM could be mixed with the diet using a blender. The tumor growth rate was slower on high fat diet (Figure 7C) compared to normal chow (Figure 7A).

### RNA sequencing

RNA-seq was performed on RNA from three biological replicates per treatment. Sequencing and raw data processing were conducted at the Institute of Molecular Biology (IMB) Genomics Core and IMB Bioinformatics Service Core, respectively, at Academia Sinica (Taipei, Taiwan, ROC). In brief, RNA was quantified using the Quant-iT ribogreen RNA reagent (ThermoFisher, R11491), and RNA quality was determined using a Bioanalyzer 2100 (Agilent; RIN > 8, OD 260/280 and OD 260/230 > 1.8). RNA libraries were prepared using the TruSeq Stranded mRNA Library Preparation Kit (Illumina, RS-122–2101). Sequencing was analyzed with an Illumina NextSeq 500 instrument. Raw data were analyzed using the CLC Genomics Workbench. Raw sequencing reads were trimmed by removing adapter sequences, low-quality sequences (Phred quality score of <20) and sequences >25 bp in length. The trimmed reads were then mapped to the mouse genome assembly (mm10) from University of California, Santa Cruz, using the following parameters: mismatches = 2, minimum fraction length = 0.9, minimum fraction similarity = 0.9, and maximum hits per read = 5. Gene expression was determined by the number of transcripts per kilobase million. Functional annotation clustering of differentially regulated genes was done using DAVID (https://david-d.ncifcrf.gov/), and the interaction maps of transcriptional regulators that were induced or repressed by M1 activation that are shown in Figure 1—figure supplement 1A were generated using STRING (https://string-db.org/). Significantly changed genes were determined by p<0.05 and FDR <0.05. Data have been deposited in GEO under the accession number GSE148510.

### qPCR

Relative gene expression was determined by real-time qPCR with SYBR Green. The expression of the ribosomal subunit 36b4 (Rplp0) was used as an internal control to normalize expression data. Primer information is described in the 'Key resources table'.

### Western blot

Standard Tris-Glycine SDS-PAGEs were run and transferred to PVDF membranes by wet transfer. Membranes were incubated with primary antibodies in TBST buffer with 1% BSA overnight. ECL signal was imaged using a BioRad ChemiDoc XRS+ imaging system. The antibody for Bmal1 (sc365645) was from Santa Cruz. The antibody for Hif-1α (NB100-449) was from Novus Biologicals. The antibodies for β-tubulin (2146) and β-actin (4970) were from Cell Signaling Technology.

### Extracellular flux analyses

Extracellular flux experiments were done using a Seahorse XF24 analyzer (Agilent) and FluxPaks (Agilent, 100850–001). 200,000 BMDMs, splenic/peritoneal macrophages or RAW264.7 cells were seeded into Seahorse XF24 plates for extracellular flux experiments. Minimal DMEM (pH 7.4) without phenol red and containing energy substrates as indicated was used as the assay medium. 2% dialyzed FBS was added to media for experiments in which LPS was injected during the assay to enhance responsiveness to LPS. Assay measurements were normalized to total protein content.

### Glucose uptake assay

BMDMs were plated at a density of 1 million cells per well in 12-well plates and stimulated as indicated. Cells were then washed with Krebs-Ringer bicarbonate HEPES (KRBH) buffer and then given 400 μL with KRBH buffer loaded with 0.8 μCi/well [3H]−2-deoxyglucose (PerkinElmer, NET549A001MC) and 0.5 mM unlabeled 2-deoxyglucose and incubated at 37°C for 30 min. 10 μL of 1.5 mM Cytochalasin B (Cayman Chemical, 11328) was then added to stop glucose uptake. 400 μL of lysate was used to measure levels of [3H]−2-deoxyglucose by a scintillation counter, and the remaining lysate was used to measure total protein content for normalization.

### Measurement of lactic acid secretion

Lactic acid was measured in the supernatants of BMDMs using the Biovision Lactate Colorimetric Kit (K627) according to the manufacturer’s protocol. Readings were normalized to total cellular protein content.

### Mitochondrial isolation

Mitochondria were isolated from primary BMDMs by differential centrifugation. In brief, cells were resuspended in 500 μL of ice-cold mitochondrial isolation buffer consisting of 70 mM sucrose, 50 mM Tris, 50 mM KCl, 10 mM EDTA, and 0.2% fatty-acid free BSA (pH 7.2) and then extruded through 29-gauge syringes 20 times. Lysates were spun at 800 g to pellet nuclei, and supernatants were spun at 8000 g to isolate mitochondria. Pelleted mitochondria were washed once more with 500 μL of mitochondria isolation buffer. Total mitochondrial protein content was determined by BCA assay.

### ETC activity assays in isolated mitochondria

The activities of ETC complexes I–IV were measured in isolated mitochondria using colorimetric assays as previously described (Spinazzi et al., 2012) with modifications. In brief, 15 μg of mitochondria were loaded per reaction for complexes III and IV, and 30 and 50 μg were used for complexes II and I, respectively. Complex I activity was determined by the decrease in absorbance at 340 nm corresponding to reduction of ubiquinone by electrons from NADH. Complex II activity was determined by the decrease in absorbance at 600 nm corresponding to reduction of decylubiquinone by electrons from succinate. Complex III activity was determined by the increase in absorbance at 550 nm corresponding to reduction of cytochrome C. Complex IV activity was determined by decrease in absorbance at 550 nm corresponding to oxidation of cytochrome C.

### Flow cytometry

For flow cytometry, BMDMs were seeded into low-attachment plates for the indicated treatments and resuspended by pipetting. Mitochondrial content in BMDMs was determined by flow cytometry of live cells stained with 100 μM Mitotracker Green FM (ThermoFisher, M7514) according to the manufacturer’s instructions.

For flow cytometry of tumor-infiltrating lymphocytes, cells were stimulated ex vivo with 20 ng/mL phorbol 12-myristate 13-acetate (PM), (Sigma-Aldrich, P8139) and 1 μg/mL ionomycin (Sigma-Aldrich, I0634) for 4 hr and co-treated with brefeldin A (Cell Signaling Technology, 9972) to inhibit cytokine release. Cells were stained with the fixable viability dye (eFluor 455uv [ThermoFisher, 65-868-14] or eFluor 506 [ThermoFisher, 65-0866-14]) for 20 min at 4°C in PBS, washed, and incubated with antibodies against the indicated surface antigens for 30 min at 4°C in fluorescence-activated cell sorting (FACS) buffer (2% FBS and 1 mM EDTA in PBS). Cells were then washed twice and fixed with 2% paraformaldehyde for 1 hr at 4°C, and resuspended and stored in FACS buffer prior to downstream analysis. Immediately before flow cytometric analysis, cells were permeabilized for intracellular staining using the Foxp3/Transcription factor staining buffer set (ThermoFisher, 00-5523-00) according to the manufacturer’s instructions. Of viable cells, CD8+ T cells were identified as CD45+CD3+CD8a+ cells and NK cells were identified by CD45+ CD3– NK1.1+ staining. To determine glucose uptake and mROS production by primary TAMs, live cells were stained with either 5 μM Mitosox Red (ThermoFisher, M36008) or 10 μM 2-NBDG (ThermoFisher, N13195) for 20 min in RPMI 1640 medium at 37°C, then washed and resuspended in FACS buffer for flow cytometry. F480+ cells were gated from live CD45+ cells to measure the mean fluorescent intensities of Mitosox or 2-NBDG. Antibodies for PerCp/Cy5.5-conjugated CD45 (103132), PE/Cy7-conjugated CD3e (100320), Alexa Fluor 700-conjugated CD8a (100730), APC-conjugated NK1.1 (108710) Alexa 488-conjugated F480 (123120) and APC-conjugated F480 (123115) were from Biolegend. The antibody for PE-conjugated Ifn-γ (12-7311-81) was from ThermoFisher Scientific.

To measure ROS production by isolated mitochondria, 15 μg of mitochondria were resuspended in 500 μL mitochondrial isolation buffer containing 5 μM MitoSox Red and 100 μM MitoTracker Green FM with or without 10 mM sodium succinate. Mitochondria were incubated for 20 min at room temperature, washed with isolation buffer, and resuspended for flow cytometry. Mitochondria were identified by side scatter and positive MitoTracker Green staining for measurement of mean MitoSox Red intensity per population.

### Steady-state metabolomics

Untargeted metabolomics analysis using GC-TOF mass spectrometry was conducted by the West Coast Metabolomics Center at UC Davis. In brief, 10 million cells were lifted, pelleted, and washed twice with PBS for each replicate. Cell lysates were homogenized by metal bead beating, and metabolites were extracted using 80% methanol. Following extraction, cell pellets were solubilized using Tris-HCl urea buffer (pH 8.0) containing 1% SDS to measure cellular protein content for each sample. All metabolite readings were normalized to total protein content.

### Collection of tumor-conditioned medium

Mice bearing subcutaneous B16-F10 tumors were sacrificed 20 days after injection with 500,000 cells. Tumors were dissected and weighed. Tumors were minced in growth medium containing 10% dialyzed FBS in high-glucose DMEM (5 mL per gram of tissue) and incubated at 37°C for 2 hr. Conditioned medium was collected and filtered through a 100 μm strainer followed by three spins at 1,000 rpm to pellet and remove residual cells and debris from the medium.

### Isolation of tumor-infiltrating immune cells

Subcutaneous mouse tumors were dissected, weighed, and then placed in six-well plates with growth medium (RPMI, 5% FBS) and minced. Minced tissues were combined into three groups per genotype, spun down in 50 mL conical tubes, and resuspended in 20 mL digestion buffer (0.5 mg/mL collagenase IV, 0.1 mg/mL DNase I in HBSS medium). Tumors were digested at 37°C with gentle shaking for 30 min and vortexed every 10 min. Contents were filtered through a 100 mm mesh, and cells were pelleted and resuspended in 45% percoll in 1X HBSS and 1X PBS. Cells were spun at 2000 rpm at 4°C with a swing bucket rotor for 20 min. The supernatant was aspirated, and the pellet was briefly resuspended in 5 mL ACK buffer to lyse red blood cells. Last, cells were pelleted and resuspended in growth medium for downstream applications.

To isolate F4/80+ cells from tumors, tissues were homogenized and processed as above to collect tumor-infiltrating leukocytes. F4/80+ cells were then isolated by positive selection using a rat anti-F4/80 antibody (Biolegend, 123120) and sheep anti-rat Dynabeads (ThermoFisher Scientific, 11035) according to the manufacturer’s instructions.

### Statistical analysis

All data are presented as mean ± SEM. GraphPad Prism 7 was used for statistical analyses. Two-tailed Student’s t test was used for comparisons of two parameters. Two-way ANOVA was used for multi-parameter analyses for time course comparisons. Cell-based experiments were performed with 3–5 biological replicates (cell culture replicates). For tumor volume, outliers were determined using a Rout test (p<0.05), and outliers were omitted from downstream experiments.
