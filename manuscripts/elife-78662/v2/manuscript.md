# CXCR4high megakaryocytes regulate host-defense immunity against bacterial pathogens

## Authors

- Jin Wang<sup>1</sup> ([ORCID: 0000-0002-4924-1716](https://orcid.org/0000-0002-4924-1716))
- Jiayi Xie<sup>2</sup> ([ORCID: 0000-0001-8977-6654](https://orcid.org/0000-0001-8977-6654))
- Daosong Wang<sup>3</sup> ([ORCID: 0000-0002-4786-6202](https://orcid.org/0000-0002-4786-6202))
- Xue Han<sup>2</sup>
- Minqi Chen<sup>3</sup>
- Guojun Shi<sup>1</sup> †
- Linjia Jiang<sup>2</sup> ([ORCID: 0000-0001-8854-2610](https://orcid.org/0000-0001-8854-2610)) †
- Meng Zhao<sup>2</sup> ([ORCID: 0000-0001-7909-7594](https://orcid.org/0000-0001-7909-7594)) †

### Affiliations

1. Department of Endocrinology & Metabolism, The Third Affiliated Hospital, Sun Yat-sen University Guangzhou China ([ROR:04tm3k558](https://ror.org/04tm3k558))
2. RNA Biomedical Institute, Sun Yat-sen Memorial Hospital, Sun Yat-sen University Guangzhou China ([ROR:01px77p81](https://ror.org/01px77p81))
3. Key Laboratory of Stem Cells and Tissue Engineering, Zhongshan School of Medicine, Sun Yat-sen University, Ministry of Education Guangzhou China ([ROR:0064kty71](https://ror.org/0064kty71))

† Corresponding author

## Abstract

Megakaryocytes (MKs) continuously produce platelets to support hemostasis and form a niche for hematopoietic stem cell maintenance in the bone marrow. MKs are also involved in inflammatory responses; however, the mechanism remains poorly understood. Using single-cell sequencing, we identified a CXCR4 highly expressed MK subpopulation, which exhibited both MK-specific and immune characteristics. CXCR4high MKs interacted with myeloid cells to promote their migration and stimulate the bacterial phagocytosis of macrophages and neutrophils by producing TNFα and IL-6. CXCR4high MKs were also capable of phagocytosis, processing, and presenting antigens to activate T cells. Furthermore, CXCR4high MKs also egressed circulation and infiltrated into the spleen, liver, and lung upon bacterial infection. Ablation of MKs suppressed the innate immune response and T cell activation to impair the anti-bacterial effects in mice under the Listeria monocytogenes challenge. Using hematopoietic stem/progenitor cell lineage-tracing mouse lines, we show that CXCR4high MKs were generated from infection-induced emergency megakaryopoiesis in response to bacterial infection. Overall, we identify the CXCR4high MKs, which regulate host-defense immune response against bacterial infection.

## Introduction

Megakaryocytes (MKs) are large and rare hematopoietic cells in the bone marrow, which continually produce platelets to support hemostasis and thrombosis (Deutsch and Tomer, 2006). MK progenitors undergo multiple rounds of endomitosis during maturation to achieve polyploidy (Chang et al., 2007; Deutsch and Tomer, 2013; Machlus and Italiano, 2013; Nagata et al., 1997; Patel et al., 2005). MKs and their progenitors migrate between distinct microenvironments and organs for their proliferation, maturation, and biological functions (Avecilla et al., 2004; Fuentes et al., 2010; Lefrançais et al., 2017; Pal et al., 2020; Tamura et al., 2016; Wang et al., 1998). Although platelet generation is the prominent role of MKs, emerging evidence suggests that MKs have other biological functions. Mature MKs interact with HSCs and constitute a unique niche to preserve HSC quiescence in the bone marrow (Bruns et al., 2014; Zhao et al., 2014). MKs also interact with other niche cells, such as osteoblasts (Dominici et al., 2009; Olson et al., 2013), non-myelinating Schwann cells (Jiang et al., 2018; Yamazaki et al., 2011), and blood vessels (Avecilla et al., 2004; Saçma et al., 2019) to further influence the attraction and retention of hematopoietic stem and progenitor cells during homeostasis and stress.

MK-biased hematopoietic stem cells (HSCs) induce emergency megakaryopoiesis to actively generate MKs upon acute inflammation, which can efficiently replenish the platelet loss during inflammatory insult (Haas et al., 2015). Studies suggested that MKs might participate in immune responses independent of their platelet generation role (Cunin and Nigrovic, 2019). MKs express multiple immune receptors, such as IgG Fc receptors and toll-like receptors (TLRs), enabling them to sense inflammation directly (Cunin and Nigrovic, 2019). Mature MKs also express major histocompatibility complex (MHC) to activate antigen-specific CD8+ T cells and enhance CD4+ T cells and Th17 cell responses through stimulating antigen processing (Finkielsztein et al., 2015; Pariser et al., 2021; Zufferey et al., 2017). Furthermore, MKs release multiple cytokines and chemokines to influence immune cells. For example, MKs produce IL-1α and IL-1β to promote arthritis susceptibility in mice resistant to arthritis (Cunin et al., 2017) and produce CXCL1 and CXCL2 to promote neutrophil efflux from the bone marrow (Köhler et al., 2011). Lung MKs contribute to thrombosis (Lefrançais et al., 2017) and, more interestingly, participate in immune responses (Pariser et al., 2021), although the relationship between lung MKs and bone marrow circulating MKs (Nishimura et al., 2015) remains unexplored. Furthermore, the recent single-cell atlas shows that MKs are heterogeneous and contain subpopulations that express multiple immune genes and are involved in inflammation response (Liu et al., 2021; Pariser et al., 2021; Sun et al., 2021; Yeung et al., 2020). Here, by combining scRNA-seq with functional assays, we identified a CXCR4high MK population, which was generated by infection-induced emergency megakaryopoiesis, and stimulated innate immunity against bacterial infection.

## Results

### Single-cell atlas identifies an immune-modulatory subpopulation of MKs

We applied droplet-based scRNA-seq with CD41+ forward scatter (FSC)high bone marrow MKs to explore the MK heterogeneity (Figure 1A; Figure 1—figure supplement 1A,B). To enrich accurate MKs, we further performed transcriptomic profile analysis in the phenotypically enriched MKs (Yeung et al., 2020). Our scRNA-seq successfully detected 5368 high-quality cells (Figure 1—figure supplement 1B,C), in which one MK cluster (1712 cells) and six immune cell clusters (3656 cells) were annotated according to their gene profile (Figure 1—figure supplement 1D-G) and the alignment with published scRNA-seq data (Almanzar et al., 2020; Hamey et al., 2021; Pariser et al., 2021; Xie et al., 2020; Yeung et al., 2020). Our annotated MKs were similar to MKs but distinct to immune cells, including myeloid progenitors, basophils, neutrophils, monocytes, dendritic cells, macrophages, B cells, and T cells, in an integrated scRNA-seq analysis platform (Figure 1—figure supplement 2). Therefore, we re-clustered the transcriptionally enriched 1712 MKs into five subpopulations, termed MK1 to MK5 (Figure 1B; Figure 1—figure supplement 3A,B), which were further confirmed by the integrated scRNA-seq analysis platform to rule out the potential immune cell contamination (Pariser et al., 2021; Xie et al., 2020; Yeung et al., 2020; Figure 1—figure supplement 3C,D). We noticed that mature MKs with huge sizes were captured at a relatively low rate, potentially due to the limitation in current techniques in cell purification and single-cell preparation (Liu et al., 2021; Sun et al., 2021).

![Figure 1.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig1-v2.jpg)

**Figure 1.:** (A) Schematic strategy for MK preparation, scRNA-seq and data analysis. (B) Clustering of 1712 bone marrow MKs. (C) Heatmap of signature gene expression in MK subpopulations (fold-change >1.5, p value <0.05) with exemplar genes listed on the right (top, color-coded by subpopulations). Columns denote cells; rows denote genes. Z score, row-scaled expression of the signature genes in each subpopulation. (D) Gene Ontology (GO) analysis of signature genes (fold-change >1.5, p value <0.05) for each MK subpopulations. GO terms selected with Benjamini–Hochberg-corrected p values <0.05 and colored by –log10(p value). Bubble size indicates the enriched gene number of each term. (E–F) UMAP visualization (E) and statistical analysis (F) of cytokine score (left), inflammatory score (middle) and chemokine score (right) in MK1 to 5. (G) Dotplots of significant cytokine ligand (source) -receptor (target) interactions between MKs and immune cells discovered. The color indicates the means of the receptor-ligand pairs between two cell types and bubble size indicates p values. Mon, monocytes; MΦ, macrophages (Dong et al., 2020); DC, dendritic cells; Neu, neutrophils; MP, myeloid progenitors; T, T cells; B, B cells. (H–I) Violin plot (H) and feature plot (I) of selected signature genes of MK5. Red lines in (H) indicate the median gene expression. Repeated-measures one-way ANOVA followed by Dunnett’s test for multiple comparisons in (F), ǂǂ <0.01, ǂǂǂ p<0.001.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Flow cytometry gating for isolation of MKs (CD41+ FSChigh) in bone marrow for scRNA-seq. (B) Quality control of scRNA-seq data. Violin plots showing the number of unique genes (gene number) before and after removing doublets, number of total unique molecular identifiers (UMI counts) and percentage of mitochondrial transcripts in single cells after removing doublets. Scatter plot showing the correlation between UMI counts and gene numbers. corr indicates Pearson correlation coefficient. (C–D) UMAP of 5368 bone marrow cells, colored by gene numbers (C) and by cluster identity indicated on the right (D). MK, megakaryocytes; Neu, neutrophils; MΦ, macrophages; MP, myeloid progenitors; DC, dendritic cells; Mon, monocytes; B, B cells; T, T cells. (E) Heatmap of row-scaled signature gene expression in each cell type (top, color-coded by subpopulations). Columns denote cells; rows denote genes. Z score, row-scaled expression of the signature genes in each subpopulation. (F) Feature plots showing selected gene expression. (G) Violin plots showing the number of unique genes (gene number) of 1712 MKs.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Radar charts showing cell similarities of our single cell dataset with the published bone marrow MK single cells (Pariser et al., 2021; Yeung et al., 2020), bone marrow immune cells and myeloid progenitor single cells (Almanzar et al., 2020; Hamey et al., 2021; Xie et al., 2020) using MetaNeighbor R package. (B) Comparison of our bone marrow scRNA-seq data with published bone marrow MK (Pariser et al., 2021; Yeung et al., 2020) and immune cell (Almanzar et al., 2020; Hamey et al., 2021; Xie et al., 2020) datasets. All cells were integrated by iMAP.py and projected on UMAP. (C) Column-scaled Euclidean distances between the centroid of each cluster. Z score, column-scaled Euclidean distance. MK, megakaryocytes; Neu, neutrophils; MΦ, macrophages; MP, myeloid progenitors; DC, dendritic cells; Mon, monocytes; B, B cells; T, T cells.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Re-clustering of 1712 MKs from 5368 cells. (B) Violin plots showing MK marker gene expression (Aburima et al., 2021; Bernardes et al., 2020; Kanaji et al., 2005; Liu et al., 2021; Couldwell and Machlus, 2019; Ozaki et al., 2005; Sun et al., 2021; Yeung et al., 2020) of MK1 to 5. Red lines indicate the median gene expression. (C) Projection of our datasets on reported MK (Pariser et al., 2021; Yeung et al., 2020) and immune cell (Hamey et al., 2021; Xie et al., 2020) scRNA-seq datasets by Symphony R package. MK, megakaryocytes; Neu, neutrophils; MΦ, macrophages; MP, myeloid progenitors; DC, dendritic cells; Mon, monocytes; Bas, basophils; B, B cells; T, T cells; ABM, adult bone marrow. (D) MKs (MK1 to 5) and cell types projection based on similarities of our single-cell transcriptional profiles and published MK (Pariser et al., 2021; Yeung et al., 2020) and immune cell datasets (Hamey et al., 2021; Xie et al., 2020) by scmap R package.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A) Volcano plot showing MK5 and MK1 to 4 enriched genes (|fold change|>1.4, p value <0.05). (B–C) Gene Ontology (GO) analysis showing MK5 enriched immune pathway genes and MK1 to 4 mainly enriched hemopoiesis and RNA processing pathway genes. (D–F) Gene set enrichment analysis (GSEA) evaluated enrichment of selected pathways in MK5 cells compared to other MK subpopulations (MK1 to 4).

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** (A) Dotplots of significant cytokine ligand (source) -receptor (target) interactions between MKs and immune cells discovered using CellChat. Color indicates communication probabilities, and bubble size indicates p value of the ligand-receptor pairs between MK subpopulations (source) and immune cells (target). (B) Selected signature gene expression in MK subpopulations.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** (A) Representative flow cytometry plots of gating strategy of CD41 and CXCR4 in the bone marrow of control mice and mice 3 days after L. monocytogenes infection. (B) Relative expression of Pf4, Vwf and Mpl in CXCR4high and CXCR4low MKs by RT-qPCR. (C) Representative immunofluorescent staining image showing membranous CD41 staining typical of sorted bone marrow CXCR4high MKs. (D) Sorted CXCR4low and CXCR4high MKs produced proplatelets in vitro on day five post cultured under 100 ng ml–1 TPO. White arrowheads indicate proplatelet formation. (E) Polyploidy distribution of CXCR4low MKs and CXCR4high MKs (right). (F) Representative immunofluorescent staining images showing CD41 and CXCR4 expression of CXCR4low and CXCR4high MKs in the bone marrow. CD41, green; CXCR4, red; DAPI, blue. (G) Comparison of cell size between CXCR4low MKs and CXCR4high MKs on day three post cultured under 100 ng ml–1 Thrombopoietin (TPO). (H) Median fluorescence intensity of CXCR4 in small and large sizes of MKs by flow cytometry. Scale bars, 20µm. Data represent mean ± s.e.m in (B, D, E, H) or mean ±first and third quartiles in (G). Two-sample KS test was performed to assess statistical significance in (G). Two-tailed Student’s t-test was performed to assess statistical significance in (B, D, E, H). * p<0.05, ** p<0.01, *** p<0.001.

Enriched signature genes by Gene Ontology exhibited that MK1 and MK2 highly expressed nuclear division, DNA replication and repair genes for endomitosis (Figure 1C,D). MK3 enriched blood coagulation and thrombosis genes for platelet generation (Figure 1C,D). No signature pathways were enriched in MK4. MK5 enriched cell migration and immune response genes (Figure 1C,D; Figure 1—figure supplement 4A-E), cytokine, chemokine (Figure 1E,F; Figure 1—figure supplement 4F), and genes involved in immune cell interaction (Figure 1G, Figure 1—figure supplement 5A). MK5 also expressed signature genes in recently reported inflammatory-related MKs (Cd53, Lsp1, Anxa1, Spi) (Sun et al., 2021) and immune MKs (Ccl3, Cd52, Selplg, Sell, Adam8) (Liu et al., 2021; Figure 1—figure supplement 5B). We also noticed that MK5 highly expressed Cxcr4 than other MK subpopulations (Figure 1H,I), although most MKs express CXCR4 (Hamada et al., 1998; Figure 1—figure supplement 6A). To confirm this, we found that CXCR4high MKs expressed MK markers (Figure 1—figure supplement 6B), were mainly polyploid cells (Figure 1—figure supplement 6C), and had platelet generation ability (Figure 1—figure supplement 6D), although they have relatively low polyploidy (Figure 1—figure supplement 6E) and smaller cell size (Figure 1—figure supplement 6F-H). CXCR4high MKs generated platelets in lower efficiencies compared to CXCR4low MKs (Figure 1—figure supplement 6D), suggesting CXCR4high MKs might be specialized for immune functions. Overall, using scRNA-seq, we identified an MK subpopulation that exhibited both MK-specific and immune transcriptional characteristics.

### CXCR4high MKs enhance myeloid cell mobility and bacterial phagocytosis

As MK5 enriched genes involved in myeloid cell activation (Figure 1—figure supplement 4E) and myeloid cell interactions (Figure 1G, Figure 1—figure supplement 5A), we further explored the role of CXCR4high MKs, which enriched MK5, in regulating myeloid immune cells, in regulating the innate immunity function of myeloid cells against pathogens. We challenged mice with Listeria (L.) monocytogenes, a Gram-positive facultative intracellular bacterium (Bishop and Hinrichs, 1987; Edelson and Unanue, 2000), which induce myelopoiesis (Eash et al., 2009; Figure 2—figure supplement 1A, B). Interestingly, we noticed that CXCR4high MKs were more dramatically associated with myeloid cells in the bone marrow of mice 3 days after L. monocytogenes infection, which was a significant increase than the association between myeloid cells and CXCR4low MKs or the association between randomly placed myeloid cells and CXCR4high MKs (Figure 2A,B). The myeloid cell-CXCR4high MK association (mean distance 15.36 μm) was significantly closer than the myeloid cell-CXCR4low MKs association (Figure 2C; mean distance 25.62 μm, p=7.0 × 10–4 by KS test), and the association between randomly placed myeloid cells and CXCR4high MKs [35.37 μm, p (μ<15.36)=1.8 × 10–10] in the bone marrow of mice 3 days after L. monocytogenes infection. Whereas the observed mean distance of myeloid cells to CXCR4low MKs (25.62 μm) is not different from random simulations [27.76 μm, p (μ<25.62)=0.14] (Figure 2C). This suggested that the increased association between myeloid cell-CXCR4high MK may not be due to the infection-induced expansion of myeloid cells. Furthermore, we did not observe a significant association between myeloid cells and MKs during homeostasis (Figure 2—figure supplement 1C,D). We also noticed that bone marrow myeloid cells were preferably adjacent to the CXCR4high MK-blood vessel intersection in mice 3 days after L. monocytogenes infection (Figure 2—figure supplement 1E,F). These observations indicated that CXCR4high MKs might regulate myeloid cells upon bacterial infection.

![Figure 2.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig2-v2.jpg)

**Figure 2.:** (A) Distribution of myeloid cells to CXCR4low or CXCR4high MKs 3 days after L. monocytogenes infection. Representative images of MKs (blue), CXCR4 (red), and myeloid cells (green) in mouse bone marrow. Yellow arrows indicate CXCR4high MKs and white arrowheads indicate CXCR4low MKs. (B–C) Distance (B) and mean distance (C) of actual or randomly positioned myeloid cells to the closest CXCR4low and CXR4high MKs 3 days after L. monocytogenes infection. (D) Numbers of transmigrated myeloid cells normalized to Ctrl (without MKs in the lower chambers) as indicated by transwell assays. Mon, monocytes; MΦ, macrophages; DC, dendritic cells; Neu, neutrophils. (E–F) Representative images (E) and quantification (F) of neutrophil phagocytosis capacity with or without MK co-culture as indicated. CD11b, red; E. coli, green; DAPI, blue. Ctrl, neutrophil without MK co-culture. (G–H) Representative images (G) and quantification (H) of macrophage phagocytosis capacity with or without MK co-culture as indicated. F4/80, red; E. coli, green; DAPI, blue. Ctrl, macrophage without MK co-culture. (I) Spearman correlation analysis between expression profiles of Cxcr4 and feature genes in MK subpopulations. (J) Quantification of TNFα+ and IL-6+ cells in CXCR4low MKs and CXCR4high MKs from control mice or mice 3 days after L. monocytogenes infection. (K–L) Quantification of neutrophil (K) and macrophage (L) phagocytosis with or without CXCR4high MK co-culture in the absence or presence of anti-TNFα or anti-IL-6 neutralizing antibodies. (M–N) Quantification of the phagocytosis abilities by neutrophils (M) and macrophages (N) with or without CXCR4low MK or CXCR4high MK co-culture in the absence or presence of anti-TNFα or anti-IL-6 neutralizing antibodies by flow cytometry. Ctrl, neutrophils (M) or macrophages (N) without MKs co-culture. Scale bars, 20 μm (A, E, G). Data represent mean ± s.e.m (D) and boxplots show medians, first and third quartiles (F, H, K–L). Repeated-measures one-way ANOVA followed by Dunnett’s test for multiple comparisons in (D, M, N), ǂ p<0.05, ǂǂ p<0.01, n.s., not significant. A two-sample KS test was performed to assess statistically significant (C, F, H, K, L), n.s., not significant. Paired Student’s t-test was performed to assess statistical significance (J), # p<0.05, ## p<0.01, n.s., not significant.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A–B) Representative immunofluorescent staining image (A) and statistical analysis (B) showing association of MKs (blue) and myeloid cells (green) in the bone marrow of control mice and mice 3 days after L. monocytogenes infection (n=30 control and infected MKs). CD41, blue; CD11b, green. (C–D) Distance (C) and mean distance (D) of actual or randomly positioned myeloid cells to the closest CXCR4low Mks and CXR4high MKs from mice without infection. (E–F) Representative images of MKs (blue), CXCR4 (red), vascular endothelial cells (green) and myeloid cells (white) (E), and statistical analysis (F) in bone marrow showing the distribution of myeloid cells to CXCR4low or CXCR4high MKs and vascular cells 3 days after L. monocytogenes infection. CD41, blue; CXCR4, red; EMCN, green; CD11b, white. Yellow arrows indicate CXCR4high MKs and white arrowheads indicate CXCR4low MKs (left) and two-dimensional probability distribution of distances from myeloid cells to CXCR4low or CXCR4high MKs and vascular cells (n=104 CD11b+ cells; p=0.04 by 2D KS test). Scale bars, 20µm. Boxplots show medians, first and third quartiles in (B). Two-sample KS test was performed to assess statistical significance in (B, D). Two-dimensional-two-sample KS test was performed to assess statistical significance in (F).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A–B) Quantification of phagocytosis abilities in neutrophils (A) and macrophages (B) without or with CXCR4low MKs or CXCR4high MKs as indicated. (C–E) TNFα and IL-6 protein levels in CXCR4low and CXCR4high MKs were shown by immunofluorescent staining (C–D) using sorted MKs, compared to their levels in sorted macrophages upon L. monocytogenes infection (E).Scale bars, 5μm. Data represent mean ± s.e.m in (A, B) and boxplots show medians, first and third quartiles in (C–E). Repeated-measures one-way ANOVA followed by Dunnett’s test for multiple comparisons in (A, B), ǂ p<0.05, ǂǂ p<0.01. Two-sample KS test was performed to assess statistical significance in (C–E).

To explore how CXCR4high MKs regulate myeloid cells, we interestingly found that CXCR4high MKs, but not CXCR4low MKs, effectively promoted myeloid cell mobilization in our transwell assays (Figure 2D). Furthermore, we asked whether CXCR4high MKs regulate myeloid cell function against pathogens. To this aim, we incubated purified CXCR4low MKs and CXCR4high MKs with neutrophils or macrophages for bacterial phagocytosis analysis. We found that CXCR4high MKs, but not CXCR4low MKs, efficiently enhanced the bacterial phagocytosis of neutrophils and macrophages (Figure 2E–H; Figure 2—figure supplement 2A,B).

Our scRNA-seq also exhibited that the high expression of Cxcr4 was positively correlated with immune cell-stimulating cytokines, such as Ccl6, Tnf, and Il6 (Li et al., 2018; Rothe et al., 1993; Shapouri-Moghaddam et al., 2018) in MKs (Figure 2I). In line with this, CXCR4high MKs had higher TNFα and IL-6 protein levels than CXCR4low MKs (Figure 2J; Figure 2—figure supplement 2C,D). The TNFα and IL-6 levels in CXCR4high MKs were comparable to macrophages from mice 3 days after L. monocytogenes infection (Figure 2—figure supplement 2E), which are known as the primary cellular source of TNFα and IL-6 upon infection (Shapouri-Moghaddam et al., 2018). These observations suggested that CXCR4high MKs might stimulate myeloid cell phagocytosis by producing TNFα and IL-6. Indeed, anti-TNFα and anti-IL-6 blocking antibodies compromised the role of CXCR4high MKs in stimulating bacterial phagocytosis of neutrophils and macrophages (Figure 2K–N).

### CXCR4high MKs stimulate host-defense immunity against bacterial pathogens

To explore the in vivo role of MKs upon L. monocytogenes infection in mice, we employed Pf4Cre; Rosa26fs-iDTR mice, in which MKs were rendered sensitive to diphtheria toxin (DT) (Zhao et al., 2014; Figure 3A and B). MK ablation increased the number of hematopoietic stem and progenitor cells and myelopoiesis in the bone marrow upon infection (Figure 3—figure supplement 1A-D). Notably, MK ablation dramatically increased the bacterial burdens in the liver and spleen 3 days after L. monocytogenes infection (Figure 3C). We also found that MK ablation reduced the number of myeloid cells, including monocytes, macrophages, dendritic cells (DCs), and neutrophils, in the liver and spleen (Figure 3D,E; Figure 3—figure supplement 1E,F), suggesting the role of MKs in promoting myeloid cells against pathogens. We further investigated whether MKs regulate adaptative immunity against pathogen infection. Interestingly, we noticed that CXCR4high MKs were able to phagocytose bacteria and presented the ovalbumin (OVA) antigens on their surface via MHC-I (Figure 3F,G). Furthermore, OVA antigens presented by CXCR4high MKs activated OT-I CD8+ T cells (Figure 3H) and B3Z T cells (Figure 3—figure supplement 2), a T cell hybridoma which expresses TCR that specifically recognizes OVA (Karttunen et al., 1992). We challenged Pf4Cre; Rosa26fs-iDTR mice with OVA-expressing recombinant microbe (L. monocytogenes-OVA). Seven days after L. monocytogenes-OVA infection, splenocytes from control or MK ablated mice were re-stimulated with OVA peptide in vitro to assess OVA-specific T cell activation (Figure 3I). Notably, MK ablation dramatically reduced the number of CD4+ IFNγ+ Th1, CD4+ IL4+ Th2, and CD8+ cytotoxic T lymphocytes but did not impact the total number of CD4+ T cells and CD8+ T cells (Figure 3J). These observations demonstrated that MKs regulate host-defense immunity against L. monocytogenes infection. To explore whether CXCR4high MKs contribute to the immune response against bacterial pathogens, we infused the purified CXCR4high MKs and CXCR4low MKs into MK ablation mice during L. monocytogenes infection (Figure 3K). Notably, we found that the infusion with CXCR4high MKs, but not CXCR4low MKs, partially rescued the bacterial clearance defect in MK ablation mice (Figure 3L). This is potentially due to the reduced platelets known for regulating immune responses (Semple et al., 2011).

![Figure 3.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig3-v2.jpg)

**Figure 3.:** (A) Schema for diphtheria toxin (DT) and L. monocytogenes administration used for the experiments shown in (B–E). (B) Representative images of MKs (blue, indicated by arrows) and vascular endothelial cells (green) in the bone marrow of mice after four daily DT treatments. (C) Bacterial burdens in the liver and spleen of Pf4Cre; Rosa26fs-iDTR mice 3 days after L. monocytogenes (L.m.) infection with four-time DT injections. (D–E) Myeloid cells in the liver (D) and spleen (E) of Pf4Cre; Rosa26fs-iDTR mice 3 days after L. monocytogenes (L.m.) infection with four-time DT injections. (F) Quantification of bacterial phagocytosis capacities of neutrophils, CXCR4low MKs and CXCR4high MKs. (G) Quantification of MHCI-OVA levels on CXCR4low MKs, CXCR4high MKs and bone-marrow-derived dendritic cells (DCs) upon a pulse of 24 hr with or without OVA. (H) Quantification of activated OT-I CD8+ T cells after co-culture with bone-marrow-derived DCs, OVA-pulsed bone-marrow-derived DCs, CXCR4low MKs, or CXCR4high MKs. (I) Schema for antigen-specific T cell activation assay shown in (J). (J) Splenocytes from control or MK ablated mice 7 days after L. monocytogenes-OVA257-264 infection and seven DT injections were stimulated with OVA peptide in vitro for 4 hr, and antigen-specific activated T cells were quantified (n=4 mice). L.m.-OVA, L. monocytogenes-OVA257-264. (K) Schema for DT, L. monocytogenes administration, MK transfusing and bacterial burden determination shown in (L). (L) Bacterial burdens in the liver and spleen of Pf4Cre; Rosa26fs-iDTR mice without or with CXCR4low or CXCR4high MK transfused. Scale bars, 20μm. Data represent mean ± s.e.m. Repeated-measures one-way ANOVA followed by Dunnett’s test for multiple comparisons in (F), ǂǂǂ p<0.001. Paired Student’s t-test was performed to assess statistical significance (G), # p<0.05, n.s., not significant. Two-tailed Student’s t-test was performed to assess statistical significance except (F), * p<0.05, ** p<0.01, *** p<0.001, n.s., not significant.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Schema for diphtheria toxin (DT) and L. monocytogenes administration used for the experiments shown in (B–D). (B) Number of bone marrow hematopoietic stem and progenitor cells in Pf4Cre+; Rosa26fs-iDTR+/- mice compared to Pf4Cre-; Rosa26fs-iDTR+/- mice after L. monocytogenes infection and DT injection. (C–D) Gating strategies (C) and numbers (D) of myeloid cells in the bone marrow of Pf4Cre; Rosa26fs-iDTR+/- mice after L. monocytogenes infection and DT injection. (D–E) Gating strategies of myeloid cells in the liver (D) and spleen (E) of Pf4Cre; Rosa26fs-iDTR+/- mice at 3 days after L. monocytogenes infection. Neu, neutrophil; MF, macrophage; Mono, monocyte; DC, dendritic cell. Two-tailed Student’s t-test was performed to assess statistical significance. * p<0.05, ** p<0.01, *** p<0.001.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** The LacZ activity in B3Z T cells with or without co-culture as indicated. Ctrl indicates B3Z cells without MKs co-culture; bone-marrow-derived DCs, CXCR4low MKs and CXCR4high MKs were pulsed with OVA for 24 hr. Two-tailed Student’s t-test was performed to assess statistical significance, * p<0.05.

### Bacterial infection stimulates the migration of CXCR4high MKs

High Cxcr4 expression indicated that CXCR4high MKs might migrate between the bone marrow microenvironment and circulation in response to infection (Suraneni et al., 2018). In line with this, our spatial distribution analysis showed that ~80% of MKs directly contacted blood vessels 3 days after L. monocytogenes infection, which was much higher than in control mice (~40%) (Figure 4A,B; Figure 4—figure supplement 1A). Furthermore, more CXCR4high MKs, with small cell sizes (Figure 1—figure supplement 6F-H), were tightly associated with blood vessels and trapped in the sinusoid than CXCR4low MKs 3 days after L. monocytogenes infection (Figure 4C,D). However, L. monocytogenes infection did not influence the association between MKs and HSCs (Figure 4A,E), albeit the critical role of perivascular MKs in maintaining HSC quiescence (Bruns et al., 2014; Itkin et al., 2016; Zhao et al., 2014) and the dramatic HSC activation upon infection (Figure 4—figure supplement 1B).

![Figure 4.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig4-v2.jpg)

**Figure 4.:** (A) Representative image of CD41 (blue), CD150 (red), EMCN (green), and lineage cells (white) in bone marrow from control mice or mice at 3 days after L. monocytogenes infection. dHSC and dEC indicate the distance between the MK (blue, marked with an asterisk) and the closest HSC (red), endothelial cell (green), respectively. Yellow boxes indicate the locations of the magnified images. Arrowheads indicate HSCs. EMCN, endomucin; EC, endothelial cell. (B) Comparison of the distance between MKs to Ecs (n=119 control and 103 infected MKs) in the bone marrow of control mice or mice at 3 days after L. monocytogenes infection. (C) Comparison of the distance between CXCR4low or CXCR4high MKs and endothelial cells (Ecs) in the bone marrow of mice 3 days after L. monocytogenes infection (n=68 CXCR4low and 78 CXCR4high MKs). CD41 (blue), CXCR4 (red), and EMCN (green). Yellow arrows indicate CXCR4high MKs, while white arrowheads indicate CXCR4low MKs. (D) Representative immunofluorescent staining images (left) and quantification (right) of CXCR4 (red) labeled MKs (blue) egressed into sinusoids (green) upon infection (n=46 CXCR4low MKs and 69 CXCR4high MKs in 4 biological replicates). Yellow arrows indicate CXCR4high MKs. (E) Comparison of the distance between HSCs to MKs (n=96 control and 127 infected HSCs, p=0.21 by two-sample KS test) in the bone marrow of control mice or mice at 3 days after L. monocytogenes infection. (F) Visualization of MK migration (red, arrowhead) into sinusoids (green) by live imaging in the bone marrow of Pf4Cre+; Rosa26fs-tdTomato+/- mice 24 hr after L. monocytogenes infection (Movie S1). ‘S’ indicates sinusoid and dashed lines demarcate the border of sinusoids. (G) Quantification of CXCR4high MKs in bone marrow, peripheral blood, liver, spleen, and lung of control mice and mice 3 days after L. monocytogenes infection. (H) Quantification of CXCR4 levels on CXCR4low MKs treated with IFN-γ, LPS or L. monocytogenes for 4 hr compared to CXCR4high MKs. (I) Quantification of tdTomato+ CXCR4high MKs in the liver and spleen from control mice or mice 3 days after L. monocytogenes infection by flow cytometry. (J) Schema of mtdTomato+ bone marrow (from R26RmTmG mice) cell perfusion in control and L. monocytogenes infected recipients. (K) The percentage of CXCR4high mtdTomato+ MKs and CXCR4low mtdTomato+ MKs in bone marrow, liver, and spleen of control or infected recipients were analyzed 2 days after mtdTomato+ bone marrow cells were perfused. (L) Radar chart showing transcriptomic similarities of bone marrow MK subpopulations with reported BM and lung MK datasets (Pariser et al., 2021; Yeung et al., 2020). (M) Schema for transfer experiments using tdTomato+ MKs from Pf4Cre+; Rosa26fs-tdTomato+/- mice into control recipients or recipients 1 day following L. monocytogenes infection. (N–O) Representative images (N) and quantification by flow cytometry (O) of tdTomato+ MKs in the lung of control or infected recipients 2 days after cell perfusion (n=3 mice). Arrows indicate tdTomato+ MKs in the lung. Scale bars without indicated, 20 μm. Data represent mean ± s.e.m. A two-sample KS test was performed to assess statistical significance in (E). Repeated-measures one-way ANOVA followed by Dunnett’s test for multiple comparisons in (H), ǂǂ p<0.01, ǂǂǂ p<0.001. Two-tailed Student’s t-test was performed to assess statistical significance except (E, H), * p<0.05, ** p<0.01, *** p<0.001, n.s., not significant.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Bone marrow MKs (blue) and sinusoids (green) in control mice and mice 3 days after L. monocytogenes infection. CD41, blue; EMCN, green. Yellow arrows indicate MKs egressed into sinusoids. ‘S’ indicates sinusoid and dashed lines demarcate the border of sinusoids. (B) HSC and progenitor cell number in the bone marrow of control mice and mice 3 days after L. monocytogenes infection. LT, long term; ST, short term; MPP, multipotential progenitor. (C–D) MK numbers (C) and CXCR4low MK frequency (D) in the bone marrow of control mice and mice 3 days after L. monocytogenes infection (n=8 mice). (E–F) Frequency of BrdU+ (E) and Annexin V+ (F) cells in CXCR4high MKs from bone marrow of control mice or mice 3 days after L. monocytogenes infection (n=5 mice). Scale bars, 20µm. Data represent mean ± s.e.m. Two-tailed Student’s t-test was performed to assess statistical significance. * p<0.05, n.s., not significant.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Schematic depicting the strategy of scRNA-seq using bone marrow MKs from mice 3 days after L. monocytogenes infection. (B) Violin plots showing the number of unique genes (gene number) before and after removing doublets, number of total unique molecular identifiers (UMI counts) and percentage of mitochondrial transcripts in single cells after removing doublets. Scatter plot showing the correlation between UMI counts and gene numbers. corr indicates Pearson correlation coefficient. (C) UMAP of the combined 5368 cells from control bone marrow and 4276 cells from L. monocytogenes infection bone marrow, colored by cell types. Neu, neutrophil; MP, myeloid progenitor; Mon, monocytes; B, B cells; T, T cells. (D) UMAP of the combined 1712 control MKs and 1560 infection MKs in the bone marrow, colored by clusters. (E) Fraction of each MK subpopulation from control MKs or L. monocytogenes infection MKs. (F) Violin plot showing Cxcr4 expression in each MK subpopulation of control and infection MKs.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A–H) Relative expression of Cxcl12 (A–D) and frequency of CXCL12DsRed cells (E–H) in the bone marrow (A), lung (B), liver (C), and spleen (D) from control mice and mice 3 days after L. monocytogenes infection by RT-qPCR (A–D) and flow cytometry (E–H), respectively. Two-tailed Student’s t-test was performed to assess statistical significance. * p<0.05, ** p<0.01, *** p<0.001.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** (A–B) Fraction of BrdU+ and Annexin V+ MKs in CXCR4high MKs in the liver (A) and spleen (B) from control mice or mice 3 days after L. monocytogenes infection. (C) Quantification of CXCR4low MKs in peripheral blood, liver, spleen, and lung of control mice and mice at 3 days after L. monocytogenes infection. (D) Quantification of CXCR4 levels on CXCR4high MKs and CXCR4low MKs treated with LPS or IFN-γ for 18 or 24 hr. (E–F) Representative images and quantification of mGFP+ MKs (green) in the liver (E) and spleen (F) from control mice or mice 3 days after L. monocytogenes infection (n=4 and 7 mice, respectively). (G–H) Gating strategies for CXCR4high MKs in the liver (G) and spleen (H). (I) Quantification of tdTomato+CXCR4low MKs in the liver and spleen from control mice or mice 3 days after L. monocytogenes infection by flow cytometry. Scale bars, 20μm. Data represent mean ± s.e.m. Two-tailed Student’s t-test was performed to assess statistical significance except (D). * p<0.05, ** p<0.01, *** p<0.001, n.s., not significant. Repeated-measures one-way ANOVA followed by Dunnett’s test for multiple comparisons in (D), ǂǂ p<0.01, ǂǂǂ p<0.01.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** (A) Gene set variation analysis (GSVA) of each MK subpopulation under control or L. monocytogenes infection, colored by row-scaled GSVA enrichment scores. (B) Antigen processing and presentation score of control MK5, infection MK5, and bone marrow and lung MKs from Yeung et al., 2020. (C) Heatmap showing the row-scaled antigen processing and presentation gene expression of control and infection MK5 cells, comparing with bone marrow MK and lung MK from Yeung et al., 2020. Data represent mean ±first and third quartiles in (B). Two-sample KS test was performed to assess statistical significance in (B).

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig4-figsupp6-v2.jpg)

**Figure 4—figure supplement 6.:** (A) Schema for transfer experiments using tdTomato+ MKs from Pf4Cre+; Rosa26fs-tdTomato+/- mice into recipients 1 day following L. monocytogenes infection. (B) Transfused MKs (red) and sinusoids (green) in the lung of mice after L. monocytogenes infection as indicated in Figure 4M. DAPI, blue; EMCN, green; tdTomato, red. (C) Quantification of transfused intravascular and extravascular MKs in the lung. Scale bar, 20μm. Data represent mean ± s.e.m. Two-tailed Student’s t-test was performed to assess statistical significance. *** p<0.001.

To further explore the dynamic migration of MKs upon pathogen infection, we adapted an ex vivo real-time imaging method to trace MK migration in the bone marrow (Xie et al., 2009). Using Pf4Cre; Rosa26fs-tdTomato mice and ex vivo live imaging approach, we observed that small tdTomato+ MKs rapidly migrated into sinusoids without rupture or platelet release upon infection (Figure 4F, Figure 4—video 1). In contrast, MKs with large sizes showed much slower migration (Figure 4—video 1). Additionally, CXCR4high MKs were decreased in the bone marrow 3 days after L. monocytogenes infection but with a similar proliferation and apoptosis rate compared to CXCR4low MKs (Figure 4G; Figure 4—figure supplement 1C-F), indicating CXCR4high MKs might migrate out of bone marrow. Consistent with this, the frequency of MK5, which enriched CXCR4high MKs, decreased in bone marrow after L. monocytogenes infection in our single-cell atlas (Figure 4—figure supplement 2). Furthermore, we found that L. monocytogenes infection decreased the expression of CXCL12, the ligand of CXCR4 (Sugiyama et al., 2006), in bone marrow but increased CXCL12 expression in the lung, liver, and spleen (Figure 4—figure supplement 3), suggesting that the distinguished CXCL12 levels between tissues might drive the migration of CXCR4high MKs between tissues. In line with this, CXCR4high MKs were increased in the peripheral blood and organs, including the liver, spleen, and lung 3 days after L. monocytogenes infection without an alternation of cell cycle and apoptosis, whereas CXCR4low MKs did not differ except for a slight increase in the liver (Figure 4G; Figure 4—figure supplement 4A-C). Moreover, inflammatory stresses, such as IFNγ and Lipopolysaccharides (LPS), or L. monocytogenes treatment did not increase CXCR4 expression in CXCR4low MKs (Figure 4H; Figure 4—figure supplement 4D).

To further explore how MKs migrate between organs during bacterial infection in vivo, we employed Pf4Cre; Rosa26fs-tdTomato, and Pf4Cre; cell membrane-localized tdTomato cell membrane-localized EGFP (Rosa26fs-mTmG) mice in which Tomato or cell membrane-localized EGFP (mGFP) were exclusively expressed in MK lineage (Tiedt et al., 2007). mGFP expressing MKs or Tomato expressing CXCR4high MKs were increased in the liver and spleen 3 days after L. monocytogenes infection (Figure 4I; Figure 4—figure supplement 4E-H), whereas Tomato expressing CXCR4low MKs did not change (Figure 4—figure supplement 4I). To further confirm the tissue infiltration of MKs upon infection, we intravenously injected membrane-localized tdTomato (mTomato) expressing bone marrow cells from Rosa26Rfs-mTmG mice into control recipients or recipients infected with L. monocytogenes 1 day before mTomato+ cell perfusion (Figure 4J). We found that 2 days after mTomato+ cell perfusion, engrafted mTomato+ CXCR4high MKs more efficiently infiltrated into the liver (92.1%) and spleen (92.5%); by contrast, most mTomato+ CXCR4low MKs (66.7%) migrated to the bone marrow (Figure 4K).

As the lung is an important site for platelet generation (Lefrançais et al., 2017), we aligned our MK sc-RNAseq data with lung MKs (Pariser et al., 2021; Yeung et al., 2020), and found that MK5, MK4, and MK3 showed similar gene profiles with lung MKs (Figure 4L). Moreover, MK5 enriched more inflammatory pathway genes, antigen processing, and presentation pathway after L. monocytogenes infection, which enabled MK5 to achieve a more similar transcriptional profile as the lung MKs than normal MK5 (Figure 4—figure supplement 5). Interestingly, we found that engrafted Tomato+ MKs (from Pf4Cre; Rosa26fs-tdTomato mice) more efficiently infiltrated the lungs in the infected recipients as extravascular MKs than in the control recipients (Figure 4M–O and Figure 4—figure supplement 6).

### Acute inflammation-induced emergency megakaryopoiesis generates CXCR4high MKs upon infection

Infection-induced emergency megakaryopoiesis compensates the platelet consumption (Verschoor et al., 2011). Consistently, we observed that MKs were ruptured in the bone marrow 3 days after L. monocytogenes infection to recover the reduced platelets post-L. monocytogenes infection (Couldwell and Machlus, 2019; Nishimura et al., 2015; Figure 5A–C). However, CXCR4high MKs were increased at 18 hr after L. monocytogenes infection and substantially declined at 72 hr in bone marrow, whereas CXCR4low MKs remained unchanged upon infection (Figure 5D). As MK-committed HSCs drive infection-induced emergency megakaryopoiesis (Haas et al., 2015), we asked whether emergency megakaryopoiesis also generates CXCR4high MKs to participate in the host-defense response. To this aim, we employed SclCreER; Rosa26fs-tdTomato mice (Göthert et al., 2005) to monitor the HSPC derived emergency megakaryopoiesis upon bacterial infection. Eighteen hours after tamoxifen recombining Tomato in HSPCs and L. monocytogenes infection (Figure 5E), we observed that Tomato+ HSPCs derived Tomato+ CXCR4high MKs rapidly increased in the bone marrow, similar to the platelet-generating MKs (tdTomato+ CXCR4low MKs) (Figure 5F), without a noticeable rise of hematopoietic progenitors (Figure 5G). Overall, our observations indicated that CXCR4high MKs might be generated by emergency megakaryopoiesis to stimulate pathogen defense.

![Figure 5.](https://cdn.elifesciences.org/articles/78662/elife-78662-fig5-v2.jpg)

**Figure 5.:** (A–B) Representative images (A) and statistical analysis (B) of CD41 (green) and DAPI (blue) in bone marrow from control mice or mice 3 days after L. monocytogenes infection. Arrows indicate ruptured MKs, yellow boxes indicate the locations of the magnified images. (C) Platelets in peripheral blood in control mice or mice after L. monocytogenes infection on indicated days. (D) The dynamics percentage of CXCR4high MKs (left) or CXCR4low MKs (right) in the bone marrow of L. monocytogenes-challenged mice within 72 hr of infection. (E) Schema for HSC lineage tracing upon L. monocytogenes infection using SclCreER+; Rosa26fs-tdTomato+/- mice. (F–G) Cell numbers of tdTomato+ CXCR4low MKs and tdTomato+ CXCR4high MKs (F), and tdTomato+ progenitors (G) in the bone marrow of control and L. monocytogenes infected SclCreER+; Rosa26fs-tdTomato+/- recipients 18 hr after L. monocytogenes infection and tamoxifen administration. CMP, common myeloid progenitor; GMP, granulocyte-monocyte progenitor; MEP, megakaryocyte-erythroid progenitor. Scale bars, 20 μm. Data represent mean ± s.e.m. Two-tailed Student’s t-test was performed to assess statistical significance, * p<0.05, ** p<0.01, n.s., not significant.

## Discussion

MKs participate in megakaryocyte maturation, platelet activation, and potentially influence neutrophils and the adaptive immune cells (Cunin and Nigrovic, 2019). Accordingly, MKs prevent the spread of dengue virus infection by enhancing the type 1 interferons pathway in murine and clinical biospecimens (Campbell et al., 2019) and contribute to cytokine storms in severe COVID-19 patients (Bernardes et al., 2020; Ren et al., 2021; Stephenson et al., 2021). MKs were reported to express multiple inflammation receptors, such as Fcγ receptors (Markovic et al., 1995), Toll-like receptors (Beaulieu et al., 2011; Ward et al., 2005), interleukin receptors (Navarro et al., 1991; Yang et al., 2000), and IFN receptors (Negrotto et al., 2011), which might enable MKs to receive inflammation signals and express cytokines. Recent scRNA-seq studies suggested the existence of MK subpopulations for inflammation responses (Liu et al., 2021; Pariser et al., 2021; Sun et al., 2021; Wang et al., 2021a). Here, we identified that MK5 has both MK and immune cell characteristics for platelet generation and immune responses. More importantly, we demonstrated that CXCR4high MKs recruited and stimulated innate myeloid cells by producing TNFα and IL-6, for bacterial phagocytosis. Furthermore, CXCR4high MKs had the ability for antigen processing and antigen presentation capacity, which suggested that CXCR4high MKs might contribute to the regulation of adaptive immune function. This is consistent with a previous observation that lung MKs are able to process and present antigens (Pariser et al., 2021). Our data suggested that CXCR4high MKs might contribute to the regulation of adaptive immune function. However, as the distinction between CXCR4high MKs and CXCR4low MKs is not entirely objective, additional markers are warranted to further enrich CXCR4high MKs.

We observed that MK ablation increased HSPCS and myeloid granulocyte/macrophage progenitor (GMP) in bone marrow under bacterial infection, which is consistent with 5-FU stress (Hérault et al., 2017). However, increased GMP only increased myeloid cells in the bone marrow but not in other organs, which further supported the role of CXCR4high MKs in promoting the migration of myeloid cells. Normal HSC to MK development takes 11–12 days in humans and 4 days in mice; However, emergency megakaryopoiesis takes less than a day to generate MKs upon inflammation stress (Couldwell and Machlus, 2019; Liu et al., 2021; Sun et al., 2021; Figure 5D). Previously, researchers believed that emergency megakaryopoiesis mainly contributes to the replenishment of damaged platelets upon acute inflammation (Haas et al., 2015). We found that inflammation signals could not upregulate CXCR4 in CXCR4low MKs in vitro, although we cannot entirely exclude the plasticity of MKs in vivo. Our data showed that CXCR4high MKs might be generated from the emergency megakaryopoiesis, instead of CXCR4low MKs, to facilitate host-defense responses against bacterial infection.

A recent report showed that the lung is a reservoir of MKs for platelet production (Lefrançais et al., 2017). Other works also indicate that lung MKs share a similar transcriptional profile with lung DCs and participate in pathogen infection (Boilard and Machlus, 2021; Pariser et al., 2021). However, the correspondence between MKs in the lung and bone marrow remains unexplored. Neonatal lung MKs lack the immune molecules in adult lung MKs (Pariser et al., 2021), which indicates that lung MKs might have distinct developmental origins. Similarly, MKs are observed to egress and migrate to the pulmonary capillary under stresses (Davis et al., 1997). Our works suggested lung MKs might migrate from bone marrow upon infection challenges, although more detailed investigations are warranted in future studies.

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
      <td>Antibody</td>
      <td>Anti-CD41a (mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>Cat#17-0411-82RRID:AB_1603237</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CXCR4 (mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>Cat#53-9991-80 RRID:AB_953573</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD11b (mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>Cat#12-0112-82 RRID:AB_2734869</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-F4/80 (mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>Cat#17-4801-80 RRID:AB_2784647</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Gr-1 (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#108424 RRID:AB_2137485</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Ly-6C (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#128022 RRID:AB_10639728</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD11c (mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>Cat#12-0114-82 RRID:AB_465552</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD45.1 (mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>Cat#15-0453-82 RRID:AB_468759</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD45.2 (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#109831 RRID:AB_10900256</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD4 (mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>Cat#12-0041-82 RRID:AB_465506</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD8a (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#100707 RRID:AB_312746</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IFN-γ (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#505813 RRID:AB_493312</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IL-4 (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#504118 RRID:AB_10898116</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD34 (mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>Cat#11-0341-82 RRID:AB_465021</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Sca-1 (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#108114 RRID:AB_493596</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-c-Kit (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#105812 RRID:AB_313221</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD135 (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#135314 RRID:AB_2562339</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD3ε (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#100310 RRID:AB_312675</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-B220 (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#103210 RRID:AB_312995</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-TER-119 (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#116210 RRID:AB_313711</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IgM (mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>Cat#15-5790-82 RRID:AB_494222</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD16/32 (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#101333 RRID:AB_2563692</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD127 (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#135021 RRID:AB_1937274</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-TNFα (mouse monoclonal)</td>
      <td>Invitrogen</td>
      <td>Cat#17-7321-81 RRID:AB_469507</td>
      <td>FACS (1 μl per test)IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IL-6 (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#504507 RRID:AB_10694868</td>
      <td>FACS (1 μl per test)IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-BrdU (mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>Cat#11-5071-42 RRID:AB_11042627</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Endomucin (mouse polyclonal)</td>
      <td>R&amp;D</td>
      <td>Cat#AF4666</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD150 (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#115908 RRID:AB_345278</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Lineage Panel (mouse monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#133307 RRID:AB_11124348</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Goat AF488 (goat polyclonal)</td>
      <td>Invitrogen</td>
      <td>Cat#A32814 RRID:AB_2762838</td>
      <td>IF (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-TNF-alpha (mouse monoclonal)</td>
      <td>Sino Biological</td>
      <td>Cat#50349-R023</td>
      <td>2 μg ml–1</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Rabbit AF488 (rabbit polyclonal)</td>
      <td>Invitrogen</td>
      <td>Cat#R37118 RRID:AB_2556546</td>
      <td>IF (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-OVA257-264 (SIINFEKL) peptide bound to H-2Kb (mouse monoclonal)</td>
      <td>Invitrogen</td>
      <td>Cat#17-5743-82 RRID:AB_1311286</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-IL-2 (mouse monoclonal)</td>
      <td>eBioscience</td>
      <td>Cat#25-7021-80 RRID:AB_1235007</td>
      <td>FACS (1 μl per test)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Diphtheria toxin (DT)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#D0564-1MG</td>
      <td>40 μg kg–1 body mass</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>BrdU (5-Bromo-2´-Deoxyuridine)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#B5002-250mg</td>
      <td>125 mg kg–1 body mass</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CFSE (5-Carboxyfluorescein, Succinimidyl Ester)</td>
      <td>Invitrogen</td>
      <td>Cat#C2210</td>
      <td>2.5 μM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>GM-CSF</td>
      <td>Abbkine</td>
      <td>Cat#PRP2116</td>
      <td>10 ng ml–1</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>IL-4</td>
      <td>novoprotein</td>
      <td>Cat#CK15</td>
      <td>10 ng ml–1</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tamoxifen</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#T5648</td>
      <td>20 mg ml–1 corn oil</td>
    </tr>
    <tr>
      <td>Commercial kit</td>
      <td>Chromium Single Cell 3′ GEM, Library &amp; Gel Bead Kit v3</td>
      <td>10 x Genomics</td>
      <td>PN-1000075</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial kit</td>
      <td>Chromium Chip B Single Cell Kit</td>
      <td>10 x Genomics</td>
      <td>PN-1000074</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>NCTC clone 929</td>
      <td>ATCC</td>
      <td>CCL-1RRID:CVCL_0462</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>B3Z hybridoma CD8 T cell</td>
      <td>Dr. Nilabh Shastri</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>scRNA sequencing data (raw and processed data)</td>
      <td>This paper</td>
      <td>GEO: GSE168224</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>C57BL/6 J</td>
      <td>Shanghai Model Organisms</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Tg(Pf4-icre)Q3Rsko/J (Pf4Cre)</td>
      <td>Jackson Laboratory</td>
      <td>Stock No: 008535</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Gt(ROSA) 26Sortm1(HBEGF) Awai/J (Rosa26fs-iDTR)</td>
      <td>Jackson Laboratory</td>
      <td>Stock No: 007900</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Gt(ROSA)26Sortm4(ACTB-tdTomato,-EGFP)Luo/J (Rosa26fs-mTmG)</td>
      <td>Jackson Laboratory</td>
      <td>Stock No: 007576</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Gt(ROSA)26Sortm9(CAG-tdTomato)Hze/J (Rosa26fs-tdTomato)</td>
      <td>Jackson Laboratory</td>
      <td>Stock No: 007905</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>SclCreER mice</td>
      <td>Göthert et al., 2005</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Cxcl12tm2.1Sjm/J (Cxcl12fs-DsRed)</td>
      <td>Jackson Laboratory</td>
      <td>Stock No: 022458</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>C57BL/6-Tg(TcraTcrb)1,100Mjb/J (OT-I)</td>
      <td>Jackson Laboratory</td>
      <td>Stock No: 003831</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (L. monocytogenes)</td>
      <td>10403 S</td>
      <td>Bishop and Hinrichs, 1987</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cell ranger_3.0.2</td>
      <td>10 x Genomics</td>
      <td>tenxRRID:SCR_01695</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R_3.6.3</td>
      <td>https://cran.r-project.org/</td>
      <td>R 3.6.3</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Seurat_3.0.2</td>
      <td>Butler et al., 2018</td>
      <td>SeuratRRID:SCR_016341</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ggplot2_3.2.0</td>
      <td>https://cran.r-project.org/web/packages/ggplot2/index.html</td>
      <td>ggplot2 RRID:SCR_014601</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>clusterProfiler_3.12.0</td>
      <td>Yu et al., 2012</td>
      <td>clusterProfiler RRID:SCR_016884</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pheatmap_1.0.12</td>
      <td>https://cran.r-project.org/web/packages/pheatmap/</td>
      <td>pheatmap RRID:SCR_016418</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CellPhoneDB_2.1.7</td>
      <td>Efremova et al., 2020</td>
      <td>CellPhoneDB RRID:SCR_017054</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CellChat_1.1.3</td>
      <td>Jin et al., 2021</td>
      <td>CellChat 1.1.3</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>symphony_1.0</td>
      <td>Kang et al., 2021</td>
      <td>symphony 1.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MetaNeighbor_1.10.0</td>
      <td>Crow et al., 2018</td>
      <td>MetaNeighbor RRID:SCR_016727</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>iMAP_1.0.0</td>
      <td>Wang et al., 2021b</td>
      <td>iMAP 1.0.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>scmap_ 1.16.0</td>
      <td>Kiselev et al., 2018</td>
      <td>Scmap RRID:SCR_017338</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>enrichplot_1.4.0</td>
      <td>Yu, 2019</td>
      <td>enrichplot 1.4.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Imaris_8.4</td>
      <td>Bitplane</td>
      <td>Imaris RRID:SCR_007370</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FlowJo_10</td>
      <td>BD Bioscience</td>
      <td>FlowJo RRID:SCR_008520</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ_ 1.8.0</td>
      <td>National Institutes of Health</td>
      <td>ImageJ RRID:SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DAPI (4',6-Diamidino-2-Phenylindole, Dihydrochloride)</td>
      <td>Thermo Fisher</td>
      <td>Cat#D1306</td>
      <td>IF (0.5 µg/mL)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Corn oil</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#PHR2897</td>
      <td>Tamoxifen dissolution</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Lymphocyte Separation Medium</td>
      <td>TBD Science</td>
      <td>Cat#LTS1077</td>
      <td>Liver cell isolation</td>
    </tr>
  </tbody>
</table>

### Mice

C57BL/6-Tg(Pf4-cre)Q3Rsko/J (Pf4Cre), C57BL/6-Gt(ROSA) 26Sortm1(HBEGF) Awai/J (Rosa26fs-iDTR), C57BL/6-Gt(ROSA)26Sortm4(ACTB-tdTomato,-EGFP)Luo/J (Rosa26fs-mTmG), Gt(ROSA)26Sortm9(CAG-tdTomato)Hze (Rosa26fs-tdTomato), CXCL12tm2.1Sjm/J (Cxcl12DsRed) and C57BL/6-Tg(TcraTcrb)1,100Mjb/J (OT-I) mice were obtained from the Jackson Laboratory. SclCreER mice were provided by J. R. Göthert. All mice were maintained in the C57BL/6 background. Animals were blindly included in the experiments according to genotyping results as a mix of male and female. All animal experiments were performed according to protocols approved by the Sun Yat-sen University animal care and use committee (approval No. SYSU-IACUC-2021-B0617).

### Cell line

B3Z hybridoma T cells were kindly gifted by Dr. Nilabh Shastri (Johns Hopkins University). This cell line was verified to be mycoplasma free by EZdetect PCR Kit for Mycoplasma Detection (HiMedia).

### Bacteria and infections

Listeria (L.) monocytogenes infection was performed as described with minor modifications (Edelson and Unanue, 2000; Verschoor et al., 2011). In brief, wild-type L. monocytogenes strain 10,403 S grown to exponential phase at 37 °C in TSB media was injected intravenously at a dose of 2500 colony-forming units (CFUs) to determine spleen and liver bacterial burdens 3 days after infection. Recombinant L. monocytogenes expressing the chicken ovalbumin peptide (OVA257-264) (L.m. – OVA257-264) was injected intravenously at a dose of 2500 CFUs to determine activated spleen T cells 7 days after infection. Escherichia (E.) coli wild-type strain 85,344 expressing GFP was constructed as previously described (Feng et al., 2020). GFP-labeled E. coli was grown to exponential phase at 37 °C in LB media and washed with PBS before being suspended for phagocytosis assays.

### Antibodies for flow cytometry analysis and cell sorting

For cell sorting and analysis, monoclonal antibodies to CD41 (MWReg30, eBioscience), CXCR4 (2B11, eBioscience), CD11b (M1/70, eBioscience), F4/80 (BM8, eBioscience), Gr-1 (RB6-8C5, Biolegend), Ly6C (HK1.4, Biolegend), CD11c (N418, eBioscience), CD45.1 (A20, eBioscience), CD45.2 (104, Biolegend), CD4 (GK1.5, eBioscience), CD8 (53–6.7, Biolegend), INF-γ (XMG1.2, Biolegend), IL4 (11B11, Biolegend), CD34 (RAM34, eBioscience), Sca-1 (D7, Biolegend), c-kit (2B8, Biolegend), CD135 (A2F10, Biolegend), CD3ε (145–2 C11, Biolegend), CD45R (RA3-6B2, Biolegend), TER-119 (Ter-119, Biolegend), IgM (II/41, eBioscience), FγRII (93, Biolegend), IL-7R (A7R34, Biolegend), TNFα (MP6-XT22, Invitrogen), IL-6 (MP5-20F3, Biolegend), OVA257-264 (SIINFEKL) peptide bound to H-2Kb (eBio25-D1.16 (25-D1.16), Invitrogen) and IL-2 (JES6-5H4, eBioscience) were used where indicated.

### Flow cytometry and cell sorting

Bone marrow cells were isolated from mouse femora and tibiae as previously reported (Jiang et al., 2018). Splenocytes were mechanically dissociated in PBS with 2% FBS. Peripheral blood was collected from the retro‐orbital sinus and anticoagulated by K2-EDTA. Those three kinds of cells then underwent red blood cell lysis for 5 min using 0.16 M ammonium chloride solution. Liver cells were mechanically dissociated and lysed using 0.16 M ammonium chloride solution, followed by gradient sedimentation using a density reagent (LTS1077, TBD Science) following the manufacturer’s instruction. Cell sorting was performed using a cell sorter (MoFlo Astrios, Beckman Coulter) with a 100 μm nozzle at a speed of around 5000 cells s–1. For intracellular cytokine staining, cells were pretreated with Brefeldin-A (BFA, 10 μg ml–1) for 4 hr at 37℃ before staining. For MK antigen presentation detection, MKs were co-culture with 100 μg ml–1 soluble full-length OVA for 24 hr before staining. For IFNγ, LPS and L. monocytogenes treatment, cells were co-culture with 10 ng ml–1 IFN-γ or 30 μg ml–1 LPS for 4, 18, or 24 hr, or 106 L. monocytogenes for 4 hr in a 37℃ incubator before staining. Cell analysis was performed on either one of the flow cytometers (Attune NxT, Thermo Fisher; Cytek AURORA, Aurora).

### Single-cell library construction and sequencing

Sorted CD41+ FSChigh single cells from four mice of a control MK group and an MK group from mice 3 days upon L. monocytogenes infection each were processed through the Chromium Single Cell Platform using the Chromium Single Cell 3’ Library and Gel Bead Kit v3 (PN-1000075, 10 x Genomics) and the Chromium Single Cell B Chip Kit (PN-1000074, 10 x Genomics) as the manufacturer’s protocol. In brief, over 7000 cells were loaded onto the Chromium instrument to generate single-cell barcoded droplets. Cells were lysed and barcoded reverse transcription of RNA occurred. The library was prepared by following amplification, fragmentation, adaptor, and index attachment then sequenced on an Illumina NovaSeq platform.

### scRNA-seq processing

The scRNA-seq reads were aligned to the mm10 reference genomes, and unique molecular identifier (UMI) counts were obtained by Cell Ranger 3.0.2. Normalization, dimensionality reduction, and clustering were performed with the Seurat 3.0 R package (Butler et al., 2018). For the control and Listeria (L.) monocytogenes infection group, we loaded one 10 x Genomics well each and detected 5663 and 5948 cells that passed the Cell Ranger pipeline, respectively. To ruled out low quality cells, cells with >12% mitochondrial content or <200 detected genes were excluded with Seurat function subset (percent.mt <12 & nFeature_RNA >200). We ruled out doublets with default parameters of DoubletDecon R package, and 54 control cells and 939 L. monocytogenes infected cells were excluded. Following the standard procedure in Seurat’s pipeline, we identified 3272 MKs from control mice (1712 MKs) and mice with L. monocytogenes infection (1560 MKs) (3897 and 3449 immune cells were discarded, respectively) in combination with MetaNeighbor method. Preprocessed dataset normalization was performed by dividing the UMI counts per gene by the total UMI counts in the corresponding cell and log-transforming before scaling and centering. SCT normalization was performed with the script: object <- SCTransform(object, vars.to.regress = “"percent.mt”", verbose = FALSE). Signature genes of each cluster were obtained using the Seurat function FindMarkers with Wilcox test with fold change >1.5 and p value <0.05 after clustering. Heatmaps, individual UMAP plots, and violin plots were generated by the Seurat functions in conjunction with ggplot2 and pheatmap R packages.

Similarities and UMAP projection between our scRNA-seq data and published datasets GSE152574 (Yeung et al., 2020), GSE158358 (Pariser et al., 2021), GSE137540 (Xie et al., 2020), GSE128074 (Hamey et al., 2021), or GSE132042 (Almanzar et al., 2020) were conducted by MetaNeighbor R package (Crow et al., 2018), iMAP.py and Symphony R package (Kang et al., 2021). iMAP integration was performed using the default parameters except n_top_genes = 2000, min_genes = 0, min_cells = 0, and n_epochs = 100 before doing dimensionality reduction using Uniform Manifold Approximation and Projection method (UMAP, n_neighbors = 30, n_pca = 30). Radar charts were generated with JavaScript written by Nadieh Bremer (https://www.visualcinnamon.com/). Euclidean distances denote the distances between the centroid of each cluster.

Correlations were calculated based on normalized RNA values, with the function cor and the parameter ‘method = “spearman”’. Multiple testing correction using the function cor.test with the parameter “method = “spearman” and it was applied for Cxcr4 expression correlations. We calculated the similarities between MK1 to 5 with the published MK, immune cell, and myeloid progenitor datasets (Almanzar et al., 2020; Hamey et al., 2021; Pariser et al., 2021; Xie et al., 2020; Yeung et al., 2020) using scmap R package (Kiselev et al., 2018). Default parameters and 1000 features were used and threshold >0 was set. Cell-type matches are selected based on the highest value of similarities and the second-highest value which is not 0.01 less than the highest value across all reference cell types.

Cytokine, inflammatory, chemokine, and antigen processing and presentation scores were evaluated with the AddModuleScore function of Seurat using genes from KEGG pathway ko04060, cytokine-cytokine receptor interaction; GO:0006954, inflammatory response; chemokine ligands from CellPhoneDB.mouse (Jin et al., 2021) and GO:0019882, antigen processing and presentation.

Interaction analysis of MKs and immune cells were conducted by CellPhoneDB (Efremova et al., 2020) (transformed to human orthologous genes Davidson et al., 2020) and CellChat R package (Jin et al., 2021). Only interactions involving cytokines were shown. Gene Ontology (GO) analysis was performed using clusterProfiler R package (Yu et al., 2012) and visualized using enrichplot R package (Yu, 2019).

Gene set enrichment analysis (GSEA) was performed using gsea R package (Subramanian et al., 2005) and visualized using enrichplot R package. Gene lists were pre-ranked by the fold change values of the differential expression analysis using Seurat function FindMarkers. Gene sets for GSEA were obtained from GO database (GO:0002367, cytokine production involved in immune response; GO:0006954, inflammatory response; GO:0008009, chemokine activity; GO:0022409, positive regulation of cell-cell adhesion; GO:0002275, myeloid cell activation involved in immune response).

Gene set variation analysis (GSVA) was performed using GSVA R package (Hänzelmann et al., 2013). GSVA was performed to calculate GSVA score of indicated pathway genes in single cell datasets with the whole protein encoding genes after log normalization of expression values. Gene sets for GSVA were obtained from GO database (GO:0022409, positive regulation of cell-cell adhesion; GO:0002275, myeloid cell activation involved in immune response; GO:0002367, cytokine production involved in immune response; GO:0007596, blood coagulation; GO:0019882, antigen processing and presentation; GO:0034340: response to type I interferon; GO:0034341: response to interferon-gamma; GO:0045088, regulation of innate immune response; GO:0042742, defense response to bacterium; GO:0002819, regulation of adaptive immune response; GO:1903708, positive regulation of hemopoiesis).

### Lung cells preparation for flow cytometry

Lungs were removed and digested as described with minor modifications (Lefrançais et al., 2017). In brief, removed lungs were placed in 1.5 ml tubes, minced with scissors, and digested with 1 ml digestion buffer (HBSS with 1 mg ml–1 collagenase D, 0.1 mg ml–1 DNase I, 25 mM HEPES, 2 mM L-glutamine, and 2% FBS) for 30 min at 37℃ before filtration through a 100 μm cell strainer and red blood cell lysis for 5 min. Samples were then filtered through 70 μm strainers and resuspended for subsequent surface marker staining for flow cytometry.

### Megakaryocyte ablation induction

Pf4Cre mice were mated with the Rosa26fs-iDTR line to generate Pf4Cre; Rosa26fs-iDTR mice. Diphtheria toxin (DT, Sigma-Aldrich) was injected intraperitoneally every day at a dose of 40 ng g–1 bodyweight into Pf4Cre+; Rosa26fs-iDTR+/– mice and their cre negative counterparts to induce megakaryocyte ablation as indicated.

### Cre-ER recombinase induction

SclCreER mice were mated with the Rosa26fs-tdTomato line to generate SclCreER; Rosa26fs-tdTomato mice. For induction of cre-ER recombinase, SclCreER, Rosa26fs-tdTomato+/– mice were injected with tamoxifen intraperitoneally once (2 mg in 0.1 ml corn oil; Sigma-Aldrich).

### BrdU incorporation assay

5-Bromo-2-deoxyuridine (BrdU) was administered at a single dose of 125 mg kg–1 body mass by intraperitoneal injection. Whole bone marrow cells were collected 12 hr later and incubated with anti-CD41 and anti-CXCR4 for 1 hr. Cells were washed and then fixed with 4% PFA at 4 °C overnight. Cells were then permeabilized with 0.5% TritonX-100 for 15 min at room temperature and incubated with 1 mg ml–1 DNase I (Roche) for 1 hr at 37 °C followed by incubating with anti-BrdU (BU20A, eBioscience) for 1 hr at room temperature before being analyzed.

### Annexin V binding assay

For Annexin V binding assay, bone marrow cells were incubated with cell surface markers for 1 hr at 4 °C and then washed with PBS before being resuspended with Annexin V binding buffer (Biolegend). Cells were then incubated with FITC Annexin V (Biolegend) for 15 min at room temperature in dark, and then 300 μl Annexin V binding buffer was added to each tube. Cells were analyzed by a flow cytometer.

### Immunostaining

Immunostaining of frozen sections was performed as described (Jiang et al., 2018). For bone sections, mice were perfused with PBS and 4% paraformaldehyde (PFA). Then the bones were fixed with 4% PFA for 24 hr, decalcified with 0.5 M EDTA for 2 days, and gradient dehydrated by 15% and 30% sucrose for another 2 days. The thick of sections was 30 μm. We used CD41 (MWReg30; eBioscience; 1:200), Endomucin (R&D; 1:100), CD150 (TC15-12F12.2; Biolegend; 1:100), CD48 (HM48-1; Biolegend; 1:100), CXCR4 (2B11, eBioscience; 1:100) antibodies, and lineage panel (Biolegend; cat #133307; 1:50). Secondary staining was done with donkey anti–goat AlexaFluor 488 (Invitrogen; 1:1000). For the liver and spleen from Pf4Cre+; Rosa26fs-mTmG+/– mice, and lung from Pf4-cre+; Rosa26fs-tdTomato+/– mice, we used DAPI (Thermo Fisher; 0.5 μg ml–1) to stain the frozen sections. For phagocytosis analysis, F4/80 (BM8, eBioscience; 1:100), CD11b (M1/70; Invitrogen; 1:100), CD41 (MWReg30; Thermo Fisher; 1:200) and DAPI was used. For sorted MKs, we used CXCR4 (2B11, eBioscience; 1:100), TNFα (R023, Sino Biological; 1:100) and IL-6 (MP5-20F3, Biolegend; 1:100) antibody. Secondary staining was performed with donkey anti-rabbit AlexaFluor 488 (Invitrogen; 1:1000). Confocal images were obtained using a spinning-disk confocal microscope (Dragonfly, Andor) and analyzed using Imaris 9.0 software (Oxford Instruments). Three-Dimension plots were generated using Matplotlib (Hunter, 2007).

### Quantitative real-time (qRT-) PCR

For RT-qPCR, MKs were dissociated in Trizol (Magen), and RNA was extracted following the manufacture’s instruction. RNA was reverse transcribed into cDNA using the TransCript All-in-One First-Strand cDNA Synthesis kit (Transgene). Quantitative PCR was performed using a Bio-Rad CFX 96 touch. The primers for Pf4 were 5’-GGGATCCATCTTAAGCACATCAC-3’ (forward) and 5’-CCATTCTTCAGGGTGGCTATG-3’ (reverse). The primers for Vwf were 5’-CTTCTGTACGCCTCAGCTATG-3’ (forward) and 5’-GCCGTTGTAATTCCCACACAAG-3’ (reverse). The primers for Mpl were 5’-AACCCGGTATGTGTGCCAG-3’ (forward) and 5’-AGTTCATGCCTCAGGAAGTCA-3’ (reverse). The primers for Cxcl12 were 5’-AGGTTCTTATTTCACGGCTTGT-3’ (forward) and 5’-TGGGTGCTGAGACCTTTGAT-3’ (reverse). The primers for Gapdh were 5’-AGGTCGGTGTGAACGGATTTG-3’ (forward) and 5’-GGGGTCGTTGATGGCAACA-3’ (reverse). Gapdh was used as the reference gene for qRT-PCR analysis.

### Transwell migration

Transmigration assays were performed on a transwell with a pore size of 5 μm (Biofil). CXCR4low MKs or CXCR4high MKs from bone marrow were sorted (5000 cells per well) from control mice and added to the lower chamber with 600 μl IMDM (Thermo Fisher) plus 10% FBS (Gibco). Peripheral blood cells were collected as described in the ‘Flow cytometry and cell sorting’ section. 6×105 peripheral blood cells were resuspended in 100 μl RPMI 1640 (Gibco) plus 10% FBS and added to the upper insert to continue for 2-hr incubation at 37 °C, 5% CO2. Cells in the lower chamber were harvested, washed with PBS once, and resuspended with 100 μl PBS for staining and FACS counting.

### Phagocytosis

Bone-marrow-derived macrophages (BMDM) from C57BL/6 mice at 6–8 weeks of age were differentiated from bone marrow precursors with minor modifications (Minutti et al., 2019). In brief, bone marrow cells were isolated and propagated for 7 days in DMEM without sodium pyruvate or HEPES (Gibco), containing 20% FBS (Gibco), 30% supernatants of L929 conditioned media, and 1% Pen/Strep (Hyclone) at 37 °C. Macrophage phagocytosis assays were performed on a transwell plate with a pore size of 3 μm (Biofil) as described with modifications (Sharif et al., 2014). Briefly, attached cells were replated into 24-well plates, 5×104 cells per well, on glass coverslips for 24 hr culture. Then 5000 sorted CXCR4low MKs or CXCR4high MKs were added in the upper inserts and placed onto macrophages chambers for additional 16 hr incubation without or with 2 μg ml–1 TNFα neutralizing antibody (R023, Sino Biological; 1:100) or 2 μg ml–1 IL-6 neutralizing antibody (MP5-20F3, Biolegend) at 37 °C, 5% CO2. The upper inserts were discarded and macrophages were washed with PBS without antibiotics and incubated with 105 GFP-labeled E. coli for 2 hr at 37 °C, 5% CO2. Cells were washed three times with PBS and incubated with DMEM without sodium pyruvate or HEPES (Gibco) with gentamycin (50 μg ml–1) for 30 min at 37 °C, 5% CO2 to remove adherent bacteria. Cells were then detected by flow cytometry or fixed by cold methanol for 15 min and blocked with 10% BSA overnight, followed by incubation with F4/80 (BM8, eBioscience; 1:100) for 2 hr at room temperature before being quantified using a spinning disk confocal microscope (Dragonfly, Andor).

For neutrophil phagocytosis, CD11b+ Gr1+ Ly6c– neutrophils were sorted from the spleen and propagated in RPMI 1640 (Gibco) containing 10% FBS. Neutrophil phagocytosis was performed as described in macrophage phagocytosis assay, except cells were sedimented for 30 min and fixed on glass coverslips after incubated with GFP-E. coli and gentamycin. The capacity of phagocytosis was evaluated by flow cytometry or by fluorescence intensity of GFP-E. coli. using the confocal microscope within macrophages and neutrophils.

For megakaryocyte phagocytosis, CXCR4low and CXCR4high MKs were sorted from the bone marrow and propagated in RPMI 1640 (Gibco) containing 10% FBS without antibiotics and incubated with 105 GFP-labeled E. coli for 2 hr at 37 °C, 5% CO2. Cells were washed three times with PBS and incubated with DMEM without sodium pyruvate or HEPES (Gibco) with gentamycin (50 μg ml–1) for 30 min at 37 °C, 5% CO2 to remove adherent bacteria. Cells were then detected by flow cytometry.

### Bone marrow ex vivo live imaging

Pf4Cre+; Rosa26fs-tdTomato+/– mice were infected with L. monocytogenes for 24 hr. FITC-Dextran (average mol wt 2000000, Sigma-Aldrich) was injected intravenously at a dose of 1.25 mg per mouse before being sacrificed. The ends of the femur below the end of the marrow cavity were cut. The bone marrow plug was gently flushed out of the end of the bone with a 21-gauge blunt needle not to break up the marrow plug. Bone marrow was flushed integrally and fixed onto a glass slide in a chamber, rinsed with RPMI 1640 (Gibco), and covered slightly with a coverslip. The integrity of the vascular structure in the bone marrow was observed and warranted through FITC-Dextran inflorescence before capturing images. Confocal images were obtained every minute on the spinning-disk confocal microscope (Dragonfly, Andor) and analyzed using Imaris 9.0 software (Oxford Instruments).

### In vitro MK culture, MK size, and proplatelet formation measurement

MKs were sorted using a cell sorter (MoFlo Astrios, Beckman Coulter) and cultured in 24-well plates in SFEM (Stem Cell Technologies) plus 100 ng ml–1 mTPO (Novoprotein) and 1% Pen/Strep (Hyclone), and incubated at 37 °C, 5% CO2 for 4 days. Images were taken by a Nikon Ts2R microscope equipped with a Nikon DS-Ri2 camera. Cell size and proplatelet formation were measured on day 3 or day 5 post-cultured, respectively, using Nikon NIS-Elements BR.

### Bone marrow transfer experiments

Pf4Cre mice were mated with the Rosa26fs-tdTomato line to generate Pf4Cre+; Rosa26fs-tdTomato+/– mice. tdTomato+ MKs were isolated from Pf4Cre+; Rosa26fs-tdTomato+/– mice. Six- to 8-week-old recipient mice were pre-treated with PBS or 2500 CFUs of L. monocytogenes as previously described 1 day before cell perfusion. 1×105 tdTomato+ MKs were sorted and intravenously injected into control or L. monocytogenes infected mice. tdTomato+ MKs were detected in lungs with immunostaining 2 days after cell perfusion.

mtdTomato+ bone marrow cells were isolated from Pf4Cre–; Rosa26fs-mTmG+/– mice. 1×106 mtdTomato+ bone marrow cells were intravenously injected into control or one-day-L. monocytogenes infected mice. mtdTomato+ MKs were detected in bone marrow, liver, and spleen 2 days after cell perfusion.

For in vivo CXCR4high MK function assay in MK ablation mice, DT was intraperitoneally injected every day for 5 days. On the second and fourth days, 2×105 sorted wild-type CXCR4high MKs or CXCR4low MKs were intravenously injected into indicated groups. PBS or 2500 CFUs of L. monocytogenes as previously described were injected intravenously on the third day. Spleen and liver were harvested 3 days after infection to determine the bacterial burdens as described.

### T cell reactivation in vitro

Splenocytes (1×106 cells well–1) from control or MK ablated mice after 7 days L.m.-OVA infection were re-stimulated for 4 hr in vitro with OVA peptide (10 μM) in the presence of Brefeldin-A (BFA, 10 μg ml–1). Activated T cells were then analyzed by a flow cytometer.

For MK-induced T cell activation, 3×104 MK subpopulations for each sample were sorted and co-cultured with 100 μg ml–1 soluble full-length OVA for 24 hr, then co-cultured with 6×104 OT-I CD8+ T cells or B3Z T cells (Karttunen et al., 1992) for 48 hr at 37 °C in a 5% CO2 incubator as described (Zufferey et al., 2017). OT-I T cell activation was detected by measuring intracellular IL-2 levels. B3Z T cell activation was detected using β-galactosidase Assay Kit (RG0036, Beyotime). Bone marrow-derived dendritic cells (DCs) were adopted as positive controls for T cell activation assay. To obtain bone marrow-derived DCs, isolated bone marrow cells were cultured in RPMI 1640 with 10 ng ml–1 of GM-CSF and 10 ng ml–1 of IL-4 as described (Roney, 2019).

### Computational modeling of random myeloid cell localization

We have performed randomized simulations as in previous reports (Bruns et al., 2014; Jiang et al., 2018) in Python. Images of a 400 μm × 400 μm bone marrow region with CXCR4high and CXCR4low MKs, in which background staining was removed, were used to generate MKs onto which 200 myeloid cells were randomly placed, consistent with an average density of 200 myeloid cells per field. Each simulated run placed 200 random myeloid cells (mean diameter 5 μm) was repeated 500 times. The shortest Euclidean distance was calculated for each myeloid cell to CXCR4high or CXCR4low MKs. Random and observed distance distributions were compared using the modified nonparametric two-dimensional (2D) KS test as described (Bruns et al., 2014; Jiang et al., 2018).

### Statistical analyses

Data are presented as means ± s.e.m or presented medians, first and third quartiles. For phagocytosis assay and MK size measurement, data were analyzed by a one-dimensional KS test. Differences were considered statistically significant if p<0.05. For the comparison of three-dimensional distances, a two-dimensional KS test was used. The difference was considered statistically significant if p<0.05. For multiple comparisons analysis, data were analyzed by repeated-measures one-way analysis of variance (ANOVA) followed by Dunnett’s test. Differences were considered statistically significant if p<0.05. ǂ p<0.05, ǂǂ p<0.01, ǂǂǂ p<0.001, n.s., not significant. For pairs of measurements, data were analyzed by paired Student’s t-test. Differences were considered statistically significant if p<0.05. # p<0.05, ## p<0.01, ### p<0.001, n.s., not significant. For other experiments except for scRNA-seq analysis, data were analyzed by a two-tailed Student’s t-test. Differences were considered statistically significant if p<0.05. * p<0.05, ** p<0.01, *** p<0.001, n.s., not significant.
