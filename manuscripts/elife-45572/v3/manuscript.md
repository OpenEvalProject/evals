# Cysteine dioxygenase 1 is a metabolic liability for non-small cell lung cancer

## Authors

- Yun Pyo Kang<sup>1</sup>
- Laura Torrente<sup>1</sup>
- Aimee Falzone<sup>1</sup>
- Cody M Elkins<sup>1</sup>
- Min Liu<sup>2</sup>
- John M Asara<sup>3</sup>
- Christian C Dibble<sup>5</sup>
- Gina M DeNicola<sup>1</sup> ([ORCID: 0000-0001-6611-6696](https://orcid.org/0000-0001-6611-6696)) †

### Affiliations

1. Department of Cancer Physiology H Lee Moffitt Cancer Center and Research Institute Tampa United States
2. Proteomics and Metabolomics Core Facility H Lee Moffitt Cancer Center and Research Institute Tampa United States
3. Division of Signal Transduction Beth Israel Deaconess Medical Center Boston United States
4. Department of Medicine Harvard Medical School Boston United States
5. Department of Pathology and Cancer Center Beth Israel Deaconess Medical Center Boston United States
6. Department of Pathology Harvard Medical School Boston United States

† Corresponding author

## Abstract

NRF2 is emerging as a major regulator of cellular metabolism. However, most studies have been performed in cancer cells, where co-occurring mutations and tumor selective pressures complicate the influence of NRF2 on metabolism. Here we use genetically engineered, non-transformed primary murine cells to isolate the most immediate effects of NRF2 on cellular metabolism. We find that NRF2 promotes the accumulation of intracellular cysteine and engages the cysteine homeostatic control mechanism mediated by cysteine dioxygenase 1 (CDO1), which catalyzes the irreversible metabolism of cysteine to cysteine sulfinic acid (CSA). Notably, CDO1 is preferentially silenced by promoter methylation in human non-small cell lung cancers (NSCLC) harboring mutations in KEAP1, the negative regulator of NRF2. CDO1 silencing promotes proliferation of NSCLC by limiting the futile metabolism of cysteine to the wasteful and toxic byproducts CSA and sulfite (SO32-), and depletion of cellular NADPH. Thus, CDO1 is a metabolic liability for NSCLC cells with high intracellular cysteine, particularly NRF2/KEAP1 mutant cells.

## Introduction

NRF2 (Nuclear factor-erythroid 2 p45-related factor two or NFE2L2) is a stress-responsive cap’n’collar (CNC) basic region leucine zipper (bZIP) transcription factor that directs various transcriptional programs in response to oxidative stress. Under basal conditions, NRF2 is kept inactive through binding to its negative regulator KEAP1 (Kelch-like ECH-associated protein), which is a redox-regulated substrate adaptor for the Cullin (Cul)3-RING-box protein (Rbx)1 ubiquitin ligase complex that directs NRF2 for degradation (Kobayashi et al., 2004). KEAP1 is the major repressor of NRF2 in most cell types, which is supported by the evidence that disruption of Keap1 in the mouse increased the abundance and activity of Nrf2 (Wakabayashi et al., 2003). NRF2 plays a critical role in tumor initiation and progression in response to oncogenic signaling and stress (DeNicola et al., 2011; Todoric et al., 2017). Further, NRF2 and KEAP1 mutations are common in many cancers and lead to impaired NRF2 degradation and constitutive NRF2 accumulation (Ohta et al., 2008; Shibata et al., 2008), thereby promoting glutathione (GSH) synthesis, detoxification of reactive oxygen species (ROS) and proliferation.

While the role of NRF2 in ROS detoxification is well established, novel roles of NRF2 in the regulation of cellular metabolism have been recently identified. NRF2 promotes the activity of the pentose phosphate pathway to support the production of NADPH and nucleotides (Mitsuishi et al., 2012; Singh et al., 2013). Further, NRF2 promotes serine biosynthesis to support GSH and nucleotide production (DeNicola et al., 2015). These metabolic programs support cell proliferation and tumor growth but not all metabolic consequences of NRF2 activation are favorable. Although uptake of cystine (CYS)2 via the xCT antiporter (system xc-) promotes GSH synthesis and antioxidant defense (Sasaki et al., 2002), it also induces glutamate export and limits glutamate for cellular processes (Sayin et al., 2017). NRF2 suppresses fatty acid synthesis to conserve NADPH, which may antagonize proliferation (Wu et al., 2011). Importantly, the activity of these metabolic pathways may be influenced by co-occurring mutations found in the model systems used for study, such as LKB1 mutations, which commonly co-occur with KEAP1 mutations and influence NADPH levels (Jeon et al., 2012; Skoulidis et al., 2015). Further, NRF2 directs distinct transcriptional programs under basal and stress-inducible conditions (Malhotra et al., 2010), complicating the interpretation of its effects on cellular metabolism.

To examine the immediate consequence of constitutive NRF2 stabilization on cellular metabolism in non-transformed cells, we generated a genetically engineered mouse model expressing the KEAP1R554Q loss-of-function mutation found in human lung cancer. Using this model, we have examined the control of cellular metabolism by NRF2 in mouse embryonic fibroblasts (MEFs) and find that NRF2 promotes the accumulation of intracellular cysteine (CYS) and sulfur-containing metabolites, including GSH and the intermediates of the taurine (TAU) biosynthesis pathway cysteine sulfinic acid (CSA) and hypotaurine (HTAU). Entry of CYS into the TAU synthesis pathway was mediated by cysteine dioxygenase 1 (CDO1), which was elevated in KEAP1R554Q MEFs. TAU synthesis is initiated by the irreversible metabolism of CYS by CDO1 to CSA, which is then decarboxylated by cysteine sulfinic acid decarboxylase (CSAD) to HTAU. In turn, HTAU is non-enzymatically converted to TAU, or CSA is transaminated by the cytosolic aspartate aminotransferase (GOT1) to produce β-sulfinyl pyruvate, which spontaneously decomposes to pyruvate and sulfite (SO32-). At the organismal level, decarboxylation of CSA via CSAD predominates over transamination by GOT1 (Weinstein et al., 1988). By contrast, lung cancer cell lines accumulated significant CYS due to epigenetic silencing of the CDO1 locus. CDO1 re-expression antagonized proliferation and promoted the metabolism of CYS to CSA, but surprisingly most CSA was exported from cells or transaminated to produce toxic SO32-. Further, continual (CYS)2 reduction to replenish the CYS pool impaired NADPH-dependent cellular processes. These results demonstrate that CDO1 antagonizes the proliferation of lung cancer cells with high intracellular CYS and its expression is selected against during tumor evolution.

## Results

### NRF2 promotes the accumulation of sulfur-containing metabolites

To evaluate how constitutive NRF2 activity reprograms metabolism, we generated a genetically engineered, conditional knock-in mouse model of the cancer mutation KEAP1R554Q (Figure 1A). Mutations at this residue prevent the association of KEAP1 with NRF2, thereby stabilizing NRF2 and inducing the expression of NRF2 target genes (Hast et al., 2014). We inserted a loxP-flanked wild-type Keap1 cDNA upstream of the R554Q mutation in exon four in the endogenous Keap1 gene. Prior to exposure to Cre recombinase, wild-type Keap1 protein is expressed. Following Cre-mediated excision of the loxP-flanked cargo, mutant Keap1R554Q is expressed at physiological levels, thus recapitulating the genetic events of human NSCLC and allowing for the interrogation of the consequences of Keap1R554Q expression in an isogenic system. Mouse embryonic fibroblasts (MEFs) harboring this allele were derived to evaluate the consequence of Keap1R554Q expression in primary cells. The expression of homozygous Keap1R554Q led to Nrf2 accumulation and increased expression of the Nrf2 target Nqo1 (Figure 1B). We performed non-targeted metabolomics to identify metabolite alterations in these cells and found that the most abundant metabolites following Nrf2 accumulation are sulfur-containing metabolites derived from CYS (Figure 1C), while infection of wild-type MEFs with adenoviral Cre did not significantly alter metabolite levels (Figure 1—figure supplement 1A). To interrogate cysteine metabolism in more detail, we performed targeted metabolomics to quantify the concentration of intracellular CYS and its downstream metabolites (Figure 1—figure supplement 1B). As expected, Nrf2 promoted an increase in intracellular CYS and its downstream metabolite GSH (Figure 1D–F), consistent with previous observations that NRF2 promotes the uptake of (CYS)2 and the synthesis of GSH (Sasaki et al., 2002; Wild et al., 1999). Surprisingly, we also observed a significant increase in intermediates of the TAU biosynthesis pathway, including CSA and HTAU (Figure 1G–I). Importantly, HTAU is a highly abundant metabolite and the increase of HTAU was similar to the increase of GSH in the millimolar range (Figure 1F,H), suggesting that entry into the TAU biosynthesis pathway may represent a significant percentage of total CYS usage. Collectively, these results indicate that NRF2 promotes the accumulation of intracellular cysteine and entry of cysteine into multiple downstream pathways.

![Figure 1.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig1-v3.jpg)

**Figure 1.:** (a) Schematic of the murine Keap1R554Q allele. The Keap1R554Q allele was created by inserting a loxP-flanked wild-type Keap1 cDNA containing exons 3–5 upstream of a R554Q mutation in the endogenous exon 4 of the Keap1 gene. Prior to recombination, wild-type Keap1 protein is expressed due to splicing into the cDNA containing exons 3–5, and is referred to as Keap1WT. Following Cre-mediated excision of the loxP-flanked cargo, Keap1R554Q is expressed at physiological levels and is referred to as Keap1 R554Q. PA, poly A signal. (b) Western blot analysis of Nrf2, Nqo1, and β-Actin levels following Nrf2 stabilization in wild-type (WT) vs. homozygous Keap1R554Q/R554Q (R554Q) MEFs. (c) LC-HRMS metabolomics profiling of Keap1R554Q/R554Q MEFs compared to Keap1WT/WT MEFs. GSH, glutathione. CSA, cysteine sulfinic acid. HTAU, hypotaurine. CTH, cystathionine. NAC, N-acetyl cysteine. SAH, S-adenosyl homocysteine. aKG, α-ketoglutarate. PYR, pyruvate. N = 3, representative of 2 individual MEF lines. (d–i) Quantitation of cystine ([CYS]2, d), cysteine (CYS, e), glutathione (GSH, f), cysteine sulfinic acid (CSA, g), hypotaurine (HTAU, h) and taurine (TAU, i) levels in Keap1R554Q/R554Q MEFs compared to Keap1WT/WT MEFs. Cysteine and glutathione were derivatized with N-ethylmaleamide (NEM) to prevent oxidation during extraction here and for all quantification experiments. TXN, thioredoxin. TXN-ox, oxidized thioredoxin. GSH-ox, oxidized glutathione. GLU, glutamate. GLY, glycine. N = 3.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** (a) LC-HRMS metabolomics profiling of wild-type MEFs infected with adenoviral-cre compared to MEFs infected with empty adenovirus. N = 3 replicates/group. (b) Verification of stable-isotope labeled CSA and cystine internal standards for absolute quantification. Stable isotope labeled CSA and cystine standards were synthesized from [13C3, 15N]-cysteine and analyzed by LC-MS/MS based MRM against authentic standards. RT, retention time.

### Nrf2 promotes the entry of cysteine into the taurine synthesis pathway via Cdo1 in non-transformed, primary MEFs

The significant accumulation of intracellular CYS and TAU synthesis intermediates led us to hypothesize that Nrf2 promotes the accumulation of Cdo1 protein, which is stabilized following CYS accumulation due to a loss its ubiquitination and degradation (Dominy et al., 2006). We observed a robust increase in Cdo1 protein in Keap1R554Q MEFs compared to Keap1WT MEFs in the absence of an increase in mRNA expression (Figure 2A,B), consistent with the known mechanism of Cdo1 regulation. To examine whether Cdo1 mediates CYS metabolism to CSA and HTAU, and whether this limits the use of CYS for GSH synthesis, we deleted Cdo1 with CRISPR/Cas9, followed by infection with empty or Cre expressing adenovirus to generate Cdo1-deficient, isogenic Keap1WT and Keap1R554Q MEFs. Western analysis of Cdo1 protein revealed a significant reduction of Cdo1 expression in Keap1R554Q MEFs, although the already low Cdo1 levels did not change significantly in Keap1WT MEFs (Figure 2C). We performed quantitative 13C6-cystine [(CYS)2] tracing to examine the entry of CYS into GSH and TAU synthesis and found that depletion of Cdo1 inhibited HTAU synthesis from CYS (Figure 2H,I). However, HTAU labeling was not completely abolished, which may be explained by incomplete Cdo1 deletion or Cdo1-independent HTAU synthesis from CYS via CoA breakdown, which cannot be distinguished by this method. By contrast, the total CYS and GSH levels as well as GSH labeling from 13C6 labeled (CYS)2 were modestly increased by Cdo1 depletion, without any change in CYS2 levels (Figure 2D–G). These results demonstrate that Cdo1 accumulation in Keap1R554Q MEFs promotes CYS entry in into the TAU synthesis pathway, and modestly limits CYS accumulation and GSH synthesis.

![Figure 2.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig2-v3.jpg)

**Figure 2.:** (a) Western blot analysis of Cdo1 and β-Actin levels following Nrf2 stabilization in wild-type (WT) vs. homozygous Keap1R554Q/R554Q (R554Q) MEFs. (b) Real-time PCR analysis of Cdo1 and Nqo1 mRNA levels following Nrf2 stabilization in wild-type (WT) vs. homozygous Keap1R554Q/R554Q (R554Q) MEFs. mRNA expression was normalized to β-Actin expression, followed by normalization to WT. N = 3. (c) Western blot analysis of Nrf2, Cdo1, Nqo1 and β-Actin levels following expression of sgControl (sgCON) or Cdo1 deletion (sgCdo1 #2 and #3) with CRISPR/Cas9 in primary wild-type (WT) and homozygous Keap1R554Q/R554Q (R554Q) MEFs. (d–i) Quantitation of cysteine (CYS, (d), glutathione (GSH, (e,f), cystine ([CYS]2,(g), and hypotaurine (HTAU, (h,i) total levels and 13C-labeling from 13C-cystine in cells from (c). 13C-label is shown in red, while 12C-label is gray. Cells were labeled for 4 hr. N = 3.

### CDO1 is preferentially silenced in KEAP1 mutant NSCLC and antagonizes proliferation

The limitation of CYS availability by CDO1 suggests that this enzyme may antagonize NRF2-dependent processes in cancer. Thus, we hypothesized that the CDO1-mediated CYS homeostatic control mechanism might be deregulated in NSCLC, allowing enhanced CYS entry into GSH synthesis and other pathways. To evaluate this possibility, we examined the expression of CDO1 in NSCLC patient samples from The Cancer Genome Atlas (TCGA). CDO1 mRNA expression was significantly lower in lung adenocarcinoma samples compared to normal lung (Figure 3A), which was associated with CDO1 promoter methylation (Figure 3B) and poor prognosis (Figure 3—figure supplement 1A). Methylation was strongly correlated with mRNA expression across patient samples (Figure 3—figure supplement 1B). Interestingly, the incidence of CDO1 promoter methylation was significantly higher and its mRNA expression significantly lower in KEAP1 mutant lung adenocarcinoma compared to wild-type (Figure 3A,B), and NRF2 activity high lung adenocarcinoma compared to NRF2 low (Figure 3—figure supplement 1C), suggesting that CDO1 expression confers a selective disadvantage in the context of NRF2 accumulation. CDO1 protein expression was undetectable in a panel of NSCLC cell lines with the exception of H1581 cells (Figure 3C), and treatment with the DNMT inhibitor decitabine restored CDO1 mRNA expression (Figure 3—figure supplement 1D). These results indicate that CDO1 epigenetically silenced by promoter methylation in NSCLC cell lines and patient samples.

To investigate the NRF2-dependent regulation of CDO1 protein in NSCLC, we generated a doxycycline-inducible lentiviral expression system to reintroduce GFP, CDO1WT or a catalytically inactive CDO1 mutant (Y157F, Ye et al., 2007) at single copy into the panel of NRF2LOW and NRF2HIGH NSCLC cell lines (Figure 3D, Figure 3—figure supplement 2). The level of CDO1 protein expression in these cells was similar with the physiological Cdo1 levels in mouse lung and liver (Figure 3—figure supplement 2B), with liver being one of the highest CDO1-expressing tissues that is responsible for supplying TAU to the body (Stipanuk et al., 2015). We find that CDO1 accumulated to higher levels in NRF2HIGH cells than NRF2LOW, although accumulation was observed in many NRF2LOW cell lines as well (Figure 3D). We investigated the association with intracellular CYS levels across the panel of parental cell lines and found a strong association between the level of CDO1 accumulation and intracellular CYS levels but not with the level of CDO1 mRNA expressed from our inducible promoter system (Figure 3D, Figure 3—figure supplement 2A), which is consistent with our findings in Keap1R554Q MEFs (Figure 2A,B). Consistent with MEFs, we also find that deletion of endogenous CDO1 in H1581 cells, the only NSCLC line with detectable CDO1 expression, promoted CYS accumulation, demonstrating that CDO1 functions to limit intracellular CYS in lung cells as well (Figure 3E).

![Figure 3.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig3-v3.jpg)

**Figure 3.:** (a) CDO1 mRNA expression of normal lung (Normal) or or KEAP1 wild-type (WT) and mutant (MUT) lung adenocarcinoma patient tumor samples. Normal, N = 45. MUT, N = 39, WT, N = 189. (b) Methylation of the CDO1 promoter in samples from normal lung (Normal) or KEAP1 wild-type (WT) and mutant (MUT) lung adenocarcinoma patient tumor samples. Normal, N = 28. MUT, N = 29, WT, N = 154. (c) Western blot analysis of NRF2, CDO1, xCT and α-Tubulin levels in KEAP1 wild-type and KEAP1 mutant NSCLC cell lines. Arrowhead denotes specific band. (d) (Top) Western blot analysis of NRF2, CDO1 and α-Tubulin expression in NRF2LOW and NRF2HIGH (KEAP1 mutant: H1792, HCC15, A549, H322, and H460) NSCLC cell lines expressing CDO1Y157F. (Bottom) Intracellular cysteine concentration of the parental cell lines (minus doxycycline). (Right) Correlation between CDO1 protein levels and intracellular cysteine concentrations. CDO1 protein was normalized to α-Tubulin. N = 13. (e) (Top) Western blot analysis of CDO1 and β-ACTIN expression in H1581 cells following expression of control (sgCON) or CDO1-targeting sgRNAs (sgCDO1 #1 and #2) and Cas9. (Bottom) Intracellular cysteine concentration of the same cells. N = 4 replicates/group. (f–h) Western blot analysis of NRF2, CDO1, xCT, TXN1, α-Tubulin and β-ACTIN levels following re-expression of CDO1WT (WT), CDO1Y157F (Y157F), or GFP in (f) NRF2 knockout A549 cells reconstituted with either pLX317 empty (-) or pLX317-NRF2 (+), (g) H1975 and H1299 cells expressing either pLX317 empty (-) or pLX317-NRF2T80K (+), or (h) H1944 cells reconstituted with inactive pLenti-KEAP1 (C273S), super repressor KEAP1 (C151S) or wild-type KEAP1 (WT). (i) Analysis of cysteine levels in the cells from (e–g). N = 3 replicates/group. (j) Analysis of the proliferation of cells from (f). Cells were collected on the indicated days, stained with crystal violet and their absorbance at 600 nm determined. N = 3 replicates/group. (k) Analysis of proliferation of NSCLC cells expressing CDO1WT and correlation with CDO1 protein expression. Cells were collected after 3 days, and CDO1 dependent growth inhibition was determined by taking the ratio of CDO1WT / CDO1Y157F cell quantity. For individual lines (N = 13), see Figure 3—figure supplement 3D. For (d-j), cells were treated with 0.25 μg/ml doxycycline for 2 days prior to and during the assay and fresh medium was added 4 hr prior to sample collection.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** (a) Association of CDO1 mRNA expression with NSCLC patient outcome. (b) Correlation between CDO1 promoter methylation and mRNA expression in lung adenocarcinoma patient samples from the TCGA. N = 185. (c) Methylation of the CDO1 promoter in samples from normal lung (Normal) or lung adenocarcinoma patient tumor samples based on NRF2 activity. Normal, N = 28. NRF2 high group = KEAP1 mutant patients + KEAP1 wild-type patients with NRF2 activity score >lowest KEAP1 mutant tumor (N = 51). NRF2 low group = KEAP1 wild-type patients with NRF2 activity score <lowest KEAP1 mutant tumor (N = 134). (d) Real-time PCR analysis of CDO1 mRNA expression following 5 uM decitabine treatment for 3 days with daily medium change. CDO1 expression was normalized to β-ACTIN expression, and relative expression compared to H1581 DMSO is shown. H1581 demonstrates high basal expression, in agreement with the western blot from Figure 3C. N = 3 replicates/group. Cells were treated with 0.25 µg/ml doxycycline for 2 days prior to and during the assay and fresh medium was added 4 hr prior to sample collection.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** (a) Correlation between CDO1 protein levels (from Figure 3d) and CDO1 mRNA expression in the same cell lines. N = 13. (b) Western blot analysis of NRF2, xCT, CDO1 and HSP90 expression in NSCLC cell lines expressing CDO1WT with mouse liver and lung lysates. Liver expresses high physiological levels of CDO1, while lung expresses low. Cells were treated with 0.25 µg/ml doxycycline for 2 days prior to and during the assay and fresh medium was added 4 hr prior to sample collection.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig3-figsupp3-v3.jpg)

**Figure 3—figure supplement 3.:** (a) Western blot analysis of NRF2, xCT, CDO1 and β-Actin protein expression in H460 control cells, or CDO1WT-expressing H1299 and H1975 cells following treatment with 2 µM β-lapachone (βLap). Cells were treated with βLap for 8 hr (8 hr) or 4 hr followed by a 24 hr recovery period (24 hr). (b) Analysis of intracellular cysteine levels in the 24 hr group from (d). N = 3 replicates/group. (c) Western blot analysis of CDO1 and β-ACTIN levels in NRF2 knockout A549 cells reconstituted with either pLX317 empty (NRF2 -) or pLX317-NRF2 (NRF2 +), followed by re-expression of CDO1WT (WT), CDO1Y157F (Y157F), or GFP. Cells were grown in medium containing 200 μM or 10 μM CYS for 24 hr prior to lysate collection. (d) Individual proliferation data for Figure 3k. Cells were collected on the indicated days, stained with crystal violet and their absorbance at 600 nm determined. Proliferation of each line expressing CDO1WT was normalized to the proliferation of cells expressing CDO1Y157F. N = 3 replicates/group. (e) Correlation of CDO1 mRNA expression with cell growth inhibition (%). N = 13. For (a,b,e), cells were treated with 0.25 µg/ml doxycycline for 2 days prior to and during the assay and fresh medium was added 4 hr prior to sample collection.

To directly examine the effect of NRF2 on CDO1 expression in NSCLC cell lines, we used multiple isogenic cell systems. First, we used NRF2-deficient A549 cells (Torrente et al., 2017), in which we restored NRF2 expression in combination with CDO1WT, CDO1Y157F, or GFP. NRF2 restoration in these cells led to higher expression of endogenous xCT and accumulation of ectopically expressed CDO1 compared to GFP control (Figure 3F). Next, we selected the two KEAP1WT NSCLC cell lines that had the lowest ectopic CDO1 accumulation and low intracellular CYS in our cell line panel, H1299 and H1975. Using a NRF2T80K mutant that is unable to bind KEAP1 (Berger et al., 2017), the effects of NRF2 on CDO1 accumulation were recapitulated in these KEAP1WT NSCLC cell lines (Figure 3G). Interestingly, we observed that NRF2T80K could also promote the accumulation of endogenous CDO1 in H1299 cells. Further, NRF2 stabilization with the ROS inducing agent β-lapachone promoted NRF2, CYS and CDO1 accumulation in H1299 and H1975 cells (Figure 3—figure supplement 3A,B), which was most pronounced the day following the 4 hr treatment window. Consistently, NRF2 depletion in KEAP1MUT NSCLC cells following KEAP1WT expression led to CDO1 depletion (Figure 3H), although the effects were more modest than what was observed with NRF2 activation. Notably, NRF2 expression promoted intracellular CYS accumulation, while NRF2 depletion impaired CYS accumulation (Figure 3I), supporting a role for intracellular CYS in CDO1 stabilization. To directly assess the requirement for CYS, A549 cells were cultured in high or low (CYS)2 and CDO1 levels were found to be dependent on CYS availability (Figure 3—figure supplement 3C).

Next, we examined the consequence of CDO1 expression on cellular proliferation. Using the isogenic NRF2 KO A549 cell system, we observed that CDO1 expression significantly impaired the proliferation of NRF2-expressing cells, while no effect was observed on NRF2 KO cells (Figure 3J). Looking more broadly, we observed that CDO1 expression generally antagonized the proliferation of NSCLC cell lines and proliferation inhibition was strongly correlated with CDO1 protein expression, but not RNA expression (Figure 3K and Figure 3—figure supplement 3D,E). Overall, these results demonstrate that NRF2 and other mechanisms of intracellular CYS accumulation promote CDO1 accumulation, which leads to a selective growth disadvantage in lung cancer cells.

### CDO1 depletes CYS, leading to its export as CSA

To evaluate the mechanism by which CDO1 expression impaired proliferation we interrogated CYS metabolism following CDO1 expression. CYS has multiple intracellular fates, including the synthesis of GSH. CDO1 metabolizes CYS to CSA, which is then decarboxylated to HTAU (Figure 4A). CDO1WT and CDO1Y157F-expressing A549 cells were fed fresh (CYS)2-containing medium and sulfur containing metabolites were quantified over time (Figure 4B–D). CDO1WT, but not the enzyme-inactive CDO1Y157F, limited intracellular CYS levels and promoted the accumulation of CSA, which peaked at 4 hr (Figure 4B). We observed a steady increase in both CDO1Y157F and CDO1WT protein over the 24 hr time period, although CDO1WT protein levels were lower, consistent with the intracellular CYS levels (Figure 4—figure supplement 1A). Interestingly, unlike what was observed in MEFs, the levels of GSH, HTAU, and TAU were not changed over the time course of this assay (Figure 4C). We also interrogated metabolite changes in the medium and observed that (CYS)2 was rapidly depleted from the medium by 24 hr, while CSA steadily accumulated (Figure 4D). Based on this time course, 4 hr was selected for all subsequent experiments to prevent (CYS)2 starvation by CDO1. Importantly, deletion of endogenous CDO1 in H1581 cells reduced CSA production and (CYS)2 consumption (Figure 4E,F). To examine the NRF2-dependence of these metabolite alterations, we utilized the NRF2KO cells, KEAP1WT cells, or KEAP1MUT cells from Figure 3. NRF2 promoted CSA accumulation and (CYS)2 consumption following CDO1WT expression in NRF2 KO cells (Figure 4G,H). This effect was recapitulated by NRF2T80K expression in KEAP1WT cells (Figure 4I,J). Consistently, NRF2 depletion by KEAP1WT expression in KEAP1MUT cells inhibited the CDO1-dependent production of CSA (Figure 4K–M). Interestingly, KEAP1WT expression did not robustly affect CDO1 protein levels in H322 cells but significantly impaired CSA production by CDO1. Intracellular CYS can also influence CDO1 activity promoting its catalytic efficiency (Dominy et al., 2008), which may explain these results. Collectively, these results demonstrate that CDO1 expression promotes the production of CSA from CYS, leading to CSA accumulation both intracellularly and extracellularly, and enhanced (CYS)2 consumption.

![Figure 4.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig4-v3.jpg)

**Figure 4.:** (a) Schematic depicting intracellular cysteine metabolism. Following uptake of cystine via xCT, it is reduced to cysteine via the cellular antioxidant systems. Cysteine then enters glutathione synthesis mediated by GCL and GSS, or undergoes irreversible metabolism by CDO1 to CSA, and subsequently to HTAU by CSAD. (b) Time-dependent quantification (0, 1, 2, 4, 8, 24 hr) of intracellular cysteine (CYS) and cysteine sulfinic acid (CSA) concentrations following medium replenishment of CDO1WT-expressing (red) and CDO1Y157F-expressing (gray) A549 cells. *= CDO1WT vs. CDO1Y157F CYS, #= CDO1WT vs. CDO1Y157F CSA. N = 3 replicates/group, except 8 hr CYS for which N = 6 replicates/group. (c) Time-dependent quantification of GSH, HTAU, and TAU in the extracts from (b). N = 3 replicates/group. (d) Time-dependent quantification of the levels of (CYS)2 and CSA in the medium from the cells from (b). N = 3 replicates/group. (e) Intracellular CSA concentration of H1581 cells following expression of control (sgCON) or CDO1-targeting sgRNAs (sgCDO1 #1 and #2) and Cas9. N = 4 replicates/group. (f) Quantification of (CYS)2 consumption from the medium of the cells from (e). N = 4 replicates/group. (g) CSA production rate of NRF2 KO A549 cells reconstituted with either pLX317 empty (NRF2 -) or pLX317-NRF2 (NRF2 +), followed by expression of CDO1Y157F (Y157F) or CDO1WT (WT). N = 6 replicates/group. (h) Quantification of (CYS)2 consumption from the medium of the cells from (g). (i) Intracellular CSA concentration in H1975 and H1299 cells expressing either pLX317 empty (-) or pLX317-NRF2T80K (NRF2T80K), followed by expression of CDO1Y157F (Y157F) or CDO1WT (WT). N = 3 replicates/group. (j) Quantification of (CYS)2 consumption from the medium of the cells from (i). (k–m) CSA production rate of A549 (k), H1944 (l) and H322 (m) cells following expression of CDO1Y157F (Y157F) or CDO1WT (WT), and reconstituted with inactive KEAP1 (C273S), super repressor KEAP1 (C151S) or wild-type KEAP1 (WT). N = 3 replicates/group. For (g–m) cells were treated with 0.25 μg/ml doxycycline for 2 days prior to and during the assay and fresh medium was added 4 hr prior to sample collection.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** (a) Time-dependent western blot analysis of CDO1 and β-Actin protein expression at 0, 1, 2, 4, 8, or 24 hr following media replenishment of CDO1WT-expressing and CDO1Y157F-expressing A549 cells. (b) Quantification of CDO1-dependent (CYS)2 consumption and CSA production as cysteine molar equivalents. Because (CYS)2 contains 2 molecules of cysteine, it counts as two molar equivalents. CDO1-dependent changes were determined by subtracting the rates of change in CDO1Y157F cells from CDO1WT cells. CSA accounts for 2–25% of CDO1-dependent (CYS)2 consumption. N = 3 replicates/group, except NRF2 KO A549 (N = 6 replicates). Cells were treated with 0.25 µg/ml doxycycline for 2 days prior to and during the assay and fresh medium was added 4 hr prior to sample collection (b) or prior the indicated time points (a).

### CDO1 restoration in NSCLC cells promotes sulfite production, thereby depleting cystine via sulfitolysis

We found that CSA only accounted for a fraction of CDO1-dependent (CYS)2 depletion (Figure 4—figure supplement 1B), suggesting that CSA is metabolized to an alternative product in NSCLC cell lines. To further characterize the consequence of CDO1 expression on CYS metabolism, we performed untargeted metabolomics and found significant accumulation of SO32- in CDO1-expressing cells (Figure 5A). Importantly, CSA can be transaminated by the cytosolic aspartate aminotransferase (GOT1) to produce β-sulfinyl pyruvate, which spontaneously decomposes to pyruvate and SO32- (Singer and Kearney, 1956) (Figure 5B). While HTAU and TAU are non-toxic molecules that have important physiological functions (Aruoma et al., 1988; Hansen et al., 2010; Schaffer et al., 2000; Suzuki et al., 2002), SO32- is toxic at high levels due to its cleavage of disulfide bonds in proteins and small molecules, including (CYS)2 (Clarke, 1932). Thus, we hypothesized that in addition to accounting for the fate of CSA metabolism, SO32- production may also contribute to (CYS)2 depletion through disulfide cleavage, also known as sulfitolysis.

![Figure 5.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig5-v3.jpg)

**Figure 5.:** (a) Relative abundance of cysteine-related metabolites in cell extracts following CDO1WT or CDO1Y157F expression in A549 cells. Fresh medium was added 4 hr prior to extraction. Metabolites were analyzed by untargeted LC-MS. N.B. - cysteine and GSH were not derivatized with NEM for this analysis. N = 3 replicates/group. (b) GOT1 mediates the transamination of CSA to produce β-sulfinyl pyruvate, which decomposes to pyruvate and sulfite (SO32-). Sulfite hydrolyzes (CYS)2 to produce cysteine-S-sulfate (CYS-SO3-) in a process known as sulfitolysis. (c,d) Time-dependent quantification of the medium concentrations of and SO32- (c) and CYS-SO3- (d) concentrations from Figure 4d. (e) Time-dependent quantification of (CYS)2 and CYS-SO3- following the addition of 1 mM Na2SO3 to RPMI +10% FBS in the absence of cells. N = 3 replicates/group. (f) CYS-SO3- production rate of H1581 cells following expression of control (sgCON) or CDO1-targeting sgRNAs (sgCDO1 #1 and #2) and Cas9. N = 4 replicates/group. (g) CYS-SO3- production rate of NRF2 KO A549 cells reconstituted with either pLX317 empty (NRF2 -) or pLX317-NRF2 (NRF2 +), followed by expression of CDO1Y157F (Y157F) or CDO1WT (WT). N = 6 replicates/group. (h) CYS-SO3- production rate of H1975 and H1299 cells expressing either pLX317 empty (-) or pLX317-NRF2T80K (NRF2T80K), followed by expression of CDO1Y157F (Y157F) or CDO1WT (WT). N = 3 replicates/group. (i) CYS-SO3- production rate of A549 cells following expression of CDO1Y157F (Y157F) or CDO1WT (WT), and reconstituted with inactive KEAP1 (C273S), super repressor KEAP1 (C151S) or wild-type KEAP1 (WT). N = 3 replicates/group. (j) Intracellular SO32- concentration in the cells from (i). (k) CYS-SO3- production rate of H1944 cells following expression of CDO1Y157F (Y157F) or CDO1WT (WT), and reconstituted with inactive KEAP1 (C273S), super repressor KEAP1 (C151S) or wild-type KEAP1 (WT). N = 3 replicates/group. For a, c, d, g-k, cells were treated with 0.25 μg/ml doxycycline for 2 days prior to and during the assay.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** (a) Verification of the stable-isotope labeled CYS-SO3- internal standard for absolute quantification. Stable isotope labeled CYS-SO3- was synthesized from [13C3, 15N]-cysteine and analyzed by LC-MS/MS based SRM against an authentic standard. RT, retention time. (b) Time-dependent quantification of (CYS)2 and CYS-SO3- following the addition of 1 mM CSA to RPMI +10% FBS in the absence of cells. (c) Relative quantification of (CYS)2 and CYS-SO3- following the addition of 1 mM SO32- to cystine-free RPMI +200 µM (Cys)2 + 10% dFBS in the absence of cells. (d) Relative quantification of GSSG and GS-SO3- following the addition of 1 mM SO32- to cystine-free RPMI +200 µM GSSG +10% dFBS in the absence of cells. (e–f) Quantitation of the levels of (Cys)2 and GSSG in blank (blank) or the conditioned medium (e) or cellular extracts (f) from H460 cells expressing CDO1WT (WT) or CDO1Y157F (Y157F). Cells were treated with 0.25 µg/ml doxycycline for 2 days prior to and during the assay, and fresh medium was added 6 hr (e) or 4 hr (f) prior to sample collection.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** (a) Western blot analysis of NRF2, CDO1, GOT1, CSAD and β-ACTIN levels following expression of GFP, CDO1WT, or CDO1Y157F in Keap1WT/WT (WT) and Keap1R554Q/R554Q (R554Q) MEFs. A549s expressing CDO1WT are included for comparison. (b–g) Quantitation of cystine (CYS2, (b), cysteine (CYS, (c), glutathione (GSH, (d), cysteine sulfinic acid (CSA, (e), hypotaurine (HTAU, (f) and taurine (TAU, (g) levels in Keap1R554Q/R554Q MEFs (red) compared to Keap1WT/WT MEFs (black) following expression of CDO1Y157F (Y157F) or CDO1WT (WT). N = 3 replicates/group. Cells were treated with 0.25 µg/ml doxycycline for 2 days prior to and during the assay, and fresh medium was added 4 hr prior to sample collection.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig5-figsupp3-v3.jpg)

**Figure 5—figure supplement 3.:** (a) Western blot analysis of GOT1, CSAD and HSP90 levels in NRF2LOW and NRF2HIGH NSCLC cell lines. Mouse liver is included as a positive control for GOT1 and CSAD expression. Cells were fed with fresh RPMI +10% FBS 4 hr prior to lysate collection. (b) Intracellular SO32- concentration of NRF2 KO A549 cells reconstituted with either pLX317 empty (NRF2 -) or pLX317-NRF2 (NRF2 +), followed by re-expression of CDO1Y157F (Y157F) or CDO1WT (WT). N = 3 replicates/group. (c) SO32- production rate of cells from (b). (d–f) Intracellular CSA concentration of A549 (d), H1944 (e) and H322 (f) cells following re-expression of CDO1Y157F (Y157F) or CDO1WT (WT), and reconstituted with inactive KEAP1 (C273S), super repressor KEAP1 (C151S) or wild-type KEAP1 (WT). N = 3 replicates/group. (g) CYS-SO3- production rate of H322 cells following expression of CDO1Y157F (Y157F) or CDO1WT (WT), and reconstituted with inactive KEAP1 (C273S), super repressor KEAP1 (C151S) or wild-type KEAP1 (WT). N = 3 replicates/group. (h–j) Analysis of CDO1-dependent CSA production (h), Cys-SO3- production (i) and cystine consumption (j) in the 24 hr group from Figure 3—figure supplement 3B. N = 3 replicates/group. For a–j), cells were treated with 0.25 µg/ml doxycycline for 2 days prior to and during the assay, and fresh medium was added 4 hr prior to sample collection.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig5-figsupp4-v3.jpg)

**Figure 5—figure supplement 4.:** (a) Analysis of cell viability following treatment of A549 cells with 0–10 mM HTAU, CSA or Na2SO3 for 5 days. Viable cells were analyzed with CellTiter-Glo and normalized to untreated cells. N = 3 replicates/group. (b) Analysis of cell viability following starvation of NRF2LOW (gray) and NRF2HIGH (red) NSCLC cell lines of cystine for 3 days. Cell numbers were analyzed with crystal violet and normalized to cells grown in cystine-containing media. N = 3 replicates/group. (c) Analysis of cell viability following treatment of NRF2LOW (gray) and NRF2HIGH (red) NSCLC cell lines with 0–10 mM Na2SO3 for 3 days. Viable cells were analyzed with CellTiter-Glo and normalized to untreated cells. N = 3 replicates/group. (d) Analysis of cell viability following treatment of A549 cells expressing GFP, CDO1Y157F or CDO1WT with 0–100 µM cumene hydroperoxide (CuH2O2) for 24 hr. A549s were treated with 0.25 µg/mL doxycycline for 3 days prior to CuH2O2 treatment to induce cDNA expression. Cell numbers were analyzed with crystal violet and normalized to untreated cells. *CDO1WT vs. CDO1Y157F. #CDO1WT vs. GFP. N = 3 replicates/group. (e) Analysis of cell viability following treatment of A549 cells with 2.5 mM CSA, 2.5 mM Na2SO3 or control for 3 days, followed by treatment with 0–100 µM CuH2O2 for 24 hr. Cell numbers were analyzed with crystal violet and normalized to untreated cells. *Control vs. CSA. #Control vs. Na2SO3. N = 3 replicates/group.

We next performed a quantitative analysis of SO32- levels following CDO1 expression. CDO1WT-, but not CDO1Y157F-expressing A549s demonstrated rapid accumulation of extracellular SO32- over the 24 hr time course following media replenishment (Figure 5C). Further, the accumulation of the product of the sulfitolysis reaction, cysteine-S-sulfate (CYS-SO3-), was also observed in the medium of CDO1WT-expressing cells (Figure 5D, Figure 5—figure supplement 1A). We observed that CYS-SO3- appeared earlier than SO32-, and stopped accumulating once (CYS)2 levels were depleted, suggesting that SO32- reacted with (CYS)2 in a rapid and complete manner. To test this possibility, we incubated either CSA or sodium sulfite (Na2SO3) with culture medium in the absence of cells, and observed rapid and robust conversion of (CYS)2 to CYS-SO3- by Na2SO3 (Figure 5E), but not CSA (Figure 5—figure supplement 1B), within 5 min. Interestingly, similar depletion kinetics in this experiment could also be observed by substituting (CYS)2 with oxidized glutathione (GSSG) (Figure 5—figure supplement 1C,D), although intracellular and extracellular levels of GSSG in cell culture were much lower than (CYS)2 (Figure 5—figure supplement 1E,F), suggesting it is not the major target of SO32-. These results demonstrate that SO32- is generated downstream of CDO1 and rapidly reacts with (CYS)2, thereby depleting (CYS)2 from the culture media.

To evaluate whether SO32- production was a consequence of our CDO1 overexpression system, we transduced Keap1WT and Keap1R554Q MEFs with our inducible CDO1 vectors (Figure 5—figure supplement 2A). Consistent with its regulation by intracellular CYS, ectopic CDO1 expression was significantly higher in Keap1R554Q MEFs compared to Keap1WT MEFs. While CDO1 overexpression promoted the accumulation of intracellular CSA and HTAU, and the depletion of CYS and GSH (Figure 5—figure supplement 2B–G), we did not observe the production of SO32- or CYS-SO3- in MEFs (data not shown). Interestingly, MEFs express lower Got1 but higher Csad protein compared to A549 cells (Figure 5—figure supplement 2A), and NSCLC cell lines were uniformly low for CSAD and high for GOT1 (Figure 5—figure supplement 3A) suggesting that expression of CSA metabolic enzymes may be a key determining factor in the generation of HTAU vs. SO32-. Importantly, deletion of endogenous CDO1 in H1581 cells resulted in a dramatic reduction in CYS-SO3- production (Figure 5F), thereby demonstrating that SO32- is generated by CDO1 under physiological expression levels in lung cells.

To examine the NRF2-dependence of (CYS)2 depletion via SO32-, we utilized the NRF2 KO cells, KEAP1WT, and KEAP1MUT cell lines. NRF2 promoted CYS-SO3- production following CDO1WT expression (Figure 5G), which was accompanied by significant accumulation of both intracellular and extracellular SO32- (Figure 5—figure supplement 3B,C). These findings were recapitulated in KEAP1WT and KEAP1MUT NSCLC cell lines expressing NRF2T80K or following KEAP1 restoration, respectively (Figure 5H–K), with the exception of H322, which maintained CYS-SO32- production following KEAP1 restoration (Figure 5—figure supplement 3G). While KEAP1 restoration in these cells significantly reduced CSA production (Figure 4M), unlike A549 and H1944, intracellular CSA levels in H322 cells were still in the millimolar range (Figure 5—figure supplement 3D–F), suggesting that CSA transamination by GOT1 was saturated. Further, NRF2 stabilization with β-lapachone promoted CDO1-dependent CSA and CYS-SO3- production and (CYS)2 depletion in H1299 and H1975 cells (Figure 5—figure supplement 3H–J). Collectively, these results suggest that NRF2 induces CDO1-mediated sulfitolysis, thereby depleting extracellular (CYS)2 in NSCLC cells.

Next, we examined the toxicity of CDO1 products to NSCLC cell lines. Treatment of cells with CSA and Na2SO3, but not HTAU, led to cytotoxicity (Figure 5—figure supplement 4A). We found that (CYS)2 starvation and Na2SO3 treatment were universally toxic to NSCLC cell lines, which did not depend on NRF2 activity (Figure 5—figure supplement 4B,C). In addition, CDO1, CSA and Na2SO3 sensitized A549 cells to oxidative stress (Figure 5—figure supplement 4D,E), consistent with their ability to deplete (CYS)2. Collectively, these results demonstrate that CSA and SO32- are toxic to NSCLC cells regardless of NRF2 activity, suggesting that resistance to (CYS)2 starvation is not an inherent phenotype of NRF2HIGH cells. Rather, they are sensitive to CDO1 expression due to high intracellular CYS and CDO1 stabilization.

### Sulfitolysis is not required for the inhibition of proliferation by CDO1

To evaluate the role of GOT1 in CDO1-dependent sulfitolysis and cell growth inhibition, we generated GOT1 KO A549 and H460 cells (Figure 6A). Two independent clones of each were generated, and a sgRNA-resistant GOT1 cDNA was expressed in each to restore GOT1 expression (Birsoy et al., 2015). In support of GOT1 mediating the production of SO32- and (CYS)2 depletion, GOT1 KO cells had significantly lower CDO1-dependent (CYS)2 consumption and SO32- and CYS-SO3- production rates compared to each parental line, which was rescued by GOT1 restoration (Figure 6B). Surprisingly, we observed that CDO1 antagonized cell proliferation independent of GOT1 expression and sulfitolysis, suggesting that the intracellular metabolism of CYS also contributes to the phenotype (Figure 6C). To address this mechanism, we evaluated whether CDO1 could limit CYS-dependent processes in NSCLC cell lines, similar to what was observed in MEFs. However, unlike in MEFs, CDO1 expression did not affect CYS utilization as the rates of GSH, Coenzyme A (CoA), and protein synthesis were similar (Figure 6D–G).

![Figure 6.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig6-v3.jpg)

**Figure 6.:** (a) Western blot analysis of GOT1 and β-ACTIN expression in parental (P) A549 and H460 cells, and GOT1 KO clones #1 and #2 for each cell line expressing empty pMXS (GOT1 -) and reconstituted with pMXS-GOT1 (GOT1 +). (b) Contribution of sulfitolysis to (CYS)2 consumption by CDO1. CDO1-dependent (CYS)2 consumption, and CSA, SO32-, and CYS-SO3- production were determined as cysteine molar equivalents. N = 3 replicates/group. (c) Analysis of the proliferation of GOT1 KO A549 cells from (a) expressing CDO1Y157F (Y157F) or CDO1WT (WT). Cells were collected on the indicated days, stained with crystal violet and their absorbance at 600 nm determined. N = 3 replicates/group. (d,e) Quantitation of glutathione (GSH) total (12C + 13C) levels (d) and 13C-labeling only (e) from 13C-cystine in cells from (A) following expression of CDO1Y157F (Y157F) or CDO1WT (WT). 13C-label is shown in red, while 12C-label is gray. Cells were labeled for 1 hr. N = 3 replicates/group. (f) Analysis of Coenzyme A (CoA) labeling from 13C, 15N-cystine in cells from (a) expressing CDO1Y157F (Y157F) or CDO1WT (WT). 13C,15N-label (M + 3) is shown in red, while 12C, 14N-label is gray. Cells were labeled for 4 hr. N = 3 replicates/group. (g) Analysis of protein synthesis rates with azidohomoalanine labeling in cells from (a) expressing CDO1Y157F (Y157F) or CDO1WT (WT). Cells treated with 50 μg/mL cyclohexamide (C) were used as a positive control for translation inhibition. N = 4 replicates/group. For b–g,) cells were treated with 0.25 μg/ml doxycycline for 2 days prior to and during the assay.

### CDO1 limits NADPH availability for cellular processes

Next, we examined other consequences of CDO1 expression in cells. After (CYS)2 enters cells through its transporter xCT, it must be reduced to two CYS molecules using NADPH as the electron donor. As such, we hypothesized that the continual reduction of (CYS)2 to CYS in CDO1-expressing cells would consume a significant amount of cellular NADPH. Indeed, we observed that the NADPH/NADP+ ratio was lower following CDO1 expression in both GOT1 KO and GOT1 expressing cells (Figure 7A). Consistently, (CYS)2 starvation had the opposite effect on the NADPH/NADP+ ratio, which increased following starvation (Figure 7—figure supplement 1A). NADPH is critical for both antioxidant defense and cellular biosynthetic processes. While we found that the decrease in the NADPH/NADP+ ratio did not dramatically influence the levels of GSH and GSSG in non-stressed cells (Figure 7B), expression of CDO1 increased sensitivity to the lipid peroxidation inducer cumene hydroperoxide (CuH2O2) independent of GOT1 expression (Figure 7C), and CDO1 deletion in H1581 cells promoted CuH2O2 resistance (Figure 7—figure supplement 1B). Next, we placed cells into detached conditions, which has been shown to increase reliance on IDH1-dependent reductive carboxylation to promote NADPH generation in the mitochondria (Jiang et al., 2016). Consistently, CDO1 expression significantly impaired the ability of NSCLC cell lines to grow in soft agar (Figure 7—figure supplement 1C). Next, we examined the consequence of the altered NADPH/NADP+ ratio on NADPH-dependent metabolic reactions. Using 13C5-glutamine tracing, we observed that glutamine readily entered the TCA cycle to produce M + 4 citrate, which was unaffected or increased following CDO1 expression (Figure 7E,F), but CDO1 impaired both NADPH-dependent synthesis of proline from glutamate (Figure 7D), and NADPH-dependent reductive carboxylation of α-ketoglutarate to produce M + 5 citrate (Figure 7E,F). The antiproliferative effects of CDO1 were CYS-dependent, as either inhibition of (CYS)2 uptake with erastin or low (CYS)2 conditions resulted in loss of CDO1 expression and completely rescued the CDO1-induced proliferation defect (Figure 7—figure supplement 1D–F). Collectively, these results suggest that CDO1 further inhibits cellular processes by limiting NADPH availability, thereby impairing cellular proliferation.

![Figure 7.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig7-v3.jpg)

**Figure 7.:** (a) The NADPH/NADP + ratio was assayed following expression of CDO1Y157F (Y157F) or CDO1WT (WT) in A549 and H460 GOT1 KO cells expressing empty pMXS (GOT1 -) or reconstituted with pMXS-GOT1 (GOT1 +). N = 3 replicates/group. (b) Quantitation of reduced glutathione (GSH) and oxidized glutathione (GSSG) in KEAP1C273S-expressing cells from Figure 4k,l following expression of CDO1Y157F (Y157F) or CDO1WT (WT). N = 3 replicates/group. (c) A549 and H460 GOT1 KO cells expressing empty pMXS (dashed line, open circle) or reconstituted with pMXS-GOT1 (solid line, solid circle), followed by expression of CDO1Y157F (gray) or CDO1WT (red), were treated with 0–25 μM cumene hydroperoxide (CuH2O2) for 24 hr. Cell numbers were analyzed using crystal violet and normalized to untreated cells. *=GOT1+ CDO1WT vs. CDO1Y157F, #=GOT1- CDO1WT vs. CDO1Y157F. N = 3 replicates/group. (d) Analysis of proline (M + 5) labeling from L-[U]-13C-glutamine in GOT1 KO A549 and H460 cells expressing empty pMXS (Control) or reconstituted with pMXS-GOT1 (GOT1), followed by expression of CDO1Y157F or CDO1WT. Proline M + 5 abundance was normalized to the abundance of its precursor glutamate M + 5, and then CDO1WT levels were normalized to CDO1Y157F. Cells were labeled for 1 hr in proline-free media. N = 3 replicates/group. (e,f) Mass isotopomer analysis of citrate labeling in GOT1 KO A549 (d) and H460 (e) cells expressing empty pMXS (Control) or reconstituted with pMXS-GOT1 (GOT1) following expression of CDO1Y157F or CDO1WT cultured with L-[U]-13C-glutamine for 4 hr. N = 3 replicates/group. For (a–f), cells were treated with 0.25 µg/ml doxycycline for 2 days prior to and during the assay.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig7-figsupp1-v3.jpg)

**Figure 7—figure supplement 1.:** (a) The NADPH/NADP+ ratio was assayed following growth of A549 cells in medium containing 200 µM or 0 µM cystine for 24 hr. The ratio was normalized to cells grown in 200 µM cystine. N = 3 replicates/group. (b) H1581 cells were infected with lentivirus encoding Cas9 and non-targeting (sgCON) or CDO1-targeting (#1, #2) sgRNAs to delete CDO1 in the bulk population. Cells were treated with the indicated doses of CuH2O2 for 24 hr and cell number normalized to EtOH (Vehicle) treated cells. N = 3 replicates/group. (c) Soft agar growth of NSCLC cell lines expressing CDO1Y157F (Y157F) or CDO1WT (WT). Cells were treated with 0.25 µg/ml doxycycline for 2 days prior to and during the assay. N = 3 replicates/group. (d) Western blot analysis of CDO1 and HSP90 levels in GOT1 KO A549 and H460 cells expressing empty pMXS (Cntl) or reconstituted with pMXS-GOT1 (GOT1), followed by expression of CDO1Y157F or CDO1WT. Cells were cultured in either 200 µM or 10 µM (Cys)2, or 200 µM (Cys)2 + 0.5µM Erastin. (e) Quantification of medium (Cys)2 levels following Erastin treatment or growth in 10 µM (Cys)2. Control medium contains 200 µM (Cys)2. (f) Analysis of the proliferation of the cells from (d). Cells were fed with fresh media daily, collected on the indicated days, stained with crystal violet and their absorbance at 600 nm determined. N = 3 replicates/group. For (d,f), cells were treated with 0.25 µg/ml doxycycline for 2 days prior to and during the assay, and fresh medium was added 5 hr prior to sample collection (d) or during the assay (f).

### Nrf2 activation promotes Cdo1 accumulation in lung tumors in vivo

We next examined the ability of NRF2 to promote CDO1 stabilization under physiological (CYS)2 conditions. To this end, we generated KrasG12D; Trp53flox/flox lung tumor mice expressing either wild-type Keap1 (Keap1WT), heterozygous for Keap1R554Q (Keap1R554Q/WT), or homozygous for Keap1R554Q (Keap1R554Q/R554Q). We chose this model because Keap1 deletion in the KrasG12D; Trp53flox/flox lung tumor model was recently shown to activate Nrf2 and promote cystine uptake (Romero et al., 2017). We found that KrasG12D; Trp53flox/flox mice had similar survival regardless of Keap1 mutation status (Figure 8A). However, survival was not related to tumor burden, as KrasG12D; Trp53flox/flox; Keap1R554Q/R554Q mice displayed significant lung hemorrhage at endpoint (Figure 8B) despite small tumors (Figure 8C). Quantification of average lung tumor size revealed that KrasG12D; Trp53flox/flox mice expressing one copy of Keap1R554Q had modestly larger tumors, consistent with the findings of Romero et al., and in agreement with the dominant negative activity displayed by select Keap1 mutants (Suzuki et al., 2011). Surprisingly, complete loss of Keap1 function in the Keap1R554Q/R554Q mice led to significantly smaller tumors (Figure 8C). Further, Keap1 loss of function led to a gradient of Nrf2 activation with Keap1WT tumors expressing little to no Nqo1, Keap1R554Q/+ tumors displayed increased Nqo1 expression, and Keap1R554Q/R554Q tumors were strongly positive (Figure 8D). Importantly, Keap1R554Q/R554Q tumors strongly expressed Cdo1 (Figure 8D), demonstrating that Nrf2 activation promotes Cdo1 accumulation under physiological conditions in vivo, and suggesting that Cdo1 may impede tumor progression. Additional work is needed to understand whether induction of Cdo1, or even Nrf2, is responsible for the apparent block in tumorigenesis observed in the Keap1R554Q/R554Q mice, or whether an alternative Keap1 substrate may mediate these effects.

![Figure 8.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig8-v3.jpg)

**Figure 8.:** (a) Overall survival of Trp53flox/flox and KrasG12D; Trp53flox/flox mice expressing homozygous Keap1WT (WT/WT), heterozygous for Keap1R554Q (R554Q/WT) or homozygous for Keap1R554Q (R554Q/R554Q). (b) Representative hematoxylin and eosin (H&E) stained section depicting lung hemorrhage in KrasG12D; Trp53flox/flox; Keap1R554Q/R554Q mice compared to KrasG12D; Trp53flox/flox; Keap1WT/WT mice. (c) (Left) Representative H&E image of lung tumor burden in KrasG12D; Trp53flox/flox mice expressing Keap1WT/WT, Keap1R554Q/WT or homozygous for Keap1R554Q/R554Q. (Right) Quantification of average lung tumor size per mouse. WT/WT (N = 10 mice), R554Q/WT (N = 8 mice), R554Q/R554Q (N = 10 mice). (d) (Left) Representative Nqo1 and Cdo1 immunohistochemistry of KrasG12D; Trp53flox/flox mouse tumors expressing Keap1WT/WT, Keap1R554Q/WT or homozygous for Keap1R554Q/R554Q. B, Bronchiole; T, Tumor. (Right) Average score (scale = 0–4) for Nqo1 staining across mice. WT/WT (N = 10 mice), R554Q/WT (N = 6 mice), R554Q/R554Q (N = 10 mice).

## Discussion

The carbon, nitrogen and sulfur molecules of CYS are used for diverse cellular processes that are required for both homeostasis and proliferation. The carbon, nitrogen and sulfur atoms are incorporated into protein, GSH, TAU and CoA. Further, the sulfur atom of cysteine is incorporated into iron-sulfur (Fe-S) clusters. CYS is generally thought to be more limiting than glycine or glutamate for GSH synthesis in most tissues (Stipanuk et al., 2006). CDO1 plays a critical role in limiting CYS availability and toxicity (Jurkowska et al., 2014). CYS promotes both the stability and activity of CDO1 (Stipanuk et al., 2009), leading to the irreversible metabolism of CYS to CSA (Stipanuk et al., 2009). This mechanism of regulation prevents toxicity associated with CYS accumulation. However, the contribution of this regulatory process to CYS availability in cancer was not well understood.

Our findings implicate CDO1 as a metabolic liability for lung tumor cells with high intracellular CYS levels, particularly those with NRF2/KEAP1 mutations (Figure 9). We find that high intracellular CYS levels are a common feature of lung cancer cell lines, suggesting that NRF2-independent mechanisms exist to promote (CYS)2/CYS uptake. Indeed, (CYS)2 uptake is regulated by many signaling pathways, including EGFR, mTORC2 and p53 (Gu et al., 2017; Jiang et al., 2015; Tsuchihashi et al., 2016). Further, de novo CYS synthesis via the transsulfuration pathway (Prigge et al., 2017), direct CYS transport, or decreased CYS utilization may play a role in CYS accumulation. Notably, CDO1 promoter methylation is common across multiple cancer types (Brait et al., 2012; Jeschke et al., 2013) raising the possibility that CDO1 antagonizes the proliferation or viability of other cancers through similar mechanisms. We find that CDO1 promotes the wasting of the carbon, nitrogen and sulfur molecules of CYS as CSA and SO32-, promotes (CYS)2 depletion by SO32-, and induces depletion of NADPH. Any of these mechanisms could contribute to its growth suppressive function in vivo, but additional work is needed to evaluate the consequence of CDO1 loss in the relevant tumor microenvironment. Importantly, while limited GSSG is present in our cells and media, Sullivan et al. find that GSSG levels may exceed (Cys)2 levels in murine tumor interstitial fluid (Sullivan et al., 2019), suggesting that GSSG may be a major target of SO32-in vivo. Our findings suggest that oncogene-induced metabolic processes can be unfavorable, and warrant further investigation into the selection against metabolic processes in the context of specific driving oncogenes or nutritional states.

![Figure 9.](https://cdn.elifesciences.org/articles/45572/elife-45572-fig9-v3.jpg)

**Figure 9.:** (Left) Elevated intracellular cysteine (CYS) stabilizes CDO1, leading to the production of CSA and SO32-. In turn, SO32- depletes cystine via sulfitolysis to produce CYS-SO3-, further limiting cysteine availability and utilization. SO2 (sulfur dioxide) exists in equilibrium with SO32- and is a gas that may diffuse in and out of cells. The continual reduction of (CYS)2 to CYS depletes cellular NADPH, limiting its availability for cellular processes. (Right) CDO1 silencing promotes the accumulation of intracellular CYS and NADPH, and prevents wasting of CYS as CSA and toxic SO32-. GSR, glutathione reductase. TXNRD1, thioredoxin reductase 1. Fe-S, iron sulfur cluster.

A surprising finding from this study is that NRF2 stabilization promotes the accumulation of intracellular CYS to levels that far exceed those which are necessary for CYS-dependent metabolic processes in cancer cells. Normal intracellular CYS concentrations are approximately 100 μM (Stipanuk et al., 2006), around the Km for GCLC for CYS and typically an order of magnitude lower than GSH levels, consistent with our observed concentrations in wild-type MEFs. However, in many cases KEAP1 mutant NSCLC cell lines and even some KEAP1 wild-type lines accumulated CYS to millimolar levels without any apparent toxicity. CYS toxicity is a poorly described phenomenon that has been attributed to the reactivity of the free thiol on the CYS molecule, the production of hydrogen sulfide (H2S), autooxidation and free radical formation, and other mechanisms (Stipanuk et al., 2006). More work is needed to understand whether high intracellular CYS levels are a vulnerability of CDO1-silenced cancer cells as a consequence of these mechanisms, or whether there is an advantage to high intracellular CYS.

We observe that Cdo1 modestly limits GSH synthesis in MEFs, similar to what has been demonstrated in the liver, where deletion of Cdo1 in vivo resulted in the accumulation of CYS and GSH (Roman et al., 2013). By contrast, CDO1 depleted intracellular CYS but did not limit GSH synthesis or other CYS-dependent processes in NSCLC cell lines. One potential explanation for this difference is that cancer cells are more efficient at maintaining intracellular CYS levels and/or GSH synthesis. While more efficient maintenance of intracellular CYS is an advantage for CYS-dependent metabolism, it is also a liability because considerable resources in the form of reducing power must be committed to continually reduce (CYS)2 to replenish the CYS pool. Although we do not know the rate of NADPH production in our cell lines, comparison with NADPH production rates in other lines (Fan et al., 2014) suggest that CDO1-dependent (CYS)2 consumption would consume a significant fraction of the cellular NADPH produced, consistent with our observations.

Interestingly, we find that CSA is differentially metabolized in cancer cells and mouse embryonic fibroblasts, which correlates with differential expression of CSAD and GOT1. Partitioning between the decarboxylation and transamination reactions is likely influenced by the levels and activities of CSAD and GOT1, but this is not well studied. Evaluation of CSA metabolism at the organismal level has shown that decarboxylation of CSA via CSAD predominates over transamination by GOT1 (Weinstein et al., 1988) but little is known about this partitioning in individual tissues. Consistently, CSAD has a lower Km for CSA than GOT1 (Recasens et al., 1980; Wu, 1982). Importantly, HTAU and TAU are non-toxic molecules that have important physiological functions in controlling osmolarity, mitochondrial function, cellular redox, and other processes (Aruoma et al., 1988; Hansen et al., 2010; Schaffer et al., 2000; Suzuki et al., 2002). TAU biosynthesis is not a required process in non-hepatic tissues, however, as adequate TAU is supplied from the liver via the blood supply (Stipanuk, 2004). By contrast, SO32- is toxic in large quantities (Menzel et al., 1986) and thus excessive CSA transamination is likely disadvantageous in most cell types. Interestingly, hemorrhagic pulmonary edema is a consequence of sulfur dioxide exposure in humans (Charan et al., 1979), and additional work is needed to determine if Cdo1-mediated SO32- production is the cause of lung hemorrhage in the Keap1R554Q/R554Q mice. It is unclear what function the CSA transamination reaction serves for cells. Unlike the decarboxylation pathway, it retains carbon and nitrogen intracellularly as pyruvate and glutamate. Sulfite oxidase (SUOX) can reduce sulfite (SO32-) to sulfate (SO42-), which is an important precursor for sulfation-based detoxification of phenols, hydroxylamines, or alcohols to sulfate esters. Sulfation is also an important post-translational modification of proteins.

There are currently several approaches being developed to target aberrant CYS metabolism in cancer, including NRF2/KEAP1 mutant cancer. Despite their increased antioxidant capacity, KEAP1 mutant cells are still sensitive to (CYS)2 starvation, which could be targeted with cyst(e)inase (Cramer et al., 2017). Further, (CYS)2 uptake via xCT results in a central carbon imbalance and dependence on glutamine that can be targeted with glutaminase inhibitors (Romero et al., 2017). Our findings suggest excessive (CYS)2 uptake can also impair NADPH-dependent processes and activating CDO1 expression may have unique therapeutic potential compared to (CYS)2-depleting strategies. We find that Cdo1 accumulates in tumors from our Keap1R554Q/R554Q mutant lung cancer GEMM, which is correlated with a block in lung tumor formation. Further work is needed to determine whether Cdo1 impairs tumorigenesis in this model, and to evaluate the consequences of strategies to induce CDO1 expression on tumor growth and metabolism in vivo.

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
      <td>Chemical compound, drug</td>
      <td>Cycloheximide</td>
      <td>Sigma Aldrich</td>
      <td>01810–1G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Pyridine</td>
      <td>Sigma Aldrich</td>
      <td>270970–1L</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CuCl2</td>
      <td>Sigma Aldrich</td>
      <td>203149–10</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Methoxylamine hydrochloride</td>
      <td>Sigma Aldrich</td>
      <td>226904–5G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ethyl acetate (LC-MS grade)</td>
      <td>Sigma Aldrich</td>
      <td>34972–1 L-R</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Methanol (HPLC grade)</td>
      <td>Sigma Aldrich</td>
      <td>34860–1 L-R</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cysteine</td>
      <td>Sigma Aldrich</td>
      <td>C6852-25G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cystine</td>
      <td>Sigma Aldrich</td>
      <td>C6727-25G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>L-Cysteine S-sulfate</td>
      <td>Sigma Aldrich</td>
      <td>C2196-25MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>L-Cysteine sulfinic acid</td>
      <td>Sigma Aldrich</td>
      <td>270881–1G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hypotaurine</td>
      <td>Sigma Aldrich</td>
      <td>H1384-100MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Na2SO3</td>
      <td>Sigma Aldrich</td>
      <td>71988–250G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[34S]-Na2SO3,</td>
      <td>Sigma Aldrich</td>
      <td>753572</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Doxycycline</td>
      <td>Sigma Aldrich</td>
      <td>D9891-1G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[13C2,15N]-Glutathione trifluoroacetate salt,</td>
      <td>Sigma Aldrich</td>
      <td>683620</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>GSSG</td>
      <td>Sigma Aldrich</td>
      <td>G4376-250MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Decitabine (5-Aza-2’-deoxycytidine)</td>
      <td>Sigma Aldrich</td>
      <td>A3656-5MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cumene hydroperoxide</td>
      <td>Invitrogen</td>
      <td>component of C10445</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>N-Ethylmaleimide</td>
      <td>Chem-Impex International</td>
      <td>00142</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[13C5]-glutamine,</td>
      <td>Cambridge Isotope Labs</td>
      <td>CLM-1822-H-0.25</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[13C3, 15N]-Cysteine</td>
      <td>Cambridge Isotope Labs</td>
      <td>CNLM-3871-H-0.25</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[13C3]-Cysteine,</td>
      <td>Cambridge Isotope Labs</td>
      <td>CLM-4320-H-0.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[D4]-Cystine,</td>
      <td>Cambridge Isotope Labs</td>
      <td>DLM-1000–1</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[13C2]-Taurine</td>
      <td>Cambridge Isotope Labs</td>
      <td>CLM-6622</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[D5]-Glutathione</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-489493</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[D4]-Hypotaurine</td>
      <td>CDN Isotopes</td>
      <td>H1384-100MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Formic acid</td>
      <td>Fisher Chemical</td>
      <td>MFX04405</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>NaOH</td>
      <td>Fisher Chemical</td>
      <td>SS256500</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MSTFA + 1% TMCS solution</td>
      <td>Fisher Chemical</td>
      <td>TS-48915</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HPLC-grade water</td>
      <td>Fisher Chemical</td>
      <td>W5-1</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Acetonitrile (HPLC grade)</td>
      <td>Honeywell</td>
      <td>34967</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Erastin</td>
      <td>Cayman Chemical</td>
      <td>17754</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>β-lapachone</td>
      <td>Dr. David Boothman</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>puromycin</td>
      <td>Invivogen</td>
      <td>ant-pr-1</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>blasticidin</td>
      <td>Invivogen</td>
      <td>ant-bl-1</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (mouse)</td>
      <td>LSL-KrasG12D</td>
      <td>(Jackson et al., 2001)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (mouse)</td>
      <td>Trp53flox</td>
      <td>(Marino et al., 2000)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (mouse)</td>
      <td>Keap1R554Q</td>
      <td>this paper</td>
      <td></td>
      <td>A minigene containing a cDNA encoding wild -type exons 3–5, followed by a SV40 polyA signal, was inserted upstream of endogenous exon 3 of the Keap1 gene. Codon 554 in endogenous exon four was mutated from arginine to glutamine</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Keap1R554Q genotyping primers</td>
      <td>this paper</td>
      <td>Common (R) 5’-GCCACC CTATTCACAGACCA-3’ Mutant (F) 5’-ATGGCCA CACTTTTCTGGAC 3’ WT (F) 5’-GGGGGTAGA GGGAGGAGAAT-3’</td>
      <td>WT PCR product = 326 bp Mutant PCR product = 584 bp</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>adenoviral-Cre</td>
      <td>University of Iowa</td>
      <td>VVC-U of Iowa-5</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pRRL-CDO1</td>
      <td>this paper</td>
      <td></td>
      <td>The LT3GEPIR vector backbone (Fellmann et al., 2013) was obtained from Johannes Zuber and the MiR-E cassette was excised to generate pRRL-GFP. GFP was excised and replaced with CDO1 using pQTEV-CDO1 (addgene# 31292) as a PCR template.</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pRRL-CDO1 Y157F</td>
      <td>this paper</td>
      <td></td>
      <td>The enzyme inactive mutant (CDO1Y157F) was generated from pRRL-CDO1 by site-directed mutagenesis of the wild-type protein.</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pQTEV-CDO1</td>
      <td>Addgene</td>
      <td>31292</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>lentiCRISPR-V2</td>
      <td>(Shalem et al., 2014)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>lentiCRISPR-V2 mCdo1 #2</td>
      <td>this paper</td>
      <td></td>
      <td>progenitor: lentiCRISPR-V2; oligonucleotides for sgRNAs targeting mCDO1 (#2F 5’- caccgCGAGAGCAATCCCGCCGAGT- 3’, #2R 5’-aaacACTCGGCG GGATTGCTCTCGc-3’)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>lentiCRISPR-V2 mCdo1 #3</td>
      <td>this paper</td>
      <td></td>
      <td>progenitor: lentiCRISPR-V2; oligonucleotides for sgRNAs targeting mCDO1 (#3F 5’-caccgCGAAGAGCTCATGTAA GATG-3’, #3R 5’-aaacCATCTT ACATGAGCTCTTCGc-3’)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>lentiCRISPR-V2 hCDO1 #1</td>
      <td>this paper</td>
      <td></td>
      <td>progenitor: lentiCRISPR-V2; oligonucleotides for sgRNAs targeting hCDO1 (F - 5’-caccgGAT GCGGATCAGATCAGCCA-3’, R - 5’-aaacTGGCTGATCT GATCCGCATCc-3’)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>lentiCRISPR-V2 hCDO1 #2</td>
      <td>this paper</td>
      <td></td>
      <td>progenitor: lentiCRISPR-V2; oligonucleotides for sgRNAs targeting hCDO1 (R - 5’-caccgCGAGAGCGACCCC ACCGAGT-3’,R - 5’-aaacACTCG GTGGGGTCGCTCTCGc-3’)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLX317-NRF2</td>
      <td>Dr. Alice Berger, (Berger et al., 2016)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLX317-NRF2T80K</td>
      <td>Dr. Alice Berger, (Berger et al., 2016)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLX317-empty</td>
      <td>this paper</td>
      <td></td>
      <td>pLX317-empty was generated from pLX317 -NRF2 by site directed mutagenesis.</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti KEAP1WT</td>
      <td>this paper</td>
      <td></td>
      <td>The KEAP1WT cDNA was provided by Dr. Christian Metallo (Zhao et al., 2018); pLenti-GFP-blast was generated from pLenti- GFP-puro (addgene #17448)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti KEAP1C151S</td>
      <td>this paper</td>
      <td></td>
      <td>The KEAP1C151S cDNA was provided by Dr. Christian Metallo (Zhao et al., 2018); pLenti-GFP-blast was generated from pLenti-GFP -puro (addgene #17448)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti KEAP1C273S</td>
      <td>this paper</td>
      <td></td>
      <td>The KEAP1C273S cDNA was provided by Dr. Christian Metallo (Zhao et al., 2018); pLenti-GFP-blast was generated from pLenti-GFP-puro (addgene #17448)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>plentiCRISPR-sgGOT1</td>
      <td>addgene</td>
      <td>72874</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pMXS-GOT1</td>
      <td>addgene</td>
      <td>72872</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pMXS-empty</td>
      <td>this paper</td>
      <td></td>
      <td>pMXS-empty was generated from pMXS-GOT1 by site-directed mutagenesis.</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCMV-dR8.2 dvpr</td>
      <td>addgene</td>
      <td>8455</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCMV-VSV-G</td>
      <td>addgene</td>
      <td>8454</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>Lenti-X 293T</td>
      <td>Takara</td>
      <td>632180</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>Phoenix-AMPHO</td>
      <td>ATCC</td>
      <td>CRL-3213</td>
      <td>RRID:CVCL_H716</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>Calu3</td>
      <td>Dr John Minna, Hamon Cancer Center Collection (University of Texas-Southwestern Medical Center)</td>
      <td>(DeNicola et al., 2015)</td>
      <td>RRID:CVCL_0609</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H1581</td>
      <td>Dr John Minna, Hamon Cancer Center Collection (University of Texas-Southwestern Medical Center)</td>
      <td>(DeNicola et al., 2015)</td>
      <td>RRID:CVCL_1479</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H1975</td>
      <td>Dr John Minna, Hamon Cancer Center Collection (University of Texas-Southwestern Medical Center)</td>
      <td>(DeNicola et al., 2015)</td>
      <td>RRID:CVCL_1511</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H2087</td>
      <td>Dr John Minna, Hamon Cancer Center Collection (University of Texas-Southwestern Medical Center)</td>
      <td>(DeNicola et al., 2015)</td>
      <td>RRID:CVCL_1524</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H2347</td>
      <td>Dr John Minna, Hamon Cancer Center Collection (University of Texas-Southwestern Medical Center)</td>
      <td>(DeNicola et al., 2015)</td>
      <td>RRID:CVCL_1550</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H1792</td>
      <td>Dr John Minna, Hamon Cancer Center Collection (University of Texas-Southwestern Medical Center)</td>
      <td>(DeNicola et al., 2015)</td>
      <td>RRID:CVCL_1495</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H1944</td>
      <td>Dr John Minna, Hamon Cancer Center Collection (University of Texas-Southwestern Medical Center)</td>
      <td>(DeNicola et al., 2015)</td>
      <td>RRID:CVCL_1508</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H322</td>
      <td>Dr John Minna, Hamon Cancer Center Collection (University of Texas-Southwestern Medical Center)</td>
      <td>(DeNicola et al., 2015)</td>
      <td>RRID:CVCL_1556</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H460</td>
      <td>Dr John Minna, Hamon Cancer Center Collection (University of Texas-Southwestern Medical Center)</td>
      <td>(DeNicola et al., 2015)</td>
      <td>RRID:CVCL_0459</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>HCC15</td>
      <td>Dr John Minna, Hamon Cancer Center Collection (University of Texas-Southwestern Medical Center)</td>
      <td>(DeNicola et al., 2015)</td>
      <td>RRID:CVCL_2057</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H2009</td>
      <td>ATCC</td>
      <td>CRL-5911</td>
      <td>RRID:CVCL_1514</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H1299</td>
      <td>ATCC</td>
      <td>CRL-5803</td>
      <td>RRID:CVCL_0060</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H1993</td>
      <td>ATCC</td>
      <td>CRL-5909</td>
      <td>RRID:CVCL_1512</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H441</td>
      <td>ATCC</td>
      <td>HTB-174</td>
      <td>RRID:CVCL_1561</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>A549</td>
      <td>ATCC</td>
      <td>CCL-185</td>
      <td>RRID:CVCL_0023</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>NRF2 KO A549</td>
      <td>Dr. Laureano de la Vega</td>
      <td>(Torrente et al., 2017)</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>mouse embryonic fibroblasts</td>
      <td>this paper</td>
      <td></td>
      <td>MEFs were isolated from E13.5–14.5 day old embryos</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>JetPRIME</td>
      <td>VWR</td>
      <td>89129–922</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ImmPRESS HRP anti-rabbit kit</td>
      <td>Vector Labs</td>
      <td>MP-7451</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>E.Z.N.A. Total RNA Kit I</td>
      <td>Omega Biotek</td>
      <td>R6834-02</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>PrimeScript RT Master Mix</td>
      <td>Takara</td>
      <td>RR036A</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Taqman gene expression assays - mCdo1</td>
      <td>Thermo Fisher</td>
      <td>4448892, Mm00473573_m1</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Taqman gene expression assays - hCDO1</td>
      <td>Thermo Fisher</td>
      <td>4448892, Hs01039954_m1</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Taqman gene expression assays - mActb</td>
      <td>Thermo Fisher</td>
      <td>4448892, Mm02619580_g1</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Taqman gene expression assays - hACTB</td>
      <td>Thermo Fisher</td>
      <td>#4333762F</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>CellTiter-Glo</td>
      <td>Promega</td>
      <td>G7571</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>DC protein assay</td>
      <td>Biorad</td>
      <td>500112</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>NRF2 (Rabbit mAb)</td>
      <td>Cell Signaling Technologies</td>
      <td>12721</td>
      <td>RRID:AB_2715528; 1:1000 WB</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HSP90 (Rabbit pAb)</td>
      <td>Cell Signaling Technologies</td>
      <td>4874 s</td>
      <td>RRID:AB_2121214; 1:5000 WB</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>TXN1 (Rabbit mAb)</td>
      <td>Cell Signaling Technologies</td>
      <td>2429S</td>
      <td>RRID:AB_2272594; 1:1000 WB</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>α-tubulin (Mouse mAb)</td>
      <td>Santa Cruz</td>
      <td>sc-8035, clone TU-02</td>
      <td>RRID:AB_628408; 1:500 WB</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>β-actin (Mouse mAb)</td>
      <td>Thermo Fisher</td>
      <td>AM4302, clone AC-15</td>
      <td>RRID:AB_2536382; 1:100,000 WB</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CDO1 (Rabbit pAb)</td>
      <td>Abcam</td>
      <td>ab53436</td>
      <td>RRID:AB_940958; 1:1000 WB, discontinued, verified with Sigma CDO1 antibody</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>xCT (Rabbit pAb)</td>
      <td>Abcam</td>
      <td>ab37185</td>
      <td>RRID:AB_778944; 1:1000 WB</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>GOT1 (Rabbit pAb)</td>
      <td>Biovision</td>
      <td>A1272</td>
      <td>RRID:AB_2801348; 1:1000 WB</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>CSAD (Rabbit pAb)</td>
      <td>LSBio</td>
      <td>C375526</td>
      <td>RRID:AB_2801349; 1:1000 WB</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-NQO1 antibody (Rabbit pAb)</td>
      <td>Sigma Aldrich</td>
      <td>HPA007308</td>
      <td>RRID:AB_1079501; 1:100, IHC; 1:1000 WB</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CDO1 antibody (Rabbit pAb)</td>
      <td>Sigma Aldrich</td>
      <td>HPA057503</td>
      <td>RRID:AB_2683451; 1:100, IHC</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>dialyzed FBS</td>
      <td>Sigma Aldrich</td>
      <td>F0392</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Cysteine/cystine, methionine and glutamine free RPMI</td>
      <td>MP Biomedicals</td>
      <td>91646454</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Cysteine/cystine, methionine, pyruvate and glutamine free DMEM</td>
      <td>Gibco</td>
      <td>21013024</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MZmine 2</td>
      <td>(Pluskal et al., 2010)</td>
      <td>Version 2.30</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Thermo Xcaliber Qual Browser</td>
      <td>Thermo Fisher</td>
      <td>Version 4.0.27.19</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>EI Maven</td>
      <td>https://elucidatainc.github.io/ElMaven</td>
      <td>Version 0.3.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Agilent Mass Hunter Workstation Software - Qualitative Analysis</td>
      <td>Agilent</td>
      <td>Version B.07.00</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Image Scope software</td>
      <td>Aperio</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Mice

The Keap1 targeting vector was constructed to contain homology arms and a minigene containing a cDNA encoding wild-type exons 3–5, followed by a SV40 polyA signal, inserted upstream of endogenous exon 3 of the Keap1 gene. Codon 554 in endogenous exon four was mutated from arginine to glutamine in the targeting vector and the endogenous Keap1 locus in C10 murine ES cells (Beard et al., 2006) was targeted and cells were selected with blasticidin. Positive clones were screened by copy number real-time PCR and injected into blastocysts. Mice were housed and bred in accordance with the ethical regulations and approval of the IACUC (protocol # R IS00003893). Keap1R554Q mice were crossed with LSL-KrasG12D and Trp53flox mice for lung tumor studies. Lung tumor formation was induced by intranasal installation of 2.5 × 107 PFU adenoviral-Cre (University of Iowa) as described previously (Jackson et al., 2001). Viral infections were performed under isofluorane anesthesia, and every effort was made to minimize suffering.

### Immunohistochemistry and tumor volume analyses

Tissues were fixed in 10% formalin overnight before embedding in paraffin and sectioning. Sections were de-paraffinized in xylene and rehydrated in a graded alcohol series. Antigen retrieval was performed in 10 mM citrate buffer (pH 6.0) and endogenous peroxidase activity was quenched with 3% hydrogen peroxide. Immunohistochemical staining was performed with the ImmPRESS HRP anti-rabbit kit according to manufacturer’s instructions (Vector Labs), followed by incubation with DAB substrate (Vector Labs). Staining intensity was graded on a 0 (no staining) – 4 (most staining) scale. Slides were scanned with the Aperio imager and tumor volume calculations were performed with Image Scope software (Aperio).

### Mouse embryonic fibroblast generation and culture

MEFs were isolated from E13.5–14.5 day old embryos and maintained in pyruvate-free DMEM (Corning) supplemented with 10% FBS. MEFs were infected with empty adenovirus or adenoviral-Cre (University of Iowa) at an MOI of 500 and used within four passages.

### Generation of lentivirus and retrovirus

For lentivirus production, Lenti-X 293 T cells (Clontech) were transfected at 90% confluence with JetPRIME (Polyplus). Packaging plasmids pCMV-dR8.2 dvpr (addgene # 8455) and pCMV-VSV-G (addgene #8454) were used. For retroviral production, Phoenix-AMPHO packaging cells (ATCC CRL-3213) were used.

### Lentiviral infection of MEFs

To generate CDO1 KO MEFs, MEFs were first infected with empty pLenti-CRISPR-V2, or pLenti-CRISPR-V2 encoding sgCDO1 #2 or #3 and selected with 1 μg/mL puromycin for 4 days, followed by infection with empty or cre-encoding adenovirus. To generate CDO1 overexpressing MEFs, MEFs were first infected with pRRL-CDO1 or GFP lentivirus and selected with 1 μg/mL puromycin for 4 days, followed by infection with empty or cre-encoding adenovirus, and then treated with doxycycline.

### NSCLC cell lines and culture

GOT1 knockout A549 and H460 cells were generated using the plentiCRISPR-sgGOT1 vector and KO clones were verified by western blotting. Cell lines were infected with lentivirus at a MOI <0.2 to achieve single copy integration and CDO1 expression verified by Q-RT-PCR. Cell lines were routinely tested and verified to be free of mycoplasma (MycoAlert Assay, Lonza). All lines were maintained in RPMI 1640 medium (Hyclone or Gibco) supplemented with 10% FBS without antibiotics at 37°C in a humidified atmosphere containing 5% CO2 and 95% air.

### Analysis of CDO1 mRNA expression and promotor methylation in patient samples

Patient lung adenocarcinoma data from The Cancer Genome Atlas (TCGA), with associated KEAP1 mutation and CDO1 methylation status (Illumina HM450 Beadchip), was obtained via cBioPortal (Cerami et al., 2012; Gao et al., 2013). Patient normal lung and lung adenocarcinoma data from The Cancer Genome Atlas (TCGA), containing CDO1 methylation status (Illumina HM450 Beadchip, beta value 0 [least methylated] – 1 [most methylated]) and mRNA expression data (RNA-seq RPKM), was obtained via the MethHC database (Huang et al., 2015). The CDO1 promoter was defined as the region from 1.5 kb upstream to 0.5 kb downstream of the RefSeq TSS. The NRF2 activity score was determined as described previously (DeNicola et al., 2015).

### Analysis of mRNA expression

MEFs were seeded onto 6-well dishes and the cells were harvested at 70% confluence. NSCLC lines were harvested at 70% confluence, after treatment with 5 μM Decitabine for 3 days. During the treatment, medium was changed every 24 hr. For the NSCLC lines expressing CDO1, cells were pre-treated with DOX for 48 hr, and harvested at 4 hr after medium change. RNA was isolated with the E.Z.N.A. Total RNA Kit I (Omega Bio-Tek) according to the manufacturer’s instructions. cDNA was synthesized from 500 ng of RNA using PrimeScript RT Master Mix (Takara) according to the manufacturer’s instructions, and analyzed with Taqman gene expression assays.

### Preparation of NEM-derivatized cysteine and GSH internal standards

The N-ethylmaleamide (NEM) derivatized, isotope labeled, [13C3, 15N]-cysteine-NEM, [13C3]-cysteine-NEM, [13C2,15N]-GSH-NEM and [D5]-GSH-NEM which were prepared by derivatizing the [13C3, 15N]-cysteine, [13C3]-cysteine, [13C2,15N]-GSH, and [D5]-GSH standards with 50 mM NEM in 10 mM ammonium formate (pH = 7.0) at room temperature (30 min) as previously described (Ortmayr et al., 2015). [13C4, 15N2]-GSSG was prepared from the oxidation of [13C2,15N]-GSH as described (Zhu et al., 2008).

### Generation of internal standards for the quantification of CSA, CYS-SO3-, and cystine

[13C3, 15N]-CSA was synthesized from [13C3, 15N]-cysteine as previously described (Santhosh-Kumar et al., 1994). Briefly, 1.23 mg of [13C3, 15N]-cysteine was combined with 300 μL of 0.1 N NaOH, followed by addition of 300 nmol of CuCl2. After a 12 hr incubation at 37°C, 400 μL of 0.1 N NaOH was added and the product purified by solid phase extraction (SPE) as following. The reaction mixture was passed through 100 mg of AG MP-1M strong anion exchange resin (Bio-Rad), which was pre-equilibrated with 1.5 mL of 0.1N NaOH. After washing with 12 mL of HPLC-grade water, the isotope labeled [13C3, 15N]-CSA was eluted with 1.8 mL of 1N HCl (Figure 1—figure supplement 1B). In addition to [13C3, 15N]-CSA, [13C6, 15N2]-Cystine and [13C3, 15N]-Cysteine S-sulfate (CYS-SO3-) (Figure 5—figure supplement 1A) were also obtained during [13C3, 15N]-CSA synthesis as byproducts. The quantities of synthesized metabolites were determined using unlabeled CSA, CYS-SO3-, and Cystine standards and LC-MS/MS analysis as described (Bennett et al., 2008). Following quantification, these internal standards were used to quantify concentrations of CSA, CYS-SO3- and cystine in cell and medium extracts.

### Sample preparation for non-targeted metabolite profiling

Cells were grown in 6-well dishes, quickly washed in cold PBS, and extracted in 80% methanol (0.5 mL for NSCLC cells, 0.2 mL for MEFs, −80°C). The extracts were cleared by centrifugation, and the metabolites in the supernatant were directly analyzed (MEFs) or dried by centrifugation under vacuum (NSCLC cells, SpeedVac, Thermo Scientific). The dried pellets were re-dissolved in 20 μL of HPLC grade water and analyzed by liquid chromatography-high resolution mass spectrometry (LC-HRMS). The extracellular metabolites from 10 μL of cell culture medium were extracted with 40 μL 100% methanol (−80°C). The extract was cleared by centrifugation, and 5 μL of the supernatant analyzed by LC-HRMS.

### Sample preparation for analysis of NEM-cysteine, NEM-GSH, cystine, GSSG, hypotaurine, and taurine

Cells were plated the day before extraction in 6-well dishes so they were 70% confluent at extraction. The medium was changed the next day and the cells harvested at the indicated time point. The metabolites were extracted and derivatized with 0.5 mL of ice-cold extraction solvent (80% MeOH:20% H2O containing 25 mM NEM and 10 mM ammonium formate, pH 7.0) containing 20 μM [13C3, 15N]-cysteine-NEM, 36.4 μM [13C2,15N]-GSH-NEM, 0.13 μM [13C4, 15N2]-GSSG, 10 μM [D4]-Cystine, 20 μM [13C2]-Taurine, and 20 μM [D4]-Hypotaurine, followed by incubation on ice for 30 min. The NEM-derivatized metabolite extracts were cleared by centrifugation and analyzed by LC-MS/MS via multiple reaction monitoring (LC-MRM) or LC-HRMS. Cell volumes and number were determined using a Scepter 2.0 cell counter (Millipore) and used to calculate the intracellular metabolite concentrations and to normalize metabolite consumption/production rates.

### Sample preparation for intracellular CSA quantification

The cell culture medium was aspirated after reserving 1 mL for extracellular metabolite analysis. Cells were quickly washed with ice cold PBS, and intracellular CSA was extracted with 80% MeOH including approximately 1 μM [13C3, 15N]-CSA as an internal standard. The exact quantity was determined for each experiment using unlabeled CSA standard. After incubation for 15 min (−80°C) and scraping, the cell and metabolite mixture were transferred into a 1.5 mL tube. After clarification by centrifugation, the metabolite extracts were dried under vacuum and re-dissolved into HPLC grade water (20 μL for 6-well dishes or 40 μL for 100 mm dishes) for analysis by targeted LC-MRM.

### Sample preparation for extracellular CSA, CYS-SO3-, and cystine quantification

10 μL of cell culture medium was extracted at −80°C for at least 15 min with 40 μL of 100% ice cold MeOH containing approximately 25 μM [13C3, 15N]-CSA, 10 μM [13C3, 15N]-CYS-SO3-, and 300 μM [13C6, 15N2]-Cystine internal standards. The exact quantity was determined for each experiment using unlabeled standards. Following centrifugation (16,000 g, 20 min, 4°C), the extracellular metabolite extracts were transferred into a vial and analyzed by LC-MRM-based quantification.

### Sample preparation for sulfite quantification

A [34S]-Na2SO3 standard was purchased from Sigma Aldrich (99% purity). The cells were extracted in 80% methanol containing 1 μM of [34S]-Na2SO3 (0.5 mL for 6-well dish or 3 mL for 100 mm dishes, −80°C). The extracts were cleared by centrifugation, and the metabolites in the supernatant were dried by centrifugation under vacuum. The pellets were re-dissolved in HPLC grade water (20 μL for 6-well dishes or 40 μL for 100 mm dishes) and analyzed by UPLC-Q-Exactive-HF (Thermo Fisher Scientific, Waltham, MA). The extracellular metabolites from 10 μL of cell culture medium were extracted with 40 μL 100% methanol containing 96.5 μM [34S]-Na2SO3. The extract was cleared by centrifugation, and the metabolites in the supernatant were analyzed by LC-HRMS.

### [13C6]-Cystine tracing into cysteine, cystine, GSH, and hypotaurine

Medium containing 200 μM [13C6]-cystine were prepared as follows: For NSCLC cell line studies, cysteine/cystine, methionine and glutamine free RPMI (MP Biomedicals) was supplemented with 400 μM [13C3]-cysteine, 100 μM methionine, 2 mM glutamine and 10% dialyzed FBS (dFBS). For MEF studies, cysteine/cystine, methionine, pyruvate and glutamine free DMEM (Gibco) was supplemented with 400 μM [13C3]-cysteine, 200 μM methionine, 4 mM glutamine and 10% dFBS. Medium was sterile filtered using a 0.2 um PES vacuum filter and incubated for 48 hr at 4°C to allow oxidation of cysteine to cystine. Prior to 13C-labeling, cells were preconditioned in medium containing dFBS and 12C-cystine for 24 hr. Cells were labeled with 13C-cystine for the indicated timepoints, and then harvested. The metabolites were extracted and derivatized with NEM in ice-cold extraction solvent (80% MeOH:20% H2O containing 25 mM NEM and 10 mM ammonium formate, pH = 7.0) which includes stable isotope labeled internal standards of 20 μM [13C3, 15N]-cysteine-NEM, 6.4 μM [D5]-GSH-NEM, 10 μM [D4]-Cystine, and 20 μM [D4]-Hypotaurine followed by incubation on 4°C for 30 min. The NEM-derivatized metabolite extracts were cleared by centrifugation and analyzed by targeted LC-MRM.

### [13C6, 15N2]-Cystine tracing into CoA

Cysteine/cystine, methionine and glutamine free RPMI (MP Biomedicals) was supplemented with 200 μM [13C6, 15N2]-Cystine, 100 μM methionine, 2 mM glutamine and 10% dFBS as described above. NSCLC cell lines were preconditioned in medium containing dFBS and 12C-cystine for 24 hr in 10 cm dishes, followed by feeding with [13C6, 15N2]-Cystine containing media. After 4 hr, the medium was aspirated, cells were quickly washed with ice cold PBS, and cellular metabolites extracted with 1 mL of 80% MeOH (−80°C, 15 min). After scraping, the metabolite extract was transferred into an Eppendorf tube and cleared by centrifugation (17000 g, 20 min, 4°C). The supernatant was dried under vacuum overnight, and stored at −80°C. Dried sample pellets were resuspended in HPLC-grade water (20 μl) and centrifuged at 20,000 g for 2 min to remove insoluble material. Supernatants (5 μl) were injected and analyzed using a hybrid 6500 QTRAP triple quadrupole mass spectrometer (AB/SCIEX) coupled to a Prominence UFLC HPLC system (Shimadzu) via selected reaction monitoring (MRM). ESI voltage was +4900V in positive ion mode with a dwell time of 3 ms per SRM transition. Approximately 10–14 data points were acquired per detected metabolite. The following SRM transitions were used: native Coenzyme A [M + 0] (Q1 = 768.13, Q2 = 261.13, collision energy =+ 39V) and 13C2,15N1 isotope labeled Coenzyme A [M + 3] (Q1 = 771.13, Q2 = 264.13, collision energy =+ 39V). Incorporation of 13C3,15N1-cysteine into Coenzyme A yields 13C2,15N1-Coenzyme A due to a decarboxylation step during Coenzyme A synthesis. Samples were delivered to the mass spectrometer via hydrophilic interaction chromatography (HILIC) using a 4.6 mm i.d x 10 cm Amide XBridge column (Waters) at 400 μl/min. Gradients were run starting from 85% buffer B (HPLC grade acetonitrile) to 42% B from 0 to 5 min; 42% B to 0% B from 5 to 16 min; 0% B was held from 16 to 24 min; 0% B to 85% B from 24 to 25 min; 85% B was held for 7 min to re-equilibrate the column. Buffer A was comprised of 20 mM ammonium hydroxide/20 mM ammonium acetate (pH = 9.0) in 95:5 water:acetonitrile. Peak areas from the total ion current for each metabolite SRM transition were integrated using MultiQuant v3.0 software (AB/SCIEX).

### [13C5]-glutamine tracing into citrate and proline

Cysteine/cystine, methionine, pyruvate and glutamine free DMEM (Gibco) was supplemented with 4mM [13C5]-glutamine, 200μM methionine, 200μM cystine and 10% dFBS. NSCLC cell lines were seeded onto 6-well dishes, preconditioned in DMEM containing 12C-glutamine and 10% dFBS for 24 hr, and subsequently the medium was changed to [13C5]-glutamine containing medium for the indicated time. The medium was aspirated, cells were quickly washed with ice cold PBS, and cellular metabolites were extracted with 500 μL of 80% MeOH (-80°C, 15 min). After scraping, the metabolite extract was cleared by centrifugation (17000g, 20 min, 4°C). For [13C5]-glutamine $→$ (M+5) proline tracing, the supernatant was directly analyzed by LC-MS. For the [13C5]-glutamine $→$ citrate tracing, the supernatant was dried under vacuum and derivatization was performed for GC-MS analysis (Carey et al., 2015). The dried pellet was derivatized by adding 50 μL of methoxylamine hydrochloride (40 mg/mL in Pyridine) at 30°C for 90 min. After mixing the derivatized solution with 70 μL of Ethyl-Acetate in a glass vial, the metabolite mixture was further derivatized by adding 80 μL of MSTFA + 1%TMCS solution (37°C for 30 min). The final derivatized solution was transferred into a glass vial insert, and analyzed using an Agilent 7890B/5977B MSD (Agilent, Santa Clara, CA) GC-MS system.

### LC-HRMS conditions for NSCLC non-targeted metabolomics and sulfite quantification

Non-targeted metabolite profiling and sulfite quantification was conducted using Ultimate 3000 or Vanquish UPLC systems coupled to a Q Exactive HF (QE-HF) mass spectrometer equipped with HESI (Thermo Fisher Scientific, Waltham, MA). The analytical condition was as following. A Luna 3 µm HILIC 200 Å, LC Column 100 × 2 mm (Phenomenex, Torrance, CA, Part N: 00D-4449-B0) was applied as a stationary phase. The mobile phase A was 0.1 % formic acid in water, and the mobile phase B was 100% Acetonitrile (ACN). The column temperature was set to 30°C, and the gradient elution was conducted as following at a flow rate of 0.35 mL/min: 0 to 3 min, 0 % of phase A; 3 to 13 min, linear gradient from 0% to 80% of phase A; 13 to 16 min, 80% of phase A. The MS scan was operated in negative mode and the mass scan range was 58 to 870 m/z. The FT resolution was 120,000, and the AGC target was 3 × 106. The capillary temperature was 320°C, and the capillary voltage was 3.5 kV. The injection volume was 5µL. The MS peak extraction, the chromatographic peak extraction and deconvolution, the peak alignment between samples, gap filling, putative peak identification, and peak table exportation for untargeted metabolomics were conducted with MZmine 2 (2.23 Version) (Pluskal et al., 2010). The identity of CSA, cysteine, GSH, and sulfite were further confirmed by authentic standards. For sulfite quantification, [34S]-HSO3- and [32S]-HSO3- peaks were extracted with a 20 ppm MS filter, and their peak areas were manually integrated using Thermo Xcaliber Qual Browser. The quantification was based on previous methods (Bennett et al., 2008).

### LC-HRMS conditions for MEF non-targeted metabolomics and intracellular cysteine quantification

The LC-HRMS method is modified from previous study (Cantor et al., 2017) using Vanquish UPLC systems coupled to a Q Exactive HF (QE-HF) mass spectrometer equipped with HESI (Thermo Fisher Scientific, Waltham, MA). For chromatographic separation, a SeQuant ZIC-pHILIC LC column, 5 µm, 150 × 4.6 mm (MilliporeSigma, Burlington, MA) with a SeQuant ZIC-pHILIC guard column, 20 × 4.6 mm (MilliporeSigma, Burlington, MA) was used. The mobile phase A was 10mM ammonium carbonate and 0.05% ammonium hydroxide in water, and the mobile phase B was 100% Acetonitrile (ACN). The column temperature was set to 30°C, and the gradient elution was conducted as following at a flow rate of 0.25 mL/min: 0 to 13 min, linear gradient from 80% to 20% of phase B; 13 to 15 min, 20% of phase B. The MS1 scan was operated in both positive and negative mode for non-targeted metabolomics, or only in positive mode for the NEM-derivatized cysteine quantification. The mass scan range was 60 to 900 m/z. The MS resolution was 120,000, and the AGC target was 3 × 106. The capillary temperature was 320°C, and the capillary voltage was 3.5 kV. The injection volume was 5µL for both positive mode and negative mode. For the non-targeted metabolomics, the data analysis was performed with EI Maven v0.3.1 (https://elucidatainc.github.io/ElMaven/) (Clasquin et al., 2012). Metabolite identification was based on comparison of both retention time and m/z value of sample peaks with an internal library (MSMLS Library, Sigma Aldrich). For cysteine quantification, the Cysteine-NEM and [13C3, 15N]-Cysteine-NEM peaks were extracted with a 10 ppm MS tolerance, and their peak areas were manually integrated using Thermo Xcaliber Qual Browser. The quantification was based on previous method (Bennett et al., 2008).

### LC-MRM conditions for targeted analyses

The targeted analysis of Cysteine-NEM, GSH-NEM, GSSG, cystine, hypotaurine, taurine, CSA, CYS-SO3-, GS-SO3-, Glutamic acid, and Proline were conducted by selected reaction monitoring (MRM) using an Ultimate 3000 UPLC system coupled to a Thermo Finnigan TSQ Quantum equipped with HESI (Thermo Fisher Scientific, Waltham, MA). The chromatographic separation was performed as previously described (Liu et al., 2014). As a stationary phase, an XBridge Amide Column 3.5µm (2.1 × 100mm) (Waters, Milford, MA) was used. The mobile phase A was 97% Water and 3% ACN (20 mM NH4Ac, 15 mM NH4OH, pH = 9.0) and the mobile phase B was 100% ACN. The column temperature was set to 40°C, and the gradient elution was as following at 0.35 mL/mL of flow rate: 0 to 3 min, linear gradient from 15% to 70% of Phase A; 3 to 12 min: linear gradient from 70% to 98% of Phase A; 12 to 15 min, sustaining 98% of Phase A. The MS acquisition operated at the positive or negative mode. The capillary temperature was 305 °C, the vaporizer temperature was 200 °C. The sheath gas flow was 75 and the auxiliary gas flow was 10. The spray voltage was 3.7 kV. The MRM conditions (parent ion → fragment ion; collision energy) of metabolites were as follows. Positive mode: Hypotaurine (m/z 110 → m/z 92; 10); [13C2]-Hypotaurine (m/z 112 → m/z 94; 10); [D4]-Hypotaurine (m/z 114 → m/z 96; 10); Taurine (m/z 126 → m/z 108; 11); [13C2]-Taurine – (m/z 128 → m/z 110; 11); Cysteine-NEM (m/z 247 → m/z 158; 30); [13C3]-Cysteine-NEM (m/z 250 → m/z 158; 30); [13C3, 15N]-Cysteine-NEM (m/z 251 → m/z 158; 30); GSH–NEM m/z (m/z 433 → m/z 304; 15); [13C2,15N]-GSH-NEM (m/z 436 → 307m/z; 15); [D5]-GSH–NEM (m/z 438 → m/z 304; 15); GSSG (m/z 613 → m/z 355; 25), [13C4, 15N2]-GSSG (m/z 619 → m/z 361; 25); Cystine (m/z 241→ m/z 74; 30); [D4]-Cystine (m/z 245 → m/z 76; 30); [13C6]-Cystine (m/z 247 → m/z 76; 30); [13C6, 15N2]-Cystine (m/z 249 → m/z 77; 30); CYS-SO3- (m/z 202 → m/z 74; 27), [13C3, 15N]- CYS-SO3- (m/z 206 → 77; 27); [M+5]-Glutamate (m/z 153 → m/z 88; 20); [M+5]-Proline (m/z 121.1 → m/z 74.1). Negative mode: CSA (m/z 152 → m/z 88; 17), [13C3, 15N]-CSA (m/z 156 → m/z 92; 17), GS-SO3- (m/z 386 → m/z 306; 20). All peaks were manually integrated using Thermo Xcaliber Qual Browser. The quantification of metabolites was calculated by an isotope ratio-based approach according to published methods (Bennett et al., 2008).

### GC-MS-based selective ion monitoring (SIM)

For the [13C5]-glutamine $→$ citrate labeling analysis, the TMS-derivatized samples were analyzed using previously established GC-MS conditions (Kind et al., 2009). The inlet temperature was set to 250°C and the inlet pressure was 11.4 psi. The purge flow was 3 mL/min and the split ratio was 2:1. The stationary phase was an Agilent J&W DB-5MS +10m Duraguard Capillary Column (30 m × 250 μm × 0.25 μm) (Part number: 122-5532G, Agilent Technology, Santa Clara, CA). The oven temperature gradient condition was set as following: 0 to 27.5 min, linear gradient from 60 to 325°C; 27.5 to 37.5 min, 325°C. The EI-MS scan range was 50 to 600 m/z and the scan speed was 2.7 scans/sec. The solvent delay was set to 5.90 min. The MSD transfer line temperature was 250°C, The EI energy was 70 eV, the EI source temperature was 230°C, and the MS Quadrupole temperature was 150°C. The ions for Selective Ion Monitoring (SIM) of derivatized citrate (4TMS) were as following: 465 [M]+, 466 [M+1]+, 467 [M+2]+, 468 [M+3]+, 469 [M+4]+, 470 [M+5]+, and 471 [M+6]+. All peaks were manually integrated using Agilent MassHunter Qualitative Analysis Software and the natural abundance isotopes correction was performed according to published methods (Mullen et al., 2011) using IsoCor software (Millard et al., 2012).

### Cell viability assays

Cells were plated in 96-well plates at a density of 5,000–10,000 cells/well in 100 μL final volume. The next day, the medium was changed to 100 μL medium containing CSA, Na2SO3 or HTAU at the indicated concentrations. 3–5 days later, CellTiter-Glo (Promega) was used to measure cell viability. Alternatively, cells were fixed with 4% paraformaldehyde, stained with crystal violet, washed and dried. Crystal violet was solubilized in 10% acetic acid and the OD600 was measured. Relative cell number was normalized to untreated cells. Experiments were repeated more than twice.

### Cell proliferation assays

Prior to the start of the proliferation assay, cells were treated with 0.25 μg/mL doxycycline for 2 days to induce CDO1 or GFP expression. Cells were seeded at 5,000 cells/well in 96-well plates and allowed to proliferate for the indicated time points. Plates were fixed with 4% paraformaldehyde, stained with crystal violet, washed and dried. Crystal violet was solubilized in 10% acetic acid and the OD600 was measured.

### Immunoblotting

Lysates were prepared in RIPA buffer (20 mM Tris-HCl [pH 7.5], 150 mM NaCl, 1 mM EDTA, 1 mM EGTA, 1% NP-40, 1% sodium deoxycholate) containing protease inhibitors (Roche complete). Protein concentrations were determined by the DC protein assay (Bio-Rad). Lysates were mixed with 6X sample buffer containing β-ME and separated by SDS-PAGE using NuPAGE 4–12% Bis-Tris gels (Invitrogen), followed by transfer to 0.45 μm Nitrocellulose membranes (GE Healthcare). The membranes were blocked in 5% non-fat milk in TBST, followed by immunoblotting. During this study, the Abcam CDO1 antibody was discontinued. The CDO1 antibody from Sigma Aldrich provides similar results for human and mouse CDO1 (data not shown).

### NADPH/NADP+assay

NSCLC cells were plated in 6 cm dishes and analyzed at 70% confluence. 4 hr prior to harvest, cell culture medium was changed to fresh media. Cells were extracted and the NADPH/NADP+ ratio was measured using the NADP/NADPH-Glo Assay kit (Promega) according to the manufacturer’s instructions.

### Protein synthesis assay

Protein synthesis analysis was performed using the Click-It HPG Alexa Fluor 488 Protein Synthesis Assay Kit (Life Technologies). Briefly, cells were treated with doxycycline (0.25 μg/mL) for 24 hr, then seeded into black walled, clear bottom 96-well tissue culture plates at 20,000 cells/well in doxycycline-containing media. The following day, cells were treated with HPG (1 μg/mL) in methionine-free DMEM (10% dFBS, 1% Pen/Strep, 10 mM HEPES). Cycloheximide (50 μg/mL) treatment was included as a positive control. After 4 hr, the cells were fixed with 3.7% formaldehyde in PBS for 15 min at room temperature, and stained according to the manufacturer’s instructions. The fluorescence signal (ex/em: 475/520 nm) was measured using a Glomax plate reader (Promega), followed by staining with crystal violet. The fluorescence signal was normalized to the crystal violet absorbance value.

### Soft agar assays

Soft agar assays were performed in triplicate in 6-well dishes. A 1 mL base layer of 0.8% agar in RPMI was plated and allowed to solidify, then 5,000 cells/well were plated in 0.4% agar on top. The following day, 1 mL of RPMI was added to each well, and changed as needed. Colonies were allowed to form for 10–14 days, and wells were stained with 0.01% crystal violet in a 4%PFA/PBS solution. Plates were scanned on a flatbed scanner and colonies quantified with Image J.

### Statistical analysis

Data were analyzed using a two-sided unpaired Student’s t test unless otherwise noted. GraphPad Prism seven software was used for all statistical analyses, and values of p<0.05 were considered statistically significant (*p<0.05; **p<0.01; ***p<0.001, ****p<0.0001. In some figures with multiple comparisons # is used in addition to *). The mean ± standard error of experiments performed in at least triplicate is reported. Similar variances between groups were observed for all experiments. Normal distribution of samples was not determined.
