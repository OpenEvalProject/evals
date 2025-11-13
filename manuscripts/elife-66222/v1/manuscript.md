# A systematic CRISPR screen reveals an IL-20/IL20RA-mediated immune crosstalk to prevent the ovarian cancer metastasis

## Authors

- Jia Li<sup>1</sup>
- Xuan Qin<sup>1</sup>
- Jie Shi<sup>1</sup>
- Xiaoshuang Wang<sup>1</sup>
- Tong Li<sup>2</sup>
- Mengyao Xu<sup>1</sup>
- Xiaosu Chen<sup>1</sup>
- Yujia Zhao<sup>1</sup>
- Jiahao Han<sup>1</sup>
- Yongjun Piao<sup>1</sup>
- Wenwen Zhang<sup>3</sup>
- Pengpeng Qu<sup>4</sup>
- Longlong Wang<sup>1</sup>
- Rong Xiang<sup>1</sup> †
- Yi Shi<sup>1</sup> ([ORCID: 0000-0003-2530-410X](https://orcid.org/0000-0003-2530-410X)) †

### Affiliations

1. The School of Medicine, Nankai University Tianjin China
2. Department of Lung Cancer Surgery, Tianjin Medical University General Hospital Tianjin China
3. Research Institute of Obstetrics and Gynecology, Tianjin Central Hospital of Obstetrics and Gynecology Tianjin China
4. Department of Gynecological Oncology, Tianjin Central Hospital of Obstetrics and Gynecology Tianjin China

† Corresponding author

## Abstract

Transcoelomic spread of cancer cells across the peritoneal cavity occurs in most initially diagnosed ovarian cancer (OC) patients and accounts for most cancer-related death. However, how OC cells interact with peritoneal stromal cells to evade the immune surveillance remains largely unexplored. Here, through an in vivo genome-wide CRISPR/Cas9 screen, we identified IL20RA, which decreased dramatically in OC patients during peritoneal metastasis, as a key factor preventing the transcoelomic metastasis of OC. Reconstitution of IL20RA in highly metastatic OC cells greatly suppresses the transcoelomic metastasis. OC cells, when disseminate into the peritoneal cavity, greatly induce peritoneum mesothelial cells to express IL-20 and IL-24, which in turn activate the IL20RA downstream signaling in OC cells to produce mature IL-18, eventually resulting in the polarization of macrophages into the M1-like subtype to clear the cancer cells. Thus, we show an IL-20/IL20RA-mediated crosstalk between OC and mesothelial cells that supports a metastasis-repressing immune microenvironment.

## Introduction

Ovarian cancer (OC) has the highest mortality among all gynecological malignancies that seriously threatens women's health worldwide (Siegel et al., 2020). Among OC, epithelial ovarian cancer (EOC) is the most common type accounting for 90% of all cases (Farley et al., 2008). EOC is classified by tumor cell histology as serous (52%), endometrioid (10%), mucinous (6%), clear cell (6%), and other rare subtypes. Due to the lack of clear symptoms at the early stage, the spread of cancer cells across the peritoneal cavity occurs in most patients at the initial diagnosis, with approximately 70% of OC patients already at metastatic stage (stages III and IV) (Vaughan et al., 2011). For OC patients with metastasized cancer cells, current therapies including chemotherapy and targeted therapies can only achieve very limited clinical outcome, with the 5-year survival rate of 20–40% for OC patients at advanced stages (Torre et al., 2018).

Although OC cells can metastasize to other distant organs through blood vessels and lymphatic vessels, the transcoelomic metastasis of OC occurs most commonly, which includes multiple processes, such as detachment of tumor cells from primary sites, immune evasion of disseminated tumor cells in the peritoneal cavity, and colonization of tumor cells on the omentum and peritoneum (Tan et al., 2006). Disseminated OC cells have to survive in a peritoneal environment constituted by lymphocytes, macrophages, natural killer (NK) cells, fibroblasts, mesothelial cells, as well as cytokines and chemokines secreted by these cells for a successful transcoelomic metastasis (Ahmed and Stenvers, 2013; Worzfeld et al., 2017). Although the role of the immune microenvironment in peritoneal cavity is indisputable in the metastasis of OC, the molecular network regulating the crosstalk between the disseminated tumors cells and immune microenvironment in peritoneal cavity is still just a tip of the iceberg. Therefore, it is imperative to understand the specific immune microenvironment in the peritoneal cavity for developing more efficient immunotherapeutic strategies against metastatic OC.

To systematically identify key genes involved in the regulation of the peritoneal metastasis of OC, we performed genome-wide gene knockout screening in an orthotopic mouse model of OC by using CRISPR/Cas9 knockout library, which has been successfully utilized to discover novel genes in the occurrence and development of diseases, especially in cancers (Huang et al., 2019; Ng et al., 2020; Shalem et al., 2014). We identified interleukin 20 receptor subunit alpha (IL20RA) as a potent suppressor of the transcoelomic metastasis of OC. IL20RA is mainly expressed in epithelial cells and forms the functional receptor, when heterodimerized with interleukin 20 receptor subunit beta (IL20RB), to bind immune cell-produced IL-20 subfamily of cytokines IL-19, IL-20, and IL-24, which have essential roles in regulating epithelial innate immunity and tissue repair (Rutz et al., 2014). IL20RA and IL20RB are also detected in tumors of epithelial origin including breast cancer, non-small-cell lung cancer, and bladder cancer, while IL-20 subfamily of cytokines has been reported to have either tumor-promoting or tumor-suppressing roles depending on tumor types and the local immune environment (Gopalan et al., 2007; Lee et al., 2013; Pestka et al., 2004; Rutz et al., 2014; Whitaker et al., 2012). In the present study, we discovered a novel IL-20/IL20RA-mediated crosstalk between disseminated OC cells and peritoneum mesothelial cells that eventually promotes the generation of M1-like inflammatory macrophages to prevent peritoneal dissemination of OC cells.

## Results

### IL20RA is an anti-transcoelomic metastasis gene in OC identified by a genome-scale knockout screening in vivo

To screen key genes regulating transcoelomic metastasis of OC, we utilized human epithelial OC cell SK-OV-3 with relatively low metastatic capacity to set up the orthotopic transplant tumor model in NOD-SCID mice. Prior to the inoculation of these cells into the mouse ovaries, SK-OV-3 cells were transduced with the human CRISPR knockout library (GeCKO v2.0) made by Feng Zhang et al., which contains sgRNAs specifically against 19,050 protein-encoding genes and 1864 miRNA genes and 1000 non-targeting control sgRNAs (Shalem et al., 2014). Peritoneal metastasized SK-OV-3 cells in the intraperitoneal cavity were isolated and expanded in vitro for next runs of orthotopic transplant (Figure 1A). After three runs of in vivo screening, highly metastatic SK-OV-3 cells were subjected to high-throughput sgRNA library sequencing to reveal the sgRNA representations. The RNAi Gene Enrichment Ranking (RIGER) p-value analysis was used to identify significantly enriched sgRNAs in metastasized (sgRNAMet) or primary (sgRNAPri) OC xenografts. By using the criteria of the number of enriched sgRNAs targeting each gene ≥3, p-value<0.05 and the normalized enrichment score (NES) <−1.2, we got two high-ranked genes, namely IL20RA and TEX14 (Figure 1B). Given all the six sgRNAs targeting IL20RA in GeCKO library were enriched with high NES, we chose IL20RA for further investigation on its function in the transcoelomic metastasis of OC.

![Figure 1.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig1-v1.jpg)

**Figure 1.:** (A) Schematics of experiment design to screen metastasis-related genes using CRISPR/Cas9 library in OC orthotopic murine model. (B) Venn diagram comparing the hits met the indicated enrichment criteria. (C, D) Western blot analysis of IL20RA in control shRNA (shCtrl)- or IL20RA shRNA (shIL20RA)-transfected SK-OV-3 cells (C) and in IL20RA- or empty vector-transfected ID8 cells (D). (E, F) Representative images of NOD-SCID mice with shCtrl- or shIL20RA-transfected SK-OV-3 cells orthotopically transplanted in the ovaries at 40 days post-inoculation (E, left panel). The ascites volumes (E, right panel) and the numbers of metastatic nodules on the surfaces of intestines (F) were quantified (n = 7, data are shown as means ± SEM, *p<0.05, **p<0.01, by unpaired two-sided Student’s t-test). (G, H) Representative images of C57BL/6 mice at 60 days after orthotopically inoculated with IL20RA-reconstituted or control ID8 cells in ovaries (G, left panel). The ascites volumes (G, right panel) and the numbers of metastatic nodules on the surfaces lining the peritoneal cavities (H) were quantified (n = 6, data are shown as means ± SEM, *p<0.05, **p<0.01 by unpaired two-sided Student’s t-test).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Western blot analysis of IL20RA in different OC cells. (B) qRT-PCR analysis of IL20RA in SK-OV-3 cells transfected with shCtrl or shIL20RA (means ± SEM, ***p<0.001, by unpaired two-sided Student’s t-test). (C, D) Representative images of C57BL/6 mice at 45 days after direct intraperitoneal injection of IL20RA-reconstituted or control (Vec) ID8 cells (C, D, left panels). The ascites volumes and numbers of metastatic nodules on the surfaces of diaphragm, peritoneum, and mesentery were quantified (n = 6 mice for each group). Data are shown as means ± SEM, *p<0.05, **p<0.01, ***p<0.001, by unpaired two-sided Student’s t-test.

To confirm the role of IL20RA in OC metastasis, we knocked down IL20RA in SK-OV-3 cells, which had relatively high level of IL20RA (Figure 1C, Figure 1—figure supplement 1A, B), and reconstituted IL20RA in highly metastatic murine epithelial OC cell ID8, which was isolated from peritoneal ascites of ID8-injected C57BL/6 mice as described by Ward and colleagues (Ward et al., 2013) with high-grade serous ovarian carcinoma (HGSOC)-like characteristics (Diaz Osterman et al., 2019) and had very low level of endogenous IL20RA (Figure 1—figure supplement 1A, Figure 1D). In the SK-OV-3 orthotopic mouse OC model, silencing IL20RA greatly promoted the transcoelomic metastasis of OC and the formation of ascites (Figure 1E, F), while in ID8 syngeneic mouse OC model, reconstitution of IL20RA in ID8 cells dramatically reduced the volumes of ascites and the numbers of metastatic nodules in diaphragm, peritoneum, and mesentery (Figure 1G, H).

To further investigate whether IL20RA suppresses transcoelomic metastasis of OC at the later stage when OC cells have disseminated into the peritoneal cavity, we directly injected ID8 cells into the peritoneal cavity of C57BL/6 mice. We were still able to observe that IL20RA-reconstituted ID8 cells formed much less metastases on the diaphragm, peritoneum, and mesentery and resulted in much less ascites as well (Figure 1—figure supplement 1C, D). Together, these data suggest that IL20RA is a potent suppressor gene for the transcoelomic metastasis of OC.

### The IL20RA expression is dramatically decreased in metastases of OC patients and positively correlates with the clinical outcome

To further get the clinical evidences on the relevance of IL20RA in OC metastasis, we collected primary OC tissues and paired cancer cells isolated from ascites and metastatic nodules in peritoneal cavity from 20 serous OC patients. Analysis of IL20RA protein by western blot shows a dramatic decrease of IL20RA in the transcoelomic spread cancer samples when compared with those from the primary sites (Figure 2A, B), which is confirmed by the quantitative reverse-transcriptase-PCR (qRT-PCR) analysis of IL20RA mRNA (Figure 2C, D). Immunohistochemical (IHC) analysis also shows the much lower level of IL20RA in metastatic cancer cells than that in the cancer cells at the primary sites (Figure 2E, F). To further investigate the relevance of IL20RA with OC metastasis, we analyzed the correlation between the IL20RA level and the survival of serous OC patients given that metastasis accounts for over 90% of cancer death. High level of IL20RA significantly correlates with the better overall survival (OS) and progression-free survival (PFS) of serous OC patients (Figure 2G), supporting that IL20RA functions as a suppressor of OC metastasis. Besides, IL20RA expression is also positively correlated with the clinical outcome of patients in patients of bladder carcinoma, uterine corpus endometrial carcinoma, rectum adenocarcinoma, and gastric cancer (Figure 2—figure supplement 1).

![Figure 2.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig2-v1.jpg)

**Figure 2.:** (A, B) Western blot analysis of IL20RA in primary OC tissues (Pri) and paired metastatic cancer cells in ascites (Asc) and metastatic nodules on the surfaces of the abdominal organs (Met) (A). Quantification results are plotted in (B) (n = 20, ***p<0.001, by unpaired two-sided Student’s t-test). (C, D) qRT-PCR analysis of IL20RA in human primary OC tissue (Pri) and paired peritoneal metastases (Asc and Met) (C, data are plotted as means ± SEM from three independent measurements, *p<0.05, **p<0.01, ***p<0.001, by unpaired two-sided Student’s t-test). The comparison of the IL20RA levels in these two groups is analyzed in (D) (**p<0.01, ***p<0.001, by unpaired two-sided Student’s t-test). (E, F) Representative images of immunohistochemical analysis of IL20RA in in human primary OC tissue and paired peritoneal metastases (E) and quantification by H-score (F, n = 18, ***p<0.001, by paired two-sided Student’s t-test). Scale bar: 100 μm (left panel in E); 20 μm (right panel in E). (G) Kaplan–Meier survival plot to show the progression-free survival and overall survival of serous OC patients with different IL20RA expression.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Kaplan–Meier survival plots to show the correlations of different IL20RA expression with the overall survival in patients of bladder carcinoma, uterine corpus endometrial carcinoma, rectum adenocarcinoma, and gastric cancer.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A, B) qRT-PCR analysis of IL20RB in human primary OC tissue and paired peritoneal metastases (A, data are plotted as means ± SEM from three independent measurements, *p<0.05, **p<0.01, ***p<0.001, ns, not significant, by unpaired two-sided Student’s t-test). The comparison of the IL20RB levels in these two groups is statistically analyzed in (B) (ns, not significant, by unpaired two-sided Student’s t-test). (C) Kaplan–Meier survival plot to show the progression-free survival and overall survival of OC patients with different IL20RB expression.

By contrast, as a heterodimerization partner for IL20RA, IL20RB expression shows no significant difference between primary and metastatic OC specimen (Figure 2—figure supplement 2A, B) and negatively correlates with the OS and PFS of OC patients (Figure 2—figure supplement 2C), suggesting that IL20RA is the key subunit of IL20RA/IL20RB receptor complex that is regulated during the transcoelomic metastasis of OC.

### Characterization of IL20RA-mediated modulation on the peritoneal immune microenvironment during the transcoelomic metastasis of OC

To get insights into the mechanisms of IL20RA-mediated inhibition on OC metastasis, we firstly excluded the possibility that IL20RA might regulate the proliferation and migration of OC cells (Figure 3—figure supplement 1A–D). We next examined the possible impacts of IL20RA in shaping the immune microenvironment during the spreading of OC cells into the intraperitoneal cavity. In the syngeneic murine OC model by orthotopic transplant of ID8 cells, we analyzed the proportions of immune cells in ascites, including macrophages, T lymphocytes, and B lymphocytes. Compared with control ID8 cells with very low level of endogenous IL20RA (Figure 1—figure supplement 1A), reconstitution of IL20RA does not change the total proportion of macrophages (CD11b+ F4/80+) among leukocytes (CD45+). However, we observed a significant increase in the proportion of M1-like (MHCII+ CD206-) macrophages and a dramatic decrease of M2-like (MHCII- CD206+) macrophages in the malignant ascites caused by IL20RA-reconstituted ID8 cells (Figure 3A, B), which were further confirmed by dramatically increased M1-like marker genes and decreased M2-like markers (Figure 3C).

![Figure 3.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig3-v1.jpg)

**Figure 3.:** (A, B) Flow cytometry analysis of macrophages (CD45+ CD11b+ F4/80+) and M1-like (MHC II+ CD206-) and M2-like (MHC II- CD206+) subpopulations in ascites formed in C57BL/6 mice at 60 days after orthotopically inoculated with IL20RA-reconsitituted or control (Vec) ID8 cells (A). The quantification is shown in (B) as means ± SEM (n = 5), *p<0.05, ns, not significant, by unpaired two-sided Student’s t-test. (C) qRT-PCR analysis of key marker genes in peritoneal macrophages (CD11b+ F4/80+) isolated in (A) (shown as means ± SEM, *p<0.05, **p<0.01, ***p<0.001, by unpaired two-sided Student’s t-test). (D, E) Flow cytometry analysis of peritoneal T lymphocytes (D) and B lymphocytes (E) from syngeneic OC mouse model (same mice as described in A), ns, not significant, by unpaired two-sided Student’s t-test. (F) Flow cytometry analysis of macrophages in ascites formed in NOD-SCID mice at 40 days after orthotopically inoculated with indicated SK-OV-3 cells. Data are shown as means ± SEM, n = 3, *p<0.05, **p<0.01, ***p<0.001, by unpaired two-sided Student’s t-test.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Growth curves of IL20RA-reconstituted or control (Vec) ID8 cells under the stimulation of IL-20. (B) Growth curves of shIL20RA- or shCtrl-transfected SK-OV-3 cells under the stimulation of IL-20. (C, D) Transwell cell migration assay of shIL20RA- or shCtrl-transfected SK-OV-3 cells in the presence of IL-20, which were quantified in (D) (shown as means ± SEM from three independent experiments, ns, not significant, by unpaired two-sided Student’s t-test). Scale bar: 50 μm.

We also found that neither the ratios of T lymphocytes (CD45+ CD3+) and their subtypes (i.e., CD4+ and CD8+ T lymphocytes) nor that of B lymphocytes (CD45+ B220+) showed significant change upon the reconstitution of IL20RA (Figure 3D, E), which was consistent with the fact that IL20RA was screened in immunodeficient NOD-SCID mice lacking both T and B lymphocytes and NK cells (Figure 1A).

To further confirm that IL20RA in OC cells affects the macrophages during the transcoelomic metastasis, we examined the immune cells in malignant ascites caused by the inoculation of SK-OV-3 cells with silenced IL20RA into NOD-SCID mice. FACS results show that the population of M1-like (MHCII+) macrophages is significantly decreased and M2-like (CD206+) macrophages is significantly increased upon silencing IL20RA (Figure 3F). Collectively, these data demonstrate that IL20RA in OC cells is able to regulate the polarization of peritoneal macrophages, instead of T lymphocytes and B lymphocytes, to prevent the transcoelomic spreading of OC cells into the peritoneal cavity.

### IL20RA mediates a direct conversation between OC cells and the macrophages that regulates the polarization of macrophages

To investigate if IL20RA supports a metastasis-preventing peritoneal immune-microenvironment through a direct crosstalk between OC cells and macrophages, we checked the polarization of macrophages in vitro under the stimulation of conditioned medium (CM) from OC cells (Figure 4A). CM from IL-20-stimulated IL20RA-reconstituted ID8 cells (hereafter referred to as ‘CMIL20RA IL-20 (+)) significantly stimulates the expression of M1-like markers while decreases the expression of M2-like markers in RAW 264.7 cells when compared with CM from IL-20-stimulated empty vector-transfected ID8 control cells (referred to as CMVec IL-20 (+)) (Figure 4B). To further confirm, we prepared bone marrow-derived macrophages (BMDMs) by treating the bone marrow cells (BMCs) isolated from healthy C57BL/6 mice with 20 ng/mL macrophage colony stimulating factor (M-CSF) for 7 days, which were characterized by the adherent morphology and the expression of Cd68 (Figure 4C, D). Consistently, CMIL20RA IL-20 (+) dramatically induces the expression of M1-like markers and decreases the M2-like markers in BMDM (Figure 4E).

![Figure 4.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig4-v1.jpg)

**Figure 4.:** (A) Schematic of the in vitro crosstalk experiment using conditioned medium (CM) from OC cells to educate macrophages. (B) qRT-PCR analysis of macrophage marker genes in RAW 264.7 cells stimulated with CM of IL-20-stimulated/unstimulated IL20RA-reconsitituted (CMIL20RA) or control (CMVec) ID8 cells for 72 hr. (C, D) Representative image of bone marrow-derived macrophage (BMDM) differentiated from bone marrow cell with the treatment of macrophage colony stimulating factor for 7 days (C), which were further characterized by qRT-PCR analysis of its marker gene Cd68 (D). Scale bar: 20 μm. (E) qRT-PCR analysis of macrophage marker genes in BMDM treated with CM of IL-20-stimulated/unstimulated IL20RA-reconsitituted (CMIL20RA) or control (CMVec) ID8 cells for 72 hr. (F, G) Image of macrophages differentiated from THP-1 cells with the treatment of phorbol-12-myristate-13-acetate for 48 hr (F) and further characterization by qRT-PCR analysis of CD68 (G). Scale bar: 20 μm. (H) qRT-PCR analysis of macrophage marker genes in THP-1-derived macrophages treated with CM from IL-20-stimulated/unstimulated shIL20RA or control shRNA (shCtrl)-transfected SK-OV-3 cells for 72 hr. All the qRT-PCR data are shown as means ± SEM from three independent experiments, *p<0.05, **p<0.01, ***p<0.001, by unpaired two-sided Student’s t-test.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Schematic of the in vitro co-culture experiments. (B, C) Transwell migration assay to show the migrated RAW 264.7 cells co-cultured with IL20RA-reconstituted or control (Vec) ID8 cells (B), which were quantified in (C) (shown as means ± SEM from three independent experiments, ns, not significant, by unpaired two-sided Student’s t-test). Scale bar: 50 μm. (D) qRT-PCR analysis of macrophage marker genes in bone marrow-derived macrophage co-cultured with IL20RA-reconstituted or control (Vec) ID8 cells for 72 hr. (E) qRT-PCR analysis of macrophage marker genes in THP-1-derived macrophages co-cultured with shIL20RA- or shCtrl-transfected SK-OV-3 cells for 72 hr. (F) qRT-PCR analysis of macrophage marker genes in RAW 264.7 cells stimulated with IL-20 protein for 72 hr. (G) qRT-PCR analysis of macrophage marker genes in RAW 264.7 cells stimulated with IL-24 protein for 72 hr. All the qRT-PCR data are shown as means ± SEM from three independent experiments, *p<0.05, **p<0.01, ***p<0.001, by unpaired two-sided Student’s t-test.

In human macrophages differentiated from THP-1 monocytes by phorbol-12-myristate-13-acetate (PMA) treatment (Figure 4F, G), CM from IL-20-stimulated, IL20RA-silenced SK-OV-3 cells significantly increases the expression of M2-like markers and decreases the expression of M1-like markers when compared with CM from IL-20-stimulated control shRNA (shCtrl)-transfected SK-OV-3 cells (Figure 4H). Besides, the polarization of macrophages is not changed under the stimulation of CM from unstimulated IL20RA-reconstituted or IL20RA-silenced OC cells, indicating that IL20RA-mediated macrophage polarization needs the prior stimulation of the IL-20 (Figure 4B, E, H).

We also checked the polarization of macrophages in vitro using the indirect co-culture system (Figure 4—figure supplement 1A). IL-20-stimulated, IL20RA-reconstituted ID8 cells have no effect on the migration capacity of RAW 264.7 cells (Figure 4—figure supplement 1B, C). However, co-culture with IL-20-stimulated IL20RA-reconstituted ID8 cells dramatically induces the expression of M1-like markers and reduces the M2-like markers in RAW 264.7 cells (Figure 4—figure supplement 1D). Besides, co-culture with IL-20-stimulated, IL20RA-silenced SK-OV-3 cells significantly increases the expression of M2-like markers and decreases the expression of M1-like markers in THP-1-derived macrophages (Figure 4—figure supplement 1E). We also excluded the possibility that IL-20 and IL-24 directly regulated the polarization of macrophages since it did not affect the expression of both the M1- and M2-like markers in RAW 264.7 cells (Figure 4—figure supplement 1F, G). Collectively, these data reveal a conserved, IL20RA-mediated direct crosstalk between OC cells and macrophages that favors an inflammatory immune microenvironment.

### IL20RA-mediated education of macrophages plays essential roles in the prevention of the transcoelomic metastasis of OC

To investigate the function of the macrophages educated by IL20RA-mediated crosstalk with OC cells in the transcoelomic metastasis of OC, we injected ID8 cells alone or together with CMVec IL-20 (+)- or CMIL20RA IL-20 (+)-educated BMDM into the peritoneal cavity of C57BL/6 mice (Figure 5A). CMIL20RA IL-20 (+)-educated BMDM significantly reduces the volume of malignant ascites (Figure 5B, C) and dramatically inhibits the formation of metastatic nodules in peritoneal cavity (Figure 5D, E), indicating that IL20RA-mediated crosstalk between OC cells and macrophages prevents the transcoelomic metastasis of OC. In addition, in peritoneal macrophage-depleted mice, reconstitution of IL20RA in ID8 cells can no longer reduce the volume of malignant ascites and inhibit the peritoneal metastasis of OC, indicating that IL20RA-mediated education of macrophages plays an essential role to suppress the transcoelomic metastasis of OC (Figure 5F–J).

![Figure 5.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig5-v1.jpg)

**Figure 5.:** (A) Schematic of the experiments. ID8 cells alone or mixed with CMIL20RA IL-20 (+)- or CMVec IL-20 (+)-stimulated bone marrow-derived macrophage were injected into the peritoneal cavity of C57BL/6 mice. (B–E) Representative images of the ascites formation (B) and metastatic nodules in peritoneal cavity (D) at day 45 post-inoculation. The quantification of ascites and metastatic nodules is shown in (C) and (E), respectively. Data are shown as means ± SEM, n = 6, *p<0.05; **p<0.01; ***p<0.001, by unpaired two-sided Student’s t-test. (F) Schematic of the experiments. IL20RA-reconsitituted or control (Vec) ID8 cells were injected into the peritoneal cavity of C57BL/6 mice. The phosphate-buffered saline liposomes (PBS) or clodronate liposomes (CLO) were intraperitoneal (i.p.) injected every 3 days. (G–J) Representative images of the ascites formation (G) and metastatic nodules in peritoneal cavity (I) at day 45 post-inoculation. The quantification of ascites and metastatic nodules is shown in (H) and (J), respectively. Data are shown as means ± SEM, n = 6 (ID8Vec/PBS and ID8IL20RA/PBS), n = 3 (ID8Vec/CLO and ID8IL20RA/CLO), ns, not significant; **p<0.01; ***p<0.001, by unpaired two-sided Student’s t-test.

### Mesothelial cells in peritoneum produce IL20RA ligands IL-20 and IL-24 when challenged with OC cells in the peritoneal cavity

To identify the signal sources in the peritoneal cavity that respond to the disseminated OC cells through IL20RA, we injected ID8 cells into the peritoneal cavity of C57BL/6 mice to mimic the peritoneal dissemination of OC cells and checked the expression of possible IL20RA ligands, including IL-19, IL-20, and IL-24, in different tissues in the peritoneal cavity. A dramatic increase of Il20 and Il24 from the abdominal wall occurs upon the injection of OC cells into the peritoneal cavity (Figure 6A), while there is no induction of these ligands in the intestine, ovary, and peritoneal macrophages (CD11b+ F4/80+) (Figure 6A, B). In addition, reconstitution of IL20RA in ID8 cells does not induce these ligands in themselves (Figure 6C). The amounts of IL-20 and IL-24 in peritoneal flushing fluid are significantly increased upon the injection of OC cells into the peritoneal cavity (Figure 6D). To further confirm, we isolated abdominal wall and co-cultured with ID8 cells in vitro and a boosted expression of Il20 and Il24 was observed (Figure 6E). Hematoxylin and eosin (H&E) and IHC staining of the abdominal walls from mice bearing peritoneal-disseminated OC cells show that IL-20 and IL-24 are originated from mesothelial cells (Figure 6F, G), which are further confirmed by immunofluorescent (IF) staining (Figure 6—figure supplement 1A, B).

![Figure 6.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig6-v1.jpg)

**Figure 6.:** (A, B) qRT-PCR analysis of IL20RA ligands (Il19, Il20, and Il24) in peritoneal organs (intestinal, abdominal wall, ovary) (A) or peritoneal macrophages (CD11b+ F4/80+) (B) taken from C57BL/6 mice with intraperitoneal injection of ID8 cells (OC) or phosphate-buffered saline (PBS) control (Ctrl) 9 days before. Data are shown as means ± SEM, n = 18 for Ctrl group and n = 6 for OC group, ***p<0.001, ns, not significant, by unpaired two-sided Student’s t-test. (C) qRT-PCR analysis of IL20RA ligands in IL20RA-reconstituted or control (Vec) ID8 cells (means ± SEM, ns, not significant). (D) ELISA measurement of IL-20 and IL-24 in peritoneal flushing fluid from mice with intraperitoneal injection of ID8 cells (OC) or PBS control (Ctrl) 9 days before. n = 6 for each group. Data are shown as means ± SEM, ***p<0.001, by unpaired two-sided Student’s t-test. (E) qRT-PCR analysis of the abdominal walls dissected from C57BL/6 mice and co-cultured with medium (Ctrl) or ID8 cells for 48 hr (means ± SEM from three independent experiments, ***p<0.001, ns, not significant, by unpaired two-sided Student’s t-test). (F) Hematoxylin and eosin staining of the abdominal wall of C57BL/6 mice. Scale bar: 50 μm (upper panel); 20 μm (lower panel). (G) Immunohistochemical staining of IL-20 and IL-24 in abdominal walls dissected from mice with intraperitoneal injection of ID8 cells (OC) or PBS control (Ctrl) 9 days before. Scale bar: 20 μm.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A, B) Immunofluorescent staining of IL-20/IL-24 (red), cytokeratin CK18 (green), and DAPI (blue) in peritoneum dissected from mice with intraperitoneal injection of ID8 cells (OC) or phosphate-buffered saline control (Ctrl) 9 days before. Scale bar: 30 μm.

### IL-20/IL20RA activates OAS/RNase L-mediated NLR signaling to produce mature IL-18 for macrophage polarization

To explore the IL-20/IL20RA-mediated downstream signaling that modulates the polarization of peritoneal macrophage, we analyzed the transcriptome of ID8 cells with reconstituted IL20RA under the stimulation of IL-20. Kyoto Encyclopedia of Genes and Genomes (KEGG) enrichment analysis shows that the differentially expressed genes are enriched in the immune system (Figure 7—figure supplement 1A). In particular, IL-20/IL20RA-mediated signaling greatly increases the expression of several genes, that is, 2'−5'-oligoadenylate synthetase (Oas1a and Oas1g) and Il18, involved in OAS-RNase L-mediated NOD-like receptor (NLR) signaling pathway (Figure 7—figure supplement 1B, C), which regulates inflammasome signaling to activate Caspase-1 and hence the production of functional inflammatory cytokines IL-1β and IL-18 by cleavage during viral infections (Banerjee, 2016; Chakrabarti et al., 2015).

The induction of Oas1a and Il18 in IL20RA-reconsitituted ID8 cells upon IL-20 stimulation is further confirmed by qRT-PCR (Figure 7A) and enzyme-linked immunosorbent assay (ELISA) for secreted IL-18 (Figure 7B). Western blot analysis shows that IL-20/IL20RA triggers the phosphorylation of STAT3 and results in increased OAS1A, activated Caspase-1 and IL-18 by cleavage (Figure 7C), which also occurs in human SK-OV-3 cells when stimulated by IL-20 (Figure 7D, E). We further identify a STAT3-binding site on the promoter of Oas1a gene by chromatin immunoprecipitation and qPCR (ChIP-qPCR) (Figure 7F, G), confirming that IL-20/IL20RA induces Oas1a and Il18 through downstream STAT3. Consistently, IHC staining of human OC tissues shows that the levels of phosphorylated STAT3, OAS1, and IL-18 are significantly lower in metastatic lesions than those in primary sites (Figure 7H, I). In addition, transcriptome analysis on a cohort of 530 serous OC patients from TCGA database shows the positive correlation of IL20RA with both OAS1 and IL18 (Figure 7—figure supplement 1D), further supporting that IL-20/IL20RA activates OAS/RNase L-mediated inflammasome signaling in human OC as well.

![Figure 7.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig7-v1.jpg)

**Figure 7.:** (A) qRT-PCR analysis of Oas1a and Il18 upon IL20RA reconstitution in ID8 cells. (B) The secreted IL-18 from IL20RA-reconstituted and control ID8 cells was measured by ELISA. (C) Western blot analysis of indicated proteins in IL20RA-reconstituted and control ID8 cells under the stimulation of IL-20. (D) Western blot analysis of indicated proteins in SK-OV-3 cells stimulated with IL-20 or phosphate-buffered saline (PBS) (Ctrl) for 24 hr. (E) ELISA measurement of IL-18 secreted from SK-OV-3 cells stimulated by IL-20 for 24 hr. (F) Schematic of the Oas1a promoter and Il18 promoter with predicted STAT3-binding sites and the primer sets. (G) IL20RA-reconstituted ID8 cells were stimulated with IL-20 or PBS (Ctrl) for 24 hr before the STAT3 binding on Oas1a promoter and Il18 promoter was analyzed by ChIP-qPCR. (H, I) Immunohistochemical analysis of IL20RA, p-STAT3, OAS1, and IL-18 in human primary ovarian cancer tissues (Pri) and paired peritoneal metastatic nodules (Met) (H) and quantification (I). **p<0.01; ***p<0.001, by paired two-sided Student’s t-test. Scale bar: 20 μm. (J) qRT-PCR analysis of macrophage marker genes in RAW 264.7 cells stimulated with IL-20 protein for 72 hr. (K) qRT-PCR analysis of macrophage marker genes in RAW 264.7 cells treated by CMIL20RA IL-20 (+) or CMVec IL-20 (+) together with IL-18 neutralizing antibody (nAb) or nonspecific lgG (IgG) for 72 hr. All the qRT-PCR and ELISA data are shown as means ± SEM from three independent experiments, *p<0.05, **p<0.01, ***p<0.001, by unpaired two-sided Student’s t-test.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** (A) KEGG gene set (based on organism systems) enrichment analysis on significantly changed genes in IL20RA-reconstituted ID8 cells. (B) KEGG pathway enrichment analysis on significantly changed, immune-related genes in IL20RA-reconstituted ID8 cells. (C) Heatmap of differentially expressed, immune-related genes in IL20RA-reconstituted ID8 cells. (D) The Spearman’s correlation analysis on the expression of IL20RA, OAS1, and IL18 in ovarian cancer patients.

To get insights into the role of IL-18 in macrophage polarization, RAW 264.7 cells were treated with IL-18, which resulted in greatly increased expression of M1-like markers and significantly decreased M2-like markers (Figure 7J). CMIL20RA IL-20 (+)-induced polarization of RAW 264.7 cells to M1-like phenotypes can be dramatically blocked by IL-18 neutralization antibody (Figure 7K).

To investigate the essential role of IL-18 in IL-20/IL20RA-mediated downstream signaling to suppress the peritoneal dissemination of OC cells in vivo, we knock down IL-18 in IL20RA-reconsitituted ID8 cells (ID8IL20RA/shIL-18) and further inject ID8Vec, ID8IL20RA, and ID8IL20RA/shIL-18 cells into the peritoneal cavity of C57BL/6 mice (Figure 8A, B), which results in dramatically reduced IL-18 in the peritoneal fluids (Figure 8C). Silencing IL-18 abolishes the effects of reconstituted IL20RA in the inhibition of the malignant ascites formation and the peritoneal dissemination of OC cells (Figure 8D–G). In addition, IL-20/IL20RA-induced polarization of peritoneal macrophages to M1-like phenotypes is also disappeared upon the silenced of IL-18 (Figure 8H). These data suggest that IL-18 is the essential factor downstream IL-20/IL20RA signaling to regulate the polarization of macrophages and suppress the OC dissemination.

![Figure 8.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig8-v1.jpg)

**Figure 8.:** (A) qRT-PCR analysis of Il18 in ID8Vec and ID8IL20RA cells transfected with shCtrl or shIL-18 (means ± SEM, ***p<0.001, by unpaired two-sided Student’s t-test). (B) Western blot analysis of IL-18 in ID8Vec and ID8IL20RA cells transfected with shCtrl or shIL-18. (C) ELISA measurement of IL-18 in ascites from mice with intraperitoneal injection of ID8Vec, ID8IL20RA, and ID8IL20RA/shIL-18 cells 45 days post-injection. Data are shown as means ± SEM, n = 6, ***p<0.001, by unpaired two-sided Student’s t-test. (D–G) Representative images of ascites formation (D) and the metastatic nodules in peritoneal cavity (E) of C57BL/6 mice at day 45 after intraperitoneal injected with ID8Vec, ID8IL20RA, and ID8IL20RA/shIL-18 cells. The quantification of ascites and metastatic nodules is shown in (F) and (G), respectively. Data are shown as means ± SEM, n = 6, **p<0.01, ***p<0.001, by unpaired two-sided Student’s t-test. (H) Flow cytometry analysis of macrophages (CD45+ CD11b+ F4/80+) and M1-like (MHC II+ CD206-) and M2-like (MHC II- CD206+) subpopulations in ascites formed in C57BL/6 mice at day 45 after intraperitoneal injected with ID8Vec, ID8IL20RA, and ID8IL20RA/shIL-18 cells. Data are shown as means ± SEM, n = 3, *p<0.05, ns, not significant, by unpaired two-sided Student’s t-test.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** (A) qRT-PCR analysis of Il20rb in ID8Vec and ID8IL20RA cells transfected with shCtrl or shIL20RB (means ± SEM, ***p<0.001, by unpaired two-sided Student’s t-test). (B) Western blot analysis of indicated proteins in IL20RB-silenced ID8Vec and ID8IL20RA cells and their control cells under the stimulation of IL-20. (C) qRT-PCR analysis of macrophage marker genes in RAW 264.7 cells stimulated with conditioned medium of IL-20-stimulated IL20RB-silenced ID8Vec and ID8IL20RA cells and their control cells for 72 hr. Data are shown as means ± SEM from three independent experiments, *p<0.05, **p<0.01, ***p<0.001, ns, not significant, by unpaired two-sided Student’s t-test. (D–G) Representative images of ascites formation (D) and the metastatic nodules in peritoneal cavity (E) at day 45 after intraperitoneal injected with ID8Vec, ID8IL20RA, and ID8IL20RA/shIL20RB cells. The quantification of ascites and metastatic nodules is shown in (F) and (G), respectively. Data are shown as means ± SEM, n = 6, ***p<0.001, ns, not significant, by unpaired two-sided Student’s t-test.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig8-figsupp2-v1.jpg)

**Figure 8—figure supplement 2.:** (A) qRT-PCR analysis of potential IL20RA ligands from the abdominal wall taken from C57BL/6 mice with intraperitoneal injection of SK-OV-3 cells or phosphate-buffered saline control (Ctrl) 9 days before. (B) qRT-PCR analyses of macrophage marker genes in RAW 264.7 cells stimulated with human IL-18 protein for 72 hr. (C) qRT-PCR analysis of macrophage marker genes in RAW 264.7 cells treated with conditioned medium from IL-20-stimulated shIL20RA or control shRNA (shCtrl)-transfected SK-OV-3 cells for 72 hr. All the qRT-PCR data are shown as means ± SEM from three independent experiments, *p<0.05, **p<0.01, ***p<0.001, by unpaired two-sided Student’s t-test.

As IL20RB is the heterodimerization partner for IL20RA, we investigate the role of IL20RB in IL-20/IL20RA signaling-mediated OC metastasis. We knock down IL20RB in control ID8 cells and IL20RA-reconsitituted ID8 cells (Figure 8—figure supplement 1A, B). Western blot analysis and qRT-PCR analysis show that silencing IL20RB blocks the activation of the STAT3/NLR signaling in IL20RA-reconstituted ID8 cells and hence the polarization of macrophages educated by ID8 cells (Figure 8—figure supplement 1B, C). In ID8 cell-grafted murine model of OC, silencing IL20RB in IL20RA-reconstituted ID8 cells dramatically abolishes the suppressive roles of IL20RA in the formation of malignant ascites and the peritoneal dissemination of OC cells, indicating that IL20RA signaling-inhibited OC dissemination needs the functional IL20RA/IL20RB heterodimer receptor (Figure 8—figure supplement 1D–G).

As the role of IL-20/IL20RA in preventing the peritoneal dissemination of OC was observed in the murine models of OC established by both human and mouse OC cells (Figure 1F–H), we further investigate whether the cytokines involved in the process (IL-20, IL-24, and IL-18) have cross-reactivities between two species. Intraperitoneal injection of SK-OV-3 cells induces the increased expression of Il20 and Il24 from the abdominal wall of C57BL/6 mice (Figure 8—figure supplement 2A). Besides, a previous study has showed that murine IL-20 subfamily cytokines were also able to cross-react with human receptors (Kolumam et al., 2017). In addition, human IL-18 also significantly stimulates the expression of M1-like markers while inhibits the expression of M2-like markers in RAW 264.7 cells (Figure 8—figure supplement 2B). CM of the IL-20-stimulated IL20RA-silenced SK-OV-3 cells (CMshIL20RA) also can increase the expression of M2-like markers and inhibit the expression of M1-like markers of RAW 264.7 cells (Figure 8—figure supplement 2C). Therefore, these data suggest that IL-20/IL20RA signaling also works in NOD-SCID mice challenged with SK-OV-3 cells.

### Administration of IL-18 protein strongly suppresses the transcoelomic metastasis of OC

Given the dramatic decrease of IL20RA in the peritoneal metastasized OC cells (Figure 2) and the essential role of IL-18 as a major IL20RA downstream factor inhibiting peritoneal dissemination, we postulated that the direct administration of IL-18 might be an easy strategy to suppress the peritoneal growth of OC. To test, we treated the mice bearing orthotopically transplanted ID8 xenografts with recombinant IL-18 protein (Figure 9A). It shows that intraperitoneal injection of IL-18 dramatically reduces the ascites formation and the numbers of metastatic nodules in diaphragm, peritoneum, and mesentery (Figure 9B–E). Furthermore, direct administration of IL-18 significantly increases the proportion of M1-like (MHCII+ CD206-) macrophages and decreases M2-like (MHCII- CD206+) macrophages in the malignant ascites (Figure 9F).

![Figure 9.](https://cdn.elifesciences.org/articles/66222/elife-66222-fig9-v1.jpg)

**Figure 9.:** (A) Schematic of the experiments. ID8 cells were orthotopic injected into the ovaries of C57BL/6 mice. The phosphate-buffered saline or IL-18 protein were intraperitoneal (i.p.) injected every 2 days. (B–E) Representative images of the metastatic nodules in peritoneal cavity (B) and ascites formation (D) at day 60 post-inoculation. The quantification of metastatic nodules and ascites is shown in (C) and (E), respectively. Data are shown as means ± SEM (n = 7). ***p<0.001, by unpaired two-sided Student’s t-test. (F) Flow cytometry analysis of macrophages (CD45+ CD11b+ F4/80+) and M1-like (MHC II+ CD206-) and M2-like (MHC II- CD206+) subpopulations in ascites formed in C57BL/6 mice at 60 days after orthotopically inoculated with ID8 cells (means ± SEM, n = 5, *p<0.05, ***p<0.001, ns, not significant, by unpaired two-sided Student’s t-test). (G) Schematics summarizing the IL-20/IL20RA-OAS1/RNase L-NLR-IL-18 axis in preventing the transcoelomic metastasis of OC.

In conclusion, we discovered a new crosstalk of disseminated OC cells with peritoneal mesothelial cells and macrophages through IL-20/IL20RA/IL-18 axis in shaping the peritoneal immunomicroenvironment to prevent the transcoelomic metastasis of OC cells. OC cells, when disseminated into the peritoneal cavity, stimulate the mesothelial cells of the peritoneum to produce IL-20 and IL-24, which in turn activate the IL20RA downstream signaling in OC cells to trigger the OAS/RNase L-mediated NLR inflammasome signaling to produce mature IL-18, which consequently promotes the polarization of peritoneal macrophages into M1-like subtype to clear invaded OC cells in peritoneal cavity (Figure 9G). Highly metastatic OC cells always block this pathway by decreasing IL20RA expression, suggesting that reactivation of its downstream signaling, such as the application of IL-18, could be a useful strategy for the therapy of OC at advanced stages.

## Discussion

The common metastasis mode of OC is transcoelomic metastasis, in which the cancer cells disseminate into the peritoneal cavity and colonize on the peritoneum and abdominal organs. Transcoelomic metastasis occurs in about 70% of OC patients and many other types of cancers, such as pancreatic cancer, gastric cancer, endometrial cancer, and colon cancer (Mikuła-Pietrasik et al., 2018). Patients with transcoelomic metastasis are diagnosed at stages III and IV, which means high mortality and poor prognosis. The mechanisms, in particular, the peritoneal specific factors, behind this process still remain largely unclear. Here, through a genome-scale gene knockout screening in the orthotopic murine model of OC, we reveal an essential role of IL-20/IL20RA-mediated crosstalk between cancer cells and peritoneum mesothelial cells in regulating the polarization of peritoneal macrophages to prevent transcoelomic metastasis. This peritoneal-specific immune modulation mechanism may also happen in other types of cancers that can disseminate into the peritoneal cavity, such as gastric cancer, endometrial carcinoma, colon cancer, and bladder carcinoma, in which the high expression of IL20RA also correlates with a better clinical outcome of patients (Figure 2—figure supplement 1), highlighting the importance of IL-20/IL20RA-mediated epithelial immunity in preventing cancer metastasis into the peritoneal environment.

Immune cell-produced IL-20 subfamily cytokines and their receptors mainly expressed in epithelial cells facilitate the crosstalk between leukocytes and epithelial cells, which has essential functions in epithelial innate immunity for the host defense and tissue repair at epithelial surfaces. Due to the complicated effects of IL-20 subfamily cytokines in inflammation stimulation upon infection or injury and later immunosuppression for wound repair and tissue homeostasis restoration, both tumor-promoting and tumor-suppressing roles of IL-20 subfamily cytokines have been reported. IL-20 and IL-26 were discovered to promote proliferation and migration of bladder cancer, breast cancer, and gastric cancer cells, while IL-24 was found to inhibit the proliferation and metastasis of melanoma, prostate cancer, and OC (Fisher et al., 2007; Gopalan et al., 2007; Hsu et al., 2012; Lee et al., 2013; Pradhan et al., 2018; You et al., 2013). Although IL-20 subfamily cytokines have been extensively reported to activate STAT3 to exhibit oncogenic effects, STAT3 has also been shown to be able to switch its roles from tumor-promoting at early stages to tumor-suppressing in the invasion process (Musteanu et al., 2010). The different roles of IL-20 subfamily cytokines in tumor growth and metastasis may depend on the local inflammatory environment that involves a complex network of conversations between cancer cells and various stromal components. For OC metastasized to omentum, cancer cell-mediated conversion of omentum stromal cells, including adipocytes, fibroblasts, macrophages, and mesenchymal stem cells, to cancer-associated stromal cells is of vital importance for the metastatic growth of OC cells on omentum (Motohara et al., 2019; Thibault et al., 2014). The abdominal cavity is lined with a layer of mesothelial cells that form the first line of defense against microbial pathogens through the expression of retinoic acid-inducible gene-I-like (RIG-I–like) receptors, Toll-like receptors, and C-type lectin-like receptors (Colmont et al., 2011; Kato et al., 2004; Park et al., 2007). Besides, mesothelial cells can secret cytokines, chemokines, and growth factors to regulate the inflammatory responses in peritoneal cavity (Isaza-Restrepo et al., 2018; Yao et al., 2004). However, whether and how mesothelial cells response to cancer cells invaded into the peritoneal cavity remain largely unknown. It is more difficult for OC cells to attach to mesothelial cells compared with the extracellular matrix and the fibroblasts (Agarwal et al., 2019; Kenny et al., 2007; Niedbala et al., 1985). During the metastatic growth, OC cells can destroy the mesothelial cell layer by promoting the mesothelial-to-mesenchymal transition (MMT) of mesothelial cells and hence the loss of cell-cell adherence (Iwanicki et al., 2011; Kenny et al., 2011; Sandoval et al., 2013). Here, we revealed, for the first time, that mesothelial cells can actively respond to OC cells invaded into the peritoneal cavity by secreting IL-20 and IL-24 to communicate with OC cells, consequently resulting in a further crosstalk between OC cells and macrophages for the formation of an antitumor microenvironment. This mesothelial-initiated defense mechanism is oftentimes overcome by successfully metastasized OC cells through the downregulation of IL-20/IL-24 receptor IL20RA (Figure 2A–F) to shut down the communication between OC and mesothelial cells.

It has been reported that in OC patients the majority of cell types in ascites are lymphocytes (37%) and macrophages (32%), contributing to the progression and metastasis of OC (Kipps et al., 2013). Generally, macrophages have the potential to differentiate into cancer-inhibiting M1-subtype and cancer-promoting M2-subtype. The ratio of M1/M2-subtype macrophages has predictive value for the prognosis of OC patients, with a higher M1/M2-subtype ratio being associated with a better prognosis, while a higher CD163+ (M2-subtype)/CD68+ (total macrophages) ratio with a poor prognosis (Reinartz et al., 2014; Zhang et al., 2014). Re-polarization of macrophages to increase the ratio of M1/M2 macrophages in ascites is a promising strategy for the treatment of OC. It has reported that host-produced histidine-rich glycoprotein (HRG) could inhibit the growth and metastasis of tumors via re-polarizing the macrophages from M2-subtype to M1-subtype (Rolny et al., 2011). Nanoparticles encapsulating miR-125b could specifically re-polarize the peritoneal macrophages to M1-subtype, thereby improving the efficacy of paclitaxel in OC (Parayath et al., 2019). Here, we reveal IL20RA as a key receptor in regulating the polarization of peritoneal macrophages, which is silenced in disseminated OC cells for the accumulation of M2-subtype macrophages in the peritoneal cavity for a successful metastatic growth. This indicates that reactivation of IL-20/IL20RA signaling by the application of IL-20 or IL-24 may not be a useful strategy to prevent OC transcoelomic metastasis. However, we also identify the key downstream effector of IL-20/IL20RA signaling that promotes M1-like macrophage, IL-18, which is usually involved in the regulation of innate immune responses against various pathogens (Fabbi et al., 2015).

IL-18 is an immunoregulatory cytokine with anti-cancer effect in many types of cancers (Coughlin et al., 1998; Nishio et al., 2008; Salcedo et al., 2010; Zaki et al., 2010). The normal ovarian and colon epithelia have the capacity to process and release active IL-18, thereby supporting a local antitumor immune microenvironment. However, during the malignant transformation, the ovarian and colon cancer cells lose the ability to process IL-18 as a result of the defective Caspase-1 activation (Feng et al., 2005; Wang et al., 2002). Thus, OC cells express more pro-IL-18 but poorly produce mature-IL-18. Elevated IL-18 was reported in the ascites and sera of OC patients in a 23 kDa pre-form, whereas the 18 kDa mature and active form was undetectable (Orengo et al., 2011). Here, we show that reconstitution of IL20RA in highly metastatic OC cells can reactivate the production of mature IL-18 via IL-20/IL20RA-OAS1/RNase L-NLR axis, suggesting the silence of IL20RA to be a possible reason for the loss of mature IL-18 in OC. IL-18 has been shown to exert antitumor activity through the activation of T cell (Fabbi et al., 2015). Here, our results expand its roles to promote the polarization of macrophages to inflammatory M1-like subtype to exhibit a potent antitumor effect against OC. Several clinical trials testing the antitumor efficacy of IL-18 have been conducted in lymphomas and melanoma (Robertson et al., 2013; Robertson et al., 2006; Tarhini et al., 2009). Our study shows that the administration of recombinant IL-18 significantly suppresses the metastasis of IL20RA-deficient OC cells, suggesting the great value of IL-18 in the therapy of OC at advanced stages.

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
      <td>Gene (Mus musculus)</td>
      <td>Il20ra</td>
      <td>GenBank</td>
      <td>Gene ID: 237313</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>DH5α</td>
      <td>Shanghai Weidi Biotechnology</td>
      <td>Cat.#: DL1002</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BL21(DE3)</td>
      <td>CWBIO</td>
      <td>Cat.#: CW0809S</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>THP-1</td>
      <td>ATCC</td>
      <td>RRID:CVCL_0006</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HEK 293T</td>
      <td>ATCC</td>
      <td>RRID:CVCL_0063</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>SK-OV-3</td>
      <td>ATCC</td>
      <td>RRID:CVCL_0532</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>RAW 264.7</td>
      <td>ATCC</td>
      <td>RRID:CVCL_0493</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>ID8</td>
      <td>Merck</td>
      <td>RRID:CVCL_IU14</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Homo sapiens)</td>
      <td>IL20RA shRNA</td>
      <td>Sangon Biotech</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Mus musculus)</td>
      <td>Il18 shRNA</td>
      <td>Sangon Biotech</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Mus musculus)</td>
      <td>Il20rb shRNA</td>
      <td>Sangon Biotech</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IL20RA (Rabbit polyclonal)</td>
      <td>Abcam</td>
      <td>RRID:AB_2123854</td>
      <td>WB (1:1000) IHC (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IL20RB (Mouse monoclonal)</td>
      <td>Proteintech</td>
      <td>RRID:AB_11182930</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-ACTB (Mouse monoclonal)</td>
      <td>Immunoway</td>
      <td>RRID:AB_2629465</td>
      <td>WB (1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-STAT3 (Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>RRID:AB_628293</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-STAT3 (Mouse monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>RRID:AB_331757</td>
      <td>ChIP (5 μL for 7 μg DNA)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-p-STAT3 (Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>RRID:AB_628292</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-p-STAT3 (Rabbit polyclonal)</td>
      <td>Signalway Antibody</td>
      <td>RRID:AB_895980</td>
      <td>IHC (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IL18 (Rabbit polyclonal)</td>
      <td>Proteintech</td>
      <td>RRID:AB_2123636</td>
      <td>WB (1:1000) IHC (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-OAS1A (Mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>RRID:AB_10990911</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-OAS1 (Rabbit polyclonal)</td>
      <td>Proteintech</td>
      <td>RRID:AB_2158292</td>
      <td>WB (1:1000) IHC (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Caspase-1 (Rabbit polyclonal)</td>
      <td>Proteintech</td>
      <td>RRID:AB_2876874</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-ARG1 (Rabbit polyclonal)</td>
      <td>Proteintech</td>
      <td>RRID:AB_2289842</td>
      <td>IHC (1:750)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-NOS2 (Rabbit polyclonal)</td>
      <td>Proteintech</td>
      <td>RRID:AB_2782960</td>
      <td>IHC (1:750)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IL20 (Rabbit polyclonal)</td>
      <td>Abclonal</td>
      <td>RRID:AB_2750843</td>
      <td>IF (1:200) IHC (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IL24 (Rabbit polyclonal)</td>
      <td>Proteintech</td>
      <td>RRID:AB_2880630</td>
      <td>IF (1:200)  IHC (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Cytokeratin 18 (Mouse monoclonal)</td>
      <td>Abcam</td>
      <td>RRID:AB_305647</td>
      <td>IF (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD16/CD32 (Mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>RRID:AB_467133</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD45-PE (Mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>RRID:AB_312971</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD11b-APC (Mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>RRID:AB_312795</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-F4/80-APC/CY7 (Mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>RRID:AB_10803170</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-I-A/I-E-PERCP/CY5.5 (rat monoclonal)</td>
      <td>Biolegend</td>
      <td>RRID:AB_2191071</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD206-FITC (Mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>RRID:AB_10900988</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD11c-FITC (Mouse monoclonal)</td>
      <td>BD Biosciences</td>
      <td>RRID:AB_396683</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD3-FITC (Mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>RRID:AB_312661</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD4-APC (Rat monoclonal)</td>
      <td>BD Biosciences</td>
      <td>RRID:AB_398528</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD8-PE/CY7 (Mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>RRID:AB_469584</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD45R/B220-FITC (Rat monoclonal)</td>
      <td>BD Biosciences</td>
      <td>RRID:AB_394617</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLV-H1-EF1α-puro (plasmid)</td>
      <td>Biosettia</td>
      <td>Cat.#: SORT-B19</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLV-EF1α-MCS-IRES-Bsd (plasmid)</td>
      <td>Biosettia</td>
      <td>Cat.#: cDNA-pLV03</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET-20b(+) vector (plasmid)</td>
      <td>Novagen</td>
      <td>Cat.#: 69739–3</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Murine recombinant IL-20 protein</td>
      <td>Origene</td>
      <td>Cat.#: TP723795</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Murine recombinant IL-24 protein</td>
      <td>R&amp;D Systems</td>
      <td>Cat.#: 7807 ML-010</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Human recombinant IL-20 protein</td>
      <td>Sino Biological</td>
      <td>Cat.#: 13060-HNAE</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Murine recombinant M-CSF</td>
      <td>Peprotech</td>
      <td>Cat.#: 315-02-10</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>PMA</td>
      <td>Sigma-Aldrich</td>
      <td>Cat.#: 16561-29-8</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Clodronate liposomes</td>
      <td>LIPOSOMA</td>
      <td>Cat.#: CP-030030</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Murine IL18 ELISA Kit</td>
      <td>Wuxin Donglin Sci &amp; Tech Development</td>
      <td>Cat.#: DL-IL18-Mu</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Human IL18 ELISA Kit</td>
      <td>Wuxin Donglin Sci &amp; Tech Development</td>
      <td>Cat.#: DL-IL18-Hu</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Murine IL20 ELISA Kit</td>
      <td>Wuxin Donglin Sci &amp; Tech Development</td>
      <td>Cat.#: DL-IL20-Mu</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Murine IL24 ELISA Kit</td>
      <td>Wuxin Donglin Sci &amp; Tech Development</td>
      <td>Cat.#: DLIL24-Mu</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ChIP-IT Express Kits</td>
      <td>Active Motif</td>
      <td>Cat.#: 53035</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Cell culture and cytokine treatment

THP-1, RAW 264.7, A2780, SK-OV-3, and HEK 293T cells were purchased from the American Type Culture Collection (ATCC, Washington, USA). ES-2 cells were purchased from the Cell Bank of the Chinese Academy of Sciences (Shanghai, China). ID8 cells were purchased from Merck (Darmstadt, Germany) and screened in C57BL/6 mice for highly metastatic and HGSOC-like ID8 cells as described by Ward and colleagues (Diaz Osterman et al., 2019; Ward et al., 2013). Cell lines are mycoplasma free and genotypes were confirmed using Short Tandem Repeat (STR) profiling. SK-OV-3 and OVCAR-5 cells were cultured in McCoy's 5A Medium Modified (Biological Industries, Israel). ES-2, A2780, ID8, and HEK 293T cells were cultured in Dulbecco’s modified Eagle’s medium (DMEM) with high glucose (Biological Industries). THP-1 and RAW 264.7 cells were cultured in RPMI-1640 (Biological Industries). All the mediums were supplemented with 10% fetal bovine serum (Biological Industries), 100 U/mL penicillin, and 100 μg/mL streptomycin (Gibco, Grand Island, NY) and maintained at an atmosphere of 5% CO2% and 95% air at 37°C.

To study the role of IL-18, IL-20, and IL-24 protein in the polarization of RAW 264.7 cells, RAW 264.7 cells were treated with 5 ng/mL murine recombinant IL-18 protein or 5 ng/mL human recombinant IL-18 protein (10119-HNCE, Sino Biological, Beijing, China) or 5 ng/mL murine recombinant IL-20 protein (TP723795, Origene, Rockville, MD) or 5 ng/mL murine recombinant IL-24 protein (7807 ML-010, R&D Systems, Minneapolis, MN) for 72 hr, respectively. To detect the activation of signaling pathway, ID8 and SK-OV-3 cells were stimulated with 2.5 ng/mL murine and human recombinant IL-20 protein (Sino Biological) for 24 hr, respectively.

### The differentiation of THP-1 and BMCs

THP-1 was differentiated into macrophages by the treatment with 100 ng/mL PMA (Sigma-Aldrich, St Louis, MO) for 48 hr. BMCs were isolated from the femurs and tibias of C57BL/6 mice. The bone marrow in the femurs and tibias were flushed and collected with DMEM/F-12. Erythrocytes in bone marrow were lysed using Red Blood Cell Lysis Buffer (Solarbio, Beijing, China). BMCs were cultured in DMEM/F-12 supplemented with 20 ng/mL murine M-CSF (315-02-10, Peprotech, Cranbury, NJ) in a density of 4 × 106/mL. The medium was changed every 3 days. BMCs were differentiated into BMDM with the stimulation of M-CSF for 7 days. 5 mM of EDTA was used to detach the cells from the culture dishes. The detached cells were seeded in the six-well plates for subsequent treatment with CM from cancer cells.

### Establishment of stable cell lines

Knocking down IL20RA, IL-18, and IL20RB was achieved by the insertion of shRNA templates into the lentivirus- based RNAi vector pLV-H1-EF1α-puro (Biosettia, San Diego, CA). The sequence of shRNA targeting human IL20RA (shIL20RA) is 5′ AAAAC CCTCT CCTGT AAGAA CAAGT TGGAT CCAAC TTGTT CTTAC AGGAG AGGGT 3′, murine Il18 (shIL-18) is 5′ AAAAC CCTCT CCTGT AAGAA CAAGT TGGAT CCAAC TTGTT CTTAC AGGAG AGGGT 3′, murine Il20rb (shIL20RB) is 5′ AAAAG CTGGC ACTAG CTCTG TTTGC TTGGA TCCAA GCAAA CAGAG CTAGT GCCAG C 3′. The control shRNA plasmid targeting Escherichia coli lacZ gene (shCtrl) was purchased from Biosettia with the sequence of 5′ AAAAG CAGTT ATCTG GAAGA TCAGG TTGGA TCAAC CTGAT CTTCC AGATA ACTGC 3′. The coding sequence of mouse Il20ra was synthesized by Sangon Biotech (Shanghai, China) and cloned into plasmid pLV-EF1α-MCS-IRES-Bsd (Biosettia). All plasmids were validated by sequencing. The procedures of lentivirus package and infection were described previously (Chang et al., 2015). Cells infected with lentivirus for RNAi or reconstituted expression were selected with 2.5 μg/mL of puromycin and 2.5 μg/mL of blasticidin (Thermo Fisher Scientific, Waltham, MA), respectively.

### CRISPR/Cas9 knockout in vivo screening

GeCKO v2 human library made by Zhangfeng’s lab was purchased from Addgene (Watertown, MA) amplified as described (Joung et al., 2017). The library contains 122,756 sgRNAs targeting 19,050 genes and 1864 miRNAs, and 1000 non-targeting sgRNAs. Lentivirus carrying the library were generated and infected SK-OV-3 cells with the multiplicity of infection (MOI) around 0.5. After the selection with puromycin, 2 million SK-OV-3 cells expressing sgRNAs were orthotopically injected into NOD-SCID mice. The mice were sacrificed after 40 days. Primary tumors were dissected. Metastatic nodules in the peritoneal cavity were isolated, in vitro expanded for next run of orthotopic injection. After three rounds of in vivo selection, peritoneal metastatic cells were collected for subsequent high-throughput DNA deep sequencing to identify metastasis-related candidate genes. The RIGER P analysis was used to analyze the data of sgRNA libraries sequencing.

### Murine OC models

All of the animals were handled according to approved Institutional Animal Care and Use Committee protocols of the Nankai University. Animal experiments were approved by Institutional Animal Care and Use Committee of Nankai University (ethic approved number: 20180014). All attempts were made to minimize the handling time during surgery and treatment so as not to unduly stress the animals. Animals are observed daily after surgery to ensure there are no unexpected complications. 6–8-week-old female NOD-SCID and C57BL/6 mice were purchased from SPF Biotechnology (Beijing, China). 2 million human SK-OV-3 cells or 5 million murine ID8 cells suspended in 20 μL phosphate-buffered saline (PBS) were orthotopically injected into the left ovary of NOD-SCID and C57BL/6 mice, respectively. Ascites volumes and the numbers of metastatic nodules were measured, and total cells in ascites were harvested 40 days post-inoculation for the SK-OV-3 OC xenograft model and 60 days post-inoculation for the ID8 OC syngeneic model. For the intraperitoneal OC mouse model, 5 million ID8 cells suspended in 100 μL of PBS were injected directly into the peritoneal cavity of C57BL/6 mice. At day 45 post-injection, ascites and the number of metastatic nodules were analyzed.

To investigate the role of peritoneal macrophage in IL20RA-mediated OC metastasis, 5 million ID8 cells alone or together with 1.25 × 106 of BMDM (educated by CM from ID8 cells for 72 hr) in 100 μL of PBS were directly injected into the peritoneal cavity of C57BL/6 mice. In another model, 5 million IL20RA-reconstituted or control ID8 cells were injected into the peritoneal cavity of C57BL/6 mice. The mice were then intraperitoneal injected with PBS liposomes or clodronate liposomes (100 μL/10 g of mouse weight) (CP-030030, LIPOSOMA, Netherlands) every 3 days from day 4 to day 34 post-injection.

To identify the source of IL20RA ligands in peritoneal cavity, 5 million ID8 cells in 100 μL PBS (OC) or only 100 μL PBS (control) were directly injected into the peritoneal cavity of C57BL/6 mice. To investigate whether the intraperitoneal injection of SK-OV-3 cells was able to stimulate the production of IL20RA ligands, 5 million SK-OV-3 cells in 100 μL PBS (OC) or only 100 μL PBS (control) were directly injected into the peritoneal cavity of C57BL/6 mice. The mice were sacrificed 9 days post-injection. Peritoneal flushing fluid by PBS was collected. Total cells in peritoneal cavity were harvested for sorting the peritoneal macrophages. The total RNAs from intestine, abdominal wall, and ovary were extracted by using TRIzol reagent (Thermo Fisher Scientific) for subsequent gene expression analysis.

To investigate the therapeutic effect of IL-18, 5 million murine ID8 cells suspended in 20 μL PBS were orthotopically injected into the left ovaries of C57BL/6 mice. The mice were intraperitoneal injected with PBS or IL-18 protein (0.25 mg/kg of mouse weight) every 2 days from day 8 to day 60 post-injection.

### Analysis of OC patient samples

OC specimens from human patients were obtained from the Tianjin Center Hospital of Gynecology Obstetrics. The patients’ study was performed in accordance with the ethics committee of Nankai University and Tianjin Center Hospital of Gynecology Obstetrics (ethic approved number: 2018KY032) and conformed to the principles embodied in the Declaration of Helsinki. All OC patients from the Tianjin Center Hospital of Gynecology Obstetrics provided informed consent. Twenty fresh paired samples, including primary serous OC tissues, ascites, and metastasis nodules in peritoneal cavity, were obtained from OC patients during operation between 2017 and 2019. The inclusion criteria included serous ovarian adenocarcinoma, age >40, and TNM stage III–IV. Primary tumor tissues and metastases samples were dissected into two parts: one stored in 4% paraformaldehyde for IHC staining, the other stored in TRIzol reagent for the extraction of protein and RNA. Cancer cells in ascites were harvested for the extraction of protein and RNA. The histopathology and TNM stages of OC patients were confirmed by pathologists and clinical doctors.

The analysis on the correlation between the prognosis of OC patients and the expression of IL20RA or IL20RB were performed using the online Kaplan–Meier plotter tool (http://www.kmplot.com/) on serous OC cohorts (Gyorffy et al., 2012). The co-expression analysis on IL20RA with IL18 and OAS1 in OC patients was examined using the data from TCGA database (Ovarian Serous Cystadenocarcinoma, Provisional, n = 530). We used mRNA RNA-seq on pan-cancer section in the online Kaplan–Meier plotter tool to analyze the correlation between the prognosis of other cancer types and the expression of IL20RA.

### Protein extraction and western blot

The tissues were homogenized by TissueLyser (SCIENTZ-48, Ningbo, Zhejiang, China). Total protein in tissues was extracted using TRIzol reagent. Cells were lysed in RIPA lysis buffer with protease inhibitor cocktail (Roche Life Science, Switzerland) and phosphatase inhibitor cocktail (Sigma-Aldrich). The concentrations of proteins were measured by Pierce BCA Protein Assay Kit (Thermo Fisher Scientific), and 20 μg of total protein were loaded into Tris-acrylamide gels. Proteins were transferred onto PVDF membranes (Merck). The membranes were blocked with 5% defatted milk before blotted with primary antibodies and secondary antibodies (anti-mouse IgG-HRP [at 1:2000 dilution], anti-rabbit IgG-HRP [at 1:2000 dilution] [ZSGB-BIO, Beijing, China]). The membranes were incubated with Immobilon Western Chemiluminescent HRP Substrate (Merck) and visualized and photographed by Tanon-5200 (Tanon, Shanghai, China).

### IL-18 protein expression and purification

The coding sequence of the mature IL-18 was cloned into pET-20b plasmid (Novagen) before being transduced into E. coli BL21 (DE3) cells (CWBIO, Beijing, China). The expression of recombinant IL-18 was induced by 0.5 mM IPTG (Thermo Fisher Scientific) for 8 hr at 37°C. Cells were harvested and lysed by sonication in the lysis buffer (300 mM NaCl, 50 mM NaH2PO4 pH 8.0, 10 mM imidazole, and 2 mg/mL lysozyme). The supernatants were incubated with Ni-NTA agarose beads (Qiagen) overnight at 4°C. The beads were consecutively washed with wash buffer containing 20 mM imidazole (300 mM NaCl, 50 mM NaH2PO4 pH 8.0, 20 mM imidazole). The recombinant proteins were eventually eluted with elution buffer containing 250 mM imidazole (300 mM NaCl, 50 mM NaH2PO4 pH 8.0, 250 mM imidazole) and were dialyzed to remove imidazole. The endotoxin in the purified protein was removed using High Performance Endotoxin Removal Agarose Resin (20518ES10, Yeasen Biotech, Shanghai, China) and examined by using Kinetic Turbidimetric LAL (60401ES06, Yeasen Biotech) (final concentration of endotoxin <0.03 EU/mL).

### qRT-PCR

1 µg of total RNAs from cells and tissues were reversely transcribed into cDNAs using M-MLV reverse transcriptase (Promega, Madison, WI). Quantitative PCR analysis was performed by using SYBR Green SuperMix (Yeasen Biotech) on LightCycler96 system (Roche) with the program as follows: 95°C for 300 s, 45 cycles of two-step reaction, that is, 95°C for 30 s followed by 60°C for 45 s. The primer sequences are listed in Supplementary file 1. The relative gene expression was calculated by the 2-ΔΔCt method with β-actin used for the normalization.

### H&E staining, IHC, and IF

The tissues dissected from patients and mice were fixed in 4% paraformaldehyde, dehydrated, paraffin-embedded, consecutive sectioned in 6 μm thickness, and then deparaffinized. For H&E staining, tissue sections were stained with hematoxylin and eosin (Origene). For IHC staining, after treated with antigen retrieval solution (Solarbio) and 3% hydrogen peroxide, tissue sections were blocked with 5% goat serum, incubated with primary antibodies, biotin-conjugated secondary antibodies (Vector Laboratories, Burlingame, CA) and streptavidin-HRP (Vector Laboratories). The sections were visualized with 3,3′-diaminobenzidine (DAB) substrate (ZSGB-BIO), then counterstained with hematoxylin. Images were taken using an Olympus BX53 microscope (Tokyo, Japan). H score was used to quantify the degree of immunostaining, which was calculated by multiplying positively stained area (P) with staining intensity (I). The degrees for P were 0–4 (0, <5%; 1, 5–25%; 2, 25–50%; 3, 50–75%; 4, 75–100%). The degrees for I were 0–3 (0, none; 1, weak; 2, moderate; 3, strong). For IF staining, tissue sections were blocked with 5% goat serum, incubated with primary antibodies, secondary antibodies conjugated with Alexa Fluor-488 and Alexa Fluor-594 (Thermo Fisher Scientific), then counterstained with 4′,6-diamidino-2-phenylindole (DAPI, Sigma-Aldrich). Images were taken using an Olympus FV1000 confocal microscope (Tokyo, Japan).

### Flow cytometry

Total ascites was collected when the mice were sacrificed. Erythrocytes in ascites were lysed using Red Blood Cells Lysis Buffer (Solarbio). Cells were washed using PBS with 1% FBS and passed through a 40 μm nylon filter (BD Biosciences, San Diego, CA, USA), then cells were Fc-blocked with anti-CD16/32, and stained with CD45-PE, CD11b-APC, and F4/80-APC/CY7 antibodies for detecting macrophages. MHC II-PERCP/Cy5.5 and CD206-FITC antibodies were used to differentiate M1- and M2-subtype macrophages. For detecting T cells and B cells, cells were stained with CD45-PE, CD3-FITC, CD4-APC, CD8-PE/CY7, and CD45R/B220-FITC antibodies. Cells were incubated with the antibodies for 30 min in the dark and washed twice using PBS with 1% FBS. LSRFORTESSA (BD Biosciences) was used to obtained the data, and FlowJo software (BD Biosciences) was used to analyze the data.

### Isolation of peritoneal macrophages

Total cells in peritoneal cavity of healthy C57BL/6 mice were harvested by peritoneal lavage using PBS. As per the staining protocol described in flow cytometry, cells from peritoneal flushing fluid of healthy mice and ascites of OC mice were stained with CD11b-APC and F4/80-APC/CY7 antibodies. CD11b+ F4/80+ peritoneal macrophages were isolated from total cells using FACSAria SORP (BD Biosciences) and processed for RNA extraction.

### Cell proliferation and migration assay

The proliferation of ID8 and SK-OV-3 cells was examined by cell counting under the stimulation of IL-20. 2000 ID8 cells and SK-OV-3 cells were seeded in 96-well plates evenly. The cells were digested and counted by using the Invitrogen Countess II FL Automated Cell Counter (Thermo Fisher Scientific) every 24 hr until they reached nearly 100% confluence.

Transwell Permeable Supports System (Corning Inc, Corning, NY, USA) was used for SK-OV-3 cells migration assays. 2 × 104 cells in 200 μL medium containing 2% FBS were seeded into the top chamber of an 8 μm Millipore transwell insert in a 24-well plate, and medium containing 10% FBS was added to the bottom chamber. After 8 hr, cells migrated to the bottom surface of the transwell membranes were fixed in 4% paraformaldehyde and stained with crystal violet (Beyotime, Shanghai, China). The migration ability of RAW 264.7 cells was examined using indirect transwell cell culture system (8 μm, Millipore). 4 × 105 of ID8 cells were seeded in six-well plates evenly. After 24 hr, 1 × 105 of RAW 264.7 cells were seeded in the upper transwell chamber. After co-cultured for 24 hr, cells migrated to the bottom surface of the transwell membranes were fixed in 4% paraformaldehyde and stained with crystal violet. The membranes were washed by PBS. Images of the membranes were taken using an Olympus BX53 microscope (Tokyo, Japan), and the numbers of migrated cells were counted in five randomly chosen fields.

### CM stimulation and co-culture system

IL20RA-silenced SK-OV-3, IL20RA-reconstituted ID8 or their parallel control cells were cultured in 10 cm dishes for 72 hr with/without the stimulation of IL-20 protein, and their CM were collected and centrifuged at 2000 rpm for 10 min to obtain the supernatants. 2 × 105 of RAW 264.7 cells, 1 × 106 of BMDM, and 1 × 106 of THP-1-derived macrophages were seeded in six-well plates 24 hr before the medium was changed to fresh medium mixed with OC cell-derived CM at the ratio of 2:1 and incubated for 72 hr. The macrophages were then collected in TRIzol reagent for RNA extraction. To investigate the role of IL-18 in regulating the polarization of macrophages, RAW 264.7 cells were stimulated with the ID8 cell-derived CM supplemented with 5 μg/mL of IL-18 neutralizing antibody (R&D Systems) or 5 μg/mL of rat IgG1 Isotype as a control (Thermo Fisher Scientific).

Macrophages and OC cells were indirect co-cultured using 0.4 μm pore membrane transwell (Merck). 2 × 105 of RAW 264.7 cells and 1 × 106 of THP-1-derived macrophages were seeded in six-well plates and cultured for 24 hr before 1 × 105 of SK-OV-3 cells or 5 × 104 of ID8 cells stimulated with IL-20 protein were seeded in the upper transwell chamber. After co-cultured for 72 hr, macrophages were collected in TRIzol reagent for subsequent gene expression analysis. To investigate whether OC cells induce the production of IL-20 and IL-24 from peritoneum in vitro, abdominal wall and OC cells were co-cultured. 2 × 105 of ID8 cells were seeded in six-well plates. After 24 hr, 2 × 2 cm2 abdominal wall tissue collected from C57BL/6 mice was put in the medium of ID8 cells and co-cultured for 48 hr.

### ELISA

Cultured medium from ID8 and SK-OV-3 cells were collected. Total protein of cultured cells was extracted by using the cell lysis buffer (20 mM Tris-HCl [pH 7.5], 150 mM NaCl, 1 mM of EDTA, 1 mM EGTA, 1% Triton X-100, 2.5 mM sodium pyrophosphate, 1 mM beta-glycerophosphate, 1 mM Na3VO4, and protease inhibitor cocktail), and the concentration was measured by Pierce TM BCA Protein Assay Kit (Thermo Fisher Scientific) for normalization. The ascites from ID8 intraperitoneal OC mouse model were collected at 45 days post-injection. Peritoneal fluid washed by 1 mL PBS from mice with intraperitoneal injection of ID8 cells or PBS control was collected at 9 days post-injection. Cultured medium, ascites, and peritoneal flushing fluid were centrifuged at 1000 × g for 20 min at 4°C. The concentration of murine and human IL-18 in the supernatants was assayed by murine IL18 ELISA Kit (Wuxin Donglin Sci & Tech Development, Wuxi, Jiangsu, China) and human IL18 ELISA Kit (Wuxin Donglin Sci & Tech Development). The concentrations of murine IL-20 and IL-24 in peritoneal flushing fluid were assayed by murine IL20 ELISA Kit (Wuxin Donglin Sci & Tech Development) and murine IL24 ELISA Kit (Wuxin Donglin Sci & Tech Development). The OD (450 nm) values were measured by Infinite M200 PRO (TECAN, Männedorf, Switzerland) microplate reader. The data were analyzed by Curve Expert (Hyams Development).

### Deep RNA sequencing

Total RNA of IL20RA-reconstituted and control ID8 cells were stimulated with IL-20 for 24 hr before harvested using TRIzol reagent for RNA extraction. The deep RNA sequencing was performed and analyzed on BGI seq500 platform (BGI-Shenzhen, China). KEGG pathway analyses were conducted and analyzed based on KEGG pathway database (http://www.genome.jp/kegg/).

### ChIP-qPCR

The ChIP was performed by using ChIP-IT Express Kits according to the manufacturer’s instructions (Active Motif, San Diego, CA). For immunoprecipitation, 7 μg of sheared chromatin DNA fragments were incubated with IgG or STAT3-specific antibodies. qPCR assay was used to detect the relative enrichment. The primer sequences are listed in Supplementary file 1.

### Statistics

Prism 8.0 software (GraphPad Software, San Diego, CA, USA) was used for statistical analysis. Statistical parameters including the definitions and exact values of n, statistical test, and statistical significance are reported in the figures and figure legends. Quantitative data were presented as means ± SEM, and the differences between the groups were analyzed using the Student’s t-test. Survival curves were analyzed using the Kaplan–Meier method, and the log-rank test was used to calculate the differences between the curves. Differences are considered statistically significant at *p<0.05; **p<0.01; ***p<0.001; ns means no significance.
