# Genetic parallels in biomineralization of the calcareous sponge Sycon ciliatum and stony corals

## Authors

- Oliver Voigt<sup>1</sup> ([ORCID: 0000-0001-8708-0872](https://orcid.org/0000-0001-8708-0872)) †
- Magdalena V Wilde<sup>1</sup> ([ORCID: 0000-0002-1997-8768](https://orcid.org/0000-0002-1997-8768))
- Thomas Fröhlich<sup>2</sup> ([ORCID: 0000-0002-4709-3211](https://orcid.org/0000-0002-4709-3211))
- Benedetta Fradusco<sup>1</sup>
- Sergio Vargas<sup>1</sup> ([ORCID: 0000-0001-8704-1339](https://orcid.org/0000-0001-8704-1339))
- Gert Wörheide<sup>1</sup> ([ORCID: 0000-0002-6380-7421](https://orcid.org/0000-0002-6380-7421))

### Affiliations

1. Department of Earth and Environmental Sciences, Paleontology and Geobiology, Ludwig Maximilians-Universität München Munich Germany ([ROR:05591te55](https://ror.org/05591te55))
2. Gene Center—Laboratory for Functional Genome Analysis, Ludwig-Maximilians-Universität München Munich Germany ([ROR:05591te55](https://ror.org/05591te55))
3. GeoBio-Center, Ludwig-Maximilians-Universität München Munich Germany ([ROR:05591te55](https://ror.org/05591te55))

† Corresponding author

## Abstract

The rapid emergence of mineralized structures in diverse animal groups during the late Ediacaran and early Cambrian periods likely resulted from modifications of pre-adapted biomineralization genes inherited from a common ancestor. As the oldest extant phylum with mineralized structures, sponges are key to understanding animal biomineralization. Yet, the biomineralization process in sponges, particularly in forming spicules, is not well understood. To address this, we conducted transcriptomic, genomic, and proteomic analyses on the calcareous sponge Sycon ciliatum, supplemented by in situ hybridization. We identified 829 genes overexpressed in regions of increased calcite spicule formation, including 17 calcarins—proteins analogous to corals’ galaxins localized in the spicule matrix and expressed in sclerocytes. Their expression varied temporally and spatially, specific to certain spicule types, indicating that fine-tuned gene regulation is crucial for biomineralization control. Similar subtle expression changes are also relevant in stony coral biomineralization. Tandem gene arrangements and expression changes suggest that gene duplication and neofunctionalization have significantly shaped S. ciliatum’s biomineralization, similar to that in corals. These findings suggest a parallel evolution of carbonate biomineralization in the calcitic S. ciliatum and aragonitic corals, exemplifying the evolution of mechanisms crucial for animals to act as ecosystem engineers and form reef structures.

## Introduction

The evolution of biomineralization allowed animals to produce important mineralized functional structures, such as shells, teeth, and skeletons. For this, they most frequently use calcium carbonate, calcium phosphate, and silicate as mineral components, of which calcium carbonate is taxonomically the most diverse (Knoll, 2003; Murdock and Donoghue, 2011). Animal biominerals are usually composite materials of organic and mineral compounds and exhibit material properties and shapes that differ enormously from their purely mineral counterparts. Their formation requires biological control governed by specific genes and proteins in specialized biomineralization cells and tissues. Those then ensure supply with the necessary inorganic substances into the calcifying space (intracellularly or extracellularly) to enable crystal precipitation and growth, e.g., by pH regulation. They also provide organic components, including secreted, so-called ‘matrix proteins’ that influence the polymorph and shape of the biomineral and subsequently may become embedded in it (Aizenberg et al., 1996; Aizenberg et al., 1994).

The ability to form biominerals evolved several times independently in animal lineages, and early instances of mineralized animal skeletons appeared within a geologically brief span, from the latest Ediacaran to the Middle Cambrian (Murdock and Donoghue, 2011). According to the ‘biomineralization toolkit’ hypothesis, animals of this era had acquired pre-adapted genes and gene-regulatory networks necessary to produce biominerals in a controlled manner that were further refined independently in different lineages (Murdock, 2020). This can be achieved by gene family expansion, in which, after initial gene duplication, diversification by mutation and natural selection leads to the neofunctionalization of a copied gene in the biomineralization process.

Among early branching, non-bilaterian calcifiers, stony corals are best studied, and essential elements of their genetic biomineralization machinery are known that originate from gene duplication and neofunctionalization, such as the SLC4γ bicarbonate transporter (SLC4γ) that is a key component of the coral aragonite skeleton forming machinery (Tinoco et al., 2023; Zoccola et al., 2015). Numerous skeletal matrix proteins have been identified (Drake et al., 2013; Peled et al., 2020; Ramos-Silva et al., 2013). Among those, galaxin and related proteins were the first to be characterized, and at least in some species, comprise the most dominant protein in skeletal matrix extractions (Fukuda et al., 2003; Watanabe et al., 2003). Acidic proteins are another essential component of coral skeletal matrices, presumably influencing the polymorph of the precipitating carbonate (Drake et al., 2013; Laipnik et al., 2020; Mass et al., 2016). However, the genetic mechanisms of the calcium carbonate biomineralization in sponges (class Porifera) are less known. Sponges produce skeletal elements in the form of differently shaped spicules, siliceous in the extant sponge classes Demospongiae, Hexactinellida, and Homoscleromorpha, and calcitic only in the class Calcarea (calcareous sponges). Nonetheless, some demosponges like the polyphyletic ‘sclerosponges’ may form a rigid calcium carbonate basal skeleton in addition to or instead of siliceous spicules (Wörheide, 1998). Essential skeletal matrix proteins occluded in such rigid calcitic carbonate skeletons of sclerosponges have been studied in Astrosclera willeyana (Jackson et al., 2011; Jackson et al., 2007) and Vaceletia sp. (Germer et al., 2015). In contrast to those aragonite-producing sclerosponges, calcareous sponges continuously produce calcitic spicules of different shapes, providing a unique opportunity to observe all stages of the process and study differences in their production. Additionally, their spicule formation is often faster than the production of skeletal elements in other calcifiers. It takes only a few days from initiation to the finished spicule and involves only a few specialized cells called sclerocytes (Ilan et al., 1996; Woodland, 1905). They control biomineralization by their relative movement to each other and by secreting specific proteins, ions, and other substances into the calcification space, a process still little understood at the molecular level. Only a few genes involved in calcification in calcareous sponges are known, including two specific carbonic anhydrases, and two SLC4 bicarbonate transporters, and three acidic proteins, two of which are spicule-type specific (Voigt et al., 2021; Voigt et al., 2017; Voigt et al., 2014). Skeletal matrix proteins have not yet been identified but are of particular interest because they may play a crucial role in spicule morphogenesis (Aizenberg et al., 1995).

In this study, we used genomic data, differential gene expression (DGE) analysis, and RNA in situ hybridization (ISH) experiments, supplemented by a proteomic approach, to identify genes directly involved in the spicule formation in the calcarean model species Sycon ciliatum (subclass Calcaronea), and compare those with another non-bilaterian calcifying clade, the scleractinian (stony) corals, the ecosystem engineers of today’s coral reefs. We found surprising similarities in key components of the biomineralization toolkit between calcareous sponges and corals that shed new light on the evolution of calcium carbonate biomineralization in animals.

## Results

Sycon ciliatum is a tube-shaped sponge with a single apical osculum and a sponge wall of radial tubes around the central atrium (Figure 1A). The radial tubes are internally lined with choanoderm, which forms elongated chambers in an angle of approximately 90° to the tube axis. The sponge tissue is supported by a skeleton composed of countless spicules arranged in a specific pattern within the sponge body (Figure 1A). The spicules are formed by sclerocytes located within the mesohyl, the extracellular matrix of the sponge. Connected by septate junctions, they enclose an extracellular space where a spicule grows (Ledger, 1975). Only a small number of sclerocytes participate in forming a single spicule (Figure 1C). Production of each actine (ray) of a spicule involves a pair of sclerocytes (Woodland, 1905): a founder cell, which initiates actine elongation at the tip, and a thickener cell, located alongside the actine. The thickener cell enhances actine strength in some species by precipitating additional calcium carbonate. More spicules are produced in the apical growth zone than in other regions of Sycon’s body (Voigt et al., 2014). In this zone, diactine spicules, one-rayed spicules with two pointed tips, are arranged in a palisade-like manner and continuously grow around the osculum opening. Simultaneously, new triactines, three-rayed spicules resembling a Mercedes star, and four-rayed tetractines form in the atrial skeleton. Large amounts of triactines and distal diactine bundles are also produced within newly developing radial tubes (Figure 1B).

![Figure 1.](https://cdn.elifesciences.org/articles/106239/elife-106239-fig1-v1.jpg)

**Figure 1.:** (A) The S. ciliatum skeleton features specific spicule types in distinct body regions: parallel diactines in the oscular region (upper inset), radial tubes supported by triactines and tufted with diactines (lower inset), and the atrial skeleton composed of triactines and tetractines. (B) The upper oscular region shows increased spicule formation (calcein staining) in the growing zone of new radial tubes and around the osculum, where oscular diactines are predominantly produced (modified from Voigt et al., 2014). Scale bars: 0.5 mm. (C) Spicules are formed by sclerocytes, specialized cells controlling spicule formation. Diactine formation involves two sclerocytes, triactine formation six (f=founder cell, t=thickener cell).

### DGE analysis

We performed a DGE analysis comparing gene expression of the apical oscular region to the inner and outer body walls of the more basal body regions in five specimens (Appendix 1—table 1). We observed 1575 differentially expressed genes (log2-fold change ≥2, padj<0.01). Of these genes, 829 were overexpressed in the oscular region, including the known biomineralization genes with documented sclerocyte-specific expression: CA1, CA2, AE-like1, AE-like2, Diactinin, Triactinin, Spiculin (Voigt et al., 2017; Voigt et al., 2014).

To gain further insight into these genes’ potential function, we performed a GO-term enrichment analysis, considering the GO-term annotation of the closest hit in Uniprot against each transcript as a potential annotation for the S. ciliatum genes. The genes overexpressed in the oscular regions were enriched in biological process GO-terms relevant for biomineralization (e.g. with the representative terms GO:0001501 ‘skeletal system development’, GO:0001503: ‘ossification’, GO:0030282 ‘bone mineralization’, Supplementary file 1). Among them were genes similar to Fibrilin-1, Collagen alpha-1 (XXVIII) chain B, Collagen alpha-1 (I) chain, Collagen alpha-1 (XI) chain, V-type proton ATPase subunit a, and to Fibroblast growth factor receptor 2. Additionally, the S. ciliatum-specific growth factor SciTgfBH, with similarity to bone morphogenetic protein 2, and the homeobox protein SciMsx, with similarity to the homeobox protein MSX-2, belong to genes with these enriched GO terms. Other enriched GO terms related to ongoing morphogenesis, cell differentiation, cell signaling, cell migration, and organization of the organic matrix are all indicative of the growth zone that the oscular region represents (Supplementary file 1). Noteworthy among them are genes of the Wnt pathway (SciWntG, I, J, K, L, M, O, U, SciFzdD, and Metalloprotease TIKI homolog).

Fourteen secreted proteins, with significantly higher expression in the oscular region, showed similarity to the coral skeletal organic matrix proteins galaxin and galaxin-like proteins, first described from the coral Galaxea fascicularis (Fukuda et al., 2003; Watanabe et al., 2003). In total, 17 proteins similar to galaxins were identified from the predicted proteins of the S. ciliatum genome using BLASTp. We refer to these as calcarin 1–17 (Cal1–Cal17) to discriminate them from galaxin and galaxin-like proteins of scleractinian corals. The presence of signal peptides indicates that calcarins are secreted. Except for a Reeler domain (Pfam PF02014) in Cal16, calcarins lack recognizable domains. Like galaxins, calcarins contain regions with 10–23 di-cysteine residues, typically separated by 10–15 amino acids. Additionally, a single cysteine occurs approximately at the inter-di-cysteine distance upstream and downstream of the di-cysteine region. Monomer AlphaFold predictions propose that disulfide bridges between these cysteines provide a tertiary structure typical of calcarins and galaxins (Figure 2; Figure 2—figure supplement 1). The di-cysteines form the N-terminal part of a common four-amino acid beta-hairpin with a short, often two-amino acid long turn. The first cysteine of a di-cysteine connects with the second cysteine of the preceding beta-hairpin by a disulfide bridge, linking the beta-hairpins together. This disulfide bridge backbone is continuous in galaxins, whereas the predictions in calcarins may show one or two interruptions.

![Figure 2.](https://cdn.elifesciences.org/articles/106239/elife-106239-fig2-v1.jpg)

**Figure 2.:** (A) Structural similarities in AlphaFold predictions of galaxins (A. millepora) and selected calcarins (S. ciliatum). (B) Beta-hairpins in Cal7 connected by disulfide bridges of di-cysteines. (C) Number of calcarins, galaxin-like, and galaxins transcripts in sponges and corals, assigned to orthogroups. Additional AlphaFold structure predictions of selected S. ciliatum calcarins and coral galaxin-like proteins are provided in Figure 2—figure supplements 1 and 2.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/106239/elife-106239-fig2-figsupp1-v1.jpg)

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/106239/elife-106239-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Two octocoral galaxin-like proteins exhibit the same number of beta-hairpins as S. ciliatum calcarins Cal2, Cal4, and Cal6 (top left). In contrast, stony coral galaxin-like proteins belonging to the same orthogroups as S. ciliatum Cal12 or Cal14 display considerably more beta-hairpins than their calcareous sponge counterparts (top right, bottom). Notably, the galaxin-like proteins shown here were not detected in the skeletal matrix proteomes of the respective cnidarian species.

### Temporal and spatial expression of calcarins

The expression of Cal1 to Cal8 was investigated using chromogenic in situ hybridization (CISH) and hairpin chain reaction fluorescence in situ hybridization (HCR-FISH), confirming their presence in sclerocytes (Figure 3). Additionally, antisense probes were used against the mRNA of Spiculin, an acidic protein specific to all thickener cells, Triactinin, a marker for triactine and tetractine thickener cells, and the sclerocyte-specific carbonic anhydrase SciCA1 (Voigt et al., 2017; Voigt et al., 2014). This approach enabled us to visualize and contextualize calcarin-positive cells (Figure 3—figure supplement 1). The expression patterns of calcarins varied with sclerocyte type and spicule formation stage.

![Figure 3.](https://cdn.elifesciences.org/articles/106239/elife-106239-fig3-v1.jpg)

**Figure 3.:** Insets indicate the location of the depicted view within the sponge body, where applicable. To improve accessibility for individuals with red/green color vision deficiency, original RGB channel colors (Figure 3—figure supplement 3) were modified to a cyan/magenta/blue color scheme. AF: autofluorescence; osc = osculum; rt: radial tubes; Spic: Spiculin (A–D) Cal1, Cal2, and Spiculin expression in a regenerated S. ciliatum at the asconoid juvenile stage. Scale bars = 50 µm. (A) Overview of the entire specimen, highlighting distinct gene expression with minimal co-expression in the apical half of the sponge. Arrow points to the ring of founder and thickener cells that form the oscular diactines. (B) Detailed view on the expression around the oscular region; Spiculin in thickener cells (apical), Cal2 in diactine founder cells (basal), and Cal1 in triactine/tetractine founder cells (f). (C) Sponge wall detail; Cal2 in diactine founder cells, Spiculin in thickener cells (arrow: one diactine thickener cell). (D) Triactine/tetractine founder cells expressing Cal1, thickener cells expressing Spiculin. (E) Cal1 expression in founder cells ceases as they transform into thickener cells, and Spiculin expression sets in. Cal1 continues to be expressed in actine-producing founder cells in triactines, but in the diactine actine-forming founder cell, it is replaced by Cal 2 expression in later stages. Scale bars; 10 µm. (F) Expression of Cal3 in founder cells and Spiculin in thickener cells attached to the preserved diactine (di) and triactine (tri) spicules (overlay with light microscopic image). Note how thickener cells thinly ensheath the spicule. Scale bar: 50 µm. (G) Cal7 expression in the founder cells of oscular diactines. Co-expression of Spiculin and Cal7 rarely occurs in transient stages of emerging thickener cells. Scale bar: 50 µm. (H) Early triactine stage with six founder cells expressing Cal7. Scale bar: 50 µm. (I) In later triactine formation stages, thickener cells no longer express Cal7. Scale bar: 50 µm. (J) Expression of Cal4 and Cal5 in thickener cells. Scale bar: 50 µm. (K) Cal6 and Spiculin expression in oscular region (osc: oscular opening) and expression at the distal end of radial tubes (rt) of the body wall. Scale bars = 100 µm, inset 20 µm. (L) Expression of Cal8 in founder cells and Spiculin in thickener cells of diactines at the end of radial tubes (left) and of a triactine (right).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/106239/elife-106239-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Overview of fluorescent signals in radial tubes. Inset in the top left shows bright-field view for orientation. Dotted boxes indicate the position of details in B–E. (B–E) Details with superimposed sketches to show the original position of dissolved spicules. Triactinin and Spiculin are co-expressed in thickener cells of triactines (B and C). Spiculin additionally occurs in thickener cells of diactines at the distal end of radial tubes (e.g. arrows in A). Cal1 is expressed in founder cells of both spicule types (B–E). Co-expression of Cal1 and Spiculin marks the transition stage from founder to thickener cell (arrows in D and E). Many Spiculin signals at the distal end of radial tubes are not associated with a Cal1 signal, suggesting that Cal1 expression in diactine founder cells ceases before spicule formation is complete (A). In contrast, Cal1 signal is detected in founder cells of late triactine stages (C). Cal1=Calcarin1, Tria = Triactinin, Spic = Spiculin, rt = radial tube. Scale bar: 100 µm. Images processed with large volume computational image clearing (LVCC).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/106239/elife-106239-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (A) The radial tube’s distal end shows Cal2 expression in spherical sclerocytes closely associated with the choanoderm. Inset: View that shows the position of Cal2-expressing cells at the basal surface of the choanoderm inside the mesohyl (images processed with large volume computational image clearing [LVCC], channel colors changed to cyan/magenta/yellow as described in Appendix 1). (B–D) Similar expression patterns of Cal2 and Cal6 in distal radial tubes. (E) Expression of Cal6 and Spiculin around the oscular opening. (F) Atrial wall (no diactines) of the same individual lacks Cal6-expressing cells associated with triactine and tetractine thickener cells. AF: autofluorescence detected with the Leica TXR filter (approx. 590–650 nm), included to help distinguish true signal from background autofluorescence observed in the FITC channel (used for Spiculin detection). Cal: calcarin, choa: choanocytes, mes: mesohyl, pin: pinacocyte, rt = radial tube, Spic: Spiculin. Scale bars: 50 µm (A), 20 µm (B–D), 100 µm (E–F).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/106239/elife-106239-fig3-figsupp3-v1.jpg)

Cal1 is predominantly observed in the founder cells of triactines and tetractines and only minimal overlap with Cal2 expression (Figure 3A–D). Initially expressed in all six founder cells, expression ceases in the central sclerocytes after they transform into thickener cells. The Cal1 signal persists in the remaining founder cells at the tips of the growing spicules (Figure 3D and E). In the founder cells of the diactines, Cal1 is only expressed transiently, as is evident by the lack of Cal1 signal in most oscular diactine founder cells (Figure 3A and B). Occasionally, we observed co-expression of Spiculin and Cal1 in diactine sclerocytes, presumably during the onset of the conversion of a diactine founder cell to a thickener cell (Figure 3E). At slightly later stages (recognizable by the elongated cell shape), Cal1 is no longer expressed in the thickener cells. At even later stages, Cal1 expression also ceases in the founder cells of the diactines, which instead express Cal2 (Figure 3E, Figure 3—figure supplement 1). The expression of Cal2 and Spiculin can be recognized in two superimposed rings of cells around the osculum, representing the founder cells and the associated thickener cells of the oscular diactines (Figure 3B).

Cal3, Cal7, and Cal8 are produced by all founder cells, regardless of the type of spicule they form (Figure 3F–I and L). During the transformation into thickener cells, the expression of these calcarins ceases and is replaced by the expression of Spiculin. Again, co-expression of some of these calcarins with Spiculin was observed in a few cells, probably in sclerocytes transitioning from founder to thickener cells (Figure 3G). Cal4 is expressed in thickener cells, Cal5 only in thickener cells of triactines, like Spiculin and Triactinin, respectively (Figure 3J). Cal6 expression mirrors that of Cal2, occurring in rounded cells at the distal tip of radial tubes and in a ring of cells around the oscular ring (Figure 3K). In these regions, Spiculin-expressing cells are spatially associated. In regions without diactines, like the atrial cavity, no Cal6 expression occurs, even if Spiculin expression indicates ongoing production of triactines and tetractines (Figure 3—figure supplement 2). Like Cal2, Cal6 must be expressed by later-stage diactine founder cells, which appear more spherical than elongated. At the end of radial tubes, Cal2 and Cal6 positive founder cells are in contact with choanocytes (Figure 3—figure supplement 2A). In summary, calcarin expression in sclerocytes varies across spicule formation stages and between sclerocytes of different spicule types (Figure 4), adding further complexity to the spatiotemporal expression of biomineralization genes that was reported before (Voigt et al., 2017). Notably, in young coral polyps, normalized and scaled expression data of the raw cell counts of 980 calicoblastic cells indicate nonoverlapping expression of two galaxin-like proteins, an uncharacterized skeletal matrix protein and a skeletal-aspartic acid-rich protein (Appendix 2—figure 1), suggesting spatiotemporal expression changes of skeletal matrix proteins also occur in calicoblastic cells of corals.

![Figure 4.](https://cdn.elifesciences.org/articles/106239/elife-106239-fig4-v1.jpg)

**Figure 4.:** In initial spicule formation stages, all sclerocytes act as founder cells. Genes with expression patterns described previously (Voigt et al., 2017; Voigt et al., 2014) are shown in gray.

### Calcarins and other proteins are embedded in the spicule matrix

We extracted spicules from the tissue using sodium hypochlorite to examine the proteins incorporated in the biomineral. The spicules were then washed with water and dissolved in acetic acid. Mass spectrometry was employed to analyze the acid-insoluble proteins, while the acid-soluble ones were too diluted for adequate examination. With the obtained spectra, we identified 35 proteins (1.0% FDR protein threshold, with at least two peptides per protein, Supplementary file 2). Fifteen of these proteins are encoded by overexpressed transcripts in the oscular region (Figure 5A; Supplementary file 2). We consider these proteins to be specialized biomineralization proteins. Several calcarins expressed in founder cells (Cal1, Cal2, Cal3, Cal7, Cal8) were most prominent. Additional calcarins of the skeletal matrix were Cal9, Cal11, and Cal10, although the latter was only supported by one peptide.

![Figure 5.](https://cdn.elifesciences.org/articles/106239/elife-106239-fig5-v1.jpg)

**Figure 5.:** (A) Osculum region vs sponge wall. (B) Changes in relative expression during whole-body regeneration. Scale bars: 100 µm.

In addition, we found three secreted proteins without any domain or other prominent features other than a signal peptide, which we refer to as skeletal matrix proteins 1–3 (SMP 1–3). Other spicule matrix proteins contain recognizable domains. Two proteins, similar to cysteine-rich secretory protein LCCL domain-containing 2-like (CAH0893205) and peptidase inhibitor 15-like protein (CAH0891878), both belong to the CAP superfamily. Further, we detected a fibronectin III-domain-containing protein (CAH0869470), a subtilisin-like protease (CAH0797261), and an EGF-like domain-containing protein (CAH0821874). Both the LCCL domain-containing 2-like protein and the fibronectin III-domain-containing protein are acidic with isoelectric points of 4.34 and 4.75, respectively. Thickener cell-specific proteins, such as Cal4, Cal5, or the Asx-rich proteins Triactinin and Spiculin, were not observed in the spicule matrix.

When comparing the 15 spicule matrix proteins of Sycon to the skeletal matrix proteins of a Vaceletia sp. (Germer et al., 2015), a demosponge with a calcium carbonate (aragonite) basal skeleton, their similarity is limited to subtilisin-like proteases found in both proteomes. Additional similarity can be seen only in eight additional proteins of presumably intracellular origin (annotated as or containing domains of Histones, Actin, Tubulin, Elongation factor 1a, mitochondrial ATP synthase alpha, Supplementary file 3), which were not overexpressed in the oscular region of S. ciliatum. These proteins may represent ubiquitous extracellular matrix components or, particularly in the case of proteins with intracellular origins, could result from contamination by residual cellular material or their incorporation into the forming biomineral, as suggested before (Ramos-Silva et al., 2013; Germer et al., 2015), and we do not consider them to have specific function in biomineralization.

### Expression of biomineralization genes during whole-body regeneration

Dissociated cells of S. ciliatum form spherical cell aggregations that differentiate into small functional sponges within 16–18 days. This regeneration resembles the post-larval development in S. ciliatum after the first days (Soubigou et al., 2020). The first stages are free of spicules, and the first diactines appear 3–4 days after reaggregation. Spicule production, including triactines and tetractines, increases in the following days. After about 16 days, an osculum is formed and framed by diactines. Reanalyzing raw RNA-seq data covering the complete regeneration process (Appendix 1—table 2; Soubigou et al., 2020), we find downregulated expression of calcarins 1–13, the other spicule-matrix proteins, and previously identified sclerocyte-specific genes (Voigt et al., 2017; Voigt et al., 2014) in regeneration stages with no or on-setting spicule formation (days 1–4) compared to later stages (days 6–18) with higher numbers of newly forming spicules (Figure 5B). Noteworthy, dissociated cells (day 0) also have low expression of these sclerocyte-specific genes, suggesting that most sclerocytes do not survive the cell-dissociation process.

### The majority of calcareous sponge biomineralization genes show concerted changes in expression in different biological settings

We performed a weighted gene co-expression network analysis (WGCNA) of the body part and regeneration datasets to identify co-expression modules representing groups of genes displaying concerted expression patterns. The analysis provided eight meta-modules, of which four showed significant changes in expression module eigengenes—summary profiles that capture the overall expression pattern of each module—between samples with high spicule formation context (osculum region and regeneration stages older than 4 days) and samples with low spicule formation (sponge wall and early regeneration stages until days 3–4) (Appendix 2—figure 2). One meta-module ‘midnightblue’ showed higher module eigengene expressions in the context of higher spicule formation. The module includes 196 genes, all differentially expressed in the body part dataset. Of these, 189 genes were overexpressed in the oscular region, including the suggested biomineralization genes, except for Cal6, Cal9, Cal13, and SMP2. Only seven genes in this meta-module are underexpressed in the oscular region. Some enriched biological process GO terms of genes in this meta-module could be relevant in the context of spicule formation, e.g., monoatomic anion transport, cell junction organization and assembly, and cell-to-cell signaling (Appendix 2—figure 3). Eight proteins in the meta module ‘midnightblue’ are involved in the regulation of transcription (GO:0006355), including SciMsx and other transcription factors. The meta module also contains five genes annotated as similar to Integrin alpha 8 or Paxillin from the transforming growth factor beta signaling pathway (GO:0007179), and three genes annotated to belong to the Wnt signaling pathway (GO:0016055), namely SciFzdD, SciDvlB, and SciWntI (Supplementary file 4).

### Calcarins and related galaxin-like proteins in other species

To identify potential homologs of calcarins in a range of other species, we employed OrthoFinder to analyze transcriptomes from calcareous sponges, other sponge classes, octocorals, and stony corals (Appendix 1—table 3). This analysis segregated 14 S. ciliatum calcarins into distinct orthogroups while grouping Cal2, Cal4, and Cal6 in a single orthogroup. Calcarins in each orthogroup were found in the transcriptomes of other calcareous sponges, either exclusively in Calcaronea (Cal3, Cal5, Cal13, Cal15, and Cal17) or in both Calcaronea and Calcinea (Supplementary file 5). Within the same orthogroup, Cal2, Cal4, and Cal6 exhibited sequence identities of 25–36% among themselves, while each showed a higher match in Grantia compressa, with identities ranging from 44% to 58%.

Two orthogroups, one containing Cal2, Cal4, Cal6, and the other Cal15, also included galaxin-like sequences from octocorals. Orthogroups containing Cal12 and Cal14 include sequences from the genome of the scleractinian coral Stylophora pistillata, but not from Acropora millepora. Despite their presence in the same orthogroups, the octocoral and stony coral proteins were only distantly related to the calcareous sponge calcarins (e.g. 12–24% identity between octocoral and calcareous sequences in orthogroup Cal 2-4-6), resulting in poor sequence alignment. AlphaFold predictions suggest that the galaxin-like proteins from the octocorals Heliopora coerulea and Tubipora muscia share a similar structure with Cal2, 4, and 6, each featuring 12 beta-hairpins (Figure 2—figure supplement 2). In contrast, galaxin-like proteins from Stylophora exhibit a substantially higher number of beta-hairpins than the S. ciliatum calcarins that are part of the same orthogroup (Figure 2—figure supplement 2). Furthermore, none of these scleractinian and octocoral proteins included in the calcarins orthogroup have been directly linked to biomineralization: they were not detected in these species’ skeletons (Conci et al., 2020, Peled et al., 2020) nor have their expression patterns been characterized. Their homology to calcarins, therefore, remains to be determined. Finally, no other sponge proteins grouped with the 17 identified calcarins from S. ciliatum, although a few galaxin-like sequences were detectable using BLASTp (Supplementary file 6)—precisely one in Homoscleromorpha, one in each Hexactinellida species, and four in the transcriptome, but not the skeletal proteome (Germer et al., 2015), of the demosponge Vaceletia sp. While the galaxin-like transcripts of Vaceletia are short and incomplete, the hexactinellid and homoscleromorph proteins are complete and are large proteins of about 5000 amino acids. A signal peptide suggests that they, too, are secreted. In contrast to calcarins or galaxins, they contain multiple recognizable domains, such as several fibronectin type III and laminin EGF domains. Only about 200 amino acids of these proteins are made from the di-cysteine-containing region of the Galaxin BLASTp hit, which lies between fibronectin type III domains (Appendix 2—figure 4). The demosponges Ephydatia muelleri and Tethya wilhelma lack galaxin-like sequences in their genomes.

Galaxins and galaxin-like proteins are attributed to a PANTHER ‘family’ PTHR34490, and in InterPro (https://www.ebi.ac.uk/interpro/), 623 proteins are currently annotated to this family (with 381 available AlphaFold structures, see Supplementary file 6). They occur in several animal phyla, but also other eukaryotes and archaeans. Species without skeletons, such as the cnidarians Hydra, Actinia, Exaiptasia, and Nematostella, also possess galaxin-like proteins assigned to the PANTHER ‘family’ PTHR34490 (Supplementary file 6).

### Sequential order and expression of biomineralization genes

In the S. ciliatum genome, the 17 calcarins occur on chromosomes 1, 2, 4, 7, and 13. On chromosome 2, Cal12, Cal4, Cal6, and Cal2 are positioned sequentially (Figure 6 and Supplementary file 7). Cal4, Cal6, and Cal2 belong to a single orthogroup, indicating their homology. Cal4 is expressed in thickener cells, while Cal2 and Cal6 have identical expression patterns, suggesting they are produced by diactine founder cells during the late diactine formation stage (see above). Cal12 has low expression levels, and we did not locate its expression. The founder cell-specific carbonic anhydrase gene CA2 is situated on the reverse strand of chromosome 4, flanked by CA8 and CA3 on the forward strand. Upstream on the same chromosome, other membrane-bound carbonic anhydrases (Voigt et al., 2021) are present, including CA4, CA5, CA6, and CA7.

![Figure 6.](https://cdn.elifesciences.org/articles/106239/elife-106239-fig6-v1.jpg)

**Figure 6.:** *Predicted nested genes not shown. (A) Calcarins (Cal) in S. ciliatum. (B) Galaxin (Glx) and Galaxin-like (Glx-l) proteins in the stony coral A. millepora. (C) Membrane-bound carbonic anhydrases (CA) in S. ciliatum.

In the coral A. millepora, Galaxin1 and Galaxin2 are located subsequently on the genome, making a past gene duplication likely as well. The galaxin-like proteins 1 and 3 also occur in subsequent pairs or triplets. The genes for galaxin-like 2, 1, and 5, as well as galaxin-like 3 and 4, are separated by a maximum of two short predicted genes (Figure 6).

## Discussion

### Calcarins are galaxin-like biomineralization proteins

Our study significantly expanded the known non-bilaterian biomineralization genes and found that galaxin-like calcarins are key components of the calcareous sponge biomineralization machinery. Most calcarins could be linked to biomineralization by their higher expression levels in body parts or regeneration stages with increased spicule formation, sclerocyte-specific expression, presence in the extracted spicule matrix, or a combination of these. Additionally, they change their expression in concert with other previously characterized biomineralization genes.

In stony corals and octocorals, certain galaxins and galaxin-like proteins are part of the coral skeletal organic matrix (Fukuda et al., 2003; Watanabe et al., 2003) or expressed briefly before the onset of biomineralization in the primary polyp (Reyes-Bermudez et al., 2009). Typically, one or two galaxins occur in stony coral (Peled et al., 2020; Ramos-Silva et al., 2013; Takeuchi et al., 2016) or octocoral (Conci et al., 2020; Le Roy et al., 2021) skeletons. In the spicule matrix of S. ciliatum, however, we found seven to eight calcarins, so these galaxin-like matrix proteins are much more diverse in calcareous sponges than in corals.

### Role of calcarins, galaxins, and galaxin-like proteins

The temporal and spatial differences in expression patterns of calcarins suggest specialized functions in controlling the biomineralization process. The observed expression patterns of calcarins show that initially, all sclerocytes involved in the formation of a single spicule are functional founder cells expressing the same repertoire of biomineralization genes (e.g. expression of Cal1 and Cal7, Figure 3E and H). Founder cell-specific calcarins are integrated into the spicule matrix, much like galaxins and galaxin-like proteins are in coral skeletons. In corals, galaxins and galaxin-like proteins may provide either a structural framework for the growing biomineral or might influence the nucleation and growth of the carbonate crystals (Fukuda et al., 2003; Watanabe et al., 2003), although their function is not fully understood. We assume similar roles for the calcarins we identified from the spicule matrix. A recent study has shown that calcareous sponge spicules grow by addition of calcium carbonate granules that form near the membranes of active sclerocytes (Wendt et al., 2025). Secreted calcarins may play a role in the formation of these granules and are likely among the previously unidentified intercalated proteins that were supposed to influence crystal growth in calcareous sponges by selectively inhibiting growth in specific directions (Aizenberg et al., 1996). We hypothesize that differences in calcarin composition in different spicule types influence their specific crystallographic features and possibly their macromorphology (Aizenberg et al., 1995; Aizenberg et al., 1994).

Our results suggest thickener cells emerge from founder cells by changing gene expression, including calcarins. Thickener cell-specific calcarins and acidic proteins are not found in the spicule matrix, implying that S. ciliatum thickener cells do not add significant calcite material to the spicule. Instead, biomineralization genes secreted by thickener cells (Cal4, Cal5, acidic proteins Triactinin and Spiculin) may affect only the spicule’s surface. For instance, spicules in one Calcinea species have a calcitic core surrounded by amorphous calcium carbonate cored again by a thin calcitic sheath (Aizenberg et al., 2003). Here, acidic proteins and calcarins might be involved in transforming amorphous calcium carbonate to calcite, but due to the thin nature of the sheath, they are more likely to be lost (due to dissolution during clean-up) or remain below the detection threshold.

### The calcareous sponge biomineralization toolkit resembles that of corals

Our widened understanding of the calcareous sponge biomineralization machinery revealed that the identified effector genes are distinct from those reported from other sponges. This is not surprising because even the formation of siliceous spicules in the classes Demospongiae and Hexactinellida shows little overlap (Francis et al., 2023; Shimizu et al., 2024), which indicates that the formation of spicules in these three extant sponge groups evolved independently. Based on our data, we can also exclude that there are major genetic similarities between the formation of calcite spicules of calcareous sponges and the aragonitic basal skeletons of some demosponges, called sclerosponges. Only specific subtilisin-like protease and carbonic anhydrases are shared in the biomineralization machinery of the sclerosponge Vaceletia and the calcarean S. ciliatum. Both belong to larger gene families, and phylogenetic analyses of carbonic anhydrases suggest that they were independently recruited for biomineralization in calcareous sponges and carbonate-producing demosponges (Voigt et al., 2021; Voigt et al., 2014). Spherulin, a skeletal protein of aragonitic sclerosponges (Germer et al., 2015; Jackson et al., 2011), is not present in the calcareous sponge genome. Although we identified galaxin-like sequences in Vaceletia’s transcriptome, the proteins are not reported from its skeleton (Germer et al., 2015). In contrast, the galaxin-like calcarins are diverse in calcareous sponges and their spicules.

Considering these genetic differences in sponge biomineralization between taxa that secrete aragonite (Astrosclera, Vaceletia) and calcite (Sycon), it is unexpected that the essential biomineralization effector genes of calcareous sponges that produce calcite resemble those utilized by aragonitic stony corals, suggesting parallel evolution in gene recruitment between these calcifying organisms. The gene families involved are key parts of the pre-adapted carbonate ‘biomineralization toolkit’ of their common ancestor, including essential pH regulators and for the directional transport of inorganic carbon, i.e., specialized carbonic anhydrases (Bertucci et al., 2013; Voigt et al., 2014) and bicarbonate transporters (Voigt et al., 2017; Zoccola et al., 2015; Appendix 2—figure 5). Galaxin and galaxin-like proteins from corals and calcarins from calcareous sponges extend the set of similar biomineralization genes.

### Possible origin of galaxins, galaxin-like proteins, and calcarins

The high sequence divergence within calcarins, galaxin, and galaxin-like proteins makes a resolved phylogenetic analysis of all these genes impossible. The likeliest origin of these biomineralization proteins is the recruitment of secreted di-cysteine-rich proteins with other functions and probably different origins. The characteristic feature of these proteins is the more or less evenly distributed di-cysteines, which, according to the AlphaFold prediction, establish a similar tertiary structure with beta-hairpins connected via disulfide bridges. Secreted proteins with this structure are not limited to calcifying organisms and can be portions of larger proteins. For example, in hexactinellid and homoscleromorph sponges, the few proteins similar to calcarins are large and contain numerous functional domains, while the typical di-cysteine region only resembles a small proportion of the protein. Clearly, then, galaxin-like proteins in non-calcifying organisms have other functions.

Although our results clearly show that some calcarins have a common origin, it is unclear whether galaxin-like proteins generally have common or multiple convergent origins. For example, the di-cysteine regions of galaxin and galaxin-like proteins of the Scleractinia consist of more or less conserved repeat motifs of different lengths (Fukuda et al., 2003; Reyes-Bermudez et al., 2009). These galaxin-like proteins may result from repeated duplication of an original motif, gradually extending the di-cysteine region. In contrast to the galaxin-like proteins of corals, the calcareous sponge calcarins do not show such detailed repeat structures, which could indicate a different origin.

### Gene duplication gave rise to and diversified biomineralization genes in calcareous sponges and corals

Our results provide evidence about the origin and diversification of biomineralization genes. The similarity and sequential arrangement of Cal4, Cal6, and Cal2 on chromosome 2 in the S. ciliatum genome suggest that these genes originated from two successive gene duplications. Their different expression patterns reveal that a functional change must have occurred after the gene duplication. Accordingly, the first duplication event produced two copies, leading to one gene specialized for thickener cells and another for late diactine founder cells. Subsequently, the latter gene duplicated again, resulting in the origin of Cal2 and Cal6, which, despite beginning to diverge in sequence, maintain identical expression patterns. This sequence of events highlights the role of gene duplication in the functional diversification of calcarin genes in S. ciliatum.

Similar observations for galaxins and galaxin-like genes of the stony coral A. millepora suggest that gene duplication is a typical pattern in galaxins and galaxin-like proteins. Galaxin1 and Galaxin2 also occur adjacently in the coral’s genome, indicating past gene duplication. The clustering of galaxin-like proteins in pairs or triplets and the separation of genes for Galaxin-like2, 4, and 5, as well as Galaxin-like3 and 4, by a maximum of two short predicted genes, may also be evident for their origin by past duplication events. The fact that one of the S. ciliatum sclerocyte-specific carbonic anhydrases, SciCA2, is likewise located on the reverse strand of chromosome 4 and flanked by two non-biomineralizing carbonic anhydrases (SciCA8 and SciCA3) (Voigt et al., 2014) encoded on the forward strand provides additional support that gene duplication followed by a neofunctionalization of SciCA2 is the origin of this biomineralization gene. A similar process, tandem gene duplication, neofunctionalization, and inversion, gave rise to the coral-specific biomineralization-specific bicarbonate transporter SLC4γ (Tinoco et al., 2023). Our data show that similar genes in both lineages were independently duplicated, and one copy was recruited in the biomineralization machinery by a functional shift and expression in calcifying cells. The example of the three calcarins provides evidence of how the biomineralization process can evolve to become more and more fine-tuned by further gene duplications and subfunctionalization, e.g., in our case, becoming specific for a distinct spicule type.

### Gene regulatory networks

While our study identified biomineralization genes at the effector level, more research is required to understand the underlying gene regulatory networks, e.g., what triggers the expression changes in some of the spicule’s sclerocytes to change from functioning as a founder cell to a thickener cell. The genes that change expression in meta-module midnightblue might include some key players, as they are enriched in some regulatory biological process GO terms (Appendix 2—figure 3). Cell-cell signaling between the cooperating sclerocytes could play a critical role in controlling the temporal change in gene expression, and several apically overexpressed genes reported here may be involved, such as components of the Wnt or BMP signaling pathways, involved in mammal bone morphogenesis and homeostasis (Sánchez-Duffhues et al., 2015; Zhong et al., 2014). However, what these are and how the control mechanisms do function must be investigated in further studies because, in both biological scenarios, apical gene expression or regeneration, additional growth and differentiation processes run parallel to spicule formation, which we cannot differentiate from each other with the methods used here.

### Conclusion

We have identified calcarins, galaxin-like proteins, as novel components of the biomineralization toolkit in calcareous sponges. The diversity of calcarins in the calcitic sponge spicules, compared to galaxin and galaxin-like proteins in aragonitic coral skeletons, underscores their specialized roles in biomineralization. Their varied spatial and temporal expression patterns highlight the precise genetic regulation involved in calcification in this class of sponges. Our results show that similar genes or genes from the same families surprisingly are involved in biomineralization in both calcareous sponges and corals that produce different calcium carbonate polymorphs, calcite vs aragonite, respectively. This demonstrates that there are parallels between the formation of calcareous sponge spicules and coral skeleton formation at the proteome level. Furthermore, our results highlight how gene duplication and neofunctionalization of an original gene pool gave rise to dedicated biomineralization genes that could further differentiate to refine the biological control of the process. Single-cell expression data of calicoblastic cells in corals indicates that coral biomineralization may equally depend on small-scale spatial and temporal expression changes to fine-tune calcification, an aspect that requires further study and could help predict the responses of these reef-builders to global environmental changes.

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
      <td>Gene (Sycon ciliatum)</td>
      <td>Calcarin 1–17 (Cal1–17)</td>
      <td>This study</td>
      <td></td>
      <td>De novo annotation of GenBank assembly GCA_964019385, available at https://zenodo.org/records/14755899, gene IDs provided in Supplementary file 7</td>
    </tr>
    <tr>
      <td>Gene (Sycon ciliatum)</td>
      <td>SciCarbonic anhydrase 1, Triactinin, Spiculin</td>
      <td>Voigt et al., 2014; Voigt et al., 2017</td>
      <td></td>
      <td>De novo annotation of GenBank assembly GCA_964019385, available at https://zenodo.org/records/14755899, gene IDs provided in Supplementary file 7</td>
    </tr>
    <tr>
      <td>Biological sample (Sycon ciliatum)</td>
      <td>DNA, RNA, tissue for in situ hybridization experiments</td>
      <td>AWI Biologische Anstalt Helgoland, Germany</td>
      <td></td>
      <td>Living specimens were shipped to Munich, Germany</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>PCR primers for generating probes for CISH</td>
      <td>This study</td>
      <td>PCR primers</td>
      <td>Sequences of gene-specific primers for calcarin 1–8 are provided in Appendix 1—table 4</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>HCR-FISH probe sets</td>
      <td>Molecular Instruments</td>
      <td></td>
      <td>Probe sets consist of 20 pairs of probes per gene and were generated for Calcarin 1, Calcarin 2, Calcarin 3, Calcarin 7, Calcarin 8, Triactinin, Spiculin, SciCarbonic, andrase 1 by Molecular Instruments based on the de novo annotation of GenBank assembly GCA_964019385, available at https://zenodo.org/records/14755899, gene IDs provided in Supplementary file 7</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNA-Duet extraction kit</td>
      <td>Zymo Research</td>
      <td>Cat. # D7001</td>
      <td>Extraction of RNA</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNA 6000 Nano Kit</td>
      <td>Agilent</td>
      <td>Cat. # 5067-1511</td>
      <td>RNA extraction quality control</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>SENSE mRNA-Seq Library Prep Kit V2</td>
      <td>Lexogen</td>
      <td>Cat. # 001.24</td>
      <td>Illumina library preparation</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>pCR4-TOPO cloning vector</td>
      <td>Invitrogen</td>
      <td>Cat. # K457502</td>
      <td>Used for probe generation in CISH</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>T3 polymerase</td>
      <td>Promega</td>
      <td>Cat. # P208C</td>
      <td>Used for probe generation in CISH</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>T7 polymerase</td>
      <td>Promega</td>
      <td>Cat. # P207B</td>
      <td>Used for probe generation in CISH</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>DIG RNA Labeling Mix</td>
      <td>Roche</td>
      <td>Cat. # 11277073910</td>
      <td>Used for generating DIG-labeled RNA probes</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Fluorescein RNA Labeling Mix</td>
      <td>Roche</td>
      <td>Cat. # 11685619910</td>
      <td>Used for generating fluorescein-labeled RNA probes</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NuPAGE 4–12% Bis-Tris Gel</td>
      <td>Invitrogen</td>
      <td>–</td>
      <td>Preparation of proteins for mass spectrometry</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>NBT/BCIP Stock Solution</td>
      <td>Roche</td>
      <td>Cat. # 11681451001</td>
      <td>Substrate for CISH</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>FastRed Tablets</td>
      <td>Roche</td>
      <td>Cat. # 11496549001</td>
      <td>Substrate for CISH</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>EverBrite Hardset Mounting Medium</td>
      <td>Biotum</td>
      <td>Cat. # 23004</td>
      <td>Hardset antifade mounting medium with DAPI; used for mounting of tissue sections after HCR-FISH</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Lysyl Endopeptidase (Lys-C), Mass Spectrometry Grade</td>
      <td>FUJIFILM Wako Pure Chemical Corporation, USA</td>
      <td>–</td>
      <td>Used for in-gel digestion of proteins</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Geneious</td>
      <td>Kearse et al., 2012</td>
      <td>RRID:SCR_010519</td>
      <td>Used for mapping trimmed reads to Sycon transcriptome</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Salmon</td>
      <td>Patro et al., 2017</td>
      <td>RRID:SCR_017036, PMID:28263959</td>
      <td>Used for transcript quantification prior to DGE analysis</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq2</td>
      <td>Love et al., 2014</td>
      <td>RRID:SCR_015687, DOI: 10.18 129/B9.bio c.DESeq2</td>
      <td>Version 1.42.1; used for analysis of differential gene expression between body parts and regeneration stages</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>WGCNA</td>
      <td>Langfelder and Horvath, 2008</td>
      <td>RRID:SCR_003302, PMID:19114008</td>
      <td>Version 1.72.5; WGCNA to identify gene modules associated with spicule formation</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>topGO</td>
      <td>Alexa and Rahnenfuhrer, 2023</td>
      <td>RRID:SCR_014798,DOI: 10.18129/B9.bioc.topGO</td>
      <td>Version 2.54.0; GO-term enrichment analysis for genes overexpressed in osculum region and genes included in the ‘midnightblue’ module (WGCNA result)</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>REVIGO</td>
      <td>Supek et al., 2011</td>
      <td>RRID:SCR_005825, PMID:21789182</td>
      <td>Summarizing significantly enriched GO terms from GO analyses</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>TransPi</td>
      <td>Rivera-Vicéns et al., 2022</td>
      <td>PMID:35119207</td>
      <td>Nextflow-based pipeline for transcriptome assembly and annotation; used to reassemble raw reads and predict protein sequences for OrthoFinder analysis</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BLASTp</td>
      <td>Camacho et al., 2009</td>
      <td>RRID:SCR_001010, PMID:20003500</td>
      <td>Used for homology search of galaxin-like proteins</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>OrthoFinder</td>
      <td>Emms and Kelly, 2019</td>
      <td>RRID:SCR_017118, PMID:31727128</td>
      <td>Version 2.5.5; orthogroup identification</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MASCOT</td>
      <td>Matrix Science Limited, UK, Creasy et al., 1999</td>
      <td>RRID:SCR_014322, PMID:10612281</td>
      <td>Version 2.6.2; protein identification from LC-MS/MS spectra</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Scaffold</td>
      <td>Proteome Software Inc, Portland, USA</td>
      <td>Version 5.01</td>
      <td>Available at : https://www.proteomesoftware.com/products/scaffold-5. Used for threshold filtering of identified proteins and visualization</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Seurat</td>
      <td>Hao et al., 2024</td>
      <td>RRID:SCR_016341, DOI: 10.32614/ CRAN.package.Seurat</td>
      <td>Version 5.1.0</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>PepMap RSLC C18</td>
      <td>Thermo Scientific</td>
      <td></td>
      <td>EASY-Spray column</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>PepMap 100 C18</td>
      <td>Thermo Scientific</td>
      <td></td>
      <td>Trap columns</td>
    </tr>
  </tbody>
</table>

### Specimens, regeneration, and RNA-seq of body parts

Specimens of S. ciliatum were obtained from the AWI Biologische Anstalt Helgoland and sent alive to Munich. Here, specimens were transferred to glass Petri dishes and maintained in seawater for a few days with daily seawater changes. To verify the timing of the occurrence of spicules during the regeneration of S. ciliatum, we performed a regeneration experiment of the S. ciliatum as used for the regeneration RNA-seq dataset (Soubigou et al., 2020). We mechanically dissociated sponge cells through a 60 µm strainer, then incubated the cells in filtered seawater at 14°C in Petri dishes, changing the water every 1–2 days. The timing of whole-body regeneration stages and occurrence of spicules aligned with prior studies. After 30 days, the experiment ended, and we fixed some juvenile asconoid sponges for ISH.

For DGE analysis, we dissected three body parts from five living specimens (Figure 1): (1) The oscular region with mainly large diactine and tetractine spicules, (2) inner sponge wall, including the atrial skeleton (tetractines +diactines) and the proximal radial tube (triactines), (3) outer sponge wall, including the distal parts of the radial tube with triactines and tufts of curved diactines.

The body parts were instantly transferred into the lysis buffer of the RNA-Duet extraction kit (Zymo). We extracted RNA according to the manufacturer’s instructions and confirmed its integrity with an Agilent Bioanalyzer using the RNA 6000 Nano Kit. We used the SENSE mRNA-Seq Library Prep Kit V2 for Illumina (Lexogen) to produce sequencing libraries. The 15 libraries were pooled and sequenced on a HiSeq Illumina Sequencer at the Gene Center of LMU. 100 bp paired raw reads were quality-checked with FastQC and trimmed to 92 bp to remove low-quality 3’ bases.

### DGE analysis

Trimmed raw reads (Appendix 1—table 1) were mapped to a high-quality transcriptome of S. ciliatum (Caglar et al., 2021) using Geneious (Kearse et al., 2012). We omitted non-mapping reads to remove commensal sequences common in sponge tissues/samples. The trimmed and filtered reads were submitted to the European Nucleotide Archive (PRJEB78728). Raw reads from a whole-body regeneration experiment (Soubigou et al., 2020) were downloaded from the European Nucleotide Archive and processed identically (see Appendix 1—table 2 for accession numbers). For mapping, we used the S. ciliatum transcriptome published in Caglar et al., 2021. This transcriptome showed better BUSCO (Manni et al., 2021) values than a transcriptome assembled using Trinity and the filtered reads from our experiments and was therefore preferred for mapping prior to DGE analysis with DESeq2 1.42.1 (Love et al., 2014). Gene and transcript counts for each filtered set were obtained with Salmon (Patro et al., 2017) and combined into count matrices for the body parts experiment and the regeneration data. For the body part dataset, we compared gene expression of the apical osculum region with increased spicule formation with gene expression of the more basally located regions of the sponge wall (inner and outer side). In the regeneration dataset, we identified the differentially expressed genes for two regeneration series between the initial spicule-free stages (days 1+2) and the subsequent stages that produce spicules (days 3–24). Differentially expressed genes (|log2-fold change|≥2, padj<0.01) were identified, extracted from the reference transcriptome, and used in subsequent analysis.

### WGCNA

We combined both count datasets, filtered them to exclude low-count genes (genes with less than 10 samples with counts>10), and used them to construct a DESeq2 data set in R, followed by variance stabilizing transformation for normalization. We performed a WGCNA (1.72.5; Langfelder and Horvath, 2012; Langfelder and Horvath, 2008) to identify gene modules associated with spicule formation. For this purpose, a distinction was made between ‘low spicule formation’ for the body wall and the first stages of regeneration with no or only a few first diactines (days 0–4) compared to the other states (high spicule formation). The resulting modules were detected using the dynamic tree cut algorithm, and module eigengenes were calculated. A permutation test (n=1000) was conducted to assess the significance of modules regarding their association with conditions (low vs high spicule formation).

### GO-term enrichment analysis

Best hit proteins with e-values≤e-05 were obtained by running BLASTx of S. ciliatum transcripts (Caglar et al., 2021) against the UniProt database. GO terms for these best hit proteins (e-values≤e-05) were retrieved from QuickGO (http://www.ebi.ac.uk/QuickGO/) using a custom Perl script. Transcript-associated GO terms were compiled by genes and used as input for GO-term enrichment analysis with topGO 2.54.0 (Alexa and Rahnenfuhrer, 2023) in R. This analysis was performed for genes overexpressed in the osculum region and genes included in the ‘midnightblue’ module identified by WGCNA. GO terms with fewer than 10 annotated genes were excluded. For each ontology (Molecular Function, Biological Process, and Cellular Component), gene lists were mapped to GO terms, and enrichment was tested using Fisher’s exact test with the ‘classic’ algorithm. Significantly enriched GO terms (p≤0.05) were summarized using REVIGO (Supek et al., 2011) to provide representative terms. All scripts, input files, and parameters used in the analysis are provided in a GitHub repository.

### OrthoFinder and BLASTp

Raw RNA-seq data of several non-bilaterians was downloaded from SRA and reassembled using the TransPi pipeline (Rivera-Vicéns et al., 2022). The predicted proteins of these assemblies, of genomes and transcriptomes of calcareous sponges, sponges from other classes, octocorals, and stony corals were used as input to OrthoFinder to generate orthogroups (Emms and Kelly, 2019), focusing on species in which biomineralization genes are best studied: A. millepora (Ramos-Silva et al., 2013; Reyes-Bermudez et al., 2009; Takeuchi et al., 2016), S. pistillata (Drake et al., 2013; Peled et al., 2020; Zoccola et al., 2015), three octocoral species (Conci et al., 2020), the calcifying demosponge Vaceletia sp. (Germer et al., 2015), as well as some other high-quality sponge genomes (Francis et al., 2023; Francis et al., 2017; Kenny et al., 2020; Shimizu et al., 2024). Sequences of calcarins from Calcaronea were extracted from orthogroup sequences and aligned using MUSCLE (Edgar, 2004). We used BLASTp (Camacho et al., 2009) with A. millepora Galaxin (D9IQ16) with a maximum e-value of 1e-5 as the threshold to identify proteins similar to galaxins in the proteomes (Supplementary file 6).

### RNA ISH

We conducted RNA ISH to study the spatial and temporal expression of selected genes using standard chromogenic ISH and HCR-FISH. Fixation of specimens and chromogenic ISH followed published procedures (Fortunato et al., 2012). Further details about fixation, probe preparation, and HCR-FISH are provided in the Supplementary Information.

### Identification of spicules organic matrix proteins

Identification and analysis of organic matrix proteins from S. ciliatum spicules involved isolating 6 g of spicules with a solution of sodium hypochlorite, decalcifying them with acetic acid, and separating the acid-soluble and insoluble fractions, of which only the latter provided enough protein to be further analyzed. Proteomic analysis included gel electrophoresis, in-gel digestion, and LC-MS/MS. Proteins were identified using MASCOT (Creasy et al., 1999) with the predicted proteins from the Sycon transcriptome (PRJEB49276), and additional analyses were performed in Scaffold V5.01 (Proteome Software Inc, Portland, OR, USA). Detailed experimental procedures are available in Appendix 1.

### Genome analysis

We accessed the assembly of the S. ciliatum genome (GCA_964019385) of the Tree of Life Programme (https://www.sanger.ac.uk/programme/tree-of-life/, https://www.sanger.ac.uk/collaboration/aquatic-symbiosis-genomics-project/). Because we found the provided gene predictions were incomplete, we performed gene predictions using BRAKER3 installed on a public Galaxy server installation (https://usegalaxy.eu), using a HiSat2 (Kim et al., 2019) mapping of our filtered reads and the peptides from genomic scaffolds (Fortunato et al., 2014) as training data. For the stony corals, we obtained the annotated genomes from GenBank (A. millepora v2.1, GCF_013753865, S. pistillata v1.1, GCF_002571385). The genetic locations of biomineralization genes, additional carbonic anhydrases, and SLC4 transporters were identified using BLASTp. These coordinates were then extracted from the genome’s GFF file.

### Structure predictions of calcarins

AlphaFold express (https://www.line-d.net/alphafold-express) was used to predict the structures of selected calcarins. AlphaFold predictions of A. millepora Galaxin (D9IQ16) and Galaxin 2 (B8UU51) were downloaded from UniProt (Bateman et al., 2021) as pdb files. Model confidence for the structure predictions of the beta-hairpin structure was very high (pLDDT >90) in most cases, but it was generally low or lower for adjacent regions. We visualized predicted structures with the Mol* 3D viewer (Sehnal et al., 2021).

### Inspection of skeletal matrix protein expression in coral calicoblasts

To investigate fine-tuned changes in expression occurring in the coral S. pistillata calicoblasts, we examined publicly available single-cell sequencing datasets (Levy et al., 2021). Using the species’ online cell atlas tool (https://sebe-lab.shinyapps.io/Stylophora_cell_atlas/), we visualized the expression of skeletal matrix proteins (Peled et al., 2020). This analysis revealed specific expression of 14 skeletal matrix proteins in calicoblast metacells of young coral polyps (Appendix 2—figure 1), whereas only very few adult coral calicoblast metacells expressed documented skeletal matrix proteins, indicating no or limited calcification activity (Appendix 2—figure 6). The raw UMI counts (Spis_polyp_sc_UMI_counts.RDS, Spis_adult_sc_UMI_counts.RDS) and the celltype assignments (Spis_polyp_cell_type_assignments.txt, Spis_coral_cell_type_assignments.txt) were downloaded from GitHub (https://github.com/sebepedroslab/Stylophora_single_cell_atlas; Elek, 2025). Single-cell RNA-seq data from cells expressing more than 100 genes were normalized and scaled using the LogNormalize and ScaleData functions of the Seurat R package version 5.1.0 (Hao et al., 2024), respectively, to adjust gene expression counts to 10,000 molecules per cell, and to center and scale each gene to a mean of zero and a variance of one. Normalized and scaled expression data of calicoblasts were visualized as heatmaps using pheatmap version 1.0.12.
