# Stable flow-induced expression of KLK10 inhibits endothelial inflammation and atherosclerosis

## Authors

- Darian Williams<sup>1</sup> ([ORCID: 0000-0002-4572-3056](https://orcid.org/0000-0002-4572-3056))
- Marwa Mahmoud<sup>1</sup>
- Renfa Liu<sup>1</sup>
- Aitor Andueza<sup>1</sup>
- Sandeep Kumar<sup>1</sup>
- Dong-Won Kang<sup>1</sup>
- Jiahui Zhang<sup>1</sup>
- Ian Tamargo<sup>2</sup>
- Nicolas Villa-Roel<sup>1</sup> ([ORCID: 0000-0002-2981-9330](https://orcid.org/0000-0002-2981-9330))
- Kyung-In Baek<sup>1</sup>
- Hwakyoung Lee<sup>4</sup>
- Yongjin An<sup>4</sup>
- Leran Zhang<sup>5</sup>
- Edward W Tate<sup>5</sup>
- Pritha Bagchi<sup>6</sup>
- Jan Pohl<sup>7</sup>
- Laurent O Mosnier<sup>8</sup>
- Eleftherios P Diamandis<sup>9</sup> ([ORCID: 0000-0002-1589-820X](https://orcid.org/0000-0002-1589-820X))
- Koichiro Mihara<sup>10</sup>
- Morley D Hollenberg<sup>10</sup>
- Zhifei Dai<sup>3</sup>
- Hanjoong Jo<sup>1</sup> ([ORCID: 0000-0003-1833-372X](https://orcid.org/0000-0003-1833-372X)) †

### Affiliations

1. Coulter Department of Biomedical Engineering, Emory University and Georgia Institute of Technology Atlanta United States
2. Molecular and Systems Pharmacology Program, Emory University Atlanta United States
3. Department of Biomedical Engineering, Peking University Beijing China
4. Celltrion Incheon Republic of Korea
5. Department of Chemistry, Imperial College London London United Kingdom
6. Emory Integrated Proteomics Core, Emory University Atlanta United States
7. Biotechnology Core Facility Branch, Centers for Disease Control and Prevention Atlanta United States
8. Department of Molecular Medicine, Scripps Research Institute San Diego United States
9. Department of Pathology and Laboratory Medicine, Mount Sinai Hospital Toronto Canada
10. Department of Physiology and Pharmacology, University of Calgary Calgary Canada
11. Department of Medicine, Emory University Atlanta United States

† Corresponding author

## Abstract

Atherosclerosis preferentially occurs in arterial regions exposed to disturbed blood flow (d-flow), while regions exposed to stable flow (s-flow) are protected. The proatherogenic and atheroprotective effects of d-flow and s-flow are mediated in part by the global changes in endothelial cell (EC) gene expression, which regulates endothelial dysfunction, inflammation, and atherosclerosis. Previously, we identified kallikrein-related peptidase 10 (Klk10, a secreted serine protease) as a flow-sensitive gene in mouse arterial ECs, but its role in endothelial biology and atherosclerosis was unknown. Here, we show that KLK10 is upregulated under s-flow conditions and downregulated under d-flow conditions using in vivo mouse models and in vitro studies with cultured ECs. Single-cell RNA sequencing (scRNAseq) and scATAC sequencing (scATACseq) study using the partial carotid ligation mouse model showed flow-regulated Klk10 expression at the epigenomic and transcription levels. Functionally, KLK10 protected against d-flow-induced permeability dysfunction and inflammation in human artery ECs, as determined by NFκB activation, expression of vascular cell adhesion molecule 1 and intracellular adhesion molecule 1, and monocyte adhesion. Furthermore, treatment of mice in vivo with rKLK10 decreased arterial endothelial inflammation in d-flow regions. Additionally, rKLK10 injection or ultrasound-mediated transfection of Klk10-expressing plasmids inhibited atherosclerosis in Apoe−/− mice. Moreover, KLK10 expression was significantly reduced in human coronary arteries with advanced atherosclerotic plaques compared to those with less severe plaques. KLK10 is a flow-sensitive endothelial protein that serves as an anti-inflammatory, barrier-protective, and anti-atherogenic factor.

## Introduction

Atherosclerosis is an inflammatory disease that preferentially occurs in branched or curved arterial regions exposed to disturbed flow (d-flow), while areas of stable flow (s-flow) are protected from atherosclerosis (Chiu and Chien, 2011; Davies, 1995; Kwak et al., 2014; Tarbell et al., 2014). Endothelial cells (ECs) are equipped with several mechanosensors located at the luminal and abluminal surface, cell–cell junction, and cytoskeleton, which detect fluid shear stress and trigger cascades of signaling pathways and cellular responses (Kwak et al., 2014; Tarbell et al., 2014; Mack et al., 2017; Tzima et al., 2005; Li et al., 2015; Chachisvilis et al., 2006; Florian et al., 2003; Wang et al., 2016). D-flow induces endothelial dysfunction and atherosclerosis in large part by regulating flow-sensitive coding and noncoding genes, as well as epigenetic modifiers (Davies, 1995; Kumar et al., 2014; Kumar et al., 2019; Dunn et al., 2014). Using the partial carotid ligation (PCL) mouse model of atherosclerosis and transcriptomic studies, we identified hundreds of flow-sensitive genes in ECs that change by d-flow in the left carotid artery (LCA) compared to the s-flow in the right carotid artery (RCA) (Nam et al., 2009; Ni et al., 2010). Among the flow-sensitive genes, kallikrein-related peptidase 10 (Klk10) was identified as one of the most flow sensitive; with high expression under s-flow and low expression under d-flow conditions (Ni et al., 2010). However, its role in endothelial function and atherosclerosis was not known.

KLK10 was initially identified as a normal epithelial cell-specific 1 (NES1) (Diamandis et al., 2000) and is a member of the kallikrein-related peptidase ‘KLK’ family of 15 secreted serine proteases, which are found as a gene cluster on human chromosome (19q13.4) (Yousef et al., 1999). The tissue KLKs are distinct from plasma kallikrein, which is encoded on a separate chromosome (4q35) (Yousef and Diamandis, 2003). Despite the chromosomal clustering of the KLKs, each enzyme has a unique tissue expression pattern with different cellular functions. Typically, the KLKs are produced as inactive full-length prepropeptides, which are then secreted and activated by a complex process to yield active extracellular enzyme (Yousef and Diamandis, 2003). KLKs are involved in a wide variety of processes ranging from skin desquamation to tooth development, hypertension, and cancer (Madeddu et al., 2007; Clements et al., 2004; Yousef and Diamandis, 2001; Pampalakis and Sotiropoulou, 2007; Margolius, 1998; Campbell, 2001).

KLK10 was initially discovered as a potential tumor suppressor with its expression downregulated in breast, prostate, testicular, and lung cancer (Goyal et al., 1998; Liu et al., 1996; Hu et al., 2015; Luo et al., 2001; Zhang et al., 2010). Further studies, however, showed a more complex story as KLK10 is overexpressed in ovarian, pancreatic, and uterine cancer (Luo et al., 2003; Yousef et al., 2005; Dorn et al., 2013; Tailor et al., 2018; Sotiropoulou et al., 2009; Bharaj et al., 2002). However, the role of KLK10 for endothelial function and atherosclerosis is not known.

Here, we tested the hypothesis that KLK10 mediates the anti-atherogenic effects of s-flow, while the loss of KLK10 under d-flow conditions leads to proatherogenic effects.

## Results

### KLK10 expression is increased by s-flow and decreased by d-flow in ECs in vitro and in vivo

We first validated our previous mouse gene array data at the mRNA and protein levels by additional quantitative real-time polymerase chain reaction (qPCR), immunostaining, western blots, and ELISA in ECs in vivo and in vitro. To validate the flow-dependent regulation of KLK10 expression in vivo, mouse PCL surgery was performed to induce d-flow in the LCA while maintaining s-flow in RCA (Figure 1a). Consistent with our previous data (Nam et al., 2009; Ni et al., 2010), KLK10 protein (Figure 1b, c) and mRNA expression (Figure 1d) were significantly higher in ECs in the s-flow RCA compared to the d-flow LCA. Interestingly, KLK10 protein was also found in the adventitia and occasionally observed in the subendothelial layer as well (Figure 1b). In addition, KLK10 protein expression was reduced in the lesser curvature (LC; the atheroprone aortic arch region that is naturally and chronically exposed to d-flow) compared to the greater curvature region (GC; the atheroprotected aortic arch region that is naturally and chronically exposed to s-flow) as shown by en face immunostaining (Figure 1e, f).

![Figure 1.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig1-v2.jpg)

**Figure 1.:** (a) Depiction of the partial carotid ligation (PCL) surgery and flow-sensitive regions in the aortic arch: right carotid artery (RCA; s-flow), left carotid artery (LCA; d-flow), greater curvature (GC: s-flow), and lesser curvature (LC; d-flow). Two days following the PCL of C57BL/6J mice, the RCA and LCA were collected for frozen section imaging (b, c) and (d) endothelial-enriched RNA preparation. (b) Confocal images of immunostaining with anti-KLK10 or anti-CD31 antibodies (red) and counterstained with 4',6-diamidino-2-phenylindole (DAPI, blue) are shown. Scale bar = 20 μm. Arrows indicate endothelial cells and L is the lumen. (c) Quantification of endothelial KLK10 fluorescence intensity expressed as fold-change normalized to the RCA. N = 4. (d) Klk10 mRNA was measured in endothelial-enriched RNA from the carotid arteries by quantitative real-time polymerase chain reaction (qPCR). Data are expressed as fold-change normalized to 18s internal control. N = 3–4. (e) Confocal images of en face coimmunostaining of the LC and GC with anti-KLK10 (green) and anti-VE-Cadherin (red) antibody are shown counterstained with DAPI (blue). Scale bar = 10 μm. (f) Quantification of endothelial KLK10 fluorescence intensity expressed as fold-change normalized to the GC. N = 5. (g–j) Human artery endothelial cells (HAECs) subjected to 24 hr of unidirectional laminar shear (LS; 15 dynes/cm2) or oscillatory shear (OS; ± 5 dynes/cm2) were used to measure expression of KLK10 mRNA by qPCR (g), KLK10 protein in cell lysates by western blot (h, i), and KLK10 protein secreted to the conditioned media by ELISA (j). N = 4–6. All data are represented as mean ± standard error of mean (SEM). Statistical analyses were performed using paired t-test (Figure 1—source data 1). (k) Single-cell RNAseq analysis of Klk10 gene transcripts and (l) single-cell ATACseq analysis of Klk10 chromatin accessibility in eight endothelial cell clusters (E1–E8), smooth muscle cells (SMCs), fibroblasts (Fibro), 4 monocytes/macrophages clusters (Mo1–4), dendritic cells (DCs), and T cells (T) in the mouse carotid arteries following 2 days or 2 weeks of the PCL surgery as we recently reported (Andueza et al., 2020). The published datasets (Andueza et al., 2020) were reanalyzed here for the Klk10 gene. E1–E4 clusters represent ECs exposed to s-flow conditions in the RCA. E5 and E7 clusters represent ECs exposed to acute (2 days) d-flow in the LCA. E6 and E8 clusters represent ECs exposed to chronic (2 weeks) d-flow in the LCA. TSS indicates transcription start site.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Violin plots show single-cell expression of (a) Klk10 and (b) CD31 (Pecam1) gene transcripts in eight endothelial cell clusters (E1–E8), smooth muscle cells (SMCs), fibroblasts (Fibro), 4 monocytes/macrophages clusters (Mo1–4), dendritic cells (DCs), and T cells (T) in the mouse carotid arteries following 2 days or 2 weeks of the PCL surgery as we recently reported (Andueza et al., 2020). The published scRNAseq data (Andueza et al., 2020) were reanalyzed here for Klk10 and Pecam1 genes. E1–E4 clusters represent ECs exposed to s-flow conditions in the right carotid artery (RCA). E5 and E7 clusters represent ECs exposed to acute (2 days) d-flow in the LCA. E6 and E8 clusters represent ECs exposed to chronic (2 weeks) d-flow in the LCA.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** The plots display single-cell chromatin accessibility status of (a) Klk10 and (b) CD31 (Pecam1) genes in eight endothelial cell clusters (E1–E8), smooth muscle cells (SMCs), fibroblasts (Fibro), 4 monocytes/macrophages clusters (Mo1–4), dendritic cells (DCs), and T cells (T) in the mouse carotid arteries following 2 days or 2 weeks of the PCL surgery as we recently reported (Andueza et al., 2020). The published scATACseq data (Andueza et al., 2020) were reanalyzed here for Klk10 and Pecam1 genes. E1–E4 clusters represent ECs exposed to s-flow conditions in the right carotid artery (RCA). E5 and E7 clusters represent ECs exposed to acute (2 days) d-flow in the LCA. E6 and E8 clusters represent ECs exposed to chronic (2 weeks) d-flow in the LCA.

We next tested whether flow can regulate KLK10 expression in vitro using human aortic ECs (HAECs) exposed to unidirectional laminar shear (LS at 15 dynes/cm2) or oscillatory shear (OS at ±5 dynes/cm2 at 1 Hz) for 24 hr using the cone-and-plate viscometer, mimicking s-flow and d-flow conditions in vivo, respectively (Jo et al., 2006; Chang et al., 2007). KLK10 mRNA (Figure 1g), KLK10 protein in cell lysates (Figure 1h, j), and secreted protein in the conditioned media (Figure 1j) were decreased by OS and increased by LS, confirming the role of KLK10 as a flow-sensitive gene and protein in vivo and in vitro.

We further confirmed the flow-dependent expression of Klk10 by reanalyzing the single-cell RNA sequencing (scRNAseq) and scATACseq datasets that we recently published using the PCL model (Andueza et al., 2020). For the scRNAseq and scATACseq study, single cells and nuclei obtained from the LCAs and RCAs, respectively, at 2 days or 2 weeks after the PCL were used. As described previously, the carotid artery wall cells were identified as EC clusters (E1–E8), smooth muscle cells (SMCs), fibroblasts (Fibro), monocytes/macrophages (Mo1–4), dendritic cells (DCs), and T cells (Andueza et al., 2020, Figure 1k). E1–E4 clusters consisted of ECs exposed to acute and chronic s-flow conditions (2 days and 2 weeks). E5–E7 clusters consisted of ECs exposed to acute d-flow (2 days). E8 cells were exclusively found in the chronic d-flow condition (2 weeks). As shown in the scRNAseq data analysis (Figure 1k; Figure 1—figure supplement 1), Klk10 transcript expression is highest in s-flow (E2 and E3) and decreases in response to acute (E5 and E7) and chronic (E6 and E8) d-flow. It also shows Klk10 expression is specific to ECs and not expressed in other cell types studied in the carotid artery. Similarly, scATACseq data (Figure 1i; Figure 1—figure supplement 2) showed that the Klk10 promoter region is open and accessible (indicating active transcription status) only in ECs exposed to s-flow conditions but closed and inaccessible (indicating inactive transcription status) in ECs under d-flow conditions and all other non-EC types. Together, both the scRNAseq and scATACseq results demonstrate that Klk10 expression is potently regulated by flow in ECs at the epigenomic and transcriptome level, supporting the in vitro and in vivo results shown above (Figure 1b–g). Importantly, all non-EC types in the carotid artery express nearly undetectable levels of Klk10 mRNA transcript and also display closed chromatin accessibility in the Klk10 promoter region, demonstrating that Klk10 is primarily expressed by ECs. This suggests that KLK10 protein observed in nonendothelial layers, including the adventitia and subendothelial layer (Figure 1b), is unlikely to be originated from cell types other than ECs.

### KLK10 inhibits endothelial inflammation and protects permeability barrier

We next tested if KLK10 regulates EC function by evaluating its role in endothelial inflammatory response, tube formation, migration, proliferation, and apoptosis, which play critical roles in the pathogenesis of atherosclerosis. Treatment of human umbilical vein ECs (HUVECs) with rKLK10 significantly inhibited migration and tube formation, but not proliferation and apoptosis (Figure 2—figure supplement 1). In addition, transfection of HAECs with plasmids to overexpress KLK10 reduced THP-1 monocyte adhesion to the ECs in response to tumor necrosis factor alpha (TNFα) and under basal conditions (Figure 2a; Figure 2—figure supplement 2). Next, we pretreated HAECs overnight with increasing concentrations of rKLK10, followed by TNFα treatment (5 ng/ml for 4 hr). Treatment with rKLK10 significantly inhibited monocyte adhesion to ECs in a concentration-dependent manner (Figure 2b). Of note, the anti-inflammatory effect of rKLK10 was lost if rKLK10 was heated, implicating the importance of the enzymatic activity or native conformation of KLK10 (Figure 2b; Figure 2—figure supplement 3). Furthermore, treatment with rKLK10 significantly inhibited mRNA and protein expression of the proinflammatory adhesion molecules vascular cell adhesion molecule 1 (VCAM1) and intracellular adhesion molecule 1 (ICAM1) (Figure 2c–g).

![Figure 2.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig2-v2.jpg)

**Figure 2.:** (a) THP-1 monocyte adhesion assay was carried out in human artery endothelial cells (HAECs) transfected with 0.1 or 0.25 μg of KLK10 plasmid (KLK10-p) or GFP plasmid (GFP-p) for 48 hr followed by TNFɑ treatment (5 ng/ml for 4 hr). Data are represented as percentage of monocyte adhesion normalized to GFP-p control. N = 3. (b) THP-1 monocyte adhesion assay was carried out in HAECs treated with rKLK10 (0.1–10 ng/ml) or heat-inactivated rKLK10 (HI-10) for 24 hr followed by TNFɑ treatment (5 ng/ml for 4 hr). Data are represented as percentage of monocyte adhesion normalized to vehicle control. N = 3. (c–g) HAECs were treated with rKLK10 (0.1–10 ng/ml for 24 hr) followed by TNFɑ treatment (5 ng/ml for 4 hr) and expression of vascular cell adhesion molecule 1 (VCAM1) and intracellular adhesion molecule 1 (ICAM1) were assessed by quantitative real-time polymerase chain reaction (qPCR) (c, d) or western blot (e–g). N = 3. Data are represented as fold-change of the vehicle control and normalized to 18s or GAPDH (Figure 2—source data 1). (h, i) THP-1 monocyte adhesion assay was conducted on HAECs subjected to 24 hr of either laminar shear (LS; 15 dynes/cm2) or oscillatory shear (OS; ±5 dynes/cm2) with either (h) rKLK10 (100 ng/ml) or (i) KLK10 siRNA (50 nM) or a nontargeting siRNA control. Data are represented as percentage of monocyte adhesion normalized to the control OS condition. N = 3–7. (j) C57BL/6J mice were injected with rKLK10 (0.6 mg/kg) or a vehicle control by tail vein once every 2 days for 5 days. The aortic arches were en face immunostained and imaged using confocal microscopy with an anti-VCAM1 antibody (red) and DAPI (blue). (k) Quantification of endothelial VCAM1 fluorescence intensity represented as fold-change normalized to control LC condition. N = 4–5. Scale bar = 10 μm. All data are represented as mean ± standard error of mean (SEM). Statistical analyses were performed using one-way analysis of variance (ANOVA) with Bonferroni correction for multiple comparisons.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Human umbilical vein endothelial cells (HUVECs) were treated with rKLK10 from 0.5 to 100 ng/ml and (a) the scratch assay was performed to measure the rate at which endothelial cells migrated across the scratch; (b) apoptosis was assessed by TUNEL staining; (c) proliferation was assayed by Ki67 imunnostaining. (d) HUEVCs were grown on Matrigel and treated with rKLK10 at 100 ng/ml or vehicle and tube length was measured in ImageJ. N = 3–5. One-way analysis of variance (ANOVA) with Bonferroni correction for multiple comparisons where appropriate (a–c) or paired two-tailed t-test (d). Mean ± standard error of mean (SEM).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (a) Human aortic endothelial cells (HAECs) were transfected with KLK10 plasmid ranging from 0.1 to 1 or 1 μg/ml GFP plasmid for 24 hr and the THP-1 monocyte adhesion assay was performed. N = 3. (b) HAECs were treated with 0.5–100 ng/ml rKLK10 and monocyte adhesion assay was performed. N = 4–6. (c) HAECs were treated with 100 ng/ml rKLK10 for 24 hr and quantitative real-time polymerase chain reaction (qPCR) was performed to assess mRNA expression of VCAM1, ICAM1, and MCP1. N = 3–5. One-way analysis of variance (ANOVA) with Bonferroni correction for multiple comparisons (a, b) or two-way ANOVA with Bonferroni correction for multiple comparisons. (c) Mean ± standard error of mean (SEM).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (a, b) Human aortic endothelial cells (HAECs) were treated with TNFα (5 ng/ml) for 4 hr followed by 1, 10, or 10 ng/ml heat-inactivated (HI) rKLK10 overnight and mRNA expression of (a) Vcam1 and (b) Icam1 mRNA was measured by quantitative real-time polymerase chain reaction (qPCR). n = 3. One-way analysis of variance (ANOVA) with Bonferroni correction for multiple comparisons. Mean ± standard error of mean (SEM).

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (a) Mice (male, C57BL/6J) were administered 0.006–0.6 mg/kg rKLK10 or vehicle by tail-vein injection and inflammation was assessed by en face immunostaining of VCAM1 at the lesser curvature (LC) and the greater curvature (GC) of the aortic arch. Red = VCAM1, blue = DAPI, green = Elastin. Scale bar = 10 µm. (b) Quantification of VCAM1 staining in A normalized to the LC. Shown are mean ± standard error of mean (SEM), N = 3–6. Two-way analysis of variance (ANOVA) with Bonferroni correction for multiple comparisons. Part of results in (a) and (b) are shown in Figure 2j. (c) C57BL/6J mice (8-week-old males, n = 12) were injected with human rKLK10 (0.6 mg/kg) via tail-vein injection in three groups (n = 4 mice per group) to collect blood via cheek vein at three different time points per group: (1) before injection (Time 0), 1, and 12 hr, (2) 0, 3, and 24 hr, and (3) 0, 6, and 48 hr after the injection. rKLK10 levels in the plasma were determined by human KLK10 ELISA and data were shown as one phase decay plot. t1/2 of rKLK10 was 4.458 hr. Mean ± SEM is shown.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** En face immunostaining for VCAM1 (shown in Figure 2j) was imaged by confocal microscopy. Shown is a Z-section image demonstrating VCAM1 expression (red) at the endothelial layer above the internal elastic lamina (green). Blue is DAPI. XYZ refers to an optical plane in the confocal image.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** (a) Human aortic endothelial cells (HAECs) were transfected with 0.02–1 μg/ml KLK10 plasmid or 1 μg/ml GFP plasmid and KLK10 mRNA expression was measured by quantitative real-time polymerase chain reaction (qPCR). N = 3–4. (b) HAECs were transfected with 0.02–1 μg/ml KLK10 plasmid or 1 μg/ml GFP plasmid and KLK10 secretion into the media was measured by ELISA. N = 3–5. (c) HAECs were transfected with 0.5–2 μg/ml KLK10 plasmid or 2 μg/ml GFP and KLK10 protein expression was measured by western blot, using GAPDH as an internal control. N = 3 (Figure 2—figure supplement 6—source data 1). (d) HAECs were transfected with 25–100 nM KLK10 siRNA or 100 nM scrambled siRNA and KLK10 mRNA expression was measured by qPCR. N = 3–5. Mean ± standard error of mean (SEM). One-way ANOVA with Bonferroni correction for multiple comparisons where appropriate.

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig2-figsupp7-v2.jpg)

**Figure 2—figure supplement 7.:** Human rKLK10 with His-tag overexpressed in CHO cells was purified by affinity chromotagraphy. Purified rKLK10 (5 µg) was resolved by sodium dodecyl sulfate–polyacrylamide gel electrophoresis (SDS–PAGE) under reducing (R) or nonreducing (NR) conditions and stained with Coomassie blue (Figure 2—figure supplement 7—source data 1).

We then tested the effect of KLK10 on the endothelial inflammatory response under flow conditions in vitro and in vivo. rKLK10 treatment inhibited OS-induced monocyte adhesion in HAECs (Figure 2h). In contrast, siRNA-mediated knockdown of KLK10 significantly increased monocyte adhesion under LS conditions (Figure 2i). We next tested if rKLK10 could also inhibit the endothelial inflammation in naturally flow-disturbed LC of the aortic arch in mice. Treatment with rKLK10 in vivo (intravenous injection every 2 days for 5 days at 0.6 mg/kg) dramatically reduced VCAM1 expression in the d-flow (LC) region in the aortic arch of these mice (Figure 2j, k). We also observed a dose-dependent effect of rKLK10 on VCAM1 expression in the same study (Figure 2—figure supplement 4). Injection of rKLK10 at 0.6 mg/kg dose increased its plasma level to a peak of ~1600 ng/ml with a t1/2 of 4.5 hr, becoming undetectable by 24 hr (Figure 2—figure supplement 4). These results demonstrate that either KLK10 overexpression using plasmids or rKLK10 treatment protects against EC inflammation both in vitro and in vivo under TNFα or d-flow conditions, whereas the reduction of KLK10 by d-flow condition or KLK10 mRNA knockdown using siRNA increases inflammation.

Since NFκB is a well-known proinflammatory transcription factor, which induces expression of VCAM1 and ICAM1 and subsequent monocyte adhesion to ECs (Baeriswyl et al., 2019; Baeyens et al., 2014; Chen et al., 2003; Coleman et al., 2020; Lay et al., 2019; Mohan et al., 1997; Petzold et al., 2009; Stefanini et al., 2015; Wang et al., 2009; Wilson et al., 2013), we tested whether KLK10 inhibits NFκB activation in response to shear stress and TNFα. We first found that KLK10 prevented phosphorylation (p-Ser536) and trans-nuclear location of p65, two important markers of NFκB activation, in response to TNFα (Figure 3a–d). KLK10 also prevented trans-nuclear location of p65 in response to acute shear challenge using LS condition (Figure 3e, f), which is well known to induce robust and transient NFκB activation (Baeriswyl et al., 2019; Baeyens et al., 2014; Chen et al., 2003; Coleman et al., 2020; Lay et al., 2019; Mohan et al., 1997; Petzold et al., 2009; Stefanini et al., 2015; Wang et al., 2009; Wilson et al., 2013).

![Figure 3.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig3-v2.jpg)

**Figure 3.:** (a, b) Human aortic endothelial cells (HAECs) were treated with rKLK10 (10 ng/ml) or vehicle for 16 hr followed by TNFα (5 ng/ml for 4 hr). Cell lysates were then collected and analyzed for phosphorylated p65 (p-p65) by sodium dodecyl sulfate–polyacrylamide gel electrophoresis (SDS–PAGE). Data are expressed as p-p65 fold-change normalized to GAPDH and vehicle control. N = 3 (Figure 3—source data 1). (c, d) HAECs were treated with rKLK10 (10 ng/ml) or vehicle for 16 hr followed by TNFα (5 ng/ml for 4 hr). Cells were then fixed and immunostained for p65 using anti-p65 antibody. Data are expressed as nuclear p65/total p65, normalized to the vehicle control. N = 6. (e, f) HAECs were treated with rKLK10 (10 ng/ml) or vehicle for 16 hr and exposed to shear for 1 hr. Cells were then fixed and immunostained for p65 using anti-p65 antibody. Data are expressed as nuclear p65/total p65, normalized to the static control. N = 4. All data are represented as mean ± standard error of mean (SEM). Statistical analyses were performed using one-way analysis of variance (ANOVA) with Bonferroni correction.

Next, we tested if rKLK10 treatment can protect the permeability barrier function of ECs. As a positive control, thrombin treatment increased the permeability of HAECs as measured by increased binding of fluorescently labeled (FITC)-avidin to biotin-gelatin as reported previously (Dubrovskyi et al., 2013). Overnight rKLK10 pretreatment prevented the permeability increase induced by thrombin in HAECs (Figure 4a, b). Similarly, rKLK10 reduced the permeability induced by OS (Figure 4c, d). Together, these results demonstrate the protective role of KLK10 in endothelial inflammation and barrier function.

![Figure 4.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig4-v2.jpg)

**Figure 4.:** Human aortic endothelial cells (HAECs) were grown to confluency on biotinylated gelatin and were treated with (a, b) rKLK10 (10 ng/ml) or vehicle for 16 hr followed by thrombin (5 U/ml for 30 min), or (c, d) exposed to OS (±5 dynes/cm2) with rKLK10 (10 ng/ml) or vehicle for 24 hr. Endothelial permeability was then measured by the binding of FITC-avidin to the biotinylated gelatin. (b, d) Quantification of endothelial permeability measured as FITC-avidin fluorescence intensity. N = 3 each. Scale bar = 50 μm. All data are represented as mean ± standard error of mean (SEM). Statistical analyses were performed using one-way analysis of variance (ANOVA) with Bonferroni correction (b) or paired t-test (d).

### Treatment with rKLK10 inhibits atherosclerosis in Apoe−/− mice

Given its anti-inflammatory and barrier-protective effect in ECs, we tested if atherosclerosis development could be prevented by treating mice with rKLK10. For this study, we used the PCL model of atherosclerosis to induce atherosclerosis rapidly in a flow-dependent manner in hyperlipidemic Apoe−/− mice fed with a high-fat diet. Injection with rKLK10 by tail vein (twice per week at 0.6 mg/kg for 3 weeks post-PCL surgery) significantly reduced atherosclerosis development and macrophage accumulation in the LCA (Figure 5a–e). The rKLK10 treatment showed no effect on plasma levels of total, LDL (low-density lipoprotein), and HDL (high-density lipoprotein) cholesterols and triglycerides (Figure 5f–i). Thus, rKLK10 showed an anti-atherogenic effect in vivo.

![Figure 5.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig5-v2.jpg)

**Figure 5.:** (a) Apoe−/− were subjected to partial carotid ligation and high-fat diet feeding. The mice received either rKLK10 (0.6 mg/kg) or vehicle injection every 3 days for the duration of 3 weeks. Left carotid artery (LCA) showed plaque development, which was reduced by rKLK10 as shown by dissection microscopy. Frozen sections from the LCA and right carotid artery (RCA) were stained with (b) H&E and (c) for CD68 in LCA. DAPI (blue). Scale bar low mag = 250 μm, high mag = 50 μm. (d) Plaque area was quantified from H&E staining and is represented as μm2. (e) CD68 fluorescence intensity was quantified and is represented as the CD68 fold-change normalized to the control. Plasma lipid analysis of (f) total cholesterol, (g) low-density lipoprotein (LDL cholesterol), (h) high-density lipoprotein (HDL) cholesterol, or (i) triglycerides showed no effect of rKLK10 compared to control. All data are represented as mean ± standard error of mean (SEM). Statistical analyses were performed using paired t-test. N = 6. ns = not significant.

### Ultrasound-mediated overexpression of KLK10 inhibits atherosclerosis in Apoe−/− mice

We next asked whether overexpression of KLK10 using a plasmid vector could also inhibit atherosclerosis in vivo. For this study, we injected either KLK10 plasmid (pCMV-Igκ-Klk10-T2A-Luc) or luciferase plasmid (pCMV-Luc) as a control along with microbubbles to the hind-limbs of Apoe−/− mice and sonoporated the legs with ultrasound as previously described (Liu et al., 2019; Borden et al., 2005; Shapiro et al., 2016). The plasmid injection and sonoporation were repeated 10 days later to ensure sustained protein expression for the duration of the study. Bioluminescence imaging showed that all mice expressed luciferase in the hind-limbs at the conclusion of the study, indicating successful and sustained overexpression of the plasmids (Figure 6a).

![Figure 6.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig6-v2.jpg)

**Figure 6.:** (a) Bioluminescent imaging of Apoe−/− partial carotid ligation (PCL) mice on a high-fat diet injected with luciferase control plasmid or Klk10-luciferase plasmid, measured in photons/second. (b) Gross plaque images of excised carotid arteries and (c) quantification of plaque burden normalized to the percentage of the luciferase control. (d) H&E staining of sections from the left carotid artery (LCA) and right carotid artery (RCA) of mice injected with luciferase control plasmid or Klk10-luciferase plasmid. Scale bar low mag = 250 μm, high mag = 50 μm. (e) Quantification of plaque area measured in μm2. All data are represented as mean ± standard error of mean (SEM). Statistical analyses were performed using paired t-test. N = 11. (f) Sections from the RCA and LCA were coimmunostained with anti-KLK10 (orange) and anti-CD31 (red) antibodies. Blue is DAPI. Arrows indicate the ECs. L is the lumen and Adv is the adventitia. Scale bar = 10 μm. (g) Quantification of endothelial KLK10 fluorescent intensity represented as fold-change normalized to luciferase control. (h) Western blot analysis of KLK10 expression in lung tissue from mice injected with control luciferase plasmid or Klk10 plasmid (Figure 6—source data 1). (i) Quantification of KLK10 expression normalized to GAPDH and luciferase control. Plasma lipid analysis of (j) total cholesterol, (k) triglycerides, (l) high-density lipoprotein (HDL) cholesterol, (m) low-density lipoprotein (LDL) cholesterol, or (n) non-HDL cholesterol. All data are represented as mean ± SEM. Statistical analyses were performed using paired t-test. N = 5. ns = not significant.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** KLK10 expression was measured in the plasma from mice overexpressing luciferase (Ctrl) or mouse Klk10 plasmid with ultrasound treatment in the hind-limb as described in Figure 6. Plasma KLK10 level was determined using mouse KLK10 ELISA (BG-MUS11429). Paired two-tailed t-test was used. Shown are mean ± standard error of mean (SEM), n = 5.

Atherosclerotic plaque formation in the LCA was significantly reduced in the KLK10 overexpressing mice compared to the luciferase control (Figure 6b). Further assessment of the carotid artery sections by histochemical staining with hematoxylin and eosin (Figure 6d, e) showed decreased plaque area in the LCA of these mice. Circulating plasma KLK10 levels in the mice measured by ELISA at the time of sacrifice showed no measurable difference between the luciferase and KLK10 groups (Figure 6—figure supplement 1). This may be due to a waning plasmid expression at the sacrifice time. However, we found higher levels of KLK10 staining at the endothelial layer in the LCA and RCA (Figure 6f, g), as well as in the lung tissue samples as shown by western blot (Figure 6h, i). We observed no significant difference in plasma total cholesterol, triglycerides, HDLc, LDLc, and non-HDLc (Figure 6j–n) in the KLK10-injected mice compared to the control mice. These results demonstrate that treatment with KLK10 by either rKLK10 or KLK10 expression vector can inhibit atherosclerosis development in Apoe−/− mice.

### KLK10 expression is decreased in human coronary arteries with advanced atherosclerotic plaques

We next examined if KLK10 expression is altered in human coronary artery tissue sections with varying degrees of atherosclerotic plaques (n = 40 individuals, Table 1). KLK10 and CD31 immunostaining demonstrated that KLK10 expression was significantly reduced at the endothelial layer in arteries with significant plaques (grades 4–6; Figure 7a, b) than less-diseased arteries (grades 1–3).

**Table 1.**
 Patient characteristics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Age (mean ± SEM)</th>
      <th>Stroke</th>
      <th>Hypertension</th>
      <th>Diabetes</th>
      <th>Smoking</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total (n = 40)</td>
      <td>52.25 ± 13.35</td>
      <td>15</td>
      <td>26</td>
      <td>8</td>
      <td>17</td>
    </tr>
    <tr>
      <td>Sex</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Male (n = 27)</td>
      <td>53.21 ± 11.15</td>
      <td>10</td>
      <td>16</td>
      <td>5</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Female (n = 13)</td>
      <td>51.93 ± 16.22</td>
      <td>5</td>
      <td>10</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Race</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>White (n = 21)</td>
      <td>54.95 ± 13.14</td>
      <td>8</td>
      <td>12</td>
      <td>3</td>
      <td>9</td>
    </tr>
    <tr>
      <td>Black (n = 17)</td>
      <td>49.72 ± 14.17</td>
      <td>7</td>
      <td>14</td>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <td>Hispanic (n = 2)</td>
      <td>44 ± 5.66</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

_SEM, standard error of mean._

![Figure 7.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig7-v2.jpg)

**Figure 7.:** (a) Human coronary artery sections with varying degrees of atherosclerotic lesions were stained with anti-KLK10 antibody (red) and DAPI (blue). Scale bar low mag = 500 μm, scale bar; high mag = 50 μm. Arrows indicate endothelial cells. (b) Consecutive arterial sections from the same patients were stained with anti-CD31 antibody (red) and DAPI (blue). (c) Quantification of endothelial KLK10 fluorescence intensity in lower stage plaques (AHA grades 1–3) and advanced stage plaques (AHA grades 4–6). Data are from 40 different patients. Statistical analyses were performed using unpaired t-test. Mean ± standard error of mean (SEM) (Table 1).

## Discussion

Here, we describe that s-flow promotes, while d-flow inhibits, expression and secretion of KLK10 in ECs in vitro and in vivo. We found for the first time that KLK10 inhibits endothelial inflammation, endothelial barrier dysfunction, and reduces endothelial migration and tube formation, but not apoptosis or proliferation. Importantly, treatment of ECs in vitro with rKLK10 or a KLK10 expression plasmid inhibited endothelial inflammation induced by d-flow or TNFα. Moreover, treatment with rKLK10 or overexpression of KLK10 by ultrasound-mediated plasmid expression inhibited endothelial inflammation and atherosclerosis development in vivo. Our findings also indicate that KLK10 is likely to be important in human atherosclerotic plaque development. The protective effects of rKLK10 or plasmid-driven KLK10 expression on endothelial inflammation, barrier function, and atherosclerosis suggest its therapeutic potential for atherosclerosis treatment.

The Klk10 mRNA transcript was primarily found in ECs, while KLK10 protein was found not only in ECs but also in the adventitia and subendothelial layer (Figure 1). It is important to note that our single-cell RNAseq and ATACseq analyses of Klk10 expression in the mouse carotid artery clearly demonstrate that Klk10 mRNA is highly expressed only in ECs but not in other cell types including the SMCs, fibroblasts, or immune cells (Figure 1k, l). In addition, KLK10 is a secreted protein, which could be released to the circulation to be found in other locations including the adventitia and diffuse to the subendothelial layer. Therefore, we conclude that KLK10 protein signals observed in the subendothelial and adventitial layers are likely to be originated from ECs.

KLK10 expression is downregulated in breast, prostate, testicular, and lung cancer (Goyal et al., 1998; Liu et al., 1996; Hu et al., 2015; Luo et al., 2001; Zhang et al., 2010) but overexpressed in ovarian, pancreatic, and uterine cancer (Luo et al., 2003; Yousef et al., 2005; Dorn et al., 2013; Tailor et al., 2018). These suggest that abnormal, either too low or too high, levels of KLK10 are associated with various pathophysiological conditions. Overall, the effective concentration of rKLK10 we used in this study is within a reasonable range of human and mouse KLK10 levels in the plasma. Our mouse KLK10 ELISA study (Figure 6—figure supplement 1) showed that plasma KLK10 level in Apoe−/− mice is in the range of 5–10 ng/ml. In humans, normal plasma KLK10 levels are ~0.5 ng/ml, with a range from nearly undetectable to ~20 ng/ml in various cancers patients (Luo et al., 2003; Planque et al., 2008). We found that KLK10 levels in HAECs exposed to the anti-inflammatory LS was ~0.3 ng/ml, which decreased to ~0.13 ng/ml by the proinflammatory OS (Figure 1j). In functional studies, we found that 1–10 ng/ml of rKLK10 inhibits permeability and inflammation in HAECs, which falls within the reasonable physiological range. The effective rKLK10 dose used in mouse studies was 0.6 mg/kg, although how this effective dose translates to humans will need to be further studied. It is also worth noting that the effect of rKLK10 on monocyte adhesion (Figure 2b) is weaker than that of KLK10 overexpression using the plasmid vector (Figure 2a). We speculate that KLK10 produced from plasmid directly in HAECs is processed to be more effective than the rKLK10 produced and processed in CHO cells, which underwent multiple purification steps and storage conditions.

Interestingly, the anti-inflammatory effect of KLK10 seems to be unique in comparison to other KLKs expressed in ECs, including KLK8 and KLK11. Analysis of the sc-RNAseq dataset showed that Klk8 and Klk11 are two other KLK members expressed in ECs (Figure 8—figure supplement 1). We found that rKLK10, but not rKLK8 or rKLK11, inhibited endothelial inflammation in response to TNFα in HAECs (Figure 8—figure supplement 2).

Taken together, we demonstrated that KLK10 is a flow-sensitive protein that is upregulated by s-flow and downregulated by d-flow in ECs. Our results also demonstrate that KLK10 is a potent mediator of the anti-inflammatory, barrier-protective, and anti-atherogenic effects of s-flow in an autocrine manner in ECs (Figure 8). KLK10 may serve as potential anti-atherogenic therapeutic targets.

![Figure 8.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig8-v2.jpg)

**Figure 8.:** KL10 is upregulated by s-flow and downregulated by d-flow at the genomic and protein levels. Under s-flow conditions when KLK10 is expression is high, KLK10 inhibits NFκB and expression of vascular cell adhesion molecule 1 (VCAM1) and intracellular adhesion molecule 1 (ICAM1), thereby preventing monocyte adhesion. Additionally, KLK10 produced by s-flow protects the endothelial permeability barrier. Together, the anti-inflammatory and barrier-protective effects of KLK10 lead to an overall protection against atherosclerosis.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** Violin plots representing single-cell expression of (a) Klk8 and (b) Klk11 gene transcripts in eight endothelial cell clusters (E1–E8), smooth muscle cells (SMCs), fibroblasts (Fibro), 4 monocytes/macrophages clusters (Mo1–4), dendritic cells (DCs), and T cells (T) in the mouse carotid arteries following 2 days or 2 weeks of the PCL surgery as we recently reported (Andueza et al., 2020). The published scRNAseq data (Andueza et al., 2020) were reanalyzed here for Klk8 and Klk11 genes. E1–E4 clusters represent ECs exposed to s-flow conditions in the right carotid artery (RCA). E5 and E7 clusters represent ECs exposed to acute (2 days) d-flow in the left carotid artery (LCA). E6 and E8 clusters represent ECs exposed to chronic (2 weeks) d-flow in the LCA.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/72579/elife-72579-fig8-figsupp2-v2.jpg)

**Figure 8—figure supplement 2.:** HAECs were treated with rKLK8, 10, or 11 (10 ng/ml each) or vehicle (UTC) for 16 hr, followed by TNFα (5 ng/ml) or vehicle for 4 hr. Then, (a) THP-1 monocyte adhesion assay and (b) western blot analysis for VCAM1 expression were performed (Figure 8—figure supplement 2—source data 1). (c) is the quantification of (b) using beta-actin as an internal control using the NIH ImageJ. One-way analysis of variance (ANOVA) was used for statistical analysis. Shown are mean ± standard error of the mean (SEM), n = 4–6.

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
      <td>Gene (human)</td>
      <td>KLK10</td>
      <td></td>
      <td>Gene ID: 5655</td>
      <td>Kallikrein-related peptidase 10</td>
    </tr>
    <tr>
      <td>Gene (mouse)</td>
      <td>Klk10</td>
      <td></td>
      <td>Gene ID: 69,540</td>
      <td>Kallikrein-related peptidase 10</td>
    </tr>
    <tr>
      <td>Strain, strain background (mouse)</td>
      <td>C57BL/6J</td>
      <td>The Jackson Laboratory</td>
      <td>000664</td>
      <td>Male, 6–10 weeks of age</td>
    </tr>
    <tr>
      <td>Genetic reagent (mouse)</td>
      <td>Apoe−/− (B6.129P2-Apoetm1Unc/J)</td>
      <td>The Jackson Laboratory</td>
      <td>002052</td>
      <td>C57BL/6J Mice homozygous for the Apoetm1Unc mutation. Male, 6–10 weeks of age</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Recombinant human KLK10</td>
      <td>RayBiotech</td>
      <td>230-00040-10</td>
      <td>Human produced in E. coli</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Recombinant human KLK10-6xHis</td>
      <td>This paper</td>
      <td>Gene ID: 5655</td>
      <td>Ala34-Asn276 with C-terminal His tagHuman produced in CHO cells</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Human TNFα</td>
      <td>Thermo Fisher</td>
      <td>PHC3011</td>
      <td>Human produced in E. coli</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pcDNA3.4_hKLK10-6X His Plasmid</td>
      <td>This paper</td>
      <td>Gene ID: 5655</td>
      <td>Human KLK10 Met1- Asn276 with C-terminal His tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCMV-Igκ-Klk10-T2A-Luc Plasmid</td>
      <td>This paper</td>
      <td>Gene ID: 69,540</td>
      <td>Mouse Klk10 Met1-Lys278 with secretion tag and cleavable Luc reporter</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PCMV-Luciferase Plasmid</td>
      <td>Addgene</td>
      <td>#45,968</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PmaxGFPPlasmid</td>
      <td>Lonza</td>
      <td>#D-00059</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Human KLK10 siRNA</td>
      <td>Dharmacon</td>
      <td>J-005907-08</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Human Scrambled siRNA</td>
      <td>Dharmacon</td>
      <td>D-001810-10-05</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line</td>
      <td>Primary Human Aortic Endothelial Cells</td>
      <td>Cell Applications</td>
      <td>304-05a</td>
      <td>25–40-Year-old males. Multiple lots. Cell identity confirmed through diacetylated LDL and FACs. Company tested cells free of mycoplasma, bacteria, yeast, and fungi</td>
    </tr>
    <tr>
      <td>Cell line</td>
      <td>Primary Human Umbilical Vein Endothelial Cells</td>
      <td>Lonza</td>
      <td>CC-2519</td>
      <td>Pooled female donors. Multiple lots. Cell identity confirmed through diacetylated LDL and FACs. Company tested cells free of mycoplasma, bacteria, yeast, and fungi</td>
    </tr>
    <tr>
      <td>Cell line</td>
      <td>THP1 Human Monocytes</td>
      <td>ATCC</td>
      <td>Cat TIB-202</td>
      <td>STR Profiling and mycoplasma testing done by ATCC</td>
    </tr>
    <tr>
      <td>Biological sample (human)</td>
      <td>Human Coronary Arteries</td>
      <td>Lifelink Georgia</td>
      <td></td>
      <td>Deidentified human hearts not suitable for cardiac transplantation donated to LifeLink of Georgia</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>KLK10 (Rabbit Polyclonal)</td>
      <td>Bioss</td>
      <td>Bioss Cat# bs-2531R, RRID:AB_10882440</td>
      <td>IF (1:100), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CD31 (Rabbit Polyclonal)</td>
      <td>Abcam</td>
      <td>Abcam Cat# ab28364, RRID:AB_726362</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>VCAM1 (Rabbit Monoclonal)</td>
      <td>Abcam</td>
      <td>Abcam Cat# ab134047, RRID:AB_2721053</td>
      <td>IF (1:100)WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>VE-Cadherin (Mouse monoclonal)</td>
      <td>Santacruz</td>
      <td>Santa Cruz Biotechnology Cat# sc-9989, RRID:AB_2077957</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>NFKB P65 (Rabbit Monoclonal)</td>
      <td>Cell Signaling</td>
      <td>Cell Signaling Technology Cat# 8242, RRID:AB_10859369</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>phospho-NFκB p65 S356 (Rabbit Monoclonal)</td>
      <td>Cell Signaling</td>
      <td>Cell Signaling Technology Cat# 3033, RRID:AB_331284</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor Secondaries</td>
      <td>Thermo Fisher</td>
      <td></td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Ki67 (Rabbit Polyclonal)</td>
      <td>Abcam</td>
      <td>Abcam Cat# ab15580, RRID:AB_443209</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>H&amp;E Staining Kit</td>
      <td>American Mastertech</td>
      <td>KTHNEPT</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Human KLK10 ELISA</td>
      <td>MyBioSource</td>
      <td>Cat. #: MBS009286</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Mouse Klk10 ELISA</td>
      <td>NovateinBio</td>
      <td>BG-MUS11429</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TUNEL Staining Kit</td>
      <td>Roche</td>
      <td>12156792910</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>2′,7′-bis(carboxyethyl)-5 (6)-carboxyfluorescein-AM</td>
      <td>Thermo Fisher</td>
      <td>B1150</td>
      <td>1 mg/ml</td>
    </tr>
    <tr>
      <td>Primers</td>
      <td>Human KLK10</td>
      <td></td>
      <td></td>
      <td>For: GAGTGTGAGGTCTTCTACCCTGRev:ATGCCTTGGAGGGTCTCGTCAC</td>
    </tr>
    <tr>
      <td>Primers</td>
      <td>Mouse Klk10</td>
      <td></td>
      <td></td>
      <td>For:CGC TAC TGA TGG TGC AAC TCTRev:ATA GTC ACG CTC GCA CTG G</td>
    </tr>
    <tr>
      <td>Primers</td>
      <td>Human/Mouse 18s</td>
      <td></td>
      <td></td>
      <td>For:AGGAATTGACGGAAGGGCACCARev:GTGCAGCCCCGGACATCTAAG</td>
    </tr>
    <tr>
      <td>Primers</td>
      <td>Human VCAM1</td>
      <td></td>
      <td></td>
      <td>For:GATTCTGTGCCCACAGTAAGGCRev:TGGTCACAGAGCCACCTTCTTG</td>
    </tr>
    <tr>
      <td>Primers</td>
      <td>Human ICAM1</td>
      <td></td>
      <td></td>
      <td>For:AGCGGCTGACGTGTGCAGTAATRev:TCTGAGACCTCTGGCTTCGTCA</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Zen Blue</td>
      <td>Zeiss</td>
      <td></td>
      <td>Confocal Microscopy</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>NIH</td>
      <td></td>
      <td>Image Analysis</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DAPI Mounting media</td>
      <td>Vector Biolabs</td>
      <td>H-1200-10</td>
      <td>Methods – immunostaining of mouse artery sections an en face preparation of the aortic arch</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Oligofectamine</td>
      <td>Thermo Fisher</td>
      <td>12252011</td>
      <td>Methods – overexpression or knockdown experiments in vitro</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Lipofectamine</td>
      <td>Thermo Fisher</td>
      <td>L3000008</td>
      <td>Methods – overexpression or knockdown experiments in vitro</td>
    </tr>
  </tbody>
</table>

### PCL surgery

All animal studies were performed with male C57BL/6J or Apoe−/− mice (Jackson Laboratory), were approved by Institutional Animal Care and Use Committee by Emory University, and were performed in accordance with the established guidelines and regulations consistent with federal assurance. All studies using mice were carried out with male mice at 6–10 weeks to reduce the sex-dependent variables. For PCL studies, mice at 10 weeks were anesthetized and three of four caudal branches of LCA (left external carotid, internal carotid, and occipital artery) were ligated with 6–0 silk suture, but the superior thyroid artery was left intact. The development of d-flow with characteristic low and oscillating shear stress in each mouse was determined by ultrasound measurements as we described (Nam et al., 2009). Following the partial ligation, mice were either continued to be fed chow-diet for 2 days or high-fat diet for atherosclerosis studies for 3 weeks as specified in each study.

Endothelial-enriched RNA was prepared from the LCA and the contralateral RCA control following 48 hr after the partial ligation as we described previously (Nam et al., 2009).

### Immunostaining of mouse artery sections and en face preparation of the aortic arch

For mouse frozen section staining studies, fresh mouse aortas were fixed in 4% paraformaldehyde for 15 min and placed in Tissue-Tek OCT compound, snap-frozen in liquid nitrogen, and sectioned at 7 μm as we described (Son et al., 2013). Sections were then permeabilized using 0.1% Triton X-100 in Phosphate-buffered saline (PBS) for 15 min, blocked for 2 hr with 10% donkey serum, and incubated with anti-KLK10 (BiossUSA bs-2531R, 1:100) or anti-CD31 (R&D Systems AF3628, 1:100) primary antibodies overnight at 4°C followed by Alexa Fluor secondary antibodies (Thermo Fisher Scientific, 1:500) for 2 hr at room temperature. All images were taken with a Zeiss (Jena, Germany) LSM800 confocal microscope. Endothelial KLK10 fluorescent intensity was measured with NIH ImageJ using CD31 as a reference. Hematoxylin and eosin staining (American Mastertech) and plaque area quantification were performed using ImageJ software (NIH) as we described (Chang et al., 2007; Kim et al., 2013).

For en face immunostaining, mice were euthanized under CO2 and the aortas were pressure fixed with 10% formalin saline (Nam et al., 2009). The aortas were carefully cleaned in situ, and the aortic arches and thoracic aortas were dissected, opened longitudinally, and fixed in 4% paraformaldehyde for 1 hr, permeabilized using 0.1% Triton X-100 in PBS for 15 min, blocked for 2 hr with 10% donkey serum, and incubated with anti-KLK10 (BiossUSA bs-2531R, 1:100), anti-VCAM1 (Abcam ab134047, 1:100), or anti-VE-Cadherin (Santa Cruz sc-9989, 1:100) primary antibodies overnight at 4°C followed by Alexa Fluor-647 secondary antibodies (Thermo Fisher Scientific, 1:500) for 2 hr at room temperature. The LC and GC of each arch were separated and the aortas were then mounted on glass slides with VectaShield that contained DAPI (Vector Laboratories). En face images were collected as a Z-stack with a Zeiss LSM 800 confocal microscope. We used three Z-sections showing the endothelial layer using the internal elastic laminar as a reference from each tissue sample to quantify VCAM1 or KLK10 expression in the ECs (orthogonal image shown in Figure 2—figure supplement 5). The fluorescence intensity was quantified using the NIH ImageJ program.

### Cell culture and in vitro shear stress study

HAECs were obtained from Lonza and maintained in EGM2 medium (Lonza) supplemented with 10% fetal bovine serum (Hyclone), 1% bovine brain extract, 10 mM L-glutamine, 1 μg/ml hydrocortisone hemisuccinate, 50 μg/ml ascorbic acid, 5 ng/ml EGF, 5 ng/ml VEGF, 5 ng/ml FGF, and 15 ng/ml IGF-1 as we described (Son et al., 2013). HUVECs were purchased from BD Biosciences, cultured in M199 media (Cellgro) supplemented with 20% fetal bovine serum (Hyclone), 1% bovine brain extract, 10 mM L-glutamine, and 0.75 U/ml heparin sulfate as we described (Ni et al., 2011). All ECs were grown at 5% CO2 and 37°C and used between passages 5 and 9. EC identity was confirmed through diacetylated-LDL uptake and FACs-based cell sorting. THP-1 monocytes were obtained from ATCC and maintained in RPMI-1640 medium supplemented with 10% fetal bovine serum and 0.05 mM 2-mercaptoethanol at 5% CO2 and 37°C as we described (Ni et al., 2011). THP-1 STR Profiling and mycoplasma testing were done by ATCC. For flow experiments, confluent HAECs or HUVECs were exposed to steady unidirectional laminar shear stress (LS, 15 dynes/cm2) or bidirectional oscillatory shear stress (OS, ±5 dynes/cm2 at 1 Hz), mimicking s-flow and d-flow conditions, respectively, using the cone-and-plate viscometer for 24 hr experiments, as we reported (Jo et al., 2006; Chang et al., 2007).

### Preparation of whole-cell lysate and immunoblotting

After treatment, cells were washed 3× with ice-cold Hank's Balanced Salt Solution (HBSS) and lysed with Radioimmunoprecipitation Assay buffer (RIPA) buffer containing protease inhibitors (Boston Bioproducts BP-421) Son et al., 2013. The protein content of each sample was determined by Pierce BCA protein assay. Aliquots of cell lysate were resolved on 10% to 12% sodium dodecyl sulfate–polyacrylamide gels and subsequently transferred to a polyvinylidene difluoride membrane (Millipore). The membrane was incubated with the following primary antibodies: anti-KLK10 (BiossUSA bs-2531R, 1:1000), anti-GAPDH (Abcam ab23565, 1:2000), anti-β-actin (Sigma-Aldrich A5316, 1:2000), anti-VCAM1 (Abcam ab134047, 1:1000), anti-ICAM1 (Abcam ab53013, 1:1000), and anti-phospho-NFκB p65 S356 (Cell Signaling #3033, 1:1000) overnight at 4°C in 5% milk in TBST at the concentration recommended by the manufacturer, followed by secondary antibody addition for 1 hr at RT in 5% milk in TBST. Protein expression was detected by a chemiluminescence method (Son et al., 2013).

### Quantitative real-time polymerase chain reaction

Total RNAs were isolated using RNeasy Mini Kit (Qiagen 74106) and reverse transcribed to cDNA using High-Capacity cDNA Reverse Transcription Kit (Applied Biosystems 4368814). qPCR was performed for genes of interests using VeriQuest Fast SYBR QPCR Master Mix (Affymetrix 75690) with custom designed primers (Table 2) using 18S as house-keeping control as we previously described (Son et al., 2013).

**Table 2.**
 Quantitative real-time polymerase chain reaction (qPCR) primers.


<table>
  <thead>
    <tr>
      <th>Primer (custom)</th>
      <th>Sequence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>h_KLK10 For</td>
      <td>GAGTGTGAGGTCTTCTACCCTG</td>
    </tr>
    <tr>
      <td>h_KLK10 Rev</td>
      <td>ATGCCTTGGAGGGTCTCGTCAC</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>m_Klk10 For</td>
      <td>CGC TAC TGA TGG TGC AAC TCT</td>
    </tr>
    <tr>
      <td>m_Klk10 Rev</td>
      <td>ATA GTC ACG CTC GCA CTG G</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>H/M 18S For</td>
      <td>AGGAATTGACGGAAGGGCACCA</td>
    </tr>
    <tr>
      <td>H/M 18S Rev</td>
      <td>GTGCAGCCCCGGACATCTAAG</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>h_VCAM1 For</td>
      <td>GATTCTGTGCCCACAGTAAGGC</td>
    </tr>
    <tr>
      <td>h_VCAM1 Rev</td>
      <td>TGGTCACAGAGCCACCTTCTTG</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>h_ICAM1 For</td>
      <td>AGCGGCTGACGTGTGCAGTAAT</td>
    </tr>
    <tr>
      <td>h_ICAM1 Rev</td>
      <td>TCTGAGACCTCTGGCTTCGTCA</td>
    </tr>
  </tbody>
</table>

### KLK10 ELISAs

KLK10 secreted into the conditioned cell culture media from HAECs exposed to shear stress was measured by using a human KLK10 ELISA kit (MyBioSource, MBS009286). KLK10 in mouse plasma was measured by using a mouse KLK10 ELISA kit (NovateinBio, BG-MUS11429).

### rKLK10 and KLK10 plasmids

Initially, human rKLK10 (Ala34-Asn276 with a 6× N-terminal His tag) produced in E. coli (Ray Biotech, 230-00040-10) was used. Additional studies using human rKLK10 produced in the mammalian CHO-K1 cells validated the initial results. Most studies were carried out using human rKLK10 produced in CHO-K1 cells using a full-length expression vector (pcDNA3.4 hKLK10-6X His). rKLK10 with a 6× C-terminal His tag was affinity purified using HisPur Ni-NTA Resin (Thermo Scientific) per the manufacturer’s instruction (Figure 2—figure supplement 7) using the conditioned medium. Amino acid sequencing analysis of the purified rKLK10 by mass spectrometry showed that our rKLK10 preparation was a mature form expressing Ala34-Asn276 (data not shown).

### Overexpression or knockdown experiments in vitro

Cells were transiently transfected with a human KLK10-encoding plasmid (pcDNA3.4 hKLK10-6X His) at 0.1–2 μg/ml or as a control a GFP plasmid (PmaxGFP, Lonza, Cat. No. D-00059) using Lipofectamine 3000 (Invitrogen, Cat. No. L3000008) as we described (Son et al., 2013). Alternatively, cells were transfected with KLK10 siRNA (Dharmacon; J-005907-08) or Scrambled siRNA (Dharmacon; D-001810-10-05) using Oligofectamine (Invitrogen, Cat. No. 12252011) as we described (Son et al., 2013). Overexpression and knockdown of KLK10 were confirmed in HAECs (Figure 2—figure supplement 6).

### Endothelial functional assays

Endothelial migration was measured by the endothelial scratch assay, as we described (Tressel et al., 2007). Briefly, HUVECs were treated with rKLK10 at increasing doses overnight and cell monolayers were scratched with a 200 μl pipette tip. The monolayer was washed once, and the medium was replaced with 2% serum media. After 6 hr, the number of cells migrated into the scratch area was quantified microscopically using NIH ImageJ.

Endothelial apoptosis was determined using the TUNEL apoptosis assay, as we described (Alberts-Grill et al., 2012). Briefly, HUVECs were treated with rKLK10 at increasing doses overnight and the cells were fixed using 4% paraformaldehyde for 15 min and permeabilized with 0.1% Triton X-100 for 15 min. TUNEL staining was then performed using a commercially available kit (Roche, 12156792910) and the number of TUNEL-positive cells was counted using NIH ImageJ.

Endothelial proliferation was determined using Ki67 immunohistochemistry, as we described (Wang et al., 2019). Briefly, HUVECs were treated with rKLK10 at increasing doses overnight and the cells were washed twice with PBS, fixed using 4% paraformaldehyde for 15 min, and permeabilized with 0.1% Triton X-100 for 15 min. After blocking with 10% Goat Serum for 2 hr at RT, cells were incubated overnight at 4°C with rabbit anti-Ki67 primary antibody (Abcam ab15580, 1:100). The following day, cells were washed three times with PBS, incubated for 2 hr at RT protected from light with Alexa Fluor-647-labeled goat anti-rabbit IgG (1:500 dilution), and counterstained with VectaShield that contained DAPI (Vector Laboratories). The number of Ki67-positive cells was counted using NIH ImageJ.

Endothelial tube formation was measured using a Matrigel tube formation assay, as we described (Tressel et al., 2007). Briefly, HUVECs were seeded in a growth factor reduced Matrigel (BD Bioscience) coated 96-well plate and incubated with rKLK10 (100 ng/ml) for 6 hr at 37°C. Tubule formation was quantified microscopically by measuring tubule length using NIH ImageJ.

Endothelial permeability was determined by FITC-avidin binding to biotinylated gel, as previously described (Dubrovskyi et al., 2013). Briefly, HAECs were seeded on biotinylated gelatin and treated with rKLK10 overnight followed by thrombin (5 U/ml) for 4 hr or OS for 24 hr as described above. Following the completion of the experiments, FITC-avidin was added to the cells and fluorescent intensity was measured using NIH ImageJ.

Monocyte adhesion to ECs was determined using THP-1 monocytes (ATCC TIB-202) as we described (Son et al., 2013). In brief, THP-1 cells (1.5 × 105 cells/ml) were labeled with a fluorescent dye 2′,7′-bis(carboxyethyl)-5 (6)-carboxyfluorescein-AM (Thermo Fisher Scientific B1150; 1 mg/ml) in serum-free RPMI medium (Thermo Fisher Scientific 11875093) for 45 min at 37°C. After exposure to flow or other experimental treatments, the ECs were washed in RPMI medium before adding 2′,7′-bis(carboxyethyl)-5 (6)-carboxyfluorescein-AM-loaded THP-1 cells. After a 30-min incubation at 37°C under no-flow conditions, unbound monocytes were removed by washing the endothelial dishes 5× with HBSS and cells with bound monocytes were fixed with 4% paraformaldehyde for 10 min. Bound monocytes were quantified by counting the number of labeled cells at the endothelium under a fluorescent microscope.

NFκB p65 nuclear translocation was performed using HAECs treated with rKLK10 (10 ng/ml for 16 hr) followed by TNFα (5 ng/ml for 4 hr) or LS (20 dynes/cm2 for 1 hr). Cells were washed three times, fixed with 4% paraformaldehyde for 15 min, and then permeabilized using 0.1% Triton X-100 in PBS for 15 min. Cells were then blocked for 2 hr with 10% donkey serum, and incubated with anti-p65 antibody (Cell Signaling #8242) overnight at 4°C followed by Alexa Fluor secondary antibodies (Thermo Fisher Scientific, 1:500) for 2 hr at room temperature. All images were taken with a Zeiss (Jena, Germany) LSM800 confocal microscope and nuclear p65 fluorescence intensity was quantified in comparison to total p65 fluorescence intensity using NIH ImageJ.

### rKLK10 treatment and KLK10 overexpression in C57BL/6J and Apoe−/− mice

Two independent methods were used, rKLK10 and Klk10 plasmid, to treat mice with KLK10. Treatment with rKLK10 was first performed in C57BL/6J mice by administering rKLK10 (0.006–0.6 mg/kg) by tail vein once every 2 days and sacrificed on day 5. At the completion of the study, mice were euthanized by CO2 inhalation and en face preparation of the aorta was performed as we described (Son et al., 2013). Alternatively, Apoe−/− on a high-fat diet containing 1.25% cholesterol, 15% fat, and 0.5% cholic acid were given the PCL surgery and rKLK10 or vehicle was administered by tail vein once every 3 days for 3 weeks as we described (Son et al., 2013). Following the completion of the study, mice were euthanized by CO2 inhalation and the aortas were excised, imaged, and sectioned for IHC (Son et al., 2013).

Klk10 plasmid overexpression was performed using ultrasound-mediated sonoporation method of gene therapy as reported (Liu et al., 2019; Borden et al., 2005; Shapiro et al., 2016). Briefly, perfluoropropane microbubbles encapsulated by DSPC and DSPE-PEG2000 (9:1 molar ratio) were made using the shaking method as previously described (Liu et al., 2019; Borden et al., 2005; Shapiro et al., 2016). Klk10 plasmid expressing secreted KLK10 and luciferase (pCMV-Igκ-Klk10-T2A-Luc) from GENEWIZ or luciferase plasmid (pCMV-Luc) from Invitrogen (50 μg each) was then mixed with the microbubbles (5 × 105) and saline to reach 20 μl total volume. Following PCL, Apoe−/− mice were intramuscular injected to the hind-limbs with the plasmid-microbubble solution. The injected areas of the hind-legs were then exposed to ultrasound (0.35 W/cm2) for 1 min, and repeated 10 days later. At the completion of the study 3 weeks after the partial ligation and on high-fat diet, mice were anesthetized, administered with luciferin (IP; 3.75 mg) and imaged for bioluminescence on a Bruker In Vivo Xtreme X-ray Imaging System. Mice were then euthanized by CO2 inhalation and the aortas were excised, imaged, and sectioned for staining as described above.

### Immunohistochemical staining of sections from human coronaries

For human coronaries arteries, 2 mm cross-sections of the left anterior descending arteries were obtained from deidentified human hearts not suitable for cardiac transplantation donated to LifeLink of Georgia. The deidentified donor information is shown in Table 1. Tissues were fixed in 10% neutral buffered formalin overnight, embedded in paraffin, and 7 μm sections were taken, and stained as we described (Chang et al., 2007; Kim et al., 2013). Sections were deparaffinized and antigen retrieval was performed as described previously (Chang et al., 2007; Kim et al., 2013). Sections were then permeabilized using 0.1% Triton X100 in PBS for 15 min, blocked for 2 hr with 10% goat serum, and incubated with anti-KLK10 (BiossUSA bs-2531R, 1:100) or anti-CD31 (Abcam ab28364, 1:100) primary antibody overnight at 4°C followed by Alexa Fluor-647 (Thermo Fisher Scientific, 1:500) secondary antibody for 2 hr at room temperature. Nuclei were counterstained with VectaShield that contained DAPI (Vector Laboratories). All confocal images were taken with a Zeiss (Jena, Germany) LSM800 confocal microscope. Endothelial KLK10 fluorescent intensity was measured with NIH ImageJ using CD31 as a reference.

### Serum lipid analysis

Serum lipid analysis was performed at the Cardiovascular Specialty Laboratories (Atlanta, GA) using a Beckman CX7 biochemical analyzer for total cholesterol, triglycerides, HDL and LDL as we reported (Son et al., 2013).

### Statistical analyses

Statistical analyses were performed using GraphPad Prism software. All of the n numbers represent biological replicates. Error bars depict the standard error of means (SEMs). Initially, the datasets were analyzed for normality using the Shapiro–Wilk test (p < 0.05) and equal variance using the F-test (p > 0.05). Data that followed a normal distribution and possessed equal variance were analyzed using two-tailed Student t-test or one-way analysis of variance (ANOVA), where appropriate with Bonferroni post hoc test as needed. In the case where the data showed unequal variances, an unpaired t-test with Welch correction was performed or Brown–Forsythe and Welch ANOVA for multiple comparisons. In the case where the data failed the Shapiro–Wilk test (p > 0.05), a nonparametric Mann–Whitney U-test was conducted for pairwise comparisons or the Kruskal–Wallis for multiple groups was performed.
