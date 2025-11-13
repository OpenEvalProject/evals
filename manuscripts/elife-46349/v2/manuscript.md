# Single-cell sequencing of neonatal uterus reveals an Misr2+ endometrial progenitor indispensable for fertility

## Authors

- Hatice Duygu Saatcioglu<sup>1</sup> ([ORCID: 0000-0003-2210-0005](https://orcid.org/0000-0003-2210-0005))
- Motohiro Kano<sup>1</sup> ([ORCID: 0000-0002-5443-0175](https://orcid.org/0000-0002-5443-0175))
- Heiko Horn<sup>1</sup> ([ORCID: 0000-0003-4898-0557](https://orcid.org/0000-0003-4898-0557))
- Lihua Zhang<sup>1</sup>
- Wesley Samore<sup>4</sup>
- Nicholas Nagykery<sup>1</sup>
- Marie-Charlotte Meinsohn<sup>1</sup>
- Minsuk Hyun<sup>5</sup>
- Rana Suliman<sup>1</sup>
- Joy Poulo<sup>1</sup>
- Jennifer Hsu<sup>6</sup> ([ORCID: 0000-0001-6928-2585](https://orcid.org/0000-0001-6928-2585))
- Caitlin Sacha<sup>6</sup>
- Dan Wang<sup>7</sup>
- Guangping Gao<sup>7</sup>
- Kasper Lage<sup>1</sup>
- Esther Oliva<sup>4</sup>
- Mary E Morris Sabatini<sup>8</sup>
- Patricia K Donahoe<sup>1</sup>
- David Pépin<sup>1</sup> ([ORCID: 0000-0003-2046-6708](https://orcid.org/0000-0003-2046-6708)) †

### Affiliations

1. Pediatric Surgical Research Laboratories Massachusetts General Hospital Boston United States
2. Department of Surgery Harvard Medical School Boston United States
3. Stanley Center Broad Institute of MIT and Harvard Cambridge United States
4. Department of Pathology Massachusetts General Hospital Boston United States
5. Department of Neurobiology Harvard Medical School Boston United States
6. Department of Gynecology and Reproductive Biology Massachussets General Hospital Boston United States
7. Horae Gene Therapy Center University of Massachusetts Medical School Worcester United States
8. Department of Gynecology and Reproductive Biology Massachussets General Hospital Boston United States

† Corresponding author

## Abstract

The Mullerian ducts are the anlagen of the female reproductive tract, which regress in the male fetus in response to MIS. This process is driven by subluminal mesenchymal cells expressing Misr2, which trigger the regression of the adjacent Mullerian ductal epithelium. In females, these Misr2+ cells are retained, yet their contribution to the development of the uterus remains unknown. Here, we report that subluminal Misr2+ cells persist postnatally in the uterus of rodents, but recede by week 37 of gestation in humans. Using single-cell RNA sequencing, we demonstrate that ectopic postnatal MIS administration inhibits these cells and prevents the formation of endometrial stroma in rodents, suggesting a progenitor function. Exposure to MIS during the first six days of life, by inhibiting specification of the stroma, dysregulates paracrine signals necessary for uterine development, eventually resulting in apoptosis of the Misr2+ cells, uterine hypoplasia, and complete infertility in the adult female.

## Introduction

In mammals, both sexes initially develop Mullerian ducts, consisting of a single layer of epithelial cells surrounded by undifferentiated mesenchymal cells. Mullerian Inhibiting Substance Receptor (Misr2/Amhr2) expression is first detected in the Mullerian mesenchyme at around E13.5 both in males and in females (Arango et al., 2008). In male mice, secretion of MIS (also known as Anti-Mullerian Hormone or AMH) by the developing testes causes regression of the Mullerian ducts during embryonic days 14.5–15.5 (Jost, 1947; Josso et al., 1976). Regression of the male Mullerian ductal epithelium is mediated through non-cell autonomous paracrine signals emanating from the underlying Misr2+ mesenchymal cells in response to MIS, and is thought to be dependent on Wnt signaling and beta-catenin activity in the epithelium (Mullen and Behringer, 2014). The Mis/Misr2 (Amh/Amhr2) pathway is highly specific to this process, since either ligand or receptor knockout mice present with identical phenotypes of persistent Mullerian duct syndrome (PMDS), a rare form of male pseudohermaphroditism in mice (Behringer et al., 1994; Mishina et al., 1996; Mishina et al., 1999) and humans (Imbeaud et al., 1994). It is thought that the narrow developmental window when Mullerian duct regression occurs is the only period when these Misr2+ mesenchymal cells are able to respond to MIS, beyond which further differentiation of the duct renders it insensitive to this inhibitory signal (Josso et al., 1976). Indeed, transgenic mice with constitutive overexpression of MIS, driven by a metallothionein-1 promoter, during the critical period of Mullerian duct formation displayed Mullerian agenesis and quickly lost all germ cells in the ovary after birth (Behringer et al., 1990).

In females, which do not express MIS during embryonic development, the fate of these subluminal Misr2+ mesenchymal cells remains unclear. In adult mice, expression of Misr2 is restricted to the myometrium, suggesting a common origin for both cell types (Arango et al., 2005; Arango et al., 2008); however, the lack of an inducible Misr2 reporter mouse has precluded a precise lineage tracing. Many cell types of the urogenital ridge primordium including the coelomic epithelium, mesonephric mesenchyme, and Wolffian duct epithelium are thought to contribute to the formation and development of the Mullerian duct as it further differentiates into the oviduct, uterus, cervix, and upper vagina (Fujino et al., 2009; Mullen and Behringer, 2014). In rodents, most of the differentiation of the uterine layers occurs postnatally; at birth, the uterus consists of a single layer of luminal epithelium surrounded by undifferentiated mesenchyme which later develops into myometrium and endometrial stromal cells, while the epithelium subsequently gains the ability to form endometrial glands though invagination at postnatal day (PND) 6–9 (Branham et al., 1985; Brody and Cunha, 1989). The timing of development of the endometrial stroma, and its contribution to the coordination of development of the myometrium and endometrial glands in early postnatal development are poorly understood. Mutations of genes which orchestrate early Mullerian mesenchyme development can have drastic consequences on female fertility and lead to Mullerian aplasia or uterine hypoplasia as observed in the Mayer-Rokitansky-Kuster-Hauser syndrome (Patnaik et al., 2015). Therefore, the pathways involved in early postnatal specification of the uterine compartments are critical to our understanding of Mullerian development and uterine factor infertility. Here, we characterize the persistence of subluminal Misr2+mesenchymal cells beyond the embryonic period of sexual differentiation, document their retained sensitivity to MIS neonatally, and characterize their critical role in the development of the endometrial stroma.

## Results

### Female mullerian subluminal mesenchyme maintains Misr2 expression and MIS sensitivity postnatally in rodents

To determine the fate of the Mullerian subluminal mesenchyme in the developing uterus, we sought to identify specific markers whose expression in that cell type perdured postnatally. Although the embryonic development of the Misr2+ Mullerian mesenchyme has been extensively studied (Jamin et al., 2002; Arango et al., 2008; Kobayashi et al., 2011), its early postnatal fate has not. Using lineage tracing in a Misr2-CRE/TdTomato reporter transgenic cross in C57BL/6 mice, we first confirmed that embryonic urogenital Misr2+ intermediate mesoderm gives rise to both the endometrial and the myometrial layers of the uterus, but not its epithelium (Figure 1—figure supplement 1A). Because Misr2-CRE is not inducible, any Misr2 expression during early development will result in permanent expression of the TdTomato reporter (Figure 1—figure supplement 1A) Therefore, to track further the Misr2+ cells in Mullerian mesenchyme, we conducted careful spatiotemporal studies using Misr2 RNA in situ hybridization (RNAish) from the embryonic period (E14-15) into postnatal life (Figure 1A). As expected, expression of Misr2 is restricted to the mesenchyme surrounding the Mullerian duct in both male and female urogenital ridges during embryonic development (E17-19) (Figure 1A). Postnatally, Misr2 expression becomes increasingly restricted to a thin band of subluminal mesenchyme, while being excluded from the epithelium and developing myometrium (Figure 1A, PND 0, PND 2) (Figure 1A, Figure 1—source data 1). Following differentiation of the functional layers of the uterus around PND 6 (Brody and Cunha, 1989), Misr2 expression commences to be detectable in the myometrium consistent with previous findings (Arango et al., 2008) (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig1-v2.jpg)

**Figure 1.:** (A) RNAish (RNA scope) analysis of Misr2 in transverse sections of male urogenital ridges at E 17.5, and in a time series of the developing uteri including E 18.5, E 19.5, PND 0, 2, and 6 in mice). Scale bars = 50 µm (n = 8 for<PND6; n = 4 for>PND6). Number of mice analyzed per time point is presented in Figure 1—source data 1. Black arrows demarcate to the myometrial layer at PND 20. (B) Representative scheme of the Misr2 expression pattern in the developing uterus. Subluminal mesenchymal cells continue to express Misr2 in the postnally until around PND 6. We sought to investigate the fate of these postnatal Misr2+ subluminal cells, and their possible role as progenitor cells of the endometrial stroma.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Uteri from Misr2-cre-tdtomato mice were analyzed on PND 20. Scale bar = 50 µm. Note that all the layers of the adult uterus except the epithelium are derived from Misr2+ cells during early embryonic development. (B) Misr2 QPCR analysis of the developing rat uteri at PND 3, 4, 6, 10, 15, and 60. (C) Endogenous MIS (MISR2 ligand) levels were measured in the serum of wild-type rats at PND 1, 4, 6 and 20 by ELISA (left) (n > 2), mean ± SEM, statistical significance indicated by ** (p<0.01) by one-way ANOVA followed by Tukey Multiple comparison test. (D) Misr2 expression pattern from the fallopian side (a) and the cervix side (b) of the developing uteri (PND 4 and PND 6) in rats. Note that the Misr2 expression pattern is consistently subluminal in proximal and distal transverse locations of the uterine horn. Scale bars = 50 µm. E. RNAish (RNA scope) of Misr2 in middle transverse sections in a time series of the developing rat uteri including PND 0, 2, 3 and 6 in rats. Scale bars = 50 µm (n = 8 for<PND 6; n = 5 for>PND 6). Number of replicates per time point is presented in Figure 1—source data 1. Rats were used as the model organism to replicate the findings observed in mice tissue sections in Figure 1A.

To evaluate the effect of MIS on the development of the uterus, we chose to use rats which have larger litters and display a similar spatiotemporal pattern of Misr2 expression (Figure 1—figure supplement 1D–E, Figure 1—source data 1). Furthermore, in rats, Misr2 expression is gradually attenuated in the PND1-6 period, both at the proximal (cervix) and at the distal (oviduct) ends of the developing uterine horns (Figure 1—figure supplement 1D) coinciding with the timing of expansion of the endometrial stroma, and the rise in secretion of MIS from the developing ovaries, which was measured in the rat serum by ELISA (Figure 1—figure supplement 1B and C). To evaluate the sensitivity of Misr2+ mesenchymal cells to MIS during this postnatal period, we treated rat pups with adeno-associated viral vectors (AAV9) (Pépin et al., 2015; Kano et al., 2017) delivering MIS at PND 1 (Figure 1B and Figure 2A). Administration of a single dose of AAV9-MIS (5E10 particles/pup) on PND 1 led to a robust induction (2.8 ± 0.7 µg/ml) of circulating exogenous MIS as measured by ELISA on PND6 (Figure 2B). Postnatal exposure to MIS led to an alteration in the appearance of the uterus by PND 6, and severe uterine hypoplasia by PND 20, suggestive of a failure of the uterus to develop beyond its perinatal state (Figure 2C). Histomorphological analyses of transverse uterine sections revealed smaller uteri with underdeveloped endometrial stromal layers and smaller lumina in MIS-treated rats compared to their sibling controls at all time points analyzed (PND 6, 10, and 20) (Figure 2C and D, Figure 2—source data 1).

![Figure 2.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig2-v2.jpg)

**Figure 2.:** (A) Rat pups were treated with AAV9-MIS (MIS) or empty vector control (CTL) on postnatal day1 (PND 1) and euthanized at different developmental time points (B–F). Rats were used as the initial model organism since their litter sizes are bigger than mice. (B) MIS serum levels from control and AAV9-MIS treated rats on day 6 (n = 3 for both). (C) H& E sections from CTL and AAV9- MIS treated uteri on PND 3, 6, and 20. Endometrial glands are demarcated by black arrows on day 20. Scale bars = 100 µm. (D) Percentage of the endometrial stroma area (%), and luminal duct height of the CTL and MIS-treated uteri (Figure 2—source data 1). (E) Misr2 and Smad6 expression pattern by RNAish. Scale bars = 100 µm. (F) Smooth muscle α-actin (SMA) in red, and Vimentin (Vim) in green on CTL and AAV9-MIS treated uterine sections (PND 6, scale bars = 100 µm).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Foxa2 immunofluorescence (red) in CTL and MIS-treated rat uteri sections at postnatal day 20. Note that the glandular ducts were missing in the treated uteri. Scale bars = 50 µm. (B) Foxa2 QPCR analysis of control and treated rats at various time points (n > 2, unpaired Student t-test, mean ± SEM, * (p<0.05)). (C) Smooth muscle α actin (SMA) immunofluorescence (red) on CTL and MIS-treated uteri at PND 3 and 45. Scale bars = 50 µm (D) SMA and Transgelin (Tagln) expression levels by qPCR on PND 6, 15, and 60.

Treatment with MIS prevented the gradual decrease of Misr2+ cells, and inhibited the expansion of the endometrial stroma normally observed by PND 6 (Figure 2E). For consistency and clarity, we will refer to these persistent Misr2+ subluminal mesenchymal cells in the MIS-treated animal as ‘inhibited progenitors’, although this function remains presumptive. In response to MIS, these inhibited putative progenitors expressed high levels of Smad6, a negative regulator of TGFβ signaling, and a previously reported canonical downstream target of MIS in the Mullerian mesenchyme (Figure 2E), suggesting MIS signaling was both operational and autonomous to these Misr2+ cells (Clarke et al., 2001; Mullen et al., 2018).

Interestingly, the endometrial stromal hypoplasia resulting from MIS exposure precluded later development of endometrial glands, as confirmed by absence of Foxa2 marker expression in immunofluorescence and qPCR (Figure 2—figure supplement 1A and B). However, the development of the circular myometrial layers was unaffected by exposure to MIS, as shown in the MIS-treated transverse uterine sections by immunofluorescence, and qPCR analysis of smooth muscle markers such as smooth muscle actin (Acta2) and transgelin (Tagln), which remain similar at various time points between control and MIS exposed uteri (Figure 2—figure supplement 1C and D). Surprisingly, the inhibited progenitor cells expressed Acta2 ectopically (shown in red) as well as Vimentin (shown in green) in response to MIS on PND 6 (Figure 2F), suggesting a metaplastic effect of MIS.

#### Single Cell RNA sequencing of the PND 6 uterus uncovered an unexpected diversity of cell types in control and MIS-treated uteri

To understand how MIS dysregulates stromal differentiation, we followed the fate of the Misr2+ subluminal mesenchymal cells following MIS treatment using single-cell RNA sequencing (scRNAseq), based on droplet microfluidic sorting of single cells (inDROP) (Klein et al., 2015). We performed an enzymatic digestion of the whole uteri on PND 6 (Figure 3A), a time point at which the Misr2+ subluminal mesenchymal cells are almost completely gone in the normal uteri, but are retained in the MIS-treated ones (Figure 2E).

![Figure 3.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig3-v2.jpg)

**Figure 3.:** (A) Rat pups were treated with empty vector control (CTL) or AAV9-MIS (MIS) on PND 1, and euthanized on PND 6 (n = 3 for both). Following whole-tissue dissociation, RNA isolated from single uterine cells, were barcoded and sequenced using inDROP. (B) t-SNE plot of unbiased clustering of uterine cells, where each color-coded cluster represents one cell type/state (only the main uterine parenchymal clusters are represented) (Figure 3—source data 1). (C) Schematic representation of the differential cellular composition of control and MIS-treated uteri. (D) t-SNE plot of unbiased clustering of uterine cells (dots) color-coded by treatment with CTL (orange) and MIS (blue) (Figure 3—source data 1). (E) Gene expression levels of representative cell-type-specific markers for each cluster overlaid on t-SNE plots (featureplot, color-coded arrow refers to cell type). (F) RNAish stains of representative cell-type markers in transverse uterine sections of empty vector control (CTL) and AAV9-MIS (MIS) treated mice at PND 6. Scale bars = 100 µm, same for all sections. Mouse tissues were used for validation purposes as the RNA in situ probes were readily available for mice and the effect of MIS was conserved among mice and rats. (G) Rat pups treated with AAV9-MIS (MIS) or empty vector (CTL) on PND 1 were euthanized at different developmental time points (PND3, 6, and 15), and their uteri were harvested for QPCR analysis of one representative marker for each cluster (n > 2, unpaired Student’s t test, mean ± SEM, *(p<0.05), **(p<0.01)) (Figure 3—source data 3).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Rat pups were treated with empty vector control (CTL) or AAV9-MIS (MIS) on PND1, and euthanized on PND 6 (n = 3 for both). t-SNE plot displaying the results of unbiased clustering of single uterine cells, where each color-coded cluster represents one cell type/state (all clusters included). Labels are as follows: 0: censored, 1: outer stroma, 2: myometrium, 3: inner stroma, 4: inhibited cluster, 5: luminal epithelium, 6: dividing cells, 7: vascular endothelium, 8: dividing epithelium, 9: mesothelium, 10: myeloid, 11: erythroid, 12: pericyte, 13: lymphatic endothelium, 14: neurons (Figure 3—source data 1). (B) t-SNE plot displaying the clustering of single uterine cells where each dot/cell is color-coded according to treatment, either CTL (orange) or MIS (blue) (all clusters included) (Figure 3—source data 1). (C) Relative percentage of representation of cells by clusters based on treatment (CTL, orange and MIS, blue) in the main parenchymal uterine cell types (only the main uterine cell types are shown in Figure 3B). (D) Gene expression levels of selected markers in the main parenchymal uterine cell types.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Heatmap of top five markers (showing top five genes by fold expression over average) amongst 14 different clusters (Figure 3—source data 1).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Violin plots of the top two marker genes revealed by highest p values (Figure 3—source data 1 and Table 1).

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** Rat pups were injected with empty vector control (CTL) or AAV9-MIS (MIS) on PND 1 and analyzed by scRNAseq at PND 6 (A–E). (A) Representative schema of the myometrial layer composition in control (orange) and MIS-treated (blue) uteri. (B) t-SNE plot of the myometrial cluster with cells labeled according to treatment. Note that both the CTL and the MIS-treated cells are numerically and spatially similarly represented in the t-SNE plot. (C) Heatmap of differentially expressed genes in CTL and MIS-treated myometrium (Figure 3—source data 2). (D) Sub-clustering of the myometrium cluster revealed three distinct myometrial sub-populations in the developing PND 6 rat uteri. (E) Specific markers for the three cell subtypes (outer, interstitial (microfibril enriched), and inner) of the developing rat myometrium.

The uterine horns of three control (treated with 5E10 empty vector particles/pup on PND1) and three AAV9-MIS-treated animals (treated with 5E10 particles/pup on PND1) were recovered at PND 6 and digested in a cocktail of proteases into single-cell suspensions (Figure 3A). The inDROP libraries were sequenced, demultiplexed, normalized, and analyzed using the Seurat package in ‘R’, as previously described (Butler et al., 2018). The processed sample of 9801 cells clustered into 15 groups: outer stroma (1494), inner stroma (1081), myometrium (1172), inhibited progenitor (946), luminal epithelium (898), dividing mesenchyme (750), vascular endothelium (535), dividing epithelium (314), mesothelial (313), myeloid (297), erythroid (155), pericyte (139), lymphatic endothelium (54), and nerve cells (33), along with a low-information cluster (high % of mitochondrial genes) which was censored from further analysis (1620) (Figure 3—figure supplement 1A–C, Figure 3—source data 1). Cell identity of each cluster was assigned based on the presence of previously reported cell-type markers using the top 15 significantly enriched genes (by adjusted p-value) of the single cell analysis, summarized in Table 1. Markers include Smoc2 (Mucenski et al., 2019) for stromal cells; Ptn (Mucenski et al., 2019) for myometrial cells; Epcam and Wnt7a (Litvinov et al., 1997) (Miller and Sassoon, 1998) for luminal epithelium cells; Top2a (Whitfield et al., 2006) for proliferating cells, Cdh5 (Bhasin et al., 2010) for vascular endothelial cells; Wnt7a and Hmgb2 for dividing epithelium (Miller and Sassoon, 1998) (Stros et al., 2009); Msln for mesothelium (Chang and Pastan, 1996); Csf1r (MacDonald et al., 2010) for myeloid cells (Zilionis et al., 2019); Alas2 (Kaneko et al., 2014) for erythroid cells; Mcam (Barron et al., 2016) for pericytes; Lyve1 (Hirakawa et al., 2003) for lymphatic endothelium; and Sox10 (Nonaka et al., 2008) (Zeisel et al., 2018) for neuronal cells (Table 1). A heatmap of the top five genes for each cluster (by fold expression over average) is also presented in (Figure 3—figure supplement 2). The top two markers generated from the heatmaps were also analyzed by violin plots among 14 different clusters (Figure 3—figure supplement 3).

Subsequent analyses focused on the five clusters representing the functional layers of the PND 6 uterus including luminal epithelium, myometrium, inner and outer endometrial stroma, and a unique cluster of cells responding to MIS treatment (inhibited progenitor) (Figure 3B and C). To validate the gene signatures of these clusters, and their changes in response to MIS treatment, we selected one marker gene (Figure 3—figure supplement 1D) for each unique cluster, and confirmed its cell-type-specific expression pattern in transverse uterine tissue sections of control as well as treated mice uteri at PND 6 by RNAish (Figure 3E and F). Endometrial stromal cells were found to have two transcriptionally distinct cell types: inner stroma (Bmp7+) and outer stroma (Wfikkn2+) (Figure 3B,C). Further subdivision of the myometrium cluster led to three distinct cell subtypes in the developing myometrial layer, all of which presented similar numbers of control and treated cells: inner myometrium (Myh11+), outer myometrium (Thbs2+), and interstitial (myofibril enriched) myometrium (Mfap5+) (Figure 3D–F, Figure 3—figure supplement 4, Figure 3—source data 2).

### MIS blocks the expansion and differentiation of an Misr2+ putative stromal progenitor

We next focused on differential gene expression in response to MIS treatment using our dataset of 6811 control and 2990 MIS-treated cells. In our cell atlas, the control and treated uterine cell datasets were of similar quality, and had comparable distributions of unique molecular identifiers (UMI) and gene numbers (Figure 3D, Figure 3—figure supplement 1B, Figure 3A). While both the epithelial (CTL 9.63%, MIS 8.06%) and the myometrial (CTL 11.98%, MIS 16.72%) (Figure 3—figure supplement 1B–C, Figure 3—figure supplement 4) cell types were re-presented in similar proportions in both datasets, ‘inner’ (CTL 18.68%, MIS 3.28%) and ‘outer’ (CTL 15.64%, MIS 0.27%) endometrial stroma clusters (Figure 3—figure supplement 1B–C) were almost entirely composed of control cells unlike the ‘inhibited progenitor’ cluster, which was unique to the MIS treatment (Figure 3B–D, Figure 3—figure supplement 1B–C, Figure 4A, Figure 4—figure supplement 1). Misr2 expression was enriched only in the inhibited progenitor cluster (Figure 3C–D, Figure 4A) as previously observed by RNAish (Figure 2E). MIS stimulation caused the sub-luminal inhibited progenitor cells to persist longer and induced overexpression of genes related to the bone morphogenic protein and transforming growth factor beta (BMP/TGFβ) signaling pathways (Smad6, Bambi), epigenetic markers (Hdac4), and, strikingly, to express ectopically smooth muscle (Thbs2) and epithelial (Msx2) markers, reflecting the multipotent characteristics of the early Mullerian progenitors (Figure 3E–G, Figure 4A, Figure 4—figure supplement 1A–D, Table 1). QPCR analysis of these ectopically expressed genes revealed that the large differences observed at PND 6 diminished with time, and became less pronounced by PND 15 (Figure 3G, Figure 4A, Figure 4—figure supplement 1; Figure 4—figure supplement 2; Figure 4—figure supplement 1B, Figure 3—source data 3).

![Figure 4.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig4-v2.jpg)

**Figure 4.:** (A) When treated with MIS, a unique population of Misr2+ subluminal putative progenitor cells are retained (inhibited progenitors), while the inner and the outer endometrial stromal layers fail to develop (representative scheme on the left). Note the differential expression pattern of stromal markers in the violin plots of the control and the MIS-treated uterine cells. See Figure 3 and Figure 4—figure supplements 1–3 for validation of these markers on tissue sections. (B) Diagrams of the unique receptor-ligand pairs present 1) between luminal epithelial cells and inner stromal cells (which are absent in MIS-treated uteri) (left), and 2) between the epithelial cells and the inhibited progenitor cells, (which are only present in the MIS-treated group).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Rat or mouse pups were injected with empty vector control (CTL) or with AAV9-MIS (MIS) on PND 1 and analyzed at different developmental time points (A–E). (A) Representative schema of the CTL and MIS-treated uteri at PND6. Note that the MIS-inhibited subluminal mesenchymal cell cluster (blue) is missing in the control uterus. (B) Control and MIS-treated mice uteri probed by RNAish using specific inhibited progenitor cluster markers at PND 6 (Misr2, Smad6, and Hdac4). Note that the Misr2+ cells reside in the subluminal space and express the anticipated markers identified by scRNAseq (shown by arrows in small inserts). Scale bars = 50 µm. (C) Expression pattern of Misr2, Smad6, and Hdac4 (markers for the MIS-inhibited cluster) in CTL and MIS treated cells on the t-SNE plots (FeaturePlot). Black arrows indicate the inhibited progenitor cells' cluster. (D) QPCR analysis of Misr2, Smad6, and Hdac4 in CTL (orange) and MIS-treated (blue) rat uteri at different developmental time points. (n > 2 for all time points, unpaired Student’s t test, mean ± SEM), *(p<0.05), **(p<0.01), (Figure 3—source data 3). (E) Cleaved-caspase-3 immunofluorescence (red) on ovarian (positive control), and MIS-treated rat uteri at PND 10. Note that only the MIS-treated subluminal cells (white arrows) are positive for cleaved caspase-3 on uterine sections. Scale bars = 50 µm.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Rat or mouse pups were injected with empty AAV9 vector control (CTL) or with AAV9-MIS (MIS) on PND 1 and analyzed at different time points (A–D). (A) Representative schema of the CTL and MIS-treated uteri at PND6. Note the absence of the endometrial stroma (orange) in the MIS-treated uteri. (B) Control and MIS-treated mice uteri probed by RNAish using specific endometrial stromal cluster markers at PND 6 (Cpxm2, Enpp2). Scale bars = 50 µm. (C) Expression pattern of Cpxm2, Enpp2, and Lipg (markers of endometrial stroma) in the uterine t-SNE plots (FeaturePlot). (D) QPCR analysis of Cpxm2, Enpp2 and Lipg in CTL and MIS-treated rat uteri at different developmental time points (PND3, 6, 15). (n > 2 for all time points, unpaired Student’s t test, mean ± SEM, *(p<0.05), **(p<0.01)) (Figure 3—source data 3). Note the endometrial stromal markers are significantly down-regulated in the MIS-treated uteri.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Rat or mouse pups were injected with empty vector control (CTL) or with AAV9-MIS (MIS) on PND 1 and analyzed at different time points (A–D). (A) Representative schema of the CTL (orange) and MIS-treated (blue) rat uteri at PND 6. (B) Immunofluorescence of Cdh1 on control and MIS-treated mouse uteri at PND6. Scale bars = 50 µm. (C) RNAish analysis of Cd24 (one of the top epithelial markers of Table 1) in control and MIS-treated rat uteri at PND6. Scale bars = 50 µm. (D) Cdh1, Cd24, and Klf5 expression pattern in t-SNE plots. Black arrows indicate the luminal epithelial cell cluster. (E) QPCR analysis of Klf5 in control and MIS-treated tissue. CTL (orange), MIS (blue). (F) Heatmap of differentially expressed genes in CTL and MIS-treated luminal epithelium (Figure 4—source data 2). (G) T-SNE plot of unbiased clustering of uterine luminal epithelial cells (dots) color-coded by treatment with CTL (orange) and MIS (blue). Note that the CTL and MIS-treated cells have distinctive sub-clustering pattern. (H) Further analysis of the commonly (Cdh1, Cd24, and Klf5) and differentially (Id3, Acsm3, and Msx2) expressed luminal epithelial genes from the T-SNE plots. (I) Id3 expression pattern by RNAish in control and MIS-treated uteri. Dotted lines demarcate the luminal epithelium. Scale bars = 50 µm.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** (A) Overview of ligand–receptor interactions in the PDN6 rat uteri was generated using scRNAseq data, which was extrapolated to protein-protein interactions using the CellPhoneDB algorithm. P-values indicated by circle size (see legend on right) and average gene expression values are indicated by blue color (see legend on right) (Figure 4—source data 1).

**Table 1.**
 Unique gene signatures of the 14 different cell types (clusters) from the developing rat uteri on PND 6.Gene markers revealed by single cell RNA sequencing, sorted by highest adjusted p-value with positive LogFc (Figure 3—source data 1). Clusters identities were assigned to different cell types by RNAish validation and/or manual literature review. Top 15 markers, citations, and associations are listed in the table. Selected markers were further validated in Figure 3.


<table>
  <thead>
    <tr>
      <th>Outer stroma (1)</th>
      <th>Myometrium (2)</th>
      <th>Inner stroma (3)</th>
      <th>Inhibited Progenitor (4)</th>
      <th>Epithelium (5)</th>
      <th>Proliferating cells (6)</th>
      <th>Vascular endothelium (7)</th>
      <th>Dividing epithelium (8)</th>
      <th>Mesothelium (9)</th>
      <th>Myeloid (10)</th>
      <th>Erythroid (11)</th>
      <th>Pericyte (12)</th>
      <th>Lymphatic endothelium (13)</th>
      <th>Neuronal (14)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RGD1305645</td>
      <td>Lum</td>
      <td>Nrgn</td>
      <td>AC109891.2</td>
      <td>Cd24 **</td>
      <td>Hmgb2</td>
      <td>Cd93 *</td>
      <td>Epcam * (Litvinov et al., 1997)</td>
      <td>Bsg</td>
      <td>Fcer1g *</td>
      <td>Hba.a1 *</td>
      <td>Mgp *</td>
      <td>Ccl21</td>
      <td>Plp1 *</td>
    </tr>
    <tr>
      <td>Smoc2 * (Mucenski et al., 2019)</td>
      <td>Postn</td>
      <td>Cpxm2 **</td>
      <td>Rn60_1_221 6.1</td>
      <td>Epcam * (Litvinov et al., 1997)</td>
      <td>Stmn1 *</td>
      <td>Cdh5 ** (Bhasin et al., 2010)</td>
      <td>Cldn3</td>
      <td>Upk1b *</td>
      <td>Tyrobp *</td>
      <td>Hba.a2 *</td>
      <td>Mcam ** (Barron et al., 2016)</td>
      <td>Mmrn1 **</td>
      <td>Sox10 * (Nonaka et al., 2008)</td>
    </tr>
    <tr>
      <td>Dpt *</td>
      <td>NEWGENE_ 621351</td>
      <td>Tgfbi *</td>
      <td>AABR070687 05.1</td>
      <td>Wfdc2 * (Mucenski et al., 2019)</td>
      <td>Top2a * (Whitfield et al., 2006)</td>
      <td>RGD1310587</td>
      <td>Cd24 *</td>
      <td>Msln ** (Chang and Pastan, 1996)</td>
      <td>Csf1r ** (MacDonald et al., 2010)</td>
      <td>LOC1036948 57</td>
      <td>Rergl *</td>
      <td>Lyve1** (Hirakawa et al., 2003)</td>
      <td>Gfra3 *</td>
    </tr>
    <tr>
      <td>Cpe</td>
      <td>Col1a1</td>
      <td>Plac8</td>
      <td>Fgfr2</td>
      <td>Wnt7a * (Miller and Sassoon, 1998)</td>
      <td>Mki67 * (Whitfield et al., 2006)</td>
      <td>Emcn *</td>
      <td>Cdh1 *</td>
      <td>Fmod</td>
      <td>Lyz2 *</td>
      <td>Hbb *</td>
      <td>Eln *</td>
      <td>Flt4 ** (Hirakawa et al., 2003)</td>
      <td>Abca8a</td>
    </tr>
    <tr>
      <td>Vcan *</td>
      <td>Ptn * (Mucenski et al., 2019)</td>
      <td>Vcan *</td>
      <td>Unc5b * (Mullen et al., 2018)</td>
      <td>Cldn3</td>
      <td>Tubb5 *</td>
      <td>Tie1 *</td>
      <td>Klf5</td>
      <td>Cav1</td>
      <td>Ftl1</td>
      <td>LOC1036948 55</td>
      <td>Col4a1 *</td>
      <td>Cldn5 *</td>
      <td>Egfl8</td>
    </tr>
    <tr>
      <td>Dcn *</td>
      <td>Thbs2 **</td>
      <td>Fn1 *</td>
      <td>Ugt1a2</td>
      <td>Krt8 *</td>
      <td>LOC1003595 39</td>
      <td>Plvap</td>
      <td>Krt8 *</td>
      <td>Dpp4 *</td>
      <td>Cybb *</td>
      <td>Alas2 * (Kaneko et al., 2014)</td>
      <td>Igfbp7 *</td>
      <td>Fgl2 *</td>
      <td>Cdh19</td>
    </tr>
    <tr>
      <td>Col4a5 *</td>
      <td>Col3a1</td>
      <td>Apcdd1</td>
      <td>Bambi ** (Mullen et al., 2018)</td>
      <td>Cdh1 *</td>
      <td>Racgap1</td>
      <td>Cav1</td>
      <td>Mt1</td>
      <td>Anxa3</td>
      <td>Laptm5 *</td>
      <td>Ybx3 *</td>
      <td>Cspg4 **</td>
      <td>Klhl4 *</td>
      <td>Afap1l2</td>
    </tr>
    <tr>
      <td>Apoe</td>
      <td>Ogn (Mucenski et al., 2019)</td>
      <td>Cdh11 *</td>
      <td>Srgn</td>
      <td>Tacstd2</td>
      <td>LOC1003603 16</td>
      <td>Adgrl4</td>
      <td>Wnt7a * (Miller and Sassoon, 1998)</td>
      <td>Igfbp6</td>
      <td>Tmsb4x</td>
      <td>Hba.a3 *</td>
      <td>Abcc9 *</td>
      <td>Cdh5 *</td>
      <td>L1cam *</td>
    </tr>
    <tr>
      <td>Osr2</td>
      <td>Sparc</td>
      <td>Col6a3 *</td>
      <td>Kcnk3</td>
      <td>Cldn4 *</td>
      <td>Prc1 *</td>
      <td>Plxnd1</td>
      <td>Mt2A</td>
      <td>Cfb</td>
      <td>Ctsb *</td>
      <td>Alox15</td>
      <td>Epas1</td>
      <td>Tbx1</td>
      <td>Col5a3</td>
    </tr>
    <tr>
      <td>Tnfrsf21</td>
      <td>Cxcl12</td>
      <td>Tnfrsf21</td>
      <td>Igfbp5</td>
      <td>Msx1</td>
      <td>Cdk1 *</td>
      <td>Epas1 *</td>
      <td>Msx1</td>
      <td>Lox</td>
      <td>Lcp1 *</td>
      <td>Car2</td>
      <td>Rgs5</td>
      <td>Slc45a3</td>
      <td>Olfml2a</td>
    </tr>
    <tr>
      <td>Adamts7</td>
      <td>Igfbp5</td>
      <td>Nkd2</td>
      <td>Igf2r</td>
      <td>Klf5</td>
      <td>Depdc1</td>
      <td>Esam *</td>
      <td>Wfdc2</td>
      <td>Muc16 *</td>
      <td>Ptprc *</td>
      <td>Ahsp *</td>
      <td>Foxs1 *</td>
      <td>Adgrg3</td>
      <td>Metrn</td>
    </tr>
    <tr>
      <td>Slc26a7</td>
      <td>Ccdc80</td>
      <td>Axin2</td>
      <td>Plac8</td>
      <td>Elf3 *</td>
      <td>Smc2</td>
      <td>Cyyr1</td>
      <td>Dlx5</td>
      <td>Itm2a</td>
      <td>C1qa *</td>
      <td>Rbm38</td>
      <td>Myl9</td>
      <td>Sdpr</td>
      <td>Mpz *</td>
    </tr>
    <tr>
      <td>Wfikkn2 **</td>
      <td>Gpc3</td>
      <td>Vim *</td>
      <td>Prrx2</td>
      <td>Dlx5</td>
      <td>Kif11 *</td>
      <td>Clec14a</td>
      <td>Sbspon</td>
      <td>Sema3c</td>
      <td>C1qc *</td>
      <td>Lgals5</td>
      <td>RGD1564664</td>
      <td>LOC1009120 34</td>
      <td>Plekha4</td>
    </tr>
    <tr>
      <td>Col6a3 *</td>
      <td>Igsf10</td>
      <td>Col6a2 *</td>
      <td>Alpl</td>
      <td>Aldh2</td>
      <td>Cenpf *</td>
      <td>Adgrf5</td>
      <td>Hmgb2 ** (Stros et al., 2009)</td>
      <td>Fbln2 *</td>
      <td>Aif1 *</td>
      <td>Slc4a1</td>
      <td>Acta2 *</td>
      <td>Rn50_1_043 5.2</td>
      <td>Dbi</td>
    </tr>
    <tr>
      <td>Islr</td>
      <td>Itm2a *</td>
      <td></td>
      <td>AABR070253 16.1</td>
      <td>Mt2</td>
      <td>Tmpo *</td>
      <td>Col3a1</td>
      <td>Tacstd2</td>
      <td>Eln</td>
      <td>Cxcl2</td>
      <td>Slc25a39</td>
      <td>Cald1 *</td>
      <td>Il2rg</td>
      <td>Col20a1</td>
    </tr>
    <tr>
      <td>* extracellular matrix, collagen or cytoskeleton related **validated new marker (in uterus)</td>
      <td>* muscle related **validated new marker (in uterus)</td>
      <td>*extracellular matrix, collagen or cytoskeleton related **validated new marker (in uterus)</td>
      <td>*implicated during Mullerian duct regression in males ** validated new marker (in uterus)</td>
      <td>*epithelium associated **validated new marker (in uterus)</td>
      <td>*cell cycle or proliferation associated</td>
      <td>*endothelial related **implicated higher expression in vascular tissues</td>
      <td>*epithelium associated **cell proliferation associated</td>
      <td>*mesothelium associated or enriched **mesothelium specific</td>
      <td>* myeloid associated (Zilionis et al., 2019) **myeloid specific</td>
      <td>*hemoglobin associated</td>
      <td>* fibroblast associated **pericyte marker</td>
      <td>*endothelial related ** lymphatic endothelium associated</td>
      <td>*neuronal related (Zeisel et al., 2018)</td>
    </tr>
  </tbody>
</table>

Cleaved caspase-3 histological staining of the MIS-treated uteri confirmed that the inhibited progenitor cells underwent apoptosis at approximately 9 days after treatment, whereas normally developing endometrial stromal cells were negative for the apoptotic marker (Figure 4—figure supplement 1E). QPCR and RNAish validation of differentially expressed genes in the stroma confirmed that both Wfikkn2 (‘outer stroma’), Bmp7 (‘inner stroma’) failed to be induced over time in the MIS treated group (Figure 3G), along with other markers such as Cpxm2 and Enpp2 (Figure 4—figure supplement 3A–D), consistent with the hypothesis that MIS prevented the subluminal progenitor cells from undergoing stromal specification and amplification; instead they eventually underwent apoptosis (Figure 4—figure supplement 1E).

### MIS disrupts gene expression in the luminal epithelium in a non-cell-autonomous manner

Our results indicate that neonatal exposure to MIS induces changes in gene expression in the epithelial cell cluster as visible by the shifted treatment population in the t-SNE plot (Figure 3D, Figure 3—figure supplement 1B, Figure 4—figure supplement 4A). Even though expression of the basic luminal epithelial cell markers were not significantly different between control and MIS-treated cells (Ecad, Cd24, and Klf5) (Figure 4—figure supplement 4 (A-E), differential gene expression analysis of the epithelial cluster based on treatment (CTL and MIS) revealed gene candidates whose expressionwas significatly changed by MIS treatment (Figure 4—figure supplement 4F–I) despite the lack of Misr2 expression in epithelial cells (Figure 1A,E). We confirmed that Id3 was downregulated in the MIS-treated epithelial cells (Figure 4—figure supplement 4H). Another intriguing gene expression pattern in response to MIS treatment was the downregulation of the epithelial cell marker Msx2 at PND6, which coincides with its ectopic expression in the inhibited putative progenitor (Figure 3F–G (Msx2), Figure 4A, Figure 4—figure supplement 4F). These results are consistent with MIS mediating the indirect repression of epithelial Msx2 and Id3 through paracrine signals emanating from the Misr2+ mesenchymal cells, or the lack of normal endometrial stromal signals, which in turn may prevent subsequent endometrial gland formation at later time points (Figure 4—figure supplement 4I, Figure 2—figure supplement 1A–D).

Finally, to survey the paracrine signaling between the inner stroma and epithelium and catalog how it may be disrupted by MIS treatment (inhibited putative progenitor and epithelium), we performed a comprehensive ligand/receptor analysis using the CellPhoneDB algorithm (Vento-Tormo et al., 2018) (Figure 4B- Figure 4—figure supplement 4, Figure 4—source data 1). Briefly, significantly expressed ligand/receptor pairs were systematically cataloged between each functional cell types (Figure 4B), revealing important developmental pathways dysregulated in MIS-treated uteri, such as Wnt and Igf2 signaling (Figure 4B, Figure 4—figure supplement 4, Figure 4—source data 1).

### Misr2+ putative progenitors are necessary for uterine development and fertility only during the first 6 days of life

The timing of expression of Misr2 in the subluminal mesenchyme led us to hypothesize that limiting exposure to MIS during only the first 6 days of development could be sufficient to explain the observed long-term uterine hypoplasia. To test this hypothesis, we treated rat pups with recombinant MIS protein (rhMIS) during 6 days intervals (3 mg/kg) starting from days 1, 6, or 11 (Figure 5A). Consistent with this hypothesis, only when rats were treated during PND1-6 period were the uteri smaller than controls, at PND6, 20, 45, and even up to 8 months (Figure 5B,C,G). In contrast, when rhMIS was administered starting from PND6 or PND11, uterine hypoplasia was muted or absent, suggesting a narrow window of susceptibility with long-lasting consequences (Figure 5B). Therefore, only perinatal (PND1-6) administration of rhMIS completely phenocopied the continuous exposure phenotypes observed with AAV9-MIS, including lower percentage of endometrial stromal cells, smaller luminal ducts, and absence of glandular development (Figure 5B, Figure 5—figure supplement 1A) as confirmed by downregulation of Foxa2 expression and absence of glandular ducts (Figure 5D–E). Strikingly, this 6-day postnatal treatment was also sufficient to cause complete infertility later in adulthood (n = 3 per group, p<0.05) (Figure 5F). Analysis of the control and the 6-day rhMIS-treated uteri at a later time point (8 months) confirmed that the profound endometrial stromal hypoplasia persists in the adult (Figure 5G–H). In contrast, the ovaries fully recover from the short MIS inhibition of folliculogenesis (PND1-6) and display normal ovarian sizes and follicular composition at this timepoint (Figure 5H).

![Figure 5.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig5-v2.jpg)

**Figure 5.:** (A) Rat pups were injected daily with recombinant MIS protein (3 mg/kg) (MIS), or saline control (CTL), from PND1-6, PND6-11, or PND11-17. (B) Uterine morphology was analyzed on PND45 with H and E stained transverse sections (n > 2). Scale bars are 100 µm. (C) Total uterus area, the percentage of the endometrial area, and the luminal duct height in CTL and MIS-treated (from PND1-6) were compared at PND20 and 45. (D) Foxa2 immunofluorescence (red) on CTL and MIS-treated uteri (from PND1-6) was analyzed at PND20. Scale bars = 50 µm. (for C and D: for PND20, n = 2 for control, n = 3 for MIS; for PND45, n = 2 both for control and MIS, mean ± SEM, unpaired Student’s t test * (p<0.05), ** (p<0.01)). (E) Endometrial gland counts were compared in CTL and MIS-treated uteri (from PND1-6) at PND20 and 45 from H and E sections. (F) Cumulative pups per females in 3 months continuous mating studies of the control and MIS-treated rat uteri. (n = 3 both for the control and the treated, unpaired Student’s t test mean ± SEM, * (p<0.05), *** (p<0.001)). (G) Gross morphology of the CTL and the MIS-treated (PND1-6) uteri at 8 months of age. Scale bar = 0.5 cm. (H) Uterine transverse sections (top) and ovaries (bottom) of the control and MIS-treated rats at 8 months of age. CL stands for corpus luteum. Scale bars = 100 µm.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Rat pups were treated with recombinant MIS protein daily from PND1-6 and their uteri were analyzed on PND20, showing evidence of hypoplasia and absence of endometrial glands. (B) Rat pups were treated with empty vector control (CTL) or with AAV9-MIS (MIS) on PND1. Estradiol (left) and progesterone (right) serum levels from CTL and MIS-treated rats at different developmental time points (PND3, 5, 6, 10, 15, 30) (n > 2 both for the control and treated serum). (C) Rat pups were treated with recombinant MIS protein (or vehicle control) from PND1-6, to examine gross ovarian morphology, and (D) ovarian histology from H and E sections at PND 20 and PND45. Scale bars = 50 µm.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Rat pups were gonadectomized on PND 2, and treated with empty vector (CTL) or AAV9-MIS (MIS) 6 hr after surgery. Gonadectomized (GDX) rats were sacrificed on PND 10 (n = 2 for each). (B) Representative transverse uterine section stained by H&E (left column) and Misr2 expression pattern by RNAish (right column) from GDX animals subsequently treated with CTL or MIS and analyzed at PND10. Scale bars = 100 µm. (C) Misr2cre/+ knock in cre recombinase bearing males and females were crossed to generate Misr2cre/cre mice, which are deficient in MISR2 (Misr2-/-). Mouse pups were injected with AAV9-MIS on PND 1, and euthanized on PND 20, and genotype was confirmed. (D) Transverse sections of the uteri of AAV9-MIS treated Mirs2+/-(Mirs2+/cre) heterozygous and Misr2-/- (Misr2cre/cre) homozygous mice were analyzed by H&E on PND 20. Note that the AAV9-MIS treated-Misr2-/- uteri do not present with hypoplasia. Scale bars = 100 µm.

The impaired uterine development and infertility is unlikely to be secondary to ovarian suppression since folliculogenesis only starts reaching early pre-antral stages by PND6, and MIS treatment appears to have little effect on steroid hormones (E2 and P4) during that time (Figure 5—figure supplement 1B). Furthermore, as previously described (Kano et al., 2017), MIS inhibition of folliculogenesis by rhMIS is reversible, and while the MIS-treated PND1-6 ovaries showed an initial delay in folliculogenesis at early timepoints (PND 20), it was resolved by PND 45 confirming no lasting impact on ovarian function (Figure 5—figure supplement 1C–D).

To confirm that the effect of MIS on the Misr2+ putative stromal progenitor was intrinsic to the uterus (and not the ovary), we treated gonadectomized rat pups with control or AAV9-MIS on PND2 (Figure 5—figure supplement 2A,B), which resulted in the same uterine hypoplasia phenotype by PND 10 (Figure 1C). Finally, to confirm that the signaling in the ‘inhibited progenitor’ was dependent on the canonical MIS receptor, we treated Misr2-deficient female mice (Misr2-/-) with AAV9-MIS, which failed to recapitulate the uterine hypoplasia phenotype (Figure 5—figure supplement 2B,C). Together, these results revealed a cell-autonomous effect of MIS in the subluminal mesenchyme, intrinsic to the uterus, and dependent on Misr2, in which progenitors normally specified to form endometrial stromal layers at PND1-6 are inhibited by MIS, leading to long-term infertility.

### MISR2+ subluminal mesenchymal cells are transiently present in the developing embryonic human uterus

We sought to determine whether uterine subluminal mesenchymal cells expressing MISR2 are also present in the human female fetus preceding production of the ligand (MIS) by the ovary. We used paraffin-embedded archival tissue of human female reproductive tract from fetuses ranging from 22 weeks (wk) to 37 weeks of gestation. Using the adjacent fetal ovary tissue as a positive control for MISR2 RNAish, we analyzed the uterus at different developmental stages, revealing a spatiotemporal pattern of expression strikingly similar to that of the rodents (Figure 6A–C). MISR2+ cells were present in the same location in the fetal uterus, directly adjacent to the lumen at 22 weeks of gestation and receded at later timepoints (24wk, 37wk), coinciding with the production of MIS by the human ovary, which is thought to begin at 24 weeks of gestation (Kuiri-Hänninen et al., 2011). To determine if candidate genes suspected to cause Mullerian aplasia or hypoplasia in humans (Nik-Zainal et al., 2011) may be present in the developing rat uterus, we analyzed their expression in our cell atlas, revealing the enrichment of several candidates within the ‘inhibited progenitor’ cluster (Figure 6D).

![Figure 6.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig6-v2.jpg)

**Figure 6.:** (A) The MISR2 expression pattern in human fetal uteri was analyzed by RNAish in fixed tissue sections. First row consists of stitched images of human fetal uteri at embryonic weeks 20, 22, and 37 (approximately 60 images (20x objective) per developmental time point were used for stitching). Middle-row panels show a higher magnification image for each subsequent time point. Red dots (MISR2 transcripts) were quantified using the Keyence BZ-X800 analysis software. Software-enhanced red dots in the bottom-row panels show the quantified region by the automated system. Scale bars = 25 µm (B) MISR2 transcripts were quantified per cell area from five random sections of 20, 22 weeks, and 37 weeks fetal tissue. (unpaired Student t-test, five section per one sample, per time point, **(p<0.01)). (C) Adjacent human fetal ovaries were used as internal positive controls for the MISR2 RNAish analysis. Black arrowheads indicate granulosa cells from primordial follicles positive for MISR2 transcripts. Scale bars = 25 µm. (D) Candidate genes of Mullerian aplasia in humans have enriched expression in the ‘inhibited progenitor’ cluster (black arrows) from the t-SNE plots of scRNAseq in rats.

## Discussion

Single-cell RNA sequencing of the PND6 uterus revealed that the subluminal Mullerian duct mesenchyme contains a previously uncharacterized cell type (Figure 7) that plays a crucial role in the specification of the endometrial stroma during neonatal uterine development. We hypothesize that these Misr2+ cells represent stromal progenitors, which normally gives rise to the inner and outer endometrial stromal layer around PND6 in mice and rats (Figure 1B). Surprisingly, these Misr2+ putative stromal progenitors retain sensitivity to inhibition by MIS postnatally, and can be reprogrammed to undergo apoptosis instead of developing into the endometrial stromal layers if exposed to MIS (Figure 7).

![Figure 7.](https://cdn.elifesciences.org/articles/46349/elife-46349-fig7-v2.jpg)

**Figure 7.:** Mullerian inhibiting substance receptor-2 is expressed in a specific subluminal mesenchymal cell type surrounding the Mullerian duct epithelium during early fetal urogenital ridge development of both sexes. In male embryos, secretion of MIS, the ligand of Misr2, by the embryonic testes causes the Misr2+ mesenchymal cell to trigger regression of the Mullerian duct epithelium. In the female, the Misr2+ mesenchymal cells persist postnatally, and give rise to the endometrial stromal layers of the adult uterus. If females are exposed to MIS during the first week of uterus development, these subluminal progenitor cells can be reprogrammed to undergo apoptosis instead of developing into the endometrial stromal layers, resulting in uterine hypoplasia and future infertility.

Although postnatal MIS exposure is no longer able to induce regression of the uterine luminal epithelium, its normal function in male fetuses (Jost, 1947), it does irreversibly block its ability to form endometrial epithelial glands. We speculate that this retained sensitivity to MIS in the female may be a vestigial pathway of the male, which is normally silenced in females prior to the emergence of secretion of MIS by the ovary. However, it is unlikely that MIS itself is an important developmental trigger regulating endometrial stroma development, since the uterus develops normally in both Mis and Misr2 knockout mice (Behringer et al., 1994)(Mishina et al., 1999) (Mishina et al., 1999).

The postnatal response of the Misr2+ putative progenitors to MIS provides some unique insights into the developmental pathways elicited during fetal Mullerian duct regression. The nascent fetal Mullerian duct is mesoepithelial in origin, being derived from the invagination of the coelomic epithelium, and begins further differentiation into epithelium proper coincidentally with the timing of regression. Others have suggested that this epithelial differentiation may subsequently restrict the ability of the ductal cells to undergo the epithelial to mesenchymal transition characteristic of ductal regression (Allard et al., 2000). This raises the possibility that the Misr2+ mesenchyme in the neonatal female may be responding to MIS similarly to male urogenital mesenchyme, but that the neonatal epithelium is unable to regress in response to those signals. Supporting this interpretation of recapitulated mesenchymal regression is the ectopic expression of many of the same genes and pathways previously identified in the regressing male fetal Mullerian duct (Bambi, Smad6, Wif1, etc.) (Mullen et al., 2018).

Even though gain of function MIS or MISR2 mutations have not been reported in women with Mullerian anomalies, the uterine hypoplasia observed in the present study is suggestive of Mayer-Rokitansky-Küster-Hauser syndrome (MRKH), also known as Mullerian aplasia which affects 1 in 4500 women (Nik-Zainal et al., 2011). Genes expressed in the Misr2+ putative progenitor cells in response to MIS treatment likely represent either pathways of Mullerian duct regression or of uterine endometrial stroma progenitor development. Therefore, we speculate that the markers described herein may represent candidate genes underlying developmental disorders of the Mullerian duct. Efforts to identify causative genes within regions of copy number variation in patients affected with Mullerian aplasia have turned up candidate genes such as KHDRBS2, and GFRA1 (Nik-Zainal et al., 2011), which we see uniquely expressed in the ‘inhibited progenitor’ cluster (Figure 6D). Similarly, both Gata3 which causes hypoparathyroidism, sensorineural deafness, renal anomaly (HDR) syndrome with uterine hypoplasia (Van Esch et al., 2000) and Fgfr2, which causes disorders of sexual dimorphism in males (Bagheri-Fam et al., 2015; Barseghyan et al., 2018), and decidualization defects in females (Filant et al., 2014), are highly expressed in the inhibited MISR2+ progenitors (Figure 6D).

The importance of the endometrial stroma in the formation of endometrial glands and fertility has been demonstrated in multiple mouse models such as Wnt4 mutant mice, and neonatal diethylsilbesterol (DES) treatments, both of which carry phenotypes of endometrial glandular dysplasia also observed in our rodents with postnatal exposure to MIS (Herbst et al., 1980; Medlock et al., 1988; Hayashi et al., 2011; Prunskaite-Hyyryläinen et al., 2016). These mouse models display endometrial stromal hypoplasia, which precludes glandular development as a result of the disruption of Wnt pathways and the communication between stromal and epithelial compartments. Our single-cell transcriptomic analysis identified distinct inner and outer endometrial stromal layers with molecular signatures that might presage specialized stromal functions, such as regulation of the adjacent epithelium or myometrium. A comprehensive characterization of such paracrine signals across the cell types of our control and MIS-treated uterine atlases using the CellPhoneDB algorithm (Vento-Tormo et al., 2018) revealed the immense complexity of those cellular interactions, and their dysregulation by MIS (e.g. Wnt signaling, Figure 4B). MIS treatment is likely especially disruptive to the interaction between the inner endometrial stroma and adjacent luminal epithelium, as seen by the absence of expression of Bmp7, and coincidental downregulation of Msx2 in those cell types, respectively, which have been previously implicated in the coordination of endometrial gland formation in the uterus (Phippard et al., 1996; Kodama et al., 2010; Yin et al., 2015) and decidualization defects (Daikoku et al., 2011; Monsivais et al., 2017). The nature of the paracrine signals emanating from the inner stroma regulating epithelial development, and their dysregulation during MIS treatment, including the ephrin, notch, Igf, Tnf, Mdk/Ptn, Tyro3, and Fn1 pathways (Figure 3, Figure 3—figure supplement 4), should be systematically investigated in future studies.

Furthermore, the involvement of premature exposure of the developing Mullerian ducts to MIS in disorders of sexual differentiation of the female is not fully appreciated (Chen et al., 2014; Van Batavia and Kolon, 2016). Moreover, the recent identification of an Misr2+ subepithelial adult endometrial stem cell suggests that some neonatal endometrial stromal sprogenitor may persist into adulthood, where they could play a role in endometrial homeostasis and repair (Yin et al., 2019). Interestingly, we have recently reported an increased incidence of preterm birth in PCOS patients with high circulating MIS (Hsu et al., 2018) raising the possibility of a causative link between high MIS exposure and uterine dysfunction. Conversely, the complete infertility resulting from a short treatment with MIS could have useful applications in the veterinary settings where it may be used as a permanent contraceptive that does not affect ovarian function (Hay et al., 2018).

Finally, given our findings that MIS is a potent inhibitor of MISR2+ putative endometrial stromal progenitors during uterine development, and that this cell type is likely also active in fetal human uteri, it would be of interest to explore possible clinical applications of MIS, or related pathways, in the context of Mullerian development pathologies, uterine infertilities, and endometrial stromal cancers, should these pathways become reactivated in those tumors (Chiang and Oliva, 2013).

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
      <td>Genetic reagent (M. muculus)</td>
      <td>B6;129S7-Amhr2tm3(cre)Bhr/Mmnc</td>
      <td>PMID: 12368913</td>
      <td>RRID_MGI:3042214</td>
      <td>Dr. Richard R Behringer, MD Anderson Cancer Center</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. muculus)</td>
      <td>C57BL/6-Tg(UBC-GFP)30Scha/J</td>
      <td>Jackson Laboratory</td>
      <td>stock #004353</td>
      <td>Hongkui Zeng, Allen Institute for Brain Science</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. muculus)</td>
      <td>FVB/NCrl</td>
      <td>Charles River</td>
      <td>#207</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Rat)</td>
      <td>Sprague Dawley</td>
      <td>Envigo</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>LR-MIS</td>
      <td>(Pépin et al., 2013)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>AAV9-LRMIS</td>
      <td>(Pépin et al., 2015)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Smooth muscle alpha action (SMA) (Rabbit polyclonal)</td>
      <td>Abcam</td>
      <td>#5694</td>
      <td>(1:300), IF</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Vimentin (rabbit monoclonal)</td>
      <td>Abcam</td>
      <td>#92547</td>
      <td>(1:300), IF</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Foxa2 (rabbit polyclonal)</td>
      <td>LifeSpan Biosciences</td>
      <td>#138006</td>
      <td>(1:500), IF</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Cleaved caspase-3 (rabbit polyclonal)</td>
      <td>Cell signaling</td>
      <td>#9661S</td>
      <td>(1:200), IF; (1:500) IHC</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>E-cadherin (Cdh1) (rat monoclonal)</td>
      <td>Invitrogen</td>
      <td>#13–1900</td>
      <td>(1:200), IF</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa flour 488 donkey anti rat IgG</td>
      <td>Invitrogen</td>
      <td>#A21208</td>
      <td>(1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa flour 555 donkey anti rabbit IgG</td>
      <td>Invitrogen</td>
      <td>#A31572</td>
      <td>(1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa flour 568 anti rabbit IgG</td>
      <td>Invitrogen</td>
      <td>#A10042</td>
      <td>(1:500)</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNA scope 2.5 HD red detection kit</td>
      <td>ACD bio</td>
      <td>#322360</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>the target retrieval and protease plus reagents</td>
      <td>ACD bio</td>
      <td>#322330</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MIS commercial ELISA</td>
      <td>Beckmen</td>
      <td>#A73818</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>REDExtract-N-Amp Tissue PCR Kit</td>
      <td>Sigma</td>
      <td>#SLBT8193</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Bambi (M. muculus) (NM_026505.2)</td>
      <td>ACD bio</td>
      <td>#523071</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Bmp7 (M. muculus) (NM_007557.3)</td>
      <td>ACD bio</td>
      <td>#407901</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>CD24a (M. muculus) (NM_009846.2)</td>
      <td>ACD bio</td>
      <td># 432691</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Cpxm2 (M. muculus) (NM_018867.5)</td>
      <td>ACD bio</td>
      <td># 559759</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Enpp2 (M. muculus) (NM_001136077.1)</td>
      <td>ACD bio</td>
      <td># 402441</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Hdac4 (M. muculus) (NM_207225.1)</td>
      <td>ACD bio</td>
      <td># 416591</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Misr2 (Amhr2) (M. muculus) (NM_144547.2)</td>
      <td>ACD bio</td>
      <td># 489821</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Misr2 (Amhr2) (Rat) (NM_030998.1)</td>
      <td>ACD bio</td>
      <td># 517791</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Misr2 (Amhr2) (Human) (NM_020547.2)</td>
      <td>ACD bio</td>
      <td># 490241</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Msx2 (M. muculus) (NM_013601.2)</td>
      <td>ACD bio</td>
      <td># 421851</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Myh 11 (M. muculus) (NM_001161775.1)</td>
      <td>ACD bio</td>
      <td># 316101</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Smad6 (M. muculus and Rat) (NM_001109002.2)</td>
      <td>ACD bio</td>
      <td># 517781</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Thbs2 (M. muculus) (NM_011581.3)</td>
      <td>ACD bio</td>
      <td># 492681</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Wfikkn2 (M. muculus)</td>
      <td>ACD bio</td>
      <td># 531321</td>
      <td>commercial probe</td>
    </tr>
    <tr>
      <td>Software, algoritm</td>
      <td>R</td>
      <td>R Project for Statistical Computing</td>
      <td>https://scicrunch.org/resolver/SCR_001905</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algoritm</td>
      <td>BZ-X800 analysis software</td>
      <td>Keyence</td>
      <td>https://www.keyence.com/landing/microscope/lp_fluorescence.jsp</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algoritm</td>
      <td>GraphPad Prism, version 7</td>
      <td>Graphpah</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Animals

This study was performed in accordance with experimental protocols 2009N000033 and 2014N000275 approved by the Massachusetts General Hospital Institutional Animal Care and Use Committee. Strains of Sprague–Dawley (purchased from Envingo) and Friend leukemia virus B (FVB) (purchased from Charles River Laboratories) were used for rat and mouse experiments, respectively. Misr2/Amhr2-Cre knock-in mice were purchased from the Mutant Mouse Regional Resource Centers (MMRRC) (strain B6;129S7-Amhr2tm3(cre)Bhr/Mmnc, backcrossed with C57BL/6J) (Jamin et al., 2002). Tail genotyping of the Misr2-cre knock-in and WT mice were done with REDExtract-N-Amp Tissue PCR Kit (Sigma, #SLBT8193) with the previously described sets of primers (Jamin et al., 2002).

### AAV9-MIS and recombinant protein treatment

The adeno-associated virus serotype 9 (AAV9) gene therapy vector was used for sustained delivery of a higher concentration of human MIS analog (LR-MIS) as described (Pépin et al., 2015). To test the effect of continuous MIS exposure on uteri, rats or mice were injected subcutaneously with AAV9-recombinant human LR or RF MIS (AAV9-MIS) on postnatal day 1, and their uteri were harvested at different time points for histological analysis (5E10 particles/pup). Blood was collected by cardiac puncture at endpoint, and centrifuged at 900 × g for 10 min at room temperature from control and AAV9-MIS-treated female rat pups on PND3, 5, 6, 10, 15, and 30 (n > 2). To validate the RNA scope markers on tissue sections, mice were injected with AAV9-MIS on PND 1 (1E10 particles/pup), and sacrificed on PND 6 (n = 3 both for the control and the treated). For each time point, the uteri were cut radially in halves. One half was fixed in formalin for histological analysis and immunohistochemistry, the other half was flash-frozen for RNA isolation and qPCR analyses. In mice, the paraffin-embedded fixed tissue was sectioned for RNAish analysis, while in rats it was used for histomorphological analyses.

To test the window of sensitivity to exogenous MIS during uterus development, rats were injected subcutaneously with a human recombinant MIS (LR-MIS) protein (Pépin et al., 2013) daily (3 mg/kg/day) for 6 days starting from PND1-6, PND6-11, or PND11-17 (Figure 5A). Uteri of rat pups injected from PND1-6 were harvested and fixed on 20, and 45 (for PND20, n = 2 for control, n = 3 for treated, for PND45 n = 2 both for the control and the treated). Uteri of the rat pups injected from PND6-11, or PND11-17, were harvested and fixed on PND45 (n > 2 for all) (Figure 5A).

### Gonadectomy

To rule out the involvement of ovarian hormones as a contributor to the MIS-induced uterine hypoplasia, rat pups were gonadectomized two days after birth (n = 4), prior to receiving MIS treatment (Figure 5—figure supplement 2A–B). For gonadectomy, the rat pups were anesthetized using isofluorane. Bilateral longitudinal incisions were made in the mid dorsal line through the skin and musculature one-third the distance between the base of the tail and the neck, directly over the position of the ovary. The ovaries together with the oviducts were extruded through the incision via the ovarian fat pad. The ovarian vasculature was ligated between the oviduct and uterine horn and the ovaries and oviducts were resected. The muscle layer was closed with silk sutures, and the outer skin was closed with a single metal clip. The rats were then kept warm until they had completely recovered from the anesthesia. Analgesia was provided for 3 days with Carprofen PO. Two of the rat pups were treated with AAV9-MIS, while the controls were treated with empty vector (5E10 particles, subcutaneously, n = 2 both for control and treated) 6 hr after the surgery. The pups were then euthanized on PND10, and their uteri were fixed for histomorphological analysis (Figure 5—figure supplement 2A–B).

### Misr2cre/cre transgenic mice

To verify that the MIS Receptor 2 (Misr2) is the mediator of the uterine phenotype caused by exogenous MIS, Misr2cre/+ and Misr2cre/cre transgenic mice (Jamin et al., 2002) were treated with empty vector or AAV9-MIS (5E10 particles, subcutaneously) on day 1 and their uteri were analyzed on PND20 (Figure 5—figure supplement 2C–D) (n = 2 for Misr2cre/+, n = 1 for Misr2cre/cre). Misr2cre/cre males had retained Mullerian ducts confirming the loss-of-function of the Misr2 (Jamin et al., 2002).

### ELISA

The Beckman AMH ELISA (Beckman, #A73818), which can detect both endogenous murine MIS and exogenous human MIS secreted by the AAV9-MIS infected muscles was used to measure the serum MIS levels. To detect the murine endogenous MIS levels during the developmental time span of rat females, serum from control PND1, 4, 6, and 20 rats, as well as AAV9-MIS-treated rats on PND six were measured by ELISA (n = 3 for PND4, 6 and 20, and n = 2 for PND 1, n = 3 for AAV9-MIS treated rat).

Murine Estradiol and Testosterone serum levels were measured with specific ELISAs at the Ligand Assay and Analysis Core of the Center for Research in Reproduction at University of Virginia School of Medicine under a cooperative agreement (The core is supported by the Eunice Kennedy Shriver NICHD/NIH (NCTRI), Grant P50-HD28934). (n = 3 for PND3 and 30 control and treated, and PND 5 control; n = 2 for PND five treated; PND6, 10, 15 control and treated animals).

### Fertility tests

Sprague–Dawley rats were injected subcutaneously with 3 mg/kg/day of recombinant MIS (LR-MIS) or 20 µl saline (vehicle control) from PND1-6. One MIS-treated and one sibling control female were caged with one experienced breeder male (n = 3 cages) at 6 weeks of age. The male was separated from the cage after pregnancy was identified and returned after the pups were weaned. The total number of pups and litters from each female was monitored for a period of 4 months.

### Histology, immunofluorescence (IF), immunohistochemistry (IHC) and RNA in situ hybridization

Dissected uteri and ovaries were fixed in 4% (wt/vol) paraformaldehyde at 4°C (for histology and immunofluorescence) or in 10% neutral buffered formalin at room temperature overnight (for RNAish). Tissues were embedded in paraffin blocks in an automated tissue processor (Leica #TP1020). 5 μm transverse uterine sections from the middle of the uterine horn (i.e ‘b’ in Figure 1—figure supplement 1D) were used for hematoxylin and eosin (H&E) staining, immunofluorescence (IF), and RNAish using the RNA scope (ACD bio) system. Archival human fetal tissue sections were provided by the Massachusetts General Hospital, Gynecological Pathology Department through an IRB approved protocol (IRB 2007P001918).

Tissue sections were rehydrated for IF in an alcohol series after deparaffinization in xylene. Antigen retrieval was performed by parboiling in 10 mM sodium citrate (pH 6.0), cooling at room temperature, blocking in 3% bovine serum albumin (BSA) in Tris-buffered solution (TBS) for 1 hr, followed by three washes (10 min each) in TBS and the sections incubated in primary antibody overnight at 4°C. For double-labeling, the slides were blocked after washes, and then incubated with a second primary antibody overnight at 4°C. The sections were then incubated in fluorescently conjugated secondary antibodies (Alexa Fluor 555-conjugated donkey anti-rabbit IgG antibody, # A31572; Alexa Fluor 488-conjugated donkey anti-rabbit IgG, #A21206) for one hour at room temperature and cover-slipped with vectashield mounting medium with DAPI (Vector Laboratories # NC9265087). For immunohistochemistry (IHC), Dako EnVision + System horseradish peroxidase (HRP) Labeled Polymer Anti-Rabbit was used as the secondary antibody (#K4002), and the HRP signal was detected using the DAKO detection system (Dako, #K5007). Antibody dilutions for IF and IHC were as follows: Smooth muscle alpha action (SMA) (1:300, abcam, #5694), Vimentin (1:300, abcam, #32547), Foxa2 (1:500, LifeSpan Biosciences, #138006, 1:500), cleaved caspase-3 (1:50, cell signaling, #9661S), E-cadherin (Cdh1) (1:200, Invitrogen #13–1900).

RNAish was performed with the manual RNAscope 2.5 HD Reagent Kit (RED) (ACD Bio, # 322350) following the manufacturer’s instructions as previously described (Wang et al., 2012). The tissue sections were hybridized with pre-designed or custom-designed probes spanning mRNAs of the target genes (see Table S1 for accession number, target region, and catalog number of each gene) in the HybEZ hybridization oven (ACD Bio) for 2 hr at 40°C, following deparaffinization in xylene, dehydration, peroxidase blocking, and heat-induced epitope retrieval by the target retrieval and protease plus reagents (ACD bio, #322330). The slides were then processed for standard signal amplification steps, and a red chromogen development was performed using the RNAscope 2.5 HD (Red) detection Kit (ACD Bio, #322360). The slides were then counterstained in 50% hematoxylin (Dako, #S2302) for 2 min, air-dryed and coverslipped with EcoMount.

### Histomorphological analysis and quantification of RNA-scope images

Middle sections (‘b’ in the scheme of Figure 1—figure supplement 1D) of control and MIS-treated rat uteri were stained with H and Es for histomorphological analyses, which were conducted at different developmental time points) (Figure 2—source data 1, Figure 5—source data 1). Luminal duct height, area of the whole uterus, and area of the endometrium were calculated from the transverse sections using the image J software. For Figure 2, n = 3 for PND3 control and treated; n = 2 for PND6, 20 control and treated, n = 1 for PND10 control and treated samples. For Figure 4, n = 2 for the PND20 control; PND45 control and the treated; n = 3 for the treated PND20 sample (Figure 2—source data 1).

Human fetal tissue sections were imaged by the Keyence BZ-X800 microscope at 20x resolution, and the RNAish stains were auto-quantified by BZ-X800 analysis software. Approximately 60 images were obtained per stained section, and stitched together for the top panel of Figure 6a. 5 random 20x images were selected per time point for analysis, and areas of red RNA scope dots (Misr2 transcripts amplified by RNA-scope) were detected and labeled based on hue (see red dots on the bottom section of Figure 4a, labeled as ‘enhanced Misr2’). Total cell area was calculated by setting the masked area as the hematoxylin-stained region. RNAish dots/total area were auto-calculated by the same settings in 5 random 20X sections of human fetal tissues from 20, 22, and 37 weeks of gestation, n = 1 for each time point.

### Quantitative PCRs

Total RNA was extracted from the uteri of control and AAV9-MIS treated rats at different time points (Figure 3—source data 3) using the Qiagen RNA extraction kit. For all the samples, cDNA was synthesized from 500 ng total uterine RNA using SuperScript III First-Strand Synthesis System for RT-PCR according to manufacturer’s instructions using random hexamers (Invitrogen, # 18080–051). The primers were designed to span the exon-exon junctions of the target genes (see Figure 3—source data 3 for complete list of primers) to avoid genomic DNA contamination. Expression levels relative to 18S (for Acta2) and Gapdh (for all the other genes analyzed) were calculated by using cycle threshold (Ct) values logarithmically transformed using the 2−ΔCt function and the average value of the relative expression levels were normalized to PND three control set; and fold changes were calculated relative to PND three control time point with three technical replicates per sample. For Acta2, Tgln, and Foxa2 expression levels were normalized to PND six control set. Sample sizes and p values for each gene and time point are listed in Figure 3—source data 3.

### Generation of single cell (sc) suspension for scRNAseq

Newborn rats (PND1) were injected with 5E10 particles of AAV9-MIS (N = 3) or AAV9 empty particle controls (N = 3). On PND6, rat pups were sacrificed and the uterine tissue was microdissected, taking care to exclude the oviduct, cervix, and ureter. Both uterine horns from each animals (N = 3 per group) were combined and placed in 5 mL of dissociation medium (82 mM Na2SO4, 30 mM K2SO4, 10 mM Glucose, 10 mM HEPES, and 5 mM MgCL2 - 6H2O, pH 7.4) containing 15 mg of Protease 23 (Worthington), 100 U Papain with 5 mM L-Cysteine and 2.5 mM EDTA (Worthington), and 1333 U of DNase 1 (Worthington) prewarmed to 34C. The samples were placed on a rocker at 34C for 15 min. The medium was then removed with a pipette and replaced with 5 mL chilled (4C) stop medium (dissociation medium containing 0.025% BSA) supplemented with 0.5 mg trypsin Inhibitor and 0.5 mg ovomucoid protease Inhibitor. Samples were triturated 10 times with a 5 mL pipette, then 10 times with a 1000 µl micropipette, and finally filtered through a prewetted 100 µm filter. Filtered samples were spun at 1000 g for 10 min, and the cell pellet was resuspended in 1 ml of stop solution with 267 U of DNase. This step was repeated twice. Ten microliters was removed from each sample and combined with trypan blue to assess viability and concentration of cells. The cell mixture was spun a final time and resuspended in stop solution containing 20% Optiprep (Sigma) to a concentration of 150,000 cells/mL for inDrop sorting.

Single-cell RNA sequencing (inDrop) inDrop microfluidic sorting was performed as previously described (Hrvatin et al., 2018) generating two libraries of approximately 5000 cells from each combined (N = 3 rats) cell suspensions (control and MIS). Transcripts were processed as previously described and samples were sequenced on a NextSeq 500 (Ilumina) in a single combined lane (Hrvatin et al., 2018).

### Data analysis of scRNAseq

The analysis of the demultiplexed data was performed using the Seurat package in ‘R’ (Butler et al., 2018). Filtering parameters were set to remove cells with fewer than 200 genes, and those with more than 3000 genes and/or 10,000 UMIs from the dataset. Dataset included 6811 control cells, and 2990 MIS treated cells which were jointly normalized. The Pearson correlation coefficient of UMI and nGene across the dataset was 0.97. Principal component analysis was performed using 20 dimensions and FindClusters parameters were set at k.param = 30, k.scale = 25, and prune.SNN = 0.0667 with a resolution of 0.6 using 5346 variable genes. Data set and R codes are presented in Figure 3—source data 1. For differential expression analysis of the myometrium and the epithelial cell clusters, data sets are presented in Figure 3—source data 2 and Figure 4—source data 2.

### CellPhoneDB analysis

CellPhoneDB predicts signaling between cell clusters through analyzing co-expression of known Human receptors and secreted proteins. We downloaded ortholog information for Rat (Rnor_6.0) and Human (GRCh38.p12) from ENSEMBL (Release 95). For non one-to-one orthologs, we assigned the maximum of gene expression values for all Rat to Human mappings. CellPhoneDB was subsequently run using default parameters (Vento-Tormo et al., 2018). The resulting data set is presented in Figure 4—source data 1.

### Statistical analysis

For serum MIS ELISA measurements of the control rats, two-way ANOVA analysis was used. For the serum ELISA measurements of the control and the treated rats on PND6, the histomorphology, and the staining analyses, unpaired Student’s t test was used to compare the control and the treated samples using the Prism software (Graphpad version 8.0). p values are presented in Figure 2—source data 1, and Figure 3—source data 3, and Figure 5—source data 1.
