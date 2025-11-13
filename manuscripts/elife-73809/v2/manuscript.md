# Diversification of multipotential postmitotic mouse retinal ganglion cell precursors into discrete types

## Authors

- Karthik Shekhar<sup>1</sup> ([ORCID: 0000-0003-4349-6600](https://orcid.org/0000-0003-4349-6600)) †
- Irene E Whitney<sup>4</sup>
- Salwan Butrus<sup>1</sup>
- Yi-Rong Peng<sup>4</sup>
- Joshua R Sanes<sup>4</sup> ([ORCID: 0000-0001-8926-8836](https://orcid.org/0000-0001-8926-8836)) †

### Affiliations

1. Department of Chemical and Biomolecular Engineering; Helen Wills Neuroscience Institute; Center for Computational Biology; California Institute for Quantitative Biosciences, QB3, University of California, Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))
2. Biological Systems and Engineering Division, Lawrence Berkeley National Laboratory Berkeley United States ([ROR:02jbv0t02](https://ror.org/02jbv0t02))
3. Broad Institute of Harvard and MIT Cambridge United States ([ROR:05a0ya142](https://ror.org/05a0ya142))
4. Center for Brain Science and Department of Molecular and Cellular Biology, Harvard University Cambridge United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
5. Department of Ophthalmology, Stein Eye Institute, UCLA David Geffen School of Medicine Los Angeles United States ([ROR:046rm7j60](https://ror.org/046rm7j60))

† Corresponding author

## Abstract

The genesis of broad neuronal classes from multipotential neural progenitor cells has been extensively studied, but less is known about the diversification of a single neuronal class into multiple types. We used single-cell RNA-seq to study how newly born (postmitotic) mouse retinal ganglion cell (RGC) precursors diversify into ~45 discrete types. Computational analysis provides evidence that RGC transcriptomic type identity is not specified at mitotic exit, but acquired by gradual, asynchronous restriction of postmitotic multipotential precursors. Some types are not identifiable until a week after they are generated. Immature RGCs may be specified to project ipsilaterally or contralaterally to the rest of the brain before their type identity emerges. Optimal transport inference identifies groups of RGC precursors with largely nonoverlapping fates, distinguished by selectively expressed transcription factors that could act as fate determinants. Our study provides a framework for investigating the molecular diversification of discrete types within a neuronal class.

## Introduction

A central question in developmental neurobiology is how the brain’s diverse neuronal types arise from multipotential progenitors (Lodato and Arlotta, 2015; McConnell, 1991; Wamsley and Fishell, 2017). The vertebrate retina has been a valuable model for addressing this question: it is about as complicated as any other region of the brain, but has several features that facilitate mechanistic analysis (Dowling, 2012). The retina contains five classes of neurons – photoreceptors that sense light, three interneuronal classes (horizontal, bipolar, and amacrine cells) that process visual information, and retinal ganglion cells (RGCs) that pass the information to the rest of the brain through the optic nerve (Figure 1a; Masland, 2012). These classes can be divided into numerous types, ~130 in mouse and chick, each of which has characteristic morphological, physiological, and molecular properties, and plays distinct roles in information processing (Baden et al., 2016; Franke et al., 2017; Goetz et al., 2021; Macosko et al., 2015; Rheaume et al., 2018; Shekhar et al., 2016; Shekhar and Sanes, 2021; Tran et al., 2019; Yamagata et al., 2021; Yan et al., 2020). Remarkably, nearly all types are distributed across the entire retina (Kay et al., 2012; Keeley et al., 2020; Rockhill et al., 2000), so morphogen gradients, which play a critical role in other parts of the central nervous system (e.g., Sagner and Briscoe, 2019), cannot provide an explanation for retinal neuronal diversification (Marquardt and Gruss, 2002).

![Figure 1.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig1-v2.jpg)

**Figure 1.:** (a) Sketch of a section of the mouse retina showing major cell classes – photoreceptors (PRs; rods and cones), horizontal cells (HCs), bipolar cells (BCs), amacrine cells (ACs), Müller glia (MGs), and RGCs. PRs reside in the outer nuclear layer (ONL), while BCs, HCs, and most ACs reside in the inner nuclear layer (INL). RGCs and some ACs reside in the ganglion cell layer (GCL). Axons of RGCs project to higher visual areas via the optic nerve. (b) Retinal section of the indicated ages labeled for the cell cycle marker MKI67 (red) and the RGC marker RBPMS (green); nuclei are counterstained by the Hoeschst dye (blue). Micrographs are orientated as the schematic in panel (a). (c) Visualization of transcriptional diversity of 98,452 cells using Uniform Manifold Approximation and Projection (UMAP), a nonlinear dimensionality reduction algorithm that assigns proximal x-y coordinates to cells (dots) with similar transcriptional profiles (Becht et al., 2018). (d) Same as (c), with cells colored by cell class, assigned based on transcriptional signatures displayed in panel (e). RPC, retinal progenitor cells; Ant. Seg., anterior segment cells. (e) Tracksplot showing expression patterns of cell class-specific marker genes (rows) across single cells (columns). Cells are grouped by class as in (d). For each class, we randomly sampled 20% of total cells covering all immature time points (embryonic day [E]13, E14, E16, postnatal day [P]0, P5). For each gene, the scale on the y-axis (right) corresponds to normalized, log-transformed transcript counts detected in each cell.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (a) Retinal sections stained with L1CAM (red), which was used to enrich for RGCs at early stages, and the pan-RGC marker RBPMS, (green) at E13, E14, E16, and P0. Nuclei are counterstained by the Hoeschst dye (blue). (b) Relative proportions (y-axis) of major cell classes shown in Figure 1c–e at each combination of age and enrichment method. Both anti-Thy1 and anti-L1cam were used to enrich RGCs at E13, E14, E16, and P0, but only anti-Thy1 was used at P5, because L1cam becomes localized to axons postnatally. AC, amacrine cells; RPC, retinal progenitor cells. (c) Box-and-whisker plots show gene expression levels of key markers by RGCs as a function of age and enrichment method. Markers shown are two pan-RGC markers, Rbpms, Nefl, and the two cell surface proteins used for enrichment, Thy1 and L1cam. Note that Thy1 expression is poor at E13, consistent with low RGC yield in anti-Thy1-enriched cells in panel (b). Black horizontal line, median; bars, interquartile range; vertical lines, range; dots, outliers. (d) Dotplot showing genes (columns) that are selectively expressed in RGCs and RPCs. The size of each circle is proportional to the percentage of cells expressing the gene, and the color depicts the average log-normalized expression. (e) Co-embedding analysis of E14, E16, and P0 data collected in this study with whole retina single-cell transcriptomes in independent studies: E14, E16, and P0 data from Clark et al., 2019 and E15.5 data from Lo Giudice et al., 2019. Cells (points) are visualized in Uniform Manifold Approximation and Projection (UMAP) and colored by study of origin. (f) Same as (e), with cells colored by the expression level of Nefl, an RGC marker. This shows the higher enrichment of RGCs in our study compared to Clark et al., 2019 and Lo Giudice et al., 2019. (g) Same as (e), with cells colored by expression level of Fgf15, an RPC marker. (h) Relative proportions of major cell classes across different datasets analyzed in panel (e) separated by age. T, this study. (i) Confusion matrix showing post hoc transcriptomic correspondence between P5 RGC types identified in Rheaume et al., 2018 (y-axis) and P5 RGC clusters reported in this study (x-axis). In each case, RGCs from Rheaume et al. were assigned P5 cluster labels using an XGBoost classifier trained on P5 RGCs profiled in this study.

Seminal studies have provided deep insights into how retinal classes arise (Bassett and Wallace, 2012; Cepko, 2014). First, lineage tracing in rodents and frogs showed that single retinal progenitor cells (RPCs) can give rise to neurons of all classes as well as glia, and are therefore multipotential (Holt et al., 1988; Turner and Cepko, 1987; Turner et al., 1990; Wetts and Fraser, 1988). Second, the competence of multipotential RPCs to generate cells of particular classes changes over time, accounting for their sequential (but overlapping) birth windows (Cepko, 2014; Livesey and Cepko, 2001). Such segregation of birth windows is a hallmark of many neuronal systems (Holguera and Desplan, 2018) and is believed to arise from the differential temporal regulation of gene expression in RPCs (Blackshaw et al., 2004; Brown et al., 2001; Chen et al., 1997; Clark et al., 2019; Trimarchi et al., 2008). Third, competence is probabilistic rather than deterministic, with stochastic factors accounting for variations in the distribution of cell classes generated by individual RPCs (Boije et al., 2014; Gomes et al., 2011; Johnston and Desplan, 2010).

In contrast to these well-established tenets of neuronal class generation, we know far less about how immature postmitotic neurons (which we call neuronal precursors here) committed to a specific class identity diversify into distinct types. We address this issue here, focusing on RGCs. All RGCs are similar in many respects: for example, they all elaborate dendrites that receive input from amacrine and bipolar interneurons, send axons through the optic nerve, and use glutamate as a neurotransmitter (Sanes and Masland, 2015). However, they differ in molecular, morphological, and physiological details, which have led to their division into ~45 distinct types in mice (Baden et al., 2016; Bae et al., 2018; Goetz et al., 2021; Rheaume et al., 2018; Tran et al., 2019). Most of these types appear to be feature detectors that collectively transmit a diverse set of highly processed images of the visual world to the rest of the brain (Baden et al., 2020; Sanes and Masland, 2015). Several genes have been implicated in maturation of a few mouse RGC types (Clark et al., 2019; Kiyama et al., 2019; Liu et al., 2018; Lo Giudice et al., 2019; Lyu and Mu, 2021; Peng et al., 2017; Sajgo et al., 2017), but a comprehensive investigation of RGC diversification has been lacking.

To gain insight into how and when adult RGC types emerge, we used high-throughput single-cell RNA-seq (scRNA-seq) to profile RGC precursors during embryonic and postnatal life in mice. We find that the number and distinctiveness of molecularly defined groups of precursors increases with developmental age, implying that types arise by a gradual process rather than from ~45 committed precursor types. Using statistical inference approaches, we identify fate associations among immature RGCs as transcriptomically distinct types emerge. These analyses suggest a model in which types arise from multipotential precursors by a process of restriction that we term fate decoupling. The decoupling is gradual and asynchronous, resulting in different types emerging at different times. We also use markers of RGCs that project to contralateral or ipsilateral retinorecipient areas to subdivide each type by its projection pattern, leading to the conclusion that laterality may be specified prior to type identity is fixed. Together, our results provide both a model of RGC diversification and a computational framework that can be applied generally to analyze the diversification of closely related neuronal types within a class.

## Results

### Transcriptomic atlas of developing mouse RGCs

Mouse RGCs are born between approximately embryonic days (E) 11 and 17 with newborn RGCs exiting the mitotic cycle near the apical margin, then migrating basally to form the ganglion cell layer (Dräger, 1985; Marcucci et al., 2019; Voinescu et al., 2009; Figure 1b). Reported birthdates differ among publications and are complicated by naturally occurring cell death and the central-peripheral developmental gradient, but a detailed analysis concludes that >95% of RGCs in adult mouse retina are born after E12.8 and >85% before E16 (Farah and Easter, 2005). Shortly after they are born, RGCs extend axons through the optic nerve, with some reaching retinorecipient areas by E15 (Godement et al., 1984; Osterhout et al., 2011) and forming diverse projection patterns (Martersteck et al., 2017). During early postnatal life, they extend dendrites apically into the inner plexiform layer of the retina, receiving synapses from amacrine cells by postnatal day (P)4 and bipolar cells a few days later (Kim et al., 2010; Lefebvre et al., 2015). Light responses are detected in RGCs by P10 but image-forming vision does not begin until eye-opening, around P14 (Hooks and Chen, 2020).

To determine when and how RGCs diversify, we used droplet-based scRNA-seq (Macosko et al., 2015; Zheng et al., 2017) to profile them at five stages: E13 and E14 (during the period of peak RGC genesis), E16 (by which time RGCs axons are reaching target retinorecipient areas), P0 (as dendrite elaboration begins), and P5 (shortly after RGCs begin to receive synapses). As RGCs comprise ≤1% of retinal cells (Jeon et al., 1998), we enriched them with antibodies to two RGC-selective cell surface markers, Thy1/CD90 (Barres et al., 1988) and L1cam (Demyanenko and Maness, 2003; Figure 1—figure supplement 1a).

We obtained a total of 98,452 single-cell transcriptomes with acceptable quality metrics (Materials and methods). Of these, we identified 75,115 (76%) as RGCs based on their expression of canonical RGC markers, including Rbpms (an RNA-binding protein) and Slc17a6 (the vesicular glutamate transporter VGLUT2) (Figure 1c–e, Figure 1—figure supplement 1b and c). Non-RGCs included amacrine cells (Tfap2a+ Tfap2b+), cone photoreceptors (Otx2+ Crx+ ), microglia (P2ry12+ C1qa+), anterior segment cells (Mgp+ Bgn+ ), and RPCs. Anterior segment cells were found only in E13 and E14 samples because whole eyes were dissociated at these stages. RPCs formed a continuum, containing both ‘primary’ RPCs expressing cell cycle-related genes (e.g., Mki67, Ccnd5, and Birc5) and previously described RPC regulators (e.g., Sfrp2, Vsx2, and Fgf15), and ‘neurogenic’ RPCs expressing proneural transcription factors (TFs) (e.g., Hes6, Ascl1, and Neurog2) (Clark et al., 2019). Importantly, these markers were not expressed in cells annotated as RGCs (Figure 1—figure supplement 1d). These stringent criteria ensured that our dataset comprised postmitotic committed RGCs, allowing us to focus on their diversification and maturation.

Overall, we recovered ~5900–18,500 RGCs at each of the five time points. Of the two surface markers used for enriching RGCs, Thy1 was effective at later stages as shown previously (Kay et al., 2011; Rheaume et al., 2018; Tran et al., 2019), whereas L1cam expression was more selective at E13 and E14 (Figure 1—figure supplement 1b and c). However, identical clusters were observed with both methods at E13, E14, and E16, albeit with different frequencies. This concordance supports the idea that neither marker fails to capture particular RGC types. To further evaluate the effectiveness of our enrichment strategy at early stages, we compared our data with two recent studies in which developing retinal cells were profiled using scRNA-seq without any enrichment (Clark et al., 2019; Lo Giudice et al., 2019). A joint analysis of these datasets at embryonic time points showed consistency in the transcriptional signatures of major cell groups without discernible biases (Figure 1—figure supplement 1e–g). However, our enrichment protocols increased the fractional yield of RGCs by >3× at E14 and E16 and by >100× at P0 (Figure 1—figure supplement 1h), which enabled us to resolve heterogeneity within this class at immature stages. We also compared our P5 data with those from an earlier study in which P5 RGCs were profiled (Rheaume et al., 2018) and found a good correspondence (Figure 1—figure supplement 1i). For the analysis that follows, we combined precursor RGCs (E13–P5) with a previously described dataset of 35,699 mature RGCs at P56 (Tran et al., 2019).

### Immature RGCs diversify postmitotically

One can envision two extreme models of RGC diversification. In one, RGC type would be specified at or before mitotic exit, with each type arising from a distinct set of committed precursors that are transcriptomically defined. At the other extreme, all precursor RGCs would be identical when they exit mitosis and gradually acquire distinct identities as they mature (Figure 2a). Intermediate models could involve multiple groups of precursor RGCs, each biased towards a distinct set of terminal types.

![Figure 2.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig2-v2.jpg)

**Figure 2.:** (a) Extreme models of RGC diversification. In one scenario (left), immature RGCs commit to one of the terminal types by the time of birth (i.e., mitotic exit) or shortly after. Alternatively (right), initially identical postmitotic RGC precursors acquire distinct molecular identities in a gradual process of restriction. (b–g) Visualization of transcriptomic diversity of immature RGCs at embryonic day (E)13 (b), E14 (c), E16 (d), postnatal day (P)0 (e), P5 (f), and P56 (g) using Uniform Manifold Approximation and Projection (UMAP). Cells are colored by their cluster identity, determined independently using dimensionality reduction and graph clustering (Materials and methods). Clusters are numbered based on decreasing size at each age. Data for adults (P56) are replotted from Tran et al., 2019. In that study, 45 transcriptomic types were identified via unsupervised approaches, one of which was mapped to two known functional types by supervised approaches. We do not distinguish them in this study. (h) Transcriptional diversity of RGCs as measured by the Rao diversity index (y-axis) increases with age (x-axis). The trend is insensitive to the number of genes used to compute inter-cluster distance (colors). See Materials and methods for details underlying the calculation. (i) Transcriptomic distinctions between RGC clusters become sharper with age as shown by decreasing average per-cluster error of a multiclass classifier with age. Gradient boosted decision trees (Chen and Guestrin, 2016) were trained on a subset of the data and applied on held-out samples to determine the test error. (j) RGC clusters also become better separated in the UMAP embedding, as shown by the decreasing values of the average relative cluster diameter with age.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (a–c) Uniform Manifold Approximation and Projection (UMAP) embedding for RGCs at embryonic day (E)14 (a, same as Figure 2c), E16 (b, same as Figure 2d), and postnatal day (P)0 (c, same as Figure 2e) with cells colored by enrichment method showing comparable transcriptomic diversity of immature RGCs enriched by L1cam or Thy1. All clusters are present in both collection types, although the relative frequencies vary. This concordance supports the idea that neither marker excludes particular types. (d) Simpson and Shannon diversity indices (see Materials and methods) associated with clustering decrease and increase with age, respectively, consistent with increasing transcriptomic diversity.

To distinguish among these alternatives, we analyzed the transcriptomic diversity of RGCs at each developmental stage using the same dimensionality reduction and graph clustering approaches devised for analysis of adult RGCs (Tran et al., 2019; see Materials and methods). This analysis led to three main results.

First, RGCs were already heterogeneous soon after mitotic exit. There were 10 transcriptionally defined precursor clusters at E13 (Figure 2b) before or at the peak time of RGC birth. The number of discrete clusters increased only slightly by E14 (from 10 to 12; Figure 2c), arguing against a model in which the number of precursor types extrapolated back to 1. No single cluster dominated the frequency distribution at either time as would be expected if a totipotent precursor RGC were to exist shortly after terminal mitosis.

Second, the number of transcriptionally defined clusters increased gradually, between E13 and adulthood, reaching 45 only after P5 (Figure 2b–g). Several arguments indicate that this increase is biologically significant rather than being an artifact of the data or computational analysis. (1) We used the same clustering procedure at all ages. (2) The qualitative trends were robust against variations in clustering parameters. (3) All embryonic clusters contained cells isolated with both cell markers, L1cam and Thy1 (Figure 2—figure supplement 1a–c), indicating that lower cluster numbers at early stages did not result from biased collection methods. (4) The increase in the number of effective molecular types was robust as demonstrated by three diversity indices – Rao, Simpson, and Shannon – all of which buffer against artificial inflation of diversity due to small clusters (Figure 2h, Figure 2—figure supplement 1d; see Materials and methods). (5) There was no systematic dependence of the number of clusters on the number of cells. For example, we identified 12 clusters from 17,100 cells at E14 and 38 clusters from 17,386 cells at P5.

Third, the transcriptomic variation became increasingly discrete with age. We quantified this increase in inter-cluster separation by calculating (1) the average cross-validation error of a multi-class classifier, and (2) the ratio of mean cluster diameter to mean inter-cluster distance in the low dimensional embedding (Materials and methods). Both metrics decrease in numerical value as the clusters are more well defined. From these trends, we conclude that the boundaries between RGC clusters become sharper as development proceeds (Figure 2i and j).

Taken together, our results show that transcriptomic clusters of RGCs increase in number and distinctiveness over time, making it unlikely that RGC-type identity is fully specified at the progenitor stage.

### Temporal relationships among immature RGC clusters

We next investigated the temporal relationships among precursor RGC clusters identified at different ages. We again consider two extreme models. In a ‘specified’ model, each terminal type arises from a single cluster at every preceding developmental stage (Figure 3a, left). In this model, distinct transcriptomic states among precursor RGCs correspond to distinct groups of fates. At the other extreme, distinct clusters would share similar sets of fates (Figure 3a, right). In an intermediate model, fates of precursor clusters would exhibit partial overlap.

![Figure 3.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig3-v2.jpg)

**Figure 3.:** (a) Top: specified (left) and nonspecified (right) modes of diversification. Nodes denote transcriptomic clusters of immature RGCs, and arrows denote fate relationships. Bottom: confusion matrices depicting transcriptomic correspondence between late and early clusters expected for the two modes. Circles and colors indicate the percentage of a given late cluster (row) assigned to a corresponding early cluster (column) by transcriptome-based classifier trained on early clusters. The number of late and early clusters has been set to 8 and 4 for illustration purposes. (b) Barplot showing values of the normalized conditional entropy (NCE) for each age calculated using the transcriptional cluster IDs and the XGBoost-assigned cluster IDs corresponding to the next age or to postnatal day (P)56 (e.g., for embryonic day [E1]3, the NCE was calculated across E13 RGCs by comparing their transcriptional cluster ID with the assigned E14 cluster IDs based on a classifier trained on the E14 data). Lower values indicate specific mappings. (c) Same as (b), but plotting values of the adjusted Rand Index (ARI), where larger values correspond to higher specificity. (d–h) Confusion matrices (representation as in a), showing transcriptomic correspondence between consecutive ages: E14–E13 (d), E16–E14 (e), P0–E16 (f), P5–P0 (g), and P56–P5 (h). In each case, the classifier was trained on the late time point and applied to the early time point. Rows sum to 100%.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (a–d) Confusion matrices showing transcriptomic correspondence between adult retinal ganglion cell (RGC) types at postnatal day (P)56 (rows) and immature RGC clusters (columns) at ages embryonic day (E)13 (a), E14 (b), E16 (c), and P0 (d). In each case, immature RGCs were assigned adult labels using an XGBoost classifier trained on adult RGCs. The P56 to P5 mapping is shown in Figure 3h. (e) Line plots showing occupancy fraction (OF) of mapping of an early cluster to cluster IDs at later ages. OF values quantify the specificity of mapping of an early cluster to late clusters, with lower values denoting higher specificity. The average OF across clusters decreases steadily with age consistent with the decrease and increase in normalized conditional entropy (NCE) and adjusted Rand Index (ARI), respectively (Figure 3b and c). Error bars indicate standard deviation computed across clusters. Also, as expected, the OF values are lower for mapping to adjacent time points than to P56.

As a first step in discriminating among these scenarios, we used transcriptome-wide correspondence among clusters as a proxy for fate association. We identified mappings between clusters across each pair of consecutive developmental stages (E13–E14, E14–E16, E16–P0, P0–P5, and P5–P56) using gradient boosted trees (Chen and Guestrin, 2016), a supervised classification approach (Materials and methods). In each case, a classifier trained on transcriptional clusters at the older stage was used to assign older cluster labels to cells at the younger stage (e.g., E16 labels assigned to E14 RGCs). Patterns expected for the extreme models are schematized as ‘confusion matrices’(Stehman, 1997) in the lower panels of Figure 3a.

Correspondence fell between the two extremes (Figure 3d–h, Figure 3—figure supplement 1a–d). We quantified the extent of correspondence using two metrics: normalized conditional entropy (NCE) and the adjusted Rand Index (ARI) (Materials and methods). Both NCE and ARI are restricted to the range (0,1), with lower values of NCE and higher values of ARI consistent with a specified mode of diversification. Both metrics exhibited an increased degree of specificity with age (Figure 3b and c). Since NCE and ARI provide a single measure of specificity for the entire datasets being compared, we also computed a ‘local metric,’ the occupancy fraction (OF), which quantifies mapping specificity for each cluster (Materials and methods). Results based on this metric were consistent with increased specificity of correspondence with age (Figure 3—figure supplement 1e). Overall, this analysis of transcriptomic correspondence suggests that poorly specified relationships among transcriptomic clusters at early stages are gradually refined to yield increasingly specific associations at later stages.

### Immature RGCs are multipotential

The classification analysis presented so far relied on comparing clusters between ages and was therefore unable to link individual precursors to specific terminal fates. At one extreme, individual precursor clusters might contain several groups of cells, each committed to a distinct, small number of fates. Alternatively, individual cells might be as multipotential as the clusters in which they reside (Figure 4a).

![Figure 4.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig4-v2.jpg)

**Figure 4.:** (a) Extreme models of diversification at single-cell resolution. Multipotential fate associations in a transcriptionally defined cluster (ellipse) could arise from a mixture of unipotential RGCs (left) or from multipotential RGCs (right). (b) Distributions of potential P across immature RGCs by age showing that restriction increases with age. (c) Inter- and intra-cluster variation of potential by age. At each age, variation in the potential values is shown for each transcriptomically defined cluster at that age. Dots denote the average potential, and dotted lines depict the standard deviation for cells within each cluster. (d–h) Uniform Manifold Approximation and Projection (UMAP) projections of embryonic day (E)13 (d), E14 (e), E16 (f), postnatal day (P)0 (g), and P5 (h) RGCs as in Figure 2, but with individual cells colored by their inferred potential. Potential of all RGCs at P56 = 1. The colorbar on the lower right is common to all panels, and values are thresholded at P = 20.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (a) Variations in WOT-inferred temporal couplings ($Π_{ij}$) at the level of cells and clusters to changes in the set of highly variable genes (HVGs) used for computing transport maps. Four sets of features were tested corresponding to the top 800, 1100, 1400, and 1800 HVGs based on our previously described Poisson-Gamma model (Liu et al., 2018). Using these sets, we inferred four corresponding transport maps at each of the five age pairs embryonic day (E)13–E14, E14–E16, E16–postnatal day (P0), P0–P5, and P5–P56. The entropic regularization hyperparameter $ϵ$ (see panels b, c) was held constant at a value 2–7 in these tests. At each age pair, we computed the Pearson correlation coefficient (PCC) between estimated temporal couplings for every older cell (column of the transport map $Π$) across each pairwise combination of the four transport maps, towards a total of six combinations. These are indicated as red dots and lines (mean ± SD). We then grouped (summed) the rows of the transport map by transcriptomic cluster at the younger age, such that each element of the new matrix indicates cell (column)–cluster (row) couplings. The PCC values of these couplings were computed for each older cell (column) within each pairwise combination of the four transport maps and are indicated as green dots and lines (mean ± SD). Finally, we grouped (summed) both the rows and columns of the transport map by transcriptomic cluster at either age to obtain a matrix of cluster–cluster couplings. The PCC values of these couplings were computed for each older cluster within each pairwise combination of the four transport maps and are indicated as blue dots and lines (mean ± SD). We find that the cell–cell couplings increase in robustness at later ages, but the cell–cluster and cluster–cluster couplings are quite robust (correlation >0.6). (b) Variations in WOT-inferred temporal couplings at the level of cells and clusters as in panel (a), but to changes in the entropic regularization $ϵ$. Six values were used (2–8 , 2–7 , 2–6, 2–5, 2–4, 2–3) with increasing values corresponding to more transport maps with decreasingly localized (or increasingly distributed) couplings. At each age pair, six transport maps are computed and PCC values for cell–cell, cell–cluster, and cluster–cluster couplings are computed as in panel (a) for each of the 15 transport map pairs. Here too, the cluster–cluster and cell–cluster couplings show higher stability, although at later stages higher values of $ϵ$ exhibit loss of stability even at the cluster–cluster level (see panel c). (c) Heatmap showing cluster–cluster PCC values for P5–P56 transport maps inferred using different values of the entropic regularization parameter, epsilon (rows and columns). Loss of stability occurs at higher values of the entropic regularization, consistent with panel (b). Based on this, we used ε = 2–7 to calculate the results shown in Figure 4.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (a–e) Average temporal couplings at the level of clusters. Panels correspond to the pairs embryonic day (E14)–E13 (a), E16–E14 (b), postnatal day (P0)–E16 (c), P5–P0 (d), and P56–P5 (e), respectively. In each case, the WOT-inferred transport map was grouped along rows and columns based on transcriptomic cluster, and the elements were summed within each group. The resulting matrix was normalized such that each row sums to 100%. These matrices strongly resemble those in Figure 3d–h, as confirmed by the high values of the Pearson correlation coefficient (top, all P ≥ 0.92).

Unfortunately, this approach does not afford a straightforward way to explore variations in patterns of fate associations within clusters. We therefore turned to Waddington optimal transport (WOT), a computational method rooted in optimal transport theory (Kantorovich, 2006; Monge, 1781) that utilizes scRNA-seq measurements at multiple stages to infer developmental relationships (Schiebinger et al., 2019). Briefly, WOT computes a ‘transport matrix’ $Π$ between each pair of consecutive ages with elements $Π_{ij}$ encoding fate associations between a single RGC i at the younger age and RGC j at the older age (see Materials and methods). WOT directly computes fate associations at the level of individual cells without requiring clustering as a prior step. We conducted computational tests to assess the numerical stability of associations reported by WOT (Figure 4—figure supplement 1). We also determined that when collapsed to the level of clusters the WOT-inferred transport maps strikingly mirrored the confusion matrices obtained from multi-class classification (Figure 4—figure supplement 2).

Based on the success of these tests, we applied WOT to compute the ‘terminal fate’ for each precursor RGC. We leveraged the fact that in WOT fate associations between RGCs at nonconsecutive ages (e.g., E16 and P56) can be estimated in a principled way by multiplying the intermediate transport matrices. This yielded a fate vector $f→  $ for each of the 75,115 immature RGCs, whose kth element $f_{k}$ represents the predicted probability of commitment to adult type $k\in(1, 2, …, 45)$ (Materials and methods). A fully committed precursor would have all but one element of $f→$ equal to zero, whereas a partially committed precursor would have multiple nonzero elements in $f→$ . Since the elements of $f→$ are interpreted as probabilities, they are normalized such that $\sum_{k}f_{k}=1$.

We quantified the commitment of each precursor by computing its ‘potential’ $P=\frac{1}{\sum_{k}f_{k}^{2}}$ , which is defined analogously to the ‘inverse participation ratio’ in physics (Fyodorov and Mirlin, 1992). In our case, the value of P for a given RGC ranges continuously between 1 and 45, with lower values implying a commitment to specific fates and higher values reflecting indeterminacy. Importantly, this measure of commitment does not rely on arbitrary thresholding of the $f_{k}$ values to assign precursors to types.

Five results emerged from this analysis.

From these results, we conclude that early postmitotic RGCs are multipotential but not totipotential, and that type identity is specified gradually via progressive restriction.

### Asynchronous specification of mouse RGC types via fate decoupling

As a first step in understanding the progressive restriction of RGC fate, we analyzed the extent to which pairs of mature types were likely to have arisen from the same set of immature precursors. To this end, we computed a ‘fate coupling’ value $C(l,m;age)$ for each pair of terminal RGC types (l and m), defined as the Pearson correlation coefficient between the values of $f_{l}$ and $f_{m}$ across all precursors at a given age (Materials and methods). $f_{l}$ and $f_{m}$ are fate probabilities corresponding to types l and m as defined in the previous section. Values of $C(l,m;age)$ in our data ranged from –0.11 to 0.95. Higher values of $C(l,m;age)$ indicate strong fate coupling between types l and m, implying the existence of common postmitotic precursors, whereas low $Cl,m;age$ values suggest that types l and m arose from largely nonoverlapping sets of precursors. We visualized the pattern of fate couplings as network graphs, where the nodes represent types and the edge weights represent values of $C(l,m;age)$. The arrangement of nodes was determined at E13 using a force-directed layout algorithm (Fruchterman and Reingold, 1991), with pairwise distances being inversely proportional to the values of $C(l,m;E13)$, the fate coupling values at E13 (Figure 5a). To visualize the temporal evolution of these fate couplings, we retained the same layout of nodes while updating edge weights according to $C(l,m;age)$ (Figure 5b–e).

![Figure 5.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig5-v2.jpg)

**Figure 5.:** (a) Force-directed layout visualization of fate couplings at embryonic day (E)13, with nodes representing RGC types (numbered as in Tran et al., 2019) and the thickness of edges representing values of C(l,m;E13). Edges with C(l,m; E13) < 0.2 are not shown. Number of edges with C(l,m; E13) > 0.2 are indicated on top. (b–e) Visualization of fate couplings at E14 (b), E16 (c), postnatal day (P)0 (d), and P5 (e). The positions of the nodes are maintained as in panel (a), but the edges are redrawn based on values of C(l,m;age) at each age. As in panel (a), we only show edges C(l,m; age) > 0.2. (f) The decay of pairwise fate couplings (y-axis) with age (x-axis). Each line corresponds to the temporal decay of C(l,m) for RGC pair l and m estimated via a logistic model (Materials and methods). For each pair, couplings at each age were fit to a model $Cl,m;age=1/(1+e^{\beta_{0}+\beta_{1}*age})$ with $\beta_{0}, \beta_{1}$ representing fitted parameters. The fitting was performed using data for ages E13, E14, E16, P0, and P5. The shaded portions correspond to the periods E8–E13 and P5 representing the extrapolations of the model. Black lines highlight the decay of all nonzero pairwise couplings for RGC type C8 as an example. (g) Schematic showing logistic modeling to estimate specification time $\tau_{sp}$ for a particular type. The y-axis is a measure of the extent to which precursors biased towards the type are present in a single transcriptomically defined cluster (i.e., localization, see Materials and methods for details). Localization is defined as a numerical value in the range (0, 1) with higher values consistent with increasing specification. Individual triangles represent the localization values computed using Waddington optimal transport (WOT)-inferred fate couplings at each age, while the curve represents the fit using the logistic model. Dotted line shows the minimum threshold a type to be specified at each age. Its curved shape arises due to the increase in the number of clusters with age. (h) Localization curves (as in g) for the 38 RGC types showing the range of inferred specification times. Seven low-frequency types have been excluded from display (see Figure 5—figure supplement 1d). (i) Scatter plot showing poor correlation between adult frequency of a type (from Tran et al., 2019) and its predicated specification time (calculated from h).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (a–c) Examples of fate decoupling. Panels from left to right correspond to ages embryonic day (E)13–postnatal day (P)5 with precursor RGCs shown on a reduced dimensional Uniform Manifold Approximation and Projection (UMAP) representation as in Figure 2c–g. Each RGC is colored using a biaxial color scale (legend) based on its predicted fate values. C12 and C22 are transcriptomically distinct as early as E13 (a). C19 and C20 exhibit high fate coupling at all embryonic ages and are only decoupled at P5 (b). C21 and C34 decouple around E16 (c). (d) Same as Figure 6h showing specification curves for RGC types, but in this case each curve is colored based on adult frequency (colorbar, right). The seven curves marked by asterisks correspond to late-specified types. As can be seen from their colors, they are also among the types with the lowest frequency (<0.3%), which may result in the dropout of the corresponding precursors because of sampling fluctuations. Such dropouts at earlier time points give the appearance of late specification. Because of this issue, we exclude them from our analysis.

Types that were coupled in fate at the earliest time point gradually decoupled as development proceed. For example, at E13, 118/990 pairs (12%) were strongly coupled (threshold of $C(l,m;age)$>0.2 as determined by randomization tests; see Materials and methods), while at P5, only 8/990 (<1%) passed this criterion (Figure 5a and e). Lowering this threshold for coupling to 0.05 increased the number of strongly coupled pairs at P5 to only 2% (20/990).

Different pairs of types decoupled at different rates (Figure 5f). As they decoupled, RGC precursors became increasingly restricted to a single type (i.e., $f_{k}≫f_{l\neqk}$ for a precursor favoring type k). This corresponded to a ‘localization’ of precursors in transcriptomic space and is a proxy for specification (see Materials and methods). We modeled the extent of localization vs. age via a logistic function (Figure 5g, Figure 5—figure supplement 1d) and used this to calculate a specification time for each type ($\tau_{sp}$) (see Materials and methods for details). Based on this analysis, 7/45 types are specified postnatally. The average $\tau_{sp}$ for RGCs was E17.8, but individual RGC types exhibited a wide range from E13.9 to P5.2 (Figure 5h). The inferred specification time was not correlated with adult frequency (Figure 5i).

We illustrate this range by considering three pairs of RGC types in Figure 5—figure supplement 1. C12 and C22 (numbered as in Tran et al., 2019; see Figure 2g) exhibit low fate coupling at all ages profiled (Figure 5—figure supplement 1a), indicative of separate precursor populations. In contrast, C19 and C20 decouple only at P0, implying the existence of a common precursor throughout embryogenesis (Figure 5—figure supplement 1b). C21 and C34 display an intermediate pattern, decoupling around E16 (Figure 5—figure supplement 1c). Taken together, these results suggest that RGC types emerge by asynchronous fate decoupling of multipotential precursors.

### Fate decoupled groups of RGC types defined by transcription factors

Because fate coupling is a metric of inferred overlap of developmental history, it is likely that tightly coupled types share common precursors. This relationship implies that tightly coupled types might also be specified by common transcriptional programs. As a step towards identifying candidate fate determinants, we identified eight TFs that are expressed by distinct groups of mature RGC types (Figure 6a, Figure 6—figure supplement 1a). Three of these are well-characterized RGC-selective TFs: Foxp2, expressed by five F-RGC types (Rousso et al., 2016); Tbr1, expressed by five T-RGC types (Liu et al., 2018); and Eomes (also known as Tbr2), expressed by seven types (Mao et al., 2020; Tran et al., 2019). The seven Eomes/Tbr2 types include the melanopsin-expressing intrinsically photosensitive (ip) RGC types (Berson et al., 2002). The remaining five were Neurod2, Irx3, Mafb, Tfap2d, and Bnc2, which label 8, 5, 4, 6, and 3 types, respectively. Eomes types also co-expressed Tbx20 and Dmrbt1 while Neurod2 types also co-express Satb2. Together, 40/45 mature types expressed at least one of these TFs in a manner that was, with a few exceptions, mutually exclusive. In many cases, the fate proximity of types that shared TF expression was obvious (Figure 6a).

![Figure 6.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig6-v2.jpg)

**Figure 6.:** (a) Embryonic day (E)13 network graph of fate couplings from Figure 5a, with RGC types colored based on their selective expression of TFs at postnatal day (P)56. Asterisks denote 3/45 types that express more than one TF (also see Figure 6—figure supplement 1a). (b) Box-and-whisker plots showing that pairwise fate couplings are higher between types within the same TF subclass than between types in different TF subclasses at all immature ages. Black horizontal line, median; bars, interquartile range; vertical lines, 1st and 99th percentile; dots, outliers. Asterisks indicate significant p-values based on a two-sided t-test (****p<10–7; ***p<10–5; **p<10–2). (c) Eomes+ types. Top: Uniform Manifold Approximation and Projection (UMAP) representation of E13 RGCs with cells colored based on their cumulative fate association towards the seven Eomes+ types. Bottom: UMAP representation of P5 RGCs with cells colored based on their cumulative fate association towards the seven Eomes+ types. The value corresponding to the color of each cell (colorbar, right) can be interpreted as the probability of commitment towards the corresponding subclass. Note that the color does not denote the expression level for the gene. (d) Same as (c) for Mafb+ types. (e) Same as (c) for Neurod2+ types (f–h). Localization curves (as in Figure 5g) for Eomes+ types (f), Mafb+ types (g), and Neurod2+ types (h). The mean inferred specification time $\tau_{sp}$ for each group is indicated on the top of each panel.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (a) Dotplot showing mutually exclusive patterns of expression of TFs that mark groups of retinal ganglion cell (RGC) types. In addition to the eight TFs shown in Figure 6a, we highlight Zic1, which selectively labels C6. Selectively expressed TFs could not be identified for four types (C1, C2, C11, and C15). (b–e) Localization curves (as in Figure 5g) for Tbr1+ types (b), Tfap2d+ types (c), Foxp2+ types (d), and Bnc2+ types (e). Note that the ‘low-frequency’ types labeled in Figure 5—figure supplement 1d are not shown. The mean specification time $\tau_{sp}$ for each group is shown above the graphs. (f) Correlation of fate coupling at embryonic day (E)13 with transcriptomic correlation at postnatal day (P)56. (g) Same as Figure 6a, with nodes corresponding to subclasses defined in Tran et al., 2019, which includes ipRGCs, alpha-RGCs, and T5-RGCs.

We refer to these TF-based groups as fate-restricted RGC subclasses – an intermediate taxonomic level between class and type based on inferred fate relationships. Consistent with their definition, the pairwise fate coupling among types from different subclasses was significantly lower than among types from the same subclass (Figure 6b). Thus, precursor RGC states associated with any two subclasses are more distinct than those associated with any two types. This is evident by the significant separation at E13 and negligible overlap at P5 for precursors favoring the Eomes, Mafb, and Neurod2 subclasses, respectively, as shown in Figure 6c–e.

We also asked whether the TF-based subclasses differed in inferred transcriptomic specification time $\tau_{sp}$ , as defined in Figure 5g. As shown in Figure 6f–h and Figure 6—figure supplement 1b–e, four subclasses were specified within a narrow interval (E16.8–E17.2), but three others differed substantially. The average specification time for the Eomes group was E14.6 (p<0.0001, Student’s t-test, compared to the mean for all types), while that for the Mafb and Neurod2 groups were E16.9 (p<0.001) and E18.5 (p<0.0001), respectively. The early specification of the Eomes group is consistent with birthdating studies showing the average earlier birthdate of ipRGCs compared to all RGCs (McNeill et al., 2011).

In summary, our results suggest the existence of fate-restricted RGC subclasses that arise from distinct sets of precursors and diversify into individual types. This method of defining RGC groups, which relies on inferred proximity of precursors in transcriptomic space, is distinct from previous definitions of RGC subclass based on shared patterns of adult morphology, physiology, or gene expression (see Discussion). Accordingly, the fate couplings at E13 were only weakly correlated with transcriptomic proximity in the adult retina (Figure 6—figure supplement 1f). Further, while TF-based groups align with some previously defined subclasses (e.g., ipRGCs or Tbr1+ RGCs), they do not map to other subclasses such as alpha-RGCs (four types) or T5-RGCs (nine types) (Figure 6—figure supplement 1g).

### Transcriptomic profiles of ipsilateral and contralateral RGCs

Finally, we considered the origin of two RGC groups defined by their projections: those with axons that remain ipsilateral at the optic chiasm (I-RGCs) and those that cross the midline to innervate contralateral brain structures (C-RGCs). The proportion of I-RGCs varies among vertebrates, in rough correspondence to the extent of binocular vision, ranging from none in most lower vertebrates to ~50% in primates. In mice, 3–5% of RGC axons remain ipsilateral, with most I-RGCs residing in the ventrotemporal (VT) retinal crescent (Mason and Slavi, 2020). While some I-RGCs have been observed to project from the dorsocentral retina during embryonic stages, these are rapidly eliminated so-called ‘transient’ I-RGCs (Soares and Mason, 2015). Thus, in adulthood, C-RGCs are present throughout the retina while ‘permanent’ I-RGCs are confined to the VT crescent.

The zinc-finger TF Zic2 is expressed in a subset of postmitotic RGCs in VT retina and is both necessary and sufficient for establishing their ipsilateral identity (Herrera et al., 2003); transient dorsolateral I-RGCs do not express Zic2 (Pak et al., 2004). Isl2 marks a subset of C-RGCs throughout the retina and appears to specify a contralateral identity in part by repressing Zic2 (Pak et al., 2004). These two TFs were expressed in a mutually exclusive fashion in RGC precursors between E13 and E16 (Figure 7a); Zic2 was downregulated at later ages (Figure 7—figure supplement 1a). Furthermore, Zic2 expression at E13 correlated with Igfbp5 and Zic1, and anticorrelated with Igf1 and Fgf12, consistent with recent reports (Wang et al., 2016; Figure 7b, Figure 7—figure supplement 1b and c). We scored each cell at E13 based on its expression of ipsilateral genes (Materials and methods), confirming that the expression of ipsilateral and contralateral gene signatures was anticorrelated (Figure 7c). Together, these observations support the idea that at E13 Zic2+ cells represent I-RGCs and Isl2+ cells represent some but not all C-RGCs.

![Figure 7.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig7-v2.jpg)

**Figure 7.:** (a) Zic2, an I-RGC marker, and Isl2, a C-RGC marker, are expressed in a mutually exclusive pattern at embryonic day (E)13 (left), E14 (middle), and E16 (right). Zic2 is undetectable after E16 (Figure 7—figure supplement 1a). Cells are colored based on a bivariate color scale representing co-expression of two markers (colorbar, right). (b) Zic2 and Igfbp5, two I-RGC markers, are co-expressed at E13 (left) and E14 (middle). Representation as in panel (a). (c) Scatter plots of gene signatures used to identify I-RGCs (y-axis) and C-RGCs (x-axis) at E13 are negatively correlated (Pearson R = –0.61). Each dot corresponds to a cell, the color represents the number of cells located at a particular (x, y) location (see colorbar, right). (d) Barplot showing % of putative I-RGCs (y-axis) within each of the 45 adult RGC types, estimated by computing the descendants of E13 I-RGCs using Waddington optimal transport (WOT). RGC types are arranged along the x-axis based on their membership of transcription factor (TF) groups shown in Figure 6a (annotation matrix, bottom). (e) Volcano plot showing differentially expressed genes (MAST test) between predicted I-RGCs and C-RGCs at E13. The x- and the y-axes show the fold change and the p-value in log2- and log10- units, respectively. Dots represent genes, with red and blue dots highlighting I- and C-RGC-enriched genes, respectively, at fold change >1.5 and Bonferroni-corrected p-value<5 × 10–5. The two vertical bars correspond to a fold change of 1.5 in either direction. Select I-RGC- and C-RGC-enriched genes are labeled. (f) Same as panel (e), for E14.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/73809/elife-73809-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (a) RGCs at embryonic day (E)13, E14, E16, postnatal day (P)0, and P5 colored by their expression of Zic2, an I-RGC marker. Zic2 is expressed in a localized fashion until E16 and becomes undetectable beyond this age. (b) Zic2, an I-RGC marker, and Igf1, a C-RGC marker, are expressed in mutually exclusive patterns at E13–E16. (c) Zic2 and Zic1, two I-RGC markers, are co-expressed in subsets of RGCs at E13–E16. (d) Volcano plot showing differentially expressed genes (MAST test, p<10–6) between predicted I-RGCs and C-RGCs at E16. The x- and the y-axes show the fold change and the p-value in log2- and log10- units, respectively. Dots represent genes, with red and dots highlighting I- and C-RGC-enriched genes, respectively, at fold change >1.5 and Bonferroni-corrected p-value<5e-5. The two vertical bars correspond to a fold change of 1.5 in either direction. (e) Same as (d), for P0.

Using WOT, we then identified the descendants of presumptive I-RGCs at later ages. We found that I-RGCs comprised 4.3% of adult RGCs, consistent with the range of 3–5% noted above. We queried these cells to identify the genes that distinguished putative I-RGCs and C-RGCs throughout the developmental time course. At a fold change of ≥1.5, we found 59 differentially expressed (DE) genes at E13 and 89 at E14 (Figure 7e and f). In addition to Zic2, Igfbp5, Isl2, and Igf1, which had been used to define I-RGCs and C-RGCs at E13, they included Igfbpl1, Pou3f1, and Cntn2 enriched in I-RGCs, and Lmo2, Pcsk1n, and Syt4 enriched in C-RGCs. The number of genes differentially expressed between I- and C-RGCs decreased after E14, with 20, 9, and 0 significant genes at E16, P0, and P5, respectively (Figure 7—figure supplement 1d and e), presumably reflecting the downregulation of axon guidance programs once retinorecipient targets have been reached (see Discussion).

We also asked which RGC types included I-RGCs. At E13, putative I-RGCs were highly enriched in 2 of 10 clusters, comprising 38–40% of clusters 2 and 9, 9–14% of clusters 3 and 5, and <2% of the other six clusters (Figure 7d). In adults, RGCs expressing Tbr1, Mafb, Foxp2, and Neurod2 contained 3–4× more I-RGCs than RGCs expressing Eomes, Irx3, or Tfap2d. These results are consistent with previous observations that I-RGCs are morphologically and physiologically heterogenous but not uniformly distributed across types (Hong et al., 2011; Johnson et al., 2021). Lastly, the WOT-predicted relationship between E13 precursor RGC clusters and I-RGC-rich or -poor terminal types was consistent with these patterns. The top six I-RGC-rich types (C4, C15, C19, C20, C38, and C45) derived 14 and 4% of their relative fate association from E13 clusters 2 and 9, while the top six I-RGC-poor types (C8, C14, C18, C22, C31, and C41) derived only 3.8 and 0.2% of their relative fate association from E13 clusters 2 and 9. Thus, E13 clusters 2 and 9 are preferred precursors of adult types that are relatively rich in I-RGCs.

## Discussion

The staggering diversity of its neurons underlies the computational power of the nervous system. Accordingly, a major quest in developmental neurobiology is to understand the mechanisms that diversify progenitors. A generally accepted way to deal with this diversity is to divide neurons into classes, and then subdivide classes into subclasses and subclasses into types (Zeng and Sanes, 2017). While much has been learned about how neural progenitors give rise to distinct neuronal classes, little is known about how classes diversify into subclasses and types.

Here, we used mouse RGCs to address this issue. We recently generated a molecular atlas that divided RGCs into ~45 distinct types based on their patterns of gene expression (Tran et al., 2019). We used this atlas here as a foundation to ask how these types are specified during development. We conclude that the earliest precursor RGCs are multipotential and exhibit continuous variation in transcriptomic identity, then diversify into definitive types by a gradual process of fate restriction. Interestingly, these features resemble those that have been discovered to control the generation of retinal cell classes from cycling progenitors (RPCs): multipotentiality, progressive restriction of fate, and stochastic rather than deterministic fate choice (see Introduction). We suggest that, at least in this case, similar strategies are used to generate cell classes from mitotically active progenitors and cell types from postmitotic precursors.

### Classes, subclasses, and types

Definitions of neuronal class, subclass, and type have been contentious (Yuste et al., 2020). In general, classes share general features of structure, function, molecular architecture, and location, whereas types comprise the smallest groups within classes that can be qualitatively distinguished from other groups based on these and other criteria. Subclasses lie in-between. For RGCs, class identity has been clear for a century, but inventories of subclasses and types have emerged only over the last few decades as high-throughput methods have been implemented for quantifying structural (primarily dendritic morphology), functional (responses to an array of visual stimuli), and molecular properties (gene and transgene expression) of large numbers of RGCs. Fortunately, to the extent that they have been compared, there is excellent concordance among types defined by molecular, structural, and physiological criteria (Bae et al., 2018; Goetz et al., 2021; Tran et al., 2019; see http://www.rgc.types.org). Moreover, RGCs of a single type exhibit a regular spacing, called a mosaic arrangement, in that they tend to avoid other members of the same cell type, whereas their association with members of other types is random (Kay et al., 2012; Keeley et al., 2020; Rockhill et al., 2000). The molecular basis of this property is poorly understood, but it provides an additional criterion for defining a type. Thus, while no two RGCs are identical, and variation may be continuous in some other structures (Cembrowski and Spruston, 2019), there is strong reason to believe that RGC types are discrete.

### The adult RGC atlas

Developmental trajectories of cell types cannot be better than the adult types at which they are aimed. We have two reasons to believe that our adult RGC atlas (Tran et al., 2019) is accurate and complete.

First, the atlas is based on a detailed analysis of 35,699 cells and is therefore powered to detect types occurring at ~0.1% frequency (>40 cells per type; https://satijalab.org/howmanycells/). Results were stable over a variety of parameters (Tran et al., 2019). Moreover, in the course of studies on responses of RGCs to injury, we recently profiled an additional ~120,000 cells (A. Jacobi, N. Tran, W Yan, and J.R.S, in preparation), without identifying additional types.

Second, RGCs have now been classified by functional and structural properties, based on physiological responses to visual stimuli (Baden et al., 2016; Goetz et al., 2021) and serial section electron microscopy (Bae et al., 2018). The numbers of types defined in these ways (47 in Bae et al., 2018, 42 in Goetz et al., 2021, and >32 in Baden et al., 2016) match well to the 45–46 defined molecularly (Tran et al., 2019).

### Multipotentiality of precursor RGCs

The multipotentiality of dividing progenitor cells can be demonstrated by indelibly labeling a progenitor and then examining its progeny at a later stage. For mammals, this was initially done by infecting single cells with a recombinant retrovirus encoding a reporter gene that could be detected following multiple cell divisions (Price et al., 1987; Sanes et al., 1986; Turner and Cepko, 1987). More recently, it has become possible to greatly increase throughput by tracking scars or barcodes introduced by CRISPR/Cas9 (Baron and van Oudenaarden, 2019; Espinosa-Medina et al., 2019; McKenna et al., 2016). In sharp contrast, conclusively demonstrating that a single postmitotic cell is multipotential would require following a cell from an unspecified to a specified state, then turning back time, watching it again, and asking if it acquired the same mature identity. Since this is impossible, we used computational methods to draw tentative conclusions about the extent to which newly postmitotic RGCs are committed to mature into a particular type based on their transcriptomic profiles. Consequently, our results are based on inferred rather than experimentally determined lineages.

Our analysis proceeded in three steps. First, to ask whether RGCs were committed to a particular fate before or shortly after they were born, we assessed transcriptomic heterogeneity at a time when a large fraction was newly postmitotic (E13 and E14). We found that heterogeneity was present but limited: 10 transcriptomic clusters were distinguishable at E13 and 12 at E14. Thus, some heterogeneity is present in precursor RGCs, but far less than would be required to specify type identity before or immediately after their birth. A relevant issue is whether at these early stages the transcriptomic variation among cells could reflect variation in their stages of differentiation, perhaps as a consequence of different intervals between birthdate and sampling. Although we cannot exclude this possibility, inter-cluster variability of key RGC-specific genes (e.g., Rbpms) was no greater at early times than in adults (data not shown).

Second, we used a supervised classification approach to ask whether precursor RGC clusters mature into mutually exclusive sets of adult types. This model would imply an orderly, step-wise restriction of cell fates. However, our results indicate substantial overlap in the types derived from cells in different immature clusters. This result argues against a deterministic model of diversification and suggests that precursor RGCs are incompletely committed to a specific type for a substantial period after they are generated.

Third, we used optimal transport inference (WOT) to ask whether the multipotentiality observed at the level of groups was also a property of individual cells. This approach circumvents the limitation of the supervised classification approach, which compares similarity only at the level of clusters. WOT utilizes time-course scRNA-seq snapshots to infer fate associations between individual cells sampled at different time points, without reference to the clusters in which they reside (Schiebinger et al., 2019). While being consistent with supervised classification results at the cluster level, WOT indicated that the majority of individual RGCs were multipotential at E13 and E14. Of equal importance, immature RGCs were not totipotential: the average predicted potential (P) was 11.6 at E13, or ~25% of the maximum possible value of 45, and no RGCs had P > 30. We conclude that single multipotential immature RGCs are biased in favor of particular groups of adult RGC types.

### Progressive restriction of RGC fate

Further analysis provided insight into the structure of multipotentiality among RGCs. The adult RGC types associated with a precursor RGC were not a randomly chosen subset; rather some were more likely to arise from a common precursor state (‘fate coupled’) than others. This suggests a model in which RGC types arise via a progressive decoupling of fates within multipotential precursors. Decoupling is asynchronously, with different types emerging at different times. By modeling the temporal kinetics of fate decoupling, we were able to estimate a tentative specification time for each type – that is, the time at which precursors acquire a distinct transcriptomic identity. Analysis of transcriptomic changes that occur during this process, and the effects of visual experience on maturation, will be presented elsewhere (K.S., I.E.W., S.B. and J.R.S., in preparation).

Our conclusions about fate restriction are based on analyzing cell states defined by expression patterns of highly variable genes (HVGs) identified in the data (Figure 2h). An alternative and common view is that if a small set of genes is sufficient to define cell state, they should be the focus of analysis. We believe this is an incorrect argument based on confusion between genes that determine a cell type or state and those that define it. The only way a small number of genes, whatever their functional role, can exclusively define cell state is if they are expressed at very high levels. If this were the case, they would be detected in our data and drive the clustering.

### Fate-restricted RGC subclasses

For RGCs, class identity has been clear for a century, and type identity has been solidified during over the last few decades, but criteria for defining subclasses remain unclear. Tentative classifications have used molecular, physiological, and morphological criteria (Sanes and Masland, 2015; Tran et al., 2019). In general, these criteria correlate imperfectly with each other, a main exception being that ON and OFF RGCs (responding preferentially to increases and decreases in illumination, respectively) have dendrites that arborize in the inner and outer portions of the inner plexiform layer (Famiglietti and Kolb, 1976).

The pattern of fate couplings between RGC types at E13–14 provides an alternative way to define RGC subclasses – groups of RGC types that arise from the restriction of a common transcriptionally defined precursor state. We identified TFs selectively expressed within these subclasses. Our rationale was that among them would be fate determinants, an idea that could be tested by conventional genetic manipulations. Support for this idea is that there is already strong evidence that one such factor is a fate determinant in mouse: Eomes is selectively expressed by ipRGCs (and a few other types), and Eomes mutants fail to form ipRGCs although their retinas are normal in many respects (Mao et al., 2014). This encourages the hope that some of the other TFs in this set are also fate determinants. It will also be interesting to determine whether members of fate-restricted subclasses share structural or functional properties.

### Laterality

The TFs Isl2 and Zic2 are selective markers of embryonic RGCs that project contralaterally or ipsilaterally, respectively, and are critical determinants of this choice (Herrera et al., 2003; Pak et al., 2004). We found that their expression was largely nonoverlapping in RGCs at E13, and that they were co-expressed with previously reported markers of contralaterally and ipsilaterally projecting RGCs, respectively. Because few RGC axons reach the optic chiasm before E14, our results are consistent with genetic evidence that this differential expression is a cause rather than a consequence of the divergent choices the axons make at the chiasm. Among many genes co-expressed with Isl2 or Zic2 may be others that play roles in this choice.

Zic2 is downregulated later in embryogenesis, so we selected some RGCs as putative I-RGCs using genes known to be expressed in them (Wang et al., 2016), then used WOT to infer the RGC types to which they gave rise. Our analysis suggests that I-RGCs comprise many differentiated types, consistent with previous results (Hong et al., 2011; Johnson et al., 2021). Surprisingly, however, there were few if any genes differentially expressed between the putative mature I- and C-RGCs. Assuming that WOT results are valid – an assertion that can be tested directly in the future – this result suggests a model in which newborn RGCs are doubly specified – by laterality and type – but that once axonal choice has been made the laterality program is shut down.

### Beyond the retina

Generation of neuronal classes has been analyzed in many parts of the vertebrate nervous system, but we are aware of few reports on how classes diversify into types. A recent study addressed this issue for primary sensory neurons and reached the conclusion that newborn neurons in dorsal root ganglia are transcriptionally unspecialized and become type-restricted as development proceeds (Sharma et al., 2020). Similarly, both excitatory neuronal subclasses appear to diversify postmitotically in the mouse cerebral cortex (Di Bella et al., 2021; Lodato and Arlotta, 2015), and there is suggestive evidence that the same is true for interneuronal subclasses (Wamsley and Fishell, 2017). In all of these cases, it is attractive to speculate that diversification may occur by a process of fate decoupling in subpopulations of distinct multipotential precursors, akin to that documented here for RGCs. Our study provides a computational framework for investigating this issue.

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
      <td>C57BL/6</td>
      <td>Charles River or Jackson Labs</td>
      <td>Cat#JAX000664; RRID: IMSR_JAX:000664</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Thy1/anti-CD90(rat monoclonal)</td>
      <td>Thermo Fisher Scientific</td>
      <td>#17-0902-82</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-L1cam(rat monoclonal)</td>
      <td>Miltenyi Biotec</td>
      <td>#130-102-243</td>
      <td>1:10</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CD90 pre-conjugated (rat monoclonal)</td>
      <td>Miltenyi Biotec</td>
      <td>#130-049-101</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-RBPMS (guinea pig polyclonal)</td>
      <td>PhosphoSolutions</td>
      <td>#1832-RBPMS</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-KI67 (rabbit monoclonal)</td>
      <td>Thermo Fisher Scientific</td>
      <td>#MA5-14520</td>
      <td>1:250</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Fluoro-Gel</td>
      <td>Electron Microscopy Sciences</td>
      <td>#17985</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MACS Large Cell Columns</td>
      <td>Miltenyi Biotec</td>
      <td>#130-042-202</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Drop-seq beads</td>
      <td>ChemGenes Corporation</td>
      <td>#Macosko201110</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Papain dissociation system</td>
      <td>Worthington</td>
      <td>#LK003160</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Chromium Single Cell 30Library and Gel Bead Kit v2, 10X Genomics 16rxns</td>
      <td>10X Genomics</td>
      <td>#120237</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cell Ranger v2.6.0</td>
      <td>10X Genomics</td>
      <td>https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/latest</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ (Fiji) version 2.1.0</td>
      <td>Fiji</td>
      <td>https://imagej.net/Fiji</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R 3.6.2</td>
      <td>The R Foundation</td>
      <td>https://www.r-project.org/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RStudio 1.3.1056</td>
      <td>RStudio</td>
      <td>https://www.adobe.com</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Mice

All animal experiments were approved by the Institutional Animal Care and Use Committees (IACUC) at Harvard University. Mice were maintained in pathogen-free facilities under standard housing conditions with continuous access to food and water. Animals used in this study include both males and females. A meta-analysis (not shown) did not show any systematic sex-related effects in either DE genes or cell-type proportions. For scRNA-seq and histology, we used C57Bl/6J (JAX #000664). Embryonic and early postnatal C57Bl/6J mice were acquired either from Jackson Laboratories (JAX) from time-mated female mice or time-mated in-house. For timed-matings, a male was placed with a female overnight and removed the following morning (with the corresponding time recorded as E0.5).

### Cell preparation

RGCs were enriched from dissociated retinal cells as previously described with minor modifications (Tran et al., 2019). All solutions were prepared using Ames' Medium with L-glutamine and sodium bicarbonate (equilibriated with 95% O2/5% CO2), and all spin steps were done at 450 × g for 8 min. Retinas were dissected out in their entirety immediately after enucleation and digested in ~80 U of papain at 37°C, with the exception of some E13 and E14 eyes that were digested whole, followed by manual trituration in ovomucoid solution. Clumps were removed using a 40 μm cell strainer and the cell suspension was spun down and resuspended in Ames + 4% BSA at a concentration of 10 million cells per 100 μl. Cells from E13, E14, E16, and P0 were incubated for 15 min at room temperature with antibodies to Thy1 (also known as CD90) and L1CAM pre-conjugated to the fluorophores APC (Thermo Fisher Scientific #17-0902-82) and PE (Miltenyi Biotec #130-102-243), respectively. Cells were washed with 6 ml of Ames + 4% BSA, spun down and resuspended at a concentration of ~7 million cells/ml, and calcein blue was added to label metabolically active cells.

Viable Thy1- or L1CAM-positive cells were sorted using a MoFlo Astrios sorter into ~100 μl of AMES + 4% BSA. Sorted cells were spun down a final time and resuspended in PBS + 0.1% BSA at a concentration of 500–2000 cells/μl. P5 RGCs were enriched using only CD90, with either magnetic-activated cell sorting (MACS) using large cell columns and CD90 pre-conjugated to microbeads (#130-042-202 and #130-049-101, Miltenyi Biotec) or fluorescence-activated cell sorting with CD90 pre-conjugated to PE/Cy7 (Thermo Fisher Scientific #25-0902-81), or both.

### Droplet-based single-cell RNA-seq

#### Statement on replicates

We profiled immature RGCs using scRNA-seq at five developmental time points: E13, E14, E16, P0, and P5. At each age, data was collected from four replicate experiments. Experiments at E13, E14, E16, and P0 involved two biological replicates (distinct mice). Each of these biological replicates was further subdivided into two equal pools, and the cells were subjected to two different enrichment methods (anti-Thy1 and anti-L1cam). Thus, each of these time points consisted of four replicate experiments. RGC enrichment at P5 exclusively utilized anti-Thy1, but four biological replicate experiments were performed. One of these was profiled using 10X, and three of these were profiled using Drop-seq.

#### Drop-seq

A subset of P5 RGC dataset was collected using Drop-seq (Macosko et al., 2015), performed largely as described previously (Shekhar et al., 2016). Briefly, cells were diluted to an estimated final droplet occupancy of 0.05, and co-encapsulated in droplets with barcoded beads, which were diluted to an estimated final droplet occupancy of 0.06. The beads were purchased from ChemGenes Corporation, Wilmington, MA (# Macosko201110). Individual droplet aliquots of 2 ml of aqueous volume (1 ml each of cells and beads) were broken by perfluorooctanol, following which beads were harvested, and hybridized RNA was reverse transcribed. Populations of 2000 beads (~100 cells) were separately amplified for 14 cycles of PCR (primers, chemistry, and cycle conditions identical to those previously described) and pairs of PCR products were co-purified by the addition of 0.6x AMPure XP beads (Agencourt). Fifteen experimental replicates were sequenced in total from five biological replicates using an Illumina NextSeq 500. Read 1 was 20 bp; read 2 (paired-end) was 60 bp.

#### 10X Genomics

Single-cell libraries were prepared using the single-cell gene expression 3′ kit on the Chromium platform (10X Genomics, Pleasanton, CA) following the manufacturer’s protocol. As our datasets were collected over a long period of time, we used a combination of v1 (a single channel of P5 RGCs) and v2 (E13, E14, E16, P0). Briefly, single cells were partitioned into Gel beads in EMulsion (GEMs) in the 10X Chromium instrument followed by cell lysis and barcoded reverse transcription of RNA, amplification, enzymatic fragmentation, 5′ adaptor attachment, and sample indexing. On average, approximately 8000–12,000 single cells were loaded on each channel and approximately 3000–7000 cells were recovered. Libraries were sequenced on the Illumina HiSeq 2500 platforms at the Broad Institute (paired-end reads: read 1, 26 bases; read 2, 98 bases).

#### Power analysis

An important question in all single-cell experiments is that of the number of cells to profile. A widely used approach is the power analysis tool published by the Satija lab (https://satijalab.org/howmanycells/). Fortunately, in this study we were also guided by our previous study of adult RGCs, where we had knowledge of the frequency distribution of adult RGC types, with the rarest type being approximately 0.2% (Tran et al., 2019). In that study, we also found that when classification is performed in a supervised fashion based on an existing atlas, approximately ~8000 RGCs were sufficient to recover the accurate relative frequency distribution of 45 RGC types. We therefore aimed to profile ~8000 cell at each time point as our analysis involved mapping immature RGCs to the adult atlas. With the exception of E13, all time points contain 1.5–2× more cells than this target value.

### Histology

#### Tissue fixation

Adult (P56) mice were intracardially perfused with 2–5 ml of PBS followed by 15 ml of 4% PFA, followed by additional fixation of eyes for 15 min in 4% PFA. P0 and P5 mice were not perfused, rather eyes were fixed in 4% PFA for 30 min. At E13, 14, and 16, embryos were fixed whole for 30 min in 4% PFA, following which eyes were removed. Following fixation, eyes from all time points were transferred to PBS and stored at 4°C until subsequent use.

#### Sectioning

Cross sections for immunohistochemistry (IHC) were generated using a Leica CM1850 cryostat. For some early developmental time points, eyes were kept whole for IHC, otherwise retinas were either (1) dissected out in their entirety from eyes or (2) the cornea, iris, and lens were removed, leaving the sclera and retina intact. Tissues were sunk in 30% sucrose overnight at 4°C, embedded in tissue freezing medium, and cryo-sectioned into 25 mm slices. Slides with tissue sections were air-dried for ~3 hr and stored at –80°C until staining.

#### Immunohistochemistry

All IHC solutions were made up in PBS + 0.3% Triton-X, and all incubation steps were carried out in a humidified chamber. Following a 1 hr protein block in 5% normal donkey serum at room temperature, slides were incubated overnight at 4°C with primary antibodies, washed twice for 5 min each in PBS, incubated for 2 hr at room temperature with secondary antibodies conjugated to various fluorophores (1:1000, Jackson Immunological Research) and Hoechst (1:10,000, Life Technologies), and washed again twice for 5 min each in PBS before coverslipping with Fluoro-Gel (#17985, Electron Microscopy Sciences). Primary antibodies used include guinea pig anti-RBPMS (1:1000, #1832-RBPMS, PhosphoSolutions), rabbit anti-KI67 (1:250, #MA5-14520, Thermo Fisher Scientific), and rat anti-L1CAM (1:10, #130-102-243, Miltenyi Biotec).

#### Imaging

All images were acquired using an Olympus Fluoview 1000 scanning laser confocal microscope, with a ×20 oil immersion objective and ×2 optical zoom. Optical slices were taken at 1 μm steps. Fiji was used to pseudocolor each channel and generate a maximum projection from image stacks. Brightness and contrast were adjusted in Adobe Photoshop.

### Alignment and quantification of gene expression in single cells

All single-cell libraries were aligned to the UCSC mm10 transcriptomic reference (Mus musculus), and gene expression matrices were quantified using standard protocols described previously. For the single-cell libraries generated using the 10X platform (E13, E14, E16, P0, and P5), these steps were performed using cellranger v2.1.0 (10X Genomics). For the single-cell libraries generated using Drop-seq (P5), we used Drop-seq tools (v1.12; Macosko et al., 2015), following the procedures described earlier (Shekhar et al., 2016). Alignment and quantification was done for each sample library separately to generate a genes × cells expression matrix of transcript counts. These matrices were column-concatenated for further analysis.

We retained cells that expressed at least 700 genes, resulting in 98,452 cells. We also removed genes expressed in fewer than 10 cells. The resulting M genes × N cells matrix of UMI counts $C_{mn}$ was normalized along each column (cell) to sum to 8340, the median of the column sums resulting in a normalized matrix $X_{mn}$ . This was followed by the transformation $X_{mn}←log⁡(X_{mn}+1)$.

### Overview of clustering analysis

The following procedure was adopted to perform batch correction, dimensionality reduction, and clustering throughout the article. The procedure was first applied on the entire dataset to separate RGCs from other cell classes, and then to RGCs at each age to identify transcriptomically distinct groups.

We began by clustering the full dataset combining all ages using the procedure outlined above. We identified groups of clusters corresponding to cell classes, which included RGCs (Rbpms, Slc17a6, Sncg, Nefl), microglia (P2ry12, C1qa-c, Tmem119), photoreceptors (Otx2, Gngt2, Gnb3), amacrine cells (Tfap2a, Tfap2b, Onecut2), anterior segment cells (Mgp, Col3a1,Igfbp7), cycling progenitors (Ccnd1, Fgf15, Hes5), and neurogenic progenitors (Hes6, Ascl1, Neurog2). Deeper annotation (e.g., of RGC type) was not done at this stage. No other cellular classes were identified. Three clusters comprising fewer than 1.2% of the cells expressed markers of more than one class. These were flagged as doublets and removed from further analyses.

### Defining RGC precursor heterogeneity at each age

RGC precursors at each age were separately analyzed following the clustering pipeline outlined previously. When implementing Liger, each biological replicate was regarded as a separate batch. The nominal clusters identified by the Louvain algorithm were refined as follows:

is defined to be the log-fold change in expression. Clusters that showed fewer than 10 significant DE genes were merged. In this manner, we identified 10 RGC clusters at E13, 12 at E14, 19 at E16, 27 at P0, and 38 at P5. Using MAST, we identified DE genes that distinguished each cluster against the rest at any given age.

### Quantifying RGC diversity at different ages

We quantified the molecular diversity of RGCs based on clusters at each stage using three measures of population diversity – the Rao index (Figure 2), the Shannon index, and the Simpson index (Figure 2—figure supplement 1). For N clusters with relative frequencies $p_{1}, p_{2}, …, p_{N}$ , these indices are defined as follows:

### Analysis of cluster distinctiveness

We quantified the mutual separation of clusters at each age using two approaches:

For a cluster C, a low of value $r_{C}/d_{C}$ indicates a higher degree of separatedness. Averaging this metric across all the clusters at a given age quantifies the degree to which clusters are separated in the UMAP representation.

### Relating clusters across ages using supervised classification

#### Analysis overview

To distinguish between ‘specified’ and ‘nonspecified’ modes of diversification (Figure 3), we first used a supervised classification approach to associate immature RGC clusters at young ages (tests) to cluster IDs determined at older ages (references). We used XGBoost, a decision-tree-based ensemble learning algorithm (Chen and Guestrin, 2016), to train multi-class classifiers on reference clusters and used these to assign labels to individual test RGCs.

Two kinds of references were used: (1) classifiers trained on the adult (P56) clusters were used to assign immature RGCs at each of the five developmental ages (five separate analyses) to adult labels. (2) Classifiers trained on E14, E16, P0, and P5 clusters were used to assign E13, E14, E16, and P0 RGCs to labels corresponding to the previous age, respectively (four separate analyses). The correspondence between classifier assigned labels and cluster IDs of test RGCs was visualized using confusion matrices (e.g., Figure 3d–h) and quantified using two metrics – the ARI and NCE metrics, described below.

#### Classification overview

To describe our classification analysis, we introduce some notation to facilitate a description in general terms. Let $A^{R}$ and $A^{T}$ denote the reference and the test atlases for the purpose of supervised classification. The number of cells (i.e., RGCs) contained in the reference and test atlases is denoted $|A^{R}|$ and $|A^{T}|$, respectively. $A^{R}$ and $A^{T}$ could correspond to any pair of ages as described above. Without loss of generality, let us assume that $A^{R}$ contains r transcriptomic clusters denoted ${C_{1}^{R},C_{2}^{R}, … C_{r}^{R}}$. Similarly, $A^{T}$ is assumed to contain t transcriptomically defined clusters denoted ${C_{1}^{T},C_{2}^{T}, … C_{t}^{T}}$.

Each cell in our dataset is the member of a particular atlas and is assigned to a single cluster within the atlas based on its transcriptome. The transcriptome of each cell is a vector (denoted using lowercase boldface symbols, e.g., $u$ or $v$) with the number of elements equal to the number of HVGs (the features used for classification). Let $cluster(u)$ denote the transcriptionally assigned of cell $u$. For example, the following statement,

$$
u\in A^{T},  cluster(u)=C_{k}^{T}
$$

translates to ‘Cell $u$ in atlas $A^{T}$ is a member of cluster $C_{k}^{T}$ .’ Our goal is to assign each cell $u\inA^{T}$ a second ID $cluster^{′}(u)$ based on its transcriptomic correspondence to the reference atlas $A^{R}$ . We perform this via an XGBoost classifier trained on $A^{R}$ and applied it to every cell in $A^{T}$ , allowing us to infer transcriptomic correspondences between the two sets of clusters. The main steps are as follows:

xgb_params <- list("objective" = "multi:softprob",

"eval_metric" = "mlogloss",

"num_class"= nClusters,

"eta" = 0.2,"max_depth" = 6, subsample = 0.6)

### Quantifying cluster correspondence using global and local metrics

Let $N_{ij}$ denote the number of cells in $A^{T}$ that are part of transcriptomic cluster $C_{j}^{T}$ and are assigned by $Class^{R}$ to reference cluster $C_{i}^{R}$ . Thus,

$$
N_{ij}=#{cluster^{′}(u)=C_{i}^{R}, cluster(u)=C_{j}^{T} ∀ u\inA^{T}}
$$

$N_{ij}$ defines a contingency table, whose marginal sums are defined as

$$
a_{i}=\sumj=1tN_{ij}
$$



$$
b_{j}=\sumi=1rN_{ij}
$$

Let $N=\sumi,jN_{ij}=|A^{T}|,$ the number of cells in $A^{T}$ . Then, the ARI corresponding to the assignments can be evaluated using the following equation:

$$
ARI= \frac{\sum_{ij}\frac{N_{ij}}{2}-\sum_{i}\frac{a_{i}}{2}\sum_{j}\frac{b_{j}}{2}/\frac{N}{2}}{\frac{1}{2}\sum_{i}\frac{a_{i}}{2}+\sum_{j}\frac{b_{j}}{2}-\sum_{i}\frac{a_{i}}{2}\sum_{j}\frac{b_{j}}{2}/\frac{N}{2}}
$$

The ARI ranges from 0 and 1, with extremes corresponding to random association and 1:1 correspondences between $A^{R}$ and $A^{T}$ , respectively. The ARI can technically also take on negative values for certain scenarios, but these are not observed in our data.

As an alternative, we also used the NCE, an information-theoretic measure. The NCE quantifies the extent to which knowledge of the value of $cluster^{`}u$ reduces the uncertainty (measured in information bits) about the value of $clusteru$ for $u\inA^{T}$ .

We introduce probability weights $q_{ij}$ and the corresponding marginals $q_{i,.}$ and $q_{.,j}$ as follows:

$$
q_{ij}=\frac{N_{ij}}{N}
$$



$$
q_{i,.}=\frac{a_{i}}{N}
$$



$$
q_{.,j}=\frac{b_{j}}{N}
$$

The conditional entropy (CE) is then given by the expression:

$$
H(cluster(u)|cluster^{′}(u))= − \sumij q_{ij}log \frac{q_{ij}}{q_{i,.}}
$$

Note that CE is asymmetric, that is, $H(cluster(u)|cluster^{′}(u))\neq H(cluster^{′}(u)cluster(u))$. One notes that H = 0 if for each cluster $i\in {1, …, r}$, $q_{ij} =\delta_{i,k_{i}}$ for a single cluster $k_{i}$ , where $\delta_{ij}$ is the Kronecker delta defined as

$$
\delta_{ij}=1, if i=j
$$



$$
\delta_{ij}=0, if i\neqj
$$

Finally, NCE is defined as

$$
NCE=\frac{H(cluster(u)|cluster^{′}(u))}{(cluster(u))}
$$

where $Hclusteru=-\sum_{j}q_{.,j}log⁡q_{.,j}$ is the Shannon entropy. Due to this normalization, NCE values range from 0 to 1, with extremes corresponding to fully specific mapping or random association, respectively, between $A^{R}$ and $A^{T}$ . ARI and NCE are inversely related. Unlike ARI, however, NCE is able to detect specificity in both many:1 and 1:1 mappings. ARI returns a value lower than 1 for specific mappings if the number of clusters in $A^{R}$ and $A^{T}$ is not equal.

ARI and NCE quantify global correspondences between $A^{R}$ and $A^{T}$ . We also computed a local metric, the OF that quantified whether individual reference labels $C_{i}^{R}$ were distributed in a ‘localized’ or ‘diffuse’ manner between test clusters$\in{C_{1}^{T},C_{2}^{T}, … C_{t}^{T}}.$

$$
OF(C_{i}^{R})=\frac{1}{t}[\frac{1}{\sumj(\frac{q_{ij}}{q_{i,.}})^{2}}]
$$

Note that the term $\frac{q_{ij}}{q_{i,.}}$ is simply the fraction of the total test cells belonging to test cluster $C_{j}^{T}$ that are assigned to reference cluster $C_{i}^{R}$ by the classifier. Defined this way, the term in the square brackets computes an occupation number that ranges from 1 to t and can be interpreted as the number of test clusters that are specifically associated with $C_{i}^{R}$ . Division by t the number of test clusters, therefore, converts this number into a fraction.

### Overview of WOT analysis

To identify fate relationships among maturing RGCs, we used WOT (Schiebinger et al., 2019), a recently developed framework that is rooted in optimal transport theory (Villani, 2009). WOT does not rely on clustering, and therefore is able to identify ancestor–descendant relationships between any pair of temporally separated RGCs in our data.

At its heart, WOT models cellular transcriptomes $u$ measured at a given age t as a probability distribution in gene expression space $P_{t}(u)$ (note that $u$ may represent the original gene expression space or a reduced dimensional embedding estimated via PCA or diffusion maps). This probability distribution evolves with time as cells differentiate and mature. Different temporal measurements collected at times $…, t_{i-1}, t_{i}, t_{i+1}, …$ represent temporal snapshots of the corresponding cell distributions $…,P_{t_{i-1}}, P_{t_{i}}, P_{t_{i+1}}, …$ . Unfortunately, as each cell can only be measured once, the measurement at different times is from different cells. Therefore, for a particular cell $u$ at time $ t_{i}$ , it is not clear which cell(s) at time $t_{i-1}$ are likely to be its ancestor(s) and which cell(s) at time $t_{i+1}$ are likely to be descendant(s). It is this problem that WOT addresses.

Briefly, for a given pair of consecutive transcriptomic snapshots $P_{t_{i}}(u)$ and $P_{t_{i+1}}(v)$, we wish to estimate the joint distribution $Π_{t_{i},t_{i+1}}(u,v)$, representing the probability that a cell having an expression vector $u$ at time $t_{i}$ transitions to a cell with an expression vector $v$ at time $t_{i+1}$ . $Π_{t_{i},t_{i+1}}(u,v)$ is also called the temporal coupling, which, owing to the destructive nature of scRNA-seq assays, is not directly observable. Under the assumption that cells move short distances in transcriptomic space when $Δt_{i}=t_{i+1}-t_{i}$ is ‘reasonably close,’ WOT estimates $Π_{t_{i},t_{i+1}}(u,v)$ as the solution to the following convex optimization problem:

$$
Π^_{t_{i},t_{i+1}}=argmin_{Π} \sumu\inA^{t_{i}}\sumv\inA^{t_{i+1}}c(u,v)Π(u,v)−ϵ\int\intΠ(u,v)log⁡Π(u,v)dudv+\lambda_{1}KL[\sumu\inA^{t_{i}}Π(u,v)||dP^_{t_{i+1}}(v)]+\lambda_{1}KL[\sumv\inA^{t_{i+1}}Π(u,v)||dQ^_{t_{i}}(u)]
$$

In the above equation,

We note that the values of the hyperparameters $ϵ, \lambda_{1}$, and $\lambda_{2}$ are held fixed for all pairwise transport map calculations (E13, E14), (E14, E16), ….

### Application of WOT to RGC diversification and long-range couplings

We apply WOT to each pair of consecutive ages $t_{i}$ and $t_{i+1}$ to estimate the transport map $Π^_{t_{i},t_{i+1}}$ . Transport maps connecting nonconsecutive time points $t_{i}$ and $t_{i+k}$ are estimated through a simple matrix multiplication of intermediate transport maps

$$
Π^_{t_{i},t_{i+k}}=Π^_{t_{i},t_{i+1}}Π^_{t_{i+1},t_{i+2}}…Π^_{t_{i+k−1},t_{i+k}}
$$

The transport matrices $Π^_{t_{i},t_{j}}$ encode fate relationships between cells at $t_{i}$ and cells at a later time $t_{j}>t_{i}$ . These relationships can be analyzed at the level of clusters at $t_{j}$ to associate each cell $u\inA^{t_{i}}$ with transcriptomically defined cluster. This is particularly useful in estimating the terminal identity of immature RGCs.

Operationally we compute for each cell $u\inA^{t_{i}}$ a ‘cell fate vector’ $f_{t_{j}}\beta;u, t_{i}, (\beta=1, 2, …)$ encoding the probabilities that $u$ is associated with cluster $C_{\beta}^{t_{j}}$ at time $t_{j}$ ,

$$
f_{t_{j}}(\beta;u, t_{i})= \frac{\sumv\inC_{\beta}^{t_{j}}Π^_{t_{i},t_{j}}(u,v)}{\sum\beta\sumv\inC_{\beta}^{t_{j}}Π^_{t_{i},t_{j}}(u,v)}
$$

It is easy to verify that

$$
\sum\betaf_{t_{j}}(\beta;u, t_{i})=1 ∀ u\inA^{t_{i}}
$$

The cell fate vector $f_{t_{j}}\beta;u, t_{i}$ encodes probabilistic associations between the cell $u$ and terminal clusters at $t_{j}>t_{i}$ indexed by $\beta$. The ‘cluster ancestry vector’ at an earlier time $t_{i}$ of a cluster $C_{\beta}^{t_{j}}$ at time $t_{j}>t_{i}$ , denoted $Γ_{t_{i}}(u;C_{\beta}^{t_{j}})$ , is defined as follows:

$$
Γ_{t_{i}}(u,C_{\beta}^{t_{j}})=\frac{\sum_{v\inC_{\beta}^{t_{j}}}Π^_{t_{i},t_{j}}(u,v)}{\sum_{u\inA^{t_{i}}}\sum_{v\inC_{\beta}^{t_{j}}}Π^_{t_{i},t_{j}}(u,v)}(t_{j}>t_{i})
$$

In a similar vein, the ‘cluster descendant vector’ at a later time $t_{o}$ of a cluster $C_{\beta}^{t_{j}}$ at a time $t_{j}<t_{o}$ , denoted $Γ_{t_{o}}u;C_{\beta}^{t_{j}}$ , is defined as

$$
Γ_{t_{o}}(u;C_{\beta}^{t_{j}})=\frac{\sum_{v\inC_{\beta}^{t_{j}}}Π^_{t_{j},t_{o}}(v,u)}{\sum_{u\inA^{t_{o}}}\sum_{v\inC_{\beta}^{t_{j}}}Π^_{t_{i},t_{o}}(v,u)} (t_{o}>t_{j})
$$

These equations can be used to compute the putative ancestral or descendent cells associated with a cluster $C_{\beta}^{t_{j}}$ at time $t_{j}$ .

### Implementation details of WOT

RGC vectors from all ages were combined, median-normalized, and log-transformed. 2854 HVGs were identified using the Gamma-Poisson model, and WOT was run on this matrix as follows:

wot optimal_transport --matrix RGC_mat.mtx --cell_days cell_day.txt --growth_iters 3 --epsilon 0.005 --out tmaps/RGC

Cell days were specified in cell_day.txt as 0, 1, 3, 6, 11, and 20 for E13, E14, E16, P0, P5, and P56, respectively. We computed trajectories and fates for each age using the following command illustrated for P0:

wot trajectory --tmap tmaps/RGC --cell_set cell_sets.gmt --day 6 --out tmaps/traj_RGC_P0.txt

Fates were computed as

wot fates --tmap tmaps/RGC --cell_set cell_sets.gmt --day 6 --out tmaps/fate_RGC_P0.txt

The above process was repeated for each age.

#### Multipotentiality of precursors

For each cell at ages E13–P5, we computed the terminal fate association $f_{P56}\beta;u, t , t\in(E13, E14, …, P5)$, quantifying the probability that it is a precursor of type $\beta\in(1, 2, …45)$. Note that $f_{P56}\beta;u, t$ is denoted $f_{\beta}$ for brevity in the main text. We define

$$
Pu;t= \frac{1}{\sum_{\beta}f_{P56}\beta;u, t^{2}}
$$

as the potential of precursor $u$ at age t. Values of P range between 1 and 45, with lower values indicating restriction of fate and higher values suggesting multipotentiality.

### Network analysis of fate couplings

We define

$$
C(\alpha,\beta;t)= \frac{\frac{1}{|A^{t}|}\sumu\inA^{t}(f_{P56}(\alpha;u, t)−f_{P56}(\alpha; t)¯)(f_{P56}(\beta;u, t)−f_{P56}(\beta; t)¯)}{\sqrt{\frac{1}{|A^{t}|}\sumu\inA^{t}(f_{P56}(\alpha;u, t)−f_{P56}(\alpha; t)¯)^{2}}\sqrt{\frac{1}{|A^{t}|}\sumv\inA^{t}(f_{P56}(\beta;v, t)−f_{P56}(\alpha; t)¯)^{2}}}
$$

as the fate coupling between RGC types $\alpha$ and $\beta  $ at age $t$. Clearly, $C\alpha,\beta;t$ is simply the Pearson correlation coefficient between $f_{P56}\alpha;u, t$ and $f_{P56}\beta;u, t$ , the probabilities that a cell $u\inA^{t}$ is a precursor of $\alpha$ and $\beta  $ precursor. Here,

$$
f_{P56}(\alpha; t)=\frac{1}{|A^{t}|}\sumu\inA^{t}f_{P56}(\alpha;u, t)
$$

is the mean probability that a cell at age t is a precursor of type $\alpha$. We computed $C\alpha,\beta;t$ across all 990 pairs of RGC types at each immature age $t\inE13, E14, …, P5.$ The values $C\alpha,\beta;E13$ were used as edge weights to visualize the fate coupling network of RGC types using the force-directed layout method (Fruchterman and Reingold, 1991) as implemented in the R package igraph. The node layout was computed using $C\alpha,\beta;E13$ values. For other ages, the node layout at E13 was retained but the edges were replotted based on $C\alpha,\beta;t$ values at the corresponding age.

We computed a null distribution of $C\alpha,\beta;t$ by randomizing the values of $f_{P56}\alpha;u, t$ within each cell $u$ across types. The null values of $C\alpha,\beta;t$ rarely exceeded 0.1 and never exceeded 0.2, so only the edges with larger weights were visualized in Figure 5.

### Decay of pairwise couplings

For each pair of RGC types $\alpha$ and $\beta$, we fitted a logistic equation to model the decay of pairwise couplings as

$$
C\alpha,\beta;t=\frac{1}{1+exp⁡(\beta_{0}+\beta_{1}t)}
$$

The values of t corresponding to E13, E14, E16, P0, and P5 were t = 0, 1, 3, 6, and 11, with $C\alpha,\beta;t$ computed as above. We also assumed that $C\alpha,\beta;t=0$ at t = 36, corresponding to P30. Thus, six data points were used to estimate two parameters for each of the 180 pairs of RGC types that had nonzero values of $C\alpha,\beta;t$ . The nls function from the R package stats was used to estimate $\beta_{0}$ and $\beta_{1}$ . The results are plotted in Figure 5f.

### Logistic modeling of specification and calculation of τsp

We hypothesized that the specification of a type $\beta$ corresponds to the localization of its precursors in transcriptomic space. The extent of localization for a RGC of type $\beta$ across the time course was calculated as follows. At each age t, we identified the set of precursor RGCs $Prec(\beta;t)$ showing the highest fate probability corresponding to type $\beta$:

$$
Prec(\beta;t)={u\inA^{t} | f_{P56}(\beta;u,t)>f_{P56}(\alpha\neq\beta;u, t)}
$$

Next, we calculated how the precursors of $\beta$ were distributed across clusters at time t. We computed the OFs (see above) of precursor cells for type $\beta$ across all clusters $C_{k}, k=1, 2, …, N(t)$ at a particular time t ($N(t)$ is the number of transcriptomically defined clusters at time t):

$$
p_{k}(\beta;t)= \frac{#{cluster(u)= C_{k} ∀ u\inPrec(\beta;t)}}{#{u\inPrec(\beta;t)}}
$$

The localization score for each type $\beta$ at a given time t was defined as

$$
Localization(\beta;t)=1− \frac{\sum_{k=1}^{N(t)}\frac{1}{p_{k}(\beta;t)^{2}}}{N(t)}
$$

where the index k ranges over the number of clusters at time t. As defined, $Localization(\beta;t)$ is restricted to be between 0 and 1, with higher values representing a greater specification. We used a logistic model to approximate the localization of each type as

$$
Localization\beta;t= \frac{exp⁡(\gamma_{0}+\gamma_{1}t)}{1+exp⁡(\gamma_{0}+\gamma_{1}t)}
$$

As in the previous section, the nls function was used to estimate the logistic parameters $\gamma_{0}$ and $\gamma_{1}$ . We consider a type $\beta$ as specified if its specification crosses the line $yt=0.95 1-1/N(t)$ . Thus, the specification time for a type $\beta$ is defined as

$$
\tau_{sp}\beta=argmin_{t} Localization\beta;t\geqy(t)
$$

Note that, as defined, $\tau_{sp}$ can be any time point in the interval (E13, P30) corresponding to $t\in(0,36)$.

### Inference of laterality in RGC types

To identify putative ipsilateral- and contralateral-specified RGC precursors at E13, we scored each precursor RGC based on their expression of bona fide ipsilateral genes (Zic2, Zic1, and Igfbp5) and bona fide contralateral genes (Isl2, Fgf12, Igf1) as in Wang et al., 2016. We refer to these as I-RGC and C-RGC scores. Putative I-RGCs were those cells that expressed the I-RGC score at 1.5 standard deviations higher than the mean across all cells, and those that express the C-RGC score at 1.5 standard deviations lower than the mean across all cells. C-RGCs were defined analogously. Many cells did not express either of these marker sets as shown in Figure 7c. These are likely to be RGCs that have not declared their laterality or C-RGCs that are not defined by the expression of Isl2, Fgf12, and Igf1.

WOT was then used to compute the descendants of E13 I-RGCs at all subsequent ages through P56 using the wot fates command introduced above. These descendants were used for two purposes. First, we assessed the proportion of putative I-RGCs across types as in Figure 7d. We also performed a differential gene expression test between putative I-RGCs and the remaining RGCs at all ages, as shown in Figure 7e and f and Figure 7—figure supplement 1d and e.

### Comparison with previous retina scRNA-seq datasets

We compared our data with three scRNA-seq studies that profiled the whole retina during development:

For consistency with our filtering parameters, we extracted cells based on a cutoff of 700 genes/cell from each of the above datasets. For the Clark et al. dataset, this selected 17,827 cells at E14, 1674 cells at E16, and 8343 cells at P0, respectively (N = 27,844 cells). In these samples, RGCs comprised 19, 28, and 0.45%. For the Giudice et al. dataset, this selected 5218 cells, of which 23% were RGCs.

The Rheaume et al. dataset was directly compared with P5 RGCs collected in this study using supervised classification (Figure 1—figure supplement 1i). Clark et al. and Lo Giudice et al. data were combined with the retinal cells profiled in this study at corresponding time points (25,685 cells at E14; 21,274 cells at E16; and 23,251 cells at P0). Together, this resulted in a 14,350 genes × 103,272 cells expression matrix that was analyzed following the steps outlined previously. In the alignment step, cells from each combination of age and study were considered as a separate ‘batch.’ We visualized the transcriptional heterogeneity of the full dataset using UMAP and used the expression of canonical markers to confirm the co-clustering of cell classes in Figure 1—figure supplement 1 (Rbpms for RGCs, Tfap2b for ACs, Fgf15 for RPCs, and Gngt2 for RPCs).

### Data availability

All scRNA-seq data collected in this study were submitted to the Gene Expression Omnibus (GEO) under GSE185671. The data can be visualized on the Broad Institute’s Single Cell Portal under the identifier SCP1706.

### Code availability

The scripts (written in R) generated for this study are shared at https://github.com/shekharlab/mouseRGCdev, (copy archived at swh:1:rev:ca6a97adabb7bc4ffb2fb1187c78cb277513665c; Shekhar, 2022).
