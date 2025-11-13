# Single nuclei RNA-sequencing of adult brain neurons derived from type 2 neuroblasts reveals transcriptional complexity in the insect central complex

## Authors

- Derek G Epiney<sup>1</sup>
- Gonzalo Morales Chaya<sup>1</sup>
- Noah R Dillon<sup>1</sup>
- Sen-Lin Lai<sup>1</sup> ([ORCID: 0000-0002-7531-283X](https://orcid.org/0000-0002-7531-283X)) †
- Chris Q Doe<sup>1</sup> ([ORCID: 0000-0001-5980-8029](https://orcid.org/0000-0001-5980-8029)) †

### Affiliations

1. Institute of Neuroscience, Howard Hughes Medical Institute, University of Oregon Eugene United States ([ROR:0293rh119](https://ror.org/0293rh119))

† Corresponding author

## Abstract

In both Drosophila and mammals, the brain contains the most diverse population of cell types of any tissue. It is generally accepted that transcriptional diversity is an early step in generating neuronal and glial diversity, followed by the establishment of a unique gene expression profile that determines morphology, connectivity, and function. In Drosophila, there are two types of neural stem cells, called Type 1 (T1) and Type 2 (T2) neuroblasts. The diversity of T2-derived neurons contributes a large portion of the central complex (CX), a conserved brain region that plays a role in sensorimotor integration. Recent work has revealed much of the connectome of the CX, but how this connectome is assembled remains unclear. Mapping the transcriptional diversity of T2-derived neurons is a necessary step in linking transcriptional profile to the assembly of the adult brain. Here we perform single nuclei RNA sequencing of T2 neuroblast-derived adult neurons and glia. We identify clusters containing all known classes of glia, clusters that are male/female enriched, and 161 neuron-specific clusters. We map neurotransmitter and neuropeptide expression and identify unique transcription factor combinatorial codes for each cluster. This is a necessary step that directs functional studies to determine whether each transcription factor combinatorial code specifies a distinct neuron type within the CX. We map several columnar neuron subtypes to distinct clusters and identify two neuronal classes (NPF+ and AstA+) that both map to two closely related clusters. Our data support the hypothesis that each transcriptional cluster represents one or a few closely related neuron subtypes.

## Introduction

In all organisms, the brain has arguably the most complex cellular diversity, from human (Siletti et al., 2023) to Drosophila (Davie et al., 2018; Franconville et al., 2018; Hulse et al., 2021). Neuronal diversity is essential for the assembly and function of the adult brain, yet the ‘parts list’ of different neuronal and glial cell types remains incomplete. In Drosophila, the laterally positioned optic lobes have been well characterized for transcriptionally distinct neurons and glia (Konstantinides et al., 2018; Konstantinides et al., 2022; Özel et al., 2022), as has the central brain and ventral nerve cord (Croset et al., 2018; Davie et al., 2018; Lago-Baldaia et al., 2023; Li et al., 2022; McLaughlin et al., 2021; Naidu et al., 2020; Nguyen et al., 2021; Sato and Suzuki, 2022; Shu et al., 2023; Velten et al., 2022).

The central brain contains many diverse neurons that populate important neuropils, such as the mushroom body (MB) used for learning and memory (Sgammeglia and Sprecher, 2022), or the central complex (CX) used for celestial navigation and sensory-motor integration (Fisher, 2022), among other behaviors. The central brain neurons are all generated from neural stem cells, called neuroblasts (NBs). There are two types of NBs that generate central brain neurons: Type 1 (T1) and Type 2 (T2) NBs. T1 NBs undergo asymmetric divisions to self-renew and generate a series of ganglion mother cells (GMCs), which each produce two post-mitotic neurons (Pollington et al., 2023; Yu et al., 2010; Yu et al., 2013). There are ~100 T1 NBs per larval central brain lobe that each generate 20–100 neurons and glia (Ito et al., 2013; Yu et al., 2013). In addition, there are Type 0 (T0) NBs which generate post-mitotic neuron progeny (Baumgardt et al., 2014); T0 NB lineages yet to be documented in the central brain. T2 NBs have a more complex division pattern than T1 NBs (Bello et al., 2008; Boone and Doe, 2008; Bowman et al., 2008). T2 NBs undergo asymmetric division to self-renew and generate an intermediate neural progenitor (INP); each INP undergoes 4–6 divisions to self-renew and generate a GMC and its two neuron or glial progeny (Bello et al., 2008; Boone and Doe, 2008; Bowman et al., 2008). Thus, each T2 NB division will generate 8–12 progeny cells. Most T2 NBs generate ~500 neurons (Yu et al., 2013), have highly complex neuronal cell types based on morphology and connectivity (Hulse et al., 2020; Wang et al., 2014; Yang et al., 2013; Yu et al., 2013), and produce the columnar neurons of the adult CX (Boyan and Williams, 2011; Kandimalla et al., 2023). Subsequently, we will call neurons born from type I NBs ‘T1-derived’ and neurons born from type 2 NBs ‘T2-derived’.

Although single-cell RNA-seq (scRNA-seq) has been done on adult central brain neurons and glia (Croset et al., 2018), the transcriptomic profile of T1 versus T2 neuronal and glial progeny has not yet been characterized. Furthermore, the T2 lineages generate diverse neuronal progeny (Hulse et al., 2020; Wang et al., 2014; Yang et al., 2013; Yu et al., 2013) but focused transcriptional profiling of T2-derived progeny has not been reported. In this report, we generate a single nuclei (snRNA-seq) atlas of T2-derived progeny of the adult central brain. We use several complementary methods to link neuron identity to transcriptional clusters. Our data will facilitate linking neuronal transcriptomes with connectomes to gain a molecular understanding of CX development, connectivity, and behavior.

## Results

### Generation of a transcriptomic atlas of adult central brain neurons and glia

The adult central brain (i.e. brain without optic lobes) is composed of neuronal and glial progeny derived from both T1 and T2 NBs. We first generated a transcriptomic atlas of all central brain neurons derived from both T1 and T2 NBs. The flies were of a genotype that gave permanent lineage tracing of T2 NB-derived progeny in the adult (Figure 1A and A'). This allowed us to first analyze all central brain T1- and T2-derived neurons and glia (Figure 1) and then focus on neurons and glia produced specifically by T2-derived lineages.

![Figure 1.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig1-v1.jpg)

**Figure 1.:** (A-A’) Genetics (A) to label progeny (A’) derived from T2 NBs. Dashed lines show the boundary of optic lobes and central brain, and the optic lobes were removed during dissection. (B) Central brain atlas labeled with known cell types. Abbreviations: CLK, clock neurons; CRZ, Corazonergic neurons; DOP, dopaminergic neurons; HEM, hemocytes; MBN, mushroom body neurons; OCTY, octopaminergic-tyraminergic neurons; OC, ocelli; OL, optic lobe; OPN, olfactory projection neurons; SER: serotoninergic neurons. (C) Central brain atlas labeled by NB (T1 or T2) lineage. Dash line-outlined box shows the region enriched with the cells derived from T2 NBs, and the identity are shown at the bottom-right box. (D) Dot plot of top 5 marker genes of the T2-enriched clusters. (E) Atlas of central brain glia labeled with known cell types. (E’) T1 and T2 derived cells colored cyan and red respectfully. (F) Dot plot of known and top marker genes of glial clusters.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Vertical shades mark the cluster with T2/(T1+T2)>50%.

We dissociated nuclei from 7-day-old adult fly central brains with optic lobes removed using methods previously described (Li et al., 2022; McLaughlin et al., 2021). The cDNA libraries were then prepared from dissociated nuclei with split-pool-based barcoding for single-nuclei transcription profiling (Rosenberg et al., 2018). We sequenced a total of 30,699 nuclei at 589 median genes per nuclei from the T1+T2 central brain.

To distinguish T2-derived progeny from T1-derived progeny, we expressed worniu-Gal4,asense-Gal80 to drive expression of FLP recombinase (FLP) specifically in T2 NBs. This resulted in the flip out of a stop cassette and thus continuous expression of Gal4 under the ubiquitous actin5C enhancer. After removal of the stop cassette in T2 NBs, the actin5c-Gal4 can continuously drive expression of the reporter genes (RFP or GFP) and FLP in the T2-derived neuronal and glial progeny in adult brains (Figure 1A). We assigned 3,125 nuclei which have expression of RFP, GFP, or FLP as being derived from T2 lineages. We assigned 27,574 triple-negative nuclei as derived from the T1 lineages. We used Seurat for filtering, integrating, and clustering the atlas to provide transcriptionally unique cell clusters (Stuart et al., 2019). We used uniform manifold approximation and projection (UMAP)-based dimension reduction to visualize the 152 clusters (Figure 1B). The most enriched or least expressed genes (marker genes) for each cluster are shown in Supplementary file 1.

We used known markers (Supplementary file 2; Croset et al., 2018; Davie et al., 2018) to identify distinct cell types in the central brain, including glia, mushroom body neurons, olfactory projection neurons, clock neurons, Poxn+ neurons, serotonergic neurons, dopaminergic neurons, octopaminergic neurons, corazonergic neurons, hemocytes, and ocelli (Figure 1B; Supplementary file 1). We did not observe any cluster exclusively containing progeny from T1 or T2 NB lineages (Figure 1C, Figure 1—figure supplement 1). We conclude that both T1 and T2 generate transcriptionally similar cells, despite their different developmental origins. Alternatively, deeper sequencing may resolve a single cluster into two clusters with each derived from T1 or T2 lineages. We next searched for cluster-defining genes in the T2 enriched clusters (Figure 1C’) and found high expression of AstA (Allatostatin A), SerT (Serotonin transporter), Tk (Tachykinin), and Vmat (Vesicular monoamine transporter) (Figure 1D). These enriched marker genes suggest that AstA+ neurons, serotonergic neurons, and TK+ neurons may be primarily derived from T2 lineages.

We explored the central brain atlas for glial cell types and their gene expression. We focused on the 3409 glial nuclei from clusters that expressed the pan-glial marker repo (Campbell et al., 1994; Xiong et al., 1994) in the T1+T2 atlas (Figure 1E). Each cluster contained a mix of T1 and T2 glial progeny (Figure 1E’). We identified six known glial cell types (astrocytes, cortex, ensheathing, surface glial and the two subtypes: perineurial and subperineurial) based on canonical glial makers (Figure 1F; Supplementary file 3). Similar to a previous glial cell atlas (Lago-Baldaia et al., 2023), we found some glial subtypes (astrocytes, ensheathing, and subperineurial) mapping to multiple clusters (Figure 1E and F).We identified a glial cluster that expressed genes associated with extracellular matrix, vkg and Col4a1 (Figure 1F), which have previously been identified as pan surface glial markers (DeSalvo et al., 2014; Hindle and Bainton, 2014). Interestingly, the two surface glial subtypes, perineurial and subperineurial clusters, do not express these markers at cluster defining levels, and conversely the surface glia cluster 5 does not express perineurial or subperineurial specific makers (Figure 1F, Supplementary file 4). Differential gene expression analysis for all genes between T1 and T2 glial progeny did not show differences across any glial cell types or clusters (Supplementary file 5). We conclude that the adult central brain contains known glial cell types with no differences in gene expression between T1 and T2-derived glia.

### Generation of a T1- and T2-specific cell atlas

We explored the diversity of T1- and T2-derived neurons by generating T1- and T2-specific cell atlases. We identified T1-derived neurons by bioinformatically excluding cells co-expressing T2-specific markers FLP+/GFP+/RFP+ plus repo+ glial clusters. We then generated a T1 neuron atlas containing 22,807 T1-derived neurons that form 114 clusters. Marker genes of each cluster are shown in Supplementary file 5. We identified the neurons that are known to be generated by T1 NBs, including MB neurons and olfactory projection neurons (Croset et al., 2018; Davie et al., 2018; Li et al., 2022; Supplementary file 2). We identified other T1-derived neurons, including clock neurons, Poxn+ neurons, and neurons that release dopamine, serotonin, octopamine/tyramine, and other neuropeptides (Figure 2—figure supplement 1, Supplementary file 6; Croset et al., 2018; Davie et al., 2018). We gathered a list of genes that represented the 10 most enriched genes from each cluster and calculated the scaled averaged expression of each gene from each cluster (Figure 2—figure supplement 1). Each unique combination of enriched genes could be referred to as cluster markers. We conclude that our T1-derived nuclei contain the expected abundance of neuronal diversity seen in previous scRNA-seq atlases (Croset et al., 2018; Davie et al., 2018; Li et al., 2022).

In our whole brain atlas described above, T2-derived cells represent a minor contribution to the atlas due to their low nuclei numbers relative to the T1-derived neurons (Raji and Potter, 2021). To generate a comprehensive T2 atlas, we needed to increase the percentage of T2-derived nuclei for RNAseq. We used fluorescence-activated cell sorting (FACS) to select nuclei that are labeled by T2-specific permanent lineage tracing (Figure 1A and B). We then selected the nuclei in silico that showed expression of UAS-transgenes (FLP, GFP, or RFP, see above) to eliminate contamination of T1 nuclei during FACS. In total, we sequenced 61,118 T2 nuclei. We included 3125 UAS transgene-labeled nuclei from the dissociated central brain without sorting from the T1+T2 atlas (see above). We used integration in Seurat to generate an atlas containing 64,243 nuclei that formed 198 clusters. T2 NBs have been estimated to produced ~5000 neurons/glia in the central brain (Ito et al., 2013; Yang et al., 2013), with ~1800 neurons in the central complex (Hulse et al., 2020; Schlegel et al., 2024), giving our atlas ~12 x coverage. We next filtered out the repo+ glial cell clusters to generate a T2 neuron cell atlas with 50,148 non-glial nuclei forming 161 clusters (Figure 2A). Marker genes of each cluster are shown in Supplementary file 8; Marsh, 2024.

![Figure 2.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig2-v1.jpg)

**Figure 2.:** (A) Cell atlas from T2 NBs. (B) Heatmap of scaled average expression of top 10 markers genes from each T2 neuronal cluster.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Cell atlas from T1 NBs. (B) Heatmap of scaled average expression of top 10 markers genes from each neuronal cluster. Annotations: AstA, Allatostatin A+ neurons; CLK, clock neurons; CRZ, Corazonin+ neurons; DOP, dopaminergic neurons; IPC, insulin-like peptide producing cells; MBN, mushroom body neurons; OCTY, octopaminergic-tyraminergic neurons; OPN olfactory projection neurons; Tk, Tachykinin+ neurons; Poxn, Pox neuro+ neurons; PROC, Proctolin + neurons; SER, serotonergic neurons.

We calculated the scaled average expression of the top 10 most enriched genes from each T2 neuron cluster (Supplementary file 8). Each set of genes could serve as cluster marker genes (Figure 2B). We conclude that each cluster within our T2 neuron atlas represents a transcriptionally unique cell type. For the remainder of the paper, we focus solely on the diversity of T2-derived neurons and glia.

### T2 neuroblasts generate all major classes of fast-acting neurotransmitters

An important aspect of neuronal identity and function is fast-acting neurotransmitter expression. We determined the neuronal populations that expressed seven fast-acting neurotransmitters: glutamatergic, cholinergic, GABAergic, tyraminergic, dopaminergic, serotonergic, and octopaminergic in T2-derived neurons (Figure 3A–G). In neurons, we found that cholinergic neurons were most abundant (21%), followed by glutamatergic neurons (12%), GABAergic neurons (9%), tyraminergic neurons (2.6%), dopaminergic neurons (1.2%), serotonergic neurons (1.2%), and octopaminergic neurons (0.7%). Additionally, 12% of neurons were co-expressing two or three neurotransmitters. The remaining 40% in our atlas were not expressing any neurotransmitter with a log normalized expression <2 (Figure 3H); this is similar to the ratios in the adult midbrain (Croset et al., 2018) and optic lobes (Konstantinides et al., 2022). The nuclei co-expressing two or more fast-acting neurotransmitters may reflect an authentic feature of these neurons, as see in other systems (see Discussion). Alternatively, our double- and triple-positive neurons may be false positives (see Discussion).

![Figure 3.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig3-v1.jpg)

**Figure 3.:** (A–G) UMAP distribution plots demonstrate the expression of the following neurotransmitters: (A) vesicular glutamate transporter (VGlut, glutamatergic neurons), (B) vesicular acetylcholine transporter (VAChT, cholinergic neurons), (C) glutamic acid decarboxylase 1 (Gad1, GABAergic neurons), (D) tyramine β hydroxylase (Tbh, tyraminergic neurons), (E) tyrosine 3-monooxygenase (Ple, dopaminergic neurons), (F) serotonin transporter (SerT, serotonergic neurons) (G) tyrosine decarboxylase (Tdc2, octopaminergic neurons). All plots have a minimum cutoff value set at 0. (H) The UpSet quantifies the number of cells in the atlas that express each neurotransmitter gene with a scaled expression >2 (Gu, 2022).

### T2 neuroblasts generate all major classes of glia

We next explored the complete T2 atlas for glial cell types and their gene expression. We sub-clustered from the T2 atlas for 12,315 glial nuclei from clusters that expressed the pan glial marker repo (Figure 4A; Campbell et al., 1994; Xiong et al., 1994). Similar to our T1+T2 glial atlas, we identified glial cell types: astrocytes, cortex, ensheathing, astrocyte-like, and two surface glial subtypes, perineurial and subperineurial, based on canonical glial makers (Figure 4B; Supplementary file 9). In line with our T1+T2 atlas and previous glia cell atlas (Lago-Baldaia et al., 2023), some subtypes mapped to several subclusters including ensheathing, astrocytes, and chiasm (Figure 4A–B).Interestingly, we identified chiasm glia that may represent the migratory chiasm glia generated from the DL1 lineage (Viktorin et al., 2013; see Discussion). We conclude that our T2 atlas contains the expected glial cell types.

![Figure 4.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig4-v1.jpg)

**Figure 4.:** (A) Sub-clustered of 12,315 nuclei from Repo + T2 clusters in UMAP distribution. (B) Dot plot of validated glial subtype markers to identify glial clusters by differential gene expression.

### T2 neuroblasts generate sex-biased cell types

When generating our atlas, we dissected both female and male adult brains that were processed as separate samples in order to differentiate the sex of nuclei in the snRNAseq atlas. We noticed that several cell types in the T2 glial atlas showed unequal number of male and female nuclei (Figure 5A–B and E–F). We identified sex-biased clusters by normalizing the number of input nuclei between male and female samples and compared the proportion of nuclei by sex within each cluster to identify sex-biased clusters (Figure 5B and F). We found that the T2 glial atlas contained two female enriched clusters: ensheathing/astrocyte (cluster 7) and chiasm (cluster 5), and one male enriched cluster: the astrocyte-like (cluster 3; Figure 5B). We determined differential genes expressed between male and female nuclei across all glia (Figure 5C; Supplementary file 10). We found female nuclei expressed higher levels of genes including the female-specific genes yp1, yp2, and yp3 (Figure 5C; Warren et al., 1979). Additionally, female nuclei were enriched for dsx (Supplementary file 10).Male glial nuclei expressed higher levels of genes including the male-specific genes lncRNA:rox1/2 and fru (Figure 5C; Supplementary file 10; Amrein and Axel, 1997; Meller et al., 1997; Ryner et al., 1996).We next looked at expression within the sex-biased clusters. We found similar results that male nuclei expressed high levels of the male-specific lncRNA:roX1/2 and low expression of the female-specific genes yp1, yp2, and yp3 compared to the female nuclei (Figure 5D; see Discussion). We conclude that male and female adult T2 glia have sex-specific differences in gene expression within the same glial cell type.

![Figure 5.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig5-v1.jpg)

**Figure 5.:** (A-A’’) T2 glia in UMAP distribution across samples: (A) T2 Female (3,910 nuclei), (A’) T2 Male (4,385 nuclei), (A’’) Female and Male mixed (4,020 nuclei). (B) Biased clusters for male to female ratio for number of nuclei in the T2 glia clusters. (C) Differential expression between male and female T2 glia. (D) Heatmap of top differential gene expression between male and female nuclei within glial clusters. (E-E’’) T2 neuron in UMAP distribution across samples: (E) T2 Female (8,151 nuclei), (E’) T2 Male (16,201 nuclei), (E’’) Female and Male mixed (25,796 nuclei). (F) Biased clusters for male to female ratio for number of nuclei in the T2 neuron clusters. (G) Differential expression between male and female T2 neurons. (H) Heatmap of top differential gene expression between male and female nuclei within neuron clusters.

We next explored sex differences among neurons (Figure 5E–E’’). We identified 14 neuronal clusters with disproportionate amounts of male and female nuclei (Figure 5F). We first tested the differential genes expressed between male and female nuclei across all T2-derived neurons (Figure 5G; Supplementary file 11). Similar to the T2 glia sex differences, we found female nuclei expressed higher levels of the female-specific genes yp1, yp2, and yp3 (Figure 5G; Warren et al., 1979). Additionally, female nuclei were enriched for dsx (Supplementary file 11). Male neuronal nuclei expressed higher levels of the male-specific genes lncRNA:rox1/2 and fru (Figure 5G; Supplementary file 11; Amrein and Axel, 1997; Meller et al., 1997; Ryner et al., 1996). We next looked at expression levels within the sex-biased clusters. We found similar results that male nuclei expressed high levels of the male-specific lncRNA:roX1/2 and low expression of the female-specific genes yp1, yp2, and yp3 compared to the female nuclei (Figure 5H; see Discussion). We conclude that male and female adult T2 neurons have sex-specific differences in gene expression within the same neuronal subtype.

### T2 neuroblasts generate neurons expressing a diverse array of neuropeptides

Neuropeptides are often used as markers to distinguish different neuronal populations. We examined whether individual neuropeptide-encoding genes were exclusively expressed within single clusters, representing single neuronal subtypes. Among the 49 neuropeptides in Drosophila, we identified 13 with enriched expression in a limited number of clusters, making them suitable as cluster-defining markers (Figure 6A). For all clusters significantly expressing cluster-defining neuropeptides, we assessed their co-expression with specific fast-acting neurotransmitters (Figure 6A). We found that all neuropeptide-expressing clusters, co-express one or more neurotransmitters (see Figure 3H).

![Figure 6.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig6-v1.jpg)

**Figure 6.:** (A) Dot plot showing expression of 13 neuropeptides and their co-expression with the 7 fast-acting neurotransmitters (red dashed line) across selected clusters. (B) Genetic scheme to map neuropeptide expression in T2-derived adult neurons. (C–E) Neuropeptide-expressing neurons labeled with GFP in three-dimensional projections. (C'–E’) Fan-shaped body projections. (C''-E'') Ellipsoid body projections. nc82 counterstains (magenta) in the brain for neuropil projections. (F) Heatmap showing the top 5 transcription factors most strongly correlated with each neuropeptide across all cells (Sigorelli, 2024). Scale bar represents 20 μm.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Heatmap of expression correlation coefficient of transcription factors and neuropeptides calculated from each individual T2 neuron.

These data raise several questions. What is the relationship between neuropeptide expression and cluster identity? Can two distinct clusters express the same neuropeptide? Can two neuropeptides be co-expressed by the same cluster? Our data show that all of these patterns exist. For example, in some cases, one cluster expresses two or more neuropeptide genes (e.g. clusters 100 and 128 express NPF and AstA); conversely, we also observe one neuropeptide expressed in multiple clusters (e.g. Ms, 2 clusters; Tk, 2 clusters; Figure 6A).

Next, we wanted to validate whether these neuropeptidergic cells indeed come from T2 lineages and target the CX. This required a method for specifically labeling of T2 peptidergic neurons, as antibody staining could be contaminated with T1-derived neurons. We developed a genetic approach to selectively visualize neuropeptide expression exclusively in neurons originating from T2 NB lineages. This technique involves driving FLP recombinase (FLP) under the control of the T2-specific driver wor-Gal4,ase-Gal80. The T2-specific FLP catalyzes the excision of a stop codon in the lexAop-FRT-stop-FRT-myr::gfp transgene, allowing existing neuropeptide-2A-LexA transgenes (Deng et al., 2019) to drive GFP expression specifically in neuropeptide-positive T2-derived neurons (Figure 6B). This method revealed the morphology of specific T2-derived peptidergic neurons.

We first assayed Ms+ neurons because Wolff et al., 2025 reported that at least two FB neurons, FB4Z and FB5R express Ms and they target to two distinct FB layers. However, we found that T2-derived Ms-2A-LexA-expressing neurons project to multiple layers of the dorsal fan-shaped body and the entire ellipsoid body, suggesting an unknown class of Ms+ neurons targeting to EB and/or FB (Figure 6C–C'’, Video 1). In our atlas, Ms is mainly expressed in clusters 157 and 160; however, we cannot distinguish the corresponding identity of each neuron.

![Video 1.](https://cdn.elifesciences.org/articles/105896/elife-105896-video1.mp4.jpg)

**Video 1.:** Genotype: 20xUAS-flp;worniu-gal4,asense-gal80; lexAop-FRT-stop-FRT-myr::gfp x Ms-2A-LexA.

Next, we assayed neurons in two clusters (100 and 128) that express the same two neuropeptides, AstA and NPF (Figure 6D–E). We wanted to determine if these clusters contain two cell types with similar gene expression, or a single cell type that co-expressed both neuropeptides. We used NPF-2A-lexA and AstA-2A-lexA to label each class of neurons. We found that they were generated at indistinguishable numbers of cells and projections: both had ~20 neurons projecting to a lateral domain of the ellipsoid body and the same two layers of the fan-shaped body (Figure 6D–E; Video 2 and Video 3). Whether these T2-derived NPF and AstA neurons are indeed the same would require antibody validation.

![Video 2.](https://cdn.elifesciences.org/articles/105896/elife-105896-video2.mp4.jpg)

**Video 2.:** Genotype: 20xUAS-flp;worniu-gal4,asense-gal80; lexAop-FRT-stop-FRT-myr::gfp x NPF-2A-LexA.

![Video 3.](https://cdn.elifesciences.org/articles/105896/elife-105896-video3.mp4.jpg)

**Video 3.:** Genotype: 20xUAS-flp;worniu-gal4,asense-gal80; lexAop-FRT-stop-FRT-myr::gfp x AstA-2A-LexA.

We investigated whether specific transcription factors (TFs), or TF combinatorial codes, might correlate with the expression of cluster-defining neuropeptides, and thus provide candidates for a regulatory relationship where each cluster may have a TF code that drives transcription of a specific neuropeptides. To address this, we performed an unbiased correlation analysis of TF and neuropeptide expression patterns across all cells in our dataset to identify potential regulatory relationships. Interestingly, we found high correlations of multiple TFs to each neuropeptide (Figure 6, Figure 6—figure supplement 1, Supplementary file 12). Our data provide a stepping-stone to the analysis of upstream TF combinatorial codes that drive neuropeptide expression.

### Each neuron cluster consists of a unique combination of transcription factors

It is generally thought that neuronal diversity is generated by TF combinatorial codes that are uniquely expressed in neuronal subtypes, with an emphasis on homeodomain TFs (Reilly et al., 2020; Sagner et al., 2021). Thus, we assayed each class of TFs to determine how many were expressed in cluster-specific (i.e. neuron-specific) patterns. We found that most clusters expressed a unique TF combination (Figure 7). This is true for all zinc-finger TFs (Figure 7A) and helix-turn-helix TFs (Figure 7B). Nearly, all clusters expressed a unique combination of homeodomain TFs (Figure 7C), with only a few clusters sharing a homeodomain code (Figure 7C'). In contrast, basic domain, unspecified domain, and high mobility group TFs were more promiscuously expressed (Figure 7D). We conclude that zinc finger, helix-turn-helix, and homeodomain TFs are good candidates for forming unique combinatorial codes that should be tested for a role in generating neuronal diversity.

![Figure 7.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig7-v1.jpg)

**Figure 7.:** Binarized heatmaps of positive (A) zinc finger (B) helix-turn-helix (C) homeodomain TF markers in T2-derived neurons. Clusters are sorted by similarity based on Jaccard index scores. (C`) Top five marker genes for clusters which had non-unique combinations of homeodomain TF expression. Percentage of clusters with unique combinations of TF expression based on TF class zinc finger TFs = 100% (161 unique clusters), helix-turn-helix TFs = 100% (161 unique clusters), homeodomain TFs = 93.8% (150 unique clusters), basic domain TFs = 69.6% (112 unique clusters), unidentified DNA binding domain TFs = 59% (95 unique clusters), high motility group TFs = 34.2% (55 unique clusters).

### Linking neurons to UMAP clusters

We sought to link well characterized CX neurons to their transcriptomes within the T2 atlas. We chose columnar neurons due to known cell type markers and genetic access. We used four complementary approaches to identify them, described below.

![Figure 8.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig8-v1.jpg)

**Figure 8.:** (A) Heatmap of the coefficients (r) of expression profiles of single cell clusters (columns) to the expressions of known central complex neurons (rows) profiled with bulk RNA sequencing. The matching of the cluster to the central complex neurons is determined by the highest coefficient value (gray box) for each cluster. FB6A(1) and FB6A(2) are labeled and profiled with two different split-Gal4 drivers (Wolff et al., 2025). Cluster 75 and 95 identified as E-PG were verified in Dillon et al., 2024. (B) Scaled average expression of the enhancer genes of split-Gal4 drivers (columns) in each cluster (rows). The name of central complex neurons (CX) labeled by split-Gal4 drivers are listed at the top. The cluster identity was determined by the combination of positive scaled average expression of the enhancer genes (black boxes). (C) Dotplot of the known marker genes (toy, runt) expressed in central complex neurons (PF-R, P-FN, and P-EN), lexA-driver enhancer gene (rho, Gγ30A), split-Gal4-driver (SS00191) enhancer genes (shakB, Pkc53E), and newly identified marker genes. (D) PF-R (R37G12-Gal4 UAS-V5) neuronal cell bodies labeled with V5, and co-stained with marker genes boxed in (C). (E,F) PF-N (R16D01-Gal4 UAS-V5) neuronal cell bodies labeled with V5, and co-stained with marker genes boxed in (C). (G) PE-N (R12D09-Gal4 UAS-V5) neuronal cell bodies labeled with V5, and co-stained with marker genes boxed in (C). (H) Percentage of marker genes in PE-N and PF-N. Scale bar: 5 μm in all panels.

![Figure 9.](https://cdn.elifesciences.org/articles/105896/elife-105896-fig9-v1.jpg)

**Figure 9.:** Asterisk, known neuron-cluster associations; others are predicted neuron-cluster associations. Underline, neurotransmitter expressing clusters. Abbreviations: AstC, Allatostatin C+ neurons; CCAP, Crustacean cardioactive peptide+ neurons; DOPA, dopaminergic neurons; dsx, doublesex+ neurons; MBN, mushroom body neurons; OCTY, octopaminergic-tyraminergic neurons; Proc, Proctolin + neurons; Tk, Tachykinin+ neurons; SER, serotonergic neurons. E-PG, FB1C, FB2A, FB2B, FB2I_ab, FB3C, FB4K, FB4L, FB6A, FB6H, FB7B, FB8B, FB8G, FR1, hΔA, hΔD, hΔE, hΔH, hΔI, hΔK, lbSps-P, P-EG, P-EN, P-FGs, P-FN, PF-R, vΔC and vΔE are the names of central complex neurons (Hulse et al., 2021).

The differential expression of TFs probably contributes to the morphological or connectivity diversity found within each class of CX neurons (Hulse et al., 2021; Turner-Evans et al., 2020; Wolff and Rubin, 2018; Wolff et al., 2015). We conclude that our T2 atlas can be used to link known neuron subtypes to their transcriptome (Figure 9). This is a necessary step in determining how cluster-specific gene expression regulates neuron-specific functional properties such as morphology, connectivity, and physiology.

## Discussion

We used a genetic approach to express RFP in the progeny of T2 NBs in the adult central brain. We excluded optic lobes by manual dissection, and thus our data are similar to recent scRNA-seq data from the central brain (Croset et al., 2018; Davie et al., 2018; Li et al., 2022). Similarities include neurons expressing predominantly single fast-acting neurotransmitters (discussed below). Both datasets show major classes of neurons including MB neurons, olfactory projection neurons, clock neurons, Poxn+ neurons, serotonergic neurons, dopaminergic neurons, octopaminergic neurons, corazonergic neurons, and hemocytes. The MB neurons that appear in the T2-derived progeny may be due to off-target expression of our Gal4 driver at stages we have not assayed, or more likely, due to ambient RNA released during the dissociation and sorting steps.

Interestingly, we observed fewer distinct neuronal clusters in the T1-derived population (114 clusters; Figure 2—figure supplement 1) than in the T2-derived neuronal population (161 clusters; Figure 2). This could be due to the T1-derived progeny containing a large population of transcriptionally similar Kenyon cells of the MB, whereas T2-derived clusters contain fewer, but transcriptionally more diverse, cells than T1-derived progeny. It would be interesting to know whether T1 NB lineages are generally less diverse, or whether the Kenyon cells are exceptional in their lack of transcriptional diversity, despite the presence of protein gradient in young vs. old neurons (Liu et al., 2015). Our results are consistent with lineage analysis of T2 NBs, which make distinct neurons across the temporal axis of T2 NBs, plus unique neurons across the INP temporal axis (Doe, 2017; Ito et al., 2013; Sullivan et al., 2019; Wang et al., 2014; Yang et al., 2013).

### Neurotransmitters and neuropeptides

We observed that most fast-acting neurotransmitters are uniquely expressed in neuronal populations, but we also observed a smaller group of neurons that express two or three neurotransmitters. This includes excitatory and inhibitory neurons, for example 2.9% of all neurons express genes necessary for cholinergic and GABAergic neurotransmitters (Figure 3). Co-expression of neurotransmitters has been reported in other systems (Granger et al., 2020; Granger et al., 2023; Lozovaya et al., 2018; Meye et al., 2016; Saunders et al., 2015; Shabel et al., 2014; Spitzer, 2015; Takács et al., 2018) and it may be biologically relevant in the T2-derived neurons.

Neuropeptides are profoundly important for a vast array of behaviors (Schoofs et al., 2017), and thus our mapping of neuropeptide expression to distinct neuronal subtypes may facilitate a functional analysis linking neuron identity, neuropeptide expression, and behavior.

### Glial identities

We identified six classes of glia in the T1+T2 glial atlas that reflects previous scRNAseq datasets (Figure 1E–F; Konstantinides et al., 2018; Lago-Baldaia et al., 2023). Similar to a recent glial cell atlas (Lago-Baldaia et al., 2023), we found glial subtypes like astrocytes, ensheathing, and subperineurial glia mapped to several clusters (Figure 1E–F). It remains unclear if these clusters with the same cell type annotation represent distinct glial identities or different transcriptional states within these populations. Interestingly, we detected a small population of vkg+ surface glia specific to the whole atlas (T1+T2) and not the T2 glia atlas. The lack of differential gene expression between T1- and T2-derived glia suggests these cell types are similar despite different developmental origins. It will be for future work to understand how different progenitors produce similar glial fates.

Similar to the T1+T2 glial atlas, our T2 atlas captured the known glial subtypes found in other scRNAseq datasets (Figure 4; Konstantinides et al., 2018; Lago-Baldaia et al., 2023). The T2 glia atlas contains more clusters than the T1+T2 atlas that may be due to the nearly 4x the number of glia captured (T1+T2 atlas 3,409 nuclei; T2 atlas – 12,315 nuclei). Interestingly, we identified the astrocyte-like glia of the central brain previously described (Awasaki et al., 2008). Additionally, we captured chiasm glia that have been shown to be derived from the T2 lineage DL1 and migrate into the optic lobe (Viktorin et al., 2013). These nuclei could represent either chiasm glia that did not migrate out of the central brain or optic lobe tissue that was not completely removed during dissections. It will be interesting to investigate how these T2-derived migratory chiasm glia compared to the optic-lobe derived chiasm glia, because of their different developmental origins.

### Sex differences found in the adult neurons and glia

The T2 glia and neuron atlases contained clusters with disproportionate enrichment of female and male nuclei when normalized for sample input. We found the expected differential expression of yolk protein transcripts (yp1, yp2, yp3) enriched in female nuclei and the long non-coding RNAs rox1/2 and fru enriched in male nuclei (Amrein and Axel, 1997; Meller et al., 1997; Ryner et al., 1996). Interestingly, we found dsx to be enriched in both glial and neuronal female nuclei. Surprisingly, we found additional female and male-specific gene enriched in both neurons and glia including ATPsyndelta and undescribed, computationally predicted genes (CGs; Figure 5). It remains to be determined if these genes are driving sex-specific differences within glial and neuronal subtypes. These genes may reflect sex-specific differences in the adult central brain and may provide insight into how behavioral circuits are linked to sex-specific behaviors. Future work should aim to characterize and test these genes for functional roles.

### TF codes

Our atlas showed zinc finger TFs and homeodomain TFs as forming combinatorial codes specific for distinct cell types. This raises the possibility that these TF combinations determine neuronal functional properties, by establishing and maintaining neuronal identities. This is consistent with data from C. elegans (Hobert, 2021; Reilly et al., 2020), mammalian spinal cord (Briscoe et al., 2000; Sagner et al., 2021), Drosophila optic lobe (Holguera and Desplan, 2018; Konstantinides et al., 2018), leg motor neurons (Baek et al., 2013; Enriquez et al., 2015), and VNC (Soffers et al., 2024). Interestingly, we found more zinc finger TFs expressed in unique combinatorial codes compared to homeodomain TFs; this may be a caution to focusing too narrowly on homeodomain TFs function. We note that our results are mostly correlative and await functional analysis of the TF combinatorial codes found in our dataset. It is also possible that the current sparse TF expression patterns are due, in part, to false negative results due to low read depths. This can be resolved by increasing read depth or by performing functional assays.

### Mapping neurons to clusters

In this study, we used several complementary approaches to map identified neurons to their transcriptomic UMAP cluster. First, we used bulk-seq data from specific neurons with our atlas to match neuron to cluster. Second, we used enhancer elements from neuron-specific split Gal4 lines to link enhancer-associated genes to each hemi-driver with common expression in a cluster. Third, we used known or novel TFs and other molecular markers that are expressed by a cluster as an entry point to look for other cluster specific genes. Each of these methods provides candidate neuron-cluster association, which requires experimental validation. It is not clear which method is more robust at identifying functional neuron-cluster associations. Nevertheless, we have validated a number of neuron-cluster associations using the third approach: beginning with a single gene-cluster correlation. In the future, our data can be used in two pipelines for linking neuron subtype to transcriptome. First, start with at least one validated marker for a cluster, then search all labeled clusters for candidate TFs that co-express with the validated marker, followed by validation via RNA in situ (or antibodies). Second, we can collect neurons of interest with FACS or antibody selection (Davis et al., 2020), and perform bulk RNA sequencing, followed by looking for clusters enriched for the TFs found in bulk sequencing data, and then validation via RNA in situ (or antibodies). Notably, the second pipeline requires no prior markers beyond the Gal4 or LexA line expressed in single neuronal populations. Both pipelines result in a transcriptome that can be used to identify (a) TFs for their role in neuronal specification and/or maintenance, (b) cell surface molecules that may regulate neuronal morphology and/or connectivity, or (c) functionally relevant genes encoding ion channels, neuropeptides, receptors, and signaling pathways.

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
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>20xUAS-FLPG5.PEST;worniu-gal4,asense-gal80; Act5c(FRT.CD2)gal4</td>
      <td>Syed et al., 2017</td>
      <td></td>
      <td>Type II lineage immortalization</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>20xUAS-FLPG5.PEST;worniu-gal4,asense-gal80; lexAop(FRT.stop)-mCD8:GFP</td>
      <td>This work</td>
      <td></td>
      <td>Label type II derived lexA + cells</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>TI{2A-lexA::GAD}AstA[2A-lexA]/TM3,Sb[1]</td>
      <td>BDSC</td>
      <td>RRID:BDSC_84356</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>TI{2A-lexA::GAD}Ms[2A-lexA]/TM3,Sb[1]</td>
      <td>BDSC</td>
      <td>RRID:BDSC_84403</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>TI{2A-lexA::GAD}NPF[2A-lexA]/TM3,Sb[1]</td>
      <td>BDSC</td>
      <td>RRID:BDSC_84422</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-RedStinger</td>
      <td>BDSC</td>
      <td>RRID:BDSC_8545</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-unc84-2xGFP</td>
      <td>Henry et al., 2012</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>GMR12D09-lexA/CyO</td>
      <td>BDSC</td>
      <td>RRID:BDSC_54419</td>
      <td>P-EN</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>GMR16D01-lexA</td>
      <td>BDSC</td>
      <td>RRID:BDSC_52503</td>
      <td>P-FN</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>GMR37G12-lexA</td>
      <td>BDSC</td>
      <td>RRID:BDSC_52765</td>
      <td>PF-R</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>13xLexAop2-IVS-myr::smGdP-V5</td>
      <td>BDSC</td>
      <td>RRID:BDSC_62215</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>mouse anti-Cut2B10, monoclonal</td>
      <td>DSHB</td>
      <td>RRID:AB_528186</td>
      <td>2 μg/mL</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>guinea pig anti-DIP-β, polyclonal</td>
      <td>Xu et al., 2024</td>
      <td></td>
      <td>1:300</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>guinea pig anti-E93, polyclonal</td>
      <td>Syed et al., 2017</td>
      <td></td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rabbit anti-Imp, polyclonal</td>
      <td>Syed et al., 2017</td>
      <td></td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rabbit anti-Lim1,polyclonal</td>
      <td>Desplan, New York University</td>
      <td></td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>guinea pig anti-Runt, polyclonal</td>
      <td>Sullivan et al., 2019</td>
      <td></td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>guinea pig anti-Rx, polyclonal</td>
      <td>Desplan, New York University</td>
      <td></td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rabbit anti-Syp, polyclonal</td>
      <td>Syed et al., 2017</td>
      <td></td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rabbit anti-Toy, polyclonal</td>
      <td>Sullivan et al., 2019</td>
      <td></td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>chicken anti-V5, polyclonal</td>
      <td>Fortis Life Sciences, Waltham, MA</td>
      <td></td>
      <td>1 μg/mL</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rat anti-Zfh2, olyclonal</td>
      <td>Tran et al., 2010</td>
      <td></td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>DyLight405, Alexa Fluor 488, Rhodamine Red-X (RRX), or Alexa Fluor 647 conjugated donkey whole IgG, polyclonals</td>
      <td>Jackson ImmunoResearch Laboratories Inc, West Grove, PA</td>
      <td></td>
      <td>5 μg/mL</td>
    </tr>
    <tr>
      <td>Commercial kit</td>
      <td>Evercode WT</td>
      <td>Parse Bioscience</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial kit</td>
      <td>PIPseq 3’ Single Cell RNA T20 kit</td>
      <td>Fluent BioSciences</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R Studio</td>
      <td>Posit Software</td>
      <td></td>
      <td>https://posit.co/products/open-source/rstudio/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Seurat</td>
      <td>Rahul Satija, New York University</td>
      <td></td>
      <td>https://satijalab.org/seurat/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ComplexHeatmap</td>
      <td>Gu, 2022</td>
      <td></td>
      <td>https://github.com/jokergoo/ComplexHeatmap (Gu, 2025)</td>
    </tr>
  </tbody>
</table>

### Single nuclei isolation, library preparation, and sequencing

We first used the split-pool method (Parse Bioscience, Seattle, WA, USA) to barcode RNAs from whole brain to generate a library which includes both T1 and T2 progeny. This library, T1+T2, was used for analysis in Figures 1 and 5. To increase the number of T2 nuclei for snRNAseq, we labeled T2 nuclei by crossing 20xUAS-FLPG5.PEST;worniu-Gal4,asense-Gal80; Act5c(FRT.CD2)Gal4 to UAS-RedStinger (RFP) or UAS-unc84-2xGFP (GFP) flies. The adult flies were aged for 1 week at 25 °C before dissection. Equal amounts of male and female central brains (excluding optic lobes) were dissected at room temperature within 1 hr. The samples were flash-frozen in liquid nitrogen and stored separately at –80 °C. Dissociation of nuclei from the frozen, dissected brains was performed according to published protocols (McLaughlin et al., 2022). RFP +or GFP +nuclei were collected by sorting dissociated nuclei with SONY-SH800 with 100 μm chip. We performed three rounds of sorting and snRNAseq. In the first round, we pooled male and female brains together to select GFP + nuclei and used particle-templated instant partitions to capture single nuclei to generate cDNA library (Fluent BioSciences, Waterton, MA). In the second round, RFP +nuclei from male and female were pooled together. In the third round, RFP +nuclei from male and female brains were collected separately. The split-pool method was then used to generate barcoded cDNA libraries from each individual nucleus from the second and third rounds. All libraries were sequenced with pair-ends reads 150 bp on Illumina Novaseq 6000 (University of Oregon’s Genomics and Cell Characterization Core Facility).

#### snRNA-seq analysis

Our bioinformatic analysis was performed using pipeline from Fluent BioSciences, Parse Bioscience, and the Seurat R package (Hao et al., 2024; Satija et al., 2015). Briefly, pipelines from Fluent BioSciences and Parse Biosciences were used to perform demultiplexing, alignment, filtering, counting of barcodes and UMIs with an output being a cell-by-genes matrix of counts. We aligned our sequences to a custom reference genome by adding flpD5 (RRID:Addgene_32132), redstinger (RRID:Addgene_46165), and unc84sfGFP (RRID:Addgene_46023; +SV40 tail) sequences and annotations to the Drosophila genome release BDGP6.32.109.To further ensure that only high-quality cells were retained, we removed any cells with fewer than 200 genes or more than 2500 genes expressed and more than 5% mitochondrial RNA. For the T2 atlas, snRNA-seq data from three rounds of sorting and barcoding were integrated in Seurat with Anchor-based RPCA integration to generate an integrated dataset, and the downstream analysis was performed with the default parameters. The UMAP was generated with resolution 12. The integrated dataset was used for analyses.

#### Glia analyses

The T1+T2 glia atlas dataset was derived from the T1+T2 repo+ glial clusters and re-clustered to represent the glial subtypes. The T2 glia atlas was derived from the T2 repo+ glial clusters and re-clustered to represent the glial subtypes. Cell identity was determined by the validated markers for glia shown to differentially expressed between the clusters. Identities were assigned based on expression of these validated markers. Overlapping identities were assigned if multiple subtype markers were expressed within a single cluster.

#### Sex differences

We determined sex-biased clusters within the T2 glia and neuron atlases by identifying clusters that were disproportionate after normalizing the number of inputs for ‘female’ and ‘male’ samples respectively. The ‘female and male’ mixed samples were excluded from the analyses as we could not differentiate the sex origin of these nuclei. To determine differential gene expression between females and males, we pseudo bulked nuclei by aggregating the snRNAseq for comparison between sex and clusters. Heatmaps were generated in Seurat using the Scillus package (https://github.com/xmc811/Scillus; Xu, 2021) to display the heatmap. Both male and female Drosophila melanogaster were used for input into the RNA-seq pipeline.

#### Transcription factor combinatorial analysis

We used the Seurat function FindAllMarkers to find positively differentially expressed TFs in all clusters. We then removed TFs which were not significantly differentially expressed. We gave a value of 1 to any TF that was found to be a positive marker in each cluster and a value of 0 in clusters which it was not a positive marker. Next, we found the number of unique combinations of markers for six classes (zinc finger, helix-turn-helix, homeodomain, basic domain, unidentified DNA binding domain, and high motility group) of TFs. The Jaccard index between each cluster was then calculated and clusters were sorted from most to least similar. The python packages Matplotlib and Seaborn were then used to generate heatmaps.

#### Immunohistochemistry and imaging

Standard methods were used for adult brain staining (Sullivan et al., 2019). The antibody stained brains were mounted in DPX (https://www.janelia.org/project-team/flylight/protocols) on poly-L-Lysine coated coverslip (Corning, Glendale, AZ) and imaged with Zeiss confocal LSM800 with software Zen.

#### Contact for reagent and resource sharing

Further information and requests for resources and reagents should be directed to and will be fulfilled by the corresponding author Chris Doe (cdoe@uoregon.edu).

#### Figure production

We used Imaris (Bitplane, Abingdon, UK) for confocal image processing, and Illustrator (Adobe, San Jose, CA) to assemble figures.
