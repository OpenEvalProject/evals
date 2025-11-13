# Rvb1/Rvb2 proteins couple transcription and translation during glucose starvation

## Authors

- Yang S Chen<sup>1</sup> ([ORCID: 0000-0003-3174-091X](https://orcid.org/0000-0003-3174-091X))
- Wanfu Hou<sup>2</sup>
- Sharon Tracy<sup>2</sup>
- Alex T Harvey<sup>2</sup>
- Vince Harjono<sup>2</sup>
- Fan Xu<sup>1</sup> ([ORCID: 0000-0002-0041-4276](https://orcid.org/0000-0002-0041-4276))
- James J Moresco<sup>3</sup>
- John R Yates<sup>3</sup> ([ORCID: 0000-0001-5267-1672](https://orcid.org/0000-0001-5267-1672))
- Brian M Zid<sup>2</sup> ([ORCID: 0000-0003-1876-2479](https://orcid.org/0000-0003-1876-2479)) †

### Affiliations

1. Division of Biological Sciences, University of California, San Diego San Diego United States ([ROR:0168r3w48](https://ror.org/0168r3w48))
2. Department of Chemistry and Biochemistry, University of California San Diego San Diego United States ([ROR:0168r3w48](https://ror.org/0168r3w48))
3. Department of Chemical Physiology, The Scripps Research Institute La Jolla United States ([ROR:02dxx6824](https://ror.org/02dxx6824))

† Corresponding author

## Abstract

During times of unpredictable stress, organisms must adapt their gene expression to maximize survival. Along with changes in transcription, one conserved means of gene regulation during conditions that quickly repress translation is the formation of cytoplasmic phase-separated mRNP granules such as P-bodies and stress granules. Previously, we identified that distinct steps in gene expression can be coupled during glucose starvation as promoter sequences in the nucleus are able to direct the subcellular localization and translatability of mRNAs in the cytosol. Here, we report that Rvb1 and Rvb2, conserved ATPase proteins implicated as protein assembly chaperones and chromatin remodelers, were enriched at the promoters and mRNAs of genes involved in alternative glucose metabolism pathways that we previously found to be transcriptionally upregulated but translationally downregulated during glucose starvation in yeast. Engineered Rvb1/Rvb2-binding on mRNAs was sufficient to sequester mRNAs into mRNP granules and repress their translation. Additionally, this Rvb tethering to the mRNA drove further transcriptional upregulation of the target genes. Further, we found that depletion of Rvb2 caused decreased alternative glucose metabolism gene mRNA induction, but upregulation of protein synthesis during glucose starvation. Overall, our results point to Rvb1/Rvb2 coupling transcription, mRNA granular localization, and translatability of mRNAs during glucose starvation. This Rvb-mediated rapid gene regulation could potentially serve as an efficient recovery plan for cells after stress removal.

## Introduction

Gene expression encompasses many steps across discrete cellular boundaries, including transcription, mRNA processing and export, translation, and decay. Cells do not always live in stable and optimal conditions, instead they are faced with various types of stresses, such as nutrient starvation, heat shock, toxins, pathogens, and osmotic stresses (Majmundar et al., 2010; Richter et al., 2010). In dynamic environmental conditions, cells must balance disparate responses in gene expression as they quickly transition between homeostatic states. This can present challenges such as when cells repress overall translation while needing to upregulate the protein expression of stress response genes (de Nadal et al., 2011). To date, it is generally thought that mRNA cytoplasmic activities are predominantly dictated by cis-acting sequence elements within the RNA; however, coupling steps in gene expression presents an attractive strategy to overcome the challenges by creating regulons of mRNAs that are similarly controlled at the transcriptional level and can be coordinately tuned at the post-transcriptional level as well.

In recent years. ‘imprinting’ by co-transcriptional loading has been implicated as an alternative mechanism to cis-acting RNA sequence elements in determining cytoplasmic mRNA fate (Choder, 2011; Haimovich et al., 2013). For instance, it was found that promoters determined mRNA decay rates through the co-transcriptional loading of RNA-binding proteins (RBPs) to the nascent RNA (Bregman et al., 2011; Trcek et al., 2011). Similarly, Vera et al. showed that the translation elongation factor eEF1A coupled the transcription and translation of HSP70 mRNAs through co-transcriptional loading during heat shock in mammalian cells (Vera et al., 2014). Zander et al. showed that transcription factor Hsf1 might function in loading the nuclear mRNA export protein Mex67 on stress-related mRNAs during heat shock in yeast (Zander et al., 2016).

During stressful conditions, one proposed means of post-transcriptional control is the phase separation of select mRNA transcripts and post-transcriptional regulatory proteins into phase-dense, concentrated, and membrane-less cytoplasmic structures generally described as phase-separated granules (Glauninger et al., 2022; Guzikowski et al., 2019; Zid and O’Shea, 2014). Two well-known stress-induced phase-separated messenger ribonucleoprotein (mRNP) granules are processing bodies (P-bodies) and stress granules (Protter and Parker, 2016; Youn et al., 2019). During stress, the direct connection between the formation of these granules coincident with an overall translational reduction suggests that the localization of mRNAs to these cytoplasmic granules might sequester the mRNAs away from the translational machineries, thus repressing the translation of the mRNAs (Attwood et al., 2020; Ivanov et al., 2019; Kedersha and Anderson, 2002; Sahoo et al., 2018). Yet how mRNAs are partitioned to or excluded from stress-induced granules remains unclear.

Previously we found that during glucose starvation in yeast, promoter sequences play an important role in determining the cytoplasmic fate of mRNAs (Zid and O’Shea, 2014). mRNAs transcribed by active promoters in unstressed cells (class III, e.g., PGK1, PAB1) were directed to P-bodies and are poorly translated (Guzikowski et al., 2022). Meanwhile, stress-induced mRNAs showed two distinct responses: mRNAs of most heat shock genes (class I, e.g., HSP30, HSP26) are transcriptionally induced, actively translated, and remain diffuse in the cytoplasm; however, class II mRNAs are transcriptionally induced but become sequestered in both P-bodies and stress granules and are associated with inactive translation. Class II mRNAs are enriched for alternative glucose metabolic function such as glycogen metabolism (e.g., GSY1, GLC3, GPH1). Surprisingly, instead of the mRNA sequence itself, the promoter sequence that sits in the nucleus directs the translation and cytoplasmic localization of the corresponding induced mRNAs. Specifically, Hsf1-target sequences were shown to direct mRNAs to be excluded from mRNP granules and well translated. However, the mechanism by which the promoter can couple steps of gene expression during glucose starvation is unclear. As the promoter exclusively resides in the nucleus, we hypothesize factors exist that interact with promoters and are co-transcriptionally loaded onto mRNA prior to nuclear export.

In this study, we developed a novel proteomics-based screening method that enabled us to identify Rvb1/Rvb2 as interacting proteins with the promoters of the class II alternative glucose metabolism genes (e.g., GLC3) that are upregulated in transcription but downregulated in translation and have granular-localized mRNA transcripts. Rvb1/Rvb2 (known as RuvbL1/RuvbL2 in mammals) are two highly conserved AAA+ (ATPases Associated with various cellular Activities) proteins that are found in multiple nucleoprotein complexes. Structural studies have shown that in yeast they form an alternating heterohexameric ring or two stacked heterohexameric rings (Jeganathan et al., 2015). They were reported as the chaperones of multiprotein complexes involved in chromatin remodeling processes and other nuclear pathways including snoRNP assembly (Eickhoff and Costa, 2017; Huen et al., 2010; Jeganathan et al., 2015; Jha and Dutta, 2009; Nano and Houry, 2013; Paci et al., 2012; Seraphim et al., 2021; Tian et al., 2017). These two proteins are generally thought to act on DNA but have been found localized to cytoplasmic granules under stress and to be core components of mammalian and yeast cytoplasmic stress granules (Jain et al., 2016; Kakihara et al., 2014; Rizzolo et al., 2017). Rvb1/Rvb2 have also been shown to regulate the dynamics and size of stress granules (Narayanan et al., 2019; Zaarur et al., 2015). The dual presence of Rvb1/Rvb2 at chromatin and stress granules hints to their potential in coupling activities in the nucleus and cytoplasm. Furthermore, a human homolog of Rvb2 was found to be an RNA-binding protein that promotes the degradation of translating HIV-1 Gag mRNA (Mu et al., 2015). Relatedly, in this study we found that Rvb1/Rvb2 have roles in coupling transcription, cytoplasmic mRNA localization, and translation of specific glucose starvation-induced genes in yeast, providing insight into how gene expression can be coordinated during fluctuating environmental conditions.

## Results

### Rvb1/Rvb2 co-purify with plasmids containing an alternative glucose metabolism gene promoter

To identify proteins involved in the ability of promoter sequences to direct the cytoplasmic fate of mRNAs during stress, we developed Co-Transcriptional ImmunoPrecipitation (CoTrIP), a novel biochemical screening technique to identify co-transcriptionally loaded protein factors (Figure 1A). Here, we modified a yeast plasmid containing LacO-binding sites that were previously used as an efficient purification system to isolate histones (Unnikrishnan et al., 2010; Unnikrishnan et al., 2012). To this plasmid, we added a uniform cyan fluorescent protein (CFP) open-reading frame (ORF) and different promoters of interest. We then used FLAG-tagged LacI, which binds to the LacO sequences, and UV-crosslinking to purify the plasmid along with the nascent mRNAs, and co-transcriptionally loaded proteins. Thereafter, mass spectrometry was performed to identify proteins enriched in a promoter-specific manner. Real-time quantitative PCR (RT-qPCR) validates that the CoTrIP method yields enrichment of the target nascent mRNAs, indicating that proteins enriched could be co-transcriptionally loaded (Figure 1—figure supplement 1). Here, we performed CoTrIP of three plasmids (two heat shock genes’ promoters, HSP30 and HSP26, and an alternative glucose metabolism gene’s promoter, GLC3) in cells subject to 10 min of glucose deprivation. Those promoters had previously been shown to be sufficient to determine the cytoplasmic fate of the uniform ORF (Zid and O’Shea, 2014).

![Figure 1.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig1-v2.jpg)

**Figure 1.:** (A) A schematic view of Co-Transcriptional ImmunoPrecipitation (CoTrIP). CoTrIP plasmid has an 8X lacO, a uniform open-reading frame (ORF), and various promoters of interest. CoTrIP plasmid was purified by immunoprecipitation of lacI-3XFlag protein. Enriched protein factors were identified by mass spectrometry. (B) Quantitative volcano plot of co-transcriptional-loaded protein candidates. X-axis: log2 scale of fold change of protein enrichment on two replicates of GLC3 promoter-containing CoTrIP plasmid over on two replicates of HSP30 promoter-containing and one replicate of HSP26 promoter-containing plasmid. Y-axis: minus log10 scale of the p-values from two-sample t-test. Null hypothesis: enrichment on GLC3 promoter equals the enrichment on HSP promoters. Rvb1 and Rvb2 are highlighted in red dots and labeled. (C) Table of protein factors enriched on GLC3 promoters. FC of GLC3 vs. HSP: fold change of protein enrichment on two replicates of GLC3 promoter-containing CoTrIP plasmid over on two replicates of HSP30 promoter-containing and one replicate of HSP26 promoter-containing plasmid. GFPFC of GLC3 vs. CRAPome: fold change of protein enrichment on two replicates of GLC3 promoter-containing CoTrIP plasmid over the CRAPome repository. CRAPome: a contaminant repository for affinity purification–mass spectrometry data. CRAPome was used as a negative control. p-Values were from two-sample t-test of GLC3 vs. HSP. Null hypothesis: enrichment on GLC3 promoter equals the enrichment on HSP promoters. Protein factors were ranked from highest to lowest by ‘FC GLC3 over HSP.’.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** HSP30 promoter-driven reporter mRNA was tested via RT-qPCR. Y-axis: Ct value of the reporter mRNA was first normalized by the housekeeping gene PDC1 and further normalized by the promoter-less CoTrIP plasmid negative control (n = 3).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** In the upper panel, Rvb1/Rvb2 is C-terminally fused with green fluorescent protein mNeonGreen. In the lower panel, Rvb1/Rvb2 is C-terminally fused with red fluorescent protein mRuby2 and P-body marker Dcp2 is C-terminally fused with GFP. Cells are imaged in both log-phase and 30 min glucose starvation conditions. Quantification was performed on 200 cells in each imaging experiment. % of cells w/ foci: among the cells analyzed, the percentage of cells that have a Rvb-containing foci. % of co-localization: among the cells with the Rvb-containing foci, the percentage of cells that have a co-localized foci with Dcp2-containing foci.

After comparing the protein enrichment on GLC3 promoter and on HSP30/HSP26 promoters (Figure 1B and C), we were able to detect differences in protein factors across the specific classes of promoters. The ATP-dependent DNA RuvB-like helicase Rvb1 was enriched tenfold more on GLC3 promoter plasmids versus both HSP30/HSP26 promoters (p-value=0.02). To further verify this enrichment, we compared our protein enrichment data against the CRAPome repository, a large database of contaminant proteins from various immunoprecipitation (IP) experiments, and we found that Rvb1 was significantly enriched on the GLC3 promoter-containing plasmid (Figure 1C; Mellacheruvu et al., 2013). Proteins that were both enriched in ‘promoter versus promoter comparison’ as well as in comparison to the CRAPome are listed (Figure 1C).

Rvb1/Rvb2 are two highly conserved members of the AAA+ family that are involved in multiple nuclear pathways (Jha and Dutta, 2009). These two proteins are generally thought to act on DNA but have been found to be core components of mammalian and yeast cytoplasmic stress granules (Jain et al., 2016; Kakihara et al., 2014; Rizzolo et al., 2017). Microscopy revealed that Rvb1/Rvb2 are predominately present in the nucleus when cells are not stressed but a portion of them becomes localized to cytoplasmic granules that are distinct from P-bodies after 30 min glucose starvation conditions (Figure 1—figure supplement 2). Similar results were previously seen with 2-deoxyglucose-driven glucose starvation, where Rvb1 formed cytoplasmic foci independent of P-bodies and stress granules (Rizzolo et al., 2017). Rvb1/Rvb2’s interactions with DNA in the nucleus and presence in the cytoplasm suggest the potential of Rvb1/Rvb2 to shuttle between the nucleus and cytoplasm.

### Rvb1/Rvb2 are enriched at the promoters of endogenous alternative glucose metabolism genes

To validate the CoTrIP results as well as more globally explore the location of Rvb1 and Rvb2 on DNA during stress, Chromatin ImmunoPrecipitation sequencing (ChIP-seq) was used to investigate Rvb1/Rvb2’s enrichment across the genome. Rvb1/Rvb2 were fused with a tandem affinity purification (TAP)-tag at the C-terminus and purified by rabbit IgG beads. The TAP-tagged strains grow at a normal rate (~90 min doubling time), which suggests TAP-tagging does not generally disrupt the endogenous protein function of these essential proteins. Here, we performed ChIP-seq on Rvb1, Rvb2, and the negative control Pgk1 in 10 min of glucose starvation (the Western validation of Rvb1 and Rvb2’s IP is shown in Figure 2—figure supplement 1A). Rvb1/Rvb2 are enriched from the –500 bp to the transcription start site (TSS) along the genome at 10 min of glucose starvation, whereas ChIP-seq of the negative control Pgk1 is not enriched in the promoter region (Figure 2A). The overall enrichment of promoters is consistent with findings that Rvb’s can function as chromatin remodelers (Zhou et al., 2017). We found that Rvb1/Rvb2 are highly enriched on GSY1, GLC3, and HXK1 promoters but not HSP30, HSP26, or HSP104 promoters, which is consistent with our CoTrIP results (Figure 2C). Rvb1/Rvb2 are significantly more enriched on the proximal promoters of the transcriptionally upregulated, poorly translated genes versus the transcriptionally upregulated and well-translated genes and the average genome (Figure 2D, Figure 2—source data 1). More generally we found that, for genes that show a greater than threefold increase in mRNA levels during glucose starvation, their promoters are significantly more enriched for Rvb2 binding. Previously we had found that Hsf1-binding sequences were sufficient to exclude mRNAs from mRNP granules during glucose starvation (Zid and O’Shea, 2014). Interestingly we found that glucose starvation-induced Hsf1-target promoters have no difference in Rvb1/Rvb2 binding than an average gene, and significantly lower Rvb1/Rvb2 enrichment than stress-induced non-Hsf1 targets (Figure 2B).

![Figure 2.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig2-v2.jpg)

**Figure 2.:** (A) Rvb1/Rvb2 are enriched on promoters and nascent gene bodies. Chromatin ImmunoPrecipitation sequencing (ChIP-seq) of cells in 10 min glucose starvation. X-axis: normalized scale of all genes containing –500 bp to transcription start site (TSS), TSS to transcription end site (TES) and TES to +500 bp. Y-axis: normalized density of target protein on the loci. Normalized density: RPKM of ChIP over RPKM of input. Input: 1% of the cell lysate. Rvb1/Rvb2/Pgk1 are C-terminally fused with tandem affinity purification (TAP) tag and immunoprecipitated by IgG-conjugating breads. Pgk1: a negative control that considered as noninteractor on the genome. (B) Cumulative distribution of Rvb2’s enrichment on genes. X-axis: log2 scale of Rvb2 ChIP read counts over Pgk1 ChIP read counts from –500 bp to TSS. Y-axis: cumulative distribution. >3-fold: genes that have more than threefold transcriptional induction during 10 min glucose starvation. >3-fold Hsf1 targets: genes that have more than threefold transcriptional induction and are Hsf1-regulated. List of genes is given in the supplementary file. (C) Representative gene tracks showing Rvb1/Rvb2’s enrichment. X-axis: gene track with annotation (in Mb). Arrow’s orientation shows gene’s orientation. Y-axis: normalized density of Rvb1/Rvb2 over Pgk1. Normalized density: RPKM of ChIP over RPKM of input. Class I genes are labeled in red and class II genes are labeled in blue. Promoters are highlighted by red rectangles. (D) Enrichment profile of Rvb1/Rvb2 on class I, II genes and genome. X-axis: normalized scale of genome containing –500 bp to TSS, TSS to TES. Y-axis: RPKM of ChIP over RPKM of input. p-Values are from two-sample t-test. Null hypothesis: normalized density from –500 bp to TSS on class II promoters equals on class I promoters.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Western blot validating the efficiency of the immunoprecipitation (IP). Rvb1/Rvb2 are C-terminally fused with the tandem affinity purification (TAP) tag, labeled as Rvb1-TAP and Rvb2-TAP. The proteins of interest were pulled down by rabbit IgG. Cells are harvested at 10 min glucose starvation. Input is 1% of the total lysate. (B) Full Western blot from (A). (C) Comparison analysis of Rvb1/Rvb2/Pgk1’s enrichment on the genome. X-axis: the enriched regions aligned by the center. Y-axis: regions arranged high to low by the level of overlapping. Color code: red indicates that the two IPs are highly overlapped and blue means not overlapped. Left panel: use Pgk1’s enriched regions as reference, score Rvb1’s enrichment. Middle panel: use Pgk1’s enriched regions as reference, score Rvb2’s enrichment. Right panel: use Rvb2’s enriched regions as reference, score Rvb1’s enrichment.

Enrichment peaks of Rvb1/Rvb2 were called using the macs algorithm (Zhang et al., 2008). Consistently, enrichment peaks of Rvb1/Rvb2 were identified on the promoter regions of the class II alternative glucose metabolism genes but not the class I heat shock genes (Figure 2—source data 2). Rvb1 and Rvb2 also show a highly overlapped enrichment pattern across the genome, but neither of them shows overlapped enrichment with the negative control Pgk1 (Figure 2—figure supplement 1C). Structural studies have shown that Rvb1/Rvb2 assemble as heterohexamers (Gribun et al., 2008). Their overlapped ChIP enrichment further supports that Rvb1 and Rvb2 function together along DNA.

### Rvb1/Rvb2 are co-transcriptionally loaded on the alternative glucose metabolism mRNAs

Although Rvb1/Rvb2 are predominantly considered to act on DNA, they are also found to interact with various mRNAs and regulate mRNA translation and stability (Izumi et al., 2012; Mu et al., 2015). We next sought to test whether Rvb1/Rvb2 established similar enrichment patterns on mRNAs. To test the interaction, we performed RNA ImmunoPrecipitation (RIP) on Rvb1, Rvb2, and the negative control wild-type (WT) strain followed by RT-qPCR in both log-phase and 15 min glucose-starved cells. Consistently, during 15 min of glucose starvation, Rvb1/Rvb2 are significantly more enriched on the mRNAs of the class II alternative glucose metabolism genes versus the class I heat shock genes (Figure 3A). Rvb2 is specifically highly enriched on GSY1 mRNA, where it is around 20-fold more enriched than on HSP30 mRNAs. However, in glucose-rich log-phase conditions, Rvb1/Rvb2 are generally less enriched on the mRNAs compared to starvation conditions. Additionally, in log phase, Rvb1/Rvb2 do not show differential enrichment between the alternative glucose metabolism genes and the heat shock genes (Figure 3—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig3-v2.jpg)

**Figure 3.:** (A) Rvb1/Rvb2’s enrichment on endogenous mRNAs in 15 min glucose starvation. RNA immunoprecipitation qPCR of cells in 15 min glucose starvation. Error bars are from two biological replicates. X-axis: four class I mRNAs labeled in red and four class II mRNAs in blue. Y-axis: Ct values were firstly normalized by internal control ACT1, then normalized by input control, finally normalized by the wild-type immunoprecipitation control group. Input: 1% of the cell lysate (n = 3). (B) A schematic view of the reporter mRNA only swapping the promoter. 5UTR: 5′ untranslated region; CDS: coding sequence; CFP: cyan fluorescent protein. (C) Rvb1/Rvb2’s enrichment on the reporter CFP mRNAs in 15 min glucose starvation. RNA immunoprecipitation qPCR of cells in 15 min glucose starvation. X-axis: HSP26 promoter-driven reporter mRNA labeled in red and GLC3 promoter-driven mRNA in blue. Y-axis: Ct values were firstly normalized by internal control ACT1, then normalized by input control. Input: 1% of the cell lysate. Standard deviations are from two biological replicates. Statistical significance was assessed by two-sample t-test (*p<0.05, **p<0.01). Null hypothesis: the enrichment on the two reporter mRNAs is equal.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** RNA immunoprecipitation qPCR of cells in log phase. Error bars are from two technical replicates. X-axis: four class I mRNAs labeled in red and four class II mRNAs in blue. Y-axis: Ct values were firstly normalized by internal control ACT1, then normalized by input control, finally normalized by the wild-type immunoprecipitation control group. Input: 1% of the cell lysate.

Since Rvb1/Rvb2 are enriched on both promoters and mRNAs of class II alternative glucose metabolism genes, we hypothesized that Rvb1/Rvb2 are loaded from the interacting promoters to the nascent mRNAs via the transcription process. To test this, we eliminated the effects from the ORF sequences by designing a pair of reporter mRNAs with a uniform CFP ORF but driven by either the GLC3 promoter or HSP26 promoter (Figure 3B). Interestingly, although the mRNA transcribed virtually identical mRNA sequences (Zid and O’Shea, 2014), Rvb1/Rvb2 are significantly more enriched on the mRNA driven by the GLC3 promoter compared to the one driven by the HSP26 promoter during 15 min of glucose starvation (Figure 3C). This suggests that only the promoter itself can determine the transcribed mRNA’s interaction with Rvb1/Rvb2, further indicating that Rvb1/Rvb2 are likely to be co-transcriptionally loaded from the promoters to nascent mRNAs.

### Engineered Rvb1/Rvb2 tethering to mRNAs directs the cytoplasmic localization and repressed translation

As Rvb1/Rvb2 were found to be located at both promoters in the nucleus and associated with mRNAs in the cytoplasm, we asked whether Rvb1/Rvb2 have an impact on the cytoplasmic fates of bound mRNAs. To test this, we engineered interactions between Rvb1 or Rvb2 and the mRNAs transcribed from various promoters of class I heat shock genes (e.g., HSP30, HSP26). We took advantage of the specific interaction between a phage-origin PP7 loop RNA sequence and the PP7 coat protein (Lim and Peabody, 2002). Here, in our engineered strains, a reporter construct consists of a promoter of interest, a nanoluciferase (nLuc) reporter ORF for measuring protein synthesis, a PP7 loop to drive the engineered interaction, and an MS2 loop for the mRNA subcellular visualization. Along with the reporter, Rvb1 or Rvb2 are fused with PP7-coat protein to establish binding on the reporter mRNA (Figure 4A). As previously shown, Rvb1/Rvb2 do not display strong binding on the promoters and mRNAs of class I heat shock genes (Figures 2C and 3A) (e.g., HSP30). Therefore, we specifically engineered the interaction between Rvb1 or Rvb2 and two types of mRNAs driven by the class I heat shock promoters (HSP30/HSP26). Strikingly, binding of both Rvb1 and Rvb2 alters the cytoplasmic fates of these class I heat shock mRNAs to be similar to the class II alternative glucose metabolism mRNAs (Figure 4, Figure 4—figure supplements 1 and 2). Taking HSP30 promoter-driven reporter mRNA as an example, during glucose starvation the binding of Rvb1 or Rvb2 reduces protein synthesis by ~40% (Figure 4B). It is important to consider that final protein abundance is determined by both mRNA levels and translation. Interestingly, we observed an increase in mRNA abundance when Rvb2 is tethered to the reporter mRNA (Figure 4B). When the translational efficiency was normalized by the mRNA abundance, we were surprised to observe Rvb2 tethering reduces translational efficiency by greater than twofold during glucose starvation (Figure 4B). This change in gene expression was specific to Rvb2 as tethering a GFP PP7-coat protein control had no significant impact on protein levels, mRNA levels, or translational efficiency. Additionally, Rvb1/Rvb2 binding does not significantly repress the translational efficiency of mRNA in glucose-rich unstressed cells, indicating that Rvb1/Rvb2 has a more significant effect on mRNAs when mRNP granules have visibly formed (Figure 4—figure supplements 1 and 2).

![Figure 4.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig4-v2.jpg)

**Figure 4.:** (A) A schematic view of Rvb-tethering methodology. The reporter mRNA contains an HSP30 promoter, nLuc CDS, PP7 loop sequence, and 12XMS2 sequence. Rvb1, Rvb2, or GFP are C-terminally fused with PP7-coat protein (CP). Upper panel shows cloning strategy and lower panel shows mRNA’s situation upon engineering. (B) Protein, mRNA, and translatability levels of HSP30 promoter-driven reporter mRNA in glucose starvation. Y-axis: nLuc synthesized within 5 min time frame after 25 min glucose starvation. NLuc reading was subtracted by the nLuc reading of cycloheximide added 5 min earlier. mRNA levels of HSP30 promoter-driven reporter mRNA in 15 min glucose starvation relative to No PP7-CP. Initial samples were normalized by the internal control ACT1. Translatability was calculated by subtracting the log2 protein values from mRNA relative to No PP7-CP. No PP7-CP (n = 5), RVB1-CP (n = 2), RVB2-CP (n = 5), and GFP-CP (n = 3). Error bars are SEM from these biological replicates. Statistical significance was assessed by a one-sample t-test to test whether the mean differs from 0 (no change from No PP7-CP) (*p<0.05, **p<0.01). (C) Live imaging showing the subcellular localization of the HSP30 promoter-driven reporter mRNA in 30 min glucose starvation. Reporter mRNA is labeled by the MS2 imaging system. P-body is labeled by marker protein Dcp2. PP7 ctrl: negative control, cells only have the reporter mRNA with PP7 loop. PP7+Rvb1-PCP: Rvb1 is tethered to mRNA. PP7+Rvb2-CP: Rvb2 is tethered to mRNA. (D) quantification of the subcellular localization of the reporter mRNA.Y-axis: percentage of cells that have the reporter mRNA-containing granule foci (n = 200). Error bars are from two biological replicates. Statistical significance was achieved by two-sample t-test. Null hypothesis: the proportion of cells with mRNA foci mRNA of experimental and control groups is equivalent. (E) mRNA fold induction of Rvb2-tethered mRNAs and nontethered mRNAs over time. Reporter mRNA is HSP30 promoter driven. X-axis: time (minute) after glucose is removed. Y-axis: mRNA fold induction compared to pre-stress condition (log scale). n = 4, error bars are the SEM of these four replicates. (F) mRNA decay curve of HSP30 promoter-driven reporter mRNAs. X-axis: after cells were starved for 15 min, time (minute) after stopping the transcription using 1,10-phenanthroline. Y-axis: log2 scale of normalized mRNA levels. Ct values of reporter mRNAs were normalized by the internal control ACT1. Statistical significance was achieved by linear regression modeling. Null hypothesis: the mRNA levels of experimental and control groups are equivalent (*p<0.05, **p<0.01, **p<0.001).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) protein synthesis of HSP30 promoter-driven reporter mRNA in log phase and 25 min glucose starvation. Y-axis: nLuc synthesized within 5 min time frame. NLuc reading was subtracted by the nLuc reading of cycloheximide added 5 min earlier. X-axis: different Rvb-tethering conditions. Ctrl: negative control, no PP7 and PP7-coat protein. Rvb1-PCP ctrl: negative control, Rvb1 is fused with PP7-coat protein but no reporter mRNA with PP7 loop. Rvb2-PCP ctrl: negative control, Rvb2 is fused with PP7-coat protein but no reporter mRNA with PP7 loop. PP7 ctrl: negative control, cells only have the reporter mRNA with PP7 loop. PP7+Rvb1-PCP: Rvb1 is tethered to mRNA. PP7+Rvb2-PCP: Rvb2 is tethered to mRNA. Log phase is labeled in blue and glucose starvation in red. Error bars are from two biological replicates. Statistical significance was assessed by two-sample t-test. Null hypothesis: experimental groups and control groups have equivalent results (*p<0.05, **p<0.01, ***p<0.001). (B) Protein synthesis of HSP30 promoter-driven reporter mRNA in log phase and 25 min glucose starvation. Y-axis: nanoluciferase synthesized within 5 min time frame. Nanoluciferase reading was subtracted by the nanoluciferase reading of cycloheximide added 5 min earlier. (C) mRNA levels of HSP30 promoter-driven reporter mRNA in log phase and 15 min glucose starvation. Y-axis: Ct values of reporter mRNAs were normalized by the internal control ACT1. (D) Live imaging showing the subcellular localization of the HSP30 promoter-driven reporter mRNA in 15 min and 30 min glucose starvation. Reporter mRNA is labeled by the MS2 imaging system. P-body is labeled by marker protein Dcp2. PP7 ctrl: negative control, cells only have the reporter mRNA with PP7 loop. PP7+Rvb1-PCP: Rvb1 is tethered to mRNA. PP7+Rvb2-CP: Rvb2 is tethered to mRNA. (E) Quantification of the subcellular localization of the reporter mRNA in 30 min glucose starvation. Cells with foci: percentage of cells that have the reporter mRNA-containing granule foci. Cells with non-P-body foci: among the cells that have the reporter mRNA-containing granule foci, the percentage of cells that have reporter mRNA-containing granule foci that are not co-localized with P-body. N = 200. Error bars are from two biological replicates.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Protein synthesis of HSP26 promoter-driven reporter mRNA in log phase and 25 min glucose starvation. Y-axis: nLuc synthesized within 5 min time frame. NLuc reading was subtracted by the nLuc reading of cycloheximide added 5 min earlier. (B) mRNA levels of HSP26 promoter-driven reporter mRNA in log phase and 15 min glucose starvation. Y-axis: Ct values of reporter mRNAs were normalized by the internal control ACT1. (C) Translatability of HSP26 promoter-driven reporter mRNA in log phase and 15 min glucose starvation. mRNA translatability: normalized protein level over normalized mRNA level. (A–C) Log phase is labeled in blue and glucose starvation in red. Error bars are from two biological replicates. Ctrl: negative control, no PP7 and PP7-coat protein. Rvb1-PCP ctrl: negative control, Rvb1 is fused with PP7-coat protein but no reporter mRNA with PP7 loop. Rvb2-PCP ctrl: negative control, Rvb2 is fused with PP7-coat protein but no reporter mRNA with PP7 loop. PP7 ctrl: negative control, cells only have the reporter mRNA with PP7 loop. PP7+Rvb1-PCP: Rvb1 is tethered to mRNA. PP7+Rvb2-PCP: Rvb2 is tethered to mRNA. (D) Live imaging showing the subcellular localization of the HSP26 promoter-driven reporter mRNA in 15 min and 30 min glucose starvation. Reporter mRNA is labeled by the MS2 imaging system. P-body is labeled by marker protein Dcp2. PP7 ctrl: negative control, cells only have the reporter mRNA with PP7 loop. PP7+Rvb1-PCP: Rvb1 is tethered to mRNA. PP7+Rvb2-CP: Rvb2 is tethered to mRNA. (E) Quantification of the subcellular localization of the reporter mRNA in 30 min glucose starvation. Cells with foci: percentage of cells that have the reporter mRNA-containing granule foci. Cells with non-P-body foci: among the cells that have the reporter mRNA-containing granule foci, the percentage of cells that have reporter mRNA-containing granule foci that are not co-localized with P-body. N = 200. Error bars are from two biological replicates.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) Ribosome profiling was performed on cells in 15 min glucose starvation and followed by 1 min and 5 min glucose addback. Y-axis: log2 scale of ribosome occupancy fold changes on mRNAs compared to log-phase condition. X-axis: each bar represents a gene group. Bars are grouped by conditions. Class I genes and class II genes refer to Figure 2—source data 1. (B) Endogenous class I and II genes were tagged with nLuc. Luciferase expression was measured after 30 min glucose starvation and 10 min after 2% glucose was readded to cultures starved of glucose for 30 min. Statistical significance was tested by two-sample t-test (n = 3) (*p<0.05, **p<0.01).

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** (A, B) Mathematical modeling on mRNA abundance upon varied transcription rates and varied mRNA degradation rates. X-axis: time (minute) after glucose is removed. Y-axis: mRNA fold induction compared to pre-stress condition. Modeling function: ∆X(t) = (β/α −X0)(1−e−αt), dX/dt = β −αX. α/a denotes the degradation rate constant. mRNA is produced at a constant rate (β/b). mRNA concentration is (X). (A) Varying β – transcription rate. (B) Varying α – mRNA degradation rates. (C) Half-lives of HSP30 promoter-driven reporter mRNAs. Error bars are from four biological replicates. Statistical significance was achieved by two-sample t-test. Null hypothesis: the mRNA half-lives of experimental and control groups are equivalent.

Since the translation of the mRNAs bound by Rvb1/Rvb2 was reduced, we further visualized the subcellular localization of those mRNAs. Consistent with reduced translation, Rvb1/Rvb2 tethering significantly increases the granular localization of the heat shock mRNA reporters (Figure 4C, Figure 4—figure supplements 1 and 2). Taking HSP30 promoter-driven reporter mRNA as an example, only 4% of the cells form HSP30 promoter-driven mRNA-containing granules when the mRNA is not bound by Rvb1 or Rvb2, yet Rvb1 tethering increases the mRNA’s granular localization to 27% of the cells and Rvb2 tethering increases the mRNA’s granular localization to 39% of the cells (Figure 4C and D). Furthermore, the binding of Rvb1 and Rvb2 to mRNA increases the formation of granules that are non-colocalized with a P-body marker (Figure 4—figure supplements 1 and 2). This indicates that Rvb2 is sufficient to drive the interacting mRNA to P-body independent starvation-induced granules. To further eliminate any potential artifacts caused by the C-terminal modification on Rvb1/Rvb2, the negative controls were tested where Rvb1 or Rvb2 are fused with PP7 coat protein, but the mRNA does not have the PP7 loop. The negative control strains did not show a decrease in translatability of the reporter mRNAs in glucose starvation. It indicates translation only decreases and the mRNA granular localization level only increases when the full Rvb-mRNA interaction was established (Figure 4—figure supplements 1 and 2). These results support the ability of Rvb1/Rvb2 to suppress the translation of the binding mRNAs, potentially through sequestering the mRNAs into cytoplasmic granules.

The coupling of induced transcription and repressed translation of the class II alternative glucose metabolism genes may be an important adaptation for cells to survive from stress conditions. Results showed that after replenishing the glucose to the starved cells, the translation of those genes is quickly induced, with an approximately eightfold increase in ribosome occupancy 5 min after glucose readdition for class II mRNAs (Figure 4—figure supplement 3A). We also find that class II mRNAs quickly increase their protein production upon glucose readdition (Figure 4—figure supplement 3B). This indicates the potential biological role of the starvation-induced granules as a repository for these translationally repressed class II mRNAs during stress that does not preclude these mRNAs from potentially being quickly released and translated once the stress is removed.

### Engineered Rvb2 binding to mRNAs increases the transcription of corresponding genes

Interestingly, Rvb2 not only suppress the translation of bound mRNAs, but also increases the abundance of the interacting mRNAs by approximately almost twofold (Figure 4C). There are two possibilities for this increased mRNA abundance by Rvb2 tethering: increased transcription and/or slower mRNA decay. To address this, we performed time-course measurements on the HSP30 promoter-driven reporter mRNA abundance in 0, 5, 10, 15, 30, and 45 min of glucose starvation. Here, we compared the mRNA abundance when mRNA is bound by Rvb2 and when mRNA is not bound by Rvb2 as a control. A mathematical modeling approach was performed to predict the mRNA induction abundance change caused by varied transcriptional efficiency or varied decay rate (Figure 4—figure supplement 4; Elkon et al., 2010). In the model, we assumed that mRNA level is mainly dependent on the transcriptional and decay rates, and these parameters stay constant over the course of induced expression during glucose starvation. From the mathematical modeling, mRNA fold induction differs between varied transcriptional induction versus mRNA decay changes. If transcriptional rates vary, differences in mRNA levels are the same (equal distance shift) at each time point on a log-log scale (Figure 4—figure supplement 4). While if mRNA decay varies, although little difference is seen in mRNA abundance in early glucose starvation, our simulation predicts increasing differences in mRNA abundance at later time points of glucose starvation (Figure 4—figure supplement 4B). By comparing experimental measurements of mRNA induction of the Rvb2-tethered condition to the unbound control condition, the mRNA induction differences are similar at each time point. When Rvb2 binds to the mRNA, the abundance of the mRNA is constantly greater than the unbound mRNA at all time points during glucose starvation, indicating that the greater mRNA abundance is mainly due to greater transcription differences driven by the Rvb2 binding (Figure 4E).

To further experimentally validate that the greater mRNA abundance caused by Rvb2 binding is due to increased transcription and not slower decay, we stopped cellular transcription after 15 min of glucose starvation by treatment with the transcription inhibitor drug 1,10-phenanthroline. Then we performed time-course measurements on mRNA abundance and compared the decay of mRNAs with and without Rvb2 binding. Consistently, mRNAs bound by Rvb2 decay at a slightly but not significantly faster rate, not a slower rate (Figure 4F). Whether or not bound by Rvb2, the reporter mRNA has around a 25 min half-life (Figure 4—figure supplement 4C). These results further point to Rvb2 mRNA tethering driving transcriptional upregulation. Since Rvb2 is targeted to the mRNA, it is likely that local recruitment of Rvb2 to the nascently transcribed mRNA increases the local concentration of Rvb2 protein to the vicinity of the regulatory region of the corresponding gene, further showing the connections between the transcriptional and translational processes.

### RVB2 knockdown drives decreased mRNA induction but enhanced protein production of Rvb1/Rvb2 target genes

To further test the role of RVB1/RVB2 in regulating gene expression during glucose starvation, we sought to reduce RVB function in cells. RVB1/RVB2 deletions are inviable (Jónsson et al., 2001) so we aimed to identify gRNA targets that would temporally reduce RVB expression through inducible gRNAs and dCas9-MXi (Smith et al., 2016). We found an RVB2 gRNA that gave an ~20-fold reduction in RVB2 expression 8 hr after treatment with anhydrotetracycline (ATc) (Figure 5A and B). To investigate the necessity of Rvb1/Rvb2 in the translational repression of class II genes during glucose starvation, we C-terminal tagged two class II genes (GSY1 and HXK1) and one class I gene (HSP30) and then quantified their protein induction after 30 min glucose starvation. While both class II genes had robust mRNA induction upon glucose starvation in the control samples (Figure 5—figure supplement 1), this was associated with no significant upregulation of protein production (Figure 5C). Upon RVB2 knockdown, we find a significant increase in the stress induction of the class II proteins Gsy1 and Hxk1, while we find no significant difference in the protein induction of the class I protein Hsp30 (Figure 5C). While the higher protein induction could be because of even further increases in mRNA levels, we instead find that RVB2 knockdown causes a greater than twofold decrease in GSY1 and HXK1 mRNA induction (Figure 5D). This is consistent with previous findings (Jónsson et al., 2001) as well as our tethering data that Rvb1/Rvb2 have a role in transcriptional induction. Together this data further supports the role for Rvb1/Rvb2 repressing the translatability of target mRNAs during glucose starvation.

![Figure 5.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig5-v2.jpg)

**Figure 5.:** (A) A schematic view of CRISPRi repression of RVB2 transcription. The RVB2 gRNA was placed under the control of a TetOn promoter. Upon anhydrotetracycline (ATc) treatment, this induces RVB2 gRNA expression, targeting dCas9-MXi to the upstream region of RVB2 and repressing transcription. (B–D) RVB2 knockdown was accomplished by inoculating log-phase cultures with 250 ng/L ATc for 8 hr. Control cells have no ATc. (B) mRNA levels of RVB2 and ACT1 were determined in log-phase cultures expressing either an RVB1 or RVB2 gRNA. RVB2 mRNA levels were normalized to ACT1. Statistical significance was achieved by two-sample t-test. RVB1 gRNA (n = 2); RVB2 gRNA (n = 5). (C) Endogenous genes were tagged with nLuc and luciferase was quantified during log-phase growth and 30 min after glucose starvation in ±ATc cultures. Statistical significance was achieved by two-sample t-test (GSY1, HXK1 n = 4, HSP30 n = 3). (D) mRNA levels of the genes of interest were tested in log phase and 30 min of glucose starvation ±ATc. The log2 fold change -Glu/+Glu in the RVB2 knockdown was subtracted from the control mRNA fold change. Statistical significance was assessed by a one-sample t-test to test whether the mean fold change differs from 0 (no change from -ATc control) (GSY1, HXK1 n = 4, HSP30 n = 3) (*p<0.05, **p<0.01, **p<0.001).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** mRNA levels for endogenously tagged genes were measured upon 30 min of glucose starvation in control and RVB2 knockdown strains that have been treated for 8 hr with ATC (GSY1, HXK1 n = 4, HSP30 n = 3).

## Discussion

In fluctuating environments, cells must quickly adjust the expression of different genes dependent upon cellular needs. Here, our results demonstrate a novel function of the AAA+ATPases Rvb1/Rvb2 in the cytoplasm, and a novel mechanism of Rvb1/Rvb2 in coupling the transcription, mRNA cytoplasmic localization, and translation of specific genes (Figure 6). We identified Rvb1/Rvb2 as enriched protein factors on the promoters of the class II alternative glucose metabolism genes that are upregulated in transcription but downregulated in translation during glucose starvation. Results showed that Rvb1/Rvb2 have a strong preferred interaction with both promoters and mRNAs of these genes, suggesting that Rvb1/Rvb2 are loaded from enriched promoters to the nascent mRNAs. More interestingly, when we tethered Rvb1/Rvb2 to the mRNAs, the binding of Rvb1/Rvb2 had a strong impact on reducing mRNA translation and increasing the mRNA granular localization. We are uncertain whether Rvb1/Rvb2 tethering represses translation, which directs mRNAs to mRNP granules; or Rvb1/Rvb2 binding directly targets the mRNA to the granule, which represses translation; or some combination of both – as these are very hard to disentangle. Either way, these data, along with our RVB2 depletion data, suggest the potential co-transcriptional loading of Rvb1/Rvb2 directs post-transcriptional mRNA fate in the cytoplasm. Additionally, Rvb1/Rvb2’s interaction with the mRNA can also induce transcription of the corresponding genes, further indicating that Rvb1/Rvb2 couple the transcription and translation of the interacting genes.

![Figure 6.](https://cdn.elifesciences.org/articles/76965/elife-76965-fig6-v2.jpg)

**Figure 6.:** First, Rvb1/Rvb2 are recruited by specific promoters and loaded onto the nascent mRNAs during glucose starvation. Then Rvb1/Rvb2 escort the interacting mRNAs to the cytoplasm and cause repressed translation and localization to cytoplasmic granules. Also, forced Rvb binding on an mRNA drives an increase in the transcription of the corresponding genes, further showing the coupling of transcription and translation.

It is not clear how tethering Rvb1/Rvb2 to an mRNA reporter increases transcription of the corresponding DNA locus. Rvb1/Rvb2 were initially found to be associated with many chromatin remodeling and transcription-related complexes. This has further been expanded on, and several studies have demonstrated a chaperone-like activity in the formation of various complexes including the assembly of chromatin remodeling complexes and RNA polymerase II (Nano and Houry, 2013; Paci et al., 2012; Seraphim et al., 2021). It may be that recruiting Rvb1/Rvb2 to the nascent RNA increases the local concentration, driving further enhancement of transcription-related processes. It is also intriguing to think about Rvb1/Rvb2’s reported role in escorting client proteins to large macromolecular complexes. Like their escorting protein function, it is plausible to hypothesize that they might have additional functions in escorting mRNAs to large macromolecule mRNP granule complexes in stressful conditions.

The coupling of transcription and translation of specific genes may be an important adaptation for cells to survive during stress conditions. It has been postulated that to save energy during stress mRNAs are temporarily stored in the cytoplasmic granules associated with inactive translation instead of mRNA decay (Guzikowski et al., 2019; Horvathova et al., 2017; Pitchiaya et al., 2019; Protter and Parker, 2016; Schütz et al., 2017). Our results show that, after replenishing glucose to the starved cells, the translation of those genes is quickly induced (Figure 4—figure supplement 3). The stress-induced phase-separated granules may serve as temporary repositories for the inactive translating mRNAs of many genes that are regulated by Rvb1/Rvb2 in glucose starvation and involved in alternative glucose metabolism pathways. From the perspective of cell needs, many alternative glucose metabolism genes are involved in glycogen synthesis, which may be superfluous for survival during times of complete glucose starvation, but the cell may want to produce them as quickly as possible upon glucose replenishment to drive quick protein synthesis. The special coupling of increased transcription but repressed translation mediated by Rvb1/Rvb2 may serve as an emergency but prospective mechanism for cells to precisely repress the translation of these alternative glucose metabolism mRNAs during stress but be able to quickly translate these pre-stored mRNAs once the cells are no longer starved (Jiang et al., 2020). Also, the genes regulated by Rvb1/Rvb2 may be dependent on the type of stresses. We observed this mechanism of gene expression control on alternative glucose metabolism genes during glucose starvation stress. It will be interesting to test whether there is similar regulation on different sets of genes that are related to other types of stresses, such as heat shock and osmotic stress responses.

To further understand the function of Rvb1/Rvb2 mechanistically, it is crucial to understand how Rvb1/Rvb2 are recruited to these specific promoters. We prefer the hypothesis that the recruitment of Rvb1/Rvb2 is mediated by other DNA-binding proteins as we were unable to identify specific binding motifs of Rvb1/Rvb2 from our ChIP-seq data. As we found that Rvb1/Rvb2 are generally enriched on the promoters of transcriptionally upregulated mRNAs, we favor a model in which the default is for Rvb1/Rvb2 to be recruited to active transcription sites. This fits with previous data that Rvb1/Rvb2 are required to maintain expression of many inducible promoters including galactose-inducible transcripts (Jónsson et al., 2001). While Rvb1/Rvb2 are generally recruited to the promoters of induced mRNAs during glucose starvation, we find that Hsf1-regulated promoters circumvent this recruitment through an unknown mechanism as the transcriptionally upregulated Hsf1 targets show reduced recruitment relative to non-Hsf1 targets (Figure 2B). Intriguingly, Hsf1-regulated genomic regions have been found to coalesce during stressful conditions (Chowdhary et al., 2017; Pincus et al., 2018). It will be interesting to explore whether Rvb1/Rvb2 may be excluded from these coalesced regions in future studies.

This study provides new insights into how gene expression is controlled under stressful conditions, including how mRNAs can be targeted to stress-induced mRNP granules. It also identifies Rvb1/Rvb2 as key proteins connecting discrete steps of gene expression across cellular compartments. In mammalian cells, overexpression of the RVB1/2 homologs, RUVBL1/2, is correlated with tumor growth and poor prognosis in several cancer types, yet precise mechanisms for how these proteins impact cancer progression are unclear (Grigoletto et al., 2011; Lauscher et al., 2012; Lin et al., 2020). It is important to further study the role these proteins have on connecting gene expression in different conditions to better understand how they may be impacting cancer progression in mammalian cells.

## Materials and methods

### Yeast strains and plasmids

The yeast strains and plasmids used in this study are listed in Key resources table, and the oligonucleotides used for the plasmid construction, yeast cloning, and RT-qPCR are described in Key resources table. The strains were created through genomic integration of a linear PCR product, or a plasmid linearized through restriction digest or the transformation of an episomal vector. The background strain used was W303 (EY0690), one laboratory strain that is closely related to S288C. In yeast cloning for the C-terminal fusion on the endogenous proteins (e.g., Rvb1-mNeongreen, Rvb1-PP7CP, Rvb1-TAP), we used plasmids of Pringle pFA6a and pKT system (Lee et al., 2013; Longtine et al., 1998; Zid and O’Shea, 2014), gifts from the E. K. O’Shea laboratory and the K. Thorn laboratory. We modified the pFA6a and pKT plasmids by inserting in the peptides of interest into the plasmids. The primers used to amplify the fragments from these plasmids contain two parts from 3′ to 5′: a uniform homolog sequence to amplify the plasmid and a homolog sequence to direct inserting the fragments to the genomic loci of interest. The fragments were transformed into the yeasts and integrated to the genome by homologous recombination. The integrations were confirmed by genomic DNA PCR (Yeast DNA Extraction Kit from Thermo Fisher). In the cloning of the reporter strains, we used a strain that was derived from W303 and has one-copied genomic insertion of MYOpr-MS2CP-2XGFP and an endogenous fusion Dcp2-mRFP (Zid and O’Shea, 2014), as the background strain. Further, we transformed the linearized MS2-loop-containing reporter plasmids into the strain by restriction digest and genomic integration. RT-qPCR was performed to verify the one-copied genomic integration. To generate the MS2-loop-containing reporter plasmids (e.g., ZP207 pRS305-HSP30prUTR-nLuc-PEST-12XMS2-tADH1), we started from the plasmid ZP15 pRS305-12XMS2-tAdh1 (Zid and O’Shea, 2014). ZP15 was linearized by the restriction enzymes SacII and NotI (NEB). Promoter fragments, nanoluciferase-pest CDS fragments were inserted into linearized ZP15 using Gibson Assembly. Promoter sequences were amplified by PCR from the W303 genomic DNA. Nanoluciferase-pest CDS was amplified by PCR from the geneblock (Masser et al., 2016). To generate the PP7-MS2-containing reporter plasmids (e.g., ZP296 pRS305-HSP30prUTR-nLuc-PEST-1XPP7-12XMS2-tADH1), ZO680 and ZO679 were firstly annealed using the primer annealing protocol described by Thermo Fisher. ZP15 was linearized by restriction enzymes BamHI and NotI. Then annealed oligos were inserted into linearized ZP15 by T4 ligation to generate ZP440. ZP440 was further linearized by restriction enzymes SacII and NotI. Promoter fragments, nanoluciferase-pest CDS fragments were inserted into linearized ZP440 using Gibson Assembly. In the cloning of the CoTrIP experiments, detailed procedures are described in ‘CoTrIP and CoTrIP analysis.’.

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
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>EY0690/w303</td>
      <td>Lab stock</td>
      <td>MATa trp1 leu2 ura3 his3 can1 GAL+psi +</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY1</td>
      <td>This study</td>
      <td>EY0690; pRS406-CMV lacIA-FLAG</td>
      <td>Available in the Zid lab</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY2</td>
      <td>This study</td>
      <td>EY0690; HSP30-CFP-CoTrIP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY3</td>
      <td>This study</td>
      <td>ZY1; HSP30prUTR-CFP-CoTrIP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY4</td>
      <td>This study</td>
      <td>ZY1; HXK1prUTR-CFP-CoTrIP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY5</td>
      <td>This study</td>
      <td>ZY1; HSP26prUTR-CFP-CoTrIP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY6</td>
      <td>This study</td>
      <td>ZY1; GLC3prUTR-CFP-CoTrIP</td>
      <td>(include dilution)</td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY7</td>
      <td>This study</td>
      <td>ZY1; Blank-CoTrIP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY18</td>
      <td>Zid and O’Shea, 2014</td>
      <td>EY0690; MYO2pr-MS2-CP-GFP2x; Dcp2-RFP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY147</td>
      <td>This study</td>
      <td>EY0690; Rvb1-TAP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY148</td>
      <td>This study</td>
      <td>EY0690; Rvb2-TAP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY282</td>
      <td>This study</td>
      <td>EY0690; Dcp2-GFP; Rvb1-mRuby2</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY284</td>
      <td>This study</td>
      <td>EY0690; Dcp2-GFP; Rvb2-mRuby2</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY266</td>
      <td>This study</td>
      <td>ZY18; HSP30prUTR-nLuc-pest-1XPP7-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY269</td>
      <td>This study</td>
      <td>ZY18, PDhh1-GFP-6xHis-PP7CP;HSP30prUTR-nLuc-pest-1XPP7-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY314</td>
      <td>This study</td>
      <td>ZY18; Rvb1-PP7CP-6Xhis; HSP30prUTR-nLuc-pest-1XPP7-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY315</td>
      <td>This study</td>
      <td>ZY18; Rvb2-PP7CP-6Xhis; HSP30prUTR-nLuc-pest-1XPP7-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY193</td>
      <td>This study</td>
      <td>ZY18; HSP30prUTR-nLuc-pest-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY446</td>
      <td>This study</td>
      <td>ZY18; Rvb1-PP7CP-6Xhis; HSP30prUTR-nLuc-pest-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY449</td>
      <td>This study</td>
      <td>ZY18; Rvb2-PP7CP-6Xhis; HSP30prUTR-nLuc-pest-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY316</td>
      <td>This study</td>
      <td>ZY18; Rvb1-PP7CP-6Xhis</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY317</td>
      <td>This study</td>
      <td>ZY18; Rvb2-PP7CP-6Xhis</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY318</td>
      <td>This study</td>
      <td>EY0690; Rvb1-mNeogreen</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY319</td>
      <td>This study</td>
      <td>EY0690; Rvb2-mNeogreen</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY488</td>
      <td>This study</td>
      <td>ZY18; HSP26prUTR-nLuc-pest-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY489</td>
      <td>This study</td>
      <td>ZY18; HSP12prUTR-nLuc-pest-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY490</td>
      <td>This study</td>
      <td>ZY18; HSP26prUTR-nLuc-pest-1XPP7-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY491</td>
      <td>This study</td>
      <td>ZY18; HSP12prUTR-nLuc-pest-1XPP7-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY492</td>
      <td>This study</td>
      <td>ZY18; HSP26prUTR-nLuc-pest-12XMS2-tADH1; Rvb1-PP7CP-6Xhis</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY493</td>
      <td>This study</td>
      <td>ZY18; HSP12prUTR-nLuc-pest-12XMS2-tADH1; Rvb1-PP7CP-6Xhis</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY494</td>
      <td>This study</td>
      <td>ZY18; HSP26prUTR-nLuc-pest-1XPP7-12XMS2-tADH1; Rvb1-PP7CP-6Xhis</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY495</td>
      <td>This study</td>
      <td>ZY18; HSP12prUTR-nLuc-pest-1XPP7-12XMS2-tADH1; Rvb1-PP7CP-6Xhis</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY496</td>
      <td>This study</td>
      <td>ZY18; HSP26prUTR-nLuc-pest-12XMS2-tADH1; Rvb2-PP7CP-6Xhis</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY497</td>
      <td>This study</td>
      <td>ZY18; HSP12prUTR-nLuc-pest-12XMS2-tADH1; Rvb2-PP7CP-6Xhis</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY498</td>
      <td>This study</td>
      <td>ZY18; HSP26prUTR-nLuc-pest-1XPP7-12XMS2-tADH1; Rvb2-PP7CP-6Xhis</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY499</td>
      <td>This study</td>
      <td>ZY18; HSP12prUTR-nLuc-pest-1XPP7-12XMS2-tADH1; Rvb2-PP7CP-6Xhis</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY642</td>
      <td>This study</td>
      <td>EY0690; HSP26prUTR-CFP-12XMS2-tADH1; Rvb1-TAP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY643</td>
      <td>This study</td>
      <td>EY0690; GLC3prHSP26UTR-CFP-12XMS2-tADH1; Rvb1-TAP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY644</td>
      <td>This study</td>
      <td>EY0690; HSP26prUTR-CFP-12XMS2-tADH1; Rvb2-TAP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY645</td>
      <td>This study</td>
      <td>EY0690; GLC3prHSP26UTR-CFP-12XMS2-tADH1; Rvb2-TAP</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY831</td>
      <td>This study</td>
      <td>EY0690,GSY1p-GSY1ORF-pKT-ERVB-nLucPEST; RVB2-gRNA; dCas9-Mxi</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY833</td>
      <td>This study</td>
      <td>EY0690,HXK1p-HXK1ORF-pKT-ERVB-nLucPEST; RVB2-gRNA; dCas9-Mxi</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY834</td>
      <td>This study</td>
      <td>EY0690,HSP30p-HSP30ORF-pKT-ERVB-nLucPEST; RVB2-gRNA; dCas9-Mxi</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY362</td>
      <td>This study</td>
      <td>EY0690, HSP30-pKT-ERBV1-nLucPEST</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY407</td>
      <td>This study</td>
      <td>EY0690, HSP26-pKT-ERBV1-nLucPEST</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY408</td>
      <td>This study</td>
      <td>EY0690, HXK1-pKT-ERBV1-nLucPEST</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>ZY409</td>
      <td>This study</td>
      <td>EY0690, GSY1-pKT-ERBV1-nLucPEST</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP66</td>
      <td>This study</td>
      <td>pUC-TalO8 (Blank-CoTrIP)</td>
      <td>Addgene:178303</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP67</td>
      <td>This study</td>
      <td>TalO8-HSP30-CFP</td>
      <td>Addgene:178304</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP68</td>
      <td>This study</td>
      <td>TalO8-HXK1-CFP</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP69</td>
      <td>This study</td>
      <td>TalO8-HSP26-CFP</td>
      <td>Addgene:178306</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP70</td>
      <td>This study</td>
      <td>TalO8-GLC3-CFP</td>
      <td>Addgene:178307</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP64</td>
      <td>Unnikrishnan et al., 2010</td>
      <td>pRS406-CMV-LacI-3xFLAG</td>
      <td>Addgene:83410</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP60</td>
      <td>Lab stock</td>
      <td>pFA6-TAP(CBP-TEV-ZZ)-Kan</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP61</td>
      <td>Lab stock</td>
      <td>pFA6-TAP(CBP-TEV-ZZ)-His</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP47</td>
      <td>Lab stock</td>
      <td>pKT-mNeongreen-Ura</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP224</td>
      <td>Lab stock</td>
      <td>pFA6a-link-yoEGFP-SpHis5</td>
      <td>Addgene:44836</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP109</td>
      <td>Lab stock</td>
      <td>pKT-mRuby2-HPH</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP93</td>
      <td>Carroll et al JCB 2011</td>
      <td>pRS316 PDhh1-GFP-6×His-PP7CP</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP296</td>
      <td>This study</td>
      <td>pRS305-HSP30prUTR-nLuc-pest-1XPP7-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZY311</td>
      <td>Lab stock</td>
      <td>pKT-PP7CP-6xHis-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP207</td>
      <td>This study</td>
      <td>pRS305-HSP30prUTR-nLuc-PEST-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP214</td>
      <td>This study</td>
      <td>pRS305-GLC3prUTR-nLuc-PEST-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP315</td>
      <td>This study</td>
      <td>pRS305-GSY1prUTR-nLuc-PEST-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP441</td>
      <td>This study</td>
      <td>pRS305-HSP26prUTR-nLuc-pest-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP442</td>
      <td>This study</td>
      <td>pRS305-HSP12prUTR-nLuc-pest-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP443</td>
      <td>This study</td>
      <td>pRS305-HSP26prUTR-nLuc-pest-1XPP7-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP444</td>
      <td>This study</td>
      <td>pRS305-HSP12prUTR-nLuc-pest-1XPP7-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP440</td>
      <td>Lab stock</td>
      <td>pRS305-1XPP7-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP29</td>
      <td>Zid and O’Shea, 2014</td>
      <td>pRS305-HSP26prUTR-CFP-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP32</td>
      <td>Zid and O’Shea, 2014</td>
      <td>pRS305-GLC3prHSP26UTR-CFP-12XMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP15</td>
      <td>Zid and O’Shea, 2014</td>
      <td>pRS305-12xMS2-tADH1</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP480</td>
      <td>McGlincy et al., 2021</td>
      <td>pNTI647 dCas9-Mxi1 TetR KanMX</td>
      <td>Addgene:139474</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP479</td>
      <td>McGlincy et al., 2021</td>
      <td>pNTI661 pRPR1(TetO)-sgRNA</td>
      <td>Addgene:139475</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP577</td>
      <td>This study</td>
      <td>pNTI661 pRPR1(TetO)-sgRNA (Rvb2gRNA_i04)</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ZP345</td>
      <td>Guzikowski et al., 2022</td>
      <td>pKT ERBV-1 nLucPEST</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>NLuc+PestR</td>
      <td>This paper</td>
      <td>Amplify nLuc-pest to assemble into reporter vector</td>
      <td>ATCCACTAGTTCTAGAGC TTAAACATTAATACGAGCAGAAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>yNLucF</td>
      <td>This paper</td>
      <td>Amplify nLuc-pest to assemble into reporter vector</td>
      <td>ATGGTTTTTACTTTAGAAGATTTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>HSP30pr-F</td>
      <td>This paper</td>
      <td>Amplify HSP30 promoter and UTR to assemble into reporter vector</td>
      <td>TCACTATAGGGCGAATTGGAGCTCCACCGC CCTTTCTTCAAAAGTAGAAAACTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>HSP30utr-R</td>
      <td>This paper</td>
      <td>Amplify HSP30 promoter and UTR to assemble into reporter vector</td>
      <td>TCTAAAGTAAAAACCAT TTGAAATTTGTTGTTTTTAGTAATCAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cRvb2-R</td>
      <td>This paper</td>
      <td>Checking the C-terminal fusion of Rvb2</td>
      <td>CACCAACCAAGGCTTTTTGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cRvb2-F</td>
      <td>This paper</td>
      <td>Checking the C-terminal fusion of Rvb2</td>
      <td>TGACCAAAACAGGTGTGGAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cRvb1-R</td>
      <td>This paper</td>
      <td>Checking the C-terminal fusion of Rvb1</td>
      <td>CACAGCCATTACCACACCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>cRvb1-F</td>
      <td>This paper</td>
      <td>Checking the C-terminal fusion of Rvb1</td>
      <td>CCTGAAGACGCAGAGAATCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RVB1TAPtag_F</td>
      <td>This paper</td>
      <td>C-terminal TAP-tag</td>
      <td>AAGGTCAACAAAGATTTTAGAAACTTCCGCAAATTATTTG cggatccccgggttaattaa</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RVB1Taptag_R</td>
      <td>This paper</td>
      <td>C-terminal TAP-tag</td>
      <td>TATTTTTATTTATGAAATGTGCTTTAGGCTTTCTTCACTG gaattcgagctcgtttaaac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RVB2TAPtag_F</td>
      <td>This paper</td>
      <td>C-terminal TAP-tag</td>
      <td>TGCTAAATCAGCAGACCCTGATGCCATGGATACTACGGAAcggatccccgggttaattaa</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RVB2TAPtag_R</td>
      <td>This paper</td>
      <td>C-terminal TAP-tag</td>
      <td>TATATATTTGATGCAATTTCTGCCTTAAAGTACAAAATGCgaattcgagctcgtttaaac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>pKT_Rvb2_R</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>TATATATTTGATGCAATTTCTGCCTTAAAGTACAAAATGC tcgatgaattcgagctcg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>pKT_Rvb2_F</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>TGCTAAATCAGCAGACCCTGATGCCATGGATACTACGGAA ggtgacggtgctggttta</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>pKT_Rvb1_R</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>TATTTTTATTTATGAAATGTGCTTTAGGCTTTCTTCACTG tcgatgaattcgagctcg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>pKT_Rvb1_F</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>AAGGTCAACAAAGATTTTAGAAACTTCCGCAAATTATTTG ggtgacggtgctggttta</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>PP7_RE2</td>
      <td>This paper</td>
      <td>PP7 stem loop with NotI/BamHI overhangs</td>
      <td>GATCC TAAGGGTTTCCATATAAACTCCTTAA GC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>PP7_RE1</td>
      <td>This paper</td>
      <td>PP7 stem loop with NotI/BamHI overhangs</td>
      <td>GGCCGC TTAAGGAGTTTATATGGAAACCCTTA G</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Rvb2gRNA_i04rc</td>
      <td>This paper</td>
      <td>Reverse complement gRNA cloning oligo</td>
      <td>gctatttctagctctaaaacGTGTGAATGTACAGTCTTCAtgccaatcgcagctcccaga</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Rvb2gRNA_i04</td>
      <td>This paper</td>
      <td>RVB2 gRNA cloning oligo</td>
      <td>tctgggagctgcgattggcaTGAAGACTGTACATTCACACgttttagagctagaaatagc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Rvb1gRNA_i05rc</td>
      <td>This paper</td>
      <td>Reverse complement gRNA cloning oligo</td>
      <td>gctatttctagctctaaaacTCTCTTCTTCATCACCACGAtgccaatcgcagctcccaga</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Rvb1gRNA_i05</td>
      <td>This paper</td>
      <td>RVB1 gRNA cloning oligo</td>
      <td>tctgggagctgcgattggcaTCGTGGTGATGAAGAAGAGAgttttagagctagaaatagc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>NM637</td>
      <td>This paper</td>
      <td>Primers to extend gRNA oligos for Gibson Assembly ZP479</td>
      <td>gccttattttaacttgctatttctagctctaaaac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>NM636</td>
      <td>This paper</td>
      <td>Primers to extend gRNA oligos for Gibson Assembly ZP479</td>
      <td>ggctgggaacgaaac tctgggagctgcgattggca</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Gsy1_pKTR</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>GCTAAAAGAGTAAGATATGTTAGCAGAAGTTAAGATGGTT tcgatgaattcgagctcg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Gsy1_pKTF</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>CGATGATGACAACGATACGTCTGCATACTACGAGGATAATggtgacggtgctggttta</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>HXK1_pKTR</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>CATTACATTTTTTTCATTAAGCGCCAATGATACCAAGAGAC tcgatgaattcgagctcg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>HXK1_pKTF</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>CTGTTATTGCTGCATTGTCCGAAAAAAGAATTGCCGAAGG ggtgacggtgctggttta</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>HSP26_pKTR</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>GGTCCTCGCGAGAGGGACAACACTATAGAGCCAGGTCACTtcgatgaattcgagctcg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>HSP26_pKTF</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>CAAGAAGATTGAGGTTTCTTCTCAAGAATCGTGGGGTAAC ggtgacggtgctggttta</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>HSP30_pKTR</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>TGTGTTAAGCAAAGAATGATTAAGACAATCTCAAGCTGCTtcgatgaattcgagctcg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>HSP30_pKTF</td>
      <td>This paper</td>
      <td>C-terminal tagging of pKT vector</td>
      <td>ACCCGAACCTGAAGCAGAGCAAGCTGTCGAAGATACTGCTggtgacggtgctggttta</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qMS2-CP-R</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>GTCGGAATTCGTAGCGAAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qMS2-CP-F</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>GCAGAATCGCAAATACACCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qnLuc_R</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>CCTTCATAAGGACGACCAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qnLuc_F</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>TGGTGATCAAATGGGTCAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp12prR</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>GAGCGGGTAACAGATGGAAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp12prF</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>GCGCTGCAAGTTCCTTACTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp104prR</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>ATGAAACTCTCGCCACAACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp104prF</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>AAATGGACTGGATCGACGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp26R</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>ATCATAAAGAGCGCCAGCAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp26F</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>AACAGATTGCTGGGTGAAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGsy1prR</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>GCGGGAAGAAAAGAAGGAGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGsy1prF</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>AGGGCAGACAAGAGGCTGTA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qActR</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>CGGTGATTTCCTTTTGCATT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qActF</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>CTGCCGGTATTGACCAAACT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qTub1prR</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>CGCTAGATGCATTAAACATGAAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qTub1prF</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>GTGCTCACACCAAGCATCAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qAct1prR</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>GAGAGGCGAGTTTGGTTTCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qAct1prF</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>TCACCCGGCCTCTATTTTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGPH1prR</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>TCGTCGGTGTTCCTTCCTTA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGPH1prF</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>GAACGCCTTCCCCAATTAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHxk1prR</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>CCTGGTTGCTCCAGTAAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHxk1prF</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>TTCAGGAAGAATGGCAGTCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGlc3prR</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>TTGCAACAGCCCCTTGGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGlc3prF</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>GGGCACTCATCAACAATGTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp26prF</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>CTGTCAAGGTGCATTGTTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp30prR</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>CGGGATATGGCTTTGCTTAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp30prF</td>
      <td>This study</td>
      <td>qPCR primers</td>
      <td>CGATTTTGTTGGCCATTTTCCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGsy1R</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>GCAGTGATTTGCGACACAGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGsy1F</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>GCCGCTGGTGATGTAGATTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp12R</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>TTGGTTGGGTCTTCTTCACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp12F</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>CGAAAAAGGCAAGGATAACG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp104R</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>CACTTGGTTCAGCGACTTCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp104F</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>CGACGCTGCTAACATCTTGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGph1R</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>TCATAAGCAGCCATGTCATCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGph1F</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>TTCCCCAAGAAATCAAGTCAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qTub1R</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>GGTGTAATGGCCTCTTGCAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qTub1F</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>CCACGTTTTTCCATGAAACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp30R</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>TCAGCTTGAACACCAGTCCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp30F</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>GGGCAGTGTTTGCAGTCTTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGlc3R</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>CGAAATCGCCGTTAGGTAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qGlc3F</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>CAATCCGGAAACCAAAGAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHsp26prF</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>CATAAGGGGGAGGGAATAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qCITCFPf</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>CTGGTGAAGGTGAAGGTGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qCITCFPr</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>TGTGGTCTGGGTATCTAGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHXK1F</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>TTTGTAGCAATGGGACGACA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qHXK1R</td>
      <td>Zid and O’Shea, 2014</td>
      <td>qPCR primers</td>
      <td>GTACCCAGCTTCCCAAAACA</td>
    </tr>
  </tbody>
</table>

### Yeast growth and media

The background yeast strain w303 (EY0690) was used for all experiments. For cells cultured in the functional experiments, cells were streaked out on the yeast extract peptone dextrose (YPD) agarose plate (BD) from the frozen stocks and grew at 30°C for 2 days. Single colony was selected to start the overnight culture for each biological replicate. Cells were grown at 30°C in batch culture with shaking at 200 r.p.m. in synthetic complete glucose medium (SCD medium: yeast nitrogen base from RPI, glucose from Sigma-Aldrich, SC from Sunrise Science). When the OD660 of cells reached 0.4, half of the culture was harvested as the pre-starved sample. The other half of the culture was transferred to the prewarmed synthetic complete medium lacking glucose (SC-G medium) by centrifugation method. Cells are centrifuged at 3000 × g, washed once by SC medium, and resuspended in the same volume as the pre-starvation medium of SC medium. Glucose starvation was performed at the same 200 r.p.m. shaking speed and 30°C. The length of the glucose starvation time varies from 10 min to 30 min depending on the experiments.

### CoTrIP and CoTrIP analysis

The protocol was developed based on Unnikrishnan et al., 2012. ZP64 PRS406-CMV-lacI-FLAG was integrated into the W303 yeast background by linearization within the URA3 gene with BstBI digestion and transformation into yeast. The CoTrIP plasmid was constructed by modifying the ZP66 pUC-TALO8 plasmid that contains eight copies of the Lac operator. The EcoRI sites in ZP66 were mutated to NotI using QuikChange II Site-directed mutagenesis kit (Stratagene). Promoter-specific reporters driving CFP were inserted into pUC-TALO8-NotI by digesting with NheI followed by Gibson Assembly. The plasmid backbone was then digested with NotI, gel purified, ligated, and transformed into yeast using standard lithium acetate transformation. Then, 1 L of yeast were grown overnight in SCD medium-Trp to maintain selection on the CoTrIP plasmid, until an OD660 0.3–0.4. Cells were filtered, washed with SC-G -Trp media, and resuspended in 1 L of prewarmed media and grown at 30°C for 5 min. Cells were then refiltered, resuspended in 4 mL of PBS in a glass Petri dish, and crosslinked using UV from a Stratalinker 1800 (254 nm, 9999 microjoules × 100, 5 cm from the UV bulb). Crosslinked cells were pelleted and resuspended in 2 mL of Buffer H 150 (25 mM HEPES KOH pH 7.6, 2 mM MgCl2, 0.5 mM EGTA, 0.1 mM EDTA, 10% glycerol, 150 mM KCl, 0.02% NP40) plus protease inhibitor (P8215 MilliporeSigma) and then dripped into liquid N2 to be cryogenically ball milled using a Retsch PM100. Ground lysate was clarified by spinning at 3500 × g for 5 min at 4°C, isolating the supernatant and spinning at 12K for 5 min at 4°C. Supernatant was aliquoted and frozen at –80°C. Then, 10 µL of unpacked Anti-FLAG M2 Magnetic Beads (M8823 MilliporeSigma) per sample were pre-washed with Buffer H 150. Then, 300 µL of extract was added to magnetic beads and incubated at 4°C for 3 hr with rotation. Beads were then washed three times with Buffer H 150, three times with Buffer H 300 (300 mM KCl), and once with Buffer H 150. Then, 500 µg/mL 3xFLAG peptide (F4799 MilliporeSigma) was diluted in Buffer H 150 and CoTrIP plasmids were eluted with 100 µL elution buffer with FLAG peptide. Elutions were taken forward for DNA, RNA, and mass spectrometry. Mass spectrometry was performed through the Yeast Resource Center by James Moresco of the Yates lab and was funded through a P41GM103533 Biomedical Technology Resource Center grant. Data-dependent acquisition of MS/MS spectra was performed with an LTQ-Orbitrap. Tandem mass spectra were extracted from raw files using RawExtract 1.9.9 (McDonald et al., 2004) and were searched against a yeast protein database (http://www.yeastgenome.org) using ProLuCID (Peng et al., 2003; Xu et al., 2015). Enrichment analysis was performed using the CRAPome online data analysis software (https://reprint-apms.org/; Mellacheruvu et al., 2013).

### ChIP-sequencing

The protocol was developed based on Grably and Engelberg, 2010. Pgk1-TAP was included as a negative control that should not be bound to chromatin to control for previous effects showing that highly expressed regions are hyper-ChIPable in yeast even with no tag present (Teytelman et al., 2013). Then, 100 mL of yeast were grown overnight in SCD medium, until an OD660 around 0.4. Also, 50 mL of cells were filtered, washed with SC-G media, and resuspended in 50 mL of prewarmed media and grown at 30°C for 10 min. Then, 50 mL of pre-starved and 50 mL of 10 min glucose-starved cell culture was fixed by incubating in the freshly made crosslink buffer (1% formaldehyde, 10 mM NaCl, 0.1 mM EDTA, 5 mM HEPES pH 7.5), respectively, with gentle shaking at room temperature for 15 min. Crosslink was quenched by introducing 0.5 M of glycine for 5 min at room temperature. Cells were harvested by centrifugation at 3000 × g at 4°C, washed twice in the ice-cold TBS buffer (20 mM Tris pH 7.5, 150 mM NaCl). Cells were resuspended in 400 µL of ChIP lysis buffer (50 mM HEPES-KOH pH 7.5, 150 mM NaCl, 1 mM EDTA, 1% Triton X-100, 0.1% sodium deoxycholate, 1 mM PMSF, 0.5% SDS), and lysed by bead-beating (Biospec Products) for 1 min five times. Lysis was verified under microscope. Lysates were sonicated by Covaris Sonicator to ~500 bp fragments (130 µL/tube, 105 PIP, 5% Duty F, 200 cycles/burst, 80 s). Lysates were centrifuged at 15,000 × g at 4°C to remove the cell debris and diluted to 1 mL. Save 10% of the clear lysate to verify the sonication by protein digestion using Pronase, reverse crosslinking, RNA digestion using RNase A, and running the samples on 1% agarose gel. Then, 50 µL of IgG-Dynabeads per sample was used. The protocol of making the IgG-Dynabeads from Dynabeads M-270 Epoxy (Thermo Fisher) was taken from Li, 2011. IgG-Dynabeads were pre-washed three times with ChIP lysis buffer. And 1% of the lysate was saved as the input and for Western blotting, respectively. The IP sample was incubated with IgG-Dynabeads, rotating at 4°C for 4 hr. The IP samples were further washed twice by ChIP lysis buffer with 0.1% SDS, twice by ChIP lysis buffer with 0.1% SDS and 0.5 M NaCl, once by ChIP wash buffer (50 mM Tris pH 7.5, 0.25 mM LiCl, 1 mM EDTA, 0.5% NP-40, 0.5% sodium deoxycholate), and once by TE buffer pH 7.5. Before the last wash, save 10% of the sample for Western blotting. Western blotting was performed to verify the successful enrichment and purification of the protein of interest. Samples were later eluted from beads in 250 µL 2X Pronase buffer (50 mM Tris pH 7.5, 10 mM EDTA, 1% SDS) at 65°C for 10 min and beads were removed. Samples were then digested by 1.6 mg/mL Pronase (20 µL of 20 mg/mL Pronase, Sigma-Aldrich) at 42°C for 2 hr and reverse-crosslinked at 65°C for 6 hr. DNA was extracted from the sample using phenol-chloroform, washed once with chloroform, and pelleted using ethanol, washed twice with 75% ethanol (Sigma-Aldrich), and resuspended in 200 µL TE buffer. DNA sequencing libraries were prepared and sequenced following the NextSeq 500 SR 75 protocol at The UCSD IGM Genomics Center (Illumina).

### ChIP-sequencing analysis

Sequencing reads were demultiplexed and the quality was verified by FastQC (Anders, 2010). The reads were mapped to S288C Saccharomyces cerevisiae genome using Bowtie2 (Langmead and Salzberg, 2012). The mapped reads were then sorted, indexed, and converted into BAM files using SAMtools (Li et al., 2009). Duplicated reads were removed using Picard Tools (Broad Institute, 2009). The genome browser files for visualizing the reads were generated by igvtools and were visualized on Integrative Genomics Viewer by Broad Institute and Sushi.R (Phanstiel et al., 2014; Robinson et al., 2011; Thorvaldsdóttir et al., 2013). Enriched peaks for Rvb1/Rvb2 were called using MACS (Zhang et al., 2008). deepTools was used to calculate and plot the enrichment of Rvb1/Rvb2 on genome and selected genes (Ramírez et al., 2016). The coverage of reads (BigWig files) was calculated from indexed BAM files using bamCoverage. To compare the enrichment of two targets, the matrix was computed from BigWig files of two targets using computeMatrix and further presented as a heatmap by plotHeatmap. To visualize Rvb1/Rvb2’s enrichment, the matrix was computed from BigWig files of the target and S288C genome annotation as the reference using computeMatrix and further presented by plotProfile. Additionally, BEDtools was used to calculate the coverage of regions of interest and a home-made R script was generated to analyze and plot the enrichment of Rvb1/Rvb2 on genome and specific gene groups (Quinlan and Hall, 2010).

### RNA immunoprecipitation (RIP)

The RIP protocol was developed based on the protocol from Van Nostrand et al., 2016; Zander et al., 2016. Also, 100 mL of yeast were grown overnight in SCD medium, until an OD660 around 0.4. Then, 50 mL of cells were filtered, washed with SC-G media, and resuspended in 50 mL of prewarmed media and grown at 30°C for 15 min. Then, 50 mL of pre-starved and 15 min glucose-starved cell culture was washed and resuspended in 10 mL of ice-cold PBS buffer, fixed by UV irradiation on a 10 cm Petri dish using a Stratalinker 1800 (254 nm, 9999 microjoules × 100, 5 cm from the UV bulb), and harvested. Cells were resuspended in 400 µL of ice-cold RIP lysis buffer (50 mM Tris pH 7.5, 100 mM NaCl, 1% NP-40, 0.5% SDS, 0.2 mM PMSF, 1 mM DTT, 10U RNase inhibitor from Promega, cOmplete Protease Inhibitor Cocktail from Roche), and lysed by bead-beating (Biospec Products) for 1 min five times. Bright-field microscopy was used to verify that more than 90% of cells were lysed. The lysates were centrifuged softly at 1000 × g at 4°C for 10 min to remove cell debris and diluted to 500 µL. Clear lysates were treated with 5U RQ1 DNase and 5U RNase inhibitor (Promega) at 37°C for 15 min. Then 1% of the lysate was saved as the input and for Western blotting, respectively. Also, 50 µL of IgG-Dynabeads per sample was used. The protocol of preparing the IgG-Dynabeads from Dynabeads M-270 Epoxy (Thermo Fisher) was taken from Li, 2011. IgG-Dynabeads were pre-washed three times with RIP lysis buffer. The IP samples were incubated with IgG-Dynabeads, rotating at 4°C for 4 hr. The IP samples were further washed six times by RIP wash buffer (50 mM Tris pH 7.5, 100 mM NaCl, 0.1% NP-40) at 4°C. Samples were later eluted from the beads in 100 µL of PK buffer (100 mM Tris pH 7.5, 50 mM NaCl, 10 mM EDTA) at 65°C for 15 min and later the proteins were digested by 10U Proteinase K (NEB) at 37°C for 30 min. Digestion was later activated by incubation with urea (210 mg/mL) at 37°C for 20 min. RNA was extracted using TRIzol reagent (Thermo Fisher) according to the vendor’s protocol. RNA was washed twice by 70% EtOH and eluted in 10 µL of RNase-free water. RNA samples were further digested fully by RQ1 DNase (Promega) in 10 µL system and were reverse transcribed by ProtoScript II reverse transcriptase (NEB) (a 1:1 combination of oligo dT18 and random hexamers was used to initiate reverse transcription). The cDNA was investigated by RT-qPCR.

### Live-cell microscopy and analysis

Cells were grown to an OD660 to ~0.4 in SCD medium at 30°C and glucose-starved in SC-G medium for 15 and 30 min. Then, 100 µL of cell culture was loaded onto a 96-well glass-bottom microplate (Cellvis). Cells were imaged using an Eclipse Ti-E microscope (Nikon) with an oil-immersion ×63 objective. Imaging was controlled using NIS-Elements software (Nikon). Imaging analysis was performed on Fiji software.

### Nanoluciferase assay and analysis

The nanoluciferase (nLuc) assay was adapted from methods previously described by Masser et al., 2016. Cells were grown to an OD660 to ~0.4 in SCD medium at 30°C and glucose-starved in SC-G medium for 30 min. Then, 90 µL of cell culture was loaded onto a Cellstar non-transparent white 96-well flat-bottom plate (Sigma-Aldrich). OD660 of cells was taken for each sample. For cells treated with cycloheximide (CHX), CHX was added to a final concentration of 100 µg/mL to stop the translation for 5 min. To measure the nanoluciferase signal, 11 µL of substrate mix (10 µL of Promega Nano-Glo Luciferase Assay Buffer, 0.1 µL of Promega NanoLuc luciferase substrate, and 1 µL of 10 mg/mL CHX) was added and mixed with the samples by pipetting. Measurements were taken immediately after addition of substrate mix by Tecan Infinite Lumi plate reader. To analyze the data, the luciferase level of samples was firstly divided by the OD660 level of the samples. Then the normalized luciferase level of non-CHX-treated sample was further normalized by subtracting the luciferase level of CHX-treated sample. For glucose readdition experiments, cells were starved for 30 min and then 2% glucose was added back to the cultures and then the luciferase production was followed over a 10 min period.

### RVB2 CRISPRi knockdown

RVB2 gRNA forward and reverse complement oligos were annealed together and then further extended using NM637 and NM636. This PCR product was inserted into the TetO gRNA vector pNTI661 by digesting this vector with BamHI/HindIII as described previously (McGlincy et al., 2021). Cells were grown overnight in SC-Leu+Glu media to low OD < 0.5. Cells were diluted and 250 ng/L of ATc was added to the experimental sample and control and experimental samples were allowed to grow for 8 hr to an OD ~0.4. Yeast were either prepped for assays or glucose-starved for 30 min and then prepped for nLuc and RT-qPCR assays.

### Western blotting

The Western blotting protocol was adapted from Tsuboi et al., 2020. IP and input samples were mixed with the same volume of 2X Laemmli buffer (Bio-Rad) and were boiled at 95°C for 10 min. The samples were then resolved by SDS-PAGE (Bio-Rad), and a rabbit polyclonal antibody specific for calmodulin-binding peptide (A00635-40, GenScript), a Goat anti-Rabbit IgG (H+L) Secondary Antibody, HRP (Thermo Fisher), and SuperSignal West Femto Maximum Sensitivity Substrate (Thermo Fisher) were used to detect TAP-tagged proteins. The blotting was imaged using a Gel Doc XR+ Gel Documentation System (Bio-Rad).

### Real-time quantitative PCR

The RT-qPCR protocol was adapted from Tsuboi et al., 2020. RNA was extracted using the MasterPure Yeast RNA Purification Kit (Epicentre). cDNA was prepared using ProtoScript II Reverse Transcriptase (NEB #M0368X) with a 1:1 combination of oligodT 18 primers and random hexamers (NEB) according to the manufacturer’s instructions. mRNA abundance was determined by qPCR using a home-brew recipe with SYBR Green at a final concentration of 0.5× (Thermo Fisher #S7564). Primers specific for each transcript are described in Key resources table. The mRNA levels were normalized to ACT1 abundance, and the fold change between samples was calculated by a standard ∆∆Ct analysis. All data were included except for one sample that had high technical variation, and another that had very high ACT1 CT values. Both samples were flagged as analysis began.

### Mathematical modeling on the mRNA induction

The mathematical modeling method was adapted from Elkon et al., 2010 and performed in Python Jupyter Notebook (https://jupyter.org/). To accurately describe the dynamics of induced mRNA transcription, we used an ordinary differential equation as follows:

$$
\frac{dX}{dt}=\beta-\alphaX
$$

where X is the mRNA concentration, α is the degradation constant, and β is the transcription rate.

We assumed that transcription and degradation rates play essential roles in shaping the overall curve of mRNA increase, and these parameters stay constant over the course of induced expression. We then hypothesized that Rvb1/Rvb2 binding to mRNAs could either increase β or decrease α, leading to greater mRNA abundance than the PP7 control. To observe the effects of varied transcription or degradation rates on the mRNA abundance, we solved the differential equations with different parameters using ODEINT algorithm, and generated time profiles of the mRNA fold in log2 scale. Solution to the differential equation was expressed as the following function of change in X with respect to time:

$$
ΔXt=(\frac{\beta}{\alpha}-X_{0})(1-e^{-\alphat})
$$

where X0 is the mRNA level at t = 0, the initial time of mRNA induction. Since the degradation rate was proportional to the mRNA concentration, we expected the curves to have a steady increase, followed by a gradual leveling off where the mRNA concentrations stay constant over time. Closer look at the differential equation showed that at steady state (dX/dt = 0) the mRNA concentration is determined by the ratio of β to α:

$$
X_{ss}=\frac{\beta}{\alpha}
$$

whereas for the time it takes for the curve to transition into steady state, inversely proportional to the degradation constant, is given by

$$
T_{1/2}=ln⁡(\frac{2}{\alpha})
$$

Thus, we showed that for a log-log plot, the expected shape of the curves can be altered by varying α and β. At constant α, increasing β would only shift the curve up, while at constant β, increasing α would cause the mRNA abundance to enter steady state more rapidly. Through the comparison between mathematical modeling and experimental data, we could infer the actual effects of Rvb1/Rvb2 binding to mRNA on the transcription and decay rates.

### Ribosome profiling

The ribosome profiling protocol was adapted from Zid and O’Shea, 2014. Yeast was grown in SCD to an OD660 between 0.3 and 0.4. Then, cells were collected by filtration, resuspended in SC-G medium. After 15 min, 2% glucose was added back. CHX was added to a final concentration of 0.1 mg/mL for 1 min, and cells were then harvested. Cells were pulverized in a PM 100 ball mill (Retsch), and extracts were digested with RNase I followed by the isolation of ribosome-protected fragments by purifying RNA from the monosome fraction of a sucrose gradient. Isolated 28-base sequences were polyadenylated, and reverse transcription was performed using OTi9pA. OTi9pA allowed samples to be multiplexed at subsequent steps. RNA-seq was performed on RNA depleted of rRNA using a yeast Ribo-Zero kit (Epicentre). Samples were multiplexed and sequenced on a HiSeq analyzer (Illumina).

To analyze the ribosomal profiling and RNA-seq sequences, reads were trimmed of the 39 run of poly(A)s and then aligned against S. cerevisiae rRNA sequences using Bowtie sequence aligner (Langmead and Salzberg, 2012). Reads that did not align to rRNA sequences were aligned against the full S. cerevisiae genome. Reads that had an unambiguous alignment with less than three mismatches were used in the measurements of ribosome occupancy and mRNA levels. Since there were many reads mapping to the initiation region (216 bp to 120 bp in relation to the AUG), the ribosome occupancy for each mRNA was calculated by taking the total number of ribosome reads (normalized to the total number of aligned reads in reads per million reads [RPM]) in the downstream region (120 bp from the AUG to the end of the ORF) and dividing this by the number of mRNA reads (RPM) in the same region. The ribosome occupancy along the mRNA was calculated by dividing the ribosome read counts at each base pair along the gene by the average number of mRNA reads per base pair for each gene.
