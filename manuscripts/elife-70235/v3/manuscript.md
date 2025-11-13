# Identification of bipotent progenitors that give rise to myogenic and connective tissues in mouse

## Authors

- Alexandre Grimaldi<sup>1</sup> ([ORCID: 0000-0002-5978-2057](https://orcid.org/0000-0002-5978-2057))
- Glenda Comai<sup>1</sup> ([ORCID: 0000-0003-3244-3378](https://orcid.org/0000-0003-3244-3378))
- Sebastien Mella<sup>4</sup> ([ORCID: 0000-0002-8679-5718](https://orcid.org/0000-0002-8679-5718))
- Shahragim Tajbakhsh<sup>1</sup> ([ORCID: 0000-0003-1809-7202](https://orcid.org/0000-0003-1809-7202)) †

### Affiliations

1. Stem Cells and Development Unit, Institut Pasteur Paris France ([ROR:0495fxg12](https://ror.org/0495fxg12))
2. UMR CNRS 3738, Institut Pasteur Paris France ([ROR:0495fxg12](https://ror.org/0495fxg12))
3. Sorbonne Universités, Complexité du Vivant, F-75005 Paris France ([ROR:02en5vm52](https://ror.org/02en5vm52))
4. Cytometry and Biomarkers UTechS, Institut Pasteur Paris France ([ROR:0495fxg12](https://ror.org/0495fxg12))
5. Bioinformatics and Biostatistics Hub, Institut Pasteur Paris France ([ROR:0495fxg12](https://ror.org/0495fxg12))

† Corresponding author

## Abstract

How distinct cell fates are manifested by direct lineage ancestry from bipotent progenitors, or by specification of individual cell types is a key question for understanding the emergence of tissues. The interplay between skeletal muscle progenitors and associated connective tissue cells provides a model for examining how muscle functional units are established. Most craniofacial structures originate from the vertebrate-specific neural crest cells except in the dorsal portion of the head, where they arise from cranial mesoderm. Here, using multiple lineage-tracing strategies combined with single cell RNAseq and in situ analyses, we identify bipotent progenitors expressing Myf5 (an upstream regulator of myogenic fate) that give rise to both muscle and juxtaposed connective tissue. Following this bifurcation, muscle and connective tissue cells retain complementary signalling features and maintain spatial proximity. Disrupting myogenic identity shifts muscle progenitors to a connective tissue fate. The emergence of Myf5-derived connective tissue is associated with the activity of several transcription factors, including Foxp2. Interestingly, this unexpected bifurcation in cell fate was not observed in craniofacial regions that are colonised by neural crest cells. Therefore, we propose that an ancestral bi-fated program gives rise to muscle and connective tissue cells in skeletal muscles that are deprived of neural crest cells.

## Introduction

Stromal cells that are associated with skeletal muscles play critical roles in providing structural support and molecular cues (Biferali et al., 2019; Kardon et al., 2003; Sefton and Kardon, 2019). The majority of muscle-associated connective tissues in the head is derived from cranial neural crest cells (NCCs), an embryonic cell population that contributes to most of the structural components of the ‘new head’, a vertebrate innovation (Le Douarin and Kalcheim, 1999; Gans and Northcutt, 1983; Grenier et al., 2009; Heude et al., 2018; Noden and Trainor, 2005). Recently, the extent of this contribution was redefined in muscles derived from cranial mesoderm, including extraocular (EOM), laryngeal and pharyngeal muscles (Comai et al., 2020; Grimaldi et al., 2015; Heude et al., 2018; Kuroda et al., 2021; Noden and Epstein, 2010). Interestingly, these muscles contain mesenchyme that is mesoderm-derived in their dorso-medial component, whereas the remaining muscle mass is embedded in mesenchyme that is neural crest-derived. It is unclear how the coordinated emergence of myogenic and connective tissues takes place during development, and how they establish long-lasting paracrine communication.

Along the trunk axis, paraxial somitic mesoderm gives rise to skeletal muscles and associated connective tissues (Burke and Nowicki, 2003). Upon signals emanating from adjacent tissues, the dermomyotome (dorsal portion of the somite) undergoes an epithelial-to-mesenchymal transition and gives rise to several cell types including all skeletal muscles of the body, vasculature, tendons and bones (Ben-Yair and Kalcheim, 2008; Christ et al., 2007). Similarly, cranial mesodermal progenitors give rise to these diverse cell types, yet, its unsegmented nature raises the question of how spatiotemporal control of these cellular identities is established. Moreover, cardiopharyngeal mesoderm, which constitutes the major portion of cranial mesoderm, has cardiovascular potential, which manifests in the embryo as regions of clonally related cardiac and craniofacial skeletal muscles (Diogo et al., 2015; Swedlund and Lescroart, 2020). This skeletal muscle/cardiac branchpoint has been the subject of intense investigation in several model organisms including ascidians, avians, and mouse (Wang et al., 2019). While cardiopharyngeal mesoderm was shown to give rise to connective tissues in the mammalian pharynx, the extent of its contribution to other craniofacial muscles in general has not been fully addressed (Adachi et al., 2020).

Recently, advanced pipelines integrating scRNAseq data and modern algorithms have been instrumental for identifying new lineage relationships during development (Cao et al., 2019; He et al., 2020; Qiu et al., 2021). Here, we employed lineage-restricted single-cell transcriptomics using multiple transgenic mouse lines combined with various computational methods, in situ labeling and loss-of-function experiments, and show that bipotent progenitors expressing the muscle determination gene Myf5 give rise to both skeletal muscle and anatomically associated connective tissues. Surprisingly, this property was restricted to muscle masses lacking NCC-derived connective tissues, indicating that cranial mesoderm acts as a source of connective tissues in the absence of neural crest cells.

## Results

### Myogenic and non-myogenic mesodermal populations coexist within distinct head lineages

Somitic (Pax3-dependent) and cranial (Tbx1/Pitx2-dependent) mesoderm give rise to diverse cell types including those of the musculoskeletal system (Figure 1A). We first set out to explore the emergence of skeletal muscles and other associated mesodermal tissue within these programs. To that end, we employed a broad anterior mesoderm lineage-tracing strategy using the Mesp1Cre/+;Rosa26mTmG/+ line as it labels cranial-derived mesoderm and the anterior somites (Heude et al., 2018). At E10.5, when craniofacial skeletal muscles start to be specified, the upper third (anterior to forelimb) of the embryos was dissected, live GFP+ cells were isolated by FACS, and processed for scRNAseq analysis (Figure 1—figure supplement 1A-C). After removal of doublets and lower quality cells (see Materials and methods), a large portion of the cells obtained by Mesp1Cre/+;Rosa26mTmG/+ lineage tracing segregated as individual clusters expressing markers of adipogenic, chondrogenic, sclerotomal, endothelial, and cardiovascular lineages as well as the foregut and primitive lung mesenchyme (Figure 1B, Figure 1—figure supplement 2A-B). Pax3, Pitx2, Tbx1, Myf5, and Myod expression were used to identify clusters containing the cranial myogenic progenitors, annotated as ‘Cardiopharyngeal mesoderm’ and ‘Anterior somite’ (Figure 1B–C, Figure 1—figure supplement 2A).

![Figure 1.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig1-v3.jpg)

**Figure 1.:** (A) Scheme of connective tissue origin in the head and known mesodermal upstream regulators. E: Eye, 1–4: Pharyngeal arches 1–4. (B–F) scRNAseq analysis on Mesp1Cre/+; Rosa26mTmG/+ embryos at E10.5 (2 datasets of 2 embryos were aggregated to generate this data, see methods). (B) UMAP of Mesp1Cre/+; Rosa26mTmG/+ E10.5 scRNAseq with main cell types highlighted. The clusters ‘Anterior somite’ and ‘Cardiopharyngeal mesoderm’ were subsetted for further analysis below. (C) UMAP expression plots of Pitx2 (EOM), Tbx1 (cranial mesoderm except EOM) and Pax3 (somitic mesoderm), indicating the clusters of progenitors that were selected. (D) UMAP of progenitor subset annotated as myogenic and non-myogenic based on expression patterns found in E and F. (E) UMAP expression plots of Pitx2, Tbx1 and Pax3 in the Mesp1Cre/+; Rosa26mTmG/+ E10.5 subset. (F) Heatmap of top 20 markers of myogenic versus non-myogenic clusters Mesp1Cre/+; Rosa26mTmG/+ E10.5 subset. Pdgfra/Pdgfa genes are highlighted.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** (A) Gating strategy used to isolate by FACS Mesp1Cre/+; Rosa26mTmG/+ cells. The FITC channel was used to identify GFP+ cells. The AmCyan channel was used to identify the Calcein Blue+ live cells. The PE-Texas Red channel was used to discard mTomato+ cells and Propidium Iodide+ cells. The percentage of cells captured by each gate is displayed on each plot. (B) Violin plots of gene count, UMI count and mitochondrial fraction for overall dataset. (C) Violin plots of gene count and UMI count by cluster (n = 2 pooled datasets).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig1-figsupp2-v3.jpg)

**Figure 1—figure supplement 2.:** (A) Mesp1Cre/+;Rosa26mTmG/+ E10.5 UMAP expression plots of markers of various mesodermal lineages. (B) Heatmap of top 5 markers of each cluster of Mesp1Cre/+;Rosa26mTmG/+ E10.5. (C) UMAP expression plot of the Mesp1Cre/+;Rosa26mTmG/+ E10.5 subset. En2: marker of pharyngeal arch 1 (Knight et al., 2008), En1: marker of epaxial somitic progenitors (Spörle, 2001), Lbx1: marker of tongue progenitors (Gross et al., 2000), Isl1: marker of cardiopharyngeal mesoderm of pharyngeal arch 2–6 (Nathan et al., 2008), Shox2: marker of caudal cardiopharyngeal mesoderm (Wang et al., 2020), Pitx2: marker of the extraocular region (Zacharias et al., 2011) (n = 2 pooled datasets).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig1-figsupp3-v3.jpg)

**Figure 1—figure supplement 3.:** (A) Pearson correlation plot of myogenic (Pdgfa, Myf5, Myod1, Myog, Acta2) and non-myogenic (Pdgfra, Prrx1, Meis1, Twist1, Osr1, Col1a1) genes in the Mesp1Cre/+;Rosa26mTmG/+ E10.5 subset. The size of the dots is inversely proportional to their p-value. A cross indicates a p-value > 0.05. The color of the dots indicates the strength of the positive (blue) or negative (red) correlation. (B) Expression patterns of Myf5, Myod, Myog, Pdgfa, Pdgfra, and Col1a1 in the Mesp1Cre/+;Rosa26mTmG/+ E10.5 subset dataset. Note that Myf5+ cells were overwhelmingly Pdgfra- and Myf5+/Pdgfra+ cells represent 8% of all cells (i.e. expressing at least one transcript of both genes). Pdgfra+ cells represent 40% of all cells (n = 2 pooled datasets).

After subsetting these clusters (‘Cardiopharyngeal mesoderm’ and ‘Anterior somite’), a few subclusters clearly separated based on their origin and anatomical location (Figure 1D–E, Figure 1—figure supplement 2C). Surprisingly, about half of the supposedly myogenic cells exhibited a connective tissue signature, including a strong bias toward Prrx1, a marker of lateral plate mesoderm (Durland et al., 2008), Col1a1, a major extracellular matrix component of connective tissue cells (De Micheli et al., 2020), and Twist1, a key determinant for the mesenchymal properties of cranial mesoderm (Bildsoe et al., 2016; Figure 1F). Furthermore, the expression of Pdgfra, a well-defined marker of stromal cells (Farahani and Xaymardan, 2015), was robustly anticorrelated with the expression of its ligand Pdgfa and associated with non-myogenic genes. Conversely, Pdgfa, was correlated with a myogenic cell state (Figure 1F, Figure 1—figure supplement 3A-B). Of note, myogenic Pdgfa expression was shown to promote adjacent sclerotomal cells to adopt a rib cartilage fate (Tallquist et al., 2000). Therefore, this analysis identified anatomically distinct muscle and closely associated connective tissue progenitors and highlights a potential PDGFR-mediated crosstalk between these 2 cells types.

### Transcriptional trajectories reveal a myogenic to non-myogenic cell state transition

To understand the lineage relationship between myogenic and non-myogenic cells, we exploited the unspliced and spliced variants of our scRNAseq data, and computed the RNA velocity in each cell, using a recently described tool (Bergen et al., 2020; Figure 2, Figure 2—figure supplement 1). RNA velocity interrogates the relative abundance of unspliced and spliced gene variants, which depends on the rates of transcription, degradation, and splicing to infer directional trajectories (Bergen et al., 2020; La Manno et al., 2018). The cell cycle status constitutes a potential bias in scRNAseq data, especially when heterogeneous populations undergo cellular expansion, commitment and differentiation (McDavid et al., 2016). To eliminate this potential bias, cell cycle genes were consistently regressed out during preprocessing and directional trajectories were overlaid with cell cycle phase visualization for comparisons (Figure 2—figure supplement 1A, Materials and methods). Notably, RNA velocity-inferred trajectories suggested that Myf5+ cells from the myogenic compartment contributed to non-myogenic cells (Figure 2A). These calculations were based on gene- and cluster-specific dynamics, which yield higher accuracy than the initially described RNA velocity method, while providing quantitative metrics for quality control (Figure 2—figure supplement 1B-D and Materials and methods).

![Figure 2.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig2-v3.jpg)

**Figure 2.:** (A) Velocity UMAP plots of Mesp1Cre/+; Rosa26mTmG/+ embryos at E10.5 displaying myogenic and non-myogenic clusters. Arrows represent the lineage progression based on RNA velocity (relative abundance of unspliced and spliced transcripts). (B) Heatmap of driver genes accounting for anterior somite velocity, highlighting Pdgfra. Driver genes are genes that are transcriptomically active in a given cluster. (C) Phase portraits of few selected driver genes in the anterior somites: Foxp1, Meox2, Meis1, Twist2, Fap, Pdgfra, Prrx1, and Pcolce. Y-axis represents the amount of unspliced transcript per cell; X-axis represents the number of spliced transcripts per cell. A high fraction of unspliced variants indicates an active transcription of the locus, while the inverse indicates inactive/repressed transcription. Dynamics of transcription were inferred at a gene- and cluster-specific level (see Methods). (D) Phase portraits, RNA velocity and expression plots of Pdgfa and Pdgfra showing splicing dynamics of these two genes. (E) Working model of myogenic and non-myogenic fate decisions from a common bipotent progenitor in anterior somites.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** (A) UMAP of Mesp1Cre/+;Rosa26mTmG/+ E10.5 subset with overlaid velocity and cell cycle phase. (B–D) Quality control metrics of scvelo, including velocity length, velocity confidence and spliced/unspliced abundance in the overall dataset and by cluster (n = 2 pooled datasets).

Another powerful feature of this method is the ability to infer ‘driver genes’ that are responsible for most of the calculated RNA velocity, hence actively transcribed, or repressed (Bergen et al., 2020). Therefore, these genes can identify transitory states underlying cell fate decisions. We used this approach to uncover the driver genes that were responsible for the velocity found in anterior somites, as these cells displayed the most consistent directionality, and appeared to be independent of cell cycle (Figure 2B, Figure 2—figure supplement 1A, Table 1). Top transcribed driver genes included Foxp1 (Shao and Wei, 2018), Meox2 (Noizet et al., 2016), Meis1 (López-Delgado et al., 2020), Twist2 (Franco et al., 2009), Fap (Puré and Blomberg, 2018), Pdgfra (Tallquist et al., 2000), Prrx1 (Leavitt et al., 2020), and Pcolce (Bildsoe et al., 2016; Figure 2C), which are associated with fibrosis and connective tissue development. Interestingly, we noted that Pdgfra appeared as a driver gene and was activated along this inferred trajectory, whereas Pdgfa expression decreased rapidly (Figure 2D). Taken together, RNA velocity analysis for anterior somite mesodermal progenitors showed that Myf5+/Pdgfa+ cells shifted toward a non-myogenic fate, which includes the downregulation of Myf5 and Pdgfa and the activation of Pdgfra expression (Figure 2E).

**Table 1.**
 Driver genes underlying cell fate decisions in each dataset.


<table>
  <thead>
    <tr>
      <th>E10.5 Anterior somites</th>
      <th>E11.5 EOM Myogenic</th>
      <th>E11.5 EOM Non-myogenic</th>
      <th>E12.5 Non-myogenic</th>
      <th>E14.5 Non-myogenic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tshz2</td>
      <td>Ccdc141</td>
      <td>Zfpm2</td>
      <td>Mgat4c</td>
      <td>Dnm1</td>
    </tr>
    <tr>
      <td>Eya1</td>
      <td>Mcm6</td>
      <td>Plxna4</td>
      <td>Cenpv</td>
      <td>Pid1</td>
    </tr>
    <tr>
      <td>C1qtnf3</td>
      <td>Dync1i1</td>
      <td>Col23a1</td>
      <td>C130073E24Rik</td>
      <td>Nrp2</td>
    </tr>
    <tr>
      <td>Meis2</td>
      <td>Tpm2</td>
      <td>Edil3</td>
      <td>Tbx3os1</td>
      <td>Ntrk3</td>
    </tr>
    <tr>
      <td>Limch1</td>
      <td>Celf2</td>
      <td>Map2</td>
      <td>E330013P04Rik</td>
      <td>Tmem132c</td>
    </tr>
    <tr>
      <td>Moxd1</td>
      <td>Sox6</td>
      <td>Rora</td>
      <td>Stk26</td>
      <td>Egflam</td>
    </tr>
    <tr>
      <td>Epha4</td>
      <td>Tnc</td>
      <td>Sema5a</td>
      <td>Edil3</td>
      <td>Gpr153</td>
    </tr>
    <tr>
      <td>Pitx2</td>
      <td>Magi3</td>
      <td>Colec12</td>
      <td>Fdft1</td>
      <td>Efemp1</td>
    </tr>
    <tr>
      <td>Parm1</td>
      <td>Sh3glb1</td>
      <td>Smoc1</td>
      <td>Lima1</td>
      <td>Adamts2</td>
    </tr>
    <tr>
      <td>Hpse2</td>
      <td>Parm1</td>
      <td>Ptprt</td>
      <td>Trim59</td>
      <td>Brinp1</td>
    </tr>
    <tr>
      <td>Lrrn1</td>
      <td>Ephb1</td>
      <td>Ror1</td>
      <td>Meg3</td>
      <td>Vegfc</td>
    </tr>
    <tr>
      <td>Dmrt2</td>
      <td>Bmpr1b</td>
      <td>Dock5</td>
      <td>Gins3</td>
      <td>Twist2</td>
    </tr>
    <tr>
      <td>Myl3</td>
      <td>Hells</td>
      <td>Map1b</td>
      <td>Tpm2</td>
      <td>Itgb5</td>
    </tr>
    <tr>
      <td>Fap</td>
      <td>Pdgfc</td>
      <td>Fn1</td>
      <td>Cdh6</td>
      <td>Gria1</td>
    </tr>
    <tr>
      <td>Hs6st2</td>
      <td>Ptprd</td>
      <td>Limch1</td>
      <td>Csmd3</td>
      <td>Sned1</td>
    </tr>
    <tr>
      <td>Ddr2</td>
      <td>Cnr1</td>
      <td>Tenm4</td>
      <td>Tceal5</td>
      <td>Sorcs3</td>
    </tr>
    <tr>
      <td>Cald1</td>
      <td>Sema3d</td>
      <td>Rbms3</td>
      <td>Pclaf</td>
      <td>Ebf2</td>
    </tr>
    <tr>
      <td>Prrx1</td>
      <td>Clcn5</td>
      <td>Srgap3</td>
      <td>Tspan9</td>
      <td>Fam19a1</td>
    </tr>
    <tr>
      <td>Magi3</td>
      <td>Chd7</td>
      <td>Tmem132c</td>
      <td>Eps8</td>
      <td>Trabd2b</td>
    </tr>
    <tr>
      <td>Ntn1</td>
      <td>Col25a1</td>
      <td>Sdc2</td>
      <td>Lmna</td>
      <td>Plxdc2</td>
    </tr>
    <tr>
      <td>Zfhx3</td>
      <td>Reep1</td>
      <td>Add3</td>
      <td>Dmrt2</td>
      <td>Sh3gl3</td>
    </tr>
    <tr>
      <td>Meis1</td>
      <td>Ctnnal1</td>
      <td>Pdgfra</td>
      <td>Cpeb4</td>
      <td>Luzp2</td>
    </tr>
    <tr>
      <td>Tnni1</td>
      <td>Tpm1</td>
      <td>Gmds</td>
      <td>Hpgd</td>
      <td>Pdzd2</td>
    </tr>
    <tr>
      <td>Crym</td>
      <td>Zim1</td>
      <td>St6galnac3</td>
      <td>Rcsd1</td>
      <td>Sema3e</td>
    </tr>
    <tr>
      <td>Ebf1</td>
      <td>Lmx1a</td>
      <td>Epb41l3</td>
      <td>Pdgfra</td>
      <td>Rims1</td>
    </tr>
    <tr>
      <td>Nr2f1</td>
      <td>Neb</td>
      <td>Pde3a</td>
      <td>Plac1</td>
      <td>Epha3</td>
    </tr>
    <tr>
      <td>Ntng1</td>
      <td>Atad2</td>
      <td>Tox</td>
      <td>Palmd</td>
      <td>Cyp7b1</td>
    </tr>
    <tr>
      <td>Pgm5</td>
      <td>Dapk2</td>
      <td>Smarca2</td>
      <td>Gucy1a1</td>
      <td>Gem</td>
    </tr>
    <tr>
      <td>Cdh6</td>
      <td>Prox1</td>
      <td>Ctdspl</td>
      <td>Wif1</td>
      <td>Ldb2</td>
    </tr>
    <tr>
      <td>Foxp1</td>
      <td>Lsamp</td>
      <td>Magi2</td>
      <td>Naalad2</td>
      <td>Scube1</td>
    </tr>
    <tr>
      <td>Celf2</td>
      <td>Ttn</td>
      <td>Dpysl3</td>
      <td>Smoc2</td>
      <td>Pdgfra</td>
    </tr>
    <tr>
      <td>Tbx1</td>
      <td>Pls3</td>
      <td>Fgfr2</td>
      <td>Rassf4</td>
      <td>Pde1a</td>
    </tr>
    <tr>
      <td>Bdnf</td>
      <td>Slf2</td>
      <td>Ldb2</td>
      <td>Pttg1</td>
      <td>Nde1</td>
    </tr>
    <tr>
      <td>Colec12</td>
      <td>Vat1l</td>
      <td>Igf1</td>
      <td>Josd2</td>
      <td>Enpp2</td>
    </tr>
    <tr>
      <td>Eya4</td>
      <td>E2f1</td>
      <td>Elk3</td>
      <td>Plxna4</td>
      <td>Fam107b</td>
    </tr>
    <tr>
      <td>Sobp</td>
      <td>Epb41l2</td>
      <td>Zmiz1</td>
      <td>Eya2</td>
      <td>Stxbp6</td>
    </tr>
    <tr>
      <td>Peg3</td>
      <td>Gm28653</td>
      <td>Dlc1</td>
      <td>Nrsn1</td>
      <td>Rerg</td>
    </tr>
    <tr>
      <td>Pdgfra</td>
      <td>Lrrn1</td>
      <td>Nhs</td>
      <td>Fign</td>
      <td>Prex2</td>
    </tr>
    <tr>
      <td>Nrk</td>
      <td>Mef2c</td>
      <td>Cdkn1c</td>
      <td>Inppl1</td>
      <td>Man1a</td>
    </tr>
    <tr>
      <td>Ptn</td>
      <td>St8sia2</td>
      <td>Plpp3</td>
      <td>Rnf152</td>
      <td>Tmem45a</td>
    </tr>
    <tr>
      <td>Daam1</td>
      <td>Tshz1</td>
      <td>Ebf1</td>
      <td>Lasp1</td>
      <td>Sh3bp4</td>
    </tr>
    <tr>
      <td>Dlk1</td>
      <td>Wee1</td>
      <td>Sorbs2</td>
      <td>Mrln</td>
      <td>Mcc</td>
    </tr>
    <tr>
      <td>Unc5c</td>
      <td>Slc24a3</td>
      <td>Baz1a</td>
      <td>Cdt1</td>
      <td>Ncald</td>
    </tr>
    <tr>
      <td>Lpar1</td>
      <td>Ncoa1</td>
      <td>Fat4</td>
      <td>Notch3</td>
      <td>Kdelr2</td>
    </tr>
    <tr>
      <td>Syne2</td>
      <td>Dek</td>
      <td>Golgb1</td>
      <td>Pax3</td>
      <td>Pcdh19</td>
    </tr>
    <tr>
      <td>Nkd2</td>
      <td>Kdm5b</td>
      <td>Hpse2</td>
      <td>Egfr</td>
      <td>Gas7</td>
    </tr>
    <tr>
      <td>Brinp1</td>
      <td>Unc13c</td>
      <td>Samd4</td>
      <td>Dbf4</td>
      <td>Cpt1c</td>
    </tr>
    <tr>
      <td>Zfhx4</td>
      <td>Ddr1</td>
      <td>Itga9</td>
      <td>Bcr</td>
      <td>Adam22</td>
    </tr>
    <tr>
      <td>Nnat</td>
      <td>Pip4k2a</td>
      <td>Magi1</td>
      <td>Mllt3</td>
      <td>Itgb8</td>
    </tr>
    <tr>
      <td>Gxylt2</td>
      <td>Fndc3c1</td>
      <td>Pcdh9</td>
      <td>Nectin1</td>
      <td>Dchs2</td>
    </tr>
    <tr>
      <td>Clmp</td>
      <td>Rbm24</td>
      <td>Tgfbr2</td>
      <td>Grin3a</td>
      <td>Cep350</td>
    </tr>
    <tr>
      <td>Ror2</td>
      <td>Rreb1</td>
      <td>Ntf3</td>
      <td>Cbfa2t3</td>
      <td>Oat</td>
    </tr>
    <tr>
      <td>Nfia</td>
      <td>Rragd</td>
      <td>Col11a1</td>
      <td>Cdh2</td>
      <td>Rab30</td>
    </tr>
    <tr>
      <td>Ebf2</td>
      <td>Acsl3</td>
      <td>Runx1t1</td>
      <td>Anln</td>
      <td>Aff2</td>
    </tr>
    <tr>
      <td>Ednra</td>
      <td>Acvr2a</td>
      <td>Tnrc18</td>
      <td>Ccdc6</td>
      <td>Gna14</td>
    </tr>
    <tr>
      <td>Fli1</td>
      <td>Zeb1</td>
      <td>Crym</td>
      <td>Mcu</td>
      <td>Slc29a1</td>
    </tr>
    <tr>
      <td>Tspan12</td>
      <td>Rgma</td>
      <td>Fap</td>
      <td>Fnip2</td>
      <td>Pls3</td>
    </tr>
    <tr>
      <td>Ttc28</td>
      <td>Arpp21</td>
      <td>Ppp1r1a</td>
      <td>Kcnk13</td>
      <td>Traf3ip1</td>
    </tr>
    <tr>
      <td>Nfib</td>
      <td>Lef1</td>
      <td>Tes</td>
      <td>Sned1</td>
      <td>Rcsd1</td>
    </tr>
    <tr>
      <td>Ccdc88c</td>
      <td>Nr2f2</td>
      <td>Bicc1</td>
      <td>Nde1</td>
      <td>Lgr4</td>
    </tr>
    <tr>
      <td>Col13a1</td>
      <td>Foxo1</td>
      <td>Il1rapl1</td>
      <td>Hipk3</td>
      <td>Zfp9</td>
    </tr>
    <tr>
      <td>2700069I18Rik</td>
      <td>Pdzrn4</td>
      <td>Alcam</td>
      <td>Arhgap11a</td>
      <td>Hs3st5</td>
    </tr>
    <tr>
      <td>Pcolce</td>
      <td>Hmga2</td>
      <td>2700069I18Rik</td>
      <td>Fam8a1</td>
      <td>Aspn</td>
    </tr>
    <tr>
      <td>Scn3a</td>
      <td>Lurap1l</td>
      <td>Dab2</td>
      <td>Kif21a</td>
      <td>Nrxn1</td>
    </tr>
    <tr>
      <td>Acvr2a</td>
      <td>Pkig</td>
      <td>Cntln</td>
      <td>Mtss1</td>
      <td>Rrm1</td>
    </tr>
    <tr>
      <td>Auts2</td>
      <td>Ncl</td>
      <td>Clmn</td>
      <td>Abcd2</td>
      <td>Igfbp7</td>
    </tr>
    <tr>
      <td>Col3a1</td>
      <td>CT025619.1</td>
      <td>Rbms1</td>
      <td>Irx5</td>
      <td>Slc35f3</td>
    </tr>
    <tr>
      <td>Gap43</td>
      <td>Erbb4</td>
      <td>Tmem2</td>
      <td>Pacs2</td>
      <td>Kif15</td>
    </tr>
    <tr>
      <td>Mrln</td>
      <td>Cdk14</td>
      <td>Cdh6</td>
      <td>Nab1</td>
      <td>Slc1a3</td>
    </tr>
    <tr>
      <td>Pax3</td>
      <td>Kif21a</td>
      <td>Lypd6</td>
      <td>Ccnd2</td>
      <td>Bmp6</td>
    </tr>
    <tr>
      <td>Sim1</td>
      <td>Zfp704</td>
      <td>Mmp2</td>
      <td>Bok</td>
      <td>Dkk2</td>
    </tr>
    <tr>
      <td>Epb41l2</td>
      <td>Nasp</td>
      <td>Kif5c</td>
      <td>Dok5</td>
      <td>Tspan9</td>
    </tr>
    <tr>
      <td>Ppp3ca</td>
      <td>Plekha5</td>
      <td>Cadm2</td>
      <td>Ncapg</td>
      <td>Ets1</td>
    </tr>
    <tr>
      <td>Tnfaip6</td>
      <td>Cap2</td>
      <td>Prkg2</td>
      <td>Rfx8</td>
      <td>Gria3</td>
    </tr>
    <tr>
      <td>Tmem132c</td>
      <td>Snca</td>
      <td>Cped1</td>
      <td>Fhod3</td>
      <td>Sox8</td>
    </tr>
    <tr>
      <td>Tmem2</td>
      <td>Epha4</td>
      <td>Dtl</td>
      <td>Tk1</td>
      <td>Melk</td>
    </tr>
    <tr>
      <td>Epb41l3</td>
      <td>Atad5</td>
      <td>Ror2</td>
      <td>Asf1b</td>
      <td>Ntm</td>
    </tr>
    <tr>
      <td>Crybg3</td>
      <td>Cntn3</td>
      <td>Utrn</td>
      <td>Tek</td>
      <td>Synpo2l</td>
    </tr>
    <tr>
      <td>Nrxn1</td>
      <td>Cacna2d1</td>
      <td>Foxp1</td>
      <td>Arfgef3</td>
      <td>Hlf</td>
    </tr>
    <tr>
      <td>Farp1</td>
      <td>Pak3</td>
      <td>L3mbtl3</td>
      <td>Rnf182</td>
      <td>Adamts5</td>
    </tr>
    <tr>
      <td>Sulf1</td>
      <td>Megf10</td>
      <td>Cdh23</td>
      <td>Kif14</td>
      <td>Plcb4</td>
    </tr>
    <tr>
      <td>Tmtc2</td>
      <td>Tnnt1</td>
      <td>Negr1</td>
      <td>1810041L15Rik</td>
      <td>Cdc25b</td>
    </tr>
    <tr>
      <td>Pde4dip</td>
      <td>Acta2</td>
      <td>Hmcn1</td>
      <td>Rrm2</td>
      <td>Mgat4a</td>
    </tr>
    <tr>
      <td>Phldb2</td>
      <td>Barx2</td>
      <td>Col26a1</td>
      <td>Fgf5</td>
      <td>Mdfic</td>
    </tr>
    <tr>
      <td>Plpp3</td>
      <td>Mrln</td>
      <td>Fbn2</td>
      <td>Barx2</td>
      <td>Trpc5</td>
    </tr>
    <tr>
      <td>Ybx3</td>
      <td>Pgm5</td>
      <td>Ankrd12</td>
      <td>Fli1</td>
      <td>Kif4</td>
    </tr>
    <tr>
      <td>Ppm1l</td>
      <td>Fmr1</td>
      <td>Lhfp</td>
      <td>Jph2</td>
      <td>Plce1</td>
    </tr>
    <tr>
      <td>Twist2</td>
      <td>Smc4</td>
      <td>Hs3st3b1</td>
      <td>Dtx4</td>
      <td>Il17rd</td>
    </tr>
    <tr>
      <td>Nuak1</td>
      <td>Clmp</td>
      <td>Adgrl3</td>
      <td>Ncald</td>
      <td>Mmp16</td>
    </tr>
    <tr>
      <td>Tgfb2</td>
      <td>Alpk2</td>
      <td>Svil</td>
      <td>Zic4</td>
      <td>Hhip</td>
    </tr>
    <tr>
      <td>Sfrp1</td>
      <td>Kctd1</td>
      <td>Mob3b</td>
      <td>Dlc1</td>
      <td>Tpx2</td>
    </tr>
    <tr>
      <td>Sncaip</td>
      <td>Meg3</td>
      <td>Trabd2b</td>
      <td>Cdc45</td>
      <td>Ndc80</td>
    </tr>
    <tr>
      <td>Tenm3</td>
      <td>Samd5</td>
      <td>Rmst</td>
      <td>Gatm</td>
      <td>Bub1b</td>
    </tr>
    <tr>
      <td>Cdh2</td>
      <td>Nrk</td>
      <td>Prrx1</td>
      <td>Ssc5d</td>
      <td>Hmmr</td>
    </tr>
    <tr>
      <td>Iqgap2</td>
      <td>Piezo2</td>
      <td>5330434G04Rik</td>
      <td>Phactr2</td>
      <td>Kank4</td>
    </tr>
    <tr>
      <td>App</td>
      <td>Robo1</td>
      <td>Zfhx3</td>
      <td>Ppp1r14c</td>
      <td>Tmeff2</td>
    </tr>
    <tr>
      <td>Pgam2</td>
      <td>Col1a2</td>
      <td>Foxp2</td>
      <td>Agl</td>
      <td>Nr4a1</td>
    </tr>
    <tr>
      <td>Rspo3</td>
      <td>Cntrl</td>
      <td>Mpp6</td>
      <td>Tox3</td>
      <td>Aurkb</td>
    </tr>
    <tr>
      <td>Cdon</td>
      <td>Mllt3</td>
      <td>Crispld1</td>
      <td>Aurka</td>
      <td>Lrrtm3</td>
    </tr>
    <tr>
      <td>Ebf3</td>
      <td>Peg3</td>
      <td>Eya1</td>
      <td>Cdh15</td>
      <td>Cenpq</td>
    </tr>
  </tbody>
</table>

### Myf5-derived lineage contributes to connective tissue cells in the absence of neural crest

Given that the number of cells examined in the EOM and pharyngeal arch mesodermal clusters from the E10.5 dataset was lower than for anterior somites, we decided to validate the relevance of Myf5-derived non-myogenic cells in these cranial regions directly in vivo. We thus examined the EOM, larynx and upper back muscles in the early fetus at E14.5 using a Myf5-lineage reporter mouse (Myf5Cre/+; Rosa26TdTomato/+) combined with a contemporary reporter for Pdgfra (PdgfraH2BGFP/+) (Figure 3). Notably, we observed GFP+ TOM+ double-positive cells in regions of EOM, laryngeal and upper back muscles that are partially or fully deprived of neural crest (Adachi et al., 2020; Comai et al., 2020; Heude et al., 2018; Figure 3A–C'). Conversely, no double-positive cells were detected in muscles that are fully embedded in neural crest derived mesenchyme such as mandibular and tongue muscles (Heude et al., 2018; Figure 3D–E').

![Figure 3.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig3-v3.jpg)

**Figure 3.:** (A-E') Transverse sections of an E14.5 Myf5Cre/+; Rosa26TdTomato/+; PdgfraH2BGFP/+ embryo immunostained for Myod/Myog. White arrowheads indicate cells double-positive GFP/TOM and negative for Myod/Myog (n = 3 embryos). (F-I') Transverse cryosections of the EOM at E13.5 of Wnt1Cre/+; Rosa26mTmG/+; Myf5nlacZ/+ (G,I) and Mesp1Cre/+; Rosa26mTmG/+; Myf5nlacZ/+ (F,H) immunostained for β-gal, at the level of the medial attachment (F,G) and lateral muscle masses (H,I). Yellow arrowheads indicate Myf5-expressing cells in the context of mesodermal and neural crest lineages. Note that Myf5-expressing cells are mGFP+ in the Mesp1 lineage and mGFP- in the Wnt1 lineage. Red arrowheads indicate neural-crest cells that are excluded from the Myf5 lineage (n = 2 embryos for each). (J) Scatter plots of the proportion of double positive cells in E14.5 Myf5Cre/+; Rosa26TdTomato/+; PdgfraH2BGFP/+ embryos in various regions throughout the EOM (the line is the mean, each dot is a tissue section, each color is a different embryo, n = 3 embryos). (K) Scheme highlighting the quantified regions in (J) and summarising the contribution of each population to periocular connective tissues. TOM: TdTOMATO.

Mesenchymal tissues associated with the EOM arise from mesoderm in its most dorso-medial portion and from neural crest in its ventro-lateral portion (Comai et al., 2020; Kuroda et al., 2021). This dual origin makes it a prime candidate to explore the relative contribution of Myf5-derived cells to the associated connective tissues within a single functional unit. Using Wnt1Cre/+; Rosa26mTmG/+; Myf5nlacZ/+ (NCC tracing with Wnt1) and Mesp1Cre/+;Rosa26mTmG/+;Myf5nlacZ/+ (mesoderm tracing with Mesp1) at E13.5, we found that GFP+ cells that expressed Myf5 (β-gal+) were exclusively present in Mesp1-derived domains and absent from the Wnt1 lineage (Figure 3F–I'). To further evaluate the contribution of Myf5-derived cells to connective tissues in either domain, we re-examined the Myf5Cre/+; Rosa26TdTomato/+; PdgfraH2BGFP/+mouse line and quantified the percentage of GFP+ TOM+ cells in the EOM. As expected, we observed a medio-lateral gradient of Myf5-lineage contribution to EOM-associated connective tissues by E14.5, and this was anticorrelated with the local contribution of neural crest cells to connective tissues (Figure 3J–K). Thus, in agreement with our scRNAseq velocity analysis, these observations suggest that the mesodermal Myf5-lineage contributes to muscle-associated connective tissue in domains that are deprived of neural crest mesenchyme.

### Myf5-derived cells can maintain a molecular crosstalk following bifurcation into myogenic and connective tissue fates

To identify the transition between these two fates, we generated an additional sc-RNAseq dataset based on Myf5-lineage tracing at E11.5 (Myf5Cre/+;Rosa26mTmG/+) and produced RNA velocity streams (Figure 4A, Figure 4—figure supplement 1). We focused on the EOM and anterior somites, which were clearly distinguished as independent clusters based on the expression of Alx4 (Bothe and Dietrich, 2006) and Pax3 (Heude et al., 2018), respectively (Figure 4B). In agreement with the E10.5 mesodermal (Mesp1) sc-RNAseq dataset, these progenitors presented a strong dichotomy in Pdgfa and Pdfgra expression between myogenic and non-myogenic cells, respectively (Figure 4—figure supplement 1D). Moreover, RNA velocity suggested more myogenic to non-myogenic conversion (Figure 4A, Figure 4—figure supplement 1E-H). To explore further the cell fate transition in these regions, we used a recently described approach by creating a ‘Coexpression score’ based on myogenic and non-myogenic signatures (Kameneva et al., 2021) (see Materials and methods, Figure 4C). This analysis revealed that individual cells undergo a progressive switch from myogenic to non-myogenic gene expression along the inferred trajectories, where cells at the transition zone shut off the myogenic program and start activating fibrogenic genes (Figure 4C heatmap).

![Figure 4.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig4-v3.jpg)

**Figure 4.:** (A–D) scRNAseq analysis of the Myf5Cre/+; Rosa26mTmG/+ E11.5 dataset (2 datasets of 2 embryos were aggregated to generate this data, see Materials and methods). (A) UMAPs of Myf5Cre/+; Rosa26mTmG/+ E11.5 RNA velocity trajectories. (B) Expression plots of Alx4 and Pax3, highlighting EOM and Anterior somite clusters, respectively. (C) Plots of Myogenic and Non-myogenic signatures, Coexpression score and heatmaps of top markers, highlighting the transition population in EOM and anterior somites. Cells are ordered based on their non-myogenic signature score (increasing). The coexpression score is the product of the myogenic and non-myogenic signatures. Cells presenting a coexpression score higher than 0.20 are highlighted in yellow. These cells represent the transition between the myogenic and non-myogenic fates. (D) UMAP of the EOM subset revealing the bipartite fate of Myf5-expressing cells. (E-G’) RNAscope on Myf5Cre/+; Rosa26mTmG/+ E14.5 tissue sections with Pdgfra (cyan) and Pdgfa (red) probes (E-E’’), Bmprb1 (red) and Bmp4 (cyan) probes (F-F’) and Ephb1 (red) and Efnb1 (cyan) probes (G-G’). Myf5-derived cells are labelled by membrane GFP staining (n = 3 embryos each). Red and yellow arrowheads indicate Myf5-derived myogenic and non-myogenic cells respectively. The dotted lines highlight the boundary of the muscle masses. (H) Quantification of the Ligand-Receptor scores for each pair (see Materials and methods). Note that these ratios are negative in the case of Bmp and Eph (signaling from non-myogenic to myogenic) but positive for Pdgf (signaling from myogenic to non-myogenic). (G) Model of myogenic and non-myogenic cell communication following bifurcation from a bipotent cell.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** (A) Gating strategy used to isolate by FACS Myf5Cre/+; Rosa26mTmG/+ cells. The Alexa Fluor 488 channel was used to identify GFP+ cells. The Alexa Fluor 405 channel was used to identify the Calcein Blue+ live cells. The PE-Texas Red channel was used to discard mTomato+ cells (non recombined) and Propidium Iodide+ cells. The percentage of cells captured by each gate is displayed on each plot. (B) Violin plots of gene count, UMI count and mitochondrial fraction for overall dataset. (C) Violin plots of gene count and UMI count by cluster. (D) Expression patterns of Myf5, Myod, Myog, Pdgfa, Pdgfra, and Col1a1 in the Myf5Cre/+; Rosa26mTmG/+ E11.5 dataset. Note that Myf5+ cells were overwhelmingly Pdgfra- and Myf5+/Pdgfra+ cells represent 5.5% of all cells (i.e. expressing at least one transcript of both genes). Pdgfra+ cells represent 56% of all cells. (E) UMAP of Myf5Cre/+; Rosa26mTmG/+ E11.5 with overlaid velocity and cell cycle phase. (F–H) Quality control metrics of scvelo, including velocity length, velocity confidence and spliced/unspliced abundance in overall dataset and by cluster (n = 2 pooled datasets).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** (A) GO Molecular Function network of top 100 driver genes of the Myf5Cre/+; Rosa26mTmG/+ E11.5 EOM dataset (see Table 1), including relative contribution of each cluster (myogenic and non-myogenic) to the term and significance levels. Insert show the significance of each term. (B) UMAPs of the Myf5Cre/+; Rosa26mTmG/+ E11.5 EOM dataset showing the expression of kinase ligands (left side) and the velocity of their corresponding receptors (right side). Note the complementary patterns of the L/R pairs (n = 2 pooled datasets).

To investigate in more detail potential paracrine cell-cell communication between myogenic and non-myogenic cells, we examined their expression patterns within the EOM, given its well-defined morphology (Comai et al., 2020), and its strong myogenic/non-myogenic bi-directional cell-fate (Figure 4D). We performed single molecule fluorescent in situ hybridization (RNAscope) for Pdgfa and Pdgfra on E14.5 lineage-traced Myf5Cre/+;Rosa26mTmG/+ fetuses (Figure 4E). In accordance with the scRNAseq analysis, we observed cells exhibiting a mostly non-overlapping, complementary pattern of Pdgfa and Pdgfra transcripts within the Myf5-derived lineage, while retaining anatomical proximity, even at later stages of EOM development.

Gene set enrichment analysis of EOM myogenic and non-myogenic driver genes showed that transmembrane receptor protein kinase and SMAD activity were shared terms between the two clusters, suggesting that specific complementary signaling networks could be actively maintained between these two populations (Figure 4—figure supplement 2A). Both signaling pathways were reported to act as inhibitors of myogenic differentiation and could therefore be associated with progenitor cell maintenance (Arnold et al., 2020; Cossu et al., 2000). Notably, Bmpr1b and Ephb1 were among the top 100 driver genes of the myogenic EOM compartment, suggesting that myogenic commitment is associated with upregulation of these kinase receptors in the EOM (Figure 4—figure supplement 2B, Table 1). Strikingly, two of their respective ligands, Bmp4 and Efnb1, were preferentially expressed in non-myogenic cells. Analysis of their expression patterns in E14.5 embryos by RNAscope validated these complementary expression patterns in adjacent muscle and connective tissue domains (Figure 4F–H). These results favor a model where paracrine signaling networks operate between myogenic and non-myogenic Myf5-derived cells (Figure 4I), while their cellular juxtaposition is maintained through fetal stages.

### Obstructing myogenesis expands connective tissue formation from bipotent cells

The directional trajectories identified by RNA velocity in the EOM at E11.5 showed a strong bidirectionality in fate with a higher velocity confidence index at each end of the myogenic and non-myogenic domains, and lower at their interface (Figure 5—figure supplement 1A). This suggested that cells at the interface are bipotential while cells located on either side of this central region are committed either to a myogenic-or non-myogenic fate. To identify the regulatory factors underlying this potential bipotency, we used SCENIC, a regulatory network inference algorithm (Aibar et al., 2017). This tool allows regrouping of sets of correlated genes into regulons (each regulon consists of a transcription factor and its targets) based on binding motifs and co-expression. The top regulons of this analysis revealed active transcription factors underlying myogenic and non-myogenic cell fates in the EOM at E11.5. Notably, Myf5, Pitx1, Mef2a, and Six1, transcription factors known to be implicated in myogenic development (Buckingham and Rigby, 2014), appeared among the top regulons in myogenic cells whereas Fli1, Ebf1, Ets1, Foxc1, Meis1, and Six2, genes known for their involvement in adipogenic, vascular, mesenchymal and tendon development (Jimenez et al., 2007; López-Delgado et al., 2020; Noizet et al., 2016; Truong and Ben-David, 2000; Whitesell et al., 2019; Yamamoto-Shiraishi and Kuroiwa, 2013), constituted some of the highly active non-myogenic transcription factors (Figure 5A). Interestingly, recent work uncovered Fli1 as a potential regulator of vascular fate in multipotent myogenic progenitors (Ferdous et al., 2021). Accordingly, we found that Scube1, a gene known for its involvement in vasculature development, was upregulated in the Pdgfra+ non-myogenic fraction of the EOM (Figure 5—figure supplement 1B). RNAscope in situ hybridization confirmed these findings and showed that Scube1 was expressed at the level of the EOM medial attachment at E14.5 (Figure 5—figure supplement 1C-E). In addition, Scube1 was reported to promote BMP signaling (Liao et al., 2016). Thus, the EOM tendon attachment seems to rely on transcription factors and markers that are typically vascular, hence suggesting that some of them are coopted.

![Figure 5.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig5-v3.jpg)

**Figure 5.:** (A) Heatmap of top regulons (transcription factor and associated targets) of the EOM subset of the Myf5Cre/+; Rosa26mTmG/+ E11.5 dataset. The suffix ‘_extended’ indicates that the regulon includes motifs that have been linked to the TF by lower confidence annotations, for instance, inferred by motif similarity. Number in brackets indicates number of genes comprising the regulon (n = 2 pooled datasets). (B–C) Transverse sections of Myf5nlacZ/+ (B), and Myf5nlacZ/nlacZ (C) embryos in the EOM region at E12.5 immunostained for β-gal (green), and Myod/Myog/Pax7 (red). Red arrowheads indicate β-gal/ Myod/Myog/Pax7 double positive cells in control EOM/Masseter and in mutant Masseter. Asterisk highlights the lack of myogenic progenitors in the EOM region of the mutant embryo, indicated by the absence of Myod/Myog/Pax7 staining. (D-E’) Transverse sections of Myf5nlacZ/+ (D-D'), and Myf5nlacZ/nlacZ (E-E') in the EOM region at E12.5 immunostained for β-gal (green), Sox9 (red), and Myod/Myog/Pax7 (gray). Yellow arrowheads indicate β-gal/Sox9 double positive cells and show an expansion of this cell population in the mutant. (F) Quantification of proportion of β-gal+;Sox9+ double positive cells in the total Sox9+ population of the EOM and Masseter muscles. Each dot is a different sample, the center line of the boxplot is the median value. (n = 3 embryos, p-values were calculated using a two-sided Mann-Whitney U test). (G-I’) Transverse sections of MyodiCre/+; Rosa26TdTomato/+; PdgfraH2BGFP/+ embryos at E14.5 immunostained for Myod/Myog (committed and differentiating myoblasts) in the extraocular (G-G’’), mandibular (H-H’), and back muscles (I-I’). White arrowhead indicates double positive cells (GFP+ TOM+). (J) Quantification of double positive cells (GFP+ TOM+) in EOM, mandibular muscles and back muscles per 100 μm2 area on MyodiCre/+; Rosa26TdTomato/+; PdgfraH2BGFP/+ sections shown in E-G (n = 4 embryos). (K) Model of lineage progression from bipotent cells in a Myf5 null background.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** (A) UMAP of Myf5Cre/+; Rosa26mTmG/+ E11.5 EOM dataset illustrating velocity confidence and velocity length. Higher confidence is found on both ends of the EOM cluster. (B) Expression pattern of Scube1 in the EOM subset (mostly in the non-myogenic compartment). (C-C’’) Combined RNAscope for Scube1 and Myod/Myog/GFP immunostaining on transverse sections of Myf5Cre/+; Rosa26mTmG/+ at E14.5. (D) Model of the EOM muscle vs EOM origin compartmentalization used for quantification in (E). (E) Quantification of Scube1 signal in each compartment (n = 2 embryos).

Given that Myf5 appeared itself as a top myogenic regulon (Figure 5A), we interrogated the fate of Myf5-expressing progenitors in a Myf5nlacZ/nlacZ null embryos at E12.5 (Figure 5B–E’). As previously reported, the EOMs are absent in this mutant (Figure 5C, asterisk) (Sambasivan et al., 2009). Interestingly, some β-gal+ cells were found in the cartilage primordium (Sox9+) of the EOM in the heterozygous control indicating that cells with recent Myf5 activity diverged to this non-myogenic fate (Figure 5D–D'). Notably, disruption of Myf5 activity led to a threefold increase in the proportion of non-myogenic Myf5-derived cells in this region (Figure 5E–F). In contrast, no double-positive cells were found in the masseter, a muscle fully embedded in neural crest-derived connective tissue, even in the absence of Myf5 (Figure 5F). Myf5 expression is thus necessary to maintain a balance between myogenic and non-myogenic cell fates of Myf5+ progenitors only in neural crest-depleted regions. In contrast, very few Pdgfra+ cells were found to be derived from Myod expressing cells in MyodiCre;Rosa26TdTomato/+;PdgfraH2BGFP/+ fetuses at E14.5, particularly in the EOM and the back muscles (about 3 and 1.5 cells per 100 μm2 of muscle, respectively)(Figure 5G, I, J). Accordingly, the masseter lacked Myod-derived connective tissue cells (Figure 5H and J). These observations indicate that progenitors that bifurcate to myogenic and non-myogenic cell fates are present only in neural-crest depleted regions. This property is associated primarily with Myf5 expression, as subsequent activation of Myod within this lineage appears to lock cell fate into the myogenic program and suppress their connective tissue potential (Figure 5K).

### Myf5-derived connective tissues are observed in fetal stages

Although we identified Myf5-derived non-myogenic cells in various regions of the embryo, it was not clear if this population was continuously generated throughout development. To address this issue, we performed two more scRNAseq experiments at E12.5 and E14.5, using contemporary Myf5 labeling, which led to much fewer non-myogenic cells that could be captured (Myf5GFP-P/+; Figure 6, Figure 6—figure supplement 1, Figure 6—figure supplement 2). In accordance with the earlier datasets, some cells that appeared to belong to muscle anlagen of EOM, somites and caudal arches progressed toward a non-myogenic state (Figure 6A–C’). To assess the identity of these cells, we performed a gene set enrichment network analysis combining the differentially expressed genes of non-myogenic clusters of all stages. We found that all stages contributed relatively equally to each ‘GO Molecular Function’ and ‘Reactome pathways’ terms despite their relatively diverse gene expression signatures (Figure 6D–E’, Figure 6—figure supplement 3). This suggests that these non-myogenic cells are relatively homogeneous in gene signatures throughout cranial muscles. Highly significant terms hinted at a myogenic-supporting role, providing muscle progenitors with extracellular matrix components, and contributing to neuronal guidance (Figure 6E). Among these terms, presence of Pdgf signalling and receptor kinase activity indicated, once again, that the interactions found in the EOM could occur also at later stages in various craniofacial muscles that are deprived of neural crest derived connective tissue.

![Figure 6.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig6-v3.jpg)

**Figure 6.:** (A-C') RNA velocity plots of Myf5Cre/+; Rosa26mTmG/+ E11.5, Myf5GFP-P/+ E12.5 and Myf5GFP-P/+ E14.5 datasets (n = 2 pooled datasets, n = 1 embryo and n = 1 embryo, respectively) displaying cell-type annotation (A–C) and myogenic and non-myogenic clustering (A’-C’). The dotted boxes highlight the transitions to non-myogenic clusters in each dataset. (D–E) Gene ontology network of GO Molecular Function and Reactome pathway performed on combined top 100 markers using Cluego. These terms were generated using the sum of all differentially expressed genes of the non-myogenic clusters across all datasets (see Materials and methods). (D’-E’) Relative contribution of each stage to term node represented as piecharts (i.e. the proportion of genes underlying this term coming from that stage). Dotted boxes highlight the shared tyrosine kinase and PDGF signaling pathways.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig6-figsupp1-v3.jpg)

**Figure 6—figure supplement 1.:** (A) Gating strategy used to isolate by FACS Myf5GFP-P/+ cells. The FITC channel was used to identify GFP+ cells. The BV421 was used to identify the Calcein Blue+ live cells. The PE-Texas Red channel was used to discard Propidium Iodide+ cells. The percentage of cells captured by each gate is displayed on each plot. (B) Violin plots of gene count, UMI count and mitochondrial fraction for overall dataset. (C) Violin plots of gene count and UMI count by cluster. (D) Expression patterns of Myf5, Myod, Myog, Pdgfa, Pdgfra, and Col1a1 in the Myf5GFP-P/+ E12.5 dataset. Note that Myf5+ cells were overwhelmingly Pdgfra- and Myf5+/Pdgfra+ cells represent 0.5% of all cells (i.e. expressing at least one transcript of both genes). Pdgfra+ cells represent 3% of all cells. (E) UMAP of Myf5GFP-P/+ E12.5 with overlaid velocity and cell cycle phase. (F–H) Quality control metrics of scvelo, including velocity length, velocity confidence and spliced/unspliced abundance in overall dataset and by cluster (n = 1 embryo).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig6-figsupp2-v3.jpg)

**Figure 6—figure supplement 2.:** (A) Violin plots of gene count, UMI count and mitochondrial fraction for overall dataset. (B) Violin plots of gene count and UMI count by cluster. (C) Expression patterns of Myf5, Myod, Myog, Pdgfa, Pdgfra, and Col1a1 in the Myf5GFP-P/+ E14.5 dataset. Note that Myf5+ cells were overwhelmingly Pdgfra- and Myf5+/Pdgfra+ cells represent 0.15% of all cells (i.e. expressing at least one transcript of both genes). Pdgfra+ cells represent 7% of all cells (n = 1 embryo). (D) UMAP of Myf5GFP-P/+ E14.5 with overlaid velocity and cell cycle phase (n = 1 embryo). (E–G) Quality control metrics of scvelo, including velocity length, velocity confidence and spliced/unspliced abundance in overall dataset and by cluster (n = 1 embryo).

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig6-figsupp3-v3.jpg)

**Figure 6—figure supplement 3.:** Gene ontology analysis for Reactome pathways, including genes underlying each term, and their representation in each dataset generated using Cluego based on top 100 differentially expressed genes of the non-myogenic clusters (see Materials and methods, E10.5: n = 2 pooled datasets, E11.5: n = 2 pooled datasets, E12.5: n = 1 embryo and E14.5: n = 1 embryo).

### A novel regulatory network underlies the non-myogenic cell fate

Myf5+ bipotent progenitors were observed at multiple stages and anatomical locations, and they yielded a relatively homogeneous population expressing common markers associated with extracellular matrix components, cell adhesion molecules, and kinase signalling. To assess whether the regulatory mechanisms guiding this transition are distinct in different locations in the head, we set out to explore the common molecular switches underlying cell fate decisions. To do so, we developed a pipeline where we combined the list of driver genes at the start of the non-myogenic trajectory (Table 1) with the most active regulons in the non-myogenic region (Materials and methods, code in open access). This resulted in a network consisting of the most active transcription factors and the most transcriptionally dynamic genes found at the non-myogenic branchpoint. We performed this operation for each dataset independently and displayed them as individual networks (Figure 7—figure supplement 1A-D). Finally, we overlapped the list of these ‘driver regulators’ to identify the common transcription factors guiding the non-myogenic cell fate decision (Figure 7A). Notably, Foxp2, Hmga2, Meis1, Meox2, and Tcf7l2 were identified in all four scRNAseq datasets as key driver regulators, and thus are likely to play significant role in the non-myogenic transition (Figure 7A, Table 2).

![Figure 7.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig7-v3.jpg)

**Figure 7.:** (A) Barplot displaying frequency of appearance of most predominant transcription factors as driver regulators (4 = present in all four datasets as driver regulon, 1 = present in a single dataset). (B-D’’) Transverse sections of an E12.5 Myf5Cre/+; Rosa26TdTomato/+; PdgfraH2BGFP/+ embryo immunostained for Foxp2 at the level of the EOM (B-B’’), Mandibular muscles (C-C’’), and Back muscles (D-D’’). Yellow arrowheads indicated the double positive cells to better appreciate Foxp2 intensity in Myf5-derived cells. (E) Quantification of Foxp2 signal intensity in TOM+ (Myf5-derived) cells in each muscle (n = 3 embryos). Statistical test performed: Mann-Whitney U test. (F) FACS plots of dissected E12.5 Myf5Cre/+; Rosa26TdTomato/+; PdgfraH2BGFP/+ embryos (head region here) highlighting the Myf5-derived GFP- TOM+ population transitioning to the GFP+ TOM+ population. Each plot was generated on the population gated in the previous one (‘Singlets’, ‘TOM+’ and ‘NonFaps’). FAPS:Fibroadipogenic progenitors, a denomination for resident Pdgfra+ cells. (G) Quantification of the transitioning population in Head, Limb and Trunk. Proportion of transitioning cells is calculated as the number of Alexa488+/Total cell number in the ‘NonFAPs’ gate. Note that the Head region is mostly populated by muscles embedded in neural crest (n = 5 embryos). TOM: TdTOMATO.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig7-figsupp1-v3.jpg)

**Figure 7—figure supplement 1.:** (A–D) Driver genes and regulatory networks (regulons) were produced for each stage independently, and a stage-specific network of active transcription factor and associated driver gene targets was built (n = 2 pooled datasets, n = 2 pooled datasets, n = 1 embryo and n = 1 embry, respectively). The size of nodes corresponds to the number of edges (connections) they have, i.e. the number of driver genes the transcription factor regulates. (E–H) Dotplot of the expression levels and percent of Axin2 and Dkk2 in the myogenic and the non-myogenic portions of all four datasets.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/70235/elife-70235-fig7-figsupp2-v3.jpg)

**Figure 7—figure supplement 2.:** Model for bipotent Myf5+/Pdgfa+ progenitors giving rise to myogenic and non-myogenic cells; discrete parts of the head deprived of neural crest are indicated. Upon activation of a set of transcription factors including Prrx1/2, Foxp2, Hmga2, Meis1, Meox2, Fli1, Twist1, Ets1, Tcf7l2, and Tcf4, a fibrogenic fate is acquired. A molecular dialogue is initiated at the branchpoint including extracellular matrix components and kinase signalling such as Pdgf, Ephrins, and Bmps. The non-myogenic fate may be maintained cell-autonomously by a canonical Wnt-positive feedback loop.

**Table 2.**
 Driver regulators of non-myogenic fate in each dataset.


<table>
  <thead>
    <tr>
      <th></th>
      <th>E10.5</th>
      <th>E11.5</th>
      <th>E12.5</th>
      <th>E14.5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Foxp2</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Hmga2</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Meis1</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Meox2</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Tcf7l2</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Fli1</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Lef1</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Prrx1</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Prrx2</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Six2</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Creb3l1</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Ebf1</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Ets1</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Foxp4</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Hoxb3</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Klf6</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Nfatc4</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Nfib</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Pax7</td>
      <td>(-)</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Pbx1</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Rreb1</td>
      <td>(-)</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Tbx15</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Tcf4</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Twist1</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Zic4</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Zmiz1</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(+)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Ar</td>
      <td>(-)</td>
      <td>(-)</td>
      <td>(-)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Arid5b</td>
      <td>(-)</td>
      <td>(-)</td>
      <td>(+)</td>
      <td>(-)</td>
    </tr>
    <tr>
      <td>Atf3</td>
      <td>(-)</td>
      <td>(-)</td>
      <td>(-)</td>
      <td>(+)</td>
    </tr>
    <tr>
      <td>Chd2</td>
      <td>(+)</td>
      <td>(-)</td>
      <td>(-)</td>
      <td>(-)</td>
    </tr>
  </tbody>
</table>

_(+): Present, (-): Absent._

Forkhead box transcription factors FOXC1 and FOXC2 were reported to regulate the balance between myogenic and vascular lineages within somites (Lagha et al., 2009; Mayeuf-Louchart et al., 2016). Interestingly, Foxc1 has been reported to promote both cranial vasculature and cranial cartilage development in zebrafish (Whitesell et al., 2019; Xu et al., 2021). FOXP2 immunostaining on Myf5Cre/+;Rosa26TdTom/+;PdgfraH2BGFP/+ E12.5 embryos showed that the Myf5-derived EOM cells expressed a relatively high level of Foxp2 compared to mandible and trunk muscles, consistent with their apparent high contribution to connective tissue (Figure 7B–E).

To gain further insights into the transitioning population, we performed FACS analysis of dissected head, limb and trunk regions of Myf5Cre/+;Rosa26TdTom/+;PdgfraH2BGFP/+ embryos at E12.5 (Figure 7F–G). We focused on TOM+ cells (Myf5-lineage) and assessed their GFP expression levels as a readout of their commitment toward connective tissue. This analysis identified non-FAPs cells (GFPlow) transitioning towards a Pdgfra+ state in head and trunk regions but very few in the limb (Figure 7G). Interestingly, while trunk muscles presented the largest portion of transitioning cells (40%), a similar transitioning population was noted in the head (20%) despite a large contribution of NCC to head connective tissues. Thus, cardiopharyngeal mesoderm may have a superior potential to give rise to connective tissue compared to somite-derived progenitors in the limb (1.5%).

In addition, Tcfs and Lef1 were among the top common regulators identified, and they form a complex effector for the canonical Wnt pathway. Previous work showed that during cranial myogenesis, neural crest cells release inhibitors of the Wnt pathway to promote myogenesis (Tzahor et al., 2003). It is thus tempting to speculate that in the absence of neural crest, mesoderm-derived progenitors can give rise to connective tissue by maintaining canonical Wnt activity. To test this hypothesis, we examined the expression of Axin2, a common readout for Wnt/β-cat activity (Babb et al., 2017; van de Moosdijk et al., 2020). Interestingly, Axin2 levels were elevated in the non-myogenic portion of all the different datasets (Figure 7—figure supplement 1E-H). Additionally, Dkk2, which has been described as an activator of Wnt/β-cat pathway in the neural crest (Devotta et al., 2018), was also found to be elevated, indicative of a putative positive-feedback loop mechanism supporting the maintenance of this population.

## Discussion

Distinct fates can emerge through the specification of individual cell types, or through direct lineage ancestry from bipotent or multipotent cells. Here, we addressed this issue in the context of the emergence of myogenic and associated connective tissue cells during the formation of craniofacial muscles. By combining state-the-art computational methods and in-situ analyses, we identified the transcriptional dynamics, the intercellular communication networks, and the regulators controlling the balance between complementary cell fates. Specifically, our work provides evidence for a novel mesoderm-derived bipotent cell population that gives rise to muscle and associated connective tissue cells spatiotemporally, and only in regions deprived of neural crest cells (Figure 7—figure supplement 2).

Brown adipocytes, neurons, pericytes, and rib cartilage have been reported to express Myf5 in ancestral cells (Daubas et al., 2000; Haldar et al., 2008; Sebo et al., 2018; Stuelsatz et al., 2014). Interestingly, when Myf5 expression is disrupted, cells can acquire non-myogenic fates and contribute to connective tissue (this study), cartilage, and dermis (Tajbakhsh et al., 1996), while others remain apparently undifferentiated (cells labeled with an asterisk in Figure 5C). It is likely that these cells are undergoing apoptosis as reported previously (Sambasivan et al., 2009). These studies suggest that Myf5-expression alone is not sufficient to promote robust myogenic fate in multiple regions of developing embryos. Consistent with these observations, Myod+ cells do not contribute to rib cartilage (Wood et al., 2020) and give rise to few connective tissue cells in the periocular and back regions (this study). These findings are also consistent with the role of Myod in defining the committed myogenic cell state and its higher chromatin-remodelling capacity compared to Myf5 (Conerly et al., 2016; Tapscott, 2005). In contrast to a previous study (Stuelsatz et al., 2014), we found no neural-crest derived cells expressing Myf5 during EOM tissue genesis at E13.5 (using Wnt1Cre/+;Rosa26mTmG/+;Myf5nlacZ/+). We note that Myf5-expressing cells contribute to non-myogenic cells from early embryonic stages (E10.5) and continue to do so in the fetus, indicating that these bipotent cells persist well after muscles are established.

Here, we also identifed a core set of transcription factors specifically active in the non-myogenic cells across all datasets. We propose that these genes guide bipotent cells to a non-myogenic fate and thus confer mesenchymal properties to non-committed progenitors. Recent studies have identified anatomically distinct fibroblastic populations using single-cell transcriptomics, yet unique markers could not be identified (Muhl et al., 2020; Sacchetti et al., 2016), making characterisation of cell subtypes challenging. Tcf4/Tcf7l2 was identified as a master regulator of fibroblastic fate during muscle-associated connective tissue development, although it is also expressed in myogenic progenitors at lower levels (Kardon et al., 2003; Mathew et al., 2011; Sefton and Kardon, 2019). We also report that this gene is one of the main regulators of connective tissue fate. Other transcription factors have been linked to skin fibroblast fates including Tcf4, Six2, Meox2, Egr2, and Foxs1, and their repression favors a myofibroblastic potential (Noizet et al., 2016). Six2 and Meox2 were also identified in our analysis, which raises the question of the shared genetic programs between myofibroblastic cells and fibroblastic cells derived from progenitors primed for myogenesis during development.

Interestingly, Prrx1, a marker for lateral plate mesoderm (Durland et al., 2008), was differentially expressed in the connective tissue population at various stages. Although lateral plate mesoderm is identifiable in the trunk, its anterior boundaries in the head are unclear (Prummel et al., 2020). More detailed analyses of Prrx1, Isl1, and Myf5 lineages need to be carried out to delineate the specific boundaries of each progenitor contribution to cranial connective tissues.

Kinase receptors have been implicated in a number of developmental programs for both muscle and associated connective tissues (Arnold et al., 2020; Knight and Kothary, 2011; Olson and Soriano, 2009; Tallquist et al., 2000; Tzahor et al., 2003; Vinagre et al., 2010). For example, the differentiation of fetal myoblasts is inhibited by growth factors Tgfβ and Bmp4 (Cossu et al., 2000). Epha7 signaling is active in embryonic and adult myocytes and promotes their differentiation (Arnold et al., 2020). Significantly, we noticed a striking and lasting complementary expression of Pdgfa and Pdgfra throughout embryonic stages, in the myogenic and non-myogenic progenitors respectively. Pdgf ligands emanating from hypaxial myogenic cells under the control of Myf5 were shown to be necessary from rib cartilage development (Tallquist et al., 2000; Vinagre et al., 2010). Additionally, Pdgfra promotes expansion of fibroblasts during fibrosis (Olson and Soriano, 2009). Interestingly, we found that Pdgfa expression was reduced in cells expressing high levels of Myog at the fetal stage (Figure 6—figure supplement 2C). Therefore, Myf5-derived myogenic progenitor cells might guide non-myogenic Myf5-derived expansion, which in turn provides ligands and extracellular matrix components to favor myogenic development and patterning. Moreover, unlike trunk myogenesis, cranial muscle development relies on the expression of Wnt and Bmp inhibitors from surrounding tissues (Tzahor et al., 2003). Interestingly, we showed that the Myf5-derived non-myogenic cells express Bmp4, Dkk2, and Axin2. Additionally, we showed that the Wnt effector complex Tcf/Lef is expressed to a lower extent in these cells. It is thus likely that these cells maintain their non-myogenic fate by promoting Bmp production and Wnt activity cell-autonomously.

Of note, another study suggested shared fate relationships between fibroblast connective tissue cells and skeletal muscle where fibroblastic cells commit to myogenic fate during limb development (Esteves de Lima et al., 2021). Regarding the possibility that some non-myogenic cells may retain bipotent characteristics, our data suggests that the opposite is true during cranial muscle development. First, RNA velocity analysis did not reveal transitioning cells from non-myogenic clusters to myogenic (even at early stages), nor do they express myogenic markers. Further, at least some of these non-myogenic cells gave rise to chondrocytes, which to our knowledge has never been shown to give rise to skeletal muscle. Additionally, bipotency appears to be more associated with myogenic cells since they express Myf5, and to a minor extent Myod. Finally, we did not observe NCC-derived Myf5+ cells indicating that connective tissue in the head does not give rise to muscle. Nevertheless, to formally exclude the possibility of connective tissue progenitors giving rise to muscle in the embryo, analysis of appropriate markers would need to be done (ex. Pdgfra-driven lineage). Further studies should provide insights into the evolutionary ancestry of progenitors that bifurcate to give rise to myogenic and connective tissue cells by studying other model organisms that are devoid of neural crest cells.

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
      <td>Strain, strain background (Mus musculus)</td>
      <td>B6D2F1/JRj</td>
      <td>Janvier</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>Myf5Cre</td>
      <td>PMID:17418413</td>
      <td>MGI:3710099</td>
      <td>Dr. Mario R Capecchi (Institute of Human Genetics, University of Utah, USA)</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>Wnt1Cre</td>
      <td>PMID:9843687</td>
      <td>MGI:J:69326</td>
      <td>Pr. Andrew P. McMahon (Keck School of Medicine of the University of Southern California, USA)</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>Mesp1Cre</td>
      <td>PMID:10393122</td>
      <td>MGI:2176467</td>
      <td>Pr. Yumiko Saga (National Institute of Genetics, Japan)</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>Myf5nlacZ</td>
      <td>PMID:8918877</td>
      <td>MGI:1857973</td>
      <td>Dr. Shahragim Tajbakhsh (Department of Developmental and Stem Cell Biology, Institut Pasteur, France)</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>Rosa26tdTomato</td>
      <td>PMID:20023653</td>
      <td>MGI:3809524</td>
      <td>Dr. Hongkui Zeng (Allen Institute for Brain Science, USA)</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>Rosa26mT/mG</td>
      <td>PMID:17868096</td>
      <td>MGI:3716464</td>
      <td>Pr. Philippe Soriano (Icahn School of Medicine at Mt. Sinai, USA)</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>PdgfraH2BGFP</td>
      <td>PMID:12748302</td>
      <td>MGI:2663656</td>
      <td>Pr. Philippe Soriano (Icahn School of Medicine at Mt. Sinai, USA)</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>MyodiCre</td>
      <td>PMID:19464281</td>
      <td>MGI:3840216</td>
      <td>Pr. David Goldhamer (University of Connecticut, USA)</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. musculus)</td>
      <td>Myf5GFP-P</td>
      <td>PMID:15386014</td>
      <td>MGI:3055340</td>
      <td>Dr. Shahragim Tajbakhsh (Department of Developmental and Stem Cell Biology, Institut Pasteur, France)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sucrose,for molecular biology, ≥ 99.5% (GC)</td>
      <td>Sigma-Aldrich</td>
      <td>S0389-500G</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Gelatin</td>
      <td>Sigma-Aldrich</td>
      <td>G-7041</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Foxp2 5C11A8 (Mouse monoclonal)</td>
      <td>Santa Cruz</td>
      <td>SC-517261</td>
      <td>IF (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-β-gal (Chicken polyclonal)</td>
      <td>Abcam</td>
      <td>Cat. #: ab9361 RRID:AB_307210</td>
      <td>IF (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-β-gal (Rabbit polyclonal)</td>
      <td>MP Biomedicals</td>
      <td>Cat. #: MP 559761 RRID:AB_2687418</td>
      <td>IF (1:1500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GFP (Chicken polyclonal)</td>
      <td>Aves Labs</td>
      <td>Cat. #: 1020 RRID:AB_10000240</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GFP (Chicken polyclonal)</td>
      <td>Abcam</td>
      <td>Cat. #: 13970 RRID:AB_300798</td>
      <td>IF (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Myod (Mouse monoclonal)</td>
      <td>Dako</td>
      <td>Cat. #: M3512 RRID:AB_2148874</td>
      <td>IF (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Myod (Mouse monoclonal)</td>
      <td>BD-Biosciences</td>
      <td>Cat. #: 554130 RRID:AB_395255</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Pax7 (Mouse monoclonal)</td>
      <td>DSHB</td>
      <td>Cat. #: Pax7 RRID:AB_528428</td>
      <td>IF (1:20)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Myog (Mouse monoclonal)</td>
      <td>DSHB</td>
      <td>Cat. #: F5D RRID:AB_2146602</td>
      <td>IF (1:20)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 633 F(ab')2 Fragment of Goat Anti-Rabbit IgG (H + L) (polyclonal antibody)</td>
      <td>Life Technologies</td>
      <td>Cat. #: A-21072 RRID:AB_2535733</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 555 F(ab')2 Fragment of Goat Anti-Rabbit IgG (H + L) (polyclonal antibody)</td>
      <td>Life Technologies</td>
      <td>Cat. #: A-21430 RRID:AB_2535851</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 488 F(ab')2 Fragment of Goat Anti-Rabbit IgG (H + L) (polyclonal antibody)</td>
      <td>Life Technologies</td>
      <td>Cat. #: A-11070 RRID:AB_2534114</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 633 Goat Anti-Chicken IgG (H + L) (polyclonal antibody)</td>
      <td>Life Technologies</td>
      <td>Cat. #: A-21103 RRID:AB_2535756</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 488 Goat Anti-Chicken IgG (H + L) (polyclonal antibody)</td>
      <td>Life Technologies</td>
      <td>Cat. #: A-11039 RRID:AB_2534096</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 633 Goat Anti-Mouse IgG1 (γ1) (polyclonal antibody)</td>
      <td>Life Technologies</td>
      <td>Cat. #: A-21126 RRID:AB_2535768</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor488 AffiniPure Goat Anti-Mouse IgG1 (γ1) (polyclonal antibody)</td>
      <td>Jackson ImmunoResearch</td>
      <td>Cat. #: 115-545-205 RRID:AB_2338854</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Cy3-AffiniPure Goat Anti-Mouse IgG1 (γ1) (polyclonal antibody)</td>
      <td>Jackson ImmunoResearch</td>
      <td>Cat. #: 115-165-205 RRID:AB_2338694</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Cy3-AffiniPure Goat Anti-Mouse IgG2a (γ2a) (polyclonal antibody)</td>
      <td>Jackson ImmunoResearch</td>
      <td>Cat. #: 115-165-206 RRID:AB_2338695</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Dylight 405 Goat Anti-Mouse IgG2a (γ2a) (polyclonal antibody)</td>
      <td>Jackson ImmunoResearch</td>
      <td>Cat. #: 115-475-206 RRID:AB_2338800</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Hoechst 33,342</td>
      <td>Thermo Scientific</td>
      <td>Cat. #:H3570</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNAscope Multiplex Fluorescent reagent Kit-V2</td>
      <td>ACD/Bio-techne</td>
      <td>Cat. #: 323100</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNAscope H202 &amp; Protease Plus Reagents</td>
      <td>ACD/Bio-techne</td>
      <td>Cat #: 322330</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Opal 650 Reagent Pack</td>
      <td>PerkinElmer</td>
      <td>Cat. #: FP1496001KT</td>
      <td>1:1,500 of reconstituted reagent in RNAscope Multiplex TSA Buffer</td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Opal 570 Reagent Pack</td>
      <td>PerkinElmer</td>
      <td>Cat. #: FP1488001KT</td>
      <td>1:1,500 of reconstituted reagent in RNAscope Multiplex TSA Buffer</td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNAscope Mm-Pdgfa</td>
      <td>Advanced Cell Diagnostics, Inc</td>
      <td>Cat #:411361</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNAscope Mm-Pdgfra</td>
      <td>Advanced Cell Diagnostics, Inc</td>
      <td>Cat #:480661-C2</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNAscope Mm-Bmpr1b</td>
      <td>Advanced Cell Diagnostics, Inc</td>
      <td>Cat #:533941</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNAscope Mm-Efnb1</td>
      <td>Advanced Cell Diagnostics, Inc</td>
      <td>Cat #:526761</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNAscope Mm-Bmp4-O1-C3</td>
      <td>Advanced Cell Diagnostics, Inc</td>
      <td>Cat #:527501-C3</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNAscope Mm-Ephb1-C3</td>
      <td>Advanced Cell Diagnostics, Inc</td>
      <td>Cat #:567571-C3</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNAscope Mm-Scube1</td>
      <td>Advanced Cell Diagnostics, Inc</td>
      <td>Cat #:488131</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Paraformaldehyde</td>
      <td>Electron Microscopy Sciences</td>
      <td>Cat. #: 15710</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Isopentane</td>
      <td>VWR</td>
      <td>Cat. #: 24872.298</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Triton X-100</td>
      <td>Sigma</td>
      <td>Cat. #: T8787</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tween 20</td>
      <td>Sigma</td>
      <td>Cat. #: P1379</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TrypLE</td>
      <td>ThermoFisher</td>
      <td>Cat #: 12604013</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Calcein Blue</td>
      <td>eBioscience</td>
      <td>Cat #: 65-0855-39</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Propidium Iodide</td>
      <td>ThermoFisher</td>
      <td>Cat #: P1304MP</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Chromium Next GEM Chip G Single Cell Kit, 16 rxns</td>
      <td>10 X Genomics</td>
      <td>Cat #: 1000127</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Chromium Next GEM Single Cell 3' GEM, Library &amp; Gel Bead Kit v3.1, 4 rxns</td>
      <td>10 X Genomics</td>
      <td>Cat #:1000128</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>NextSeq 500/550 High Output Kit v2.5</td>
      <td>Illumina</td>
      <td>Cat #: 20024906</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Agilent High Sensitivity DNA Kit</td>
      <td>Agilent</td>
      <td>Cat #:5067–4626</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Agilent High Sensitivity DNA Reagents</td>
      <td>Agilent</td>
      <td>Cat #:5067–4627</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Qubit dsDNA HS Assay Kit</td>
      <td>Life Technologies</td>
      <td>Cat #:Q32854</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RStudio</td>
      <td>Rstudio</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Anaconda</td>
      <td>Anaconda Inc</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Zen</td>
      <td>Zeiss</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cytoscape</td>
      <td>Cytoscape Team</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji</td>
      <td>Johannes Schindelin, Ignacio Arganda-Carreras, Albert Cardona, Mark Longair, Benjamin Schmid, and others</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism</td>
      <td>GraphPad Software</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FlowJo</td>
      <td>FlowJo</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### scRNAseq data generation

For E10.5 to E12.5 embryos, the cranial region above the forelimb was dissected in ice-cold 3% FBS in PBS and mechanically dissociated with forceps and pipetting. The same procedure was applied at E14.5 but the dissection was refined to the pharyngeal and laryngeal regions. Tissues were then digested in TrypLE (ThermoFisher Cat #: 12604013) during 3 rounds of 5 min incubation (37 °C, 1400 RPM), interspersed with gentle pipetting to further dissociate the tissue. Cells were resuspended in FBS 3%, filtered, and incubated with Calcein Blue (eBioscience, Cat #: 65-0855-39) and Propidium Iodide (ThermoFisher Cat #: P1304MP) to check for viability. Viable cells were sorted on BD FACS Aria III and manually counted using a hemocytometer. RNA integrity was assessed with Agilent Bioanalyzer 2,100 to validate the isolation protocol prior to scRNAseq (RIN >8 was considered acceptable). A total of 4000–13,000 cells were loaded onto 10 X Genomics Chromium microfluidic chip and cDNA libraries were generated following manufacturer’s protocol. Concentrations and fragment sizes were measured using Agilent Bioanalyzer and Invitrogen Qubit. cDNA libraries were sequenced using NextSeq 500 and High Output v2.5 (75 cycles) kits. Genome mapping and count matrix generation were done following 10X Genomics Cell Ranger pipeline.

### RNA velocity and driver genes

RNA velocity analyses were performed using scvelo (Bergen et al., 2020) in Python. This tool allows inferring velocity flow and driver genes using scRNAseq data, with major improvements from previous methods (La Manno et al., 2018). First, unspliced and spliced transcript matrices were generated using velocyto (La Manno et al., 2018) command line function, which outputs unspliced, spliced, and ambiguous matrices as a single loom file. These files were combined with filtered Seurat objects to yield objects with unspliced and spliced matrices, as well as Seurat-generated annotations and cell-embeddings (UMAP, tSNE, PCA). These datasets were then processed following scvelo online guide and documentation. Velocity was calculated based on the dynamical model (using scv.tl.recover_dynamics(adata), and scv.tl.velocity(adata, mode=’dynamical’)) and when outliers were detected, differential kinetics based on top driver genes were calculated and added to the model (using scv.tl.velocity(adata, diff_kinetics = True)). Specific driver genes were identified by determining the top likelihood genes in the selected cluster. The lists of top 100 drivers for each stage are given in Table 1.

### Data processing

scRNAseq datasets were preprocessed using Seurat in R (https://satijalab.org/seurat/) (Butler et al., 2018). Cells with more than 20% of mitochondrial gene fraction were discarded. The number of genes expressed averaged to 4000 in all four datasets. Dimension reduction and UMAP generation were performed following Seurat workflow. Doublets were inferred using DoubletFinder v3 (McGinnis et al., 2019). Cell cycle genes, mitochondrial fraction, number of genes, number of UMI were regressed in all datasets following Seurat dedicated vignette. We noticed that cell cycle regression, although clarifying anatomical diversity, seemed to induce low and high UMI clustering (Figure 4A, Figure 4—figure supplement 1C). For the E10.5 and E11.5 datasets, two replicates were generated from littermates and merged after confirming their similitude. For subsequent datasets (E12.5 and E14.5), no replicates were used. Annotation and subsetting were also performed in Seurat. ‘Myogenic’ and ‘Non-myogenic’ annotations were based on Pdgfa and Pdgfra expression and myogenic genes Myf5, Myod, and Myog. Cells not expressing Pdgfa were annotated as ‘non-myogenic’ unless they express myogenic genes. Cells expressing Pdgfa were annotated as ‘myogenic’. We noticed that at later stages, Pdgfa expression decreases in Myog+ cells. Driver genes of connective tissue at E12.5 and E14.5 were determined using cluster annotations obtained from Leiden-based clustering. Myogenic and non-myogenic scores were generated by aggregating the total expression of all genes in a signature based on the top 10 markers of these compartments (visible on Figure 4C). Each score was then divided by the sum of the two to generate myogenic and non-myogenic signatures. The coexpression score was defined by the product of these signatures. To generate the plots, cells were ordered based on their non-myogenic signature. The ‘transition’ was defined as cells with a coexpression score higher than 0.20.

### Gene regulatory network inference

Gene regulatory networks were inferred using SCENIC (R implementation) (Aibar et al., 2017) and pySCENIC (Python implementation) (Van de Sande et al., 2020). This algorithm allows regrouping of sets of correlated genes into regulons (i.e. a transcription factor and its targets) based on motif binding and co-expression. UMAP and heatmap were generated using regulon AUC matrix (Area Under Curve) which refers to the activity level of each regulon in each cell. We used two cisTarget databases: ‘mm9-500bp-upstream-7species.mc9nr’ (500 bp upstream of TSS) and ‘mm9-tss-centered-10kb-7species.mc9nr’ (10kb ±TSS).

### Driver regulons

Results from SCENIC and scvelo were combined to identify regulons that could be responsible for the transcriptomic induction of driver genes. Similarly to the steps mentioned above, SCENIC lists of regulons were used to infer connections between transcription factors and driver gene. Networks were generated as explained above and annotated with ‘Active regulon’ or ‘driver gene’. The lists of individual driver regulons of each dataset were then combined and the most recurring driver regulons were identified. The code is available at this address: https://github.com/TajbakhshLab/DriverRegulators, (copy archived at swh:1:rev:49db57e7ede9f248de937b7a47eb96b02aa2ce67; Grimaldi, 2021).

### Gene set enrichment analysis

Gene set enrichment analyses were performed on either the top markers (obtained from Seurat function FindAllMarkers) or from driver genes (obtained from scvelo), using Cluego (Bindea et al., 2009). ‘GO Molecular Pathway’, ‘GO Biological Process’ and ‘Reactome pathways’ were used independently to identify common and unique pathways involved in each dataset. In all analyses, an enrichment/depletion two-sided hypergeometric test was performed and p-values were corrected using the Bonferroni step down method.

### Mouse strains

Animals were handled as per European Community guidelines and the ethics committee of the Institut Pasteur (CETEA) approved protocols (APAFIS#6354–20160809 l2028839). The following strains were previously described: Myf5Cre (Haldar et al., 2008), MyodiCre (Kanisicak et al., 2009), Mesp1Cre (Saga et al., 1999), Tg:Wnt1Cre (Danielian et al., 1998), Rosa26TdTom (Ai9; Madisen et al., 2010), Rosa26mTmG (Muzumdar et al., 2007), Myf5nlacZ (Tajbakhsh et al., 1996), PdgfraH2BGFP (Hamilton et al., 2003) and Myf5GFP-P (Kassar-Duchossoy et al., 2004). To generate Myf5Cre/+;Rosa26TdTomato/+;PdgfraH2BGFP/+embryos, Myf5Cre/+ females were crossed with PdgfraH2BGFP/+;Rosa26TdTomato/TdTomato males. Mice were kept on a mixed genetic background C57BL/6JRj and DBA/2JRj (B6D2F1, Janvier Labs). Mouse embryos and fetuses were collected between embryonic day (E) E10.5 and E14.5, with noon on the day of the vaginal plug considered as E0.5.

### Immunofluorescence

Collected embryonic and adult tissues were fixed 2.5 h in 4% paraformaldehyde (Electron Microscopy Sciences, Cat #:15710) in PBS with 0.2–0.5% Triton X-100 (according to their stage) at 4 °C and washed overnight at 4 °C in PBS. In preparation for cryosectioning, embryos were equilibrated in 30% sucrose in PBS overnight at 4 °C and embedded in OCT. Cryosections (16–20 µm) were left to dry at RT for 30 min and washed in PBS. For Foxp2 immunostaining (Santa Cruz Cat. #: SC-517261), embryos were first equilibrated in 15% sucrose overnight, then in a 15% sucrose/7.5% gelatin solution at 37 °C the next day and embedded in the same solution the following day. Blocks were then kept at 4 °C in a humid environment and trimmed, before being submerged in liquid nitrogen-cooled isopentane at –60 °C to freeze. After cryosectioning, slides were washed twice for 15 min each at 37 °C inPBS to remove the gelatin. The primary antibodies used in this study are chicken polyclonal anti-β-gal (Abcam, Cat #: ab9361, dilution 1:1000), mouse monoclonal IgG1 anti-Myod (BD Biosciences, Cat# 554130, dilution 1:100), mouse monoclonal IgG1 anti-Pax7 (DSHB, Cat. #: AB_528428, dilution 1:20), rabbit anti-mouse Sox9 (Millipore, Cat. #: AB5535, dilution 1/2000), rabbit polyclonal anti-Tomato (Clontech Cat. #: 632496, dilution 1:400) and chicken polyclonal anti-GFP (Abcam Cat. #: 13970, dilution 1:1000). Images were acquired using Zeiss LSM780 or LSM700 confocal microscopes and processed using ZEN software (Carl Zeiss). Control and mutant embryos were selected randomly, quantifications were performed blindly by hiding the discriminating channels. Quantifications were performed using Fiji (https://imagej.net/software/fiji/). Barplots, dotplots and boxplots were generated using Seaborn (https://seaborn.pydata.org; https://seaborn.pydata.org/) or Prism (https://www.graphpad.com/scientific-software/prism/). For the Myf5Cre/+;Rosa26TdTomato/+;PdgfraH2BGFP/+ embryos, 4 regions were manually defined across the medio-lateral axis. For each region, the absolute number of double-positive cells within the defined area was divided by the total number of GFP+ cells which was determined first, and blindly (with the TOMchannel disabled). For the MyodiCre lineage-tracing experiment, the absolute number of double positive cells were counted and divided by the area of the muscle given by the TOM channel. These ‘number of cells/area’ scores were then corrected based on the size of the image in microns, and adjusted to match an area of 100 μm2 of muscle. To quantify the intensity of Foxp2 immunostaining, we first generated ROIs of the Myf5-derived cells based on the TOM channels as previously mentioned and extracted the mean pixel value. All images were acquired using the exact same settings for a given embryo.

### RNAscope in situ hybridization

Embryos for in situ hybridization were fixed overnight in 4% PFA. Embryos were equilibrated in 30% sucrose in PBS and sectioned as described for immunofluorescence. RNAscope probes Mm-Pdgfa (411361), Mm-Pdgfra (480661-C2), Mm-Bmpr1b (533941), Mm-Efnb1 (526761), Mm-Bmp4-O1-C3 (527501-C3), Mm-Ephb1-C3 (567571-C3) and Mm-Scube1 (488131) were purchased from Advanced Cell Diagnostics, Inc. In situ hybridization was performed using the RNAscope Multiplex Fluorescent Reagent Kit V2 as described previously (Comai et al., 2019). Quantifications were performed using Fiji (https://imagej.net/software/fiji/). 2 ROIs were first defined visually using the GFP channel: ‘myogenic’ and ‘non-myogenic’. The channels containing the RNAscope signals were then thresholded to obtain binary images, and measurement of the ‘Area%’ was performed for each ROI. For each probe, we generated a ratio of myogenic to non-myogenic signal. The ratio of each receptor was then substracted from the ratio of each corresponding ligand.
