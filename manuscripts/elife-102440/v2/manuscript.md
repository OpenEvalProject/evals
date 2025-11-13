# Evaluating the transcriptional regulators of arterial gene expression via a catalogue of characterized arterial enhancers

## Authors

- Svanhild Nornes<sup>1</sup> ([ORCID: 0000-0002-5301-5252](https://orcid.org/0000-0002-5301-5252))
- Susann Bruche<sup>1</sup> ([ORCID: 0000-0002-5814-7166](https://orcid.org/0000-0002-5814-7166))
- Niharika Adak<sup>1</sup>
- Ian R McCracken<sup>1</sup>
- Sarah De Val<sup>1</sup> ([ORCID: 0000-0002-2566-2348](https://orcid.org/0000-0002-2566-2348)) †

### Affiliations

1. Institute of Developmental and Regenerative Medicine, Department of Physiology, Anatomy and Genetics Oxford United Kingdom ([ROR:05t17k830](https://ror.org/05t17k830))
2. University Medical Centre Groningen Groningen Netherlands ([ROR:03cv38k47](https://ror.org/03cv38k47))
3. Ludwig Institute for Cancer Research Ltd, Nuffield Department of Medicine, University of Oxford Oxford United Kingdom ([ROR:01e473h50](https://ror.org/01e473h50))

† Corresponding author

## Abstract

The establishment and growth of the arterial endothelium require the coordinated expression of numerous genes. However, regulation of this process is not yet fully understood. Here, we combined in silico analysis with transgenic mice and zebrafish models to characterize arterial-specific enhancers associated with eight key arterial identity genes (Acvrl1/Alk1, Cxcr4, Cxcl12, Efnb2, Gja4/Cx37, Gja5/Cx40, Nrp1, and Unc5b). Next, to elucidate the regulatory pathways upstream of arterial gene transcription, we investigated the transcription factors binding each arterial enhancer compared to a similar assessment of non-arterial endothelial enhancers. These results found that binding of SOXF and ETS factors was a common occurrence at both arterial and pan-endothelial enhancers, suggesting neither are sufficient to direct arterial specificity. Conversely, FOX motifs independent of ETS motifs were over-represented at arterial enhancers. Further, MEF2 and RBPJ binding was enriched but not ubiquitous at arterial enhancers, potentially linked to specific patterns of behaviour within the arterial endothelium. Lastly, there was no shared or arterial-specific signature for WNT-associated TCF/LEF, TGFβ/BMP-associated SMAD1/5 and SMAD2/3, shear stress-associated KLF4, or venous-enriched NR2F2. This cohort of well-characterized and in vivo-verified enhancers can now provide a platform for future studies into the interaction of different transcriptional and signaling pathways with arterial gene expression.

## Introduction

The blood vessel system consists of a highly branched network of tubes lined by endothelial cells (ECs) and hierarchically organized into arteries, veins, and capillaries. The EC layer is the first part of the blood vessel to form, initially via differentiation from mesoderm (vasculogenesis) and later from existing ECs (angiogenesis) (Payne et al., 2024). While the first arterial ECs arise during vasculogenesis (Chong et al., 2011), single-cell transcriptomics and fate-mapping experiments spanning humans, mice, and zebrafish indicate that most arterial ECs form via angiogenesis from venous and venous-like capillary ECs (Su et al., 2018; Hou et al., 2022; McCracken et al., 2022; Lee et al., 2021; Xu et al., 2014; Fujita et al., 2011; Kaufman et al., 2015; Marín-Juez et al., 2016; McCracken et al., 2023). During this process, a subset of ECs reduce cell-cycling and venous gene transcription, induce arterial gene expression, and migrate against flow to form into new arteries or extend existing ones. While significant alterations to gene transcription occur during this transition, the precise mix of hardwired signalling pathways and environmental stimuli regulating the differentiation of arterial ECs has been challenging to untangle and identify.

Many components of Notch signalling are selectively expressed in arterial ECs and are essential for arterial formation (e.g. the DLL4 ligand) (Quillien et al., 2014). However, the assumed model of Notch signalling directly activating arterial gene expression has recently been challenged by new evidence. In particular, retinal and coronary vessels lacking both endothelial MYC (a driver of metabolism and proliferation) and RBPJ (the nuclear effector of Notch signalling) can still express arterial genes and form arterial structures (Luo et al., 2021). This research led to a new paradigm in which Notch drives arterial EC differentiation by reducing metabolism and cell-cycle rather than by directly activating arterial genes (Luo et al., 2021). However, cell-cycle changes alone do not necessarily alter arterial identity, and Myc loss in retinal EC does not affect arterial patterning (Wilhelm et al., 2016). Therefore, Notch-mediated cell-cycle exit likely works alongside other regulators which directly control arterial gene transcription, while the precise role of Notch in directing arterial gene expression remains unclear.

Although numerous other regulatory pathways have been implicated in arterial transcriptional regulation, their exact contribution has been challenging to establish and none appear essential for arterial EC identity (McCracken et al., 2023). Both canonical WNT and TGFβ/BMP signalling pathways have been implicated in arterialization yet ECs lacking β-catenin or SMAD4 still express arterial genes and form arterial structures (Neal et al., 2019; Wythe et al., 2013). Likewise, blood flow is required for full expression of arterial genes, yet arteries in both early embryonic and coronary vasculatures form prior to blood flow (Su et al., 2018; Lee et al., 2021; Fang et al., 2017; Hwa et al., 2017). Our knowledge of the transcription factors activating arterial gene expression is also incomplete. ETS factors are required for arterial gene activity but are also essential for vein-specific and pan-endothelial gene expression, suggesting a more general requirement for endothelial identity (Neal et al., 2021). The link between FOXC factors and arteries was partially predicated on binding to Dll4 regulatory regions later found to lack arterial activity (Wythe et al., 2013). DACH1 potentiates arterial differentiation but is widely expressed and cannot alter EC identity (Raftrey et al., 2021), while arterial-enriched MECOM is linked to repression of venous gene expression rather than activation of arterial identity genes (McCracken et al., 2022). The evidence linking SOXF transcription factors to arterial differentiation is more extensive, with loss of either SOX17 (the SOXF factor most specific to arterial ECs) or SOX7 resulting in arterial defects (Lilly et al., 2017; Kim et al., 2016; Corada et al., 2013; Zhou et al., 2015). Whilst losing a single SOXF factor does not entirely compromise the arterial programme, arterial differentiation appears absent after compound Sox17;Sox18 and Sox7;Sox17;Sox18 deletion, although this occurs alongside significantly impaired angiogenesis and severe vascular hyperplasia (Lilly et al., 2017; Kim et al., 2016; Corada et al., 2013; Zhou et al., 2015). Additionally, the manner in which SOXF factors contribute to the specific activation of arterial genes is still unknown: while SOX17 is considered arterial-specific by late fetogenesis, both SOX7 and SOX18 are more widely expressed, and all SOXF factors bind the same motifs (Francois et al., 2010). It is also unclear whether SOXF factors primarily act upstream of Notch signalling (and subsequent cell-cycle-related control of arterial differentiation), or whether they more widely activate arterial gene expression. Direct SOXF binding is best characterized at Notch pathway enhancers Dll4in3, Dll4-12, and Notch1+16, and the arterial defects seen after Sox17 deletion were attributed to a requirement for SOX17 in activation of Notch1 and Dll4 (Payne et al., 2024; Corada et al., 2013; Sacilotto et al., 2013). However, SOXF motifs are also required for the activity of the arterial-specific ECE1in1 enhancer and are associated with coronary arterial Nestin expression (González-Hernández et al., 2020; Robinson et al., 2014).

In this article, we identify a cohort of arterial enhancers associated with eight key arterial identity genes, combining in silico analysis with verification and characterization in transgenic models. We then use sequence analysis and DNA-protein binding surveys to investigate the involvement of many endothelial- and arterial-associated transcription factors in arterial enhancer binding, and to compare this pattern with that seen at pan-endothelial and venous enhancers. Our results indicate that ETS and SOXF factors play a general role in endothelial gene transcription, suggest a role for FOX factors more selectively in arterial activation, and link both RBPJ and MEF2 factors to a limited number of arterial genes, potentially related to specific expression patterns. This cohort of well-characterized, in vivo-verified enhancers can also now be used as a platform for future studies into the interaction of different transcriptional and signalling pathways with specific arterial genes and with subtype-specific gene expression within the endothelium more generally. Additionally, our data provides a useful training set for attempts to more accurately classify endothelial enhancers genome-wide.

## Results

### In silico identification of putative enhancers for key arterial identity genes

Transcription factors primarily regulate endothelial gene transcription through binding to enhancers (cis-regulatory elements) (Payne et al., 2024). Consequently, analysis of enhancer sequences can elucidate the precise combination of transcription factors, and cognate upstream signalling pathways, involved in different patterns of gene expression. One of the main challenges in understanding arterial regulation has been a paucity of characterized enhancers for key arterial genes. For example, of the 16 genes used to define mouse coronary arterial EC identity in single-cell transcriptomics (Raftrey et al., 2021), only four have in vivo-verified enhancers (Dll4, Hey1, Notch1, and Acvrl1). Three of these are genes in the Notch pathway and are either self-regulated by Notch/RBPJ (Dll4-12 and Hey1-18) (Sacilotto et al., 2013; Watanabe et al., 2020) or lack specificity during early coronary arterial specification (Notch1+16) (Payne et al., 2019). The fourth enhancer, for Acvrl1, is of a size (9 kb) that precludes analysis (Seki et al., 2004). Beyond this, there are only four other in vivo-validated arterial enhancers described in the literature, for Ece1, Flk1, Sema6d, and Sox7. Of these, only the Ece1in1 and Flk1in10 arterial enhancers, both associated with genes not specific to arterial ECs, have been analysed at the level of transcription factor binding (Robinson et al., 2014; Zhou et al., 2017). It is therefore clear that a better understanding of the regulatory pathways directing arterial differentiation requires the identification and characterization of a larger number of arterial enhancers orchestrating the expression of key arterial identity genes. To identify a cohort of such enhancers, we looked in the loci of eight non-Notch genes: Acvrl1(ALK1) Cxcr4, Cxcl12, Efnb2, Gja4(CX37), Gja5 (CX40), Nrp1, and Unc5b. Although not a definitive list of arterial identity genes, single-cell transcriptomic analysis indicates these genes are all significantly enriched in arterial ECs (Hou et al., 2022; Raftrey et al., 2021), and they are commonly used to define arterial EC populations in mouse and human scRNAseq analysis (Hou et al., 2022; McCracken et al., 2022; Raftrey et al., 2021; Phansalkar et al., 2021). Additionally, the genes selected here are also equally split between the two arterial subgroups identified by single-cell transcriptomics: Cxcr4, Efnb2, Gja4, and Unc5b included in the earlier expressed arterial plexus/pre-arterial EC subgroup, Acvrl1, Cxcl12, Gja5, and Nrp1 restricted to the mature arterial EC subgroup (Hou et al., 2022; Raftrey et al., 2021). We did not exclude genes implicated in angiogenesis/expressed in sprouting ECs as these overlapped with genes within the pre-arterial EC subgroup.

To identify putative enhancers in silico, we used five published datasets detailing different enhancer-associated chromatin marks: (i) open chromatin as assessed by ATAC-seq in primary mouse adult aortic ECs (MAECs) from Engelbrecht et al., 2020; (ii) open chromatin as assessed by ATAC-seq in mouse postnatal day 6 (P6) retina ECs (MRECs) from Yanagida et al., 2020; (iii) enriched EP300 binding in Tie2Cre+ve cells from embryonic day (E) 11.5 mouse embryos from Zhou et al., 2017; (iv) enriched H3K27Ac and/or H3K4Me1 in human umbilical vein ECs (HUVECs, data available on the UCSC Genome Browser; Rosenbloom et al., 2013); and (v) open chromatin regions assessed by DNAseI hypersensitivity in HUVECs and dermal-derived neonatal and adult blood microvascular ECs (HMVEC-dBl-neo/ad) comparative to non-ECs (UCSC Genome Browser; Rosenbloom et al., 2013; Figure 1). A retrospective analysis of 32 previously described mammalian in vivo-validated EC enhancers (Payne et al., 2024), which included eight arterial enhancers, found that 31/32 were marked by at least one enhancer mark in both human and mouse samples (including 8/8 of arterial enhancers) (see Table 1). We analysed the loci of our target arterial genes to identify putative enhancers using these enhancer marks. For arterial genes robustly transcribed in both human and mouse EC datasets (determined by open chromatin/H3K4Me3 at the promoter region), we defined a putative enhancer as a region containing at least one enhancer mark in both mouse and human ECs. Because Cxcr4, Cxcl12, and Gja5 were poorly transcribed in the human cell lines studied here, for these genes the putative enhancer definition was relaxed to include regions containing two enhancer marks in mouse ECs with no marks in human cells. Orthologous human enhancer sequences were identified for every enhancer using the Vertebrate Multiz Alignment & Conservation Track on the UCSC Genome Browser. Each putative enhancer was named according to their neighbouring arterial gene and distance from the transcriptional start site (TSS) in mice (e.g. the putative Efnb2-112 enhancer is 112 kb upstream of the mouse Efnb2 TSS). In total, this analysis considered over 110 regions and identified 41 putative enhancers for further testing (Figure 1, Table 2—source data 1). We also assessed seven regions previously identified as potential enhancers for Efnb2, Nrp1, and Cxcr4 but whose independent activity was never validated in vivo (Grego-Bessa et al., 2007; Yamamizu et al., 2010; Tsaryk et al., 2022; Stewen et al., 2024). None of these met our putative enhancer threshold for further testing: two regions were associated with no enhancer marks, three had a single enhancer mark in HUVECs, one had non-specific enhancer marks in human cells only (Nrp1+76/NRP1A; Yamamizu et al., 2010) and one contained enhancer marks in human ECs only (Cxcr4-117/CXCR4+125; Tsaryk et al., 2022; Figure 1, Table 2—source data 1).

![Figure 1.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig1-v2.jpg)

**Figure 1.:** Enhancer marks from mouse tissue include: dark red ‘ATAC adult artery EC’ denotes open chromatin assessed by ATAC-seq in primary adult aortic endothelial cells (ECs) Engelbrecht et al., 2020; bright red ‘ATAC P6 EC’ denotes open chromatin assessed by ATAC-seq in postnatal day 6 retinal ECs Yanagida et al., 2020; orange ‘EP300 E11 EC’ denotes enriched EP300 binding in Tie2Cre+ve cells in embryonic day 11.5 embryos (Zhou et al., 2017). Enhancer marks from human cells include: light blue peaks denotes enriched H3K27Ac and H3K4Me1 in human umbilical vein ECs (HUVECs) (UCSC Genome Browser; Rosenbloom et al., 2013); grey heat map denotes open chromatin regions assessed by DNAseI hypersensitivity in HUVECs (upper line) and dermal-derived neonatal and adult blood microvascular ECs (HMVEC-dBl-neo/ad, middle and bottom line) (UCSC Genome Browser). Red, pink, and orange solid boxes indicate regions fitting putative enhancers criteria and selected for analysis (red/pink/orange indicates strong/weak/silent EC activity in transgenic models, see Table 2 and Figures 2 and 3). Numbers represent approximate distance from TSS. Orange dashed boxes indicates regions below the putative enhancer threshold but included in transgenic assays as controls, grey boxes indicate regions below the putative enhancer threshold and not tested. * indicates that enhancer marks were not specific for ECs but rather found in many cell types.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** This enhancer was first reported in Sacilotto et al., 2013 but not tested in zebrafish. (A) The Dll4-12:GFP transgene directs arterial endothelial cell expression in mosaic F0 (upper) and stable F1 (middle) transgenic zebrafish at 2 days post fertilization (dpf), arterial specificity is confirmed at 3 dpf by crossing with tg(kdrl:HRAS-mCherry) (lower two panels). Grey dashed box specifies region of zoom, a indicates dorsal aorta, v indicates cardinal vein, * indicates intersegmental vessels, and n indicates neural tube expression. (B) The mouse Dll4-12:LacZ transgene directs arterial expression in a stable transgenic line. Representative whole-mount embryos from the Dll4-12:lacZ transgenic line show reporter gene expression (X-gal staining, blue) in the vasculature from embryonic day 9.5 (E9.5) to E15.5.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Example of the expression of known pan-EC (kdrl1:HRAS-mCherry) (Chi et al., 2008), arterial (Dll4in3:GFP; Sacilotto et al., 2013), and vein (CoupTFII-965:GFP; Neal et al., 2019) enhancers in 2 dpf zebrafish. (B) Two representative F0 transgenic zebrafish expressing each of the 15 new strong arterial enhancers alongside a schematic of each transgene. Grey dashed box indicates region of zoom, a indicates dorsal aorta, v indicates cardinal vein, white arrow indicates intersegmental vessels, * indicates expression in neural tube, and # indicates expression in muscle fibres.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A,, B) The Unc5b-57:GFP transgene is expressed in the vasculature when investigated in either F0 Tol2 transgenic zebrafish (A) or F1/2 stable transgenic zebrafish (B). Crossing with the kdrl:HRAS-mCherry transgene demonstrates that Unc5b-57:GFP expression is restricted to venous locations towards the anterior of the fish. (C) Expression pattern driven by the three ‘weak’ enhancers identified in our F0 mosaic Tol2 transgenic zebrafish screen. Grey dashed box indicates region of zoom, a indicates dorsal aorta, v indicates cardinal vein, white arrows indicate intersegmental vessels, * indicates expression in neural tube, and # indicates expression in muscle fibres. (D) The Cxcr4-117:GFP transgene directs very limited reporter gene expression in transgenic zebrafish. The six transgenic zebrafish shown exhibited the greatest level of GFP expression seen in all injected zebrafish. Grey dashed box indicates region of zoom. (E) Expression pattern of the Efnb2-159 and Efnb2-112 enhancer:GFP transgenes in 4-week-old juvenile zebrafish fins. Grey dashed box indicates regions of zoom, a fin artery, and v fin vein.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** These are shown relative to the enhancer marks in human vein-origin and microvascular-origin ECs used to originally identify putative arterial enhancers in Figure 1. Red and orange boxes denote the regions identified as putative enhancers in original analysis, grey boxes denote regions below threshold, and numbers represent approximate distance from TSS in mouse sequence. * indicates that enhancer marks were not specific for ECs but rather found in many cell types. Enhancer marks in human vein-origin and microvascular-origin ECs used in original analysis: light blue peaks denote enriched H3K27Ac and H3K4Me1 in human umbilical vein ECs (HUVECs), data from the UCSC Genome Browser Hou et al., 2022; grey heat map denotes open chromatin regions assessed by DNAseI hypersensitivity in HUVECs (upper line) and dermal-derived neonatal and adult blood microvascular ECs (HMVEC-dBl-neo/ad, middle and bottom line) from the UCSC Genome Browser (Hou et al., 2022). Enhancer marks in human arterial-origin ECs are all shaded green, including very dark green ‘HAEC ATAC-seq’ denoting open chromatin assessed by ATAC-seq in human aortic ECs from Hogan et al., 2017; dark green ‘telo-HAEC ATAC-seq’ denoting open chromatin assessed by ATAC-seq in immortalized human aortic ECs from Schnitzler et al., 2024; green ‘HAEC H3K27Ac’ denoting enriched H3K27Ac enhancer marks in human aortic ECs from Hogan et al., 2017; bright green ‘HUAEC H3K27Ac’ denoting enriched H3K27Ac enhancer marks in human umbilical aortic ECs from Sissaoui et al., 2020; and lime green ‘HUAEC p300’ denoting enriched p300 binding peaks in human umbilical aortic ECs from Sissaoui et al., 2020.

**Table 1.**
 Enhancer marks around 32 known in vivo-characterized endothelial enhancers (all described in Payne et al., 2024).Red text indicates arterial enhancers.


<table>
  <thead>
    <tr>
      <th>Enhancer</th>
      <th>hg19 coordinates</th>
      <th>H DNAseI</th>
      <th>H histone</th>
      <th>Mm9 coordinates</th>
      <th>M artery ATAC</th>
      <th>M retina ATAC</th>
      <th>M E11 p300</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Apln+28</td>
      <td>chrX:128,756,756–128,757,160</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chrX:45,359,306–45,359,632</td>
      <td>No</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Dab2-240</td>
      <td>chr5:39,755,997–39,756,596</td>
      <td>Yes*</td>
      <td>Yes</td>
      <td>chr15:6,009,719–6,010,138</td>
      <td>No</td>
      <td>No</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Dll4in3</td>
      <td>chr15:41,222,881–41,223,570</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr2:119,152,838–119,153,684</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Dll4-12</td>
      <td>chr15:41,210,706–41,211,825</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr2:119,140,274–119,141,353</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Ece1in1</td>
      <td>chr1:21,606,038–21,607,057</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr4:137,475,719–137,476,738</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Egfl7-9</td>
      <td>chr9:139,540,750–139,541,299</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr2:26,427,513–26,427,707</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Egfl7-2</td>
      <td>chr9:139,550,292–139,550,891</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr2:26,434,087–26,434,301</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Emcn-22</td>
      <td>chr4:101,460,885–101,461,224</td>
      <td>No</td>
      <td>Yes</td>
      <td>chr3:136,984,547–136,984,951</td>
      <td>Yes</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <td>Eng-8</td>
      <td>chr9:130,624,538–130,624,804</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr2:32,493,606–32,493,823</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Eng +9</td>
      <td>chr9:130,607,199–130,607,657</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr2:32,511,282–32,511,641</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Ephb4-2</td>
      <td>chr7:100,426,337–100,427,259</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr5:137,789,910–137,790,581</td>
      <td>No</td>
      <td>No</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Fli1+12</td>
      <td>chr11:128,575,436–128,575,782</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr9:32,337,295–32,337,538</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Flk1+3</td>
      <td>chr4:55,987,345–55,987,920</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr5:76,370,627–76,371,056</td>
      <td>No</td>
      <td>No</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Flk1in10</td>
      <td>chr4:55,972,978–55,973,903</td>
      <td>Yes</td>
      <td>No</td>
      <td>chr5:76,357,891–76,358,715</td>
      <td>No</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Flt4+26</td>
      <td>chr5:180,050,291–180,050,684</td>
      <td>No</td>
      <td>Yes</td>
      <td>chr11:49,445,777–49,446,175</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Foxp1+138</td>
      <td>chr3:71,493,515–71,493,886</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr6:99,338,958–99,339,515</td>
      <td>No</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Gata2+9</td>
      <td>chr3:128,201,971–128,202,273</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr6:88,153,077–88,153,386</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Hey1-18</td>
      <td>chr8:80,695,610–80,697,109</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr3:8,685,099–8,685,821</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Hlx-3</td>
      <td>chr1:221,049,978–221,050,354</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr1:186,558,918–186,559,303</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Mef2F10</td>
      <td>chr5:88,110,980–88,111,253</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr13:83,721,761–83,722,057</td>
      <td>No</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Mef2F7</td>
      <td>chr5:88,123,031–88,123,357</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr13:83,711,180–83,711,509</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Notch1+16</td>
      <td>chr9:139,424,543–139,424,953</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr2:26,346,100–26,346,671</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Notch1+33</td>
      <td>chr9:139,406,356–139,406,655</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr2:26,330,559–26,330,785</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>CoupTFII-965</td>
      <td>chr15:95,908,708–95,909,240</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr7:78,456,407–78,456,767</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Nrp1+28</td>
      <td>chr10:33,590,960–33,591,499</td>
      <td>No</td>
      <td>Yes</td>
      <td>chr8:130,911,132–130,911,551</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Nrp2+26</td>
      <td>chr2:206,573,202–206,573,523</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr1:62,776,231–62,776,553</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Pdgfrb +18</td>
      <td>chr5:149,516,883–149,517,356</td>
      <td>No</td>
      <td>Yes</td>
      <td>chr18:61,219,244–61,219,566</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <td>Epcr-5</td>
      <td>chr20:33,754,176–33,754,585</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr2:155,568,588–155,569,127</td>
      <td>Yes</td>
      <td>No</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Sema6d-55</td>
      <td>chr15:47,958,023–47,958,764</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr2:124,380,522–124,381,285</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Sox7+14</td>
      <td>chr8:10,573,085–10,574,291</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr14:64,576,271–64,577,533</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Tal +19</td>
      <td>chr1:47,677,539–47,677,958</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>chr4:114,748,131–114,748,530</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Tal1-4</td>
      <td>chr1:47,701,050–47,701,347</td>
      <td>No</td>
      <td>Yes</td>
      <td>chr4:114,725,243–114,725,552</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>

_* “H DNAseI” indicates open chromatin regions as defined by DNAseI hypersensitivity in HUVECs, HMVEC-dBl-neo and HMVEC-dBl-ad comparative to non-ECs and relative to surrounding region (UCSC genome browser38); “H histone” indicates relatively enriched binding of H3K27Ac and/or H3K4Me1 in HUVECs (UCSC genome browser38), * indicates this extends to many non-EC lines as well; “M artery ATAC” indicates regions of relatively open chromatin assessed by ATAC-seq in primary mouse adult aortic ECs (MAECs) (Engelbrecht et al35); “M retina ATAC” indicates regions of relatively open chromatin assessed by ATAC-seq in mouse postnatal day 6 (P6) retina ECs (MRECs) (Yanagida et al36); “M E11 p300” indicates regions relatively enriched for EP300 binding in Tie2Cre+ve cells from embryonic day (E)11.5 mouse embryos (Zhou et al37). * indicates that enhancer marks were not specific for ECs but rather found in many cell types.‘M artery ATAC’ indicates regions of relatively open chromatin assessed by ATAC-seq in primary mouse adult aortic ECs (MAECs) Engelbrecht et al., 2020; ‘M retina ATAC’ indicates regions of relatively open chromatin assessed by ATAC-seq in mouse postnatal day 6 (P6) retina ECs (MRECs) Yanagida et al., 2020; ‘M E11 p300’ indicates regions relatively enriched for EP300 binding in Tie2Cre+ve cells from embryonic day (E) 11.5 mouse embryos (Zhou et al., 2017). *indicates that enhancer marks were not specific for ECs but rather found in many cell types._

**Table 2.**
 Summary of putative enhancer activity in mosaic Tol2 transgenic zebrafish.‘In vivo classification’ indicates the results of this screen, ‘in silico classification’ indicates designation from dataset from Sissaoui et al., 2020, as defined by relative enhancer and promoter marks in HUVECs vs. HUAECs.Table 2—source data 1.Enhancer marks in different human and mouse ECs at putative enhancer regions within the loci of eight arterial genes.‘Selected’ indicates that the region meets our threshold as a putative enhancer, ‘exception’ indicates region did not meet our threshold but was included in transgenic analysis as a control (grey text). Numbers indicate approximate distance from the TSS of the named arterial gene. * indicates that enhancer mark was widely seen beyond endothelial cells. Grey italic text refers to regions previously implicated in enhancer activity, with the /enhancer name ascribed in the original reference. Cxcr4-117/CXCR4-125 is from Tsaryk et al., 2022 ; Cxcr4-1, Nrp1- 1/NRP1A and Nrp1+76/NRP1B are from Yamamizu et al., 2010 ; Efnb2+17/EFNB2A and Efnb2+25/EFNB2B are from Grego-Bessa et al., 2007; and Efnb2+4/EFNB2R1 and Efnb2+28/EFNB2R4 are from Stewen et al., 2024.Table 2—source data 2.Genome locations for all enhancer (and human orthologues) investigated in this paper.Values given for mm10 represent the core enhancer regions analysed for motif sequences and protein binding.


<table>
  <thead>
    <tr>
      <th>Enhancer</th>
      <th># Injected/# any EC GFP</th>
      <th>In vivo classification</th>
      <th>In silico classification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cxcr4-232</td>
      <td>163/0</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Cxcr4-194</td>
      <td>46/25</td>
      <td>Arterial enhancer</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Cxcr4-130</td>
      <td>95/0</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Cxcr4-117^</td>
      <td>209/9*</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>hCxcr4-117^/CXCR4-125</td>
      <td>81/0</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Cxcr4-113</td>
      <td>300/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Cxcr4-109</td>
      <td>89/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Cxcr4+1</td>
      <td>33/0</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Cxcr4+119</td>
      <td>187/0</td>
      <td>Inactive</td>
      <td>Arterial enhancer</td>
    </tr>
    <tr>
      <td>Cxcr4+135</td>
      <td>69/56</td>
      <td>Arterial enhancer</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Cxcr4+151</td>
      <td>96/50</td>
      <td>Arterial enhancer</td>
      <td>Arterial TSS</td>
    </tr>
    <tr>
      <td>Efnb2-333</td>
      <td>152/93</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Efnb2-159</td>
      <td>247/217</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Efnb2-141</td>
      <td>74/36</td>
      <td>Arterial enhancer</td>
      <td>Arterial TSS</td>
    </tr>
    <tr>
      <td>Efnb2-112</td>
      <td>65/30</td>
      <td>Arterial enhancer</td>
      <td>Arterial TSS</td>
    </tr>
    <tr>
      <td>Efnb2+3</td>
      <td>92/0</td>
      <td>Inactive</td>
      <td>Common EC TSS</td>
    </tr>
    <tr>
      <td>Efnb2+37</td>
      <td>114/18*</td>
      <td>Weak enhancer*</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Efnb2+172</td>
      <td>63/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Efnb2+209</td>
      <td>158/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Gja4+24</td>
      <td>52/0</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Gja4+50</td>
      <td>232/187</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Gja4+57</td>
      <td>192/0</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Unc5b-57</td>
      <td>50/21</td>
      <td>Venous enhancer</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Unc5b+14</td>
      <td>61/0</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Unc5b+23</td>
      <td>82/16*</td>
      <td>Weak enhancer*</td>
      <td>Arterial enhancer</td>
    </tr>
    <tr>
      <td>Unc5b+30</td>
      <td>96/79</td>
      <td>Arterial enhancer</td>
      <td>Arterial enhancer</td>
    </tr>
    <tr>
      <td>Unc5b+39</td>
      <td>96/56</td>
      <td>Arterial enhancer</td>
      <td>Arterial enhancer</td>
    </tr>
    <tr>
      <td>Unc5b+43</td>
      <td>111/0</td>
      <td>Inactive</td>
      <td>Arterial enhancer</td>
    </tr>
    <tr>
      <td>Acvrl1-5</td>
      <td>Seki et al., 2004</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Acvrl1-1/p</td>
      <td>Seki et al., 2004</td>
      <td>Inactive</td>
      <td>Common EC TSS</td>
    </tr>
    <tr>
      <td>Acvrl1+6</td>
      <td>127/49</td>
      <td>Arterial enhancer</td>
      <td>Common EC TSS</td>
    </tr>
    <tr>
      <td>Acvrl1+16</td>
      <td>205/0</td>
      <td>Inactive</td>
      <td>Common EC TSS</td>
    </tr>
    <tr>
      <td>Acvrl1+19</td>
      <td>95/0</td>
      <td>Inactive</td>
      <td>Common EC TSS</td>
    </tr>
    <tr>
      <td>Cxcl12-184</td>
      <td>64/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Cxcl12-2</td>
      <td>32/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Cxcl12+239</td>
      <td>70/1</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Cxcl12+265</td>
      <td>42/1</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Cxcl12+269</td>
      <td>163/63</td>
      <td>Arterial enhancer</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Cxcl12+298</td>
      <td>51/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Cxcl12+376</td>
      <td>149/0</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Cxcl12+383</td>
      <td>152/37*</td>
      <td>Weak enhancer*</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Cxcl12+439</td>
      <td>73/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Cxcl12+445</td>
      <td>145/0</td>
      <td>Inactive</td>
      <td>Common EC TSS</td>
    </tr>
    <tr>
      <td>Gja5-7</td>
      <td>66/39</td>
      <td>Arterial enhancer</td>
      <td>Arterial enhancer</td>
    </tr>
    <tr>
      <td>Gja5-21†</td>
      <td>38/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Gja5-28</td>
      <td>156/0</td>
      <td>Inactive</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Gja5-78</td>
      <td>76/62</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Gja5-93</td>
      <td>253/0</td>
      <td>Inactive</td>
      <td>Arterial enhancer</td>
    </tr>
    <tr>
      <td>Nrp1+28</td>
      <td>De Val et al., 2008</td>
      <td>Pan-EC enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Nrp1+76</td>
      <td>54/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Nrp1+78</td>
      <td>191/34</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Nrp1+91</td>
      <td>109/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Nrp1+129</td>
      <td>110/0</td>
      <td>Inactive</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>DLL4-12</td>
      <td>Sacilotto et al., 2013</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>DLL4in3</td>
      <td>Sacilotto et al., 2013</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>ECE1in1</td>
      <td>Robinson et al., 2014</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Flk1in10</td>
      <td>Becker et al., 2016</td>
      <td>Arterial enhancer</td>
      <td>Uncalled</td>
    </tr>
    <tr>
      <td>Hey1-18</td>
      <td>Watanabe et al., 2020</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>NOTCH1+16</td>
      <td>Chiang et al., 2017</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>Sema6d-55</td>
      <td>Zhou et al., 2017</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
    <tr>
      <td>SOX7+14</td>
      <td>Zhou et al., 2017</td>
      <td>Arterial enhancer</td>
      <td>Common EC enhancer</td>
    </tr>
  </tbody>
</table>

_*indicates only limited expression in a very small number of ECs. Acvrl1-5 and Acvrl1-1/p were previously investigated by Seki et al., 2003, Nrp1+28 by De Val et al., 2008, Notch1+16 by Chiang et al., 2017, Dll4-12 and Dll4in3 by Sacilotto et al., 2013, Flk1in10 by Becker et al., 2016, Sema6d-55 by Zhou et al., 2017, Sox7+14 by Zhou et al., 2017; Andersson et al., 2014, Ece1in10 by Robinson et al., 2014, and Hey1-18 by Watanabe et al., 2020.†After this analysis but prior to this publication, Gja5-21 was shown to direct expression in the zebrafish endocardium at 4 dpf (Chiang et al., 2023)._

Out of the 41 putative enhancers identified here, 3 had been previously investigated in vivo: Nrp1+28, which was able to drive robust pan-endothelial expression of the lacZ reporter gene in transgenic mouse embryos (De Val et al., 2008); and Acvrl-5 and Acvrl1-1/p, which were silent in a similar mouse assay (Seki et al., 2004; Table 2). Additionally, Acvrl1+6 is contained within a nine kilobase region known to direct arterial-specific expression of lacZ in transgenic mice (Seki et al., 2004). However, because of the size of this original piece, we treated the smaller Acvrl1+6 enhancer as untested.

### Transgenesis in zebrafish confirms arterial activity for a subset of putative enhancers

It is well established that DNA sequences associated with enhancer marks do not necessarily act as enhancers (e.g. by independently activating gene transcription). To establish the ability of the 38 untested putative enhancers to drive arterial EC activity, we first analysed the activity of each in F0 Tol2-mediated mosaic transgenic zebrafish embryos (Kawakami, 2005). Similar zebrafish assays have been conducted with five of the eight previously identified arterial enhancers, and in each case these mammalian enhancer sequences were able to drive GFP expression in arterial ECs in zebrafish embryos (Figure 1, Figure 1—figure supplement 1; Sacilotto et al., 2013; Chiang et al., 2017; Becker et al., 2016; Andersson et al., 2014). Here, the mouse sequence of each of the 38 putative arterial enhancers was cloned upstream of the E1b minimal promoter and GFP reporter gene and used to generate mosaic transgenic embryos, which were examined at 2 days post fertilization (dpf) (Kawakami, 2005). This analysis identified 19 enhancers able to drive GFP expression in ECs of transgenic zebrafish, defined as vascular GFP expression in more than 5% of injected embryos (Table 2). Sixteen of these active enhancers were able to drive robust and reproducible patterns of endothelial GFP expression in F0 mosaic transgenics (Figure 1—figure supplement 2) from which we were able to establish stable transgenic zebrafish lines. Of these, 15/16 enhancer:GFP transgenes were clearly expressed in arteries and were therefore selected for further analysis (Figure 2 and Figure 3, genome coordinates Table 2—source data 2). This included at least one enhancer for each of our eight target genes. The outlier, Unc5b-57, was active only in the anterior portion of the caudal vein and was excluded from further analysis (Figure 1—figure supplement 3A–B). The remaining three enhancers were able to drive only weak GFP and/or were limited to a small number of ECs in all analysed zebrafish (Table 2, Figure 1—figure supplement 3C). GFP expression pattern within the vasculature could not be determined and no stable lines could be established; therefore, these weak vascular enhancers were not followed up further. Another 19 putative enhancer regions did not consistently drive detectable GFP expression in ECs (Table 2). These were designated inactive regions without developmental enhancer activity.

![Figure 2.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig2-v2.jpg)

**Figure 2.:** Grey dashed box indicates region of zoom, da indicates dorsal aorta, cv indicates cardinal vein, dlav indicates dorsal longitudinal anastomotic vessel, white arrow indicates intersegmental vessels, and * indicates expression in neural tube. tg(Cxcr4-135:GFP) was crossed with tg(kdrl:HRAS-mCherry), which expresses mCherry in all blood vascular ECs and is shown here on the top line as a guide to vessel structure at this timepoint. F1/2 indicates generation of embryo.

![Figure 3.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig3-v2.jpg)

**Figure 3.:** Stable transgenic zebrafish expressing the 15 strong arterial enhancer:GFP transgenes crossed with tg(kdrl:HRAS-mCherry), which expresses mCherry in all blood vascular ECs. Grey dashed box indicates region of zoom, da indicates dorsal aorta, cv indicates cardinal vein, dlav indicates dorsal longitudinal anastomotic vessel, pale pink filled arrows indicates intersegmental arteries, pale blue open arrows indicate intersegmental veins, * indicates expression in neural tube, and F1/2 indicates generation of embryo.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Schematic diagram of the primary ocular vasculature adapted from Hashiura et al., 2017. (B) Expression pattern of 15 novel arterial enhancers in the ocular vasculature at 2 dpf and 3 dpf. At 3 dpf, kdrl:HRAS-mCherry transgene was crossed with arterial zebrafish lines to enable visualization of all ECs.

![Figure 4.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig4-v2.jpg)

**Figure 4.:** DA dorsal aorta, ISA intersegmental arteries, DLAV dorsal longitudinal anastomotic vessel, CV cardinal vein, ISV intersegmental veins, NT neural tube, NCA nasal ciliary artery, NCAx extends beyond NCA in direction of blood flow, HA hyaloid artery, DCV dorsal ciliary vein, OV optic vein. A fin artery, V fin vein. Letters “s” “m” and “w” equate to strong medium or weak relative expression, *restricted to distal regions, ** restricted to anterior regions, *** restricted to subset of ECs.

In addition to the 38 putative enhancers identified through our screen, we tested another 11 regions that fell below our enhancer threshold. This included regions with enhancer marks in mice only or human only, regions with only one enhancer mark, and the two regions previously implicated as enhancers (Nrp1+76 and Cxcr4-117; Tsaryk et al., 2022). Of these 11 regions, only Cxcr4-117 was able to drive any detectable expression in ECs. However, this was seen in only 9 of 209 injected embryos (<5%) and was limited to 1–2 ECs in each F0 fish (Table 2, Figure 1—figure supplement 3D). A human version of this enhancer, CXCR4-125 (identified as an enhancer in Tsaryk et al., 2022), was also tested but was not able to drive any detectable GFP expression (Table 2), and this enhancer region was therefore not further analysed.

### Assessing arterial enhancer activity patterns in transgenic models

We next examined the activity of our 15 strong arterial enhancers in further detail. To determine the expression pattern of these enhancers in stable transgenic zebrafish lines, we first assessed GFP expression in the trunk vasculature at 2–3 dpf (Figures 2—4). Interestingly, whilst all 15 enhancers were preferentially active in trunk arteries, the pattern of GFP activity within the arterial tree varied. By 3 dpf, five enhancers were broadly active in both the dorsal aorta and the intersegmental arteries sprouting off the aorta, whilst four enhancers were restricted to the dorsal aorta only, and five were restricted to the intersegmental arteries only. In addition, we saw some differences in arterial specificity. By 3 dpf, 6/9 enhancers active in the dorsal aorta showed no expression in the cardinal vein, whilst the other three were also weakly expressed in anterior or posterior segments of the cardinal vein (Figures 3 and 4). Transgene expression in the intersegmental vessels was more complicated to interpret as these vessels form by angiogenic sprouting from the dorsal aorta and many arterial genes are also expressed during angiogenic sprouting (including Efnb2, Cxcr4, Dll4, Nrp1, and Sox7). Consequently, GFP expression seen during early intersegmental sprouting could potentially reflect angiogenic or arterial expression (Sacilotto et al., 2013; Yamamizu et al., 2010). However, our analysis demonstrated that all enhancers active in the intersegmental vessels domain became either arterial-enriched or arterial-specific by 3 dpf: all 12 enhancers active in the intersegmental vessels were strongly enriched in the 3 dpf intersegmental arteries (as defined by direct connections to the dorsal aorta rather than the cardinal vein), with only 4/12 showing weaker expression in some intersegmental veins (Figures 2—4). Overall, this analysis suggests that, in the zebrafish trunk vasculature, 10/15 of our enhancers were arterial-specific whilst 5/15 were arterial-enriched.

Arterial development in the zebrafish trunk at the timepoints investigated primarily occurs via vasculogenesis and arterial-to-arterial sprouting, as opposed to the vein/capillary origin of many mammalian arterial ECs (Su et al., 2018; Hou et al., 2022; Red-Horse and Siekmann, 2019). In order to investigate whether our enhancers were also active in arterial vessels formed directly from venous ECs, we also looked at expression in the developing zebrafish eye. In the zebrafish ocular system, venous ECs from the dorsal ciliary vein (DCV) sprout to form the nasal ciliary artery (Kaufman et al., 2015; Hasan et al., 2017; Hashiura et al., 2017). Analysis of our enhancers in the 2–3 dpf eye found that 11/15 were active in the nasal ciliary artery, of which only two were also expressed in the dorsal ciliary vein (Figure 3—figure supplement 1, Figure 4). Only four enhancers active in the trunk arteries showed no ocular expression. This did not correspond to any particular arterial expression pattern in the trunk vasculature, suggesting that the two behaviours may not be transcriptionally linked.

We also investigated arterial enhancer activity in adult zebrafish. For this, we examined uninjured adult dorsal fins from 13 enhancer:GFP adult stable lines, alongside two previously studied arterial enhancers (Dll4in3 and Dll4-12) and the pan-EC marker line tg(fli1a:GFP) previously used for similar analysis (Xu et al., 2014; Figures 4 and 5). 11/13 novel arterial enhancers and 2/2 known arterial enhancers were active in the adult fin arteries and/or arterial sprouts (Figure 5). Although no adult F1 fish were available for the Ephb2-112:GFP and Efnb2-159:GFP transgenes, analysis in 4-week-old juveniles also confirmed arterial fin expression (Figure 1—figure supplement 3E). Consequently, it is clear that our developmentally active arterial enhancers are largely also able to direct arterial patterns of expression in the adult, more quiescent, vasculature.

![Figure 5.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig5-v2.jpg)

**Figure 5.:** (A) Schematic drawing of the zebrafish fin vasculature adapted from Xu et al., 2014. (B) Expression pattern of the common EC marker line Fli1a:GFP in an adult fin. (C) Expression pattern of 13 novel arterial enhancer:GFP transgenes in adult fins, alongside previously identified arterial enhancers Dll4in3 and Dll4-12. Grey dashed box indicates regions of zoom, a indicates fin artery, v indicates fin vein, * arterial sprout. See also Figure 1—figure supplement 4.

Lastly, we investigated whether these enhancers (all mouse sequences) also directed arterial activity in transgenic mice, selecting five enhancers active in zebrafish for further analysis. In each case, the enhancer was able to drive activity of the lacZ reporter gene in arterial ECs in E14.5 F0 transgenic mouse embryos in patterns similar to the previously described arterial Dll4in3:lacZ transgene (Figure 6). We additionally tested one enhancer which was only weakly active in transgenic zebrafish (Efnb2-37). No endothelial activity was seen for this enhancer in transgenic mice (Figure 6—figure supplement 1). In combination, this transgenic zebrafish and mouse analysis indicates that we have successfully identified a cohort of enhancers directing gene expression to arterial ECs, accurately reflecting the expression of their cognate genes in mammals.

![Figure 6.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig6-v2.jpg)

**Figure 6.:** (A–E) Two representative F0 embryos expressing each tested putative enhancer alongside a schematic of the transgene and two transverse sections through the embryo body wall and tail. Numbers in bottom left indicate embryos with arterial lacZ/total transgenic embryos. Grey dashed boxes indicate region in zoom, arrow indicates artery. (F) shows a representative E14.5 embryo from a stable transgenic line expressing the arterial Dll4in3:lacZ transgene alongside similar transverse sections through the embryo body wall and tail. Black line = 100 um.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** No expression is seen in vessels.

### In vivo enhancer activity does not always correlate with in silico predictions

We compared our results to a published genome-wide classification of EC regulatory elements, which used assessment of relative H3K27ac and acEP300 occupancy in freshly isolated HUVEC and HUAECs to classify enhancer regions as arterial-enriched, venous-enriched and common (arterial and venous enriched) regulatory elements (Sissaoui et al., 2020). Only 3/15 of our in vivo-validated arterial enhancers were classified as arterial enhancers using this assay, with 5/15 classified as common enhancers, 4/15 characterized as TSS, and 3/15 as uncalled (Table 2). A similar analysis of the eight previously identified arterial enhancers found none were classified as arterial enhancers (7/8 were marked as common enhancers and 1/8 was uncalled) (Table 2). Conversely, 10/19 of the regions that were inactive in our transgenic assays were classified as enhancers in the in vitro assay (8 as common enhancers, 2 as arterial enhancers) (Table 2). The low correlation between predicted activity and behaviour in transgenic assays suggests that in silico assessments using enhancer marks in cultured ECs alone may not strongly predict the ability of a putative enhancer region to independently direct gene expression nor the resultant specificity of this expression.

We also considered whether the use of vein-origin (HUVEC) and microvascular-origin (HMVEC-dBl-neo/ad) ECs in our analysis of human enhancer marks may have affected the accuracy of our putative enhancer selection by expanding our analysis to enhancer marks in arterial-origin ECs. However, analysis of enhancer marks in human aortic endothelial cells (HAEC and telo-HAECs) and human umbilical artery endothelial cells (HUAECs) showed a very similar pattern and identified the same set of putative enhancers as when HUVEC/HMVEC data was considered (Figure 1—figure supplement 4). This suggests that the arteriovenous original of cultured cells did not significantly influence putative enhancer marks, further emphasizing the challenges of using selective enhancer marks in such lines to predict expression patterns in vivo.

### Assessment of transcription factor motifs and binding patterns at arterial enhancers

This work so far has identified a cohort of enhancers able to drive strong gene expression selectively to arterial ECs. We next investigated whether this arterial expression pattern was associated with the binding of particular transcription factors. The ability of a transcription factor to bind an enhancer or promoter sequence is commonly established by identifying one or more binding motif(s) within the region of interest, and/or by observing direct binding to the region of interest by chromatin immunoprecipitation (ChIP) or similar methodologies. Here, we combined both approaches. First, we performed HOMER analysis to identify overrepresented motifs within the core regions of all 15 arterial enhancers identified here (≈250–400 bp, centred on enhancer marks and cross-species conservation) alongside all eight previously identified arterial enhancers (a total of 23). This HOMER motif analysis indicated the repeated presence of motifs for ETS (including EC-associated factors ETS1, ERG and ETV2), SOX (including EC-associated SOX17 and SOX7), FOX (including EC-associated FOXO1 and FOXO3), RBPJ (the transcriptional effector of NOTCH signalling), and MEF2 (including EC-associated MEF2A) (Figure 7—figure supplement 1). We next directly searched the sequences of all 23 core arterial enhancers to accurately determine the frequency of motifs for each of these transcription factors. In addition, we also looked for possible binding of other transcription factors previously implicated in arterial gene expression. The enhancer motif search used a combination of the JASPAR Transcription Factors Track Settings (TFTS) on the UCSC Genome Browser and hand annotation using previously defined consensus motifs (Figure 7—figure supplement 1). Because the level of conservation of motifs can often be an indication of their importance to enhancer activity, we classified each motif into three categories: strongly conserved (motif conserved to the same depth of the surrounding sequence), weakly conserved (motif conserved in orthologous human enhancer but not to the same depth as the surrounding sequence), and not conserved (motif is not conserved within the orthologous human sequence). In parallel, we compared this motif analysis with a variety of published endothelial ChIP-seq and CUT&RUN datasets to determine where there was evidence of direct binding for each of these transcription factors at each enhancer (see Figure 7 and Figure 8, Figure 7—figure supplements 2–6, Figure 8—figure supplements 1 and 2, Figure 9).

![Figure 7.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig7-v2.jpg)

**Figure 7.:** All enhancers shown in 3’–5’ orientation relative to the arterial gene TSS. Deep black-lined rectangle boxes indicate strongly conserved motifs for transcription factors (conserved at the same depth as the surrounding enhancer sequence), shallow grey-lined boxes/text indicate weakly conserved motifs (conserved between mouse and human enhancer sequence but not at the same depth as the surrounding sequence), and rounded boxes mark motifs in enhancers conserved only human-mouse. Bold transcription factor names indicate places where ChIP-seq (or similar analysis) confirms binding. See Figure 7—figure supplements 2–6 for annotated sequences. Arterial enhancers listed with * are previously published (as detailed in Payne et al., 2024), genome locations for each enhancer are provided in Table 2—source data 2. Distances between motifs are representative but not scaled.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Homer known motif enrichment results on core enhancer sequences from all 23 arterial enhancers listed in Table 1. Exact sequences include in this analysis are listed in Figure 7—figure supplement 2, and the coordinates in mm10 recorded in Table 2—source data 2. (B) Table summarizing sequence logos used to guide motif analysis, alongside the source of each logo and EC type (where relevant). (C) Exact sequences assigned as motifs for each transcription factor.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** ETS motifs highlighted in green, SOXF motifs in yellow, FOX motifs in darker blue, FOX:ETS motifs in turquoise, RBPJ motifs in red, MEF2 in bright light blue, SMAD4 motifs in light pink, SMAD1/5 GC-rich motifs in darker pink, TCF/LEF (Wnt pathway) in grey, NR2F2 motifs in purple, and KLF4 motifs in orange. The sequences assessed as transcription factor motifs are listed in Figure 8C. Bold underline strong motifs conserved to the same depth as surrounding sequence (conservation depth indicated after title of each enhancer), bold indicates weak motif conserved between human and mouse but not to the comparable depth of the surrounding sequence, and italic indicates motif just found in mouse sequence.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig7-figsupp3-v2.jpg)

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig7-figsupp4-v2.jpg)

![Figure 7—figure supplement 5.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig7-figsupp5-v2.jpg)

![Figure 7—figure supplement 6.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig7-figsupp6-v2.jpg)

![Figure 8.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig8-v2.jpg)

**Figure 8.:** Red dashed box indicates arterial enhancer region. Tracks show ChIP-seq/CUT&RUN signal for ERG (Sissaoui et al., 2020), ETS1 (Chen et al., 2017), SOX7, SOX17 and SOX18 (this paper), FOXO1 (Andrade et al., 2021), RBPJ (Wang et al., 2019), MEF2C (Maejima et al., 2014), SMAD1/5 (Morikawa et al., 2011), SMAD2 (Chen et al., 2019), and NR2F2 (Sissaoui et al., 2020) in HUVECs, alongside FOXO1 (Sissaoui et al., 2020), and MEF2A (Akerberg et al., 2019) in adult mouse hearts.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig8-figsupp1-v2.jpg)

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig8-figsupp2-v2.jpg)

![Figure 8—figure supplement 3.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig8-figsupp3-v2.jpg)

**Figure 8—figure supplement 3.:** (A–B, D, F, H) Venn diagrams assessing overlap of genomic regions called as peaks of various combinations of ChIP-seq and CUT&RUN datasets. (A) Comparison of called binding peaks for ERG (Sissaoui et al., 2020) and SOX7_mCherry (Overman et al., 2017) with marks for enhancers and TSS (Sissaoui et al., 2020). (B) Comparison of called binding peaks for ERG and SOX17 (new CUT&RUN) with marks for enhancers and TSS. (D) Comparison of called binding peaks for ERG and SOX7 (new CUT&RUN) with marks for enhancers and TSS. (D, F) Comparison of called binding peaks for ERG and SOX7 (new CUT&RUN) with marks for enhancers and TSS. (H) Comparison of called binding peaks for the overlap of called peaks of our SOX7, SOX17, and SOX18 CUT&RUN data with each another and previously published ERG ChIP-seq data. (C, E, G) Top motif families called by HOMER in the SOX17 (C) and SOX7 (E) and SOX18 (G) CUT&RUN peaks.

![Figure 8—figure supplement 4.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig8-figsupp4-v2.jpg)

**Figure 8—figure supplement 4.:** (A) UMAP visualization of scRNA-seq data of CD31+EC isolated from E12 BmxCreERT2;RosatdTomato lineage traced hearts with accompanying gene expression profiles. Raw data obtained from D’Amato et al., 2022. (B) Chosen gene expression profiles from scRNA-seq data of ApjCreER lineage traced EC isolated from E14.5 hearts. Plots taken from publicly available Shinyapp visualization of data from Su et al., 2018 . (C) UMAP plot and chosen gene expression profiles of CD31+EC from BmxCreERT2;RosatdTomato lineage traced from E17.5 hearts. Raw data obtained from D’Amato et al., 2022 for reanalysis.

![Figure 9.](https://cdn.elifesciences.org/articles/102440/elife-102440-fig9-v2.jpg)

**Figure 9.:** (A) All known (e.g. published) endothelial enhancers with adequately described expression patterns in transgenic mouse embryos were analysed to determine occurrence of selected TF motifs and direct binding. See Figure 7—figure supplement 1 for TF motif information, Figure 7—figure supplements 2–6 for annotated enhancer sequences and Figure 8 and Figure 8—figure supplements 1 and 2 for TF binding peaks. Enhancers in bold were identified in this paper, those with * are previously published (as detailed in 1), genome locations for each enhancer is provided in Table 2—source data 2. (B) TF binding patterns for each arterial enhancer grouped by expression patterns in the 3 dpf zebrafish trunk. DA dorsal aorta, ISA intersegmental arteries, DLAV dorsal longitudinal anastomotic vessel, CV cardinal vein, ISV intersegmental veins, NT neural tube, NCA nasal ciliary artery, NCAx extends beyond NCA in direction of blood flow, HA hyaloid artery, DCV dorsal ciliary vein, OV optic vein. A fin artery, V fin vein. Letters s m w equate to strong medium or weak relative expression, * restricted to distal regions, ** restricted to anterior regions, *** restricted to subset of ECs.

### ETS, SOXF, and FOX binding is a common but not unique occurrence at arterial enhancers

Our motif analysis revealed near-ubiquitous binding sites for ETS, SOXF and FOX transcription factors at all arterial enhancers (Figure 7, Figure 7—figure supplements 2–6, Figure 9). For ETS, 23/23 arterial enhancers contained at least one strongly conserved motif. Confirming this motif identification, 18/23 of these enhancers also directly bound ERG and ETS1, two very common EC-associated ETS factors (Figure 8, Figure 8—figure supplement 1). For FOX, 22/23 arterial enhancers contained conserved FOX motifs (22 strongly conserved) with 13/23 directly binding FOXO1 (Figure 8, Figure 8—figure supplement 1). For SOXF, 22/23 arterial enhancers contained conserved motifs (21 strongly conserved). Initial comparison of our enhancer cohort with publicly available information on SOX7 binding (from Overman et al., 2017, which used ChIP-seq in HUVECs over-expressing SOX7-mCherry) showed no overlap. However, only 6% of SOX7-mCherry peaks overlapped with EC-associated enhancers or TSS marks and only 4% correlated with ERG binding, an ETS family transcription factor strongly associated with EC gene transcription (Figure 8—figure supplement 3A, ERG and enhancer mark data from Sissaoui et al., 2020). Further, no SOX17 ChIP-seq in ECs has been published, despite SOX17 being most closely associated with arterial identity. We therefore performed an assessment of SOX17 binding with antibodies against the endogenous protein using CUT&RUN in HUVECs. In this analysis, 75% of SOX17 binding peaks overlapped with EC enhancer/promoter marks (Sissaoui et al., 2020), 73% overlapped with ERG binding (Sissaoui et al., 2020), and HOMER analysis identified the SOX17 consensus motif as the most significantly enriched motif (Figure 7—figure supplement 3B and C). Assessment of our 23 arterial enhancer cohort found called SOX17 peaks at 20/23 arterial enhancers, in every case correlating with the presence of strongly conserved SOXF motifs (Figure 8, Figure 8—figure supplement 1, Figure 9). We also considered whether the pattern of SOX17 binding was different to SOX7 and SOX18, proteins with similar binding motifs but different expression profiles within the vasculature (Zhou et al., 2015). For this, we again used CUT&RUN in HUVECs with antibodies against the endogenous SOX7 and SOX18 proteins. In these assays, 91% of SOX17 peaks were also bound by SOX7 and/or SOX18 (86% shared with SOX7, 71% with SOX18, 66% with both) (Figure 8—figure supplement 3). For our arterial enhancers, all 20 SOX17-bound enhancers were also bound by either SOX7 (9/23), SOX18 (2/23) or both SOX7 and SOX18 (9/23) (Figure 4, Figure 8, Figure 8—figure supplement 1). These data therefore suggest that binding of the arterial-enriched SOX17 was not a specific event at arterial-selective enhancers and that other SOXF proteins can also recognize and bind the SOX motifs within these enhancers.

Looked at in isolation, this analysis would strongly suggest that ETS, FOX, and SOXF transcription factors work together to direct arterial-specific gene expression. However, although our enhancers are all specific or highly enriched in arterial ECs, this analysis cannot by itself distinguish between factors that specifically direct arterial expression, and those required for endothelial gene expression more generally. Consequently, to determine if these common ETS, SOXF and FOX binding patterns were unique to arterial enhancers, we expanded our analysis to 16 in vivo-validated endothelial enhancers that were not selectively active in arterial ECs (Figure 7B and C, Figure 7—figure supplements 5 and 6 and Figure 8—figure supplement 2, Figure 9). As assessed in transgenic mouse embryos at mid-late gestation, 13 of these enhancers drove relatively equal expression in arterial and venous ECs (pan-EC enhancers), while the activity of the other three was vein-enriched and artery-excluded (vein enhancers) (Payne et al., 2024). Unsurprisingly, given their known role in general endothelial gene expression and identity, binding of ETS factors was ubiquitous at pan-EC enhancers and venous enhancers in addition to arterial enhancers. However, despite the association of SOXF factors with arterial identity, 12/13 pan-EC enhancers also directly bound SOXF factors (11/13 bound by SOX17, 11/13 by SOX7, and 9/13 by SOX18), with 9/13 containing strongly conserved SOXF motifs (Figure 8—figure supplement 2, Figure 9). The binding patterns at venous enhancers were harder to interpret due to a limited number of well-validated enhancers in this category and the activity of the CoupTFII-965 enhancer in lymphatic ECs in addition to veins. While the Ephb4-2 or Mef2cF10 vein enhancers contained no SOXF motifs, the CoupTFII-965 enhancer contained strongly conserved SOXF motifs and bound all SOXF proteins (Figure 8—figure supplement 2, Figure 9). Consequently, while the enhancers of some venous genes may lack sensitivity to SOXF factors, our data suggests that SOXF binding is not a unique feature of arterial-restricted gene expression. These observations align with previous studies showing roles for SOXF factors in vasculogenesis and angiogenesis (Lilly et al., 2017; Kim et al., 2016; Lee et al., 2014), and with the expression of SOXF factors throughout the vascular plexus during arterial-venous differentiation in the embryonic heart (Figure 8, Figure 8—figure supplement 4 and Chiang et al., 2017; Sharma et al., 2017) and postnatal retina (Zhou et al., 2015). This also agrees with the severe vascular phenotypes seen after compound loss of SOXF factors, which include EC hyperplasia, loss of angiogenic markers, and inhibited arteriovenous differentiation (Kim et al., 2016; Zhou et al., 2015).

Our findings were somewhat less clear for FOX transcription factors. 9/13 pan-EC enhancers contained some kind of FOX motif (compared to 22/23 arterial enhancers). However, the only FOX motif within 6 of these pan-EC enhancers was a composite part of a FOX:ETS motif (a vasculogenic-associated element whose FOX component is often fairly degenerative) Figures 7 and 8, Figure 7—figure supplements 1–6; Figure 7—figure supplements 2–6; Figure 7—figure supplements 4–6; Figure 7—figure supplements 3–6; Figure 7—figure supplements 3–5; Figure 9 This leaves only 3/13 pan-EC enhancers containing independent FOX motifs, compared to 20/23 arterial enhancers, suggesting that FOX binding may be enriched among our arterial enhancer cohort. While this aligns with previous observations linking FOXC1 and FOXC2 with arterial differentiation expression (Seo et al., 2006), neither are highly expressed in developing coronary arteries nor commonly identified as arterial-enriched in single cell transcriptomics in developing mouse embryos (Figure 8, Figure 8—figure supplement 4 and Hou et al., 2022; Chen et al., 2024). In addition to FOXC1/2, FOXO1 is also expressed widely throughout the endothelium and directly bound many of our arterial enhancers, but direct links between deletion or constitutive activation of FOXO1 and changes in arterial differentiation have not yet been reported (e.g.Wilhelm et al., 2016).

### MEF2 binding occurs at a subset of arterial enhancers and may be associated with sprouting

MEF2 factor binding was overrepresented in arterial enhancers compared to pan-EC enhancers, although it was seen at only a minority of enhancers. In total, 9/23 arterial enhancers contained conserved MEF2 motifs (8 strongly conserved) compared to only 1/13 pan-EC enhancers. This arterial-skewed pattern was repeated in assays of MEF2 factor binding, with direct MEF2 binding found at 8/23 arterial enhancers and only 2/13 pan-EC enhancers (Figure 8, Figure 8—figure supplements 1 and 2, Figure 9). Given the known role of MEF2 factors in angiogenic sprouting and the close link between angiogenesis and arterial differentiation (Sacilotto et al., 2016; Pitulescu et al., 2017), it is possible that MEF2 factors are regulating gene expression in response to angiogenic rather than arterial cues at these enhancers. This has been already shown for the Dll4in3 enhancer, where loss of MEF2 binding ablated enhancer activity in angiogenic ECs but not in mature arterial ECs (Sacilotto et al., 2016). Supporting this hypothesis, MEF2-bound enhancers were associated with genes expressed in early ‘pre-arterial’ EC and/or involved in angiogenesis (Cxcr4, Efnb2, Nrp1, Unc5b, Flk1, and Dll4) (Hou et al., 2022; Raftrey et al., 2021; Figure 9). To determine if there was a relationship between MEF2 motif/binding and expression pattern, we grouped the enhancers according to zebrafish expression profiles in the trunk and looked at the resultant clusters of TFs (Figure 9). Strikingly, all five arterial enhancers restricted to the intersegmental vessels were MEF2-bound, indicating a possible angiogenic role as these vessels form by angiogenic sprouting. In addition, the MEF2-bound Efnb2-333 is active in both compartments in a similar pattern to the Dll4in3. However, MEF2 factors are also associated with transcriptional activation downstream of shear stress, which is a known effector of Efnb2 and other arterial gene expression (Hwa et al., 2017; Lu et al., 2021), and the MEF2-bound Unc5b+30 enhancer was preferentially active in the dorsal aorta only (Figures 2—4). Further studies would therefore be required to definitely link MEF2 binding at these enhancers to either an angiogenic or sheer stress response.

### RBPJ binding indicates a role for Notch in transcription of arterial genes

RBPJ is the transcriptional effector of the Notch pathway, complexing with the Notch intracellular domain (NICD) and the co-activator MAML in order to directly bind DNA and activate transcription (Bray, 2006). Strongly conserved RBPJ motifs were found in 14/23 arterial enhancers and 4/13 pan-EC enhancers, while direct RBPJ binding was confirmed at 6/23 arterial enhancers only (Figures 7 and 8, Figure 8—figure supplements 1–3, Figure 9). RBPJ motifs are relatively short and share close similarity to the ETS motifs (consensus TGGGAA vs. HGGAAR), potentially explaining the discrepancy between motif and direct binding. Direct RBPJ binding to arterial enhancers has previously only been reported for genes in the Notch pathway, a fact that supported the hypothesis that Notch does not directly induce arterial differentiation through gene activation but instead by reducing their MYC-dependent metabolic and cell-cycle activities (Luo et al., 2021). However, here we found good evidence for RBPJ binding at enhancers for Cxcr4, Efnb2, Gja4, and Unc5b, suggesting that Notch may directly influence at least some arterial identity genes. In most cases, these genes also contained additional enhancers not directly bound by RBPJ, potentially providing an explanation for the maintenance of some arterial gene expression in the absence of RBPJ/Notch (Luo et al., 2021). Additionally, previous studies on the Dll4in3 enhancer found that loss of RBPJ (and Notch signalling) did not affect enhancer or gene expression unless SOXF factors were also perturbed (Sacilotto et al., 2013). Cooperation between SOXF and Notch may also partly explain how the widely expressed SOXF factors enact arterial-specific gene activation, although SOX factors bound arterial enhancers more commonly than RBPJ. An alternative explanation may be that these results instead reflect the known involvement of RBPJ/Notch in angiogenesis. However, whilst all RBPJ-bound arterial enhancers were active in the sprout-formed intersegmental vessels in zebrafish (Figure 9), neither RBPJ binding or RBPJ motifs were ubiquitous in intersegmental-expressed enhancers.

### No other arterial or venous-related transcription factors are commonly present or excluded at our arterial enhancers

Lastly, we investigated potential roles for SMADs (transcription factors downstream of TGFβ/BMP signalling), TCF7/TCF7L1/TCFL2/LEF1 (transcription factors downstream of canonical WNT signalling), and KLF4 (downstream of laminar shear stress). Although the binding motifs for these factors were not overrepresented in our arterial cohort as assessed by HOMER analysis, these pathways have all previously been implicated in arterial gene expression. We also looked for evidence of NR2F2/COUP-TFII binding, a vein and lymphatic-specific transcription factor previously implicated in both activation of venous genes and repression of arterial/Notch genes. This analysis found little evidence supporting a broad role for any of these pathways in arterial gene expression nor a link to any particular expression type within the arterial tree (Figures 7 and 8, Figure 7—figure supplements 2–6, Figure 8—figure supplements 1 and 2, Figure 9). NR2F2 motifs were seen in 7/23 arterial enhancers (but only strongly conserved in 4/23) and 3/13 pan-EC enhancers. Largely uncorrelated ChIP-seq peaks were seen at 11/23 arterial enhancers, and at 8/13 pan-EC enhancers. Strongly conserved KLF4 motifs were only seen in 2/23 arterial and 4/13 pan-EC enhancers but none correlated with KLF4 binding. Strongly conserved TCF/LEF motifs were only found in 3/23 arterial enhancers and 2/13 pan-EC enhancers. SMAD1/5-SMAD4 factors downstream of BMP signalling have been previously associated with the expression of venous genes including Nr2f2 and Ephb4 (Neal et al., 2019; Stewen et al., 2024), and all three vein enhancers contained multiple motifs for SMAD factor binding (with 2/3 also directly binding SMAD1/5 and SMAD2 in HUVECS after BMP9/TGFβ stimulation) (Figures 7 and 8, Figure 8—figure supplement 2, Figure 9). However, here we found that SMAD binding also occurred at arterial enhancers, with 12/23 containing strongly conserved motifs, 8/23 directly binding SMAD1/5 of which three also bound SMAD2. This agrees with the lack of venous-specificity reported for phosphorylated SMAD1/5, which led to the supposition that addition factors work alongside SMAD1/5 to regulate vein specification (Neal et al., 2019). An arterial role for SMADs is not without precedent, particularly downstream of TGFβ (e.g.Ola et al., 2018; Chavkin et al., 2022; Roman and Hinck, 2017Roman and Hinck, 2017; Daems et al., 2024). While Tie2:Cre-mediated excision of SMAD4 (effectively knocking out all canonical BMP/TGFβ signalling) did not obviously affect arterial differentiation at E9.5, an earlier or later role cannot be dismissed, as Tie2:Cre becomes active after vasculogenic-driven arterial differentiation occurs, and vein-related lethality occurs in these embryos by E10.5 (Neal et al., 2019), prior to most vein/capillary-to-arterial EC differentiation.

## Discussion

Recent years have brought a new appreciation of the vein/capillary origin of most arterial ECs, and an increasing interest in arterialization as a therapeutic aim of regenerative medicine. However, the transcriptional pathways driving arterial differentiation are still incompletely understood. Many factors have contributed to this, including a focus on the Notch signalling pathway and a lack of characterized arterial enhancers for most key arterial genes. The latter has resulted in regulatory pathways being linked to arterial gene expression through proposed binding at promoter regions, although these elements are often poorly characterized or unsupported by functional data (e.g. binding motifs located kilobases away from TSS at regions without promoter or enhancer marks, transcription factor binding not verified by available ChIP-seq datasets). As well as the potential for incorrect assumptions, a reliance on poorly defined enhancer/promoter regions prevents further research building on these initial observations, for example, by looking for associated motifs to identify combinatorial, synergistic, and antagonistic factors or to link with newly discovered pathways or transcription factors. In this paper, we sought to generate a useful and accessible cohort of arterial enhancers with which to study arterial transcriptional regulation more effectively. Alongside Dll4, Notch1, and Hey1 (all genes with previously described enhancers included in our analysis), the eight arterial genes focused on here represent the majority of genes used to define arterial identity in single cell transcriptomics in mice and humans (e.g. Hou et al., 2022; McCracken et al., 2022; Raftrey et al., 2021; Chen et al., 2024). Further, our choice of targets included genes with essential and well-studied roles in arterial differentiation (e.g. Efnb2), implicated in arteriovenous malformations in humans (e.g. Acvrl1), associated with processes important for regeneration (Cxcr4 and Cxcl12; Das et al., 2019), or commonly used as arterial markers in animal models (e.g. Gja5). Thus, our hope was to identify a cohort of arterial enhancers likely to be directly targeted by arterial lineage specification and differentiation factors that represent key stages of arterial development of interest to a wide range of researchers and that we can easily link to previous observations on arterial development in animal models of gene depletion.

Analysis of single-cell transcriptomic data has indicated that arterial ECs can be further subdivided into two groups, reflecting maturity but also potentially slightly different developmental trajectories (Hou et al., 2022; Raftrey et al., 2021). The genes studied here cover both subgroups, with Acvrl1, Cxcl12, Gja5, and Nrp1 primarily restricted to the mature arterial EC subgroup, while Cxcr4, Efnb2, Gja4, and Unc5b were also expressed in the less mature/arterial plexus/pre-arterial EC subgroup (Hou et al., 2022; Raftrey et al., 2021). Although we saw no obvious differences in transcription factor motif and binding between the two sets overall, the genes expressed in both immature and mature subgroups tended to have multiple enhancers with differential expression patterns: there are four Efnb2 enhancers, of which Efnb2-141 is largely restricted to the dorsal aorta and Efnb2-159 is restricted to the intersegmental arteries, while Efnb2-333 and Efnb2-112 enhancers are more widely active; there are two Unc5b arterial enhancers, of which Unc5b+39 is restricted to the intersegmental arteries while Unc5b+30 is expressed more widely. It is therefore possible that the upstream signals involved at different stages of arterial differentiation may, to some extent, target separate enhancers. Although this article has focused on transcriptional signatures of arterial versus non-arterial-specific enhancers, future research into the transcriptional differences seen between these differentially expressed arterial enhancers may therefore bring further insights into arterial transcription factors, and the manner in which upstream pathways combine to enact subtle but essential changes in gene expression.

Alongside a deficit of characterized enhancers, our understanding of vascular transcription is also affected by the considerable redundancy shown by many endothelial transcription factors. In particular, this can complicate analysis of gene disruption in animal models. A good example of this problem is the SOXF factors. SOX7, SOX17, and SOX18 not only show distinct yet overlapping expression patterns, but their ability to functionally compensate for each other can vary on different mouse backgrounds. For example, the phenotype in mice lacking SOX18 varies from essentially normal to complete loss of lymphatic ECs, with lethality depending on the mouse strain and associated variation in the ability of SOX7 and SOX17 to compensate (Hosking et al., 2009). SOX17 is the SOXF factor most strongly expressed in arterial ECs, and arterial defects occur after its deletion (Corada et al., 2013). This has resulted in the hypothesis that SOX17 selectively activates arterial genes, but this is not well supported by the results here. An alternative explanation could be that SOXF factors are required for endothelial gene expression more generally, potentially as master regulators. This aligns with their robust and primarily endothelial-specific expression (particularly after mid-gestation; Payne et al., 2024), and by the widespread presence of SOXF motifs and binding at endothelial enhancers of all varieties. In this second model, the loss of SOX17 may affect the arterial compartment more severely simply because it comprises the majority of arterial SOXF (so the total amount of SOXF factors is more significantly depleted in arteries than elsewhere when SOX17 is deleted), with similar explanations for the consequences of SOX7 depletion on vasculogenesis (Lilly et al., 2017) and SOX18 depletion on lymphangiogenesis (Hosking et al., 2009; François et al., 2008). Alternatively, Stewen et al., 2024 have recently shown that combined depletion of SOXF factors in cultured ECs significantly reduced Efnb2 expression while increasing Ephb4 expression, and instead argue for a more specific role for SOXF factors in arteriovenous differentiation related to elevated SOXF levels in arterial ECs (Stewen et al., 2024). While this alone cannot explain the widespread binding of SOXF factors to pan-EC genes, SOXF factors are also crucial during vasculogenesis/early angiogenesis. Therefore, the role of SOXF factors in general, and SOX17 in particular, may instead be to drive a less specific angiogenic/arterial gene expression program. Supporting this, neither the Ephb4-2 or Mef2cF7 vein enhancers had SOXF motifs, while the role of SOXF in CoupTFII-965 regulation may be simply related to its expression in lymphatic ECs. The paucity of defined venous/capillary enhancers currently limits our ability to make conclusions here. However, endothelial SOXF factors are clearly strongly expressed widely in the endothelium at timepoints where a much more limited number of ECs become committed to an arterial fate (perfectly illustrated in the coronary vasculature), suggesting that additional transcriptional regulators must be involved alongside SOXF to enable this exquisitely specific pattern of gene activation. While RBPJ, MEF2, and FOX factors represent obvious potential partners, none would fully explain the specificity of all arterial enhancers and they all have wider roles in the vasculature.

Complicating analysis of our arterial enhancer cohort is the possibility that all arterial enhancers are not necessarily directly activated by the same regulator(s). Instead, a transcriptional cascade may be started by the activation of just one or two early genes, which then create a more permissive environment (e.g. high concentration or post-translation modification of transcription factors) for later arterial gene expression downstream of more widely expressed transcription factors. This would align with the observed elevated levels of SOXF expression as ECs switch to an arterial fate (Stewen et al., 2024) and may suggest that the pathways upstream of SOXF expression play the most important role in arterial gene expression. However, a far more systematic analysis of all three SOXF loci, and the enhancers within, is required to test this hypothesis.

The relatively simple and cost-effective approach of in silico identification and zebrafish transgenesis of arterial enhancers used here had a success rate around 50%. This could doubtless be further refined (e.g. by including assessments of ERG binding, obtaining enhancer marks from in vivo arterial cells), and made more efficient by limiting verification to F0 transgenic fish or utilizing a higher throughput assay (e.g.Xiao et al., 2024). However, a potentially more pressing issue is how to better understand the exact transcriptional regulators of these enhancers, a challenge shared with the gene regulatory field more widely. Transcription factors do not always bind DNA at their consensus motifs, with optimal syntax (order, orientation, and spacing of motifs) often able to compensate for poor binding sites. Additionally, the presence of multiple motifs within a single enhancer, and the ability of many transcription factors to both directly and indirectly bind enhancers, means that enhancer sequence mutational analysis can be very complicated (e.g. Sacilotto et al., 2013), whilst restricting this analysis to a single timepoint (usually required to make such an approach practical) can be an issue where angiogenic and arterial programmes overlap. While assessments of direct binding by ChIP-seq or similar approaches can bypass a requirement to understand the exact motifs at an enhancer, neither cultured HUVECs nor iPSC-derived arterial cells recapitulate conditions in vivo, particularly regarding availability of ligands, exposure to shear stress, and other environmental stimuli. Here, for example, the low expression of some of our arterial genes in culture HUVECs and HUAECs has probably affected verification of motifs with ChIP-seq data. Consequently, while this analysis has provided clarity as to some transcription factors involved (and not involved) in arterial gene expression, none of our observations fully explain the shared ability of these short sequences of DNA to direct arterial patterns of expression even when removed from native chromatin context and endogenous promoters. Some of these answers can be expected to come from increasing identification of new or unappreciated transcription factors specifically expressed or specifically modified in either arterial or non-arterial ECs (e.g. MECOM), better appreciation of the consensus motifs and binding patterns of proteins already known to be involved (e.g. DACH1), and improved proteomic techniques. Additionally, new iPSC models of endothelial differentiation offer the opportunity to more easily study the consequences of transcription factor perturbation during angiogenesis and arterial differentiation, and artificial intelligence, improved bioinformatic pathways, and machine learning all offer new avenues for research. It is anticipated that the cohort of in vivo-verified arterial enhancers characterized here will provide a vital platform for these future studies.

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
      <td>Genetic reagent (Danio rerio)</td>
      <td>tg(kdrl:Has.HRAS-mcherry)s896</td>
      <td>Chi et al., 2008</td>
      <td>ZFIN:s896</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(fli1:EGFP)</td>
      <td>Lawson et al., 2001</td>
      <td>ZFIN:y1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Cxcr4-194:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr6</td>
      <td>Enhancer mm10 chr1:128,785,499–128,786,173</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Cxcr4+135:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr7</td>
      <td>Enhancer mm10 chr1:128,456,948–128,457,375</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Cxcr4+151:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr8</td>
      <td>Enhancer mm10 chr1:128,440,589–128,441,003</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Efnb2-333:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr9</td>
      <td>Enhancer mm10 chr8:8,994,329–8,995,063</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Efnb2-159:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr10</td>
      <td>Enhancer mm10 chr8:8,819,219–8,819,856</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Efnb2-141:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr11</td>
      <td>Enhancer mm10 chr8:8,801,433–8,802,174</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Efnb2-112:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr12</td>
      <td>Enhancer mm10 chr8:8,772,171–8,772,912</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Gja4-50:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr13</td>
      <td>Enhancer mm10 chr4:127,263,607–127,264,323</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Unc5b+30:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr14</td>
      <td>Enhancer mm10 chr10:60,800,677–60,801,144</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Unc5b+39:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr15</td>
      <td>Enhancer mm10 chr10:60,792,705–60,793,377</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Acvrl1+6:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr16</td>
      <td>Enhancer mm10 chr15:101,134,018–101,134,405</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Cxcl12+269:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr17</td>
      <td>Enhancer mm10 chr6:117,437,567–117,438,123</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Gja5-78:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr18</td>
      <td>Enhancer mm10 chr3:96,953,659–96,954,322</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Gja5-7:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr19</td>
      <td>Enhancer mm10 chr3:97,025,305–97,025,791</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>tg(Nrp1+78:EGFP)</td>
      <td>This paper</td>
      <td>ZFIN:lcr20</td>
      <td>Enhancer mm10 chr8:128,437,292–128,437,815</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>tg(Dll4in3:lacZ)</td>
      <td>Sacilotto et al., 2013</td>
      <td>Tg(Rr393-lacZ)#Sav</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>E1b-GFP-Tol2-Gateway</td>
      <td>Ahituv; Birnbaum et al., 2012</td>
      <td>AddGene_#37846</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Hsp68-LacZ-Gateway</td>
      <td>Ahituv; Pennacchio et al., 2006</td>
      <td>AddGene_#37843</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HUVECs</td>
      <td>Lonza</td>
      <td>C2519A</td>
      <td>Grown in EBM-2 basal medium (Lonza CC-3156) with EBM-2 SingleQuot (Lonza CC-4176)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IgG control (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>CST 66362</td>
      <td>1:20(antibody total amount 0.5 µg)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Sox7 (goat polyclonal)</td>
      <td>R&amp;D Systems</td>
      <td>AF2766</td>
      <td>1:50 (antibody total amount 0.4 µg)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Sox17 (goat polyclonal)</td>
      <td>R&amp;D Systems</td>
      <td>AF1924</td>
      <td>1:40 (antibody total amount 0.5 µg)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Sox18 (mouse monoclonal)</td>
      <td>Abnova</td>
      <td>H00054345-M05</td>
      <td>1:100 (antibody total amount 1 µg)</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NEBNext(R) Ultra II DNA Library Prep Kit</td>
      <td>New England Biolabs</td>
      <td>NEB E7645L</td>
      <td>Using NEBNext Dual Index Multiplex Oligos NEB E7600S</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ChIP DNA Clean &amp; Concentrator kit</td>
      <td>Zymo Research</td>
      <td>D5205</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Gateway LR Clonase II Enzyme mix</td>
      <td>Thermo Fisher Scientific</td>
      <td>11791100</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>CUT&amp;RUN Kit</td>
      <td>Cell Signaling Technologies</td>
      <td>CST 86652</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>pCR8/GW/TOPO TA Cloning Kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>K250020</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ZEN 2.3 lite (blue edition)</td>
      <td>Zeiss</td>
      <td>RRID:SCR_023747</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>nf-core/cutandrun</td>
      <td>Cheshire et al., 2023</td>
      <td></td>
      <td>Version 3.1.0</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Homer</td>
      <td>Heinz et al., 2010</td>
      <td>RRID:SCR_023747</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>vennRanges</td>
      <td>https://rdrr.io/github/antonio-mora/vennRanges/#vignettes; Antonio, 2019</td>
      <td></td>
      <td>Version 0.1</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FIJI</td>
      <td>Schindelin et al., 2012</td>
      <td>RRID:SCR_002285</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Animals

All animal procedures were approved by a local ethical review committee at Oxford University and licensed by the UK Home Office and follow ARRIVE guidelines. All zebrafish were maintained in groups. F0 mosaic transgenic zebrafish embryos were generated using Tol2-mediated integration (Kawakami, 2005). The F1 stable transgenic lines were generated from an initial outcross of adult F0 carriers, in each case selecting founder transgenic zebrafish representative of the general expression patterns seen in F0 analysis. An intercross of adult F1 lines produced F2 lines. To enable visualization of the entire vasculature, the adult F1 transgenic lines were intercrossed with the tg(kdrl:HRAS-mCherry) zebrafish line. Embryos were maintained in E3 medium (5 mM NaCl; 0.17 mM KCl; 0.33 mM CaCl2; 0.33 mM MgSO4) at 28.5°C. Some of the embryos were incubated at 30–32°C to modify the speed of embryonic development. Some embryos were also treated with 0.003% phenylthiourea (Merck, P7629) at 24 hpf onwards, to inhibit pigmentation. To image, all embryos were dechorionated and anaesthetized with 0.01% Tricaine methanesulfonate in E3 medium. For analysis of transgenic zebrafish, single embryos were transferred into a flat-bottom 96-well plate, mounted in 0.1% TopVision low-melting point agarose (Thermo Fisher Scientific, R0801) in E3 medium with tricaine methanesulfonate (Merck, A5040). GFP and mCherry reporter gene expression was screened with a Zeiss LSM 980 (Carl Zeiss) confocal microscope at 32–72 hpf. Whole zebrafish were imaged using the ‘tile scan’ command, combined with Z-stack collection, at 488 nm excitation and 510 nm emission for EGFP, and at 561 nm excitation and 610 nm emission for mCherry. The eyes of the zebrafish were imaged similarly, but without tile scanning.

Adult fin analysis was performed by treating adult (3–14 months old) zebrafish with 5 g/l tricaine methanesulfonate and amputating the caudal fins with a razor blade Fins were transferred to a flat-bottom glass plate and mounted in 0.1% TopVision low-melting point agarose. GFP expression was imaged with a Zeiss LSM 980 confocal microscope as above.

E14.5 F0 transgenic mouse embryos were generated, dissected, and stained in X-gal by Cyagen Biosciences. Yolk sac was collected separately and used for genotyping. All embryos were imaged using a Leica M165C stereo microscope equipped with a ProGres CF Scan camera and CapturePro software (Jenoptik). For each enhancer, embryos were also sectioned for histological analysis to investigate X-gal staining patterns. For histological analysis, embryos were dehydrated through a series of ethanol washes, cleared by xylene, and paraffin wax-embedded. 5 or 6 μm sections were prepared, dewaxed, and counterstained with nuclear fast red (Electron Microscopy Sciences).

### Cloning

All enhancer sequences were generated as custom-made, double-stranded linear DNA fragments (GeneArt Strings, Life Technologies). The sequences of all tested enhancers are provided in Appendix 1. DNA fragments containing the enhancer sequences were cloned into the pCR8 vector using the pCR8/GW/TOPO TA Cloning Kit (Thermo Fisher Scientific, K250020) following the manufacturer’s instructions. Once cloning was confirmed, the enhancer sequence was transferred from the pCR8/GW/enhancer entry vector to a suitable destination vector using Gateway LR Clonase II Enzyme mix (Thermo Fisher Scientific, 11791100) following the manufacturer’s instructions. For zebrafish transgenesis, the enhancer was cloned into the E1b-GFP-Tol2-Gateway vector (Birnbaum et al., 2012). For mouse transgenesis, the enhancer was cloned into the hsp68-LacZ-Gateway vector.

### Enhancer mark assays

ATAC-seq in primary MAECs (SRX7016284-6) came from Engelbrecht et al., 2020, ATAC-seq in mouse postnatal day 6 (P6) retina ECs (MRECs) (SRX7267172-4) came from Yanagida et al., 2020, EP300 binding in Tie2Cre+ve cells from embryonic day (E)11.5 mouse embryos (SRX2246376-8) came from Zhou et al., 2017, H3K27Ac and H3K4Me1 in HUVECs, and DNAseI hypersensitivity in HUVECs and dermal-derived neonatal and adult blood microvascular ECs (HMVEC-dBl-neo/ad) came from the UCSC Genome Browser (Rosenbloom et al., 2013). ATAC-seq (SRX2355049 GSM2394391) and H3K27Ac (SRX2355060 GSM2394402) in cultured HAECs came from Hogan et al., 2017, ATAC-seq in telo-HAEC (SRX1689050 GSM6431161) came from Schnitzler et al., 2024, and H3K27Ac and p300 ChIP-seq in HUAECs (GSM3673407 and GSM3673413) came from Sissaoui et al., 2020.

### HOMER analysis on arterial enhancers

Analysis of overrepresented motifs within our validated arterial enhancer cohort was performed with HOMER’s findMotifsGenome tool using the full validated region of the arterial enhancers. The analysis used the hg38 masked genome and otherwise default settings for all other parameters including randomly selected background regions.

### Transcription factor binding assays

With the exception of SOX7, SOX17 and SOX18, all transcription factor binding data was previously published, and was assessed in IGV (Thorvaldsdóttir et al., 2013) either through downloading from GEO or via ChIP Atlas (Oki et al., 2018). In every case, we first verified the correct data was accessed by reproducing images at loci used in the primary publication, and highly recommend this practice for others as errors inevitably occur during data deposition. ERG and NR2F2 binding data in HUVECs (GSM3673462 and GSM3673452) came from Sissaoui et al., 2020, ETS1 binding data in HUVECs after 12 hr of VEGFA stimulation (GSM2442778 SRX2452430) came from Chen et al., 2017. FOXO1 binding data in HUVECs (GSM3681485/6 SRX5548892) came from Andrade et al., 2021 and FOXO1 binding in adult untreated mouse hearts (GSM4278011 SRX7586623) came from Pfleger et al., 2020. RBPJ binding data in HUVECs after 12 hr of VEGFA stimulation (GSM2947456 SRX3599311) came from Wang et al., 2019. SMAD1/5 binding in HUVECs after BMP9 stimulation (GSM684747 SRX045541) was from Morikawa et al., 2011, SMAD2 in HUVECs after TGFβ stimulation (GSM3955796 SRX6476491) came from Chen et al., 2019. MEF2C binding data in HUVECs (GSM809016 SRX100256) came from Maejima et al., 2014, and MEF2A binding data in mouse adult hearts (GSM3518665 SRX5146756) came from Akerberg et al., 2019.

For SOX7, SOX17, and SOX18 CUT&RUN, HUVECs were cultured in EBM-2 basal medium (Lonza CC-3156) supplemented with EBM-2 SingleQuot supplement and growth factor kit (Lonza CC-4176). DNA binding assays were performed using the CUT&RUN Kit from Cell Signaling Technologies (CST 86652) following the manufacturer’s protocol with slight modifications. For SOX7 and SOX17, harvested cells were lightly crosslinked with 0.1% formaldehyde for 2 min and processed with buffers supplemented with 1% Triton X-100 and 0.05% SDS. SOX18 CUT&RUN was performed without crosslinking and with buffers as per standard protocol. Cells were bound to Concanavalin A beads and incubated overnight with antibodies against IgG control (CST 66362), SOX7 (R&D Systems, AF2766), or SOX17 (R&D Systems, AF1924) or SOX18 (Abnova, H00054345-M05) in wash buffer containing 0.05% digitonin. DNA around binding sites was cleaved with pAG-MNase enzyme. For SOX7 and SOX17, the released DNA was reverse-crosslinked with proteinase K and 0.1% SDS overnight at 65°C. DNA fragments were purified with a ChIP DNA Clean & Concentrator kit (Zymo Research D5205). DNA was converted into Illumina-compatible libraries with the NEBNext(R) Ultra(TM) II DNA Library Prep Kit (NEB E7645L) following the protocol described by Liu, 2019 and using NEBNext Dual Index Multiplex Oligos (NEB E7600S). Libraries were sequenced on a NextSeq2000 (SOX17) or a NovaSeq (SOX7 and SOX18) using paired end reads. Data was processed using the nf-core/cutandrun v3.1 pipeline (10.5281/zenodo.5653535; Ewels et al., 2020) with the following adjustments to the default settings: --normalisation_mode CPM and --trim_nextseq 20. The CUT&RUN hg38 blacklist (Nordin et al., 2023) or hg19 ENCODE blacklist (Amemiya et al., 2019) was used during sequence alignment. Peak calling was performed with SEACR (Meers et al., 2019) using stringent settings, and by HOMER (Heinz et al., 2010) using default settings for transcription factors (-style factor). Motif analysis was performed with HOMER using 200 nt regions around peak centres. Overlap of SOX7, SOX17, and SOX18 hg19-aligned peaks with published mCherry-SOX7 data (Overman et al., 2017), HUVEC enhancer marks and TSS (Sissaoui et al., 2020) was executed using the vennRanges R package. Data has been deposited to GEO under the accession number GSE283369.

### Reanalysis of scRNA-seq data

Publicly available E12 and E17.5 scRNA-seq data from EC isolated from BmxCreERT2;RosatdTomato lineage traced murine hearts (D’Amato et al., 2022) was obtained from GEO (GSE214942) prior to processing FASTQ files with the 10X Genomics CellRanger pipeline (V7.0.0). RNA-seq reads were aligned to the mm10 genome reference downloaded from 10X Genomics with the addition of the TdTomato-WPRE sequence. Exclusion of low-quality cells with either a UMI count >100,000,, total gene count <1500, or a high proportion of reads originating from mitochondrial genes (>10%) was performed using Scater (McCarthy et al., 2017). Data normalization was performed using the MultiBatchNormalisation method prior to merging of TdTomato-positive and -negative datasets from individual timepoints. The top 2000 most highly variable genes (excluding mitochondrial and ribosomal genes) in the merged datasets were identified using the Seurat FindVariableFeatures method and utilized to calculate principal component analysis. Normalized data was scaled using the ScaleData function. Cell clustering was performed using the standard unsupervised graph-based clustering method implemented within Seurat (V4) (Hao et al., 2024). Clusters were visualized in two dimensions using UMAP based non-linear dimensional reduction following the standard Seurat (V4) workflow (Chen et al., 2019). Identified clusters were assigned identities based on marker genes shown to be differentially expressed between populations previously identified in the original study (Wang et al., 2019). Key markers include Npr3 (endocardial), Fabp4 (coronary vascular endothelial), and Nfatc1 (valvular endothelial). The E12.5 sinus venosus EC cluster was assigned based in Aplnr as previously described (D’Amato et al., 2022). Arterial and venous EC clusters in the E17.5 datasets were annotated based on their enriched expression of Gja5 and Nr2f2, respectively.

### Materials availability statement

The newly created zebrafish lines tg(Cxcr4-194:EGFP), tg(Cxcr4+135:EGFP), tg(Cxcr4+151:EGFP), tg(Efnb2-333:EGFP), tg(Efnb2-159:EGFP), tg(Efnb2-141:EGFP), tg(Efnb2-112:EGFP), tg(Gja4-50:EGFP), tg(Unc5b+30:EGFP), tg(Unc5b+39:EGFP), tg(Acvrl1+6:EGFP), tg(Cxcl12+269:EGFP), tg(Gja5-78:EGFP), tg(Gja5-7:EGFP) and tg(Nrp1+78:EGFP), and the plasmids used to generate them are all available on request from the corresponding author. The SOX7, SOX17, and SOX18 CUT&RUN data is deposited at GEO under the accession number GSE283369.
