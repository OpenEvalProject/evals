# Osterix-Cre marks distinct subsets of CD45- and CD45+ stromal populations in extra-skeletal tumors with pro-tumorigenic characteristics

## Authors

- Biancamaria Ricci<sup>1</sup> ([ORCID: 0000-0003-1574-6043](https://orcid.org/0000-0003-1574-6043))
- Eric Tycksen<sup>2</sup>
- Hamza Celik<sup>3</sup>
- Jad I Belle<sup>3</sup>
- Francesca Fontana<sup>3</sup>
- Roberto Civitelli<sup>4</sup> ([ORCID: 0000-0003-4076-4315](https://orcid.org/0000-0003-4076-4315))
- Roberta Faccio<sup>1</sup> ([ORCID: 0000-0003-1639-2005](https://orcid.org/0000-0003-1639-2005)) †

### Affiliations

1. Department of Orthopedics, Washington University School of Medicine St. Louis United States
2. Genome Technology Access Center, Department of Genetics, Washington University School of Medicine St. Louis United States
3. Department of Medicine, Division of Oncology, Washington University School of Medicine St. Louis United States
4. Department of Medicine, Division of Bone and Mineral Diseases, Washington University School of Medicine St. Louis United States
5. Shriners Children Hospital St. Louis United States

† Corresponding author

## Abstract

Cancer-associated fibroblasts (CAFs) are a heterogeneous population of mesenchymal cells supporting tumor progression, whose origin remains to be fully elucidated. Osterix (Osx) is a marker of osteogenic differentiation, expressed in skeletal progenitor stem cells and bone-forming osteoblasts. We report Osx expression in CAFs and by using Osx-cre;TdTomato reporter mice we confirm the presence and pro-tumorigenic function of TdTOSX+ cells in extra-skeletal tumors. Surprisingly, only a minority of TdTOSX+ cells expresses fibroblast and osteogenic markers. The majority of TdTOSX+ cells express the hematopoietic marker CD45, have a genetic and phenotypic profile resembling that of tumor infiltrating myeloid and lymphoid populations, but with higher expression of lymphocytic immune suppressive genes. We find Osx transcript and Osx protein expression early during hematopoiesis, in subsets of hematopoietic stem cells and multipotent progenitor populations. Our results indicate that Osx marks distinct tumor promoting CD45- and CD45+ populations and challenge the dogma that Osx is expressed exclusively in cells of mesenchymal origin.

## Introduction

In the past couple of decades the common beliefs of how an incipient tumor grows and progresses to a metastatic stage have drastically changed due to the increasing findings of a tight crosstalk between tumor cells and the surrounding stroma, known as the tumor microenvironment (TME) (Hanahan and Weinberg, 2011). Tumor stroma comprises a variety of different cells from the mesenchymal and hematopoietic compartments, with pro- and anti-tumor functions. Cancer-associated fibroblasts (CAFs) are cells of the mesenchymal lineage involved in supporting various stages of tumorigenesis from growth to metastatic dissemination (Kalluri and Zeisberg, 2006; Chen and Song, 2019). Their abundance and phenotypic markers differ among the various types of cancers. CAFs support tumor growth by stimulating tumor cell proliferation, inhibiting apoptotic signals and anti-tumor immune responses, altering the extra-cellular matrix (ECM) to favor invasiveness, and by offering protection from chemotherapeutic approaches. Their heterogeneity probably accounts for the different tumor promoting effects and reflects the fact that CAFs can originate from multiple cellular sources (Chen and Song, 2019). Several studies indicate that CAFs derive from bone marrow mesenchymal stem and progenitor cells recruited at the tumor site. Additional evidence indicates that they can also derive from myofibroblasts, as well as from the trans-differentiation of local pericytes, endothelial and epithelial cells. In breast cancer, subsets of bone marrow-derived CAFs can exhibit a unique inflammatory profile depending on the location to which they are recruited, thus being functionally distinct from the resident CAFs and having better tumor-promoting functions (Raz et al., 2018). Adding more complexity to the origin of CAFs, an additional population expressing several markers commonly found in fibroblasts and CAFs, is the fibrocyte (Abe et al., 2001; McDonald and LaRue, 2012; van Deventer et al., 2013). Fibrocytes originate from the bone marrow, where they have been described to contribute to bone marrow fibrosis under pathological conditions (Ohishi et al., 2012). These cells have also been implicated in supporting tumor progression, but they differ from the bone marrow-derived CAF populations in that they also express the hematopoietic marker CD45, along with markers associated with the monocyte/macrophage lineage populations (Abe et al., 2001). Fibrocytes support tumor growth by making collagen, albeit at lower levels than the CAFs, releasing growth factors, commonly produced by immune suppressive myeloid cells, and by modulating resistance to anti-angiogenic therapy (Goto and Nishioka, 2017). Recent single-cell RNA sequencing (scRNAseq) studies further confirmed the complexity of the CAF populations, suggesting tumor specificity as well as functional differences among the various subsets (Bartoschek et al., 2018; Costa et al., 2018; Elyada et al., 2019). However, these studies did not directly address the origin of the various subsets, which could account for their specific cellular phenotype.

Because of their ability to produce collagen and other extracellular matrix proteins, we sought to determine whether a subset of bone marrow-derived CAFs could share markers of committed osteolineage cells. Osteolineage cells derive from bone marrow mesenchymal stem cells (MSCs) and their differentiation program is driven by sequential activation of two specific transcription factors, Runx2 and Sp7(Osx gene), and subsequent acquisition of a phenotype characterized by the ability to produce bone matrix, primarily type I collagen, and to mineralize (Nakashima et al., 2002). Although Osx is largely thought as a marker of differentiated osteoblasts, emerging data demonstrate that in the embryonic and perinatal bone marrow Sp7 is expressed in definitive MSCs that give rise to the marrow stroma, including osteoblasts and adipocytes (Liu et al., 2013; Mizoguchi et al., 2014). Furthermore, during embryogenesis, Osx is present in extra-skeletal tissues, including the olfactory bulb, the intestine and the kidney (Chen et al., 2014; Jia et al., 2015).

Based on the above observations, we hypothesized that a subset of CAFs, derived from Osx+ cells in the bone marrow, contributes to ECM (i.e. collagen) production at the tumor site, thereby creating a tumor supporting stroma. Using a cell tracking system, we found the presence of cells targeted by the Osx promoter within the TME; these TdTOSX+ cells favor tumor growth when co-injected with tumor cells in mice. Surprisingly, only a minority of tumor-resident cells derived from Osx+ cells expresses fibroblast markers, extracellular matrix and matrix remodeling genes. The majority of these newly identified TdTOSX+ tumor infiltrating cells are also positive for CD45, a marker of hematopoietic lineage, and share markers expressed by tumor-infiltrating immune cells. Importantly, we confirmed Sp7 transcripts and Osx protein in a subset of hematopoietic stem cells (HSC), giving rise to TdTOSX+;CD45+ tumor infiltrating immune populations. This study further identifies new populations of TME cells targeted by Osx and challenges the use of Osx-cre driven lineage tracing mouse models to exclusively study mesenchymal lineage cell fate.

## Results

### Embryonic and adult-derived osteolineage Osx+ cells are present in extra-skeletal tumors

To determine whether osteolineage cells may be present in the TME, we crossed the established tetracycline-dependent Tg(Sp7-tTA,tetO-EGFP/cre)1Amc/J (Osx-cre) to the B6.Cg-Gt(ROSA)26Sortm9(CAG-tdTomato)Hze/J (TdT) to generate the Osx-cre;TdT reporter mouse model (Rodda and McMahon, 2006). When constitutively activated, TdT marks the entire osteolineage, including bone surface osteoblasts, osteocytes and bone marrow cells with mesenchymal stem and osteoprogenitor cell features; while delaying Osx-cre expression until postnatally restricts TdT targeting to committed osteoblasts and osteocytes (Mizoguchi et al., 2014; Fontana et al., 2017). Therefore, Osx-cre;TdT mice and control animals carrying only the TdT transgene (WT;TdT) were kept on standard chow to allow constitutive embryonic transgene activation, or fed a doxycycline (doxy)-containing diet until weaning to suppress transgene activation until one month of age (Figure 1A). We previously reported that doxy-fed mice display less than 1% of spontaneous recombination in the bone residing osteoblasts at weaning, but full transgene activation 1 month thereafter (Fontana et al., 2017).

![Figure 1.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig1-v2.jpg)

**Figure 1.:** (A) Doxycycline (doxy)-repressible Sp7-cre/loxP mouse model used to activate Ai9/TdTomato expression for lineage tracing experiments. In no doxy-fed mice, TdT is expressed in embryonic-derived osteolineage cells (left), while in mice fed a doxy diet until weaning, TdT is expressed in adult-derived osteolineage cells. (B–I) Flow cytometry analysis and fluorescence images of primary tumors showing presence of TdTOSX+ cells in no-doxy fed Osx-cre;TdT mice or WT;TdT controls inoculated with B16-F10 melanoma subcutaneously (B–C), or with PyMT breast cancer cells in the mammary fat pad (MFP) (D–E), and in doxy-fed mice injected with B16-F10 subcutaneously (F–G), or with PyMT in the MFP (H–I). Slides for fluorescence images were counterstained with DAPI (blue), magnification 200X. Inserts are further magnified 4.5 folds. Data representative of a single experiment, experiments were repeated between 2 and 5 times. p values represent Student t-test statistical analysis.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Tumor growth in Osx-cre;TdT and WT;TdT male mice injected subcutaneously with B16-F10 tumor cells. (B) Body weight of the mice showed in (A) at the day of tumor injection (day 0) and at the end point (day 14 post-injection). (C) Tumor growth in Osx-cre;TdT and WT;TdT female mice injected in the MFP with PyMT tumor cells. (D) Body weight of the mice showed in (C) on day 0 and day 14 post-injection.

Osx-cre;TdT reporter mice and WT;TdT fed a normal diet (no doxy) were inoculated with either 105 B16-F10 melanoma cells subcutaneously or 105 PyMT breast cancer cells in the mammary fat pad (MFP). To account for the possible growth delay sometimes observed in no-doxy fed Osx-cre mice (Davey et al., 2012), tumor cells were injected at 12 weeks of age, when the growth delay is fully recovered. Importantly, no differences in tumor growth were observed in age and sex matched Osx-cre;TdT and WT;TdT mice, excluding any potential confounding effect of the Osx-cre (Figure 1—figure supplement 1). To assess the presence of osteolineage Osx+ derived cells within the tumor stroma of no doxy-fed mice, we performed flow cytometry analysis on B16-F10 and PyMT tumors isolated 2 weeks post-inoculation, and found that about 10–18% of the total cells were TdTOSX+ (Figure 1B and D). Histological analysis of frozen sections from the same tumors confirmed the presence of TdTOSX+ cells. These cells had either round or elongated shape, indicating morphologic heterogeneity within the TdTOSX+ population (Figure 1C and E). These TdTOSX+ cells within the tumor stroma of no-doxy mice may derive from resident Osx-expressing embryonic progenitors or from mobilization of bone marrow Osx+ cells.

Remarkably, TdTOSX+ cells were also present in the B16-F10 and PyMT TME of doxy-fed animals 4 weeks post weaning, although their numbers were lower than in tumors isolated from no doxy-treated mice (Figure 1F and H). Fluorescence micrographs also confirmed the presence of TdTOSX+ cells in the stroma in both tumor models (Figure 1G and I), with the same pleiotropic morphology as seen in no doxy-treated mice. Thus, embryonic and adult-derived osteolineage Osx+ cells are present in the stroma of extra-skeletal tumors. Based on these findings, the doxy-fed Osx-cre;TdT mice were used for all the subsequent studies.

### TdTOSX+ cells from primary tumors express mesenchymal markers

To determine the phenotype of TdTOSX+ cells more in depth, we isolated TdTOSX+ cells by FACS sorting 14 days after inoculation of B16-F10 tumor cells into doxy-fed Osx-cre;TdT reporter mice (Figure 2A). Due to the limited number of TdTOSX+, tumors from 2 to 4 mice were pooled for FACS sorting and reported as one experimental replicate (single data point). Messenger RNA from an immortalized murine CAF cell line (i-CAFs) and cortical long bone devoid of bone marrow cells were used as controls. Real-Time PCR confirmed Sp7 expression in TdTOSX+ cells but not in the TdTOSX– fraction, which includes the remaining stroma and the tumor cells (Figure 2B). Interestingly, Sp7 expression was also detected in i-CAFs (Figure 2B), and as expected in bone extracts in higher abundance. Expression of osteoblast-specific markers such as Runx2, Bglap (Ocn) (Osteocalcin), Ibsp (Bsp, bone sialoprotein) and Alpl (Tnap, tissue non-specific alkaline phosphatase) were negligible in TdTOSX+ cells and undetectable or barely detectable in the i-CAFs (Figure 2C–F). However, S100a4(Fsp1) (Fibroblast-specific protein 1) and Acta2 (α-SMA) (α-smooth muscle actin), two CAFs specific markers, were detected in TdTOSX+ cells (Figure 2G and H). TdTOSX+ also expressed Col1a1 (Collagen Type Ia1) and Col1a2 (Collagen Type Ia2) similar to i-CAFs and bone extracts (Figure 2I and J). Expression of matrix metalloproteinases, Mmp2 and Mmp9, involved in matrix remodeling and highly expressed in CAFs and osteoblasts respectively, was also detected in the TdTOSX+ cells (Figure 2K and L).

![Figure 2.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig2-v2.jpg)

**Figure 2.:** (A) Experimental design for isolating TdTOSX+ cells from primary tumors isolated from doxy-fed Osx-cre;TdT mice inoculated with B16-F10. TdTOSX- cells comprise all TdT negative cells including the tumor cells. Immortalized CAFs (iCAFs) and crushed long bones were used as reference controls. (B–L) Quantitative Real-Time PCR for (B) Sp7(Osterix), (C) Runx2, (D) Bglap(Osteocalcin), (E) Ibsp (Bone sialoprotein), (F) Alpl (Tnap, Tissue non-specific alkaline phosphatase), (G) S100a4 (Fsp1), (H) Acta2 (α-SMA) (I) Collagen1a1 (J) Collagen1a2, (K) Mmp2 (Metalloproteinase2) and (L) Mmp9 (Metalloproteinase9) genes in TdTOSX+, TdTOSX- cells, iCAFs and bone. Each data point includes cells isolated from 3 to 4 mice and from two independent experiments. (M–N) Real-Time PCR of Sp7(Osterix) in B16-F10 or PyMT cell lines, CAFs isolated from primary B16-F10 or PyMT tumors or from the remaining cells comprising the tumor minus the CAFs (susp) (n = 3–4 mice). (O) Sp7(Osx) expression based on the Finak Breast Cancer Stroma gene set in the Oncomine cancer microarray database. Significance was determined by one-way ANOVA with Tukey post-hoc test, *p<0.05, **p<0.01, ***p<0.001, ****p<0.0001.

To validate expression of Sp7 in CAFs from primary tumors, we orthotopically injected B16-F10 or PyMT cells in 8 week old WT mice and the CAFs were isolated as the adherent fraction of a single cell suspension of the tumor mass. We detected Sp7 expression only in CAFs but not in the tumor cell lines nor in the non-adherent fraction of the single cell suspension from the tumor mass (Figure 2M and N). Importantly, corroborating our findings in mice, using Oncomine (Rhodes et al., 2004) we found that microarray analysis of human breast stromal cells collected from patients with invasive breast carcinoma from the Finak gene set (Finak et al., 2008) showed significantly higher Sp7 expression in the tumor associated stroma compared to the adjacent normal breast tissue (Figure 2O). Thus, a subset of cells in the TME of mice and humans express Sp7, an osteolineage cell marker, but also markers associated with the CAFs. TdTOSX+ cells may represent a subpopulation of CAFs with specific features.

### Tumor resident but not bone marrow resident TdTOSX+ cells increase tumor growth

To determine whether tumor resident TdTOSX+ cells can affect tumor growth as do CAFs, TdTOSX+ cells were sorted from primary B16-F10 tumors inoculated in 8 week old doxy-fed Osx-cre;TdT mice and re-injected along with B16-F10 tumor cells at 5:1 ratio into age-matched WT recipient animals (Figure 3A). Remarkably, co-injecting TdTOSX+ with tumor cells resulted in larger tumors (Figure 3B) compared to injection of B16-F10 cells alone.

![Figure 3.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig3-v2.jpg)

**Figure 3.:** (A) Model showing isolation of TdTOSX+ cells from B16-F10 primary tumors injected into doxy-fed Osx-cre;TdT mice and re-inoculation of TdTOSX+ cells together with B16-F10 tumor cells into WT recipient mice at the ratio 5:1. Mice injected with B16-F10 alone were used as controls. (B) Tumor growth of experimental model described in (A) determined by caliper measurement. n = 3/group, experiment repeated twice. Significance was determined by one-way ANOVA with Tukey post-hoc test. (C) Fluorescence images of bone sections showing presence of TdTOSX+ within the bone and bone marrow of naïve Osx-cre;TdT, Osx-cre;TdT mice inoculated subcutaneously with B16-F10 tumors or WT;TdT mice used as negative control. Sections were counterstained with DAPI (blue), magnification 200X. (D–E) Quantification of TdTOSX+ cells in the bone marrow of tumor-free and B16-F10 tumor bearing (D) Osx-cre;TdT mice (doxy-fed) and (E) Osx-creERT2;TdT (TAM-treated) determined by FACS. Experiment repeated twice. Significance was determined by student t-test statistical analysis. (F) Tumor growth of WT mice inoculated with bone marrow-derived TdTOSX+ cells from B16-F10 bearing doxy-fed Osx-cre;TdT mice together with B16-F10 tumor cells (ratio 5:1). Mice injected with B16-F10 alone were used as controls. n = 3/group. Significance was determined by two-way ANOVA followed by Tukey post-hoc test. ***p<0.001, ****p<0.0001.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Fluorescence images of WT;TdT and Osx-cre;TdT mice inoculated with PyMT tumors in the MFP. Slides for fluorescence images were counterstained with DAPI (blue), magnification 200X. (B) Quantification of TdTOSX+ cells in the bone marrow of tumor-free and PyMT bearing mice. Experiment repeated twice. p value represents Student t-test statistical analysis.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A–K) Quantitative Real-Time PCR for (A) Sp7 (Osterix), (B) Runx2, (C) Bglap (Osteocalcin), (D) Ibsp (Bone sialoprotein), (E) Alpl (Tnap, Tissue non-specific alkaline phosphatase), (F) S100a4 (Fsp1), (G) Acta2 (α-SMA), (H) Collagen 1a1, (I) Collagen 1a2, (J) Mmp2 (Metalloproteinase2) and (K) Mmp9 (Metalloproteinase9) genes in TdTOSX+ isolated from the B16-F10 melanoma primary tumors, bone marrow of B16-F10 bearing mice and bone marrow of naïve tumor-free mice.

Because TdTOSX+ cells normally reside in the bone microenvironment (Fontana et al., 2017; Strecker et al., 2013), we next examined bone sections from 8 week old doxy-fed Osx-cre;TdT reporter mice, naïve or bearing soft tissue B16-F10 or PyMT tumors. We confirmed presence of TdTOSX+ cells on the surface of cortical and trabecular bone, TdTOSX+ osteocytes, and also abundant staining in the bone marrow. TdT was not detected WT;TdT mice (Figure 3C and Figure 3—figure supplement 1A). We further analyzed the percentage of TdTOSX+ cells in the bone marrow by FACS and found that TdTOSX+ cells accounted for about 10% of total marrow cells in naïve mice and their number increased in mice injected with B16-F10 or PyMT tumor cells (Figure 3D and Figure 3—figure supplement 2B). Similar findings were observed in the Tamoxifen (TAM) inducible Sp7-creERT2; Rosa26<fs-TdTomato> (Osx-creERT2;TdT) mouse model. TAM was administered to 7 week old mice via IP injections starting 3 days prior to B16-F10 tumor inoculation, and 1, 6, and 9 days post tumor cell injection (Figure 4—figure supplement 1A). No tumor bearing mice were used as control. Similar to the Tet-OFF Osx-cre model, we found that bone marrow TdTOSX+ cells significantly increased in presence of a tumor (Figure 3E).

To test their capacity to promote tumor growth, bone marrow-derived TdTOSX+ cells were isolated from tumor bearing mice and re-injected with B16-F10 tumor cells into WT mice (5:1 ratio). In contrast to what observed with tumor-derived TdTOSX+ cells, bone marrow-derived TdTOSX+ cells did not enhance tumor growth compared to mice injected with tumor cells alone; if anything, there was a trend towards a smaller tumor size (Figure 3F). This result further prompted us to isolate bone marrow-derived TdTOSX+ cells and analyze the expression levels of the same mesenchymal genes analyzed in the tumor-derived TdTOSX+ cells (Figure 2). Interestingly, TdTOSX+ cells from the TME expressed higher levels of Sp7, CAF markers S100a4 and Acta2, and matrix proteins Col1a1 and Ibsp compared to TdTOSX+ from the bone marrow (Figure 3—figure supplement 2). Bone marrow TdTOSX+ cells instead expressed significantly higher levels of the early osteoblast transcription factor Runx2 and of the protease Mmp9, while no differences in other osteoblast markers such as Bglap and Alpl were detected between the tumor and bone marrow sorted TdTOSX+ cells (Figure 3—figure supplement 2).

These results suggest that Osx+ cells infiltrating a tumor are functionally and phenotypically distinct from bone marrow resident Osx+ cells.

### The majority of TdTOSX+ cells express CD45

To gain insights on the possible origin of tumor-derived TdTOSX+ cells, we performed FACS analysis of circulating cells in naïve mice and two weeks post B16-F10 or PyMT tumor inoculation. Interestingly, we found 5–8% of TdTOSX+ cells in the blood of tumor-free doxy-fed Osx-cre;TdT mice, and this percentage was 3- to 4-fold higher in tumor-bearing animals (Figure 4A and B). The unexpected high number of circulating TdTOSX+ cells prompted us to determine whether they may express the immune marker CD45, which is also present in fibrocytes. Surprisingly, 95% of TdTOSX+ cells in circulation of tumor bearing mice were also positive for CD45, and they represented about 13–18% of total blood cells (Figure 4C and D). Similarly, about 92–95% of total TdTOSX+ cells in the bone marrow were CD45+ (Figure 4E and F), representing 12–20% of total marrow cells. Such finding explained the low expression levels of mesenchymal markers in the bone marrow-derived TdTOSX+ cells (Figure 3—figure supplement 2). Intriguingly, also the majority of TdTOSX+ cells in the TME expressed CD45 (Figure 4G and H), data further confirmed by RT-PCR in TdTOSX+ fraction sorted from B16-F10 tumors (not shown).

![Figure 4.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig4-v2.jpg)

**Figure 4.:** (A–B) Representative FACS dot plots and quantification of TdTOSX+ cells in the peripheral blood of tumor-free and B16-F10 or PyMT tumor bearing mice. Significance was determined by student t-test statistical analysis for each tumor model relative to no tumor controls. (C–D) Representative FACS dot plots and quantification of TdTOSX+;CD45+ and TdTOSX+;CD45- populations in the blood of doxy-fed Osx-cre;TdT mice injected with B16-F10 or PyMT cells. (E–H) Representative FACS dot plots and quantification of TdTOSX+;CD45+ and TdTOSX+;CD45- populations in the bone marrow (E–F) or tumor site (G–H) of doxy-fed Osx-cre;TdT mice injected with B16-F10 or PyMT cells, respectively. Experiments were repeated at least twice. (I) Immunohistochemistry staining of paraffin-embedded B16-F10 tumors inoculated into Osx-cre;TdT reporter mice, pseudo colored with red representing TdTOSX+ cells (RFP stained), green representing CD45+ cells (DAB stained) and blue representing nuclei (hematoxylin), magnification 200X.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Schematic representation of TAM administration and tumor injection in Osx-creERT2;TdT mice. (B) Representative image of flow cytometry dot plots and quantification of TdTOSX+;CD45+ and TdTOSX+;CD45- populations in the bone marrow of B16-F10 bearing mice. A cre negative mouse was used as control to set gates. Experiment was repeated three times.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Immunofluorescence on paraffin-embedded B16-F10 tumors isolated from Osx-cre;TdT reporter mice. Staining was done using anti-RFP (red) to detect TdTomato and anti-CD45 (green) to stain immune populations. Slides were counterstained with DAPI (blue), magnification 200X. (B) Staining for CD45 on a single cell suspension from bone marrow of Osx-cre;TdT reporter mice, magnification 200X. Yellow arrows point to TdTOSX+ single cells expressing CD45, while the white arrow points to a TdTOSX+ cell negative for CD45.

To exclude a possible off-target effect of the doxy-dependent Tet-OFF system, we turned to the TAM inducible Osx-creERT2;TdT model. FACS analysis confirmed presence of both CD45- and CD45+ TdTOSX+ populations in the bone marrow of B16-F10 bearing Osx-creERT2;TdT mice, but not in the cre negative mice (Figure 4—figure supplement 1B).

Next, to confirm that expression of CD45 in the TdTOSX+ cells was not due a tight interaction between a CD45+ immune cell and TdTOSX+ mesenchymal cell, we performed CD45 immunostaining on paraffin-embedded B16-F10 tumor sections and on bone marrow single cell suspension from Osx-cre;TdT reporter mice. We found co-localization of Osx-driven TdTomato and CD45 in the same cell, confirming that CD45 is indeed expressed in subsets of TdTOSX+ cells (Figure 4I and Figure 4—figure supplement 2). Thus, Osx not only marks mesenchymal cells, but also cells expressing the hematopoietic marker CD45, suggesting that they could represent bone marrow fibrocytes or an immune cell subset.

### Presence of functionally distinct populations of TdTOSX+ cells in the tumor microenvironment

To further characterize the phenotype of the CD45- and CD45+ TdTOSX+ populations, we next performed RNAseq analysis. We subcutaneously injected the GFP-labeled PyMT-BO1-tumor line in Osx-cre;TdT reporter mice. Two weeks post tumor inoculation, the stromal cells were separated from the GFP+ tumor cells and sorted based on the expression, or lack of thereof, of TdT and CD45 markers. We sorted 4 groups of cells: double negative (TdTOSX-;CD45-), representing the non-immune tumor stroma, CD45 single positive (TdTOSX-;CD45+), representing the tumor infiltrating immune populations, TdTOSX single positive (TdTOSX+;CD45-), and double positive (TdTOSX+;CD45+).

Principal components analysis of RNA-seq expression patterns across all four groups revealed clustering that was uniquely dependent on CD45 expression and suggested that there were only two very distinct cell populations regardless of TdTOSX (Figure 5A). Inspection of each cell population in a one versus all other approach for only statistically significant up-regulated genes (FDR >= 0.05, log2 fold-change >= 2) to identify robustly expressed biomarkers, showed that all four groups shared many genes in common based on CD45 expression alone. The CD45 negative populations shared 1248 genes in common with 536 in the TdTOSX single positive and 477 in the double negative cells uniquely up-regulated (Figure 5B). Likewise, the CD45 single and double positive cells shared 495 significantly up-regulated genes with an additional 77 and 316 uniquely expressed, respectively.

![Figure 5.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig5-v2.jpg)

**Figure 5.:** (A) Multidimensional Principal Component Analysis of RNAseq data obtained from four tumor stroma subsets sorted according to TdTOSX and CD45 expression. (B) Venn diagram depicting uniquely and commonly expressed genes among the four groups. (C–D) First ten GO pathways obtained from the GO analysis of the log two fold-changes for (C) CD45 negative subsets and (D) CD45 positive subsets.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Real Time PCR performed on TdTOSX+;CD45+ and TdTOSX+;CD45- populations sorted from B16-F10 tumors in doxy-fed mice. Each sample is a pool of two tumors. Data show three genes (A) Cd163l1, (B) Wdr79 and (C) Spock2 to be upregulated in the TdTOSX+;CD45+ compared to TdTOSX-;CD45+ cells.

Subsequent Gene Ontology (GO) analysis of the log2 fold-changes for each cell population revealed that the CD45 negative subsets showed upregulation of GO pathways related to cellular responses to growth factors, extracellular structure and matrix organization and skeletal system development, confirming their mesenchymal nature (Figure 5C). Among the top upregulated genes in the TdTOSX single positive cells versus the double negative (Table 1) we found several markers expressed by osteolinage cells, such as fibromodulin (Fmod), a binding protein regulating bone mineralization (Gori et al., 2001) and also involved in TGFβ signaling during cancer pathogenesis (Pourhanifeh et al., 2019), Collagen 24a1 (Col24a1), known to modulate collagen chain trimerization (Koch et al., 2003; Matsuo et al., 2006), Frem1, a protein involved in the formation and organization of basement membranes (Vissers et al., 2011), and Msx1, a transcription factor important in craniofacial bone development (Orestes-Cardoso et al., 2002). TdTOSX single positive cells also expressed high levels of fibulin 7 (Fbln7), a cell adhesion molecule overexpressed in glioblastoma by pericytes and involved in neovascularization (de Vega et al., 2019; Ikeuchi et al., 2018). Such result confirmed the osteolineage nature of the TdTOSX+ cells and indicated their tumor supporting role.

**Table 1.**
 Top 50 uniquely up-regulated genes in tumor-derived TdTOSX+;CD45- cells.List of the 50 most highly expressed genes in the TdTOSX+;CD45- cells compared to the TdTOSX-;CD45- cells isolated from the TME.


<table>
  <thead>
    <tr>
      <th>external_gene_name</th>
      <th>description</th>
      <th>TdTOSX+CD45- logFC</th>
      <th>TdTOSX+CD45- linearFC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Reg1</td>
      <td>regenerating islet-derived 1</td>
      <td>7.675801</td>
      <td>204.477899</td>
    </tr>
    <tr>
      <td>Fbln7</td>
      <td>fibulin 7</td>
      <td>7.184048</td>
      <td>145.416614</td>
    </tr>
    <tr>
      <td>Adcyap1r1</td>
      <td>adenylate cyclase activating polypeptide 1 receptor 1</td>
      <td>6.864422</td>
      <td>116.51905</td>
    </tr>
    <tr>
      <td>Col24a1</td>
      <td>collagen, type XXIV, alpha 1</td>
      <td>6.788179</td>
      <td>110.521192</td>
    </tr>
    <tr>
      <td>Moxd1</td>
      <td>monooxygenase, DBH-like 1</td>
      <td>6.74623</td>
      <td>107.35382</td>
    </tr>
    <tr>
      <td>Fmod</td>
      <td>fibromodulin</td>
      <td>6.739645</td>
      <td>106.864989</td>
    </tr>
    <tr>
      <td>4930562D21Rik</td>
      <td>RIKEN cDNA 4930562D21 gene</td>
      <td>6.149924</td>
      <td>71.008705</td>
    </tr>
    <tr>
      <td>Angpt4</td>
      <td>angiopoietin 4</td>
      <td>6.131627</td>
      <td>70.113799</td>
    </tr>
    <tr>
      <td>Tmem132c</td>
      <td>transmembrane protein 132C</td>
      <td>5.933002</td>
      <td>61.095844</td>
    </tr>
    <tr>
      <td>Frem1</td>
      <td>Fras1 related extracellular matrix protein 1</td>
      <td>5.906166</td>
      <td>59.969876</td>
    </tr>
    <tr>
      <td>Cxcl5</td>
      <td>chemokine (C-X-C motif) ligand 5</td>
      <td>5.88881</td>
      <td>59.252728</td>
    </tr>
    <tr>
      <td>Ccl19</td>
      <td>chemokine (C-C motif) ligand 19</td>
      <td>5.748355</td>
      <td>53.756054</td>
    </tr>
    <tr>
      <td>Rab15</td>
      <td>RAB15, member RAS oncogene family</td>
      <td>5.696057</td>
      <td>51.842269</td>
    </tr>
    <tr>
      <td>Prlr</td>
      <td>prolactin receptor</td>
      <td>5.673651</td>
      <td>51.04334</td>
    </tr>
    <tr>
      <td>Msx1</td>
      <td>msh homeobox 1</td>
      <td>5.657661</td>
      <td>50.480738</td>
    </tr>
    <tr>
      <td>Pabpc4l</td>
      <td>poly(A) binding protein, cytoplasmic 4-like</td>
      <td>5.657301</td>
      <td>50.46814</td>
    </tr>
    <tr>
      <td>Reg3g</td>
      <td>regenerating islet-derived 3 gamma</td>
      <td>5.651841</td>
      <td>50.2775</td>
    </tr>
    <tr>
      <td>Rflna</td>
      <td>refilin A</td>
      <td>5.651765</td>
      <td>50.274843</td>
    </tr>
    <tr>
      <td>Adamts3</td>
      <td>a disintegrin-like and metallopeptidase (reprolysin type) with thrombospondin type 1 motif, 3</td>
      <td>5.52646</td>
      <td>46.092506</td>
    </tr>
    <tr>
      <td>Lrp3</td>
      <td>low density lipoprotein receptor-related protein 3</td>
      <td>5.465865</td>
      <td>44.196651</td>
    </tr>
    <tr>
      <td>Clstn2</td>
      <td>calsyntenin 2</td>
      <td>5.41628</td>
      <td>42.703438</td>
    </tr>
    <tr>
      <td>Adam5</td>
      <td>a disintegrin and metallopeptidase domain 5</td>
      <td>5.36495</td>
      <td>41.210775</td>
    </tr>
    <tr>
      <td>H2-M11</td>
      <td>histocompatibility 2, M region locus 11</td>
      <td>5.335531</td>
      <td>40.378937</td>
    </tr>
    <tr>
      <td>Ptx3</td>
      <td>pentraxin related gene</td>
      <td>5.320565</td>
      <td>39.962237</td>
    </tr>
    <tr>
      <td>Rtl3</td>
      <td>retrotransposon Gag like 3</td>
      <td>5.252916</td>
      <td>38.131634</td>
    </tr>
    <tr>
      <td>Gm26682</td>
      <td>predicted gene, 26682</td>
      <td>5.252803</td>
      <td>38.128648</td>
    </tr>
    <tr>
      <td>Morc1</td>
      <td>microrchidia 1</td>
      <td>5.251594</td>
      <td>38.096689</td>
    </tr>
    <tr>
      <td>Hoxc6</td>
      <td>homeobox C6</td>
      <td>5.176329</td>
      <td>36.160165</td>
    </tr>
    <tr>
      <td>Mcpt8</td>
      <td>mast cell protease 8</td>
      <td>5.146576</td>
      <td>35.422062</td>
    </tr>
    <tr>
      <td>Gabrb3</td>
      <td>gamma-aminobutyric acid (GABA) A receptor, subunit beta 3</td>
      <td>5.110873</td>
      <td>34.556218</td>
    </tr>
    <tr>
      <td>Sbspon</td>
      <td>somatomedin B and thrombospondin, type 1 domain containing</td>
      <td>5.085426</td>
      <td>33.952042</td>
    </tr>
    <tr>
      <td>Akap6</td>
      <td>A kinase (PRKA) anchor protein 6</td>
      <td>5.073102</td>
      <td>33.663235</td>
    </tr>
    <tr>
      <td>Hmcn1</td>
      <td>hemicentin 1</td>
      <td>5.060346</td>
      <td>33.366905</td>
    </tr>
    <tr>
      <td>Aqp2</td>
      <td>aquaporin 2</td>
      <td>5.031264</td>
      <td>32.701036</td>
    </tr>
    <tr>
      <td>Gria3</td>
      <td>glutamate receptor, ionotropic, AMPA3 (alpha 3)</td>
      <td>5.011924</td>
      <td>32.265589</td>
    </tr>
    <tr>
      <td>AI464131</td>
      <td>expressed sequence AI464131</td>
      <td>5.001414</td>
      <td>32.03138</td>
    </tr>
    <tr>
      <td>Muc13</td>
      <td>mucin 13, epithelial transmembrane</td>
      <td>4.997132</td>
      <td>31.936452</td>
    </tr>
    <tr>
      <td>Syt4</td>
      <td>synaptotagmin IV</td>
      <td>4.994666</td>
      <td>31.881898</td>
    </tr>
    <tr>
      <td>Spon1</td>
      <td>spondin 1, (f-spondin) extracellular matrix protein</td>
      <td>4.916033</td>
      <td>30.190712</td>
    </tr>
    <tr>
      <td>Caln1</td>
      <td>calneuron 1</td>
      <td>4.85996</td>
      <td>29.039801</td>
    </tr>
    <tr>
      <td>Hoxc4</td>
      <td>homeobox C4</td>
      <td>4.844155</td>
      <td>28.723415</td>
    </tr>
    <tr>
      <td>Tbx2</td>
      <td>T-box 2</td>
      <td>4.842042</td>
      <td>28.681376</td>
    </tr>
    <tr>
      <td>Jph2</td>
      <td>junctophilin 2</td>
      <td>4.816833</td>
      <td>28.18456</td>
    </tr>
    <tr>
      <td>Frzb</td>
      <td>frizzled-related protein</td>
      <td>4.79214</td>
      <td>27.706253</td>
    </tr>
    <tr>
      <td>Galnt5</td>
      <td>polypeptide N-acetylgalactosaminyltransferase 5</td>
      <td>4.77782</td>
      <td>27.432606</td>
    </tr>
    <tr>
      <td>Gm29100</td>
      <td>predicted gene 29100</td>
      <td>4.77255</td>
      <td>27.332593</td>
    </tr>
    <tr>
      <td>Tspyl5</td>
      <td>testis-specific protein, Y-encoded-like 5</td>
      <td>4.771509</td>
      <td>27.312867</td>
    </tr>
    <tr>
      <td>Spag17</td>
      <td>sperm associated antigen 17</td>
      <td>4.770653</td>
      <td>27.296671</td>
    </tr>
    <tr>
      <td>Ldoc1</td>
      <td>regulator of NFKB signaling</td>
      <td>4.7479</td>
      <td>26.86954</td>
    </tr>
    <tr>
      <td>4833422C13Rik</td>
      <td>RIKEN cDNA 4833422C13 gene</td>
      <td>4.730678</td>
      <td>26.550693</td>
    </tr>
  </tbody>
</table>

Conversely, both CD45+ subsets were significantly up-regulated for GO pathways related to regulation of lymphocyte activation and proliferation, and innate immune cell responses (Figure 5D). Interestingly, among the top genes upregulated in the TdTOSX+ CD45+ subsets versus the CD45 single positive populations (Table 2), we found many genes expressed by tumor promoting immune cells, such as regulatory T cells (i.e. Foxp3) and gamma-delta T cells (i.e. Tcrg-C1). The most upregulated gene in the TdTOSX+;CD45+ subset (>80 fold versus CD45 single positive) was Cd163l1, a marker of gamma-delta IL-17 producing cells (Tan et al., 2019) and M2 macrophages (González-Domínguez et al., 2015), two tumor-promoting immune populations. We confirmed Cd163l1 higher expression by RT-PCR together with other two genes, Wdr78 and Spock2, also upregulated in the double positive cells (Figure 5—figure supplement 1). The second most expressed gene was Lymphotoxin beta (Ltb), a cytokine produced by lymphocytes and NK cells and associated with carcinogenesis (Wolf et al., 2010). The third one, Klrg1, negatively regulates cytotoxic lymphocytes and is associated with lymphocyte senescence and dysfunction (Henson and Akbar, 2009). Thus, these analyses revealed that two main transcriptional programs predominate based on CD45 expression, and suggest that TdTOSX+;CD45- comprise a subset of CAFs with some characteristics of skeletal cells, while TdTOSX+;CD45+ cells represent a heterogeneous subset of tumor-promoting immune cells.

**Table 2.**
 Top 50 uniquely up-regulated genes in tumor-derived TdTOSX+;CD45+ cells.List of the 50 most highly expressed genes in the TdTOSX+;CD45+ cells compared to the TdTOSX-;CD45+ cells isolated from the TME.


<table>
  <thead>
    <tr>
      <th>external_gene_name</th>
      <th>description</th>
      <th>TdTOSX+CD45+logFC</th>
      <th>TdTOSX+CD45+linearFC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cd163l1</td>
      <td>CD163 molecule-like 1</td>
      <td>6.482112</td>
      <td>89.394369</td>
    </tr>
    <tr>
      <td>Ltb</td>
      <td>lymphotoxin B</td>
      <td>6.217037</td>
      <td>74.389998</td>
    </tr>
    <tr>
      <td>Klrg1</td>
      <td>killer cell lectin-like receptor subfamily G, member 1</td>
      <td>5.915697</td>
      <td>60.367363</td>
    </tr>
    <tr>
      <td>Foxp3</td>
      <td>forkhead box P3</td>
      <td>5.882423</td>
      <td>58.991007</td>
    </tr>
    <tr>
      <td>Trbv19</td>
      <td>T cell receptor beta, variable 19</td>
      <td>5.83901</td>
      <td>57.242322</td>
    </tr>
    <tr>
      <td>Cd5</td>
      <td>CD5 antigen</td>
      <td>5.822965</td>
      <td>56.609196</td>
    </tr>
    <tr>
      <td>Gm4759</td>
      <td>predicted gene 4759</td>
      <td>5.712238</td>
      <td>52.426999</td>
    </tr>
    <tr>
      <td>Tcrg-C1</td>
      <td>T cell receptor gamma, constant 1</td>
      <td>5.709921</td>
      <td>52.342868</td>
    </tr>
    <tr>
      <td>Icos</td>
      <td>inducible T cell co-stimulator</td>
      <td>5.588856</td>
      <td>48.129715</td>
    </tr>
    <tr>
      <td>Gm19585</td>
      <td>predicted gene, 19585</td>
      <td>5.577582</td>
      <td>47.755056</td>
    </tr>
    <tr>
      <td>Fasl</td>
      <td>Fas ligand (TNF superfamily, member 6)</td>
      <td>5.571314</td>
      <td>47.548033</td>
    </tr>
    <tr>
      <td>Rln3</td>
      <td>relaxin 3</td>
      <td>5.518062</td>
      <td>45.824955</td>
    </tr>
    <tr>
      <td>Ubash3a</td>
      <td>ubiquitin associated and SH3 domain containing, A</td>
      <td>5.432308</td>
      <td>43.180511</td>
    </tr>
    <tr>
      <td>Pcsk1</td>
      <td>proprotein convertase subtilisin/kexin type 1</td>
      <td>5.376329</td>
      <td>41.537117</td>
    </tr>
    <tr>
      <td>Ccr8</td>
      <td>chemokine (C-C motif) receptor 8</td>
      <td>5.32423</td>
      <td>40.06386</td>
    </tr>
    <tr>
      <td>Gimap3</td>
      <td>GTPase, IMAP family member 3</td>
      <td>5.257508</td>
      <td>38.253185</td>
    </tr>
    <tr>
      <td>Slamf1</td>
      <td>signaling lymphocytic activation molecule family member 1</td>
      <td>5.220641</td>
      <td>37.288037</td>
    </tr>
    <tr>
      <td>Klrb1f</td>
      <td>killer cell lectin-like receptor subfamily B member 1F</td>
      <td>5.204067</td>
      <td>36.86212</td>
    </tr>
    <tr>
      <td>Ikzf3</td>
      <td>IKAROS family zinc finger 3</td>
      <td>5.185332</td>
      <td>36.386518</td>
    </tr>
    <tr>
      <td>Trdv4</td>
      <td>T cell receptor delta variable</td>
      <td>5.179288</td>
      <td>36.234394</td>
    </tr>
    <tr>
      <td>Trat1</td>
      <td>T cell receptor associated transmembrane adaptor 1</td>
      <td>5.144648</td>
      <td>35.374755</td>
    </tr>
    <tr>
      <td>Pdcd1</td>
      <td>programmed cell death 1</td>
      <td>5.092017</td>
      <td>34.107504</td>
    </tr>
    <tr>
      <td>Izumo1r</td>
      <td>IZUMO1 receptor, JUNO</td>
      <td>5.053635</td>
      <td>33.212045</td>
    </tr>
    <tr>
      <td>Cd3e</td>
      <td>CD3 antigen, epsilon polypeptide</td>
      <td>5.042174</td>
      <td>32.949246</td>
    </tr>
    <tr>
      <td>Itk</td>
      <td>IL2 inducible T cell kinase</td>
      <td>5.027182</td>
      <td>32.608632</td>
    </tr>
    <tr>
      <td>Ctla4</td>
      <td>cytotoxic T-lymphocyte-associated protein 4</td>
      <td>4.978043</td>
      <td>31.516668</td>
    </tr>
    <tr>
      <td>Actn2</td>
      <td>actinin alpha 2</td>
      <td>4.919967</td>
      <td>30.27316</td>
    </tr>
    <tr>
      <td>Trbv1</td>
      <td>T cell receptor beta, variable 1</td>
      <td>4.891164</td>
      <td>29.674756</td>
    </tr>
    <tr>
      <td>Dkkl1</td>
      <td>dickkopf-like 1</td>
      <td>4.820628</td>
      <td>28.258804</td>
    </tr>
    <tr>
      <td>Cd300e</td>
      <td>CD300E molecule</td>
      <td>4.801355</td>
      <td>27.883791</td>
    </tr>
    <tr>
      <td>Pglyrp2</td>
      <td>peptidoglycan recognition protein 2</td>
      <td>4.80032</td>
      <td>27.863797</td>
    </tr>
    <tr>
      <td>Cd226</td>
      <td>CD226 antigen</td>
      <td>4.766441</td>
      <td>27.21709</td>
    </tr>
    <tr>
      <td>Themis</td>
      <td>thymocyte selection associated</td>
      <td>4.760082</td>
      <td>27.097397</td>
    </tr>
    <tr>
      <td>Dpep3</td>
      <td>dipeptidase 3</td>
      <td>4.694473</td>
      <td>25.892693</td>
    </tr>
    <tr>
      <td>Cd209a</td>
      <td>CD209a antigen</td>
      <td>4.650261</td>
      <td>25.111233</td>
    </tr>
    <tr>
      <td>Cd27</td>
      <td>CD27 antigen</td>
      <td>4.648725</td>
      <td>25.084512</td>
    </tr>
    <tr>
      <td>Gpr55</td>
      <td>G protein-coupled receptor 55</td>
      <td>4.621113</td>
      <td>24.608975</td>
    </tr>
    <tr>
      <td>Ccr6</td>
      <td>chemokine (C-C motif) receptor 6</td>
      <td>4.596004</td>
      <td>24.18439</td>
    </tr>
    <tr>
      <td>Gpr174</td>
      <td>G protein-coupled receptor 174</td>
      <td>4.594683</td>
      <td>24.16225</td>
    </tr>
    <tr>
      <td>A630023P12Rik</td>
      <td>RIKEN cDNA A630023P12 gene</td>
      <td>4.586499</td>
      <td>24.025577</td>
    </tr>
    <tr>
      <td>Cd28</td>
      <td>CD28 antigen</td>
      <td>4.564255</td>
      <td>23.657981</td>
    </tr>
    <tr>
      <td>Cd3g</td>
      <td>CD3 antigen, gamma polypeptide</td>
      <td>4.547609</td>
      <td>23.386577</td>
    </tr>
    <tr>
      <td>Lta</td>
      <td>lymphotoxin A</td>
      <td>4.534293</td>
      <td>23.171712</td>
    </tr>
    <tr>
      <td>Ccr3</td>
      <td>chemokine (C-C motif) receptor 3</td>
      <td>4.526527</td>
      <td>23.047318</td>
    </tr>
    <tr>
      <td>Gzmb</td>
      <td>granzyme B</td>
      <td>4.518658</td>
      <td>22.921957</td>
    </tr>
    <tr>
      <td>Lrrc66</td>
      <td>leucine rich repeat containing 66</td>
      <td>4.47147</td>
      <td>22.184347</td>
    </tr>
    <tr>
      <td>Xirp2</td>
      <td>xin actin-binding repeat containing 2</td>
      <td>4.462937</td>
      <td>22.053513</td>
    </tr>
    <tr>
      <td>St8sia1</td>
      <td>ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 1</td>
      <td>4.460924</td>
      <td>22.022769</td>
    </tr>
    <tr>
      <td>Sit1</td>
      <td>suppression inducing transmembrane adaptor 1</td>
      <td>4.417363</td>
      <td>21.367754</td>
    </tr>
    <tr>
      <td>Tnfrsf4</td>
      <td>tumor necrosis factor receptor superfamily, member 4</td>
      <td>4.381868</td>
      <td>20.84844</td>
    </tr>
  </tbody>
</table>

### Double positive TdTOSX+;CD45+ cells are a heterogeneous immune population enriched in lymphoid cells

Next we performed flow cytometry analysis to better characterize the TdTOSX+;CD45+ population and validate some of the RNAseq findings using the B16-F10 melanoma model. We confirmed that the double positive TdTOSX+;CD45+ represented about 20% of the total CD45+ cells in both the primary tumor and the bone marrow of doxy-fed Osx-cre;TdT mice (Figure 6A and B). Next, we analyzed the percentage of TdTOSX+ expressing the common myeloid and lymphoid markers (gate strategy in Figure 6—figure supplement 1), such as CD11b (monocytes), F4/80 (macrophages), Gr1 (granulocytes/neutrophils), CD3 (T cells, further divided into CD4+ and CD8+), and NK1.1 (Natural Killer cells). To standardize the comparison between the TdTOSX+;CD45+ and TdTOSX-;CD45+ (single positive) populations within each sample, data were represented as percentage of either total TdTOSX+;CD45+ or total CD45 single positive cells (Figure 6C and D). TdTOSX+;CD45+ subset expressed both myeloid and lymphoid markers, with a similar pattern as the CD45 single positive cells. In both subsets, the majority of the tumor immune infiltrate included myeloid populations, which represented about 60% of the TdTOSX+;CD45+ and over 70% of the total CD45 single positive cells. Lymphoid cells appeared to be more abundant among the TdTOSX+;CD45+ (32.3 ± 6.5%), compared to the TdTOSX-;CD45+ cells (23.3 ± 4.3%). Based on this observation, we calculated the ratio of lymphoid over myeloid populations and observed that the tumor-infiltrating TdTOSX+;CD45+ double positive population was enriched in lymphoid cells (Figure 6E). Flow cytometric analysis of the bone marrow from tumor bearing Osx-cre;TdT mice revealed similar pattern of distribution between the TdTOSX+;CD45+ and the CD45 single positive immune populations (Figure 6F and G), although the frequencies of each immune subset in the bone marrow differed compared to the cells at tumor site. These data suggest that Osx marks multiple immune cell types but that TdTOSX+-derived immune cells infiltrating a tumor are skewed towards lymphoid populations.

![Figure 6.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig6-v2.jpg)

**Figure 6.:** (A–B) Quantification of FACS analysis showing the percentage of TdTOSX+;CD45+ and TdTOSX-;CD45+ populations in the tumor and bone marrow of Osx-cre;TdT mice injected subcutaneously with B16-F10 tumor cells. Data showed as % of total CD45+ cells. (C–D) Quantification of FACS analysis showing the percentage of tumor infiltrating myeloid and lymphoid populations within the TdTOSX+;CD45+ or TdTOSX-;CD45+ subsets, each considered as 100%. (E) Lymphoid over myeloid ratio within the tumor infiltrating TdTOSX+;CD45+ or the TdTOSX-;CD45+ subsets. Statistical analysis was performed by student t-test. (F–G) Quantification of FACS analysis showing the percentage of the bone marrow resident myeloid and lymphoid populations within the TdTOSX+;CD45+ or TdTOSX-;CD45+ subsets, each considered as 100%. n = 3/group. (H) Tumor growth in mice injected with B16-F10 tumor cells alone or together with tumor-derived TdTOSX+;CD45+ or TdTOSX-;CD45+ cells at the ratio 1:5. n = 3–6/group.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Representative gate strategy analysis of total tumor mass stained for CD45, myeloid immune markers CD11b, F4/80 and Gr1. Analysis performed in both TdTOSX+ and TdTOSX- populations. Identical analysis was performed on BM samples. (B) Representative gate strategy analysis of BM stained for lymphoid immune markers CD3, CD8, CD4 and NK1.1. Analysis performed in both TdTOSX+ and TdTOSX- populations. Identical analysis was performed on tumor samples. Fluorescence minus one (FMO) controls were used to set the gates. WT;TdT mice were used to set the gate for TdT+ cells.

Since adoptive transfer of tumor-derived TdTOSX+ cells increases tumor growth (Figure 3B), we asked whether TdTOSX+;CD45+ immune populations contribute to tumor progression. We isolated by FACS sorting TdTOSX+;CD45+ and the TdTOSX-;CD45+ from B16-F10 subcutaneous tumors from doxy-fed Osx-Cre;TdT mice. Sorted cells were then re-injected along with B16-F10 tumor cells (ratio 5:1) into new WT recipient mice. The co-injection of CD45 single positive cells decreased tumor growth relative to B16-F10 injected alone at day 15, while TdTOSX+;CD45+ did not show anti-tumor effects (Figure 6H).

Collectively, these data indicate that Sp7 marks cells of both mesenchymal and hematopoietic origin to support the development of tumor promoting populations.

### Double positive TdTOSX+;CD45+ cells derive from TdTOSX+ HSCs

To determine whether Sp7 may be activated at early stages of hematopoiesis as a potential explanation for the heterogeneity of TdTOSX+;CD45+ cells, we performed flow cytometric analysis for hematopoietic stem cell (HSC) markers in the bone marrow of doxy-fed Osx-cre;TdT and TAM-induced Osx-creERT2;TdT mice bearing B16-F10 tumors subcutaneously. We analyzed the lineage negative (Lin-) LSK and LK populations (Figure 7A) gated based on the expression of Sca1 and c-kit and found 10.9–11.45% TdTOSX+ LSK and 7.08–8.94% TdTOSX+ LK in Osx-cre;TdT and Osx-creERT2;TdT mice, respectively (Figure 7B and D). The LSK population was further divided into HSC and multipotent progenitor MPP(1-4) subsets (Figure 7A and gate strategy in Figure 7—figure supplement 1). Interestingly, TdTOSX+ cells represented about 30% of MPP1, and between 7–11% of the MPP2-MPP3 and MPP4 subsets in Osx-cre;TdT mice (Figure 7C). Similar results were also obtained in Osx-creERT2;TdT mice (Figure 7E). The slight difference in frequency between the two mouse models could depend on the different timing of Cre activation, but both models succeeded to find TdTOSX+ cells in HSCs.

![Figure 7.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig7-v2.jpg)

**Figure 7.:** (A) Schematic of hematopoietic differentiation. (B–E) Flow cytometry quantification of TdTOSX+ cells in the bone marrow of (B–C) doxy-fed Osx-cre;TdT mice and (D–E) TAM-treated Osx-creERT2;TdT mice injected subcutaneously at 7 weeks of age with B16-F10 tumors. In (B and D) LSK and LK subsets are shown, while in (C and E) the LSK population is further divided into HSCs and MPP1-4 subsets. Red numbers represent the average of TdTOSX+ cells in each specific subset. n = 2–6/group.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Representative gate strategy analysis of bone marrow stained for HSC subsets. TdTOSX+ cells were quantified in each subset. Fluorescence minus one (FMO) controls were used to set the gates. WT;TdT mice were used to set the gate for TdT+ cells.

Importantly, RT-PCR of isolated HSCs from the bone marrow of 7–8 week old wild-type naïve mice showed Sp7 expression compared to the TdTOSX- fraction isolated from the tumor mass, used as negative control (Figure 8A). Similarly, Sp7 transcripts were found in the MPP1-4 subsets, and in the common lymphoid progenitors CLP, but not in the common myeloid progenitors CMP (Figure 8A). In contrast, RT-PCR analysis of mature immune populations from naïve mice (macrophages, dendritic cells and T cells) failed to detect Sp7 expression (Figure 8B). Finally, we performed immunostaining for Osx to confirm protein expression on a single cell level. To enrich for Osx+ cells, we FACS sorted TdTOSX+ HSCs from the bone marrow of Osx-cre;TdT reporter mice after enrichment for c-kit+ cells. Sorted cells were plated on serum-coated coverslips for two days before immunostaining for Osx and with DAPI for nuclear localization. We confirmed Osx localization in the nuclei of the majority of TdTOSX+ HSCs (Figure 8D). As positive control for Osx staining, we used bone marrow stromal cells isolated from WT mice cultured for 4 days in osteogenic medium (Figure 8C). Whole bone marrow was used as additional control confirming that only a small number of cells expressed Osx while the majority was negative (Figure 8E). Thus, for the first time we show that subsets of HSCs express the transcription factor Sp7, giving rise to tumor infiltrating immune populations.

![Figure 8.](https://cdn.elifesciences.org/articles/54659/elife-54659-fig8-v2.jpg)

**Figure 8.:** (A) Real Time PCR analysis comparing sorted hematopoietic stem cells (HSC), multipotent progenitors (MPP), common myeloid progenitors (CMP), common lymphoid progenitors (CLP) and whole bone marrow (WBM) from 7 to 9 week old mice. FACS sorted TdTOSX- cells from the tumor of Osx-cre;TdT mice were used as negative control (n = 3–8/group). Statistical analysis was determined by two-way ANOVA followed by Tukey post-hoc test. *p<0.05, **p<0.01, ***p<0.001, ****p<0.0001. (B) Real Time PCR analysis of isolated mature CD3+ T cells, conventional dendritic cells (cDC) and bone marrow-derived macrophages (mφ) from WT naïve mice. (C–E) Immunofluorescence for Osx in (C) primary osteoblasts differentiated from BMSC cultured for 4 days in osteogenic media, (D) TdTOSX+ HSCs sorted from Osx-cre;TdT reporter mice and (E) whole bone marrow cells from WT mice. DAPI is used for nuclear staining. Magnification 200X.

## Discussion

Numerous studies have established the importance of the TME for primary tumor growth and metastatic dissemination (Goubran et al., 2014). In skeletal metastases, crosstalk between bone residing cells, osteoblasts and osteoclasts, and tumor cells drives tumor growth (Weilbaecher et al., 2011). Recent studies also suggest that osteoblasts and their secretory products stimulate the expansion of bone marrow-derived myeloid populations, which in turn escape the bone marrow and reach distant sites to support tumor growth by inhibiting anti-tumor immune responses (D'Amico et al., 2016; Engblom et al., 2017). Our study demonstrates that a transcription factor required for osteoblast differentiation, Osterix, marks pro-tumorigenic stromal cells infiltrating extra-skeletal tumors. A possible role of Osx in tumorigenesis is emerging from human studies as well showing that presence of Sp7 in the tumor is associated with poor patient survival (Yao et al., 2019). Our own analysis of published gene microarray data of breast cancer stroma (Finak et al., 2008), reveals higher Sp7 expression in tumor stroma relative to healthy tissue from the same subject, corroborating the notion that Osx+ stromal cells regulate tumor growth. Therefore, Osx function may well extend beyond its known role in bone development and homeostasis.

Osterix has been primarily studied in the context of osteoblast differentiation and regulation of bone mass. Sp7 deficient mice die within 1 hr of birth with a complete absence of intramembranous and endochondral bone formation (Nakashima et al., 2002; Baek et al., 2009). During embryogenesis and perinatally, Sp7 is expressed in MSCs in the bone marrow, and it is necessary for the full osteogenic program. In adult mice, Sp7 is mainly confined to committed osteoblasts and osteocytes. There is increasing evidence of Sp7 expression in cells residing outside the skeleton, including synovial fibroblasts (Miura et al., 2019), dental pulp (Monterubbianesi et al., 2019), olfactory glomerular cells, gastric and intestinal epithelium (Chen et al., 2014), and kidney (Strecker et al., 2013). Here we demonstrate that Sp7 is also present in a CAF subset, and in hematopoietic precursors, thus challenging the dogma that Sp7 is exclusively expressed by mesenchymal cells. Our cell tracking studies using the repressible Tet-OFF Osx-cre;TdT reporter and the tamoxifen-inducible Osx-creERT2;TdT model demonstrate the presence of TdTOSX+;CD45+ cells in the bone marrow of adult mice. At least two other independent studies have also shown abundant and persistent Osx+ cells in the bone marrow when the reporter gene is activated either embryonically or neonatally (Liu et al., 2013; Mizoguchi et al., 2014), and at 3 weeks of age (Strecker et al., 2013), but no signal in the bone marrow when the Osx-cre is activated after 8 weeks of age (Mizoguchi et al., 2014). Notably, most of the studies with Osx-cre reporter mice have excluded the hematopoietic marker CD45 in the analysis of the Osx+ populations, and no report to date has shown Sp7 expression in the hematopoietic compartment. Importantly, we also report that bone marrow residing TdTOSX+ populations expand during tumor progression. Such result is highly unlikely linked to systemic factors released from extra-skeletal tumors enhancing the Tet-transactivator in the Tet-OFF;Osx-cre;TdT mice. In fact, we observed increased TdTOSX+ cells (CD45- and CD45+ subsets) also in the bone marrow of tumor bearing Osx-creERT2;TdT animals. Our findings are instead consistent with previous observations reporting increased numbers of bone marrow residing MSCs and osteoblast precursors in mice and patients with lung adenocarcinomas (Engblom et al., 2017), and with the reprogramming of hematopoiesis towards increased myelopoiesis during tumor progression (Capietto et al., 2013; Meyer et al., 2018).

Here, we report for the first time that a subset of hematopoietic lineage cells in the bone marrow and at tumor site derives from an Osx+ progenitor, which is present embryonically and persists until 7–8 weeks of age. Importantly, we detected Sp7 transcripts and Osx nuclear localization in a subset of HSCs. These results support the observation that TdTOSX+;CD45+ cells are very heterogeneous and express monocyte, macrophage, granulocyte, T cell and NK cell markers. The heterogeneity of the TdTOSX+;CD45+ populations is most likely derived from expression of Sp7 in HSC and MPP subsets. These precursors can give rise to the lineage committed common lymphoid (CLP) and myeloid (CMP) progenitors that differentiate into all the mature immune cells (Pietras et al., 2015). Sp7 transcripts are also detected in CLP but not in CMP or mature immune populations, indicating that Osx is activated early during hematopoiesis, with higher expression in cells committed to the lymphoid lineage. Despite expressing both myeloid and lymphoid markers, we noted increased in lymphoid over myeloid ratio in the TdTOSX+;CD45+ tumor infiltrating cells relative to the TdTOSX-;CD45+ cells. TdTOSX+;CD45+ subset is also enriched in genes expressed by immunosuppressive or exhausted lymphocytes. Such result is consistent with the functional tumor co-injection studies showing that TdTOSX-;CD45+ cells reduce tumor growth while the TdTOSX+;CD45+ subset does not.

Co-injection of tumor cells with cells sorted from the primary tumor has been used to validate the pro-tumorigenic roles of CAFs and certain immune suppressive CD45+ populations. Here, we show that tumor-derived TdTOSX+ cells, comprising both CD45 positive and negative subsets, increase tumor growth compared to tumor cells injected alone. By contrast, co-injection of bone marrow-derived TdTOSX+ cells with the tumor cells does not exert any pro-tumor effect suggesting that bone marrow-derived TdTOSX+ cells are functionally distinct from tumor-derived TdTOSX+ cells. Hence, if tumor-derived TdTOSX+ cells originate from the bone marrow in response to an incipient tumor, as it would be anticipated by their increase in the circulation of tumor-bearing mice, they must undergo a conditioning process within the TME to acquire a pro-tumorigenic function. Because Osx regulates expression of proteins required for the generation of the bone tissue, it is likely that a main role of Osx+ mesenchymal cells (TdTOSX+;CD45-) in the TME is to produce and remodel extracellular matrix. Fibroblasts with an osteoblast signature involved in matrix production have been recently identified by single cell RNA sequencing in rheumatoid arthritis (Croft et al., 2019). ECM accumulation is quite frequent within the TME, causing in more severe cases an intense fibrotic response, or desmoplasia, and tumor stiffening (Gkretsi and Stylianopoulos, 2018). Stiffening is not only required for a primary tumor to displace the host tissue and grow in size, but also contributes to cell–ECM interactions and can promote cancer cell invasion to surrounding tissues (Gkretsi and Stylianopoulos, 2018). As noted earlier, upregulation of Sp7 in breast cancer cells is associated with increased invasion and bone metastasis, and this may occur by upregulation of ECM modifying metalloproteinases, MMP9 and MMP13, and other factors that increase vascularization, and affect bone cell function (Yao et al., 2019).

Since Sp7 is not expressed in mature immune populations, it is difficult to envision a role for Osx in modulating anti-tumor immune responses. Co-injection experiments indicate that TdTOSX+;CD45+ cells have better pro-tumorigenic function than TdTOSX–;CD45+ cells. However, only the co-injection of the bulk TdTOSX+ cells increases tumor growth over the B16-F10 tumor cells alone, suggesting that the Osx+ mesenchymal population (TdTOSX+;CD45-) is responsible for enhancing tumor growth. This finding is intriguing since the TdTOSX+;CD45- mesenchymal cells represent only 5% of the total tumor infiltrating TdTOSX+ populations. One could speculate that TdTOSX+;CD45- cells represent a subset of highly pro-tumorigenic CAFs, which can support tumor progression even when present in very limited numbers. Another possibility is that the TdTOSX+;CD45- mesenchymal cells might be required to create and maintain an immune suppressive environment where the CD45+ populations fail to exert anti-tumor effects.

In conclusion, we demonstrate that Sp7 is expressed in a subset of tumor infiltrating mesenchymal cells with CAF and osteogenic cell features. Surprisingly, Sp7 expression is also found in hematopoietic precursors, and marks tumor infiltrating immune populations enriched in immune suppressive markers. Considering the emerging data that Sp7 expression in the tumor cells is linked to tumor progression, our results emphasize the importance of Osx in the TME and the need to evaluate the prognostic value of stromal Sp7 expression in the patients.

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
      <td>Sp7(Osx)</td>
      <td>NCBI Gene</td>
      <td>RRID:MGI:2153568</td>
      <td>NCBI ID:170574</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Tg(Sp7-tTA,tetO-EGFP/cre)1Amc/J (Osx-cre)</td>
      <td>The Jackson Laboratories</td>
      <td>Cat#006361 RRID:MGI:3689350</td>
      <td>C57Bl/6</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>B6.Cg-Gt(ROSA)26Sortm9(CAG-tdTomato)Hze/J (TdT)</td>
      <td>The Jackson Laboratories</td>
      <td>RRID:MGI3813511</td>
      <td>C57Bl/6</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Sp7-creERT2/Ai9tdTomato (Osx-creERT2;TdT)</td>
      <td>PMID:31768488</td>
      <td>Cat#007909 RRID:MGI:4829803</td>
      <td>Prof. Silva MJ (Washington University in St Louis) C57Bl/6</td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus, C57Bl/6)</td>
      <td>B16-F10 melanoma cell line</td>
      <td>ATCC</td>
      <td>RRID:CRL-6475-LUC2</td>
      <td>C57Bl/6</td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>PyMT breast cancer cell line</td>
      <td>PMID:27216180</td>
      <td></td>
      <td>Prof. Weilbaecher KN (Washington University in St Louis) C57Bl/6</td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>Immortalized Cancer Associated Fibroblast cell line</td>
      <td>PMID:27264173</td>
      <td></td>
      <td>Prof Longmore GD (Washington University in St Louis)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD45-APCeFluor780(clone 30-F11)</td>
      <td>eBioscience</td>
      <td>Cat #47-0451-82 RRID:AB_1548781</td>
      <td>FACS (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD45-PE Cy7 (clone 30-F11)</td>
      <td>eBioscience</td>
      <td>Cat #25-0451-82 RRID:AB_2734986</td>
      <td>FACS (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD11b-AlexaFluor700 (clone M1/70)</td>
      <td>eBioscience</td>
      <td>Cat#56-0112-82 RRID:AB_657585</td>
      <td>FACS (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse Gr1(Ly6G)-FITC (clone RB6-8C5)</td>
      <td>Miltenyi Biotec</td>
      <td>Cat#130-102-837 RRID:AB_2659858</td>
      <td>FACS (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse F4/80 PerCP Cy5.5 (clone BM8)</td>
      <td>Biolegend</td>
      <td>Cat#123126 RRID:AB_10802654</td>
      <td>FACS (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Hamster anti-mouse CD3e-PE (clone 145–2 C11)</td>
      <td>eBioscience</td>
      <td>Cat#A14714 RRID:AB_2534230</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD4-APC (clone RM4-5)</td>
      <td>BD Biosciences</td>
      <td>Cat#553051 RRID:AB_398528</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD8a-FITC (clone 53–6.7)</td>
      <td>BD Biosciences</td>
      <td>Cat#561966 RRID:AB_10896291</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse anti-mouse NK1.1 (clone PK136)</td>
      <td>Biolegend</td>
      <td>Cat#108722 RRID:AB_2132712</td>
      <td>FACS (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD45R (B220)-Biotin (clone RA3-6B2)</td>
      <td>eBioscience</td>
      <td>Cat#13-0452-82 RRID:AB_466449</td>
      <td>FACS (0.4 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Hamster anti-mouse CD3e-Biotin (clone 145–2 C11)</td>
      <td>eBioscience</td>
      <td>Cat#13-0031-82 RRID:AB_466319</td>
      <td>FACS (0.4 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse Ter119 (clone TER119)</td>
      <td>eBioscience</td>
      <td>Cat# 13-5921-82 RRID:AB_466797</td>
      <td>FACS (0.4 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse Ly-6G/Ly-6C Biotin (clone RB6-8C5),</td>
      <td>eBioscience</td>
      <td>Cat#13-5931-82 RRID:AB_466800</td>
      <td>FACS (0.2 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD41Biotin (clone MWReg30)</td>
      <td>eBioscience</td>
      <td>Cat#13-0411-82 RRID:AB_763484</td>
      <td>FACS (1 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Streptavidin-BV510</td>
      <td>BD Biosciences</td>
      <td>Cat#563261</td>
      <td>FACS (0.5 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse Sca-1 BV711 (clone D7)</td>
      <td>BD Biosciences</td>
      <td>Cat#563992 RRID:AB_2738529</td>
      <td>FACS (0.25 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse c-kit(CD117)-APCeFluor780 (clone ACK2)</td>
      <td>eBioscience</td>
      <td>Cat#47-1172-82 RRID:AB_1582226</td>
      <td>FACS (1 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD16/32-BUV395 (clone 2.4G2)</td>
      <td>BD Biosciences</td>
      <td>Cat#740217 RRID:AB_2739965</td>
      <td>FACS (0.5 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD34-FITC (clone RAM34)</td>
      <td>eBioscience</td>
      <td>Cat#11-0341-82 RRID:AB_465021</td>
      <td>FACS (4 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD150(SLAM)-BV421 (clone TC15-12F12.2)</td>
      <td>Biolegend</td>
      <td>Cat#115943 RRID:AB_2650881</td>
      <td>FACS (1 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Hamster anti-mouse CD48-PE Cy7 (clone HM48-1)</td>
      <td>eBioscience</td>
      <td>Cat#25-0481-80 RRID:AB_1724087</td>
      <td>FACS (0.15 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD135(Flt3)-APC (clone A2F10)</td>
      <td>eBioscience</td>
      <td>Cat#17-1351-82 RRID:AB_10717261</td>
      <td>FACS (2 ul/sample)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD45 (clone 30-F11)</td>
      <td>Invitrogen</td>
      <td>Cat#14-0451-82 RRID:AB_467251</td>
      <td>IF, IHC (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-mouse RFP/TdT</td>
      <td>Rockland</td>
      <td>Cat#600-401-379 RRID:AB_2209751</td>
      <td>IF,IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat-anti-Rat IgG-Biotin</td>
      <td>Thermo Fisher</td>
      <td>Cat#31830 RRID:AB_228355</td>
      <td>IF, IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Streptavidin-HRP</td>
      <td>Bio-Rad</td>
      <td>Cat#STAR5B</td>
      <td>IF, IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat-anti-rabbit Alexa-fluor647</td>
      <td>Thermo Fisher</td>
      <td>Cat#A21244 RRID:AB_2535812</td>
      <td>IF (4 ug/ml)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-mouse Sp7/Osx</td>
      <td>Abcam</td>
      <td>Cat#ab227820</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-rabbit AlexaFluor488</td>
      <td>Abcam</td>
      <td>Cat#ab150077 RRID:AB_2630356</td>
      <td>IF (1:1000)</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Cyclophilin</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>5’-AGC ATA CAG GTC CTG GCA TC-3’ and 5’-TTC ACC TTC CCA AAG ACC AC-3’</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Sp7(Osx)</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>5’-AAG GGT GGG TAG TCA TTT GCA-3’ and 5’-CCC TTC TCA AGC ACC AAT GG-3’</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>S100A4(Fsp-1)</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>5’-TGA GCA ACT TGG ACA GCA ACA-3’ and 5’-TTC CGG GGT TCC TTA TCT GGG-3’</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Acta2(α-SMA)</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>5’-GTC CCA GAC ATC AGG GAG TAA-3’ and 5’-TCG GAT ACT TCA GCG TCA GGA-3’</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Col1a1</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>5’-GGC CTT GGA GGA AAC TTT GC-3’ and 5’-GGG ACC CAT TGG ACC TGA AC-3’</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Bglap(Ocn)</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>5’-GGA CTG AGG CTC TGT GAG GT-3’ and 5’-CAG ACA CCA TGA GGA CCA TC-3’</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Runx2</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>5’-GTT ATG AAA AAC CAA GTA GCC AGG-3’ and 5’-GTA ATC TGA CTC TGT CCT TGT GGA-3’</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>BSP</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>5’-AGG ACT AGG GGT CAA ACA C-3’ and 5’-AGT AGC GTG GCC GGT ACT TA-3’</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>TNAP</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>5’-GGG GAC ATG CAG TAT GAG TT-3’ and 5’-GGC CTG GTA GTT GTT GTG AG-3’</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TSA FITC System</td>
      <td>Perkin Elmer</td>
      <td>Cat#NEL701A001KT</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>BOND Intense R detection kit</td>
      <td>Leica Biosystem</td>
      <td>Cat#DS9263</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>BOND Polymer Refine Red detection kit</td>
      <td>Leica Biosystem</td>
      <td>Cat#DS9390</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Avidin/Biotin Blocking kit</td>
      <td>Vector Labs</td>
      <td>Cat#SP2001 RRID:AB_2336231</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STAR</td>
      <td>STAR</td>
      <td>RRID:SCR_015899</td>
      <td>Version 2.0.4b</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Subread</td>
      <td>Subread</td>
      <td>RRID:SCR_009803</td>
      <td>Version 1.4.5</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R</td>
      <td>R</td>
      <td>RRID:SCR_001905</td>
      <td>Version 3.4.1</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>EdgeR</td>
      <td>EdgeR</td>
      <td>RRID:SCR_012802</td>
      <td>Version 3.20.2</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>LIMMA</td>
      <td>LIMMA</td>
      <td>RRID:SCR_010943</td>
      <td>Version 3.34.4</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GAGE</td>
      <td>GAGE</td>
      <td>RRID:SCR_017067</td>
      <td>Version 2.28.0</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>VECTASHIELD Mounting Medium with DAPI</td>
      <td>Vector Labs</td>
      <td>Cat#H1200 RRID:AB_2336790</td>
      <td>one drop</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>ProLong Gold with DAPI</td>
      <td>Invitrogen</td>
      <td>Cat#P10144</td>
      <td>one drop</td>
    </tr>
  </tbody>
</table>

### Tumor cell lines, CAF isolation and generation of primary cell cultures

B16-F10 (C57BL/6 mouse melanoma cell line, ATCC # CRL-6475-LUC2), PyMT and PyMT-BO1-GFP (Su et al., 2016) (C57BL/6 mouse breast cancer cell lines), kindly provided by Prof. Katherine N Weilbaecher (Washington University in St. Louis), were cultured at 37°C in complete media (DMEM supplemented with 2 mM l-glutamine, 100 μg/ml streptomycin, 100 IU/ml penicillin, and 1 mM sodium pyruvate) containing 10% FBS. Immortalized CAF cell line was kindly provided by Prof. Gregory D Longmore (Washington University in St. Louis). All the cell lines used have been tested for mycoplasma and were mycoplasma free. CAFs were isolated from primary tumors as described in Corsa et al., 2016. Tumors were minced, digested and plated as single cell suspension on a tissue plastic dish for 30 min to separate the adherent fraction, composed of CAFs, from the cells in suspension, comprising of tumor cells, tumor infiltrating immune populations and endothelial cells, among few others. CAFs were then left 24 hr in culture and RNA was extracted afterwards.

Bone marrow stromal cells (BMSCs) were cultured in complete alpha-MEM (without ascorbic acid) containing 10% FBS and differentiated for 4 days in osteogenic medium (complete alpha-MEM supplemented with 50 μg/ml ascorbic acid and 10 μM beta-glycerophosphate) to obtain pre-osteoblasts.

Sorted hematopoietic stem cells (HSCs) were plated overnight on a glass coverslip coated with serum in the presence of StemPRO (Gibco) media and then fixed and used for immunostaining.

### Mouse strains and tumor models

Animals were housed in a pathogen-free animal facility at Washington University (St. Louis, MO, USA). Age and sex-matched animals were used in all experiments according to IACUC guidelines. B6.Cg-Tg(Sp7-tTA,tetO-EGFP/cre)1Amc/J (catalog #006361; The Jackson laboratory, ME USA) mice, which carry a tetracycline-responsive Osx promoter driving Cre (Osx-cre) were mated with reporter mice B6.Cg-Gt(ROSA)26SorTm9(CAG-tdTomato)Hze/J (TdT) (catalog #007909; The Jackson Laboratory), to generate Osx-cre;TdT mice. To suppress Cre expression, 200ppm doxycyline (doxy) was added to the chow (Test Diet #1816332–203, Purina, MO USA) and fed to some groups of mice until weaning (P28); pups were switched to standard rodent chow at weaning. Sp7-creERT2/Rosa26<fs-TdTomato> mice were kindly provided by Prof. Matthew D Silva (Washington University in St. Louis). Tamoxifen (#T5648, Millipore Sigma, MO USA) was dissolved in corn oil and injected at 100 mg/kg intra-peritoneally. Wild-Type (WT) C57BL/6 mice were purchased from The Jackson Laboratory.

Subcutaneous (sq) injections were performed using 105 B16-F10 tumor cells suspended in 100 µl of sterile PBS and Matrigel Matrix (Corning #354234), while 105 PyMT were suspended in 50 µl of sterile PBS and Matrigel Matrix and injected into the MFP. Adoptive transfer and co-injection with tumor cells were performed using a 5:1 ratio of TdTOSX+:B16-F10 tumor cells. The number of cells injected in each experiment varied depending upon the number of cells obtained from sorting in each experiment (hence, the differences in tumor size among the different experiments), but within (2.5×105:5×104) and (5×105:1×105) cells. B16-F10 cells only were injected as control using the same number of tumor cells co-injected with TdTOSX+ cells. Tumors were monitored by caliper measurements and mice were sacrificed between day 14 and 16 post tumor inoculation. Tumor volume was calculated according to the formula: 0.5236*length*(width [Kalluri and Zeisberg, 2006]).

### Flow cytometry and sorting

Single cell suspensions were prepared from fresh bone marrow and tumors upon sacrifice. Bone marrow cells were obtained from femurs and tibias by centrifugation, while tumors were minced and digested with 3.0 mg/ml collagenase A (Roche, Basel Switzerland) and 50 U/ml DNase I (Millipore Sigma) in serum-free media for 45 min at 37°C. Cells were filtered through 70 μm strainers, red blood cells (RBC) were then removed with RBC lysis buffer (Millipore Sigma), washed twice in PBS and stained in FACS buffer (0.5% BSA, 2 mM EDTA, 0.01%NaN3) with the following antibodies: CD45 (clone 30-F11, eBioscience), CD11b (clone M1/70, eBioscience), Ly6G (Gr-1) (clone RB6-8C5, eBioscience), F4/80 (BM8, Biolegend), CD3 (145–2 C11, eBioscience), CD4 (RM4-5, BD Biosciences), CD8 (clone 53–6.7, BD Biosciences), NK1.1 (clone PK136, Biolegend). Once stained, cells were sorted for the adoptive transfer, RT-PCR and RNAseq studies or were fixed for flow cytometry (gate strategy in Figure 7—figure supplement 1) in BD Cytofix fixation buffer (BD Biosciences, 554655). Samples were acquired using the BD LSR-Fortessa cytometer and analyzed with FlowJo version 9.3.2.

Hematopoietic stem cell subsets were analyzed from fresh bone marrow isolated from femurs, tibias and hip bones crushed with mortar and pestle in 3 ml of PBS, filtered in a 70μm-nylon strainer to remove bone fragments and lysed of red blood cells (RBC). 10 million cells were stained for each sample using the following antibodies: CD3, Gr1, B220 (clone RA3-6B2, eBioscience), Ter119 (clone TER119, e Bioscience), CD41 (clone eBioMWReg30, eBioscience) for lineage negative gating, Sca-1 (clone D7, BD Biosciences), CD117/c-kit (clone ACK2, eBioscience), CD16/32 (clone 2.4G2, BD Biosciences), CD34 (clone RAM34, eBioscience), CD150/SLAM (clone TC15-12F12.2, Biolegend), CD48 (clone HM48-1, eBioscience), CD135/Flt3 (clone A2F10, eBioscience), gate strategy in Figure 7—figure supplement 1. Once stained, cells were fixed in BD Cytofix fixation buffer, acquired using the Bio-Rad ZE5 (YETI) cytometer and analyzed with FlowJo version 10.4.1.

Isolation of hematopoietic progenitor subsets for Real Time analysis was obtained by FACS sorting using the following markers: HSCs (Lineage- c-Kit+Sca-1+CD48-CD150+), MPPs (Lineage- c-Kit+Sca-1+CD48-CD150-), CLPs (Lineage- c-Kit+Sca-1+IL7rα+Flt3+Ly6D-) and CMPs (Lineage- c-Kit+Sca-1-CD34+CD16/32). For IF, TdTomato was also used to sort Osx+ HSCs.

Isolation of hematopoietic stem cells for Osx immunostaining was performed as following: whole bone marrow was isolated from femurs, tibias and iliac crests and incubated with mouse CD117-conjugated microbeads (Miltenyi Biotec #130-091-224). CD117-enrichment was then carried out using the AutoMACS Pro Seperator (Miltenyi Biotec). Post CD117 enrichment, the positive cell fraction was stained to sort phenotypically defined TdTomato+ HSCs (Lineage- c-Kit+Sca-1+CD48-CD150+) by FACS.

### Histology

Tumors and bones (femur and tibia) were fixed in 4% PFA over-night (ON) at 4°C. The fixed bones were partially decalcified in 14% EDTA for 3 days, washed in a sucrose gradient (1 hr in 10% sucrose, 1 hr in 20% sucrose, ON in 30% sucrose) before snap-freezing them in OCT embedding medium. Tumors were directly put in sucrose gradient and then embedded in OCT. Frozen sections were cut at 5 μm thickness and kept at −20°C until analysis.

Thawed sections were washed in PBS and mounted with VECTASHIELD Mounting Medium containing DAPI (Vector Laboratories, CA USA).

Images were taken using the Leica DMi8 Confocal Microscopy at the Musculoskeletal Research Center (Washington University in St Louis), magnification 200X.

### Immunohistochemical staining

Tissues were fixed in 10% neutral-buffered formalin for 18 hr, embedded in paraffin after graded-ethanol dehydration, and sectioned into 6 μm sections using a microtome. Automated staining was carried out on the BondRxm (Leica Biosystems). Following dewaxing and citrate-buffered antigen retrieval, sections were stained with the primary antibody for 1 hr at RT. Sequential chromogenic detection was performed with the Bond IntenseR (Rat primary) and Bond Polymer Refine Red (Rabbit primary) detection kits (Leica Biosystems). The primary antibodies used were rat anti-CD45 (Invitrogen clone 30-F11, #14-0451-82) followed by rabbit anti-RFP/TdT (Rockland, # 600-401-379). Stained sections were dehydrated in graduated ethanol and xylene washes then mounted with xylene-based Cytoseal (Thermo Fisher).

Stained slides were imaged at 20X magnification with the Zeiss Axioscan slide scanner. For image analysis, Halo v3 (Indica Labs) was used to deconvolve dual stained images into single channels and pseudo colored with blue representing nuclei (hematoxylin), green representing CD45+ cells (DAB stained), and red representing Osx+ cells (RFP stained).

### Immunohistochemestry and immunofluorescence staining

For colocalization of TdT+ cells and CD45 in B16-F10 soft tissue tumors, subcutaneous tumors were dissected and fixed in 10% neutral-buffered formalin for 18 hr, embedded in paraffin after graded-ethanol dehydration, and sectioned into 6 μm sections using a microtome. Sections were dewaxed in xylene and then hydrated through graded ethanol washes. Endogenous peroxidases were quenched by incubating in hydrogen peroxide (1% in PBS) for 10 min at RT. Antigen retrieval was then performed by microwave treatment in a citrate buffer for 15 min. Sections were washed in TBS-T (1X TBS with 0.05%Tween-20) followed by blocking for 30 min at RT in blocking buffer (5% goat serum, 2.5% BSA in TBS). Slides were then blocked using the Avidin/Biotin Blocking Kit (Vector Labs). For staining, slides were incubated overnight in a humidified chamber at 4°C with 1:200 rat anti-CD45 (Invitrogen clone 30-F11, #14-0451-82) and 1:400 rabbit anti-RFP (Rockland, #600-401-379) antibodies diluted in 50% blocking buffer. After primary staining, slides were washed in TBS-T and then incubated with HRP-conjugated anti-rat IgG secondary (1:500 in 50% blocking buffer) for 30 min at RT. For fluorescent detection of CD45, slides were washed and then incubated in 1:50 FITC Tyramide reagent (PerkinElmer, # NEL701A001KT) for 8 min at RT. For fluorescent detection of RFP, slides were washed and incubated in AlexaFluor 594-conjugated anti-rabbit IgG secondary (1:500 in 50% blocking buffer) for 30 min at RT. Stained slides were washed and mounted using ProLong Gold with DAPI (Invitrogen).

#### Osx staining

HSCs, BMSC or whole bone marrow cells were plated overnight on coverslips coated with FBS for 30 min at RT then cells. Cells were fixed in 4% PFA for 15 min, washed and permeabilized with PBS/0.3%TritonX-100 for 3 min. Blocking was performed with 5% normal serum in permeabilization buffer for 1 hr at RT. Anti-Osx antibody (Abcam, #ab227820) was dissolved 1:500 in a buffer containing PBS/0.3%TritonX-100/1%BSA and incubated ON at 4°C. For fluorescent detection, coverslips were washed and incubated in AlexaFluor 488-conjugated anti-rabbit secondary antibody (1:1000) in PBS/0.3%TritonX-100/1%BSA for 1 hr at RT. Stained slides were washed and mounted using VECTASHIELD Mounting Medium containing DAPI (Vector Laboratories, CA USA). Fluorescent signals were captured by using a Nikon Eclipse 80i microscope and a Nikon DS-Qi1MC camera (Nikon, CO, USA).

### Real Time PCR

Total RNA was extracted with TRIzol (Invitrogen, CA USA) and quantified on a ND-1000 spectrophotometer (NanoDrop Technologies). The cDNA was synthesized with 1 μg RNA using High Capacity cDNA Reverse Transcription Kit (#4368814, Applied Biosystems, CA USA).

For purified hematopoietic precursors (HSC, MPP, CLP and CMP) total RNA was extracted using the NucleoSpin RNA XS kit (Macherey-Nagel #740902) and reverse transcribed with the SuperScript VILO kit (Invitrogen #11754–050).

The amount of each gene was determined using Power SYBR Green mix on 7300 Real-Time PCR System (Applied Biosystems). Cyclophilin mRNA was used as housekeeping control. Specific primers for mice were as follows: Cyclophilin, 5’-AGC ATA CAG GTC CTG GCA TC-3’ and 5’-TTC ACC TTC CCA AAG ACC AC-3’; Osterix, 5’-AAG GGT GGG TAG TCA TTT GCA-3’ and 5’-CCC TTC TCA AGC ACC AAT GG-3’; S100a4 (Fsp1), 5’-TGA GCA ACT TGG ACA GCA ACA-3’ and 5’-TTC CGG GGT TCC TTA TCT GGG-3’; Acta2 (a-SMA), 5’-GTC CCA GAC ATC AGG GAG TAA-3’ and 5’-TCG GAT ACT TCA GCG TCA GGA-3’; Col1a1, 5’-GGC CTT GGA GGA AAC TTT GC-3’ and 5’-GGG ACC CAT TGG ACC TGA AC-3’; Bglap (Osteocalcin), 5’-GGA CTG AGG CTC TGT GAG GT-3’ and 5’-CAG ACA CCA TGA GGA CCA TC-3’; Runx2, 5’-GTT ATG AAA AAC CAA GTA GCC AGG-3’ and 5’-GTA ATC TGA CTC TGT CCT TGT GGA-3’; Ibsp (Bsp), 5’-AGG ACT AGG GGT CAA ACA C-3’ and 5’-AGT AGC GTG GCC GGT ACT TA-3’; Alpl (Tnap), 5’-GGG GAC ATG CAG TAT GAG TT-3’ and 5’-GGC CTG GTA GTT GTT GTG AG-3’. The relative quantification in gene expression was determined using the 2-ΔΔCt method.

### RNA sequencing and analysis

Single cell suspensions were prepared from fresh tumor upon sacrifice. Tumors were minced and digested as described above. Tumor stromal cells were separated from the GFP+ tumor cells and sorted based on the expression, or lack of thereof, of TdT and CD45 markers.

Library preparation was performed with 10 ng of total RNA and integrity was determined using an Agilent bioanalyzer. ds-cDNA was prepared using the SMARTer Ultra Low RNA kit for Illumina Sequencing (Clontech) per manufacturer’s protocol. The cDNA was fragmented using a Covaris E220 sonicator using peak incident power 18, duty factor 20%, cycles/burst 50, for a 120 s. cDNA was blunt ended, had an A base added to the 3’ ends, and then had Illumina sequencing adapters ligated to the ends. Ligated fragments were then amplified for 12 cycles using primers incorporating unique index tags. Fragments were sequenced on an Illumina HiSeq 3000 using single end reads extending 50 bases. Basecalls and demultiplexing were performed with Illumina’s bcl2fastq software and a custom python demultiplexing program with a maximum of one mismatch in the indexing read. RNA-seq reads were then aligned to the Mus musculus Ensembl release 76 top-level assembly with STAR version 2.0.4b (Dobin et al., 2013). Gene counts were derived from the number of uniquely aligned unambiguous reads by Subread:featureCount version 1.4.5 (Liao et al., 2014). Isoform expression of known Ensembl transcripts were estimated with Sailfish version 0.6.13 (Patro et al., 2017). Sequencing performance was assessed with RSeQC version 2.3 (Wang et al., 2012).

All gene counts were then imported into the R/Bioconductor package EdgeR (Robinson et al., 2010) and TMM normalization size factors were calculated to adjust for samples for differences in library size. Ribosomal genes and genes not expressed in at least two samples greater than one count-per-million were excluded from further analysis. The TMM size factors and the matrix of counts were then imported into the R/Bioconductor package Limma (Ritchie et al., 2015) and weighted likelihoods based on the observed mean-variance relationship of every gene and sample were then calculated with Limma’s voomWithQualityWeights (Liu et al., 2015). The data were then fitted to a Limma generalized linear model to test for changes in a single cell population relative to the mean of all other populations to find only genes that were uniquely up-regulated with Benjamini-Hochberg false-discovery rate adjusted p-values less than or equal to 0.05. For each group of cells, global perturbations in known Gene Ontology (GO) terms were then measured using the R/Bioconductor package GAGE (Luo et al., 2009) to quantify the mean log two fold-changes of ll genes in a given term versus the background log two fold-changes of all genes found outside the respective term. Only globally up-regulated GO terms with Benjamini-Hochberg false-discovery rate adjusted p-values less than or equal to 0.05 were considered for comparison across populations.
