# A switch in transcription and cell fate governs the onset of an epigenetically-deregulated tumor in Drosophila

## Authors

- Joana Torres<sup>1</sup> ([ORCID: 0000-0002-5651-4575](https://orcid.org/0000-0002-5651-4575))
- Remo Monti<sup>1</sup>
- Ariane L Moore<sup>1</sup>
- Makiko Seimiya<sup>1</sup>
- Yanrui Jiang<sup>1</sup>
- Niko Beerenwinkel<sup>1</sup> ([ORCID: 0000-0002-0573-6119](https://orcid.org/0000-0002-0573-6119))
- Christian Beisel<sup>1</sup>
- Jorge V Beira<sup>1</sup> ([ORCID: 0000-0002-2884-4964](https://orcid.org/0000-0002-2884-4964)) †
- Renato Paro<sup>1</sup> ([ORCID: 0000-0003-3308-2965](https://orcid.org/0000-0003-3308-2965)) †

### Affiliations

1. Department of Biosystems Science and Engineering ETH Zürich Basel Switzerland
2. Swiss Institute of Bioinformatics Basel Switzerland
3. Faculty of Science University of Basel Basel Switzerland

† Corresponding author

## Abstract

Tumor initiation is often linked to a loss of cellular identity. Transcriptional programs determining cellular identity are preserved by epigenetically-acting chromatin factors. Although such regulators are among the most frequently mutated genes in cancer, it is not well understood how an abnormal epigenetic condition contributes to tumor onset. In this work, we investigated the gene signature of tumors caused by disruption of the Drosophila epigenetic regulator, polyhomeotic (ph). In larval tissue ph mutant cells show a shift towards an embryonic-like signature. Using loss- and gain-of-function experiments we uncovered the embryonic transcription factor knirps (kni) as a new oncogene. The oncogenic potential of kni lies in its ability to activate JAK/STAT signaling and block differentiation. Conversely, tumor growth in ph mutant cells can be substantially reduced by overexpressing a differentiation factor. This demonstrates that epigenetically derailed tumor conditions can be reversed when targeting key players in the transcriptional network.

## Introduction

During development, epigenetic regulators are responsible for controlling and restraining cellular plasticity. This tight regulation allows cells to differentiate faithfully and heritably towards a specific fate (Roy and Hebrok, 2015; Wainwright and Scaffidi, 2017). An appropriate balance between proliferation and differentiation is fundamental and multiple regulatory layers of transcription factors and epigenetic regulators are employed to accomplish the underlying transcriptional control (Gonda and Ramsay, 2015; Piunti and Shilatifard, 2016).

Many epigenetic regulators are evolutionary conserved and among the most commonly mutated genes in human cancer (Piunti and Shilatifard, 2016). Disruption of epigenetic constraints leads to global reorganization of the epigenome and changes in transcriptional profiles, which might provide a cellular state permissive for tumorigenesis (Wainwright and Scaffidi, 2017). Indeed, disturbed transcriptional profiles and putative oncogenic transcriptional regulators have recently gained significance as better alternatives for therapeutic targets in comparison to signaling pathways. Transcription factors (TFs) are less prone to be bypassed by alternative mutational events, and their perturbation can affect several cancer hallmarks. In addition, due to the complexity of transcriptional networks, it is unlikely that one TF functioning as an oncogenic driver can be entirely replaced by another (Gonda and Ramsay, 2015). For these reasons it is fundamental to identify the core transcriptional networks defining cancer cell types, and target those regulators crucial for survival (Bonifer and Cockerill, 2015).

Epigenetic regulators involved in preserving cellular identity are composed of two classes of chromatin proteins, the Polycomb (PcG) and the Trithorax group (TrxG), whose complementary functions maintain the repressed and active gene expression state, respectively (Geisler and Paro, 2015). PcG proteins are organized into two basic complexes, Polycomb repressive complex 1 and 2 (PRC1 and PRC2) (Piunti and Shilatifard, 2016). One example of classical PcG targets are homeotic genes encoding Homeobox TFs, first identified in Drosophila and responsible for correct spatial body development in flies (Shah and Sukumar, 2010; Abate-Shen, 2002). The altered expression of Hox genes in human tumors suggests important roles for both oncogenesis and tumor suppression (Shah and Sukumar, 2010), which further hints towards an role for PcG proteins in oncogenesis.

The tumor suppressive role of PcG proteins, in particular PRC1 members in Drosophila imaginal discs, has been extensively investigated (Classen et al., 2009; Martinez et al., 2009). However, the effects on the transcriptional landscape after PRC1 deregulation in tumorigenesis has only recently started to be assessed (Bunker et al., 2015; Loubière et al., 2016). Here, we show that loss of Polyhomeotic (ph), a member of the PRC1 complex, in eye-antennal imaginal discs of larvae leads to a reprogramming of cellular identity towards an embryonic state and a concomitant loss of differentiation markers. Among the reactivated genes is knirps, an orphan nuclear hormone receptor. Depletion of knirps revealed its vital role in tumor maintenance, while misexpression showed its capacity to drive tumorigenesis in otherwise wild-type tissues. Tumors initiated by ph disruption or misexpression of knirps share features such as ectopic activation of JAK/STAT signaling and a differentiation block. We conclude that the embryonic TF knirps is an oncogene in eye-antennal imaginal discs and is crucial for the tumorigenic capacity of the epigenetic tumor under study. Additionally, we found that overexpressing a pro-neural TF leads to reduction of proliferation and suppression of the tumor phenotype.

## Results

ph505 mitotic mutant clones were generated using the Flp/FRT system, allowing for specific tumor growth within eye-antennal imaginal discs (from here on referred to as ph505-tumor). Mutant clones were fluorescently labeled with GFP, by using the mosaic analysis with a repressible cell marker (MARCM) system (Wu and Luo, 2006).

Reduced expression of Ph in the mutant clones compared to tissues carrying FRT19A (neutral) mitotic clones was observed (Figure 1—figure supplement 1A–B). Only a small number of larvae carrying ph505-tumors reached adulthood (Figure 1—figure supplement 1C). The majority of tumors arising in these epithelial tissues display disrupted cell polarity (Martinez et al., 2009), which was confirmed using the cell adhesion marker Armadillo (Figure 1—figure supplement 1D–E). Additionally, we observed ectopic expression of Matrix metalloprotease 1 (MMP1) (Figure 1—figure supplement 1F–G), which is required for matrix degradation and the invasive potential of tumor cells (Christofi and Apidianakis, 2013; Uhlirova and Bohmann, 2006).

The tumorigenic capacity of PcG mutant tissues has been previously reported (Classen et al., 2009; Martinez et al., 2009). Here we show for the first time that neoplastic growth of ph505 mutant clones in eye-antennal imaginal discs can be rescued by wild-type ph (via UAS-ph) co-expression. The resulting tissues with restored Ph levels harbored smaller clones compared to the tissues containing ph505 clones (Figure 1—figure supplement 1H–I). To better quantify changes of tumor volume in these tissues we developed an image analysis pipeline (see Materials and methods). This enabled us to concomitantly measure the volume of mutant clones (GFP-labeled) as well as the volume of the tissue. We found that in tissues with ph505 clones 46% of the disc was composed of tumor cells, while in the rescue experiment this ratio was reduced to only 7% (Figure 1—figure supplement 1K–N). Consistent with these observations, a reduced number of larvae carrying ph505-tumors reached adulthood (eclosion rate <20%). In contrast the eclosion rate of ph505, UAS-ph pupae (97%) was similar to control flies (99%) (Figure 1—figure supplement 1J).

Overall, these results show that the tumorigenic phenotype of ph505 tissues is primarily due to the loss of ph since it can be rescued by the expression of the wild-type protein. We had shown previously that tumors with impaired ph do not accumulate genetic instabilities, even when cultivated for prolonged time in adult hosts (Sievers et al., 2014). Hence, the observed neoplastic behavior can be solely restricted to the loss of the silencer ph and the ensuing deregulation of the transcriptional state described below.

### ph505-tumor cells exhibit global gene expression deregulation

To better understand the molecular consequences of polyhomeotic loss-of-function in vivo, we analyzed the transcriptome of ph505-tumor cells by RNA sequencing (RNA-seq). We used fluorescence activated cell sorting (FACS) of dissociated eye-antennal imaginal discs to separate GFP-labeled tumor cells from surrounding unlabeled and non-mutant cells (Martinez et al., 2009; Dutta et al., 2013; Harzer et al., 2013). This proved to be an essential step for an accurate diversification of the tumor transcriptome. Transcriptome analysis showed substantial deregulation of gene expression in mutant cells compared to neighboring non-mutant cells. We identified 1337 differentially expressed genes (Benjamini adjusted p-value, padj. <0.01), with 275 genes being upregulated in ph505-tumor cells (Figure 1A, Figure 1—figure supplement 2A, Figure 1—source data 1). Furthermore, gene set enrichment analysis revealed that neurogenesis-related genes were mainly downregulated in ph505-tumor cells, while genes regulating transcription were upregulated (Figure 1B). Since PcG target genes encode crucial developmental regulators, such as TFs (Simon and Kingston, 2009), our expression data corroborates its impaired function. Moreover, we observed deregulation of genes involved in tissue development (e.g., GO-terms for genital disc development, imaginal disc development) and enrichment for TFs among the upregulated genes (GO-term sequence-specific DNA binding transcription factor activity) (Figure 1B, Figure 1—source data 2). The observed global modulation of transcription output is in agreement with PcG proteins constituting a global regulatory system (Simon and Kingston, 2009).

![Figure 1.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig1-v1.jpg)

**Figure 1.:** RNA-sequencing was performed in FACS-sorted ph505 tissue samples. Gene expression in tumor cells (GFP+) was compared with surrounding wild-type cells (GFP-) from the same pool of eye-antennal tissues. Volcano plot in (A) shows 1337 differentially expressed genes: 1062 genes are downregulated (pink) and 275 are upregulated (green) (padj ≤0.01, Benjamini). Names of 6 genes are provided in the volcano plot: cad, eve, kni, eya, elav, ato. Representation of selected Gene Ontology (GO) terms that were found enriched (for details please check Figure 1—source data 2) (B). Green/Pink light bars correspond to the expected number of genes for each category, Green/Pink dark bars correspond to the number of observed hits in our analysis. Black bars correspond to the log10(padj). Pink, downregulated genes; green, upregulated genes. Heatmap and respective dendogram obtained for clustering analysis with 83 samples (Figure 1—sources data 3 and 4) (C), showing tumor samples clustering together with early embryos. ph505-tumor samples in black (**), control samples (#) in grey and other tumor samples (brat- and RASV12/Scrib- tumors) are highlighted below the clustering. Embryonic transcription factor Even-skipped (Eve) is not detected in FRT neutral clones (D) but is ectopically expressed in ph505 clones (E). Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green; antibody staining, magenta). See also Figure 1—figure supplements 1–4 and Figure 1—source datas 1–4.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Mitotic clones were generated by using eyFlp/FRT and MARCM systems, allowing for generation of GFP-labeled clones within eye-antennal imaginal discs. Ph expression in FRT19A control (A–A’’’) and in ph505 (B–B’’’) eye-antennal imaginal discs, showing a mutant clone specific reduction of Ph (B’–B’’). Eclosion rate for FRT19A and ph505 larvae (C). Armadillo (Arm) adherent junction normal protein expression in eye-antennal discs bearing neutral clones D–D’’. Loss of Arm is observed specifically in tumor clones (E–E’’). Dashed rectangles (D’ and E’) show the position of the Z-cross section in D1-D2 and E1-E2, respectively. Matrix metalloproteinase 1 (MMP1) expression in eye-antennal tissues is shown in F–F’’). MMP1 is recurrently expressed in neoplastic context, and its ectopic expression is specifically observed in tumor clones (G–G’’ and one middle Z-section at higher magnification G1–G1’’). Eye-antennal discs expressing UAS-ph in the context of FRT19A neutral clones (H–H’) and in ph505 mutant background (I–I’). Expression of UAS-ph per se does not change eclosion rate in a FRT19A neutral clones background (J). Eclosion rate for all conditions is shown (J). Number of larvae analyzed (J): FRT19A N = 163; FRT19A, UAS-ph N = 137; ph505 N = 784; ph505, UAS-ph N = 48. Rescue of phenotype by ectopic expression of ph is shown (J–K). Percentage of tumor volume (K), average tumor volume (L), tissue size (M) and number of clones per tissue (N) in ph505 and ph505, UAS-ph conditions. Percentage of tumor volume is the sum of the volume of all GFP+ clones in a tissue divided by the tissue size (volume of DAPI). Number of tissues analyzed (K–N): ph505 N = 50; ph505, UAS-ph N = 23. Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue, except where otherwise stated (DAPI, cyan; GFP MARCM clones, green; antibody staining, magenta). Data (C, J–N) are represented as mean ± SD. Statistics: ****p<0.0001.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** Heatmap of normalized expression levels of 1337 differentially expressed genes across tumor and control samples (A). A total of 1337 genes are differentially expressed in tumor samples in comparison to control cells (p adj. <0.01). Clustering analysis (represented with a dendogram) shows a clear separation between the seven tumor samples and four control samples analyzed. (B) Heatmap and respective dendograms obtained from clustering analysis of other samples by using the TF-signature of ph505-tumors. Details regarding sample and gene names are provided in the heatmap. See also Figure 1—source datas 1, 3 and 4.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** Normal pattern (A) expression of ELAV retinal cell marker is interrupted in ph505 clones (B). Eyes absent (Eya) and Homothorax (Hth) protein expression in FRT neutral (C, E) and ph505 (D, F) clones. Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green; antibody staining, magenta).

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** Embryonic TF Abdominal-B (Abd-B) and Caudal (Cad) are ectopically expressed in ph505 clones (B–D) in comparison to FRT19A control tissues (A–C). Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green; antibody staining, magenta).

### Tumor transcription factor signature reveals loss of larval cell identity and acquisition of embryonic features

TFs are essential to define cell types and are among the main targets of PcG silencing (Simon and Kingston, 2009). As such, we decided to focus on the fraction of differentially expressed TF-encoding genes, due also to the enrichment of genes in this category in our RNA-seq dataset. We evaluated which upregulated TFs, and thus the primary response to the ph knock-out, could be contributing to the overall deregulation of gene expression observed. Employing the iRegulon tool (Janky et al., 2014), predictions based on motif enrichment revealed caudal, grain and knirps (direct Ph targets in eye discs [Loubière et al., 2016]) as TFs putatively responsible for all differentially expressed genes in our RNA-seq dataset. To further reveal the transcriptional identity of ph505-tumor cells, we integrated available datasets from the Gene Expression Omnibus (Edgar et al., 2002) and compared the gene expression signature of ph505-tumors with other tissues and/or developmental stages of Drosophila. In total, 83 samples including different tissues and cell types (namely ovaries, larval brain, adult head, wing disc, eye-antennal disc, larval neurons and larval neuroblasts) and developmental stages (embryo, larva and pupa) were considered for the analysis (Figure 1—source data 3). Specifically, we compared 124 differentially expressed genes involved in transcriptional regulation (GO0006355) (Figure 1—source data 4). Strikingly, hierarchical clustering of 83 transcriptome samples showed that ph505-tumor cells clustered close to samples from early embryonic developmental stages (Figure 1C and Figure 1—figure supplement 2B). As expected, our RNA-seq control samples (neighboring unlabeled cells) clustered with wild-type eye-antennal imaginal disc transcriptomes. This result might reflect the re-establishment of an earlier developmental program in ph505-tumors as a consequence of a reprogrammed epigenomic state. Additionally, this is not a general feature shared by all tumors, as depicted by other tumor types (i.e. brat [Jüschke et al., 2013] and RasV12/scrib- tumors [Atkins et al., 2016]) not clustering with embryos.

We hypothesize that the clustering of ph505-tumor cells with early embryos was not only the result of the ectopic expression of embryonic TFs in the ph505-tumor cells, but also due to reduced expression of the TFs, which characterize differentiated tissues. Downregulation of neurogenesis-related genes suggests that these tumor cells may be unable to differentiate, losing cell fate markers and their normally established identity. We confirmed the downregulation of neurogenesis-related markers at the protein level for ELAV (Embryonic Lethal Abnormal Vision), which is normally expressed in the differentiated neuronal cells that make up the eye imaginal disc (Figure 1—figure supplement 3A–B) and for Eya (Eyes absent, Figure 1—figure supplement 3C–D). This supports previous findings that suggested that neoplastic Drosophila epithelial cells reverse their developmental commitments and switch to primitive cell states (Khan et al., 2013). In this particular report, the switch in the eye primordium was shown to be Homothorax (Hth)-dependent (Khan et al., 2013). Conversely, in our RNA-seq dataset hth was downregulated and at the protein level we confirmed that Hth is not ectopically expressed in the ph505 clones (Figure 1—figure supplement 2E–F). Thus, our study reveals that ph505-tumors do not depend upon ectopic expression of Hth to keep cells in a non-differentiated state and support neoplastic growth.

The similarity of the ph505-tumor TF signature with Drosophila early embryos was reinforced by confirmation of the presence of embryonic-TF misexpression across tumor-tissue samples. We performed immunostaining for additional embryonic TFs, namely Even-skipped, Abdominal-B and Caudal, and observed ectopic expression of these proteins specifically in mutant clones (Figure 1D–E and Figure 1—figure supplement 3A–D). Overall, these results suggest that ph505-tumor cells previously committed to a neurogenesis-related path switch their cell fate as they fail to differentiate during the process of tumorigenesis due to the modulation of the transcriptional regulatory program of the cells.

### TFs as key regulators of tumorigenesis – candidate-hit validation in vivo

In order to pinpoint key regulators of tumorigenesis in ph505-tumors, we performed an in vivo screen for a subset of selected candidates. Among all the TFs upregulated in ph505-tumor cells, we chose, based on literature search, 24 to assess their importance in promoting tumorigenic potential in these cells. Our approach to test the ability of candidate genes playing a key role in ph505-tumorigenesis was to combine generation of ph505-tumor clones with RNAi-mediated knock-down (KD) of a target of interest within these clones. We compared effects of RNAi to the baseline ph505 neoplastic phenotype and observed that some RNAi lines targeting TFs (in ph505 clones) resulted in a strong increase in viability (close to 90–100%, for example cad, drm, kni, bgcn), while others did not change or only slightly changed pupal viability (Figure 2A). We further characterized 6 RNAi lines: crocodile (croc), lateral muscles scarcer (lms), caudal (cad), drumstick (drm), knirps (kni) and benign gonial cell neoplasm (bgcn) (Figure 2B–H), which showed significant differences in eclosion rate in comparison to flies carrying ph505 clones (Figure 2B and Figure 2—figure supplement 1A). The eclosion rate for three of these perturbations (drm-, kni- and bgcn-KD) reached similar levels as control flies (carrying FRT19A neutral clones) and rescue experiment (ph505, UAS-ph). By quantifying tumor volumes relative to tissue size of the six above-mentioned perturbations, we observed that only cad-, drm-, kni- and bgcn-KD showed a significant difference compared to the baseline of 46% tumor volume in the ph505 condition (14, 13, 5 and 14% tumor volume, respectively). In addition, the two perturbations (croc- and lms-KD) that did not show a significant effect on tumor volume were also those with less remarkable differences in eclosion rate (Figure 2B and Figure 2—figure supplement 1B–D). These results suggest that higher eclosion rate is a good approximation for decreased tumor volume. Furthermore, the tissue volume of the eye-antennal imaginal disc in the drm-, kni- and bgcn-KD conditions was closer to the control tissue volume than the ph505 condition (Figure 2—figure supplement 1C).

![Figure 2.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig2-v1.jpg)

**Figure 2.:** Eclosion rates (%) for FRT19A control, ph505 and for specific KD in ph505 background (ph505 +UAS RNAi). Fly stocks carrying RNAi constructs were used for the KD of 24 TFs upregulated in ph505-tumor cells (A). Dashed line represents the mean eclosion rate for ph505 larvae. Number of larvae analyzed: FRT19A N = 163; ph505 N = 784; ph505, UAS-ph N = 48; for each TF-KD in ph505 background: btd- N = 329, grn- N = 256, vvl- N = 250, odd- N = 108, Dr- N = 96, Sox100b- N = 304, Kr- N = 309, gsc- N = 177, fkh- N = 231,pb- N = 110, Doc1- N = 337, Doc2- N = 128, Doc3- N = 297, AbdA- N = 119, AbdB- N = 129, nub- N = 216, tin- N = 54, eve- N-117, croc- N = 355, lms- N = 58, cad- N = 137, drm- N116, kni- N = 340, bgcn- N = 158. Targets whose KD induced a significantly different eclosion rate compared with ph505 were further characterized at the tumor volume level (B). Number of tissues analyzed per condition: ph505 N = 50; ph505, UAS-ph N = 23; ph505, croc-KD N = 26; ph505, lms-KD N = 29; ph505, cad-KD N = 30; ph505, drm-KD N = 33; ph505, kni-KD N = 35; ph505, bgcn-KD N = 28. Percentage of tumor volume is significantly reduced in 4 out of 6 perturbations compared with ph505 alone (46%): 14% in ph505, cad-KD; 13% in ph505, drm-KD; 5% in ph505, kni-KD; and 14% in ph505, bgcn-KD. ph505, UAS-ph condition leads to reduction of tumor volume to 7% and is shown here as a control of the rescue phenotype. Examples of eye-antennal imaginal discs from six different genotypes used for quantification of tumor volume (C–H). Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green). Data (A–B) are represented as mean ± SD. Statistics: ****p<0.0001; ***p<0.001; *p<0.05. See also Figure 2—figure supplement 1 and 2.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Example of eye-antennal imaginal disc carrying ph505 cells used for quantification of tumor volume (A). Average tumor volume (µm3) (B), tissue volume (µm3) (C) and number of clones per tissue (D) for the 6 RNAi perturbations in a ph505 background are presented. Number of tissues analyzed per condition (B–D): ph505 N = 50; ph505, croc-KD N = 26; ph505, lms-KD N = 29; ph505, cad-KD N = 30; ph505, drm-KD N = 33; ph505, kni-KD N = 35; ph505, bgcn-KD N = 28. In (C) FRT19A neutral clones tissue size is also included (N = 32). Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green). Data (B–D) are represented as mean ± SD. Statistics: ****p<0.0001; **p<0.01.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Representative adult eyes of 4 different genotypes: FRT19A neutral clones (A), FRT19A, kni-KD (B), ph505 (C) and ph505, kni-KD (D). ELAV protein expression in ph505, kni-KD tissues (E). Higher magnification inset is shown in E’’’. Percentage of tumor volume (F), average tumor volume (µm3) (G), tissue volume (µm3) (H) and number of clones per tissue (I) for the KD of knirps with two different RNAi constructs in a ph505 background. Number of tissues analyzed per condition (F–I): ph505 N = 50; ph505, kni-KD N = 35, ph505, kni-KD(2) N = 25. Reduction of tumor volume to 5% and 14% for ph505, kni-KD-(1) and -(2), respectively. Eclosion rate of ph505, kni-KD (J). Number of larvae analyzed: FRT19A N = 163; ph505 N = 784; ph505, kni-KD N = 340, ph505, kni-KD(2) N = 112. Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green, antibody staining, magenta). Data (F–J) are represented as mean ± SD. Statistics: ****p<0.0001; *p<0.05.

From all the RNAi conditions tested, kni-KD in ph505 mutant clones showed the most striking decrease in tumor volume (9.2 fold decrease), similar to the rescue experiment (ph505, UAS-ph) (Figure 2B). Additionally, the phenotype of adult eyes of this genotype suggests a recovery of the differentiation program (Figure 2—figure supplement 2A–D). This is supported by immunostaining against ELAV showing that it is no longer disrupted when expression of kni is blocked in ph505 (Figure 2—figure supplement 2E). Altogether, this shows that the differentiation block observed in ph505-tumors is prevented upon reducing the level of knirps expression by RNAi KD. We confirmed that a second, independent RNAi line against kni also led to a significant decrease of tumor volume (14% of tumor volume vs. 46% in ph505) and an increase in eclosion rate (85%) (Figure 2—figure supplement 2F–J). We can thus minimize the chance that the effects observed using either kni-RNAi were due to off-target effects.

### knirps-KD reduces ph505 tumorigenic capacity

We characterized the tumorigenic potential of ph505-tumors and ph505, kni-KD by conducting transplantation assays (Rossi and Gonzalez, 2015) of these tissues into the abdomen of adult host flies (Figure 3A–D). In the case of the ph505-tumors the percentage of tumor-bearing hosts increased from 40% to 60%, from the first week to subsequent weeks after transplantation indicating hyperproliferation of the transplanted tissues (Figure 3A). The tumorigenic potential of ph505-transplanted tissue was already detected on day seven after transplantation (Figure 3B). By contrast, when transplanting ph505, kni-KD clones we did not observe any tumors in the host flies within the first three weeks. Even after up to 5 weeks post-transplantation, we could only find a single fly with GFP+ tissue overgrowth (Figure 3C–D). Our data demonstrate that the TF Knirps plays a crucial role in tumorigenesis of ph505-tumors given that kni-KD in these tissues not only led to a reduction of tumor volume but also the remaining clones were not able to proliferate in the host fly abdomen.

![Figure 3.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig3-v1.jpg)

**Figure 3.:** Female host shows abdominal tumor growth one week after transplantation (B–B’). Percentage of ph505, kni-KD tumor-bearing hosts is shown over time and ranges from 0% to 3% (C). One single host with a tumor was observed on week 4 (C). Brightfield (D) and fluorescence images (D’) of the tumor-bearing host on day 35. ‘N’ represents the total number of hosts analyzed per time point. Green bars represent the percentage of hosts with visible tumors, while grey bars represent the percentage of hosts without tumors. Levels of apoptosis (Dcp-1) are shown for ph505, kni-KD (E–E’) and ph505, kni-KD, UAS-p35 (F–F’). Higher magnification insets are shown in E’ and F’. Percentage of tumor volume (G). Number of tissues analyzed per condition: ph505 N = 50; ph505, kni-KD N = 35; ph505, kni-KD, UAS-p35 N = 27. Percentage of tumor volume is significantly reduced in the two conditions compared with ph505 alone (46%): 5% in ph505, kni-KD; and 6% in ph505, kni-KD, UAS-p35. Eclosion rate for same conditions (H). Number of larvae analyzed: ph505 N = 784; ph505, kni-KD N = 340; ph505, kni-KD, UAS-p35 N = 48. Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green). Data (G–H) are represented as mean ± SD. Statistics: ****p<0.0001; *p<0.05. See also Figure 3—figure supplements 1

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Levels of apoptosis (Dcp-1) are shown for FRT19A, kni-KD (A–A’) and FRT19A, kni-KD, UAS-p35 (B–B’). Higher magnification insets are shown in A’ and B’. Eclosion rates for the same conditions (C). Number of larvae analyzed: FRT19A N = 163; FRT19A, kni-KD N = 219; FRT19A, kni-KD, UAS-p35 N = 75. Average tumor volume (µm3) (D), tissue volume (µm3) (E) and number of clones per tissue (F) for the blockage of apoptosis (via UAS-p35) in ph505, kni-kD clones. Number of tissues analyzed per condition (D–F): ph505 N = 50; ph505, kni-KD N = 35; ph505, kni-KD, UAS-p35 N = 27. Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green; antibody staining, magenta). Data (C–F) are represented as mean ± SD. Statistics: ****p<0.0001, ***p<0.001.

Evasion of apoptosis is one of the hallmarks of cancer (Hanahan and Weinberg, 2000). As we observed a significant reduction of tumor volume upon depleting kni in ph505 mutant cells, we hypothesized that kni-KD could trigger cell death of tumor cells. We blocked apoptosis within mutant clones (via expression of anti-apoptotic protein p35 [Hay et al., 1994]). Levels of apoptosis as assessed by immunostaining against Death caspase-1 (Dcp-1) confirmed a decrease in apoptosis in tissues where p35 was expressed in ph505, kni-KD clones (Figure 3E–F and Figure 3—figure supplement 1A–B). However, we observed that blocking apoptosis in ph505, kni-KD clones was not sufficient to revert the anti-oncogenic effects of kni-KD (Figure 3G–H and Figure 3—figure supplement 1C–F). Furthermore, the tumor volume of ph505, kni-KD, UAS-p35 was similar to ph505, kni-KD (Figure 3G and Figure 3—figure supplement 1D–F). We also tested the effect of this particular RNAi line in the context of neutral clones generated with the same driver as for ph505-tumors. These FRT19A, kni-KD flies showed neither difference in eclosion rate nor in the adult eye phenotype, compared to control flies (Figure 3E–F and Figure 3—figure supplement 1C). This suggests that the RNAi line targeting kni does not per se affect eye-antennal imaginal disc development.

### Ectopic expression of knirps is sufficient to drive tumorigenesis

Ectopic expression of cell fate-specifying TFs was recently shown to lead to the formation of epithelial cysts (Bielmeier et al., 2016). Cyst formation in wing and eye imaginal discs represents a response to cell fate mis-specification, compromising tissue integrity and potentially promoting precancerous lesions. We thus assessed the effect of ectopic kni expression in eye-antennal imaginal discs by generating mitotic clones using again the eyFlp system. We observed that FRT19A clones expressing kni (Figure 4A) displayed a more pronounced round shape in comparison to the notchy-shape of FRT19A neutral clones (Figure 1—figure supplement 1A). Additionally, ectopic kni expression compromised the viability of the flies, evidenced by an eclosion rate of only 35% (Figure 4B), and the defective development of the adult eye structures (Figure 4C). Furthermore, we confirmed that ectopic expression of kni leads to the formation of cysts (Figure 4D) and thus interferes with epithelial polarity (Figure 4D and Figure 5—figure supplement 1A).

![Figure 4.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig4-v1.jpg)

**Figure 4.:** Ectopic expression of knirps in eye-antennal imaginal discs shows a distinct pattern of clones (A–A’). Eclosion rate (B) for FRT19A and FRT19A, UAS-Kni. Ectopic expression of kni in these particular tissues compromises the viability of the flies. Number of larvae analyzed: FRT19A N = 163; FRT19A, UAS-Kni N = 441. Ectopic expression of knirps in eye-antennal discs compromises normal eye development as assessed by adult eye structures (C). Formation of cysts in tissues carrying ectopic expression of kni (D–D’), highlighted by middle sections (five middle Z-stacks) with Phalloidin staining (D’’). Insets (i and ii) for orthogonal views (YZ) are shown and cutting plane is depicted in (D’’–D’’’). Assays of transplantation were performed with tissues carrying ectopic expression of kni (E). Tumor-bearing hosts were observed 3 weeks after transplantation (<25% of hosts). In week 5, almost 50% of the hosts that survived carried GFP+-tumor tissue. Blue bars represent the percentage of hosts with tumors, while grey bars show percentage of hosts without tumor. Tumor-bearing host on week five is shown in (F) and tumor fluorescence in (F’). Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue, except where otherwise stated (DAPI, cyan; GFP MARCM clones, green; antibody staining, magenta). Data (B) are represented as mean ± SD. Statistics: ****p<0.0001. See also Figure 5—figure supplement 1.

To test if ectopic expression of kni alone is sufficient to drive tumorigenesis we conducted transplantations of eye-antennal imaginal disc tissues ectopically expressing kni. We observed that knirps is sufficient to generate tumors in the host flies, visible 3 weeks after transplantation (ranging from 15–50%, from week 3 to 5 after transplantation respectively) (Figure 4E–F). Our data suggest that ectopic expression of knirps interferes with the normal course of development and that knirps is a new oncogene, possibly acting in a context/tissue-dependent manner.

### Knirps activates JAK/STAT pathway and blocks cellular differentiation

Since knirps-KD alone was sufficient to reduce the tumorigenic potential of ph505-tumors, we hypothesized that some features of clones ectopically expressing knirps in a wild-type context could resemble ph505-tumor clones. We therefore evaluated the activation of signaling pathways in this context. We observed that of the JNK, JAK/STAT and Notch signaling pathways (all are activated in ph505-tumors [Classen et al., 2009; Martinez et al., 2009; Beira et al., 2018]), only JAK/STAT was ectopically activated, particularly in knirps cyst-like clones (Figure 5A–C). This observation suggests that ectopic expression of knirps alone is sufficient to activate the JAK/STAT pathway in mitotic clones. Hence, ectopic activation of the other signaling pathways in ph505-tumors is likely attributable to other factors regulated by Ph and independent of knirps.

![Figure 5.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig5-v1.jpg)

**Figure 5.:** Activity of JAK/STAT, JNK and Notch signaling pathways in the context of kni-ectopic expression in eye-antennal discs was assessed by evaluating the expression of the respective activity reporters: 10x STAT-GFP (A, RFP MARCM clones in red, JAK/STAT reporter in green), TRE-DsRed (B, GFP MARCM clones in green, JNK reporter in red) and NRE-EGFP (C, RFP MARCM clones in red, Notch reporter in green). Ectopic expression of STAT is specifically observed in kni cyst-like clones (A’–A’’’). JNK and Notch pathways are not ectopically activated in UAS-Kni clones. Differentiation of eye progenitors is compromised as observed by ELAV and Eya protein expression (D–E). Normal ELAV and Eya protein expression is interrupted in the presence of Kni ectopic clones, particularly in cysts (D’’’ and E’’’), without ectopic expression of Hth (F). Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green, unless otherwise stated; antibody staining, magenta). See also Figure 5—figure supplement 1.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Disruption of Armadillo protein expression is observed in UAS-Kni expressing clones (A). ELAV protein expression is interrupted in ph505, dome.∆CYT (blockage of JAK/STAT pathway in ph505 background) clones (B). These particular larvae have also an increased eclosion rate in comparison to ph505-tumors (C). Number of larvae analyzed: FRT19A N = 163; ph505 N = 784; ph505, dome.∆CYT N = 290. Eye structures from adults carrying ph505, dome.∆CYT genotypes (D). Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green; antibody staining, magenta). Data (C) are represented as mean ± SD. Statistics: ****p<0.0001.

In light of the compromised eye development seen in kni-ectopic flies, and suggestions that the JAK/STAT pathway needs to be switched off to allow differentiation (Amoyel and Bach, 2012), we investigated the expression of a number of neurogenesis-related markers in kni-ectopic eye-antennal imaginal discs. Similarly to what we observed with ph505 clones, ELAV expression was disrupted in kni-expressing cyst-like structures, as shown in Figure 5D, as well as Eya (Figure 5E), without ectopic activation of Hth (Figure 5F). These observations are thus in agreement with the hypothesis that knirps alone is sufficient to initiate tumorigenesis.

Our data argue in favor of a role for JAK/STAT in contributing to the differentiation block in ph505 and kni-ectopic tumors. We decided to block this pathway in ph505-tumors (ph505, dome∆CYT) and examine cellular differentiation in these eye-antennal imaginal discs. Upon blocking JAK/STAT in ph505-tumors, we observed that ELAV expression is re-established almost to a normal situation, even in the presence of clones (Figure 5—figure supplement 1B in comparison to Figure 1—figure supplement 3B). Moreover, the viability of these flies is increased, close to normal levels (Figure 5—figure supplement 1C, eclosion rate 85%) and some adult flies presented eye structures similar to wt individuals Figure 5—figure supplement 1D).

### Overexpression of a pro-neural TF in ph505-clones suppresses the tumorigenic phenotype

Blockage of normal differentiation appears to be a common feature between ph505 and kni-ectopic tumors in eye tissues, suggesting that kni expression in the ph505-tumors contributes to the differentiation defects observed (Figure 1—figure supplement 3 and Figure 2—figure supplement 2C). Hence, we expected that apart from the knock-down of an embryonic TF with tumorigenic capacity, forcing differentiation of tumor cells could restrain the tumorigenic phenotype.

Atonal (ato), encoding a pro-neural TF, was previously shown to have an anti-oncogenic role in the fly retina, where it instructs tissue differentiation (Bossuyt et al., 2009). Notably, ato is also among our downregulated set of genes (padj. <0.01). We ectopically expressed ato in ph505 clones, which led to the rescue of the phenotype by a reduction of the tumor volume from 46% baseline to 3% and an increase in the eclosion rate from 12% to 84% (Figure 6A–C and Figure 6—figure supplement 1A–E). Hence, expression of ato in ph505 clones was sufficient to restore the normal pattern of differentiation of this tissue, as confirmed by the expression of ELAV (Figure 6D and Figure 6—figure supplement 1G). Indeed, also the eye phenotype of the hatched flies resembled the phenotype of wild-type flies (Figure 6—figure supplement 1F). We then asked whether these effects can be attributed to the capacity of atonal in preventing proliferation, as previously shown in a different tumor model (Bossuyt et al., 2009). To test this hypothesis, we assessed levels of phospho-histone H3 (pH3) as a measure of proliferation (Figure 6E–G and Figure 6—figure supplement 2). Quantitative analysis showed an overall increase in proliferation levels in ph505-tumor tissues in comparison to control tissues. This was largely due to an increase of proliferative cells outside of ph505 clones (Figure 6—figure supplement 2C). The analysis also showed a decrease in pH3+ cells inside clones co-expressing ph505 and atonal (in comparison to ph505 clones) (Figure 6G). Thus, atonal antagonizes ph tumor growth by counterbalancing proliferation, ultimately leading to a reduction of tumor burden and to a normal eye differentiation pattern.

![Figure 6.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig6-v1.jpg)

**Figure 6.:** Forcing differentiation of ph505 cells by ectopically expressing pro-neural TF atonal leads to a reduction of tumor volume (A–B). Number of tissues analyzed: ph505 N = 50; ph505, UAS-ato N = 23. On average, tumor volume is reduced to 3% of the eye-antennal imaginal disc volume (B). Eclosion rate of larvae of ph505, UAS-ato genotype is increased and comparable to FRT19A neutral clones’ genotype (C). Number of larvae analyzed: ph505 N = 784; ph505, UAS-ato N = 95. ELAV protein expression in ph505 clones expressing UAS-ato (D). Proliferation levels (phospho-histone H3, pH3) upon overexpressing ato in ph505-cells (E–F). Quantitative analysis of pH3+ cell numbers in ph505 and ph505, UAS-ato (G). These values were normalized to the respective volumes, such as ‘whole tissue’ data was normalized to the total tissue volume, ‘inside clones’ normalized to volume taken by GFP+ clones and ‘outside clones’ normalized to the volume of tissue that is GFP-. Number of tissues analyzed: ph505 N = 19; ph505, UAS-ato N = 18. Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green; antibody staining, magenta). Data (B–C, G) are represented as mean ± SD. Statistics: ****p<0.0001, ***p<0.001, *p<0.05. See also Figure 6—figure supplements 1–2.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Ectopic expression of pro-neural TF atonal in FRT19A neutral clones (A). Average tumor volume (µm3) (B), tissue volume (µm3) (C) and number of clones per tissue (D) for the ectopic expression of ato in a ph505 background. Number of tissues analyzed per condition (B–D): ph505 N = 50; ph505, UAS-ato N = 95. Eclosion rate of larvae carrying FRT19A, UAS-ato (E). Number of larvae analyzed: FRT19A N = 163; FRT19A, UAS-ato N = 87. Examples of eye adult structures of ectopic expression of ato in ph505 background (F). ELAV protein expression in FRT19A, UAS-ato tissues (G). Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green; antibody staining, magenta). Data (B–E) are represented as mean ± SD. Statistics: ****p<0.0001.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/32697/elife-32697-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** Proliferation levels (phospho-histone H3, pH3) upon overexpressing ato in control tissues (A–B). Quantitative analysis of pH3+ cell numbers in FRT19A; FRT19A, UAS-ato; ph505 and ph505, UAS-ato (C). These values were normalized to the respective volumes, such as ‘whole tissue’ data was normalized to the total tissue volume, ‘inside clones’ normalized to volume taken by GFP+ clones and ‘outside clones’ normalized to the volume of tissue that is GFP-. Number of tissues analyzed: FRT19A N = 14, FRT19A, UAS-ato N = 19; ph505 N = 19; ph505, UAS-ato N = 18. Scale bar corresponds to 100 µm. All microscope images are a maximum intensity projection of all z-stacks acquired for the tissue (DAPI, cyan; GFP MARCM clones, green; antibody staining, magenta). Data (C) are represented as mean ± SD. Statistics: ***p<0.001, **p<0.01, *p<0.05.

## Discussion

### Loss of an epigenetic regulator leads to acquisition of an embryonic and oncogenic gene signature

With the analysis of a ph mutant transcriptome we highlight the complexity of disrupting global gene expression programs and, with that, newly established transcriptional dependencies. Previous approaches of generating PcG-negative transcriptomes investigated gene expression of mutant cells that were deprived from contact with non-mutant cells (using the cell lethal system), which was then compared with wild-type discs composed of neutral clones (Loubière et al., 2016; Bunker et al., 2015). In contrast, we set out to compare ph505 mutant cells with their surrounding wild-type cells to gain potential additional information by taking into account non-autonomous growth effects previously reported (Feng et al., 2011). The RNA-seq dataset presented here reveals enrichment for TFs in the upregulated gene set. It also indicates that tumor cells fail to differentiate, supported by the downregulation of neural-cell fate markers characteristic of this tissue and by the upregulation of embryonic TFs. This is also highlighted by the clustering of the TF-signature of ph505-tumors with embryonic stages of Drosophila development. Moreover, we also found several Hox genes in our set of upregulated genes (e.g., Antp, Ubx, Abd-A, Abd-B), which are classical embryonic PcG-targets shown to be important in oncogenesis.

Although not regarded as a traditional hallmark of cancer (Hanahan and Weinberg, 2000), a key event in tumorigenesis is the perturbation of normal cell fate (Gonda and Ramsay, 2015). Re-expression of particular embryonic genes in an aberrant spatial-temporal pattern could contribute to oncogenesis by maintenance of a more embryonic state through the activation of anti-apoptotic pathways or suppression of differentiation (Shah and Sukumar, 2010). For example, re-establishment of an earlier developmental program has been proposed in human pediatric gliomas that frequently have mutations in histone H3 lysine 27 (H3K27M) and compromised PRC2 function (Funato et al., 2014; Wainwright and Scaffidi, 2017).

Since several classic TFs with important functions during embryogenesis are among the upregulated genes in the ph505-tumor transcriptome, we subsequently blocked their expression and showed for some TFs their potential to rescue the ph knock-out phenotype and reduce tumor growth. Quantitative measurements of tumor volume in various conditions ensured the reproducibility of the data, excluding an observer bias. The observed effects of TF-KD on eclosion rate and tumor volume did not necessarily correlate with the genes that are direct targets of Ph silencing in eye discs. This is illustrated for example by the strong effects of bgcn-KD that has not been identified as a direct Ph target (Loubière et al., 2016).

These observations on TFs are particularly important since transcription has a direct influence on the balance between proliferation and differentiation. Furthermore, when transcriptional regulators (TFs, co-regulators or epigenetic modifiers) are misregulated, differentiation is blocked and pre-cancer cells can proliferate (Gonda and Ramsay, 2015).

### An embryonic nuclear hormone receptor as new oncogene

kni is a gap gene involved in the subdivision of the embryo anterior-posterior axis that can function as an activator (Langeland et al., 1994) or a repressor (Pankratz et al., 1990). Besides its classic function in embryonic development, kni is subsequently also required for vein formation in wing imaginal discs (Lunde et al., 2003). We show that KD of knirps in ph505-tumors is sufficient to reduce tumor volume by 90%. It also reduces the tumorigenic capacity of ph505-tumors, as assessed by a transplantation assay. Misexpression of TFs in imaginal discs and formation of cysts has been suggested to be an indicator of precancerous lesions (Bielmeier et al., 2016). Here we show that ectopic expression of knirps in eye-antennal imaginal discs leads to the formation of cysts and is sufficient to recapitulate the phenotypic tumor appearance. Moreover, we believe that this TF, with its dual regulatory role, could activate or repress other genes and thus form a regulatory circuit that is beneficial for tumor initiation and progression.

Inducing a cell fate switch can be achieved by forcing expression of a TF that can activate the transcriptional network of the resulting cell type (Yamada et al., 2014). We show that impairment of a global silencing regulator leads to reversion of neurogenesis-lineage committed cells to a less differentiated cell state, but also that this can be achieved by single ectopic expression of kni. This raises the possibility that embryonic TFs such as kni drive the establishment of a regulatory circuit that blocks differentiation. Although the involved factors of such mechanisms remain to be identified, we consider the identification of kni as a strong oncogene a valuable starting point for future studies.

The identification of a tumorigenic role of the embryonic TF Kni in Drosophila, is in line with the identification of other embryonic TFs playing a role in several different tumor models. For instance, aberrant expression of the embryonic TF Oct-4 blocks progenitor-cell differentiation and causes dysplasia in mouse adult epithelial tissues (Kumar et al., 2012; Hochedlinger et al., 2005). In humans, activation of the TF TAL1, normally expressed early in the erythroid lineage, has been shown to alter a core transcriptional regulatory circuit that in turn leads to tumor onset (T cell leukemia) (Bradner et al., 2017). Additionally, other relevant embryonic TFs, such as FOXF1, normally expressed in mesenchyme-derived cells, activate MAPK signaling when expressed in prostate epithelial cells and contribute to tumorigenesis (Fulford et al., 2016).

Taken together, our data show that knirps can drive tumor onset and is a strong oncogene in ph505-tumors. Moreover, our work is consistent with a growing understanding between the connections of developmental gene expression and cancer. We hope that in the long-term these findings can contribute to the development of new therapies for cancers driven by misexpression of TFs.

### Inability to differentiate as target for therapy in embryonic-like tumors

Loss of differentiation capabilities, as well as the emergence of a progenitor-like state that promotes cellular transformation and tumor initiation are common processes observed in cancer (Roy and Hebrok, 2015; Bossuyt et al., 2009). The concept of dedifferentiation preceding tumorigenesis has been shown in Drosophila neurons, where neurons lacking the TF Lola dedifferentiate, turning on neural stem cell genes, begin to divide, and form tumors (Southall et al., 2014).

We provide evidence that kni-ectopic tumors, very similar to ph505-tumors, also fail to undergo differentiation. Besides commonalities such as loss of polarity and loss of cell identity, these two tumor models also share the ectopic activation of the JAK/STAT signaling pathway. Developmental studies suggest the cooperation between JAK/STAT and gap genes (e.g. knirps) in regulating expression of pair-rule genes for segmentation during embryogenesis (Hou et al., 2002). Hyperactivation of the JAK/STAT pathway has been observed in different human cancers, where it activates survival and proliferation genes (Buchert et al., 2016). Also, cells can be maintained in a less differentiated and more proliferative state by JAK/STAT pathway activation, as highlighted by its activation in stem cell niches in Drosophila (Hou et al., 2002; Amoyel and Bach, 2012; Christofi and Apidianakis, 2013) and in mouse embryonic stem cells (Hao et al., 2006). Furthermore, there is evidence suggesting that this pathway must be switched off to allow differentiation of hematopoietic progenitors in flies (Amoyel and Bach, 2012). In agreement with this, blocking JAK/STAT activity suppresses the PRC1 mutant tumor phenotype (Classen et al., 2009) and in our hands induces the re-establishment of the differentiation program characteristic of eye-antennal imaginal discs.

However, using the blockage of signaling pathways as a therapeutic target has been shown to be difficult due to the redundancy of the signaling networks and thus acquired drug resistance is common in cancer cells (Gonda and Ramsay, 2015; Buchert et al., 2016). Alternatively, forced differentiation by means of TF activation might solve this issue. We used atonal, a pro-neural TF in eye discs (Bossuyt et al., 2009) and downregulated in ph505-tumors, to ultimately restore differentiation in eye-antennal tissues. This approach proved to be sufficient to prevent tumor cells from proliferating, reduce tumor burden and recover the normal pattern of differentiation.

The significance of these observations, referred to as ‘differentiation therapy’, is supported by work done in acute myeloid leukemia where therapies to overcome the cellular differentiation arrest have led to favorable outcomes (Gocek and Marcinkowska, 2011). Moreover this strategy has also been suggested to restrict the cellular plasticity of cancer stem cells (Wainwright and Scaffidi, 2017). Our findings highlight the importance of embryonic transcription factors in oncogenesis and favor the potential of re-establishing differentiation as an attractive alternative in future considerations for cancer therapy.

## Materials and methods

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
      <td>genetic reagent (D. melanogaster)</td>
      <td>OregonR (host flies)</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BL25211</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>w[1118] (host flies)</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BL5905</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>yw, FRT19A</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BL1744</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>FRT19A, ph505/FM7 act-GFP</td>
      <td>A.-M. Martinez</td>
      <td>ph505</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>w, tubGal80, FRT19A; eyFlp5, Act5C &gt; y +&gt; Gal4, UAS-GFP.S56T</td>
      <td>T. Xu</td>
      <td>19A Tester</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>P{w[+mC]=tubP-GAL80}LL1, w* P{ry[+t7.2]=ey FLP.N}2P{ry[+t7.2]=neoFRT}19A</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BL42717</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>w[1118]; P{w[+mC]=GAL4-Act5C(FRT.CD2).P}S, P{w[+mC]=UAS RFP.W}3/TM3</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BL30558</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>w; UAS-dome∆CYT</td>
      <td>J. Hombría</td>
      <td>dome∆CYT</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>UAS-ph L7 (#3)</td>
      <td>F. Maschat</td>
      <td>UAS-ph</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>w; UAS-p35</td>
      <td>S. Kurata</td>
      <td>UAS-p35</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>UAS-Kni/Cyo</td>
      <td>M. Affolter</td>
      <td>UAS-Kni</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>UAS-ato (#2)</td>
      <td>G. Mardon</td>
      <td>UAS-ato</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>w1118;; P{NRE-EGFP.S}1</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BL30728 (Notch reporter, NRE-GFP on #3)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>w;;TRE-DsRed</td>
      <td>Chatterjee &amp; Bohmann 2012</td>
      <td>JNK reporter</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>w[1118]; P{w[+mC]=10XStat92E-GFP}2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>BL26198 (JAK/STAT reporter)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of Kni: y(Abate-Shen, 2002) sc[*] v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMS01184}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL34705 (kni-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of Kni: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.JF02544}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL27259 (kni-KD (2))</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of Abd-A: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.JF03167}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL28739 (Abd-A-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of lms: y(Abate-Shen, 2002) sc[*] v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMS02709}attP2/TM3, Sb(Abate-Shen, 2002)</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL43995 (lms-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of gsc: y(Abate-Shen, 2002) sc[*] v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMC02397}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL50894 (gsc-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of cad: y(Abate-Shen, 2002) sc[*] v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMC04863}attP40</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL57546 (cad-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of bgcn: y(Abate-Shen, 2002) sc[*] v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP .GL00596}attP40</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL36636 (bgcn-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of Sox100b: y(Abate-Shen, 2002) sc[*] v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.GLV21021}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL35656 (Sox100b-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of btd: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.JF03389}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL29453 (btd-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of eve: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.JF03161}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL28734 (eve-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of tin: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMC03064}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL50663 (tin-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of Dr: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMC03402}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL51830 (Dr-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of nub: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMC03992}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL55305 (nub-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of fkh: y(Abate-Shen, 2002) sc[*] v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMS01103}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL33760 (fkh-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of Abd-B: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.JF02309}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL26746 (Abd-B-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of pb: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMC03065}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL50664 (pb-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of grn: y(Abate-Shen, 2002) sc[*] v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMS01085}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL33746 (grn-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of odd: y(Abate-Shen, 2002) sc[*] v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMS01315}attP2/TM3, Sb(Abate-Shen, 2002)</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL34328 (odd-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of croc: y(Abate-Shen, 2002) sc[*] v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMS01122}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL34647 (croc-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of drm: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMJ02120}attP40</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL42548 (drm-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of Doc2: y(Abate-Shen, 2002) sc[*] v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.HMS02804}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL44087 (Doc2-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of Doc3: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.JF02223}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL31932 (Doc3-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of vvl: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.JF02126}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL26228 (vvl-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of Doc1: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.JF02222}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL31931 (Doc1-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>genetic reagent (D. melanogaster)</td>
      <td>RNAi of Kr: y(Abate-Shen, 2002) v(Abate-Shen, 2002); P{y[+t7.7] v[+t1.8]=TRiP.JF02745}attP2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>Trip BL27666 (Kr-KD)</td>
      <td></td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>Ph (rabbit)</td>
      <td>R. Paro Lab</td>
      <td>N/A</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>Arm (mouse)</td>
      <td>DSHB</td>
      <td>N27A1</td>
      <td>(1:5)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>MMP1 (mouse)</td>
      <td>DSHB</td>
      <td>5H7B11</td>
      <td>(1:300)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>ELAV (rat)</td>
      <td>DSHB</td>
      <td>7E8A10</td>
      <td>(1:30)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>Eya (mouse)</td>
      <td>DSHB</td>
      <td>eya10H6</td>
      <td>(1:500)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>Hth (goat)</td>
      <td>H. Sun</td>
      <td>dG20, Santa Cruz</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>Eve (mouse)</td>
      <td>DSHB</td>
      <td>Eve 3C10</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>Cad (rabbit)</td>
      <td>P. Macdonald Lab</td>
      <td>#1</td>
      <td>(1:500)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>Abd-B (mouse)</td>
      <td>DSHB</td>
      <td>N/A</td>
      <td>(1:10)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>Dcp-1 (rabbit)</td>
      <td>Cell Signaling</td>
      <td>9578S</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>Phalloidin Alexa 633</td>
      <td>Life Technologies</td>
      <td>A22284</td>
      <td>(1:400)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>phospho-Histone H3, Ser 10 (pH3, rabbit)</td>
      <td>Millipore</td>
      <td>06–570</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>antibody</td>
      <td>Alexa 568- or 594 secondaries</td>
      <td>Life Technologies</td>
      <td>A-11036, A11031, A-11077, A-11058</td>
      <td>(1:500)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>commercial assay or kit</td>
      <td>PicoPure RNA Isolation Kit</td>
      <td>Thermo Fisher</td>
      <td>KIT0204</td>
      <td></td>
    </tr>
    <tr>
      <td>commercial assay or kit</td>
      <td>RNase-Free DNase Set</td>
      <td>Qiagen</td>
      <td>#79254</td>
      <td></td>
    </tr>
    <tr>
      <td>commercial assay or kit</td>
      <td>Quant-iT RiboGreen RNA Assay Kit</td>
      <td>Thermo Fisher</td>
      <td>R11490</td>
      <td></td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>Collagenase</td>
      <td>Sigma</td>
      <td>C1639</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>iRegulon</td>
      <td>Janky et al. (2014)</td>
      <td>http://iregulon.aertslab.org</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>Trimmomatic</td>
      <td>Bolger et al. (2014)</td>
      <td>http://www.usadellab.org/cms/?page=trimmomatic</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>FastQC</td>
      <td>FastQC A Quality Control tool for High Throughput Sequence Data (v0.11.2)</td>
      <td>www.bioinformatics.babraham.ac.uk/projects/fastqc/</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>STAR</td>
      <td>Dobin et al. (2013)</td>
      <td>https://github.com/alexdobin/STAR</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>Picard Tools</td>
      <td>Picard tools (version 1.121)</td>
      <td>www.broadinstitute.github.io/picard/</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>HTSeq</td>
      <td>Anders et al. (2015)</td>
      <td>http://www-huber.embl.de/HTSeq/doc/overview.html#</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>DESeq2</td>
      <td>Love et al. (2014)</td>
      <td>https://bioconductor.org/packages/release/bioc/html/DESeq2.html</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>WEB-based GEne SeT AnaLysis Toolkit</td>
      <td>Wang et al., 2013</td>
      <td>WebGestalt: www.webgestalt.org</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>Ilastik</td>
      <td>Sommer, 2011</td>
      <td>http://ilastik.org</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>Matlab</td>
      <td>MATLAB 2016b, The MathWorks Inc., Natick, MA</td>
      <td>https://ch.mathworks.com/products/matlab.html</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>Imaris</td>
      <td>Imaris v 8.4.1 (Build 41809 for x64), Bitplane AG</td>
      <td>http://www.bitplane.com/imaris/imaris</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>GraphPad Prism 7.0</td>
      <td>GraphPad Prism version 7.00 for Windows, GraphPad Software, La Jolla California USA</td>
      <td>https://www.graphpad.com/scientific-software/prism/</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Contact for reagent and resource sharing

Further information and requests for resources and reagents should be directed to and will be fulfilled by the corresponding authors.

### Experimental model

Flies were maintained on standard food at 25°C and 60% relative humidity, under a 12 hr light: 12 hr dark cycle. All fly stocks used are listed in the Key Resources Table.

### Mitotic recombination and generation of clones

Mitotic recombination was induced by the expression of FLP recombinase under the control of eyeless promoter (eyFlp). Additionally, using the mosaic analysis with a repressible cell marker (MARCM) system (Wu and Luo, 2006), clones were fluorescently labeled with GFP. For our mutant experiments, we used ph505 allele to knock-out both genes in the ph locus (ph-p and ph-d). For control experiments, MARCM clones were generated with a FRT19A blank stock line. Specifically, ‘19A tester’ stock line was crossed either with FRT19A, ph505/FM7 act-GFP or with FRT19A in order to generate mutant or control clones in eye-antennal imaginal discs, respectively. Larvae were examined at the late third instar stage.

### Candidate hit-validation in vivo – RNAi constructs

RNAi strains were initially balanced (#2, Cyo or #3 TM6b) and subsequently crossed with the strain carrying the mutant allele and maintained as a stock. For generation of clones and simultaneous expression of RNAi-target, the stock mentioned above was crossed with ‘19A tester’ strain. For all final crosses 25 female virgins were crossed with eight males, in order to insure that number of larvae per fly food vial would be similar and not overcrowded. Two independent crosses for each RNAi were performed. Up to three replicates were collected from each RNAi cross.

Confirmation of the results obtained by RNAi KD with a knirpsmut allele could not be realized. We did not succeed in generating a recombinant mutant allele (Kni[FC13]) with a FRT element, probably caused by the expected low frequency of recombination between the two elements.

For determination of eclosion rates, larvae were selected accordingly to GFP expression in eye discs, counted and transferred to a new food vial. After eclosion the number of adults was counted. Eclosion rate was measured as the ratio of number larvae over the number of adults that hatched. Images of adult eyes were acquired with Nikon SMZ1270.

### Immunostaining of eye-antennal imaginal discs

Third instar larvae were dissected in PBS 1x and fixed in 4% paraformaldehyde (SIGMA, #P6148) in PBS 1x for 20 min at room temperature (RT) and washed with PBS with 0.1% TritonX-100 (SIGMA, #T9284) (0.1% PBS-T) for 30 min (3 × 10 min) and blocked (0.1% Bovine Serum Albumin (Serva, #11930.04) in 0.1% PBS-T) for 1 hr at RT. Larvae were then incubated with primary antibodies in blocking solution overnight at 4°C, washed with 0.1% PBS-T (3 × 15 min) and incubated with secondary antibodies in blocking solution for 2 hr at RT. After washing with 0.1% PBS-T for 15 min, DAPI (Invitrogen #62248, 1:500) was added and incubated for 15 min at RT. Imaginal discs were then dissected in PBS 1x and mounted in a slide with Vectashield mounting medium (Vector Laboratories).

The primary antibodies used in this study were: rabbit anti-Ph (Paro lab; 1:100), mouse anti-Arm (DSHB N27A1; 1:5), mouse anti-MMP1 (DSHB 5H7B11; 1:300), rat anti-ELAV (DSHB 7E8A10; 1:30), mouse anti-eve (DSHB Eve3C10; 1:100), rabbit anti-cad (Macdonald lab; 1:500), mouse anti-Eya (DSHB eya10H6; 1:500), goat anti-Hth (H. Sun; 1:100), mouse anti-Abd-B (DSHB; 1:10), rabbit anti-Dcp-1 (Cell Signaling 9578S; 1:200), rabbit anti-pH3 (Millipore 06–570; 1:200).

Appropriate combinations of Alexa-coupled secondary antibodies were subsequently applied. Phalloidin-633 (Life Technologies A22284, 1:100) was used for actin staining. The secondary antibodies used were: goat anti-Rabbit Alexa 568 (Life Technologies., Bleiswijk, Netherlands, A-11036), goat anti-mouse Alexa 568 (Life Technologies, A-11031), goat anti-rat Alexa 568 (Life Technologies, A-11077), donkey anti-goat Alexa 594 (Life Technologies, A-11058). All secondary antibodies were used at 1:500 dilutions.

Samples were analyzed with a Leica SP5 or SP8 confocal microscope. Images were processed using ImageJ and were assembled with Adobe Photoshop.

### Transplantations

Transplantation assays were performed according to previous reports (Rossi and Gonzalez, 2015). Briefly, eye-antennal discs of genotypes of interest (either ph505; ph505, kni-KD; or FRT19A, UAS-Kni) were cut into small pieces and transplanted into the abdomen of female hosts (w[1118] or wild-type Oregon R). Transplanted hosts were kept at 25°C and monitored for GFP+ overgrowth mass. Number of tumor-bearing hosts was assessed every week upon transplantation. Transplanted hosts with ph505 tissues were used as control to account for pathogen contaminations, temperature changes or other issues that could affect the survival of the flies. Adult hosts were analyzed and images were acquired with Nikon SMZ1270.

### Workflow for sample preparation for RNA-sequencing

Protocol for sample preparation for RNA-sequencing was adapted from published work (Harzer et al., 2013; Martinez et al., 2009; Dutta et al., 2013). Each biological replicate for FACS was composed of a total of 200–250 eye-antennal imaginal discs of third instar larvae dissected in PBS 1x. After spinning down and removing PBS 1x, imaginal discs were placed in low-binding 1.5 mL tube with 200 uL of saline solution containing collagenase (25 discs/tube) (collagenase SIGMA, C1639 - 1.5 mg/mL diluted in Rinaldini’s saline solution) and incubated at RT for 45 min, 300rpms. Tubes were agitated every 15 min and mechanical digestion was performed twice during collagenase incubation (pipetting up-and-down with 27G syringe). After digestion, tubes were pooled in a total of 2 1.5 mL tubes and centrifuged for 25 min, 300 g, 4°C. Supernatant was removed and pellet was resuspended in PBS 1x. Solution was filtered and shortly kept on ice before proceeding for FACS. Several rounds of FACS-sorting were performed from pools of ph505 eye-antennal discs, using a BD FACS Aria cell sorter (BD Biosciences) of the FMI FACS facility (FMI, Basel) and data was collected on the basis of FSC/SSC parameters. Sorting time was kept below 45 min to insure the maximum viability of the cells. Two populations of cells were collected separately, GFP+- (mutant cells) and GFP--sorted cells (control), directly into extraction buffer (200 µL, PicoPure RNA isolation kit, Thermo Fisher, KIT0204). RNA extraction was performed accordingly to manufacturers instructions, including a step of DNase treatment (Qiagen, catalog #79254). Samples were eluted in the final volume of 11 µL and kept at −80°C. RNA concentration (RiboGreen, ThermoFisher, #R11490) and integrity (Fragment analyzer, AATI) of sorted samples was assessed by the Genomics Facility Basel (D-BSSE, Basel). From the several rounds of samples’ preparation, we choose 4 pairs of samples (tumor and matched-control) and three extra tumor samples from batches where control cells did not have the desired quality, to prepare libraries for sequencing. Due to the low amount of RNA in these samples, libraries were prepared by the Genomics Facility Basel using a method conceived for single cell RNA-seq (Smart-seq2) (Picelli et al., 2014).

### RNA-sequencing – Differential expression analysis

The following steps were performed on 22 libraries. There were two technical replicates per sample corresponding to a total of 11 samples (seven tumor, four control). The libraries were sequenced in paired-end mode (2 × 150 bp) in a NextSeq500 (Illumina), and insert sizes around 300 bp (ungapped forward and reverse tags). Adaptor clipping and quality trimming was performed with Trimmomatic (Bolger et al., 2014) (v0.30), after initial quality checks with FastQC (v0.11.2, www.bioinformatics.babraham.ac.uk/projects/fastqc/). Reads were aligned using the splice aware aligner STAR (Dobin et al., 2013) (v2.3.0e) and subsequently filtered to remove potential PCR-duplicates with Picard Tools (v1.121, broadinstitute.github.io/picard/). Transcript counts were produced with HTSeq (Anders et al., 2015) (v0.6.1) using the Ensembl 78 annotation (Aken et al., 2016). The subsequent differential expression analysis was performed in R (v3.1.0, www.r-project.org) using the DESeq2 package (Love et al., 2014) (v1.6.1), neglecting one library (technical replicate), which did not meet quality standards. All the differentially expressed genes were submitted to the”WEB-based GEne SeT AnaLysis Toolkit’ (WebGestalt (Wang et al., 2013), www.webgestalt.org), submitting either all differentially expressed genes at the same time, or splitting them into up- and down-regulated genes.

For the in vivo screen, we decided not to exclude candidates based on their log2 fold change, as is commonly done, but rather selected candidates based on a stringent adjusted p value (padj. <0.01) and a-priori knowledge.

### Incorporation of other gene expression datasets

RNA-seq profiles of our tumor and control samples were compared with available D. melanogaster datasets (Figure 1—source data 3), specifically comparing 124 differentially expressed TF-encoding genes (Figure 1—source data 4). All additional samples (fastq-files) were obtained from the Gene Expression Omnibus (GEO, www.ncbi.nlm.nih.gov/geo/) and processed in a similar fashion as the original 11 samples. For single-end-libraries, the removal of duplicates was not performed. Settings in Trimmomatic were adjusted for each sample, taking into account the sequencer type and read lengths. All samples were aligned with STAR and counting was performed with HTSeq.

### Hierarchical clustering

Hierarchical clustering was performed after normalizing gene-expression values with DESeq2. The expression values after variance stabilizing transformation were then mean-centered for each gene. Hierarchical clustering was performed between samples using 1-Pearson correlation as distance measure, while genes were clustered using Euclidean distance. The datasets used for comparison were retrieved from the following references: (Graveley et al., 2011; Gan et al., 2010; Jüschke et al., 2013; Potier et al., 2014; Berger et al., 2012; Naval-Sánchez et al., 2013; Czech et al., 2013; Atkins et al., 2016).

### Image analysis

Images of eye-antennal imaginal tissues were acquired using 20x or 40x objectives on the Leica SP5/SP8 confocal microscopes and processed using ImageJ or Imaris. Images of adult eyes or transplantation hosts were acquired with Nikon SMZ1270.

### Quantification pipeline for tumor volumes

As a measure of tumor volume, we quantified the space taken up by the tumor in these tissues employing a quantification pipeline developed in our lab (Beira et al., 2018). To automate image segmentation and identification of clones across imaginal discs, we used Ilastik (Interactive Learning and Segmentation Toolkit, [Sommer, 2011]) to build an unbiased supervised learning classification of clone regions and surrounding tissue (with 5 ph505-tumor eye-antennal imaginal discs). Confocal images of tissues of interest were acquired with a 0.8–1.1 μm z-stacks. The classification method was then used for the test set of ph505-tumor tissues (N = 50), as well as upon perturbation (either TF-KD or overexpression of ph, p35 and ato). After unbiased classification of clones, a Matlab script (kindly developed by Aaron Ponti, SCF, D-BSSE) was used to enable us to use Imaris (Bitplane) in order to obtain volume data for each spatially defined clone, total clone number per tissue, and tissue volume (DAPI). Tumor volume (%) was then calculated as the ratio of tumor volume (sum up volumes of all GFP-clones in a tissue) over the size of the respective tissue (volume, DAPI).

### Quantification of phospho-histone H3 cells

In order to measure proliferation levels, we quantified the number of phospho-histone H3 (pH3) positive cells within eye-antennal imaginal discs in the four conditions of interest (FRT19A; FRT19A, UAS-ato; ph505; ph505, UAS-ato). We used Imaris (Bitplane) for semi-automated image segmentation of total tissue volume (DAPI), total volume of clones (GFP+ cells) and number of pH3+ cells. In addition, we used the segmented GFP signal to mask voxels of the pH3 +channel inside and outside of GFP positive cells to zero. In this way we were able to measure pH3+ cells inside and outside the clones. To account for differences in the size of tissues and clones, we normalized the data accordingly. For the ‘whole tissue’ condition, total numbers of pH3+ cells were normalized to total tissue volume (per tissue); for ‘inside clones’, numbers of pH3+ cells within clones were normalized to volume of GFP+ cells per tissue; for ‘outside clones’, numbers of pH3+ cells outside of GFP+ clones were normalized to volume of GFP- cells per tissue. Values of pH3+ cells are represented per mm3.

### Statistical analysis

GraphPad Prism 7.0 was used for statistical analysis and generation of the graphical output. No statistical analysis was used to predetermine sample size. Sample sizes (N) and p-values are indicated in the figures and/or figure legends. Statistical tests used: Kruskal-Wallis with Dunn's multiple comparisons test for eclosion rate, tumor volume (%), number of clones and number of pH3+ cells; one-way ANOVA with Dunnett's multiple comparisons test for tissue size and average tumor volume. ****p<0.0001; ***p<0.001; **p<0.01; *p<0.05. All data points represented by dots in the plots for tumor volume, average tumor volume, tissue volume, number of clones and number of pH3+ cells per tissue are randomly distributed along x-axis.

### Data availability

The accession number for the sequencing data reported in this paper is GEO: GSE101463.
