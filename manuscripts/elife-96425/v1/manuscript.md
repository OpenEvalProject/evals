# Chemokine expression profile of an innate granuloma

## Authors

- Megan E Amason<sup>1</sup> ([ORCID: 0009-0000-2834-5834](https://orcid.org/0009-0000-2834-5834))
- Cole J Beatty<sup>1</sup>
- Carissa K Harvest<sup>1</sup>
- Daniel R Saban<sup>1</sup>
- Edward A Miao<sup>1</sup> ([ORCID: 0000-0001-7295-3490](https://orcid.org/0000-0001-7295-3490)) †

### Affiliations

1. Department of Integrative Immunobiology, Duke University School of Medicine Durham United States ([ROR:00py81415](https://ror.org/00py81415))
2. Department of Ophthalmology, Duke University School of Medicine Durham United States ([ROR:00py81415](https://ror.org/00py81415))
3. Department of Molecular Genetics and Microbiology, Duke University School of Medicine Durham United States ([ROR:00py81415](https://ror.org/00py81415))
4. Department of Microbiology and Immunology, University of North Carolina at Chapel Hill Chapel Hill United States ([ROR:0130frc33](https://ror.org/0130frc33))
5. Department of Pathology, Duke University School of Medicine Durham United States ([ROR:00py81415](https://ror.org/00py81415))
6. Department of Cell Biology, Duke University School of Medicine Durham United States ([ROR:00py81415](https://ror.org/00py81415))

† Corresponding author

## Abstract

Granulomas are defined by the presence of organized layers of immune cells that include macrophages. Granulomas are often characterized as a way for the immune system to contain an infection and prevent its dissemination. We recently established a mouse infection model where Chromobacterium violaceum induces the innate immune system to form granulomas in the liver. This response successfully eradicates the bacteria and returns the liver to homeostasis. Here, we sought to characterize the chemokines involved in directing immune cells to form the distinct layers of a granuloma. We use spatial transcriptomics to investigate the spatial and temporal expression of all CC and CXC chemokines and their receptors within this granuloma response. The expression profiles change dynamically over space and time as the granuloma matures and then resolves. To investigate the importance of monocyte-derived macrophages in this immune response, we studied the role of CCR2 during C. violaceum infection. Ccr2–/– mice had negligible numbers of macrophages, but large numbers of neutrophils, in the C. violaceum-infected lesions. In addition, lesions had abnormal architecture resulting in loss of bacterial containment. Without CCR2, bacteria disseminated and the mice succumbed to the infection. This indicates that macrophages are critical to form a successful innate granuloma in response to C. violaceum.

## Introduction

Granulomas are organized aggregates of immune cells defined by the presence of macrophages, with a variety of other features (i.e. necrosis and fibrosis) being more variable (Warren, 1976). The evolved function of the granuloma response is thought to be a protective mechanism by which immune cells sequester a foreign body or pathogen, walling-off the threat (Pagán and Ramakrishnan, 2018). Some pathogens are not successfully eliminated, however, leading to chronic granulomas that persist for months or sometimes even years. New in vivo models are needed to study the complicated mechanisms that coordinate the formation of protective granulomas, in order to understand the events that lead to the successful clearance of pathogens that initiate this response.

We seek to identify environmental pathogens that have immense virulence capacity but are defeated by the innate immune system. Chromobacterium violaceum is one such pathogen that invades host cells and replicates in the intracellular niche, but only causes morbidity and mortality in immunocompromised animals or individuals (Macher, 1982). We discovered that during infection, wildtype (WT) C57BL/6 mice develop necrotic liver granulomas in response to this ubiquitous soil microbe (Harvest et al., 2023; Maltez et al., 2015). As soon as 1 day post-infection (1 DPI), liver microabscesses can be macroscopically visualized. These lesions are composed primarily of neutrophils until approximately 3–5 DPI, when, importantly, monocytes traffic into the area and form a mature granuloma starting at 5 DPI. Once the resulting macrophage zone surrounds the infected lesion, bacterial burdens begin to decrease, suggesting that granuloma macrophages are an important cell type for the clearance of C. violaceum. By 21 DPI, virtually all mice clear the infection and resolve the granuloma pathology, leaving small collagen scars in place of lesions (Harvest et al., 2023). Though we identified neutrophils and macrophages as the key immune players in this model, much remains to be learned about the cellular mechanisms that initiate formation of the granuloma in response to C. violaceum, and what signals instruct immune cells to organize within the granuloma architecture. Indeed, by studying the granuloma response that successfully clears C. violaceum, we hope to identify critical cellular mechanisms that underlie the basic biology of the granuloma response.

Within the granuloma response to C. violaceum, neutrophils and then macrophages migrate and assemble in an organized manner. Cellular movement, or chemotaxis, must be carefully regulated during tissue development, homeostasis, and inflammatory responses (Hughes and Nibbs, 2018). Chemotaxis is controlled by small, secreted proteins called chemokines that signal through transmembrane chemokine receptors. Since their discovery in the 1980s, approximately 50 chemokines are now appreciated for their role in cellular chemotaxis (Zlotnik and Yoshie, 2012). The temporal and spatial expression of chemokines and chemokine receptors dictate cellular trafficking, and dysregulation of these systems is linked to many diseases (Turner et al., 2014).

As more chemokines have been identified, there have been multiple revisions to their nomenclature, and now a systematic naming of chemokines and their receptors is in wide use. Chemokines have conserved cysteine residues, and the current naming system categorizes four subfamilies based on the arrangement of these N-terminal cysteines: CXC, CC, XC, and CX3C (Zlotnik and Yoshie, 2000). Though there are exceptions, most chemokines fit into one of these four subfamilies. Similarly, chemokine receptors fall into four subfamilies based on their chemokine ligand. The naming scheme has become complicated due to promiscuous ligand–receptor interactions, reassigning of mouse and human homologs after syntenic analysis, and divergent evolution of ligands in mice and humans (Nomiyama et al., 2013). Nonetheless, the detailed description of many chemokines and their receptors has been accomplished in both species. Herein, we focus on the mouse chemokines and their role in the C. violaceum-induced murine granuloma.

Inflammatory chemokines are those that are rapidly upregulated in the presence of infection or other inflammatory stimuli (David and Kubes, 2019). Several cell types can upregulate chemokines, creating a gradient of ligand that diffuses away from the point of infection. Still other cell types can respond to this gradient if/when they express the appropriate receptor. Furthermore, activated cells that migrate to the area can also upregulate expression of chemokines, creating a feed-forward loop to enhance cell recruitment. In addition to mediating chemotaxis, chemokines can induce a variety of other cellular responses including proliferation, oxidative burst, and even degranulation (Hughes and Nibbs, 2018). Lastly, it is now appreciated that chemokines also contribute to wound healing and resolution of inflammation, with coordinated efforts between neutrophils and macrophages to clean up debris and halt immune cell infiltration (Soehnlein and Lindbom, 2010).

Here, we use spatial transcriptomics to identify key genes that are upregulated in response to C. violaceum, and assess the importance of CCR2-dependent monocyte trafficking to the site of infection in the liver.

## Results

### Spatial transcriptomics of an innate granuloma

In our initial characterization of the granuloma response to C. violaceum, we used spatial transcriptomics (10x Genomics, Visium Platform) to identify genes that are upregulated at critical timepoints during infection, including 0.5, 1, 3, 5, 7, 10, 14, and 21 DPI (note: we excluded the 7 DPI timepoint from analysis because the granuloma in this capture area was not representative of typical 7 DPI granulomas histologically). A major advantage of this technology is the ability to conserve the spatial location of expression data by overlapping cDNA output with hematoxylin and eosin (H&E)-stained tissue sections (Figure 1A). Each capture area can collect nearly 5000 barcoded spots, each spot being 55 µm in diameter. Though this is not single-cell resolution, the dataset successfully identified 16 unique clusters with differentially expressed genes (Figure 1B), representing cell types (e.g. hepatocytes and endothelial cells), and also representing spatial elements (e.g. necrotic core center, etc.). We further characterized the clusters by assigning appropriate cell types based on each cluster’s gene expression profile and its location within the granuloma (original characterization performed in Harvest et al., 2023, annotation shown in Figure 1B–D). Our previous analysis revealed that the clusters on the left of the UMAP (5: necrotic core center, 11: necrotic core-periphery, 9: coagulative necrosis, 0: macrophage, 8: coagulative necrosis-macrophage1, 6: coagulative necrosis-macrophage2, and 15: outside granuloma) all expressed varying levels of CD45 (Harvest et al., 2023). In contrast, the clusters on the right of the UMAP lacked CD45 but expressed higher levels of albumin. Though these hepatocyte clusters were abundantly present at each timepoint (not shown), the CD45-positive clusters were present to varying degrees. 10 DPI was the most enriched timepoint with all seven non-hepatocyte clusters present (Figure 1C). The sequencing depth varied between clusters, with areas of necrosis displaying relatively lower counts (Figure 1—figure supplement 1A). Cluster 0, which we previously identified as a macrophage-rich cluster, also had relatively lower counts (Figure 1—figure supplement 1A, B). Nevertheless, sufficient reads were obtained to reveal upregulated genes in these clusters, and the sctransform method was used to normalize the data such that biological heterogeneity was highlighted while minimizing technical variation associated with low counts (Hafemeister and Satija, 2019).

![Figure 1.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig1-v1.jpg)

**Figure 1.:** (A) SpatialDimPlots showing hematoxylin and eosin (H&E) and cluster overlay of spatial transcriptomics data corresponding to various days post-infection (DPI). Each circle is an individual barcoded spot that is 55 µm in diameter. (B) UMAP plot of 16 unique clusters identified based on differentially expressed genes during the course of infection. Characterization of predominant cell types and/or location of each cluster (initial characterization performed in Harvest et al., 2023); macrophage zone (M), hepatocyte (HEP), representative HEP (rep HEP), necrotic core center (NC-C), NC-periphery (NC-P), coagulative necrosis (CN), CN-macrophage (CN-M), endothelial cell (EC), outside granuloma (OG). (C) Temporal prevalence of CD45+ clusters, calculated as proportion of spots represented by each cluster within each timepoint. (D) SpatialDimPlot at 10 DPI as in (A), showing cluster overlay and annotated with cluster identity. (E) SpatialFeaturePlot at 10 DPI, showing log-normalized expression of Pf4 (murine homolog of CXCL4). Source code 1. Streamlined code for analysis using RStudio.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) SpatialFeaturePlot displaying raw counts (nCount) per spot at various days post-infection (DPI). Scale set at 0–60,000 reads. (B) Violin plot displaying raw counts (nCount) per cluster across all timepoints. (C) SpatialFeaturePlots displaying normalized gene expression data of CXCR3 ligands (i.e. Cxcl4, Cxcl9, and Cxcl10) at various DPI. Scale set at 0–3.0 expression.

The spatial transcriptomics dataset was rich with candidate genes that could be critical for the successful granuloma response. Specifically, we were interested in the expression of chemokines and chemokine receptors that could be involved in the recruitment of key cell types, namely neutrophils and monocytes, to the site of infection within the liver. Indeed, immune cell trafficking is required for granuloma formation in various infectious and non-infectious models, and chemokines are the obvious candidates for facilitating this chemotaxis (Chensue, 2013).

To investigate various chemokines (Table 1) and chemokine receptors (Table 2), we used the Seurat package in RStudio to analyze gene expression over time and space. We used the SpatialFeaturePlot to assess relative gene expression within the granuloma at each timepoint (Source code 1). For example, Pf4 (the murine homolog of CXCL4) is highly expressed at 10 DPI, corresponding with clusters 0, 6, 9, 11, and 15 (Figure 1E). Though chemokines and chemokine receptors are key facilitators of chemotaxis, other pro-inflammatory molecules such as damage-associated molecular patterns (DAMPs) and pathogen-associated molecular patterns (PAMPs) also direct cells to sites of inflammation. In fact, neutrophils respond to chemotactic molecules in a hierarchical manner, integrating a variety of signals and prioritizing end-target molecules (David and Kubes, 2019; Kolaczkowska and Kubes, 2013). Further demonstrating the complexity of chemotaxis, various adhesion molecules are also required for transmigration of cells out of the blood and into tissues. Indeed, we saw significant upregulation of a number of these genes in this model (Table 3), with many chemokines, chemokine receptors, and adhesion molecules appearing in the top twenty upregulated genes in several clusters (Table 4). Though these chemoattractive and adhesion molecules are likely involved and could be explored in future studies, in this paper we focus on the chemokines and their receptors.

**Table 1.**
 Expression level of chemokine ligands during infection with C. violaceum.Expression was visually ranked as absent, low, medium, or high based on SpatialFeaturePlots. Maximum expression rank recorded here. Table generated from David and Kubes, 2019; Hughes and Nibbs, 2018; Sokol and Luster, 2015; Zlotnik and Yoshie, 2000; Zlotnik and Yoshie, 2012. Lymph node (LN); natural killer cell (NK); NK T cell (NKT); innate lymphoid cell (ILC); dendritic cell (DC).


<table>
  <thead>
    <tr>
      <th>Ligand</th>
      <th>Max expression</th>
      <th>Alias and main functions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cxcl1</td>
      <td>High</td>
      <td>(NAP-3) Neutrophil migration</td>
    </tr>
    <tr>
      <td>Cxcl2</td>
      <td>High</td>
      <td>(MIP-2) (MIP2-α) Neutrophil migration; 90% identical to Cxcl1; involved in wound healing</td>
    </tr>
    <tr>
      <td>Cxcl3</td>
      <td>High</td>
      <td>(MIP2-β) Neutrophil migration; migration and adhesion of monocytes</td>
    </tr>
    <tr>
      <td>Cxcl4</td>
      <td>High</td>
      <td>(Pf4) Neutrophil and monocyte migration; released by platelets; wound repair and coagulation; angiogenesis</td>
    </tr>
    <tr>
      <td>Cxcl5</td>
      <td>High</td>
      <td>(LIX) Neutrophil migration; connective tissue remodeling</td>
    </tr>
    <tr>
      <td>Cxcl9</td>
      <td>High</td>
      <td>Th1, CD8, NK, monocyte migration; closely related to CXCL10 and CXCL11</td>
    </tr>
    <tr>
      <td>Cxcl10</td>
      <td>High</td>
      <td>Th1, CD8, NK, monocyte migration</td>
    </tr>
    <tr>
      <td>Cxcl11</td>
      <td>Absent</td>
      <td>Th1, CD8, NK, monocyte migration</td>
    </tr>
    <tr>
      <td>Cxcl12</td>
      <td>High</td>
      <td>(SDF-1) Lymphocyte migration; bone marrow homing</td>
    </tr>
    <tr>
      <td>Cxcl13</td>
      <td>Low</td>
      <td>B cell migration within follicles of lymphoid tissues; highly expressed in liver, spleen, LN</td>
    </tr>
    <tr>
      <td>Cxcl14</td>
      <td>Low</td>
      <td>Monocyte migration to skin; potent activator of DC</td>
    </tr>
    <tr>
      <td>Cxcl15</td>
      <td>Absent</td>
      <td>Neutrophil migration during inflammation of lungs</td>
    </tr>
    <tr>
      <td>Cxcl16</td>
      <td>Med</td>
      <td>NKT and ILC migration and survival; found in red pulp of the spleen</td>
    </tr>
    <tr>
      <td>Cxcl17</td>
      <td>Absent</td>
      <td>Monocyte and DC migration in the lung</td>
    </tr>
    <tr>
      <td>Ccl1</td>
      <td>Absent</td>
      <td>(TCA3) T cell trafficking</td>
    </tr>
    <tr>
      <td>Ccl2</td>
      <td>High</td>
      <td>(MCP1) Monocyte trafficking</td>
    </tr>
    <tr>
      <td>Ccl3</td>
      <td>High</td>
      <td>(MIP-1α) Macrophage and NK cell migration</td>
    </tr>
    <tr>
      <td>Ccl4</td>
      <td>High</td>
      <td>(MIP-1β) Macrophage and NK cell migration</td>
    </tr>
    <tr>
      <td>Ccl5</td>
      <td>High</td>
      <td>(RANTES) Macrophage and NK cell migration; also chemotactic for T cells, eosinophils, basophils</td>
    </tr>
    <tr>
      <td>Ccl6</td>
      <td>High</td>
      <td>(C10) Myeloid cell differentiation; monocyte, T cell, and eosinophil chemotaxis</td>
    </tr>
    <tr>
      <td>Ccl7</td>
      <td>Med</td>
      <td>(MCP3) (MARC) Monocyte mobilization</td>
    </tr>
    <tr>
      <td>Ccl8</td>
      <td>Med</td>
      <td>(MCP2) Th2 response; skin homing</td>
    </tr>
    <tr>
      <td>Ccl9</td>
      <td>High</td>
      <td>(MIP-1γ) (MRP-2) DC migration</td>
    </tr>
    <tr>
      <td>Ccl11</td>
      <td>Low</td>
      <td>(Eotaxin) Eosinophil and basophil migration; selectively recruits eosinophils</td>
    </tr>
    <tr>
      <td>Ccl12</td>
      <td>Low</td>
      <td>(MCP5) Inflammatory monocyte trafficking</td>
    </tr>
    <tr>
      <td>Ccl17</td>
      <td>Absent</td>
      <td>(ABCD2) (TARC) T cell chemotaxis; lung and skin homing</td>
    </tr>
    <tr>
      <td>Ccl19</td>
      <td>Med</td>
      <td>(MIP-3β) T cell and DC migration to LN</td>
    </tr>
    <tr>
      <td>Ccl20</td>
      <td>Low</td>
      <td>(MIP-3α) Th17 responses; B cell and DC homing to gut-associated lymphoid tissue</td>
    </tr>
    <tr>
      <td>Ccl21a</td>
      <td>Med</td>
      <td>(TCA4) T cell and DC migration to LN</td>
    </tr>
    <tr>
      <td>Ccl21b</td>
      <td>Absent</td>
      <td>Very similar to Ccl21a</td>
    </tr>
    <tr>
      <td>Ccl21c</td>
      <td>Absent</td>
      <td>Identical to Ccl21b</td>
    </tr>
    <tr>
      <td>Ccl22</td>
      <td>Low</td>
      <td>(ABCD1) Th2 response and migration; monocyte, DC, NK migration; produced by monocytes and DC</td>
    </tr>
    <tr>
      <td>Ccl24</td>
      <td>Med</td>
      <td>(MPIF-2) (Eotaxin-2) Eosinophil and basophil migration</td>
    </tr>
    <tr>
      <td>Ccl25</td>
      <td>Low</td>
      <td>(TECK) T cell homing to gut; T cell development; thymocyte, macrophage, and DC migration</td>
    </tr>
    <tr>
      <td>Ccl26</td>
      <td>Absent</td>
      <td>(Eotaxin-3) Eosinophil and basophil migration</td>
    </tr>
    <tr>
      <td>Ccl27a</td>
      <td>Low</td>
      <td>T cell migration to skin</td>
    </tr>
    <tr>
      <td>Ccl27b</td>
      <td>Absent</td>
      <td>T cell migration to skin</td>
    </tr>
    <tr>
      <td>Ccl28</td>
      <td>Absent</td>
      <td>(MEC) T and B cell migration to mucosal tissues</td>
    </tr>
    <tr>
      <td>Cx3cl1</td>
      <td>Low</td>
      <td>(Fractalkine) NK, monocyte, and T cell migration</td>
    </tr>
    <tr>
      <td>Xcl1</td>
      <td>Low</td>
      <td>(Lymphotactin) Cross-presentation by CD8+ DCs</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Expression level of chemokine receptors during infection with C. violaceum.Expression was visually ranked as absent, low, medium, or high based on SpatialFeaturePlots. Maximum expression rank recorded here. Table generated from David and Kubes, 2019; Hughes and Nibbs, 2018; Sokol and Luster, 2015; Zlotnik and Yoshie, 2000; Zlotnik and Yoshie, 2012. Natural killer cell (NK); innate lymphoid cell (ILC); dendritic cell (DC); plasmacytoid DC (pDC); lymph node (LN); red blood cell (RBC).


<table>
  <thead>
    <tr>
      <th>Receptor</th>
      <th>Max expression</th>
      <th>Alias, cellular expression, and main functions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cxcr1</td>
      <td>Absent</td>
      <td>(IL8R-α) Neutrophil, monocyte, NKs, mast cell, basophil, CD8 T cells; neutrophil migration and activation</td>
    </tr>
    <tr>
      <td>Cxcr2</td>
      <td>Med</td>
      <td>(IL8R-β) Neutrophil, monocyte, NKs, mast cell, basophil, CD8 T cells; B cell and neutrophil migration; neutrophil egress from BM</td>
    </tr>
    <tr>
      <td>Cxcr3</td>
      <td>Med</td>
      <td>Various T cells, NKs, pDCs, B cells; effector T cell migration and activation</td>
    </tr>
    <tr>
      <td>Cxcr4</td>
      <td>Med</td>
      <td>Most leukocytes; bone marrow homing and retention</td>
    </tr>
    <tr>
      <td>Cxcr5</td>
      <td>Absent</td>
      <td>B cells, T cells; T and B cell migration within LN to B cell zones</td>
    </tr>
    <tr>
      <td>Cxcr6</td>
      <td>Med</td>
      <td>Various T cells, ILCs, NKs, plasma cells; T cell and ILC function</td>
    </tr>
    <tr>
      <td>Ccr1</td>
      <td>High</td>
      <td>Monocyte, macrophage, neutrophil, Th1, basophil, DC</td>
    </tr>
    <tr>
      <td>Ccr2</td>
      <td>High</td>
      <td>Monocyte, macrophage, Th1, DC, basophil, NK; monocyte migration, Th1 immunity</td>
    </tr>
    <tr>
      <td>Ccr3</td>
      <td>Absent</td>
      <td>Highly expressed on eosinophils and basophils; allergic airway; eosinophil trafficking</td>
    </tr>
    <tr>
      <td>Ccr4</td>
      <td>Absent</td>
      <td>Various T cells, monocytes, B cells, DCs; T cell homing to skin and lung</td>
    </tr>
    <tr>
      <td>Ccr5</td>
      <td>High</td>
      <td>Monocytes, macrophages, various T cells, NK, DC, neutrophils, eosinophils; adaptive immunity</td>
    </tr>
    <tr>
      <td>Ccr6</td>
      <td>Absent</td>
      <td>Various T cells, DCs, NKs; DC and B cell maturation and migration; adaptive immunity</td>
    </tr>
    <tr>
      <td>Ccr7</td>
      <td>Med</td>
      <td>Various T cells, DCs, B cells; migration of adaptive lymphocytes and DCs to lymphoid tissues</td>
    </tr>
    <tr>
      <td>Ccr8</td>
      <td>Absent</td>
      <td>Various T cells, monocytes, macrophages; surveillance in skin; expressed in the thymus</td>
    </tr>
    <tr>
      <td>Ccr9</td>
      <td>Absent</td>
      <td>T cells, thymocytes, B cells, DCs, pDCs; T cell migration to gut; key regulator of thymocyte migration and maturation</td>
    </tr>
    <tr>
      <td>Ccr10</td>
      <td>Absent</td>
      <td>T cells, melanocytes, plasma cells; immunity at mucosal sites, especially skin</td>
    </tr>
    <tr>
      <td>Xcr1</td>
      <td>Low</td>
      <td>DCs; antigen cross-presentation</td>
    </tr>
    <tr>
      <td>Cx3cr1</td>
      <td>Low</td>
      <td>Monocytes, macrophages, microglia, DCs, T cells; migration and adhesion of leukocytes; marker of anti-inflammatory monocytes; thought to promote a patrolling phenotype and pro-survival signals</td>
    </tr>
    <tr>
      <td colspan="3">Atypical receptors</td>
    </tr>
    <tr>
      <td>Ackr1</td>
      <td>Low</td>
      <td>(DARC) RBCs, endothelial cells, neurons; chemokine scavenging, neutrophil transmigration; chemokine transcytosis on lymphatic endothelium and RBCs</td>
    </tr>
    <tr>
      <td>Ackr2</td>
      <td>Low</td>
      <td>Endothelial cells, DCs, B cells, macrophages; chemokine scavenging</td>
    </tr>
    <tr>
      <td>Ackr3</td>
      <td>Low</td>
      <td>(Cxcr7) Stromal cells, B cells, T cells, neurons, mesenchymal cells; pro-survival, adhesion, shaping CXCR4 gradients; involved in CXCR4 gradients</td>
    </tr>
    <tr>
      <td>Ackr4</td>
      <td>Low</td>
      <td>(Ccrl1) Epithelial cells, leukocytes, astrocytes, microglia; chemokine scavenging and transcytosis; chemokine scavenging in thymus</td>
    </tr>
    <tr>
      <td>Ccrl2</td>
      <td>High</td>
      <td>Chemokine receptor-like protein; binds chemerin; related to CCR1; expressed on neutrophils and monocytes</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Expression level of selected proteins and receptors during infection with C. violaceum.Expression was visually ranked as absent, low, medium, or high based on SpatialFeaturePlots. Maximum expression rank recorded here. Table generated from Bui et al., 2020; David and Kubes, 2019; Parks et al., 2004; Wang et al., 2018. Dendritic cell (DC); plasmacytoid DC (pDC); Kupffer cell (KC); natural killer cell (NK); syndecan 1 (SDC1).


<table>
  <thead>
    <tr>
      <th>Other</th>
      <th>Max expression</th>
      <th>Alias, cellular expression, and main functions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Fpr1</td>
      <td>High</td>
      <td>(Formyl peptide receptor 1) Expressed on myeloid cells and lymphocytes; widely expressed by neutrophils, eosinophils, basophils, monocytes, and platelets (among others); involved in leukocyte chemotaxis and activation</td>
    </tr>
    <tr>
      <td>Fpr2</td>
      <td>Med</td>
      <td>(Formyl peptide receptor 2) Expressed on neutrophils, eosinophils, monocytes, macrophages, T cells; involved in leukocyte chemotaxis and activation</td>
    </tr>
    <tr>
      <td>C5ar1</td>
      <td>Med</td>
      <td>(Complement C5a receptor 1) Expressed on basophils, DCs, mast cells, non-immune cells; involved in leukocyte chemotaxis and activation</td>
    </tr>
    <tr>
      <td>Ltb4r1</td>
      <td>Low</td>
      <td>(Leukotriene B4 receptor) Expressed on neutrophils, macrophages, T cells; involved in leukocyte chemotaxis and activation</td>
    </tr>
    <tr>
      <td>Cmklr1</td>
      <td>Low</td>
      <td>(Chemerin chemokine-like receptor 1) Expressed mainly on myeloid cells; present in thymus, bone marrow, spleen, fetal liver, and lymphoid organs; involved in migration of macrophages, DCs, and pDCs</td>
    </tr>
    <tr>
      <td>Mmp2</td>
      <td>High</td>
      <td>(Gelatinase A) Inactivates CXCL12, CCL7; degrades S100A9</td>
    </tr>
    <tr>
      <td>Mmp8</td>
      <td>Med</td>
      <td>(Neutrophil collagenase) Stored in secondary granules; cleaves and enhances CXCL5; inactivates CXCL-9 and CXCL-10</td>
    </tr>
    <tr>
      <td>Mmp9</td>
      <td>High</td>
      <td>(Gelatinase B) Mainly expressed by neutrophils; cleaves and enhances CXCL5; cleaves SDC1 to promote neutrophil infiltration; inactivates CXCL4 and CXCL1; inactivates CXCL-9 and CXCL-10; upregulated during respiratory epithelial healing; also expressed by KCs</td>
    </tr>
    <tr>
      <td>Mmp12</td>
      <td>High</td>
      <td>(Macrophage elastase) Activates TNF release from macrophages</td>
    </tr>
    <tr>
      <td>Mmp13</td>
      <td>Med</td>
      <td>(Collagenase 3) Inactivates CXCL-12; inactivates CCL2, CCL8, CCL13</td>
    </tr>
    <tr>
      <td>Itgam</td>
      <td>Med</td>
      <td>(CR3A) (Cd11b) Regulates adhesion and migration of monocytes, granulocytes, macrophages, NKs; involved in complement system</td>
    </tr>
    <tr>
      <td>Mif</td>
      <td>High</td>
      <td>(Macrophage migration inhibitory factor) Binds to CXCR2 and CXCR4 to promote chemotaxis of leukocytes</td>
    </tr>
    <tr>
      <td>Icam1</td>
      <td>High</td>
      <td>(Intracellular adhesion molecule 1) Promotes leukocyte migration from circulation to sites of inflammation</td>
    </tr>
    <tr>
      <td>S100a8</td>
      <td>High</td>
      <td>Heterodimerizes with S100a9; involved in leukocyte recruitment and inflammation</td>
    </tr>
    <tr>
      <td>S100a9</td>
      <td>High</td>
      <td>Heterodimerizes with S100a8; involved in leukocyte recruitment and inflammation</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Top 20 differentially expressed genes per cluster.The FindAllMarkers function was used to identify the top differentially expressed genes for each cluster across all timepoints. Genes were sorted from highest to lowest average log2 fold change (avg_log2FC) values within each cluster. Genes of interest shown in red. Full dataset found in Table 4—source data 1.Table 4—source data 1.Top differentially expressed genes for each cluster across all timepoints.


<table>
  <thead>
    <tr>
      <th>M</th>
      <th>HEP1</th>
      <th>HEP0</th>
      <th>HEP4</th>
      <th>HEP3</th>
      <th>NC-C</th>
      <th>CN-M2</th>
      <th>HEP5</th>
      <th>CN-M1</th>
      <th>CN</th>
      <th>EC2</th>
      <th>NC-P</th>
      <th>HEP2</th>
      <th>EC1</th>
      <th>rep HEP</th>
      <th>OG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
    <tr>
      <td>Mmp2</td>
      <td>Spink1</td>
      <td>Mup11</td>
      <td>Acot3</td>
      <td>Mup21</td>
      <td>Ewsr1</td>
      <td>Col11a1</td>
      <td>Gm31583</td>
      <td>Ptgs2</td>
      <td>F13a1</td>
      <td>Hbb-bt</td>
      <td>Hcar2</td>
      <td>Elovl3</td>
      <td>Derl3</td>
      <td>Ly6d</td>
      <td>Ccl8</td>
    </tr>
    <tr>
      <td>Aebp1</td>
      <td>Gstm3</td>
      <td>Mup17</td>
      <td>Cyp4a14</td>
      <td>Elovl3</td>
      <td>Parp10</td>
      <td>Ptprn</td>
      <td>Mpo</td>
      <td>Il11</td>
      <td>Cxcl3</td>
      <td>Hba-a1</td>
      <td>Cxcl3</td>
      <td>Cyp4a12b</td>
      <td>3930402G23Rik</td>
      <td>Moxd1</td>
      <td>Gm32468</td>
    </tr>
    <tr>
      <td>Olfml3</td>
      <td>Ifi27l2b</td>
      <td>Cyp2b13</td>
      <td>Cyp2c69</td>
      <td>Serpina1e</td>
      <td>Fth1</td>
      <td>Ccl11</td>
      <td>Gdf10</td>
      <td>Cxcl10</td>
      <td>Pf4</td>
      <td>Hba-a2</td>
      <td>Ptges</td>
      <td>Hsd3b5</td>
      <td>Hyou1</td>
      <td>BC049987</td>
      <td>Kdelr3</td>
    </tr>
    <tr>
      <td>Cd74</td>
      <td>Klk1b4</td>
      <td>Mup12</td>
      <td>Sult2a1</td>
      <td>Cib3</td>
      <td>Ptprc</td>
      <td>Prnd</td>
      <td>Cd207</td>
      <td>Cxcl9</td>
      <td>Mmp9</td>
      <td>Hbb-bs</td>
      <td>Tnf</td>
      <td>Gm32468</td>
      <td>Sult3a1</td>
      <td>Esco2</td>
      <td>Hbb-bt</td>
    </tr>
    <tr>
      <td>Pacs2</td>
      <td>Vnn3</td>
      <td>Mup16</td>
      <td>Cyp2a4</td>
      <td>Sds</td>
      <td>Csf3r</td>
      <td>Cthrc1</td>
      <td>Gck</td>
      <td>Il6</td>
      <td>Ptges</td>
      <td>mt-Atp8</td>
      <td>Ccl4</td>
      <td>Lhpp</td>
      <td>Sdf2l1</td>
      <td>Gsta1</td>
      <td>Cyp1b1</td>
    </tr>
    <tr>
      <td>Ngp</td>
      <td>Cib3</td>
      <td>Mup7</td>
      <td>Cyp4a10</td>
      <td>Mfsd2a</td>
      <td>Pacs2</td>
      <td>Gpnmb</td>
      <td>Cyp8b1</td>
      <td>Serpine1</td>
      <td>Cstdc4</td>
      <td>mt-Nd4l</td>
      <td>Cxcl2</td>
      <td>Cyp4a12a</td>
      <td>Apcs</td>
      <td>Cdkn3</td>
      <td>Lgals1</td>
    </tr>
    <tr>
      <td>Ewsr1</td>
      <td>Cdh1</td>
      <td>Mup1</td>
      <td>Sult2a2</td>
      <td>Acmsd</td>
      <td>Lyn</td>
      <td>Actg2</td>
      <td>Abcd2</td>
      <td>Hspa1a</td>
      <td>Gpr84</td>
      <td>Malat1</td>
      <td>Il1f9</td>
      <td>Fitm1</td>
      <td>Pdia4</td>
      <td>Chrna4</td>
      <td>Vwf</td>
    </tr>
    <tr>
      <td>Clu</td>
      <td>Frzb</td>
      <td>Mup3</td>
      <td>Fmo3</td>
      <td>Slc22a7</td>
      <td>Osbpl9</td>
      <td>Fbln2</td>
      <td>1700001C19Rik</td>
      <td>Adm</td>
      <td>Itgam</td>
      <td>mt-Nd3</td>
      <td>Fth1</td>
      <td>Oat</td>
      <td>Dnajb9</td>
      <td>Nat8</td>
      <td>Cthrc1</td>
    </tr>
    <tr>
      <td>Cdk11b</td>
      <td>Spon2</td>
      <td>Cyp2b9</td>
      <td>Slc16a5</td>
      <td>Etnppl</td>
      <td>Hectd1</td>
      <td>Col12a1</td>
      <td>Defb1</td>
      <td>Gm15056</td>
      <td>Fpr2</td>
      <td>mt-Nd5</td>
      <td>Ccl3</td>
      <td>Slc1a2</td>
      <td>A1bg</td>
      <td>Nat8f5</td>
      <td>Cpe</td>
    </tr>
    <tr>
      <td>Parp8</td>
      <td>Snta1</td>
      <td>Cyp7b1</td>
      <td>Cyp2b9</td>
      <td>Slc10a2</td>
      <td>Iqgap1</td>
      <td>Sulf1</td>
      <td>Prox1os</td>
      <td>Nos2</td>
      <td>Adam8</td>
      <td>mt-Nd2</td>
      <td>Slfn4</td>
      <td>Cyp2a5</td>
      <td>Prg4</td>
      <td>Mup1</td>
      <td>Pcdh17</td>
    </tr>
    <tr>
      <td>Nisch</td>
      <td>Wfdc2</td>
      <td>Mup20</td>
      <td>A1bg</td>
      <td>Selenbp2</td>
      <td>Clk1</td>
      <td>Mmp13</td>
      <td>Socs2</td>
      <td>Gbp5</td>
      <td>Lyz2</td>
      <td>mt-Co2</td>
      <td>Asprv1</td>
      <td>Tuba8</td>
      <td>Gm26917</td>
      <td>Thrsp</td>
      <td>Rasl11a</td>
    </tr>
    <tr>
      <td>Cpxm1</td>
      <td>Gstm2</td>
      <td>Gm13775</td>
      <td>Cyp2c40</td>
      <td>Mmd2</td>
      <td>Lilr4b</td>
      <td>Sfrp1</td>
      <td>Bik</td>
      <td>Olr1</td>
      <td>Clec4d</td>
      <td>Elane</td>
      <td>Slc7a11</td>
      <td>Cyp2c55</td>
      <td>Mt2</td>
      <td>Gm32468</td>
      <td>Ccdc80</td>
    </tr>
    <tr>
      <td>Poglut1</td>
      <td>Spic</td>
      <td>mt-Atp8</td>
      <td>Slc22a27</td>
      <td>G6pc</td>
      <td>Thrap3</td>
      <td>Fkbp10</td>
      <td>Afmid</td>
      <td>Rnd1</td>
      <td>Cav1</td>
      <td>Gm26917</td>
      <td>Acod1</td>
      <td>Rhbg</td>
      <td>Cyp17a1</td>
      <td>Cdca3</td>
      <td>Mrc2</td>
    </tr>
    <tr>
      <td>Col6a2</td>
      <td>Tmem268</td>
      <td>Mup9</td>
      <td>Cyp2c37</td>
      <td>Arl4d</td>
      <td>Stip1</td>
      <td>Lox</td>
      <td>Rad51b</td>
      <td>Retnlg</td>
      <td>Mmp8</td>
      <td>mt-Atp6</td>
      <td>Slpi</td>
      <td>Slc13a3</td>
      <td>Creld2</td>
      <td>Hebp2</td>
      <td>Hbb-bs</td>
    </tr>
    <tr>
      <td>Loxl1</td>
      <td>Tstd1</td>
      <td>Serpina3m</td>
      <td>Cyp2c38</td>
      <td>Kcnk5</td>
      <td>Fbxl5</td>
      <td>Acta2</td>
      <td>1810059H22Rik</td>
      <td>Il1a</td>
      <td>Il1f9</td>
      <td>mt-Nd1</td>
      <td>Ccrl2</td>
      <td>Cyp7a1</td>
      <td>Vnn1</td>
      <td>Ect2</td>
      <td>Ccbe1</td>
    </tr>
    <tr>
      <td>Gpx3</td>
      <td>Prelp</td>
      <td>Itih4</td>
      <td>Acot1</td>
      <td>Lpin1</td>
      <td>Zfp207</td>
      <td>Col15a1</td>
      <td>Tmem25</td>
      <td>F3</td>
      <td>Fpr1</td>
      <td>mt-Nd4</td>
      <td>Il1rn</td>
      <td>Glul</td>
      <td>Hist1h4h</td>
      <td>Pbk</td>
      <td>mt-Nd1</td>
    </tr>
    <tr>
      <td>Col1a1</td>
      <td>Slc39a4</td>
      <td>Slco1a1</td>
      <td>Etnppl</td>
      <td>Tat</td>
      <td>Klf2</td>
      <td>Nbl1</td>
      <td>Angptl6</td>
      <td>Cxcl2</td>
      <td>Capg</td>
      <td>Gm29966</td>
      <td>Slc25a37</td>
      <td>Slc1a4</td>
      <td>Rcan2</td>
      <td>Cdc20</td>
      <td>Plxdc2</td>
    </tr>
    <tr>
      <td>Igha</td>
      <td>Mki67</td>
      <td>Cyp2b10</td>
      <td>Gstt3</td>
      <td>Upp2</td>
      <td>Hck</td>
      <td>Col5a2</td>
      <td>Fam89a</td>
      <td>Procr</td>
      <td>Stfa2l1</td>
      <td>mt-Co3</td>
      <td>Mmp12</td>
      <td>Rdh16</td>
      <td>Hspa5</td>
      <td>Gpam</td>
      <td>Nat8f5</td>
    </tr>
    <tr>
      <td>Ikbkb</td>
      <td>Cdk1</td>
      <td>Car3</td>
      <td>Gm13775</td>
      <td>Pck1</td>
      <td>Rhob</td>
      <td>Col5a1</td>
      <td>Mug1</td>
      <td>AA467197</td>
      <td>Pqlc3</td>
      <td>Gm42418</td>
      <td>Clec4e</td>
      <td>Serpina7</td>
      <td>mt-Atp6</td>
      <td>Nek2</td>
      <td>Chrna4</td>
    </tr>
    <tr>
      <td>Rpl4</td>
      <td>Mcm5</td>
      <td>Fbxo31</td>
      <td>Ptgds</td>
      <td>Fam47e</td>
      <td>Lilrb4a</td>
      <td>Tnc</td>
      <td>Ccl27a</td>
      <td>Plaur</td>
      <td>Pdpn</td>
      <td>mt-Co1</td>
      <td>Il1b</td>
      <td>Cyp1a2</td>
      <td>mt-Co2</td>
      <td>Aurka</td>
      <td>Snhg18</td>
    </tr>
  </tbody>
</table>

### Expression of neutrophil-attractive chemokines

We observed high expression levels of chemokines involved in neutrophil trafficking (e.g. Cxcl1 and Cxcl2) as early as 12 hr post-infection (0.5 DPI) (Figure 2A, B), which correlates with our previous data that neutrophils are the first immune cells to arrive in response to C. violaceum (Harvest et al., 2023). Two other ligands that also bind to CXCR2 are CXCL3 and CXCL5. In contrast to Cxcl1 and Cxcl2, Cxcl3, and Cxcl5 show delayed expression peaking around 10 DPI (Figure 2C, D). In addition to temporal differences, the spatial location of chemokine expression varies within the lesion. For example, at 5 DPI Cxcl1 is expressed more toward the periphery of the lesion, while Cxcl2 is expressed more toward the center (Figure 2A, B). For all of these ligands, expression is absent by 21 DPI, which correlates with the time at which the majority of mice clear the infection. Therefore, although these four chemokines all bind to CXCR2, they clearly demonstrate the complexity of different temporal and spatial expression profiles over the course of infection.

![Figure 2.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig2-v1.jpg)

**Figure 2.:** SpatialFeaturePlots displaying normalized gene expression data of CXCR2 ligands (i.e. Cxcl1, Cxcl2, Cxcl3, and Cxcl5) at various days post-infection (DPI). Scale set at 0–3.0 expression.

### Expression of monocyte-attractive chemokines

We also investigated chemokines and receptors involved in monocyte trafficking (e.g. Ccl2, Ccl7, and Ccl12). Though all three of these ligands bind to CCR2, they had vastly different expression levels through the course of infection (Figure 3). Ccl2 was the most highly upregulated, while Ccl12 was expressed only at low levels, and Ccl7 expression was somewhere in between (Figure 3A–C). Similar to the chemokines involved in neutrophil trafficking, these ligands are not expressed by 21 DPI.

![Figure 3.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig3-v1.jpg)

**Figure 3.:** SpatialFeaturePlots displaying normalized gene expression data of CCR2 ligands (i.e. Ccl2, Ccl7, and Ccl12) at various days post-infection (DPI). Scale set at 0–3.0 expression.

### Compilation of chemokine and receptor expression data

In order to summarize our findings in a way that facilitates comparisons, we used the SpatialFeaturePlot to visually rank the expression intensity of each chemokine and receptor as absent, low, medium, or high over the course of infection. Each rank was based on both the intensity of expression and the relative number of spots that expressed the gene. For example, Cxcl1 expression was ranked as medium at 0.5 DPI, and ranked as high at 1 and 3 DPI based on the large presence of orange and red spots (Figure 2A). In contrast, Cxcl3 was ranked as absent at 0.5 DPI, low at 1 DPI, and medium at 3 DPI based on the fewer spots that were orange or red (Figure 2C). We depicted these ranks as qualitative heatmaps (Figure 4A–D). The relative expression of various chemokines (Figure 4—figure supplements 1–4) was much greater than the relative expression of their receptors (Figure 4—figure supplements 5 and 6), which is expected because large quantities of chemokines are needed to create gradients in tissues, but comparatively low expression of chemokine receptors is sufficient to enable trafficking of cells that express the receptors. Therefore, we changed the scale to best visualize receptor expression.

![Figure 4.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig4-v1.jpg)

**Figure 4.:** Normalized expression in SpatialFeaturePlots was visually ranked as absent (gray), low (blue), medium (yellow), or high (red) for (A) CXCL family chemokines, (B) CCL family chemokines, (C) CXC chemokine receptors, and (D) CC chemokine receptors. Visual rankings were based on both the intensity of expression and the relative number of spots that expressed the gene. (A, B) Scale set at 0–3.0 expression; (C–D) Scale set at 0–2.0 expression. Arrows indicate ligand–receptor interactions. Ligands are color-coded based on the maximum expression level reached at any time during the course of infection.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** SpatialFeaturePlots displaying normalized gene expression data of selected Cxcl family members at various days post-infection (DPI). Scale set at 0–3.0 expression.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** SpatialFeaturePlots displaying normalized gene expression data of selected Ccl family members at various days post-infection (DPI). Scale set at 0–3.0 expression.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** SpatialFeaturePlots displaying normalized gene expression data of selected Ccl family members at various days post-infection (DPI). Scale set at 0–3.0 expression.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig4-figsupp4-v1.jpg)

**Figure 4—figure supplement 4.:** SpatialFeaturePlots displaying normalized gene expression data of selected Ccl family members at various days post-infection (DPI). Scale set at 0–3.0 expression.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig4-figsupp5-v1.jpg)

**Figure 4—figure supplement 5.:** SpatialFeaturePlots displaying normalized gene expression data of selected Cxcr family members at various days post-infection (DPI). Scale set at 0–2.0 expression.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig4-figsupp6-v1.jpg)

**Figure 4—figure supplement 6.:** SpatialFeaturePlots displaying normalized gene expression data of selected Ccr family members at various days post-infection (DPI). Scale set at 0–2.0 expression.

One aspect of chemokine biology that makes understanding their function complicated is the promiscuity of certain ligands for multiple receptors, and vice versa. For example, CCL3, which is highly upregulated during infection with C. violaceum, can bind to CCR1 (along with several other chemokines), and CCL3 can also bind to CCR5 (again, along with several other chemokines). This promiscuity often makes it challenging to determine what unique or redundant roles each chemokine and chemokine receptor are playing. In order to simplify and graphically depict ligand and receptor interactions that seem relevant to the C. violaceum-induced granuloma, we listed the ligands that bind to the receptors that were expressed (Figure 4C, D). We colored each respective ligand based on its maximum expression ranking, regardless of the timepoint. This visualization allows for easier generation of hypotheses from this complex dataset.

### Weakly expressed chemokines suggest that certain immune cells are dispensable

The chemokines that are not present or are only weakly expressed can also be informative (Figure 4A, B). Two chemokines that are important for migration to the lung, Cxcl15 and Cxcl17, are both absent (as expected). Still other chemokines that are important for migration to the skin, lymph nodes, and mucosal tissues are also absent, namely Ccl17, Ccl27b, Ccl21b-c, and Ccl28, respectively (also as expected). Such negative data provide stronger confidence in the positive expression data for other chemokines.

In our previous studies, we showed that the adaptive immune response is dispensable to successfully form granulomas around, and then to eradicate, C. violaceum (Harvest et al., 2023). In agreement with those findings, several chemokines involved in T cell trafficking are absent or only expressed at low levels (i.e. Cxcl11, Ccl1, Ccl22, and Ccl25) (Figure 4A, B). On the other hand, other chemokines involved in T cell trafficking such as Cxcl9 and Cxcl10 are highly expressed during the first few days of infection, as is their receptor Cxcr3 (Figure 4A, C). During primary infection, T cell recruitment is not essential for clearance and we found that T cells are not recruited in large numbers (Harvest et al., 2023). However, Cxcl9 and Cxcl10 could play a more important role during a secondary infection that involves the adaptive immune response. It is a curious observation that T cells are dispensable during primary infection because in Mycobacterium tuberculosis-induced granulomas, CD4+ T helper type 1 (Th1) cells are required to stimulate the antibacterial activity of macrophages (Pagán and Ramakrishnan, 2018). A key difference between granuloma formation in response to C. violaceum compared to M. tuberculosis could be that M. tuberculosis is able to intracellularly infect macrophages, whereas C. violaceum is unable to circumvent pyroptosis of macrophages.

We did not observe basophils or eosinophils histologically during infection with C. violaceum, and this was again supported by the absence or low expression of chemokines involved in trafficking of these cell types (i.e. Ccl11, Ccl24, and Ccl26) (Figure 4B). CCR3, which is expressed mainly by eosinophils, plays a major role in the granuloma response to parasitic Schistosoma mansoni eggs (Chensue, 2013). During infection with C. violaceum, however, Ccr3 is not expressed at any timepoint (Figure 4D), further supporting that eosinophils are not involved in the granuloma response to C. violaceum. Furthermore, granulomas that form in response to M. tuberculosis often contain follicular dendritic cells which secrete CXCL13 to recruit B cells via CXCR5 (Domingo-Gonzalez et al., 2016). However, Cxcl13 is expressed at low levels, and Cxcr5 is absent in the C. violaceum model (Figure 4A, C). These examples reveal chemokines that are likely dispensable in the context of C. violaceum.

### Comparison of neutrophil- and monocyte-recruiting chemokines

To compare chemokines involved in neutrophil recruitment or monocyte recruitment, we further characterized Cxcl1 and Ccl2, respectively (Figure 5). When comparing their SpatialFeaturePlots, Cxcl1 and Ccl2 had unique expression profiles corresponding to different cluster identities (Figures 2A and 3A). To more easily visualize these differences in expression, we generated UMAP plots and violin plots (Figure 5A–D). Though there is some overlap, suggesting that some clusters express both Cxcl1 and Ccl2, there are also some clusters that appear to express only one or the other (Figure 5A, B). For example, cluster 14 (a cluster enriched for hepatocytes) expressed high levels of Cxcl1 but only low levels of Ccl2 (Figure 5C, D). Furthermore, there are interesting differences in temporal expression; Cxcl1 is highly expressed at 1 DPI while Ccl2 expression peaks at 3 DPI (Figure 5E, F). Though gene expression does not necessarily correlate with the timing and intensity of protein expression, we expect CXCL1 and CCL2 protein levels to accumulate over time, which would allow proper chemokine gradients to form. Altogether, these data corroborate our previous findings that neutrophils traffic to the liver within 1 DPI, and monocytes traffic and form granulomas beginning at 3 DPI.

![Figure 5.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig5-v1.jpg)

**Figure 5.:** Comparative analysis of Cxcl1 (A, C, and E) and Ccl2 (B, D, and F). (A, B) UMAP plots of 16 unique clusters showing normalized expression level of each gene. Maximum expression level set to 1.5; annotated with cluster identity; macrophage zone (M), hepatocyte (HEP), representative HEP (rep HEP), necrotic core center (NC-C), NC-periphery (NC-P), coagulative necrosis (CN), CN-macrophage (CN-M), endothelial cell (EC), outside granuloma (OG). (C, D) Violin plots of 16 unique clusters showing normalized expression level of each gene across all timepoints. (E, F) Violin plots of various days post-infection (DPI) showing normalized expression level of each gene within all clusters.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) Schematic of the experimental procedure. Mice were injected subcutaneously (SQ) with 20 mg/kg of reparixin, or with PBS. The following day, mice were infected intraperitoneally (IP) with 1 × 104 CFU of C. violaceum and treated again with reparixin or PBS. Mice were treated daily thereafter until harvesting on day 3 post-infection. This panels was created using BioRender.com. (B) Bacterial burdens in the liver and spleen of PBS- or reparixin-treated mice at 3 days post-infection (DPI). (C) Schematic of the experimental procedure as in A, except mice were harvested on day 1 post-infection. This panels was created using BioRender.com. (D) Bacterial burdens in the liver and spleen of PBS- or reparixin-treated mice at 1 DPI. (E) Gating analysis of neutrophil (Ly6G+) and macrophage (CD68+) numbers via flow cytometry at 1 DPI. Neutrophil numbers in the (F) liver and (G) spleen. Macrophage numbers in the (H) liver and (I) spleen. Each dot represents one mouse, with 10,000 events collected per sample. Line at median. (B, D) Dotted line, limit of detection. Solid line, median. Mann–Whitney (abnormally distributed data) for all except liver CFU at 1 DPI, which was analyzed using a two-tailed t test (normally distributed data). Not significant (ns). (B) Liver, p = 0.6286; spleen, p = 0.4286. (D) Liver, p = 0.0641; spleen, p = 0.8485. (B) One experiment. (D) Two experiments combined. (F–I) Two experiments combined.

### Neutrophil chemotaxis

We next wanted to investigate whether the upregulated neutrophil-recruiting chemokines are important during infection. However, there are many challenges when studying chemokines. As previously mentioned, ligands and receptors often show promiscuity in that one receptor may bind multiple ligands, which makes it difficult to completely abrogate chemotaxis through inhibiting a single ligand. Furthermore, although chemokine-specific antibodies exist (Fox et al., 2009; Mollica Poeta et al., 2019; Vales et al., 2023), neutralizing such large quantities of ligand can be challenging. Therefore, instead of attempting to block chemokine ligands, we chose to target chemokine receptors. In fact, the promiscuity of ligands and receptors means that targeting one chemokine receptor has the potential to impact more than one ligand of interest (Figure 4C, D). Nevertheless, targeting receptors is also challenging due to poor solubility of many receptor antagonists (Li et al., 2019).

During infection with C. violaceum, neutrophils appear in the liver within 1 DPI. However, it is still unclear what signals initiate their migration into the liver. Though a large number of neutrophils are already present in the blood during homeostasis, additional neutrophils expressing CXCR2 exit the bone marrow in response to endothelial cell-derived CXCL1 and CXCL2 (David and Kubes, 2019). Furthermore, tissue-resident macrophages can also express CXCL1, CXCL2, and various leukotrienes in response to infection (Soehnlein and Lindbom, 2010). Though Cxcr2 knockout mice exist, they have abnormalities (Cacalano et al., 1994). Therefore, to assess the role of CXCL1, CXCL2, CXCL3, and CXCL5 in neutrophil trafficking during infection with C. violaceum, we used a CXCR2 inhibitor. Reparixin is an allosteric inhibitor of CXCR1 and CXCR2 that has been shown to inhibit neutrophil trafficking during ischemia–reperfusion injury and acid-induced acute lung injury (Bertini et al., 2004; Zarbock et al., 2008; Hosoki and Sur, 2018). We pre-treated mice with reparixin or saline (PBS) 1 day before infection, then infected mice with C. violaceum followed by daily treatment with reparixin or PBS (Figure 5—figure supplement 1A). We then harvested livers and spleens at 3 DPI to assess bacterial burdens. Though there was no difference in CFU for the liver, a few CFU were recovered from the spleens of two reparixin-treated mice (Figure 5—figure supplement 1B), which, though this was not statistically significant, is unusual for WT mice. Based on these results, we hypothesized that reparixin would have a stronger effect at 1 DPI (Figure 5—figure supplement 1C), before the infection causes excessive damage to the liver. At 1 DPI, we again saw no difference in bacterial burdens in the liver of reparixin-treated mice (Figure 5—figure supplement 1D). To verify that reparixin affected neutrophil numbers in the liver and spleen, we used flow cytometry to quantify Ly6G+ neutrophils (Figure 5—figure supplement 1E). We observed differences in the number of neutrophils between PBS-treated female and male mice, so data were analyzed disaggregated for sex. Though reparixin might have caused a subtle decrease in neutrophil numbers in the liver and spleen at 1 DPI, the results were variable between mice (Figure 5—figure supplement 1F, G). In our hands, reparixin was poorly soluble in PBS, which could account for some of the variability. Because monocytes also express CXCR2, albeit to a much lesser extent than neutrophils, we also stained for CD68. There was no marked difference in macrophage numbers in the liver or spleen between PBS- and reparixin-treated mice (Figure 5—figure supplement 1H, I).

Altogether, it is clear that reparixin was not a successful inhibitor of neutrophil recruitment during infection with C. violaceum. The role of CXCR1/2 and their ligands could be further studied using knockout mice. Regardless, other chemoattractants likely contribute to neutrophil recruitment as well. Indeed, neutrophils migrate in response to a variety of pro-inflammatory DAMPs and PAMPs (Kolaczkowska and Kubes, 2013). Importantly, formyl peptide receptors (FPRs) such as FPR2 promote neutrophil migration in response to bacterial infection in the liver (Lee et al., 2023). In support of this, FPRs are upregulated in this model (Table 3).

### CCR2 is essential for monocyte trafficking and defense against C. violaceum

Previously, we noticed that the appearance of organized macrophages at approximately 5 DPI correlates with a subsequent decrease in bacterial burdens (Harvest et al., 2023). We also observed that Nos2–/– mice, which lack the ability to express inducible nitric oxide synthase (iNOS), succumb to infection beginning at 7 DPI, a timepoint when the granuloma matures with a thicker macrophage ring (Harvest et al., 2023). Though neutrophils can also express iNOS (Saini and Singh, 2018), these data suggested that macrophages are playing a critical protective role. We therefore hypothesized that monocyte trafficking to the site of infection is a key event in clearing the infection. There are several candidate chemokines that could attract monocytes to the site of infection, and these chemokines bind to several different receptors (Table 1, Figure 4D). We chose to focus on the chemokine receptor CCR2 because of its known role in monocyte migration out of the bone marrow (Serbina and Pamer, 2006). Importantly, Ccr2–/– mice have intact tissue-resident macrophage populations but are unable to recruit additional monocytes in the event of infection (Kurihara et al., 1997).

To assess the role of monocyte trafficking to lesions in the liver, we infected Ccr2–/– mice with C. violaceum. Strikingly, Ccr2–/– mice were highly susceptible and succumbed to infection beginning at 5 DPI, with all mice dying by 9 DPI (Figure 6A), which is more severe than the phenotype in Nos2–/– mice (Harvest et al., 2023). This is in contrast to Yersinia pseudotuberculosis models in which deletion of Ccr2 has the opposite phenotype, and loss of monocytes is actually protective (Zhang et al., 2018). This also contrasts with M. tuberculosis models where loss of Ccr2 has no effect on survival in some contexts (Domingo-Gonzalez et al., 2016; Scott and Flynn, 2002). At 5 DPI, Ccr2–/– mice had increased liver burdens (Figure 6B), and bacterial dissemination into the spleen (Figure 6C). We also observed that Ccr2–/– mice had abnormal lesions which were more numerous and larger than the lesions of WT mice (Figure 6D).

![Figure 6.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig6-v1.jpg)

**Figure 6.:** Wildtype (WT) and Ccr2–/– mice were infected intraperitoneally (IP) with 1 × 104 CFU C. violaceum. (A) Survival analysis of WT (N = 10) and Ccr2–/– (N = 9) mice. Two experiments combined. Mantel–Cox test, ****p < 0.0001. (B–K) Livers and spleens were harvested 5 days post-infection (DPI). Bacterial burdens in the (B) liver and (C) spleen of WT and Ccr2–/– mice. Two experiments combined. Each dot represents one mouse. (B) Two-tailed t test (normally distributed data); ***p = 0.0002. (C) Mann–Whitney (abnormally distributed data); **p = 0.0012. Dotted line, limit of detection. Solid line, median. (D) Gross images of WT and Ccr2–/– livers 5 DPI. (E) Gating strategy for analysis of neutrophil (Ly6G+) and macrophage (CD68+) numbers via flow cytometry. Liver samples from infected mice shown. Frequency of CD68+ macrophages from single-cell gate in the (F) liver, (H) spleen, and (J) blood. Frequency of Ly6G+ neutrophils from single-cell gate in the (G) liver, (I) spleen, and (K) blood. (F–K) Three experiments combined using only female mice. Each dot represents one mouse, with 10,000 events collected per sample. Two-way ANOVA (for multiple comparisons to assess genotype and infection); key comparisons and p-values shown. Line represents mean ± standard deviation.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Wildtype (WT) and Ccr2–/– mice were infected intraperitoneally (IP) with 1 × 104 CFU C. violaceum. (A–E) Analysis of neutrophil (Ly6G+) and macrophage (CD68+) numbers via flow cytometry. Same samples as in Figure 6, but showing cell counts instead of percent; cell counts from single-cell gate, with 10,000 events collected per sample, or total cell counts from the whole liver or whole spleen calculated using hemocytometer values following tissue processing; three experiments combined using only female mice, each dot represents one mouse. Two-way ANOVA (for multiple comparisons to assess genotype and infection); key comparisons and p-values shown. Line represents mean ± standard deviation.

We used flow cytometry to assess macrophage (CD68+) and neutrophil (Ly6G+) numbers in the liver, spleen, and blood of mice at 5 DPI (Figure 6E, Figure 6—figure supplement 1). Uninfected WT and uninfected Ccr2–/– mice had a similar frequency of macrophages in the liver (Figure 6F), likely representing the tissue-resident Kupffer cell population, as well as a similar frequency of splenic macrophages (Figure 6H). However, upon infection, the livers of Ccr2–/– mice had markedly less macrophages and drastically more neutrophils compared to the livers of WT mice (Figure 6F, G). This trend was also observed in the spleen (Figure 6H, I) and blood (Figure 6J, K), showing that failure to recruit monocytes leads to enhanced neutrophil recruitment. Interestingly, infected Ccr2–/– mice did have slightly more macrophages in the liver, spleen, and blood compared to uninfected Ccr2–/– mice (Figure 6F, H, J), suggesting that loss of CCR2 does not completely abrogate monocyte recruitment. Alternatively, this expansion could represent emergency hematopoiesis and proliferation of pre-existing cell populations in these tissues (Boettcher and Manz, 2017).

### C. violaceum in the liver cannot be contained without macrophages

In our previous characterization of granulomas in WT mice, we identified three distinct zones using immunohistochemistry (IHC): necrotic core (NC), coagulative necrosis (CN), and macrophage zone (M) (Harvest et al., 2023). By 5 DPI, all three layers are distinctly visible through H&E staining (Figure 7A, Figure 7—figure supplement 1). Furthermore, we consistently see containment of C. violaceum within the necrotic core (Figure 7B), which overlaps with pronounced Ly6G staining (Figure 7C). Importantly, by 5 DPI the macrophage zone is clearly visible in WT mice, showing that macrophages surround the granuloma and form a protective zone between the coagulative necrosis zone and healthy hepatocytes outside the infected lesion (Figure 7D). Compared to WT mice, lesions in Ccr2–/– mice lack these distinct zones. Though Ccr2–/– mice had larger areas of necrotic debris, the coagulative necrosis zone was largely absent from most lesions (Figure 7E). In previous studies, we also observed sporadic clotting in WT mice (Harvest et al., 2023), and this clotting was even more abundant in Ccr2–/– mice (Figure 7—figure supplement 1). Excessive clotting, in addition to elevated bacterial burdens and sepsis, could also cause mortality in these mice by pulmonary embolism. Strikingly, lesions in Ccr2–/– mice had abnormal budding morphology, which stained very strongly for C. violaceum (Figure 7F) and Ly6G neutrophils (Figure 7G). In fact, many puncta that appear to be individual bacteria were visualized (Figure 7—figure supplement 1).

![Figure 7.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig7-v1.jpg)

**Figure 7.:** Wildtype (WT) and Ccr2–/– mice were infected intraperitoneally (IP) with 1 × 104 CFU C. violaceum and livers were harvested 5 days post-infection (DPI). Serial sections of livers stained by hematoxylin and eosin (H&E) or various immunohistochemistry (IHC) markers for (A–D) WT female and (E–H) Ccr2–/– male. Necrotic core (NC), coagulative necrosis zone (NC), macrophage zone (M). For 10×, scale bar is 100 µm. For 20× and 40×, scale bar is 50 µm. Representative of two experiments with 2–4 mice per group, and multiple granulomas per section.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** Wildtype (WT) and Ccr2–/– mice were infected intraperitoneally (IP) with 1 × 104 CFU C. violaceum and livers harvested 5 days post-infection (DPI). Serial sections of livers stained by hematoxylin and eosin (H&E) or various immunohistochemistry (IHC) markers for (A–D) WT female and (E–H) Ccr2–/– female. For 10×, scale bar is 100 µm. For 20× and 40×, scale bar is 50 µm.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** Ccr2–/– mice were infected intraperitoneally (IP) with 1 × 104 CFU C. violaceum. (A) Liver section from Ccr2–/– male mouse 5 days post-infection (DPI), stained for C. violaceum; zoom showing individual puncta of C. violaceum. (B–D) A Ccr2–/– female mouse from survival curve in Figure 6A that was sacrificed at 7 DPI according to euthanasia criteria. (B) Gross pathology. (C) Liver section stained by hematoxylin and eosin (H&E) showing clotting. (D) Serial sections of liver stained with H&E or various immunohistochemistry (IHC) markers. For 10×, scale bar is 100 µm.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig7-figsupp3-v1.jpg)

**Figure 7—figure supplement 3.:** Wildtype (WT) and Ccr2–/– mice were infected intraperitoneally (IP) with 1 × 104 CFU C. violaceum and livers harvested 5 days post-infection (DPI) for immunofluorescent staining. Tissue sections were stained for nuclei (DAPI, blue), neutrophils (Ly6G, red), macrophages (CD68, green), and C. violaceum (white). (A) WT female and (B, C) Ccr2–/– females. For 2×, scale bar is 500 µm. For 10×, scale bar is 100 µm.

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/96425/elife-96425-fig7-figsupp4-v1.jpg)

**Figure 7—figure supplement 4.:** Wildtype (WT) and Ccr2–/– mice were infected intraperitoneally (IP) with 1 × 104 CFU C. violaceum. (A–C) Livers harvested 5 days post-infection (DPI) for immunofluorescent staining. Tissue sections were stained for nuclei (DAPI, blue), neutrophils (Ly6G, red), and CCL2 (white). Serial sections from the same tissues in Figure 7—figure supplement 3. Quantification of CCL2 via ELISA in the liver (D) and serum (E) of WT and Ccr2–/– mice at 3 DPI; two experiments combined using male and female mice, each dot represents one mouse. Line represents mean ± standard deviation.

Though we were able to visualize the Kupffer cell population scattered throughout the liver, an organized macrophage zone was absent from the majority of lesions in Ccr2–/– mice (Figure 7H). These Kupffer cells are likely the CD68+ cells identified by flow cytometry (Figure 6F). A rare Ccr2–/– mouse that survived to 7 DPI also had few macrophages (Figure 7—figure supplement 1), in contrast to WT mice that display mature granulomas with thick macrophage zones at this timepoint (Harvest et al., 2023). Importantly, without distinct coagulative necrosis or macrophage zones, C. violaceum staining extends well outside the center of each lesion. In fact, numerous bacteria were identified in immune cells immediately adjacent to the healthy hepatocyte layer (Figure 7F). Importantly, we also observed these key differences through immunofluorescence, including larger necrotic cores with increased Ly6G staining, loss of organized macrophage zones, and bacterial staining directly adjacent to healthy hepatocytes (Figure 7—figure supplement 3). Furthermore, immunofluorescent staining of CCL2 revealed diffuse quantities in both WT and Ccr2–/– mice, with Ccr2–/– mice producing higher amounts of CCL2 in the liver and serum compared to WT mice at 3 DPI (Figure 7—figure supplement 4). This indicates that, especially in Ccr2–/– mice, the immune system is continuously calling for monocyte mobilization in response to C. violaceum infection. Taken together, the tissue staining, along with the elevated CFU burdens, suggests that monocyte recruitment fails without CCR2, and the lack of a macrophage zone leads to loss of bacterial containment. Despite the excessive number of neutrophils in the liver, spleen, and blood of Ccr2–/– mice (Figure 6G, I, K), these mice are unable to clear the infection and ultimately succumb.

Previously, we observed abnormal lesion architecture in Casp1::Casp11 DKO and Gsdmd–/– mice with budding morphology and loss of bacterial containment (Harvest et al., 2023) that is remarkably similar to the architecture observed in Ccr2–/– mice (Figure 7F). However, the Ccr2–/– mice survive a few days longer and thus develop even larger lesions over time. Together, these data suggest that macrophage recruitment and pyroptosis are both essential in defense against, and containment of, C. violaceum. In addition, because the Ccr2–/– mice succumb in a timeframe similar to that seen with Nos2–/– mice, this supports our hypothesis that it is nitric oxide derived from granuloma macrophages that is specifically required for bacterial clearance. Altogether, these data indicate that without monocytes trafficking to the site of infection, C. violaceum is able to replicate and spread into adjacent hepatocytes, resulting in ever-expanding lesions. These in vivo data support the transcriptomics dataset and provide proof-of-concept that upregulated genes, specifically chemokines, are critical to the formation of the granuloma.

## Discussion

Here, we demonstrate that macrophages are essential for clearance of C. violaceum from the infected liver, and for protection against dissemination into the spleen. Loss of CCR2-dependent monocyte trafficking results in a loss of bacterial containment, ultimately leading to uncontrolled bacterial replication in the liver, evidenced by elevated CFU burdens and increased lesion size.

There are many questions that still remain about the individual and coordinated efforts of neutrophils and macrophages during infection with C. violaceum. It is likely that the tissue-resident Kupffer cells and infected hepatocytes are the first cells to sound the alarm, calling for neutrophils. The initial recruitment of neutrophils likely involves chemokines (i.e. CXCL1 and CXCL2) redundantly with other chemoattractants such as formylated peptides and leukotrienes. However, these neutrophils are unable to clear the infection despite being recruited in large numbers.

Based on our data, CCR2 is an essential chemokine receptor for monocyte trafficking in response to C. violaceum, but we have not yet determined which ligand(s) mediate this response. CCL2 and CCL7 can both bind to CCR2 to induce monocyte trafficking. Importantly, pro-inflammatory cytokines and PAMPs can induce CCL2 expression by most cell types (Shi and Pamer, 2011). In agreement, we see upregulation of Ccl2 in several clusters and deposition of CCL2 protein in wide areas around granulomas, further suggesting that CCL2 may be a critical chemokine that promotes monocyte recruitment in response to C. violaceum. In contrast, Ccl7 is expressed by fewer clusters, and to a lesser degree, and its expression is slightly delayed compared to Ccl2. Deletion of either ligand partially diminished monocyte trafficking in response to Listeria monocytogenes infection, but the individual role of each ligand was unclear (Jia et al., 2008). Future studies using C. violaceum could further elucidate the unique or redundant roles of CCL2 and CCL7. Lastly, adoptive transfer experiments in the context of Listeria infection showed that Ccr2–/– monocytes are still able to traffic to the site of infection in the spleen (Serbina and Pamer, 2006) and liver (Shi et al., 2010). During C. violaceum infection, we have not yet determined whether CCR2 is required for migration once monocytes have left the bone marrow, as CCR2 is required for this initial egress. We saw a subtle increase in the number of macrophages in the liver of infected Ccr2–/– mice. Though macrophage numbers in Ccr2–/– tissues remain considerably lower than seen in WT mice, there are two explanations for the subtle increase: (1) loss of CCR2 may not completely abrogate monocyte recruitment, as monocytes could be migrating via other chemokine receptors, or (2) tissue-resident macrophages, or even tissue-resident hematopoietic stem cells, could undergo emergency hematopoiesis and proliferate in response to infection (Boettcher and Manz, 2017). More studies are needed to assess the origin of this small population of macrophages in Ccr2–/– mice. Regardless, this small population of macrophages is not sufficient to protect against infection with C. violaceum.

In other granuloma models, the role of CCR2 is less clear. Loss of CCR2-dependent monocyte trafficking enhances clearance of Y. pseudotuberculosis (Zhang et al., 2018), which is a surprising result as typically macrophages would be expected to be important to clear infections. The role of CCR2 during M. tuberculosis infection is strain-dependent, and also varies depending on the dose and route of infection (Dunlap et al., 2018; Peters et al., 2001; Scott and Flynn, 2002). Though there are similarities between these infection models and C. violaceum, there are numerous differences. For example, expression of specific chemokines in response to M. tuberculosis differs from those we observe in response to C. violaceum, especially chemokines that attract T cells (Kang et al., 2011). A key concept in the M. tuberculosis field is that a delicate balance exists between cellular recruitment to control infection, and excess inflammation that causes disease symptoms (Monin and Khader, 2014). Furthermore, excess recruitment of monocytes to M. tuberculosis-induced granulomas leads to increased bacterial replication due to the ability of M. tuberculosis to inhibit degradation within phagosomes in which it resides (Domingo-Gonzalez et al., 2016; Slight and Khader, 2013). In contrast, C. violaceum appears to lack sufficient virulence factors to enable it to replicate within macrophages (Batista and da Silva Neto, 2017). Importantly, while M. tuberculosis bacterial burdens plateau at 21 DPI, almost all mice clear C. violaceum by this timepoint. Though decades of research have been dedicated to investigating M. tuberculosis, fewer studies involving other granuloma-inducing pathogens have been performed. As we continue to study the cellular mechanisms that allow for successful granuloma formation and clearance of C. violaceum, it will be interesting to compare the two pathogens, as future studies could shed light on key differences that result in successful pathogen clearance.

In WT mice, neutrophil recruitment wanes as the granuloma matures, which coincides with clearance of C. violaceum. However, in the Ccr2–/– mice, we see elevated neutrophil numbers at 5 DPI, suggesting that neutrophils are continuously recruited in the absence of macrophages. Under normal circumstances, endocytosis of chemokines by endothelial cells helps to diminish chemokine gradients, limiting prolonged neutrophil recruitment (Kolaczkowska and Kubes, 2013). Future studies could investigate the various signals that diminish neutrophil recruitment in WT mice during clearance, and why this fails in Ccr2–/– mice. Another interesting component of the granuloma response is the spatial arrangement of neutrophils and macrophages within the granuloma. In vitro studies found that CCR1 and CCR5 differentially affected monocyte localization within a transwell system, implying that a system exists for fine-tuning the exact location of macrophages within inflamed tissues (Shi and Pamer, 2011). These receptors are highly upregulated in the C. violaceum-induced granuloma and are thus good candidates for balancing the localization of macrophages between the coagulative necrosis zone and healthy tissue outside the granuloma.

Lastly, this dataset inspires a number of new hypotheses related to granuloma resolution and tissue repair after bacterial clearance. Chemokines undergo a variety of post-translational modifications, such as glycosylation, nitration, citrullination, and proteolytic cleavage, which can either enhance or abrogate their activity (Vanheule et al., 2018). For example, nitration of CCL2 and CCL3 by peroxynitrite was shown to reduce monocyte and neutrophil chemotaxis, respectively (Sato et al., 1999; Sato et al., 2000). Furthermore, binding to atypical receptors can also affect chemokine availability, representing another mechanism to resolve inflammation (Hansell et al., 2006; Ulvmar et al., 2011). Of particular interest is the implication of matrix metalloproteinases (MMPs) in regulating chemokine functions. MMPs can not only directly cleave chemokines, they can also cleave various chemokine-binding proteins that help establish the chemokine gradient (Parks et al., 2004). Several studies have found that MMPs can cleave chemokines to alter their function, either increasing or decreasing their receptor binding activity. For example, MMP-2 cleaves both CXCL12 and CCL7, abolishing their ability to induce chemotaxis (McQuibban et al., 2000; McQuibban et al., 2001); importantly, all three of these genes are upregulated during C. violaceum infection (Table 1, Table 3, Table 4). Furthermore, MMP-2 and MMP-9 have been extensively studied in the context of lung inflammation, both of which are important to limit tissue damage (Greenlee et al., 2006). MMP-9 has also been shown to promote or inhibit liver fibrosis and wound repair, depending on the context (Feng et al., 2018). An unsolved mystery during infection with C. violaceum is how the chemotaxis of neutrophils and monocytes is abrogated when the infection is cleared, and how wound repair and resolution is initiated. Future studies could characterize the role of MMPs during resolution, especially MMP-9 and its various targets in relation to wound repair.

Analysis of a spatial transcriptomics dataset revealed the upregulation of many chemokines and their receptors during murine infection with C. violaceum. Here, we show that CCR2 is an essential chemokine receptor for monocyte trafficking, which enables the formation of mature granulomas with organized macrophage zones. Importantly, loss of organized macrophages leads to loss of bacterial containment. This work has given new insight into the function of chemokines during granuloma formation, and this model of C. violaceum-induced granuloma formation will be useful in exploring the unique and redundant roles of chemokines during infection.

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
      <td>Wildtype C57BL/6 mice (WT)</td>
      <td>Jackson Laboratory (West Grove, PA)</td>
      <td>Ref# 000664</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>Ccr2RFP (Ccr2–/–)</td>
      <td>Jackson Laboratory</td>
      <td>Ref# 017586</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Bacteria)</td>
      <td>Chromobacterium violaceum (C. violaceum)</td>
      <td>ATCC (Manassas, VA)</td>
      <td>Ref# 12472</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse Ly6G monoclonal (IA8) in BV421</td>
      <td>BD Biosciences (Franklin Lakes, NJ)</td>
      <td>Ref# 562737</td>
      <td>1:300 (FC)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse monoclonal (FA-11) CD68 in FITC</td>
      <td>BioLegend (San Diego, CA)</td>
      <td>Ref# 137005</td>
      <td>1:300 (FC)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-C. violaceum polyclonal</td>
      <td>Cocalico Biologicals (Denver, PA)</td>
      <td>Custom polyclonal antibody</td>
      <td>1:2000 (IHC, IF)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse Ly6G monoclonal (IA8)</td>
      <td>BioLegend</td>
      <td>Ref# 127601</td>
      <td>1:300 (IHC)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-mouse CD68 polyclonal</td>
      <td>Abcam (Waltham, MA)</td>
      <td>Ref# ab125212</td>
      <td>1:200 (IHC)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse CD68 monoclonal (FA-11) in Alexa Fluor 488</td>
      <td>Abcam</td>
      <td>Ref# ab201844</td>
      <td>1:100 (IF)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rat anti-mouse Ly6G monoclonal (IA8) in Alexa Fluor 647</td>
      <td>BioLegend</td>
      <td>Ref# 127610</td>
      <td>1:100 (IF)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-mouse MCP1 (CCL2) polyclonal</td>
      <td>Abcam</td>
      <td>Ref# ab315478</td>
      <td>1:100 (IF)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-rabbit secondary polyclonal in Alexa Fluor 594</td>
      <td>Invitrogen (Waltham, MA)</td>
      <td>Ref# A32740</td>
      <td>1:1000 (IF)</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Avidin/Biotin Blocking Kit</td>
      <td>Vector Laboratories (Newark, CA)</td>
      <td>Ref# SP-2001</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>SignalStain Boost IHC Detection Reagent (HRP, Anti-Rabbit)</td>
      <td>Cell Signaling (Danvers, MA)</td>
      <td>Ref# 8114</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>ImmPRESS HRP Goat Anti-Rat Detection Kit</td>
      <td>Vector Laboratories</td>
      <td>Ref# MP-7404</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>DAB Substrate Kit, HRP</td>
      <td>Vector Laboratories</td>
      <td>Ref# SK-4100</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>H&amp;E Stain Kit (Modified Mayer’s Hematoxylin and Bluing Reagent)</td>
      <td>Abcam</td>
      <td>Ref# ab245880</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MCP-1/CCL2 Mouse Uncoated ELISA Kit</td>
      <td>Thermo Scientific (Waltham, MA)</td>
      <td>Ref# 88-7391-22</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Reparixin</td>
      <td>MedChemExpress (Monmouth Junction, NJ)</td>
      <td>Ref# HY-15251</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RStudio</td>
      <td>Posit PBC (Boston, MA)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FlowJo</td>
      <td>BD Biosciences</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism 9</td>
      <td>GraphPad (Boston, MA)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji</td>
      <td>ImageJ (Burleson, TX)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Collagenase Type IV</td>
      <td>Gibco</td>
      <td>Ref# 17104019</td>
      <td>Tissue dissociation media</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>1× DMEM, +4.5 g/l D-Glucose, +L-Glutamine, +110 mg/l Sodium Pyruvate</td>
      <td>Gibco</td>
      <td>Ref# 11995-065</td>
      <td>Cell culture media</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>1× RPMI Medium 1640, +L-Glutamine</td>
      <td>Gibco</td>
      <td>Ref# 11875-093</td>
      <td>Cell culture media</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>PenStrep +10,000 units/ml Penicillin, +10,000 µg/ml Streptomycin</td>
      <td>Gibco</td>
      <td>Ref# 15140-122</td>
      <td>Antibiotics</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>HyClone Characterized Fetal Bovine Serum</td>
      <td>Cytiva (Marlborough, MA)</td>
      <td>Ref# SH30396.03</td>
      <td>Cell culture media</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>1× DPBS, -Calcium Chloride, -Magnesium Chloride</td>
      <td>Gibco</td>
      <td>Ref# 14190-144</td>
      <td>Cell culture media</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>70 µm Cell Strainers</td>
      <td>Genesee Scientific (El Cajon, CA)</td>
      <td>Ref# 25-376</td>
      <td>Tissue dissociation reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>40 µm Cell Strainers</td>
      <td>Genesee Scientific</td>
      <td>Ref# 25-375</td>
      <td>Tissue dissociation reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Percoll</td>
      <td>GE Healthcare (Chicago, IL)</td>
      <td>Ref# 17-0891-01</td>
      <td>Tissue dissociation reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>1× RBC Lysis Buffer</td>
      <td>eBioscience</td>
      <td>Ref# 00-4333-57</td>
      <td>Flow cytometry reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Falcon Round-Bottom Polystyrene Test Tubes</td>
      <td>Thermo Scientific</td>
      <td>Ref# 14-959-1A</td>
      <td>Flow cytometry tubes</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Mouse BD Fc Block</td>
      <td>BD Biosciences</td>
      <td>Ref# 553142</td>
      <td>Blocking reagent; used at 1 µg (FC), 2% (IF)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Intracellular Fixation &amp; Permeabilization Buffer</td>
      <td>eBioscience</td>
      <td>Ref# 88-8824-00</td>
      <td>Flow cytometry reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>10% Neutral Buffered Formalin</td>
      <td>VWR (Radnor, PA)</td>
      <td>Ref# 16004–128</td>
      <td>Histology reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>16% Paraformaldehyde</td>
      <td>VWR</td>
      <td>Ref# 15710S</td>
      <td>Immunofluorescence reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Sucrose</td>
      <td>Sigma-Aldrich</td>
      <td>Ref# S1888</td>
      <td>Immunofluorescence reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Tissue-Tek O.C.T. Compound</td>
      <td>Sakura (Torrance, CA)</td>
      <td>Ref# 4583</td>
      <td>Immunofluorescence reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Epredia Xylene</td>
      <td>Fisher Chemical</td>
      <td>Ref# 99-905-01</td>
      <td>Immunohistochemistry reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>ImmEdge Pen</td>
      <td>Vector Laboratories</td>
      <td>Ref# H-4000</td>
      <td>Immunohistochemistry reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Normal Goat Serum Blocking Solution, 2.5%</td>
      <td>Vector Laboratories</td>
      <td>Ref# S-1012</td>
      <td>Immunohistochemistry reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>SignalStain Antibody Diluent</td>
      <td>Cell Signaling</td>
      <td>Ref# 8112</td>
      <td>Immunohistochemistry reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Permount</td>
      <td>Fisher Chemical</td>
      <td>Ref# SP15-100</td>
      <td>Immunohistochemistry reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>T-PER Tissue Protein Extraction Reagent</td>
      <td>Thermo Scientific</td>
      <td>Ref# 78510</td>
      <td>Tissue dissociation reagent</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Sulfuric Acid</td>
      <td>Ricca Chemical (Arlington, TX)</td>
      <td>Ref# 8310-32</td>
      <td>ELISA Stop Buffer</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Fluoroshield with DAPI</td>
      <td>Sigma-Aldrich</td>
      <td>Ref# F6057</td>
      <td>Immunofluorescence reagent</td>
    </tr>
  </tbody>
</table>

### Analysis of spatial transcriptomics dataset

Tissues from infected mice were harvested at the indicated timepoints, which were chosen based on key events observed via H&E staining (Harvest et al., 2023). Spatial data were generated in Harvest et al., 2023 using the 10X Genomics Visium Platform. We were most interested in the immune cells present within the distinct zones of each lesion, and the adjacent healthy hepatocytes. Therefore, we used Loupe Browser v7.0 to visualize the H&E-stained tissues and manually select spots of interest. We deselected spots that were distant from infected lesions, while selecting the lesions and surrounding healthy hepatocytes. To account for cell-to-cell variation, especially across tissues, pre-processing included normalization using sctransform (Hafemeister and Satija, 2019). To further analyze the spatial transcriptomics dataset of the selected spots, we used the Seurat package in RStudio to analyze gene expression over time and space. UMAP plots, SpatialDimPlots, SpatialFeaturePlots, ggplots, and Violin plots were all used to visualize normalized gene expression data.

### Ethics statement and mouse studies

All mice were housed in groups of two to five according to IACUC guidelines at Duke University (under protocols A018-23-01 and A043-20-02). WT C57BL/6 mice (referred to as WT; from Jackson Laboratories) or Ccr2RFP mice (referred to as Ccr2–/–; originally generated in Saederup et al., 2010) were used as indicated. Mice were moved to a BSL2 facility a minimum of 3 days prior to treatment. For experiments involving infection, mice were monitored every 24 hr for signs of illness. After the appearance of symptoms, mice were monitored every 12 hr. Mice showing sever signs of illness were euthanized according to previously established euthanasia criteria.

### Treatment of mice with reparixin

Stock solutions of reparixin were prepared in PBS with gentle warming for a final concentration of 20 mg/kg in 200 µl PBS. Mice were injected subcutaneously with 200 µl of appropriate reparixin stock or with 200 µl PBS (control).

### Preparation of inoculum

Bacteria were grown overnight on brain heart infusion (BHI) agar plates (C. violaceum ATCC strain 12472) at 37°C and stored at room temperature for no more than 2 weeks. To prepare infectious inocula, bacteria were cultured in 3 ml BHI broth with aeration overnight at 37°C before being diluted in PBS to indicated infectious inoculum.

### In vivo infections

For in vivo infections, 8- to 10-week-old, age- and sex-matched mice were infected as previously described (Harvest et al., 2023). Mice were infected intraperitoneally with indicated number of bacteria in 200 µl PBS. Whole livers and spleens were harvested at indicated timepoints.

### Plating for CFUs

At the indicated DPI, mice were euthanized and the spleen and liver were harvested for quantification of bacterial burdens as previously described (Harvest et al., 2023). Briefly, spleens were placed in a 2-ml homogenizer tube with 1 large metal bead and 1 ml sterile PBS, and whole livers were placed in a 7-ml homogenizer tube with 1 large metal bead and 3 ml sterile PBS. Tube weights were recorded before and after tissue harvest to normalize CFUs/volume/tissue. After homogenizing, 1:5 serial dilutions were performed in sterile PBS, and dilutions were plated on BHI in triplicate or quadruplicate. The following day, bacterial colonies were counted and CFU burdens calculated.

### Flow cytometry

At the indicated DPI, mice were euthanized and the spleen, liver, and whole blood were harvested for flow cytometry as previously described (Harvest et al., 2023). For experiments involving whole blood, cardiac puncture was used to collect 100 µl whole blood prior to perfusion with PBS through the vena cava as described in Mendoza et al., 2022. Briefly, whole livers were minced on ice using scissors and incubated in digestion buffer (100 U/ml Collagenase Type IV in DMEM supplemented with 1 mM CaCl2 and 1 mM MgCl2) for 40 min in a 37°C water bath with intermittent vortexing. Digested livers were homogenized through a 40-µm cell strainer, followed by washing with RPMI (supplemented with 1× Pen/Strep and 1% FBS) and centrifugation at 300 × g for 8 min. Leukocytes from the liver were further isolated using a Percoll gradient where samples were resuspended in 45% Percoll with an 80% Percoll underlay, and spun at 800 × g for 20 min with no brake. For spleens, tissues were mechanically homogenized through a 70-µm strainer, followed by washing and centrifugation at 300 × g for 5 min. Red blood cells were lysed with 1× RBC Lysis Buffer according to product manual (note: whole blood was stained with Ly6G at room temperature prior to RBC lysis. Blood samples were treated identically to liver and spleen samples thereafter). Liver and spleen samples were counted using trypan blue, and 1 × 106 cells per tissue per mouse were stained for various cell markers: Mouse BD Fc Block (1 µg), rat anti-mouse Ly6G in BV421 (1:300), rat anti-mouse CD68 in FITC (1:300) for 30 min. For CD68, staining was performed using Intracellular Fixation & Permeabilization Buffer according to product manual. For each sample, 10,000 events were acquired on a BD LSRFortessa X-20 Cell Analyzer at the Duke Flow Cytometry Core Facility. Samples were analyzed using FlowJo (for Windows, version 10.7.1).

### ELISA

At 3 DPI, mice were euthanized and whole blood (about 500 µl) and a piece of liver were harvested for ELISA. Whole blood and liver tissue were collected as described for flow cytometry, except whole blood was allowed to coagulate at room temperature for 30 min before separating the serum through centrifugation at 10,000 × g for 5 min at 4°C. Serum was collected and stored at −80°C until analysis. Following perfusion, a piece of liver tissue containing visible granulomas was harvested and stored at −80°C. Liver pieces were then homogenized as described for CFU enumeration, except 30 µl T-PER per 5 mg tissue was used in place of PBS. Homogenates were incubated on ice for 2 hr prior to analysis. Serum and liver samples were analyzed for CCL2 according to ELISA kit protocol, and plates read on a BioTek Synergy H1 microplate reader. Calculations were performed in Excel.

### Histology and IHC

To prepare paraffin-embedded tissues, whole livers were harvested at the indicated DPI and submerged in 20 ml of 10% neutral buffered formalin. Samples were gently inverted every day for a minimum of 3 days before being transferred to tissue cassettes and given to the Histology Research Core at the University of North Carolina at Chapel Hill. The research core performed tissue embedding, serial sectioning, slide mounting, and staining of H&E samples. For IHC, serial sections were then processed and stained as described in Harvest et al., 2023. Washes were performed in 1× TBS-T. Primary antibodies were diluted in SignalStain antibody diluent, and included: rabbit anti-C. violaceum (1:2000), rat anti-Ly6G (1:300), and rat anti-CD68 (1:200). Slides were incubated in primary antibody overnight at 4°C in a humidity chamber. Prior to staining with secondary antibody, endogenous peroxidase activity was blocked using 3% H2O2. Slides were incubated in secondary antibody (SignalStain Boost HRP anti-rabbit or ImmPRESS HRP anti-rat) at room temperature for 30 min. Incubation with DAB Substrate Kit was performed for 30 s to 2 min, depending on the intensity of signal. Slides were counter-stained with hematoxylin for 5 s to 1 min, depending on the intensity of the DAB, and then dipped in bluing reagent for 1 min. After dehydration, slides were covered with Permount mounting medium and a coverslip. Importantly, WT slides and Ccr2–/– slides were stained side-by-side.

### Immunofluorescence

To prepare frozen tissues, livers were perfused with 2% paraformaldehyde (PFA) (diluted in PBS) through the vena cava (Mendoza et al., 2022). Individual lobes of the liver were excised and stored in 2% PFA overnight at 4°C. Tissues were subsequently stored for 48 hr in 30% sucrose at 4°C. Finally, tissues were frozen in O.C.T. compound on dry ice before being stored at −80°C. Slides with 5-µm thick tissue sections were prepared using a Thermo Scientific CryoStar NC70 Cryostat, and slides were stained as described in Harvest et al., 2023.

### Microscopy

Histology, IHC, and immunofluorescence samples were analyzed on a KEYENCE All-in-One Microscope BZ-X800. For immunofluorescence imaging, exposure times were set so that uninfected liver appeared negative, and exposure times were maintained between samples. Immunofluorescent images were further analyzed in BZ-X800 Analyzer. Histology and IHC images were further analyzed in Fiji by ImageJ.

### Statistics

Statistical analysis was performed using GraphPad Prism 9.5.1. For survival analysis, the Mantel–Cox test was used to compare WT and Ccr2–/– mice. For bacterial burdens, data were first assessed for normality using the Shapiro–Wilk test. For two groups, a two-tailed t-test (or Mann–Whitney for abnormally distributed data) was used. For more than two groups, a two-way ANOVA was used.
