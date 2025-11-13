# Coopted temporal patterning governs cellular hierarchy, heterogeneity and metabolism in Drosophila neuroblast tumors

## Authors

- Sara Genovese<sup>1</sup>
- Raphaël Clément<sup>1</sup>
- Cassandra Gaultier<sup>1</sup> ([ORCID: 0000-0001-6401-9163](https://orcid.org/0000-0001-6401-9163))
- Florence Besse<sup>2</sup> ([ORCID: 0000-0003-4672-1068](https://orcid.org/0000-0003-4672-1068))
- Karine Narbonne-Reveau<sup>1</sup>
- Fabrice Daian<sup>1</sup>
- Sophie Foppolo<sup>1</sup>
- Nuno Miguel Luis<sup>1</sup> ([ORCID: 0000-0001-5438-9638](https://orcid.org/0000-0001-5438-9638))
- Cédric Maurange<sup>1</sup> ([ORCID: 0000-0001-8931-1419](https://orcid.org/0000-0001-8931-1419)) †

### Affiliations

1. Aix Marseille Univ, CNRS, IBDM, Equipe Labellisée LIGUE Contre le Cancer Marseille France
2. Université Côte d’Azur, CNRS, Inserm, Institut de Biologie Valrose Nice France

† Corresponding author

## Abstract

It is still unclear what drives progression of childhood tumors. During Drosophila larval development, asymmetrically-dividing neural stem cells, called neuroblasts, progress through an intrinsic temporal patterning program that ensures cessation of divisions before adulthood. We previously showed that temporal patterning also delineates an early developmental window during which neuroblasts are susceptible to tumor initiation (Narbonne-Reveau et al., 2016). Using single-cell transcriptomics, clonal analysis and numerical modeling, we now identify a network of twenty larval temporal patterning genes that are redeployed within neuroblast tumors to trigger a robust hierarchical division scheme that perpetuates growth while inducing predictable cell heterogeneity. Along the hierarchy, temporal patterning genes define a differentiation trajectory that regulates glucose metabolism genes to determine the proliferative properties of tumor cells. Thus, partial redeployment of the temporal patterning program encoded in the cell of origin may govern the hierarchy, heterogeneity and growth properties of neural tumors with a developmental origin.

## Introduction

Central nervous system (CNS) tumors are rare and constitute less than 2% of all cancers in adults. In contrast, they represent more than 25% of cancer cases in children (including medulloblastoma, retinoblastoma, rhabdoid tumors (AT/RT), gliomas etc), suggesting that the developing CNS is particularly sensitive to malignant transformation (Arora et al., 2009; Curado et al., 2007). Moreover, unlike most adult tumors, pediatric tumors are often genetically stable and their initiation and progression do not necessarily require the accumulation of mutations in multiple genes. For example, the biallelic inactivation of a single gene is sometimes sufficient to trigger malignant growth as illustrated by mutations in the RB1 and SMARCB1 genes in retinoblastoma and rhabdoid tumors respectively (Biswas et al., 2016; Gröbner et al., 2018; Marshall et al., 2014; Puisieux et al., 2018; Scotting et al., 2005; Vogelstein et al., 2013). Recent studies suggest that CNS pediatric tumors such as medulloblastomas recapitulate the fetal transcription program that was active in the cell of origin (Vladoiu et al., 2019). However, it remains unclear how the invalidation of single genes during fetal stages can disrupt on-going developmental programs to trigger malignant growth, and whether these fetal/developmental programs influence the heterogeneity, composition, and proliferative properties of cells composing CNS tumors.

Faced with the complexity of brain development and neural tumors in mammals, simple animal models can represent a powerful alternative to investigate basic and evolutionary conserved principles. The development of the CNS is undoubtedly best understood in Drosophila (Homem and Knoblich, 2012). The Drosophila CNS arises from a small pool of asymmetrically-dividing neural stem cells (NSCs), called neuroblasts (NBs). NBs possess a limited self-renewing potential. They divide all along development (embryonic and larval stages) to self-renew while generating daughter cells named Ganglion Mother Cells (GMCs) (Maurange and Gould, 2005). GMCs then usually divide once to produce two post-mitotic neurons or glia. NBs are the fastest cycling cells during development, able to divide every hour during larval stages when most of the neurons are produced (Truman and Bate, 1988). However, all NBs terminate during metamorphosis and are absent in adults. Two antagonistic RNA-binding proteins, IGF-II mRNA-binding protein (Imp) and Syncrip (Syp) are essential to first promote and then conclude this formidable period of activity. During early larval development (L1/L2), NBs express Imp that promotes NB self-renewal. Around late L2/early L3, NBs silence Imp to express Syp that remains expressed until NB decommissioning during metamorphosis (Yang et al., 2017). This Imp-to-Syp transition is essential to render NBs competent to respond to subsequent pupal pulses of the steroid hormone ecdysone and initiate a last differentiative division (Homem et al., 2014; Yang et al., 2017). Failure to trigger the transition results in NBs permanently dividing in adults (Maurange et al., 2008; Narbonne-Reveau et al., 2016; Yang et al., 2017). The Imp-to-Syp transition appears to be mainly regulated by a NB intrinsic timing mechanism driven by the sequential expression of transcription factors (Narbonne-Reveau et al., 2016; Ren et al., 2017; Syed et al., 2017). This series of factors, also known as temporal transcription factors, has been first identified for its ability to specify different neuronal fates produced by NBs as they divide (Bayraktar and Doe, 2013; Isshiki et al., 2001; Li et al., 2013). In addition, temporal transcription factors also schedule the Imp-to-Syp transition to ensure that NBs will not continue cycling in adults. Recent transcriptomic analyses indicate that other genes are dynamically transcribed in NBs throughout larval stages, although their function and epistatic relationship with temporal transcription factors and the Imp/Syp module are unclear (Liu et al., 2015; Ren et al., 2017; Syed et al., 2017) All together, these studies highlight a complex, but still relatively unexplored, temporal patterning system in larval NBs.

Perturbation of the asymmetric division process during early development can lead to NB exponential amplification. In such conditions, the NB-intrinsic temporal program limiting self-renewal appears to become inoperant, and uncontrolled NB amplification is observed. Serial transplantations of asymmetric division-defective NBs have revealed an ability to proliferate for months, if not years, demonstrating tumorigenic characteristics (Caussinus and Gonzalez, 2005). Perturbation of asymmetric divisions can be induced by the inactivation of the transcription factor Prospero (Pros) in type I NB lineages (most lineages in the ventral nerve cord (VNC) and central brain (CB)). During development, Pros is strongly expressed in GMCs where it accumulates to induce cell cycle-exit and neuronal or glial differentiation (Choksi et al., 2006; Hirata et al., 1995; Matsuzaki et al., 1992). GMCs that lack pros fail to differentiate and revert to a NB-like state. This triggers rapid NB amplification at the expense of neuron production (Bello et al., 2006; Caussinus and Gonzalez, 2005). We have previously shown that inactivation of pros in NBs, and their subsequent GMCs, before mid-L3 (L3 being the last larval stage) leads to aggressive NB tumors that persist growing in adults. In contrast, inactivation of pros after mid-L3 leads to transient NB amplification and most supernumerary NB properly differentiate during metamorphosis, leading to an absence of growing tumors in adults (Narbonne-Reveau et al., 2016). Interestingly, propagation of NB tumor growth beyond normal developmental stages is caused by the aberrant maintenance of Imp and the transcription factor Chinmo from early-born GMCs, the latter representing the cells of origin of such aggressive tumors (Narbonne-Reveau et al., 2016). Chinmo and Imp positively cross-regulate and inactivation of either in NB tumors stops tumorigenic growth. Because pros-/- NB tumors can only be induced during an early window of development, and are caused by the biallelic inactivation of a single gene, they represent an exciting and simple model to investigate the basic mechanisms driving the growth of tumors with an early developmental origin, such as in the case of pediatric CNS cancers.

NB tumors can also be induced from type II NBs (a small subset of NBs in the central brain) or from neurons upon inactivation of the NHL-domain family protein Brat or Nerfin-1 respectively (Bello et al., 2006; Betschinger et al., 2006; Lee et al., 2006) (Froldi et al., 2015). In both cases, tumor growth appears to rely on the aberrant expression of the Chinmo/Imp module arguing for a general tumor-driving mechanism in the developing Drosophila CNS (Narbonne-Reveau et al., 2016). Interestingly, in the different types of NB tumors, Chinmo and Imp are only expressed in a subpopulation of cells, demonstrating heterogeneity in the population of tumor NBs (tNBs). However, the full repertoire of cells composing the tumor, the rules governing the cellular heterogeneity and the mechanisms determining the proliferative potential of each cell type remain to be investigated.

Here, we use single-cell RNA-seq, clonal analysis and numerical modeling to investigate these questions. We identify a subset of genes involved in the temporal patterning of larval NBs that are redeployed in tumors to generate a differentiation trajectory responsible for creating tumor cell heterogeneity. This cellular heterogeneity results in NBs with different types of metabolism and different proliferative properties. We also decipher a robust hierarchical scheme that drives reproducible heterogeneity through the dysregulated but fine-tuned transition between the two RNA-binding proteins Imp and Syp. This work thus identifies a core larval NB temporal patterning program, the disruption of which not only causes unlimited growth but has an overarching role in governing the cellular hierarchy, heterogeneity and metabolism of NB tumors.

## Results

### Single-cell RNA-seq reveals that a subset of larval NB temporal patterning genes are major contributors of cellular heterogeneity within NB tumors

To investigate the cellular heterogeneity existing in a given type of NB tumor, we performed single-cell RNA-seq experiments. To minimize inter-tumor heterogeneity that could result from inducing tumors with different NBs of origin, tumors were induced from the early L2 stage, when NBs exit quiescence, by knocking down pros in the six homologous poxn NBs of the VNC (one per hemisegment) using the poxn-Gal4, UAS-prosRNAi, UAS-GFP, UAS-dicer2 system - thereafter referred to as poxn > prosRNAi. We had previously demonstrated that early NB amplification triggered during early larval stages by the poxn > prosRNAi system led to tumors that persist and expand in adults (Narbonne-Reveau et al., 2016). Single-cell RNA-seq was performed on dissociated and FACS-sorted GFP+ tNBs obtained from 56 poxn > prosRNAi tumors dissected and pooled from adults aged between 4 to 6 days (tumors were therefore induced 11 to 13 days earlier).

Using the Chromium (10x Genomics) approach, we sequenced 5740 cells with a median number of 1806 genes/cell (Figure 1—figure supplement 1A). Filtering, normalization, variable gene identification, regression of cell-cycle genes, linear dimensional reduction, and principal component analysis (PCA) were performed with the R package Seurat (Butler et al., 2018) (Figure 1—figure supplement 1A,B). PC3, PC4 and PC7 in particular caught our attention, as they all identify the early and late larval NB temporal markers, Imp and Eip93F (E93) (Syed et al., 2017), being expressed in different subsets of tNBs (Figure 1A and Figure 1—figure supplement 1C). This indicates that early and late larval NB markers are major components defining cellular heterogeneity in NB tumors.

![Figure 1.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig1-v2.jpg)

**Figure 1.:** (A) PCA was performed on single-cell tNB transcriptomes to reduce the dimensions of the data for further analysis. Genes (rows) and cells (columns) are ordered by their PCA scores, and the 500 most extreme cells and 30 most extreme genes on both sides of the distribution are shown in the heatmap. PC4 reveals that tNBs can be discriminated by the expression of early (light red asterisks) vs late (light blue asterisks) larval NB temporal patterning genes. Other larval temporal genes are found in PC3 and PC7 (Figure 1—figure supplement 1C). (B) The UMAP representation of all single cells included in our analysis shows the separation of different clusters. We used a k-nearest neighbor algorithm to call seven clusters, which are shown in different colors on the UMAP plot. (C) Expression of Mira, early and late temporal markers on the UMAP map shown in B. (D) Cartoon representing a ventral view of an adult CNS containing a NB tumor induced during larval stages in the VNC. Green circles are tNBs. Green circles colored in red represent Chinmo+Imp+ tNBs. Immunostainings with anti-Chinmo, anti-Imp and anti-Syp, indicating that Imp/Chinmo and Syp are expressed in a complementary pattern in poxn > prosRNAi tumors found in 4-day-old adults. tNBs are labeled with Mira. Scale bar 20 µm. (E) Immunostainings with anti-Chinmo and anti-E93 indicating that these two transcription factors are expressed in a complementary pattern in poxn > prosRNAi tumors found in 4-day-old adults. tNBs are marked with anti-Mira. Scale bar 20 µm. (F) The light red and blue colors respectively designate ‘early’ and ‘late’ larval NB genes as determined by Liu et al. (2015), Syed et al. (2017) and Ren et al. (2017). A subset of these genes are redeployed in tumors to define distinct tNB states. Asterisks mark temporal patterning genes regulated at the post-transcriptional level in tNBs. Note that cas and svp transcription is associated with early Imp+ NBs, while br transcription is associated with late E93+ NBs during larval stages. In contrast, cas, svp and br transcription do not distinguish Imp+ and E93+ tNBs.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Plots depicting the number of genes detected in each cell (nFeature_RNA), the number of unique RNA molecules detected in each cells (nCount-RNA), and the percentage of reads mapping to the mitochondrial genome (percent.mt). (B) Plot of the standard deviations of PCs used to determine the number of PCs to include in downstream analyses of the RNA-seq analysis. (C) Heatmaps depicting the composition of the first 12 PCs. Light red asterisks mark early larval temporal patterning genes. Blue asterisks mark late larval temporal patterning genes.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Expression levels of various marker genes for NBs (dpn); cholinergic, glutamatergic and GABAergic neurons (VAChT, VGlut and Gad1 respectively); and glia (repo); on the UMAP map. (B) Expression levels of genes enriched in the small clusters 5 and 6. (C) Heatmap depicting the top 10 most highly expressed genes in each cluster compared to all other clusters. Cluster three is highly enriched in early larval NB markers (red asterisks). (D) Upper Venn diagram depicts overlaps between genes, the expression of which is enriched in early NBs of various lineages (Mushroom Body (MB), Antennal Lobe (LB), Type II)) and in cluster 2 of tNBs. Lower Venn diagram depicts overlaps between genes enriched in late NBs of various lineages (MB, AL, Type II) and in cluster 0,1,3,4 of tNBs. Early or late temporal NB genes overlapping with tumor genes are indicated.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Lists of genes enriched in NBs at various timepoints during larval development (24 hr after larval hatching (ALH), 36 hr, 50 hr, 84 hr). Lists have been extracted for Mushroom body (MB) NBs, antennal lobe (AL) NBs and type Liu et al. (2015) and Ren et al. (2017). Darks backgrounds encompass early genes, while light backgrounds encompass late larval genes. Expression of the gene br, a well-known marker for late NBs, has been chosen as the transition time from an early to late stage. Dark and light orange backgrounds represent genes that distinguish the Imp+ Cluster two from the E93+ Clusters 0,1,3,4 in the UMAP representation of tumor cells. A subset of temporal patterning genes highlighted in red distinguish Imp+ or E93+ clusters in the tumors.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** The UAS-mCherrychinmoUTRs transgene (Dillard et al., 2018) is transcribed in all tNBs using the poxn-GAL4 driver. However, the mCherry protein (anti-RFP immunostaining in red) is only present in tNBs that express endogenous Chinmo (anti-Chinmo immunostaining in grey). This demonstrates post-transcriptional regulation via the chinmo UTRs in tNBs. This is consistent with the ubiquitous presence of chinmo mRNA in all tNBs as detected with the single-cell RNA-seq protocol.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** (A) grh mRNA is detected in most if not all tNBs throughout the UMAP representation. (B) All tNBs in 4 day-old adult express grh as shown by immunostainings.

We next proceeded to graph-based clustering. This led to a UMAP representation composed of five main clusters and two smaller ones (Figure 1B). Although tNBs poxn > prosRNAi tumors may occasionally differentiate in neurons (Narbonne-Reveau et al., 2016), poxn-GAL4 is only active in the tNB population. Therefore, we expected the population of GFP+ cells after FACS sorting to be exclusively composed of tNBs. Consistently, NB identity genes like miranda (mira) or deadpan (dpn), appeared homogeneously distributed on the UMAP representation while genes defining cholinergic (VAChT), GABAergic (Gad1) and glutamatergic (VGlut) neurons were absent (Figure 1C and Figure 1—figure supplement 2A). Similarly, pan-glial genes (repo) were not detected (Figure 1—figure supplement 2A). The two smaller clusters appear to be composed of tNBs expressing stress or growth arrest factors such as Gadd45, Irbp18, Xrp1 and GstE6 possibly composing a sub-population of tNBs under cellular stress (Figure 1—figure supplement 2B) (Akdemir et al., 2007; Francis et al., 2016; Lee et al., 2018). Differential expression analysis identifies ‘cluster 2’ (1268 out of 5740 cells (22%)) as being strongly defined by the expression of the early NB temporal marker Imp (Figure 1C and Figure 1—figure supplement 2C). In contrast, E93 expression inversely correlates with Imp expression on the UMAP representation, being strongly expressed throughout all other clusters (Figure 1C). The presence of 4 large clusters (clusters 0, 1, 3, 4) within the E93 expression domain on the UMAP representation implies further cellular heterogeneity within the E93+ tNB population (Figure 1B and Figure 1—figure supplement 2C). We then crossed the list of genes that discriminates the Imp+ cluster 2 from the E93+ clusters (0, 1, 3, 4) with the lists of genes that are temporally regulated in either the mushroom body NBs, antennal lobe NBs or the type II NBs during larval development (Liu et al., 2015; Ren et al., 2017) (Figure 1—figure supplement 3). We found that the genes encoding for the transmembrane transporters Oatp74D and SP1173, the Ig-superfamily transmembrane protein Plum, the glucose metabolism protein Gapdh2, the cytoskeleton protein Chd64, as well as CG10939, CG44325, CG10512 and CG5953 distinguish the Imp+ identity in both NBs during development and tNBs in tumors. In contrast, the CDC25 gene string (stg), CG15628, CG15646 and the long non-coding RNA noe constitute a subset of genes whose transcription distinguishes the E93+ identity in both NBs during development and tNBs in tumors (Figure 1C, Figure 1—figure supplement 3 and Figure 1—figure supplement 2D). Thus, a subset of larval NB temporal patterning genes is redeployed in tumors defining various tNB states.

Of note, chinmo mRNA is globally strongly expressed throughout all clusters (Figure 1C). This is reminiscent of its known post-transcriptional regulation in NBs throughout development (Dillard et al., 2018; Zhu et al., 2006). Consistent with a post-transcriptional regulation of chinmo in tumors, we found that forced transcription of a UAS-mCherrychinmoUTRs transgene, in which the mCherry ORF is flanked by the 5’ and 3’ UTRs of chinmo (Dillard et al., 2018), in the tumor led to mCherry expression only in the tNBs that express the endogenous Chinmo (Figure 1—figure supplement 4). Chinmo+ tNBs also co-express Imp (Figure 1D). Thus, as in NBs during development, chinmo is regulated at the post-transcriptional level in tumors. During development, chinmo is post-transcriptionally silenced by Syp whose expression is activated in late NBs (Liu et al., 2015; Ren et al., 2017; Syed et al., 2017). Surprisingly, in tumors, Syp mRNA is not restricted to E93+ tNBs, as it is also highly transcribed in the Imp+ tNBs of cluster 2 (Figure 1C). However, when Syp expression was assessed by immunostaining in 6 days-old adult tumors, Syp was absent from Chinmo+Imp+ tNBs. Instead anti-Syp immunostaining labeled most if not all other tNBs, that were also positive for anti-E93 (Figure 1D,E). Thus, unlike in larval NBs where Syp is transcriptionally controlled along development, its expression in tNBs appears to be regulated mainly at the post-transcriptional level. We also find that the temporal transcription factors cas and svp that are expressed in Imp+ NBs during early larval stages (Maurange et al., 2008; Ren et al., 2017; Syed et al., 2017) are not enriched in cluster 2 indicating further differences between Imp+ NBs during development and tumorigenesis (Figure 1—figure supplement 3). In addition, while the transcription factor Broad (Br) is a pan-NB marker of late temporal identity during larval development (Liu et al., 2015; Maurange et al., 2008; Ren et al., 2017; Syed et al., 2017) (Figure 1—figure supplement 3), it is not enriched in E93+ tNBs demonstrating differences with late larval NBs (Figure 1—figure supplement 3). Lastly, single-cell RNA-seq and immunostainings also showed that all tNBs express the late embryonic and larval temporal transcription factors Grh (Figure 1—figure supplement 5) (Brody and Odenwald, 2000). This suggests that tNBs do not reverse to an early embryonic temporal identity.

Although lin-28 is known to be expressed in early larval NBs and in Chinmo+Imp+ tNBs (Narbonne-Reveau et al., 2016), mRNA levels appear to stand below the detection limit of the 10x technology, a current limitation of droplet-based assays, as it is hardly detected and not enriched in ‘cluster 2’ containing Imp+ tNBs (Figure 1C and Figure 1—figure supplement 3). Low cellular levels of lin-28 mRNA are consistent with a previous RNA-seq experiment on bulk tumors performed by the lab (about 120 times lower than levels of Imp mRNAs) (Narbonne-Reveau et al., 2016).

In conclusion, single cell transcriptomics identify a number of larval NB temporal patterning genes that are redeployed in tumors to define distinct tNB subpopulations (Figure 1F). Of these, Chinmo+Imp+ tNBs and Syp+E93+ tNBs, as defined by immunostainings, compose two exclusive subpopulations encompassing most if not all tNBs.

### poxn > prosRNAi NB tumors progress to reproducible heterogeneity

To investigate how tumor heterogeneity emerges and is regulated during the course of tumor growth, we co-stained tumors for Chinmo and Syp (respective markers for the Chinmo+Imp+ and Syp+E93+ tNBs) as they grow from their initiation during early larval to adult stages. Immuno-stainings performed about 24 hours after pros knockdown (late L2 stage) indicated that poxn+ NBs initially amplify to form small pools of Chinmo+Imp+ tNBs (Figure 2A).

![Figure 2.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig2-v2.jpg)

**Figure 2.:** (A,B) Cartoons represent a ventral view of the Drosophila CNS at late L2 and late L3. Gray circles represent normal NBs. Green circles are prosRNAi tNBs. Red tNBs express chinmo. Tumors were induced by knocking down pros in six NBs located in the VNC, throughout larval development, using the poxn-Gal4, UAS-prosRNAi, UAS-GFP, UAS-dicer2 system (poxn > prosRNAi). Because chinmo is always co-expressed with Imp in NBs, we use either anti-Chinmo or anti-Imp to label Chinmo+Imp+ tNBs. We also used Syp to label Syp+E93+ tNBs. (A) poxn > prosRNAi initially induces pools of tNBs all expressing Chinmo in early larvae (L2). tNBs are marked with anti-Mira and anti-GFP. (B) In late larvae (L3), poxn > prosRNAi tumors are composed by two distinct populations of tNBs respectively expressing Chinmo and Syp. Tumors are marked with anti-GFP and delineated by dashed lines. (C) Mitotic Imp+ tNBs and Syp+tNBs are marked with anti-PH3 in poxn > prosRNAi tumors persisting in 4-day-old adults. (D) Quantification of the mitotic index of Chinmo+Imp+ tNBs (n = 7 VNCs) and Syp+E93+ tNBs (n = 7 VNCs) in poxn > prosRNAi tumors of 4-day-old adults. p=0.0006. (E) Proportion of Chinmo+Imp+ tNBs over all tNBs composing tumors (volumes of each population are measured) at 8 days (8d) (n = 5), 10d (n = 6), 11d (n = 6) and 15d (n = 6) after tumor induction. Each dot represents the % for one tumor. (F) Scheme depicting the dynamics of tumor composition: from a homogeneous pool of Chinmo+Imp+ tNBs in early larvae to a heterogeneous tumor with a minor population of Chinmo+Imp+ and a majority of Syp+E93+ tNBs. Scale bars, 20 µm.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The G-TRACE system allows the permanent GFP labeling of neurons generated by poxn > prosRNAi tNBs. Tumor neurons, marked with anti-GFP and anti-Elav, are usually grouped and represent a minor population of cells poorly contributing to tumor mass in 4-day-old poxn > prosRNAi adult tumors. Tumor neurons localize outside the Chinmo+Imp+ tNB clusters marked with anti-GFP and anti-Imp.

No Syp+ tNBs are present at this stage. However, from early to late L3, a distinct population of Syp+ tNBs emerges within tumors (Figure 2B). Thus, Syp+ tNBs appear in tumors at about the time when normal NBs undergo the Imp-to-Syp switch regulated by the progression of temporal transcription factors (Maurange et al., 2008; Narbonne-Reveau et al., 2016; Ren et al., 2017; Syed et al., 2017). In adults, Chinmo+Imp+ tNBs are encountered in small clusters surrounded by large fields of Syp+ tNBs (Figure 1D). Thus, the initial pool of Chinmo+Imp+ tNBs evolves to generate tumors with two distinct compartments. Both the Chinmo+Imp+ and Syp+E93+ compartments show mitotic activity (Figure 2C), although the mitotic index is globally lower in the Syp+E93+ compartment (Figure 2D).

Then, following immunostaining, confocal imaging and 3D reconstruction, we quantified the proportion of Chinmo+Imp+ and Syp+E93+ tNBs within tumors aged of 8, 10, 11 and 15 days (induced in L2 and dissected in 1, 3, 4, and 8-day-old adults respectively). In total, more than 20 tumors were dissected and we reproducibly found a relatively invariant proportion of 20% of Chinmo+Imp+ tNBs (±10) at the different time-points (Figure 2E). This proportion is consistent with the proportion of Imp+ tNBs composing ‘cluster 2’ identified with the single-cell RNA-seq analysis performed from tumors of 4-to-6-day-old adults (tumors induced 11 to 13 days earlier) (Figure 1C,D). Thus, Chinmo+Imp+ tNBs globally exhibit a higher mitotic index but, counterintuitively, they rapidly become a minority compared to Syp+E93+ tNBs (Figure 2E,F). Note that neurons deriving from tNBs are rare in the bulk of the tumor and only mildly contribute to the tumor mass (Figure 2—figure supplement 1). In conclusion, poxn > prosRNAi tumors rapidly evolve from a homogenous population of Chinmo+Imp+ tNBs in early larvae to a heterogeneous population of Chinmo+Imp+ and Syp+E93+ tNBs in adults. In adults, tNB populations appear to reach a relatively stable equilibrium where Chinmo+Imp+ tNBs are in minority despite an apparent higher mitotic index. The intertumoral reproducibility of this population dynamics suggests the existence of robust intratumoral constraints.

### poxn > prosRNAi NB tumors follow a rigid hierarchical scheme

To investigate in details the rules governing the population dynamics of Chinmo+Imp+ and Syp+E93+ tNBs, we designed lineage analysis experiments in vivo. We used the Flybow technique combined with our poxn > prosRNAi system to generate random mCherry-labeled clones in otherwise GFP+ tumors (Hadjieconomou et al., 2011). Clones were randomly induced at low frequency (in about 1% to 2% of tNBs) in 2-day-old adults containing poxn > prosRNAi tumors, and examined along a time course. Of note, even 12 days after clonal induction (ACI), clones could be easily delineated, with mCherry+ cells depicted no or little dispersion denoting no active migration (Figure 3—figure supplement 1). This allowed us to characterize individual mCherry+ clones 8 hours, 2 days, 4 days and 8 days ACI (Figure 3A). We used Chinmo as a marker for Chinmo+Imp+ tNBs and its absence as a marker for Syp+E93+ tNBs. Along this time lapse, we could observe three categories of clones: clones exclusively composed of Chinmo+Imp+ tNBs (further termed CI clones), MIXED clones composed of both Chinmo+Imp+ and Syp+E93+ tNBs (they therefore contain at least two tNBs), and clones exclusively composed of Syp+E93+ tNBs (further termed SYP clones) (Figure 3C). The existence of clones exclusively composed of either Chinmo+Imp+ or Syp+E93+ tNBs is consistent with the ability of both types of tNBs to undergo self-renewing divisions. In addition, the existence of a subset of MIXED clones implies that Chinmo+Imp+ or Syp+E93+ tNBs may derive from a common precursor of either identity. In addition, clones display a large heterogeneity in their size at 8 days ACI (Figure 3A,B), indicating that all tumor cells do not possess the same proliferation potential. Interestingly, we observed that the proportion of the different categories of clones is dynamic over the period of 8 days. The proportion of CI clones exhibits a rapid decrease that is paralleled with an increase in the proportion of MIXED clones and a slight increase in the proportion of SYP clones (Figure 3D). We sought to investigate whether these clonal dynamics could reflect hierarchical rules within the tumor.

![Figure 3.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig3-v2.jpg)

**Figure 3.:** (A) Clones are labeled with mCherry and observed 8 hours (8h), 2 days (2d), 4 days (4d) and 8 days (8d) after clonal induction (ACI) in poxn > prosRNAi tumors. mCherry- tNBs are GFP+. Images represent one confocal section. (B) 3D projections of clones 8 hr, 2d, 4d and 8d ACI. The color-code labels clones according to their volume. (C) Three categories of clones can be identified in poxn > prosRNAi tumors: clones composed of Chinmo+Imp+ tNBs only (CI clones), clones composed of both Chinmo+Imp+ and Syp+E93+ tNBs (MIXED clones), and clones composed of Syp+E93+ tNBs only (SYP clones). Chinmo+Imp+ tNBs are identified by the presence of Chinmo. Syp+ tNBs are identified by the absence of Chinmo. (D) Proportion of CI (red), MIXED (gray) and SYP (blue) clones 8h, 2d, 4d and 8d ACI. Proportion of CI clones 8h ACI (n = 117 clones from 4 VNCs); 2d ACI (n = 75 clones from 4 VNCs); 4d ACI (n = 13 clones from 5 VNCs); 8d ACI (n = 17 clones from 5 VNCs). P between CI clones at 8h and 2d ACI -> PCI8h/2d = 0.2; PCI2d/4d = 0.016; PCI4d/8d = 0.88. Proportion of MIXED clones 8h ACI (n = 8 clones from 4 VNCs); 2d ACI (n = 28 clones from 4 VNCs); 4d ACI (n = 57 clones from 5 VNCs); 8d ACI (n = 66 clones from 5 VNCs). PMIXED8h/2d = 0.029; PMIXED2d/4d = 0.016; PMIXED4d/8d = 0.31. Proportion of SYP clones 8h ACI (n = 181 clones from 4 VNCs); 2d ACI (n = 196 clones from 4 VNCs); 4d ACI (n = 200 clones from 5 VNCs); 8d ACI (n = 255 clones from 5 VNCs). PSYP8h/8d = 0.016. Scale bars, 20 µm.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The picture depicts a large mCherry+ clones within an adult poxn > prosRNAi tumor 12 days after clonal induction. Clones were induced using the Flybow technique in tumors from 2 day-old adults. mCherry+ clone cells do not disperse allowing the tracking and examination of individual clones over long periods of time.

For this purpose, we designed a stochastic numerical model of clone growth (see Materials and methods for details). The model follows a simple algorithm (Figure 4A). Each clone starts from a single tNB. In the model, Chinmo+Imp+ tNBs are referred to as C cells while Syp+E93+ tNBs are referred to as S cells. The initial tNB can either be Chinmo+Imp+ (probability $p_{c}$) or Syp+E93+ (probability $1-p_{c}$). At each numerical time step, each cell in the clone (initially one) has a given probability to divide, set by its division time (Tc and Ts). Upon division, Chinmo+Imp+ tNBs can either duplicate (C→CC), generate two Syp+E93+ tNBs (C→SS), or undergo fate asymmetric division (C→CS). Similarly, Syp+E93+ tNBs can either duplicate (S→SS), generate two Chinmo+Imp+ tNBs (S→CC), or undergo fate asymmetric division (S→CS). Each new tNB has a probability to exit the cell-cycle and enter quiescence. In modeling terms, we asked whether hierarchical or plastic schemes of cell divisions are compatible with the proportions of clone categories observed experimentally.

![Figure 4.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig4-v2.jpg)

**Figure 4.:** (A) Cartoon of the stochastic clone model. C stands for Chinmo+Imp+ tNBs, S stands for Syp+E93+ tNBs. Tc means ‘division time of Chinmo+Imp+ tNBs’, Ts means ‘division time of Syp+E93+ tNBs’. Cq stands for quiescent Chinmo+Imp+ tNB, Sq stands for quiescent Syp+E93+ tNB. qc and qs are the probabilities for Chinmo+Imp+ and Syp+E93+ tNBs to be quiescent after being generated. (B) Dynamics of proportion for each clone category in four extreme model scenarios: No hierarchy, Strict hierarchy #1, Strict hierarchy #2, Plastic hierarchy. Solid lines represent the simulations (n = 1000 clones), dots represent experimental measurements. Cartoons above graphs represent the division probabilities used to generate each graph. (C) Violin plots depicting distributions of clone sizes (number of cells) for each category calculated from the experiments. (D) Violin plots depicting distributions of clone sizes (number of cells) for each category of clones after simulation, using the set of parameters minimizing the error. Center lines of boxes show the medians. (E) Proportion of clones over time in each category using the set of parameters minimizing the error. Solid lines represent the simulations (n = 1000 clones), dots represent experimental measurements. (F) Hierarchical scheme able to recapitulate the dynamics of clone growth and composition, with the parameters measured from the experimental data and defined by the fit. (G) Proportion of clones in each category using the set of parameters minimizing the error while allowing a small chance of reverse division from S to C (top: 1%, bottom: 5%).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Clones within tumors are labeled with mCherry and observed 2 days (2d) after clonal induction (ACI) in poxn > prosRNAi tumors. Three categories of two-cell clones can be identified in poxn > prosRNAi tumors: clones composed of two Chinmo+Imp+ tNBs (CI clones), clones composed of one Chinmo+Imp+ tNB and one Syp+E93+ tNB (MIXED clones), and clones composed of two Syp+E93+ tNBs (SYP clones). Chinmo+Imp+ tNBs are marked by the presence of Chinmo. Syp+ tNBs are identified by the absence of Chinmo. Images represent one confocal section. Scale bars, 20 µm.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Top left: error on clone compositions; bottom left: error on clone sizes; right: combined error.

We first tested four simplified scenarios, in which we neglected quiescence and asymmetric divisions, and assumed that C and S cells have the same division time. In each case, we simulated the growth of 1000 clones and plotted the proportion of clones in each category. In the first scenario (‘No hierarchy’), Chinmo+Imp+ tNBs have 50% chance to duplicate (symmetric self-renewing divisions C→CC), and 50% chance to divide into two Syp+E93+ tNBs (C→SS). Similarly, Syp+E93+ tNBs have 50% chance to duplicate (S→SS), and 50% chance to divide into two Chinmo+Imp+ tNBs (S→CC). Unlike our experimental observations, this non-hierarchical scenario leads to a symmetric outcome, in which all clones rapidly become mixed, while the proportion of CI and SYP clones rapidly decays to zero (Figure 4B). In the second scenario (‘Strict hierarchy #1’), Chinmo+Imp+ tNBs still have 50% chance to duplicate (C→CC), and 50% chance to divide into two Syp+E93+ tNBs (C→SS) but Syp+E93+ tNBs can only self-renew (S→SS). This hierarchical scheme leads to a fully different outcome, with a large proportion of clones remaining only composed of Syp+E93+ tNBs (SYP clones), while the proportion of clones only composed of Chinmo+Imp+ tNBs (CI clones) rapidly decays, which is consistent with our experimental observations (Figure 4B). In the third scenario, we also tested the reverse hierarchical scheme (‘Strict hierarchy #2’) where Syp+E93+ tNBs still have 50% chance to duplicate (S→SS), and 50% chance to divide into two Chinmo+Imp+ tNBs (S→CC) but Chinmo+Imp+ tNBs can only self-renew (C→CC). Consistently, we observed results opposite to the second scenario, with CI clones rapidly becoming dominant instead of SYP clones (Figure 4B). These scenarios therefore suggest that poxn > prosRNAi NB tumors follow a rather hierarchical scheme with Chinmo+Imp+ tNBs at the top of the hierarchy. Finally, we tested a fourth ‘Plastic hierarchy’ scenario for which we maintain this hierarchy, but also give Syp+E93+ tNBs a small probability (1%) to generate Chinmo+Imp+ tNBs (S→CC). This is sufficient to drastically change the outcome of the simulations, as it prevents the long-term maintenance of SYP clones (Figure 4B, right panel). These four model scenarios combined to our experimental observations therefore argue for a rigid, unidirectional, Chinmo+Imp+→Syp+E93+ hierarchy between tNBs.

### The hierarchical division scheme that defines clonal growth and composition demonstrates a cancer stem cell-like role for Chinmo+Imp+ tNBs

We then sought to use the hierarchical model #1 as a basis to investigate more quantitatively the parameters that finetune tumor growth and heterogeneity. Interestingly, in vivo, significant differences in average clone size can be observed between the three categories at the different time points (Figure 4C). SYP clones grow slower than MIXED clones, suggesting either that Syp+E93+ tNBs have a slower cell-cycle speed or possess a limited self-renewing potential - similar to Syp+E93+ NBs during development – and rapidly end up exiting the cell cycle. On the other hand, the few clones that remain within the CI category at 8 days ACI tend to completely stop growing, suggesting that these clones may be composed by quiescent Chinmo+Imp+ tNBs. Consequently, we considered non-zero probabilities $q_{s}$ and $q_{c}$ for new S cells and C cells to enter quiescence. We also implemented a non-zero probability for C cells to undergo fate asymmetric divisions (Figure 4—figure supplement 1), and distinct division times for C and S cells. Thanks to a series of measurements, we could reduce the number of independent parameters to two (see Materials and methods): the probability $P(c→cc)$, and the division time $T_{s}$ for S cells. We used these as free parameters to fit the model to the measurements of clone sizes and compositions at 8 hours, 2, 4 and 8 days ACI. To that end, we computed error maps for clone composition and clone size in the $(Pc→cc,T_{s})$ plane, and eventually a combined error map (Figure 4—figure supplement 2). We found that the error is minimized for $Pc→cc=0.64$ and $T_{s}=1.3$ days, from which we determine all the other parameters. Notably, Syp+ tNBs have a much higher probability (47%) to enter quiescence than Chinmo+Imp+ tNBs (4%), consistent with the slower growth of SYP clones. Using the set of parameters determined by the fit (Figure 4F), we found an excellent agreement between experiments and simulations, for both clone sizes (Figure 4C, D) and clone compositions (Figure 4E). Modulating these parameters to allow a small probability for S→CC reverse divisions (1% or 5%) significantly affected the simulations outcome, leading to an important loss of SYP clones and a concomitant increase of MIXED clones (Figure 4G). This further demonstrates that reverse divisions from Syp+E93+ tNBs to Chinmo+Imp+ tNBs are either very low or inexistent, at least during the first weeks of tumor growth.

Altogether, our clonal analysis demonstrates that NB tumors are strongly hierarchical. Chinmo+Imp+ tNBs are at the top at the hierarchy. They have a preference for symmetric self-renewing divisions, allowing their perpetuation, and rarely become quiescent allowing tumor growth propagation. They can also undergo fate asymmetric or symmetric differentiation divisions in order to generate Syp+E93+ tNBs, albeit with a lower probability. Subsequent Syp+E93+ tNBs can undergo symmetric self-renewing divisions but exhibit a high propensity for rapid cell-cycle exit and cannot generate Chinmo+Imp+ tNBs. Consequently, Syp+E93+ tNBs cannot generate large and heterogeneous clones in tumors unlike Chinmo+Imp+ tNBs. This set of characteristics (Figure 4F) thus confers cancer stem cell (CSC)-like properties to Chinmo+Imp+ tNBs (Nassar and Blanpain, 2016; Nguyen et al., 2012; Valent et al., 2012).

### Tumor composition is predictable but varies according to the cell of origin

We then tested whether the set of parameters defined by our analysis of clonal growth could recapitulate the tNB population dynamics, from homogeneity (in early larvae) to stable heterogeneity (in adults). When applying the uncovered set of parameters to a homogenous pool of Chimo+Imp+ tNBs as observed in early larvae (Figure 2A), simulations via the stochastic or a deterministic version of the model (see Materials and methods) predict that Chimo+Imp+ and Syp+E93+ tNB populations rapidly reach an equilibrium with a 20/80 ratio (Figure 5A). Remarkably, this is consistent with our observations that the population of Chinmo+Imp+ tNBs invariably progresses to the minority, and reaches a similar equilibrium in vivo (Figure 2E). Our observation that all poxn > prosRNAi tumors invariably reach an approximate 20/80 equilibrium during adulthood suggests a robust hierarchical scheme able to buffer intrinsic or extrinsic perturbations inherent to biological systems. Interestingly, changing the initial proportions of tNBs in the simulation does not affect the final equilibrium (Figure 5B). Thus, the uncovered hierarchical scheme robustly reproduces the observed dynamics of intratumoral heterogeneity, at least during the first two and half weeks of tumor growth (from L1 to 10-day-old adults) and provides robustness to accommodate biological perturbations.

![Figure 5.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig5-v2.jpg)

**Figure 5.:** (A) Proportion of Syp+E93+ (blue) and Chinmo+Imp+ (red) tNBs over time using the set of parameter values determined by the error minimization and starting from 100% of Chinmo+Imp+ tNBs. Dashed lines represent a stochastic simulation (clone model), thin lines represent the prediction of the deterministic model. An equilibrium is rapidly reached were Chinmo+Imp+ tNBs represent about 20% of all tNBs. (B) Dashed curves: evolution of the proportions of Syp+E93+ (blue) and Chinmo+Imp+ (red) tNBs, as predicted by the deterministic model, when starting with 100% of Chinmo+Imp+. Plain curves: evolution of the proportions of Syp+E93+ (blue) and Chinmo+Imp+ (red) tNBs, as predicted by the deterministic model, when starting with 50% of Chinmo+Imp+ and 50% of Syp+E93+ tNBs. In both scenarios, the same equilibrium is reached. (C) UAS-snr1RNAi transgenes are expressed in type II NBs using the ase-Gal80, wor-Gal4, UAS-dicer2 system causing NB tumors that persist in the CB of adult flies. tNBs in 6-day-old adults are marked with Mira, Imp, Chinmo and Syp. (D) Proportion of Chinmo+Imp+ tNBs in ase-G80, wor > snrRNAiRNAi-1 (n = 5 CB) and ase-G80, wor > snrRNAiRNAi-2 (n = 7 CB) tumors in 6-day-old adults (volume of Chinmo+Imp+ tNBs over volume of all tNBs x 100) . p=0.0061. Scale bars, 20 µm.

To investigate whether the 20/80 ratio is a property of all NB tumors, we measured this ratio in tumors induced by the loss of the SWI/SNF factor snr1 in larval type II NBs of the central brain (Eroglu et al., 2014; Koe et al., 2014). As for poxn > prosRNAi tumors, late larval and adult NB tumors induced by a null Snr1 allele or Snr1RNAi are composed by a mix of Chinmo+Imp+ tNBs and Syp+ tNBs (Figure 5C). As for poxn > prosRNAi tumors the ratio of Chinmo+Imp+ over Syp+ tNBs is reproducible from adult to adult tumors (Figure 5D). However, we observed that it is different from poxn > prosRNAi tumors with an approximate 50/50 ± 10 ratio encountered in Snr1RNAi tumors. Thus, the rules finetuning the parameters defining the hierarchical scheme in the different types of tumors are robust, but tumor-specific, possibly determined by the NB of origin.

### Imp and Syp antagonistically regulate NB growth and self-renewal during development and tumorigenesis via chinmo

We then investigated the role of the two RNA-binding proteins Imp and Syp in tumor growth and cellular heterogeneity. We had previously demonstrated that Imp sustains NB tumor growth beyond normal developmental stages at least partially by promoting chinmo expression (Narbonne-Reveau et al., 2016). To investigate the function of Syp within the tumor context, we knocked it down in poxn > prosRNAi tumors from their initiation. Syp knockdown led to tumors almost exclusively constituted of Chinmo+Imp+ tNBs (Figure 6A,B). This is consistent with the finding that Syp knockdown induces maintenance of both Imp (Yang et al., 2017) and Chinmo in NBs during development (Figure 6—figure supplement 1). This suggests that in absence of Syp, Chinmo+Imp+ tNBs tend to exclusively undergo symmetric self-renewing divisions. As predicted by the numerical model, this should lead to an increased tumor growth rate, since Chinmo+Imp+ tNBs do not, or rarely enter quiescence, unlike Syp+E93+ tNBs (Figure 6C). Consistently, in vivo, the volume of prosRNAi; SypRNAi tumors in 1-day-old adults exhibited a 3.9-fold increase compared to control prosRNAi tumors (Figure 6D and Figure 6—figure supplement 2A). By contrast, over-expressing Syp (SypOE) within prosRNAi tumors blocked tumor growth in adults (Figure 6E and Figure 6—figure supplement 2A). In addition, knockdown of both Syp and Imp in prosRNAi, SypRNAi, ImpRNAi tumors arrested tumor growth in adults (Figure 6F and Figure 6—figure supplement 2), and tumors lacked or exhibited low levels of Chinmo (Figure 6—figure supplement 2) demonstrating that, even in the absence of Syp, Imp is essential for Chinmo expression in tumors and that is required for their continuous growth. Thus, the overgrowth phenotype observed in prosRNAi, SypRNAi tumors is mediated by the Chinmo/Imp module. Together, these experiments indicate that cellular heterogeneity is not required for tumor growth, and that Syp acts as a tumor suppressor. Syp restrains the population of Chinmo+Imp+ CSC-like tNBs and its inactivation in tumors abolishes the hierarchy.

![Figure 6.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig6-v2.jpg)

**Figure 6.:** (A) Syp knockdown in poxn > prosRNAi tumors triggers a dramatic increase of Chinmo+Imp+ tNBs. tNBs are marked with an anti-Mira antibody. (B) Proportion of Chinmo+Imp+ tNBs in poxn > prosRNAi (n = 6 VNC) and poxn > prosRNAi, SypRNAi (n = 6 VNC) tumors in 4-day-old adults. p=0.0022. (C) Simulation of tumor growth (number of cells) in prosKD and prosKD, SypKD (red) tumors. Quiescence probabilities are those set by the error minimization. (D) Volume of poxn > prosRNAi (n = 6 VNC) and poxn > prosRNAi, SypRNAi (n = 6 VNC) tumors in 1-day-old adults. p=0.002. Volume of poxn > prosRNAi (n = 7 VNC) and poxn > prosRNAi, SypRNAi (n = 4 VNC) tumors in 4-day-old adults. p=0.0061. (E) Volume of poxn > prosRNAi tumors in 3-day-old (n = 10 VNC) and 8-day-old (n = 6 VNC) adults. p=0.00025. Volume of poxn > prosRNAi (n = 10 VNC) and poxn > prosRNAi, UAS-Syp (n = 8 VNC) tumors in 3-day-old adults. p=0.0005. Volume of poxn > prosRNAi (n = 6 VNC) and poxn > prosRNAi, UAS-Syp (n = 8 VNC) tumors in 8-day-old adults. p=0.00067. Volume of poxn > prosRNAi, SypOE tumors in 3-day-old (n = 8 VNC) and 8-day-old (n = 8 VNC) adults. p=0.7209. (F) Volume of poxn > prosRNAi, SypRNAi (n = 6 VNC) and poxn > prosRNAi, ImpRNAi, SypRNAi (n = 9 VNC) tumors in 4-day-old adults. p=0.0004.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) RNA affinity pull-down assay using biotinylated RNAs incubated with wild-type adult brain extracts. Proteins recovered in the bound fractions were visualized by western blot analysis. The 3’ UTR of chickadee (chic) and the coding sequence of y14 were used as positive and negative controls respectively. (B) Cartoons represent a ventral view of the adult Drosophila CNS. The nab-GAL4 driver is active in all NBs located in the VNC. In nab-Gal4, UAS-dicer2, UAS-GFP (nab >GFP) GFP labels NBs and their recent progeny. NBs, marked with GFP and Miranda (Mira) are not present in the VNC of wt pharate adults. (C) Syp knock-down (nab >SypRNAi) from early larval stages induces the persistence of active Chinmo+Imp+ NBs in the VNC of pharate adults. (D) Most of the VNC NBs lacking both Syp and Imp (nab >SypRNAi, ImpRNAi) are eliminated before the pharate adult stage. The few persisting NBs exhibit a smaller size and cytoplasmic extensions. They don’t express Chinmo and Imp. (E) Most of the VNC NBs lacking both Syp and Chinmo (nab >SypRNAi, ChinmoRNAi) are eliminated before the pharate adult stage. The few persisting NBs exhibit a smaller size and cytoplasmic extensions. They don’t express Chinmo and Imp. (F) Quantification of the number of NBs per VNC in nab >SypRNAi (n = 6 VNC), nab >SypRNAi, ImpRNAi (n = 6 VNC) and nab >SypRNAi, chinmoRNAi (n = 6 VNC). PSypKD/SypKD,ImpKD = 0.002. PSypKD/SypKD,chinmoKD = 0.002. PSypKD,ImpKD/SypKD,chinmoKD = 0.039. (G) Quantification of proliferating NBs, marked with PH3, in nab >SypRNAi (n = 6 VNC), nab >SypRNAi, ImpRNAi (n = 6 VNC) and nab >SypRNAi, chinmoRNAi (n = 6 VNC). PSypKD/SypKD,ImpKD = 0.002. PSypKD/SypKD,chinmoKD = 0.004. (H) Quantification of the NB area in nab > SypRNAi (n = 14 NBs), nab > SypRNAi, ImpRNAi (n = 10 NBs) and nab > SypRNAi, chinmoRNAi (n = 10 NBs). PSypKD/SypKD,ImpKD=<0.0001. PSypKD/SypKD,chinmoKD=<0.0001. (I) Scheme depicting the asymmetric divisions of NBs throughout larval and pupal stages and recapitulating the above experiments. Scale bars, 20 µm.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** (A) poxn > prosRNAi, SypRNAi  tumors overgrow compared to control poxn > prosRNAi tumors (Cntrl) in 1-day-old adults (1d).Tumors fail to grow in poxn > prosRNAi, SypRNAi, ImpRNAitumors (4d). Overexpression of Syp in poxn > prosRNAi, SypOE tumors arrests tumor growth compared to control poxn > prosRNAi tumors (Cntrl) in 8-day-old adults (8d). Tumors are delimited by dashed lines. The UAS-mCherrychinmoUTRs is expressed in tumors where it is post-transcriptionally regulated, reflecting chinmo expression (Figure 1—figure supplement 4). (B) poxn > prosRNAi, SypRNAi tumors are mostly composed of Chinmo+ tNBs. Chinmo is absent in poxn > prosRNAi, SypRNAi, ImpRNAi tumors indicating that Imp is necessary to promote chinmo expression in poxn > prosRNAi, SypRNAi tumors. tNBs are marked with Mira. Scale bars, 20 µm.

We then tested whether Imp and Syp exert their antagonistic activities by competing on the same RNAs. As revealed by affinity pull-down assays performed using in vitro synthesized chinmo 5’ and 3’UTRs, both Imp and Syp can associate with the UTRs of chinmo mRNA (Figure 6—figure supplement 1A). Therefore, Imp and Syp can have the same target genes. Interestingly, Syp appears to have a greater affinity for the 5’UTR (Figure 6—figure supplement 1A). This phenomenon provides a molecular explanation for the observation that chinmo 5’UTR is required for post-transcriptional silencing (Zhu et al., 2006). Together, our data indicate that NB tumor growth, hierarchy and cellular heterogeneity is governed by the finetuned activities of the two RNA-binding proteins Imp and Syp, largely via the post-transcriptional regulation of chinmo.

### tNBs follow a trajectory partially recapitulating larval temporal patterning

We then thought to use our single-cell RNA-seq data to investigate in more details the genes expressed along the Imp/Syp-mediated tumor hierarchy. For this purpose, we used Monocle 2 to perform a pseudotime analysis (Qiu et al., 2017a; Qiu et al., 2017b; Trapnell et al., 2014). Pseudotime analysis determines trajectories of differentiation by ordering cells according to their transcriptional changes. Our numerical model demonstrated that Chinmo+Imp+ tNBs are at the top of the tumor hierarchy. Therefore, tNBs with high levels of Imp can be positioned at the root of the pseudotime trajectory. In contrast, Syp+E93+ tNBs lie further down in the hierarchy and E93 marks late NBs during development (Ren et al., 2017; Syed et al., 2017). In consequence, tNBs expressing high levels of E93 can be assigned to the end of a differentiation trajectory. Based on these assumptions, we ran a semi-supervised ordering to uncover genes that are dynamically expressed along the Imp→E93 differentiation trajectory that occurs within poxn > prosRNAi tumors. The pseudotime ordering generated a trajectory that is initially enriched in Imp+ tNBs and that splits into two main branches enriched in E93+ tNBs (Figure 7A,B). We then searched for the top 200 genes whose expression changes as a function of pseudotime. They could be separated in three main clusters (Figure 7C and Supplementary file 1): Cluster 1 contains genes that, similar to Imp, decrease their expression along the pseudotime (111 genes). They include Oatp74D, Sip1/CG10939, plum/CG6490, Chd64, SP1173, CG10512, Gapdh2 and CG44325 (Figure 7B) that are expressed in early larval NBs before the Imp-to-Syp switch (Figure 1F). Of note cas and svp, the upstream temporal transcription factors scheduling the Imp-to-Syp transition in larval NBs are absent from cluster 1 consistent with our observation that they are not enriched in Imp+ tNBs (Figure 1—figure supplement 3). Cluster 2 and 3 contains genes that, similar to E93, increase their expression along the pseudotime (71 and 18 genes respectively). However, they discriminate genes that are differentially expressed along the two branches of the differentiation trajectories (Figure 7A). Cluster 2 is enriched in ribosomal proteins, and also includes the late larval NB temporal markers: stg, lncRNA:noe, and CG15628 (Figure 7C,D and Supplementary file 1). In the tumor, stg is enriched in the branch defined by state three along the trajectory (Figure 7A). In contrast, cluster 3 pinpoints genes that are highly expressed in the branch defined by state 7 (Figure 7A) including the late temporal patterning gene CG15646. Interestingly, cluster 3 is also strongly enriched in genes of the E(spl) family, known targets of the Notch pathway (Figure 7B and Supplementary file 1). Thus, the expression of stg and E(spl) genes can discriminate two distinct states within the Syp+E93+ population of tNBs (Figure 7A,B).

![Figure 7.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig7-v2.jpg)

**Figure 7.:** (A) Cell trajectory reconstructed from the population of tNBs using semi-supervised pseudotime ordering. Imp+ tNBs are enriched at the root of the trajectory while E93+ tNBs are enriched in the branches terminating the trajectories. tNBs are colored according to their State along the trajectory. (B) Dark spline indicates levels of gene expression along the pseudotime. Cells are colored according to their State along the trajectory in (A). p-values for differential expression along the pseudotime are indicated for each gene. (C) Kinetic heatmap depicting the expression of top 200 genes that vary as a function of pseudotime. Genes are grouped in three clusters based on expression kinetics. (D) Gene ontology (GO) enrichment analysis for each cluster identified in (C). (E) Heatmap depicting enrichment of various temporal patterning, metabolic and acetylcholine receptor genes when comparing poxn > prosRNAi tumors and poxn > prosRNAi, SypRNAi tumors. (F) Gene ontology (GO) enrichment analysis when comparing the transcriptome of poxn > prosRNAi, SypRNAi vs poxn > prosRNAi tumors.

To investigate whether the Imp-to-Syp transition controls the progression of transcriptional states observed along the pseudotime, we performed RNA-seq on bulk poxn > prosRNAi and poxn > prosRNAi, SypRNAi adult tumors dissected with the VNCs on which tumors grow. Between the two conditions, the expression of generic larval NB identity genes (grh, dpn) did not significantly change (Figure 7E). In contrast, larval NB temporal markers varied greatly, as observed with early (e.g. Imp, Oatp74D, Sip1/CG10939, plum/CG6490 and Chd64) and late (E93, Syp, CG15646) markers being respectively strongly enriched and down-regulated in the poxn > prosRNAi, SypRNAi tumors (Figure 7E and Supplementary file 2). Note that lin-28 and E23 were not detected in Imp+ tNBs with the single-cell RNA-seq approach but are detected with the bulk-seq approach, and their expression dynamics matches those of other early temporal genes such as Imp (Figure 7E). This transcriptomic analysis thus identifies differentiation trajectories in tumors characterized by the dynamic expression of a subset of larval temporal patterning genes that is driven by the Imp-to-Syp switch.

### The temporal trajectory governs the metabolic and proliferative properties of tNBs

In addition to temporal patterning genes, single-cell and bulk RNA-seq analyses identify other genes that are downregulated along the Imp/Syp-mediated trajectory followed by tNBs. These include for example the nicotinic acetylcholine receptors alpha3 and alpha5 (nAChRalpha3, nAChRalpha5) whose expression has not been reported to be temporally regulated in larval NBs (Figure 7E and Figure 8—figure supplement 1). They may therefore represent genes that are specifically activated in the tumor context and enriched in the Imp+Chinmo+ CSC-like tNBs. Glycolysis, TCA cycle and respiratory electron transport chain (OXPHOS) genes are also highly expressed in Chinmo+Imp+ tNBs and down-regulated along the Imp/Syp-dependent hierarchy (Figures 7D,E,F and 8A,B), a phenomenon that has not been reported in NBs during development (except for Gapdh2 expression that is high in early MB NBs) (Figure 1—figure supplement 2D and Figure 1—figure supplement 3). Highly expressed genes in the Imp+Chinmo+ tNBs also include the Glutamate dehydrogenase (Gdh) (Figure 8A,B). This suggests that Chinmo+Imp+ tNBs highly rely on glutamine and glucose metabolism.

![Figure 8.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig8-v2.jpg)

**Figure 8.:** (A) Glucose metabolism pathways (glycolysis, TCA cycle and respiratory electron transport chain). Genes whose expression is enriched in poxn > prosRNAi, SypRNAi tumors compared to poxn > prosRNAi tumors are highlighted in blue. Log2 fold change is indicated in brackets. (B) Expression dynamics of various glycolytic, respiratory electron transport chain and glutamine metabolism genes along the tumor pseudotime. p-values for differential expression along the pseudotime are indicated for each gene. (C) poxn > prosRNAi NB tumors are marked with anti-Mira (green). Silencing of glycolytic (Gapdh-1RNAi, Pglym78RNAi) or respiratory genes (Cyt-c-pRNAi, Cyt-c1RNAi) leads to smaller poxn > prosRNAi tumors in late L3 larvae. Silencing of glycolytic or respiratory genes arrests tumor growth in 4-day-old and 7-day-old adults respectively. (D) Volumes of poxn > prosRNAi tumors (n = 5 VNC), poxn > prosRNAi, Gapdh-1RNAi tumors (n = 7 VNC); poxn > prosRNAi, Pglym78RNAi tumors (n = 5 VNC); poxn > prosRNAi,Cyt-c-pRNAi tumors (n = 5 VNC); and poxn > prosRNAi,Cyt-c1RNAi tumors (n = 5 VNC) in late L3. PCntrl/Gapdh-1RNAi = 0,002. PCntrl/Pglym78RNAi = 0,007. PCntrl/Cyt-c-pRNAi= 0,007. PCntrl/Cyt-c1RNAi = 0,007. Volumes of poxn > prosRNAi tumors (n = 6 VNC); poxn > prosRNAi, Gapdh-1RNAi tumors (n = 8 VNC); poxn > prosRNAi, Pglym78RNAi tumors (n = 9 VNC); poxn > prosRNAi, Cyt-c-pRNAi tumors (n = 10 VNC); and poxn > prosRNAi, Cyt-c1RNAi tumors (n = 6 VNC) in 4-day-old adults. PCntrl/Gapdh-1RNAi = 0,0007. PCntrl/Pglym78RNAi = 0,0002. PCntrl/Cyt-c-pRNAi = 0,0002. PCntrl/Cyt-c1RNAi = 0,002. Scale bars, 50 µm. (E) Each dot represents the average area of Chinmo+Imp+ tNBs over the average area of Syp+E93+ tNBs for a single confocal section of a poxn > prosRNAi NB tumor in a 4-day-old adult. (F) Schematic representation of the tumor hierarchy. Chinmo+Imp+ tNBs are proliferative and tend to self-renew. However, they can also engage in a differentiation process triggered by the Imp-to-Syp transition and involving a subset of larval temporal genes. Syp+E93+ tNBs can self-renew but also tend to exit the cell-cycle as they decrease expression of glucose/glutamine metabolism genes. Syp+E93+ tNBs, that have exited the cell-cycle, express genes of the E(spl) family. The mechanisms controlling the Imp-to-Syp transition in NB tumors, to determine the CSC proportion are unknown.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig8-figsupp1-v2.jpg)

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig8-figsupp2-v2.jpg)

**Figure 8—figure supplement 2.:** (A) Cell trajectory reconstructed from the population of tNBs using semi-supervised pseudotime ordering. Cells are colored by States. The three main branches of the tree are labeled as: Pre-branch, E93+stg+ branch and E93+E(spl)+ branch. (B) stg and E(spl)m7-HLH are enriched in distinct branches of the trajectory. (C) Kinetic heatmap depicting the expression of genes that are differentially expressed between the Pre-branch, the E93+stg+ branch and the E93+E(spl)+ branch (qval < 1e-20).

![Figure 8—figure supplement 3.](https://cdn.elifesciences.org/articles/50375/elife-50375-fig8-figsupp3-v2.jpg)

**Figure 8—figure supplement 3.:** Anti-Mira staining was used as membrane reference. Accurate segmentation was manually double-checked using Dapi as nuclear marker. Imp-GFP+ cells represent Chinmo+Imp+ tNBs. GFP- tNBs represent Syp+E93+ tNBs.

A more careful investigation of differential expression along the two main branches of the pseudotime (Figure 8—figure supplement 2 and Supplementary file 3) indicates that the E93+stg+ branch is characterized by medium to low levels of glucose metabolism genes, when compared to early pre-branched cells (cluster 4), and a burst of cell cycle genes (cluster 4) followed by increased expression of ribosomal genes (cluster 3) (Figure 8—figure supplement 2). These data suggest that tNBs in the E93+stg+ branch exhibit transient cell cycle activity before progressing towards the end of their differentiation trajectory. In contrast, the E93+E(spl)+ branch exhibit low levels of glycolytic and cell cycle genes (cluster 4) all along (Figure 8—figure supplement 2 and Figure 8A). Thus, E(spl) genes appear to discriminate non-proliferative tNBs that are also possibly quiescent given their low levels of metabolic gene expression. Altogether, this transcriptomic and genetic analyses suggest that the Imp-to-Syp transition in tNBs induces a cell-autonomous down-regulation of glutamine and glucose metabolism genes and the production of two different types of E93+ tNBs with distinct metabolic and proliferative properties, consistent with the predictions of the numerical model.

To test the importance of glucose metabolism genes during tumor growth, we knocked down Gapdh1 and Pglym78 (glycolysis), as well as Cyt-c-p and Cyt-c1 (OXPHOS), in poxn > prosRNAi tumors, all being significantly enriched in poxn > prosRNAi, SypRNAi tumors and downregulated along the pseudotime (p-values=8,01e−63; 3,04e−146; 2,65e−46; 1,45e−26 respectively) (Figure 8A,B). In all knockdown conditions, tumors underwent a slower growth rate already detectable in late L3 (Figure 8C,D). Moreover, tumors systematically failed to be maintained in adults showing that the expression of both glycolytic and OXPHOS genes are necessary for long-term propagation of NB tumor growth (Figure 8C,D). In addition, when comparing the size of tNBs within poxn > prosRNAi tumors, we found that Syp+E93+ tNBs exhibited a smaller size than Chinmo+Imp+ tNBs in agreement with reduced glycolysis decreasing cell growth (Figure 8E and Figure 8—figure supplement 3). Together, this suggests that the Imp-to-Syp transition induces a metabolic switch that prevents long-term self-renewal and reduces cell growth as tNBs move down the hierarchy (Figure 8F). Thus, recapitulation of temporal patterning provides a tumor-intrinsic mechanism that generates metabolic heterogeneity leading totNBs with different growth properties..

## Discussion

Our study demonstrates that temporal patterning, not only determines which cells are susceptible to cancer transformation during development (Narbonne-Reveau et al., 2016), but also has an overarching role in governing different aspects of CNS tumor organization such as hierarchy, heterogeneity and the proliferative properties of the different types of cells via the regulation of their metabolism.

Given the recent discovery that temporal patterning is conserved in the developing mammalian brain (Telley et al., 2019), our study could shed light on an ancestral mechanism that governs the progression of CNS tumors with developmental origins.

### Subversion of a subset of larval NB temporal patterning genes triggers predictable hierarchical neural tumors

The rules governing the initiation and progression of CNS pediatric tumors that often exhibit stable genomes are still unclear. We had previously demonstrated that temporal patterning in Drosophila larval NBs delineates a window of time during which the Chinmo/Imp oncogenic module is expressed and makes early larval NBs prone to malignant transformation (Narbonne-Reveau et al., 2016). Here we find that after tumor initiation, temporal patterning is partly recapitulated in tNBs where it generates differentiation trajectories to constrain tumor composition and growth. This is illustrated by the presence of about 20 genes (Imp, chinmo, Lin-28, E23, Oatp74D, Gapdh2, Sip1/CG10939, plum/CG6490, SP1173, Chd64, CG10512, CG44325, CG5953, Syp, E93, lncRNA:noe, CG15646 and stg), previously identified to be temporally regulated in some larval NBs, that are differentially regulated along the pseudotime/differentiation trajectory reconstructed from single-cell RNA-seq analysis of tNBs, and/or differentially expressed in Imp+ vs Syp+ tNBs. Thus, we identify here what appears to be a subset of a core temporal patterning program encoded in central brain and ventral nerve cord NBs that becomes deregulated upon asymmetric-division defects during early development.

Notably, the larval temporal transcription factor Cas and Svp, known to schedule the Imp-to-Syp transition during development are not enriched in Imp+ tNBs suggesting that they do not play a role in regulating the Imp-to-Syp transition along the trajectory in tumors. Interestingly, while Syp is transcriptionally regulated in larval NBs, it seems rather post-transcriptionally regulated in tNBs as Syp RNAs are present throughout all clusters. This suggests that different mechanisms may be operating in tumors than during development to regulate the Imp-to-Syp transition.

We observed that the proportions of Imp+ and Syp+ tNBs systematically reach an equilibrium over a few days with a 20/80 (+ /- 10) ratio in poxn > prosRNAi tumors. This suggests that the regulation of the Imp-to-Syp transition in tumors is not random and the predictability of the final proportions possibly implies robust underlying constraints. By investigating the population dynamics of Imp+ and Syp+ tNBs in prosRNAi tumors, we have deciphered a finely tuned hierarchical division scheme that appears to constrain the growth and cellular heterogeneity of the tumor. We showed that Imp+ tNBs in the tumorigenic context favor a symmetric self-renewing mode of divisions (in more than 60% of divisions) while unlikely to exit the cell-cycle. This allows the perpetuation of a small subset of Imp+ tNBs that are endowed with a seemingly unlimited self-renewing potential by the Imp/Chinmo module. Imp+ tNBs can also make symmetric and asymmetric divisions that generate Syp+ tNBs, leading to the production of a population of Syp+E93+ tNBs that accumulates through limited self-renewal, and have a high propensity for exiting the cell-cycle. Moreover, we could show that Syp+E93+ tNBs are unable to generate Imp+ tNBs, demonstrating a rigid cellular hierarchy reminiscent of development. In addition, in this context, Syp acts as a tumor suppressor by limiting tNB proliferation while Imp acts as an oncogene by promoting tNB proliferation and propagation of tumor growth. Together, these data argue for a scenario where cooption of the Imp-to-Syp transition is responsible for installing a hierarchical mode of tumor growth with Imp+ tNBs propagating unlimited growth in a CSC-like manner, while Syp+E93+ tNBs acts as transient amplifying progenitors with limited self-renewing abilities. Although the Imp/Syp RNA-binding proteins have an essential and antagonistic role in governing the proliferative properties of tumor cells, the function of the other redeployed temporal patterning genes is unknown (except for chinmo, downstream to Imp and Syp, that is essential for tumor growth). As many are linked with the Imp+ tNB state, it will be important in the future to decipher how they contribute to establish or maintain the CSC-like identity.

The division parameters defined by our clonal analysis and modeling approach could capture both the hierarchical aspect of tumor growth as well as the global population dynamics: from an initial homogenous pool of larval Imp+ tNBs to the stable heterogeneity observed during adulthood. It could also resolve the paradoxical observation that Chinmo+Imp+ tNBs end up in minority despite exhibiting a higher average mitotic rate. Although, like all models, we don’t expect our model to perfectly recapitulate all the parameters regulating tumor growth and heterogeneity (for example, we have neglected apoptosis and neuronal differentiation that occur at low levels), we think it provides a reasonable and useful ground on which further studies can be performed for a more detailed understanding. On these lines, while the division pattern we have described with our numerical model provides estimates of division probabilities in poxn > prosRNAi tumors, it says nothing as to how these probabilities are biologically set within the tumor. A possible scenario is that cell fate determination upon division relies on signals received by immediate neighboring tumor cells, resulting in effective probabilities at the scale of the whole tumor. Such a micro-environment dependent regulation of the Imp-to-Syp transition in tumors would strongly contrast with the cell-intrinsic regulation of the Imp-to-Syp transition that systematically occurs in NBs around early L3. Future studies will aim at deciphering the mechanisms that interfere with the developmental progression of the temporal patterning, upon asymmetric-division defects, to favor the self-renewing mode of divisions undergone by the Chinmo+Imp+ tNBs, allowing perpetuation of a population of CSC-like cells.

Noteworthy, prosRNAi and snr1/dSmarcb1RNAi tumors exhibit different but reproducible ratios of Imp+ and Syp+ tNBs. This suggests the existence of tumor-specific mechanisms that fine-tune the Imp-to-Syp transition. Such mechanisms may be related to the tumor cell of origin, or to the genetic insult that initiated NB amplification. Further analysis will help identifying tumor-intrinsic signals regulating the balance between Chinmo+Imp+ tNBs and Syp+E93+ tNBs in various types of NB tumors.

Until recently, the existence of temporal patterning in mammalian neural progenitors remained uncertain. Elegant single-cell transcriptomic studies of embryonic cortical and retinal progenitors in mice have now revealed that they transit through different transcriptional states that are transmitted to their progeny to generate neuronal diversity, similar to temporal patterning in Drosophila (Clark et al., 2019; Telley et al., 2019). However, it remains unknown whether temporal patterning determines the cell of origin and governs the growth of CNS tumors in children. Along these lines, the finding that the transcriptional programs operating in cerebellar progenitors during fetal development are recapitulated in medulloblastomas is promising (Vladoiu et al., 2019). By uncovering the overarching role of temporal patterning in governing tumor susceptibility during CNS development and in constraining tumor properties during cancer progression in Drosophila, our work thus possibly provides a new conceptual framework to better understand CNS tumors in children.

### Tumor-intrinsic regulation of NB metabolism by the temporal patterning system

Because of the difficulty to investigate metabolism at the single-cell level, it has been difficult to determine how heterogeneous is the metabolic activity of cells in tumors, and how it is controlled. Here, using a combination of single-cell and bulk RNA-seq approaches, we find that progression of temporal patterning provides a tumor-intrinsic mechanism that generates heterogeneity in the proliferative abilities of tumor cells through the progressive silencing of glucose and glutamine metabolism genes.

Consequently, Chinmo+Imp+ tNBs, that lie at the top of the hierarchy, highly express glycolytic and respiratory/OXPHOS genes, as well as Gdh, that are down-regulated by the Imp-to-Syp transition. This default high expression of both glutamine and glucose metabolism genes in CSC-like Chinmo+Imp+ tNBs likely favors sustained self-renewal, but could also confer plasticity and a way to adapt cellular metabolism to different environmental conditions as frequently observed in CSCs (e.g. glutamine can compensate for glucose shortage) (Sancho et al., 2016).

We showed that Syp+E93+ tNBs exhibit a reduced size, and that knock-down of glycolytic (Gapdh1 or Pglym78) or respiratory/OXPHOS genes (Cyt-c-p or Cyt-C1) prevented propagation of tumor growth in adults. Thus, reduction of biosynthesis and energy production through down-regulation of glucose and glutamine metabolism genes after the Imp-to-Syp transition could progressively exhaust Syp+E93+ tNB growth and self-renewing ability, ultimately leading to cell-cycle exit.

With our demonstration that temporal patterning regulates glycolytic, TCA cycle and OXPHOS genes in NB tumors, our work provides a tumor-intrinsic mechanism that creates metabolic heterogeneity to control the proliferative potential of the various tumor cells. We have observed that Syp+E93+ tNBs associated with lowest levels of metabolic and cell-cycle genes also upregulate genes of the E(spl) genes. Interestingly, expression of Hes genes (orthologs of Enhancer of split genes) in vertebrate neural stem cells is associated with the maintenance of a quiescent state in adults (Chapouton et al., 2011; Sueda et al., 2019). Thus, E(spl) genes may promote the quiescent tNB state identified with our clonal and numerical analysis while preventing their differentiation in neurons.

Down-regulation of the mRNA levels of metabolic genes after the Imp-to-Syp transition could be due to the silencing of a transcriptional activator or to an increased mRNA degradation. On one hand, Chinmo is a likely candidate for the first scenario, as its inactivation reduces growth in NBs (Narbonne-Reveau et al., 2016) and we showed that it is a direct target of both Imp and Syp. On the other hand, the second scenario is consistent with Imp orthologs in human being able to promote OXPHOS and proliferation in glioma cells, through the post-transcriptional regulation of mitochondrial respiratory chain complex subunits (Janiszewska et al., 2012).

We have also identified a small population of tNBs expressing various stress or growth arrest factors. One of these factors, Xrp1, is a transcriptional target of p53 in the response to irradiation. Xrp1 expression has also recently been linked to defects in translation rates, together with the expression of Irbp18 and GstE6 (Lee et al., 2018). Thus, these factors may label a subset of tNBs undergoing DNA or translational stress. The reason and consequences of such cellular stresses in tumor progression need to be further investigated.

Our transcriptomic analyses have revealed strong similarities in the differentiation trajectories of tNBs in tumors and of NBs in larvae. Yet, it is surprising that the down-regulation of glutamine and glucose metabolism genes has not been detected in NBs during larval development, after the Imp-to-Syp transition (Ren et al., 2017). It is possible that the glial niche surrounding NBs, that is known to influence NB growth properties during larval stages (Chell and Brand, 2010; Cheng et al., 2011; Sousa-Nunes et al., 2011), somehow sustains high levels of glucose metabolism genes in late Syp+E93+ NBs. Given that this glial niche is absent in tumors, Syp+E93+ tNBs may not be able to sustain the high expression of metabolic genes imposed by the Imp/Chinmo module, leading to progressive cell-cycle exit.

### Imp and syp: a conserved couple of antagonistic RNA-binding proteins regulating cell hierarchy in human tumors?

Chinmo and Imp are reminiscent to oncofetal genes in mammals, in that their expression decrease rapidly as development progresses while they are mis-expressed in tumors. Along these lines, the three IMP orthologs in humans (also called IGF2BP1-3) are also known as oncofetal genes. They emerge as important regulators of cell proliferation and metabolism in many types of cancers including pediatric neural cancers (Bell et al., 2015; Dai et al., 2017; Degrauwe et al., 2016a; Degrauwe et al., 2016b; Janiszewska et al., 2012). Along evolution, the ancestral Syncrip gene has been subjected to several rounds of duplication and has diverged into five paralogs in mammals, some of them emerging as tumor suppressors with an important role in tumor progression (Sakurai et al., 2016; Vanharanta et al., 2014).

Thus, the respective oncogenic and tumor suppressor roles of IMP and SYNCRIP gene families appear to have been conserved in humans and they may not be restricted to tumors of neural origin. Our study therefore raises the exciting possibility that these two families of RNA-binding proteins form a master module at the top of the self-renewal/differentiation cascades, that regulates CSC populations and hierarchy in a spectrum of human cancers.

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
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Flybow. 1.1</td>
      <td>Bloomington Drosophila Stock Center (Hadjieconomou et al., 2011)</td>
      <td>RRID:BDSC_35537</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-mCherrychinmoUTRs</td>
      <td>Cédric Maurange (Dillard et al., 2018)</td>
      <td></td>
      <td>mCherry reflects the post-transcriptional regulation of chinmo.</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-SypRNAi1</td>
      <td>VDRC</td>
      <td>33011</td>
      <td>RNAi1</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-SypRNAi2</td>
      <td>VDRC</td>
      <td>33012</td>
      <td>RNAi2</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Syp-RB-HA</td>
      <td>Tzumin Lee (Liu et al., 2015)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-prosRNAi1</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>RRID:BDSC_26745</td>
      <td>RNAi1</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-prosRNAi2</td>
      <td>VDRC</td>
      <td>101477</td>
      <td>RNAi2</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-ImpRNAi</td>
      <td>VDRC</td>
      <td>20322</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-chinmoRNAi</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>RRID:BDSC_33638</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-dicer2</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>RRID:BDSC_24650 RRID:BDSC_24651</td>
      <td>was used in combination with GAL4 lines in order to improve RNAi efficiency.</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-mCD8::GFP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>RRID:BDSC_5130 RRID:BDSC_32185</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-myr::GFP</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>RRID:BDSC_32197</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-mCherry.NLS</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>RRID:BDSC_38424</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Snr1RNAi1</td>
      <td>VDRC</td>
      <td>108599</td>
      <td>RNAi1</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Snr1RNAi2</td>
      <td>VDRC</td>
      <td>32372</td>
      <td>RNAi2</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Gapdh1RNAi</td>
      <td>VDRC</td>
      <td>100596</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Pglym78</td>
      <td>VDRC</td>
      <td>106818</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Cyt-c1RNAi1</td>
      <td>VDRC</td>
      <td>9180</td>
      <td>RNAi1</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Cyt-c1RNAi2</td>
      <td>VDRC</td>
      <td>109809</td>
      <td>RNAi2</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Cyt-c-pRNAi1</td>
      <td>VDRC</td>
      <td>33019</td>
      <td>RNAi1</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-Cyt-c-pRNAi2</td>
      <td>VDRC</td>
      <td>106759</td>
      <td>RNAi2</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w, tub-GAL4, UAS-nlsGFP::6xmyc::NLS, hsFLP122; FRT82B, tubP-GAL80/TM6B</td>
      <td>Cédric Maurange (Narbonne-Reveau et al., 2016)</td>
      <td></td>
      <td>MARCM line</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>FRT82B snr16C hdac36C</td>
      <td>Bloomington Drosophila Stock Center (Koe et al., 2014)</td>
      <td>RRID:BDSC_34494</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>Imp-GFP</td>
      <td>Florence Besse</td>
      <td></td>
      <td>protein trap line</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>poxn-Gal4</td>
      <td>Bloomington Drosophila Stock Center (Boll and Noll, 2002)</td>
      <td>RRID:BDSC_ 66685</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>ase-Gal80, wor-GAL4, UAS-dcr2</td>
      <td>Juergen Knoblich (Eroglu et al., 2014)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>nab-GAL4</td>
      <td>Kyoto DGRC</td>
      <td>6190</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>UAS-FLP, Ubi-p63EFRTstopFRTnEGFP</td>
      <td>Bloomington Drosophila Stock Center (Evans et al., 2009)</td>
      <td>RRID:BDSC_28282</td>
      <td>G-trace</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>hs-mFLP5</td>
      <td>Bloomington Drosophila Stock Center (Hadjieconomou et al., 2011)</td>
      <td>RRID:BDSC_35534</td>
      <td>Flipase for Flybow</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>chicken polyclonal anti-GFP</td>
      <td>Aves Labs #GFP-1020</td>
      <td>RRID:AB_10000240</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rabbit polyclonal anti-RFP</td>
      <td>Rockland #600-401-379</td>
      <td>RRID:AB_2209751</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rat monoclonal anti-RFP</td>
      <td>Chromotek #5F8</td>
      <td>RRID:AB_2336064</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>mouse monoclonal anti-Miranda</td>
      <td>Alex Gould</td>
      <td></td>
      <td>1:50</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rabbit polyclonal anti-PH3</td>
      <td>Millipore #06–570</td>
      <td>RRID:AB_310177</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rat monoclonal anti-PH3</td>
      <td>Abcam #AB10543</td>
      <td>RRID:AB_2295065</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rat monoclonal anti-Elav</td>
      <td>DSHB</td>
      <td>#9F8A9</td>
      <td>1:50</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rabbit polyclonal anti-cleaved Dcp-1</td>
      <td>Cell Signaling #9578</td>
      <td>RRID:AB_2721060</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rat polyclonal anti-Chinmo</td>
      <td>Nick Sokol</td>
      <td></td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rabbit polyclonal anti-Imp</td>
      <td>Paul Macdonald</td>
      <td></td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>guinea pig polyclonal anti-Syp</td>
      <td>Ilan Davis</td>
      <td></td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-Syp</td>
      <td>Ilan Davis</td>
      <td></td>
      <td>1/200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rabbit polyclonal anti-E93</td>
      <td>Daniel J. McKay</td>
      <td></td>
      <td>1/2500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>guinea-pig polyclonal antibody</td>
      <td>Bill McGinnis</td>
      <td></td>
      <td>1/200</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dapi</td>
      <td>Vector Laboratories Cat# H-1400</td>
      <td>RRID:AB_2336787</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Chinmo cDNA clone</td>
      <td>DGRC, EST Collection</td>
      <td>#RE59755</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Chin-5'UTR/pBS_Forward</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>Described in Affinity pull-down assays section in the Materials and methods</td>
    </tr>
    <tr>
      <td>Sequenced-based reagent</td>
      <td>Chin-5'UTR/pBS_Reverse</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>Described in Affinity pull-down assays section in the Materials andmethods</td>
    </tr>
    <tr>
      <td>Sequenced-based reagent</td>
      <td>Chin-3'UTR/pBS_Forward</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>Described in Affinity pull-down assays section in the Materials and methods</td>
    </tr>
    <tr>
      <td>Sequenced-based reagent</td>
      <td>Chin-3'UTR/pBS_Reverse</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>Described in Affinity pull-down assays section in the Materials andmethods</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Seurat and Monocle codes used for single-cell RNA-seq data analysis</td>
      <td>This paper</td>
      <td>https://github.com/cedricmaurange/Genovese-et-al.-2019</td>
      <td>See the Single-cell mRNA sequencing and analysis section in the Materials and methods</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Code used for numerical model</td>
      <td>This paper</td>
      <td>http://dx.doi.org/10.17632/j2j9gmyb6m.1</td>
      <td>See the Numerical model section in the Materials and methods</td>
    </tr>
  </tbody>
</table>

### Fly culture

Drosophila stocks were maintained at 18°C on standard medium (8% cornmeal/8% yeast/1% agar).

### Fly lines

The protein trap line used was:

The Gal4 lines used were:

The UAS lines used were:

The MARCM and FRT stocks for used were:

Fly crosses were set up and raised at 29°C. To label all tumor cells with GFP, poxn-Gal4, UAS-prosRNAi, UAS-dicer2 flies were crossed with the G-TRACE system UAS-FLP, Ubi-p63EFRTstopFRTnEGFP (Bloomington Stock Centre #28282) (Evans et al., 2009). To generate mCherry+ clones in tumors, poxn-GAL4, UAS-prosRNAi1, UAS-mCD8::GFP; UAS-dicer2 flies were crossed to UAS-Flybow.1.1; hs-mFLP5 (Bloomington Stock Centre #35534 and #35537) (Hadjieconomou et al., 2011). The progeny of this cross was collected 48 hours after adult eclosion and heat-shocked for 1h30’ at 37°C. Flies were put back at 29°C after heat-shock. Note that differentiated neurons generated from mCherry+ tNBs will not retain mCherry expression due to the silencing of poxn-GAL4 in neurons. MARCM clones were induced by heat-shocking 1 hr at 37°C larvae that have just hatched.

### Image processing

Confocal images were acquired on a Zeiss LSM780 microscope. FIJI-ImageJ was used to process confocal data and to compile area and volume data. Imaris Image Analysis Software (http://bitplane.com) was used to generate 3D representations of clones in tumors.

### Tumor segmentation using tissue analyzer

For Figure 8E, poxn > prosRNAi tumors carrying an Imp-GFP marker were dissected, fixed in 4% paraformaldehyde and stained with antibodies against Miranda and GFP proteins. VNCs were visualized in a Zeiss LSM780 confocal microscope and co-planar images were made of several sections ranging from the tumor surface to its interior. Several confocal planes for four tumors (n = 21) were analyzed using the ‘Tissue Analyzer’ plugin for FIJI-ImageJ (Aigouy et al., 2016). This tool allows for cell membrane tracing, via the signal from Miranda which marks the cellular border of all tumor cells, segmentation and quantification of several parameters, including size, of each tumor cell individually. Chinmo+Imp+ tNBs are identified by their strong Imp-GFP signal. Initial automatic segmentation was further refined manually to ensure all cell boundaries were properly tracked and cells assigned a correct identity (Figure 8—figure supplement 3). Data points represent different planar sections within the same tumor, in order to account for variability within each tumor.

### Statistical analysis

For each experiment, at least three biological replicates were performed. Biological replicates are defined as replicates of the same experiment with flies being generated by different parent flies. For all experiments, we performed a Mann-Whitney test for statistical analysis. Statistical analysis was performed using GraphPad Prism version 7.04 for Windows (GraphPad Software, La Jolla California USA, www.graphpad.com). Results are presented as dot plots. Error bars represent s.d. from the mean. The sample size (n) and the P-value are reported in the figure legends (****p≤0.0001; ***p≤0.001; **p≤0.01; *p≤0.05; ns, not significant).

### Immunohistochemistry

Larval and adult VNCs were dissected in phosphate-buffered saline (PBS) and fixed for 10 min at room temperature (RT) in 4% paraformaldehyde/PBS. VNCs were rinsed in PBT (PBS containing 0.5% Triton X-100) and incubated with primary antibody overnight at 4°C. Secondary antibodies (Jackson ImmunoResearch) were incubated overnight at 4°C. VNCs were mounted in Vectashield (Clinisciences, France) with or without DAPI for image acquisition. The following primary antibodies were used: chicken anti-GFP (1:1000, Aves #GFP-1020), rabbit anti-RFP to label mCherry (1:500, Rockland #600-401-379), rat anti-RFP (1:500, Chromotek #5F8), mouse anti-Miranda (1:50, A Gould, Francis Crick Institute, London, UK), rabbit anti-PH3 (1:500, Millipore #06–570), rat anti-PH3 (1:500, Abcam #AB10543), rat anti-Elav (1:50, DSHB #9F8A9), rabbit anti-cleaved Dcp-1 (1:500, Cell Signaling #9578)), rat anti-Chinmo (1:500, N Sokol, Indiana University, Bloomington, USA), rabbit anti-Imp (1:500, P Macdonald), guinea pig anti-Syp (1/500, I Davis, Oxford University, UK), rabbit anti-Syp (1/200, I Davis, Oxford University, UK), rabbit anti-E93 (1/2500, DJ McKay, University of North Carolina, Chapel Hill).

### Affinity pull-down assays

Affinity pull-down assays were performed as previously described (Medioni et al., 2014), and Western Blots performed using rat anti-Imp and rabbit anti-Syp antibodies. The 5’ and 3’ UTRs of chinmo were cloned from the cDNA clone #RE59755 (DGRC, EST Collection) using the following primers:

<table>
  <tbody>
    <tr>
      <td>Chin-5'UTR/pBS_Forward</td>
      <td>aatttctagaAGTCAAAAAGAAACTGCCGTG</td>
    </tr>
    <tr>
      <td>Chin-5'UTR/pBS_Reverse</td>
      <td>gatgaagcttGGTGCCAGCAGTGATGCT</td>
    </tr>
    <tr>
      <td>Chin-3'UTR/pBS_Forward</td>
      <td>taaatctagaGAAGCAGCCGCAACAGCA</td>
    </tr>
    <tr>
      <td>Chin-3'UTR/pBS_Reverse</td>
      <td>ttttaagcttGGTGAATTTTCATTTGTACGAAGAA</td>
    </tr>
  </tbody>
</table>

Capitals represents analogous or complementary parts of the chinmo sequence. In bold are the restriction sites used for cloned into pBS-KS(-) (TCTAGA = XbaI, AAGCTT = HindIII), and in lower case are extra bases for efficient digestion. This plasmid was used to generate the UTP-biotinylated-RNA probes (5’UTR and 3’UTR).

### RNA extraction of bulk tumors

To generate NB tumors poxn-Gal4, UAS-mCherry.NLS; UAS-dicer2 flies were crossed to flies carrying:

Crosses were grown at 29°C. Sixteen adult females and 13 adult males (8 day-old) were killed in 70% ethanol and washed once in PBS. VNCs containing tumors were dissected in PBS and collected in a RNase-free Protein LoBinding tube filled with 750 μL of Lysis Buffer (Buffer RLT, RNeasy Mini Kit, Qiagen) supplemented with 7.5 μL of β-mercaptoethanol and 500 μL of glass beads (diameter 0.75–1 mm, Roth, A554.1). Samples were disrupted and homogenized using the tissue homogenizer Precellys 24 (Bertin Technologies).

Sample tubes were then stored at −80°C up to RNA extraction. Total RNA was extracted using the RNeasy Mini Kit (Qiagen). RNA quality and quantity were checked by running samples on an Agilent RNA 6000 Pico Chip (Agilent Technologies). For each condition, samples were made from 29 dissected VNCs pooled from adult flies born from several crosses (more than 3). For technical replicates, two samples of each condition were generated and treated in parallel until sequencing.

### Library preparation and sequencing of bulk tumors

Total RNA-Seq libraries were generated from 130 ng of total RNA using TruSeq Stranded Total RNA LT Sample Prep Kit with Ribo-Zero Gold (Illumina, San Diego, CA), according to manufacturer's instructions. Briefly, cytoplasmic and mitochondrial ribosomal RNA (rRNA) was removed using biotinylated, target-specific oligos combined with Ribo-Zero rRNA removal beads. Following purification, the depleted RNA was fragmented into small pieces using divalent cations at 94°C for 2 min. Cleaved RNA fragments were then copied into first strand cDNA using reverse transcriptase and random primers followed by second strand cDNA synthesis using DNA Polymerase I and RNase H. Strand specificity was achieved by replacing dTTP with dUTP during second strand synthesis. The double stranded cDNA fragments were blunted using T4 DNA polymerase, Klenow DNA polymerase and T4 PNK. A single 'A' nucleotide was added to the 3' ends of the blunt DNA fragments using a Klenow fragment (3' to 5'exo minus) enzyme. The cDNA fragments were ligated to double stranded adapters using T4 DNA Ligase. The ligated products were enriched by PCR amplification (30 s at 98°C; [10 s at 98°C, 30 s at 60°C, 30 s at 72°C] x 12 cycles; 5 min at 72°C). Surplus PCR primers were further removed by purification using AMPure XP beads (Beckman-Coulter, Villepinte, France) and the final cDNA libraries were checked for quality and quantified using capillary electrophoresis.

The libraries were loaded in the flowcell at a concentration of 2.8 nM and clusters were generated using the Cbot and sequenced on an Illumina HiSeq 4000 system as paired-end 100 base reads following Illumina’s instructions.

### RNA-Seq analysis of bulk tumors

Quality control of raw reads was done using FastQC. Reads were mapped to dmel6 reference genome with Subread aligner using default parameters (Liao et al., 2013). Read counts were calculated using Subread featureCount (Liao et al., 2014). Differential expression was computed using R package DESeq2 (Love et al., 2014). To concentrate on genes that are expressed in tNBs and remove those that are specific to wild type neurons and glia of the VNC, we excluded from the bulk RNA-seq analysis all genes that are not expressed in at least 0,5% of the 5740 cells used for the single-cell RNA-seq experiment. Among the remaining 6660 genes, we selected as significantly enriched genes those with an adjusted p-value<0001. Gene Ontology and Reactome Pathway analysis was made using Panther (http://www.pantherdb.org/). Sequencing data have been deposited in GEO under accession code GSE114562.

### Preparation of tNBs for single-cell mRNA-seq

NB tumors were generated in poxn-Gal4, UAS-GFP UAS-prosRNAi2, UAS-dicer2 flies. Fifty-six adult females (6–8 day-old) were killed in 70% ethanol and washed once in PBS. VNCs were dissected in PBS, collected in a RNase-free Protein LoBinding tube filled with ice-cold PBS, and incubated in a freshly prepared dissociation solution containing 0,4% bovine serum albumin (BSA), 1 mg/mL collagenase I and papain (Sigma Aldrich) in PBS for 75 min at 29°C with lowest agitation. Tissues were then disrupted manually by pipetting up and down with a 200 µL tip. Dissociated cells were pelleted for 20 min at 300 g at 4°C to remove the dissociation solution and to resuspend cells in ice-cold PBS + 0,4% BSA. The cell suspension was filtered through a 30 µm mesh Pre-Separation Filter (Miltenyi) to remove debris and transferred in new RNase-free Protein LoBinding tube for FACS sorting. Forty thousand GFP+ tNBs cells were isolated using a FACSAriaII machine (BD) with an 85 μm nozzle, at 45 psi low pressure and according to viability, cell size and GFP intensity. In the next 30 min, sorted-cells were encapsidated using with the Single Cell Controller (10X genomics) for single-cell RNA-seq.

### Single-cell mRNA sequencing and analysis

Codes used for single-cell RNA-seq analysis are available at: https://github.com/cedricmaurange/Genovese-et-al.-2019 (Maurange, 2019; copy archived at https://github.com/elifesciences-publications/Genovese-et-al.-2019).

#### Single-cell mRNA sequencing

Single cells were processed using the Single cell 3’ Library, Gel beads and multiplex kit (10X Genomics, Pleasanton) as per the manufacter’s protocol. Cells were partitioned into nanoliter-scale Gel Bead-In-Emulsions (GEMs) with the Chromium Single Cell Controller (10X genomics, Pleasanton), where all generated cDNA share a common 10x Barcode. Libraries were generated and sequenced from the cDNA and the10x Barcodes are used to associate individual reads back to the individual partitions. Analysis using molecular indexing information provides an absolute digital measurement of gene expression levels. Sequencing was performed using a NextSeq 500 Illumina device (1sample) containing transcript lengh of 57 bp. Sequencing data have been deposited in GEO under accession code GSE114986.

#### Data processing

Single-cell mRNA seq data were analyzed using the 10x Genomics suite Cell Ranger 2.0.1 with default settings for de-multiplexing, aligning reads to the Drosophila genome (10X Genomics pre-built dm6 reference genome) with STAR and counting unique molecular identifiers (UMIs) to build transcriptomic profiles of individual cells. This first level of analysis generates quality metrics (Q30, number of reads by sample…), FASTQ files and filtered genes matrices.

#### PC analysis, UMAP clustering and differential expression

Filtered gene matrices generated via Cell Ranger 2.0.1 was then processed with the R package Seurat v3.0.2, using the online tutorial as a guide (https://satijalab.org/seurat/v3.0/pbmc3k_tutorial.html). We kept all cells that had between 200 and 4000 genes/cell. Cells with more than 5% mitochondrial gene expression were removed. Cell cycle genes were regressed out using the CellCycleScoring and ScaleData functions.

PCA was then utilized to determine sources of variability. Twenty significant PCs were determined based on the JackStraw function. We used the PCHeatmap function to explore gene sets representing the main sources of heterogeneity in the dataset. Cells were then clustered with the FindClusters function a resolution parameter of 0.5. Differentially expressed genes were determined with the FindAllMarkers and function. Code available upon request.

#### Cell trajectory and pseudo time analysis by Single-cell mRNA sequencing

Filtered gene matrices generated via Cell Ranger 2.0.1 was processed with the R package Monocle version v2.10.1. for pseudotime analysis (Qiu et al., 2017a; Qiu et al., 2017b; Trapnell et al., 2014). Graphics were generated through ggplot2 R library. Analysis was performed following online tutorial as a guide (http://cole-trapnell-lab.github.io/monocle-release/docs/#constructing-single-cell-trajectories). UMI Counts were both normalized across cells using estimateSizeFactors function and gene expression variance was estimated using estimateDispersions functions to remove outlier genes using DESeq2 packages (Love et al., 2014). Semi-supervised ordering was performed with the classifyCells function. Only genes expressed in at least 10 cells were taken in account. Marker genes were selected for subsequent analysis based on their normalized average expression and variability across cells using markerDiffTable function. The top 200 genes were used for ordering.

Dimension reduction was performed with Monocle implementation of Discriminative Dimension Reduction Tree (DDRTree) algorithm (Qi Mao et al., 2017) using reduceDimension function. Minimum spanning tree computation, cell state assignations and pseudo time reconstruction was performed using orderCells functions. differentialGeneTest and plot_pseudotime_heatmap functions were used to uncover the top 200 genes that change as a function of pseudotime. The BEAM function was used to identify genes that are differentially expressed between the three main branches of the trajectory (qval <1e-20). Code available upon request.

### Numerical model

Codes generated for the numerical model are available at: http://doi.org/10.17632/j2j9gmyb6m.1.

#### 1. Algorithm of the clone model

In this section we detail the stochastic numerical model used to generate clones.

Each clone grows from a single initial cell. There are two cell types, Chinmo+Imp+ tNBs (which we will call C cells for simplicity) and Syp+E93+ tNBs (called S cells). The probability that the initial cell is a C cell is $p_{c}$ and the probability that the initial cell is a S cell is $p_{s}=1-p_{c}$.

We assume that C and S cells have constant division rates, $k_{c}$ and $k_{s}$ respectively. We define the division times as the inverses of the division rates, so that $T_{c}=1/k_{c}$ and $T_{s}=1/k_{s}$. An implicit assumption is that we neglect any refractory period following a division. Divisions are considered as random events occurring at a certain rate.

We use T = 1 hr long time steps. The growth of a model clone during 10 days thus runs over 240 time steps.

At each time step, for each C cell (resp. S cell) in the clone, the probability to undergo division is equal to $\int_{0}^{T}\frac{1}{T_{c}}e^{-t/T_{c}}dt=1-e^{-T/T_{c}}$ (resp.$1-e^{-T/T_{s}}$).

If a C cell undergoes division, it can either:

Similarly, if a S cell undergoes division, it can either:

In addition, each newly created C cell (resp. S cell) has a probability $q_{c}$ (resp.$q_{s}$) to be quiescent. Note that this also applies to the initial cell of the clone. Quiescent cells lose their ability to undergo further divisions. In this simplified model, this probability does not depend on cell generation (as cells have no age in the model). However, it is likely that “older” cells have a higher chance to become quiescent. This is not taken into account here.

To produce plots of size distributions and of composition ratios, we simply generate a large number of clones (N = 1000) by iterating this algorithm. Due to the stochastic nature of the algorithm, there is important size and composition variability among simulated clones, which we can compare to the variability observed in vivo.

#### 2. Reducing the amount of independent parameters

This general model has 9 independent parameters: $p_{c}$, $T_{c}$, $T_{s}$, $P(c→cc)$, $P(c→cs)$, $P(s→ss)$, $P(s→cs)$, $q_{c}$ and $q_{s}$.

To reduce the number of independent parameters, we performed experimental measurements in clones that allow to establish quantitative relationships between the parameters.

##### a. Two-cell clones

First, we analyzed clones composed of exactly two cells. To that end, we chose to look tumors 2 days after clonal induction, as at this stage many clones are composed of two cells (Figure 4—figure supplement 1).

The probability for a two-cell clone to be composed of two C cells is:

$$
P(CC)=p_{c }P(c→cc)+p_{s }P(s→cc)
$$

Similarly,

$$
P(CS)=p_{c }P(c→cs)+ p_{s} P(s→cs)
$$

and

$$
P(SS)=p_{c }P(c→ss)+ p_{s} P(s→ss)=1−P(CC)−P(CS)
$$

We estimated $P(CC)$, $P(CS)$ and $P(SS)$ from N=122 2-cell clones (7 animals), and found that $P(CC)≈0.29$, $P(CS)≈0.07$ and $P(SS)≈0.64$.

Using these values in Equations (1) and (2) reduces the number of independent parameters from 9 to 7 (as Equation (3) is not independent from Equations (1) and (2)).

##### b. Quiescent cells

We analyzed clones 8 days ACI. We reasoned that clones still composed of a single cell at this stage were most likely initiated from an initially quiescent cell. Hence the probability $PQC$ to observe a clone composed of a single C cell at 8 days is equal to the probability for an initial cell to be a quiescent C cell, so that:

$$
PQC=p_{c}q_{c}
$$

Similarly, the probability that a clone is composed of a single quiescent S cell is

$$
PQS=p_{s}q_{s}
$$

We estimated $PQC$ and $PQS$ from N=338 clones 8 days after induction (5 animals), and found that $PQC≈0.02$ and $QS≈0.26$. Using these values in equations (4) and (5) reduces the number of independent parameters by another 2.

##### c. Hierarchical scenario

We are left with 5 independent parameters. We showed in the main text that experimental clone data has the signature of a hierarchical growth mode (maintenance of clones composed of S cells only). In the following we thus rule out the generation of C cells by S cells. Hence P$s→ss=1$, and $Ps→cs=Ps→cc=0$.

In addition, if C cells can only be generated by C cells, we can estimate the division time $T_{c}$ of C cells. At time t, the number of cells in clones only composed of C cells should be on average equal to $N_{c}t=e^{t/T_{c}}$.

At 2 days, we find that clones composed only of C cells are composed, on average, of 3.4 cells (N=75 clones from 5 animals). Hence $T_{c}≈\frac{2}{ln3.4}=1.6$ days.

Hence, we are left with only two independent parameters, from which all the others can be determined. We arbitrarily chose $T_{s}$ and $P(c→cc)$ as these two parameters, and used these as free parameters to perform the fits.

#### 3. Fitting experimental data

To determine the values of $T_{s}$ and $P(c→cc)$, we adopted a fitting approach. We want to determine the values of $T_{s}$ and $P(c→cc)$ that fit best our experimental data. To that end we generated error maps in the $(Pc→cc,T_{s})$ space (Figure 4—figure supplement 2). To generate the error maps, we computed 1000 clones for each pixel (100x100) on the map.

We calculate the error on size as the Kolmogorov-Smirnov distance between model and experimental clone size distributions, for all clone categories and at all stages (12 terms).

We calculate the error on composition as the normalized sum of Euclidian distances between model and experimental proportions of each clone category at all stages (12 terms).

The combined error is the average between the normalized error on size and the normalized error on composition.

We find that the smallest error is found for $Pc→cc≈0.64$ and $T_{s}≈1.3$ days, and thus (Equations 1-5):

$$
p_{c}≈0.45
$$



$$
P(c→cs)≈0.15
$$



$$
P(c→ss)≈0.21
$$



$$
q_{c}≈0.04
$$



$$
q_{s}≈0.47
$$

We use these values to generate Figures 4C–G and 5A,B, and Figure 4—figure supplement 2.

#### 4. Tumor composition and deterministic version of the model

##### a. Proportion of S and C cells in tumors

To test whether our model also accounts for the stabilization of the volume fraction occupied by S and C cells in tumor, we simulated the growth of clones on longer periods (30 days), and plotted the overall proportion of each cell type as a function of time (Figure 5A).

##### b. Deterministic, continuous model

To better understand this homeostatic behavior without systematically simulating thousands of clones, we wrote a deterministic version of the model where the exact same ingredients and parameters are used.

For simplicity, we call $C$ the number of C cells, $S$ the number of S cells, $C_{q}$ the number of quiescent C cells and $S_{q}$ the number of quiescent S cells. The rate of change of $C$ writes:

$$
\frac{dC}{dt}=-k_{c}C+1-q_{c}2k_{c→cc}+k_{c→cs}C+1-q_{c}2k_{s→cc}+k_{s→cs}S
$$

With $k_{x→yz}=k_{x}P(x→yz)$, where $x$, $y$ and $z$ are cell types (C or S).

Each C cell division removes 1 C cell (first term). C cell divisions can also generate 1 or 2 C cells with given rates (second term), with a possibility that they are quiescent (prefactor $1-q_{c}).$ S cell divisions can also generate C cells (third term), which can also be quiescent (prefactor).

Similarly, we can write the rate of change of $S$:

$$
\frac{dS}{dt}=-k_{s}S+1-q_{s}2k_{s→ss}+k_{s→cs}S+1-q_{s}2k_{c→ss}+k_{c→cs}C
$$

And for quiescent cells:

$$
\frac{dC_{q}}{dt}=q_{c}2k_{c→cc}+k_{c→cs}C+q_{c}2k_{s→cc}+k_{s→cs}S
$$



$$
\frac{dS_{q}}{dt}=q_{s}2k_{s→ss}+k_{s→cs}S+q_{s}2k_{c→ss}+k_{c→cs}C
$$

Note that this continuous model is fully deterministic, and therefore not suited for the simulation of clone size distribution and composition, which are inherent to the stochastic aspects of divisions. However, it can recapitulate the overall proportion of cell types in a large population of cells. Integrating this system of equations, we thus computed the ratios $\frac{C+C_{q}}{N_{cells}}$ and $\frac{S+S_{q}}{N_{cells}}$, that is, the respective proportions of C and S cells. We first compared the outcome of the deterministic model to the outcome of the clone model using the exact same parameters. We find that the deterministic model perfectly fits the stochastic model (Figure 5A), and reaches the same homeostatic state. Importantly, this is also a control that both algorithms were properly implemented. We also use this deterministic model to illustrate the influence of the initial proportions of C and S cells (Figure 5B).
