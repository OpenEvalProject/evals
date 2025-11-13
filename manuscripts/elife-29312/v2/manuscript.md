# Single-cell transcriptomics reveals a new dynamical function of transcription factors during embryonic hematopoiesis

## Authors

- Isabelle Bergiers<sup>1</sup> ([ORCID: 0000-0001-9622-7960](https://orcid.org/0000-0001-9622-7960))
- Tallulah Andrews<sup>2</sup> ([ORCID: 0000-0003-1120-2196](https://orcid.org/0000-0003-1120-2196))
- Özge Vargel Bölükbaşı<sup>1</sup> ([ORCID: 0000-0003-4013-6343](https://orcid.org/0000-0003-4013-6343))
- Andreas Buness<sup>1</sup>
- Ewa Janosz<sup>1</sup>
- Natalia Lopez-Anguita<sup>1</sup>
- Kerstin Ganter<sup>1</sup>
- Kinga Kosim<sup>1</sup>
- Cemre Celen<sup>1</sup>
- Gülce Itır Perçin<sup>1</sup>
- Paul Collier<sup>3</sup>
- Bianka Baying<sup>3</sup>
- Vladimir Benes<sup>3</sup>
- Martin Hemberg<sup>2</sup> †
- Christophe Lancrin<sup>1</sup> ([ORCID: 0000-0003-0028-7374](https://orcid.org/0000-0003-0028-7374)) †

### Affiliations

1. European Molecular Biology Laboratory, EMBL Rome Monterotondo Italy
2. Wellcome Trust Sanger Institute Hinxton United Kingdom
3. Genomics Core Facility European Molecular Biology Laboratory Heidelberg Germany

† Corresponding author

## Abstract

Recent advances in single-cell transcriptomics techniques have opened the door to the study of gene regulatory networks (GRNs) at the single-cell level. Here, we studied the GRNs controlling the emergence of hematopoietic stem and progenitor cells from mouse embryonic endothelium using a combination of single-cell transcriptome assays. We found that a heptad of transcription factors (Runx1, Gata2, Tal1, Fli1, Lyl1, Erg and Lmo2) is specifically co-expressed in an intermediate population expressing both endothelial and hematopoietic markers. Within the heptad, we identified two sets of factors of opposing functions: one (Erg/Fli1) promoting the endothelial cell fate, the other (Runx1/Gata2) promoting the hematopoietic fate. Surprisingly, our data suggest that even though Fli1 initially supports the endothelial cell fate, it acquires a pro-hematopoietic role when co-expressed with Runx1. This work demonstrates the power of single-cell RNA-sequencing for characterizing complex transcription factor dynamics.

## Introduction

Over the past decade, advances in high-throughput transcriptomics and DNA occupancy analyses have provided valuable insights into how transcription factors (TFs) regulate cell fate decisions and determine cell identity. It has become clear that during embryonic development, the expression of key TFs is strictly regulated, and it has been shown that the combinatorial expression of a relatively limited number of TFs is sufficient to establish (and potentially change) cell identity and differentiation through their action on the underlying gene regulatory networks (GRNs) (Iwafuchi-Doi and Zaret, 2016). In this context, bulk transcriptomics analysis and chromatin immuno-precipitation sequencing (ChIP-seq) were used to describe TF interactions, thereby providing GRN models (Dunn et al., 2014; Mullen et al., 2011). Recently, these techniques were successfully used to study the embryonic hematopoietic system in an in vitro embryonic stem cell (ESC) differentiation model (Goode et al., 2016).

However, the use of bulk cell populations constitutes an important limitation in our efforts to fully understand the GRNs. Although bulk transcriptomics can reveal crucial overall gene correlations between semi-stable cellular states, it cannot resolve subtler gene interactions occurring in complex transitional states. In addition, using a bulk approach makes it difficult to infer the direct consequences on the transcriptional landscape upon which these TFs are acting.

These limitations can be overcome by the use of single-cell approaches. Over the past five years, tremendous technical progress has been achieved in the field. Gene expression can be efficiently assessed at the single-cell level, making it possible to distinguish subpopulations within tissues and cell cultures (Kolodziejczyk et al., 2015; Scialdone et al., 2016). Single-cell transcriptomics has previously been used to unravel complex developmental transitions such as gastrulation (Scialdone et al., 2016), demonstrating that it is possible to determine combinations of TFs that are expressed at the single-cell level as cellular differentiation progresses.

In the present work, we applied single-cell transcriptomics approaches to the ontogeny of the blood system in the mouse embryo. The GRNs that are involved in the production of the hematopoietic stem and progenitor cells (HSPCs) at the origin of all blood cells are not well understood. During mouse embryogenesis, HSPCs are generated mainly in the yolk sac (YS), from E7–E7.5, and in the aorta-gonad-mesonephros (AGM) region, from E10.5. They emerge from the endothelial cells forming the vasculature, through a process called the endothelial to hematopoietic transition (EHT) (Boisset et al., 2010; Choi et al., 1998; Eilken et al., 2009; Lancrin et al., 2009; Zovein et al., 2008). It has been proposed that a heptad of seven TFs (Gata2, Runx1, Erg, Fli1, Lmo2, Lyl1 and Tal1) known to be essential for blood development form a transcriptional complex that is potentially involved in the generation of HSPCs. This proposal was based on bulk ChIP-seq analysis of the binding of these seven TFs to the regulatory elements of 927 genes in the HPC7 cell line (Wilson et al., 2010). Nonetheless, there was no direct evidence that all seven TFs were expressed together at the single-cell level during embryogenesis or that the heptad targets play a crucial role in development. Employing single-cell transcriptomics analysis and an in vitro ESC differentiation system that gives rise to blood cells, we addressed these questions and provided novel insights into the formation of HSPCs from endothelial cells. Our data show that during EHT, two sets of TFs have opposite effects that allow proper differentiation. Through the transition, Erg and Fli1 support the endothelial cell fate while Runx1 and Gata2 promote the hematopoietic one. Unexpectedly, we found that the endothelial transcription factor Fli1 could acquire a hematopoietic function when expressed together with the hematopoietic master regulator Runx1. This work shows that GRN analysis based on single-cell transcriptomics data can highlight biological aspects that are missed by classical bulk methods, emphasizing the power of single-cell approaches in the understanding of complex developmental transitions.

## Results

### Key transcription factors identify a population intermediary between endothelial and blood cells during EHT in vivo and in vitro

We performed single-cell quantitative RT-PCR (sc-q-RT-PCR) on 95 genes associated with hematopoietic, endothelial (Endo), and vascular smooth muscle (VSM) cells (Supplementary file 1). Single cells were sorted from YS and AGM dissected from mouse embryos at E9, E10.5 and E11. To enrich for cells undergoing EHT, we selected cells using both the endothelial marker VE-cadherin (VE-Cad) and the hematopoietic marker CD41 (Figure 1—figure supplements 1 and 2). Using hierarchical clustering, these cells could be separated into three major groups in both tissues: Endo cells, Pre-HSPCs, which expressed both hematopoietic and endothelial genes (Taoudi et al., 2008), and HSPCs (Figure 1A and B, Figure 1—figure supplements 1 and 2).

![Figure 1.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig1-v2.jpg)

**Figure 1.:** (A) Principal component analysis (PCA) plot showing the cells isolated at E9, E10.5 and E11 from AGM and YS according to the indicated sample clusters (SC). For each tissue, each time point represents one experiment. (B) PCA plot showing the Gfi1–/– Gfi1b–/– GFP+ YS cells mixing with Pre-HSPCs group (black ellipse). Note that the PC2 axis has been reversed. (C) Experimental workflow used to differentiate in vitro ESCs into blood cells. BL-CFC, blast colony forming cells; EB, embryoid body; FACS, fluorescence-activated cell sorting. (D) PCA plot showing the four groups of cells coming from in vitro differentiated ESCs. (E) Heatmap showing average expression of endothelial (blue), hematopoietic genes (red) and seven key TFs (black) in the four groups found in vivo. The black rectangle highlights the expression of the seven TFs. (F) Heatmap showing the average expression of endothelial (blue), hematopoietic (red), vascular smooth muscle genes (purple) and seven key TFs (black) in the four groups found after in vitro differentiation of ESCs. The black rectangle highlights the expression of the seven TFs. See also Figure 1—figure supplements 1–6, Supplementary file 1, 2, 3 and 11.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) FACS plots of VE-Cad and CD41 expression in the AGM region at E9, E10.5 and E11. Several embryos (seven for E9, 13 for E10.5 and 9 for E11) were pooled for each time point and three subpopulations were single-cell sorted: VE-Cad+ CD41–, VE-Cad+ CD41Medium and VE-Cad+ CD41High. (B) Hierarchical clustering analysis done with sc-q-RT-PCR data from AGM cells isolated in 1A. Three main groups were defined. See also Supplementary file 11.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) FACS plots of VE-Cad and CD41 expression in the YS region at E9, E10.5 and E11. Several embryos (seven for E9, 13 for E10.5 and 9 for E11) were pooled for each time point and three subpopulations were single-cell sorted: VE-Cad+ CD41–, VE-Cad+ CD41Medium and VE-Cad+ CD41High. (B) Hierarchical clustering analysis done with sc-q-RT-PCR data from YS cells isolated in 2A. Three main groups were defined. See also Supplementary file 11.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Scatter plots showing the average expression of endothelial genes versus the average expression of hematopoietic genes at the indicated developmental time points.See also Supplementary file 11.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A) Correlation study performed on the average gene expression for the groups highlighted in Figure 1A, Figure 1—figure supplements 1B and 2B. (B) Hierarchical clustering analysis done with sc-q-RT-PCR data from AGM and YS cells presented in Figure 1—figure supplements 1B and 2B. See also Supplementary file 11.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** (A) FACS plot of GFP expression in the Gfi1–/– Gfi1b–/– yolk sac region at E9.5. Single cells expressing highly GFP were isolated and studied with sc-q-RT-PCR. (B) Hierarchical clustering analysis done with sc-q-RT-PCR data from yolk sac cells isolated in (A). See also Supplementary file 11.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** (A) Hierarchical clustering analysis done with sc-q-RT-PCR data from in vitro differentiated ESCs. Four main clusters were defined. (B) Violin plots showing the expression of the 24 genes shown in Figure 1E. Seven key transcription factors are highlighted with a black rectangle. (C) Violin plots showing the expression of the 26 genes shown in Figure 1F. Seven key transcription factors are highlighted with a black rectangle. See also Supplementary file 11.

While the frequency of each population of cells differed between tissues and time-points (Figure 1—figure supplement 3), groups were more strongly correlated (Pearson r > 0.9) to their counterparts than to other groups in the same tissue and clustered together using principal component analysis (PCA) and hierarchical clustering (Figure 1—figure supplement 4 and Figure 1A).

In addition, E9.5 YS Gfi1–/–-Gfi1b–/–- cells, which are incapable of completing EHT due to the lack of the two transcriptional repressors Gfi1 and Gfi1b (Lancrin et al., 2012), clustered together with the Pre-HSPCs, reinforcing the notion that this population is an essential intermediary step between Endo and HSPCs (Figure 1—figure supplement 5 and Figure 1B).

EHT can be recapitulated in vitro using the ESC differentiation model (Huber, 2010). We performed a 3.25 day differentiation followed by isolation of Flk1+ cells, enriched in blast colony forming cells (BL-CFCs) (Choi et al., 1998), which were cultured for a further 1.5 days before performing sc-q-RT-PCR using the same 95 genes (Figure 1C). Hierarchical clustering identified four groups, corresponding to Endo, HSPCs, and Pre-HSPCs found in the embryonic vasculature and a fourth group characterised by high expression of Acta2 (smooth muscle actin) and Serpine1 and by low expression of endothelial and hematopoietic genes, which we identified as VSM (Figure 1—figure supplement 6A and Figure 1D).

In both the in vivo and in vitro systems, the most notable characteristic of the Pre-HSPCs population is the co-expression of seven genes coding for hematopoiesis-associated transcription factors: Erg, Fli1, Tal1, Lyl1, Lmo2, Runx1 and Gata2 (Figure 1E and F, Figure 1—figure supplement 6B and C), which have been proposed to work together as a complex (Wilson et al., 2010). By contrast, Endo cells expressed only Erg, Fli1, Lmo2 and Tal1 whereas HSPCs expressed Fli1, Lmo2, Lyl1, Runx1 and Tal1. This suggested that these seven TFs might be important in establishing and/or maintaining the cell-type identity of the Pre-HSPCs population.

### Simultaneous overexpression of Erg, Fli1, Tal1, Lyl1, Lmo2, Runx1, Cbfb and Gata2 during hemangioblast differentiation leads to the formation of a population resembling Pre-HSPCs

The co-expression of the seven TFs in the Pre-HSPCs populations in vivo and in vitro prompted us to ask whether the co-expression of these genes could be linked to the identity of the Pre-HSPCs. To determine the effect of the expression of these seven factors at the single-cell level, we established an inducible ES cell line in which all seven genes and Cbfb, a protein that is essential for Runx1 DNA binding and function (Wang et al., 1996; Tahirov et al., 2001), could be expressed simultaneously following the addition of doxycycline (dox). We generated an inducible ES cell line (i8TFs) in which the eight coding sequences were linked together by T2A sequences (Figure 2A). This strategy exploits the ‘ribosomal skipping’ mechanism of the viral T2A peptide (Donnelly et al., 2001) to allow the production of eight proteins from a single transcript. The expression of all eight proteins was validated by western blot after 24 hr of dox treatment in ESC culture (Figure 2B). As a control, we created an ESC line, which does not contain any novel cDNA (Empty), but is otherwise identical to the i8TFs line.

![Figure 2.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig2-v2.jpg)

**Figure 2.:** (A) Scheme showing the generation of the i8TFs ESC line. (B) Western blot showing the protein expression of the eight TFs after doxycycline (dox) treatment in the Empty line and in the i8TFs ESC line. See also Supplementary file 11.

We studied the effect of the overexpression of the eight TFs during hemangioblast differentiation. After three days of EB culture, the Flk1+ cells were differentiated for one day in BL-CFC culture, at which time the cells have lost their mesoderm identity and have produced endothelial and vascular smooth muscle cells. Dox was added at this time point, and cells were cultured for two more days. Cells were imaged every 15 min for 48 hr and were harvested at the end of the culture for flow cytometry. The Empty cell line did not show any major difference, neither in terms of cell surface markers nor in terms of cell morphology after dox treatment. By contrast, we noticed a dramatic change following the activation of the eight TFs when almost all cells developed the same phenotype (VE-Cad+ CD41+ and cKit+ CD41+ depending on the staining) (Figure 3A). This change was accompanied by a marked decrease in the number of round cells (Figure 3B and Figure 3—figure supplement 1). The simultaneous expression of the eight TFs did not change the frequency of living cells (Figure 3C) but there was a 40% decrease in the number of cells in S phase, suggesting that the expression of the eight TFs has a negative impact on cell proliferation (Figure 3D).

![Figure 3.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig3-v2.jpg)

**Figure 3.:** (A) Representative FACS plots of VE-Cad, cKit and CD41 expression after 3 days of BL-CFC culture of the indicated ESC lines (n = 3). (B) Graphs showing the average numbers of round cells counted per frame (n = 3) in a 48 hr time course for the indicated ESC lines. Error bars represent standard deviations. (C) Bar graph indicating the frequency of non-apoptotic living cells for the indicated ESC lines. Error bars represent standard deviations (n = 3). (D) Bar graph displaying the frequency of cycling cells for the indicated ESC lines. Error bars represent standard deviations (n = 3). (E) Bar graph displaying the number of hematopoietic colonies after replating cells in a colony-forming-unit assay from the indicated conditions. Error bars represent standard deviation (n = 4). ns, non significant. ** p-value<0.01 (paired two-tailed t-test). * p-value<0.05 (paired two-tailed t-test). See also Figure 3—figure supplement 1 to 5, Supplementary file 1, 4, 5 and 11.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The scale bar corresponds to 200 μm. See also Supplementary file 11.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) FACS plot of VE-Cad and CD41 expression at day 1 of BL-CFC culture. The rectangles highlight the enriched vascular smooth muscle (eVSM) and endothelial (Endo) populations. (B) Hierarchical clustering analysis done with sc-q-RT-PCR data from VE-Cad+ CD41– (Endo) and VE-Cad– CD41– (eVSM) populations. The red rectangles indicate the cells from the eVSM population expressing endothelial markers (e.g. Ramp2, Sox7, Kdr). (C) FACS plots of VE-Cad, cKit and CD41 expression of the enriched vascular smooth muscle (eVSM) and endothelial (Endo) populations from the i8TFs cell line after 48 hr in HE culture. (D) Bar graph displaying the number of hematopoietic colonies after replating cells in a colony-forming-unit assay from the indicated conditions. Error bars represent standard deviations (n = 2). See also Supplementary file 11.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A) PCA plot showing the microarray analysis results from the eVSM after 24 hr of dox treatment on the Empty cell line. Ellipses indicate the different groups of samples. (B) PCA plot showing the microarray analysis results from the indicated conditions after 24 hr of dox treatment on the i8TFs ESC line. Numbers indicate the number of genes significantly differentially expressed between the two conditions (p-value<0.05). Ellipses indicate the different groups of samples. See also Supplementary file 11.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** (A) GO term enrichment analysis of the genes differentially expressed between –dox and +dox conditions for each population. (B) Venn diagrams showing the genes differentially expressed for both populations together with the gene targets previously identified by ChIP-seq analysis (Wilson et al., 2010). (C) List of the 26 heptad target genes differentially expressed upon induction of the eight TFs in both Endo and eVSM populations. See also Supplementary file 11.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** (A) Scheme showing the eight constructs used to make the i1TF ESC lines. (B) Western blots showing the protein expression of the eight transcription factors after doxycycline treatment for each of the i1TF ESC lines. (C) Representative FACS plots of VE-Cad, cKit and CD41 expression after three days of BL-CFC culture of the indicated ESC lines (n = 3). (D) Bar graphs indicating the frequency difference between +dox and –dox conditions for the ten indicated cell lines. Error bars represent standard deviations (n = 3). See also Supplementary file 11.

To evaluate the impact of the simultaneous overexpression of these eight genes on hematopoietic differentiation activity, we performed a colony-forming unit (CFU) assay. We plated the cells from both the i8TFs – dox and the i8TFs + dox conditions in the absence of dox in a medium that allows the growth of both myeloid and erythroid cells. We observed a dramatic increase in the number of colony-forming units from the +dox cells, suggesting that the induction of the eight TFs increases hematopoietic differentiation potential (Figure 3E).

The overexpression of the eight TFs led to the production of a majority of VE-Cad+ CD41+ cells (Figure 3A). However, at the beginning of dox treatment, the majority of cells were VE-Cad– CD41– (Figure 3—figure supplement 2A), which were enriched in vascular smooth muscle cells (named eVSMs) (Figure 3—figure supplement 2B). To understand the impact of the expression of the eight TFs on the two main non-hematopoietic populations — the VE-Cad+ CD41- endothelial population (named Endo) and the eVSM — we isolated Endo and eVSM cells at day 1 of BL-CFC culture (Figure 3—figure supplement 2A) and cultured them in hemogenic endothelial (HE) culture conditions with or without dox for 48 hr. Using flow cytometry, we showed that both populations were affected by the dox treatment and became almost entirely VE-Cad+ CD41+ (Figure 3—figure supplement 2C). Furthermore, the CFU-assay showed an increased hematopoietic differentiation capacity for the Endo +dox compared to the –dox condition, confirming their successful conversion (Figure 3—figure supplement 2D). By contrast, the eVSM cells did not show a comparable effect, and together with the flow cytometry data, this evidence suggests that even though the eVSMs gained the Pre-HSPCs phenotype, they probably remained more immature than the Endo +dox cells (Figure 3—figure supplement 2D). To further characterize the effect of the eight TFs on the eVSM and Endo populations, we carried out a microarray analysis on i8TFs eVSM and Endo conditions before (t0) and 24 hr after differentiation with or without dox treatment (+dox and –dox) (Supplementary file 5). The Empty ESC line eVSM was used as control. As expected, the dox treatment of these cells had little effect on the transcriptome as shown by PCA (Figure 3—figure supplement 3A). By contrast, the expression of the eight TFs changed the Endo and eVSM cells dramatically. Interestingly, the eVSM +dox group clustered closely to the Endo -dox and Endo +dox conditions but far apart from the eVSM -dox group. Differentially expressed gene (DEG) analysis highlighted the genes responsible for these changes (Figure 3—figure supplement 3B and Supplementary file 5). Gene ontology (GO) analysis of the DEGs showed that overexpression of the eight TFs led to the reduced expression of genes involved in vasculature and heart development, while there was an increase in the expression of genes linked to immune system and vasculature development for eVSM (compatible with the dual endothelial-hematopoietic identity of Pre-HSPCs) and cellular detoxification as well as vesicles for Endo (Figure 3—figure supplement 4A). Surprisingly, when comparing these DEGs with the 927 targets of the heptad identified by ChIP-seq, the overlap was only 26 genes (Figure 3—figure supplement 4B and C). This would suggest that the DEGs that we observed were not a direct consequence of the complex of eight TFs binding at the regulatory elements of these genes.

To find out whether the striking effect of the eight TFs is really due to the expression of several of these genes and not to the effect of one particular transcription factor, we generated eight inducible ESC lines for each of the single transcription factors (i1TF) (Figure 3—figure supplement 5A). Inducible expression of each TF was confirmed using western blot (Figure 3—figure supplement 5B). Using the same experimental layout as that used previously for i8TFs and Empty ESC lines, we performed BL-CFC assays and FACS analyses with these eight new ESC lines and studied the effect of dox treatment on each of them. We found that none of the i1TF lines were qualitatively similar to the i8TFs (Figure 3—figure supplement 5C and D).

To better distinguish differentiated cell populations, we repeated the BL-CFC culture with –dox/+dox treatment for the ten cell lines followed by sc-q-RT-PCR of the 95 genes used previously (Figure 4 and Supplementary file 6). In total, 854 cells were processed using sc-q-RT-PCR and passed quality control. Six biologically relevant cell clusters could be identified using hierarchical clustering analysis, and they were assigned names based on the expression of specific marker genes (Figure 4A). The Endo, VSM and Pre-HSPCs groups were defined as before (Figure 1). On the other hand, HSPCs were split into three groups: Erythroid Progenitor Cells I and II (EryPCs_I and EryPCs_II, respectively) and Myeloid Progenitor Cells (MyePCs). EryPCs_I and EryPCs_II were characterized by the expression of erythroid genes such as Gata1 and Hbb-bh1. EryPCs_I appeared to be more immature than EryPCs_II because the cells still express a high level of Itgb3 and Pecam1. MyePCs were characterized by the expression of myeloid markers such as Sfpi1 (or Pu.1) and Itgam and by the lack of erythroid genes.

![Figure 4.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig4-v2.jpg)

**Figure 4.:** (A) Hierarchical clustering showing the sc-q-RT-PCR results for 95 genes on the ten inducible ESC lines after three days of BL-CFC culture. The clusters were defined according to the intersection of the red dotted line with the dendrogram in the upper part of the heatmap. (B) Bar graphs displaying the cell number in each of the six clusters defined in (A) for the ten cell lines. Stars indicate significant differences for +dox conditions (see Supplementary file 6 for p-values). See also Figure 4—figure supplements 1 and 2, Supplementary file 1, 6 and 11.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** The data set is identical to the one in Figure 4. Here, fractions of cells are shown instead of absolute cell numbers. For the –dox condition, a box plot has been added. Significant differences between the –dox condition and the +dox condition for each cell line and population are indicated by red circles as determined by a general linearized model (quasi-Poisson). See also Supplementary file 11.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Experimental outline followed to compare the Empty and i8TFs ESCs with single-cell RNA sequencing. (B) PCA plot showing sc-RNA-seq analysis of the Empty and i8TFs cell lines after three days of BL-CFC culture. Ellipse highlights i8TFs + dox. See also Supplementary file 11.

For each cluster, the number of cells per condition was calculated and each +dox condition was statistically compared to all –dox conditions (Figure 4B and Figure 4—figure supplement 1). This analysis confirmed that following dox addition, the i8TFs cells form a Pre-HSPCs population co-expressing endothelial and hematopoietic genes, as suggested by the flow cytometry results. By contrast, none of the other cell lines presented such a dramatic change. Induction of Gata2 increased the frequency of EryPCs_II population by ~4 fold (Figure 4B). On the other hand, overexpression of Erg and Fli1 gave rise to slightly more Pre-HSPCs (Figure 4B). The other i1TF ESC lines had negligible changes upon dox treatment (Figure 4B and Figure 4—figure supplement 1).

Our sc-q-RT-PCR results suggested that the cells were homogeneous after the induction of the eight TFs. To confirm this observation, we carried out single-cell RNA sequencing (sc-RNA-seq) on i8TFs –dox, i8TFs +dox, Empty –dox and Empty +dox cells using the iCELL8 platform (Figure 4—figure supplement 2A). Again, PCA showed that i8TFs + dox cells were clearly clustered separately from the other cells (Figure 4—figure supplement 2B). On the basis of the PC2 variance, we noticed that there is less variance for the i8TFs +dox cells compared to the other three conditions. Altogether, this would suggest that the i8TFs +dox cells are comparatively more homogeneous than the control cells.

### In vitro generated Pre-HSPCs share similarities with AGM Pre-HSCs type I

To better characterize the i8TFs +dox cells compared to embryonic populations, we examined the expression pattern of CD41, CD43 and CD45 proteins together with VE-cad. It has been shown that these markers could define more precisely several intermediate stages in the EHT process: Pro-HSCs (VE-Cad+ CD41+ CD43– CD45–), Pre-HSCs type I (VE-Cad+ CD41+ CD43+ CD45-) and Pre-HSCs type II (VE-Cad+ CD41+ CD43+ CD45+) (Rybtsov et al., 2014). Our results show that around 99% of VE-cad+ cells in the i8TFs +dox condition have a phenotype similar to Pro-HSCs (Figure 5A and B). To verify this finding, we isolated from E10 AGM the Pro-HSCs and Pre-HSCs type I populations and performed sc-q-RT-PCR with our set of 95 genes (Figure 5—figure supplement 1A and B). Interestingly, we found that the Pro-HSCs population was heterogeneous. Although all cells express a high level of endothelial genes, only half express blood genes such as Runx1, Gfi1, Sfpi1 and Myb. By contrast, the Pre-HSCs type I is more homogenous. All cells express endothelial genes but at a lower level compared to Pro-HSCs. Moreover, all cells express hematopoietic genes (Figure 5—figure supplement 1B). When we analyzed these cells together with the in vivo data from Figure 1A and the cells from i8TFs –dox and +dox cultures, we noticed that about half of Pro-HSCs clustered with Endo, while the other part clustered with the Pre-HSPC (Figure 5C). On the other hand, the Pre-HSCs type I clustered with Pre-HSPCs. Surprisingly, in opposition to their Pro-HSCs phenotype, we found that the i8TFs +dox were very close to the Pre-HSCs type I (Figure 5C). This was confirmed when the analysis was done without the seven TFs (Figure 5—figure supplement 1C) and when the single-cell qRT-PCR data from the 1,660 cells from Figures 1, 4 and 5 were combined (Figure 5—figure supplement 2).

![Figure 5.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig5-v2.jpg)

**Figure 5.:** (A) Representative FACS plots of VE-Cad, CD45, CD43 and CD41 expression after 3 days of BL-CFC culture of the i8TFs ESC line in the presence or absence of dox (n = 3). (B) Bar graphs showing the average percentage of the four different VE-Cad+ cell populations after three days of culture (n = 3). Error bars represent standard deviations. (C) PCA plot showing the sc-q-RT-PCR results for 95 genes combining the cells from the i8TFs cell line after three days BL-CFC culture with the results from cells collected from wildtype YS and AGM regions (Figure 1B) and from the E10 AGM Pro-HSCs and Pre-HSCs type I. Note that the PC2 axis has been reversed. The ellipse highlights i8TFs +dox. See also Figure 5—figure supplements 1 and 2, Supplementary file 1, 7, 8 and 11.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) FACS plots of VE-Cad, CD45, CD43 and CD41 expression in the AGM region at E10 (31–32 somite pairs). Single cells from Pro-HSCs (VE-Cad+ CD41+ CD45- CD43-) and Pre-HSCs type I (VE-Cad+ CD41+ CD45- CD43+) populations were isolated. P9 highlights CD41– CD43– cells. (B) Hierarchical clustering analysis done with sc-q-RT-PCR data from (A). Endothelial (Cdh5, Sox7, Kdr and Pcdh12) and hematopoietic genes (Runx1, Gfi1, Sfpi1, Itgam and Sla) were marked in blue and red, respectively. (C) PCA plot showing the sc-q-RT-PCR results of the same cells as in Figure 5C but after removing Runx1, Gata2, Tal1, Fli1, Lyl1, Erg and Lmo2 genes from the expression data. Note that the PC2 axis has been reversed. The ellipse and red arrow highlight the i8TFs +dox cells. See also Supplementary file 11.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) PCA plot displaying the single-cell qPCR results of all cells from Figures 1, 4 and 5 (a total of 1,660 cells). (B) Same PCA plot as (A) but highlighting the populations from Figure 1B. (C) Same PCA plot as (A) but highlighting the populations from Figure 1D. (D) Same PCA plot as (A) but highlighting some of the populations from Figure 4. (E) Same PCA plot as (A) but highlighting some of the populations from Figure 5C. See also Supplementary file 11.

In conclusion, although the i8TFs +dox cells had a phenotype similar to that of the Pro-HSCs, their transcriptional profile was more similar to Pre-HSCs type I.

### Identification of gene regulatory network from single-cell RNA sequencing data

To determine how the induction of the 8TFs by dox treatment affected GRNs using single-cell-RNA-seq, we decided to focus on the VSM cells because, unlike the Endo population, they are not naturally undergoing EHT (Figure 3—figure supplement 2C). Indeed, between Endo +dox and Endo –dox, there was only a two-fold increase in VE-Cad+ CD41+ population. On the other hand, there was a tenfold increase in VE-Cad+ CD41+ population between eVSM +dox and eVSM –dox (Figure 3—figure supplement 2C). Moreover, this population shows the largest gene expression contrast in our microarray data upon dox treatment, facilitating the identification of the GRNs controlled by the eight TFs (Figure 3—figure supplement 3B). As in the microarray experiments, VE-Cad– CD41– cells were sorted at day 1 of BL-CFC culture and cultured in the absence or presence of dox for 24 hr. Subsequently, cells from the –dox and +dox conditions were pooled at a 1:1 ratio and put on a Fluidigm C1 chip. The Fluidigm system allowed a higher sensitivity than the Wafergen system, but it did not allow the processing of several conditions and a large number of cells at the same time. The experimental design whereby cells were mixed and loaded onto one chip minimized the technical variability that would invariably arise from using two separate chips (Figure 6—figure supplement 1A). We obtained two biological replicates, and from each chip 96 cells (192 cells in total) were isolated and sequenced together. To determine which cells were exposed to dox we used the expression of the transgene (Figure 6—figure supplement 1B). A PCA of the sequencing data showed that cells expressing high levels of the 8TFs transcripts clustered separately from those expressing low levels of these transcripts (Figure 6—figure supplement 1C).

To identify regulatory relationships for the eight TFs, we performed a network analysis using the generalized distance correlation measure, dcor statistic (Székely et al., 2007), together with its conditional version pdcor (Székely and Rizzo, 2014). This measure has the advantage of being able to detect both linear and non-linear relationships between the transcriptome and the seed genes. However, when only the eight TFs were used as seeds, the resulting network was very small with only five of the eight TFs represented (not shown). Thus, we expanded the set of seed genes to include Gata1, Gfi1b, Spi1 (or Pu.1), Ldb1 and Cbfa2t3, which are known to play important roles in hematopoiesis. Using this extended set of genes, we obtained a network that illustrated how the eight TFs indirectly interacted through a common regulatory pathway (Ferreira et al., 2005; Goardon et al., 2006; Imperato et al., 2015; Lancrin et al., 2012; Mylona et al., 2013). The directionality of the relationships, positive correlation or negative correlation, was defined using the sign of a two-tailed t-test (gene-pairs with p>0.05 were assigned to ‘other’). Finally, interactions between seed genes were identified by conditioning the ‘targets’ of each seed gene on the expression of each other seed gene. An interaction was inferred if the relationships between both seed genes and a particular ‘target’ gene increased in strength when conditioning on the other seed gene.

When visualizing the resulting network, we only plotted the seeds that interacted with at least with one other seed (black lines) and the gene targets of at least two seed interactions (Figure 6A). Consistent with evidence from the literature, our network reconstruction method reports a tight interaction between the seed factors, apart from Lbd1, they are all included in the resulting network. Furthermore, we observe a core network composed of Erg, Lyl1, Lmo2, Tal1, Gfi1b, and Gata1 with Fli1 and Runx1 on opposite ends of the periphery. Several of the genes that were identified as targets of the seed genes were also known from the literature; for example, Gpr56, which was upregulated in our microarray experiment after dox treatment (Figure 3—figure supplement 4C), and Nfe2 (Wilson et al., 2010; Woon Kim et al., 2011). Moreover, several of the targets had previously been identified as being differentially expressed following dox treatment (Figure 3—figure supplement 4C, Supplementary file 5).

![Figure 6.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig6-v2.jpg)

**Figure 6.:** (A) Network built from gene correlations. Gpr56 is highlighted with a red asterisk. (B) Centrality values for all the genes containing a heptad peak within 1 kb of the TSS that are significantly above the median. Gpr56 is highlighted with a red asterisk. (C) The upper part shows the ChIP-Seq data for the seven TFs from the Wilson et al. (2010) study in the Gpr56 locus. The y-axis shows reads displayed as density plots, which were generated by Wilson et al. (2010) and visualized using the Integrated Genome Browser software. The two putative enhancers are highlighted with red rectangles. The lower part shows the results of the transcriptional reporter assay for two potential heptad enhancers in Gpr56 locus using i8TFs ESCs treated for 24 hr with doxycycline. Error bars represent standard deviations (n = 3). See also Figure 6—figure supplement 1 and Supplementary file 11.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Experimental workflow used to differentiate in vitro eVSM cells from the i8TFs ESC line and to analyze them by sc-RNA-seq after 24 hr of treatment. (B) Scatter plot showing the expression of the 8TFs construct among all the cells from the two replicates. Red indicates high expression, blue low expression and grey undefined expression. The y-axis shows SF-normalized expression colored by quantile. (C) PCA plot of sc-RNA-seq results. The color codes are the same as those in (B). See also Supplementary file 11.

Encouraged by the results from the dcor analysis, we carried out a genome-wide analysis. Since Dcor is a slow correlation method, it was computationally infeasible to calculate the global network with it. That is why we used Spearman correlation, a very fast correlation method. We combined the two datasets and kept all correlations where the absolute value of the average correlation was greater than 0.25 and where the sign was consistent across Remove Unwanted Variation (RUV) and Size Factors (SF) normalizations. This resulted in a network containing 7,262 genes and 163,474 edges of which 123,394 were positive and 40,080 negative. Importantly, 11 genes out of the 13 seed genes used in the previous analysis where found in this large network: Cbfa2t3, Fli1, Gata2, Lmo2, Erg, Tal1, Gfi1b, Gata1, Runx1, Spi1 and Lyl1. In addition, among the 145 genes containing heptad peaks within 1 kb of their TSS, 26 were found in the network, although this was not significantly more than expected by chance (p>0.1, Fisher-exact test).

To identify the most important genes in the network, we calculated three different centrality measures (degree, betweenness and eigen) (Figure 6B). The number of genes among the 11 seed genes with values above the median was significantly higher than that expected by chance for all three measures (degree p-value=0.0005, betweenness p-value=0.006, eigen p-value=0.03). Interestingly, for the 26 heptad targets, only the betweenness presented a higher number of targets above the median than would be expected by chance (p-value=0.04). This highlights the expected central role of the heptad targets by their position ‘in between’ the main players of the network.

As Grp56 appeared as a top candidate in our two network analyses, we chose it for further experiments (Figure 6C). Gpr56 has been shown to be expressed in the hematopoietic clusters of the aorta (Solaimani Kartalaei et al., 2015) and to be upregulated along the EHT (Goode et al., 2016). ChIP-seq data (Wilson et al., 2010) show that there are two Gpr56 regulatory elements bound by seven out of the eight TFs in the HPC7 cell line (Figure 6C). We selected these putative enhancers and cloned them in a plasmid upstream of the Firefly luciferase reporter gene. A gene reporter assay in the i8TFs ESC line demonstrated that the induction of the eight TFs led to a strong increase in luciferase gene expression with the two Grp56 enhancers (Figure 6C). In conclusion, we were able to infer GRNs based on sc-RNA-seq data. We identified the key players affected by the induction of the eight TFs, among which Gpr56 was a major target gene.

### Gene regulatory network analysis reveals contrasting effects of Runx1 and Fli1

The simultaneous expression of the eight factors led to the formation of a population resembling Pre-HSPCs through their specific action on GRNs. It was not clear, however, why the cells were blocked in this normally ‘transient’ intermediate stage of the EHT. To unravel this, we applied our network analysis to a sc-RNA-seq dataset of endothelial cells and HSPCs, before and after the EHT, respectively (Pereira et al., 2016). We generated a network using the same seeds as before (Figure 6A), and the most striking feature of the new network is that Fli1 and Runx1 share several targets, but with opposing directions of correlation (Figure 7A). A genome-wide network analysis based on Spearman correlations showed a similar pattern in which 210 genes were correlated to both Fli1 and Runx1 but in opposite directions (Figure 7B and Supplementary file 9). Furthermore, GO analysis revealed that genes whose expression is positively correlated with Fli1 and negatively correlated with Runx1 (yellow rectangle) are enriched for the terms vascular development, angiogenesis and cell migration (Figure 7—figure supplement 1A). On the other hand, genes whose expression is positively correlated with that of Runx1 and negatively correlated with that of Fli1 (green rectangle) are associated with the GO term immune system process (Figure 7—figure supplement 1A). Hence, Runx1 is more associated with hematopoietic genes whereas Fli1 is more associated with vascular genes. Interestingly, ChIP-seq data from Wilson et al. (2010) showed that 77 out of the 210 are direct targets of both Runx1 and Fli1 (Figure 7—figure supplement 1B and Supplementary file 9). The observed opposite correlation could be due to the fact that most endothelial cells express only Fli1 and not Runx1, while HSPC co-express Runx1 and Fli1. There is indeed a clear shift in the relative expression of Fli1 compared to that of Runx1 between the two cellular stages (Figure 7—figure supplement 1C). In conclusion, our network analysis revealed that Fli1 and Runx1 are connected to 210 genes but with opposite correlations, which might be linked to the contrasting expression patterns of Fli1 and Runx1 and/or to the opposing functional properties of these TFs.

![Figure 7.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig7-v2.jpg)

**Figure 7.:** (A) Network built from gene correlations found in the Peirera dataset (Pereira et al., 2016). (B) Heatmap displaying Spearman correlations between the 210 genes found to be correlated to Runx1 and Fli1. The hierarchical clustering analysis gave us three groups of genes highlighted by three rectangles of different colors. The top GO term for each group of genes is indicated. See also Figure 7—figure supplement 1 and Supplementary file 9.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) GO term enrichment analysis of the genes correlated with Fli1 and Runx1. The color code matches the gene clusters from Figure 7B. (B) Heatmap displaying hierarchical clustering of the 210 genes correlated with Fli1 and Runx1. On top of the heatmap, the expression level of Fli1 and Runx1 is indicated (color gradient indicates log2 of gene expression). On the left of the heatmap, the DNA occupancy of Fli1 (F_ChIP) or Runx1 (R_ChIP) on the 210 genes is indicated (orange indicates Runx1 target genes and green Fli1 target genes). (C) Box plot showing the expression of Fli1 (green) and Runx1 (orange) in the Endo and HSPC populations isolated by Pereira et al. (2016)). The top and bottom box edges correspond to the first and third quartiles. The black line inside the box represents the median. The top and bottom whisker lines mark the maximum and minimum values of the data set, respectively.

### Gain of function analysis reveals a functional balance between Gata2/Runx1 and Erg/Fli1 TFs during the endothelial to hematopoietic transition

To find out whether Runx1 and Fli1 have opposite functional effects on the cell fate decisions occurring during EHT, we re-examined our i1TF gain-of-function analysis (Figure 3—figure supplement 5 and Figure 4B). According to these results, we identified two main groups of TFs. The first one includes Fli1 and Erg while the second one includes Runx1 and Gata2. Indeed, in +dox condition, iFli1 and iErg both displayed an increase in Endo population as well as Pre-HSPCs population, although at much lower level than with i8TFs (Figure 4B). By contrast, iRunx1 and iGata2 cells showed an increased frequency in the EryPCs_II population and a decrease in the MyePCs population in the +dox condition (Figure 4B). This result is consistent with the hypothesis that some of the eight TFs have opposing effects.

We next evaluated the functional consequences of the removal of Runx1/Gata2 or Erg/Fli1 from the 8TFs construct. We hypothesized that removing Runx1 and Gata2 would enhance the endothelial cell fate, whereas removing Erg and Fli1 would increase the hematopoietic cell fate. We consequently generated two additional ESC lines (Figure 8A). The first, i6TFs, contains 6TFs that are also found in i8TFs but is without Erg and Fli1. The second, i5TFs, lacks Runx1, Gata2 as well as Cbfb, crucial partner of Runx1. We performed ESC differentiation of these cell lines in the same way as before and analyzed the consequences of the overexpression of these two sets of TFs. Interestingly, the overexpression of the five TFs partly recapitulated the effect of overexpressing the eight TFs and led to a clear increase of the frequency of VE-cad+ CD41+ (Figure 8B). Remarkably, the frequency of the VE-Cad+ CD41– population was significantly increased too, in stark contrast to what we observed with the eight TFs (Figure 3A and Figure 8B). Consistent with this result, there was a clear decrease of the number of round cells formed during the BL-CFC assay (Figure 8C). By contrast, the overexpression of the six TFs only had a minor impact on the expression pattern of VE-cad and CD41 (Figure 8B). However, there was a clear increase of round hematopoietic cells as shown by image analysis, suggesting an enhancement of blood cell formation (Figure 8C). The observed impact of the induction on the number of round cells was confirmed specifically with endothelial cells isolated at day 1 BL-CFC and cultured for two days in the presence of doxycycline in HE medium (Figure 8D and Figure 8—figure supplement 1A). In addition, sc-q-RT-PCR performed on the i5TFs and i6TFs confirmed this duality (Figure 8E and Figure 8—figure supplement 1B). The i5TFs showed a decrease of EryPCs_I hematopoietic progenitors that was associated with an increase in Endo and Pre-HSPC populations, whereas the i6TFs showed an increase in the EryPCs_II population of hematopoietic progenitors (Figure 8E and Supplementary file 10).

![Figure 8.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig8-v2.jpg)

**Figure 8.:** (A) Scheme showing the i5TFs and i6TFs constructs used to generate the two inducible ESC lines missing Runx1, Gata2 and Cbfb, or Fli1 and Erg (respectively). (B) Representative FACS plots of VE-Cad, cKit and CD41 expression following three days of BL-CFC culture of the indicated ESC lines (n = 3). (C) Graphs showing the average numbers of round cells counted per frame (n = 3) in a 48 hr time course for the indicated ESC lines. Error bars represent standard deviations. (D) Representative pictures taken two days after HE culture of sorted VE-Cad+ CD41– (Endo) cells for the indicated cell lines. Round cells correspond to blood cells. The scale bar corresponds to 100 μm. (E) Bar graphs displaying the sc-q-RT-PCR results for the i6TFs and i5TFs ESC lines. See also Figure 8—figure supplement 1, Supplementary files 1, 10 and 11.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** (A) Graphs showing the average numbers of round cells counted per frame (n = 3) in a 48 hr time course of HE culture for the indicated cell lines. Error bars represent standard deviations. (B) Hierarchical clustering showing the sc-q-RT-PCR results for 95 genes on the i5TFs and i6TFs cell lines after three days of BL-CFC culture. Six major subpopulations were defined according to the intersection of the red dotted line with the dendrogram in the upper part of the heatmap. See also Supplementary file 11.

In conclusion, these results suggest that Fli1 and Erg on one side and Runx1 and Gata2 on the other side have opposing effects on the cell-fate decisions in hematopoiesis leading to the formation of Pre-HSPCs.

## Discussion

In this study, we used single-cell transcriptomics to define three main populations in the embryonic vasculature during blood formation: endothelial cells, pre-hematopoietic stem/progenitor cells and hematopoietic stem/progenitor cells. While these results were initially obtained with a single batch of embryos, all key patterns were reproduced in a separate batch in an additional study (Morgan Oatley, unpublished results). Despite slight timing differences, there were strong similarities in gene expression between the yolk sac and the AGM EHT, suggesting a similar process in both sites. However, due to the blood circulation, we cannot rule out cellular exchange between these two sites.

Bulk ChIP-seq analyses have suggested that Erg, Fli1, Tal1, Lyl1, Lmo2, Runx1 and Gata2 work together as a heptad (Wilson et al., 2010). Here, we show for the first time that the heptad genes are specifically co-expressed at the single-cell level within the Pre-HSPCs, and that this combination was not found in any other population along the transition. This specific co-expression may be conserved in the human species, as it was shown recently in the in vitro human EHT model system that the intermediate population between endothelial and blood cells co-expresses Runx1, Lyl1, Tal1, Gata2, Erg and Fli1 (Lmo2 was not assessed) at the single-cell level (Guibentif et al., 2017) similarly to the Pre-HSPC population that we described. In contrast to Guibentif et al. (2017), we investigated the functional meaning of the co-expression of these transcription factors. We showed that their enforced expression, together with that of Cbfb, during hematopoietic differentiation gave rise to Pre-HSPCs in culture. This suggests that the co-expression of the heptad genes is necessary for cells to reach the transient Pre-HSPCs stage before pursuing the transition.

These findings are consistent with the hypothesis of the existence of a heptad protein complex. Surprisingly, only ten percent of the differentially expressed genes are heptad targets and only ten percent of the heptad targets are differentially expressed. This suggests that the gene expression changes that we observed were not a direct consequence of the binding of the eight TFs complex at the regulatory elements of these genes. This implies that the formation of Pre-HSPCs is probably due to a combination of individual functions acting on the GRNs rather than to the sole action of an eight-protein complex.

To define these GRNs, we developed a bioinformatics pipeline for sc-RNA-seq data. We characterized the tight relationships involved in the formation of Pre-HSPCs, thereby giving directionality to the protein–DNA interactions previously identified by ChIP-seq (Goode et al., 2016; Wilson et al., 2010). Network analyses of the Pereira dataset (Pereira et al., 2016) together with our in vitro results revealed a new and unexpected opposite relationship between Runx1 and Fli1 functions. In addition, this network suggests that Gata2 and Lmo2 might act as cooperative co-regulators with Runx1 and Fli1, respectively (Figure 7A).

On the basis of our data and what is known in the literature, we propose the following model (Figure 9). Initially, the endothelial cell fate program is driven by Erg and Fli1, both ETS transcription factors, which is consistent with our functional analyses (Figure 3—figure supplement 5D and Figure 4) and studies published before (Asano et al., 2010; McLaughlin et al., 2001). In addition, Wilson et al. (2010) showed that more than 90% of the loci targeted by Fli1 are also targeted by Erg in the HPC7 cell line, suggesting functional redundancy. Then, the expression of Runx1 commenses and this — along with the expression of Gata2, which has pro-hematopoietic function — initiates the hematopoietic transcriptional program . Previous data support this functional interaction as Runx1+/−::Gata2+/− compound heterozygous embryos are not viable due to their severe hematopoietic defects, reinforcing the notion that the two proteins are involved in the same biological process (Wilson et al., 2010). At this intermediate Pre-HSPCs stage, endothelial genes are progressively downregulated as shown by our data. As Fli1 and Erg gene expression remain stable between the Endo and the Pre-HSPCs stages, this could be explained by a functional switch for these factors in favor of the hematopoietic cell fate and a decrease in the fraction dedicated to the maintenance of the endothelial program at the single-cell level. Specifically, Fli1 may be involved both in endothelial and hematopoietic gene expression depending on the cellular context. Indeed, in presence of Runx1, Fli1 could potentially activate common target genes such as Gfi1 and Gfi1b, which are involved in the repression of endothelial gene expression (Lancrin et al., 2012; Thambyrajah et al., 2016; Wilson et al., 2010). Alternatively (or concomitantly), Runx1 and Fli1 could bind together on endothelial gene loci as shown for Sox17 (Lichtinger et al., 2012) and repress their expression. On the other hand, Fli1 could switch its function upon physical interaction with Runx1, as shown during megakaryocytic differentiation where there is a synergistic transcriptional activation upon Fli1–Runx1 interaction (Huang et al., 2009).

![Figure 9.](https://cdn.elifesciences.org/articles/29312/elife-29312-fig9-v2.jpg)

**Figure 9.:** Proposed model for the dynamical function of transcription factors during the endothelial to hematopoietic transition. The upper blue arrow section shows the balance between transcription factors along the transition. The middle section indicates the gene expression levels for the two sets of transcription factors. In the lower blue arrow section, a possible mechanism for the functional switch of Erg/Fli1 in presence of Runx1/Gata2 is depicted. During the transition, epigenetically closed hematopoietic gene loci are progressively opened and activated in the presence of Runx1/Gata2 together with Fli1/Erg while the endothelial loci are progressively closed through Gfi1 and Gfi1b transcriptional repression. The DNA-binding data combined with single-cell GRN analysis suggests a dual function for Fli1 that is dependent on the cellular context (see main text for full description).

At the end of the EHT, in the HSPCs, the endothelial program is completely suppressed along with the expression of Erg. At this development stage, Fli1 is fully dedicated to the hematopoietic cell fate program and works with Runx1 to carry on blood cell development. This is supported by the observation that almost all the Runx1 target genes specific to the HSPCs are also bound by Fli1 (Supplementary file 9).

In conclusion, our work gives an important insight into the switch between endothelial and hematopoietic cell fates that is required for blood cell formation. We have identified the Pre-HSPCs as the pivotal stage in this process, at which a competition between developmental programs takes place at the single-cell level. The expression of the heptad of TFs is directly linked to this transitional stage. The balance of activity of Erg, Fli1, Gata2 and Runx1 appears to have the most important role in the EHT, whereas the Tal1/Lmo2/Lyl1 axis might have an essential role in priming it. Indeed, Tal1 acts as a repressor of alternative cellular programs such as the cardiac lineage and is actively needed to initiate the EHT (Lancrin et al., 2009; Org et al., 2015). In this context, our single-cell transcriptomics approach allowed us to shed light on an unexpected change in Fli1 activity as a consequence of Runx1 expression. This appears to be a critical process for the proper completion of the EHT. Conditions reinforcing the interaction between Runx1 and Fli1 would probably help to tilt the balance towards the hematopoietic cell fate. Likewise, preventing the Fli1–Runx1 interaction could potentially impair the formation of blood cells from endothelium.

More generally, a dual competing function for a unique transcription factor might be a key process for other developmental transitions such as the epithelial to mesenchymal transition. The bioinformatics approach that we have used in this work could be readily applicable to the study of other developmental processes and could help to address this type of question. Finally, the discrepancy observed between bulk and single-cell analyses in this work could also exist in other studies of TF complexes, which could prompt researchers in different fields to revisit previous assumptions using our approach.

## Materials and methods

### Experimental model and subject details

#### Animals

C57BL/6 N, Gfi1:GFP (Yücel et al., 2004) and Gfi1b:GFP (Vassen et al., 2007) mouse lines were used. Gfi1+/GFP and Gfi1b+/GFP were crossed with each other to generate Gfi1+/GFPGfi1b+/GFP animals. These animals were then used for timed mating to generate Gfi1GFP/GFPGfi1bGFP/GFP double-knockout embryos. Timed mating was set up and the morning of vaginal plug detection was considered day 0.5. Embryos were staged according to morphological properties. All experiments were performed in accordance with the guidelines and regulations defined by the European and Italian legislations (Directives 2010/63/EU and DLGS 26/2014, respectively). All mice were bred and maintained at the EMBL Rome Mouse Facility in accordance with European and Italian legislations (EU Directives 634/2010 and DLGS 26/2014, respectively).

#### Cell lines

##### Generation of inducible ESC lines

All doxycycline-inducible ESC lines were generated using the inducible cassette exchange method described previously (Iacovino et al., 2011; Vargel et al., 2016). For iCbfb, iRunx1, iLmo2, iGata2 and iFli1 ESC lines, the transcription factor coding sequences were tagged in 5’ with an 8His-tag and amplified by PCR from differentiated ESC cDNA. The 8His-tagged coding sequences were then inserted into a pGEM-t-easy before cloning into the p2lox plasmid. For iTal1, iLyl1 and iErg, the 8His-tagged coding sequences were synthetized and cloned into a pUC57 Simple by the GenScript Gene Synthesis Service (http://www.genscript.com/ gene_synthesis.html). The 8His-tagged coding sequences were then cloned from the pUC57 Simple into the p2lox plasmid. For each of the generated p2lox plasmids, a Kozak sequence was then added at the start codon by PCR cloning. The subsequent p2lox plasmids were used to transfect the A2lox.Cre ESC line and to generate the eight single-factor inducible ESC line as previously described (Vargel et al., 2016). For the i8TFs ESC line, three individual constructs were synthetized and cloned into a pUC57 plasmid by the GenScript Gene Synthesis Service. Construct one was composed of the coding sequence for V5-Erg-T2A-V5-Lmo2. Construct two was composed of the coding sequence for HA-Tal1-T2A-cmyc-Fli1-T2A-FLAG-Lyl1-T2A. Construct three was composed of the coding sequence for FLAG-Runx1-T2A-FLAG-Cbfb-T2A-HA-Gata2-T2A. All three constructs were flanked by a start codon and two stop codons, together with the proper restriction sites for cloning into the p2lox plasmid, in order to allow their individual use. They also contain specific restriction sites for their excision, the addition of any of the other constructs, or the removal of any of the factor sequences. Construct one together with the start codon and two stop codons was cloned into the p2lox plasmid. Then, Construct two was added between the start codon and Construct one by classic cloning. Finally, Construct three was added between the start codon and Construct two to obtain the p2lox-8TFs. This plasmid was then transfected into the A2lox.Cre ESC line for the generation of the i8TFs. For the i5TFs, the intermediate p2lox construct containing Construct one and Construct two was used to generate the ESC line. For the i6TFs, V5-Erg and cmyc-Fli1 were successively excised from the p2lox-8TFs by classic cloning to generate the p2lox-6TFs used for the generation of the inducible ESC lines. The empty ESC line was generated using the basic p2lox plasmid and following the same procedure. For each inducible ESC line, a clone was selected based on the induction of the transcript expression measured by qPCR and validated by western blot analysis.

##### Identification of cell lines

All cell lines used in this work were mESC lines. The Runx1+/hCD4 mESC line was generated in the group of Georges Lacaud by the corresponding author, Christophe Lancrin (Sroczynska et al., 2009a). All A2lox.Cre-derived mESC lines were generated from the A2lox.Cre mESC line, which was a gift from Michael Kyba who produced it in his laboratory (Iacovino et al., 2011). All A2lox.Cre-derived mESC lines were generated in our laboratory as described in the section ‘Generation of inducible ESC lines’. All ESC lines had proper stem cell morphology and were able to give rise to blood and endothelial cells after in vitro differentiation (Figure 1D, Figure 3, Figure 3—figure supplements 1 and 5, Figure 8 and Figure 8—figure supplement 1A). All the inducible mESC lines were verified by western blots and qPCR analysis (Figure 2, Figure 3—figure supplement 5, Figure 4 and Figure 8—figure supplement 1B).

All cell lines used in this manuscript were tested negative for mycoplasma contamination.

##### Maintenance and differentiation of ESC lines

Growth and differentiation of ESCs were performed as previously described (Sroczynska et al., 2009b). Briefly, ESCs were maintained on feeders in an ESC culture medium made of KnockOut DMEM (GIBCO) (supplemented with 1% Pen/Strep [GIBCO], 1% L-Glutamine [GIBCO] and 1% NEAA [GIBCO]), 15% FBS (PAA), 0.0024% 1 mg/ml LIF (The Protein Expression and Purification Core Facility, EMBL-Heidelberg) and 0.24% 50 mM 2-mercaptoethanol (GIBCO). For differentiation, ESCs were seeded on gelatin-coated plates (0.1% gelatin [BDH] in PBS for 20 min) for one day in the normal ESC culture medium and then for one day in a medium similar to the ESC medium but containing IMDM (Lonza) instead of the KnockOut DMEM and without NEAA supplement.

To obtain embryoid bodies (EBs), cells were subsequently harvested and cultured in petri dishes at a density of 0.3 × 106 cells per 10 cm2 dish with an EB medium made of IMDM (Lonza) (supplemented with 1% Pen/Strep [GIBCO] and 1% L-glutamine [GIBCO]), 0.6% transferrin (Roche, Italy), 0.039% MTG (Sigma) and 50 mg/µl ascorbic acid (Sigma). After 3–3.25 days, EBs were harvested and Flk1+ cells were sorted using MACS MicroBead Technology (Miltenyi Biotec). For hemangioblast differentiation, Flk1+ cells were then cultured on gelatin-coated plates at a density of 0.01 × 106 cells per cm2 in a medium made of IMDM (Lonza), 1% Pen/Strep (GIBCO), 1% L-glutamine (GIBCO), 10% FBS (PAA), 0.6% transferrin (Roche), 0.039% MTG (Sigma), 0.5% ascorbic acid (Sigma), 15% D4T supernatant (EMBL-Monterotondo), 0.05% VEGF (10 µg/ml) (R and D) and 0.1% IL-6 (10 µg/ml) (R and D). During the hemangioblast differentiation, the cell population could be sorted and further cultured in hemogenic endothelium culture conditions. For this purpose, sorted cells were seeded on gelatin-coated plates at a density of 0.015 × 106 cells per cm2 in a specific medium made of IMDM (Lonza), 1% Pen/Strep (GIBCO), 1% L-glutamine (GIBCO), 10% FBS (PAA), 0.6% transferrin (Roche), 0.039% MTG (Sigma), 0.5% ascorbic acid (Sigma), 0.0024% LIF (EMBL-Heidelberg), 0.25% SCF (20 µg/ml) (R and D), 0.1% oncostatin M (10 µg/ml) (R and D) and 0.01% bFGF/FGF2 (10 µg/ml) (R and D). To pursue the differentiation with a hematopoietic progenitor assay, cells were collected three days after Flk1 sort from the hemangioblast (or the hemogenic endothelium) culture and plated at a density of 3.3 × 103 cells per cm2 in a medium made of IMDM (Lonza), 1% Pen/Strep (GIBCO), 1% L-glutamine (GIBCO), 55% of 0.5 g/ml methylcellulose (VWR), 15% PDS (Antec), 10% PFMH-II (GIBCO), 0.6% transferrin (Roche), 0.039% MTG (Sigma), 0.5% ascorbic acid (Sigma), 0.5% SCF (20 µg/ml) (R and D), 0.1% IL-3 (25 µg/ml) (R and D), 0.1% GM-CSF (25 µg/ml) (R and D), 0.04% IL-11 (12.5 µg/ml) (R and D), 0.2% EPO (10 µg/ml) (R and D), 0.2% IL-6 (5 µg/ml) (R and D), 0.2% TPO (12.5 µg/ml) (R and D) and 0.05% MCSF (10 µg/ml) (R and D). Colonies were counted for three replicates after 10–12 days.

For doxycycline treatment of the inducible ESC line, doxycycline (Sigma) was added directly to the culture medium at a final concentration of 1 µg/ml for 24 or 48 hr.

### Method details

#### Embryo dissection

Yolk sac and AGM dissections were performed as described before (Bertrand et al., 2005) and Robin and Dzierzak, 2005). Briefly, pregnant mice were killed by cervical dislocation between E9.0 and E11 of gestation. Uterine horns were collected; the maternal tissues were removed as well as the placenta to isolate the embryos. The yolk sac was torn gently and separated from the embryo proper by tearing off the umbilical and vitelline arteries. Then, the somite pairs of the embryos were counted to determine their developmental stage. To isolate the AGM, the head, tail, limb buds, ventral organs and somites were removed. Yolk sac and AGM samples from the same embryonic development stage were pooled together in the same tube. To generate single-cell suspension from the isolated tissues, AGM and yolk sac samples were subjected to collagenase (Sigma) treatment for 30 min. at 37°C. AGM and yolk sac cell suspensions were then used for flow cytometry.

#### Western blot analyses

ESCs were cultured for two passages on gelatin to remove MEFs before being treated with 1 µg/ml of doxycycline (Sigma) for 24 hr. For whole protein extracts, cells were harvested using TrypLE express (GIBCO), washed with PBS and lysed in RIPA buffer (Thermo Scientific) for 30 min at 4°C. Samples were then centrifuged for 5 min at high speed and pellets were discarded. Nuclear extracts were prepared using the Nuclear Extract kit (ActiveMotif) following the manufacturer's instructions. Protein concentration was measured using the Pierce BCA Protein Assay Kit (Thermo Scientific) and equal amounts of –dox and +dox protein samples were loaded onto NuPAGE Novex 10% or 12% Bis-Tris Protein gels (Life Technologies). Migration and wet transfer on a PROTRAN nitrocellulose membrane (PerkinElmer) were performed using the XCell SureLock Mini-Cell Electrophoresis System from Invitrogen. Membranes were stained with Ponceau S solution (Sigma) to control the transfer efficiency and protein amounts. The membranes were then washed with TBST (TBS [20 mM Tris-Base, 154 mM NaCl, pH 7.5], 0.1% Tween 20) and blocked with TBST +5% milk for 45 min at RT. Membranes were then incubated ON at 4°C with primary antibodies diluted in TBST +1% milk as follows: 1:2000 anti-FLAG (Sigma), 1:1000 anti-HA (Sigma), 1:2000 anti-V5 (Life Technologies), 1:5000 anti-Runx1 (Abcam), 1:5000 anti-Cbfb (Abcam), 1:2000 anti-Gata2 (Abcam), 1:2000 anti-Tal1 (Abcam), 1:2500 anti-Fli1 (Abcam), 1:5000 anti-Lyl1 (Abcam), 1:5000 anti-Erg (Abcam), 1:1000 anti-Lmo2 (Abcam), 1:2000 anti-His tag (Abcam), and 1:10000 anti-alpha-tubulin (Sigma) (the last being used as loading control). Following primary antibody incubation, the membranes were washed three times with TBST and incubated for 45 min with HRP-conjugated secondary antibodies diluted in TBST +1% nilk as follows: 1:10000 anti-Mouse HRP (GE Healthcare Life Sciences), 1:10000 anti-Rabbit HRP (Jackson) and 1:10000 anti-Rat HRP (GE Healthcare Life Sciences). The membranes were developed using the Amersham ECL Prime Western Blotting Detection Reagent (GE Healthcare Life Sciences).

#### Time-lapse photography

Cell differentiation cultures were imaged from the time of doxycycline addition. Phase-contrast time-lapse images were taken with the IncuCyte HD (Essen Biosciences) inside the incubator, every 15 min, three areas per well. Time-lapse videos were generated with the Fiji software (http://fiji.sc/Fiji) (Schindelin et al., 2012) using 10 frames per second. Images were analyzed by CellProfiler software (http://www.cellprofiler.org) (Kamentsky et al., 2011) to quantify the number of round cells with a customized pipeline written by Christian Tischer from the EMBL Heidelberg Advanced Light Microscopy Facility. For each time point, the average and standard deviation of counts from all three spots were calculated to make graphs with Microsoft Office Excel software. A detailed explanation on how time-lapse photography and image analysis were performed can be found at Bio-protocol (Bergiers et al., 2019)

#### Flow cytometry and cell sorting

Staining was done as described previously (Sroczynska et al., 2009b) and analyses were performed with a FACSCanto (Becton Dickinson) or a FACSAria (Becton Dickinson). Cell sorts were performed with a FACSAria (Becton Dickinson) or by using magnetic sorting (MACS MicroBead Technology, Miltenyi Biotec) and anti-APC MicroBeads (Miltenyi Biotech). The monoclonal rat anti-mouse antibodies used were anti-Mouse CD309 (FLK1) APC (Avas12a1, eBioscience), anti-Mouse CD41 PE (MWReg30, eBioscience), anti-Mouse cKit APC (2B8, eBioscience), and anti-Mouse CD144 (VE-Cadherin) eFluor 660 (eBioBV13, eBioscience). FACS data were analyzed using the FlowJo software (Tree Star, Inc.).

#### Cell-cycle assay

Cell-cycle assays were performed using the Click-iT Plus EdU Alexa Fluor 488 Flow Cytometry Assay kit from Molecular Probes following the manufacturer instructions. Briefly, cells from hemangioblast, or hemogenic endothelium, culture were treated with 10 µM of EdU for 1 hr. The cells were then harvested and stained with Ghost Dye Red 780 (Tonbo Biosciences) for live/dead staining before staining with cell surface marker antibodies (anti-Mouse CD41 PE [MWReg30, eBioscience] and anti-Mouse CD144 [VE-Cadherin] eFluor 660 [eBioBV13, eBioscience]). Stained cells were fixed and permeabilized, and the Click-IT reaction was performed following the manufacturer instructions. Finally, cells were stained with Hoechst for DNA labeling and analyzed with the FACSAria (Becton Dickinson). FACS data were analyzed using the FlowJo software (Tree Star, Inc.).

#### Apoptosis assay

Cells from hemangioblast culture were harvested and stained with anti-Mouse CD41 PE (MWReg30, eBioscience), anti-Mouse CD144 (VE-Cadherin) eFluor 660 (eBioBV13, eBioscience) and AnnexinV (eBioscience). Finally, cells were stained with Sytox Blue for DNA labeling and analyzed with the FACSAria (Becton Dickinson). FACS data were analyzed using the FlowJo software (Tree Star, Inc.).

#### Luciferase assay

Sequences from the two heptad peaks found in the Gpr56 locus (Wilson et al., 2010) were synthesized and cloned by the GenScript Gene Synthesis Service into a pGL4.10[luc2] reporter plasmid (Promega), with additional 50-bp sequences upstream and downstream to ensure proper peak coverage. The pGL4.74[hRluc/TK] Renilla reporter plasmid that was used to control for transfection efficiency was obtained from Promega. ESCs were plated on gelatin-coated plates (0.1% gelatin [BDH] in PBS for 20 min) and passaged twice to remove the feeders. Cells were then seeded in gelatin-coated 96-well plates at a density of 5,000 cells per well. Next day, the medium was changed and the cells were transfected with the Firefly luciferase reporter plasmids together with the Renilla luciferase reporter plasmid using the NanoJuice Transfection kit (Merck Millipore). After 24 hr, cells were treated with doxycycline (Sigma) for 24 hr and luciferase assay was performed using the Dual-Luciferase Reporter Assay System (Promega) and the POLARstar Omega device (BMG Labtech) following manufacturer's instructions.

#### mRNA microarray

Cells were collected and washed once with PBS. Total RNA was extracted with RNAeasy Plus Micro kit (Qiagen). Samples were then tested for quality with BioAnalyzer (Agilent) and their concentrations measured using Qubit (Life Technologies). They were hybridized on an Affymetrix GeneChip Mouse Gene 2.0 ST Array.

#### Single-cell quantitative RT-PCR

A maximum of 1 day prior to the experiment, 96-well plates (BioRad) were filled with 5 µl of 2x reaction mix from the CellsDirect One-Step qRT-PCR kit (Invitrogen). On the day of the experiment, cells were harvested and stained for FACS analysis. Cells from Anti-Mouse CD41 PE (MWReg30, eBioscience)/Anti Mouse CD144 (VE-cadherin) eFluor 660 (eBioBV13, eBioscience) staining were single-cell sorted in the pre-filled 96-well plates (BioRad) using the FACSAria system (Becton Dickinson). The plates were snap-frozen on dry ice immediately after sorting and stored at −80°C for a maximum of 1 week. To perform RT/Specific Target Amplification (RT/STA), 4 µl of a reaction mix — composed of 2.8 µl of Resuspension buffer, 0.2 µl of SuperScript III and Platinum Taq polymerase from the CellsDirect One-Step qRT-PCR kit (Invitrogen) and 1 µl of 500 nM outer primer mix (primer sequence list, see table below) — was added to each well. Plates were first incubated at 50°C for 15 min. followed by incubation at 95°C for 2 min. Then, they were incubated at 95°C for 15 s. followed by incubation at 60°C for 4 min. for 20 cycles. To prepare the sample mixes, 1/5x diluted cDNAs were mixed wiyj the loading reagent (Fluidigm) and SsoFastTM EvaGreen Supermix (Bio-Rad). In parallel, individual assay mixes were prepared as 5 μM inner primer mix, with DNA suspension buffer and the assay loading reagent (Fluidigm). After the priming of 96.96 dynamic array IFC (Fluidigm), the sample mixes and assay mixes were put together in the corresponding inlets and loaded into the chip. Finally, the chip was run in the Fluidigm Biomark HD system by using the Biomark Data Collection Software and the GE96 ×96PCR + Meltv2.pcl program.

To control for technical variation in our sc-qRT-PCR runs, we used the universal cDNA reverse transcribed by Random Hexamer: Mouse Normal Tissues (BioChain). It allowed us to detect consistently 93 out of our 95 genes of interest. A sample without DNA template was also run each time to test for unspecific PCR amplification.

The primer list is as follows:

<table>
  <thead>
    <tr>
      <th>Gene name</th>
      <th>Outer forward</th>
      <th>Outer reverse</th>
      <th>Inner forward</th>
      <th>Inner reverse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Acta2</td>
      <td>aggcaccactgaaccctaag</td>
      <td>cacagcctgaatagccacat</td>
      <td>ccaaccgggagaaaatgac</td>
      <td>atggcggggacattgaag</td>
    </tr>
    <tr>
      <td>Acvr1</td>
      <td>cgagtgctaatgatgatggctttccc</td>
      <td>cgtttcacagtggtcctcgttcc</td>
      <td>cgattccccgagtgtggaagatga</td>
      <td>cgattccccgagtgtggaagatga</td>
    </tr>
    <tr>
      <td>Acvr1b</td>
      <td>atgctgcgccatgaaaacatc</td>
      <td>tcgtgatagtcagagacaagccaca</td>
      <td>ttggctttattgctgctgaca</td>
      <td>tgggtccaggtgccattatc</td>
    </tr>
    <tr>
      <td>Acvr2a</td>
      <td>gctggcaagtctgcaggtga</td>
      <td>tcagaaatgcgtccctttgga</td>
      <td>acccatgggcaggttggta</td>
      <td>tttatagcaccctccaacacctctg</td>
    </tr>
    <tr>
      <td>Acvr2b</td>
      <td>gaagggctgctggctagatga</td>
      <td>agttgccttcgcagcagca</td>
      <td>tcaattgctacgacaggcagga</td>
      <td>aagtacacctgggggttctcctc</td>
    </tr>
    <tr>
      <td>Acvrl1</td>
      <td>cgaattgcccatcgtgacctcaa</td>
      <td>cgtggttgttgccgatatccaggta</td>
      <td>cgaagtcgcaatgtgctggtcaa</td>
      <td>cgaagtcgcaatgtgctggtcaa</td>
    </tr>
    <tr>
      <td>Adcy4</td>
      <td>cgatggtggcatcttgttcccta</td>
      <td>cgttcagcttgggttccttcagta</td>
      <td>cgacattcccacgcctggctgtc</td>
      <td>cgacattcccacgcctggctgtc</td>
    </tr>
    <tr>
      <td>Atp2a3</td>
      <td>cgaccattgtggctgcagtagaa</td>
      <td>cgtcccagaattgctgtgaggaa</td>
      <td>cgagagggcagggccatctaca</td>
      <td>cgagagggcagggccatctaca</td>
    </tr>
    <tr>
      <td>Bmp4</td>
      <td>cagccgagccaacactgtga</td>
      <td>tgggatgctgctgaggttga</td>
      <td>agtttccatcacgaagaacatctgg</td>
      <td>gaggaaacgaaaagcagagc</td>
    </tr>
    <tr>
      <td>Bmpr1a</td>
      <td>acgttcaccgaaagcccagcta</td>
      <td>tcgcggatgctgccatcaaagaa</td>
      <td>acgcgcaggacaatagaatgttg</td>
      <td>acgcgcaggacaatagaatgttg</td>
    </tr>
    <tr>
      <td>Bmpr2</td>
      <td>cagacggccgcatggagtat</td>
      <td>atgagccagacggcaagagc</td>
      <td>tgcttgtgatggagtattatcccaatg</td>
      <td>tacccaatcacttgtgtggagactca</td>
    </tr>
    <tr>
      <td>Cacna2d1</td>
      <td>acgccaatggttttagctggtgaca</td>
      <td>cgtgattggccagtgacgttgaa</td>
      <td>acgagcaagttcaatggacaaatgtg</td>
      <td>acgagcaagttcaatggacaaatgtg</td>
    </tr>
    <tr>
      <td>Cdh2</td>
      <td>atcaacaatgagactggggacatca</td>
      <td>cttccatgtctgtggcttgaa</td>
      <td>cactgtggcagctggtctgg</td>
      <td>attaacgtatactgttgcactttctctcg</td>
    </tr>
    <tr>
      <td>Cdh5</td>
      <td>cgacaccatcgccaaaagagagac</td>
      <td>cgtcttagcattctggcggttcac</td>
      <td>cgaggatttggaatcaaatgcacatcg</td>
      <td>cgaggatttggaatcaaatgcacatcg</td>
    </tr>
    <tr>
      <td>Cldn5</td>
      <td>tggcaggtgactgccttcct</td>
      <td>tgcatgtgcccggtactctg</td>
      <td>accacaacatcgtgacggcgcaga</td>
      <td>accacgcacgacatccacag</td>
    </tr>
    <tr>
      <td>Col4a2</td>
      <td>cgaccctggaagccctggattta</td>
      <td>cgttgtcttcccttaagtcccaaca</td>
      <td>cgatggcagggatgcctggt</td>
      <td>cgatggcagggatgcctggt</td>
    </tr>
    <tr>
      <td>Col4a5</td>
      <td>cgaggactctctgtggattggcta</td>
      <td>cgtatgaagggagcggaacgaa</td>
      <td>cgattcatgatgcatacaagtgcagga</td>
      <td>cgattcatgatgcatacaagtgcagga</td>
    </tr>
    <tr>
      <td>Ctnnb1</td>
      <td>aactcctgcacccaccatccca</td>
      <td>gttcccgcaaaggcgcatga</td>
      <td>tggcctctgataaaggcaactg</td>
      <td>tgctgggcaaagggcaag</td>
    </tr>
    <tr>
      <td>Dcaf12l1</td>
      <td>cgaaggcctccatggcaactac</td>
      <td>cgtggtggggagacccagaaaa</td>
      <td>cgagcaggcctctggagcta</td>
      <td>cgagcaggcctctggagcta</td>
    </tr>
    <tr>
      <td>Dpysl3</td>
      <td>cgaccattgggaaggacaacttcac</td>
      <td>cgtcggccacaaactggttttca</td>
      <td>cgaccatccctgaaggcaccaat</td>
      <td>cgaccatccctgaaggcaccaat</td>
    </tr>
    <tr>
      <td>Eng</td>
      <td>gcctgactttctgggactccagc</td>
      <td>tgctgaccacatgggctgtcac</td>
      <td>gccaggctgaagacactgacg</td>
      <td>tcatgccgcagctggagtag</td>
    </tr>
    <tr>
      <td>Enpp1</td>
      <td>cgaccatgaaaggaacggcatca</td>
      <td>cgtaatttcctggcttcggatgac</td>
      <td>cgatcagcggtcccgtgttt</td>
      <td>cgatcagcggtcccgtgttt</td>
    </tr>
    <tr>
      <td>Epo</td>
      <td>ggttgtgcagaaggtcccaga</td>
      <td>gggacaggccttgccaaact</td>
      <td>ctgagtgaaaatattacagtcccaga</td>
      <td>tatggcctgttcttccacctcca</td>
    </tr>
    <tr>
      <td>Epor</td>
      <td>tgaagtggacgtgtcggcag</td>
      <td>acagcgaaggtgtagcgcgt</td>
      <td>caaccgggcaggagggaca</td>
      <td>ccgccccgcaggttgctcagaa</td>
    </tr>
    <tr>
      <td>Eps8</td>
      <td>cgaaggctgccatgcctttcaa</td>
      <td>tcgtgctgttcctcgccacaaa</td>
      <td>acgctcctaatcaccaagtagataggaattatg</td>
      <td>acgctcctaatcaccaagtagataggaattatg</td>
    </tr>
    <tr>
      <td>Erg</td>
      <td>tcccgaagctacgcaaagaa</td>
      <td>tttggactgaggggtgaggtg</td>
      <td>tacaactaggccagatttaccttatga</td>
      <td>tgtggccggtccaggctgat</td>
    </tr>
    <tr>
      <td>Esam</td>
      <td>cgaagtctatgtctgcaaggctcaa</td>
      <td>cgtcccaacaaaagtgcccacaa</td>
      <td>cgacagagtgggctttgccaagt</td>
      <td>cgacagagtgggctttgccaagt</td>
    </tr>
    <tr>
      <td>Fam122b</td>
      <td>cgaagtttctccagctccttccc</td>
      <td>cgtaaatgtcttggattgagaacaggac</td>
      <td>cgacaaccagaggatttggaaagcaatg</td>
      <td>cgacaaccagaggatttggaaagcaatg</td>
    </tr>
    <tr>
      <td>Fbn1</td>
      <td>acgtggcggggaatgtacaaaca</td>
      <td>cgtcagagctgtgtagcagtaacca</td>
      <td>cgactgtcagcagctacttctgcaaat</td>
      <td>cgactgtcagcagctacttctgcaaat</td>
    </tr>
    <tr>
      <td>Fli1</td>
      <td>tgctgttgtcgcacctcagtt</td>
      <td>ttccttgacattcagtcgtgagga</td>
      <td>ctcagggaaagttcactgctggccta</td>
      <td>tggtctgtatgggaggttgtg</td>
    </tr>
    <tr>
      <td>Flrt2</td>
      <td>cgatgccgctctagcttcttcc</td>
      <td>cgtagtggagagcagcctaggaa</td>
      <td>cgaccggacccggttggatt</td>
      <td>cgaccggacccggttggatt</td>
    </tr>
    <tr>
      <td>Fmo1</td>
      <td>cgaaaccacgtgaattacggtgta</td>
      <td>tcgccttgatgctgggcttgata</td>
      <td>cgagctccagaagacaggactca</td>
      <td>cgagctccagaagacaggactca</td>
    </tr>
    <tr>
      <td>Gata1</td>
      <td>cctgtgcaatgcctgtggct</td>
      <td>tgcctgcccgtttgctgacaa</td>
      <td>gtatcacaagatgaatggtcagaacc</td>
      <td>cattcgcttcttgggccggatg</td>
    </tr>
    <tr>
      <td>Gata2</td>
      <td>aagcaaggctcgctcctg</td>
      <td>cacaggcattgcacaggtagt</td>
      <td>cagaaggccgggagtgtgtc</td>
      <td>gcccgtgccatctcgt</td>
    </tr>
    <tr>
      <td>Gdpd5</td>
      <td>cgaacttccgacaactcccatacc</td>
      <td>cgttgccgatgatgaggctgaa</td>
      <td>cgatttctcgggtgccttctcca</td>
      <td>cgatttctcgggtgccttctcca</td>
    </tr>
    <tr>
      <td>Gfi1</td>
      <td>cgagagatgtgcggcaagacc</td>
      <td>cgtagcgtggatgacctcttgaa</td>
      <td>cgagtgagcctggagcaacacaa</td>
      <td>cgagtgagcctggagcaacacaa</td>
    </tr>
    <tr>
      <td>Gfi1b</td>
      <td>cgatggacacttaccactgtgtca</td>
      <td>cgtaggttttgccacagacatcac</td>
      <td>cgaagtgcaacaaggtgttctcc</td>
      <td>cgaagtgcaacaaggtgttctcc</td>
    </tr>
    <tr>
      <td>Gpr126</td>
      <td>cgactgtgcagccacttcactca</td>
      <td>cgtggcagatattccgcacccaata</td>
      <td>cgatggagttctgatggatcttcc</td>
      <td>cgatggagttctgatggatcttcc</td>
    </tr>
    <tr>
      <td>Gria4</td>
      <td>cgacgcccatggtgacgaaacta</td>
      <td>cgtgccattaccaagacaccatcgta</td>
      <td>acgatggatcgctggaagaaactaga</td>
      <td>acgatggatcgctggaagaaactaga</td>
    </tr>
    <tr>
      <td>Hbb-bh1</td>
      <td>gagctgcactgtgacaagcttca</td>
      <td>ggggtgaattccttggcaaaa</td>
      <td>tggatcctgagaacttcaagc</td>
      <td>gagtagaaaggacaatcaccaaca</td>
    </tr>
    <tr>
      <td>Itga2b</td>
      <td>ttccaaccagcgcttcacct</td>
      <td>tgctcggatccccatcaaac</td>
      <td>cgacaacagcaacccagtgttt</td>
      <td>gcccacggctaccgaatatc</td>
    </tr>
    <tr>
      <td>Itgam</td>
      <td>agcaggggtcattcgctacg</td>
      <td>cagctggcttagatgcgatgg</td>
      <td>attggggtgggaaatgccttc</td>
      <td>gtcgagctctctgcgggact</td>
    </tr>
    <tr>
      <td>Itgb3</td>
      <td>tcctccagctcattgttgatgc</td>
      <td>aggcaggtggcattgaagga</td>
      <td>acgggaaaatccgctctaaa</td>
      <td>agtgacagttcttccggcaggt</td>
    </tr>
    <tr>
      <td>Kdr</td>
      <td>tgtggggcttgatttcacctg</td>
      <td>tcgccacagtcccaggaaag</td>
      <td>cactctccaccttcaaagtctcatca</td>
      <td>tttcacatcccggtttacaatcttc</td>
    </tr>
    <tr>
      <td>Kit</td>
      <td>ctggctctggacctggatga</td>
      <td>cctggctgccaaatctctgtg</td>
      <td>tgctgagcttctcctaccaggtg</td>
      <td>atacaattcttggaggcgaggaa</td>
    </tr>
    <tr>
      <td>Lad1</td>
      <td>cgacctctttgagaaggagctgtca</td>
      <td>cgtcctgggtcttgctgatcca</td>
      <td>cgaggccagaaccgcacagaac</td>
      <td>cgaggccagaaccgcacagaac</td>
    </tr>
    <tr>
      <td>Lat</td>
      <td>cgatgctgcctgacagtagtcc</td>
      <td>cgttcactctcaggaacattcacgta</td>
      <td>cgactgccgtccctgttgtct</td>
      <td>cgactgccgtccctgttgtct</td>
    </tr>
    <tr>
      <td>Lgr5</td>
      <td>cgagcaacaacatcaggtcaatacc</td>
      <td>cgtcaggcaaatgctgaaaagca</td>
      <td>cgaggagcgagcgttcgtagg</td>
      <td>cgaggagcgagcgttcgtagg</td>
    </tr>
    <tr>
      <td>Lmo2</td>
      <td>tcggccatcgaaaggaagag</td>
      <td>gcggtcccctatgttctgct</td>
      <td>ctggacccgtctgaggaacc</td>
      <td>gcagccaccacatgtcagca</td>
    </tr>
    <tr>
      <td>Lyl1</td>
      <td>gctgaagcgcagaccaagccat</td>
      <td>gctcacggctgttggtgaacact</td>
      <td>gtgagctggacttggctgacg</td>
      <td>ccgagccaccttctggggttg</td>
    </tr>
    <tr>
      <td>Meis2</td>
      <td>cgacccgtacccttcagaagaacagaa</td>
      <td>cgttggtcaatcatgggctgcacta</td>
      <td>cgagaaacagttagcgcaagacac</td>
      <td>cgagaaacagttagcgcaagacac</td>
    </tr>
    <tr>
      <td>Met</td>
      <td>cgagatcattggtgcggtctcaa</td>
      <td>tcgactcttgcgtcatagcgaac</td>
      <td>cgagtagttttgttattatccgggctctt</td>
      <td>cgagtagttttgttattatccgggctctt</td>
    </tr>
    <tr>
      <td>Mpo</td>
      <td>tggccctagacctgctgaagag</td>
      <td>ttgacacggacaacagattcagc</td>
      <td>aagctgcagcccctgtgg</td>
      <td>gagcaggtgtcaacacatctgtaa</td>
    </tr>
    <tr>
      <td>Myb</td>
      <td>cgagtggcagaaagtgctgaacc</td>
      <td>cgttgcttggcaataacagaccaac</td>
      <td>cgacatcaaaggtccctggaccaaa</td>
      <td>cgacatcaaaggtccctggaccaaa</td>
    </tr>
    <tr>
      <td>Myom1</td>
      <td>cgattccgtgtacgtgctgtcaa</td>
      <td>cgttccgtcatcatccacactcac</td>
      <td>acgccaggcaggcgttggaaag</td>
      <td>acgccaggcaggcgttggaaag</td>
    </tr>
    <tr>
      <td>Notch1</td>
      <td>cgaccaaccctgtcaacggcaaa</td>
      <td>cgtatttgcctgcgtgctcacaa</td>
      <td>cgatgcccctcggggtaca</td>
      <td>cgatgcccctcggggtaca</td>
    </tr>
    <tr>
      <td>Npr1</td>
      <td>cgacagatttgtgggagcttgtacc</td>
      <td>cgtcgaaacatccagtccagggta</td>
      <td>cgagaccctcccaacatctgtatc</td>
      <td>cgagaccctcccaacatctgtatc</td>
    </tr>
    <tr>
      <td>Palld</td>
      <td>cgagcttcgcttcaaggaggac</td>
      <td>cgttctggctcctggatgttgaa</td>
      <td>cgacttctgaacaatggccaacc</td>
      <td>cgacttctgaacaatggccaacc</td>
    </tr>
    <tr>
      <td>Pcdh12</td>
      <td>cgatggctgcttttgcggaac</td>
      <td>tcgtggtttggtttgggctggaa</td>
      <td>cgaggaacccggtggagga</td>
      <td>cgaggaacccggtggagga</td>
    </tr>
    <tr>
      <td>Pdzd2</td>
      <td>cgacaacttggaaagccccaaac</td>
      <td>cgtgtccccatttcgtaccatca</td>
      <td>cgaagggcaacagtaaaatgaaactcaag</td>
      <td>cgaagggcaacagtaaaatgaaactcaag</td>
    </tr>
    <tr>
      <td>Pecam1</td>
      <td>tgcggtggttgtcattggag</td>
      <td>ctggacatctccacgggttt</td>
      <td>gtcatcgccaccttaatagttgcag</td>
      <td>tgtttggccttggctttcctc</td>
    </tr>
    <tr>
      <td>Plcd1</td>
      <td>cgatggcttctccagtcctagca</td>
      <td>cgtcccacgttatggcggacaa</td>
      <td>cgatctgggcaggcattctatgagatgg</td>
      <td>cgatctgggcaggcattctatgagatgg</td>
    </tr>
    <tr>
      <td>Ppia</td>
      <td>cgaccgactgtggacagctctaa</td>
      <td>cgtagtgagagcagagattacaggac</td>
      <td>cgatttcttttgacttgcgggcatt</td>
      <td>cgatttcttttgacttgcgggcatt</td>
    </tr>
    <tr>
      <td>Ppp1r16b</td>
      <td>cgagcgtgtggatgtgaaggac</td>
      <td>cgtgatgtcctggcactgagacta</td>
      <td>cgaatggctgggagcctct</td>
      <td>cgaatggctgggagcctct</td>
    </tr>
    <tr>
      <td>Ptprb</td>
      <td>acgccaagagcggcaattatgca</td>
      <td>cgttgcacccaggacacctttaa</td>
      <td>cgaccactccttcaccgaggaa</td>
      <td>cgaccactccttcaccgaggaa</td>
    </tr>
    <tr>
      <td>Ptprc</td>
      <td>ggcttcaaggaacccaggaaata</td>
      <td>tgacaataactgtggccttttgctc</td>
      <td>attgctgcacaagggccccgggatg</td>
      <td>cagatcatcctccagaagtcatcaa</td>
    </tr>
    <tr>
      <td>Ptprm</td>
      <td>cgacagacctcctccaacacatca</td>
      <td>tcgtctcgtctttcttagcagagtcc</td>
      <td>cgatcagatgaagtgcgctgag</td>
      <td>cgatcagatgaagtgcgctgag</td>
    </tr>
    <tr>
      <td>Ramp2</td>
      <td>tcccactgaggacagccttg</td>
      <td>tccttgacagagtccatgcaa</td>
      <td>tcaaaagggaagatggaagactacga</td>
      <td>tcttgtactcataccagcaaggtaggaca</td>
    </tr>
    <tr>
      <td>Runx1</td>
      <td>cgaactactcggcagaactgagaa</td>
      <td>cgtacggtgatggtcagagtgaa</td>
      <td>cgaatgctaccgcggccatg</td>
      <td>cgaatgctaccgcggccatg</td>
    </tr>
    <tr>
      <td>Samd4</td>
      <td>cgaacagctccgtccagaagac</td>
      <td>cgtactccagcctattgttgatgtca</td>
      <td>acgtcgctgcccgtgcata</td>
      <td>acgtcgctgcccgtgcata</td>
    </tr>
    <tr>
      <td>Sash1</td>
      <td>cgattgatctcactgaggagcccta</td>
      <td>tcgccatgttggtggcaacatcc</td>
      <td>cgactgataagcatggccgttgt</td>
      <td>cgactgataagcatggccgttgt</td>
    </tr>
    <tr>
      <td>Serpine1</td>
      <td>aaaacccggcggcagatcca</td>
      <td>cttgttccacggccccatga</td>
      <td>gatgctatgggattcaaagtcaa</td>
      <td>ccttggagagctggcggagggcatga</td>
    </tr>
    <tr>
      <td>Sfpi1</td>
      <td>gtgggcagcgatggagaaag</td>
      <td>tgcagctctgtgaagtggttctc</td>
      <td>atagcgatcactactgggatttctcc</td>
      <td>gggaagttctcaaactcgttgttg</td>
    </tr>
    <tr>
      <td>She</td>
      <td>cgaacatggaaccgtacgatgca</td>
      <td>tcgtcacagtctcccctggttca</td>
      <td>acgtaacagaaatcagacgccgtggtt</td>
      <td>acgtaacagaaatcagacgccgtggtt</td>
    </tr>
    <tr>
      <td>Sla</td>
      <td>cgacgaatcttccgtcttcccaac</td>
      <td>tcgggtgagcacacagcatagac</td>
      <td>cgaactggtactacatctcaccaagg</td>
      <td>cgaactggtactacatctcaccaagg</td>
    </tr>
    <tr>
      <td>Smad1</td>
      <td>tctcagcccatggacacgaa</td>
      <td>caccagtgttttggttcctcgt</td>
      <td>atgatggcgcctccactgc</td>
      <td>gcaactgcctgaacatctcctc</td>
    </tr>
    <tr>
      <td>Smad2</td>
      <td>tgctctccaacgttaaccgaaa</td>
      <td>tcagcaaacacttccccacct</td>
      <td>gccactgtagaaatgacaagaagaca</td>
      <td>tgtaatacaagcgcactccccttc</td>
    </tr>
    <tr>
      <td>Smad3</td>
      <td>ccaatgtcaaccggaatgcag</td>
      <td>tgaggcactccgcaaagacc</td>
      <td>cgtggaacttacaaggcgaca</td>
      <td>cccctccgatgtagtagagc</td>
    </tr>
    <tr>
      <td>Smad4</td>
      <td>ttgcctcaccaccaaaacg</td>
      <td>tggaatgcaagctcattgtga</td>
      <td>ccatcttcagcaccacccgccta</td>
      <td>tggccagtaatgtccaggatg</td>
    </tr>
    <tr>
      <td>Smad5</td>
      <td>aaccatggattcgaggctgtg</td>
      <td>tgacgtcctgtcggtggtactc</td>
      <td>tgagctcaccaagatgtgtacc</td>
      <td>gctccccagcccttgacaaa</td>
    </tr>
    <tr>
      <td>Smad6</td>
      <td>ttctcggctgtctcctcctgac</td>
      <td>ttcacccggagcagtgatga</td>
      <td>gtacaagccactggatctgtccgatt</td>
      <td>ggagttggtggcctcggttt</td>
    </tr>
    <tr>
      <td>Smad7</td>
      <td>ggaagatcaaccccgagctg</td>
      <td>tgagaaaatccattgggtatctgga</td>
      <td>tgtgctgcaacccccatcac</td>
      <td>aaggaggagggggagactcta</td>
    </tr>
    <tr>
      <td>Smad9</td>
      <td>gcacgattcggatgagctttg</td>
      <td>tgcagcggtccatgaagatg</td>
      <td>gaagggctggggagcagagt</td>
      <td>tctcgatccagcagggggtgct</td>
    </tr>
    <tr>
      <td>Snai1</td>
      <td>cgatctgcacgacctgtggaaa</td>
      <td>cgtgagcggtcagcaaaagca</td>
      <td>cgactctaggccctggctgctt</td>
      <td>cgactctaggccctggctgctt</td>
    </tr>
    <tr>
      <td>Snai2</td>
      <td>cgagcacattcgaacccacaca</td>
      <td>cgttgcagtgagggcaagagaaa</td>
      <td>cgattgccttgtgtctgcaaga</td>
      <td>cgattgccttgtgtctgcaaga</td>
    </tr>
    <tr>
      <td>Sox7</td>
      <td>agaacccggacctgcacaac</td>
      <td>ccgctctgcctcatccacat</td>
      <td>cggagctcagcaagatgc</td>
      <td>ggtctcttctgggacagtgtcagc</td>
    </tr>
    <tr>
      <td>Tal1</td>
      <td>accggatgccttccccatgtt</td>
      <td>gcgccgcactactttggtgt</td>
      <td>ccaacaacaaccgggtgaaga</td>
      <td>aggaccatcagaaatctccatctca</td>
    </tr>
    <tr>
      <td>Tek</td>
      <td>tccaaaggagaatggctcagg</td>
      <td>tccggattgtttttggccttc</td>
      <td>ttccagaacgtgagagaagaacca</td>
      <td>tgttaagggccagagttcctga</td>
    </tr>
    <tr>
      <td>Tgfb1</td>
      <td>acccccactgatacgcctga</td>
      <td>gcagtgagcgctgaatcgaa</td>
      <td>tggctgtcttttgacgtcactg</td>
      <td>gccctgtattccgtctccttgg</td>
    </tr>
    <tr>
      <td>Tgfb2</td>
      <td>ggcatgcccatatctatggagttc</td>
      <td>cagatcctgggacacacagca</td>
      <td>gacactcaacacaccaaagtcctca</td>
      <td>gggaagcggaagcttcgggattta</td>
    </tr>
    <tr>
      <td>Tgfb3</td>
      <td>catgtcacacctttcagcccaat</td>
      <td>ctccacggccatggtcatct</td>
      <td>gagacatactggaaaatgttcatgaggtg</td>
      <td>cattgtccactcctttgaatttga</td>
    </tr>
    <tr>
      <td>Tgfbr1</td>
      <td>gcagacttgggacttgctgtga</td>
      <td>catctagaacttcaggggccatgt</td>
      <td>catgattctgccacagatacaa</td>
      <td>ccttttagtgcctactctgtggtttgg</td>
    </tr>
    <tr>
      <td>Tgfbr2</td>
      <td>tggccgctgcatatcgtcct</td>
      <td>gcatctttctgggcttccatttcca</td>
      <td>tggacgcgcatcgccagca</td>
      <td>atccgacttgggaacgtg</td>
    </tr>
    <tr>
      <td>Thpo</td>
      <td>ccgacgtcgaccctttgtct</td>
      <td>tgcccctagaatgtcctgtgc</td>
      <td>tccctgttctgctgcctgct</td>
      <td>tgctctgttccgtctgggtttt</td>
    </tr>
    <tr>
      <td>Upp1</td>
      <td>cgagaaggaagacgtgctctacca</td>
      <td>cgtatgaaggtgttcatccgggaa</td>
      <td>cgattcaacctcagcactagcacac</td>
      <td>cgattcaacctcagcactagcacac</td>
    </tr>
  </tbody>
</table>

#### C1 single-cell RNA sequencing

After 6,500 cells in 13 µl of PBS were obtained using FACS enrichment, Fluidigm Suspension Reagent was added in a 3:2 ratio and gently mixed by pipetting. A Fluidigm C1 10–17 uM IFC Chip was primed, 5 µl of cell suspension mix was added to the cell inlet, and the chip was loaded into the C1 instrument. Annotation of cell capture was carried out on a brightfield microscope at 40x magnification and each captured site was noted for having single-cell capture, doublet cell capture or debris. Lysis, reverse transcription, and PCR reagents (Clontech Takara) were then loaded into appropriate inlets as per Fluidigm layout. ERCC spike-in controls (Ambion) were added at a dilution of 1:4000 within the lysis mix to gain limit of detection and normalization in downstream analysis. The IFC was loaded into the C1 instrument overnight using the mRNA-Seq RT and the Amp script, and ~3 µl of cDNA was harvested and diluted in 5 µl of Fluidigm C1 DNA dilution buffer. Size distribution and quantification of individual cDNA samples was obtained using an AATI Fragment Analyzer (AATI) and the cDNA concentration was diluted to 100 pg/µl in 10 mM Tris HCl pH 8.0 for library preparation. Illumina library preparation was carried out using the Nextera XT DNA system (Illumina), but volumes were reduced as per the modified Fluidigm C1 protocol. Tagmentation was performed on all 96 samples using 1.25 µl of cDNA (125 pg total concentration) combined with 2.5 µl of tagmentation buffer (TD) and 1.25 µl of Amplicon Tagment Mix (ATM), and incubated for 10 min at 55 degrees. After incubation, 1.25 µl of Neutrilize Tagment Mix (NT) was added. Illumina PCR barcoded indexes were combined to obtain 96 distinct combinations of i7 and i5 barcodes, and 2.5 µl of combined index was added along with 3.75 µl of Nextera PCR Mix (NPM). Samples were then put through 12 cycles of PCR as per the Illumina protocol. Each column was then pooled into a 0.2 mL 8-strip PCR tube and Ampure XP purification was performed, after which each pool was combined to obtain a single 96-sample multiplexed pool of barcoded library. The final sequencing library was quantified by Qubit (Life Technologies) and size distribution was measured on an Agilent BioAnalyzer. Samples were sequenced with the Illumina HiSeq 2000.

#### Wafergen single-cell RNA sequencing

Cells were stained with the Cell Viability Imaging kit (Molecular Probes), which contains Hoechst 33342 and propidium iodide, and afterwards were counted with the Moxi Z Mini Automated Cell Counter (ORFLO). Stained cell solution was diluted in a mix with diluent and RNase inhibitor (New England Biolabs) to 1 cell/50 nl for dispensing on the ICell8-chip (Wafergen) with the MultiSample NanoDispenser (Wafergen). Positive and negative controls were prepared according to the ICell8 protocol and dispensed with the MSND into the respective nanowells of the chip. All nanowells of the ICell8 chip were imaged with a fluorescence microscope (Olympus). The images were analyzed with the CellSelect software (Wafergen). Alive single cells, which are Hoechst-33342-positive and propidium-iodide-negative, were selected for lysis and reverse transcription inside the ICell8 chip (200 cells i8TFs + dox, 150 cells i8TFs –dox, 150 Empty –dox and 150 Empty +dox). RT reaction mix containing 5X RT buffer, dNTPs, RT e5-oligo (Wafergen), nuclease-free water, Maxima H Minus RT (Thermo Scientific) and Triton X-100 was prepared and dispensed into the previously selected nanowells with single cells inside. The chip was placed inside a modified SmartChip Cycler (Bio-Rad) for the RT reaction (42°C for 90 min, 85°C for 5 min, 4°C forever).

The cDNA of all single cells was collected together and further concentrated with the DNA Clean and Concentrator−5 kit (Zymo Research). The Exonuclease I (New England Biolabs) reaction of the cDNA (37°C for 30 min, 80°C for 20 min, 4°C forever) was performed inside a conventional thermal cycler. Afterwards, the cDNA was amplified with the Advantage 2 PCR Kit (Clontech Takara) containing buffer, dNTPs, Amp Primer (Wafergen), polymerase mix and nuclease-free water (95°C for 1 min, 18 cycles of 95°C for 15 s, 65°C for 30 s and 68°C for 6 min, followed by 72°C for 10 min and 4°C forever). The amplified cDNA was purified with Ampure XP Beads (Beckmann Coulter). The cDNA size distribution was obtained with the High Sensitivity DNA BioAnalyzer (Agilent) and quantification was performed with the Qubit (Life Technologies). Illumina library preparation was carried out by using Nextera XT DNA (Illumina). Tagmentation was performed in tagment DNA buffer, Amplicon Tagment Mix and 1 ng of purified cDNA (55°C for 5 min and 10°C forever), next Neutralize Tagment Buffer was added (room temperature for 5 min). After incubation, the NexteraXT PCR reaction mix was prepared with Nextera PCR Mastermix, i7 Index Primer from the Nextera Index Kit (Illumina), Nextera Primer P5 and Tagmented cDNA-NT buffer mix (72°C for 3 min, 95°C for 30 s, 12 cycles of 95°C for 10 s, 55°C for 30 s and 72°C for 30 s, final 72°C for 5 min and 10°C forever). Ampure XP purification was performed with the finished library. The size distribution was checked on an Agilent BioAnalyzer. Samples were sequenced with the Illumina NextSeq.

### Quantification and statistical analysis

#### GO term enrichment analysis

All GO term enrichment analyses were performed using the g:Profiler web server (Reimand et al., 2016).

#### Flow cytometry analysis

All flow cytometry experiments were independently repeated three times. For Figure 3C and Figure 3D, paired t-test was performed on the cell frequencies. For Figure 3—figure supplement 5D, frequencies for each population were plotted using JMP software (SAS). Error bars correspond to standard deviations.

#### Single-cell quantitative RT-PCR data analysis

Single-cell quantitative RT-PCR data were first processed with the Fluidigm Real Time PCR Analysis software (quality threshold, 0.65; Ct threshold, Auto (Global); and baseline correction method, linear [derivative]). Hierarchical clustering and PCAs were performed using the SINGuLAR Analysis toolset (Fluidigm version 3.5) package in R (R Core Team , 2016). Using this toolset, the Ct values were converted into log2ex. Ct value is a relative gene expression value in the log2 domain (assuming that the PCR efficiency is equal to 1). The conversion from Ct to log2ex value is based on the following formulae:

Log2ex = LOD – Ct, if Ct is less than the limit of detection (LOD)

Log2ex = 0, if Ct is equal to or greater than LOD.

Where the default is 24 (the typical Ct value for a single copy of input in the Fluidigm chip). In our case, the Ct value is a relative expression and does not have unit. Hence, following conversion to the Log2ex domain, we labelled the resulting values ‘Log2 Gene Expression’.

Hierarchical clustering and PCA analyses were performed with the HC() and PCA() functions of this package. The HC function clusters genes by the Pearson Correlation method, that is, co-profiled genes are clustered together and samples are clustered by normalized Euclidian distance (distance/number of genes), representing the average fold change. The HC analysis uses the ‘complete linkage’ method (a bottom-up method) to find similar clusters. The ‘global_z_score’ display option normalizes the expression value using the global mean and the global standard deviation.

The gene expression average of hematopoietic and endothelial genes is shown for each single cell in Figure 1—figure supplement 3. The hematopoietic average is based on the genes Epo, Epor, Gata1, Gata2, Gfi1, Gfi1b, Hbb-bh1, Itga2b, Itgam, Itgb3, Kit, Lmo2, Lyl1, Mpo, Myb, Ptprc, Runx1, Sfpi1, Sla, Tal1 and Thpo and the endothelial average on Cdh5, Cldn5, Eng, Esam, Fbn1, Gpr126, Kdr, Npr1, Pcdh12, Pecam1, Ptprb, Ptprm, Ramp2, Sox7 and Tek.

A prototype was calculated for each cluster group of single cells determined by the hierarchical clustering result shown in Figure 1—figure supplements 1 and 2. The prototype is defined by the average of all cells belonging to its cluster. The Pearson correlation coefficient between all pairwise prototypes is visualized in Figure 1—figure supplement 4A. The R package ComplexHeatmap was used (Gu et al., 2016).

A generalized linear model with Quasi-Poisson distribution and logarithm as the link function was applied to model the count table data as shown in Figure 4B. Six control groups were defined, one for each cell cluster category such as Endo or VSM. Each control group comprises 10 samples and includes all –dox conditions. For each cluster category and for each of the overexpression cell lines, the count of the +dox condition was compared to the counts in its respective control group. Out of these 60 statistical contrasts (six cluster categories times nine overexpression cell lines plus the cell line carrying an empty vector) five were identified to be significantly different with an adjusted p-value<0.05. The method of Benjamini-Hochberg was used for the multiple testing correction. In addition, the generalized linear model included an offset to model rates instead of counts. The rates account for small differences in the total number of cells measured on each of the processed well plates. All five significantly different conditions are marked with a star in Figure 4B (see Supplementary file 6 for p-values).

#### mRNA microarray data analysis

The mRNA microarray data were analyzed using oligo, phylobase, methods, biobase, stats, ggplot2, gplots, matrixstats, graphics, annotationdbi and limma packages in R (R Core Team , 2016).

#### C1 single-cell RNAseq data analysis

Each library was sequenced generating 426,065,795 and 440,774,932 paired-end reads (of 125 bp). Reads were assigned to the well with the matching barcode. Up to two mismatches are tolerated within the well barcode if the assignment remained non-ambiguous. STAR, version 2.4.0 (Dobin et al., 2013), aligned the reads to the mouse genome build mm10/GRCm38. Duplicate reads were removed using samtools, version 0.1.18 (Li et al., 2009). Wells with fewer than 1 million reads were deemed to be empty wells and excluded from further analysis (2 and 1, respectively). Reads with a minimum mapping quality of 30, which mapped to a unique gene, were counted using featureCounts, version 1.4.6 (Liao et al., 2014).

Read counts were normalized using RUVg, version 1.0.0 (Risso et al., 2014), using ERCC spike-in controls and size-factors (SF) as defined in DESeq (Anders and Huber, 2010). Cells with >7% of reads mapped to rRNA (three in each plate) and which were outliers on the basis of the first principal component after size factor normalization were excluded. The remaining cells all contained >7,000 detected genes and were used in all subsequent analyses.

We performed a network analysis using the generalized distance correlation measure, dcor statistic (Székely et al., 2007), together with its conditional version, pdcor (Székely and Rizzo, 2014). For each chip and each normalization method (four configurations), all significant relationships between the transcriptome and the seed genes were identified using the dcor statistic. The seed genes used for this analysis included the 8 TFs as well as Gata1, Gfi1b, Spi1, Ldb1 and Cbfa2t3. The additional seed genes were selected if they appeared in networks published by at least two different authors (Beck et al., 2013; Bonzanni et al., 2013; Moignard et al., 2013; Moignard et al., 2015; Tanaka et al., 2012). The directionality of the relationships (positive correlation, negative correlation or ‘other’) was defined using a two-tailed t-test, direct was based on the sign of the test and ‘other’ was assigned to all genes with uncorrected p-value>0.05. To ensure robustness, we only included relationships that were identified in at least two of the four configurations, and any relationships with conflicting directionalities were assigned to ‘other’. Finally, interactions between seed genes were identified by conditioning the ‘targets’ of each seed gene on the expression of each other seed gene. An interaction was inferred if the relationships between both seed genes and a particular ‘target’ gene increased in strength when conditioned on the other seed gene.

For the Spearman network analysis, we combined Exp1 and Exp2 into a single expression matrix for each normalization (SF and RUV). We calculated Spearman correlations using base R-function for each normalization and we averaged the correlations across the two normalizations. We changed all correlations with absolute value <0.25 (i.e <0.25 and >−0.25) to 0. We created a network with weighted edges between genes, correlations of 0 = no edge. We calculated eigen centrality using eigen_centrality from the igraph R package (Bonacich, 1987). We took the absolute value of all edges (turns all relationships to be positive) and calculated betweenness centrality (number of shortest paths passing through a node) using betweenness from the igraph R package (Brandes, 2001). We calculated degree (number of edges attached to a node) using degree from the igraph R package. Then, we calculated the median value of each measure across all genes in the network. We counted the number of genes in the list that are above the median and we tested the significance of this using a binomial test (by definition 50% of genes are above the median).

#### Wafergen single-cell RNAseq data analysis

673 wells on the Wafergen chip passed microscopic inspection. Pooling, library construction and sequencing generated 179 million paired-end sequences using the Illumina Nextera protocol. Note that this shallower sequencing greatly reduces the detection rate of TFs, but the larger number of cells facilitated evaluation of heterogeneity within and between populations. The first read of the pair encodes the well barcode and the UMI (unique molecular identifier) barcode, the second encodes the 3′ end of the transcript. Reads were assigned to the well with the matching barcode. Up to two mismatches are tolerated within the well barcode if the assignment remained non-ambiguous. Cutadapt trimmed poly-A, poly-G and adapter sequences and STAR aligned the reads to the mouse genome build mm10 (Dobin et al., 2013; Martin, 2011). FeatureCounts determined all reads in a strand-specific way so that they overlap with exactly one gene (Liao et al., 2014). Gene expression levels are calculated by counting the number of distinct UMIs of all gene specific reads (‘UMIs per gene’), as determined by featureCounts. Only uniquely aligned reads were counted. To further reduce the impact of mapping and sequencing errors on the quantification, an UMI barcode error correction and filtering step was introduced. If two or more of the distinct UMIs per gene share a similar barcode, differing by at most one or two mismatches, then they may originate from the same UMI barcode. The UMI barcode is corrected only if it has less than 10% of reads compared to the most abundant one. This correction procedure starts with the UMI barcode, which is supported by the highest number of gene-specific reads, and which determines all similar barcodes and corrects them if applicable. It restarts with all UMI barcodes that have not been considered in a previous iteration until none is left. In a separate filtering step, any of the distinct UMIs per gene that is only supported by one or two aligned reads is completely omitted from the counting. From the resulting count table, all counts originating from the 23 control wells were removed for the subsequent explorative analysis. All remaining wells correspond to single cells. Additional filtering reduced the sparseness found in this gene per cell matrix of UMI counts. Only cells with 1000 or more genes with at least one UMI count and genes with at least one UMI count in 10 or more cells were selected, leaving a matrix of 478 single cells and 10,238 genes. This matrix was scaled and normalized with the Bioconductor package scater (McCarthy et al., 2017). The principal components were calculated for the 400 genes that showed the highest variance after subtracting the mean-variance trend of all genes. The explorative analysis was performed using R (R Core Team , 2016).

### Data and software availability

#### Software

All software is freely or commercially available and is listed in the Methods description and product reference table.

#### Data resources

The accession number for all sc-RNA-seq and microarray data reported in this paper is GEO: GSE96986.

### Product reference table

<table>
  <thead>
    <tr>
      <th>Product or resource</th>
      <th>Supplier</th>
      <th>Reference No</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3">Antibodies</td>
    </tr>
    <tr>
      <td>Anti-6X His tag antibody [HIS.H8]</td>
      <td>Abcam</td>
      <td>ab18184</td>
    </tr>
    <tr>
      <td>Anti-alpha-Tubulin-Antibody (mouse)</td>
      <td>Sigma</td>
      <td>T9026</td>
    </tr>
    <tr>
      <td>Anti-APC MicroBeads</td>
      <td>Miltenyi Biotec</td>
      <td>130-090-855</td>
    </tr>
    <tr>
      <td>Anti-Cbfb Antibody</td>
      <td>Abcam</td>
      <td>ab133600</td>
    </tr>
    <tr>
      <td>Anti-Erg Antibody</td>
      <td>Abcam</td>
      <td>ab92513</td>
    </tr>
    <tr>
      <td>Anti-FLAG M2 antibody</td>
      <td>Sigma</td>
      <td>F1804</td>
    </tr>
    <tr>
      <td>Anti-FLI1 antibody [EPR4646]</td>
      <td>Abcam</td>
      <td>ab133485</td>
    </tr>
    <tr>
      <td>Anti-GATA2 antibody [EPR2822(2)]</td>
      <td>Abcam</td>
      <td>ab109241</td>
    </tr>
    <tr>
      <td>Anti-HA antibody produced in rabbit</td>
      <td>Sigma</td>
      <td>H6908</td>
    </tr>
    <tr>
      <td>Anti-Lmo2 Antibody</td>
      <td>Abcam</td>
      <td>ab91652</td>
    </tr>
    <tr>
      <td>Anti-Lyl1 antibody [KT43]</td>
      <td>Abcam</td>
      <td>ab53354</td>
    </tr>
    <tr>
      <td>Anti-Mouse CD144 (VE-Cadherin) eFluor 660, eBioBV13</td>
      <td>eBioscience</td>
      <td>50-1441-80</td>
    </tr>
    <tr>
      <td>Anti-Mouse CD309 (FLK1) APC, Avas12a1</td>
      <td>eBioscience</td>
      <td>17-5821-81</td>
    </tr>
    <tr>
      <td>Anti-Mouse CD41 PE, MWReg30</td>
      <td>eBioscience</td>
      <td>12-0411-81</td>
    </tr>
    <tr>
      <td>Anti-Mouse cKit APC Antibody</td>
      <td>eBioscience</td>
      <td>17-1171-82</td>
    </tr>
    <tr>
      <td>Anti-Mouse HRP</td>
      <td>GE Healthcare Life Sciences</td>
      <td>NA931V</td>
    </tr>
    <tr>
      <td>Anti-Rat HRP</td>
      <td>GE Healthcare Life Sciences</td>
      <td>NA935V</td>
    </tr>
    <tr>
      <td>Anti-Runx1 Antibody</td>
      <td>Abcam</td>
      <td>ab92336</td>
    </tr>
    <tr>
      <td>Anti-Tal1 Antibody</td>
      <td>Abcam</td>
      <td>ab119754</td>
    </tr>
    <tr>
      <td>Anti-V5 Antibody</td>
      <td>Life Technologies</td>
      <td>46–0705</td>
    </tr>
    <tr>
      <td>Peroxidase AffiniPure Goat Anti-Rabbit IgG (H + L)</td>
      <td>Jackson</td>
      <td>111-035-144</td>
    </tr>
    <tr>
      <td colspan="3">Chemicals</td>
    </tr>
    <tr>
      <td>2-mercaptoethanol</td>
      <td>GIBCO</td>
      <td>31350–010</td>
    </tr>
    <tr>
      <td>Ascorbic acid</td>
      <td>Sigma</td>
      <td>A4544</td>
    </tr>
    <tr>
      <td>Collagenase Type IA from Clostridium histolyticum lyophilized powder (from sterile-filtered solution), 0.5–5.0 FALGPA units/mg solid, cell culture tested</td>
      <td>Sigma</td>
      <td>C9722-50MG</td>
    </tr>
    <tr>
      <td>D4T supernatant</td>
      <td>EMBL-Rome</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Doxycycline</td>
      <td>Sigma</td>
      <td>D9891</td>
    </tr>
    <tr>
      <td>EPO</td>
      <td>R and D</td>
      <td>959-ME-010</td>
    </tr>
    <tr>
      <td>ERCC RNA Spike-In Mix</td>
      <td>Ambion</td>
      <td>4456740</td>
    </tr>
    <tr>
      <td>Exonuclease I</td>
      <td>New England Biolabs</td>
      <td>M0293L</td>
    </tr>
    <tr>
      <td>Fetal bovine plasma-derived serum platelet poor (PDS)</td>
      <td>Antech</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Fetal bovine serum (FBS)</td>
      <td>PAA</td>
      <td>A15-102</td>
    </tr>
    <tr>
      <td>Fluidigm C1 DNA Dilution Buffer</td>
      <td>Fluidigm</td>
      <td>100–5317</td>
    </tr>
    <tr>
      <td>Fluidigm Suspension Reagent</td>
      <td>Fluidigm</td>
      <td>100–6201</td>
    </tr>
    <tr>
      <td>Gelatin</td>
      <td>BDH</td>
      <td>440454B</td>
    </tr>
    <tr>
      <td>Ghost Dye Red 780</td>
      <td>Tonbo Biosciences</td>
      <td>13–0865</td>
    </tr>
    <tr>
      <td>GM-CSF</td>
      <td>R and D</td>
      <td>425 ML</td>
    </tr>
    <tr>
      <td>Human FGF basic</td>
      <td>R and D</td>
      <td>233-FB-025</td>
    </tr>
    <tr>
      <td>IL-11</td>
      <td>R and D</td>
      <td>418 ML</td>
    </tr>
    <tr>
      <td>IL-3</td>
      <td>R and D</td>
      <td>403 ML</td>
    </tr>
    <tr>
      <td>IL-6</td>
      <td>R and D</td>
      <td>406 ML</td>
    </tr>
    <tr>
      <td>IMDM</td>
      <td>Lonza</td>
      <td>BE12-726F</td>
    </tr>
    <tr>
      <td>KnockOut DMEM</td>
      <td>GIBCO</td>
      <td>10829–018</td>
    </tr>
    <tr>
      <td>L-glutamine</td>
      <td>GIBCO</td>
      <td>25030–024</td>
    </tr>
    <tr>
      <td>LIF</td>
      <td>EMBL Heidelberg</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Maxima H Minus Reverse Transcriptase</td>
      <td>Thermo Scientific</td>
      <td>EP0752</td>
    </tr>
    <tr>
      <td>MCSF</td>
      <td>R and D</td>
      <td>416 ML-010</td>
    </tr>
    <tr>
      <td>MEM Non-Essential Amino Acids Solution</td>
      <td>GIBCO</td>
      <td>11140–035</td>
    </tr>
    <tr>
      <td>Methylcellulose</td>
      <td>VWR</td>
      <td>9004-67-5</td>
    </tr>
    <tr>
      <td>Monothioglycerol (MTG)</td>
      <td>Sigma</td>
      <td>M6145</td>
    </tr>
    <tr>
      <td>Oncostatin M</td>
      <td>R and D</td>
      <td>495-MO</td>
    </tr>
    <tr>
      <td>Penicillin-streptomycin</td>
      <td>GIBCO</td>
      <td>15140–122</td>
    </tr>
    <tr>
      <td>PFMH-II</td>
      <td>GIBCO</td>
      <td>12040–077</td>
    </tr>
    <tr>
      <td>Pierce RIPA Buffer</td>
      <td>Thermo Scientific</td>
      <td>89900</td>
    </tr>
    <tr>
      <td>Ponceau S Solution</td>
      <td>Sigma</td>
      <td>P7170</td>
    </tr>
    <tr>
      <td>RNase Inhibitor</td>
      <td>New England Biolabs</td>
      <td>M0314S</td>
    </tr>
    <tr>
      <td>SCF</td>
      <td>R and D</td>
      <td>455-MC</td>
    </tr>
    <tr>
      <td>TPO</td>
      <td>R and D</td>
      <td>488-TO-005</td>
    </tr>
    <tr>
      <td>Transferrin</td>
      <td>Roche (Italy)</td>
      <td>10652202001</td>
    </tr>
    <tr>
      <td>TrypLE express</td>
      <td>GIBCO</td>
      <td>12605–036</td>
    </tr>
    <tr>
      <td>VEGF</td>
      <td>R and D</td>
      <td>293-VE</td>
    </tr>
    <tr>
      <td colspan="3">Commercial assays</td>
    </tr>
    <tr>
      <td>Advantage 2 PCR Kit</td>
      <td>Clontech Takara</td>
      <td>639207</td>
    </tr>
    <tr>
      <td>Amersham ECL Prime Western Blotting Detection Reagent</td>
      <td>GE Healthcare Life Sciences</td>
      <td>RPN2232</td>
    </tr>
    <tr>
      <td>Annexin V-FITC Apoptosis Detection Kit</td>
      <td>eBioscience</td>
      <td>88-8005-72</td>
    </tr>
    <tr>
      <td>Cell Viability Imaging kit</td>
      <td>Molecular Probes</td>
      <td>R37610</td>
    </tr>
    <tr>
      <td>CellsDirect One-Step qRT-PCR kit</td>
      <td>Invitrogen</td>
      <td>11753100</td>
    </tr>
    <tr>
      <td>Click-iT Plus EdU Alexa Fluor 488 Flow Cytometry Assay kit</td>
      <td>Molecular Probes</td>
      <td>C10633</td>
    </tr>
    <tr>
      <td>DNA Clean and Concentrator−5 kit</td>
      <td>Zymo Research</td>
      <td>D4013</td>
    </tr>
    <tr>
      <td>Dual-Luciferase Reporter Assay System</td>
      <td>Promega</td>
      <td>E1910</td>
    </tr>
    <tr>
      <td>ICell8-chip and reagent kit</td>
      <td>Wafergen</td>
      <td>430–000233</td>
    </tr>
    <tr>
      <td>NanoJuice transfection kit</td>
      <td>Merck Millipore</td>
      <td>71902</td>
    </tr>
    <tr>
      <td>Nextera Index Kit</td>
      <td>Illumina</td>
      <td>FC-131–1001</td>
    </tr>
    <tr>
      <td>Nextera XT DNA Library Prep kit – 24 samples (Wafergen experiment)</td>
      <td>Illumina</td>
      <td>FC-131–1024</td>
    </tr>
    <tr>
      <td>Nextera XT DNA Library Prep kit – 96 samples (C1 experiment)</td>
      <td>Illumina</td>
      <td>FC-131–1096</td>
    </tr>
    <tr>
      <td>Nuclear Extract kit</td>
      <td>ActiveMotif</td>
      <td>40010</td>
    </tr>
    <tr>
      <td>Pierce BCA Protein Assay kit</td>
      <td>Thermo Scientific</td>
      <td>23225</td>
    </tr>
    <tr>
      <td>RNAeasy Plus Micro kit</td>
      <td>Qiagen</td>
      <td>74034</td>
    </tr>
    <tr>
      <td>SMARTer Ultra Low RNA Kit for the Fluidigm C1 System, 10 IFCs</td>
      <td>Clontech Takara</td>
      <td>634833</td>
    </tr>
    <tr>
      <td colspan="3">Deposited data</td>
    </tr>
    <tr>
      <td>Raw and analysed sequencing and microarray data</td>
      <td>This paper</td>
      <td>GEO: GSE96986</td>
    </tr>
    <tr>
      <td>Raw and analysed sequencing data</td>
      <td>(Goode et al., 2016)</td>
      <td>GEO: GSE69101</td>
    </tr>
    <tr>
      <td>Raw and analysed sequencing data</td>
      <td>(Pereira et al., 2016)</td>
      <td>GEO: GSE54574</td>
    </tr>
    <tr>
      <td colspan="3">Cell lines</td>
    </tr>
    <tr>
      <td>A2lox.Cre mESC line</td>
      <td>(Iacovino et al., 2011)</td>
      <td>A2lox.Cre</td>
    </tr>
    <tr>
      <td>A2lox.empty mESC line</td>
      <td>This paper</td>
      <td>Empty</td>
    </tr>
    <tr>
      <td>A2lox.i8TFs mESC line</td>
      <td>This paper</td>
      <td>i8TFs</td>
    </tr>
    <tr>
      <td>A2lox.iCbfb mESC line</td>
      <td>This paper</td>
      <td>iCbfb</td>
    </tr>
    <tr>
      <td>A2lox.iErg mESC line</td>
      <td>This paper</td>
      <td>iErg</td>
    </tr>
    <tr>
      <td>A2lox.iFli1 mESC line</td>
      <td>This paper</td>
      <td>iFli1</td>
    </tr>
    <tr>
      <td>A2lox.iGata2 mESC line</td>
      <td>This paper</td>
      <td>iGata2</td>
    </tr>
    <tr>
      <td>A2lox.iLmo2 mESC line</td>
      <td>This paper</td>
      <td>iLmo2</td>
    </tr>
    <tr>
      <td>A2lox.iLyl1 mESC line</td>
      <td>This paper</td>
      <td>iLyl1</td>
    </tr>
    <tr>
      <td>A2lox.iRunx1 mESC line</td>
      <td>This paper</td>
      <td>iRunx1</td>
    </tr>
    <tr>
      <td>A2lox.iTal1 mESC line</td>
      <td>This paper</td>
      <td>iTal1</td>
    </tr>
    <tr>
      <td>Runx1+/hCD4</td>
      <td>(Sroczynska et al., 2009a)</td>
      <td>Runx1+/hCD4</td>
    </tr>
    <tr>
      <td colspan="3">Mice</td>
    </tr>
    <tr>
      <td>C57BL/6N</td>
      <td>EMBL Rome</td>
      <td></td>
    </tr>
    <tr>
      <td>Gfi1b:GFP knock-in mice</td>
      <td>(Vassen et al., 2007)</td>
      <td></td>
    </tr>
    <tr>
      <td>Gfi1:GFP knock-in mice</td>
      <td>(Yücel et al., 2004)</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Recombinant DNA</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_5TFs</td>
      <td>This paper</td>
      <td>p2lox_5TFs</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_6TFs</td>
      <td>This paper</td>
      <td>p2lox_6TFs</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_8TFs</td>
      <td>This paper</td>
      <td>p2lox_8TFs</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_empty</td>
      <td>(Vargel et al., 2016)</td>
      <td>p2lox_empty</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_K_Cbfb</td>
      <td>This paper</td>
      <td>p2lox_K_Cbfb</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_K_Erg</td>
      <td>This paper</td>
      <td>p2lox_K_Erg</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_K_Fli1</td>
      <td>This paper</td>
      <td>p2lox_K_Fli1</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_K_Gata2</td>
      <td>This paper</td>
      <td>p2lox_K_Gata2</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_K_Lmo2</td>
      <td>This paper</td>
      <td>p2lox_K_Lmo2</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_K_Lyl1</td>
      <td>This paper</td>
      <td>p2lox_K_Lyl1</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_K_Runx1</td>
      <td>This paper</td>
      <td>p2lox_K_Runx1</td>
    </tr>
    <tr>
      <td>Plasmid: p2lox_K_Tal1</td>
      <td>This paper</td>
      <td>p2lox_K_Tal1</td>
    </tr>
    <tr>
      <td>Plasmid: pGL4.10[luc2]</td>
      <td>Promega</td>
      <td>E6651</td>
    </tr>
    <tr>
      <td>Plasmid: pGL4.74[hRluc/TK]</td>
      <td>Promega</td>
      <td>E6921</td>
    </tr>
    <tr>
      <td colspan="3">Software and algorithms</td>
    </tr>
    <tr>
      <td>CellProfiler</td>
      <td>(Kamentsky et al., 2011)</td>
      <td>http://www.cellprofiler.org</td>
    </tr>
    <tr>
      <td>CellSelect software</td>
      <td>Wafergen</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Fiji</td>
      <td>(Schindelin et al., 2012)</td>
      <td>http://fiji.sc/Fiji</td>
    </tr>
    <tr>
      <td>FlowJo</td>
      <td>Tree Star, Inc.</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>JMP software</td>
      <td>SAS</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td colspan="3">Others</td>
    </tr>
    <tr>
      <td>96.96 dynamic array IFC</td>
      <td>Fluidigm</td>
      <td>BMK-M-96.96</td>
    </tr>
    <tr>
      <td>AATI Fragment Analyzer</td>
      <td>AATI</td>
      <td>DNF-474</td>
    </tr>
    <tr>
      <td>Ampure XP Beads</td>
      <td>Beckmann Coulter</td>
      <td>B23319</td>
    </tr>
    <tr>
      <td>BioAnalyzer</td>
      <td>Agilent</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Biomark HD system</td>
      <td>Fluidigm</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>FACSAria</td>
      <td>Becton Dickinson</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>FACSCanto</td>
      <td>Becton Dickinson</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Fluidigm C1 10–17 uM IFC chip</td>
      <td>Fluidigm</td>
      <td>100–5760</td>
    </tr>
    <tr>
      <td>Fluorescence microscope for Wafergen chip imaging</td>
      <td>Olympus</td>
      <td>BX43F</td>
    </tr>
    <tr>
      <td>Hard-Shell PCR plates</td>
      <td>Bio-Rad</td>
      <td>HSP9611</td>
    </tr>
    <tr>
      <td>HiSeq 2000</td>
      <td>Illumina</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>ICell8 System</td>
      <td>Wafergen</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>IncuCyte HD</td>
      <td>Essen Biosciences</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>MACS MicroBead Technology</td>
      <td>Miltenyi Biotec</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Moxi Z Mini Automated Cell Counter</td>
      <td>ORFLO</td>
      <td>MXZ001</td>
    </tr>
    <tr>
      <td>MultiSample NanoDispenser</td>
      <td>Wafergen</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>NextSeq</td>
      <td>Illumina</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>NuPAGE 12% Bis-Tris Protein Gels</td>
      <td>Life Technologies</td>
      <td>NP0343BOX</td>
    </tr>
    <tr>
      <td>PCR barcoded indexes</td>
      <td>Illumina</td>
      <td>FC-131–200</td>
    </tr>
    <tr>
      <td>POLARstar Omega device</td>
      <td>BMG Labtech</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>PROTRAN Nitrocellulose membrane</td>
      <td>PerkinElmer</td>
      <td>NBA085C</td>
    </tr>
    <tr>
      <td>Qubit</td>
      <td>Life Technologies</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>SmartChip Cycler</td>
      <td>Bio-Rad</td>
      <td>T-100</td>
    </tr>
    <tr>
      <td>Universal cDNA Reverse Trancribed by Random Hexamer: Mouse Normal Tissues</td>
      <td>BioChain</td>
      <td>C4334566-R</td>
    </tr>
    <tr>
      <td>XCell SureLock Mini-Cell Electrophoresis System</td>
      <td>Invitrogen</td>
      <td>N/A</td>
    </tr>
  </tbody>
</table>
