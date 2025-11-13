# Runx2-Twist1 interaction coordinates cranial neural crest guidance of soft palate myogenesis

## Authors

- Xia Han<sup>1</sup>
- Jifan Feng<sup>1</sup> ([ORCID: 0000-0002-9944-2604](https://orcid.org/0000-0002-9944-2604))
- Tingwei Guo<sup>1</sup>
- Yong-Hwee Eddie Loh<sup>2</sup>
- Yuan Yuan<sup>1</sup> ([ORCID: 0000-0002-7742-9433](https://orcid.org/0000-0002-7742-9433))
- Thach-Vu Ho<sup>1</sup> ([ORCID: 0000-0001-6293-4739](https://orcid.org/0000-0001-6293-4739))
- Courtney Kyeong Cho<sup>1</sup>
- Jingyuan Li<sup>1</sup>
- Junjun Jing<sup>1</sup> ([ORCID: 0000-0001-5745-5207](https://orcid.org/0000-0001-5745-5207))
- Eva Janeckova<sup>1</sup>
- Jinzhi He<sup>1</sup>
- Fei Pei<sup>1</sup>
- Jing Bi<sup>1</sup>
- Brian Song<sup>1</sup>
- Yang Chai<sup>1</sup> ([ORCID: 0000-0003-2477-7247](https://orcid.org/0000-0003-2477-7247)) †

### Affiliations

1. Center for Craniofacial Molecular Biology, University of Southern California, Los Angeles Los Angeles United States
2. USC Libraries Bioinformatics Services, University of Southern California, Los Angeles Los Angeles United States

† Corresponding author

## Abstract

Cranial neural crest (CNC) cells give rise to bone, cartilage, tendons, and ligaments of the vertebrate craniofacial musculoskeletal complex, as well as regulate mesoderm-derived craniofacial muscle development through cell-cell interactions. Using the mouse soft palate as a model, we performed an unbiased single-cell RNA-seq analysis to investigate the heterogeneity and lineage commitment of CNC derivatives during craniofacial muscle development. We show that Runx2, a known osteogenic regulator, is expressed in the CNC-derived perimysial and progenitor populations. Loss of Runx2 in CNC-derivatives results in reduced expression of perimysial markers (Aldh1a2 and Hic1) as well as soft palate muscle defects in Osr2-Cre;Runx2fl/fl mice. We further reveal that Runx2 maintains perimysial marker expression through suppressing Twist1, and that myogenesis is restored in Osr2-Cre;Runx2fl/fl;Twist1fl/+ mice. Collectively, our findings highlight the roles of Runx2, Twist1, and their interaction in regulating the fate of CNC-derived cells as they guide craniofacial muscle development through cell-cell interactions.

## Introduction

The craniofacial musculoskeletal complex is an important evolutionary innovation in vertebrates that facilitates feeding, breathing, facial expression, and verbal communication. One unique component of this complex is the cranial neural crest (CNC) cells. CNC cells and their derivatives give rise to all facial bones, ligaments, and muscle connective tissues including tendons and fascia that directly surround muscle cells (Chai and Maxson, 2006; Heude et al., 2010; Le Douarin et al., 2004). Recently, CNC cells have been shown to regulate formation of mesoderm-derived craniofacial muscles through cell-cell interactions. Mouse genetic studies have further shown that CNC cells and their derivatives surround myogenic cells, facilitate myogenic cell migration, and establish cellular scaffolding at future myogenic sites to regulate muscle morphogenesis (Grimaldi et al., 2015; Han et al., 2014; Rinon et al., 2007). For instance, disruption of Dlx5/6, which is specifically expressed by CNC-derived cells in the mouse, leads to the loss of all first pharyngeal arch-derived masticatory muscles and second pharyngeal arch-derived muscles (Heude et al., 2010). Proliferation and survival of CNC-derived cells and fourth to sixth pharyngeal arch-derived myogenic cells in the soft palate are also affected, resulting in a truncated soft palate in Dlx5-/- mice (Sugii et al., 2017). Similarly, TGFβ signaling in CNC-derived cells is critical for proliferation and differentiation of tongue and masseter muscle cells (Han et al., 2014; Hosokawa et al., 2010; Iwata et al., 2013). It is important to note that the transcription factors and signaling pathways critical for the role of CNC-derived cells in myogenesis are not restricted in their expression to merely the CNC-derived cells surrounding the muscle, known as perimysial cells; they are also expressed in other CNC-derived musculoskeletal tissues (e.g. bones, bone eminences, and tendons) and regulate their development (Depew et al., 2002; Hosokawa et al., 2010; Zhao et al., 2008). This suggests that the same transcription factors and signaling pathways could activate cell-type-specific responses in multiple components of the musculoskeletal complex that may help coordinate the development of this intricate system. Therefore, it is important to investigate the cell-type-specific signaling mechanisms that regulate the heterogeneous CNC-derived cells and reveal their impact on craniofacial musculoskeletal development.

The soft palate is a muscular structure that comprises the posterior third of the palate. Its movement opens and closes the nasopharynx and oral cavity to direct air and food into different passages, as well as during speech. Several components of the soft palate are CNC-derived, including perimysial cells, palatal stromal cells that constitute the majority of palatal shelf mesenchyme, and tendons. In contrast, the soft palatal muscles are derived from pharyngeal mesoderm (Grimaldi et al., 2015). Five muscles are involved in the human soft palate. They include the tensor veli palatini (TVP) and levator veli palatini (LVP), which descend from the skull base and elevate the soft palate, and the palatoglossus (PLG) and palatopharyngeus (PLP), which ascend from the tongue and the pharyngeal wall, respectively, and depress the soft palate (Li et al., 2019). The fifth muscle, the musculus uvulae, which is specific to humans, is located at the end of the soft palate. Patients with cleft palate often have multiple types of tissue abnormalities including bone defects and insufficient, misoriented muscle fibers (Dixon et al., 2011; Li et al., 2019). Functional restoration of cleft soft palate is challenging because the muscles have limited ability to regenerate after surgical repair of the cleft (Von den Hoff et al., 2019). Therefore, comprehensive understanding of the growth and transcription factors that regulate the coordinated development of the distinct tissues in the soft palate is of both scientific and clinical significance.

Runx2, a known regulator of skeletogenesis and odontogenesis, is a Runt DNA-binding domain family transcription factor and contains multiple activation and repression domains. Patients with haploinsufficiency of RUNX2 exhibit cleidocranial dysplasia, which is associated with specific skeletal and dental phenotypes. During osteoblast differentiation, Runx2 acts as a master organizer, recruiting phosphorylated Smad1/5, c-Fos, and c-Jun to activate expression of osteoblast-specific collagen and fibronectin upon receiving BMP signals and parathyroid hormones; it also binds histone deacetylases to repress cell cycle inhibitors and stimulate proliferation (Schroeder et al., 2005). Despite its well-known roles in regulating hard tissue development, the importance of Runx2 in soft tissue development has not been studied. Interestingly, several clinical case reports reveal that some RUNX2-deficient patients have thin masseter muscles, cleft lip, or high-arched palate (Furuuchi et al., 2005; Sapp et al., 2004; Sull et al., 2008; Yamachika et al., 2001). These studies hint that Runx2 may regulate the development of the palatal muscles and other components in sync with the bone to form the intricate craniofacial musculoskeletal complex by performing multiple tissue-specific roles.

In this study, we performed an unbiased transcriptional profile analysis of the developing soft palate using single-cell RNA-seq (scRNA-seq). We identified cellular-level heterogeneity in the CNC-derived soft palate mesenchyme, associated with distinctive cell fates: perimysial and midline mesenchymal lineages, as well as previously unknown cell types associated with putative progenitors. In addition, we found Runx2 was expressed in non-osteochondrogenic cells in the perimysial populations and in CNC-derived progenitor cells. Consistent with its expression pattern, loss of Runx2 in CNC-derived cells resulted in a soft palate cleft along with tendon, bone, and muscle differentiation defects. We further revealed that loss of Runx2 led to ectopic expression of Twist1 and reduction in the expression of perimysial marker genes (Aldh1a2 and Hic1) in CNC-derived perimysial cells. We also identified that suppression of Twist1 expression by Runx2 is important for the development of palatal muscles and for maintaining the expression of the perimysial marker and myogenic-promoting gene Aldh1a2, thus coordinating soft palate morphogenesis by orchestrating the fate determination of CNC-derived mesenchymal lineages. Taken together, our findings reveal that Runx2 regulates distinct downstream targets in different subgroups of CNC-derived cells to fine-tune the development of craniofacial structures.

## Results

### Single-cell RNA-seq analysis reveals mesenchymal cell heterogeneity within the soft palate primordium

CNC-derived cells adopt diverse fates to establish the soft palate during development. To investigate the heterogeneity of the CNC-derived population that contributes to the developing soft palate at the single-cell level, we performed unbiased single-cell RNA-seq and integration analysis at three critical stages (E13.5, E14.5, E15.5). The soft palate primordium begins to form around E13.5, followed by fusion of the soft palatal shelves at E14.5 and myotube maturation at E15.5 (Li et al., 2019). Following integration analysis by Seurat 3, we identified 19 clusters identifiable as 8 cell types using known genetic markers: CNC-derived mesenchymal cells (Meox1+, Dlx5+), myogenic cells (Myod1+, Myf5+), neurons (Tubb3+, Stmn2+), endothelial cells (Cdh5+), erythroid cells (Hba-x+), glial cells (Plp1+, Sox10+), myeloid cells (Lyz2+), and epithelial cells (Krt14+) (Figure 1A; Figure 1—figure supplement 1A). Several lineages consisted of multiple clusters, such as CNC-derived mesenchymal, epithelial, neuronal, and myogenic cells, highlighting the heterogeneity within those populations (Figure 1A). Interestingly, in the CNC-derived mesenchymal cell population, we observed eight different clusters (Clusters 0–4, 7, 8, 10) (Figure 1A–B). Besides Clusters 2 and 10, which were identified as terminally differentiated osteogenic and chondrogenic cells, respectively, the cell types and functions of the other clusters in the CNC-derived mesenchymal population have not yet been well characterized.

![Figure 1.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig1-v1.jpg)

**Figure 1.:** (A) UMAP plot integration analysis of mouse soft palate cells from E13.5, E14.5, and E15.5 based on clusters (left) and different developmental stages (right). (B) DotPlot of signature genes in CNC-derived clusters. The color code of signature genes corresponds to the colors of the names of distinct cell populations in the right panel. (C) Schematic drawings of Myod1 (green), styloid process of temporal bone (SP) and hyoid bone (HB) on coronal sections of the levator veli palatini (LVP) region and (D) Myod1 (green), tongue (T), pterygoid plate (PP), and Meckel’s cartilage (MC) on coronal sections of the tensor veli palatini (TVP) region of E14.5 control mice. PS, Palatal shelves. Yellow dashed boxes in (C) and (D) are enlarged and analyzed for expression patterns of cluster-specific markers in (E–L) and (M–T), respectively. (E–L) RNAscope in situ hybridization for Myod1 and selected marker genes from each cluster of CNC-derived cells on coronal sections of the LVP region. (M–T) RNAscope in situ hybridization for Myod1 and selected marker genes from each cluster of CNC-derived cells in the TVP region. White arrows point to masseter muscles (M) in (P, Q, R). White arrowhead points to tongue (T) in (Q). Yellow dashed lines outline the myogenic sites (LVP in E-L; TVP in M-T). White dashed lines outline the palatal shelf. Boxed areas are enlarged in the insets. Scale bar in E indicates 100 μm for E-T.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Different types of cells were identified in the soft palate region, including cranial neural crest (CNC)-derived mesenchymal cells (Meox1+, Dlx5+), myogenic cells (Myod1+, Myf5+), neuronal cells (Tubb3+, Stmn2+), endothelial cells (Cdh5+), erythroid cells (Hba-x+), glial cells (Plp1+, Sox10+), myeloid cells (Lyz2+), and epithelial cells (Krt14+). (B–C) Functional annotations of previously unidentified CNC-derived cell populations in the soft palate mesenchyme, B for Cluster 1 and C for Clusters 3, 4, and 7.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A–E) RNAscope in situ analysis of Myod1 and perimysial markers Hic1 and Tbx15 on coronal sections of the LVP region from E13.5 to E14.5. MPC: Middle pharyngeal constrictor. TT: Tensor tympani muscle. Yellow dashed lines outline the myogenic sites of the LVP. White dashed lines outline the palatal shelf. Yellow arrowheads point to migrating myogenic precursors. Scale bar in A indicates 100 µm for A-E.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A–C) RNAscope in situ analysis of Myod1 and early perimysial marker Aldh1a2 on coronal sections of the tongue of control mice from E12.5 to E14.5. (D–F) RNAscope in situ analysis of perimysial markers Aldh1a2, Hic1, and Tbx15 on E14.5 coronal sections from the hard palate of control mice. White dashed lines outline the tongue. White dotted lines outline the tooth germ. White arrowheads point to expression of perimysial markers in the tongue. White arrows point to the expression of perimysial markers surrounding the tooth germ. White asterisk indicates the missing expression of Tbx15 in the hard palate region. T: Tongue. Scale bar in A indicates 100 µm for A-F.

To characterize the roles of these less known subpopulations, we analyzed the top 10 differentially expressed genes in each cluster and performed functional annotation for those highly specific markers using Ingenuity Pathway Analysis. We thus identified four major types of CNC-derived cells in the soft palate besides osteogenic (Cluster 2) and chondrogenic cells (Cluster 10) (Figure 1B). Cluster 0 was enriched with early CNC marker genes such as Tfap2b, Six2, and Prrx1 (Simões-Costa and Bronner, 2015; Soldatov et al., 2019), so we suspected that this population might be an undifferentiated early progenitor population associated with early CNC cells, and accordingly we hypothesized that they were CNC-derived progenitors (Figure 1B). Genes enriched in Cluster 1 (Tbx22, Wnt16, Meis2) were associated with the palatal shelf midline during development (Louw et al., 2015; Pauws et al., 2013; Warner et al., 2009; Figure 1B; Figure 1—figure supplement 1B); hence, we refer to this cluster as midline mesenchymal cells. Clusters 3, 4, and 7 expressed high levels of genes related to head and muscle morphogenesis (Cxcl12, Igf1, Aldh1a2); we refer to them as perimysial cells (Matt et al., 2008; Schiaffino and Mammucari, 2011; Vasyutina et al., 2005; Figure 1B; Figure 1—figure supplement 1C). Interestingly, Cluster 8 was strongly enriched in genes associated with mitosis (Top2a, Ccnb1, Ube2c) (Nielsen et al., 2020; Pines, 2011; Strauss et al., 2018) even after cell cycle regression was performed (Figure 1B). We therefore refer to this cluster as mitotic cells.

To investigate the in vivo identities of each cluster, we performed RNAscope in situ hybridization of the soft palate at E14.5. Different soft palate myogenic sites develop sequentially from anterior to posterior direction. Specifically, in coronal sections, the unfused palatal shelves in the LVP region (posterior) protrude toward the midline and the myogenic cells grow in a lateral to medial direction along the palatal shelves at E14.5 (Figure 1C), while the palatal shelves in the TVP region (anterior) are already fused and the myogenic cells wrap around the pterygoid plate (Figure 1D). As the TVP and LVP myogenic sites are more identifiable than those of the PLG and PLP at E14.5, we used the former as reference points for the anatomical locations of each cluster in our analysis. Using the top enriched genes of each cluster, we identified their distinct anatomical locations in vivo. The Ibsp+ osteogenic (Figure 1E,M) and Col2a1+ chondrogenic clusters (Figure 1F,N) were mostly associated with part of the styloid process of the temporal bone in the LVP region and the pterygoid plate of the sphenoid bone in the TVP region. In the LVP region, the Tfap2b+ progenitor cluster was mainly located in the lateral portions of the palatal shelves (Figure 1G). The majority of the Aldh1a2+ perimysial cluster was distributed in the lateral portion while only a small portion of this cluster appeared in the central myogenic sites (Figure 1H). In contrast, the two other perimysial clusters (Hic1+ and Tbx15+) were most abundantly located in the central myogenic sites of the LVP (Figure 1I–J). Midline mesenchymal cells (Tbx22+) were mainly located in the medial portions of the palatal shelves (Figure 1K). The Top2a+ mitotic cells were distributed throughout the palatal shelves and adjacent to both early progenitors and committed CNC-derived cells (Figure 1L). A similar distribution of different cluster markers was observed in the TVP region (Figure 1O–T). Outside of the soft palate, the perimysial markers (Aldh1a2, Hic1 and Tbx15) were expressed in the mesenchyme surrounding the tongue and masseter muscles in addition to the palatal myogenic sites of the TVP (Figure 1P–R), while near the LVP region, Hic1 and Tbx15 were also expressed in the mesenchyme surrounding the migratory path of myogenic progenitors of the LVP and the myogenic sites of the middle pharyngeal constrictor muscle and tensor tympani muscle (Figure 1I–J and Figure 1—figure supplement 2A–E). These observations suggest the perimysial lineage might be a common CNC-derived sub-population involved in the development of multiple craniofacial muscles.

Because the oropharyngeal muscles are only present in the soft palate, not the hard palate, we investigated whether the perimysial markers are also specific to the soft palate. Interestingly, Tbx15 expression was absent from the hard palate, but Aldh1a2 and Hic1 were expressed in the hard palate mesenchyme specifically surrounding the tooth germ (Figure 1—figure supplement 3D–F). This suggests that Aldh1a2 and Hic1 might have different functions in the hard and soft palate. Interestingly, we also observed that Aldh1a2 was expressed in the medial mesenchyme of the tongue, while Hic1 and Tbx15 were expressed broadly in the mesenchyme of the tongue at E14.5 (Figure 1—figure supplement 3C,E–F). Moreover, the expression of Aldh1a2 in the tongue gradually decreased from E12.5 to E14.5 (Figure 1—figure supplement 3A–C). As myogenic precursors started to appear in the center of tongue primordium (Han et al., 2012), the Aldh1a2+ population might be specifically associated with early myogenic populations, while Hic1+ and Tbx15+ populations may be associated with more general myogenic populations.

### Runx2 is expressed in the perimysial populations and CNC-derived progenitor cells during soft palate development

To elucidate the dynamic process by which CNC-derived cells differentiate during soft palate development, we performed individual single-cell transcriptome analyses for E13.5, E14.5, and E15.5, then compared them. The pterygoid plate of the sphenoid bone and part of the styloid process of the temporal bone are not considered to be part of the palate, so we excluded the osteochondrogenic clusters belonging to these structures from further analysis. Interestingly, we observed decreased cell heterogeneity in CNC-derived soft palate mesenchymal populations during development. The number of CNC-derived clusters declined from seven at E13.5 to six at E14.5 and eventually five at E15.5 using the same unsupervised clustering settings (Figure 2—figure supplement 1A). In contrast, myogenic cells formed a single cluster at E13.5 but expanded to two clusters at E15.5 (Figure 2—figure supplement 1A).

To further investigate how each cluster changed over time, we extracted and compared the CNC-derived and myogenic cells from E13.5 to E15.5 based on the earlier integration analysis (Figure 2A). Consistent with previous observations, in the myogenic clusters we observed an increased number of both early myogenic precursors (Cluster 9, Msc+, Myf5+) and differentiated myocytes (Cluster 17, Myl4+) as development progressed (Figure 2A). The number of cells in Clusters 1 (Tbx22+), 3 (Hic1+) and 4 (Tbx15+) also increased from E13.5 to E15.5, but the number of cells in CNC-derived Clusters 0 (Tfap2b+), 7 (Aldh1a2+), and 8 (Top2a+) gradually decreased. This suggests that Clusters 0, 7, and 8 may be progenitors that are transiently present at early stages of soft palate development and give rise to Clusters 1, 3, and 4 (Figure 2A–B). To test this, we also computationally predicted the differentiation trajectory of CNC-derived cells using pseudotime analysis. Our results predicted Cluster 0 to be common CNC-derived progenitors that bifurcate into two more committed groups: perimysial progenitors (Cluster 7) for the later perimysial population (perimysial fibroblasts) (Clusters 3 and 4), and another group of progenitors (a subset of Cluster 0 and Cluster 8) for midline mesenchymal cells (Cluster 1) (Figure 2—figure supplement 1B–C). The integration analysis suggested that the fate decision between perimysial and midline mesenchymal cells happens at E13.5-E14.5. Cluster 8, predicted to be a more committed group of progenitors, represents the Top2a+ mitotic population. Because mitosis establishes a time window during which transcription factors can easily access and activate genes important for cell lineage determination (Gurdon, 2016), cells with high mitotic activity are likely undergoing cell fate transition. Therefore, those Top2a+ mitotic cells might be transitioning from early progenitor status to becoming more committed to a particular fate. Interestingly, the number of Aldh1a2+ cells in Cluster 7 gradually decreased, but the number of Aldh1a2+ cells increased in Clusters 3 and 4 from E13.5 to E15.5 (Figure 2B), probably because Aldh1a2 labels both the majority of the early perimysial population (Cluster 7) and also some of the late perimysial populations (Clusters 3 and 4).

![Figure 2.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig2-v1.jpg)

**Figure 2.:** (A) Individual UMAP clustering of CNC-derived mesenchymal and myogenic cells at three different embryonic stages (E13.5, E14.5, and E15.5) from integration analysis (top and middle panel). Percentages of cells in different CNC-derived and myogenic clusters in control soft palates at E13.5, E14.5, and E15.5 based on the integrated analysis (bottom panel). (B) Expression patterns of marker genes that are expressed transiently during early stages of soft palate development. (C–J) Co-expression of Runx2 with cluster-specific markers Tfap2b, Top2a, Aldh1a2, Tbx22 in E13.5-E15.5 soft palate integration analysis. Boxed areas in (C–F) are enlarged in (G–J). Black arrows point to cells co-expressing Runx2 with individual cluster-specific markers. (K–P) Runx2 with myogenic markers MyoD or Myod1 on coronal sections of the tensor veli palatini (TVP) and levator veli palatini (LVP) regions of control mice at E13.5, E14.5, and E15.5. Boxes indicate regions shown at higher magnification in the insets. (Q–X) Co-localization of Runx2 with cluster-specific marker genes Tfap2b, Aldh1a2, Top2a, and Tbx22 on coronal sections of the LVP region of E14.5 control mice. Boxed areas in Q-T are enlarged in U-X. Yellow dashed lines in (K–T) outline the myogenic cells. White dashed lines outline the palatal shelf. Scale bars in K and Q indicate 100 μm for K-P and Q-T. Scale bar in U indicates 30 μm for U-X.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) UMAP plots of CNC-derived cells from soft palate mesenchyme and myogenic cells at E13.5, E14.5, and E15.5. (B) UMAP clustering of CNC-derived cells from E13.5-E15.5 in the soft palate. Black dashed line outlines the non-osteochondrogenic CNC-derived soft palate mesenchymal clusters. (C) Monocle three pseudotime trajectory analysis of CNC-derived soft palate mesenchymal cells showing the sequential fate determinations of CNC-derived cells. Left panel: pseudotime trajectory colored by stage; Right panel: pseudotime trajectory colored by timeline.

Notably, we observed that expression of Runx2 in the CNC-derived mesenchyme gradually decreased from E13.5 to E15.5, suggesting it might play a role in regulating CNC-derived cell differentiation during early soft palate development (Figure 2B). Furthermore, Runx2 was expressed not only by the CNC-derived common progenitors Cluster 0 (Tfap2b+), but also by other more committed progenitor cells, Cluster 8 (Top2a+) and Cluster 7 (Aldh1a2+), which were mainly distributed around the bifurcation regions of different lineages; only a few midline mesenchymal cells in Cluster 1 (Tbx22+) expressed Runx2 (Figure 2C–J).

To investigate the functional significance of Runx2 for soft palate development in vivo, we examined Runx2 expression in the TVP and LVP regions of control mice. Double staining of Runx2 and the myogenic marker MyoD/Myod1 from E13.5-E15.5 revealed changes in Runx2 expression in the myogenic region as development progressed. Runx2 expression was gradually restricted from most of the palate primordium at E13.5 to only the mesenchymal cells in the putative progenitor, perimysial, and osteogenic sites in the LVP region at E14.5; eventually, it was found only in the osteogenic regions at E15.5 (Figure 2K–M). As there was no detectable Runx2 expression in the TVP perimysial site from E13.5 to E15.5 (Figure 2N–P), we focused on the LVP region as we investigated the colocalization of Runx2 with markers of early CNC-derived progenitors and different lineages in vivo. Consistent with our single-cell analysis, Runx2 was predominantly expressed in the putative progenitor population (Tfap2b+), actively amplifying population (Top2a+) and perimysial cells (Aldh1a2+), with only a few in the midline mesenchymal cells (Tbx22+) (Figure 2Q–X). Previous studies have shown that CNC-derived cells guide the migration and potentially regulate the maturation of mesoderm-derived myogenic precursors in the soft palate through tissue-tissue interactions (Grimaldi et al., 2015; Li et al., 2019; Sugii et al., 2017). We hypothesized that Runx2 may regulate differentiation of CNC-derived cells in a cell-autonomous manner at early stages, which may indirectly affect myogenesis in the soft palate mesenchyme.

### Loss of Runx2 in CNC-derived cells results in soft palate development defects

To test the functional significance of Runx2 in regulating soft palate muscle development, we specifically targeted Runx2 in CNC-derived palate mesenchymal cells. We first tested whether Osr2-Cre, which specifically labels the CNC-derived cell subset in the developing palatal mesenchyme from the beginning of palatal shelf outgrowth (Lan et al., 2007), could also label the CNC-derived population in the soft palate. We confirmed in Osr2-Cre;tdTomato mice that tdTomato+ cells indeed contribute to soft palate mesenchyme including the perimysial cells surrounding all soft palatal muscles as early as E14.5 (Figure 3—figure supplement 1A–G). Furthermore, co-expression of tdTomato and Runx2 in the soft palate suggested that we could use Osr2-Cre to specifically delete Runx2 in a subset of CNC-derived cells in the soft palate region (Figure 3—figure supplement 1A–G).

To test whether Runx2 is a key regulator of soft palate development, we next generated Osr2-Cre;Runx2fl/fl mice, which showed cleft soft palate (5/10), misoriented muscle fibers and reduced muscle size (10/10) along with defects in hard tissues including the palatine bone (3/6) and pterygoid process (6/6) (Figure 3A–F; Figure 3—figure supplement 2A–J). Intraoral imaging and CT scans showed soft palate cleft in Osr2-Cre;Runx2fl/fl mice (Figure 3A–F; Figure 3—figure supplement 2D). Notably, in analyzing the CT scans, we found that three out of six Runx2 mutant mice with missing palatine bones and more severe pterygoid plate defects also had soft palate clefts, while the other three Runx2 mutants without clefts exhibited palatine bones that were smaller, though not statistically significantly so, and less severe pterygoid plate defects, particularly shorter pterygoid plate height (Figure 3—figure supplement 2A–J), suggesting the severity of skeletal defects is associated with the variability of soft palate clefts in Osr2-Cre;Runx2fl/fl mice. Consistent with the CT scans, histological analysis showed that the height of pterygoid plate was reduced and muscle attachment was abnormal in the TVP region of Osr2-Cre;Runx2fl/fl mice (Figure 3G–H,L–M). Because the aponeurosis serves the important function of attaching the hard tissue to the muscle, we also analyzed the fibrous tendon tissue marked by Scx by RNAscope in situ hybridization. The tendon tissue did not extend to the midline in the palate primordium in the TVP region in Osr2-Cre;Runx2fl/fl mice as it did in the controls at E16.5 (Figure 3—figure supplement 3I–L). It could be seen more clearly at P0 that the aponeurosis in Osr2-Cre;Runx2fl/fl mice was thinner and it did not stretch from the lateral-oral side to the medial-nasal side as it did in control mice (Figure 3—figure supplement 4A–D), suggesting its attachment to the posterior bone probably was likely abnormal. As Runx2 is not expressed in the perimysial site of the TVP region, Therefore, this muscle attachment defect of the TVP might be due to disruption of the hard tissue and aponeurosis. In the LVP region, the muscles were reduced in size in Osr2-Cre;Runx2fl/fl mice compared to controls (Figure 3I–K,N–P). Interestingly, a significant number of LVP muscle fibers had anterior-posterior alignment in Osr2-Cre;Runx2fl/fl mice (Figure 3O–P), compared to the uniform lateral-medial alignment of LVP muscle fibers in controls (Figure 3J–K). This suggests that the muscle fibers were mis-oriented, similar to the phenotype seen in patients with cleft soft palate. Additionally, we observed that the muscle fibers had centralized nuclei in the soft palate of Osr2-Cre;Runx2fl/fl mice, which suggests that they had muscle differentiation defects (Figure 3P). Similar muscle defects were also observed in other palatal muscles such as the PLP (Figure 3—figure supplement 3C–D,G–H). We concluded that loss of Runx2 leads directly to defects in CNC-derived cells and indirectly to muscle defects in the soft palate.

![Figure 3.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig3-v1.jpg)

**Figure 3.:** (A, B) Intraoral views of palates from control and Osr2-Cre;Runx2fl/fl mice at newborn stage (P0). Arrow indicates the cleft in the posterior part of the soft palate. (C–F) Sagittal (C–D) and coronal (E–F) views of microCT scans of newborn control and Osr2-Cre;Runx2fl/fl mice (N = 3). Red arrows indicate the normal soft palate, and asterisks indicate the cleft in the posterior part of soft palate. (G–P) H and E staining of soft palate coronal sections from control and Osr2-Cre;Runx2fl/fl mice at P0 (N = 5). Yellow dashed lines outline the soft palate muscles. Black and red arrows in H and M show the pterygoid plate and tensor veli palatini (TVP) defects, respectively, of Osr2-Cre;Runx2fl/fl mice. Asterisks in N indicate the cleft soft palate in the levator veli palatini (LVP) region of Osr2-Cre;Runx2fl/fl mice. Boxed areas in G, I, L, and N are enlarged in H, J, M, and O, respectively. Boxed areas in J and O are enlarged in K and P, respectively. Scale bars in C-D and E-F indicate 0.5 mm and 0.9 mm, respectively. Scale bar in G indicates 400 µm for G, I, L, and N. Scale bar in H indicates 100 µm for H, J, M, and O. Yellow arrowheads in P indicate the centralized nuclei in mutant muscle cells.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A–G) Immunostaining of Runx2 and RNAscope in situ hybridization of tdTomato with myogenic marker Myod1 on coronal sections of tensor veli palatini (TVP), levator veli palatini (LVP), and palatopharyngeus (PLP) regions at E14.5. White dashed line outlines the palatal shelf in B. White and yellow boxes in A are enlarged in D and E. White boxes in B and C are enlarged in F and G, respectively. White arrows show the tdTomato+ cells surround all soft palatal muscles in Osr2-Cre;tdTomato mice in D, F, and G. Yellow arrows show colocalization of Runx2 and tdTomato in E, F, and G. Scale bar in A indicates 100 µm in A-C. Scale bar in D indicates 50 µm in D-G.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (A, C, E, G) Isolated palatine bones and sphenoid bones from control (A,E) and Osr2-Cre;Runx2fl/fl (C, G) mice. (B, D, F, H) Coronal views of soft tissue microCT scans of newborn control (B,F) and Osr2-Cre;Runx2fl/fl mice (D,H). (I): Quantification of the size (length and height) of the pterygoid plate from control (red bars) and Osr2-Cre;Runx2fl/fl (blue bars) mice. ***p<0.001; ****p<0.0001. (J): Quantification of the size (length, width and height) of the palatine bone and the size (length and height) of the pterygoid plate from control (red bars) and Osr2-Cre;Runx2fl/fl (blue bars) mice. **p<0.01. PB: Palatine bone; PP: Pterygoid plate. Red dashed lines outline the palatine bone. Blue dashed lines outline the pterygoid plate. White asterisk indicates the missing palatine bone or cleft. Red arrows indicate the normal soft palate. Scale bars in A and B indicate 0.6 mm for A, C, E, G and B, D, F, H, respectively.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** (A–H) H and E staining of soft palate coronal sections from control and Osr2-Cre;Runx2fl/fl mice at P0. Yellow dashed lines outline the soft palatal muscles. Asterisks in G indicate the cleft soft palate in the PLP region of Osr2-Cre;Runx2fl/fl mice. Boxed areas in A, C, E, and G are enlarged in B, D, F, and H, respectively. (I–L) RNAscope in situ hybridization of Scx and immunostaining of MHC in the tensor veli palatini (TVP) regions of coronal sections of E16.5 control and Osr2-Cre;Runx2fl/fl mice. Asterisks indicate the altered tendon structure in Osr2-Cre;Runx2fl/fl mice. Scale bar in A indicates 400 µm for A, C, E, G. Scale bar in B indicates 100 µm for B, D, F, H. Scale bars in I and J indicate 100 µm for I, K and J, L, respectively.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig3-figsupp4-v1.jpg)

**Figure 3—figure supplement 4.:** (A–D) RNAscope in situ hybridization of Scx of coronal sections in the tensor veli palatini (TVP) region of P0 control and Osr2-Cre;Runx2fl/fl mice. Scale bar in A indicates 100 µm for A and C. Scale bar in B indicates 25 µm for B and D.

To examine soft palate muscle differentiation in Osr2-Cre;Runx2fl/fl mice, we analyzed expression of myogenic markers at multiple developmental stages to identify the time point at which muscle defects began to appear using the LVP as an example. In the LVP, there was no apparent change of early myogenic marker MyoD expression between control and Osr2-Cre;Runx2fl/fl mice at E13.5 (Figure 4—figure supplement 1A–B). MyoD staining revealed that defects started to appear at E14.5 (Figure 4A–B), when the palatal shelves began to grow and protrude towards the midline. Expression of the late myogenic marker MHC was decreased in the soft palate of Osr2-Cre;Runx2fl/fl mice compared to controls at E15.5 (Figure 4C–D), suggesting delayed muscle differentiation. This reduced expression of MHC persisted in the soft palate of Osr2-Cre;Runx2fl/fl mice at E16.5 (Figure 4—figure supplement 1C–D). MHC staining suggested that the myoblasts had fused to form myofibers, which were uniformly aligned in layers running in the lateral-to-medial direction in the LVP of control samples at E15.5 (Figure 4C). However, more immature myoblasts and fewer differentiated myofibers were present in Osr2-Cre;Runx2fl/fl mice (Figure 4D) and the myofibers extended in different directions, potentially hindering further muscle development and compromising physiological function.

![Figure 4.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig4-v1.jpg)

**Figure 4.:** (A–B) MyoD and (C–D) MHC immunostaining on coronal sections of the LVP regions of control and Osr2-Cre;Runx2fl/fl mice at E14.5 and E15.5. Yellow dashed lines outline the myogenic cells. Boxed areas are enlarged as insets in the same image. (E–H) Immunostaining of BrdU and MyoD on coronal sections from the LVP regions of control and Osr2-Cre;Runx2fl/fl mice at E14.5 and E15.5. Yellow dashed lines outline the location of myogenic cells in the LVP regions. Boxed areas are enlarged as insets in the same image. White arrows in the insets indicate BrdU+ myogenic cells. (I–L) Quantitation of proliferation rates of CNC-derived and myogenic cells in E14.5 (I–J) and E15.5 (K–L) coronal sections of the LVP regions of control (E, G) and Osr2-Cre;Runx2fl/fl (F, H) mice (N = 3 mice, four sections per region per mouse). White dashed lines outline the palatal shelf. * indicates p value = 0.02. Scale bars in A and E indicate 100 µm for A-D and E-H, respectively.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A–B) Immunostaining of BrdU and MyoD on coronal sections of the LVP regions of control and Osr2-Cre;Runx2fl/fl mice at E13.5. (C–D) Immunostaining of MHC on coronal sections of the LVP regions of control and Osr2-Cre;Runx2fl/fl mice at E16.5. (E–H) Immunostaining of Caspase three on coronal sections of the LVP regions of control and Osr2-Cre;Runx2fl/fl mice at E14.5 (E–F) and E15.5 (G–H). White arrows indicate Caspase3+ cells in E-H. Yellow dotted lines outline the location of myogenic cells in the LVP regions. White dashed lines outline the palatal shelf primordium or the palatal shelf. Scale bars in A and E indicate 100 µm for A-D and E-H, respectively.

To investigate the cellular mechanism underlying soft palate defects in Osr2-Cre;Runx2fl/fl mice, we analyzed cell proliferation, apoptosis, and differentiation. Consistent with the MyoD expression pattern, we did not detect any change in the number of BrdU+ proliferating cells in the LVP region of Osr2-Cre;Runx2fl/fl mice compared to controls at E13.5 (Figure 4—figure supplement 1A–B). In the LVP region at E14.5 and E15.5, the proliferation rate of MyoD- CNC-derived cells did not have significant difference in the perimysial sites of Osr2-Cre;Runx2fl/fl mice compared to controls (Figure 4E–H,I,K). The proliferation rate of MyoD+ myogenic cells was not significantly different between controls and Runx2 mutants at E14.5 (Figure 4E–F,J), but a significant reduction in the proliferation rate was observed in Runx2 mutants at E15.5 (Figure 4G–H,L). We also performed caspase3 immunofluorescence staining to investigate cell apoptosis. The number of apoptotic cells was indistinguishable between controls and mutants at E14.5 and E15.5 (Figure 4—figure supplement 1E–H). It is worth noting that although the proliferation rate of CNC-derived cells in the Runx2 mutant mice were not significantly different from that of the controls, we observed that they had fewer and less proliferative MyoD+ cells than Runx2fl/fl control mice. These differences might be due to altered signaling in CNC-derived cells causing the reduction of MyoD expression as well as proliferation defects of myogenic cells in Osr2-Cre;Runx2fl/fl mice.

### Runx2 plays an important role in the lineage commitment of CNC-derived cells in the soft palate

To investigate whether Runx2 regulates CNC-derived cell fate determination during soft palate development, we compared cell composition and gene expression profiles of E14.5 Osr2-Cre;Runx2fl/fl and control soft palates using scRNA-seq, bulk RNA-seq, and in vivo expression analyses. Using integration analysis based on shared variance, we identified similar cell clusters in the soft palates of control and Osr2-Cre;Runx2fl/fl mice at this stage. However, the composition of the CNC-derived cells was altered in the Runx2 mutants compared to controls (Figure 5A). Using markers of different subtypes of CNC-derived cells, we observed that the percentage of perimysial cells (Cluster 4) in the population decreased in Runx2 mutants, while the percentage of midline mesenchymal cells (Clusters 0 and 3) increased (Figure 5B). Moreover, in situ RNAscope staining revealed decreased expression of perimysial markers in the soft palates of Runx2 mutants compared to controls at E14.5, suggesting the CNC-derived perimysial populations were affected, potentially leading to further myogenic defects (Figure 5—figure supplement 1A–H). Consistent with the scRNA-seq results, bulk RNA-seq also identified that certain genes associated with specific types of CNC-derived cells were differentially expressed in the Osr2-Cre;Runx2fl/fl mice (Figure 5—figure supplement 1I). A number of genes not exclusively associated with specific types of CNC-derived cells, including Twist1 and Meox2, were also identified as being differentially expressed in the bulk RNA-seq analysis (Figure 5—figure supplement 1I).

![Figure 5.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig5-v1.jpg)

**Figure 5.:** (A) Integration analysis of the soft palate regions of control and Osr2-Cre;Runx2fl/fl mice at E14.5. Left panel shows the integration analysis of control and Osr2-Cre;Runx2fl/fl at E14.5. Right panels show the split UMAP clustering views of CNC-derived mesenchymal cells from control and Osr2-Cre;Runx2fl/fl mice based on the integration analysis. Black dotted lines outline the different subtypes of CNC-derived mesenchymal cells in the soft palate. (B) Percentages of cells in different CNC-derived non-osteochondrogenic clusters in control and Osr2-Cre;Runx2fl/fl soft palates based on the integration analysis in (A). Red boxes and green boxes indicate the clusters with an increased and decreased percentages of cells, respectively, in Osr2-Cre;Runx2fl/fl mice compared to controls. (C) Violin plots show the comparative expression levels of Runx2 and Twist1 in different CNC-derived non-osteochondrogenic clusters. Red box highlights the differences in Runx2 and Twist1 expression in perimysial cell clusters. (D–K) Co-expression of Runx2 and Twist1 on coronal sections of the levator veli palatini (LVP)regions of control and Osr2-Cre;Runx2fl/fl mice at E14.5. Yellow dashed lines outline the myogenic sites. Red, yellow and blue boxes in D and H are enlarged in E, F, G and I, J, K, respectively. White dashed lines outline the palatal shelf. Scale bar in D indicates 100 µm for D and H. Scale bar in E indicates 20 µm for E-G and I-K.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A–H) Expression of Runx2 and perimysial markers Hic1 (A–D) and Aldh1a2 (E–H) on coronal sections of the levator veli palatini (LVP) regions of control and Osr2-Cre;Runx2fl/fl mice at E14.5. Yellow dotted lines outline the myogenic sites. White boxes in A, B, E, and F are enlarged in C, D, G, and H, respectively. (I) Heatmap comparison of expression profiles of lineage-specific and general cranial neural crest (CNC)-derived cell markers between control and Osr2-Cre;Runx2fl/fl mice at E14.5 by bulk RNA-seq. White dashed lines outline the palatal shelf. Scale bars in A, C, E, and G indicate 100 µm for A-B, C-D, E-F, and G-H, respectively.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) Co-expression of Twist1 and candidate progenitor marker Tfap2b, perimysial-specific marker Aldh1a2 and midline mesenchymal-specific marker Tbx22 in the integrated E13.5-E15.5 cranial neural crest (CNC)-derived cells of the soft palate mesenchyme. (B–G) Expression of Twist1 (B, D, F) and MyoD or Myod1 (C, E, G) on the coronal sections of the levator veli palatini (LVP) regions of control mice from E13.5 to E15.5. Yellow dashed lines show the location of myogenic cells in the soft palate. White dashed lines outline the palatal shelf. Scale bar in B indicates 100 µm for B-G.

We focused our attention on Twist1, which inhibits binding of Runx2 to its downstream targets and antagonizes Runx2’s function in osteoblasts (Bialek et al., 2004). We began by analyzing the expression pattern of Twist1 during soft palate development. Based on the integration analysis of E13.5-E15.5 single-cell transcriptomes from controls, we observed Twist1 was primarily expressed in midline mesenchymal cells (Tbx22+), while its expression in CNC-derived common progenitors and perimysial cells (Tfap2b+; Aldh1a2+) was relatively low (Figure 5—figure supplement 2A). In addition, expression of Twist1 in the CNC-derived cells changed over time. In the LVP region, at E13.5 Twist1 was expressed at a low level in the palate primordium and perimysial sites (Figure 5—figure supplement 2B–C). At E14.5, expression of Twist1 in the palate primordium had increased, whereas its expression was maintained at a low level in the perimysial site (Figure 5—figure supplement 2D–E). At E15.5, Twist1 showed a similar expression pattern to that of E14.5 (Figure 5—figure supplement 2F–G). This spatiotemporally specific Twist1 expression in the palate primordium and myogenic regions of the soft palate was accompanied by an opposite trend in Runx2 expression in the same regions at the same stages. This is perhaps shown most clearly by the colocalization of Runx2 and Twist1 in the LVP region at E14.5 (Figure 5D–G), which suggested that expression levels of Runx2 and Twist1 are tightly coordinated during soft palate development. Interestingly, we discovered that expression of Twist1 was upregulated in most of the palatal shelf region including the perimysial cells in Osr2-Cre;Runx2fl/fl mice (Figure 5H–K), which suggests that upregulation of Twist1 in the CNC-derived cells may interrupt their fate determination.

### Haploinsufficiency of Twist1 rescues soft palate defects in Osr2-Cre;Runx2fl/fl mice

Based on the complimentary expression patterns of Runx2 and Twist1 in the soft palate, we hypothesized that they may oppose each other in regulating their common downstream targets which are important for fate determination of CNC-derived cells. Therefore, we performed ATAC-seq and found that both Runx2 and Twist1 binding sites are present in the regulatory region located around 15–40 kb downstream of the genetic locus of perimysial marker Aldh1a2 (Figure 6A), suggesting that both Runx2 and Twist1 might directly regulate the expression of Aldh1a2. However, as the binding sites of those two transcription factors are more than 20 kb apart, they are likely to regulate Aldh1a2 independently. Based on this finding, we sought to investigate whether haploinsufficiency of Twist1 may rescue the soft palate defects in Osr2-Cre;Runx2fl/fl mice by generating Osr2-Cre;Runx2fl/fl;Twist1fl/+ mice. Histological analysis confirmed that the palatal stromal mesenchyme, pterygoid plate, and muscle defects were all indeed rescued in these mice. None of the five newborn Osr2-Cre;Runx2fl/fl;Twist1fl/+ pups we collected had palatal clefts, compared to the 50% penetrance of cleft soft palate in Osr2-Cre;Runx2fl/fl mice (Figure 6B–G). Pterygoid plate height was restored in Osr2-Cre;Runx2fl/fl;Twist1fl/+ mice (Figure 6B–D,H), and muscle fiber orientation and muscle size were also recovered (Figure 6E–G). To confirm whether the rescue of these muscle defects was due to restoration of perimysial genes, we performed in situ hybridization expression analysis of the soft palate of Osr2-Cre;Runx2fl/fl;Twist1fl/+ mice at E14.5 (Figure 6J–R). Aldh1a2 was downregulated in the region (Figure 6K) where Runx2 was deleted (Figure 6N) and Twist1 expression was expanded in the soft palate of Osr2-Cre;Runx2fl/fl mice (Figure 6Q). Compared to Osr2-Cre;Runx2fl/fl mice, the expression of Aldh1a2 was restored in the Osr2-Cre;Runx2fl/fl;Twist1fl/+mice at E14.5 (Figure 6L). This suggests that Runx2 and Twist1 exhibit opposite regulatory effects on the expression of Aldh1a2 in a subset of CNC-derived cells, which may be important for regulating muscle differentiation in the soft palate. Since haploinsufficiency of Twist1 in Osr2-Cre;Runx2fl/fl;Twist1fl/+ mice rescues the expression of Aldh1a, it is most likely that Runx2 activates the expression of Aldh1a2 through repressing Twist1 instead of directly activating Aldh1a2 during normal soft palate muscle development (Figure 6—figure supplement 1).

![Figure 6.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig6-v1.jpg)

**Figure 6.:** (A) ATAC-seq peaks showing Twist1- and Runx2-binding sites are present in the opened regulatory regions near the Aldh1a2 locus in the soft palate tissue. (B–G) H and E staining of tensor veli palatini (TVP) and levator veli palatini (LVP) coronal sections in P0 control, Osr2-Cre;Runx2fl/fl and Osr2-Cre;Runx2fl/fl;Twist1fl/+ mice (N = 5). Yellow dashed lines outline the location of myogenic cells. Arrows indicate comparable structures in the pterygoid plates (PP) of control and Osr2-Cre;Runx2fl/fl;Twist1fl/+ mice. Asterisk indicates defective pterygoid plate, palate and LVP muscles in Osr2-Cre;Runx2fl/fl. (H) Quantification of the height of the palatine bone from control (red bars), Osr2-Cre;Runx2fl/fl (blue bars) mice and Osr2-Cre;Runx2fl/fl;Twist1fl/+ (yellow bars) mice (N = 5). (I) Schematic drawings of Myod1 (green), styloid process of temporal bone (SP) and hyoid bone (HB) on coronal sections in the LVP region of E14.5 control mice. (J–R) Aldh1a2 RNAscope in situ hybridization (J–L), Runx2 immunostaining (M–O) and Twist1 RNAscope in situ hybridization (P–R) in E14.5 LVP coronal sections of control, Osr2-Cre;Runx2fl/fl and Osr2-Cre;Runx2fl/fl;Twist1fl/+ mice. White dashed lines outline the palatal shelf. Scale bars in B and J indicate 100 µm for B-G and J-R, respectively.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/62387/elife-62387-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Loss of Runx2 results in upregulated expression of Twist1 and inhibits Aldh1a2 regulating retinoic acid secretion in the palatal mesenchyme, resulting in muscle defects. PS: Palatal shelf.

## Discussion

CNC-derived cells are essential for craniofacial musculoskeletal development, as they give rise to multiple hard and soft tissues in the system, and guide muscle development (Heude et al., 2011; Sugii et al., 2017; Tzahor, 2015). These multiple roles are likely achieved by different subtypes of CNC-derived cells. The heterogeneity of CNC-derived cells has long been studied in the palate based on its anatomical structures along the anterior-posterior, mediolateral, and oral-nasal axes (Bush and Jiang, 2012; Han et al., 2009; Li et al., 2017; Potter and Potter, 2015). To date, understanding of the molecular heterogeneity in different regions of the soft palate mesenchyme has mainly been based on location-specific genes that control local development and signal induction during palate outgrowth (Han et al., 2009; Potter and Potter, 2015). However, this does not completely explain how molecular heterogeneity contributes to the multiple roles played by CNC-derived cells during palate formation, or specifically how they guide soft palate muscle development.

In this study, we have revealed the cellular-level heterogeneity in the soft palate and established that different subtypes of CNC-derived cells are associated with distinct differentiation potentials and functions. Functional analysis of each CNC-derived cluster shows previously unknown subtypes of CNC-derived cells, and computational analysis suggests previously unknown lineage differentiation trajectories. Tfap2b+ cells are the least differentiated subtype and give rise to Aldh1a2+ perimysial progenitor cells and Top2a+ transitioning cells, which further differentiate into perimysial fibroblasts and midline mesenchymal fibroblasts. Tfap2b+ common progenitors, transitioning cells and some Aldh1a2+ perimysial progenitor cells are transiently present only at early stages of soft palate development, consistent with their roles as progenitors. This transient presence of CNC-derived progenitor cells is similar to that of neural crest cells, which are known to be pluripotent during embryonic development and disappear at later stages (Bronner and LeDouarin, 2012). In addition, we show that markers labeling soft palate perimysial populations, such as Hic1, Aldh1a2, and Tbx15, are also expressed by connective tissues in other craniofacial muscles, including the tongue and masseter muscles. Consistent with our findings, Aldh1a2 is known as an important enzyme for retinoic acid signaling, which is crucial for neural crest cells as they guide the positioning of extraocular muscles (Matt et al., 2008). The potential myogenic-supportive function of Hic1 has been confirmed by the recent finding that the Hic1+ population represents a source of quiescent mesenchymal progenitors that play important roles during the regeneration of skeletal muscles in the limbs (Scott et al., 2019). Hence, Aldh1a2 and Hic1 might be novel markers for CNC-derived perimysial tissues, which may perform important pro-myogenic functions during muscle development.

During embryonic development, the palatal shelves grow in a lateral-to-medial direction both before and after their elevation (Bush and Jiang, 2012). Consistent with this, our in vivo analysis shows that the least differentiated Tfap2b+ subpopulation is located in the lateral region of the soft palate during the early stages of its development, and the perimysial and midline mesenchymal populations reside in central myogenic sites and the medial region of the soft palate. Our results have revealed complex cellular heterogeneity and a differentiation hierarchy of cell populations that contribute to the craniofacial musculoskeletal system, which will require further analysis.

Recently, studies have found that several transcription factors regulate the development of different components of a musculoskeletal complex in a coordinated fashion to form a functional unit (Colasanto et al., 2016; Hasson et al., 2010; Mathew et al., 2011; Vickerman et al., 2011). Our study shows that Runx2 is expressed in CNC-derived cells involved in early cell fate determination and in perimysial cells in the soft palate mesenchyme. Loss of Runx2 in CNC-derived cells of the soft palate mesenchyme leads to multiple tissue defects in the soft palate, including fibrous tendon tissue, soft palate cleft and muscle defects. There is a fate change of CNC-derived cells from perimysial cells to midline mesenchymal cells in the soft palate of Runx2 mutant mice. As perimysial cells are closely associated with muscle development, loss of Runx2 affecting their differentiation may in turn affect their secretion of signaling cues that promote muscle proliferation and differentiation. Indeed, we show that multiple genes associated with pro-myogenic secreted factors specifically expressed by perimysial populations, such as Aldh1a2, Igf1, Cxcl12, and Cthrc1, are downregulated in Runx2 mutant mice (Matt et al., 2008; Schiaffino and Mammucari, 2011; Spector et al., 2013; Vasyutina et al., 2005). Our study provides clues as to how those transcription factors might play different roles in regulating multiple musculoskeletal system components, but how the development of multiple components is integrated still needs further investigation.

Transcription factors often regulate different downstream targets in distinct tissues. Previous studies have shown that Runx2 regulates the differentiation of CNC-derived cells during early tooth and intramembranous bone formation through distinct sets of downstream targets including Gli1, Lef1, Tcf1, Wnt10a, Wnt10b, and Tgfb1 in osteogenic cells and Dusp6, Enpp1, Igfbp3, and Fgf3 in dental mesenchyme (James et al., 2006). In this study, we have shown that downstream targets of Runx2 have differing responses to the loss of Runx2 in the soft tissue. Perimysial markers were specifically downregulated upon loss of Runx2, while genes expressed specifically in the midline mesenchymal cells and a set of more broadly expressed genes are upregulated. Although Runx2 has both transcriptional activation and repression domains, its different regulatory effects on distinct downstream targets in the soft palate mesenchyme could be direct or indirect. Our results thus reveal previously unknown roles of Runx2 in muscle development and help to elucidate the tissue-specific regulatory mechanisms by which Runx2 guides development.

Twist1 suppresses the function of its binding partner Runx2 through blocking the DNA binding domain of Runx2 to inhibit osteoblast differentiation and promote chondrocyte maturation (Bialek et al., 2004; Hinoi et al., 2006). In this study, we reveal complimentary expression patterns of Runx2 and Twist1 in the perimysial and midline mesenchymal populations during soft palate development, which seems to confirm their antagonistic interaction (Bialek et al., 2004). However, in contrast to the previously reported model of Twist1 and Runx2 antagonistic interaction, we show that loss of Runx2 in CNC-derived cells leads to abnormal upregulation of Twist1 in the perimysial population. Further analysis has shown that suppression of Twist1 in the perimysial population by Runx2 is necessary to maintain the expression level of perimysial marker gene Aldh1a2, which may be important for regulating muscle development. Our findings thus reveal a novel mechanism of Runx2-Twist1 genetic interaction that integrates the development of different types of CNC-derived cells with muscles to guide them to form a functional unit in the soft palate.

In summary, our study reveals a complex cellular heterogeneity within the developing soft palate and demonstrates that distinct subpopulations of CNC-derived cells are associated with distinct functions, which coordinate to form intricately connected components of the oropharyngeal complex. Moreover, the regulation of myogenesis by perimysial CNC-derived cells through Runx2-Twist1 interaction in the soft palate might also be shared by other craniofacial musculoskeletal structures. Our study highlights the complex regulatory roles of CNC-derived cells in the development of craniofacial musculoskeletal systems and provides knowledge that may lead to new strategies for craniofacial muscle regeneration.

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
      <td>Strain, strain background (M. musculus)</td>
      <td>Runx2flox/flox</td>
      <td>Takarada et al., 2013</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>Twist1flox/flox</td>
      <td>Bildsoe et al., 2009</td>
      <td>RRID:MMRRC_016842-UNC</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>ROSA26loxp-STOP-loxp-tdTomato</td>
      <td>Jackson Laboratory</td>
      <td>Stock No. 007905; RRID:IMSR_JAX:007905</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus)</td>
      <td>Osr2-Cre</td>
      <td>Rulang Jiang, Cincinnati Children’s Hospital</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-Myod1 probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 316081</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-Scx probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 439981</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-Twist1 probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 414701</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-Aldh1a2 probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 447391</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-Hic1 probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 464131</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-Tfap2b probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 536371</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-Tbx22 probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 426511</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-Ibsp probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 415501</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-Col2a1 probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 407221</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-Tbx15 probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 558761</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-Top2a probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 491221</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mm-tdTomato probe</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 317041</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-Runx2</td>
      <td>Cell Signaling Technology</td>
      <td>RRID:AB_2732805 Cat# 12556S</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-active Caspase 3</td>
      <td>Cell Signaling Technology</td>
      <td>RRID:AB_2341188 Cat# 9661S</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat monoclonal anti-BrdU</td>
      <td>Abcam</td>
      <td>RRID:AB_305426 Cat# ab6326</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-MyoD</td>
      <td>DAKO</td>
      <td>RRID:AB_2148874 Cat# M3512</td>
      <td>(1:20)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-MHC</td>
      <td>DSHB</td>
      <td>Cat# P13538</td>
      <td>(1:10)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-Mouse Alexa Fluor 488</td>
      <td>Life Technologies</td>
      <td>RRID:AB_2534069 Cat# A11001</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-Mouse Alexa Fluor 568</td>
      <td>Life Technologies</td>
      <td>RRID:AB_2534072 Cat# A-11004</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-Rat Alexa Fluor 488</td>
      <td>Life Technologies</td>
      <td>RRID:AB_141373 Cat# A-11006</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-Rabbit Alexa Fluor 488</td>
      <td>Life Technologies</td>
      <td>RRID:AB_143165 Cat# A-11008</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-Rabbit Alexa Fluor 568</td>
      <td>Life Technologies</td>
      <td>RRID:AB_10563566 Cat# A-11036</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Alexa Fluor 488 Tyramide SuperBoost Kit, goat anti-mouse IgG</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat# B40912</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNAscope Multiplex Fluorescent Kit v2</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 323110</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNAscope 2.5 HD Assay – RED</td>
      <td>Advanced Cell Diagnostics</td>
      <td>Cat# 322350</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TSA Plus Cyanine 3 System</td>
      <td>Perkin Elmer</td>
      <td>Cat# NEL744001KT</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TSA Plus Fluoresceine System</td>
      <td>Perkin Elmer</td>
      <td>Cat# NEL771B001KT</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNeasy Micro Kit</td>
      <td>QIAGEN</td>
      <td>Cat# 74004</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>DAB Peroxidase (HRP) Substrate Kit (With Nickel)</td>
      <td>Vector Laboratories</td>
      <td>RRID:AB_2336382 Cat# SK4100</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Chromium Single Cell 30 GEM, Library and Gel Bead Kit v3</td>
      <td>10x Genomics Inc</td>
      <td>Cat#1000092</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ</td>
      <td>NIH</td>
      <td>RRID:SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Ingenuity Pathway Analysis</td>
      <td>Qiagen.Inc</td>
      <td>RRID:SCR_008653</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism</td>
      <td>GraphPad Software</td>
      <td>RRID:SCR_002798</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Seurat</td>
      <td>Satija lab</td>
      <td>RRID:SCR_016341</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Monocle3</td>
      <td>Trapnell lab</td>
      <td>RRID:SCR_018685</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cell ranger</td>
      <td>10X Genomics.Inc</td>
      <td>RRID:SCR_017344</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BWA</td>
      <td>PMID:19451168; PMID:20080505</td>
      <td>RRID:SCR_010910</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MACS</td>
      <td>PMID:18798982</td>
      <td>RRID:SCR_013291</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Animals

The following mice were used in this study: Osr2-Cre (gift from Rulang Jiang, Cincinnati Children’s Hospital; Chen et al., 2009), Runx2 floxed mice (gift from Dr. Takeshi Takarada, Okayama University, Japan; Takarada et al., 2013), ROSA26loxp-STOP-loxp-tdTomato conditional reporter (JAX#007905, Madisen et al., 2010) and Twist1 floxed (MMRRC_016842-UNC; Bildsoe et al., 2009). To generate Osr2-Cre;Runx2fl/fl mice, we crossed Osr2-Cre;Runx2fl/+ mice with Runx2fl/fl mice. To generate Osr2-Cre;Runx2fl/fl;Twist1fl/+ mice, we bred Osr2-Cre;Runx2fl/+ mice with Runx2fl/fl;Twist1fl/+ mice. To generate Osr2-Cre;tdTomatofl/fl mice, we crossed Osr2-Cre;tdTomatofl/+ mice with tdTomatofl/fl mice. All mice were genotyped as previously described. All mice were used for analysis without consideration of sex. All studies were performed with the approval of the Institutional Animal Care and Use Committee (IACUC) at the University of Southern California. All the animals were handled according to approved IACUC protocol #9320 of the University of Southern California.

### MicroCT analysis

All microCT scans were performed using a SCANCO µCT50 device at the University of Southern California Molecular Imaging Center. Samples were scanned with the X-ray source at 70 kVp and 114 µA, and the data were collected at a resolution of 10 μM. Morphometric analysis was performed using the AVIZO 7.1 software package. Three biological replicates were performed. Measurements of hard tissues are based on the landmarks defined previously (Ho et al., 2015).

### Histological examination

Samples were fixed in 10% formalin, then decalcified in 10% EDTA followed by ethanol dehydration and paraffin embedding. Serial sections of 7 μm thickness were used for morphological analysis. These sections were stained using Hematoxylin and Eosin (H and E) following standard methods. Sections were imaged on a Keyence BZ-X710 microscope.

### In situ RNAscope hybridization

Mouse embryos were collected at E14.5 or E15.5 and fixed in 10% formalin. Samples were dehydrated with 15% and then 30% sucrose and embedded in OCT compound (Sakura, Tissue-Tek, Cat. 4583). OCT-embedded samples were sectioned at 8 µm on a cryostat. RNAScope 2.5 HD assay – red (Advanced Cell Diagnostics, Newark, CA, 322360) and RNAScope multiplex fluorescent v2 assay (Advanced Cell Diagnostics, 323100) were used for in situ hybridization according to the manufacturer’s instructions.

Probes from Advanced Cell Diagnostics for Myod1 (316081), Scx (439981), Twist1 (414701), Aldh1a2 (447391), and Hic1 (464131), Tfap2b (536371), Tbx22 (426511), Ibsp (415501), Col2a1 (407221), Tbx15 (558761), Top2a (491221), and tdTomato (317041) were used in this study.

### Immunofluorescence staining

Sections were processed with antigen-retrieval buffer (Vector Labs, Burlingame, CA, H-3300) for 15 min at 100°C, followed by 1% triton (Sigma Aldrich, St. Louis, MO, T8787) treatment for 10 min at room temperature. Afterwards, sections were incubated with blocking reagent (PerkinElmer, Waltham, MA, FP1012) for 1 hr at room temperature and the primary antibody overnight at 4°C. Alexa-conjugated secondary antibodies were used to show the fluorescence signal at 1:200 dilution. For myoblast determination protein 1 (MyoD), poly HRP-labeled goat anti-mouse IgG (ThermoFisher Scientific, Waltham, MA, B40912) was used as a secondary antibody and Alexa Fluor 488/594 Tyramide SuperBoost kit (PerkinElmer, Waltham, MA,NEL771B001KT, NEL774001KT) were used to develop the signal. Sections were counterstained with DAPI and imaged using a Leica DMI 3000B.

The following antibodies were used for immunostaining: Runx2 (Cell signaling technology, Danvers, MA, 12556S; 1:100), MyoD (DAKO, Carpinteria, CA, M3512; 1:25), myosin heavy chain (MHC; DSHB, Iowa City, IA, P13538; 1:10), active caspase 3 (Casp3; Cell signaling technology, Danvers, MA, 9661S; 1:100), and BrdU (BrdU; Abcam, Cambridge, UK, ab6326; 1:100). Anti-mouse, anti-rat and anti-rabbit Alexa Fluor 488 and 568 were used as secondary antibodies (A-11001, A-11004, A-11006, A-11008, A-11036, Thermofisher Scientific, Waltham, MA, 1:200).

### Single-cell RNA sequencing

Soft palate tissue (posterior third of the palatal region) was digested from E13.5, E14.5, and E15.5 controls and E14.5 Osr2-Cre;Runx2fl/fl embryos by TrypLE express enzyme (Thermo Fisher Scientific, Waltham, MA) at 37°C with shaking at 600 rpm for 20 min. Single-cell suspension was prepared according to the 10X Genomics sample preparation protocol. Seventeen thousand cells were loaded into the 10X Chromium system and prepared for single-cell library construction using the 10X Genomics Chromium single cell 3’ v3 reagent kit. Sequencing was performed on the Novaseq 6000 platform (Illumina, San Diego, CA). Library quality control, sequence alignment, and read counts were analyzed using the CellRanger pipeline version 3.0.2. Raw read counts from each single cell in each sample were analyzed using Seurat R package (Stuart et al., 2019). Cell clusters and variably expressed genes in each cluster were identified by using Log Normalize, Find Variable Genes, Scale Data, and RunPCA functions. Seurat three package was used to combine the single-cell data from three stages as well as E14.5 control and Osr2-Cre;Runx2fl/fl embryos to perform the integration analysis. Shared variances between different datasets were identified using the function FindIntegrationAnchors, then Seurat objects were processed using IntegrateData function. Scaledata, PCA, and UMAP visualization were then used for downstream analysis and visualization. Pseudotime trajectory analysis was done by Monocle three using Seurat 3 UMAP embedding to show cell fate restriction of CNC-derived soft palate mesenchymal cells across three development stages. Gene ontology and pathway analysis of enriched genes in different CNC-derived clusters was performed using Ingenuity Pathway Analysis (QIAGEN. Inc, Hilden, Germany).

### ATAC-seq

Single-cell suspension was prepared from the soft palate of E13.5-E14.0 control mice as described above and processed to generate ATAC-seq libraries according to a published protocol (Buenrostro et al., 2015). Sequencing was performed on the NextSeq 500 platform (Illumina, San Diego, CA). ATAC-seq reads were aligned to the UCSC mm10 reference genome using BWA-MEM (Li, 2013). ATAC-seq peaks were called by MACS2 (Zhang et al., 2008). Peaks were annotated and known transcription factor binding motifs were analyzed in the ATAC-seq peaks by HOMER (Heinz et al., 2010).

### RNA sequencing

Soft palate tissue was collected from control and Osr2-Cre;Runx2fl/fl embryos at E14.5. mRNA was isolated using RNeasy Micro Kit (QIAGEN, Hilden, Germany, 74404). Samples with RNA integrity number (RIN) >9.0 were used for cDNA library construction and sequencing by UCLA Technology Center for Genomics and Bioinformatics. Pair-end reads with 150 cycles sequencing were performed on Illumina NextSeq 500 platform. Sequence reads were trimmed and aligned using STAR (version 2.6.1d) using mm10 as the reference genome. Read counts were normalized using the upper quartile and differential expression was calculated using gene-specific analysis on the Partek Flow platform (Partek Inc, St. Louis, MO).

### Statistical analysis

T-tests were performed for statistical analysis using GraphPad Prism 7. Statistical data are presented as mean ± SEM.
