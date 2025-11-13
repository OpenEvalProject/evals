# Fat body-derived cytokine Upd2 controls disciplined migration of tracheal stem cells in Drosophila

## Authors

- Pengzhen Dong<sup>1</sup> ([ORCID: 0009-0009-7124-695X](https://orcid.org/0009-0009-7124-695X))
- Yue Li<sup>1</sup>
- Yuying Wang<sup>1</sup>
- Qiang Zhao<sup>1</sup>
- Tianfeng Lu<sup>4</sup>
- Jian Chen<sup>1</sup>
- Tianyu Guo<sup>1</sup>
- Jun Ma<sup>5</sup>
- Bing Yang<sup>7</sup> †
- Honggang Wu<sup>3</sup> †
- Hai Huang<sup>1</sup> ([ORCID: 0000-0003-2331-6238](https://orcid.org/0000-0003-2331-6238)) †

### Affiliations

1. Second Affiliated Hospital, and Department of Cell Biology, Zhejiang University School of Medicine Hangzhou China
2. State Key Laboratory of Transvascular Implantation Devices Hangzhou China
3. Zhejiang Key Laboratory of Precision Diagnosis and Therapy for Major Gynecological Diseases, Women's Hospital, Zhejiang University School of Medicine Hangzhou China ([ROR:00a2xv884](https://ror.org/00a2xv884))
4. Department of Developmental Biology and Neuroscience, Washington University in St. Louis, Missouri Washington DC United States ([ROR:01yc7t268](https://ror.org/01yc7t268))
5. Center for Genetic Medicine, the Fourth Affiliated Hospital, Zhejiang University, School of Medicine Hangzhou China ([ROR:00a2xv884](https://ror.org/00a2xv884))
6. Institute of Genetics, Zhejiang University International School of Medicine Hangzhou China ([ROR:0569mkk41](https://ror.org/0569mkk41))
7. MOE Laboratory of Biosystem Homeostasis and Protection and Life Sciences, Institute, Zhejiang University Hangzhou China ([ROR:00a2xv884](https://ror.org/00a2xv884))
8. Zhejiang Provincial Key Laboratory of Genetic and Developmental Disorders, Zhejiang University School of Medicin Hangzhou China ([ROR:00a2xv884](https://ror.org/00a2xv884))

† Corresponding author

## Abstract

Coordinated activation and directional migration of adult stem cells are essential for maintaining tissue homeostasis. Drosophila tracheal progenitors are adult stem cells that migrate posteriorly along the dorsal trunk to replenish degenerating branches that disperse the fibroblast growth factor mitogen. However, it is currently unknown how the overall anterior-to-posterior directionality of such migration is controlled. Here, we show that individual progenitor cells migrate together in a concerted, disciplined manner, a behavior that is dependent on the neighboring fat body. We identify the fat body-derived cytokine, Upd2, in targeting and inducing JAK/STAT signaling in tracheal progenitors to maintain their directional migration. Perturbation of either Upd2 production in fat body or JAK/STAT signaling in trachea causes aberrant bidirectional migration of tracheal progenitors. We show that JAK/STAT signaling promotes the expression of genes involved in planar cell polarity leading to asymmetric localization of Fat in progenitor cells. We provide evidence that Upd2 transport requires Rab5- and Rab7-mediated endocytic sorting and Lbm-dependent vesicle trafficking. Our study thus uncovers an inter-organ communication in the control of disciplined migration of tracheal progenitor cells, a process that requires vesicular trafficking of fat body-derived cytokine Upd2 and JAK/STAT signaling-mediated activation of PCP genes.

## Introduction

Adult stem cells are multipotent cell populations which inhabit their niche but mobilize to initiate tissue reconstruction during organismal growth and regeneration. An intriguing feature of stem cells is their capability of migrating in a disciplined directionality toward locations undergoing reconstruction (Li and Clevers, 2010). Such a highly disciplined movement is critical for maintaining tissue homeostasis and is influenced by various niche-intrinsic signals and external stimuli, and its aberrancy causes diseases such as hypertrophy (Zhou et al., 2024). The damaged tissue or distant organs that elicit systemic signals promote the migration of adult stem cells (Jones and Wagers, 2008). In addition, interactions with other cell types, soluble factors (e.g. cytokines, growth factors, and hormones) and tissue stiffness collectively bolster the mobilization of stem cells (Fuchs and Blau, 2020). Despite growing appreciation of adult stem cells as a primary source for tissue regeneration, the mechanism governing directional stem cell migration remains yet to be elucidated.

Drosophila tracheal progenitors are a population of adult stem cells that rebuild the degenerating trachea during metamorphosis. The progenitor cells reside in Tr4 and Tr5 metameres and start to move along the tracheal branch toward sites of regeneration (Chen and Krasnow, 2014; Pitsouli and Perrimon, 2010). Movement of these progenitor cells follows a stereotypical anterior-to-posterior axis (Figure 1A), thus representing a suitable system to investigate mechanisms controlling the directionality of stem cell migration. The activation of tracheal progenitors is stimulated by the morphogen Branchless (Bnl), fly homolog of fibroblast growth factor (FGF) (Chen and Krasnow, 2014), and the insulin hormone (Li et al., 2022). Intercellular communication and synergy between organs also contribute to the branching morphogenesis (Perochon et al., 2021; Schottenfeld et al., 2010; Tamamouna et al., 2021). The functional role of the interactions between trachea and other organs in modulating tracheal progenitor behavior has been largely unknown.

![Figure 1.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig1-v1.jpg)

**Figure 1.:** (A) Schematic cartoon showing the migration of tracheal progenitors (red) and degenerative tracheal branches (dashed gray lines) in pupae. Fat body is shown in beige. Arrows denote anterior–posterior (A–P) axis. Frontal section (B) and sagittal view (C) showing the relative position of fat body and tracheal progenitors. (D–J’) Migration of tracheal progenitors in control and fat body perturbation flies. (D–D’’) Migration of tracheal progenitors (red) upward from transverse connective (blue dashed lines) and along the dorsal trunk (white dotted lines) at 0 hr APF (D), 1 hr APF (D’), and 3 hr APF (D’’). Bidirectional movement of tracheal progenitors in fat body-depleted (lsp2>rpr.hid) flies. 0 hr APF (E), 1 hr APF (E’), and 3 hr APF (E’’). Arrows point to anterior movement of tracheal progenitors. (F) Bar graph showing the migration distance of tracheal progenitors. The top chart of column represents the migration distance of anterior-most stem cells, and the lower chart of column represents the migration distance of posterior-most stem cells. Error bars represent SEM, n = 6. (G, G’) The distribution of progenitors at 2 hr APF. (H, H’’) The distribution of progenitors in fat body-depleted flies at 2 hr APF. (I–J’) Computer simulation depicting trajectories of progenitor migration. (I, J) Confocal images of tracheal progenitors. (I’, J’) Vectors of progenitor migration. (K) Bar graph plots the binary entropy that represents the disorderedness of migration direction of tracheal progenitors. Error bars represent SEM, n = 10. (L) The Bernoulli random variable X showing optic flow distribution of the binarized directions in each group. Error bars represent SEM, n = 10. N.S. indicates not significant. Scale bar: 100 μm (B, C, G), 200 μm (D–E’’). Genotypes: (B, C) UAS-mCD8-GFP/+; lsp2-Gal4,P[B123]-RFP-moe/+; (D–D’’, G, G’) Gal80ts/+;lsp2-Gal4,P[B123]-RFP-moe/+; (E–E’’, H, H’) UAS-rpr-hid/+;Gal80ts/+;lsp2-Gal4,P[B123]-RFP-moe/+.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Confocal images of larval fat body in control (A) and lsp2>rpr.hid (B) animals. Microscopic pictures of control (C) and lsp2>rpr.hid larvae (D). (E) Scatter plot showing migration velocity of tracheal progenitors in control and lsp2>rpr.hid animals. Error bars represent SEM, n = 6. The incorporation of EdU in the tracheal progenitors of control (F) and lsp2>rpr.hid animals (G). (H) Bar graph depicting the number of EdU incorporation. Error bars represent SEM, n = 11. Scale bar: 100 μm (A, B), 20 μm (C, D), 50 μm (F, G). Genotypes: (A, C, F) lsp2-Gal4,P[B123]-RFP-moe/+; (B, D) UAS-rpr.hid/+;lsp2-Gal4,P[B123]-RFP-moe/+; (G) UAS-rpr.hid/+;Gal80ts/+;lsp2-Gal4,P[B123]-RFP-moe/+.

Drosophila fat body is the functional analog of mammalian adipose tissue and the major organ sensing various hormonal and nutritional signals to orchestrate systemic growth, metabolism and stem cell maintenance (Sriskanthadevan-Pirahas et al., 2022). Fat body produces regulatory molecules known as fat body signals (FBSs), which remotely affect the activity of other organs (Ingaramo et al., 2020; Zheng et al., 2016). For instance, the fat body-to-brain signals modulate insulin-like peptides production (Rajan and Perrimon, 2012), visual attention, and sleep behavior (Ertekin et al., 2020).

The Drosophila family of interleukin-6 (IL-6)-like cytokines consist of Unpaired (Upd, also called Outstretched), Upd2 and Upd3, and serve as mediators of systemic signaling. Whereas Upd1 and Upd3 derive from fly brain and plasmatocytes (Beshel et al., 2017; Woodcock et al., 2015), Upd2 is primarily produced by the fat body (Rajan et al., 2017), although muscle-derived Upd2 is also reported (Zhao and Karpac, 2017). The Upd proteins act as ligands which bind to a common GP130-like receptor, Domeless (Dome) on target cells (Agaisse et al., 2003; Chen et al., 2002). Upon association of ligands, the Dome receptors dimerize and recruit the non-receptor tyrosine kinase JAKs leading to their subsequent transactivation via phosphorylation. The transactivated JAKs then phosphorylate the tyrosine residues of their substrates, including the bound receptors and cytosolic STATs. The phosphorylation of STATs promotes their dimerization and nuclear translocation to activate transcriptional program (Darnell, 1997). JAK/STAT signaling requires the IL-6 cytokines (Heinrich et al., 2003), and is implicated in numerous cellular events including cell proliferation, differentiation, migration, and apoptosis (O’Shea et al., 2002).

Here, we investigate molecular basis underlying directional stem cell migration using the Drosophila tracheal progenitors as a model. Our results identify a cytokine-mediated inter-organ communication between fat body and the progenitor cells that is necessary for their disciplined, directional migration. The directional migration of the progenitors relies on JAK/STAT signaling and its downstream targets of planar cell polarity (PCP) components. Importantly, the Upd2 cytokines derived from fat body are transported through vesicular trafficking to induce JAK/STAT signaling in tracheal progenitors. Our study reveals that tracheal progenitors establish migratory directionality as they exit their niches and that the disciplined migration of the progenitors depends on an inter-organ signaling originating from the fat body.

## Results

### Dependence of tracheal progenitors on the fat body

The fly tracheal progenitors are activated and move posteriorly along the dorsal trunk (DT) at the onset of pupariation (Figure 1A). We set out to delve into the underlying mechanisms of directional progenitor cell movement and tentatively surveyed organs that may coordinate this process. In Drosophila, the fat body resides anatomically in proximity with trachea (Figure 1B, C; Video 1) and is the principal reservoir for energy consumption. To determine whether the integrity of fat body is required for tracheal progenitors, we perturbed larval or pupal fat body by expressing pro-apoptotic cell death genes, hid and reaper (rpr), under the control of a fat body-specific driver, lsp2-Gal4 (Cherbas et al., 2003). Expression of hid and rpr in L3 stage impaired fat body integrity and adipocyte abundance, and generated slender larvae and pupae (Figure 1—figure supplement 1A–D). In these animals, the tracheal progenitors exhibited a sign of undisciplined migration and tended to move bidirectionally (Figure 1D–F), although their migration rate, cell number and proliferation remained unchanged (Figure 1—figure supplement 1E–H, Figure 3—figure supplement 1). The undisciplined bidirectional migration behavior of tracheal progenitors in fat body-defective animals is in stark contrast to control animals where the progenitors migrated unambiguously toward posterior (Figure 1D–D’’ and Video 2). To gain a quantitative view of progenitor cell migration, we traced the movement of individual cells by time-lapse confocal imaging. At 2 hr APF, tracheal progenitors from fat body deficit animals displayed a symmetrical distribution relative to the junction between DT and transverse connective (TC), compared with an L-shape localization of niche-associated and migratory progenitors established by a posterior movement in control (Figure 1G–H’). Gauging the vector denoting the movement of each progenitor (Figure 1I, I’) revealed that the traces of progenitor groups in fat body-depleted animals exhibited a fan-shaped pattern (Figure 1J, J’). Owing to this undisciplined movement, entropy of the system was notably elevated upon increased inconsistency of migration vectors (Figure 1K). The bidirectional migratory progenitors displayed longer territory as assessed by binarized direction (Figure 1L). Collectively, these results suggest that fat body has an integral role in maintaining the discipline of tracheal progenitor movement.

![Video 1.](https://cdn.elifesciences.org/articles/100037/elife-100037-video1.mp4.jpg)

**Video 1.:** Scale bar: 100 μm. Genotype: UAS-mCD8-GFP/+;lsp2-Gal4,P[B123]-RFP-moe/+.

![Video 2.](https://cdn.elifesciences.org/articles/100037/elife-100037-video2.mp4.jpg)

**Video 2.:** Scale bar: 100 μm. Genotypes: Gal80ts/+;lsp2-Gal4,P[B123]-RFP-moe/+ (control) and UAS-rpr-hid/+;Gal80ts/+;lsp2-Gal4,P[B123]-RFP-moe/+.

### Upd2–JAK/STAT signaling between fat body and trachea

Since fat body impacts the behavior of tracheal progenitors, we next attempted to investigate the signal between these two interdependent organs. For this purpose, we first performed RNA sequencing (RNA-seq) analysis of tracheal progenitors from aforementioned fat body-defective flies. The results revealed a dramatical alteration of transcriptional program in tracheal progenitors upon the perturbation of fat body (Figure 2—figure supplement 1A, B, B). Interestingly, the functional cluster of ‘cytokine activity’ showed prominent enrichment in the differentially expressed genes (DEGs) in progenitors from lsp2>rpr.hid pupae (Figure 2A). This raised the possibility that certain cytokine-responsive signaling was induced in tracheal progenitors and the signaling was compromised by impairment of fat body. Therefore, we proceeded to analyze the expression of genes responsive to cytokine signaling. Analyzing the RNA-seq data revealed that the cytokine-dependent JAK/STAT and Dpp signaling were notably upregulated upon the activation of progenitors (Figure 2B). Importantly, fat body depletion led to suppression of target genes of JAK/STAT, PI3K, and Dpp signaling in tracheal progenitors, suggesting their dependence on the function of fat body (Figure 2C).

![Figure 2.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig2-v1.jpg)

**Figure 2.:** (A) Top functional clusters among the differentially expressed genes of progenitors between control and fat body-depleted pupae. Gene ratio refers to the proportion of genes in a dataset that are associated with a particular biological process, function, or pathway. Count indicates the number of genes from an input gene list that are associated with a specific GO term. (B) Heatmap depicting expression levels of principal target genes of signaling pathways in L3 larvae, 0 hr APF pupae and 2 hr APF pupae. (C) Heatmap showing the differential expression of target genes of signaling pathways between control and fat body-depleted pupae. Migration of tracheal progenitors along the dorsal trunk at 0 hr APF (D), 1 hr APF (D’), and 3 hr APF (D’’). The white dashed line shows transverse connective. (E–E’’). Migration of tracheal progenitors in upd2RNAi flies. (F) Bar graph plots the migration distance of tracheal progenitors. Error bars represent SEM, n = 6. (G) Volcano plot showing surface proteomics of tracheal epithelium (upregulated genes with tenfold or higher changes in red; downregulated genes with tenfold or higher changes in blue). (H) Top functional classes among the surface proteomics of trachea. (I) Schematic diagram depicting the working principle of the DIPF reporter. (J) The signal of DIPF reporter in tracheal progenitors. The progenitors are outlined by dashed lines. N.S. indicates not significant. Scale bar: 200 μm (D–E’’), 50 μm (J). Genotypes: (A, C) lsp2-Gal4,P[B123]-RFP-moe/+ for control, UAS-rpr-hid/+;Gal80ts/+;lsp2-Gal4,P[B123]-RFP-moe/+; (B) P[B123]-RFP-moe/+. (D–D’’) lsp2-Gal4,P[B123]-RFP-moe/+; (E–E’’) lsp2-Gal4,P[B123]-RFP-moe/UAS-upd2RNAi; (J) btl-Gal4/UAS-DIPF.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Differentially expressed genes in tracheal progenitors of lsp2>rpr.hid pupa compared with control. (B) Volcano plot of RNA-seq showing differentially regulated genes with twofold or higher changes (upregulated genes in red; downregulated genes in blue) in lsp2>rpr.hid compared with control. (C–I’’) The migration of progenitors at 0 hr APF, 1 hr APF, or 3 hr APF in control (C–C’’) and upd1RNAi (D–D’’), upd3RNAi (E–E’’), pvf1RNAi (F–F’’), pvf2RNAi (G–G’’), pvf3RNAi (H–H’’), and hhRNAi (I–I’’). (J) Bar graph represents the migration distance of anterior movement. Error bars represent SEM, n = 4. (K) The migration of progenitors in control (K–K’’) and btl>upd2 RNAi (L–L’’). (M) Bar graph plots the migration distance of anterior movement. Error bars represent SEM, n = 4. N.S. indicates not significant. Scale bar: 200 μm (C–I’’, K–L’’). Genotypes: (C–C’’) lsp2-Gal4,P[B123]-RFP-moe/+; (D–D’’) lsp2-Gal4,P[B123]-RFP-moe/UAS-upd1RNAi; (E–E’’) lsp2-Gal4,P[B123]-RFP-moe/UAS-upd3RNAi; (F–F’’) lsp2-Gal4,P[B123]-RFP-moe/UAS-pvf1RNAi; (G–G’’) lsp2-Gal4,P[B123]-RFP-moe/UAS-pvf2RNAi; (H–H’’) lsp2-Gal4,P[B123]-RFP-moe/UAS-pvf3RNAi; (I–I’’) lsp2-Gal4,P[B123]-RFP-moe/UAS-hhRNAi; (K–K’’) btl-Gal4/+;P[B123]-RFP-moe/+; (L–L’’) btl-Gal4/+;P[B123]-RFP-moe/UAS-upd2RNAi.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Representative confocal images showing the trachea of btl >CD2-HRP flies after oxidation reaction in the presence of both BXXP and H2O2 (A), BXXP only (B), or H2O2 only (C). (D) The western blot showing the biotinylated proteins labeled by an HRP-catalyzed reaction with both BXXP and H2O2. (E) The confocal image showing the trachea of dome>GFP flies. The expression domain of dome is visualized by dome-Gal4-controlled GFP expression. The progenitors labeled by a progenitor-specific enhancer, P[B123]-RFP-moe are outlined by dashed lines. The overlapping expression of GFP and P[B123]-RFP-moe. The expression of DIPF in fat body (F) and salivary gland (G). Scale bar: 50 μm (E–H). Genotypes: (A–C) btl-Gal4/UAS-CD2-HRP; (E) dome-Gal4/+;UAS-GFP/P[B123]-RFP-moe; (F, G) tub-Gal4/UAS-DIPF.

To evaluate the roles of these signaling proteins, we perturbed their expression in fat body by the expression of RNAi constructs. Knockdown of candidates including some cytokines specifically in fat body did not affect the direction of tracheal progenitor migration (Figure 2—figure supplement 1C–J), except for upd2, whose depletion phenocopied fat body ablation-induced bidirectional movement of tracheal progenitors (Figure 2D–F and Video 3). These results suggest a role of fat body-produced Upd2 in remotely regulating the tracheal progenitors.

![Video 3.](https://cdn.elifesciences.org/articles/100037/elife-100037-video3.mp4.jpg)

**Video 3.:** Scale bar: 100 μm. Genotypes: lsp2-Gal4,P[B123]-RFP-moe/+ (control) and lsp2-Gal4,P[B123]-RFP-moe/UAS-upd2RNAi.

Then, we performed surface proteome in vivo (Li et al., 2020) to investigate the spectrum of molecules received by trachea (Figure 2—figure supplement 2). The trachea-associated proteins were biotinylated through a reaction mediated by a membrane-tethered horse radish peroxidase (HRP-CD2) (Figure 2—figure supplement 2A–D). Of the 1684 streptavidin-precipitated proteins captured by mass spectrometry (Figure 2G), a functional cluster enriched for receptor signaling via JAK/STAT was identified (Figure 2H). The JAK/STAT pathway is one of the principal cellular signaling that responds to Upd2 ligand (Hombría et al., 2005). Drosophila JAK/STAT signaling is well conserved (Arbouzova and Zeidler, 2006; Zeidler et al., 2000) and comprises a single JAK (Hopscotch, Hop) and one STAT (Stat92E), in contrast to a handful of homologues (four JAK and seven STAT genes) found in mammals. Domeless (Dome), the receptor for JAK/STAT pathway, exhibited pronounced expression in the tracheal progenitors (Figure 2—figure supplement 2E). To test if these Dome receptors actively interact with their ligands, we adapted a technique to monitor ligand–receptor interaction in vivo (Michel et al., 2011) and constructed a Dome variant (DIPF) which only fluoresces in the ligand-binding and phosphorylated state (Figure 2I). The signal of this DIPF reporter was detected in both larval fat body and salivary gland (Figure 2—figure supplement 2F, H), which is consistent with active JAK signaling implicated in the development of the tissues (Chakrabarti et al., 2016; Krautz et al., 2020). When expressed in the tracheal system, DIPF displayed robust fluorescent signal in the tracheal progenitors (Figure 2J). These data suggest that receptor signaling of JAK/STAT is active in the tracheal progenitors.

To analyze the functional importance of JAK/STAT signaling in tracheal progenitors, we perturbed the principal components of this signaling, namely the receptor Dome, signal transducer Hop, or the downstream transcription factor Stat92E, by btl-Gal4-driven expression of RNAi constructs. Under these conditions in which JAK/STAT pathway is compromised, the tracheal progenitors aberrantly migrated anteriorly, which is reminiscent of upd2 loss-of-function in the fat body (Figure 3A–E, Video 4, and Figure 3—figure supplement 1A–D). The aberrant anterior migration of tracheal progenitors upon perturbation of JAK/STAT components led to incomplete regeneration of airway and impairment of tracheal integrity and caused melanization in the trachea (Figure 3—figure supplement 1E–I). In agreement with genetic perturbation of JAK/STAT signaling, pharmacological inhibition of JAK by a small-molecule inhibitor, Tofacitinib (Palmroth et al., 2021), also triggered bidirectional movement of tracheal progenitors (Figure 3F–H). The bidirectional movement was not due to excessive progenitors or crowding (Figure 3—figure supplement 2A).

![Figure 3.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig3-v1.jpg)

**Figure 3.:** (A–D’’) Migration of tracheal progenitors along the dorsal trunk at 0 hr APF, 1 hr APF, and 3 hr APF. The white dashed line shows transverse connective. The progenitors of control (A–A’’), domeRNAi (B–B’’), hopRNAi (C–C’’), and stat92ERNAi (D–D’’) flies. (E) Bar graph showing migration distance of progenitors. Error bars represent SEM, n = 6. (F–G’’) JAK inhibition causes bidirectional movement of progenitors. Migration of tracheal progenitors in the absence (DMSO-fed) (F–F’’) or in the presence of Tofacinib (JAK inhibitor) (G–G’’). (H) Bar graph showing the distance of anterior movement. Error bars represent SEM, n = 6. Scale bar: 200 μm (A–D’’, F–G’’). Genotypes: (A–A’’, F–G’’) btl-Gal4/+;P[B123]-RFP-moe/+; (B–B’’) btl-Gal4/+;P[B123]-RFP-moe/UAS-domeRNAi; (C–C’’) btl-Gal4/+;P[B123]-RFP-moe/UAS-hopRNAi; (D–D’’) btl-Gal4/+;P[B123]-RFP-moe/UAS-stat92ERNAi.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A–E) Migration of tracheal progenitors along the dorsal trunk at 0 hr APF, 1 hr APF, and 3 hr APF. The white dashed line shows transverse connective. The progenitors of control (A–A’’), dome mutants (B–B’’), hop mutants (C–C’’). (D) Bar graphs represent migration distance of anterior movement. Error bars represent SEM, n ≥ 3. N.S. indicates not significant. The pupal trachea in control (E), upd2 RNAi (F), domeG0264 (G), hoptum (H), and stat92EF (I). Scale bar: 200 μm (A–E), 20 mm (K–L’’). Genotypes: (A, E) lsp2-Gal4,P[B123]-RFP-moe/+ (control); (B) domeG0264; lsp2-Gal4,P[B123]-RFP-moe/+; (C) hoptum; lsp2-Gal4,P[B123]-RFP-moe/+; (F) lsp2-Gal4,P[B123]-RFP-moe/upd2RNAi. (G) domeG0264. (H) hoptum. (I) stat92EF.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (A) Statistics of the number of progenitor cells. Error bars represent SEM, n ≥ 9. N.S. indicates not significant. The expression of Stat92E-GFP in tracheal progenitors of control (B), domeRNAi (C), hopRNAi (D), and stat92ERNAi (E) flies. The progenitors are outlined by dashed lines. The expression of Stat92E-GFP in tracheal progenitors of control (F) or upd2RNAi flies (G). The expression of Stat92E-GFP in tracheal progenitors of DMSO-fed control, (H) or Tofacitinib-treated (I) flies. Dashed lines outline tracheal progenitors. (J) Bar graph plots relative intensity of Stat92E-GFP reporter. Error bars represent SEM, n = 6. N.S. indicates not significant. Scale bar: 50 μm (B–I). Genotypes: (A) btl-Gal4/+;P[B123]-RFP-moe/+(control); btl-Gal4/+;P[B123]-RFP-moe/UAS-domeRNAi; btl-Gal4/+;P[B123]-RFP-moe/UAS-hopRNAi; btl-Gal4/+;P[B123]-RFP-moe/UAS-stat92ERNAi; (B) btl-Gal4,Stat92E-GFP/+; (C) btl-Gal4,Stat92E-GFP/+;UAS-domeRNAi/+; (D) btl-Gal4,Stat92E-GFP/+;UAS-hopRNAi/+; (E) btl-Gal4,Stat92E-GFP/+;UAS-Stat92ERNAi/+; (F, H, I) Stat92E-GFP/+; lsp2-Gal4/+; (G) Stat92E-GFP/+;lsp2-Gal4/UAS-upd2RNAi.

![Video 4.](https://cdn.elifesciences.org/articles/100037/elife-100037-video4.mp4.jpg)

**Video 4.:** Scale bar: 100 μm. Genotypes: btl-Gal4/+;P[B123]-RFP-moe/+ (control), btl-Gal4/+;P[B123]-RFP-moe/UAS-domeRNAi, btl-Gal4/+;P[B123]-RFP-moe/UAS-hopRNAi, and btl-Gal4/+;P[B123]-RFP-moe/UAS-stat92ERNAi.

Concurrently, the activity of JAK/STAT pathway, as assessed by the Stat92E-GFP reporter (Bach et al., 2007), was substantially impaired when components of the pathway were depleted (Figure 3—figure supplement 2B–E, J). To determine whether the tracheal JAK/STAT signaling depends on fat body-derived Upd2, we depleted Upd2 in fat body and observed that Stat92E-GFP signal in tracheal progenitors was severely decreased, suggesting that JAK/STAT signaling in the trachea requires fat body-produced Upd2 (Figure 3—figure supplement 2F, G, J). Consistently, inhibition of JAK/STAT signaling using Tofacitinib reduced the expression of Stat92E-GFP (Figure 3—figure supplement 2H–J). Taken together, these observations suggest that Upd2-responsive JAK/STAT signaling in the trachea is essential for the disciplined migration of progenitors.

### Genes regulated by JAK/STAT signaling in the trachea

To gain a comprehensive understanding of the molecular details underlying the discipline of tracheal progenitor migration, we conducted genomic chromatin immunoprecipitation (ChIP-seq) to identify loci bound by Stat92E which functions as the transcription factor of JAK/STAT pathway. This revealed a total of 21,312 Stat92E binding peaks, ~95.7% of which located within 2 kb of transcription start sites of annotated genes (Figure 4—figure supplement 1A). In particular, 86% of the peaks (18,328 peaks) were enriched either in promoter regions or within gene bodies, and 66.1% of the peaks (13,490 peaks) resided near the 5ʹ ends of annotated genes, namely in the promoter regions, first exons and first introns (Figure 4—figure supplement 1B, C). GO analysis of putative target genes of Stat92E identified one cluster associated with establishment of planar polarity (Figure 4A). In line with this, the functional class associated with establishment of planar polarity was also abundantly represented among the DEGs upon the activation of tracheal progenitors in larval–pupal transition (Figure 4B). Notably, Stat92E binding was detected in the promoters and intronic regions of genes functioning in distal-to-proximal signaling (Cho and Irvine, 2004), such as dachsous (ds), four-jointed (fj), fz, stan, Vang, and fat2 (Figure 4C). Additionally, Stat92E occupied in the promoter regions of crb and yurt, two genes involved in apical–basal polarity and tracheal tube growth (Laprise et al., 2006; Schottenfeld-Roames and Ghabrial, 2012; Schottenfeld-Roames et al., 2014; Figure 4—figure supplement 1D). The enrichment of Stat92E in the promoters and/or regulatory regions of these putative targets was confirmed by ChIP-qPCR (Figure 4—figure supplement 1E).

![Figure 4.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig4-v1.jpg)

**Figure 4.:** (A) Bubble plot represents the top functional clusters among gene targets. The establishment of planar polarity denoted in red solid box is identified with high enrichment score. (B) Top functional classes among the differentially expressed genes in larval–pupal transition. (C) ChIP-seq peaks at loci regulated by Stat92E. Scale bar: 20 kb (ds, fz, stan), 5 kb (fat2, vg), 1 kb (fj). (D–H) Validation of gene targets of Stat92E ChIP-seq. The expression of Ds-GFP in the tracheal progenitors of control (D), domeRNAi (E), hopRNAi (F), and stat92ERNAi (G). The progenitors are outlined by dashed lines. (H) The bar graphs plot the relative level of Ds. Error bars represent SEM, n = 6. (I–M) The expression of Fj in tracheal progenitors. The expression of Fj-GFP in the tracheal progenitors of control (I), domeRNAi (J), hopRNAi (K), and stat92ERNAi (L). Dashed lines outline tracheal progenitors. (M) The bar graphs plot the relative level of Fj. Error bars represent SEM, n = 6. (N–R) The level of Ft-GFP in the tracheal progenitors of control (N), domeRNAi (O), hopRNAi (P), and stat92ERNAi (Q). (R) The bar graphs plot the relative level of Ft. Error bars represent SEM, n = 4. Scale bar: 50 μm (D–G, I–L, N–Q). Genotypes: (D) btl-Gal4,Ds-GFP/+; (E) btl-Gal4,Ds-GFP/+;UAS-domeRNAi/+; (F) btl-Gal4,Ds-GFP/+;UAS-hopRNAi/+; (G) btl-Gal4,Ds-GFP/+;UAS-stat92ERNAi/+; (I) btl-Gal4,Fj-GFP/+; (J) btl-Gal4,Fj-GFP/+;UAS-domeRNAi/+; (K) btl-Gal4,Fj-GFP/+;UAS-hopRNAi/+; (L) btl-Gal4,Fj-GFP/+;UAS-stat92ERNAi/+; (N) btl-Gal4/+;Ft-GFP/+; (O) btl-Gal4/+;Ft-GFP/UAS-domeRNAi; (P) btl-Gal4/+;Ft-GFP/UAS-hopRNAi; (Q) btl-Gal4/+;Ft-GFP/UAS-stat92ERNAi.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Pie chart (A, B) and histogram (C) depicting the distribution of ChIP-seq peaks relative to the nearby annotated genes. (D) Peaks of Stat92E association in the promotor regions of yurt and crb. Scale bar: 2 kb for yurt, 5 kb for crb. (E) Relative enrichment of JAK/STAT target genes analyzed by ChIP-qPCR. The expression of Fat2-GFP in the tracheal progenitors of control (F), domeRNAi (G), hopRNAi (H), and stat92ERNAi (I). The progenitors are outlined by dashed lines. (J) The bar graphs plot the relative level of Fat2. Error bars represent SEM, n = 6. The expression of Yurt in tracheal progenitors. The expression of Yurt-GFP in the tracheal progenitors of control (K), domeRNAi (L), hopRNAi (M), and stat92ERNAi (N). The progenitors are outlined by dashed lines. (O) The bar graphs plot the relative level of Yurt. Error bars represent SEM, n = 6. The expression of Crb-GFP in the tracheal progenitors of control (P), domeRNAi (Q), hopRNAi (R), and stat92ERNAi (S). The progenitors are outlined by dashed lines. (T) The bar graphs plot the relative level of Crb. Error bars represent SEM, n = 6. (U) The expression of JAK/STAT targets in the trachea of stat92ERNAi flies. Quantitative RT-PCR was performed in triplets to analyze the mRNA level. The expression levels in stat92ERNAi larvae were presented relative to Gal4 control. Scale bar: 50 μm (F–I, K–N, P–S). Genotypes: (F) btl-Gal4,Fat2-GFP/+; (G) btl-Gal4,Fat2-GFP/+;UAS-domeRNAi/+; (H) btl-Gal4,Fat2-GFP/+;UAS-hopRNAi/+; (I) btl-Gal4,Fat2-GFP/+;UAS-stat92ERNAi/+; (J) btl-Gal4/+;Yurt-GFP/+; (K) btl-Gal4/+;Yurt-GFP/UAS-domeRNAi; (L) btl-Gal4/+;Yurt-GFP/UAS-hopRNAi; (M) btl-Gal4/+;Yurt-GFP/UAS-stat92ERNAi; (P) btl-Gal4/+;Crb-GFP/+; (Q) btl-Gal4/+;Crb-GFP/UAS-domeRNAi; (R) btl-Gal4/+;Crb-GFP/UAS-hopRNAi; (S) btl-Gal4/+;Crb-GFP/UAS-stat92ERNAi.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** The level of Ft-GFP in control (A), UAS-ds (B), and dsRNAi (C) flies. (D) Bar graph represents the signal of Ft-GFP. Error bars represent SEM, n = 4. Scale bar: 50 μm (A–C). Genotypes: (A) btl-Gal4/+;Ft-GFP/+; (B) btl-Gal4/+;Ft-GFP/UAS-ds; (C) btl-Gal4/+;Ft-GFP/UAS-dsRNAi.

To further validate these putative Stat92E targets and investigate their dependence on JAK/STAT signaling, we analyzed their expression from several fosmid transgenes which have a GFP tag fused to ds, fj, or ft and express at endogenous levels. Ds and Fj were abundant in the progenitor cells, but were vastly reduced upon depletion of dome, hop, or stat92E, suggesting that they are regulated by JAK/STAT pathway (Figure 4D–M). Furthermore, it is reported that the function of Ft is influenced by cell-autonomous increase of Ds level and its protein level is enhanced by Ds reduction (Ambegaonkar et al., 2012; Matakatsu and Blair, 2004), which is also evidenced by our analysis using dsRNAi and UAS-ds in the tracheal progenitors (Figure 4—figure supplement 2A–D). In accordance with this notion, the level of Ft, as assayed by the Ft-GFP reporter, was elevated by the reduction of JAK/STAT signaling (Figure 4N–R). We also analyzed GFP-tagged fosmid transgenes of fat2, crb, and yurt and found that they were discernably reduced upon impairment of JAK/STAT signaling, suggesting that they are also regulated by JAK/STAT pathway (Figure 4—figure supplement 1F–T). Additionally, the transcription of ds, fj, ft, fat2, crb, and yurt was compromised by expression of stat92ERNAi (Figure 4—figure supplement 1U). In sum, these results suggest that JAK/STAT promotes components involved in the establishment of polarity in tracheal cells.

### The roles of JAK/STAT targets in the disciplined migration

To evaluate the functional roles of the polarity proteins in tracheal progenitor migration, we perturbed their expression in the tracheal progenitors by expressing RNAi against ds, ft, or fj, which were identified by ChIP-seq as the targets of JAK/STAT. In these flies, tracheal progenitors exhibited bidirectional movement, which is reminiscent of the impairment of JAK/STAT signaling (Figure 5A–E and Video 5). Similar observations were obtained by over-expression of ft or ds in the trachea (Figure 5—figure supplement 1A–D), consistent with previous reports that both loss- and gain-of-function of PCP components disrupt the PCP (Adler et al., 2000; Tree et al., 2002; Vinson and Adler, 1987). The disciplined migration of tracheal progenitors was also impaired by the expression of fat2RNAi, crbRNAi, yurtRNAi, or scbRNAi (Figure 5—figure supplement 1E–I), but was not affected by perturbation of molecules involved in cell adhesion such as Enabled (Ena), Fak, E-cadherin, and Robo2 (Figure 5—figure supplement 1J).

![Figure 5.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig5-v1.jpg)

**Figure 5.:** (A–E) Migration of tracheal progenitors. The migration of progenitors in control (A–A’’), dsRNAi (B–B’’), ftRNAi (C–C’’), and fjRNAi (D–D’’) flies. (E) Bar graph plots the migration distance of anterior movement. Error bars represent SEM, n = 4. Level of Ft in tracheal progenitors of control (F, G) and stat92ERNAi (H–J) flies. The images show progenitors at 1 hr APF (H, H’) and 2 hr APF (I, I’). Ft-GFP (green) (F, H, I), phalloidin (magenta), Hoechst (blue), and merged images (F’, H’, I’). Profile plots showing the level of Ft-GFP in control (G) and stat92ERNAi (J) flies, n = 5. ANOVA test: p < 0.0001. The levels of Ft were measured along the dotted lines in F’ or I’. Anterior (A) and posterior (P). (K) Representative traces plot the migration distance relative to the origin, n = 12. The x-axis represents the number of captured images. Individual frame is captured every 5 min. (K’) Rose plot depicting the direction of cell movement. (L) Representative traces showing the movement of individual fj-KO cells relative to their origin, n = 11. The x-axis represents the number of captured images. Individual frame is captured every 5 min. (L’) Rose plot depicting the movement direction of fj-KO cells. (M) Scatter plots represent the ratio (d/D) of straight-line length displacement (d) relative to the length of the migration track (D) of individual cell. Error bars represent SEM. N.S. indicates not significant. Scale bar: 200 μm (A–D’’), 50 μm (F, F’), 100 μm (H–I’). Genotypes: (A–A’’) btl-Gal4/+;P[B123]-RFP-moe/+; (B–B’’) btl-Gal4/UAS-dsRNAi;P[B123]-RFP-moe/+; (C–C’’) btl-Gal4/+;P[B123]-RFP-moe/UAS-ftRNAi; (D–D’’) btl-Gal4/UAS-fjRNAi;P[B123]-RFP-moe/+; (F, F’) btl-Gal4/+;Ft-GFP/+; (H, H’, I, I’) btl-Gal4/+;Ft-GFP/UAS-stat92ERNAi.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** The migration of progenitors at 0 hr APF (A), 1 hr APF (A’), 3 hr APF (A’’) in control (A–A’’), UAS-ds (B–B’’), UAS-ft (C–C’’), fat2RNAi (E–E’’), crbRNAi (F–F’’), yurtRNAi (G–G’’) and scbRNAi (H–H’’). (D, I, J) Bar graph plots the migration distance of anterior movement. Error bars represent SEM, n ≥ 3. N.S. indicates not significant. Scale bar: 200 μm (A–C’’, E–H’’). Genotypes: (A–A’’) btl-Gal4/+;P[B123]-RFP-moe/+; (B–B’’) btl-Gal4/+;P[B123]/UAS-ds; (C–C’’) btl-Gal4/UAS-ft;P[B123]/+; (E–E’’) btl-Gal4/+;P[B123]-RFP-moe/UAS-fat2RNAi; (F–F’’) btl-Gal4/+;P[B123]-RFP-moe/UAS-crbRNAi; (G–G’’) btl-Gal4/+;P[B123]-RFP-moe/UAS-yurtRNAi; (H–H’’) btl-Gal4/+;P[B123]-RFP-moe/UAS-scbRNAi. (J) btl-Gal4/+;P[B123]-RFP-moe/+ (control); btl-Gal4/+;P[B123]-RFP-moe/UAS-enaRNAi; btl-Gal4/UAS-fakRNAi;P[B123]-RFP-moe/+; btl-Gal4/+;P[B123]-RFP-moe/UAS-E-cadRNAi; btl-Gal4/+;P[B123]-RFP-moe/UAS-robo2RNAi.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** The confocal image showing the filopodia at the leading edge of migrating tracheal progenitors in control (A) and upd2RNAi flies (B). Arrows denote anterior–posterior (A–P) axis. Dashed lines indicate dorsal trunk. (C) Bar graph depicting the number of filopodia extending from leading edge. Error bars represent SEM, n = 8. Expression of bnl-lacZ in the trachea of control (D) and stat92ERNAi (E) flies. Scale bar: 100 μm (A, B), 500 μm (D, E). Genotypes: (A) lsp2-Gal4,P[B123]-RFP-moe/+; (B) lsp2-Gal4,P[B123]-RFP-moe/UAS-upd2RNAi.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** (A) Representative traces plot the migration distance relative to the origin, n ≥ 10. (B) Rose plot depicting the direction of cell movement. (C) Representative traces showing the movement of individual dsRNAi cells relative to their origin. (D) Rose plot depicting the movement direction of dsRNAi cells. (E) Representative traces showing the movement of individual ftRNAi cells relative to their origin. (F) Rose plot depicting the movement direction of ftRNAi cells. (G) Scatter plots represent the ratio (d/D) of straight-line length displacement (d) relative to the length of the migration track (D) of individual cell.

![Video 5.](https://cdn.elifesciences.org/articles/100037/elife-100037-video5.mp4.jpg)

**Video 5.:** Scale bar: 100 μm. Genotypes: btl-Gal4/+;P[B123]-RFP-moe/+ (control), btl-Gal4/UAS-dsRNAi;P[B123]-RFP-moe/+, and btl-Gal4/+;P[B123]-RFP-moe/UAS-ftRNAi.

Migratory cells generate protrusions at the leading edge to initiate movement (Cetera et al., 2014). The normal posteriorly migrating tracheal progenitors extend protrusions toward the migratory directions (Figure 5—figure supplement 2A), but in the bidirectionally moving progenitors in which upd2 in fat body was perturbed, extensive filopodia were projected from both the anterior and posterior fronts (Figure 5—figure supplement 2B, C), indicating that the aberrantly anteriorly moving progenitors may adopt the identity as those moving posteriorly. Bidirectionally migrating progenitors induced by perturbation of JAK/STAT signaling did not alter the expression of the tracheal inducer, branchless (bnl) (Figure 5—figure supplement 2D, E). Further analysis revealed that the progenitors exhibited elevated levels of Ft at the leading edge where they attached to DT (Figure 5F, G). Accordingly, progenitors that underwent bidirectional movement exhibited pronounced abundance of Ft at both the anterior and posterior frontal edges (Figure 5H–J). To further evaluate the functional roles of Ft–Ds–Fj module in disciplined migration, we utilized the high-mobility carcinoma cells, SKOV-3, and found that perturbation of Fj that phosphorylates the extracellular cadherin domains of both Ft and Ds and modifies their heterophilic binding (Thomas and Strutt, 2012), Ft or Ds concurrently displayed compromised directionality and reduced consistency of movement in a two-dimensional culture (Figure 5K–M, Figure 5—figure supplement 3). Together with the results in previous sections, these observations suggest that the activated tracheal progenitors establish a disciplined migration through the asymmetrical distribution of polarity proteins which is directed by an Upd2–JAK/STAT signaling stemming from the remote organ of fat body.

### Upd2 in the fat body-produced vesicle

Besides the JAK/STAT signaling, another functional class enriched for vesicle-mediated transport was prominent from our surface proteome analysis of the trachea (Figure 2H). A series of components that function in vesicle trafficking were identified. It has been reported that IL-6 cytokines tend to be encapsulated in secretory vesicles (Kandere-Grzybowska et al., 2003; Verboogen et al., 2018). To visualize Upd2 production and investigate its transportation kinetics, an upd2-mCherry transgene was developed and expressed under the control of lsp2-Gal4, which enabled tracking the dynamics of Upd2 in fat body (Figure 6A). In agreement with Upd2 being transported through vesicles, administration of L3 larvae with Brefeldin A (BFA), which pharmacologically inhibits vesicle formation and transport, sequestered Upd2 proteins in fat body (Figure 6B, C). To track the destination of the Upd2-containing vesicles, we examined mCherry signals in adjacent tissues and detected considerable amount of Upd2 puncta in the tracheal progenitors (Figure 6D). BFA treatment reduced Upd2-mCherry puncta in the tracheal progenitors, suggesting that tracheal progenitors receive vesicular Upd2 from the fat body (Figure 6E, F). Perturbation of Grasp65, a Golgi reassembly stacking protein previously implicated in Upd2 secretion (Rajan et al., 2017), also led to sequestration of Upd2-containing vesicles in fat body (Figure 6G, H, J). The vesicle formation, function, and extracellular movement are dependent on the tetraspanin superfamily proteins (Andreu and Yáñez-Mó, 2014). We surveyed all the tetraspanin orthologs in fly for potential roles in Upd2 vesicle formation and transport. When expressing lbmRNAi in fat body, Upd2-containing vesicles were vastly increased (Figure 6I, J). Meanwhile, perturbation of vesicle secretion or transport by expressing grasp65RNAi or lbmRNAi in fat body eliminated the presence of fat body-origin Upd2 in the trachea, suggesting that fat body-produced Upd2-containing vesicles function cell non-autonomously and contribute to other tissues/organs (Figure 6K–N). It should be noted that knockdown of upd2 in the trachea did not alter the discipline of tracheal progenitor migration (Figure 2—figure supplement 1K–M). Collectively, these results suggest that fat body-produced Upd2 undergoes vesicle-mediated trafficking.

![Figure 6.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig6-v1.jpg)

**Figure 6.:** The number of Upd2-mCherry-containing vesicles in fat body of control DMSO-fed (A) and BFA-treated L3 larvae (B). Larger view in lower magnification is provided in Figure 6—figure supplement 1. (C) Bar graph plots the number of Upd2-mCherry-containing vesicles in fat body. Error bars represent SEM, n = 6. The confocal image showing the number of Upd2-containing vesicles in progenitors of DMSO-fed control (D) and BFA-treated flies (E). (F) Bar graph plots the number of Upd2-mCherry-containing vesicles in progenitors. Error bars represent SEM, n = 4. (G) The number of Upd2-mCherry containing vesicles (red) in fat body. Upd2 accumulation in fat body was increased in the presence of grasp65RNAi (H) and lbmRNAi (I). (J) Bar graph plots the number of Upd2-mCherry-containing vesicles. Error bars represent SEM, n = 4. The Upd2 vesicles (red) in tracheal progenitors (DAPI) in control (K), grasp65RNAi (L), and lbmRNAi (M) flies. Dashed lines outline tracheal progenitors. (N) Bar graph plots the number of Upd2-mCherry-containing vesicles in progenitors. Error bars represent SEM, n = 4. Scale bar: 20 μm (A, B, G–I), 50 μm (D, E, K–M). Genotypes: (A–G, K) UAS-upd2-mCherry/+;lsp2-Gal4/+; (H, L) UAS-upd2-mCherry/UAS-grasp65RNAi;lsp2-Gal4/+; (I, M) UAS-upd2-mCherry/+;lsp2-Gal4/UAS-lbmRNAi.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Scale bar: 50 um.

### The vesicular transport in JAK/STAT signaling

The results in previous section suggest that the ligand of JAK/STAT signaling is transported in a manner that depends on vesicle trafficking. To validate the role of fat body-produced vesicles in inter-organ signaling, we used genetic and pharmacological tools to perturb different processes of vesicle trafficking in fat body and monitored JAK/STAT signaling in the tracheal progenitors. Expression of grasp65RNAi in fat body reduced the activity of JAK/STAT signaling in the trachea, as assessed by the Stat92E-GFP reporter (Figure 7A, B). Similarly, RNAi targeting expression of lbm in fat body vanished JAK/STAT signal transduction in the trachea (Figure 7C). Rab GTPases coordinate vesicle trafficking and production (Stenmark, 2009) and have been shown to play pivotal roles in the regulation of intracellular trafficking of FGFR and EGFR (Letizia et al., 2023; Olivares-Castiñeira and Llimargas, 2017), and were identified in the surface proteome analysis. Consistently, knockdown of rab5 or rab7 in fat body reduced the activity of JAK/STAT signaling in the progenitor cells (Figure 7D–F). Corroborating the genetic manipulations, BFA treatment that impeded vesicular transport also resulted in impairment of JAK/STAT signaling in trachea (Figure 7G–I). Taking advantage of the aforementioned DIPF reporter to assess the response of receiving cells to ligands, we found that the fluorescent signal of DIPF was compromised upon the presence of BFA, but was unaffected by inhibitors that target the downstream JAK protein (Figure 7J–M), suggesting that signaling ligands are less abundant in the recipient progenitor cells and that the vesicle-mediated transport of ligands is essential for JAK/STAT signaling.

![Figure 7.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig7-v1.jpg)

**Figure 7.:** The expression of Stat92E-GFP in tracheal progenitors of control (A), grasp65RNAi (B), lbmRNAi (C), rab5RNAi (D), and rab7RNAi (E) flies. The progenitors are outlined by dashed lines. (F) Bar graph plots the relative expression of Stat92E-GFP. Error bars represent SEM, n = 7. The expression of Stat92E-GFP in tracheal progenitors in DMSO-fed (G) and BFA-treated (H) flies. (I) Bar graph plots the relative expression of Stat92E-GFP. Error bars represent SEM, n = 5. (J) The signal of DIPF reporter in tracheal progenitors. (K) The effects of Tofacinib (JAK inhibitor) on DIPF reporter in progenitors. (L) The effects of Brefeldin A on DIPF reporter in progenitors. Dashed lines outline tracheal progenitors. (M) Bar graphs showing the signal of DIPF reporter. Error bars represent SEM, n = 4. Migration of tracheal progenitors in DMSO-fed flies (N–N’’) and BFA-treated flies (O–O’’). (P) Bar graph plots migration distance of anterior movement. Error bars represent SEM, n ≥ 3. (Q–U’’) Migration of tracheal progenitors at 0 hr APF (Q), 1 hr APF (Q’), and 3 hr APF (Q’’). The confocal images showing the tracheal progenitors in control (Q–Q’’), grasp65RNAi (R–R’’), lbmRNAi (S–S’’), rab5RNAi (T–T’’), and rab7RNAi (U–U’’) flies. (V) Bar graph plots the migration distance of anterior movement. Error bars represent SEM, n = 4. Scale bar: 50 μm (A–E, G, H, J–L), 200 μm (N–O’’, Q–U’’). Genotypes: (A, G, H) lsp2-Gal4,Stat92E-GFP/+; (B) UAS-grasp65RNAi/+;lsp2-Gal4,Stat92E-GFP/+; (C) lsp2-Gal4,Stat92E-GFP/UAS-lbmRNAi; (D) UAS-rab5RNAi/+;lsp2-Gal4,Stat92E-GFP/+; (E) UAS-rab7RNAi/+;lsp2-Gal4,Stat92E-GFP/+; (J–L) btl-Gal4/UAS-DIPF; (N–Q’’) lsp2-Gal4,P[B123]-RFP-moe/+; (R–R’’) lsp2-Gal4,P[B123]-RFP-moe/UAS-grasp65RNAi; (S–S’’) lsp2-Gal4,P[B123]-RFP-moe/+;UAS-lbmRNAi/+; (T–T’’) UAS-rab5RNAi/+;lsp2-Gal4,P[B123]-RFP-moe/+; (U–U’’) UAS-rab7RNAi/+;lsp2-Gal4,P[B123]-RFP-moe/+.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** Migration of tracheal progenitors. The migration of progenitors at 0 hr APF, 1 hr APF, and 3 hr APF in control (A–A’’), rab2RNAi (B–B’’), rab3RNAi (C–C’’). (D) Bar graph plots the migration distance of anterior movement. Error bars represent SEM, n ≥ 3. (E–E’’) The confocal images showing the colocalization between Upd2 (red) (E) and Rab3 (GFP) (E’). (E’’) Merged images. Scale bar: 200 μm (A–C’’), 5 μm (E–E’’). Genotypes: (A–A’’) lsp2-Gal4,P[B123]-RFP-moe/+; (B–B’’) lsp2-Gal4,P[B123]-RFP-moe/UAS-rab2RNAi; (C–C’’) lsp2-Gal4,P[B123]-RFP-moe/UAS-rab3RNAi; (E–E’’) UAS-upd2-mCherry/UAS-rab3-YFP;lsp2-Gal4/+.

Phenotypically, the tracheal progenitors exhibited bidirectional migration in BFA-treated flies, which phenocopies JAK/STAT loss-of-function (Figure 7N–P). In concord with this observation, depletion of grasp65 or lbm also led to bidirectional movement (Figure 7Q–S’’, and Video 6). Similar observations were made in tracheal progenitors with either rab5 or rab7 knockdown (Figure 7T–V), whereas perturbation of neither rab2 nor rab3 affected the disciplined progenitor migration (Figure 7—figure supplement 1A–C). Taken together, these results suggest that JAK/STAT signaling in the trachea is dependent on the vesicle-mediated transport of its ligands from fat body.

![Video 6.](https://cdn.elifesciences.org/articles/100037/elife-100037-video6.mp4.jpg)

**Video 6.:** Scale bar: 100 μm. Genotypes: lsp2-Gal4,P[B123]-RFP-moe/+ (control) and lsp2-Gal4,P[B123]-RFP-moe/+;UAS-lbmRNAi/+.

### The interaction between Upd2 and endocytic machinery

Our results described thus far suggest that Upd2 emanating from fat body signals to JAK/STAT signaling in the trachea. To further explore the molecular basis underlying the vesicular transport of Upd2, we monitored Rab5-GFP and Rab7-GFP in fat body, which mark early and late endosomes, respectively (Vonderheit and Helenius, 2005). The fat body-produced Upd2 appeared vesicular (Figure 8A) and both Rab5 and Rab7 were found adjacent to the Upd2-harboring vesicles, suggesting that both Rab GTPases function in the transport of Upd2 (Figure 8A’–B’’). In contrast, Rab3 exhibited non-overlapping distribution with Upd2 (Figure 7—figure supplement 1E–E’’). Furthermore, we observed that Grasp65 was in close proximity to Upd2-containing vesicles, indicating its integral roles in these vesicles (Figure 8C–C’’). In addition, Upd2 was observed to colocalize with the tetraspanin, Lbm (Figure 8D–D’’). At higher resolution, Upd2 and Lbm showed close association in a supramolecular configuration (Figure 8D’’’, D’’’’), corroborating its role in the transport of Upd2. To determine if Upd2 interacts with the coordinators of vesicle trafficking, we employed the Duolink in situ proximity ligation assay (PLA) which revealed strong interactions between Upd2 and Rabs, such as Rab5 and Rab7 (Figure 8E–H), as well as Lbm (Figure 8I, J). The interaction was further validated by the revelation that Upd2 co-immunoprecipitated with Rab5 and Rab7 (Figure 8K, L). The presence of Upd2 in Lbm-containing vesicles was also evidenced in S2 cells (Figure 8—figure supplement 1A–C’’) and co-IP experiment showed that Lbm physically associated with Upd2 in both fat body and S2 cells (Figure 8M, Figure 8—figure supplement 1F). To further understand the biogenesis of Lbm-containing vesicles that transport Upd2, we conducted electron microscopic analysis of the Lbm-containing vesicles through the expression of an HRP-fused Lbm in the fat body (Figure 8—figure supplement 1D). The interaction between Lbm and Upd2 as simulated by Alphafold2 supported their direct association (Figure 8—figure supplement 1E). Then, we generated an Lbm chimera tagged with a pH-sensitive GFP variant, pHluorin (Yoshihara et al., 2005). PHluorin fluorescence is squelched at the low pH domain such as in intravesicular compartments, but becomes detectable when exposed to the extracellular environment, thus enabling detection of exocytosis and endocytosis. Fat body expressing Lbm-pHluorin produced GFP puncta at the plasma membrane (Figure 8N), and the GFP signal was also detected in the trachea, suggesting the reception and internalization of Lbm-containing vesicles by tracheal cells (Figure 8O). However, the GFP fluorescence in both fat body and trachea was dramatically decreased by BFA treatment, suggesting that Lbm-containing vesicles are diminished (Figure 8—figure supplement 1G–J). Accordingly, the signals of Lbm-pHluorin in both fat body and responding tracheoblasts were apparently compromised when Rab5 or Rab7 was perturbed (Figure 8P–S), suggesting that the biogenesis and production of Lbm-containing vesicles depend on Rab-mediated vesicle trafficking. Taken together, these results suggest that fat body-derived Upd2 interacts with Rab-mediated endocytic trafficking system to control the disciplined movement of tracheal progenitors.

![Figure 8.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig8-v1.jpg)

**Figure 8.:** (A–D’’’) The confocal images showing the colocalization between Upd2 (red) (A–D) and Rab5 (GFP) (A’), Rab7 (GFP) (B’), Grasp65 (GFP) (C’), or Lbm (GFP). (A’’, B’’, C’’, D’’) Merged images. (D’’’) 3D high-magnification view of the boxed inset in D’’. (D’’’’) The Pearson’s correlation coefficient depicting colocalization between Lbm and Upd2 in fat body cells. The PLA (proximity ligation assay) assay showing the interaction between Upd2 and Rab5 (E, F), Rab7 (G, H), or Lbm (I, J). Co-immunoprecipitation assay showing physical interaction between Upd2 and Rab5 (K), Rab7 (L), or Lbm (M) in larval fat body. (N–T) The expression of Lbm-pHluorin in larval fat body and progenitors of control (N, O), rab5RNAi (P, Q), and rab7RNAi (R, S) flies. Dashed lines outline tracheal progenitors. Arrowheads point to Lbm-pHluorin puncta. DAPI signal indicates nuclei. (T) Schematic diagram depicting Upd2-operated disciplined migration of tracheal progenitors. Scale bar: 5 μm (A–D’’, E–J), 10 μm (N, P, R), 20 μm (O, Q, S). Genotypes: (A–A’’, E, F) UAS-upd2-mCherry/+;lsp2-Gal4/UAS-GFP-rab5; (B–B’’, G, H) UAS-upd2-mCherry/+;lsp2-Gal4/UAS-GFP-rab7; (C–C’’) UAS-upd2-mCherry/UAS-grasp65-GFP;lsp2-Gal4/+; (D–D’’’’, I–L) UAS-upd2-mCherry/UAS-lbm-GFP;lsp2-Gal4/+; (N, O) UAS-lbm-pHluorin/+;lsp2-Gal4/+; (P, Q) UAS-lbm-pHluorin/UAS-rab5RNAi;lsp2-Gal4/+; (R, S) UAS-lbm-pHluorin/UAS-rab7RNAi;lsp2-Gal4/+.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/100037/elife-100037-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** (A–C’’) Co-localization and interaction between Lbm and Upd2. Co-transfection of act-Gal4, UAS-lbm-GFP (A) and UAS-upd2-mCherry (A’) in S2 cells. (A’’) Merged image. (B–C’’) Confocal images showing that Lbm co-localizes with Upd2 in vesicles along the protrusions of S2 cell. (D) Electron microscopic image of Lbm-HRP vesicles (dark) in fat body. (E) A predicted interaction between Lbm (blue) and Upd2 (green). (F) Co-immunoprecipitation assay showing the interaction between Lbm and Upd2 in S2 cells. The expression of Lbm-pHluorin in control fat body (G) and BFA-treated flies (H). The expression of Lbm-pHluorin in control tracheal progenitors (I) and BFA-treated flies (J). The tracheal progenitors were outlined by dashed lines. Scale bar: 10 μm (A–A’’), 20 μm (G, H). Genotypes: (G–J) UAS-lbm-pHluorin/+;lsp2-Gal4/+.

## Discussion

Resident stem cells and progenitors are mobilized to regenerate damaged or degenerated tissue. Despite the large distance between the niche where stem cells interact with their microenvironments and the destination for reconstruction, their commitment to a stereotyped track implicates sophisticated mechanism that controls disciplined migration as stem cells are activated and move out of the niche. While primary inducers expressed by damaged tissues are in play to coordinate the newly generated architecture with the degenerated counterpart (Chen and Krasnow, 2014), the present study elucidates an integral role of Upd2–JAK–STAT pathway in regulating the expression of polarity-related genes and maintaining the disciplined migration of tracheal progenitors (Figure 8T). The transport of Upd2 from fat body to trachea suggests intensive inter-organ communication during the migration of tracheal progenitors.

Several possibilities could account for the JAK/STAT-dependent polarity. The signaling components of JAK/STAT pathway could exhibit polarized localization (Sotillos et al., 2008). Alternatively, this signaling may activate genes controlling cell polarity and adhesion (Mallart et al., 2024; Tsurumi et al., 2011). Functional interplay between JAK/STAT signaling and cell polarity has been observed in various contexts (Chatterjee et al., 2023; Zeidler et al., 1999). Our results support a role of JAK/STAT signaling in promoting expression of genes with established roles in planar polarity, which may hallmark the route for the migration of the tracheal progenitor cells. Epithelial cells exhibit two aspects of polarity: apical–basal polarity and PCP. The latter refers to the collective alignment of cell polarity within the plane of an epithelial sheet (Zallen, 2007). Molecularly, PCP is generated by the asymmetry of a group of proteins (PCP proteins) that mediate communication between neighboring cells (Barlan et al., 2017; Matis and Axelrod, 2013; Williams et al., 2022). In Drosophila, the components of PCP are considered to group functionally into two core modules. The seven-pass transmembrane protein Frizzled (Fz), the cytosolic proteins Dishevelled (Dsh), Diego (Dgo), the four-pass transmembrane protein Strabismus (Stbm, also known as Van Gogh (Vang)) and the cytosolic protein Prickle (Pk) belong to the first module. The second module consists of Fat (Ft; also known as cadherin-related tumor suppressor), Dachsous (Ds), Four-jointed (Fj) and Atro (a transcription repressor) (Peng and Axelrod, 2012). Intensive functional interplay occurs between these two modules (Ayukawa et al., 2014). Aberrant activity of the core PCP proteins leads to misoriented hairs and complex swirling patterns (Ma et al., 2003; Wong and Adler, 1993). In addition to arrangement of epithelial appendages, PCP pathway is also required for collective and directed cell movements (Muñoz-Soriano et al., 2012). The migratory cell cohort is polarized into ‘pioneer’ cells that lead the trailing followers (Vitorino and Meyer, 2008).

Our data indicate that expression of Ds, Fj, Fz, Stan, and Fat2, core components or regulators of PCP, depends on JAK/STAT pathway. The interaction between atypical cadherin Fat (Ft) and its ligand, Dachsous (Ds) directs core protein asymmetry (Strutt and Strutt, 2021; Yang et al., 2002). Phenotypically, aberrancy of PCP protein abundance, either excessive core protein or deficit in expression gradients, gives rise to similar morphological abnormality (Adler et al., 2000; Casal et al., 2002; Taylor et al., 1998; Tree et al., 2002). Consistent with this notion, gain-of-function of Fj or Ds phenocopies that of perturbation of PCP proteins. JAK/STAT signaling promotes the expression of Ds, but reduces Ft expression (Figure 4). Thereby, perturbation of JAK/STAT signaling disrupts the Ds–Ft system.

A precedent for JAK/STAT signaling in directional cell movement is border cell migration from anterior to posterior compartment during Drosophila oogenesis. Migration of the border cells is guided by a gradient of PDGF and VEGF chemokines (Duchek et al., 2001). Loss of either hop (encoding JAK) or stat in the border cells impinges their recruitment into the cluster and subsequent migration (Silver et al., 2005). Our results suggest that JAK/STAT signaling does not serve as a guidance cue for tracheal progenitors, but rather directs the directionality of cell movement. The downstream PCP components may contribute to either polarity of progenitors or cell–cell interactions between the progenitors and tracheal cells that they track along. It remains unknown how individual progenitor cells perceive directional information and convert it into group choreography.

We identified the fly fat body as the major source for the JAK/STAT signaling ligand, Upd2 production. Fat body is functionally equivalent to the mammalian liver which stores proteins, lipids and sugars and functions as an energy reservoir (Li et al., 2019). It supplies proteins and/or hormones that are utilized by other organs, and thereby serves as an interchange center to disperse systemic hormonal and nutritional signals. For instance, it generates collagen IV to decorate imaginal discs and produces xanthine dehydrogenase for eye pigmentation (Pastor-Pareja and Xu, 2011; Reaume et al., 1989). The transport between fat body and trachea has been reported on a secreted chitin deacetylase, Serpentine (Serp), which is expressed by fat body and contributes to tracheal morphogenesis (Dong et al., 2014). Our results reveal that fat body also signals to regulate the disciplined migration of tracheal progenitors through the dispersion of Upd2 cytokines. These studies collectively suggest that fat body orchestrates systemic tissue growth and patterning and that metabolic regulation is critical for adult stem cells.

Proteins that are locally produced can execute systemic function in distant organs. A possible route of transport is through the hemolymph or bloodstream and taken up by the target tissues. The signaling proteins such as cytokines can be packaged in extracellular vesicles with various dimensions (Buzas, 2023; Javeed et al., 2021). A precedent of vesicular transport of signaling molecules is reported in migrasomes whose diameter exceeds 500 nm (Jiang et al., 2019).

These extracellular vesicles mediate cell-to-cell communication (Colombo et al., 2014), perhaps at a distance (Hood et al., 2011) and even traverse between organs (Corrigan et al., 2014). The vesicular Upd2 is able to signal at recipient cells, suggesting that the activity of Upd2 is preserved in the vesicle, and it is released upon vesicle fusion. Compared with conventional extracellular vesicles such as exosomes, the Upd2-containing vesicles possess larger dimension. Its production and trafficking depend on GRASP-mediated unconventional secretion and interaction with Lbm. Lbm belongs to the tetraspanin protein family that contains four transmembrane domains. The mammalian homologs of tetraspanins, CD9, CD63, CD81, or CD37 are principal constituents of extracellular vesicles. The Lbm-containing vesicles are regulated by GRASP-mediated secretion and are sensitive to pharmacological inhibition of EV transport.

It has been proposed that tetraspanins facilitate regeneration and wound healing in cultural cells and single-cell plasma membrane. Tetraspanin-enriched macrodomains are assembled into a ring-like structure (Huang et al., 2022), which is recruited to large membrane wounds and promotes membrane repair (Wang et al., 2022). The present study adds another dimension to the roles of tetraspanin proteins in tissue regeneration which can be ascribed to transport of signaling proteins and modulation of stem cells.

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
      <td>Gene (Drosophila melanogaster)</td>
      <td>upd2</td>
      <td>THFC</td>
      <td>THU1331, THU1288</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>dome</td>
      <td>THFC</td>
      <td>THU0574, THU5825</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>hop</td>
      <td>THFC</td>
      <td>THU5762, TH201501042.S</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>stat92E</td>
      <td>THFC</td>
      <td>THU0573, THU1915</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>lbm</td>
      <td>THFC,BDSC</td>
      <td>THU2602, BDSC27278</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>grasp65</td>
      <td>THFC</td>
      <td>TH04282.N, THU1429</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>rab5</td>
      <td>THFC</td>
      <td>TH02192.N, THU0671</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>rab7</td>
      <td>THFC</td>
      <td>TH02539.N, THU2437</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>fj</td>
      <td>THFC</td>
      <td>THU201500988.S, THU1538</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>fat2</td>
      <td>THFC,VDRC</td>
      <td>THU4120, VDRC27113</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>yurt</td>
      <td>THFC,VDRC</td>
      <td>THU1740, VDRC28674</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>crb</td>
      <td>THFC</td>
      <td>THU2783, THU5212</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>scb</td>
      <td>THFC</td>
      <td>THU3905, THU2707</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>ds</td>
      <td>THFC,VDRC</td>
      <td>THU2846, VDRC36219</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>ft</td>
      <td>THFC,VDRC</td>
      <td>TH201500989.S, VDRC9396</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>10×Stat92E-GFP</td>
      <td>THFC</td>
      <td>THJ0273</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Stat92E-GFP</td>
      <td>BDSC</td>
      <td>BDSC:38670</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-grasp65-GFP</td>
      <td>BDSC</td>
      <td>BDSC:8507</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Ds::GFP</td>
      <td>BDSC</td>
      <td>BDSC:59425</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-GFP-Rab7</td>
      <td>BDSC</td>
      <td>BDSC:9779</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-GFP-Rab5</td>
      <td>BDSC</td>
      <td>BDSC:24616</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>hopTum/FM7C</td>
      <td>BDSC</td>
      <td>BDSC:8492</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>stat92EF</td>
      <td>BDSC</td>
      <td>BDSC:24757</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>domeG0264</td>
      <td>Kyoto</td>
      <td>Kyoto:111866</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Yurt::GFP</td>
      <td>VDRC</td>
      <td>VDRC:318067</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Crb::GFP</td>
      <td>VDRC</td>
      <td>VDRC:318384</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Ft::GFP</td>
      <td>VDRC</td>
      <td>VDRC:318477</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Fj::GFP</td>
      <td>VDRC</td>
      <td>VDRC:318457</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-ft</td>
      <td>This paper; Brittle et al., 2010</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS-ds</td>
      <td>This paper; Brittle et al., 2012</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Fat2::GFP</td>
      <td>This paper; Barlan et al., 2017</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (D. melanogaster)</td>
      <td>S2</td>
      <td>CCTCC</td>
      <td>GDC#0138</td>
      <td>Verified by DNA barcoding; without mycoplasma contamination</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>SKOV3</td>
      <td>ATCC</td>
      <td>HTB-77</td>
      <td>Verified by STR genotyping; without mycoplasma contamination</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-GFP (Mouse monoclonal)</td>
      <td>Abclonal</td>
      <td>Cat# AE012</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-mCherry (Mouse polyclonal)</td>
      <td>Abclonal</td>
      <td>Cat# AE002</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 488</td>
      <td>Abclonal</td>
      <td>Cat# AS053</td>
      <td>IF (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 555</td>
      <td>Abclonal</td>
      <td>Cat# AS007</td>
      <td>IF (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Phalloidin Alexa Fluor 640</td>
      <td>Biotum</td>
      <td>Cat# 00050</td>
      <td>IF (1:50)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-tubulin (Rabbit polyclonal)</td>
      <td>Baoke</td>
      <td>Cat# BK7010</td>
      <td>WB (1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-GFP (Rabbit polyclonal)</td>
      <td>Invitrogen</td>
      <td>Cat# A11122</td>
      <td>IF (1:400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HRP-conjugated Streptavidin</td>
      <td>Proteintech</td>
      <td>Cat# SA00001</td>
      <td>WB (1:5000)</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>α-tubulin84b _F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CACACCACCCTGGAGCATTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>α-tubulin84b _R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CCAATCAGACGGTTCAGGTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>upd2_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TCAATCCGTATCGCGGTCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>upd2_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AGAAGAGTCGCAGGTTGTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>ds_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>ACAACCGAACTCGAACCGAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>ds_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AGTAGCATCACACACAAGTGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>ft_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CTGGATCGAGAGCAGCAGAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>ft_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GACGGTAAATTCTCGCGCAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>fj_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>ATTACTCAAGCGGTTGGGGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>fj_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CGGTTCCTGTTCCTGTCTCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>fat2_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TATCTGCGCCCATACGCATT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>fat2_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TCTCATCGGCCTTGCTTTGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>yurt_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GGTCAGCTCAGGGTGACTATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>yurt_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>ATTGGTAAGCTTGGCGTTGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>crb_F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CAGCAGTGTTTGAACGGTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>crb_R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AGGCAGTGACCAATGGGG</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Anti-FLAG M2 Magnetic Beads</td>
      <td>Millipore</td>
      <td>Cat# 8823</td>
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
      <td>SMART-Seq v4 Ultra low input RNA Kit</td>
      <td>Takara</td>
      <td>Cat# 634889</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>AMPure XP</td>
      <td>Beckman Coulter</td>
      <td>Cat# A63882</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TruePrep DNA Library Prep Kit V2</td>
      <td>Vazyme</td>
      <td>Cat# TD501</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>BXXP</td>
      <td>APEXBIO</td>
      <td>Cat# A8012</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji/ImageJ</td>
      <td>NIH</td>
      <td>RRID:SCR_002285</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism 8.0</td>
      <td>GraphPad Software</td>
      <td>https://www.graphpad.com/scientific-software/prism/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Zen 3.1</td>
      <td>Zeiss</td>
      <td>https://www.zeiss.com.cn/corporate/home.html</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PCA-flow</td>
      <td>Bradski, G.79</td>
      <td>https://www.drdobbs.com/open-source/the-opencv-library</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DAPI</td>
      <td>VECTASHIELD</td>
      <td>Cat# H1200</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Fly lines and husbandry

All flies were reared on normal cornmeal and agar medium at 25°C unless noted. UAS-upd2RNAi (THU1331, THU1288), UAS-domeRNAi (THU0574), UAS-hopRNAi (THU5762), UAS-stat92ERNAi (THU0573), UAS-lbmRNAi (THU2602), UAS-grasp65RNAi (TH04282.N), UAS-rab5RNAi (TH02192.N), UAS-rab7RNAi (TH02539.N), UAS-fjRNAi (THU201500988.S), UAS-fat2RNAi (THU4120), UAS-yurtRNAi (THU1740), UAS-crbRNAi (THU2783), and UAS-scbRNAi (THU3905) were ordered from Tsinghua Stock Center. Stat92E-GFP (BSDC#38670), UAS-grasp65-GFP (BSDC#8507), Ds::GFP (BSDC#59425) were from Bloomington Drosophila Stock Center. Yurt::GFP (v318067), Crb::GFP (v318384), Ft::GFP (v318477), Fj::GFP (v318457), UAS-dsRNAi (v36219, THU2846), and UAS-ftRNAi (v9396) were obtained from VDRC. UAS-ft was kindly provided by Dr. Xianjue Ma, UAS-ds was kindly provided by Dr. Xing Wang and UAS-fat2-GFP was from Dr. Shunfan Wu. UAS-GFP-rab5 and UAS-GFP-rab7 were kindly provided by Dr. Xiaohang Yang.

### Plasmid construction and transgenic flies

To generate UAS-upd2-mCherry and UAS-lbm-GFP, UAS-lbm-HRP transgenic flies, the coding sequence of upd2 or lbm was PCR amplified from a fly cDNA library and cloned into a pUAST vector with C-terminal mCherry, GFP, or HRP.

The DIPF reporter was generated by first fusing cpYFP and Drosophila FKBP12 and subsequently ligating to the dome cDNA via a GTG linker. The above product was then cloned into a pUAST vector and verified by DNA sequencing, and injected into y[1] M{vasint.Dm}ZH-2A w[*]; P{CaryP}attP2 recipient flies or w1118 following standard Drosophila transformation injection procedures (Core Facility of Drosophila Resource and Technology, SIBCB, CAS).

### Cell culture and transfection

S2 cells (CCTCC, GDC#0138) were grown in Schneider Drosophila Medium (Gibco, #21720024) supplemented with 10% (vol/vol) fetal bovine serum (FBS, Gibco, #10099141C) and 1% (vol/vol) penicillin–streptomycin (Pen/Strep, Life Technologies) at 28°C with 0.2% CO2. S2 cells were confirmed by DNA barcoding and verified to be mycoplasma-free using the Mycoplasma Stain Assay Kit. Transfection was conducted with 5 μg plasmids (act-GAL4, UAS-lbm-GFP, UAS-upd2-mCherry) using Effectene Transfection Reagent (QIAGEN, #301425).

SKOV3 cells (ATCC, HTB-77) were cultured in DMEM medium (CR#12800) containing 10% FBS (Gibco, #10099141C) in an incubator with 5% CO2 at 37°C. The SKOV3 cells were confirmed by STR genotyping and verified to be mycoplasma-free using the Mycoplasma Stain Assay Kit. Cells with ~80% confluency were infected with lentivirus loaded with siRNAs for gene knockdown or gRNAs for knockout, and the medium was replaced 24 hr post-infection. 72 hr after lentivirus infection, bright-field images were taken every 5 min for 12 hr using a confocal microscope.

### Quantitative reverse transcription PCR

Larval or pupal trachea were dissected in cold PBS, and then transferred to RNA extraction reagent (AG21101). Next, reverse transcription was performed using qPCR RT Mix with gDNA Remover reagent (AG11706). qPCR was performed using the Universal SYBR Select Master Mix (AG11701) with a Bio-Rad system. The foldchange of target gene expression was normalized to that of α-tubulin. The primers are listed in Key Resources Table.

### Western blotting and co-immunoprecipitation

Total protein was extracted from cells or tissues by RIPA buffer supplemented with a protease inhibitor cocktail (Merck, #11836170001) and phenylmethanesulfonyl fluoride (Beyotime, #ST507), separated by 10% SDS–PAGE gels and transferred to PVDF membrane (Millipore, #IPVH00010). Blots were detected with an ECL Western Blotting detection system (Bio-Rad). For co-immunoprecipitation, lysates of larval fat body or transfected S2 cells were incubated overnight at 4°C with protein A Magnetic beads (Thermo Scientific, #2736141) pre-coated with GFP antibody (Invitrogen, #A11122). Immunoprecipitates were eluted in SDS-containing loading buffer for subsequent immunoblotting analysis. Antibodies for immunoblotting include: α-tubulin (Baoke, #BK7010), α-HRP-conjugated streptavidin (Proteintech, #SA00001-0), α-GFP (Abclonal, #AE012, 1:1000), and α-mCherry (Abclonal, #AE002, 1:1000).

### Proximity ligation assay

PLA was carried out with Duolink In Situ Detection Reagents Far Red (Sigma-Aldrich, #DUO92013) according to manufacturer’s instructions, using the probes anti-rabbit PLUS (Sigma-Aldrich, #DUO92002) and anti-mouse MINUS (Sigma-Aldrich, #DUO92004). Briefly, larval fat body was dissected and fixed in 4% formaldehyde. The animals not expressing upd2-mCherry served as controls. After permeabilization, the samples were incubated with primary antibodies overnight at 4°C. Then, the samples were washed with PLA buffer A, hybridized with PLA probes, ligated, and amplified. Samples were washed twice with PLA buffer B (Sigma-Aldrich, #DUO82049) and fluorescence images were taken with an LSM Zeiss 900 inverted confocal laser scanner microscope.

### Immunofluorescence

Trachea from white pupae (0 hr APF) were dissected in PBS and fixed with 4% formaldehyde for 25 min at room temperature. After washes, trachea samples were permeabilized with 1% Triton X-100 in PBS, and then blocked in 10% goat serum. Incubation with primary antibody (GFP, 1:400; lacZ, 1:40) was performed at 4°C with gentle rotation for overnight. Then, the samples were incubated with secondary antibodies conjugated to Alexa Fluor 488 or 555 (1:200) and Phalloidin (1:50) for 2 hr. After washing, samples were mounted in antifade mounting medium with DAPI (VECTASHIELD) and imaged under an LSM Zeiss 900 inverted confocal laser scanner microscope.

### Live imaging of pupal trachea stem cells

White pupae (0 hr APF) were briefly washed in double distilled water and mounted in halocarbon oil 700 (Sigma, #H8898). The pupae were positioned with forceps to bring a single DT of the trachea up for optimal imaging of Tr4 and Tr5 metameres. Then, pupae were immobilized by a 22 × 30 mm No. 1.5 high precision coverslip spaced by vacuum grease. Time-lapse images were captured by an LSM Zeiss 900 inverted confocal laser scanner microscope. For migration distance measurement, we took sequential snapshots of the moving progenitors of pupae staged at 0, 1, 2, and 3 hr APF. The migration distance was measured as the distance from the starting position (the junction of TC and DT) to the leading edge of progenitor groups. The migration velocity was calculated by v = d (micrometer)/t (min).

### RNA sequencing of tracheal progenitors

Total RNA was isolated from the Tr4 and Tr5 metamere progenitors dissected from 1 hr APF pupae using RNeasy Micro Kit (QIAGEN, #74004). SMART-Seq v4 Ultra low input RNA Kit (Takara, #634889) was used for first- and second-strand cDNA synthesis and double-stranded cDNA end repair. Double-stranded cDNAs were cleaned using AMPure XP (Beckman Coulter, #A63882). Then cDNAs were subjected to tagmentation and ligation to adaptors to generate the sequencing libraries using TruePrep DNA Library Prep Kit V2 for Illumina kit (Vazyme, #TD501). The quality and concentration of the libraries were assessed using the Agilent High Sensitivity DNA Kit and Bioanalyzer 2100 (Agilent Technologies) and submitted to 150 bp paired-end high throughput sequencing using Hiseq4000 (Illumina).

Analysis of RNA-seq data was performed using a computer system equipped with multiple processors. Clean reads were mapped to the Drosophila genome sequence using Hisat2 with default parameters. Successfully mapped reads were counted using FeatureCounts. Differential gene expression analysis was performed using the DESeq2 package. Adjusted p-value <0.05 was used as the threshold to identify the DEGs. Gene ontology and KEGG pathway enrichment analyses for the DEGs were conducted using the Database for Annotation, Visualization and Integrated Discovery (DAVID).

### Chromatin immunoprecipitation

Third instar larval trachea from Stat92E-Flag (BDSC, #38670) were fixed in 1% formaldehyde. The fixation reaction was terminated by adding glycine (125 mM). Trachea were washed and resuspended in lysis buffer, and sonicated to generate 200–600 bp DNA fragments. Procedures of immunoprecipitation and ChIP sequencing library construction were as previously described (Li et al., 2022). Anti-FLAG M2 Magnetic Beads (Millipore, #8823) were used for enriched DNA binding to transcription factor Stat92E.

Immunoprecipitated DNA was subjected to next-generation sequencing using the Epicenter Nextera DNA Sample Preparation Kit or to real-time PCR. Library construction was performed using the High Molecular Weight tagmentation buffer, and tagmented DNA was linearly amplified by PCR. The libraries were then sequenced on a Novaseq according to the manufacturer’s standard protocols. The sequences were processed using Fastqc and low-quality bases and adaptor contamination were trimmed by cutadapt. Filtered reads were mapped to Drosophila genome using BWA mem algorithm. Peaks were called using macs2 callpeak (Zhao et al., 2019) and plotted using pyGenomeTracks. GO analysis of biological processes was conducted by DAVID.

### Cell-surface proteomics of fly trachea

Trachea from white pupae were dissected in pre-cooled Schneider Medium (Gibco) and collected in 1.5 ml low-binding tube (Axygen) containing 500 μl Schneider Medium. The samples were washed with 500 μl fresh medium and incubated with 100 μM BXXP (APEXBIO, #A8012) for 1 hr on ice with occasional pipetting. Labeling reaction was initiated by adding 1 mM (0.03%) H2O2 to the sample-containing medium and proceeded for 7 min at room temperature. The reaction was immediately quenched by five thorough washes with PBS containing 10 mM sodium ascorbate (Aladdin, #S105024) and 5 mM Trolox (APEXBIO, #C3183). For biochemical characterization or proteomic sample preparation, the quenching solution was drained, and the trachea in minimal residual quenching solution were quickly frozen in liquid nitrogen and stored at 80°C. LC–MS/MS analysis was performed using a Q Exactive HF-X instrument (Thermo Fisher) coupled with Easy-nLC 1200 system. The acquired MS raw data were processed using MaxQuant version 2.0.1.0 (Max Planck Institute of Biochemistry, Germany). Label-free quantification was set with a default parameter and iBAQ was selected.

### Transmission electron microscopy

Fat body of third instar larvae were dissected and fixed in 0.12 M Na-cacodylate buffer (pH 7.4) containing 2.5% glutaraldehyde for 1 hr on ice. Then the samples were rinsed in 0.12 M Na-cacodylate buffer (6 × 5 min, on ice). The dissected fat body were pre-incubated with DAB (10 mg/20 ml) in 0.12 M Na-cacodylate buffer (containing 0.1% saponin) for 30 min with agitation in the dark. Then 30% H2O2 was quickly mixed in DAB solution to a 0.03% vol/vol concentration and reacted for 30 min at RT. The fat body were transferred to 0.12 M Na-cacodylate buffer (6 × 5 min, RT). To increase the electron density of the HRP/DAB product, samples were transferred into 0.01% OsO4 in 0.12 M Na-cacodylate buffer (pH 7.4) for 10 min at RT, then rinsed in 0.12 M Na-cacodylate buffer (3 × 10 min, on ice). 0.1% thiocarbohydrazide in 0.12 M Na-cacodylate buffer (pH 7.4) was used for 10 min at RT, then rinsed in 0.12 M Na-cacodylate buffer (3 × 10 min, on ice). After post-fixation for 1 hr at RT with 1% OsO4 in 0.12 M Na-cacodylate buffer (pH 7.4), the samples were rinsed with MilliQ water (3 × 5 min, RT) and dehydrated in a series of 15 min with 10%, 30%, 50%, 70%, 90%, and 100% (3×) ethanol. Infiltration was conducted at RT with a mixture of acetone and resin 1:1 for 1.5 hr, 1:2 for 3 hr, and 1:3 overnight. The tissues were then dissected from the carcasses and placed in block molds filled with resin for hardening at 60°C during 48 hr. 70 nm ultrathin section from the hardened blocks were cut on a Leica EM UC7 ultramicrotome using an Ultra 45° diamond knife and imaged in a thermos scientific Talos L120C electron microscope.

### Numeration of tracheal progenitors

The pupae at indicated stages were dissected and then fixed with 4% PFA for 25 min. The nuclei were labeled by DAPI. The samples were imaged by an LSM Zeiss 900 inverted confocal laser scanner microscope. The number of progenitor cells was scored from image stacks.

### Optic flow analysis

#### Motion correlation

Time-lapse images of trachea progenitor cells were captured every 5 min over a total duration of 2 hr using an LSM Zeiss 900 microscope. The movies and images were subjected to a three-step motion collection using ImageJ (Schneider et al., 2012) as follows:

#### Optical flow

Optical flow represents the pattern of motion of pixels in a sequence of images. Between two consecutive frames $Ix,y,t$ and $Ix,y,t+Δt$, the optical flow vector $v=v_{x},v_{y}$ represents the motion of pixels during this time. The optical flow constraint equation is shown below:

$$
I_{x}v_{x}+I_{y}v_{y}+I_{t}=0
$$

We adopted the PCA-flow algorithm (Bradski, 2000) in openCV library (cv::optflow::OpticalFlowPCAFlow) in which the sparse optical flow vectors within each small region of the image sequence are calculated before training optical flow fields via principal component analysis (PCA) (Wulff and Black, 2015). The vectors were assembled to generate a smooth vector field of optic flow using the learning linear models of flow. The PCA-flow was validated for the efficiency and robustness.

#### Variance in 1D axis

We developed a robust estimator to evaluate the variance of optic flow projection along the 1D migration axis between samples. The vector length is normalized by a frame-specific normalization factor κ to fit with scale of optic flow computed among different frames.

$$
κ=Q_{0.9}{‖v‖_{2}|v\invectorfield|}
$$

where $Q$ is the quantile function. The variance is computed as $Var({‖v‖_{2}>Q_{0.2}|v\invectorfield})$ and scaled to 0–1 by $Varx/Varx+Vary$.

#### Random variable

The direction of optic flow in each volume was assigned to ‘left’ or ‘right’. Then the distribution of the binarized directions is modeled as a Bernoulli random variable $XBernoulli(p)$ with PMF

$$
P(X=x)={pifx=1,1−pifx=0.
$$

#### Binary entropy

The entropy for Bernoulli random variable $XBernoulli(p)$ is defined as

$$
H_{binary}(X)=−plog(p)−(1−p)log(1−p)
$$

The entropy evaluates the information contained in the random variable (also called uncertainty). In this case, when $p=0.5$, it reaches the maxima 1; if the variable is determinate (i.e. p = 0 or 1), the entropy is zero. More directed cell migration leads to a lower entropy in optic flow since the certainty is high for the migration direction. We estimated $p$ by computing ratio of left and right direction

$$
p=\frac{#left}{#left+#right}
$$

### Image and statistical analysis

Confocal z-stack images were analyzed to extract information of fluorescent intensity of stat92E-GFP and DIPF, and the number of Upd2-mCherry-containing vesicles. z slices of fluorescent intensity for Ds, Ft, and Fj were measured. The number of particles for DIPF and Upd2-mCherry-containing vesicles was analyzed using ImageJ. All statistical analysis was conducted using GraphPad Prism 8.0. Mean and SEM were shown. Unpaired t-tests with Benjamin’s correction were used to evaluate statistical significance between groups.
