# A library of lineage-specific driver lines connects developing neuronal circuits to behavior in the Drosophila ventral nerve cord

## Authors

- Jelly HM Soffers<sup>1</sup> ([ORCID: 0000-0002-1051-7375](https://orcid.org/0000-0002-1051-7375)) †
- Erin Beck<sup>1</sup>
- Daniel J Sytkowski<sup>1</sup>
- Marianne E Maughan<sup>1</sup>
- Devasri Devarakonda<sup>1</sup>
- Yi Zhu<sup>2</sup>
- Beth A Wilson<sup>2</sup>
- Yu-Chieh David Chen<sup>3</sup> ([ORCID: 0000-0002-2597-7577](https://orcid.org/0000-0002-2597-7577))
- Ted Erclik<sup>4</sup>
- James W Truman<sup>6</sup> ([ORCID: 0000-0002-9209-5435](https://orcid.org/0000-0002-9209-5435))
- James B Skeath<sup>2</sup> ([ORCID: 0000-0003-1179-4857](https://orcid.org/0000-0003-1179-4857))
- Haluk Lacin<sup>1</sup> ([ORCID: 0000-0003-2468-9618](https://orcid.org/0000-0003-2468-9618)) †

### Affiliations

1. School of Science and Engineering, Division Biological and Biomedical Systems, University of Missouri-Kansas City Kansas City United States ([ROR:01w0d5g70](https://ror.org/01w0d5g70))
2. Department of Genetics, Washington University School of Medicine St. Louis United States ([ROR:01yc7t268](https://ror.org/01yc7t268))
3. Department of Biology, New York University New York United States ([ROR:0190ak572](https://ror.org/0190ak572))
4. Department of Biology, University of Toronto - Mississauga Mississauga Canada ([ROR:03dbr7087](https://ror.org/03dbr7087))
5. Department of Cell and Systems Biology, University of Toronto - Mississauga Mississauga Canada ([ROR:03dbr7087](https://ror.org/03dbr7087))
6. Department of Biology, University of Washington Seattle United States ([ROR:00cvxb145](https://ror.org/00cvxb145))

† Corresponding author

## Abstract

Understanding developmental changes in neuronal lineages is crucial to elucidate how they assemble into functional neural networks. Studies investigating nervous system development in model systems have only focused on select regions of the CNS due to the limited availability of genetic drivers that target specific neuronal lineages throughout development and adult life. This has hindered our understanding of how distinct neuronal lineages interconnect to form neuronal circuits during development. Here, we present a split-GAL4 library composed of genetic driver lines, which we generated via editing the genomic locus of lineage-specific transcription factors and demonstrate that we can use this library to specifically target most individual neuronal hemilineages in the Drosophila ventral nerve cord (VNC) throughout development and into adulthood. Using these genetic driver lines, we found striking morphological changes in neuronal processes within a lineage during metamorphosis. We also demonstrated how neurochemical features of neuronal classes can be quickly assessed. Lastly, we documented behaviors elicited in response to optogenetic activation of individual neuronal lineages and generated a comprehensive lineage-behavior map of the entire fly VNC. Looking forward, this lineage-specific split-GAL4 driver library will provide the genetic tools needed to address the questions emerging from the analysis of the recent VNC connectome and transcriptome datasets.

## Introduction

Neuronal circuits underlie nervous system functions ranging from perception and movement to cognition and emotion. Most neurons found in the adult CNS of animals are generated and assembled into circuits during development. Investigating the formation of these circuits provides valuable insights into the functional organization and operation of the nervous system, both in health and disease.

Drosophila has served as a powerful model system to investigate how neuronal circuits function due to its medium complexity compared to vertebrate models yet rich repertoire of behaviors and unprecedented genetic toolkit. High-resolution electron microscopy data of the adult fly brain and ventral nerve cord (VNC) reveal individual neuronal morphologies and their synaptic connections (Marin et al., 2024; Azevedo et al., 2024; Li et al., 2020; Scheffer et al., 2020; Schlegel et al., 2023). The integration of these morphological data with single-cell transcriptome profiles has placed the adult fly CNS at the forefront of studies of circuit operations at the molecular level (Allen et al., 2020; Bates et al., 2019; Özel et al., 2021; Yoo et al., 2023).

In Drosophila and other model systems, less attention has been paid to how neuronal circuits develop compared to how they function, limiting our understanding of the developmental processes that instruct newly born neurons to assemble into functional circuits. In Drosophila, the same set of neural stem cells, called neuroblasts (NB), sequentially form the larval and adult CNS, with the adult CNS having 10–20-fold more neurons and greater complexity. Some of the embryonic-born neurons, which function in the larval CNS, are remodeled to integrate into adult circuits (Prokop and Technau, 1991; Truman, 1990; Truman and Bate, 1988). Most of the adult neurons are born post-embryonically during larval and early pupal stages. These neurons fully differentiate and assemble into circuits during metamorphosis into the adult, which lasts several days. This extended window of neurogenesis and neuronal maturation during the formation of the adult VNC facilitates experimental manipulations that are not feasible during the brief period of neurogenesis in the embryo, such as temporal gene silencing studies to discriminate axon guidance and synapse formation.

The fly VNC, like its vertebrate analog, the spinal cord, is functionally compartmentalized into lineally related groups of neurons, called neuronal lineages. In flies, Notch-mediated asymmetric cell division divides the neuronal population of each NB into two subclasses, called hemilineages: ‘A’ hemilineages are composed of Notch ON cells and ‘B’ hemilineages are composed of notch OFF cells (Skeath and Doe, 1998; Spana and Doe, 1996; Truman et al., 2010). The adult fly VNC is composed of ~15,000 neurons, most of which are found in the three thoracic segments. Each thoracic hemisegment contains 34 major post-embryonic hemilineages, with some segment-specific variation in the type of hemilineages and their morphology. Recent studies identified these hemilineages in the VNC Electron Microscopy (EM) volume dataset and showed that neurons within a given hemilineage exhibit a stereotyped pattern of connectivity (Marin et al., 2024; Azevedo et al., 2024; Ehrhardt et al., 2023; Lesser et al., 2024). This revealed that hemilineages display a propensity to form synaptic connections with neurons from other specific hemilineages, uncovering a macro-connectivity among hemilineages. Hemilineage-based compartmentalization of the VNC is also observed at the level of gene expression. (Allen et al., 2020) assessed the transcriptome of the entire adult VNC via single-cell RNA sequencing (scRNAseq) and showed that hemilineage identity correlates highly with unique clusters of cells, which are partitioned solely based on gene expression via dimensionality reduction. Lastly, several studies employing hemilineage-restricted neuronal manipulations showed that the VNC hemilineages represent functional modules that control animal behavior (Agrawal et al., 2020; Harris et al., 2015; Lacin et al., 2020). Indeed, like the cardinal classes of interneurons in the spinal cord (Briscoe et al., 2000; Jessell, 2000; Lu et al., 2015), hemilineages in the Drosophila VNC are functional units, each contributing to aspects that control specific behaviors. Thus, taking a hemilineage-based approach is essential for a systematic and comprehensive understanding of behavioral circuit assembly during development in complex nervous systems.

Addressing the question of how neurons in individual hemilineages develop into functional circuits requires genetic tools to manipulate individual hemilineages throughout development. Existing genetic driver lines (GAL4, Split-GAL4, and LexA libraries) are often limited in their use for developmental studies. The expression of such drivers typically relies on 2–3 kb genomic fragments that contain enhancer elements, Meissner et al., 2024 and comprehensive screening efforts have identified driver lines that mark specific neuronal populations (Meissner et al., 2024 and citations therein). However, the genomic fragments driving GAL4, Split-GAL4, or LexA expression lack the complete endogenous transcriptional control mechanisms. As a result, they are oftentimes only expressed in specific neuronal populations during particular life stages, such as exclusively in the larva or adult. Consequently, they lack the temporal stability required for comprehensive developmental analysis (Meissner et al., 2024; Luan et al., 2020; Pfeiffer et al., 2010), highlighting a critical need for developmentally stable and hemilineage-specific driver lines. These tools will allow us to track and measure individual hemilineages as well as activate or inactivate specific genes and neuronal functions within them, thereby facilitating the identification of fundamental principles underlying circuit development.

Here, we describe a split-GAL4 library that targets unique hemilineages in a developmentally stable manner. Our previous work demonstrated that many of the lineage-specific transcription factors that regulate the specification and differentiation of post-embryonic neurons are stably expressed during development (Lacin et al., 2014; Lacin et al., 2019; Lacin and Truman, 2016; Lacin et al., 2024). We employed gene knock-in strategies to insert split-GAL4 driver coding sequences in frame with the coding regions of these transcription factors, generating lineage-specific, temporally stable driver lines for selected hemilineages (Lacin et al., 2020; Lacin et al., 2014; Lacin et al., 2019). To extend this approach to all hemilineages in the VNC, we required a more comprehensive list of lineage-specific transcription factors. To compile this list, we utilized published scRNA-seq data of the VNC and expanded upon the work of Allen et al., 2020; Lacin et al., 2014; Harris et al., 2015. This work had assigned a part of the scRNAseq cell clusters to hemilineages. We analyzed the gene expression patterns of the remaining clusters for combinations of significantly enriched transcription factors, referred to as cluster markers, and tested the expression patterns of these genes with genetic reporter lines and antibody staining. We were able to assign 33 of the 34 major hemilineages to scRNAseq clusters with this approach. Then, we generated gene-specific split-GAL4 lines for 28 of these hemilineage-specific transcription factors via genome editing and recombination techniques. We performed a thorough analysis of the expression patterns of binary combinations of split-GAL4 AD and split-GAL4 DBD lines using combinations of the 28 transcription factor-specific hemidrivers we present in this study and split-GAL4 lines generated previously (Lacin et al., 2019; Lacin et al., 2024; Chen et al., 2023a). We report 44 combinations that target 32 of the 34 VNC hemilineages; most of these drivers do this specifically and in a developmentally stable manner. Finally, we demonstrate the ability of this library to map neurotransmitter expression to individual hemilineages and to map specific behaviors to defined neuronal lineages.

## Results

### Intersecting the expression of acj6 and unc-4 with the split-GAL4 method faithfully marks hemilineage 23B throughout development and adult life

Many transcription factors in the CNS are expressed in a hemilineage-specific manner, and their expression is generally maintained throughout the lifetime of the neurons that express them (Lacin et al., 2014). We asked whether we could generate specific and temporally stable driver lines by hijacking the expression of such transcription factors. We initially focused on Acj6 and Unc-4, which are transcription factors expressed in numerous neuronal cell clusters in the brain and VNC (Figure 1A–B). Our prior work demonstrated that these proteins are co-expressed exclusively in hemilineage 23B neurons in both the larva and adult (Lacin et al., 2014). We leveraged this unique co-expression pattern to develop a genetic set-up that targets only the 23B neurons in a developmentally stable manner. We combined two techniques: the Trojan-exon-based driver for target gene transcription (Diao et al., 2015) and the split-GAL4 method (Luan et al., 2006). The split-GAL4 method works by reconstituting GAL4 function through the interaction of GAL4’s DNA-binding domain (DBD) and an activation domain (AD) in cells where both transgenes are expressed. Here, we used the unc-4 split-GAL4 AD and DBD lines that we had previously generated (Lacin et al., 2020) and created acj6 split-GAL4 lines by replacing the MIMIC insertion in the acj6 coding intron with a Trojan exon encoding either p65.AD or GAL4-DBD via recombinase-mediated cassette exchange (RMCE).

![Figure 1.](https://cdn.elifesciences.org/articles/106042/elife-106042-fig1-v1.jpg)

**Figure 1.:** (A–C) Projections of confocal stacks of the adult VNC. Blue: CadN; (A) acj6-GAL4 driven nls-tdTomato expression (displayed in green) marks Acj6 expressing neurons. (B) unc-4-GAL4 driven nls-tdTomato expression (displayed in green) marks Unc-4 expressing neurons. (C) The intersection of acj6 and unc-4 expression (displayed in green) (acj6-GAL4AD, unc-4-GAL4DBD> UAS-nls-tdTomato) marks lineage 23B neurons in the SEZ and VNC. (D) A partial confocal projection showing the complete overlap between membranous GFP (green) and Acj6 (magenta) immunostainings in acj6-GAL4AD, unc-4-GAL4DBD-marked 23B neurons in the adult VNC (T1 and T2 segments shown). (E) scRNAseq t-SNE plot shows Acj6 (Purple) and Unc-4 (Dark Blue) co-expression in a group of cell clusters.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/106042/elife-106042-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A, B) Acj6 (blue) and Unc-4 (magenta) co-expression shows robust overlap in GFP-marked embryonic progeny of NB7-4, 23B neurons, in a late-stage embryo. (C–D) Acj6 (blue) expression marks 23B neurons in an early stage larval VNC (C) and an early stage pupal VNC (D). The only lineages that express Acj6 are 23B, 8B, and 9B, and of these only the posterior-dorsal cells, corresponding to hemilineage 23B, co-stained for GFP and Acj6 in the larval and pupal VNC. (E) This driver combination marks a cluster of SEZ neurons (arrowhead) in the adult brain, presumably SEZ 23B neurons in addition to sensory neuron afferents (arrows). (F) Close-up of SEZ to highlight the corresponding cell bodies (arrowhead).

By combining unc-4-GAL4AD and acj6-GAL4DBD transgenes in the same animal with a nuclear expression reporter gene, UAS-nls-tdTomato, we specifically visualized the thoracic clusters of 23B neurons in the adult CNS (Figure 1C). Small clusters of neurons were evident in the subesophageal zone, and their projections suggest that they are the labial homologs of hemilineage 23B (Figure 1—figure supplement 1D, E). Membranous GFP expression (UAS-myr-GFP) also highlighted axonal projections of a few leg, gustatory, and antennal sensory neurons which are missed with nuclear-based methods such as immunostaining for nuclear transcription factors or nuclear GFP reporter genes, since sensory cell bodies are located outside of the CNS. The reverse combination (unc-4-GAL4DBD and acj6-GAL4AD) exhibited an almost identical expression pattern (not shown).

To verify that these gene-specific split-GAL4 drivers recapitulate the intersected expression patterns of unc-4 and acj6, we performed immunostaining with antibodies against Acj6 and Unc-4 on embryos carrying the described transgenes and evaluated the overlap with the GFP signal. Robust GFP expression was observed in the late-stage embryo and marked segmentally repeated clusters of neurons in the VNC (Figure 1—figure supplement 1A, B). All GFP-positive cells were also positive for Acj6 and Unc-4 immunostaining, indicating that these cells correspond to the embryonic progeny of NB7-4, embryonic 23B neurons (Lacin et al., 2020). Occasionally, one to two cells per segment expressed both transcription factors but not GFP (not shown). These cells, located ventrally, are likely late-born, immature neurons and their GFP expression may lag endogenous gene expression of Acj6 and Unc-4 due to the additional round of transcription and translation required for GFP expression. Outside the CNS, GFP-positive sensory neurons were found in the embryonic head region, where taste organs are located (not shown). Overall, the embryonic expression analysis confirmed that the acj6-GAL4DBD and unc-4-GAL4AD split-GAL4 combination accurately recapitulates co-expression of Acj6 and Unc-4 proteins and target embryonic 23B neurons. To test whether this combination of split-GAL4 driver lines also specifically marks the 23B hemilineage during larval, pupal, and adult life, we carried out similar analysis during these stages. Like in the embryo, the intersection of acj6-GAL4DBD and unc-4-GAL4AD specifically marked 23B neurons in the larva, pupa, and adult (Figure 1—figure supplement 1C, D). Thus, this split-GAL4 combination effectively targets reporter expression specifically to the 23B neurons in the VNC from the early larva through to the adult.

### Identifying new marker genes for hemilineages and assigning hemilineages to scRNAseq clusters of the VNC transcriptome

The example described above demonstrated that combining the Trojan exon method with the split-GAL4 approach holds the potential to generate temporally stable, lineage-specific driver lines for every hemilineage in the VNC, provided suitable pairs of genes are identified. Our prior work created a map of the expression of 20 transcription factors, each of which is expressed from early larval stages to the adult in most or all neurons of a small number of hemilineages in the adult VNC (Lacin et al., 2020; Lacin et al., 2014; Lacin et al., 2019). When overlapped in a binary manner with each other, these transcription factors uniquely identify more than half of the 34 adult VNC hemilineages, rendering them ideal genomic targets from which to create a library of split-GAL4 driver lines.

To identify unique binary gene combinations that can selectively label each of the remaining hemilineages, we further analyzed scRNAseq data from the adult VNC (Allen et al., 2020). Allen et al. defined 120 t-SNE clusters based on unique combinations of significantly enriched genes, referred to as cluster markers. By comparing these cluster markers to established lineage markers, the Goodwin group assigned 18 hemilineages to one or more clusters, leaving 16 hemilineages unassigned. For example, they assigned grouped clusters 67, 93, 35, and 51 to lineage 23B. In agreement with our immunostaining that revealed that cluster markers acj6 and unc-4 mark this hemilineage (Figure 1C and D), we report that also the expression patterns of acj6 and unc-4 expression overlap in this grouped scRNAseq cluster (Figure 1E). We continued this approach and tested whether other cluster-specific marker genes were expressed in their corresponding hemilineages. For instance, Allen et al., assigned clusters 0 and 100 to hemilineage 4B. Both clusters express fkh, HLH4C, and oc genes in addition to three additional genes: hb9 (also known as exex), HGTX, and ap which we had previously shown to be expressed in 4B neurons (Lacin et al., 2009). Using GFP-tagged BAC reporter lines for fkh, oc, and HLH4C combined with immunostaining for Hb9, we demonstrate that cluster markers fkh, oc, and HLH4C are indeed expressed in 4B neurons in the larval and adult VNC, consistent with the scRNAseq data (Figure 2A, data not shown). In addition to hemilineage 4B, Hb9 marks hemilineage 10B and 16B neurons (Kuert et al., 2014). Hemilineage 10B was assigned to clusters 39, 68, and 91 and hemilineage 16B to clusters 5 and 46 (Allen et al., 2020). Knot (Kn) is a marker for clusters 39 and 91, and Sp1 for clusters 5 and 46. Reporters for both genes show that Kn and Sp1 are expressed in lineage 10B and 16B neurons, respectively (Figure 2B and C). Therefore, when a cluster marker, or marker combination, is uniquely associated with a hemilineage, it accurately marks this hemilineage.

![Figure 2.](https://cdn.elifesciences.org/articles/106042/elife-106042-fig2-v1.jpg)

**Figure 2.:** (A–C) Confocal stack of larval VNC displaying the overlapping expressions between transcription factors identified from scRNAseq data (Fkh, Kn, and Sp1; green in (A), (B), and (C), respectively) and Hb9 (magenta) in three lineages: 4B, 10B, and 16B (dashed lines). Asterisk in A indicates the Fkh+Hb9- 0 A lineage neurons. (D) Sox21a-GAL4 driven UAS-GFP (green) marks lineage 2 A neurons. (E) HmxGFSTF reporter (green) marks lineage 17 A neurons. (F, G) Wild-type MARCM clones (green) immunostained for Tj (magenta). The insets show the clone location in the VNC counterstained with CadN (blue). (F) Tj marks subpopulations of neurons in lineage 0 A in the T2 segment. These neurons likely belong to cluster 88, the only Tj+ 0A cluster in scRNAseq data. (G) Tj marks nearly all neurons of lineage 21 A in the T1 segment. Lineage identification of MARCM clones was performed based on neuronal projections detailed in Truman et al., 2004; Kanca et al., 2019. scRNAseq clusters with the corresponding lineages shown under each panel. Only one thoracic segment is shown. Neuroglian-specific antibody BP104 labels axon bundles of all lineages (magenta in D-E).

To identify the clusters that correspond to the remaining 16 hemilineages not assigned by Allen et al., we focused on the orphan clusters, which have not been assigned to any hemilineage. For each of these orphan clusters, we visualized the expression pattern of the cluster marker with reporter genes or antibody staining and studied the morphology of the neurons that expressed this cluster marker. To identify which hemilineage these neurons belonged to, we compared the observed morphology to the documented morphologies of unannotated hemilineages that used the same neurotransmitter as was expressed in the scRNAseq cluster. For example, glutamatergic clusters 15 and 86, which are adjacent in the t-SNE plot, are the only glutamatergic clusters that express Sox21a. To map these clusters to a hemilineage, we studied the morphology of the Sox21a-positive neurons in the VNC by expressing membrane-bound GFP under the control of a CRIMIC line reporting Sox21a expression (Figure 2D). This marked a group of ventral and anterior Sox21a-positive neuronal cell bodies situated near the midline in each hemisegment of the larval and adult VNC (Figure 2D). Their processes project dorsally and then sharply turn upon reaching the dorsal surface of the neuropil. Based on their glutamatergic neurotransmitter identity and their unique morphology, which matches that of 2 A interneurons (Harris et al., 2015; Shepherd et al., 2019), we assigned these clusters to hemilineage 2 A.

Another example is cluster 58, which, among all the VNC hemilineages, uniquely co-expresses unc-4 and islet (also known as tup) (Lacin et al., 2014). We had previously studied Unc-4-positive hemilineages and had identified that hemilineage 17 A is the only Unc-4-positive lineage that expresses Islet (Lacin et al., 2020). To verify that cluster 58 identified hemilineage 17 A neurons, we examined the expression pattern of another transcription factor, Hmx, which is a cluster marker for cluster 58 (Allen et al., 2020). Visualization of Hmx-positive neurons with a CRIMIC line reporting Hmx expression revealed that their cell bodies are located on the dorsal surface of the VNC and their processes project into the ipsilateral ventromedial neuropil and then loop dorsally (Figure 2E). This morphology is typical of 17 A neurons. Additionally, we found that cluster 77 is marked with the combination of Hmx and tup and is directly adjacent to cluster 58 in the adult VNC t-SNE plot (Allen et al., 2020). Thus, neurons of Hmx-positive clusters 58 and 77 likely belong to lineage 17 A (Figure 2E). Furthermore, we noted that some transcription factors are expressed in a subset of neurons within a hemilineage and appeared to correspond to one of the multiple scRNAseq clusters assigned to a hemilineage. For example, hemilineage 0 A contains clusters 22, 88, and 112. Of these three, Tj expression is only significant in cluster 88. We generated wild-type MARCM clones of lineage 0 A, and one can see that Tj is expressed in a subset of neurons only, presumably cluster 88 (Figure 2F; Lee and Luo, 1999). In contrast, other transcription factors (Fkh, Inv, Mab21a, HLH3b, and En) mark all clusters that belong to hemilineage 0 A, as revealed by scRNAseq analysis and our immunostaining-based transcription factor expression analysis (Asterisk in Figure 2A; data not shown). In hemilineage 21 A, which is composed of only one scRNAseq cluster, Tj marks nearly all cells (Figure 2G). Taken together, these data illustrate how cluster markers identified by scRNAseq data can be used to target individual hemilineages and even distinct subclasses within hemilineages.

Ultimately, we assessed the expression of 23 novel cluster-specific marker genes, all transcription factors, through immunohistochemistry with antibodies against the proteins of interest and/or reporter lines that accurately recapitulate target gene expression (Table 1). This effort allowed us to assign at least one cluster to 15 of the 16 previously unassigned hemilineages in the scRNAseq data (Allen et al., 2020; Table 1). This implies that we now have transcription profiles for 33 of the 34 major hemilineages in the VNC, which facilitates the design of lineage-specific split-GAL4 combinations. The only exception is hemilineage 18B, which remains unassigned to any scRNAseq clusters.

**Table 1.**
 Overview of cluster annotation, lineage-specific marker genes, and tested split-GAL4 driver lines.


<table>
  <thead>
    <tr>
      <th>Lineage</th>
      <th>Clusters (Allen et al.)</th>
      <th>Markers</th>
      <th>Driver line combinations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0A</td>
      <td>22, 88, 112</td>
      <td>En, Inv, Fkh, Tj, Lim1, grn, HLH3B, Mab-21, Gad1</td>
      <td>inv-GAL4-DBD, tj-p65.AD: * * * * fkh-GAL4-DBD, tj-p65.AD: * * * * mab21-p65.AD, fkhGAL4-DBD: * * *</td>
    </tr>
    <tr>
      <td>1A</td>
      <td>16</td>
      <td>Dr, Ets21C, Ptx1, ChAT</td>
      <td>Dr-p65.AD, ets21C-GAL4-DBD: * * *</td>
    </tr>
    <tr>
      <td>1B</td>
      <td>12, 47</td>
      <td>HLH4C, H15, Mid, Gad1</td>
      <td>HLH4C-GAL4-DBD, H15-p65.AD: * * *</td>
    </tr>
    <tr>
      <td>2A</td>
      <td>15, 86</td>
      <td>HLH3B, Oc, Sox21a, Drgx, Lim1, grn, svp, VGlut</td>
      <td>sox21a-GAL4-DBD, VGlut-p65.AD: * * * * sox21a-GAL4-DBD, lim1-VP16.AD: * * *</td>
    </tr>
    <tr>
      <td>3A</td>
      <td>7, 37, 85</td>
      <td>H15, HGTX, Grn, Lim1, ChAT</td>
      <td>H15-p65.AD, ChaT-GAL4-DBD: *</td>
    </tr>
    <tr>
      <td>3B</td>
      <td>26</td>
      <td>Fer3, CG4328, Gad1</td>
      <td>fer3-GAL4-DBD, cg4328-p65.AD: *</td>
    </tr>
    <tr>
      <td>4B</td>
      <td>0, 100</td>
      <td>Exex, Ap, Fkh, Tey, HGTX, HLH4C, Oc, ChAT</td>
      <td>ap-p65.AD, fkhGAL4-DBD: * * * ap-p65.AD, hgtx-GAL4-DBD: * * * *</td>
    </tr>
    <tr>
      <td>5B</td>
      <td>20, 87, 97</td>
      <td>Vg, Toy, Vsx2, Lim1, Gad1</td>
      <td>vg-p65.AD, toy-GAL4-DBD: * * * *</td>
    </tr>
    <tr>
      <td>6A</td>
      <td>9, 28</td>
      <td>Mab-21, Toy, Gad1</td>
      <td>mab21-p65.AD, toy-GAL4-DBD: * *</td>
    </tr>
    <tr>
      <td>6B</td>
      <td>3, 89</td>
      <td>Vg, Sens-2, En, CG4328, Vsx2, Gad1</td>
      <td>sens2-p65.AD, vg-GAL4-DBD sens2-GAL4-DBD, vg-p65.AD: * * CG4328-p65.AD, vg-GAL4-DBD: * * *</td>
    </tr>
    <tr>
      <td>7B</td>
      <td>2, 62</td>
      <td>Unc-4, Sv, Mab-21, ChAT</td>
      <td>unc-4-p65.AD, mab21-GAL4-DBD: * * * unc-4-GAL4-DBD, sv-p65.AD: * * *</td>
    </tr>
    <tr>
      <td>8A</td>
      <td>6, 69, 110</td>
      <td>Ey, Ems, Toy, Ets65A, VGluT</td>
      <td>ems-GAL4-DBD, eyAD: * * * * ems-GAL4-DBD, toy-p65.AD: * * ems-GAL4-DBD, vGluT-p65.AD: * * *</td>
    </tr>
    <tr>
      <td>8B</td>
      <td>8, 53, 76</td>
      <td>C15, Lim3, Acj6, ChAT</td>
      <td>C15-p65.AD, lim3-GAL4-DBD: * * *</td>
    </tr>
    <tr>
      <td>9A</td>
      <td>31, 50, 56, 57</td>
      <td>Dr, Ets65A, grn, sox21a, Gad1</td>
      <td>Dr-p65.AD, gad1-GAL4-DBD: * * * * Dr-p65.AD, sox21a-GAL4-DBD: * * * *</td>
    </tr>
    <tr>
      <td>9B</td>
      <td>54, 76</td>
      <td>Lim3, Drgx, Sens-2, Acj6, Tup, HLH4C, VGluT</td>
      <td>acj6-p65.AD, VGluT-GAL4-DBD: * * *</td>
    </tr>
    <tr>
      <td>10B</td>
      <td>39, 68, 91</td>
      <td>Exex, Kn, Sens-2, Lim3, ChAT</td>
      <td>knot-p65.AD, hb9-GAL4-DBD: * * * * hb9-p65.AD, sens-2-GAL4-DBD: * * * * knot-p65.AD, nkx6-GAL4-DBD: * * * * knot-p65.AD, lim3-GAL4-DBD: * * *</td>
    </tr>
    <tr>
      <td>11 A</td>
      <td>21</td>
      <td>Unc-4, Tey, ChAT</td>
      <td>unc-4-GAL4-DBD, tey-VP16: * * * unc-4-p65.AD, hgtx-GAL4-DBD: * * *</td>
    </tr>
    <tr>
      <td>11B</td>
      <td>38</td>
      <td>Eve, HLH4C, Gad1</td>
      <td>eve-p65.AD, gad1-GAL4-DBD: * * * *</td>
    </tr>
    <tr>
      <td>12 A</td>
      <td>40</td>
      <td>Unc-4, TfAP-2, Grn, ChAT</td>
      <td>unc-4-GAL4-DBD, TfAP2-p65.AD: * * *</td>
    </tr>
    <tr>
      <td>12B</td>
      <td>30, 73, 81, 83, 94</td>
      <td>Fer3, HGTX, CG4328, H15, Tey, Gad1</td>
      <td>HGTX-GAL4-DBD, gad1-p65.AD: * *</td>
    </tr>
    <tr>
      <td>13 A</td>
      <td>48, 75, 79</td>
      <td>Dbx, Fer2, Dmrt99B, Gad1</td>
      <td>dbx-GAL4-DBD, dmrt99B-p65.AD: * *</td>
    </tr>
    <tr>
      <td>13B</td>
      <td>17, 25</td>
      <td>D, Vg, CG4328, tey, svp, Gad1</td>
      <td>vg-GAL4-DBD, D-VP16.AD: * * vg-GAL4-DBD, tey-VP16.AD: * * *</td>
    </tr>
    <tr>
      <td>14 A</td>
      <td>13, 41, 74</td>
      <td>Dr, Toy, Lim1, Ets65A, Grn, VGluT,</td>
      <td>Dr-p65.AD, toy-GAL4-DBD: * * *</td>
    </tr>
    <tr>
      <td>15B</td>
      <td>36, 52, 80</td>
      <td>Tup, Lim3, HGTX, VGlut</td>
      <td>HGTX-GAL4-DBD, VGlut-p65.AD: * * * nkx6- GAL4-DBD, twit-p65.AD: * * *</td>
    </tr>
    <tr>
      <td>16B</td>
      <td>5, 46</td>
      <td>Lim3, Exex, Bi, Sp1, VGlut,</td>
      <td>hb9-p65.AD, bi-GAL4-DBD: * * * hb9-p65.AD, VGlut-GAL4-DBD: * * *</td>
    </tr>
    <tr>
      <td>17 A</td>
      <td>58, 77</td>
      <td>Unc-4, Hmx, Tup, ChAT</td>
      <td>unc-p65.AD, hmx-GAL4-DBD: * * * *</td>
    </tr>
    <tr>
      <td>18B</td>
      <td>N/A</td>
      <td>Unc-4, ChAT</td>
      <td>No line</td>
    </tr>
    <tr>
      <td>19 A</td>
      <td>19, 59, 82</td>
      <td>Dbx, Fer2, Scro, Gad1</td>
      <td>dbx-GAL4-DBD, scro-p65.AD: * * *</td>
    </tr>
    <tr>
      <td>19B</td>
      <td>27, 71</td>
      <td>Unc-4, Otp, ChAT</td>
      <td>No line</td>
    </tr>
    <tr>
      <td>20/22 A</td>
      <td>14, 33, 34, 78, 108</td>
      <td>Bi, Ets65A, Sv, ChAT</td>
      <td>sv-p65.AD, ets65-GAL4-DBD: * * * bi-GAL4-DBD, shaven-p65.AD: * * bi-p65.AD, ets65A-GAL4-DBD: * *</td>
    </tr>
    <tr>
      <td>21 A</td>
      <td>1</td>
      <td>Dr, Ey, Tj, VGluT</td>
      <td>Dr-p65.AD, tj-GAL4-DBD: * * * * Dr-p65.AD, ey-GAL4-DBD: * * *</td>
    </tr>
    <tr>
      <td>23B</td>
      <td>35, 51, 67, 93</td>
      <td>Unc-4, Acj6, Slou, Otp, ChAT</td>
      <td>unc-4-p65.AD, acj6-GAL4-DBD: * * *</td>
    </tr>
    <tr>
      <td>24B</td>
      <td>A small subset of clusters 52 and 36</td>
      <td>Toy, Ems, Twit, VGlut</td>
      <td>ems-GAL4-DBD, twit-p65.AD: * * *</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="4">**** Very specific for one hemilineage; *** Specific, some contamination from other neurons; ** Somewhat specific, significant contribution of e.g. motor neurons or sensory neurons; * More than one hemilineage marked</td>
    </tr>
  </tbody>
</table>

### Building specific and temporally stable driver lines for hemilineages in the VNC

To create a split-GAL4 library that uniquely marks essentially all major hemilineages, we generated gene-specific split-GAL4 driver lines by editing the genomic locus of the transcription factors identified above (Figure 3, Figure 3—figure supplement 1, Key Resources Table, Table 1). To edit the transcription factor locus, we exchanged the intronic cassette of previously engineered MIMIC or CRIMIC lines with a split-GAL4 coding Trojan exon of 13 genes (See Materials and methods). For 11 genes lacking established MIMIC or CRIMIC lines, we used CRISPR/Cas9 mediated gene editing via homology directed repair (HDR) to insert a Trojan exon carrying either DBD or AD split-GAL4 into a coding intron of the target gene and introduced attP sites to facilitate future cassette exchange with any other designer exon via phiC31 mediated cassette exchange (Diao et al., 2015; Nagarkar-Jaiswal et al., 2015; Li et al., 2023; Figure 3—figure supplement 2). In select cases, we inserted a Trojan exon directly in frame at the 3’ end of the gene (Figure 3—figure supplement 3). In total, we generated 34 split-GAL4 lines for 24 genes, 19 using the MiMIC method and 15 using CRISPR editing (Key Resources Table). The CRISPR approach failed only for tup and E5.

![Figure 3.](https://cdn.elifesciences.org/articles/106042/elife-106042-fig3-v1.jpg)

**Figure 3.:** Projections of confocal stacks showing the expression pattern of split-GAL4-driven membranous GFP (green) in the larval (A–O) and adult VNC (A’-O’). Only thoracic segments are shown in the larval images. (A, A’) Hemilineage 0 A, marked by inv-GAL4-DBD, tj-VP16.AD. (B, B’) Hemilineage 1 A marked by ets21c-GAL4-DBD, Dr-p65.AD. (C, C’) Hemilineage 2 A marked by sox21a GAL4-DBD, VGlut-p65.AD. (D, D’) Hemilineage 4B marked by ap-p65.AD, fkh-GAL4-DBD. (E, E’) Hemilineage 5B marked by vg-p65.AD, toy-GAL4-DBD. (F, F’) Hemilineage 6B marked by sens2-p65.AD, vg-GAL4-DBD. (G, G’) Hemilineage 7B marked by mab21-GAL4-DBD, unc-4-p65.AD. (H) Hemilineage 8 A marked by ems-GAL4-DBD, ey-p65.AD. (I, I’) Hemilineage 8B marked by lim3-GAL4-DBD, C15-p65.AD. (J, J’) Hemilineage 9 A marked by Dr-p65.AD, gad1-GAL4-DBD. (K, K’) Hemilineage 9B marked by acj6-p65.AD, VGlut-GAL4-DBD. (L, L’) Hemilineage 10B marked by knot-p65.AD, hb9-GAL4-DBD. (M, M’) Hemilineage 12 A marked by TfAP-2-GAL4-DBD, unc-4-p65.AD. (N, N’) Hemilineage 14 A marked by Dr-p65.AD, toy-GAL4-DBD. (O, O’) Hemilineage 17 A marked by unc-4-p.65AD, hmx-GAL4-DBD. The VNC was counterstained with CadN (magenta). The target lineage is indicated on the left bottom corner of each panel. Z-projections were made of selected regions of the VNC to highlight the cell-body clustering and axonal budling.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/106042/elife-106042-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Projections of confocal stacks showing the expression pattern of Split-GAL4-driven membranous GFP (green) in the larval (A–O) and adult VNC (A’-O’). Only thoracic segments are shown in the larval images. (A) Hemilineage 1B marked by HLH4c-GAL4-DBD, H15-p65.AD. (B) Hemilineages 3 A, 7B, and 12 A are marked by H15-p65.AD, ChAT-GAL4-DBD. (C) Hemilineages 3B and 12B marked by fer3-GAL4-DBD, cg4328-AD. (D) Hemilineage 6 A marked by mab21-p65.AD, toy-GAL4-DBD. (E) Hemilineage 11 A marked by unc-4-GAL4-DBD, tey VP16.AD. (F) Hemilineage 11B marked by eve-p65.AD, gad1-GAL4-DBD. (G) Hemilineage 12B marked by HGTX-GAL4-DBD, gad1-p65.AD. (H) Hemilineage 13 A marked by dbx-GAL4-DBD, dmrt-p65.AD. (I) Hemilineage 13B marked by vg-GAL4-DBD, D-vp16.AD. (J) Hemilineage 15B marked by HGTX-GAL4-DBD, VGlut-p65.AD. (K) Hemilineage 16B marked by hb9-p.65AD, VGlut-GAL4-DBD. (L) Hemilineage 19 A marked by dbx-GAL4-DBD, scro-p65.AD. (M) Hemilineage 20/22 A marked by bi-GAL4-DBD, shaven-p65.AD. (N) Hemilineage 23B marked by unc-4-p65.AD, acj6-GAL4-DBD. (O) Hemilineage 24B marked by twit-p65.AD, ems-GAL4-DBD.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/106042/elife-106042-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (A) Construction of CRISPR donor plasmids. For each gene of interest (GOI), a fragment is synthesized into the EcoRV restriction site of pU57_gw_OK2 as described before (Gratz et al., 2014). Briefly, this fragment contains a small sequence of the tRNA spacer, the gRNA against the gene of interest (GOI) (turquoise) and the Left HA and Right HA (turquoise) separated by a spacer containing SacI and KpnI restriction sites (black). A hemidriver cassette (gray, also see B) flanked by SacI and KpnI restriction sites is directionally cloned in between the HAs. (B) Six plasmids containing hemidriver cassettes (gray box) flanked by SacI and KpnI were made in the pBS-KS plasmid backbone. Each plasmid contains either a split-GAL4-DBD or p65.AD in phase 0, 1, and 2. Each hemidriver furthermore contains a 5’attP and FRT sequences, followed by a linker, splice acceptor (SA) and T2A proteolytic cleavage site. The linker length varies to keep the hemidriver in phase with the preceding exon (linker length: 24 nucleotides phase 0, 41 nucleotides phase 1 or 40 nucleotides phase2). An hsp70 termination sequence is introduced at the 3’end of the hemidriver followed by a splice donor (SD), FRT, and attP sequence. Note that the DBD cassettes do not contain a splice donor to keep them consistent with previously published split-GAL4 Trojan exon donors (Lacin et al., 2019). (C) The HAs promote HDR, and the entire hemidriver cassette is inserted at the site of the CRISPR/CAS9 cut, targeted by recognition sequence the gRNA-GOI. The attP sites allow for future cassette exchange with RMCE and genetic crosses.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/106042/elife-106042-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** Schematic representation of the direct tagging method that establishes split-GAL4DBD lines without any cloning. The gRNA against the gene of interest (GOI) cuts in the direct vicinity of the stop codon (+/-20 nt). The left HA 3’ end reaches up to, but does not include the stop codon, and the right HA 5’ end starts at the first nucleotide of the 3’ UTR. This ensures that the T2A-DBD fragment will be inserted at the 3’ end of the gene and is translated in frame with the GOI. (A) Construction of the CRISPR donor for direct tagging. A fragment that contains a small portion of the tRNA spacer, the gRNA-GOI, and the LHA, T2A-DBD, and RHA sequence is directly synthesized into the EcoRV site of pU57_gw_OK2. (B) Upon embryo injection, expression of gRNA1 linearizes the donor constructs, and the LHA-T2A-DBD-RHA fragment is used for CRISPR/Cas9 guided HDR. As a result, the T2A-DBD is inserted in frame at the 3’ end of the gene, and endogenous 3’ UTR posttranslational regulation mechanisms remain intact.

### Comprehensive testing of split-GAL4 combinations to target each hemilineage

Based on our analysis of scRNAseq data, we had clear predictions as to which binary combinations of split-GAL4 lines would label which hemilineages. To test these predictions, we specifically paired these new split-GAL4 lines either with one another or with previously generated split-GAL4 lines (Table 1; Lacin et al., 2019; Lacin et al., 2024; Chen et al., 2023a). Reconstituted GAL4 was visualized by UAS-myr-GFP or tdTomato and compared to the typical hemilineage morphologies of cell bodies and axonal trajectories to assess whether the split-GAL4 line targeted the predicted lineage. We identified 44 split-GAL4 combinations that target 32 out of 34 hemilineages and summarize the expression pattern of each combination in Table 1 and Supplementary file 1. Figure 3, Figure 3—figure supplement 1 display the larval and adult VNC expression patterns of the driver lines generated for 32 out of 34 hemilineages. Robust expression was also observed in 27 hemilineages in the larva, making these lines suitable for tracking the developmental history of their respective hemilineage during metamorphosis. The expression patterns of the split-GAL4 combinations for the remaining lineages (1B,3B,13A,13B, and 24B) start during pupal stages. (1B: HLH4C-GAL4DBD, H15-GAL4AD; 3B: H15-GAL4AD, ChAT-GAL4DBD; 13 A: dbx-GAL4DBD, dmrt99B-GAL4AD; 13B: vg-GAL4DBD, d-GAL4AD or vg-GAL4DBD, tey-GAL4AD; 24B: ems-GAL4DBD, twit-GAL4AD, data not shown).

### Application of developmentally stable hemilineage specific split-GAL4 lines

#### Morphological changes of 4B neurons during development

To show the applicability of our driver lines for developmental studies, we characterized the morphological changes in the neuronal processes during metamorphosis. Neurons of hemilineage 4B are excitatory cholinergic local interneurons (Lacin et al., 2019; Shepherd et al., 2019), and their arborizations are restricted to the ipsilateral leg neuropils and directly synapse with leg motor neurons in addition to many interneurons (Marin et al., 2024; Lesser et al., 2024). We have built three different combinations of split-GAL4 lines, each of which specifically targets most, if not all, post-embryonic 4B neurons. Two of these drivers, ap-GAL4AD with fkh-GAL4DBD and ap-GAL4AD with HLC4C-GAL4-DBD, drive reporter expression in 4B neurons starting from early larval stages while ap-GAL4AD with HGTX-GAL4DBD drives robust expression beginning at the white pupal stage (data not shown). Due to its stronger and earlier expression pattern, we used ap-GAL4AD with fkh-GAL4DBD to mark the morphology of 4B neurons at 0, 3, 12, 24, 48, and 72 hr APF (Figure 4). Like all the other post-embryonic neurons, 4B neurons extend an initial simple neurite bundle after they are born and do not show any further arborization until metamorphosis. As seen in the VNC of a 0 hr APF animal, this initial 4B neurite bundle projects dorsally away from the cell bodies and innervates the leg neuropil diagonally across the dorso-ventral axis (Figure 4A and A’). At 3 hr APF, multiple growth cones that point in different directions are visible on the tip of the 4B bundle (Figure 4B and B’). At 12 hr APF, these growth cones transform into three distinct branches, extending medially, laterally, or dorsally (Figure 4C and C’). At 24 hr APF, finer processes extend from these branches and puncta-like staining is visible, which suggests that synapses are being formed (Figure 4D and D’). At 48 hr APF, the crowded, finer processes are resolved into more refined and discreet processes and the synaptic puncta-like staining becomes more extensive (Figure 4E and E’). At 72 hr APF, the synaptic puncta appear to increase in size and to take on bouton-like shapes, resembling the adult morphology (Figure 4F and F’). In summary, by employing a developmentally stable driver line specific to hemilineage 4B, we documented stepwise morphological changes in the outgrowth of neuronal processes of 4B neurons throughout metamorphosis. These changes occur in distinct phases: initial neurite bundle expansion through new branch additions, followed by the formation and refinement of finer processes and synapses, and concluding with synaptic growth.

![Figure 4.](https://cdn.elifesciences.org/articles/106042/elife-106042-fig4-v1.jpg)

**Figure 4.:** Projection of confocal stacks showing the morphology of 4B neurons (green) marked with the ap-GAL4AD and fkh-GAL4DBD driver combination across different developmental time points during metamorphosis: 0, 3, 12, 24, and 48 hr after puparium formation (APF). The VNC is counterstained with CadN (magenta). Cell bodies of 4B neurons in the T3 region are marked with asterisks. (A–F) Complete projections in T2-T3 segments. Anterior (A) up; posterior (P) down. (A’-F’) Transverse views of the entire T3 segments across the dorso-ventral (D–V) axis; Dorsal is up. Arrowheads in B’ mark growth cones. Arrowheads in C’ mark three new branches towards the medial (m), lateral (l) and dorsal (d) part of the leg neuropil. Scale bar is 20 micron.

#### Neurotransmitter use

Another use for our library of transcription factor-specific Split-GAL4 lines is to determine which neurotransmitter a specific neuronal population produces. For example, we identified which neurotransmitter Acj6-positive neurons produce. We combined Acj6-split-GAL4 with a split-GAL4 line reporting the expression of one of the neurotransmitter marker genes -Gad1, ChAT, or VGlut- to visualize GABAergic, cholinergic, and glutamatergic Acj6-positive neurons, respectively (Figure 5). Acj6 is known to be expressed in glutamatergic 9B and cholinergic 8B and 23B hemilineages (Lacin et al., 2019). As expected, in each thoracic hemisegment of the VNC, these split-GAL4 combinations marked a single cluster of glutamatergic Acj6-positive neurons corresponding to 9B neurons (arrowheads in Figure 5A), two clusters of cholinergic Acj6-positive neurons corresponding to 8B and 23B neurons (arrowhead and arrows, respectively in Figure 5B), and no GABAergic Acj6-positive neurons (Figure 5C). In each hemibrain, the same split-GAL4 combinations identified one glutamatergic cluster with local projections, several cholinergic clusters with long projections, and two GABAergic clusters with long projections. Additionally, we detected cholinergic Acj6-positive leg and antennal sensory neurons and optic lobe neurons (Figure 5A–C).

![Figure 5.](https://cdn.elifesciences.org/articles/106042/elife-106042-fig5-v1.jpg)

**Figure 5.:** (A–C) Split-GAL4 line reporting Acj6 expression intersected with a cognate split-GAL4 line reporting the expression of Gad1, ChAT or VGlut to visualize GABAergic, cholinergic, and glutamatergic populations of Acj6-positive neurons, respectively. The VNC is counterstained with CadN (magenta). (A) Split-GAL4 combination acj6-GAL4AD, gad1-GAL4DBD>UAS-GFP driven UAS-GFP shows that the optic lobes contain cholinergic Acj6-positive neurons in addition to a few clusters of neurons with prominent long projections. In the VNC, two cholinergic clusters per hemisegment corresponding to 8B (arrowheads) and 23B (arrows) hemilineages are labeled in addition to some sensory neurons (asterisks). (B) Split-GAL4 combination acj6-GAL4AD, VGlut-GAL4DBD> UAS-GFP marks a single glutamatergic lineage in the dorsal part of the brain and one 9 A glutamatergic cluster in the VNC. (C) Split-GAL4 combination acj6-GAL4AD, gad1-GAL4DBD>UAS-GFP marks two GABAergic lineages in the brain and nothing in the VNC.

Furthermore, one can quickly test if the transcription factor that drives split-GAL4 expression is required for neurotransmitter production. When one inserts Trojan split-GAL4 hemidrivers in the first intron of the transcription factor gene locus, the Hsp70 transcriptional terminator located at the 5’ end of the trojan exon prematurely ends the transcript, and the truncated transcription factor oftentimes acts as a null mutant. We leverage this to test whether Acj6 has any role in the neurotransmitter identity of these neurons by using acj6 split lines. We repeated the same experimental procedure in an acj6 mutant background and found no apparent differences in neurotransmitter expression, concluding that Acj6 is dispensable for neurotransmitter identity (not shown).

In conclusion, we show that one can quickly assay neuronal identity features such as neurotransmitters and their receptors in specific populations of neurons in the entire CNS by simply using the split-GAL4 system and intersecting the expression patterns of a lineage-specific gene with the expression of another gene coding for neuronal identity. However, care should be taken interpreting these results, as the presence of the Hsp70 transcriptional terminator at the 5’ end of the Trojan exon may also affect the host gene’s 3’ UTR regulation, such that these drivers do not always faithfully recapitulate expression of genes subject to post-transcriptional regulation as was observed for ChAT (Lacin et al., 2019; Chen et al., 2023b).

#### Behavioral analysis with targeted lineage manipulation

Understanding the functional roles of specific hemilineages in the VNC is crucial for unraveling the neural circuits that govern behavior, yet the tools to study these lineages in detail have been limited. Harris et al., 2015 developed genetic tools to mark and track a small subset of VNC hemilineages through metamorphosis into the adult. This work used thermogenetic methods to stimulate neuronal activity of specific hemilineages to assess their function. This was done with decapitated flies to remove the effect of driver line expression in the brain. However, for many hemilineages, either no driver line existed or only a small portion of a hemilineage was targeted. To overcome these issues, we use our new split-GAL4 combinations to manipulate eight hemilineages for which no drivers previously existed (0 A, 1B, 4B,8B, 9B, 14 A, 16B, 17 A) and to target 16 lineages studied by Harris et al., 2015 with better coverage (Table 2). We evaluate lineage-coupled behavior with optogenetic activation, a method that is more robust and has a better time resolution compared to thermogenetic activation (Klapoetke et al., 2014). We show below how this approach is compatible with genetic methods to remove unwanted GAL4-mediated gene expression in the brain by applying a teashirt/FLP-based genetic intersection with the LexA/LexAop system to restrict GAL4 expression to the VNC (Simpson, 2016). A major advantage of such a layered genetic set-up is that behavior can be evaluated in intact flies without the need for decapitation. The lineage-behavior analysis of the 26 hemilineages is summarized in Table 2 and the response of intact and decapitated flies upon optogenetic activation is shown in Figure 3—videos 1–55. In the sections below, we summarize four examples.

**Table 2.**
 Overview of behavioral phenotypes upon optogenetic activation of specific hemilineages.


<table>
  <thead>
    <tr>
      <th>Lineage</th>
      <th>Genotype: Phenotype</th>
      <th>Videos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0A</td>
      <td>tj-p65.AD, inv-GAL4-DBD: No apparent behavioral response observed in response to acute optogenetic activation.</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>1A</td>
      <td>Dr-p65.AD, Ets21C-GAL4-DBD: Activation in both intact and decapitated animals drove leg extension making fly taller. Our observation differed from previously observed phenotypes of erratic forward locomotion, occasionally interrupted by grooming in decapitated animals (Harris et al., 2015).</td>
      <td>Figure 3—video 1; Figure 3—video 2</td>
    </tr>
    <tr>
      <td>1B</td>
      <td>H15-p65.AD, HLH4C-GAL4-DBD: Activation in both intact and decapitated flies drives leg rotational movement causing the joint between the femur and tibia to bend laterally, most pronounced by the hind legs.</td>
      <td>Figure 3—video 3; Figure 3—video 4</td>
    </tr>
    <tr>
      <td>2A</td>
      <td>VGlut-p65.AD, Sox21a-GAL4-DBD: Activation in intact animals drove high-frequency wing flapping, consistent with the findings of Harris et al which showed the same phenotype with the decapitated flies. In our experiments with decapitated animals, no wing buzzing was observed, and only halteres moved ventrally upon stimulation.</td>
      <td>Figure 3—video 5 ; Figure 3—video 6</td>
    </tr>
    <tr>
      <td>4B</td>
      <td>ap-p65.AD, HGTX-GAL4-DBD: Activation causes a full extension of all the legs in both decapitated and intact flies.</td>
      <td>Figure 3—video 7; Figure 3—video 8</td>
    </tr>
    <tr>
      <td>5B</td>
      <td>vg-p65.AD, toy-GAL4-DBD: Activation of 5B neurons halts almost every movement in the animal, causing walking, grooming, flying (tethered flight assay), and feeding flies to halt these behaviors. Decapitated animals also halt their grooming activity in response to 5B activation. Active 5B neurons also halt the larval locomotion.</td>
      <td>Figure 3—video 9; Figure 3—video 10; Figure 3—video 11; Figure 3—video 12</td>
    </tr>
    <tr>
      <td>6B</td>
      <td>CG4328-p65.AD, vg-GAL4-DBD: Activation in intact animals drove inhibition in wing buzzing and leg movements of the tethered flies. Activation in decapitated animals halted sporadic leg movements and drove a subtle change in the posture.</td>
      <td>Figure 3—video 14; Figure 3—video 15</td>
    </tr>
    <tr>
      <td>7B</td>
      <td>sv-p65.AD, unc-4-GAL4-DBD: Upon 7B activation, both decapitated and intact animals raised their wings and attempted take-offs, but only a few showed modest take-off behavior. We also observed tibia levitation in response to activation. Harris et al. observed robust take-off behavior.</td>
      <td>Figure 3—video 16; Figure 3—video 17; Figure 3—video 18</td>
    </tr>
    <tr>
      <td>8A</td>
      <td>ey-p65.AD, ems-GAL4-DBD: Activation brings the body of the fly closer to the ground likely flexing leg segments in both intact and decapitated animals. Harris et al. observed minimal effects after activation.</td>
      <td>Figure 3—video 19; Figure 3—video 20</td>
    </tr>
    <tr>
      <td>8B</td>
      <td>C15-p65.AD, Lim3-GAL4-DBD: Activation drove intact animals lean backward and take-off. A few animals initiated wing flapping after the jump; others failed to initiate wing flapping and fell after the jump, then they jumped again under the continuous activation. Decapitated animals showed a similar response but never initiated the wing flapping after the take-off.</td>
      <td>Figure 3—video 21; Figure 3—video 22-2</td>
    </tr>
    <tr>
      <td>9A</td>
      <td>Dr-p65.AD, Gad1-GAL4-DBD: Activation in intact animals drove erratic forward locomotion of the animal. Activation in tethered intact flies restricted the legs to stay in a specific posture. In decapitated animals, bodies were lowered toward the ground with legs becoming more splayed for approximately two seconds before occasional forward locomotion and leg grooming, consistent with previous research by Harris et al.</td>
      <td>Figure 3—video 23; Figure 3—video 24; Figure 3—video 25</td>
    </tr>
    <tr>
      <td>9B</td>
      <td>acj6-p65.AD, VGlut-GAL4-DBD: Activation in intact animals did not lead to any robust behavior; occasionally animals changed their posture mildly. Decapitated animals halted their grooming in response to 9B activation. This halting behavior was less penetrant compared to the halting behavior observed with 5B activation.</td>
      <td>Figure 3—video 26; Figure 3—video 27;</td>
    </tr>
    <tr>
      <td>10B</td>
      <td>Hb9-p65-AD, sens-2-GAL4-DBD: Activation in intact animals drove erratic walking behavior. 10B activation in decapitated animals drove leg extension and body twisting. Our findings differed from Harris et al., 2015, which showed erratic leg movements causing backward locomotion with occasional wing flicking and buzzing.</td>
      <td>Figure 3—video 28; Figure 3—video 29;</td>
    </tr>
    <tr>
      <td>11 A</td>
      <td>tey-VP16.AD, unc-4-GAL-4-DBD: Low intensity light activation drove lateral wing waving with occasional jumping, while high intensity activation drove wing buzzing and jumping in intact and decapitated animals.</td>
      <td>Figure 3—video 30; Figure 3—video 31; Figure 3—video 32; Figure 3—video 33</td>
    </tr>
    <tr>
      <td>11B</td>
      <td>eve-p65.AD, Gad1-GAL4-DBD: Harris et al. observed take-off behavior after activation of the 11B neurons. However, upon light activation, we observed wing movements without any take-off behavior. The wings moved from side to side in a buzzing behavior.</td>
      <td>Figure 3—video 34; Figure 3—video 35</td>
    </tr>
    <tr>
      <td>12 A</td>
      <td>TfAP2-p65.AD, unc-4-GAL4-DBD: CsChrimson expression showed a lethal phenotype with no surviving adults. We generated lineage clones using TfAP-2-GAL4. Animals expressing CsChrimson in 12 A neurons in one side of the T1 segment showed a single swing movement of the leg that is located on the same side as the animal lineage clone. We also observed bilateral wing buzzing.</td>
      <td>Figure 3—video 36; Figure 3—video 37</td>
    </tr>
    <tr>
      <td>13 A</td>
      <td>dmrt99B-p.65AD, dbx-GAL4-DBD: Upon 13 A activation, intact flies halt their walking and grooming behaviors and change the body posture, making flies slightly taller due to likely femur-coxa extension. Decapitated flies also halt the grooming behavior in response to 13 A activation. Both intact and decapitated flies buzz their wings in response to activation, a phenotype likely arising from contaminating neurons.</td>
      <td>Figure 3—video 38; Figure 3—video 39</td>
    </tr>
    <tr>
      <td>13B</td>
      <td>D-VP16.AD, vg-GAL4-DBD: Intact flies lost control of their legs and fell on their back with uncoordinated leg movements upon activation of 13B neurons. Decapitated flies responded with a postural change and a weak leg extension phenotype.</td>
      <td>Figure 3—video 40; Figure 3—video 41</td>
    </tr>
    <tr>
      <td>14 A</td>
      <td>Dr-p65.AD, toy-GAL4-DBD: Activation caused intact animals to fall on their back or side with uncoordinated leg movements; flies remained uncoordinated until the cessation of the stimulus. In decapitated animals, activation drove the femur-tibia joint to move anteriorly, most pronounced in the middle legs. We also observed flexion of the legs.</td>
      <td>Figure 3—video 42; Figure 3—video 43</td>
    </tr>
    <tr>
      <td>15B</td>
      <td>VGlut-p65.AD, HGTX-GAL4-DBD: Upon light stimulation in both intact and decapitated flies, the legs showed a severe flexing phenotype. The legs flexed tightly against the body with the flies falling into a fetal position until after light stimulation ended.</td>
      <td>Figure 3—video 44; Figure 3—video 45</td>
    </tr>
    <tr>
      <td>16B</td>
      <td>Hb9-p65.AD, Bi-GAL4-DBD: Activation in both intact and decapitated animals drove flexion at the femur-tibia joint and coxa-femur axis joint causing the animal to sink lower to the ground.</td>
      <td>Figure 3—video 46; Figure 3—video 47</td>
    </tr>
    <tr>
      <td>17 A</td>
      <td>unc-4-p65.AD, Hmx-GAL4-DBD: Activation of 17 A neurons drove flexion of all the leg segments in both decapitated and intact animals.</td>
      <td>Figure 3—video 48; Figure 3—video 49</td>
    </tr>
    <tr>
      <td>19 A</td>
      <td>scro-p65.AD, dbx-GAL4-DBD: Activation in decapitated animals drove flexion at the tibia-tarsus joint as well as anterior movement of the femur-tibia axis. In intact animals, we observed severe flexing of the legs against the body, making flies fall on their back. Harris et al. observed a leg-waving phenotype of the T2 legs in decapitated animals after stimulation.</td>
      <td>Figure 3—video 50; Figure 3—video 51</td>
    </tr>
    <tr>
      <td>21 A</td>
      <td>Dr-p65.AD, tj-GAL4-DBD: Activation of 21 A neurons in decapitated animals drove flexion of the legs, bringing the body of the fly closer to the ground. We observed a similar phenotype in intact animals tethered to a pin.</td>
      <td>Figure 3—video 52; Figure 3—video 53</td>
    </tr>
    <tr>
      <td>23B</td>
      <td>unc-4-p65.AD, acj6-GAL4-DBD: Activation caused intact animals to fall on their back due to uncoordinated leg movements and sustained flexion or extension of the leg segments; flies remained uncoordinated until the cessation of the stimulus. Flies also showed increased grooming activity. We also observed wing buzzing in response to activation. Decapitated animals showed similar responses.</td>
      <td>Figure 3—video 54; Figure 3—video 55</td>
    </tr>
  </tbody>
</table>

#### Hemilineage 8B

Hemilineage 8B neurons, which are cholinergic and excitatory, show complex segment-specific intersegmental projections that innervate the tectulum and leg neuropil (Shepherd et al., 2019). To target 8B neurons, we used lim3-GAL4DBD and c15-GAL4AD, which target most of the 8B neurons as well as numerous neuronal clusters in the brain (Figure 6A). We activated only 8B neurons through exclusion of brain neurons by layering lim3-GAL4DBD, c15-GAL4AD with a teashirt (tsh) driver that restricts expression of the optogenetic construct CsChrimson-mVenus to only VNC neurons (Simpson, 2016; Figure 6B). We observed that optogenetic stimulation of 8B neurons triggered jump behavior in intact and decapitated animals (Figure 6C and D, Figure 3—video 19, Figure 3—video 20). Unlike 7B neuronal activation, which makes flies raise their wings before jumping (Figure 3—video 16, Figure 3—video 17, Figure 3—video 18; Lacin et al., 2020), 8B activation resulted in jumping without a wing raise, which is reminiscent of the Giant Fiber (GF) induced escape movement sequence (Namiki et al., 2018; Namiki et al., 2022; Zabala et al., 2009; Card and Dickinson, 2008; Cheong et al., 2023). Therefore, our results suggest that 8B neurons participate in the GF-driven take-off circuit.

![Figure 6.](https://cdn.elifesciences.org/articles/106042/elife-106042-fig6-v1.jpg)

**Figure 6.:** (A–D) Optogenetic activation of hemilineage 8 A in the VNC triggers jump behavior. lim3-GAL4DBD; c15-GAL4AD-driven CsChrimson::mVenus (green) targets 8B neurons in the VNC but also shows an unwanted broad brain expression (A), which can be suppressed via an additional layer of intersection using teashirt (tsh)-lexA-driven FLP strategy (B). (C, D) Overlay of video frames to capture the jump sequence induced by optogenetic activation of lineage 8B in the VNC. Intact flies (C) and decapitated flies (D) jump without raising their wings upon optogenetic activation, but decapitated flies were slower to initiate the jump. (E) Optogenetic activation of hemilineage 9 A induces forward walking in decapitated flies. (F, G) Clonal stimulation of hemilineage 12 A in the VNC in decapitated flies induces bilateral wing opening and single-step behavior. (F) Confocal stack displaying the lineage 12 A clone that extends from T2 into T1 and T3. (G) Overlay of movie frames. The fly folds both wings outward and swings its right front leg forward upon optogenetic activation. (H, L) Optogenetic activation of hemilineage 21 A in the VNC on a tethered, intact fly triggers flexion of the tibia-femur joint. (H) Without stimulus, all the legs move erratically in response to being tethered. (I) Upon optogenetic activation, all legs are pulled toward the body, the tibia-femur joints are flexed, and animals stay in this position until the end of stimulus. (J) Overlay of the movie shown in panel H and I, zoomed in on the left T1 leg. Note how the leg is pulled towards the body upon activation (520 ms) compared to its more lateral position without activation (315 ms). (K, L) Elimination of 21 A neurons makes hind leg femur-tibia joints protrude laterally (L) compared to control animals (K). For all overlays of movies, green display frames without optogenetic activation, magenta with optogenetic activation.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/106042/elife-106042-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Synaptic connectivity of the GF neuron extracted from the data generated by Marin et al., 2024. (A–C) Analysis of GF input connections. (D–F) Analysis of GF output connections. (A) Count of neurons per hemilineage that form synapses with GF dendrites. A total of ten hemilineages form synapses with GF dendrites. Five neurons originate from hemilineage 8B, six from hemilineage 7B, five from lineage 5B, and three from lineage 21 A. (B) Combined connectivity per hemilineage, cumulative count of synapses between GF dendrites and hemilineage neurons. The connectivity between hemilineage 8B and the GF is significant, spanning 339 synapses. Hemilineage 7B, 5B, and 21 A forms 45, 205, and 108 connections, respectively. (C) Weighted connectivity per hemilineage, calculated as the cumulative count of synapses between GF dendrites and hemilineage neurons, divided by the total number of GF output connections observed at a threshold of five synapses per neuron. Hemilineage 8B contributes heavily, making up 25% of GF input, followed by 15% from lineage 5B. Lineage 7B contributes 3.3% and lineage 21 A 8%. (D) Count of neurons per hemilineage that form synapses with GF axons. A total of 13 hemilineages are downstream synaptic partners of the GF. Of those, the synapses formed with lineage 8B are most divergent and span 12 neurons. (E) Combined connectivity per hemilineage, cumulative count of synapses between GF axons and hemilineage neurons. Hemilineage 8B makes 208 synaptic contacts. Hemilineages 18B and 6B also form strong connections, 206 and 121 connections, albeit with fewer neurons (5 and 6, respectively). (F) Weighted connectivity per hemilineage, calculated as the cumulative count of synapses between GF axons and hemilineage neurons, divided by the total number of GF output connections observed at a threshold of five synapses per neuron. 12.5% of output GF synaptic contacts are made with hemilineage 8B, followed by 12.4% with lineage 18B and 7.3% with lineage 6B.

To investigate the relationship between 8B and the GF neurons, we analyzed the synaptic connections of the GF (DPN01) using MANC2.1 in neuPrint (Marin et al., 2024; Plaza et al., 2022; Takemura et al., 2023), and focused on neurons with at least five synapses, for one half of the bilateral symmetric circuit. We found that hemilineage 8B neurons are upstream synaptic partners of the GF, with 12 8B neurons accounting for 12.5% of the GF synaptic inputs (Figure 6—figure supplement 1, Supplementary file 2). Surprisingly, 8B neurons were also downstream synaptic partners of the GF, with 13 neurons accounting for 12.5% of the GF’s synaptic outputs (Figure 6—figure supplement 1, Supplementary file 3). This contribution is significant, as it is even higher than the 8.7% of synaptic output connections that a GF dedicates to innervating the tergotrochanter motor neuron (TTMn), which innervates the jump muscle. We next compared if those 8B neurons that are downstream partners of the GF also provide input to the GF. Surprisingly, the majority of 8B neurons that connect to the GF are both downstream and upstream synaptic partners. These nine neurons make up 21.5% and 9.1% of total GF synaptic inputs and outputs, respectively. Taken together, our behavioral data and the connectome analysis suggest that a subset of 8B neurons functions in the GF circuit and elicits take-off behavior.

#### Hemilineage 9A

Hemilineage 9 A is composed of inhibitory GABAergic neurons, which integrate sensory input from leg proprioceptive neurons (Agrawal et al., 2020; Lacin et al., 2019). To activate 9 A neurons, we drove CsChrimson expression with Dr-GAL4AD and gad1-GAL4DBD. Decapitated animals exhibited erratic walking behavior with their legs extended when the stimulus lasted over three seconds, and this erratic walking immediately stopped when the stimulus ended (Figure 6E, Figure 3—video 23, Figure 3—video 24, Figure 3—video 25). In agreement with previous reports (Agrawal et al., 2020; Harris et al., 2015), we observed that both decapitated and intact animals extended their legs in response to activation.

#### Hemilineage 12A

Hemilineage 12 A neurons are cholinergic and excitatory and display segment-specific and complex intersegmental projections to wing and leg nerve bundles (Marin et al., 2024; Lesser et al., 2024). We used the unc-4-GAL4DBD and TfAP2-GAL4AD driver line to express CsChrimson in 12B neurons. None of these animals, however, survived to adulthood, not even in the absence of retinal, the cofactor required for CsChrimson activity. To overcome this issue, we generated stochastic FLP-based lineage clones that expressed CsChrimson in 12 A neurons in one or a few hemisegment(s). We then optogenetically activated decapitated flies and recorded their behavior (Figure 3—video 36, Figure 3—video 37), followed by dissection and immunostaining to visualize which lineage clones were responsible for the observed phenotype. We found two cases where optogenetic activation resulted in bilateral wing opening and a leg swing. The segment and side of the 12 A lineage clone corresponded to the side of the leg that moved (Figure 6F and G). We also observed the following behavioral phenotypes in response to optogenetic activation, but we did not dissect the animals to further identify the lineage clone: high frequency wing beating, backward walking immediately after the stimulus termination, and abdominal extension and bending. These results indicate that 12 A neurons, as expected from their complex projections, control a magnitude of behaviors.

#### Hemilineage 21A

Hemilineage 21 A neurons are glutamatergic, likely inhibitory interneurons, and innervate the leg neuropil in all thoracic segments. To assess the behaviors executed by 21 A neurons, we used two different driver lines: Dr-GAL4AD and ey-GAL4DBD or Dr-GAL4AD and tj-GAL4DBD. Both combinations target most of the 21 A neurons, the latter with higher specificity, yet both lines showed consistent results upon optogenetic activation. Stimulation of either intact or decapitated animals forced the leg segments into a specific geometry (Figure 3—video 52, Figure 3—video 53). In tethered intact animals, whose legs are freely moving in the air, we observed a clear flexion in the femur-tibia joint (Figure 6H–J). To test whether 21 A neurons are necessary for the relative femur-tibia positioning, we eliminated 21 A neurons by expressing UAS-hid with Dr-GAL4AD, ey-GAL4DBD. Flies lacking 21 A neurons showed aberrant walking patterns. We observed that femur-tibia joints of the hind legs protruded laterally compared to the control sibling flies (Figure 6, K, L). Our results showed that 21 A neurons control the relative positioning of the leg segments, especially the femur and tibia.

#### Other anatomical region of interest

While characterizing the expression pattern of the gene-specific split-Gal4 library, we noted that the applicability of these tools extends beyond the VNC. A total of 24 driver lines targeted clusters of neurons in the subesophageal zone (SEZ) (Table 1). The SEZ processes mechanosensory and gustatory sensory input and controls motor output related to feeding behavior. It is anatomically part of the VNC and comprises the first three segments of the VNC, which are populated by NBs that are the segmental homologs of NBs found in the thoracic and abdominal segments of the VNC (Doe and Goodman, 1985; Kendroud et al., 2018; Li et al., 2014). A key difference is that only a small number of NBs pairs survive in the SEZ (Kuert et al., 2014). The SEZ NBs are expected to express a similar set of transcription factors as their thoracic counterparts. Therefore, these transcription factors and their corresponding split-GAL4 driver lines are excellent tools to target and manipulate homologous lineages in the SEZ.

## Discussion

The ability to trace neuronal lineages across their developmental journey and to manipulate their function is essential to investigate how neurons interconnect to form neuronal circuits and regulate specific behaviors. To address these questions, most studies have focused on a few specific regions of the CNS, for example, the mushroom body in flies, for which specific genetic tools exist to target defined neuronal populations during developmental and adult life. In this study, we utilized scRNAseq data from the VNC (Allen et al., 2020) that completed its annotation for all but one hemilineage and analyzed the transcriptome of individual hemilineages. Through this effort, we identified new marker genes for hemilineages, verified their expression patterns in the VNC, and created split-GAL4 driver lines for 24 lineage-specific marker genes lines by editing their genomic loci. By employing binary combinations of these new lines amongst each other or with driver lines established previously, we constructed a comprehensive split-GAL4 library that targets 32 out of 34 hemilineages during development and adult life (Table 1), enabling the genetic dissection of how each hemilineage contributes to circuit development (Lacin et al., 2020; Lacin et al., 2019; Lacin et al., 2024; Chen et al., 2023a; Xie et al., 2021; Xie et al., 2019).

### Mapping and manipulating morphological outgrowth patterns of hemilineages during development

The driver line combinations presented here are developmentally stable, and most combinations label both embryonic and post-embryonic neurons of the target hemilineage. This makes them a valuable resource for lineage-based dissection of larval nervous system development and function. Furthermore, they target individual hemilineages throughout metamorphosis and adult life. This is critical as the formation and maturation of adult neuronal circuits take place during metamorphosis and last several days. This time window is greatly prolonged compared to the rapid development of larval circuits that occurs within a few hours during embryogenesis and offers greater opportunities for experimental manipulation. By layering temperature or light-controlled genetic effectors, like shibereTS, channelrhodopsins, or LACE-Cas9 (Polstein and Gersbach, 2015; Mohammad et al., 2017) with our toolkit, researchers can manipulate neuronal and gene activity with high temporal resolution. This makes it possible to investigate dynamic processes such as synapse formation, circuit assembly, and functional maturation. For example, recent studies demonstrated that developing neuronal circuits exhibit patterned calcium activities during metamorphosis, and these activities likely regulate the synaptic connectivity among neurons (Akin et al., 2019; Bajar et al., 2022). ShibereTS expression driven by our driver lines can inhibit the developmentally observed neuronal activity in a specific hemilineage during a specific time window to test whether this manipulation alters the synaptic connectivity of the hemilineage.

### 8B neurons likely function in the giant-fiber escape circuit

Our work here demonstrated that the activation of 8B neurons elicits robust take-off behavior that closely resembles the GF-induced take-off response (Card and Dickinson, 2008). This observation raises an intriguing question: do 8B neurons function in the GF escape circuit? Interestingly, although 8B neurons do not appear to connect directly to TTMns, the primary output neurons of the escape circuit (Marin et al., 2024), we report that they do form a complex synaptic relationship with the GF. Specifically, a subset of 8B neurons is both upstream and downstream synaptic partners of the GF, accounting for 25% of GF’s synaptic input and 12.5% of GF’s output. This synaptic loop centered around the GF neurons suggests a recurrent feedback mechanism within the GF circuit. Given that hemilineage 8B neurons exhibit interconnectivity with each other and receive leg proprioceptive input (Marin et al., 2024), we speculate that lineage 8B may function as an integrator in and amplifier of the GF circuit. This example underscores that our split-GAL4 library provides an excellent resource for further exploration of lineage-coupled behavior.

### Addressing lineage differentiation by studying cell heterogeneity within hemilineages

Our lineage annotation of the VNC transcriptome revealed that most hemilineages are represented by more than one RNAseq cluster, which reflects heterogeneity within a hemilineage and indicates that hemilineages can be further subdivided into subclasses of neurons. Indeed, we found that such subclasses express specific transcription factors, which can be considered subclass-defining factors, for example Tj in hemilineage 0 A (Figure 2F). The tools we present here form a starting point to visualize or manipulate neuronal subclasses within a hemilineage. For example, one can use the split-GAL4 driver line combinations to express an UAS transgene preceded by an FRT-flanked stop codon in a specific lineage. Flippase expression can be easily restricted to a subclass of neurons in a hemilineage with the LexA/LexAop system under control of the subclass-defining transcription factor. As a result, the transgene will only be expressed in a subclass of neurons in a hemilineage. Instead of working with subclass-defining transcription factors, one can also use birth-order marking temporal genes such as chinmo, mamo, or broad-c (Liu et al., 2019; Maurange et al., 2008; Zhu et al., 2006; Zhou et al., 2009) to restrict driver activity to a group of neurons born in a specific temporal window within a hemilineage. Thus, with a strategic combination of orthogonal gene-specific driver system (e.g. split-GAL4, LexA, and QF), one can now dissect the neuronal circuit formation with unprecedented precision.

In conclusion, our study underscores the potential of temporally stable driver lines to target hemilineages in the VNC during development and adult life. This approach enables future studies investigating how neurons acquire their specific fates and integrate into the broader networks of neural networks that control intricate animal behaviors.

## Materials and methods

### scRNA-seq data analysis

Candidate genes to convert into split-GAL4 driver lines were identified using the scRNA-seq data generated by Allen et al., 2020. No modifications were made to the preprocessing pipeline, and we used the cluster markers defined by Allen et al., 2020 and investigated the combinatorial expression patterns of the highest expressed cluster markers in binary combinations using the code shared on GitHub using Seurat v5 (https://github.com/aaron-allen/VNC_scRNAseq; Allen, 2021). Candidate genes to make split-GAL4 drivers from were chosen based on their ability to selectively mark the scRNAseq cluster(s) covering a hemilineage and selected markers that were expressed by near all cells of the hemilineage for the downstream experimental validation steps. We then prioritized testing these combinations based on the availability of antibodies, BAC lines, and CRiMIC/MiMIC constructs to validate their expression pattern prior to creating split-GAL4 lines for these candidates.

### Fly stocks

Fly stocks were reared on the standard cornmeal fly food at 25 °C unless indicated otherwise. Fly lines used in this study are listed in the Key Resources Table. A current inventory of gene-specific split-GAL-4 lines is maintained by Yu-Chieh David Chen and Yen-Chung Chen from Claude Desplan’s lab (https://www.splitgal4.org). Lines were contributed by the labs of Claude Desplan, Liqun Lue, Benjamin White, Norbert Perrimon, and Haluk Lacin’s laboratories. Behavior was tested at room temperature (22–25°C) 2–10 days post-eclosion. Genotypes of animals used in figures and videos are shown in Supplementary file 5.

### Clonal analysis

Wild type MARCM analysis was performed as described before (Lee and Luo, 1999). Animals were heat-shocked within 24 hr after egg hatching (Lacin et al., 2014). Multi-Color FLP-Out NB3-5 (lineage 9) clones were generated with 49C03-GAL4 crossed to hsFlp2::PEST;; HA_V5_FLAG as described before (Lacin and Truman, 2016; Nern et al., 2015). 20X-UAS>dsFRT > CsChrimson mVenus_attp18, hs-Flp2PESt_attp3 X Tf-AP2-GAL4: lineage clones were generated via heat-shock within 24 hours window after egg hatching.

### Gene editing

#### Introduction of Trojan split-GAL4 by recombinase-mediated cassette exchange

Gene-specific split-GAL4AD and split-GAL4DBD lines were made from MiMIC or CRIMIC lines via Trojan exon insertion as described before (Lacin et al., 2019; Chen et al., 2023a; Diao et al., 2015; Nagarkar-Jaiswal et al., 2015). Briefly, pBS-KS-attB2-SA(0,1, or 2)-T2A-Gal4DBD-Hsp70 or pBS-KS-attB2-SA(0,1, or 2)-T2A-p65AD-Hsp70 were co-injected with phiC31 integrase into the respective MiMIC/CRIMIC parent stock (Key Resources Table). Transformants were identified via the absence of y+or 3xP3-GFP markers. The correct orientation of the construct was validated by GFP signal upon crossing the putative hemidriver to a line carrying the counter hemidriver under control of the tubulin promoter and an UAS-GFP transgene (Key Resources Table).

### Insertion of gene-specific Trojan split-GAL4 construct with CRISPR

Guide RNAs (gRNA) were selected to target all expressed isoforms in an amendable intronic region or to the 3’ end of the gene if no suitable intron was present (e.g. fer3 and ems; Key Resources Table, Supplementary file 4). gRNAs were identified with CRISPR target Finder for vas-Cas9 flies, BDSC#51324 with maximum stringency and minimal off-target effects (Gratz et al., 2014). gRNA targeting hb9, vg, and H15 was cloned into pCFD4 together with a guide RNA to linearize the donor vector (Port et al., 2014; Kanca et al., 2019). The remainder of the guides was synthesized into pUC57_GW_OK2 (Genewiz/Azenta (Burlington, MA)).

CRISPR donors were generated using a modified version of the strategy developed by Kanca et al., 2022. We used the Genewiz company to synthesize a DNA fragment into the EcoRV site of the pUC57-GW- OK2 vector. This fragment is made of the left and right homology arms (HA) which are immediately adjacent to the gRNA cut site and restriction enzyme sites (SacI-KpnI) between these arms (Figure 3—figure supplement 2A). We then directionally cloned the Sac1-attP-FRT-splitGAL4-FRT-attP-KpnI fragment (Figure 3—figure supplement 2B) in between the left and right HAs using the SacI and KpnI sites. Note that SacI and Kpn should only be chosen when the homology arms do not have these cut sites. To facilitate this last step, we generated universal plasmids in each reading frame for each hemi driver, DBD and p65.AD in the original Trojan vector backbones, referred to as pBS-KS-attP2FRT2-SA-T2AGAL4[AD or DBD (0,1,2)]-Hsp70 with Gibson assembly, combining the following fragments:

Note EcoRI and EcoRV (capitalized) sites were included as a back-up strategy for replacing the Trojan exon between attP FRT if needed.

3’ FRT- attP-KpnI sequence PCR amplified from pM14 (Kanca et al., 2022) with primers:

Corresponding sequences from pBS-KS are underlined, pM14 are in italics, and Trojan AD/DBD are in bold; restriction enzyme sites are in all caps. All plasmids were validated by Sanger sequencing (Genewiz/Azenta Burlington, MA).

Note that for hb9, vg, sens-2, H15, scro, Ets21C and eve we inserted the T2A- split-GAL4DBD and/or T2A-split-GAL4p65-AD into the host gene intron as a Trojan exon with flanking FRT sites in a similar manner to CRIMIC lines generated by the Bellen Lab (detailed below). However, since this is problematic for FLP-dependent mosaic experiments, we generated additional lines for hb9, sens2, Ets21C eve and vg lacking FRT sites by replacing the FRT-flanked cassettes with the original White lab Trojan AD/DBD exons via attP-phiC31-mediated recombination as described above.

Split-GAL4 drivers for and D were made by the Erclick laboratory. CRISPR-mediated gene editing was performed by WellGenetics Inc using modified methods of Kondo and Ueda, 2013. For fkh, the gRNA sequence GTGACATCACCAATACCCGC[TGG] was cloned into a U6 promoter plasmid. Cassette T2A-Gal4DBD-RFP, which contains T2A, Gal4DBD, a floxed 3xP3-RFP, a Hsp70Ba 3’UTR, and two homology arms, was cloned into pUC57-Kan as donor template for repair. fkh/CG10002-targeting gRNAs and hs-Cas9 were supplied in DNA plasmids, together with donor plasmid for microinjection into embryos of control strain w[1118]. F1 flies carrying the selection marker of 3xP3-RFP were further validated by genomic PCR and sequencing. CRISPR generates a break in fkh/CG10002 and is replaced by cassette T2A-Gal4DBD-RFP.

Similarly, for D, the gRNA sequences ACTCGACTCTAATAGAGCAC[CGG] /GCACCGGAACCGGTCGCCTC[AGG] were cloned into U6 promoter plasmid(s). Cassette T2A-VP16AD-3XP3-RFP, which contains T2A, VP16AD, and a floxed 3xP3-RFP, and two homology arms were cloned into pUC57-Kan as donor template for repair. D/CG5893-targeting gRNAs and hs-Cas9 were supplied in DNA plasmids, together with donor plasmid for microinjection into embryos of control strain w[1118]. F1 flies carrying the selection marker of 3xP3-RFP were further validated by genomic PCR and sequencing. CRISPR generates a break in D/CG5893 and is replaced by cassette T2A-VP16AD-3XP3-RFP.

### Direct split-GAL4 insertion with CRISPR

For fer3, ems, and HLH4C, we inserted T2A-GAL4DBD directly in frame with the last coding exon instead of inserting it into an intron as a Trojan exon flanked by attP and FRT sites. The gRNA and entire donor region (a LHA-GAL4-DBD-RHA fragment, without attP and FRT sequences) were synthesized in pUC57_gw_OK2 and injected into vas-Cas9 flies (w[1118]; PBac(y[+mDint2]=vas-Cas9)VK00027) by Rainbow transgenics (Camarillo, CA). Transformed animals were crossed to flies carrying Tubulin-GAL4AD, UAS-TdTomato, and offspring was scored for TdTomato expression to identify positive lines. The expression pattern of the reporter served as a verification for correct editing events; no further verification was performed.

### Immunochemistry and data acquisition

Samples were dissected in phosphate buffered saline (PBS) and fixed with 2% paraformaldehyde in PBS for an hour at room temperature and then washed several times in PBS-TX (PBS with 1% Triton-X100) for a total of 20 min. Tissues were incubated with primary antibodies (Key Resources Table) for two to four hours at room temperature or overnight at 4 °C. After three to four rinses with PBS-TX to remove the primary antisera, tissues were washed with PBS-TX for an hour. After wash, tissues secondary antibodies were applied for 2 hr at room temperature or overnight at 4 °C. Tissues were washed again with PBS-TX for an hour and mounted in Vectashield or in DPX after dehydration through an ethanol series and clearing in xylene (Truman et al., 2004). Images were collected with 20 X or 40 X objectives using confocal microscopy. Images were processed with Image J/FIJI.

### Behavioral analysis

For optogenetic stimulation, we used standard food containing 0.2 mM all-trans retinal. As a light source for optogenetic activation, we used either white light coming from the gooseneck guide attached to the halogen light box or red light (Amazon-Chanzon, 50 W, Led chip, 620 nm - 625 nm / 3500 - 4000LM). Animal behaviors were recorded via a USB-based Basler Camera (acA640-750um) under continuous infrared light source (Amazon-DI20 IR Illuminator).
