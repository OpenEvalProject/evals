# Thymic macrophages consist of two populations with distinct localization and origin

## Authors

- Tyng-An Zhou<sup>1</sup> ([ORCID: 0000-0003-4031-4947](https://orcid.org/0000-0003-4031-4947))
- Hsuan-Po Hsu<sup>1</sup>
- Yueh-Hua Tu<sup>2</sup>
- Hui-Kuei Cheng<sup>1</sup>
- Chih-Yu Lin<sup>1</sup>
- Nien-Jung Chen<sup>1</sup>
- Jin-Wu Tsai<sup>4</sup>
- Ellen A Robey<sup>5</sup> ([ORCID: 0000-0002-3630-5266](https://orcid.org/0000-0002-3630-5266))
- Hsuan-Cheng Huang<sup>2</sup>
- Chia-Lin Hsu<sup>1</sup>
- Ivan L Dzhagalov<sup>1</sup> ([ORCID: 0000-0001-9209-4582](https://orcid.org/0000-0001-9209-4582)) †

### Affiliations

1. Institute of Microbiology and Immunology, National Yang Ming Chiao Tung University Taipei Taiwan ([ROR:00se2k293](https://ror.org/00se2k293))
2. Bioinformatics Program, Taiwan International Graduate Program, Institute of Information Science, Academia Sinica Taipei Taiwan ([ROR:05bxb3784](https://ror.org/05bxb3784))
3. Graduate Institute of Biomedical Electronics and Bioinformatics, National Taiwan University Taipei Taiwan ([ROR:05bqach95](https://ror.org/05bqach95))
4. Brain Research Center, National Yang Ming Chiao Tung University Taipei Taiwan ([ROR:00se2k293](https://ror.org/00se2k293))
5. Division of Immunology and Pathogenesis, Department of Molecular and Cell Biology, University of California, Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))
6. Institute of Biomedical Informatics, National Yang Ming Chiao Tung University Taipei Taiwan ([ROR:00se2k293](https://ror.org/00se2k293))

† Corresponding author

## Abstract

Tissue-resident macrophages are essential to protect from pathogen invasion and maintain organ homeostasis. The ability of thymic macrophages to engulf apoptotic thymocytes is well appreciated, but little is known about their ontogeny, maintenance, and diversity. Here, we characterized the surface phenotype and transcriptional profile of these cells and defined their expression signature. Thymic macrophages were most closely related to spleen red pulp macrophages and Kupffer cells and shared the expression of the transcription factor (TF) SpiC with these cells. Single-cell RNA sequencing (scRNA-Seq) showed that the macrophages in the adult thymus are composed of two populations distinguished by the expression of Timd4 and Cx3cr1. Remarkably, Timd4+ cells were located in the cortex, while Cx3cr1+ macrophages were restricted to the medulla and the cortico-medullary junction. Using shield chimeras, transplantation of embryonic thymuses, and genetic fate mapping, we found that the two populations have distinct origins. Timd4+ thymic macrophages are of embryonic origin, while Cx3cr1+ macrophages are derived from adult hematopoietic stem cells. Aging has a profound effect on the macrophages in the thymus. Timd4+ cells underwent gradual attrition, while Cx3cr1+ cells slowly accumulated with age and, in older mice, were the dominant macrophage population in the thymus. Altogether, our work defines the phenotype, origin, and diversity of thymic macrophages.

## Introduction

Tissue-resident macrophages are present in every organ and maintain local homeostasis through diverse functions ranging from protection against pathogens to tissue repair (Wynn et al., 2013). To perform their roles efficiently, macrophages acquire specialized phenotypes depending on the tissue microenvironment, and as a consequence, multiple subtypes exist, frequently within the same organ. For example, the spleen harbors red pulp macrophages specialized in red blood cell phagocytosis, marginal zone macrophages, and metallophilic macrophages that are the first defense against blood-borne pathogens, T cell zone macrophages that silently dispose of apoptotic immune cells, and tingible-body macrophages that engulf less fit B cells in the germinal center (Baratin et al., 2017; A-Gonzalez and Castrillo, 2018; Bellomo et al., 2018). Thus, tissue-resident macrophages represent a fascinating developmental system that allows enormous plasticity.

The last decade has seen a paradigm shift in our understanding of the development of tissue-resident macrophages. Contrary to the long-held belief that all macrophages derive from circulating monocytes (van Furth and Cohn, 1968), multiple studies have shown that many of them are long-lived cells with an embryonic origin that can maintain themselves in the tissues (reviewed in Ginhoux and Guilliams, 2016). Three waves of distinct progenitors settle the tissues and contribute in various degrees to the resident macrophages in each organ. The first wave consists of the yolk sac (YS)-derived primitive macrophages that enter all tissues and establish the earliest macrophage populations (Perdiguero and Geissmann, 2016; Mass et al., 2016). In all organs, except for the brain and, partially, the epidermis, primitive macrophages are replaced by the next wave consisting of fetal monocytes (Ginhoux et al., 2010; Hoeffel et al., 2012; Hoeffel et al., 2015; Goldmann et al., 2016). The third wave comes from hematopoietic stem cells (HSCs)-derived monocytes that contribute to various degrees to the macrophage pool in different tissues. For example, these cells contribute little to the microglia in the brain, Langerhans cells in the epidermis, and alveolar macrophages in the lungs but substantially to most other organs (Hashimoto et al., 2013; Epelman et al., 2014; Sheng et al., 2015; Liu et al., 2019). Moreover, the kinetics and timing of HSC-derived monocyte infiltration vary in different parts of the body. For some macrophage populations, such as the arterial macrophages and subcapsular lymph node macrophages, monocytes replace embryonic macrophages soon after birth and self-maintain after that with little contribution from circulating cells (Ensan et al., 2016; Mondor et al., 2019). Others, such as heart macrophages, osteoclasts, and pancreatic islets macrophages, are progressively replaced at a low rate (Epelman et al., 2014; Molawi et al., 2014; Heidt et al., 2014; Calderon et al., 2015; Jacome-Galarza et al., 2019; Yahara et al., 2020). A third group, such as the macrophages in the dermis and most of the gut macrophages, is constantly replaced by blood monocytes with relatively fast kinetics (Tamoutounour et al., 2013; Bain et al., 2014). These conclusions have been extended to many different macrophage populations such as Kupffer cells, liver capsular macrophages, red pulp macrophages, testicular macrophages, large and small peritoneal macrophages, and T zone macrophages in the lymph nodes (Baratin et al., 2017; Hashimoto et al., 2013; Epelman et al., 2014; Liu et al., 2019; Sierro et al., 2017; Mossadegh-Keller et al., 2017; Lokka et al., 2020; Wang et al., 2021; Bain et al., 2016).

The recent revitalization in macrophage research has yet to reach thymic macrophages. Although their prodigious phagocytic ability is well appreciated (Surh and Sprent, 1994), little is known about the origin, diversity, and maintenance of these cells. This gap in our knowledge is, partly, due to the lack of a consensus about the surface phenotype of thymic macrophages. Various groups have used different markers to identify these cells, such as F4/80 and Mac-3 (LAMP-2) (Surh and Sprent, 1994), or CD4 and CD11b (Esashi et al., 2003), or Mac-2 (galectin 3), F4/80, and ED-1 (CD68) (Liu et al., 2013). Most commonly, researchers employ F4/80 and CD11b (Guerri et al., 2013; Lopes et al., 2018; Kim et al., 2010; Tacke et al., 2015). However, none of these markers is macrophage-specific: F4/80 is also expressed on eosinophils and monocytes (Gautier et al., 2012; Ingersoll et al., 2010), while CD11b is present on most myeloid cells. The lack of a clear phenotypic definition of thymic macrophages has translated into the absence of models that targets genes specifically in this population. For example, although macrophages in various organs have been successfully targeted with Lyz2Cre, Csf1rCre, or Cx3cr1Cre, very few studies have used these models in the thymus (Tacke et al., 2015; Wang et al., 2019; Chan et al., 2020).

Only a handful of studies have explored the origin of thymic macrophages. Several reports have indicated that these cells could be derived from T cell progenitors in the thymus based on an improved single-cell in vitro culture and in vivo transplantation experiments (Wada et al., 2008; Bell and Bhandoola, 2008). However, these conclusions have been questioned based on fate-mapping experiments using Il7rCre that found very limited contribution of lymphoid progenitors to thymic macrophages in vivo in unperturbed mice (Schlenner et al., 2010). Most recently, Tacke et al., 2015 used parabiosis to rule out circulating monocytes as a major source of thymic macrophages. The same study also performed fate-mapping experiments to show that most thymic macrophages descend from Flt3+ HSC-derived progenitors. However, the contribution of earlier waves of hematopoiesis has not been explored.

Here, we aimed to bring our knowledge of thymic macrophages on par with other tissue-resident macrophages. We started by clearly defining thymic macrophages according to the guidelines set by the Immunological Genome Consortium (IMMGEN) (Gautier et al., 2012) and characterized their surface phenotype and transcriptional signature. Using scRNA-Seq, we identified two populations of thymic macrophages with distinct localization. We explored the origin of these cells through genetic fate mapping, shield chimeras, and embryonic thymus transplantation and documented that different waves of progenitors give rise to the two populations of thymic macrophages. Altogether our work fills an important gap in our understanding of resident thymic macrophages and provides the framework for future functional characterization of these cells.

## Results

### CD64, F4/80, and MerTK identify the macrophages in the thymus

To unambiguously and comprehensively identify macrophages in the thymus, we evaluated several of the prototypical macrophage markers – MerTK, CD64, and F4/80 (Gautier et al., 2012) – a population that was stained with all three markers (Figure 1A). As staining with MerTK and F4/80 was relatively dim even when the brightest fluorochromes (e.g. PE) were used and could not be resolved fully from the isotype control (Figure 1—figure supplement 1), we chose to use CD64 vs. forward scatter (FSC) as the first step in our gating strategy (Figure 1B). Among CD64+FSChi cells, F4/80+CD11blo macrophages could be distinguished from F4/80loCD11b+ monocytes.

![Figure 1.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig1-v2.jpg)

**Figure 1.:** (A) Flow cytometric analysis of enzymatically digested thymus tissue with macrophage markers CD64, MerTK, F4/80, and CD11b. (B) Gating strategy for identifying ThyMacs: CD64+FSChi are first gated; the F4/80+CD11blo cells among them are the ThyMacs, while F4/80loCD11b+ are the thymic monocytes (ThyMonos). (C) Pappenheim (Hemacolor Rapid staining kit) staining of sorted ThyMacs. (D) Lack of expression of lineage markers associated with other cell types on ThyMacs. (E) The expression on ThyMacs of three receptors for phosphatidylserine that participates in the phagocytosis of apoptotic cells. (F) Labeling of ThyMacs with intravenously injected anti-CD45-PE antibody or PBS. The labeling of blood leukocytes is shown for comparison. (G) Average numbers and percentages of ThyMacs in 4–11 weeks old mice, n=82. (H) Comparison of the numbers and percentages of ThyMacs in mice of different ages, n=82. All flow cytometry plots are representative of at least three independent repeats. The numbers in the flow cytometry plots are the percent of cells in the respective gates. Data in (G) and (H) represent mean ± SEM. Statistical significance in (H) was determined with one-way ANOVA.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** The flow cytometry plots are representative of 5 individual experiments.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** The images are representative of at least three mice. The scale bar is 50 µm.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** The flow cytometry plots are representative of five individual experiments.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** On the right is a plot of the frequency of MerTK+ cells among CD11c+MHC2+SIRPα+ cells. The data are mean ± SEM from five individual mice. Each dot is an individual mouse. The numbers in the flow cytometry plots are the percent of cells in the respective gate.

The CD64+F4/80+MerTK+CD11bloFSChi cells had typical macrophage morphology with abundant cytoplasm (Figure 1C). These cells did not express lineage markers characteristic of T cells (CD3ε), B cells (CD19), eosinophils (Siglec F), NK cells (NK1.1), neutrophils (Gr1), or plasmacytoid dendritic cells (Siglec H) (Figure 1D). However, they expressed phagocytic receptors such as TIM4, CD51, and Axl (Figure 1E). Immunofluorescent staining with CD64, MerTK, and TIM4 in the thymic cortex confirmed the presence of large cells positive for all three macrophage markers (Figure 1—figure supplement 2).

Importantly, MerTK+ cells could not be labeled by intravenously injected CD45 antibody (Figure 1F), proving that they reside in the parenchyma of the organs and not in the blood vessels. Based on the above data, we will refer to CD64+F4/80+MerTK+CD11bloFSChi cells as thymic macrophages. The smaller CD64+F4/80loCD11b+FSChi population did not express MerTK but most of them expressed Ly6C, and we classified them as thymic monocytes.

Thymic macrophages expressed CD11c, MHC2, and SIRPα making them partially overlap with CD11c+MHC2+ classical dendritic cells (cDCs), thus making problematic the unambiguous identification of thymic cDCs based only on these two markers (Figure 1—figure supplement 3). Proper identification of cDC in the thymus requires the exclusion of macrophages based on CD64 or MerTK staining. Otherwise, the cDCs, particularly the SIRPα+ cDC2 subset, would be contaminated with macrophages that account for ~25% of cDC2 (Figure 1—figure supplement 4).

Thymic macrophages were ~0.1% of all the cells in the thymus of young adult mice and numbered ~4×105 on average per mouse (Figure 1G). We did not find statistically significant differences in their percentages between 4 and 11 weeks of age. Still, there was a significant decline in their numbers with age, consistent with the beginning of thymic involution (Figure 1H).

### Transcriptional signature of thymic macrophages

To further understand the identity and functions of the thymic macrophages, we analyzed the RNA sequencing data from the IMMGEN’s Open Source Mononuclear Phagocyte profiling. We first examined the expression of the core signature macrophage genes (Gautier et al., 2012) and found that they were enriched in thymic macrophages but not in Sirpa+ or Xcr1+ thymic cDCs (Figure 2A). On the contrary, cDC core signature genes were abundantly expressed in both thymic cDC subsets but not in thymic macrophages. Thus, although thymic macrophages and cDCs share the thymic microenvironment and expression of CD11c and MHC2, they have distinct transcriptional profiles.

![Figure 2.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig2-v2.jpg)

**Figure 2.:** (A) Expression of classical dendritic cell (cDC)-specific genes (top) and macrophage-specific genes (bottom) in ThyMacs and two populations of thymic cDCs (ThyDCs) – Xcr1+ ThyDCs and Sirpa+ ThyDCs. (B) Principal components analysis of ThyMacs and nine other populations of tissue-resident macrophages in duplicates. (C) Highly expressed (>500) genes enriched (>fivefold) in ThyMacs (four samples) compared to nine other tissue-resident macrophage populations (two samples each). The genes in red are >10-fold up-regulated in ThyMacs. (D) Comparison of the geometric mean expression of transcription factors in ThyMacs (four samples) and the nine other macrophage populations (two samples each). Transcription factors with expression >250 and fold change >2 are marked with red dots. (E) Top 10 gene ontology (GO) pathways in ThyMacs based on the 500 most highly expressed genes in these cells.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** On the right is a plot showing the mean ± SEM of the frequencies of ThyMacs among SpicGFP+ cells. Each dot is an individual mouse. The numbers in the flow cytometry plots are the percent of cells in the respective gate.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Data in the graphs represent mean ± SEM. Each dot is an individual mouse.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** To the right is a graph showing the mean ± SEM of the frequencies of SpicGFP+ cells among ThyMacs. Each dot is an individual mouse. The numbers in the flow cytometry plots are the percent of cells in the respective gate.

We then compared the gene expression profile of thymic macrophages to that of other well-characterized macrophage populations from the IMMGEN database. Because of the abundance of samples, we limited our comparison to only nine types of tissue-resident macrophages under steady-state conditions – splenic red pulp macrophages, Kupffer cells, broncho-alveolar lavage macrophages, large peritoneal cavity macrophages, white adipose tissue macrophages, aorta macrophages, central nervous system microglia, and spinal cord microglia. Principal component analysis revealed that thymic macrophages were most closely related to splenic red pulp macrophages and Kupffer cells (Figure 2B).

To better identify the unique functions of thymic macrophages, we looked for differentially expressed genes in these cells compared to other tissue-resident macrophages. We set three criteria: (1) high expression in thymic macrophages (>500); (2) >fivefold higher expression than the average value in the nine populations of non-thymic macrophages; (3) expression in thymic macrophages is higher than any non-thymic macrophage samples. A total of 44 genes met these criteria, and we consider them to constitute the transcriptional signature of thymic macrophages (Figure 2C). These included several degradation enzymes and their inhibitors (Cst7, Mmp2, Mmp14, Dnase1l3, Serpina3g, Acp5), non-classical MHC molecules (H2-M2, H2-Q6, H2-Q7), metabolic enzymes (Chst2, Ass1, Kynu, Cp, Dgat2, Sorl1, Lap3), molecules involved in innate immunity (Ifit2, Il18bp, Mefv, Lgals3bp), and extracellular signaling molecules and their receptors (Pdgfa, Cxcl16, Il2rg, Gpr157). We also looked for TFs highly expressed in thymic macrophages and could potentially regulate critical gene networks in these cells. A total of 25 TFs were highly expressed in thymic macrophages (>250) and were at least twofold higher as compared to the non-thymic macrophages (Table 1). Among them were several TFs involved in type I interferon (IFN-I) signaling (Stat1, Stat2, Irf7, and Irf8) and lipid metabolism (Nr1h3, Pparg, Srebf1, and Rxra) (Figure 2D). Notably, Runx3, which is essential for the development and function of cytotoxic T lymphocytes (Taniuchi et al., 2002), innate lymphoid cells (Ebihara et al., 2015), and Langerhans cells (Fainaru et al., 2004), was highly expressed in thymic macrophages. Spic, which has well-documented roles in the development of red pulp macrophages in the spleen and bone marrow macrophages (Kohyama et al., 2009; Haldar et al., 2014), was also highly expressed in thymic macrophages, further strengthening the argument for the similarity between thymus, spleen, and liver macrophages. To confirm the expression of Spic in thymic macrophages, we analyzed the thymus of SpicGFP mice (Haldar et al., 2014). We found that all SpicGFP+ cells were macrophages (Figure 2—figure supplement 1), making them the most specific thymic macrophage reporter strain compared with Lyz2GFP, MAFIA (Csf1rGFP), Cd11cYFP, and Cx3cr1GFP mice (Figure 2—figure supplement 2). However, only ~80% of thymic macrophages were SpicGFP+ suggesting heterogeneity within the cells (Figure 2—figure supplement 3).

**Table 1.**
 Expression of differentially up-regulated transcription factors in thymic macrophages.Transcription factors that were highly expressed in thymic macrophages (>250) and up-regulated >twofold in thymic macrophages compared to non-thymic macrophages were listed alphabetically, and the geometric means of four replicates of thymic macrophages (ThyMacs) and two replicates of each of the nine non-thymic macrophage populations (non-ThyMacs) were recorded. Non-thymic macrophages are: spleen red pulp macrophages, Kupffer cells, broncho-alveolar lavage macrophages, peritoneal cavity macrophages, aorta macrophages, heart macrophages, white adipose tissue macrophages, central nervous system microglia, and spinal cord macrophages.


<table>
  <thead>
    <tr>
      <th>Gene name</th>
      <th>ThyMacs</th>
      <th>non-ThyMacs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Irf7</td>
      <td>3879.32</td>
      <td>300.82</td>
    </tr>
    <tr>
      <td>Irf8</td>
      <td>3528.27</td>
      <td>1474.35</td>
    </tr>
    <tr>
      <td>Stat1</td>
      <td>2403.69</td>
      <td>522.04</td>
    </tr>
    <tr>
      <td>Dnmt3a</td>
      <td>1515.94</td>
      <td>647.81</td>
    </tr>
    <tr>
      <td>Znxf1</td>
      <td>1379.89</td>
      <td>635.36</td>
    </tr>
    <tr>
      <td>Stat2</td>
      <td>1210.35</td>
      <td>472.53</td>
    </tr>
    <tr>
      <td>Nr1h3</td>
      <td>1182.17</td>
      <td>147.05</td>
    </tr>
    <tr>
      <td>Srebf1</td>
      <td>975.09</td>
      <td>399.06</td>
    </tr>
    <tr>
      <td>Rxra</td>
      <td>760.26</td>
      <td>298.55</td>
    </tr>
    <tr>
      <td>Trps1</td>
      <td>746.36</td>
      <td>232.48</td>
    </tr>
    <tr>
      <td>Runx3</td>
      <td>723.14</td>
      <td>9.76</td>
    </tr>
    <tr>
      <td>Relb</td>
      <td>715.53</td>
      <td>293.92</td>
    </tr>
    <tr>
      <td>Sp100</td>
      <td>696.94</td>
      <td>324.47</td>
    </tr>
    <tr>
      <td>Zbp1</td>
      <td>639.19</td>
      <td>69.83</td>
    </tr>
    <tr>
      <td>Tfec</td>
      <td>588.72</td>
      <td>74.66</td>
    </tr>
    <tr>
      <td>Spic</td>
      <td>573.11</td>
      <td>34.36</td>
    </tr>
    <tr>
      <td>Nfkbie</td>
      <td>569.74</td>
      <td>226.76</td>
    </tr>
    <tr>
      <td>Ncoa4</td>
      <td>550.69</td>
      <td>249.15</td>
    </tr>
    <tr>
      <td>Rest</td>
      <td>548.22</td>
      <td>269.22</td>
    </tr>
    <tr>
      <td>Meis3</td>
      <td>530.8</td>
      <td>120.91</td>
    </tr>
    <tr>
      <td>Bhlhe40</td>
      <td>490.59</td>
      <td>99.56</td>
    </tr>
    <tr>
      <td>Parp12</td>
      <td>414.11</td>
      <td>126.82</td>
    </tr>
    <tr>
      <td>Arid5b</td>
      <td>374.03</td>
      <td>177.08</td>
    </tr>
    <tr>
      <td>Creb5</td>
      <td>295.14</td>
      <td>47.91</td>
    </tr>
    <tr>
      <td>Pparg</td>
      <td>276.54</td>
      <td>33.24</td>
    </tr>
  </tbody>
</table>

Several dominant pathways emerged when we grouped the 500 most highly expressed genes in thymic macrophages according to gene ontology (GO) terms (Figure 2E). Notably, 5 of the 10 most highly enriched GO pathways concerned antigen presentation of both exogenous and endogenous antigens. These data complement our flow cytometry findings of expression of MHC2 and suggest that thymic macrophages could be potent antigen-presenting cells and might play a role in negative selection or agonist selection of thymocytes. Two other highly enriched GO pathways were involved in lysosomal biogenesis and functions, highlighting the high capacity of these cells to degrade phagocytosed material. Thus, our transcriptional analysis has revealed that thymic macrophages are bona fide macrophages that bear significant similarity to spleen and liver macrophages and are specialized in lysosomal degradation of phagocytosed material and antigen presentation.

### Thymic macrophages can present antigens to T cells and clear apoptotic cells

Next, we investigated the biological functions of thymic macrophages. Our findings that these cells express MHC2 and many other genes involved in antigen presentations prompted us to test if they can efficiently activate T cells. We pulsed sorted thymic macrophages with chicken ovalbumin (Ova) and cultured them with naïve OT2 cells labeled with CFSE. The positive control, thymic DCs, efficiently induced OT2 cell proliferation, while peritoneal macrophages were very inefficient (Figure 3A and B), similar to other tissue-resident macrophages (Baratin et al., 2017). Surprisingly, thymic macrophages induced proliferation in a considerable proportion (~30%) of OT2 cells as calculated by FlowJo’s Proliferation Modeling module. Thus, thymic macrophages are able antigen-presenting cells, although not as good as DCs.

![Figure 3.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig3-v2.jpg)

**Figure 3.:** (A) Naïve OT2 T cells were labeled with CFSE and cultured with purified thymic dendritic cells (ThyDCs), thymic macrophages (ThyMacs), or peritoneal cavity macrophages (PC Macs) in the presence or absence of chicken ovalbumin (Ova). Three days later, the CFSE dilution was assessed by flow cytometry. (B) Quantification of the cell division in naïve OT2 cells by using the Cell Proliferation module in FlowJo that calculates the percent of cells from the initial population that has undergone division. (C) Example immunofluorescent images of ThyMacs or PC Macs phagocytosis apoptotic thymocytes. The macrophages were labeled with eFluor 450, while the apoptotic thymocytes with pHrodo Red. An intense red signal within the macrophages indicates phagocytosed thymocytes. (D) Quantification of the percentage of macrophages that have engulfed at least one thymocyte (phagocytic index). (E) Example images showing co-localization of TUNEL+ apoptotic cells and MerTK+ ThyMacs in thymic sections. (F) Example images showing co-localization of TUNEL+ apoptotic cells and TIM4+ ThyMacs in thymic sections. Scale bars in (E and F) are 50 µm. (G) Frequencies of the co-localization of TUNEL+ signal with MerTK+ and TIM4+ cells. Flow cytometry plots in (A) are representative of two independent experiments. All immunofluorescent images are representative of at least three independent repeats. Data in (B, D, and G) represent mean ± SEM. Each symbol in B and G is an individual mouse. Each symbol in D is a field of view.

To confirm the ability of thymic macrophages to clear apoptotic cells, we did in vitro engulfment assay. Thymocytes were induced to undergo apoptosis by dexamethasone treatment and labeled with pHrodo Red dye. pHrodo Red is weakly fluorescent at neutral pH, but its fluorescence increases significantly at low pH, for example, in lysosomes. Thus, engulfed apoptotic cells can be clearly identified by their strong red fluorescence. We incubated the pHrodo Red-labeled apoptotic thymocytes for 2 hr with sorted thymic or peritoneal cavity macrophages and detected the extent of efferocytosis by fluorescent microscopy. Thymic macrophages were avid phagocytes, and we could record many instances of efferocytosis at this time point (Figure 3C and D). However, peritoneal macrophages were able to phagocytose even more apoptotic cells.

To determine if thymic macrophages are the major phagocytes in the thymus in vivo, we evaluated their participation in the phagocytosis of apoptotic cells in the thymus by TUNEL staining. Most TUNEL+ cells could be found clearly inside or closely associated with MerTK+ and TIM4+ cells in the thymus (Figure 3E and F). On average, ~85% of all TUNEL+ cells were within 5 µm of MerTK+ cells, confirming that thymic macrophages are the dominant phagocytic population in the thymus (Figure 3G). The degree of co-localization between TUNEL+ cells and TIM4+ cells was slightly lower, ~75% on average, possibly reflecting the absence of TIM4 expression on a small proportion of thymic macrophages (Figure 1E).

### Expression of Timd4 and Cx3cr1 can distinguish two populations of thymic macrophages

Our phenotypic characterization showed clear signs of heterogeneity within thymic macrophages, including the presence of TIM4+ and TIM4− cells (Figure 1E) and Cx3cr1GFP+ and Cx3cr1GFP− cells (Figure 2—figure supplement 1). To determine the degree of thymic macrophage heterogeneity, we performed scRNA-Seq of sorted Csf1rGFP+ and Cd11cYFP+ thymic cells. Csf1r is required for the survival of most macrophages and is considered their definitive marker (Witmer-Pack et al., 1993; Sasmono et al., 2003), while Cd11cYFP is expressed in many myeloid cells, including macrophages (Hume, 2011). Both reporters identified an overlapping set of cells (Figure 4—figure supplement 1). At least seven clusters could be identified and assigned to different cell types by specific marker expression (Figure 4A and B), including macrophages, B cells, pDCs, contaminating thymocytes, and multiple cDC clusters. Two clusters expressed the macrophage/monocytes-specific TF Mafb and high levels of Fcgr1 (CD64), Mertk, and Adgre1 (F4/80), indicating that they are macrophages (Figure 4—figure supplement 2). An additional cluster expressed Mafb together with Fcgr1 and Adgre1 but not Mertk, fitting the description of monocytes. There was no expression of Mafb outside these three clusters confirming that our flow cytometry gating had identified all macrophages in the thymus. Once we zoomed onto Mafb-expressing cells, we could distinguish three separate populations: (1) monocytes that expressed high levels of Ly6c2 and Itgam (CD11b) but did not express Mertk; (2) Timd4+ (encoding TIM4) macrophages that also expressed high levels of Spic and Slc40a1, but low levels of Cx3cr1; (3) Cx3cr1+ macrophages that expressed low levels of Timd4, Spic, and Slc40a1 (Figure 4C and D). Both macrophages and monocytes expressed Fcgr1 (CD64). Thus, these data indicate that thymic macrophages consist of two populations with distinct expression profiles.

![Figure 4.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig4-v2.jpg)

**Figure 4.:** (A) Identification of the clusters from the single-cell RNA-sequencing data based on lineage-specific markers. (B) Expression of lineage-specific markers in different clusters. (C) UMAP clusters from A with high expression of the transcription factor Mafb fall into three groups: monocytes, Timd4+ macrophages, and Cx3cr1+ macrophages. (D) Expression of the indicated genes in the three Mafb-positive clusters. (E) A flow cytometry plot of Cx3cr1GFP and TIM4 expression in thymic macrophages (ThyMacs). The plot is representative of >10 individual experiments. The numbers inside the plot are the percentages of the cell populations in the respective gates. (F) Immunofluorescent staining of the thymus of Cx3cr1GFP mouse stained with MerTK (a marker for all macrophages) and Keratin 5 (a marker for medulla). The scale bar is 150 µm. Areas in the cortex, medulla, and the cortico-medullary junction (CMJ) represented by the dashed boxes are enlarged to the right to show the co-localization of Cx3cr11GFP and MerTK signal in CMJ and medulla, but not in the cortex. The scale bars in the images to the right are 20 µm. The images are representative of three individual mice. (G) Differentially expressed genes among Timd4+ thymic macrophages, Cx3cr1+ thymic macrophages, and thymic monocytes. The negative log10 p-values for the genes expressed in each cluster were calculated as described in the Materials and methods, and the top 50 differentially expressed genes were plotted in the figure. Ten of these genes are listed on the left.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig4-figsupp1-v2.jpg)

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig4-figsupp2-v2.jpg)

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** CD64 stains all macrophages, while TIM4 – only a subset that is located in the cortex. The image is representative of three mice. The scale bar is 400 µm.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig4-figsupp4-v2.jpg)

We confirmed the results from scRNA-Seq by flow cytometry. We could identify discrete TIM4+Cx3cr1GFP− and TIM4−Cx3cr1GFP+ macrophages (Figure 4E). There was even a TIM4+Cx3cr1GFP+ intermediate population that could not be distinguished in the scRNA-Seq dataset, likely because of the lack of statistical power. To determine the localization of the two distinct macrophage populations, we stained thymic sections from Cx3cr1GFP mice with an antibody to MerTK. The Cx3cr1GFP− MerTK+ cells correspond to Timd4+ macrophages, while the Cx3cr1GFP+MerTK+ cells would be the Cx3cr1GFP+ macrophages. Strikingly, the two macrophage populations showed distinct localization in young mice. Timd4+ macrophages were located in the cortex, while the Cx3cr1GFP+ macrophages resided in the medulla and the cortico-medullary junction (Figure 4F). The result was confirmed with direct staining for TIM4 that showed intense signal in the cortex, particularly in the deep cortex, and absence of staining in the medulla (Figure 4—figure supplement 3). However, the medulla still featured many CD64+ macrophages.

To better understand the differences between the two populations of thymic macrophages, we looked for differentially expressed genes. We included the thymic monocytes in the comparison, as these cells clustered the closest to macrophages. Timd4+ macrophages expressed the highest levels of the TFs Spic, Maf, and Nr1h3; the receptors for apoptotic cells Axl, Mertk, and Timd4; and many Slc transporters such as Slc40a1, Slc1a3, Slco2b1, Slc11a1, and Slc7a7 (Figure 4G and Table 2). Cx3cr1+ macrophages expressed high levels of the TF Runx3; a distinct set of phosphatidylserine receptors such as Stab1, Anxa5, and Anxa3; many degradative enzymes such as Mmp2, Mmp14, Dnase1l3, Acp5, Lyz2, Ctsz, Ctss, Ctsd, and Ctsl; cytokines such as Pdgfa, Cxcl16, and Ccl12; and molecules involved in MHC1 antigen presentation such as B2m, H2-M2, H2-K1, and H2-Q7. Thymic monocytes were characterized by differential expression of the typical monocyte genes Ly6c2, Ccr2, and S100a4, and genes involved in MHC2 antigen presentation such as Ciita, H2-DMb1, H2-Ab1, and Cd74.

**Table 2.**
 List of the differentially expressed genes among Timd4+ thymic macrophages, Cx3cr1+ thymic macrophages, and thymic monocytes.The top 100 differentially expressed genes among the three clusters are listed by their negative log10 transformed p-value.


<table>
  <thead>
    <tr>
      <th colspan="2">Cx3cr1 + ThyMacs</th>
      <th colspan="2">Timd4 + ThyMacs</th>
      <th colspan="2">ThyMonos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gene name</td>
      <td>Adjusted p-value</td>
      <td>Gene name</td>
      <td>Adjusted p-value</td>
      <td>Gene name</td>
      <td>Adjusted p-value</td>
    </tr>
    <tr>
      <td>Ctsz</td>
      <td>0</td>
      <td>Hpgd</td>
      <td>0</td>
      <td>Alox5ap</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Cd63</td>
      <td>0</td>
      <td>Serpinb6a</td>
      <td>0</td>
      <td>S100a6</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Pmepa1</td>
      <td>0</td>
      <td>Slc40a1</td>
      <td>0</td>
      <td>Ly6c2</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Zmynd15</td>
      <td>0</td>
      <td>Cd81</td>
      <td>0</td>
      <td>Ifi27l2a</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Olfml3</td>
      <td>0</td>
      <td>Vcam1</td>
      <td>0</td>
      <td>Fau</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Mmp2</td>
      <td>0</td>
      <td>Cfp</td>
      <td>0</td>
      <td>Coro1a</td>
      <td>0</td>
    </tr>
    <tr>
      <td>AU020206</td>
      <td>1.60E-290</td>
      <td>Spic</td>
      <td>0</td>
      <td>Ccr2</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Plxnd1</td>
      <td>1.59E-285</td>
      <td>Trf</td>
      <td>0</td>
      <td>Rps27</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Cst7</td>
      <td>8.68E-279</td>
      <td>Actn1</td>
      <td>0</td>
      <td>Tmsb10</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Dnase1l3</td>
      <td>2.45E-270</td>
      <td>Maf</td>
      <td>0</td>
      <td>Ifitm2</td>
      <td>7.21E-302</td>
    </tr>
    <tr>
      <td>Timp2</td>
      <td>2.15E-267</td>
      <td>Pld3</td>
      <td>0</td>
      <td>Fxyd5</td>
      <td>6.36E-299</td>
    </tr>
    <tr>
      <td>Lgals3bp</td>
      <td>8.69E-263</td>
      <td>Il18</td>
      <td>0</td>
      <td>Rps19</td>
      <td>2.04E-292</td>
    </tr>
    <tr>
      <td>Pdgfa</td>
      <td>6.87E-255</td>
      <td>Mrc1</td>
      <td>0</td>
      <td>Rpl18</td>
      <td>6.50E-291</td>
    </tr>
    <tr>
      <td>Mmp14</td>
      <td>2.33E-253</td>
      <td>Crip2</td>
      <td>0</td>
      <td>Rpl9</td>
      <td>1.11E-289</td>
    </tr>
    <tr>
      <td>Fam46c</td>
      <td>9.99E-235</td>
      <td>Tmem65</td>
      <td>0</td>
      <td>Rps23</td>
      <td>1.28E-289</td>
    </tr>
    <tr>
      <td>Chst2</td>
      <td>1.19E-226</td>
      <td>Igf1</td>
      <td>0</td>
      <td>Napsa</td>
      <td>8.91E-279</td>
    </tr>
    <tr>
      <td>Cp</td>
      <td>5.36E-225</td>
      <td>Epb41l3</td>
      <td>0</td>
      <td>Ms4a4c</td>
      <td>8.25E-272</td>
    </tr>
    <tr>
      <td>Camk1</td>
      <td>7.12E-225</td>
      <td>Timd4</td>
      <td>0</td>
      <td>Plac8</td>
      <td>2.10E-270</td>
    </tr>
    <tr>
      <td>B2m</td>
      <td>1.09E-222</td>
      <td>Blvrb</td>
      <td>0</td>
      <td>Rpl18a</td>
      <td>9.26E-269</td>
    </tr>
    <tr>
      <td>Lhfpl2</td>
      <td>4.52E-217</td>
      <td>Clec1b</td>
      <td>0</td>
      <td>S100a4</td>
      <td>4.98E-268</td>
    </tr>
    <tr>
      <td>Acp5</td>
      <td>5.90E-216</td>
      <td>Cd68</td>
      <td>0</td>
      <td>Cd52</td>
      <td>3.67E-267</td>
    </tr>
    <tr>
      <td>Lag3</td>
      <td>3.91E-213</td>
      <td>Axl</td>
      <td>0</td>
      <td>Rps14</td>
      <td>1.94E-266</td>
    </tr>
    <tr>
      <td>Lyz2</td>
      <td>1.28E-209</td>
      <td>Paqr9</td>
      <td>3.32E-307</td>
      <td>Ifitm3</td>
      <td>3.19E-263</td>
    </tr>
    <tr>
      <td>H2-M2</td>
      <td>1.22E-199</td>
      <td>Sdc3</td>
      <td>3.45E-305</td>
      <td>Rpl34</td>
      <td>2.02E-261</td>
    </tr>
    <tr>
      <td>Psap</td>
      <td>7.26E-198</td>
      <td>Myo9a</td>
      <td>5.59E-305</td>
      <td>Rps27a</td>
      <td>3.67E-260</td>
    </tr>
    <tr>
      <td>Gatm</td>
      <td>1.33E-192</td>
      <td>Scp2</td>
      <td>3.79E-302</td>
      <td>Rpl36</td>
      <td>1.54E-259</td>
    </tr>
    <tr>
      <td>Cpd</td>
      <td>1.50E-192</td>
      <td>Selenop</td>
      <td>2.10E-295</td>
      <td>Rps16</td>
      <td>2.55E-258</td>
    </tr>
    <tr>
      <td>C3</td>
      <td>2.34E-187</td>
      <td>Lrp1</td>
      <td>2.08E-294</td>
      <td>Rpl24</td>
      <td>1.37E-257</td>
    </tr>
    <tr>
      <td>Cxcl16</td>
      <td>8.11E-183</td>
      <td>Lap3</td>
      <td>1.45E-290</td>
      <td>Rps9</td>
      <td>6.34E-253</td>
    </tr>
    <tr>
      <td>Lgals3</td>
      <td>1.57E-182</td>
      <td>Marcks</td>
      <td>2.77E-279</td>
      <td>Gpr141</td>
      <td>1.21E-246</td>
    </tr>
    <tr>
      <td>Ube2j1</td>
      <td>1.63E-180</td>
      <td>Glul</td>
      <td>3.64E-279</td>
      <td>Rpl27a</td>
      <td>3.06E-243</td>
    </tr>
    <tr>
      <td>Plxnc1</td>
      <td>9.84E-180</td>
      <td>Hebp1</td>
      <td>3.76E-278</td>
      <td>Rpl17</td>
      <td>8.15E-241</td>
    </tr>
    <tr>
      <td>Stab1</td>
      <td>4.07E-176</td>
      <td>Ear2</td>
      <td>4.53E-276</td>
      <td>Rps24</td>
      <td>1.46E-240</td>
    </tr>
    <tr>
      <td>Cyth1</td>
      <td>3.27E-163</td>
      <td>Apoc1</td>
      <td>2.49E-275</td>
      <td>Rps13</td>
      <td>2.34E-236</td>
    </tr>
    <tr>
      <td>Spsb1</td>
      <td>3.96E-163</td>
      <td>Kcna2</td>
      <td>3.72E-275</td>
      <td>Rpl38</td>
      <td>1.95E-226</td>
    </tr>
    <tr>
      <td>Blnk</td>
      <td>2.35E-162</td>
      <td>Myo10</td>
      <td>9.05E-269</td>
      <td>H2-DMb1</td>
      <td>1.02E-223</td>
    </tr>
    <tr>
      <td>Cx3cr1</td>
      <td>9.29E-162</td>
      <td>Atp13a2</td>
      <td>2.95E-267</td>
      <td>Rps18</td>
      <td>5.39E-223</td>
    </tr>
    <tr>
      <td>Med10</td>
      <td>5.25E-161</td>
      <td>Slc1a3</td>
      <td>6.24E-263</td>
      <td>Rpl19</td>
      <td>3.68E-221</td>
    </tr>
    <tr>
      <td>Nek6</td>
      <td>5.28E-160</td>
      <td>Slco2b1</td>
      <td>1.11E-258</td>
      <td>Rpl8</td>
      <td>2.01E-219</td>
    </tr>
    <tr>
      <td>Ptms</td>
      <td>1.05E-159</td>
      <td>mt-Nd2</td>
      <td>3.45E-258</td>
      <td>Rpl7a</td>
      <td>4.17E-217</td>
    </tr>
    <tr>
      <td>Anxa5</td>
      <td>1.10E-156</td>
      <td>Wwp1</td>
      <td>2.16E-253</td>
      <td>Gm34084</td>
      <td>5.23E-216</td>
    </tr>
    <tr>
      <td>Gpnmb</td>
      <td>1.21E-154</td>
      <td>Aplp2</td>
      <td>4.22E-248</td>
      <td>Rpl13</td>
      <td>2.08E-215</td>
    </tr>
    <tr>
      <td>Itgb5</td>
      <td>2.78E-154</td>
      <td>Atp8a1</td>
      <td>5.03E-248</td>
      <td>Rpl11</td>
      <td>2.47E-213</td>
    </tr>
    <tr>
      <td>Myo5a</td>
      <td>1.11E-146</td>
      <td>P2ry13</td>
      <td>3.17E-247</td>
      <td>Rpl35a</td>
      <td>2.13E-210</td>
    </tr>
    <tr>
      <td>Runx3</td>
      <td>1.81E-146</td>
      <td>Ccdc148</td>
      <td>4.70E-245</td>
      <td>Rpsa</td>
      <td>1.62E-209</td>
    </tr>
    <tr>
      <td>Tmem176a</td>
      <td>2.34E-144</td>
      <td>Grn</td>
      <td>1.58E-244</td>
      <td>Rpl6</td>
      <td>5.70E-208</td>
    </tr>
    <tr>
      <td>Ctss</td>
      <td>4.81E-141</td>
      <td>Bank1</td>
      <td>1.82E-239</td>
      <td>Tpt1</td>
      <td>2.63E-206</td>
    </tr>
    <tr>
      <td>Sh3pxd2b</td>
      <td>9.38E-141</td>
      <td>Mertk</td>
      <td>2.15E-238</td>
      <td>Rack1</td>
      <td>2.14E-203</td>
    </tr>
    <tr>
      <td>Rtcb</td>
      <td>4.42E-140</td>
      <td>Nr1h3</td>
      <td>1.13E-235</td>
      <td>Rpl23</td>
      <td>6.14E-199</td>
    </tr>
    <tr>
      <td>Fam20c</td>
      <td>1.91E-139</td>
      <td>Prnp</td>
      <td>2.93E-235</td>
      <td>Rpl26</td>
      <td>7.48E-198</td>
    </tr>
    <tr>
      <td>Il2rg</td>
      <td>8.84E-138</td>
      <td>Ninj1</td>
      <td>2.42E-234</td>
      <td>Rps6</td>
      <td>6.64E-197</td>
    </tr>
    <tr>
      <td>Lpcat2</td>
      <td>8.53E-137</td>
      <td>Fcna</td>
      <td>3.33E-233</td>
      <td>Rps10</td>
      <td>2.06E-195</td>
    </tr>
    <tr>
      <td>Kynu</td>
      <td>8.49E-136</td>
      <td>Csrp1</td>
      <td>1.16E-230</td>
      <td>Ier5</td>
      <td>1.06E-191</td>
    </tr>
    <tr>
      <td>Tnfsf13b</td>
      <td>8.77E-136</td>
      <td>Rgl1</td>
      <td>7.18E-229</td>
      <td>Rps3</td>
      <td>8.23E-185</td>
    </tr>
    <tr>
      <td>Gpr157</td>
      <td>1.18E-135</td>
      <td>Lpl</td>
      <td>4.94E-223</td>
      <td>Rpl27</td>
      <td>8.23E-185</td>
    </tr>
    <tr>
      <td>Tgfbr1</td>
      <td>7.63E-135</td>
      <td>Fam213b</td>
      <td>1.08E-222</td>
      <td>Rps5</td>
      <td>8.36E-185</td>
    </tr>
    <tr>
      <td>H2-K1</td>
      <td>1.15E-133</td>
      <td>Tcf7l2</td>
      <td>1.26E-222</td>
      <td>Rps7</td>
      <td>3.96E-182</td>
    </tr>
    <tr>
      <td>Basp1</td>
      <td>1.23E-133</td>
      <td>AB124611</td>
      <td>4.64E-221</td>
      <td>Rps15a</td>
      <td>6.82E-182</td>
    </tr>
    <tr>
      <td>Pla2g7</td>
      <td>1.80E-132</td>
      <td>Abcc3</td>
      <td>3.28E-216</td>
      <td>Rps11</td>
      <td>1.97E-180</td>
    </tr>
    <tr>
      <td>Fth1</td>
      <td>4.19E-131</td>
      <td>Fcgrt</td>
      <td>5.79E-216</td>
      <td>Rps4x</td>
      <td>5.07E-180</td>
    </tr>
    <tr>
      <td>Ggh</td>
      <td>1.85E-126</td>
      <td>Tgm2</td>
      <td>1.88E-215</td>
      <td>Rplp0</td>
      <td>3.09E-177</td>
    </tr>
    <tr>
      <td>Adam19</td>
      <td>6.94E-126</td>
      <td>Itgad</td>
      <td>5.35E-214</td>
      <td>Ly6i</td>
      <td>8.17E-176</td>
    </tr>
    <tr>
      <td>C3ar1</td>
      <td>7.35E-125</td>
      <td>Ptgs1</td>
      <td>2.94E-213</td>
      <td>S100a11</td>
      <td>6.23E-175</td>
    </tr>
    <tr>
      <td>Ccl12</td>
      <td>3.37E-123</td>
      <td>Laptm4a</td>
      <td>1.01E-212</td>
      <td>Atox1</td>
      <td>1.22E-174</td>
    </tr>
    <tr>
      <td>Hvcn1</td>
      <td>2.51E-121</td>
      <td>Comt</td>
      <td>1.33E-206</td>
      <td>Pim1</td>
      <td>9.56E-174</td>
    </tr>
    <tr>
      <td>Anxa3</td>
      <td>8.60E-121</td>
      <td>Creg1</td>
      <td>3.24E-205</td>
      <td>Sh3bgrl3</td>
      <td>3.97E-173</td>
    </tr>
    <tr>
      <td>Tgfbi</td>
      <td>1.88E-120</td>
      <td>Adgre1</td>
      <td>9.67E-205</td>
      <td>Ciita</td>
      <td>7.35E-173</td>
    </tr>
    <tr>
      <td>Ctsd</td>
      <td>2.73E-117</td>
      <td>Clec12a</td>
      <td>6.33E-204</td>
      <td>Eef1a1</td>
      <td>6.09E-172</td>
    </tr>
    <tr>
      <td>Itm2c</td>
      <td>5.19E-116</td>
      <td>Tspan4</td>
      <td>7.80E-203</td>
      <td>Rps3a1</td>
      <td>9.09E-168</td>
    </tr>
    <tr>
      <td>Tmem119</td>
      <td>5.62E-116</td>
      <td>Txn1</td>
      <td>9.13E-203</td>
      <td>Gm2a</td>
      <td>6.07E-165</td>
    </tr>
    <tr>
      <td>Rap2a</td>
      <td>1.03E-114</td>
      <td>Ctsb</td>
      <td>9.52E-201</td>
      <td>Ptprc</td>
      <td>2.05E-163</td>
    </tr>
    <tr>
      <td>Ctsl</td>
      <td>4.00E-114</td>
      <td>Mrap</td>
      <td>5.65E-197</td>
      <td>Rpl37</td>
      <td>1.51E-161</td>
    </tr>
    <tr>
      <td>Itga6</td>
      <td>1.83E-113</td>
      <td>Slc16a9</td>
      <td>5.99E-197</td>
      <td>Rps25</td>
      <td>3.03E-160</td>
    </tr>
    <tr>
      <td>B4galnt1</td>
      <td>2.45E-113</td>
      <td>Abcg3</td>
      <td>3.83E-196</td>
      <td>H3f3a</td>
      <td>5.92E-159</td>
    </tr>
    <tr>
      <td>Fam3c</td>
      <td>1.64E-112</td>
      <td>Pla2g15</td>
      <td>4.22E-196</td>
      <td>Btg2</td>
      <td>1.14E-158</td>
    </tr>
    <tr>
      <td>Tmem173</td>
      <td>1.54E-111</td>
      <td>C1qc</td>
      <td>6.17E-192</td>
      <td>Rpl15</td>
      <td>1.42E-158</td>
    </tr>
    <tr>
      <td>Ski</td>
      <td>3.59E-111</td>
      <td>Agpat3</td>
      <td>1.68E-191</td>
      <td>Cnn2</td>
      <td>1.09E-156</td>
    </tr>
    <tr>
      <td>Anpep</td>
      <td>5.85E-111</td>
      <td>Hs6st1</td>
      <td>1.95E-191</td>
      <td>Cdkn1a</td>
      <td>2.57E-156</td>
    </tr>
    <tr>
      <td>Gng2</td>
      <td>2.37E-110</td>
      <td>Dmpk</td>
      <td>2.15E-191</td>
      <td>Slfn1</td>
      <td>4.83E-155</td>
    </tr>
    <tr>
      <td>Nceh1</td>
      <td>2.88E-110</td>
      <td>Cd38</td>
      <td>1.79E-190</td>
      <td>Sem1</td>
      <td>4.08E-154</td>
    </tr>
    <tr>
      <td>H2-Q7</td>
      <td>4.94E-108</td>
      <td>Tmem26</td>
      <td>2.02E-189</td>
      <td>Lsp1</td>
      <td>1.34E-152</td>
    </tr>
    <tr>
      <td>Rtn1</td>
      <td>1.28E-106</td>
      <td>Slc11a1</td>
      <td>1.05E-188</td>
      <td>Rpl37a</td>
      <td>1.78E-152</td>
    </tr>
    <tr>
      <td>Sorl1</td>
      <td>1.31E-103</td>
      <td>Cd300a</td>
      <td>1.41E-187</td>
      <td>Rpl22</td>
      <td>3.64E-152</td>
    </tr>
    <tr>
      <td>Glipr1</td>
      <td>1.22E-102</td>
      <td>Slc7a7</td>
      <td>3.28E-187</td>
      <td>Sirpb1c</td>
      <td>4.81E-152</td>
    </tr>
    <tr>
      <td>Gsn</td>
      <td>2.00E-102</td>
      <td>Cyb5a</td>
      <td>6.94E-187</td>
      <td>Traf1</td>
      <td>6.97E-152</td>
    </tr>
    <tr>
      <td>Afdn</td>
      <td>4.54E-102</td>
      <td>Sipa1l1</td>
      <td>7.41E-187</td>
      <td>Emb</td>
      <td>4.22E-151</td>
    </tr>
    <tr>
      <td>Ak2</td>
      <td>1.11E-101</td>
      <td>Il18bp</td>
      <td>1.48E-186</td>
      <td>Rpl30</td>
      <td>1.32E-147</td>
    </tr>
    <tr>
      <td>Ntpcr</td>
      <td>2.21E-98</td>
      <td>Cd86</td>
      <td>2.52E-183</td>
      <td>Rps15</td>
      <td>1.14E-146</td>
    </tr>
    <tr>
      <td>Scarb2</td>
      <td>3.16E-97</td>
      <td>Vamp5</td>
      <td>3.05E-183</td>
      <td>H2-Ab1</td>
      <td>2.84E-145</td>
    </tr>
    <tr>
      <td>Creb5</td>
      <td>5.41E-97</td>
      <td>Jup</td>
      <td>6.69E-182</td>
      <td>Il1b</td>
      <td>3.05E-145</td>
    </tr>
    <tr>
      <td>Gsto1</td>
      <td>5.56E-97</td>
      <td>Blvra</td>
      <td>1.30E-178</td>
      <td>Rps28</td>
      <td>4.52E-145</td>
    </tr>
    <tr>
      <td>Ncf1</td>
      <td>4.26E-96</td>
      <td>Mgst1</td>
      <td>6.48E-178</td>
      <td>Jarid2</td>
      <td>1.82E-143</td>
    </tr>
    <tr>
      <td>Ppfia4</td>
      <td>4.97E-96</td>
      <td>Tbxas1</td>
      <td>1.47E-177</td>
      <td>Rps26</td>
      <td>1.53E-142</td>
    </tr>
    <tr>
      <td>Chchd10</td>
      <td>7.77E-96</td>
      <td>Hpgds</td>
      <td>2.04E-177</td>
      <td>Rpl32</td>
      <td>4.21E-142</td>
    </tr>
    <tr>
      <td>Gna12</td>
      <td>1.23E-95</td>
      <td>Tgfbr2</td>
      <td>2.70E-176</td>
      <td>Pld4</td>
      <td>9.07E-142</td>
    </tr>
    <tr>
      <td>Mvb12b</td>
      <td>1.80E-95</td>
      <td>Clec4n</td>
      <td>3.52E-175</td>
      <td>Cbfa2t3</td>
      <td>1.54E-141</td>
    </tr>
    <tr>
      <td>Rasal3</td>
      <td>1.45E-94</td>
      <td>Ms4a7</td>
      <td>5.30E-175</td>
      <td>Rps21</td>
      <td>4.04E-141</td>
    </tr>
    <tr>
      <td>Scoc</td>
      <td>6.86E-94</td>
      <td>Sirpa</td>
      <td>3.35E-171</td>
      <td>Fgr</td>
      <td>4.04E-141</td>
    </tr>
    <tr>
      <td>Cfb</td>
      <td>6.00E-93</td>
      <td>Fyn</td>
      <td>2.84E-168</td>
      <td>Rps8</td>
      <td>1.11E-139</td>
    </tr>
    <tr>
      <td>Lmna</td>
      <td>1.04E-92</td>
      <td>Cadm1</td>
      <td>2.20E-167</td>
      <td>Cd74</td>
      <td>5.34E-138</td>
    </tr>
  </tbody>
</table>

### Yolk-sac progenitors contribute to embryonic thymic macrophages

The ontogeny of thymic macrophages has been examined by only one study since the realization that many tissue-resident macrophages are descendants of embryonic progenitors (Tacke et al., 2015). Based on Flt3Cre fate-mapping, the authors concluded that most adult thymic macrophages derive from HSCs. To determine if YS progenitors contribute to embryonic thymic macrophages, we used Cx3cr1CreER fate mapping (Yona et al., 2013). Injection of 4-OHT at E9.5 in ROSA26LSL-GFP mouse mated with a Cx3cr1CreER male permanently tags YS progenitors and their descendants with GFP (Figure 5A). Indeed, E19.5 microglia that are exclusively derived from YS progenitors were labeled to a high degree (Figure 5B). After adjusting for incomplete labeling based on the microglia, we found that at E15.5 >50% of thymic macrophages were fate mapped, i.e., from YS origin (Figure 5C). However, GFP+ thymic macrophages decreased to just ~11% at E19.5, suggesting that YS progenitors establish the embryonic thymic macrophage pool but are quickly replaced by subsequent wave(s) of macrophages.

![Figure 5.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig5-v2.jpg)

**Figure 5.:** (A) Scheme of the YS-progenitor labeling experiments. E9.5 pregnant ROSA26LSL-GFP mice mated with Cx3cr1CreER males were injected with 4-hydroxytamoxifen (4-OHT) and sacrificed at E15.5 or E19.5. (B) Representative flow cytometry plots of the Cx3cr1GFP expression in microglia (CD45+CD11b+ cells in the brain) and ThyMacs of the pups at E19.5. (C) Frequencies of GFP+ ThyMacs at E15.5 and E19.5 adjusted to the degree of labeling of microglia. (D) Scheme of the shield chimera experiments. Congenic CD45.2 mice were lethally irradiated with their upper body protected by a 5-cm thick lead shield and then injected with CD45.1+ bone marrow. (E) Representative flow cytometric analysis of CD115+CD11b+ blood monocytes, TIM4+ and TIM4− ThyMacs for donor-derived (CD45.1+) and host-derived (CD45.2+) cells. Non-chimeric CD45.1 and CD45.2 samples serve as controls for the gating. (F) Frequencies of donor-derived blood monocytes, TIM4+ and TIM4− ThyMacs. (G) Scheme of the thymus transplantation experiments. Embryonic thymuses from E15.5 SpicGFP+ CD45.2+ mice were transplanted under the kidney capsule of CD45.1+ mice and analyzed 6 weeks later. (H) Representative flow cytometry plots of donor- (CD45.2+) vs. host (CD45.1+)-derived TIM4+ and TIM4− ThyMacs in the transplanted thymus. The host thymus (endogenous thymus) serves as a negative control. (I) Frequencies of CD45.2+ (donor-derived) cells among TIM4+ and TIM4− ThyMacs in the transplanted and endogenous thymuses of the mice. Data in C, F, and I are mean ± SEM with two litters, seven, and five mice per group, respectively. The numbers in the flow cytometry plots are the percent of cells in the respective gates. Each symbol in the graphs is an individual mouse or embryo.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** The host thymus (endogenous thymus) serves as a negative control. To the right is a graph showing the mean ± SEM of the frequencies of CD45.2+ (donor-derived) cells among thymocytes in the transplanted and endogenous thymuses of the mice. Each dot is an individual mouse. The numbers in the flow cytometry plots are the percent of cells in the respective gate.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** The endogenous thymus serves as background control. Only populations comprising >5% of thymic macrophages are shown. Each dot is an individual mouse. The data are presented as mean ± SEM.

### Differential contribution of adult bone marrow-derived monocytes to the two thymic macrophage populations

To investigate the possibility that thymic macrophages arise from adult bone marrow-derived monocytes, we devised two complementary experiments. First, we evaluated the contribution of circulating adult monocytes to thymic macrophages without the confounding effect of radiation damage on the thymus. We created shield chimeras by subjecting CD45.2 mice to a lethal dose of irradiation while protecting their upper body and the thymus with a 5-cm lead shield, followed by reconstitution with CD45.1 bone marrow (Figure 5D). We analyzed Timd4+ and Cx3cr1+ thymic macrophages separately after 6 weeks because we suspected they might have different origins. As CX3CR1 protein expression was low on thymic macrophages (Figure 5B), we defined the Cx3cr1+Timd4− population as TIM4−. The donor-derived monocytes in the blood were, on average, 57%, but less than 2% of TIM4+ thymic macrophages were CD45.1+ (Figure 5E and F), suggesting very limited contribution of adult circulating monocytes to the TIM4+ macrophage pool. The percentage of HSC-derived TIM4− macrophages (on average 23%) was intermediate between the monocytes and TIM4+ macrophages, pointing out that a sizeable part of TIM4− cells was derived from adult HSCs.

We also transplanted E15.5 thymuses from SpicGFP+ CD45.2 embryos under the kidney capsule of adult CD45.1 mice and analyzed them 6 weeks later (Figure 5G). By that time, >99% of thymocytes in the transplanted thymus were derived from CD45.1+ host HSCs, indicating successful replacement by HSC-derived progenitors (Figure 5—figure supplement 1). TIM4− thymic macrophages were derived entirely from host HSCs, just like thymocytes. In contrast, most TIM4+ cells (on average 70%) were donor-derived (Figure 5Hand I). Moreover, only CD45.2+ TIM4+ macrophages expressed SpicGFP (Figure 5—figure supplement 2). As expected, thymic macrophages in the endogenous thymus were all CD45.1+. The results from our transplantation experiments show that the progenitors of most TIM4+ thymic macrophages are of embryonic origin, while TIM4− cells are derived from adult monocytes. Altogether our results suggest that the two populations of thymic macrophages have different origins. TIM4+ cells are derived from embryonic precursors and can survive long term without much contribution from adult HSC and monocytes. In contrast, TIM4− thymic macrophages rely mostly on adult HSCs for their generation and replacement.

### Thymic macrophages can proliferate in situ

TIM4+ macrophages can persist for many weeks in the thymus without constant replacement from blood monocytes, suggesting they can divide in situ. Staining for the proliferation marker Ki67 revealed that ~4% of all thymic macrophages expressed this marker compared to an isotype control (Figure 6A and B). To prove that thymic macrophages are proliferative, we tested the incorporation of the nucleotide analog 5-ethynyl-2’-deoxyuridine (EdU). Short-term EdU labeling experiments unexpectedly revealed that thymic macrophages become EdU+ with faster kinetics than thymocytes (Figure 6—figure supplement 1). The most likely explanation for this puzzling result is that some of the thymic macrophages have engulfed apoptotic thymocytes that have recently divided and incorporated EdU. Thus, EdU could have accumulated in these macrophages through phagocytosis, not cell division. To circumvent this caveat, we designed a pulse-chase experiment (Figure 6C). Mice were injected daily with EdU for 21 days so that all cells that proliferated in that period would incorporate the label. Most thymocytes and thymic macrophages became EdU+ at d. 21 (Figure 6D). After 21 more days of ‘chase period’, only ~0.2% of thymocytes had retained the EdU label, consistent with the existence of a tiny population of long-term resident thymocytes consisting mainly of regulatory T cells and NKT cells (McCaughtry et al., 2007; Figure 6D and E). However, ~5% of the thymic macrophages were EdU+, suggesting they divided during the labeling period. We also sorted thymic macrophages and subjected them to cell cycle analysis. Although almost all thymic macrophages were in G0/G1 phase, a small population of ~3% was in the G2/M phase of the cell cycle (Figure 6F and G). Surprisingly, most Mki67+ thymic macrophages belonged to the Cx3cr1+ subset, and only a few of the Timd4+ cells were positive (Figure 6H). We confirmed this result from the scRNA-Seq analysis experimentally. The expression of Ki-67 was significantly higher in TIM4− than in TIM4+ thymic macrophages (Figure 6G), suggesting that the former is the more proliferative subset. Collectively, four independent approaches documented that a small proportion (3–5%) of thymic macrophages are actively dividing under homeostatic conditions within the thymus. The majority of the dividing cells were from the adult HSC-derived Cx3cr1+ subset. Timd4+ macrophages were primarily quiescent.

![Figure 6.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig6-v2.jpg)

**Figure 6.:** (A) Example flow cytometry plots of Ki67 staining of ThyMacs. (B) Frequency of Ki67+ ThyMacs. (C) Scheme of 5-ethynyl-2’-deoxyuridine (EdU) pulse/chase experiment: mice were injected daily with 1 mg EdU i.p. for 21 days and rested for 21 more days. (D) Example flow cytometry plots of EdU staining of thymocytes (upper row) and ThyMacs (lower row). (E) Frequencies of EdU+ cells among thymocytes (top graph) and ThyMacs (bottom graph). (F) Example flow cytometry plot of cell cycle analysis of FACS-sorted ThyMacs. (G) Frequencies of ThyMacs in different stages of the cell cycle. (H) UMAP plot of Mki67 expression in Mafb-positive clusters from the single-cell RNA-sequencing data described in Figure 4. (I) Comparison of Ki67 protein expression in TIM4+ and TIM4− ThyMacs. The expression is measured as the difference of the geometric mean fluorescent intensities of the Ki67 antibody staining and isotype control (ΔgMFI). The numbers in the flow cytometry plots are the percent of cells in the respective gates. Data are mean ± SEM from three mice (B and G) or five mice (I), or six to seven individual mice (E). Each dot is an individual mouse. Statistical significance in (I) was determined by unpaired Student’s t-test.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** The numbers inside flow plots are the percentage of EdU+ cells from mice injected with EdU. Data are representative of three independent experiments.

### Cx3cr1+ cells give rise to Timd4+ cells during embryonic development

To determine if the two populations of thymic macrophages are related, we first analyzed the kinetics of their appearance during embryonic development. At the earliest time point (E14.5), all thymic macrophages were Cx3cr1+, and only ~20% were also TIM4+ (Figure 7A and B). The proportion of TIM4+ cells increased at E17.5, and TIM4+Cx3cr1− cells started to appear. In the neonatal period, almost all macrophages were TIM4+, and very few remained TIM4−. The proportion of TIM4− cells increased in 6 weeks old mice, but TIM4+ macrophages remained the dominant population. These kinetics (Figure 7C) are consistent with Timd4+ macrophages developing from Cx3cr1+ cells before birth. Another plausible scenario is that distinct progenitors give rise to different thymic macrophage populations (e.g. YS progenitors give rise to Cx3cr1+Timd4−, and HSC-derived progenitors develop into Timd4+ macrophages). To test the latter hypothesis, we revisited the fate mapping of YS progenitors (Figure 5A). Although a larger part (~60% at E15.5) of fate-mapped cells was Cx3cr1+TIM4− cells (Figure 7D), a substantial proportion (~40% at E15.5) of fate-mapped TIM4+ macrophages could clearly be identified at both E15.5 and E19.5, suggesting that YS progenitors can give rise to both Cx3cr1+ and Timd4+ cells. Thus, the simplest explanation for our findings is that Timd4+ cells develop from Cx3cr1+ cells during embryonic development. This transition is complete in the first week after birth as there were essentially no Cx3cr1+TIM4− thymic macrophages remaining at d.7 (Figure 7A and B). To formally demonstrate that Cx3cr1+ macrophages can give rise to Timd4+ cells during embryonic development, we injected 4-OHT in E15.5 pregnant females carrying Cx3cr1CreER × ROSA26LSL-GFP fetuses (Figure 7E). At this time almost all thymic macrophages are Cx3cr1+ (Figure 7A). Just before birth, at E19.5, we could identify a sizeable population of TIM4+CX3CR1− among fate-mapped cells, suggesting that they originate from Cx3cr1+ progenitors (Figure 7F and G).

![Figure 7.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig7-v2.jpg)

**Figure 7.:** (A) Example flow cytometry plots for the expression of Cx3cr1GFP and TIM4 on thymic macrophages at different times during embryonic development (E14.5, E17.5), immediately after birth, at 7 days, and 6 weeks of age. (B) Frequencies of Timd4+Cx3cr1− (Timd4 single-positive or Timd4SP), Timd4+Cx3cr1+ (double-positive or DP), and Cx3cr1+Timd4− (Cx3cr1 single-positive or Cx3cr1SP) thymic macrophages at the indicated time points. (C) Kinetics of the changes in different subpopulations of thymic macrophages from E14.5–6 weeks. (D) Frequencies at E15.5 and E19.5 of GFP-labeled cells among TIM4+ or TIM4− cells in Cx3cr1CreER × ROSA26LSL-GFP embryos treated with 4-OHT at E9.5. (E) Scheme of the fate-mapping experiments showing the relationship between Cx3cr1+ and Timd4+ thymic macrophages during embryonic development. E15.5 pregnant ROSA26LSL-GFP mice mated with Cx3cr1CreER males were injected with 4-hydroxytamoxifen (4-OHT) and sacrificed at E19.5. (F) Representative flow cytometry staining for TIM4 and CX3CR1 in fate-mapped GFP+ thymic macrophages at E19.5. The panel to the right is the isotype control for CX3CR1-PE staining. (G) Frequencies of TIM4+CX3CR1− cells among fate-mapped GFP+ macrophages. Data are shown as meanSEM and are from at least two independent experiments for each panel. Each symbol is an individual mouse or embryo.

### Cx3cr1+ thymic macrophages slowly accumulate with age at the expense of Timd4+ cells

To understand the dynamics of the two resident thymic macrophage populations with age, we induced recombination in Cx3cr1CreER × ROSA26LSL-GFP mice during the neonatal period (Figure 8A) or at 6 weeks of age (Figure 8C) and compared the proportion of GFP+ cells 3 and 42 days after labeling. The extent of labeling of TIM4+ thymic macrophages did not change within these 6 weeks, no matter whether the mice were treated with tamoxifen in the first week after birth or at 6 weeks (Figure 8B and D), suggesting an absence of a significant influx from unlabeled cells (e.g. monocytes). In contrast, the proportion of labeled TIM4− thymic macrophages decreased significantly 6 weeks after tamoxifen injection in neonatal and adult mice, suggesting that this population was diluted by unlabeled cells. To further substantiate these findings, we examined older WT mice and found out that the proportions of TIM4− thymic macrophages increased with age, and in mice >8 months old, they accounted for ~70% of all macrophages in the organ (Figure 8E). As these changes in the proportions of the thymic macrophage subpopulations occurred at the background of thymic involution, we wanted to know if the accumulation of TIM4− cells was only relative or also in absolute cell numbers. In contrast to TIM4+ thymic macrophages that reached peak numbers at an early age and then declined significantly, TIM4− cells tended to increase their numbers in older mice (Figure 8F). Thus, we conclude that, after birth, the numbers of TIM4+ macrophages follow the kinetics of the thymus size – increase in young and decrease in old mice, and they are not replaced by other cells. In contrast, since the first week of life, Cx3cr1+ cells are recruited to the thymus, accumulate with age, and in old mice, form the predominant phagocytic population in the organ.

![Figure 8.](https://cdn.elifesciences.org/articles/75148/elife-75148-fig8-v2.jpg)

**Figure 8.:** (A) Scheme of the neonatal fate mapping: A nursing dam was injected twice with tamoxifen (Tam) or vehicle (Veh) in the first week after giving birth to Cx3cr1CreER × ROSA26LSL-GFP pups. The mice were sacrificed 3 or 42 days after the last injection, and the degree of labeling of TIM4+ and TIM4− ThyMacs was examined by flow cytometry. (B) Frequencies of GFP+ TIM4+ or TIM4− ThyMacs from neonatally fate-mapped mice after 3 and 42 days. Vehicle-injected nursing dam litters (Veh) served as a control for non-specific labeling. (C) Scheme of the adult fate mapping: Six weeks old Cx3cr1CreER × ROSA26LSL-GFP mice were injected twice with Tam or Veh. The mice were sacrificed 3 or 42 days after the last injection, and the degree of labeling of TIM4+ and TIM4− ThyMacs was examined by flow cytometry. (D) Frequencies of GFP+ TIM4+ or TIM4− ThyMacs from adult fate-mapped mice after 3 and 42 days. (E) Frequencies of TIM4− ThyMacs at different ages. (F) Changes in the numbers of TIM4− and TIM4+ ThyMacs with age. The data are mean ± SEM from two independent experiments (B) or at least three individual mice per time point (D, E, and F). Each symbol is an individual mouse. Statistical significance in the difference between Tam-treated samples at different time points was determined with unpaired Student’s t-test (B and D). One-way ANOVA was used to assess the significance of the change in TIM4+ and TIM4− ThyMacs percentages and numbers with age (E and F).

## Discussion

Here, we have described the phenotype, transcriptional profile, localization, diversity, ontogeny, and maintenance of macrophages in the thymus. These cells express the typical macrophage markers CD64, MerTK, and F4/80 and are transcriptionally most similar to splenic red pulp macrophages and liver Kupffer cells. However, they have a unique expression profile dominated by genes involved in antigen presentation and lysosomal degradation. We found that thymic macrophages consist of two populations with distinct localization. Timd4+ macrophages occupied the cortex, while Cx3cr1+ cells were located in the medulla and the cortico-medullary junction. While YS-derived macrophages dominated the early stages of thymus development, they were quickly replaced by non-YS embryonic progenitors that gave rise to the Timd4+ thymic macrophages that persisted into adulthood and formed the main macrophage population in young mice. Cx3cr1+ macrophages slowly accumulated after birth and became the most abundant population in old mice.

Altogether our data depict thymic macrophages as typical tissue-resident macrophages originating from multiple hematopoietic waves, surviving long term, and expressing the core macrophage-specific genes. They are most similar transcriptionally to splenic red pulp macrophages and Kupffer cells, which is not surprising considering that they all specialize in efferocytosis and have efficient lysosomal degradation machinery. These three populations also shared expression of the TF Spic that is induced by heme released following red blood cells phagocytosis (Haldar et al., 2014). However, the thymus is not known as a place for erythrocyte degradation. Thus, the mechanism for Spic up-regulation in thymic macrophages is unclear.

The unique features of thymic macrophages include high expression of genes involved in the IFN-I pathway, antigen presentation, and lysosomal degradation. The up-regulation of IFN-I-stimulated genes such as Stat1, Stat2, Irf7, and Irf8 can be explained by the constitutive secretion of IFN-I by thymic epithelial cells (Lienenklaus et al., 2009; Otero et al., 2013). The purpose of IFN-I expression in the thymus in the absence of a viral infection is unclear. Still, one possibility is that it mediates negative selection to IFN-dependent genes as part of central tolerance.

Thymic macrophages highly express molecules involved in antigen presentation, including MHC1 and MHC2, although the latter is expressed at lower levels than in cDCs, and are functionally competent to induce T cell activation. Thus, they have the potential to present antigens for both negative selection and agonist selection. These two activities have traditionally been assigned solely to cDCs (Breed et al., 2018). However, recent evidence suggests that negative selection is most efficient when the cell that presents the antigen to an auto-reactive thymocyte is also the one that phagocytoses it (Kurd et al., 2019). So, macrophages’ participation in thymocyte selection needs to be re-evaluated.

The extraordinary ability of thymic macrophages to engulf and degrade apoptotic thymocytes has been appreciated for a long time (Surh and Sprent, 1994), and our RNA-Seq data provides additional supporting evidence for this function by highlighting the up-regulation of pathways involved in lysosomal degradation. Moreover, we recently showed that the pentose phosphate pathway has a central role in buffering the efferocytosis-associated oxidative stress in thymic macrophages (Tsai et al., 2022). An interesting topic for future research would be understanding how the metabolites derived from apoptotic cells are returned to the microenvironment to support the proliferation of immature thymocytes. A SoLute Carrier (Slc) genes-based program has been described in vitro (Morioka et al., 2018), but its relevance to tissue-resident macrophages remains to be determined. Altogether, our study demonstrates that thymic macrophages are a unique subset of tissue-resident macrophages and support the idea that resident macrophage phenotype is determined by the combination of ontogeny, microenvironment, and other factors (Blériot et al., 2020).

Together with the study by Tacke et al., 2015, our work builds the following model for thymic macrophage origin: thymic macrophages develop in three distinct waves: YS-derived progenitors dominate the early stages of thymus development but are replaced before birth by a second wave of YS-independent embryonic progenitors that forms the bulk of thymic macrophages after birth and can self-maintain into adulthood. With age, there is a slow and steady influx of Timd4−Cx3cr1+ macrophage precursors that occupy the medulla and cortico-medullary junction, becoming the major phagocytic population in the thymus of older mice (>8 months). The second wave of YS-independent macrophages is most likely the progeny of embryonic HSCs based on Flt3Cre fate mapping that showed that >80% of thymic macrophages in adult mice are descendants of HSCs (Tacke et al., 2015), whether HSC-independent fetal liver monocytes contribute to thymic macrophages and to what extent awaits the creation of models that can specifically target this population of progenitors. Recruitment of circulating monocytes to the resident macrophage pool in the thymus has been ruled out previously by parabiosis and Ccr2−/− mice (Tacke et al., 2015). Our shield chimera experiments have arrived at similar conclusions. However, the relatively short duration of these experiments and their focus on the bulk thymic macrophages has prevented the recognition of the gradual accumulation of Timd4− macrophages. Once we zoomed in on this minor cell population in young mice, the fate mapping clearly showed an influx of unlabeled progenitors. Whether the progenitors of Timd4− macrophages are monocytes remains to be formally demonstrated. However, monocytes have been singled out as the source of all macrophage populations exhibiting replacement in adults examined to date (Molawi et al., 2014; Goldmann et al., 2016; Jacome-Galarza et al., 2019; Tamoutounour et al., 2013; Bain et al., 2014; Bain et al., 2016). An alternative possibility involves thymocyte progenitors that, under certain circumstances, have been shown to differentiate into macrophages and granulocytes in the thymus (Wada et al., 2008; Bell and Bhandoola, 2008). However, if this occurs in unmanipulated mice at a steady state remains unclear.

We observed interesting dynamics of the Cx3cr1+ macrophages in the thymus. Thymic macrophage progenitors are initially Cx3cr1+ during the embryonic period but gradually down-regulate this chemokine receptor and up-regulate Timd4 so that by day 7 after birth, there are almost no Cx3cr1+Timd4− cells remaining. Cx3cr1+Timd4− macrophages start to increase after the neonatal stage, but these cells come from an entirely different source – adult hematopoietic cell-derived progenitors – and slowly accumulate in the medulla with time so that by 6–8 months, they are the majority of the resident macrophages in that tissue. Both YS-derived primitive macrophages and fetal liver monocytes express Cx3cr1 (Hoeffel et al., 2012; Mass et al., 2016). However, the tissue-resident macrophages in some organs (e.g. Kupffer cells, alveolar macrophages, red pulp macrophages, and Langerhans cells) lose Cx3cr1 expression similar to thymic macrophages, while the macrophages in the intestines, aorta, kidney, dermis, lymph node T cell zone, and microglia do not (Yona et al., 2013; Tamoutounour et al., 2013; Ensan et al., 2016; Baratin et al., 2017). Similar processes may occur in other tissues where the embryonic macrophages transition to a Cx3cr1− phenotype and are slowly replaced by monocyte-derived cells with age. However, detailed time-course analyses of Cx3cr1 expression starting before birth and extending to very old (1 year) mice coupled with lineage tracing would be necessary to document if this transition takes place.

The spatial segregation of the two macrophage populations in the thymus implies that they might have distinct functions. Timd4+ cells are restricted to the cortex and are particularly abundant in the deeper cortex, close to the medulla. Both positive and negative selection of thymocytes occur there, so we speculate that Timd4+ macrophages might be specialized in efferocytosis of CD4+CD8+ (double-positive) thymocytes that cannot interact with cortical thymic epithelial cells and die by neglect or are auto-reactive and undergo clonal deletion in the cortex (Stritesky et al., 2013). On the other hand, Cx3cr1+ macrophages accumulate in the medulla – the thymic region specialized in negative selection to tissue-restricted antigens (TRAs). They might contribute to the process in several ways: (1) by carrying TRAs from blood and peripheral organs. A similar process has been described for cDC2 (SIRPα+ DCs) (Bonasio et al., 2006; Baba et al., 2009). In fact, Cx3cr1+ thymic macrophages could have contributed to this role because they were not distinguished from cDC2 in this study. (2) By capturing TRAs from Aire+ medullary thymic epithelial cells and presenting them to auto-reactive thymocytes as shown for DCs (Gallegos and Bevan, 2004; Koble and Kyewski, 2009; Vobořil et al., 2020). (3) By phagocytosing apoptotic TRA-specific medullary thymocytes, a process we have observed before (Kurd et al., 2019). The exact involvement of thymic macrophages in the selection events in the thymus remains to be determined.

The accumulation of the Cx3cr1+ cells in older mice has clear implications for thymus aging. One key feature of thymus involution is the accumulation of extracellular matrix produced by fibroblasts and the emergence of white adipocytes (Dixit, 2012). A well-recognized driver of fibrosis is TGFβ1 (Budi et al., 2021) that is induced by efferocytosis in macrophages (Huynh et al., 2002). Tgfb1 was highly expressed in thymic macrophages. However, its expression was the highest in the Timd4+ subset (Figure 4—figure supplement 4). This expression pattern casts some doubt that this molecule is the primary driver of extracellular matrix accumulation during thymic involution because Timd4+ macrophages peak in young mice (Figure 8F). At that time, there is minimal extracellular matrix in the cortex where these cells reside. In addition, during thymic involution, the number of these cells declines significantly. The clear correlation between the accumulation of Cx3cr1+ thymic macrophages and thymic involution suggests that some factor(s) produced exclusively by these cells would be more relevant. For example, Cx3cr1+ thymic macrophages are the predominant producer of the growth factor PDGFα (Figure 4G) that is required for the maintenance of adipocyte stem cells and can stimulate tissue fibrosis (Rivera-Gonzalez et al., 2016; Olson and Soriano, 2009). The gradual accumulation of Cx3cr1+ macrophages could increase the availability of PDGFα in the aging thymus stimulating extracellular matrix production and differentiation of precursors into adipocytes. This model predicts that limiting the influx of Cx3cr1+ macrophage precursors could delay thymus involution.

Recent work described a novel phagocytic and antigen-presenting cell type in the thymus called monocyte-derived DCs (Vobořil et al., 2020). The phenotype of these cells overlaps with the CD64+F4/80loCD11b+ cells in our study. However, we favor the classification of these cells as monocytes based on their expression of Mafb, CD64, and Ly6C and lack of expression of the defining DC TF Zbtb46 (Figure 4B and D; Satpathy et al., 2012). As monocytes can differentiate into cDC2, particularly in the context of inflammation (Guilliams et al., 2018), the precise identity and relationship of this population to thymic cDC2 remain to be established.

In the past several years, scRNA-Seq has come to the forefront of biologists’ efforts to disentangle the cellular diversity of tissues. Several comprehensive studies have included samples from mouse or human thymus (Han et al., 2018; Tabula et al., 2018; Tabula, 2020). However, too few thymic macrophages were sampled in these studies to give meaningful clustering results. Efforts specifically targeting the thymus have provided considerably more information (Kernfeld et al., 2018; Park et al., 2020), but macrophage diversity was still not recognized. Characterization of rare populations such as thymic macrophages (~0.1% of all cells in the thymus) requires optimized enzymatic digestion procedures and enrichment strategies, as has already been demonstrated for thymic epithelial cells (Bornstein et al., 2018; Bautista et al., 2021). Our scRNA-Seq dataset provides a rich resource for the unbiased characterization of myeloid cells in the thymus and will greatly aid in the understanding of the myeloid landscape of the thymus.

In summary, our work comprehensively characterizes macrophages in the thymus and paves the way for the exploration of their functions.

## Materials and methods

### Mice

C57BL/6Narl (CD45.2) mice were purchased from the National Laboratory Animal Center, Taipei, Taiwan (NLAC stock# RMRC11005). MAFIA (MAcrophage Fas-Induced Apoptosis, Jackson Labs stock# 005070) (Burnett et al., 2004), Cx3cr1GFP (Jackson Labs stock# 005582) (Jung et al., 2000), SpicGFP (Jackson Labs stock# 025673) (Haldar et al., 2014), Cx3cr1CreER (Jackson Labs stock# 020940) (Yona et al., 2013), and B6.SJL-Ptprca Pepcb/BoyJ (CD45.1, Jackson Labs stock# 002014) mice were purchased from the Jackson Laboratories. Cd11cYFP (Jackson Labs stock# 008829) (Lindquist et al., 2004) and Lyz2GFP (Faust et al., 2000) mice have been described. Mice ubiquitously expressing GFP from the ROSA26 locus were generated by breeding PdgfraCre (Jackson Labs stock# 013148) (Roesch et al., 2008) and ROSA26LSL-ZsGreen (also known as ROSA26LSL-GFP or Ai6, Jackson Labs stock# 007906) mice (Madisen et al., 2010) (both from the Jackson Laboratories). A mouse from this cross was identified, in which the STOP cassette was deleted in the germline. It was designated ROSA26GFP and subsequently bred to C57BL/6 mice. All mice were used at 4–10 weeks of age unless otherwise specified. Mice were bred and maintained under specific pathogen-free conditions at the animal facility of National Yang Ming Chiao Tung University (NYCU). All experimental procedures were approved by the Institutional Animal Care and Use Committee (IACUC) of NYCU.

### Treatment with 5-ethynyl-2’-deoxyuridine

Mice were i.p. injected with 1 mg EdU (Carbosynth) dissolved in PBS daily for 21 days and then rested for 21 more days. Cells from the thymus were harvested on day 21 or 42. In some experiments, the mice were sacrificed 2 hr after the first EdU injection.

### Shield chimera generation

WT (CD45.2) mice were anesthetized by i.p. injection of 120 µg/g body weight Ketamine hydrochloride (Toronto Research Chemicals) and 12 µg/g body weight Xylazine hydrochloride (Sigma). Anesthetized mice were taped to a 5-cm thick lead block so that the lead block covered the head and the chest down to the bottom of the rib cage. Then, they were irradiated with a lethal dose (1000 rad) from a 137Cs source (Minishot II, AXR) so that only their abdomen and hind legs were exposed. After recovery from anesthesia, the mice were transfused i.v. with 107 bone marrow cells from a congenic (CD45.1) donor. Then, they were given trimerin (0.5 mg/mL sulfadiazine + 0.1 mg/mL trimethoprim, China Chemical and Pharmaceutical Co., Tainan, Taiwan) in the drinking water for the first 2 weeks after the irradiation and analyzed after 6 weeks.

### Cell isolation from thymus, blood, and peritoneal cavity

Thymocytes were obtained by mechanical disruption of the thymus with a syringe plunger. For myeloid cell isolation, mouse thymuses were cut into small pieces and digested with 0.2 mg/mL DNase I (Roche) and 0.2 mg/mL collagenase P (Roche) in complete DMEM for 20 min at 37°C with frequent agitation. In some experiments, thymic myeloid cells were enriched by 57% Percoll PLUS (GE Healthcare) discontinuous gradient centrifugation at 4°C, 1800 rpm, for 20 min without brake. Cells at the interface were collected and washed with PBS to remove residual silica particles. Then the cells were resuspended in PBS with 0.5% BSA (HM Biological), filtered through a 70 µm filter, and kept on ice.

Blood was isolated by cardiac puncture of sacrificed mice and immediately diluted with PBS. After centrifugation, the cell suspensions were treated with ammonium chloride-potassium lysis buffer for 3 min on ice once or twice. Peritoneal cavity cells were obtained by lavage with 5 mL PBS + 2 mM EDTA (Merck). Following gentle massage, the cavity was opened with an abdominal incision, and lavage fluid was collected.

### Flow cytometry

Single-cell suspensions (0.5–2×106 cells) from thymus, blood, or peritoneal cavity were blocked with supernatant from 2.4G2 hybridoma (a kind gift by Dr. Fang Liao, Academia Sinica, Taipei, Taiwan) and stained with fluorochrome- or biotin-labeled antibodies for 20 min on ice in PBS + 0.5% BSA + 2 mM EDTA + 0.1% NaN3 (FACS buffer). The following antibodies were used: CD11b (clone M1/70), MHC2 (M5/114.15.2), CD11c (N418), F4/80 (BM8), CD115 (AFS98), SIRPα (P84), CD45 (30-F11), NK1.1 (PK136), TIM4 (RMT4-54), Gr-1 (RB6-8C5), CD64 (X54-5/7.1), Siglec H (551), Ly6C (HK1.4), CD3ε (145–2 C11), CD8α (53–6.7), CD19 (6D5), B220 (RA3-6B2), CD4 (GK1.5), CD51 (RMV-7), CD45.1 (A20), CD45.2 (104), CX3CR1 (SA011F11), and EpCAM (G8.8) from BioLegend; Axl (MAXL8DS), MerTK (DS5MMER), and Ki67 (SolA15) were from eBioscience; Siglec F (E50-2440), CD90.2 (30-H12), and CD11c (HL3) were from BD Biosciences. Cells were washed, and if necessary, incubated for 20 more minutes with fluorochrome-labeled streptavidin: streptavidin-AF647 (Jackson Immunoresearch) or streptavidin-APC/cy7, streptavidin-BV421, streptavidin-BV605 (BioLegend). After the last wash, the cells were resuspended in FACS buffer containing DAPI (BioLegend), Propidium Iodide (Sigma), or DRAQ7 (BioLegend) and analyzed immediately on an LSR Fortessa flow cytometer running Diva 8 software (BD Biosciences). Typically, 500,000 cells were collected from thymus samples. Data were analyzed using FlowJo software (TreeStar).

For intracellular staining, after surface antibody staining, the cells were labeled with Zombie Aqua (BioLegend) for 30 min in ice. Then, the cells were fixed with 2% paraformaldehyde (Electron Microscope Sciences) in PBS for 20 min on ice, permeabilized with either 0.5% Triton-X 100 (Sigma) for 20 min on ice, or with Foxp3 staining kit (eBioscience) according to the protocol provided by the manufacturer and stained with antibodies for intracellular markers for 40–60 min on ice.

For cell cycle analysis, 1–5×105 sorted thymic macrophages were fixed with 70% ethanol for 2 hr on ice. The cells were spun down at 1800 rpm for 20 min at 4°C, washed with PBS, and stained with 1 μg/ml DAPI (BioLegend) for 30 min at room temperature in the dark.

For EdU staining, after surface marker and Zombie Aqua staining, cells were fixed with 2% paraformaldehyde in PBS for 20 min on ice and permeabilized with 0.5% Triton X-100 in PBS at room temperature for 20 min. EdU was detected by adding an equal volume of 2× Click reaction buffer consisting of 200 mM Tris, 200 mM ascorbic acid (Acros), 8 mM CuSO4 (Acros), and 8 μM Cy5-azide (Lumiprobe) to the permeabilized cells resuspended in 0.5% Triton X-100 in PBS and incubated at room temperature for 30 min. Cells were washed twice with 0.5% Triton X-100 in PBS and analyzed on a flow cytometer.

### Cell sorting

The sorting of thymic macrophages was done following the IMMGEN guidelines. Briefly, the thymuses of three male C57BL/6Narl mice were harvested in ice-cold staining buffer containing phenol red-free DMEM (Gibco) with 10 mM HEPES (Sigma), 0.1% NaN3, and 2% FBS (Gibco). Single-cell suspensions were prepared as described in the Flow cytometry section. Percoll PLUS was used to enrich mononuclear cells. The cells were resuspended at 108 /mL in staining buffer and labeled with appropriate antibodies for 15 min in ice. To sort thymic macrophages, the cells were first labeled with biotinylated antibodies to lineage markers (Lin) – CD3, CD8, Gr1, and B220. After washing, the cells were stained with antibodies to CD11b, F4/80, CD45, CD64, and Streptavidin-APC/cy7 for 15 min in ice. For sorting thymus XCR1+ and SIRPα+ cDCs, antibodies to XCR1, SIRPα, CD11c, MHC2, CD64, and F4/80 were used. For sorting peritoneal cavity macrophages, antibodies to ICAM2 and F4/80 were used. Immediately before sorting, the dead cells were excluded with DRAQ7 or PI. For RNA sequencing experiments, the cells were double-sorted on FACS Melody, or Aria cell sorters (BD Biosciences), and 1000 cells were directly deposited in TCL buffer (Qiagen), frozen in dry ice, and sent to IMMGEN for RNA sequencing. Four biological replicates were prepared. For cytospin and cell cycle analysis, 1–5×105 cells sorted on FACS Melody were collected in staining buffer.

### Cytospin

Sorted cells were mounted on Superfrost PLUS slides (Thermo Scientific) using a Cytospin centrifuge (Cytospin 3, Shandon) for 5 min at 500 rpm. Cells were fixed with 2% paraformaldehyde for 10 min at room temperature and stained with the Hemacolor Rapid Staining Kit (Merck Millipore). Images were collected on BX61 upright microscope (Olympus) using ×100 objective with immersion oil and captured with a CCD camera. Images were then analyzed and processed with ImageJ (NIH) and Adobe Photoshop 5.5 (Adobe).

### In vitro phagocytosis assay

107 Thymocytes were cultured in cDMEM in the presence of 1 μM of dexamethasone (Sigma) in a 3.5-cm culture dish at 37℃ in 5% CO2 incubator for 8 hr. Apoptosis levels were assessed by PI (Biolegend) and Annexin V-FITC (Biolegend) staining. Typically, more than 80% of cells were Annexin V+. The dexamethasone-treated thymocytes were stained with 1 µg/mL pHrodo Red, SE (ThermoFisher) in PBS for 30 min at room temperature. The cells were washed two times with cDMEM and resuspended at 2×106 cells/mL. 4×104 sorted peritoneal and thymic macrophages were stained with 5-µM eFluor 450 (Thermo Fisher) in PBS for 10 min at 37℃, washed two times with cDMEM, and cultured in 96-well flat-bottom culture plate (Nunc) in 100 μL cDMEM at 37℃ in 5% CO2 incubator. After 3 hr of attachment, the non-adherent cells were removed, and 200 µL (4×105) apoptotic thymocytes were added to the macrophages. The cells were incubated at 37℃ in 5% CO2 incubator for 2 hr. Fluorescent images were captured with AxioObserver 7 (Carl Zeiss) wide-field microscope equipped with Plan Apochromat 40 × NA = 1.0 objective (Zeiss) and AxioCam 702 monochrome camera (Zeiss) controlled by Zen 2.3 Blue (Zeiss) software. Image analysis was performed with Imaris 8.0.2 (Bitplane). Phagocytosis was scored by investigators blinded to the samples’ identities.

### In vitro antigen presentation assay

3×104 sorted thymic CD64−MHCII+CD11c+ dendritic cells, thymic, or peritoneal macrophages were cultured in 96-well round-bottom culture plate in 100 μL cDMEM at 37°C in 5% CO2 incubator for 3 hr to attach. Splenocytes from OT2 mice were stained with biotinylated antibodies to CD8a, CD11b, CD11c, B220, and MHCII (all from BioLegend), washed, and labeled with anti-biotin microbeads (Miltenyi) plus CD44 microbeads (Miltenyi) in cRPMI. The cells were separated on MACS LS columns (Miltenyi) according to the manufacturer’s instructions. Enriched cells (naïve CD4 T cells) were stained with 10 µM CFSE (Sigma) for 5 min in PBS at 37℃ and cocultured with the sorted thymic MHCII+CD11c+ dendritic cells, thymic, or peritoneal macrophages, in the presence or absence of 0.5-mg/mL OVA protein (Sigma) in cRPMI at 37°C in 5% CO2 incubator for 72 hr. The cells were collected and stained with antibodies to TCRβ and CD4 (from BioLegend) for flow cytometry analyses of CFSE dilution. The data were analyzed with FlowJo’s Proliferation Modeling module (BD Biosciences).

### RNA sequencing analysis

RNA sequencing was done at IMMGEN using Smart-seq2 protocol (Picelli et al., 2013; Picelli et al., 2014) on a NextSeq500 sequencer (Illumina). Following sequencing, raw reads were aligned with STAR to the mouse genome assembly mm10 and assigned to specific genes using the GENCODE vM12 annotation. Gene expression was normalized by DESeq2 (Love et al., 2014) and visualized by Morpheus (https://software.broadinstitute.org/morpheus). The principal component analysis was done by plotPCA() function of R package ‘DESeq2’. Gene expression of mouse TFs (Schmeier et al., 2017) was visualized in MultiplotStudio of GenePattern (Reich et al., 2006). GO enrichment was calculated and visualized in R by using clusterProfiler (Yu et al., 2012).

### Timed pregnancies and embryonic thymus analysis

To set up timed pregnancies, each male mouse (Cx3cr1CreER/CreER, Cx3cr1GFP/GFP, or C57BL/6) and female mouse (ROSA26LSL-GFP/LSL-GFP or C57BL/6) were housed together in the same cage for one night and separated on the next day, which we defined as embryonic day 0.5 (E0.5). Female mice were assumed to be pregnant if their weight gain was over 2 g at E8.5 (Heyne et al., 2015). Thymuses from E14.5 and E17.5 embryos, neonatal, 1-week-old pups, and adult mice (older than 6 weeks old) were harvested, mechanically dissociated with plastic sticks in 1.5-mL centrifuge tubes, and enzymatically digested with 0.2 mg/mL DNase I and 0.2 mg/mL collagenase P in complete DMEM for 20 min at 37°C with frequent agitation. The cells were resuspended in PBS with 0.5% BSA, filtered through a 70 µm filter, kept on ice, and used flow cytometric analysis as described in the Flow cytometry section.

### Genetic fate mapping – E9.5, neonatal, and adult

For genetic fate mapping, timed pregnancies of Cx3cr1CreER/CreER male and ROSA26LSL-GFP/LSL-GFP female mice were set up as described. To label the Cx3cr1+ erythromyeloid progenitors derived from embryonic YS (Mass et al., 2016), 4-hydroxytamoxifen (4-OHT from Sigma) was administered i.p. to pregnant females on E9.5 at a dose of 75 µg/g (body weight). To improve the survival of embryos and reduce the risk of abortions, progesterone (Sigma) was co-injected at a dose of 37.5 μg/g (body weight) (Iturri et al., 2017). To label the Cx3cr1+ thymic macrophages in Cx3cr1CreER × ROSA26LSL-GFP neonates and adult mice, tamoxifen (TAM from Sigma) was injected i.p. at a dose of 2 mg/mouse to lactating dams on postnatal day 3 and 4 (P3 and P4) or to adult mice for two consecutive days. Thymuses were harvested and analyzed 3 days or 6 weeks after the last injection by flow cytometry.

### scRNA-Seq – sorting, library generation, and sequencing

scRNA-Seq was performed at the Genomics Center for Clinical and Biotechnological Applications of NCFB (NYCU, Taipei, Taiwan). Briefly, the thymuses of one female MAFIA and two male Cd11cYFP mice were harvested and enzymatically digested as described previously. Mononuclear cells were enriched by 57% Percoll PLUS discontinuous centrifugation, washed to remove silica particles, and resuspended at 106 /mL in PBS with 0.04% BSA. The cell suspensions were filtered through Falcon 35 µm strainer (Corning) and stained with viability dye (PI or DAPI) immediately before sorting. Cell sorting was performed on a FACS Melody sorter (BD Biosciences) running FACS Chorus (BD Biosciences) software in purity mode. 3×105 GFP or YFP positive cells under the live/singlet gating were collected into 5-ml round bottom tubes pre-coated with 0.04% BSA in PBS. Sorted cells were washed and resuspended in 300 μL PBS with 0.04% BSA and then filtered again into 1.5 mL DNA LoBind tubes (Eppendorf) through a 35 μm strainer. The viability of the cells was evaluated by Countess II (Invitrogen) and Trypan Blue (ThermoFisher), and samples with cell viability rates higher than 85% were used for encapsulation and library preparation. Single-cell encapsulation and library preparation were performed using Single Cell 3' v3/v3.1 Gene Expression solution (10× Genomics). All the libraries were processed according to the manufacturer’s instruction and sequenced on NovaSeq 6000 (Illumina) platform at the NHRI (Zhubei, Taiwan). Post-processing and quality control were performed by the NYCU Genome Center using the CellRanger package (v. 3.0.2, 10× Genomics). Reads were aligned to mm10 reference assembly. Primary assessment with CellRanger reported 9973 cell-barcodes with 11,385 median unique molecular identifiers (UMIs, transcripts) per cell and 3076 median genes per cell sequenced to 71.0% sequencing saturation with 94,260 mean reads per cell for MAFIA mouse sample; 9801 cell-barcodes with 13,467 median UMIs per cell and 3211 median genes per cell sequenced to 74.9% sequencing saturation with 119,820 mean reads per cell for the first Cd11cYFP mouse sample; 12,938 cell-barcodes with 14,439 median UMIs per cell and 3199 median genes per cell sequenced to 71.4% sequencing saturation with 108,585 mean reads per cell for the second Cd11cYFP mouse sample.

### Analysis of scRNA-Seq

#### Preprocessing

The Scanpy (Wolf et al., 2018) pipeline was used to read the count matrix. Three batches of samples (one from GFP+ cells from MAFIA mouse and two from YFP+ cells from Cd11cYFP mice) were preprocessed independently and integrated later. Cells that expressed <200 genes and genes that were expressed in <3 cells were filtered out. The percentage of mitochondrial genes was calculated, and cells with >10% mitochondrial genes were removed. Cells with >7000 genes or <1000 genes were also removed. Read counts were normalized to library size 10,000 and log-transformed with scanpy.pp.log1p function.

#### Dataset integration and batch effect correction

Read count matrices and spliced/unspliced matrices were merged first. Principal component analysis was applied to reduce dimensions to 70. BBKNN (Polański et al., 2020) was then used to remove batch effects with the scanpy.external.pp.bbknn function with default parameters.

#### Visualization and clustering

UMAP (McInnes et al., 2018) provided by scanpy was used to visualize data with default parameters. K-nearest neighbor and Leiden clustering were applied sequentially to cluster cells into groups. K-nearest neighbor graph construction was done by scanpy.pp.neighbors with parameters n_neighbors = 12 and n_pcs = 70. Leiden clustering was then performed by scanpy.tl.leiden with parameter resolution = 0.15. To improve UMAP visualization, scanpy.tl.paga was applied, and we trimmed unnecessary graph edges by scanpy.tl.paga with threshold = 0.018.

#### Marker genes and statistics

Wilcoxon rank-sum tests were applied to examine differentially expressed genes. Clusters were selected from the result of Leiden clustering. Differentially expressed genes of a cluster against other clusters were identified by scanpy.tl.rank_genes_groups and scanpy.pl.rank_genes_groups. p-Values were collected for each cluster and transformed by negative log10 for better visualization. The top 50 differentially expressed genes were visualized in the figure.

### Immunofluorescent staining

Dissected thymus lobes from C57BL/6 mice were cleaned of connective tissue and fixed in 4% paraformaldehyde (Sigma) for 1 hr at 4°C, washed in PBS, submerged in 10% sucrose, and then in 30% sucrose for 12 hr each. The tissue was then frozen in Tissue-Tek OCT compound (Sakura Fintek) for cryostat sectioning. 10- or 20-µm thick sections were prepared with CryoStar NX50 (ThermoFisher) on Superfrost PLUS (ThermoScientific) microscope slides, dried overnight, and stored at –80°C until used. Before staining, the sections were fixed with acetone (Sigma) at –20°C for 10 min, air-dried, then blocked with 5% goat serum + 5% donkey serum (both from Jackson Immunoresearch) in PBS for 2 hr and stained with primary antibodies: rat monoclonal to MerTK (DS5MMER, eBioscience), rat monoclonal to TIM4 (RMT4-54, Bio-X-Cell), rabbit polyclonal to CD64 (Sinobiological), or rabbit polyclonal to Keratin 5 (BioLegend) overnight at 4°C in a humidified chamber. After washing in PBS, the sections were labeled with goat anti-rat-Alexa Fluor 647 (Invitrogen) or goat anti-rat Cy3 (Jackson Immunoresearch) and donkey anti-rabbit Cy3 or donkey anti-rabbit AF647 (both from Jackson Immunoresearch) secondary antibodies for 2 hr at room temperature, followed by 5 min staining with DAPI. TUNEL assay was done with the Click-iT Plus TUNEL assay Alexa Fluor 647 kit (Invitrogen) according to the manufacturer’s recommendations. Positive (pre-incubation with DNase I for 30 min at room temperature) and negative (no TdT enzyme) controls were always included. The sections were mounted with 0.1% n-propyl gallate (Sigma) in glycerol (Sigma) and imaged with an AxioObserver 7 (Carl Zeiss) wide-field microscope equipped with Plan Apochromat 20 × NA = 0.8 objective (Zeiss) and AxioCam 702 mono camera (Zeiss) and controlled by Zen 2.3 Blue (Zeiss) software. Image analysis was performed with Imaris 8.0.2 (Bitplane).

The co-localization scoring for MerTK and TIM4 with TUNEL was done with Imaris 8.2 (Bitplane). TUNEL+ cells were detected with the Spots function, while MerTK+ and TIM4+ cells were detected with the Surface function. Spots that co-localize with Surfaces were identified with the ‘Find Spots close to Surface’ function of Imaris XT. The threshold for co-localization was set to 5 µm. The results were manually curated so that Spots categorized as ‘not co-localized’ that were: (1) at the edge of the imaging field were excluded from consideration; (2) with clear surface signal around them were re-categorized as ‘co-localized’. The ratio of co-localized Spots to all Spots was calculated and presented as the co-localization index.

### Thymus transplantation

To obtain E15.5 embryos, SpicGFP (CD45.2) homozygous male and C57BL/6 (CD45.2) female mice were mated in a cage overnight and separated on the next day. Pregnant mice were sacrificed 15 days later, the viable embryos were harvested, and the thymuses were isolated in ice-cold PBS. Congenic CD45.1 recipients were anesthetized by i.p. injection of ketamine hydrochloride (120 µg/g, Toronto Research Chemicals) and xylazine hydrochloride (12 µg/g, Sigma). The fur on the left flank was removed, and the left kidney was exposed by cutting the skin, muscle layer, and peritoneum. The kidney capsule was nicked with a G23 needle, and the fetal thymus was pushed into the pocket under the kidney capsule with a G23 needle equipped with a plunger from a spinal needle. After the kidney was re-positioned back into the peritoneal cavity, the peritoneum was sutured, and the skin was stapled with metal clips. Rymadil (Carprofen, 5 µg/g, Zoetis) was given subcutaneously to ease the wound pain, and Trimerin (Sulfadiazine at 0.5 mg/mL + Trimethoprim at 0.1 mg/mL) was given in the drinking water for the first 2 weeks after the surgery. The metal clips were removed from the skin after the first week, and the transplanted thymus and recipient’s endogenous thymus were harvested and analyzed 6 weeks after the kidney transplantation.

### Statistical analysis

Comparison between groups was made with Prism 6 (GraphPad Software). Comparisons between two groups were carried out with unpaired Student’s t-test. When more than two groups were compared, a one-way ANOVA with Tukey correction was used. Differences were considered significant if p<0.05.
