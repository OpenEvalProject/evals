# Quantitative proteomics reveals the selectivity of ubiquitin-binding autophagy receptors in the turnover of damaged lysosomes by lysophagy

## Authors

- Vinay V Eapen<sup>1</sup> ([ORCID: 0000-0002-8023-387X](https://orcid.org/0000-0002-8023-387X))
- Sharan Swarup<sup>1</sup> ([ORCID: 0000-0003-0226-5582](https://orcid.org/0000-0003-0226-5582))
- Melissa J Hoyer<sup>1</sup> ([ORCID: 0000-0003-0858-4998](https://orcid.org/0000-0003-0858-4998))
- Joao A Paulo<sup>1</sup>
- J Wade Harper<sup>1</sup> ([ORCID: 0000-0002-6944-7236](https://orcid.org/0000-0002-6944-7236)) †

### Affiliations

1. Department of Cell Biology, Harvard Medical School, Boston Boston United States
2. Aligning Science Across Parkinson’s (ASAP) Collaborative Research Network Chevy Chase United States

† Corresponding author

## Abstract

Removal of damaged organelles via the process of selective autophagy constitutes a major form of cellular quality control. Damaged organelles are recognized by a dedicated surveillance machinery, leading to the assembly of an autophagosome around the damaged organelle, prior to fusion with the degradative lysosomal compartment. Lysosomes themselves are also prone to damage and are degraded through the process of lysophagy. While early steps involve recognition of ruptured lysosomal membranes by glycan-binding galectins and ubiquitylation of transmembrane lysosomal proteins, many steps in the process, and their interrelationships, remain poorly understood, including the role and identity of cargo receptors required for completion of lysophagy. Here, we employ quantitative organelle capture and proximity biotinylation proteomics of autophagy adaptors, cargo receptors, and galectins in response to acute lysosomal damage, thereby revealing the landscape of lysosome-associated proteome remodeling during lysophagy. Among the proteins dynamically recruited to damaged lysosomes were ubiquitin-binding autophagic cargo receptors. Using newly developed lysophagic flux reporters including Lyso-Keima, we demonstrate that TAX1BP1, together with its associated kinase TBK1, are both necessary and sufficient to promote lysophagic flux in both HeLa cells and induced neurons (iNeurons). While the related receptor Optineurin (OPTN) can drive damage-dependent lysophagy when overexpressed, cells lacking either OPTN or CALCOCO2 still maintain significant lysophagic flux in HeLa cells. Mechanistically, TAX1BP1-driven lysophagy requires its N-terminal SKICH domain, which binds both TBK1 and the autophagy regulatory factor RB1CC1, and requires upstream ubiquitylation events for efficient recruitment and lysophagic flux. These results identify TAX1BP1 as a central component in the lysophagy pathway and provide a proteomic resource for future studies of the lysophagy process.

## Introduction

The lysosome—a membrane-bound compartment containing proteolytic enzymes—has several indispensable functions in eukaryotic cells, including a central role in protein homeostasis (Perera and Zoncu, 2016; Saftig and Puertollano, 2021). First, lysosomes play key roles in the degradation and recycling of proteins delivered from the endocytic, phagocytic, and secretory/biosynthetic pathways. Second, lysosomes are the terminal receptacle for a form of protein and organelle turnover called autophagy. In this process, double membrane structures called autophagosomes are built around cargo through a multistep process, culminating in the closure of the autophagosome around the cargo. Closed autophagosomes then fuse with lysosomes, thereby delivering their cargo to the lysosomal lumen for degradation (Yim and Mizushima, 2020). Third, the lysosome serves as a platform for sensing intracellular (cytosolic and intralysosomal) amino acid availability through regulation of the MTOR–MLST8–RPTOR complex by the Ragulator complex on the lysosomal membrane, including amino acids from both endocytic and autophagic pathways (Saxton and Sabatini, 2017). A central element in lysosomal function is the acidification of the organelle during maturation, which promotes the activation of luminal proteolytic enzymes. Processes that lead to damaged lysosomal membranes—including physiological and pathophysiological pathways—can promote loss of the appropriate pH gradient and defective proteostasis. As such, mechanisms have evolved to both repair specific types of membrane damage or in some circumstances promote degradation of the damaged organelle by a process referred to as lysophagy (Maejima et al., 2013; Papadopoulos and Meyer, 2017; Papadopoulos et al., 2020; Yim and Mizushima, 2020).

Several mechanisms for recognition of damaged membrane-bound organelles for selective autophagy have been identified. These processes—referred to as organellophagy—generally fall into two classes—ubiquitin (Ub)-dependent and Ub-independent (Anding and Baehrecke, 2017; Khaminets et al., 2016). In Ub-independent forms of organellophagy (e.g. ER-phagy), receptor proteins typically embedded in the cognate membrane are directly recognized by the autophagic machinery to facilitate engulfment in response to regulatory signals. These cargo receptors employ LC3-interacting region (LIR) motifs to associate with the LIR-docking site (LDS) in one or more of six ATG8 adaptor proteins that are located in the growing autophagosomal membrane by virtue of attachment to phosphatidylethanolamine via their C-terminal glycine residue (Gubas and Dikic, 2021; Johansen and Lamark, 2020). In contrast, Ub-dependent forms of organellophagy frequently employ a multistep process involving: (1) sensing of organelle damage, (2) ubiquitylation of one or more proteins associated with the membrane of the damaged organelle, (3) recruitment of one or more Ub-binding autophagy receptors containing LIR or other motifs that recruit autophagic machinery, and (4) expansion of the autophagic membrane around the organelle, thereby facilitating delivery to the lysosome (Gubas and Dikic, 2021; Johansen and Lamark, 2020; Khaminets et al., 2016; Lamark and Johansen, 2021). This pathway is perhaps best understood in the context of damaged mitochondria, where the Parkin Ub ligase catalyzes ubiquitylation of mitochondrial outer membrane proteins, followed by recruitment of multiple Ub-binding autophagy receptors including Optineurin (OPTN), CALCOCO2 (also called NDP52), SQSTM1 (also called p62), TAX1BP1, and NBR1 to the outer membrane (Harper et al., 2018; Heo et al., 2015; Lazarou et al., 2015; Moore and Holzbaur, 2016; Ordureau et al., 2014; Ordureau et al., 2018; Ordureau et al., 2020; Pickrell and Youle, 2015; Richter et al., 2016; Wong and Holzbaur, 2014). However, available data suggest that only OPTN and to a lesser extent CALCOCO2 are necessary for ultimate delivery of damaged mitochondria to lysosomes in the majority of cell types examined thus far (Heo et al., 2015; Lazarou et al., 2015; Evans and Holzbaur, 2020). The mechanistic basis for the utilization of distinct Ub-binding autophagy receptors for specific types of organellophagy is largely unknown, but a common feature appears to be a role for TBK1-dependent phosphorylation of the receptor and/or other components at the ‘synapse’ between the autophagosome and target organelle (Harding et al., 2021; Heo et al., 2015; Heo et al., 2019; Moore and Holzbaur, 2016; Richter et al., 2016; Wild et al., 2011). In the case of OPTN, its phosphorylation by TBK1 promotes association with Ub chains in the context of mitophagy (Heo et al., 2015; Richter et al., 2016).

Previous studies have begun to map out pathways by which damaged lysosomes are selected for lysophagy (Figure 1A). In response to rupture of the lysosomal membrane, specific galectins (principally LGALS3 and LGALS8, but LGALS1 and LGALS9 have also been shown to be recruited) bind to glycosylated luminal domains of lysosomal transmembrane proteins, while ubiquitylation of lysosomal membrane proteins occurs with kinetics similar to that of galectin recruitment to initiate lysophagy (Aits et al., 2015; Maejima et al., 2013; Jia et al., 2018). Multiple steps in the ubiquitylation process that have been proposed include: (1) assembly of K63-linked and subsequently K48-linked Ub chains on lysosomal proteins, and (2) removal of K48-linked conjugates by the p97 (also called VCP) AAA+ ATPase in combination with the deubiquitylating enzyme YOD1 (Papadopoulos et al., 2017). Depletion of the E2 Ub-conjugating enzyme UBE2QL1 dramatically reduces the extent of K48 Ub chain synthesis and impairs K63 Ub chain synthesis (Koerver et al., 2019). Multiple E3 Ub ligases have been proposed to ubiquitylate the lysosomal surface, including SCFFBXO27 and the LGALS3-binding TRIM16 RING E3, but precisely how these E3s promote the pathway is poorly understood (Chauhan et al., 2016; Yoshida et al., 2017). Some aspects of this pathway have parallels with xenophagy, the process by which intracellular bacteria is removed by autophagy, including early ubiquitylation steps and recruitment of LGALS8 (Thurston et al., 2009; Thurston et al., 2012). In addition, multiple Ub-binding cargo receptors including OPTN, CALCOCO2, and TAX1BP1 are recruited to ubiquitylated bacteria and are required for efficient xenophagy in various contexts (Thurston et al., 2009; Thurston et al., 2012; Tumbarello et al., 2015; Wild et al., 2011). While multiple cargo receptors have been reported to be recruited to damaged lysosomes (Bussi et al., 2018; Davis et al., 2021; Koerver et al., 2019), the underlying mechanisms for recruitment, the identity of the receptors critical for lysophagic flux, and the reasons for the diversity of receptors that are recruited remain unknown.

![Figure 1.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig1-v2.jpg)

**Figure 1.:** (A) Scheme depicting major steps in lysophagy and the approaches employed to elucidate components of the pathway. (B) Scheme for tandem mass tagging (TMT)-based proteomics of lysosomes from HeLa cells in response to lysosome rupture by glycyl-l-phenylalanine 2-naphthylamide (GPN). Cells expressing TMEM192-HA were left untreated or treated with GPN for the indicated period of time (in duplicate) and cell lysates subjected to a Lyso-IP protocol prior to TMT-based proteomics. (C) Volcano plot for GPN (22.5 min)-treated cells versus untreated Lyso-IP samples (Log2 FC versus −Log10 p-value) based on the TMT experiment in (B). Specific categories of proteins are indicated by colored circles. (D) GO enrichment (component) for proteins that accumulate on lysosomes in response to GPN treatment. (E) Time course reflecting the dynamics of recruitment or loss of selected proteins from lysosomes in response to GPN treatment. Error bars represent SD from two biological replicates. (F) Dynamics of recruitment or loss of proteins linked with autophagy (top), ESCRT (middle), and MTOR (lower) pathways in association with lysosomes upon GPN treatment. All the lines for each category represent individual proteins (see Supplementary file 2), and proteins with the most highly dynamic changes are indicated as dashed lines. (G) HeLa cells were either left untreated or treated with GPN for 45 min prior to isolation of lysosomes by Lyso-IP. Samples were then subjected to immunoblotting with the indicated antibodies.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Scheme depicting the targeting strategy for insertion of a 3 x-HA epitope at the C-terminus of the TMEM192 gene in HeLa cells. (B) Whole cell extracts from the indicated HeLa cells (CONTROL or TMEM192HA) were immunoblotted using the indicated antibodies. (C) Immunostaining of HeLa TMEM192HA cells with α-TMEM192, α-NPC1 as a lysosome marker, and α-HA. Nuclei were stained with DAPI. (D) CONTROL or TMEM192HA cells were subjected to Lyso-IP and immune complexes as well as input cell extracts subjected to immunoblotting for the indicated proteins. (E) Volcano plot for 6-plex TMT experiment comparing Lyso-IP from TMEM192HA-tagged cell extracts versus CONTROL cells lacking the HA tag (−Log10 p-value versus Log2 FC TMEM192HA Lyso-IP versus control cell Lyso-IP). All proteins quantified are indicated in grey and lysosomal proteins are indicated in red and show strong enrichment in the Lyso-IP sample. (F) Violin plots for individual organelles, showing enrichment of lysosomal proteins in the Lyso-IP-enriched proteins. (G) Heatmap of Log2 FC for individual lysosomal proteins annotated based on their localization within lysosomes within the Lyso-IP. (H) Western blot analysis of TMEM192 (bait) levels after Lyso-IP from untreated and GPN-treated HeLa TMEM192HA cells. (I) Volcano plot representation for GPN-treated cells versus untreated Lyso-IP samples (Log2 FC versus −Log10 p-value) for various time points after treatment, based on the TMT experiment in Figure 1B. Specific categories of proteins are indicated by colored circles.

In this study, we set out to systematically examine lysophagy using a series of complementary proteomic approaches with the goal of identifying previously unrecognized machinery required for lysophagic flux. Using lysosomal immunoprecipitation (Lyso-IP) in the context of lysosomal membrane damage, we identified several Ub-binding cargo receptors and ATG8 proteins that are rapidly recruited to these organelles, and verified that LGALS1, LGALS3, and LGALS8 are recruited as well. Parallel APEX2-driven proximity biotinylation experiments using ATG8 proteins and specific galectins identified a cohort of lysosomal proteins, ESCRT III complex members, and autophagy regulatory proteins that are dramatically enriched during lysophagic flux, including specific Ub-binding cargo receptors. In order to assess the functional roles of various components in lysophagy, we developed LGALS3-based fluorescent flux reporters that monitor delivery of damaged lysosomes to healthy lysosomes via autophagy. We systematically examined the requirement of cargo receptors that are recruited to damaged lysosomes in HeLa cells, and found that while cells lacking TAX1BP1 were completely deficient for lysophagy, cells lacking OPTN, CALCOCO2, or SQSTM1 still maintained significant lysophagic flux, indicating that TAX1BP1 plays a critical nonredundant function. Similarly, human embryonic stem (ES) cell-derived induced neurons (iNeurons) lacking TAX1BP1 are also defective for lysophagic flux. Lysophagic flux via TAX1BP1 required its N-terminal SKICH domain, as well as Ala-114 within the SKICH domain, which is known to function in the recruitment of both the TBK1 protein kinase via the NAP1 adaptor and the RB1CC1 subunit of the ULK1 kinase complex (Fu et al., 2018; Ohnstad et al., 2020). Consistent with a role for TBK1, cells lacking TBK1 or addition of a small molecular inhibitor of TBK1 blocks lysophagic flux. Additional experiments indicate that recruitment of TAX1BP1 and OPTN to damaged lysosomes is promoted by an upstream Ub signal. These data provide a resource for factors involved in lysophagy and reveal a unique role for TAX1BP1 in the removal of damaged lysosomes that appear to be distinct from the mechanisms used for removal of mitochondria downstream of Parkin, which relies primarily on OPTN and CALCOCO2.

## Results

### Quantitative lysosomal proteomics during lysophagy

Previous studies have revealed that lysosomal membrane damage can result in increased ubiquitylation of lysosomal proteins as well as the recruitment of specific galectins (Aits et al., 2015; Jia et al., 2018; Jia et al., 2020a; Jia et al., 2020b; Maejima et al., 2013; Yoshida et al., 2017). We set out to employ a suite of unbiased quantitative proteomics approaches to systematically identify proteins that are dynamically recruited to damaged lysosomes using the well-characterized damaging agents L-Leucyl-L-Leucine methyl ester (LLOMe) or glycyl-L-phenylalanine 2-naphthylamide (GPN) (Figure 1A). LLOMe enters the lysosomal system via endocytosis and forms conjugates that can specifically rupture lysosomal membranes on a subset of lysosomes to initiate lysophagy, while GPN promotes lysosomal osmotic swelling and rupture (Bright et al., 2016; Jadot et al., 1984; Maejima et al., 2013; Skowyra et al., 2018). To facilitate quantitative identification of candidates, we merged the Lyso-IP approach (Abu-Remaileh et al., 2017) with Tandem Mass Tagging (TMT)-based proteomics via synchronous precursor selection (SPS) and quantification of reporter ions using MS3 (McAlister et al., 2014). Lysosomes in HeLa cells were tagged by integrating a 3X-HA (HA) tag into the cytosolic C-terminus of TMEM192 gene via CRISPR-Cas9 (Figure 1—figure supplement 1A-D) and α-HA immunoprecipitates from these cells yielded an enrichment of transmembrane, luminal, and membrane-associated lysosomal proteins when compared with untagged cells, as shown for the HeLa cell system (Figure 1—figure supplement 1E-G, Supplementary file 1).

To identify proteins recruited to lysosomes during lysophagy, HeLaTMEM192-HA cells in biological duplicates were left untreated or treated with GPN for 22.5, 45, 90, or 180 min, followed by Lyso-IP and analysis by TMT-MS3 (Figure 1B and Supplementary file 2). This resulted in the identification of several proteins that were enriched on ruptured lysosomes at one or more time points post-GPN, including multiple ATG8 proteins (MAP1LC3B, GABARAPL1, and GABARAPL2), galectins (LGALS1, LGALS3, and LGALS8), and the Ub-binding cargo receptors (CALCOCO2 and SQSTM1) with Log2 fold change (FC) >0.5 (p-value <0.05) for at least one time point (Figure 1C–E, Figure 1—figure supplement 1E). TAX1BP1 was also found to be slightly enriched at 22.5 min, but was also found constitutively in undamaged lysosomes (Figure 1—figure supplement 1E, Supplementary files 1 and 2). Previous studies have indicated that damaged lysosomal membranes may also be subject to repair by components of the ESCRT system (Jia et al., 2020b; Radulovic et al., 2018; Skowyra et al., 2018). Consistent with this, we observed transient enrichment of ESCRT-III components CHMP1B, CHMP5, CHMP6, and PCDC6IP by Lyso-IP (Figure 1F). We also observed a reduction in the abundance of the MTORC1 complex (MLST8, RPTOR, and MTOR) post-damage, consistent with previous reports that lysosomal damage leads to loss of this kinase complex from the lysosomal surface (Figure 1C, E and F; Jia et al., 2018). We verified enrichment of galectins, lipidated forms of MAP1LC3B and GABARAP, OPTN, CALCOCO2, TAX1BP1, and SQSTM1, as well as loss of RPTOR and MTOR, using immunoblotting of Lyso-IP fractions upon lysosomal damage (Figure 1G). The recruitment of these candidate Ub-binding cargo receptors is consistent with a previously reported role for lysosomal ubiquitylation in response to rupture (Koerver et al., 2019; Yoshida et al., 2017).

### Proximity biotinylation of autophagy receptors and galectins during lysosomal damage

The rapid recruitment of ATG8 and galectin proteins to damaged lysosomes (Figure 1E) led us to employ APEX2-driven proximity biotinylation as a complementary approach to identify proteins that may link the autophagic machinery with ruptured lysosomes (Figure 2A and B). To initially check for fusion protein function, cells stably expressing FLAG-APEX2 fusions with GABARAPL2 (WT or LDS mutant Y49A/L50A) or MAP1LC3B (WT or LDS mutant K51A) (Mizushima, 2020; Figure 2—figure supplement 1A) were treated for 1 hr with LLOMe prior to immunostaining to examine recruitment of the FLAG-tagged APEX2 protein to lysosomes marked with α-LAMP1 antibodies (Figure 2—figure supplement 1B). Both WT constructs formed more numerous and larger puncta than the LDS mutants, consistent with enhanced lysosomal recruitment. We then treated these cells together in biological triplicates (60 min) or duplicate (0 min) with LLOMe (1 hr) in the presence of biotin phenol, followed by H2O2 (1 min), and immediately processed for biotin enrichment and proteomics in two 10-plex TMT experiments (Figure 2B, Supplementary file 3). From ~1300 proteins identified with APEX2-MAP1LC3B, we identified 46 proteins that were enriched (Log2 FC >1.0; p-value <0.05) in the presence of LLOMe (Figure 2C) with only the lysosomal compartment being significantly enriched when compared with several subcellular compartments (Figure 2D). Similarly, APEX2-GABARAPL2 was also enriched in autophagy receptors and lysosomal proteins (Figure 2E and F), with numerous proteins being in common with APEX2-MAP1LC3B-enriched proteins (Figure 2G, Figure 2—figure supplement 1C). Five major functional classes of proteins were identified with one or both ATG8 proteins: (1) Ub-binding autophagy receptors (OPTN and CALCOCO2), (2) resident lysosomal membrane proteins (LAMP1, LAMP2, and SCARB2), (3) galectins (LGALS1, LGALS3, and LGALS8), (4) luminal resident lysosomal proteins (GBA, HEXB, GLB1, PSAP, PLD3, CTSZ, CTSA, CTSD, CTSC, and GNS), and (5) components of the Ragulator/Lamtor complex (RRAGC and LAMTOR1) known to associate with the cytosolic face of the lysosomal membrane (Saxton and Sabatini, 2017). Interestingly, proximity biotinylation of a subset of enriched proteins with GABARAPL2, including OPTN, LAMP1, and LAMP2, was partially dependent upon the presence of an intact LDS, although the effect was much less dramatic with the MAP1LC3BK51A mutant (Figure 2H, I, Figure 2—figure supplement 1D,E).

![Figure 2.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig2-v2.jpg)

**Figure 2.:** (A) Scheme depicting proximity biotinylation of proteins in response to recruitment of ATG8 proteins to damaged lysosomes. (B) Experimental workflow for ATG8 proximity biotinylation. APEX2-tagged GABARAPL2 (or the corresponding Y49A mutant) or MAP1LC3B (or the corresponding K51A mutant) expressed in HeLa cells were subjected to proximity biotinylation 60 min post-LLOMe treatment using 10plex TMT. (C) Volcano plot for LLOMe (60 min)-treated cells versus untreated cells (Log2 FC versus −Log10 p-value) for APEX-MAP1LC3B-based proximity biotinylation based on the TMT experiment in B. Specific categories of proteins are indicated by colored circles. (D) Log2 FC for individual proteins localized to the indicated subcellular compartments found to be enriched in biotinylated proteins from cells expressing APEX2-MAP1LC3B. Mean and standard deviation are calculated from two untreated and three treated biological replicates. (E) Volcano plot for LLOMe (60 min)-treated cells versus untreated cells (Log2 FC versus −Log10 p-value) for APEX-GABARAPL2-based proximity biotinylation based on the TMT experiment in (B). Specific categories of proteins are indicated by colored circles. (F) Log2 FC for individual proteins localized to the indicated subcellular compartments found to be enriched in biotinylated proteins from cells expressing APEX2-GABARAPL2. Mean and standard deviation are calculated from two untreated and three treated biological replicates. (G) Summary of overlap between biotinylated proteins found with MAP1LC3B and GABARAPL2 APEX2 proteomics. Proteins enriched with Log2 FC >1.0 and p-value <0.05 were included. Proteins identified in both APEX2 experiments are indicated. (H) Plot of means of Log2 FC for biotinylated proteins in cells expressing APEX-GABARAPL2 or the Y49A/L50A mutant. Means are calculated from two untreated and three treated biological replicates. (I) Plot of means of Log2 FC for biotinylated proteins in cells expressing APEX-MAP1LC3B or the Y49A/L50A mutant. Means are calculated from two untreated and three treated biological replicates.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Extracts from HeLa cells stably expressing the indicated APEX2 fusion proteins were subjected to immunoblotting with the indicated antibodies. (B) HeLa cells expressing APEX2-GABARAPL2 or APEX2-MAP1LC3B were treated with LLOMe (1 hr) followed by immunofluorescence using α-LAMP1 to detect lysosomes and α-Flag to detect the Flag epitope on the APEX2 portion of the fusion protein. Scale bar = 25 μm. Zoom-in panels 15 μm × 25 μm. (C) Summary of proteins enriched by proximity biotinylation of GABARAPL2 and MAP1LC3B (Log2 FC >1.0 and p-value <0.05). (D) Histogram showing the effect of mutation of the LIR-binding regions of MAP1LC3B on proximity biotinylation. FC for TMT intensities of both untreated samples is normalized to 1.0 for WT and mutant. Mean and standard deviation are calculated from two untreated and two treated biological replicates. (E) Histogram showing the effect of mutation of the LIR-binding regions of GABARAPL2 on proximity biotinylation. FC for TMT intensities of both untreated samples are normalized to 1.0 for WT and mutant. Mean and standard deviation are calculated from two untreated and two treated biological replicates.

In an orthogonal set of two 11-plex TMT experiments, we performed proximity biotinylation with APEX2-tagged LGALS1, LGALS3, and LGALS8 (Figure 3A and B and Supplementary file 4). Stably expressed APEX2-tagged galectins (Figure 3—figure supplement 1A) were recruited to lysosomes in response to LLOMe, based on immunofluorescence in fixed cells, indicating that the APEX2 fusions were functional (Figure 3—figure supplement 1B). Similar to the APEX2-ATG8 fusions, APEX2-LGALS1, 3, and 8 all displayed enriched biotinylation of the lysosomal compartment, consistent with the known translocation of galectins to sites of lysosome membrane damage (Figure 3C–F). Beyond shared lysosomal enrichment, the proximity interactomes of galectins 1, 3, and 8 displayed key differences. Notably, Gene Ontology (GO) analysis of the galectin interactomes indicated that only LGALS8 showed a clear increased interaction with terms associated with autophagy and MTOR signaling driven by preferential enrichment of RRAGC, LAMTOR1, and LAMTOR2 (Figure 3G, Figure 4—figure supplement 1A). The specificity of LGALS8 interactions with members of the MTOR complex is consistent with recent reports demonstrating its role in modulating MTOR signaling during lysosomal stress (Jia et al., 2018).

![Figure 3.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig3-v2.jpg)

**Figure 3.:** (A) Scheme depicting proximity biotinylation of proteins in response to recruitment of LGALS1, LGALS3, and LGALS8 proteins to damaged lysosomes. (B) Experimental workflow for galectin proximity biotinylation. APEX2-tagged LGALS1, LGALS3, and LGALS8 expressed in HeLa cells were subjected to proximity biotinylation 60 min post-LLOMe treatment using 10-plex TMT. (C) Volcano plot for LLOMe (60 min)-treated cells versus untreated cells (Log2 FC versus −Log10 p-value) for APEX-LGALS8-based proximity biotinylation based on the TMT experiment in (B). Specific categories of proteins are indicated by colored circles. (D) Volcano plot for LLOMe (60 min)-treated cells versus untreated cells (Log2 FC versus −Log10 p-value) for APEX-LGALS3-based proximity biotinylation based on the TMT experiment in B. Specific categories of proteins are indicated by colored circles. (E) Volcano plot for LLOMe (60 min)-treated cells versus untreated cells (Log2 FC versus −Log10 p-value) for APEX-LGALS1-based proximity biotinylation based on the TMT experiment in B. Specific categories of proteins are indicated by colored circles. (F) Log2 FC for individual proteins localized to the lysosomal compartment found to be enriched in biotinylated proteins from cells expressing the indicated APEX2-galectin protein. Mean and standard deviation are calculated from two untreated and two treated biological replicates. (G) GO: process enrichment categories for APEX2-LGALS8.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Extracts from HeLa cells stably expressing the indicated APEX2 fusion proteins were subjected to immunoblotting with the indicated antibodies. (B) HeLa cells expressing the indicated APEX2-fusion proteins with galectins were treated with LLOMe (1 hr) followed by immunofluorescence using α-LAMP1 to detect lysosomes and α-FLAG to detect the Flag epitope on the APEX2 portion of the fusion protein. Scale bar = 25 μm. Zoom-in panels 15 μm × 25 μm.

### Lysophagy proteome landscape

In order to develop a lysophagy proteome landscape, we organized proteins that were detected as being enriched by Lyso-IP and proximity biotinylation of ATG8 and galectin proteins based on functional categories (Figure 4A, Figure 4—figure supplement 1A). All proximity biotinylation experiments showed strong enrichment for GO terms linked with lysosomes, autophagy, and membrane fusion, among other terms (Figure 4—figure supplement 1A). All three galectins were found to associate with a cohort of luminal hydrolytic enzymes (e.g., CTSB and CTSD) and lipid modifying proteins (e.g., GLB1, HEXB, and GBA), indicating that they all likely access the lysosomal lumen upon damage (Figure 4A). Similarly, both LGALS1 and LGALS8 APEX2 experiments resulted in enrichment of LGALS3, suggesting that individual galectins themselves are in close proximity to each other within damaged lysosomes (Figure 4A). Interestingly, all three galectins were found to biotinylate lysosomal membrane proteins LAMP1 and LAMP2, but APEX2-LGALS8 was selectively enriched in CD63, TMEM192, and several V-ATPase subunits (Figure 4A). Many proteins found with APEX2-ATG8 proteins were also identified with galectin proximity biotinylation, including both luminal proteins and lysosomal membrane proteins, as well as mTOR regulatory components (Figure 4A). Interestingly, although overexpressed LGALS9 has been reported to be recruited to damaged lysosomes and to be required for lysosomal ubiquitylation (Jia et al., 2018), we failed to detect endogenous LGALS9 in any of the proteomics experiments performed here. This dataset provides a rich resource for future studies in the lysophagy pathway.

![Figure 4.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig4-v2.jpg)

**Figure 4.:** (A) Summary of proteins in proximity to galectins and integration with associations found with APEX2-ATG8 (bold) and Lyso-IP (underline). Other functional classes are indicated. (B) Localization of LGALS3 with LAMP1 and MAP1LC3B in response to lysosomal damage. Cells were treated with LLOMe for 1 hr and the LLOMe washed out for 4 hr prior to immunofluorescence using the indicated antibodies and imaging by confocal microscopy. Scale bars 10 μm. Zoom-in panels, 10 μm × 10 μm. (C) Cells were left untreated (Untreated), treated with LLOMe for 1 hr and either fixed (LLOMe 1 hr) or the LLOMe was washed out for 4 hr prior to fixation (LLOMe 1 hr+ washout 4 hr). Immunofluorescence was done using α-OPTN/α-LAMP1 and imaging by confocal microscopy. Scale bars 10 μm. Zoom-in panels, 10 μm × 10 μm. (D) Cells were treated as in (C). Immunofluorescence was done using α-TAX1BP1/α-LAMP1 and imaging by confocal microscopy. Scale bars 10 μm. Zoom-in panels, 10 μm × 10 μm. (E) Cells were treated as in (C). Immunofluorescence was done using α-CALCOCO2/α-LAMP1 and imaging by confocal microscopy. Scale bars 10 μm. Zoom-in panels, 10 μm × 10 μm. (F) Quantification of OPTN localization at LAMP1 lysosomes using Mander’s overlap coefficient (MOC). 23 (0 hr), 19 (1 hr), and 22 (4 hr washout) cells were analyzed for MOC. ***p < 0.001. + marks the mean and the line marks the median. The plot represents merged data from three biological replicates for each condition. (G) Quantification of TAX1BP1 localization at LAMP1 lysosomes using Mander’s overlap coefficient (MOC). 20 (0 hr), 17 (1 hr), and 22 (4 hr washout) cells were analyzed for MOC. ***p < 0.001. + marks the mean and the line marks the median. The plot represents merged data from three biological replicates for each condition. (H) Quantification of CALCOCO2 localization at LAMP1 lysosomes using MOC. 18 (0 hr), 20 (1 hr), and 21 (4 hr washout) cells were analyzed for MOC. **p < 0.01 and ***p < 0.001. + marks the mean and the line marks the median. The plot represents merged data from three biological replicates for each condition.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Gene Ontology (GO) terms linked with enriched proteins identified by proximity biotinylation of galectins and ATG8 proteins. Analysis was performed using the reduce and visualize gene ontology server (REVIGO) (http://revigo.irb.hr/). (B) HeLa cells expressing the indicated APEX2 constructs were lysed and extracts analyzed by immunoblotting with α-FLAG antibody to detect the expressed APEX-tagged receptor, and α-PNCA as a loading control. (C) Experimental workflow for Ub-binding cargo receptor proximity biotinylation. APEX2-tagged cargo receptors expressed in HeLa cells in biological duplicate were subjected to proximity biotinylation 60-min post-LLOMe treatment using 7-plex TMT and APEX2-GFP as a control. (D) Plot of Log2 FC for all proteins identified in the proximity biotinylation experiment for OPTN as described in C. Means are calculated from biological replicates indicated in C. Specific categories of proteins are indicated by colored circles. Inset: HeLa cells expressing APEX2-FLAG-OPTN were treated with LLOMe (1 hr) followed by immunofluorescence using α-LAMP1 to detect lysosomes (magenta) and α-FLAG (green) to detect the FLAG epitope on the APEX2 portion of the fusion protein. Scale bar = 25 μm. Zoom-in panels 15 μm × 25 μm. (E) Plot of Log2FC for all proteins identified in the proximity biotinylation experiment for SQSTM1 as described in (C). Means are calculated from biological replicates indicated in (C). Specific categories of proteins are indicated by colored circles. Inset: HeLa cells expressing APEX2-FLAG-SQSTM1 were treated with LLOMe (1 hr) followed by immunofluorescence using α-LAMP1 to detect lysosomes (magenta) and α-FLAG (green) to detect the Flag epitope on the APEX2 portion of the fusion protein. Scale bar = 25 μm. Zoom-in panels 15 μm × 25 μm. (F) Plot of Log2 FC for all proteins identified in the proximity biotinylation experiment for TAX1BP1 as described in (C). Means are calculated from biological replicates indicated in (C). Specific categories of proteins are indicated by colored circles. Inset: HeLa cells expressing APEX2-FLAG-TAX1BP1 were treated with LLOMe (1 hr) followed by immunofluorescence using α-LAMP1 to detect lysosomes (magenta) and α-FLAG (green) to detect the FLAG epitope on the APEX2 portion of the fusion protein. Scale bar = 25 μm. Zoom-in panels 15 μm × 25 μm. (G) Plot of Log2 FC for all proteins identified in the proximity biotinylation experiment for CALCOCO2 as described in Figure 3B. Means are calculated from biological replicates indicated in Figure 3B. Specific categories of proteins are indicated by colored circles. Inset: HeLa cells expressing APEX2-FLAG-CALCOCO2 were treated with LLOMe (1 hr) followed by immunofluorescence using α-LAMP1 to detect lysosomes (magenta) and α-FLAG (green) to detect the FLAG epitope on the APEX2 portion of the fusion protein. Scale bar = 25 μm. Zoom-in panels 15 μm × 25 μm.

### Multiple Ub-binding autophagy receptors are recruited to damaged lysosomes

Among the proteins found to be enriched by either APEX2-ATG8, APEX2-galectin, or Lyso-IP was the autophagy cargo receptor CALCOCO2, and in some experiments OPTN and TAX1BP1 were also enriched (Figures 1C, G, 2G). As such, we systematically examined recruitment of cargo receptor proteins to damaged lysosomes using immunofluorescence (Figure 4B–E). As expected, LGALS3 was recruited to LAMP1-positive lysosomes, a subset of which were also positive for MAP1LC3B (Figure 4B). In untreated cells, OPTN, TAX1BP1, and CALCOCO2 displayed diffuse localization with little evidence of colocalization with LAMP1-positive lysosomes (Mander’s overlap coefficient [MOC] <0.02) (Figure 4C–H). However, after addition of LLOMe for 1 hr and after 4 hr washout of LLOMe treatment for 1 hr, there was increased colocalization of these receptors with lysosomes, with TAX1BP1 displaying the most dramatic increase in MOC (a mean of 0.25–0.45 for TAX1BP1) (Figure 4C–H). As an independent approach to examine recruitment of cargo receptors to lysosomes, we employed proximity biotinylation of CALCOCO2, TAX1BP1, SQSTM1, and OPTN, and each APEX2-fusion protein was shown to associate with a subset of lysosomes upon damage (Figure 4—figure supplement 1B-D). We observed enrichment of numerous specific lysosomal proteins, ESCRT and galectins with CALCOCO2, TAX1BP1, SQSTM1, and/or OPTN-APEX2 proteins 60 min after LLOMe treatment, (Figure 4—figure supplement 1B-D; Supplementary file 5).

### Measurement of lysophagic flux with Lyso-Keima

While multiple cargo receptors are recruited to damaged lysosomes (Figure 4C–E; Davis et al., 2021; Koerver et al., 2019; Papadopoulos et al., 2017), to date, the cargo receptors critical for linking damaged lysosomes to the core autophagy machinery have not been clearly delineated, although knockdown of SQSTM1 by RNAi has been reported to result in reduced lysophagic flux (Papadopoulos et al., 2017). We therefore systematically probed cargo receptor involvement in lysophagy. We first developed a tool for the quantitative assessment of lysophagic flux by employing monomeric mKeima (referred to here as Keima) fused with LGALS3, which we term Lyso-Keima (Figure 5A). Keima is a pH-responsive reporter that undergoes a chromophore resting charge-state change upon trafficking to the lysosome (pH of ~4.5) and is stable within the lysosome, allowing flux measurements by flow cytometry or microscopy (Katayama et al., 2011). The Keima protein itself is also stable to lysosomal proteases, and the appearance of a ‘processed’ Keima protein by immunoblotting therefore reveals lysosomal trafficking of the Keima fusion protein (An and Harper, 2018; Katayama et al., 2011). HeLa cells expressing Keima-LGALS3 were treated with LLOMe (1 hr) and then chased with fresh media for the indicated time prior to analysis by imaging, flow cytometry, or immunoblotting for ‘processed’ Keima (Figure 5B–G). Under basal conditions, Keima-LGALS3 was diffusely cytosolic with signal observed only in the 442 nm excitation channel (neutral pH) (Figure 5B). However, after the LLOMe chase (1 hr LLOMe treated and 4–12 hr washout), we observed a dramatic relocalization of the reporter into puncta in the 442 nm channel, consistent with recruitment to damaged lysosomes. Importantly, a large fraction of these puncta displayed a signal ratio greater than one when comparing the 561 nm/442 nm ratio at 12 hr washout, indicative of trafficking of damaged lysosomes into an acidic compartment (Figure 5B–D). The presence of acidic Keima-LGALS3 puncta was completely blocked by the addition of Bafilomycin A1 (a lysosomal acidification inhibitor, BafA) during the washout (Figure 5C–D). This ratio shift in LLOMe chased Keima-LGALS3 cells could also be measured using flow cytometry analysis; the 561 nm/488 nm excitation ratio was increased approximately twofold 1 hr after LLOMe and washout (12 hr) in biological triplicate assays (Figure 5E). This increase was completely blocked by incubation of cells with BafA during the LLOMe washout (Figure 5E, Figure 5—figure supplement 1A). These results are consistent with the hypothesis that damaged Keima-positive lysosomes are trafficked to healthy lysosomes, potentially including those newly generated via the TFEB-mediated transcriptional response, for elimination (Nakamura et al., 2020).

![Figure 5.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig5-v2.jpg)

**Figure 5.:** (A) Scheme depicting measurement of lysophagic flux using Lyso-Keima (Keima-LGALS3). Cells stably expressing Keima-LGALS3 are treated with LLOMe (1 hr), and the Keima-LGALS3 is recruited from the cytosol to damaged lysosomes, representing the initial recruitment step (green dot). After removing LLOMe (washout), damaged lysosomes undergo autophagy-dependent trafficking to a healthy lysosome, leading to a red-shift in Keima fluorescence (red dots) due to the acidic environment of the lysosome. Cells can be analyzed by imaging, flow cytometry or SDS–PAGE for processed Keima. (B) Keima-LGALS3 in untreated HeLa cells or in cells that were treated with LLOMe for 1 hr and the LLOMe washed out for 4 or 12 hr and imaged using excitation at 442 or 561 nm. Scale bar 10 μm. Zoom-in panels, 10 μm × 20 μm. (C) Keima-LGALS3 HeLa cells were either left untreated or treated for 1 hr followed by washout (12 hr) with or without prior addition of TBK1i or BafA. Cells were imaged using excitation at 442 or 561 nm. A ratio of the 561 nm/442 nm images was taken and puncta were identified from this 561 nm/442 nm image. Scale bar 10 μm. Zoom-in panels, 10 μm × 20 μm. (D) Quantification of Keima-positive lysosomes. 69 (untreated), 83 (BafA), and 66 (TBKi) cells were analyzed ****p < 0.0001. + marks the mean and the line is at the median. The plot represents merged data from three biological replicates. (E) Triplicate HeLa cells expressing Keima-LGALS3 were either left untreated or treated for 1 hr followed by washout (12 hr) with or without addition of BafA. Cells were then subjected to flow cytometry to measure the 561 nm/488 nm ratio. All values are normalized to the untreated sample. ****p < 0.0001. The plot represents mean and standard deviation from three biological replicates. (F) Triplicate HeLa cells expressing Keima-LGALS3 were either left untreated or treated for 1 hr followed by washout (12 hr) with or without prior addition of TBK1i, ULK1i, TAK243, and p97i. Cells were then subjected to flow cytometry to measure the 561 nm/488 nm ratio. All values are normalized to the untreated sample. ****p < 0.0001. The plot represents mean and standard deviation from three biological replicates. (G) HeLa cells expressing Keima-LGALS3 were either left untreated or treated for 1 hr followed by washout followed by harvesting at the indicated times. Lysed cells were then subjected to immunoblotting with the indicated antibodies. (H) Cells were left untreated (Untreated), treated with LLOMe for 1 hr and either fixed (LLOMe 1 hr) or the LLOMe was washed out for 4 hr prior to fixation (LLOMe 1 hr + washout 4 hr). Immunofluorescence was done using α-pTBK1/α-LAMP1 and imaging by confocal microscopy. Scale bar = 10 μm. Zoom-in panels, 10 μm × 10 μm. Right: quantification of localization using Mander’s overlap coefficient (MOC). 23 (0 hr), 21 (1 hr), and 18 (4 hr washout) cells were analyzed for MOC. ***p < 0.001. + marks the mean and the line is at the median. The plot represents merged data from three biological replicates. (I) HeLa cells expressing Keima-LGALS3 were either left untreated or treated with LLOMe for 1 hr and then incubated for four or 12 hr post-washout in the presence or absence of either BafA or TBK1i. Cell lysates were subjected to immunoblotting using the indicated antibodies. (J) Triplicate WT, ATG5−/−, or TBK1−/− HeLa cells expressing Keima-LGALS3 were either left untreated or treated for 1 hr followed by washout (4 hr) prior to flow cytometry to measure the 561 nm/488 nm ratio. All values are normalized to the untreated sample within each genotype. The plot represents mean and standard deviation from three biological replicates.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Raw flow cytometry data. HeLa cells expressing Keima-LGALS3 were either left untreated (red), or treated for 1 hr followed by washout (12 hr) with (orange) or without (blue) addition of BafA. Cells were then subjected to flow cytometry to measure the 561 nm/488 nm ratio. (B) HeLa cells expressing Keima-LGALS3 were treated with LLOMe (1 hr) prior to washout for 4 or 8 hr. In one set of samples, the E1 inhibitor TAK243 at 2 μM was added prior to damage. Cell extracts at the indicated time were subjected to immunoblotting with the indicated antibodies.

Previous studies have indicated that lysophagy—as monitored by loss of galectin-positive puncta—requires both p97 activity and the Ub system (Papadopoulos et al., 2017). To further validate Keima-LGALS3 flux, we examined the effect of inhibition of the ubiquitin E1-activating enzyme (UBA1) using the TAK243 small molecule (E1i) (Hyer et al., 2018) and the p97 inhibitor CB-5083 (p97i) (Anderson et al., 2015). TAK243 completely blocked Keima-LGALS3 flux as assessed by both flow cytometry and the Keima-processing assay (Figure 5F and Figure 5—figure supplement 1B), while p97i blocked flux to an extent similar to that see with a small molecule inhibitor of ULK1 (ULK1i) (Figure 5F). Finally, we examined the time course of Keima-LGALS3 flux into the lysosome by using the Keima processing assay (Figure 5G). Cells were treated with LLOMe for 1 hr, washed and extracts from cells harvested at the indicated times were subjected to immunoblotting with α-Keima antibodies. Processed Keima was detected as early as 4 hr post-washout, reached maximal levels at 6 hr, and was maintained through 12 hr (Figure 5G). Taken together, these data indicate that Keima-LGALS3 can be used to monitor lysophagic flux using multiple assay formats.

### TBK1 is required for lysophagic flux

Given the recruitment of LGALS8 and Ub-binding autophagy receptors to damaged lysosomes and previous studies indicating that these proteins can bind and recruit TBK1 to autophagic cargo (Thurston et al., 2009; Thurston et al., 2012; Thurston et al., 2016), we explored TBK1 activation during lysosomal damage. First, as observed previously (Nozawa et al., 2020), we found that phosphorylation of TBK1 on Serine 172 (pS172, referred to as pTBK1) previously linked with activation of its kinase activity (Kishore et al., 2002) is evident after 1 hr of LLOMe and is maintained from 6-8 hr post-washout, returning to baseline by 12 hr in HeLa cells expressing the Keima-LGALS3 reporter (Figure 5G). Similarly, pTBK1 was detected on LGALS3-positive puncta after 1 hr LLOMe treatment and at 4 hr after 1 hr LLOMe treatment by immunofluorescence (mean MOC 0.1–0.3), indicating that the activated kinase is recruited to a subset of damaged lysosomes (Figure 5H). Thus, TBK1 activation and engagement of damaged lysosomes precede the earliest signs of lysophagic flux.

We next examined whether TBK1 was required for lysophagic flux. First, we found that a small molecule TBK1 inhibitor (MRT60821, referred to as TBK1i) added at the time of LLOMe washout, blocked Keima-LGALS3 flux by imaging analysis of acidic puncta (Figure 5C–D), by flow cytometry assays performed in biological triplicate (Figure 5F), and immunoblotting of processed Keima (Figure 5I) to an extent similar to that observed with BafA. Moreover, TBK1−/− HeLa cells were equally defective in Keima-LGALS3 flux as ATG5−/− cells by flow cytometry assays performed in biological triplicate, consistent with a major requirement for TBK1 in this process (Figure 5J). Interestingly, while pTBK1 was reduced to basal levels 12 hr post-LLOMe, pTBK1 remained fully elevated at this time in the presence of BafA or TBK1i (Figure 5I), suggesting that loss of pTBK1 could reflect autophagic degradation of the activated pool.

### Selectivity of Ub-binding autophagy receptors in lysophagic flux

Based on proteomic, immunofluorescence, and immunoblotting experiments described previously, multiple Ub- and TBK1-binding autophagy receptors (OPTN, CALCOCO2, and TAX1BP1) are rapidly recruited to damaged lysosomes (Figure 4 and Figure 4—figure supplement 1). However, the contribution of the various autophagy receptors to actual lysophagic flux is unknown. To address this question, we first expressed Keima-LGALS3 in HeLa cells previously engineered to lack OPTN, CALCOCO2, and TAX1BP1 (referred to as triple knockout [TKO] cells; Heo et al., 2015) and measured lysophagic flux by flow cytometry in biological triplicate. The TKO mutant cells were as defective in LLOMe-stimulated lysophagic flux as cells lacking ATG5 (Figure 6A). In order to examine the extent to which each individual receptor is capable of promoting flux, we then reconstituted TKO cells expressing the Keima-LGALS3 reporters with EGFP-tagged OPTN, CALCOCO2, or TAX1BP1 (Figure 6B and C). While EGFP-TAX1BP1 and EGFP-OPTN rescued lysophagic flux, EGFP-CALCOCO2 was ineffective (Figure 6B and C). To further examine receptor specificity, we used gene editing to created mKeima-LGALS3 reporter cells lacking individual receptors (OPTN, TAX1BP1, CALCOCO2, or SQSTM1), as well as ATG7 as a control for canonical autophagy (Figure 6—figure supplement 1A-E). We found that cells lacking TAX1BP1 have the most severe block to lysophagic flux, phenotypically similar to cells lacking ATG7 examined in parallel (Figure 6D). Cells lacking SQSTM1 or OPTN had essentially wild-type lysophagic flux whereas CALCOCO2−/− cells had a partial reduction in lysophagic flux (Figure 6D). Consistent with a block in flux, TAX1BP1−/− cells – but not OPTN−/− or CALCOCO2−/− cells – displayed extensive LGALS3-positive puncta 10 hr post-washout after LLOMe treatment, as assessed using endogenous αLGALS3 staining by immunofluorescence (Figure 6E). The defect in TAX1BP1−/− cells was rescued by expression of EGFP-TAX1BP1, which also associated with LAMP1-positive puncta in LLOMe-treated cells, but expression of EGFP alone as a negative control failed to rescue clearance of, or associate with, damaged lysosomes (Figure 6E). Taken together, these data indicate that in HeLa cells, TAX1BP1 can drive lysophagic flux and that, among cargo receptors, TAX1BP1 is both necessary and sufficient for lysophagy. Moreover, overexpression of OPTN on its own can also promote lysophagy in cells lacking OPTN, TAX1BP1, and CALCOCO2, but is not required in HeLa cells. Interestingly, in our cell system, we were unable to validate the previous report based on RNAi that SQSTM1 is required for lysophagic flux (Papadopoulos et al., 2017).

![Figure 6.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig6-v2.jpg)

**Figure 6.:** (A) Triplicate WT; ATG5−/−; or OPTN−/−; TAX1BP1−/−; CALCOCO2−/− (TKO) HeLa cells expressing Keima-LGALS3 were either left untreated or treated for 1 hr followed by washout (12 hr) prior to flow cytometry to measure the 561 nm/488 nm ratio. All values are normalized to the untreated sample within each genotype. The plot represents mean and standard deviation from three biological replicates. (B) Triplicate WT or TKO HeLa cells expressing Keima-LGALS3 were reconstituted with lentivirally expressed EGFP-FLAG-HA, EGFP-CALCOCO2, EGFP-OPTN, or EGFP-TAX1BP1. Cells were either left untreated or treated for 1 hr followed by washout (12 hr) prior to flow cytometry to measure the 561 nm/488 nm ratio. As a control for lysophagic flux, some samples were also treated with BafA during the washout. All values are normalized to the untreated sample within each genotype. ****p < 0.0001. The plot represents mean and standard deviation from three biological replicates. (C) Cells from panel B were lysed and subjected to immunoblotting with the indicated antibodies. (D) HeLa cells expressing Keima-LGALS3 (with or without deletion of ATG7, TAX1BP1, OPTN, CALCOCO2, or SQSTM1) were either left untreated or treated for 1 hr followed by washout (12 hr) prior to flow cytometry to measure the 561 nm/488 nm ratio. All values are normalized to the untreated sample within each genotype. ****p < 0.0001. The plot represents mean and standard deviation from three biological replicates. (E) HeLa cells (with or without deletion of TAX1BP1, OPTN, CALCOCO2, or SQSTM1) were either left untreated or treated for 1 hr followed by washout (10 hr) prior to immunostaining with α-LAMP1 (green) and α-LGALS3 (magenta). The number of LGALS3 puncta per cell present after washout is plotted (right top panel). The block to lysophagic flux was rescued by expression of EGFP-TAX1BP1 but not EGFP (lower right panel). 41 (WT), 21 (TAX1BP1), 25 (OPTN), 21 (CALCOCO2), and 27 (SQSTM1) cells were analyzed in the upper graph. 29 (WT), 28 (EGFP), and 32 (EGFP-TAX1BP1) cells were analyzed in the bottom graph. ****p < 0.0001. Scale bar 10 μm. Zoom-in panels, 10 μm × 10 μm. + marks the mean and the line is at the median. The plot represents merged data from three biological replicates.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A–E) Validation of gene edited cell lines by immunoblotting. The location of the target exon and CRISPR guide sequence used for targeting are shown. Extracts from the indicated cells were then subjected to immunoblotting with actin used as a loading control.

### A system for quantitative analysis of lysophagic flux in iNeurons

Lysosomal function is linked with critical cellular functions during aging, and lysosomal dysfunction is linked with neurodegenerative diseases (Peng et al., 2019). As an initial step toward defining the mechanisms underlying removal of damaged lysosomes in neurons, we created a genetically tractable system for functional analysis of lysophagic flux. We employed a previously described hESC line that contains an inducible NGN2 gene, allowing for facile conversion to cortical-like iNeurons with >95% efficiency (Ordureau et al., 2020). We used PiggyBac transposase to create cells expressing RFP-EGFP-LGALS3 as a tandem reporter of lysophagic flux. Under basal conditions in 12-day iNeurons, the EGFP signal associated with RFP-EGFP-LGALS3 was largely localized in a diffuse cytosolic pattern, as expected (Figure 7A). These cells also contained RFP-positive puncta that colocalize with LAMP1-positive puncta (Figure 7A). These structures are indicative of either lysophagic flux occurring basally during the 12-day differentiation process, nonselective bulk autophagy, or endocytosis of extracellular LGALS3 noted previously (Furtak et al., 2001; Lepur et al., 2012), as RFP is highly stable within the lysosome. To address these various possibilities, we mutated the carbohydrate recognition site Arginine 186 to Serine in LGALS3 (LGALS3R186S) (Aits et al., 2015; Delacour et al., 2007) and monitored basal RFP-positive puncta in iNeurons. The expression of RFP-EGFP-LGALS3R186S did not result in significantly fewer RFP-positive puncta under basal conditions (Figure 7—figure supplement 1C), indicating LGALS3 translocation into the lysosome was not due to an increase in damaged lysosomes and likely either represents nonselective bulk autophagic flux or increased endocytosis.

![Figure 7.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig7-v2.jpg)

**Figure 7.:** (A) RFP-EGFP-LGALS3 is trafficked to lysosomes in iNeurons. ES cells expressing RFP-EGFP-LGALS3 via a PiggyBac vector were converted to iNeurons using inducible NGN2 (see Materials and methods) and imaged for EGFP, RFP, and LAMP1 using α-LAMP1 antibodies. While EGFP signal was diffusely localized in the soma, RFP-positive puncta colocalized with lysosomes based on colocalization with LAMP1 staining, indicating that a subset of the RFP-EGFP-LGALS3 protein is trafficked to the lysosome under basal conditions. Scale bar = 20 μm. iN soma zoom-in panels, 30 μm × 40 μm. (B) iNeurons expressing RFP-EGFP-LGALS3 were either left untreated, treated with LLOMe for 1 hr, or treated with LLOMe for 1 hr followed by a 12 hr washout. Cells were imaged for EGFP and RFP and the number of EGFP puncta per cell quantified. Loss of EGFP puncta during the washout period is indicative of lysophagic flux. Scale bar = 20 μm. (C) Quantification of EGFP puncta per cell after washout from experiments in panel B. The average EGFP puncta per cell was 0.289 at 0 hr (45 cells), 6.46 at 1 hr LLOMe (55 cells) and 0.652 at 12 hr washout after LLOMe (66 cells). ****p < 0.0001. + marks the mean and the line is at the median. The plot represents merged data from three biological replicates. (D) iNeurons were subjected to LLOMe treatment and washout as in panel B but treated with or without TBK1i, VPS34i, or BafA during the washout period. Cells were imaged for EGFP and RFP. Scale bar = 20 μm. iN soma zoom-in panels, 30 μm × 40 μm. (E) Quantification of EGFP puncta per cell from the experiment in panel D. The average EGFP puncta per cell at 12 hr washout was 0.65 with no inhibitor (66 cells), 5.14 with BafA (49 cells), 11.95 with VPS34i (44 cells), and 5.84 with TBKi (63 cells). ****p < 0.0001, ***p < 0.001. + marks the mean and the line is at the median. The plot represents merged data from three biological replicates. (F) WT, TAX1BP1−/−, or TAX1BP1−/−; OPTN−/− iNeurons were subjected to LLOMe treatment and washout as in panel B. Cells were imaged for EGFP and RFP. Scale bar = 10 μm. iN soma zoom-in panels, 20 μm × 20 μm. (G) Quantification of EGFP puncta per cell from the experiment in panel F. The average EGFP puncta per cell at 12hr washout after LLOMe for wild-type cells was 0.474 (38 cells), for TAX1BP1−/− cells was 4.36 (62 cells) and for TAX1BP1−/−; OPTN−/− cells was 4.03 (39 cells). ****p < 0.0001, **p< 0.01. + marks the mean and the line is at the median. The plot represents merged data from three biological replicates.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) iNeurons stably expressing RFP-EGFP-LGALS3R186S were either left untreated, treated with LLOMe for 1 hr, or treated with LLOMe for 1 hr followed by a 12hr washout. Cells were imaged for EGFP and RFP. Scale bar = 10 μm. Zoom-in panels, 10 μm × 10 μm. (B) Quantification of GFP puncta per cell after washout from experiments in panel A demonstrates the absence of GFP-positive puncta in response to lysosomal damage. + marks the mean and the line is at the median. The plot represents data from one replicate. (C) RFP-positive puncta in cells expressing RFP-EGFP-LGALS3 WT or the R186S mutant demonstrates comparable number of puncta. + marks the mean and the line is at the median. The plot represents data from one replicate. (D) TAX1BP1 lesion read by Illumina Miseq analysis. (E) Extracts from WT or TAX1BP1−/− ES cells were immunoblotted with the indicated antibodies to demonstrate deletion of TAX1BP1. (F) OPTN lesion read by Illumina Miseq analysis. (G) Extracts from WT, TAX1BP1−/−, or TAX1BP1−/−; OPTN−/− ES cells were immunoblotted with the indicated antibodies to demonstrate deletion of OPTN and TAX1BP1.

In contrast to basal, untreated conditions, iNeurons treated with LLOMe (1 hr) displayed an increase in the number of EGFP-positive puncta per cell (Figure 7B and C). However, 12 hr post-washout, the EGFP-positive puncta associated with the tandem LGALS3 reporter had been cleared, and the number of puncta returned to near basal conditions (Figure 7B and C). Importantly, the clearing of EGFP-positive puncta was largely blocked by BafA and VPS34i, as expected if the EGFP-positive puncta were cleared via lysophagy (Figure 7D and E). Moreover, as expected, the LGALS3R186S mutant failed to be recruited to damaged lysosomes (Figure 7—figure supplement 1A-C). These data indicate that the clearing of EGFP-positive puncta can be used as a means by which to examine lysophagic flux in iNeurons, as previously demonstrated in HeLa cells (Maejima et al., 2013).

### Lysophagic flux in iNeurons requires TAX1BP1 and TBK1

In order to examine the TBK1-cargo receptor axis in the iNeuron system, we initially employed the TBK1i small molecule inhibitor during a 12 hr washout after a 1 hr LLOMe treatment. TBK1i blocked LGALS3 clearance to an extent comparable to that observed with BafA, indicating that lysophagic flux in iNeurons requires TBK1 activity (Figure 7D and E). We next employed gene editing to create ES:NGN2:LGALS3 tandem reporter cells lacking TAX1BP1 (Figure 7—figure supplement 1D,E). Deletion of TAX1BP1 led to substantial reduction in clearance of EGFP-positive puncta during a 12 hr washout after LLOMe (1 hr) treatment (Figure 7F and G). Additional deletion of OPTN with TAX1BP1 did not further exacerbate clearance of EGFP-positive puncta at 12 hr washout after LLOMe (1 hr) treatment (Figure 7F and G, and Figure 7—figure supplement 1F,G). Thus, these data indicate that TAX1BP1 and TBK1 collaborate to promote facile clearance of damaged lysosomes in iNeurons.

### Role for TAX1BP1 SKICH domain in lysophagy

Ub-binding cargo receptors typically contain three major structural elements: coiled-coil (CC) motifs, LIR motifs that bind to ATG8 proteins, and C-terminal Ub-binding domains, which include UBAN and ZnF domains (Johansen and Lamark, 2020; Figure 8A and B). In addition, TAX1BP1 also contains an N-terminal SKICH domain, which interacts with the TBK1-binding adaptor protein NAP1, to facilitate TBK1 binding (Fu et al., 2018). Interestingly, TAX1BP1 has also been recently shown to bind RB1CC1—a component of the ULK1 kinase complex required for autophagy—in a manner that requires Alanine 114 within the SKICH domain and a LGALS8-binding element located between residues 632 and 639 (Bell et al., 2021; Ohnstad et al., 2020; Figure 8A). In order to probe the activities of these functional elements in lysophagy, we stably expressed various TAX1BP1 mutants in HeLa TKO cells and measured lysophagic flux by flow cytometry in biological triplicate after lysosomal damage with LLOMe (Figure 8C and D). Consistent with a recent report (Ohnstad et al., 2020), we found that this collection of TAX1BP1 mutants displayed differential levels of expression, with several mutants including 632–639Δ displaying elevated levels compared to WT TAX1BP1 (Figure 8D). In addition, although the antibody employed does not react with the CC2Δ mutant, we demonstrated that the expression level of this mutant is equivalent to that of CC1Δ and CC3Δ based on EGFP fluorescence measured by flow cytometry (Figure 8—figure supplement 1A). We found that various TAX1BP1 mutations display varying levels of activity. First, deletion of the SKICH domain (1–140Δ) resulted in the complete inhibition of lysophagic flux, comparable to that observed in the TKO mutant, despite being expressed at a level higher than WT (Figure 8C and D). Consistent with this, expression of the A114Q mutant also severely blocked lysophagic flux. In contrast, mutations that affect LGALS8 binding (Y635A, N637A, and 632–639Δ) or removal of any of the CC domains had little or no impact on lysophagic flux (Figure 8C). The V192S mutation that affects binding to ATG8 proteins reduced activity by ~40% (Figure 8C). Finally, mutation of TAX1BP1’s C-terminal ZnF domain resulted in a partial (~50%) reduction in activity (Figure 8C), but still retained the ability to be recruited to damaged lysosomes (Figure 8—figure supplement 1B). However, previous studies have shown that this mutation has residual Ub-binding activity (Tumbarello et al., 2015), potentially accounting for residual activity. Therefore, to examine a direct role for Ub in TAX1BP1 recruitment, we treated cells with E1i before LLOMe treatment and during a 4hr washout (Figure 8—figure supplement 1C). We found that inhibition of Ub conjugation completely blocked TAX1BP1 recruitment to damaged lysosomes, while TAX1BP1 recruitment was unaffected by treatment with p97i or TBK1i (Figure 8—figure supplement 1C). In parallel, the D474N Ub-binding mutant of OPTN was tested and did not rescue the TKO phenotype to promote lysophagy while the TBK1 phosphoresistant mutants of OPTN expressed in the TKO background did rescue lysophagic flux (Heo et al., 2015; Figure 8E and F). Moreover, OPTND474N failed to be recruited to damaged lysosomes, as assessed by microscopy (Figure 8—figure supplement 1B). Taken together, these data indicate that recruitment of both TAX1BP1 and OPTN to damaged lysosomes requires upstream ubiquitylation.

![Figure 8.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig8-v2.jpg)

**Figure 8.:** (A) Domain structure of TAX1BP1 showing the location of mutations examined in this study. (B) Domain structure of OPTN showing the location of mutations examined in this study. (C) HeLa TKO cells expressing Keima-LGALS3 were infected with lentiviruses expressing GFP-tagged WT or mutant TAX1BP1 proteins to obtain stable expression. Cells in biological triplicate were either left untreated or treated for 1 hr followed by washout (12 hr) prior to flow cytometry to measure the 561 nm/488 nm ratio. All values are normalized to the untreated sample within each genotype. The plot represents mean and standard deviation from three biological replicates. ****p < 0.0001 (D) Immunoblot of cell extracts from panel C probed with α-TAX1BP1 or α-actin as a loading control. Note that some mutants are highly stabilized, as reported previously (Ohnstad et al., 2020). The EGFP-TAX1BP1 CC2Δ mutant is not detected by western blot due to the loss of the epitope-binding site of the antibody, nevertheless is detected by FACS (Figure 8—figure supplement 1A). (E) HeLa TKO cells expressing Keima-LGALS3 were infected with lentiviruses expressing GFP-tagged WT or mutant OPTN proteins to obtain stable expression. Cells in biological triplicate were either left untreated or treated for 1 hr followed by washout (12 hr) prior to flow cytometry to measure the 561 nm/488 nm ratio. The plot represents mean and standard deviation from three biological replicates. ****p < 0.0001. (F) Immunoblot of cell extracts from panel E probed with α-GFP or α-actin as a loading control. (G) HeLa TKO cells were infected with lentiviruses expressing EGFP-tagged WT or mutant TAX1BP1 proteins to obtain stable expression. Cells were either left untreated or treated for 1 hr with LLOMe followed by washout. Cells were harvested at the indicated times and subjected to immunoblotting with the indicated antibodies. (H) HeLa TKO cells were infected with lentiviruses expressing EGFP-tagged WT or mutant OPTN proteins to obtain stable expression. Cells were either left untreated or treated for 1 hr with LLOMe followed by washout (12 hr). Cells were harvested at the indicated times and subjected to immunoblotting with the indicated antibodies. (I) Model figure. Lysosomal rupture leads to the parallel recruitment of galectins and unleashes a wave of ubiquitination on the lysosome (Steps 1a and b). In step 2, ubiquitination promotes the recruitment of both OPTN-TBK1 and TAX1BP1-TBK1-RB1CC1 complexes to the damage lysosome, thereby promoting de novo phagophore formation and local TBK1 activation to drive efficient lysophagy (Steps 3–5).

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/72328/elife-72328-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** (A) Flow cytometry analysis of EGFP-TAX1BP1-CC1Δ, CC2Δ, and CC3Δ cell lines to verify comparable expression of the CC2Δ mutant. (B) Analysis of EGFP, EGFP-TAX1BP1 (WT, Q770A/E774K, Δ SKITCH, and A114Q) as well as EGFP-OPTN (WT and D747N) recruitment to damaged lysosomes (1 hr after LLOMe). Scale bar = 10 μm. (C) Recruitment of endogenous TAX1BP1 (green) to damaged LAMP1-positive lysosomes (pink) was determined by immunofluorescence after 1 hr or LLOMe treatment and a 4hr washout period. ****p < 0.0001. Scale bar = 10 μm. + marks the mean and the line is at the median. The plot represents merged data from two biological replicates.

TAX1BP1 activity appears to depend extensively on its N-terminal SKICH domain, which associates with TBK1-NAP1. When assessed by fluorescence microscopy, the A114Q and the SKICH domain mutants appeared to localize to the same region as damaged lysosomes (Figure 8—figure supplement 1B). Although these mutants are able to translocate to the lysosomal region, we found that LLOMe-dependent phosphorylation of TBK1 in TKO cells reconstituted with WT and mutant TAX1BP1 required A114Q and the SKICH domain (Figure 8G), which correlates with the loss of lysophagic flux with these mutations, and is also consistent with the genetic requirement for TBK1 in lysophagic flux. As expected (Heo et al., 2015), TBK1 activation in the context of OPTN-mediated lysophagy in TKO cells was absolutely dependent upon the ability of OPTN to bind Ub, as the D747N mutant was unable to support TBK1 phosphorylation upon LLOMe treatment (Figure 8H).

## Discussion

The lysosome is the terminal degradative organelle for the autophagic and endocytic pathways, and as a membrane-bound organelle itself, is also susceptible to damage from a plethora of sources. Irrevocably damaged lysosomes are eliminated by the selective autophagic pathway of lysophagy, which requires: (1) galectin binding to damaged lysosomes, (2) ubiquitination of lysosomal components, (3) core components of the autophagic machinery such as the VPS34 kinase complex, the ULK1-RB1CC1-ATG13 module, and the ATG5-ATG12 lipidation cascade, and (4) the biogenesis of newly formed lysosomes via the TFEB transcriptional response (Nakamura et al., 2020). Despite the identification of these individual steps in the lysophagy pathway, many events such as the role of Ub-binding cargo receptors remain poorly characterized. Using a suite of quantitative proteomic techniques, we have generated a landscape of the damaged lysosome and have identified key regulatory modules in the pathway. Lysosomal damage leads to the sequential recruitment of ESCRT-III complex proteins, galectin proteins LGALS1, 3, and 8, and ATG8 family of proteins, consistent with prior observations (Jia et al., 2018). Additionally, the proteomic data provided here provide a variety of candidates for future hypothesis-driven investigations into the molecular mechanisms of lysophagy, including the development of a spatial understanding of distinct galectins and their recruitment to damaged lysosomes.

Our proximity biotinylation maps of the ATG8 orthologs MAP1LC3B and GABARAPL2 in response to LLOMe revealed rapid, specific biotinylation of proteins associated with the lysosomal membrane, as compared to other organelles, consistent with the selectivity of this response. Interestingly, both MAP1LC3B and GABARAPL2 utilize their LIR docking sites to recruit a subset of downstream factors to the damaged lysosome. Proximity biotinylation maps of LGALS1, 3, and 8 also revealed galectin-specific interactions with LGALS8 having apparently selective interactions with the MTOR signaling machinery and autophagy. These results are consistent with prior observations that LGALS8 regulates the autophagic response after lysosomal damage and suggest that LGALS8 is a key regulatory node for lysophagy (Jia et al., 2018).

Prior observations have indicated that the selective autophagy receptors, SQSTM1 and TAX1BP1, are recruited to damaged lysosomes, and SQSTM1 has been reported to be required for lysophagy in HeLa cells using siRNA (Papadopoulos et al., 2017). Our proteomics data clearly demonstrate that SQSTM1, CALCOCO2, OPTN, and TAX1BP1 are recruited to the lysosome within 30 min post-damage, raising questions about the actual identity of the relevant receptors. Are all recruited receptors necessary for lysophagy, perhaps playing distinct roles or are some receptors recruited but not required? To address this question, we developed a lysophagic flux assay—Lyso-Keima—and demonstrated in HeLa cells that deletion of TAX1BP1 was sufficient to eliminate lysophagic flux. Reduced lysophagic flux was also found in iNeurons lacking TAX1BP1. In HeLa cells lacking TAX1BP1, OPTN, and CALCOCO2, TAX1BP1 and to a lesser extent OPTN, but not CALCOCO2, can rescue lysophagy. In iNeurons, the phenotype of TAX1BP1-/-; OPTN-/- double mutants was similar to TAX1BP1 deletion alone, suggesting that OPTN does not play a supporting role in this process in this context. The dramatic reduction in lysophagic flux in HeLa cells or iNeurons solely lacking TAX1BP1 also indicates that SQSTM1 is not sufficient to support flux in these cells under the conditions employed here. These results, together with the results of prior studies on other types of selective autophagy, indicate distinct receptor requirements for individual cargo. For example, in HeLa cells, Parkin-dependent mitophagic flux requires primarily OPTN and CALCOCO2 (Wong and Holzbaur, 2014; Heo et al., 2015; Lazarou et al., 2015), in addition to TBK1 and xenophagy require CALCOCO2 (Ravenhill et al., 2019). Moreover, our results indicate that the apparent strength of receptor recruitment to damaged organelles is not a surrogate for a functional role.

Overall, our data support the model in Figure 8I. Lysosome rupture leads to two apparently independent pathways, one resulting in the ubiquitylation of lysosomal proteins and the other reflecting association of galectins with glycosylated luminal domains in lysosomal membrane proteins. Recruitment of LGALS3 or LGALS8 does not require the Ub pathway downstream of UBE2QL1 (Koerver et al., 2019), and likewise, the activation of the ubiquitylation arm of the pathway does not require LGALS3 or LGALS8 (Jia et al., 2020a) However, it has been reported that depletion of LGALS9 leads to reduced lysosomal ubiquitylation indicating some level of cross-talk between the two pathways (Jia et al., 2020a). Precisely which ubiquitylation systems are involved and how they mechanistically are linked with LGALS9 remains unknown. Our results indicate that the Ub arm of the pathway is critical for recruitment of TAX1BP1 and OPTN. First, inhibition of the UBA1 E1-activating enzyme blocks TAX1BP1 recruitment to damaged lysosomes and point mutatations in TAX1BP1’s C-terminal ZnF domain that reduce, but do not eliminate Ub-binding, displayed reduced lysophagic flux in response to LLOMe. Interestingly, inhibition of p97 or TBK1 did not block TAX1BP1 recruitment to damaged lysosomes, although both inhibitors blocked flux and therefore p97 and TBK1 presumably have roles downstream of TAX1BP1 recruitment. Second, mutation of OPTN’s Ub-binding UBAN domain abolishes recruitment to damaged lysosomes and blocks flux in the context of rescue of the TAX1BP1/OPTN/CALCOCO2 triple mutant HeLa cells. Given that TAX1BP1 can also interact with overexpressed LGALS8 independent of lysosomal damage (Bell et al., 2021; Huttlin et al., 2021), it is formally possible that recruitment can occur via both Ub-dependent and -independent pathways under some conditions.

Both TAX1BP1 and OPTN associate with the TBK1 protein kinase, albeit through distinct structural motifs. Several findings link TBK1 with lysophagy. First, small molecular inhibitors of TBK1 block lysophagic flux in HeLa cells and iNeurons, and deletion of TBK1 blocks lysophagy in HeLa cells. Second, deletion of the SKICH domain of TAX1BP1 or mutation of A114 which is required for TBK1–NAP1 association results in loss of activity in lysophagic flux assays. Third, while reintroduction of WT TAX1BP1 into TAX1BP1–/– HeLa cells activates TBK1 phosphorylation in response to LLOMe, removal or mutation of the SKICH domain abolishes TBK1 activation in TKO cells, indicating that TBK1 activation depends on its association with TAX1BP1. The targets of TBK1 in this context remain to be identified, but we note that the cargo adaptors themselves are substrates of TBK1 in other types of selective autophagy (Heo et al., 2015; Richter et al., 2016), and RAB7 is a substrate of TBK1 in response to signals that induce mitophagy (Heo et al., 2018).

The observation that TAX1BP1 is a major receptor for lysophagy extends recent work identifying roles for the protein in various selective autophagic pathways (Gubas and Dikic, 2021). TAX1BP1 likely plays a dual role, as it interacts with both TBK1 and the RB1CC1–ULK1–ATG13 complex through its SKICH domain (Figure 8I). This may allow TAX1BP1 to orchestrate signaling via both of these kinase complexes, and could possibly promote autophagosome formation directly via recruitment of ULK1 to cargo (Ravenhill et al., 2019; Shi et al., 2020; Turco et al., 2020; Vargas et al., 2019). In addition, TAX1BP1 appears to have diverse cargo, ranging from membranous organelles as shown here to ubiquitylated protein aggregates as recently described (Sarraf et al., 2020). TBK1, OPTN, p97, and other factors involved in selective autophagy are mutated in a variety of neurological disorders such as ALS and FTD (Cirulli et al., 2015; Freischmidt et al., 2015). Further elucidation of the mechanisms used by these proteins and their relationship to other components such as TAX1BP1 will assist in the development of therapeutic approaches.

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
      <td>Cell line (Homo sapiens)</td>
      <td>Hela Flp-in-TRex</td>
      <td>This paper</td>
      <td></td>
      <td>Obtained from Brian Raught, Ontario Cancer institute</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>Hela</td>
      <td>ATCC</td>
      <td>CCL-2; RRID:CVCL_0030</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>HEK293T</td>
      <td>ATCC</td>
      <td>CRL-1573; RRID:CVCL_0045</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H9</td>
      <td>Wicell</td>
      <td>WA9, CVCL_9773;RRID: CVCL_9773</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Galectin-1/LGALS1 (D608T) (Rabbit mAb, monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#12936 S;RRID:AB_2137707</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Galectin-3/ LGALS3 (Rabbit Antibody, polyclonal)</td>
      <td>Proteintech</td>
      <td>60207–1-I; RRID:AB_10951109</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Galectin-3/ LGALS3 Antibody (M3/38) for immunofluorescence (rat, monoclonal)</td>
      <td>Santa-Cruz</td>
      <td>sc-23938; RRID:AB_627658</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Human Galectin-8/LGALS8 Antibody, (goat polyclonal)</td>
      <td>R&amp;D Systems</td>
      <td>AF1305; RRID:AB_2137229</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>LC3B D11 (Rabbit mAb, monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#3868 S; RRID:AB_2137707</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>GABARAPL2 (D1W9T) (Rabbit mAb, monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>14256; RRID:AB_2798436</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-CALCOCO2 antibody, (Rabbit, polyclonal)</td>
      <td>Abcam</td>
      <td>ab68588;RRID:AB_1640255</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-OPTN (rabbit, polyclonal)</td>
      <td>Sigma</td>
      <td>HPA003279; RRID:AB_1079527</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-TAX1BP1 (rabbit, polyclonal)</td>
      <td>Sigma</td>
      <td>HPA024432;RRID:AB_1857783</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>SQSTM1 monoclonal antibody (M01), clone 2C11 (mouse, monoclonal)</td>
      <td>Abnova</td>
      <td>H00008878-M01;RRID: AB_437085</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Raptor (24C12) (Rabbit, monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#2280 S;RRID:AB_561245</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>mTOR (7C10) (Rabbit, monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#2983; RRID:AB_2105622</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>NPC1(Rabbit, monoclonal)</td>
      <td>Abcam</td>
      <td>ab134113;RRID: AB_2734695</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>LAMP1 (D2D11) Rabbit (Rabbit, monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#9091 S; RRID:AB_2687579</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>LAMP1 (D401S) (Mouse, monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#15665 S;RRID: AB_2798750</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-TMEM192 antibody [EPR14330] (Rabbit, monoclonal)</td>
      <td>Abcam</td>
      <td>ab185545, Discontinued</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-HA,(Mouse, monoclonal)</td>
      <td>Biolegend</td>
      <td>#901513;RRID:AB_2565335</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Flag M2 (mouse, monoclonal)</td>
      <td>Sigma</td>
      <td>F1804;RRID: AB_262044</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Keima-Red (Mouse, monoclonal)</td>
      <td>MBL international</td>
      <td>M182-3M;RRID: AB_10794910</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>phospho-TBK1/NAK (Ser172) (D52C2) (Rabbit, monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#5483 S; RRID:AB_10693472</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>TBK1/NAK (Rabbit, polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>#3013 S;RRID: AB_2199749</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>beta-actin (mouse, monoclonal) (AC-15)</td>
      <td>Santa Cruz</td>
      <td>sc-69879;RRID: AB_1119529</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GFP (Mouse, monoclonal)</td>
      <td>Roche</td>
      <td>#11814460001;RRID:AB_390913</td>
      <td>IF (1:300), WB (1:1000)</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>DH5 alpha E. coli competent cells</td>
      <td>Homemade</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>T1R E. coli Competent cells</td>
      <td>Homemade</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Gly-Phe-β-naphthylamide</td>
      <td>Cayman Chemical</td>
      <td>#14634</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>l-Leucyl-l-Leucine methyl ester (hydrochloride)</td>
      <td>Cayman Chemical</td>
      <td>#16008</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Biotin Tyramide</td>
      <td>Iris Biotech(peptide solutions)</td>
      <td>LS-3500.0250</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Trolox</td>
      <td>Cayman Chemical</td>
      <td>#53188-07-1</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hydrogen peroxide solution</td>
      <td>Sigma</td>
      <td>H1009</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Pierce Anti-HA Magnetic Beads</td>
      <td>Thermo Scientific</td>
      <td>#88837</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TMTpro 16-plex Label Reagent Set</td>
      <td>Thermo Scientific</td>
      <td>A44520</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>IKKε/TBK1 Inhibitor II, MRT67307</td>
      <td>EMD millipore</td>
      <td>CAS 1190378-57-4</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ULK1 inhibitor, MRT68921</td>
      <td>Cayman chemical</td>
      <td>#1190379-70-4</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TAK-243</td>
      <td>SelleckChem</td>
      <td>S8341</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CB-5083</td>
      <td>Cayman Chemical</td>
      <td>S810</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Bafilomycin A1</td>
      <td>Cayman Chemical</td>
      <td>#88899-55-2</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Lipofectamine 3,000</td>
      <td>Invitrogen</td>
      <td>L3000008</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Pierce High pH Reversed-Phase Peptide Fractionation Kit</td>
      <td>ThermoFisher Scientific</td>
      <td>#84868</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Pierce High Capacity Streptavidin Agarose</td>
      <td>Pierce (Thermo Scientific)</td>
      <td>#20359</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PhosSTOP</td>
      <td>Sigma-Aldrich</td>
      <td>T10282</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Puromycin</td>
      <td>Gold Biotechnology</td>
      <td>Gold Biotechnology</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DAPI</td>
      <td>Thermo Fisher Scientific</td>
      <td>D1306</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Protease inhibitor cocktail</td>
      <td>Sigma-Aldrich</td>
      <td>P8340</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TCEP</td>
      <td>Gold Biotechnology</td>
      <td>TCEP2</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Formic Acid</td>
      <td>Sigma-Aldrich</td>
      <td>#94318</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Trypsin</td>
      <td>Promega</td>
      <td>V511C</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Lys-C</td>
      <td></td>
      <td>129–02541</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Trypan Blue Stain Thermo Fisher Scientific</td>
      <td>Wako Chemicals</td>
      <td>129–02541 w</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>BioRad Protein Assay Dye Reagent Concentrate</td>
      <td>Bio-Rad</td>
      <td>5000006</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Urea</td>
      <td>Sigma</td>
      <td>U5378</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>EPPS</td>
      <td>Sigma-Aldrich</td>
      <td>E9502</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>2-Chloroacetamide</td>
      <td>Sigma-Aldrich</td>
      <td>C0267</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Empore SPE Disks C18 3 M</td>
      <td>Sigma-Aldrich</td>
      <td>#66883 U</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Pierce Quantitative Colorimetric Peptide Assay</td>
      <td>Thermo Fisher Scientific</td>
      <td>#23275</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-NDP52</td>
      <td>Heo et al., 2015</td>
      <td>Addgene #175749;RRID:Addgene_175749</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-OPTN</td>
      <td>Heo et al., 2015</td>
      <td>Addgene #175750;RRID:Addgene_175750</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-APEX2-FLAG-GABARAPL2</td>
      <td>This paper</td>
      <td>RRID:Addgene_175751</td>
      <td>Addgene #175751</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-APEX2-FLAG-GABARAPL2Y49A/L50A</td>
      <td>This paper</td>
      <td>RRID:Addgene_175752</td>
      <td>Addgene #175752</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-APEX2-FLAG-MAP1LC3B</td>
      <td>This paper</td>
      <td>RRID:Addgene_175753</td>
      <td>Addgene #175753</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-APEX2-FLAG-MAP1LC3BK51A</td>
      <td>This paper</td>
      <td>RRID:Addgene_175754</td>
      <td>Addgene #175754</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-APEX2-FLAG-LGALS1</td>
      <td>This paper</td>
      <td>RRID:Addgene_175755</td>
      <td>Addgene #175755</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-APEX2-FLAG-LGALS3</td>
      <td>This paper</td>
      <td>RRID:Addgene_175756</td>
      <td>Addgene #175756</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-APEX2-FLAG-GFP</td>
      <td>This paper</td>
      <td>RRID:Addgene_175757</td>
      <td>Addgene #175757</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-APEX2-FLAG-LGALS8</td>
      <td>This paper</td>
      <td>RRID:Addgene_175758</td>
      <td>Addgene #175758</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-APEX2-FLAG-CALCOCO2</td>
      <td>This paper</td>
      <td>RRID:Addgene_175759</td>
      <td>Addgene #175759</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-APEX2-FLAG-OPTN</td>
      <td>This paper</td>
      <td>RRID:Addgene_175760</td>
      <td>Addgene #175760</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-APEX2-FLAG-TAX1BP1</td>
      <td>This paper</td>
      <td>RRID:Addgene_175761</td>
      <td>Addgene #175761</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-OPTN D474N</td>
      <td>This paper</td>
      <td>RRID:Addgene_175762</td>
      <td>Addgene #175762</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-OPTN S473A 513 A</td>
      <td>This paper</td>
      <td>RRID:Addgene_175763</td>
      <td>Addgene #175763</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-OPTN S513A</td>
      <td>This paper</td>
      <td>RRID:Addgene_175764</td>
      <td>Addgene #175764</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-OPTN E50K</td>
      <td>This paper</td>
      <td>RRID:Addgene_175765</td>
      <td>Addgene #175765</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-TAX1BP1</td>
      <td>This paper</td>
      <td>RRID:Addgene_175766</td>
      <td>Addgene #175766</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-TAX1BP1 A114Q</td>
      <td>This paper</td>
      <td>RRID:Addgene_175767</td>
      <td>Addgene #175767</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-TAX1BP1 SKICH (1-140Δ)</td>
      <td>This paper</td>
      <td>RRID:Addgene_175768</td>
      <td>Addgene #175768</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-TAX1BP1 V192S</td>
      <td>This paper</td>
      <td>RRID:Addgene_175769</td>
      <td>Addgene #175769</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-TAX1BP1 Q770A E774K</td>
      <td>This paper</td>
      <td>RRID:Addgene_175770</td>
      <td>Addgene #175770</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-TAX1BP1 632-639Δ</td>
      <td>This paper</td>
      <td>RRID:Addgene_175771</td>
      <td>Addgene #175771</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-TAX1BP1 Y635A</td>
      <td>This paper</td>
      <td>RRID:Addgene_175772</td>
      <td>Addgene #175772</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-TAX1BP1 N637A</td>
      <td>This paper</td>
      <td>RRID:Addgene_175773</td>
      <td>Addgene #175773</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-TAX1BP1 CC1Δ</td>
      <td>This paper</td>
      <td>RRID:Addgene_175774</td>
      <td>Addgene #175774</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-TAX1BP1 CC2Δ</td>
      <td>This paper</td>
      <td>RRID:Addgene_175775</td>
      <td>Addgene #175775</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-EGFP-TAX1BP1 CC3Δ</td>
      <td>This paper</td>
      <td>RRID:Addgene_175776</td>
      <td>Addgene #175776</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pSMART Tmem192-3X HA (targeting vector for genomic tagging)</td>
      <td>This paper</td>
      <td>RRID:Addgene_175777</td>
      <td>Addgene #175777</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pAC150 RFP-EGFP-LGALS3</td>
      <td>This paper</td>
      <td>RRID:Addgene_175778</td>
      <td>Addgene #175778</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pAC150 RFP-EGFP-LGALS3 R186S</td>
      <td>This paper</td>
      <td>RRID:Addgene_175779</td>
      <td>Addgene #175779</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHAGE-mKeima-LGALS3</td>
      <td>This paper</td>
      <td>RRID:Addgene_175780</td>
      <td>Addgene #175780</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCMV-hyBase-hyperactive piggyBac</td>
      <td>Yusa et al., 2011</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism</td>
      <td>GraphPad, V9</td>
      <td>https://www.graphpad.com/scientificsoftware/ prism/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SEQUEST</td>
      <td>Eng et al., 1994</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Flowjo</td>
      <td>Flowjo, v10.7</td>
      <td>https://www.flowjo.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Perseus</td>
      <td>Perseus v1.6.15.0Tyanova et al., 2016</td>
      <td>https://maxquant.org/perseus/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji</td>
      <td>ImageJ V.2.0.0</td>
      <td>https://imagej.net/software/fiji/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Imagelab</td>
      <td>BioRad, v6.0.1</td>
      <td>https://www.bio-rad.com/en-us/product/image-lab-software?ID=KRE6P5E8Z&amp;source_wt=imagelabsoftware_surl</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cell Profiler</td>
      <td>CellProfiler v4.0.6</td>
      <td>https://cellprofiler.org/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Metamorph</td>
      <td>Metamorph v</td>
      <td>https://www.moleculardevices.com/products/cellular-imaging-systems/acquisition-and-analysis-software/metamorph-microscopy#gref</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Cell culture

All assays performed in Figures 1—3 were performed in HeLa cells (ATCC). Keima flux assays in Figures 4—6 and Figure 8 were performed Hela Flip-In T-Rex (HFT) cells (Brian Raught, Ontario Cancer Institute) and have been previously described in Heo et al., 2015 or HeLa cells as indicated. HeLa and HFT cells were grown in Dulbecco’ modifies Eagles medium (DMEM) supplemented with 10% fetal bovine serum (FBS) with 5% penicillin–streptomycin. Stable cell lines were generated using lentivirus generated from HEK293T. Antibiotic selections were performed with 1 μg/ml puromycin, 10 μg/ml blasticidin, or 100 μg/ml hygromycin. Cells were subjected to karyotyping (GTG-banded karyotype) by Brigham and Women’s Hospital Cytogenomics Core Laboratory. H9 ES cells were from WiCell, who provides original cell stocks. All cell lines were found to be free of mycoplasma using Mycoplasma Plus PCR assay kit (Agilent).

### Neural differentiation of AAVS1-TRE3G-NGN2 pluripotent stem cells

A detailed version of this protocol is available at dx.doi.org/10.17504/protocols.io.br9em93e. Briefly, human ES cells (H9, WiCell Institute) with TRE3G-NGN2 integrated into the AAVS site have been previously described (Ordureau et al., 2020) and were cultured in E8 medium on Matrigel coated plates. To generate induced neurons (i3-neurons) from ES cells, cells were plated at 2 × 105 cells/ml on Day 0 on plates coated with Matrigel in ND1 medium (DMEM/F12, 1× N2 (thermo), human brain-derived neurotrophic factor (BDNF) (10 ng/ml, PeproTech)), human Neurotrophin-3 NT3 (10 ng/ml, PeproTech), 1× nonessential amino acids, Human Laminin (0.2 μg/ml) ,and doxycycline (2 μg/ml). The media was replaced with ND1 the next day. On the next day, the medium was replaced with ND2 neurobasal medium, 1× B27, 1× Glutamax, BDNF (10 ng/ml), NT3 (10 ng/ml), and doxycycline at 2 μg/ml. On Days 4 and 6, 50% of the media was changed with fresh ND2. On Day 7, cells were replated at 4 × 105 cells/well in ND2 medium supplemented with Y27632 (rock inhibitor – 10 μM). The media was replaced the next day with fresh ND2 and on Day 10 onwards 50% media change was performed until the experimental day (Day 14 of differentiation unless otherwise noted).

### Imaging

A detailed version of this protocol is available on protocols.io at dx.doi.org/10.17504/protocols.io.bxghpjt6. Briefly, cells were plated onto 35-mm glass bottom dish (No. 1.5, 14-mm glass diameter, MatTek). Live cells were imaged at 37°C in prewarmed Fluorobrite supplemented with 10% FBS. For all immunofluorescence experiments, cells were first fixed at room temperature with 4% paraformaldehyde plus in PBS, solubilized in 0.1% Triton-X in PBS blocked with 1% BSA/0.1% Triton-X in PBS and then immunostained. Primary antibodies were used at 1:500 and AlexaFluor-conjugated antibodies (Thermo Fisher) were used at 1:300. Images of fixed cells were captured at room temperature. Cells were imaged using a Yokogawa CSU-X1 spinning disk confocal on a Nikon Ti-E inverted microscope at the Nikon Imaging Center in Harvard Medical School. Nikon Perfect Focus System was used to maintain cell focus over time. The microscope equipped with a Nikon Plan Apo 40×/1.30 N.A. or 100x/1.40 N.A. objective lens and 445 nm (75 mW), 488 nm (100 mW), 561 nm (100 mW), and 642 nm (100 mW) laser lines controlled by AOTF. Pairs of images for ratiometric analysis of mKeima fluorescence were collected sequentially using 100 mW 442 nm and 100 mW 561 solid-state lasers and emission collected with a 620/60 nm filter (Chroma Technologies). All images were collected with a Hamamatsu ORCA-ER cooled CCD camera (6.45 µm2 photodiode) with MetaMorph image acquisition software. Z series are displayed as maximum z-projections and brightness and contrast were adjusted for each image equally and then converted to rgb for publication using FiJi software. Image analysis was performed using both Fiji and Cell Profiler (McQuin et al., 2018). Mander’s Overlap Correlation (MOC) in lysosomes was performed in Cell Profiler. Each field of view for every unique condition was thresholded in the same way with a consistent pipeline. The ‘identify primary objects’ tool was used to find puncta for both the lysosome channel and for the respective receptor or p-TBK1 stain. The ‘measure colocalization’ module was used to compare the fluorescence intensities within the areas defined by the threshold. The MOC with Costes was reported for each field of view.

The LGALS3 puncta detected by immunofluorescence in HeLa cells and the RFP-GFP-LGALS3 puncta detected in the iN system upon LLOMe treatment and subsequent washout were all identified using Cell Profiler and the following protocols available on protocols.io at dx.doi.org/10.17504/protocols.io.bx8pprvn (for HeLa cells LGALS3) and dx.doi.org/10.17504/protocols.io.bx48pqzw (for iN RFP-GFP-LGALS3). Each cell area was first defined using a using a ‘identify primary objects’ module that included objects 200–1000 pixels units, and each punctum was marked using a ‘identify primary objects’ module that included objects 2–20 pixels units both with an optimized ‘robust background’ threshold. Each cell for each condition was thresholded in the same way with a consistent pipeline. Object size and shape were measured, and each punctum was related to its respective cell to yield a punctum per cell readout.

### Analysis of lysophagic flux in cultured cells Using Lyso-Keima

A detailed protocol for analysis of lysophagic flux by western blotting, flow cytometry, and imaging using Lyso-Keima is available on protocols.io at dx.doi.org/10.17504/protocols.io.bx8qprvw.

#### Lysophagy assays

Lysophagy assays were carried out as previously described using as described in Maejima et al., 2013 with slight modifications. HFT cells or iNeurons were treated with DMEM or ND2 containing 500–1000 μM LLOMe (l-Leucyl-l-Leucine methyl ester hydrochloride, Cayman Chemical) or 200 μM GPN for 1 hr, then media was replaced with fresh DMEM (referred to as ‘washout’ in the text). The cells were collected at the indicated time points after the LLOMe washout for various downstream assays.

#### Western blotting

For western blotting, cell pellets were collected and resuspended in 8 M urea buffer (8 M urea, 150 mM TRIS pH, NaCl) supplemented with Protease and Phosphatase Inhibitors. The resuspended pellets were sonicated and the lysate was spun at 13,000 rpm for 10 min. Bradford or BCA assay was performed on clarified lysate and equal amounts of lysate were boiled in 1× SDS containing Laemmeli buffer. Lysates were run on 4%–20% Tris Glycine gels (BioRad) and transferred via Wet transfer onto PVDF membranes for immunoblotting with the indicated antibodies. Images of blots were acquired using Enhanced-Chemiluminescence on a BioRad ChemiDoc imager.

#### Flow cytometry

Cells of the indicated genotypes were grown to 70% confluency in 6-well plates and then treated with various drugs for the indicated time points. At the time of harvesting, cells were trypsinized, pelleted at 1000 rpm for 3 min, and then resuspended in FACS buffer (1× PBS, 2% FBS). The resuspend cells were filtered through cell strainer caps into FACS tubes (Corning, 352235) and placed on ice. The cells (~10,000 per replicate) were then analyzed by flow cytometry on a BD FACSymphony flow cytometer and the data were exported into Flowjo. After gating for live, single cells and Keima-positive cells, the 561 nm (acidic) to 488 nm (neutral) excitation ratio was calculated in Flowjo by diving the mean values of 561 nm excited cells to those excited at 488 nm.

#### Imaging

Analysis of acidic Keima-LGALS3 puncta at 12hr washout was done in Cell Profiler using a consistent pipeline for each condition. The ‘image math’ module where the 561 nm-excitation channel image was divided by the 442 nm-excitation channel image. The acidic puncta in the resulting image were marked using the ‘identify primary objects’ tool by applying an Otsu threshold for puncta 5–20 pixels in diameter. Each resulting punctum was matched to its respective cell and counted. The ‘image math’ image was exported, and a ‘Fire’look up table in Fiji was applied to show the acidic signal (561 nm/442 nm) hotspots. An image of the acidic puncta identified was also exported with each punctum having a separate color.

### Gene editing

Gene editing in HFT and HeLa cells was performed as described in Ran et al., 2013. Gene editing in H9 ES cells was performed as Ordureau et al., 2020 in HFT cells lacking TBK1 or TKO (CALCOCO2−/−, OPTN−/−, TAX1BP1−/−) were described in Heo et al., 2015. Guide sequences used were as follows: TBK1 (Exon 1, 5′-AGACATTTGCAGTAGCTCCT -3′); OPTN (Exon 1, 5′-AAACCTGGACACGTTTACCC-3′); NDP52 (Exon 1, 5′-GGATCACTGTCATTTCTCTC-3′); TAX1BP1 (Exon 2, 5′-CCACATCCAAAAGATTGGGT-3′); SQSTM1 (Exon 2, 5′-CGACTTGTGTAGCGTCTGCG-3′); ATG7 (Exon 1, 5′- ATCCAAGGCACTACTAAAAG-3′); OPTN (Exon 1, 5′-AAACCTGGACACGTTTACCC-3′); CALCOCO2 (Exon 1, 5′-GGATCACTGTCATTTCTCTC-3′); ATG5 (Exon 5, 5′ -GATCACAAGCAACTCTGGAT-3′); TMEM192 (Exon 4, 5′-AGTAGAACGTGAGAGGCTCA-3′). To engineer the Lyso-IP tag into HeLa cells using homology-directed repair, a gene block encoding a 3xHA epitope tag, a puromycin cassette, and homology arms on either side of the cleavage site was synthesized by Integrated DNA Technologies to edit the tmem192 locus. This sequence was cloned into the pSmart (Lucigen Cat#40041–2) shuttle vector using Gibson assembly (New England Biolabs). The shuttle vector along with the TMEM192 sgRNA sequence was transiently transfected into HeLa cells and puromycin selection was performed 5 days post-transfection for 7–8 days. The mixed pool of cells that were puromycin resistant were single-cell plated and clonal lines of homozygous HeLa TMEM192HA were isolated.

Gene editing in ES cells was performed as in Ordureau et al., 2018. Guide RNAs were generated using the GeneArt Precision gRNA Synthesis Kit (Thermo Fisher Scientific) according to the manufacturer’s instruction and purified using RNeasy Mini Kit (QIAGEN). 0.6 μg sgRNA was incubated with 3 μg SpCas9 protein for 10 mins at room temperature and electroporated into 2 × 105 H9 cells using Neon transfection system (Thermo Fisher Scientific). Out of frame deletions were verified by DNA sequencing with Illumina MiSeq and by immunoblotting.

### Molecular cloning

Stable expression plasmids were generally made using either Gateway technology (Thermo) or via Gibson assembly (New England biolabs) in pHAGE backbone unless otherwise noted. Entry clones from the human orfeome collection version eight were obtained and cloned via LR cloning into various destination expression vectors. Site-directed mutagenesis was carried out using the Quick-Change Site Directed Mutagenesis Kit (New England Biolabs) as per the manufacture’s instructions.

### Stable cell line generation

Lentiviral vectors were packaged in HEK293T by cotransfection of pPAX2, pMD2, and the vector of interest in a 4:2:1 ratio using polyethelenimine. Virus containing supernatant was collected 2 days after transfection and filtered through 0.22-μm syringe filter. Polybrene was added at 8 μg/ml to the viral supernatant. After infecting target cells with varying amounts of relevant viruses, cells were selected in puromycin (1 μg/ml), blasticidin (10 μg/ml), or hygromycin (100 μg/ml). In case of GFP expressing lines, further selection was carried out using FACS for GFP-positive cells.

### Lysosomal immunoprecipitation

A protocol for analysis of Lyso-IP by proteomics is provided at protocols.io: dx.doi.org/10.17504/protocols.io.bw7hphj6 and is a modification of a related protocol (dx.doi.org/10.17504/protocols.io.bybjpskn). Lysosomal immunoprecipitation was carried out as described in Wyant et al., 2018 with a few modifications. Briefly, cells endogenously tagged with TMEM192HA were seeded in 15-cm plates. All buffers were supplemented with protease inhibitors. At 80% confluency the cells were harvested on ice by scraping and washed once with PBS containing protease inhibitors (Roche). The cells were pelleted at 300 g for 5 min at 4oC and were washed once with KPBS buffer (136 mM KCl, 10 mM KH2PO4, 50 mM sucrose, pH 7.2). The cell pellet was resuspended in 1 ml KPBS and lysed using 30 strokes in a 2-ml Potter-Elvehjem homogenizer. The lysed cells were spun down at 1000 g for 5 min at 4°C. The pellet was discarded and the protein concentration of the lysate was determined by Bradford assay. After normalizing the protein concentration to be equal across all replicates, 5% of the input sample was saved and 50–100 μl of anti-HA magnetic beads was added the remainder of the sample. This mixture was placed on gentle rotation for 20 min, and beads were separated from the lysate using a magnetic stand. The beads were washed twice with KPBS containing 300 mM NaCl and once with KPBS buffer. The samples were then eluted either by boiling the beads with 100 μl 2× Laemmeli buffer (for western blot) for 10 min or with 100 μl KPBS containing 0.5% NP-40 in thermo mixer at 30°C for 20 min (for mass spectrometry). Elutes for mass spectrometry were snap frozen in liquid nitrogen and stored in –80°C until further processing.

### Quantitative proteomics

A detailed version of this protocol is available at dx.doi.org/10.17504/protocols.io.bw7hphj6.

Sample preparation for mass spectrometry-lysosomal fractions. For mass spectrometry of lysosomal eluates, samples were reduced using TCEP (5 mM for 10 min at 55oC) and alkylated (with chloroacetamide 20 mM at room temperature for 30 min) prior to TCA precipitation. TCA was added to eluates at final concentration of 20% and placed on ice at 4oC for at least an hour. Precipitates were pelleted for 30 min at maximum speed at 4oC, and then the pellets were washed three times using ice cold methanol. Dried pellets were then resuspended in in 50 μl, 200 mM EPPS, pH 8.0. Peptide digestion was carried out using LysC (Wako cat. # 129‐02541, 0.25 μg) for 2 h at 37oC followed by trypsin (0.5 μg) overnight. Digested peptides were then labelled with 4 μl of TMT reagent (at 20 μg/μl stock) for 1 hr and the reaction was quenched using hydroxylamine at a final concentration of 0.5 % (wt/vol) for 20 min. The samples were the combined and dried in a vacuum centrifuge. This combined sample was then subjected to fractionation using the high pH reversed-phase peptide fractionation kit (Thermo Fisher) for a final of six fractions. The dried fractions were processed by C18 stage tip desalting prior mass spectrometry.

Sample preparation for Mass Spectrometry-APEX2 Proteomics. For APEX2 proteomics, cells expressing various APEX2 fusions were processed as in Heo et al., 2018; Hung et al., 2016. To induce proximity labeling in live cells, cells were incubated with 500 μM biotin phenol (LS-3500.0250, Iris Biotech) for 1 hr and treated with 1 mM H2O2 for 1 min, and the reaction was quenched with 1× PBS supplemented with 5 mM Trolox, 10 mM sodium ascorbate, and 10 mM sodium azide. Cells were then harvested, and lysed in radioimmunoprecipitation assay (RIPA) buffer (supplemented with 5 mM Trolox, 10 mM sodium ascorbate, and 10 mM sodium azide). To enrich biotinylated proteins, an identical amount of cleared lysates in each cell was subjected to affinity purification by incubating with the streptavidin-coated magnetic beads (catalog no. 88817, Pierce) for 1 hr at room temperature. Beads were subsequently washed twice with RIPA buffer, once with 1 M KCl, once with 0.1 M NaCO3, once with 2 M urea, twice with RIPA buffer, and three times with PBS.

For proteomics, biotinylated protein bound to the beads was digested with trypsin in 0.1 M EPPS [4-(2-hydroxyethyl)-1-piperazinepropanesulfonic acid, 4-(2-hydroxyethyl)piperazine-1-propanesulfonic acid, N-(2-hydroxyethyl)piperazine-N′-(3-propanesulfonic acid)] (pH 8.5) overnight at 37°C. To quantify the relative abundance of individual protein across different samples, each digest was labeled with TMT reagents (Thermo Fisher Scientific), mixed, and desalted with a C18 StageTip (packed with Empore C18; 3 M Corporation) before SPS-MS3 analysis on an Orbitrap Lumos (Thermo Fisher Scientific) coupled to a Proxeon EASY-nLC1200 liquid chromatography (LC) pump (Thermo Fisher Scientific). Peptides were separated on a 100-μm inner diameter microcapillary column packed in house with ~35 cm of Accucore150 resin (2.6 μm, 150 Å, Thermo Fisher Scientific, San Jose, CA) with a gradient consisting of 5%–21% (ACN, 0.1% FA) over a total 150 min run at ~500 nl/min (McAlister et al., 2014). Details of instrument parameters for each experiment are provided below.

For Multi-Notch MS3-based TMT analysis (McAlister et al., 2014; Paulo et al., 2016), the scan sequence began with an MS1 spectrum (Orbitrap analysis; resolution 60,000 at 200 Th; mass range 375–1500 m/z; automatic gain control (AGC) target 5 × 105; maximum injection time 50 ms) unless otherwise stated in the instrument parameters in each supplemental table (Supplementary files 1–5). Precursors for MS2 analysis were selected using a Top10 method. MS2 analysis consisted of collision-induced dissociation (quadrupole ion trap analysis; Turbo scan rate; AGC 2.0 × 104; isolation window 0.7 Th; normalized collision energy [NCE] 35; maximum injection time 90 ms). Monoisotopic peak assignment was used and previously interrogated precursors were excluded using a dynamic window (150 s ± 7 ppm) and dependent scans were performed on a single charge state per precursor. Following acquisition of each MS2 spectrum, a synchronous-precursor-selection (SPS) MS3 scan was collected on the top 10 most intense ions in the MS2 spectrum (McAlister et al., 2014). MS3 precursors were fragmented by high-energy collision-induced dissociation and analyzed using the Orbitrap (NCE 65; AGC 3 × 105; maximum injection time 150 ms, resolution was 50,000 at 200 Th).

For proteomics data analysis, raw mass spectra obtained were processed as described in Huttlin et al., 2010; Paulo et al., 2015; Ordureau et al., 2020 and were processed using a Sequest. Mass spectra were converted to mzXML using a version of ReAdW.exe. Database searching included all entries from the Human Reference Proteome. Searches were performed with the following settings (1) 20 ppm precursor ion tolerance for total protein level analysis, (2) product ion tolerance was set at 0.9 Da, (3) TMT or TMTpro on lysine residues or N-termini at +229.163 Da or +304.207 Da, and (4) carbamidomethylation of cysteine residues ( + 57.021 Da) as a static modification and oxidation of methionine residues ( +15.995 Da) as a variable modification. Peptide-spectrum matches (PSMs) were adjusted to a 1% false discovery rate (Elias and Gygi, 2007). PSM filtering was performed using a linear discriminant analysis, as described previously (Huttlin et al., 2010). To quantify the TMT-based reporter ions in the datasets, the summed signal-to-noise (S:N) ratio for each TMT channel was obtained and found the closest matching centroid to the expected mass of the TMT reporter ion (integration tolerance of 0.003 Da). Proteins were quantified by summing reporter ion counts across all matching PSMs, as described previously (Huttlin et al., 2010). PSMs with poor quality, or isolation specificity less than 0.7, or with TMT reporter summed signal-to-noise ratio that were less than 100 or had no MS3 spectra were excluded from quantification. Classification of proteins to various organellar locations or functional groups were performed using manually curated databases from Uniprot and are listed in the relevant supplementary tables (Supplementary files 1–6).

Values for protein quantification were exported and processed using Perseus to calculate Log FCs and p-values. Volcano plots using these values were plotted in Excel. The mass spectrometry proteomics data have been deposited to the ProteomeXchange Consortium via the PRIDEpartner repository (Perez-Riverol et al., 2019) with the dataset identifier PXDO27476.

### Statistics

All statistical data were calculated using GraphPad Prism v7 or Perseus. Comparisons of data were performed by one-way ANOVA with Tukey’s multiple comparisons test.
