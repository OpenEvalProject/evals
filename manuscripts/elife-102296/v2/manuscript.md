# Epithelial cell chirality emerges through the dynamic concentric pattern of actomyosin cytoskeleton

## Authors

- Takaki Yamamoto<sup>1</sup> ([ORCID: 0000-0002-4321-5269](https://orcid.org/0000-0002-4321-5269))
- Tomoki Ishibashi<sup>1</sup> ([ORCID: 0000-0001-6652-9343](https://orcid.org/0000-0001-6652-9343))
- Yuko Mimori-Kiyosue<sup>3</sup>
- Sylvain Hiver<sup>4</sup>
- Naoko Tokushige<sup>1</sup>
- Mitsusuke Tarama<sup>1</sup> ([ORCID: 0000-0002-2708-1774](https://orcid.org/0000-0002-2708-1774))
- Masatoshi Takeichi<sup>4</sup> ([ORCID: 0000-0002-9931-3378](https://orcid.org/0000-0002-9931-3378))
- Tatsuo Shibata<sup>1</sup> ([ORCID: 0000-0002-9294-9998](https://orcid.org/0000-0002-9294-9998)) †

### Affiliations

1. Laboratory for Physical Biology, RIKEN Center for Biosystems Dynamics Research Kobe Japan ([ROR:023rffy11](https://ror.org/023rffy11))
2. Nonequilibrium Physics of Living Matter RIKEN Hakubi Research Team, RIKEN Center for Biosystems Dynamics Research Kobe Japan ([ROR:023rffy11](https://ror.org/023rffy11))
3. Laboratory for Molecular and Cellular Dynamics, RIKEN Center for Biosystems Dynamics Research Kobe Japan ([ROR:023rffy11](https://ror.org/023rffy11))
4. Laboratory for Cell Adhesion and Tissue Patterning, RIKEN Center for Biosystems Dynamics Research Kobe Japan ([ROR:023rffy11](https://ror.org/023rffy11))
5. Department of Physics, Kyushu University Fukuoka Japan ([ROR:00p4k0j84](https://ror.org/00p4k0j84))

† Corresponding author

## Abstract

The chirality of tissues and organs is essential for their proper function and development. Tissue-level chirality derives from the chirality of individual cells that comprise the tissue, and cellular chirality is considered to emerge through the organization of chiral molecules within the cell. However, the principle of how molecular chirality leads to cellular chirality remains unresolved. To address this fundamental question, we experimentally studied the chiral behaviors of isolated epithelial cells derived from a carcinoma line and developed a theoretical understanding of how their behaviors arise from molecular-level chirality. We first found that the nucleus undergoes clockwise rotation, accompanied by robust cytoplasmic circulation in the same direction. During the rotation, actin and Myosin IIA assemble into the stress fibers with a vortex-like chiral orientation at the ventral side of the cell periphery, concurrently forming a concentric pattern at the dorsal side. Further analysis revealed that the intracellular rotation is driven by the concentric actomyosin filaments located dorsally, not by the ventral vortex-like chiral stress fibers. To elucidate how these concentric actomyosin filaments induce chiral rotation, we analyzed a theoretical model developed based on the theory of active chiral fluid. This model demonstrated that the observed cell-scale unidirectional rotation is driven by the molecular-scale chirality of actomyosin filaments even in the absence of cell-scale chiral orientational order. Our study thus provides novel mechanistic insights into how the molecular chirality is organized into the cellular chirality, representing an important step toward understanding left–right symmetry breaking in tissues and organs.

## Introduction

Left–right asymmetry is ubiquitously observed in the bodies and organs of organisms. Despite extensive research, however, we still do not have a complete understanding of how left–right asymmetric structures are formed at an organismal scale. The breaking of left–right symmetry at the body and organ scale has been investigated in embryonic bodies, such as early vertebrate embryo (Hamada and Tam, 2014; Blum and Ott, 2018), nematodes (Naganathan et al., 2014; Pimpale et al., 2020; Sugioka and Bowerman, 2018), and pond snails (Shibazaki et al., 2004; Davison et al., 2016; Abe and Kuroda, 2019); and in organogenesis, such as embryonic hindgut (Hozumi et al., 2006; Taniguchi et al., 2011; Hatori et al., 2014) and male genitalia (Sato et al., 2015a) in Drosophila and heart-looping in the chicken (Ray et al., 2018). Interestingly, in most of these cases, the left–right symmetry breaking at the organ scale is associated with chiral features at the cellular scale, indicating that cell-level chirality induces multicellular chirality (Ishibashi et al., 2019). Chiral dynamics have been observed in isolated single cells, such as nerve cells (Tamada et al., 2010), zebrafish melanophores (Yamanaka and Kondo, 2015), human foreskin fibroblasts (HFF) (Tee et al., 2015; Tee et al., 2023), and Madin–Darby canine kidney (MDCK) cells (Chin et al., 2018). Furthermore, experimental and theoretical studies have revealed that cell-intrinsic chirality drives left–right asymmetric morphogenesis of tissues (Chen et al., 2012; Sato et al., 2015b; Yamamoto et al., 2020) and organs (Ray et al., 2018). Therefore, to elucidate the mechanism of left–right symmetry breaking of organismal structures, it is essential to comprehensively investigate the mechanism underlying chiral dynamics at the single-cell scale.

In cells, there are many chiral components, such as amino acids, proteins, and DNA, and their proper organization can induce chiral properties of cells (Brown and Wolpert, 1990). Particularly, cytoskeletal molecules such as actin and microtubules have been suggested as candidate apparatuses driving chiral dynamics at the single-cell scale. For instance, actin and myosin are responsible for the chiral nuclear rotation of zebrafish melanophore (Yamanaka and Kondo, 2015), and the chiral neurite extension in nerve cells (Tamada et al., 2010). Unconventional Myosin 1D, in particular, plays an important role in the chiral morphogenesis in several species, including Drosophila (Hozumi et al., 2006; Spéder et al., 2006), zebrafish (Juan et al., 2018), and Xenopus (Tingler et al., 2018). Overexpression of this molecule can even induce chiral twisting in otherwise non-chiral organs in Drosophila (Lebreton et al., 2018). Actin cytoskeleton-related protein formins have also been shown to contribute to the chiral patterning of actin cytoskeleton in HFF (Tee et al., 2015; Tee et al., 2023). Formins are implicated in chiral morphogenesis in several organisms, including the snail chiral morphogenesis (Davison et al., 2016; Kuroda et al., 2016; Abe and Kuroda, 2019), Drosophila hindgut and genitalia chirality (Chougule et al., 2020), and chiral cortical flow in C. elegans (Middelkoop et al., 2021). Compared to the well-documented role of actomyosins, the involvement of microtubules in cellular chirality is less frequently reported. Nevertheless, microtubules have been shown to contribute to chirality in cultured human neutrophils (Xu et al., 2007). These studies attribute the chiral cell dynamics to the chiral rotating dynamics of actin and microtubules driven by molecular motors (Nishizaka et al., 1993; Sase et al., 1997). However, a mechanistic understanding of how these molecules generate cell-scale chirality is still not complete. Several attempts to gain mechanistic insights using theoretical models indicate that the chiral symmetry breaking at the cellular level requires spatial coordination of chiral cytoskeletal molecules (Naganathan et al., 2014; Tee et al., 2015). In particular, for the chirality of HFF, it has been proposed that the transverse actin fibers physically interact with radial actin fibers, which are screwed by formin, to drive the nuclear rotation in the counterclockwise direction (Tee et al., 2015; Tee et al., 2023). In the C. elegans embryo, it has been proposed that the actomyosin cortex generates active chiral torque and its spatial gradient induces the chiral symmetry breaking (Naganathan et al., 2014). Therefore, to crack the code of cellular chirality, it is important to elucidate how molecular-scale chiral activity spatially coordinates to trigger cellular-scale chirality.

In the present study, we investigated the behavior of Caco-2 cells, a typical epithelial cell line that was derived from colorectal adenocarcinoma. We found that, when these cells were singly isolated and cultured on substrates, the nucleus rotates along with the circulation of the cytoplasm in a clockwise direction, as viewed from above. We then showed that actin and Myosin II are responsible for this rotation of intracellular components. These cytoskeletal molecules formed concentric actomyosin filaments at the dorsal side of the cells, while they were organized into stress fibers with a vortex-like chiral orientation at the ventral side. Our experiments suggest that the former structure most likely drives the rotating motion, implying that a cell nucleus can rotate without any cell-scale chiral orientational order of the cytoskeleton. To elucidate whether the concentric achiral pattern of the actomyosin filaments can indeed generate rotational flow, we analyzed a hydrodynamic model, based on the active chiral fluid theory, of a three-dimensional (3D) cell, considering the effect of molecular chirality of actin and myosin. We found that the concentric achiral structure of actomyosin can generate chiral cytoplasmic circulation, due to the force which originates from the molecular chirality of individual cytoskeletal components, even without cell-scale chiral structures. On the other hand, we found no evidence that radial actin fibers are involved in the nuclear rotation in Caco-2 cells, suggesting that there might be cell type-specific mechanisms to rotate cytoplasmic components.

## Results

### Nuclei of singly isolated Caco-2 cells rotate in a clockwise direction

To study the rotational dynamics of epithelial cells, we cultured singly isolated Caco-2 cells and imaged them using a differential interference contrast (DIC) microscope (Figure 1A, Video 1). 76% of isolated Caco-2 cells spread circularly on a collagen-coated glass substrate, generating lamellipodia in all directions along the cell periphery with no persistent migration (Ozawa et al., 2020). In the cells spreading circularly, we noticed that the nuclei exhibit rotational motion in a clockwise direction when viewed from the dorsal (apical) side (Figure 1B). There was no cell that exhibited rotational motion in a counterclockwise direction. 24% of the cells exhibited migratory behavior at the start of our live imaging, and it took a while for the cells to spread circularly without persistent migration. The cells exhibiting migratory behavior were excluded from the analysis.

![Figure 1.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig1-v2.jpg)

**Figure 1.:** (A) Rotating nucleus probed by the rotation of nuclear texture. The endpoints of the red line segments are the positions of tracked landmarks of the nucleus. (B) The cumulative angle of nuclear rotation plotted against time and (C) average angular velocity averaged over the first 10 hr ($n=22$). Here, positive angle values indicate clockwise rotation. (D) Chiral cytoskeletal structure of F-actin (phalloidin) and microtubule (immunostaining). Scale bar: 20 µm. (E) Schematic diagram of the orientation of actin stress fibers and microtubule.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Angular velocity of nucleus on the different coating applied to the glass substrate: collagen (n = 19), non-coated (n = 21), fibronectin (n = 22) and poly-l-lysine (n = 22). p values were calculated using Mann–Whitney U test (*p < 0.05, **p < 0.01, ***p < 0.001).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** In the control cell (DMSO), actin bundles (phalloidin, magenta) in the peripheral region of cell, which are tilted to form chiral pattern, appear to be anchored to vinculin (green), a focal adhesion protein, at their both ends. We call them stress fibers. In the cell treated with SMIFH2, one end of each actin bundle was anchored to vinculin, while the other ends were not anchored. Consequently, the actin bundles extend in the radial direction. We call them radial fibers.

![Video 1.](https://cdn.elifesciences.org/articles/102296/elife-102296-video1.mp4.jpg)

**Video 1.:** Scale bar: 20 µm.

The speed of nuclear rotation was about 50 degrees/hr on average (Figure 1C). We measured the rotational speed by tracking unique points of the nuclear texture (Figure 1A). The texture of the cytoplasm around the nucleus also showed a rotating motion, which indicates that the cytoplasm circulates in the same direction (Figure 1A). Furthermore, we found that microbeads attached to the dorsal surface rotate (Video 2), confirming that the dorsal membrane also rotates. The rotating motion of cell nuclei persists for more than 8 hr until cell division occurs. After the cell division, cells form two-cell colonies, and then the nuclear rotation resumes. In this work, we focus on the rotating motion in singly isolated cells.

![Video 2.](https://cdn.elifesciences.org/articles/102296/elife-102296-video2.mp4.jpg)

**Video 2.:** Scale bar: 40 µm.

The rotational speed of the nucleus depended on the type of coating applied to the glass substrate, although the direction of rotation remained unaffected. When cells were cultured on fibronectin-coated glass, they exhibited the same clockwise nuclear rotation as observed on collagen-coated substrates, albeit at a slightly reduced speed (Figure 1—figure supplement 1). On poly-L-lysine-coated or uncoated glass, the rotation speed further decreased, with some cells exhibiting little rotation (Figure 1—figure supplement 1). Notably, while different coatings influenced the speed of nuclear rotation, they did not alter its direction.

### F-actin and microtubules exhibit chiral patterns

We hypothesized that cytoskeletal molecules, such as F-actin and microtubules, are responsible for the circulating flow. To see the structure and dynamics of actin, we imaged live Caco-2 cells expressing Lifeact-RFP (Video 1). In the peripheral region of cells, actin bundles were tilted, forming a dextral chiral pattern (Figure 1D). Since each of these actin bundles appears to associate with vinculin (Figure 1—figure supplement 2), a focal adhesion protein, at their termini, we refer to them as stress fibers (Tojkander et al., 2012). In more interior regions of the cell, actin filaments became thinner, losing their attachment to vinculin, and tended to adopt an orientation parallel to the cell periphery. Next, we observed microtubules by visualizing them with the GFP-tagged microtubule-binding domain of ensconsin (EMTB-3XGFP; Miller and Bement, 2009). Microtubules spread over the entire cytoplasmic region and exhibited a sinistral chiral pattern (Figure 1D, Video 3). A similar sinistral pattern can emerge when filaments extend radially from a center and the central region rotates clockwise, which is consistent with the direction of nuclear rotation. To summarize, actin bundles in the cell peripheral region and microtubules in the cytoplasm showed chiral patterns.

![Video 3.](https://cdn.elifesciences.org/articles/102296/elife-102296-video3.mp4.jpg)

**Video 3.:** Scale bar: 20 µm.

### Chiral rotation requires actomyosin activity, independent of chiral assembly of stress fibers

To investigate whether the cytoskeletons with chiral patterns drive the circulating flow, we performed live imaging of Caco-2 cells expressing Lifeact-RFP with small-molecule inhibitors of cytoskeletal structures. When cells were treated with the actin polymerization inhibitor latrunculin A or F-actin stabilizer jasplakinolide, the shape of the cell periphery became rough and nuclear rotation stopped (Figure 2A, Figure 2—video 1, and Figure 2—video 2, respectively), indicating that F-actin is necessary for the nuclear and cytoplasmic rotation. In contrast, disruption of microtubules by nocodazole did not affect the nuclear rotation (Figure 2B, C, Figure 2—figure supplement 1, and Figure 2—video 3), which indicates that microtubules are not involved in the rotating motion.

![Figure 2.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig2-v2.jpg)

**Figure 2.:** Roles of F-actin, microtubule, Arp2/3, formin-mediated actin polymerization, and Myosin II activity were investigated. Cells were treated with DMSO (0.2%, control), actin polymerization inhibitor latrunculin A (2 µM), actin depolymerization inhibitor Jasplakinolide (10 nM), microtubule inhibitor nocodazole (50 µM), Arp2/3 inhibitor CK666 (200 µM), formin inhibitor SMIFH2 (40 µM), or Myosin II inhibitor blebbistatin (1 µM). (A) Snapshot images from the live image of actin dynamics in cells expressing Lifeact-RFP. Scale bar: 20 µm. (B) The cumulative angle of nuclear rotation averaged over different cells plotted against time for different conditions: DMSO ($n=19$), nocodazole ($n=11$), blebbistatin ($n=10$), CK666 ($n=13$), and SMIFH2 ($n=10$). The standard deviation is represented by shaded regions. (C) Angular velocity of cells under different conditions averaged over the first 5 hr of the time-evolution plot in (B). (D) Angular velocity of control and SMIFH2-treated cells averaged over the last 5 hr of the time-evolution plot in (B): DMSO ($n=13$) and SMIFH2 ($n=10$). p values were calculated using the Mann–Whitney U test ($∗p<0.05,∗∗p<0.01,∗∗∗p<0.001$). Here, positive angle values indicate clockwise rotation.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Typical snapshots of microtubule of a cell 0.5 and 3.5 hr after the addition of nocodazole (50 µM).The scale bar is 20 µm.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) RNA-sequencing (RNA-seq) analysis showing gene expression levels (transcripts per million; TPM) of major mammalian formin family members (DIAPHs and DAAMs) in Caco-2 cells. Circles represent individual samples (circles of the same color indicate replicates), and bars indicate mean values (n = 3). Western blot showing protein levels of DIAPH2 (B) and DAAM1 (C) in Caco-2 cell treated with siRNAs.GAPDH (bottom row) was used as an internal control. (D) Angular velocity of nucleus of Caco-2 cells that were treated with siRNA for DIAPH2 or DAAM1. The rotation of the nucleus was tracked for 5 hr following the start of the live imaging. Negative control (N.C.) (n = 10), DIAPH2 (n = 18), and DAAM1 (n = 17). p values were calculated using Mann–Whitney U test (*p < 0.05, **p < 0.01, ***p < 0.001). Snapshot images from the live image of actin dynamics in cells expressing Lifeact-RFP in DIAPH2 (E, E’) and DAAM1 (F, F’) depleted cells. Scale bar: 20 µm.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Angular velocity of nucleus of Caco-2 cells that were treated with siRNA for Myosin II A and/or B heavy chains. The rotation of the nucleus was tracked for 5 hr following the start of the live imaging. Negative control (N.C.) (n = 10), Myosin II A (n = 19), Myosin II B (n = 15), and Myosin IIA and B (n = 20). p values were calculated using Mann–Whitney U test (*p < 0.05, **p < 0.01, ***p < 0.001). (B) Western blot showing protein levels of Myosin IIA (top row) and IIB (middle row) heavy chains in Caco-2 cells treated with siRNAs. GAPDH (bottom row) was used as an internal control. Quantification of fold change relative to the negative control (N.C.), normalized to GAPDH protein level, is shown in bar graphs (bottom panel). Images of Myosin IIA (C) or Myosin IIB (D) (immunostaining, green) and actin filaments (phalloidin, magenta) in cells treated with siRNAs.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) Angular velocity of nucleus of Caco-2 cells that were treated with siRNA for vinculin. The rotation of the nucleus was tracked for 5 hr following the start of the live imaging. Negative control (N.C.) (n = 10) and vinculin (n = 17). p values were calculated using Mann–Whitney U test (*p < 0.05, **p < 0.01, ***p < 0.001). (B) Western blot showing protein levels of vinculin in Caco-2 cell treated with siRNAs. GAPDH (bottom row) was used as an internal control. Quantification of fold change relative to the negative control (N.C.), normalized to GAPDH protein level, is shown in bar graphs (bottom panel). (C) Images of actin filaments (phalloidin, magenta) and vinculin (immunostaining, green) in cells treated with siRNAs. Scale bar: 20 µm.

To reveal which activities of actin are involved in the chiral rotating motion, we first investigated the role of Arp2/3-driven actin polymerization on the rotating motion, since a previous report has shown that it is involved in the chiral behavior of HFF (Tee et al., 2015). When Caco-2 cells were treated with the Arp2/3 complex inhibitor CK666 (Nolen et al., 2009), lamellipodia at the cell periphery tended to shrink (Figure 2A, Figure 2—video 4), but the nuclear rotation was maintained (Figure 2B, C), indicating that the Arp2/3 complex was dispensable for the rotating motion, in contrast to HFF where the Arp2/3 complex plays a role in cell chirality formation (Tee et al., 2015).

Next, we focused on the potential role of formin, a regulator of actin polymerization, as previous studies showed that this protein is involved in inducing the chirality of some cell types (Tee et al., 2015; Davison et al., 2016; Kuroda et al., 2016; Abe and Kuroda, 2019; Middelkoop et al., 2021; Tee et al., 2023). To this end, we tested the effect of SMIFH2, a formin inhibitor (Rizvi et al., 2009), on the chiral pattern of Caco-2 cells. When cells were treated with this inhibitor, chiral stress fibers mostly disappeared in their peripheral regions, but instead, another pattern of F-actin appeared (Figure 2A and Figure 2—video 5). To investigate the distribution of F-actin more closely, we performed phalloidin staining and imaged cells in 3D (Figure 3). Figure 3B shows that a subset of actin bundles became oriented in a radial direction, unlike the chiral pattern of stress fibers originally observed in the control cells (Figure 3A). Furthermore, another population of F-actin was organized into a dense network or cluster with a concentric pattern (Figure 3B). Intriguingly, in spite of these drastic changes in the spatial organization of F-actin, and the disappearance of the peripheral chiral stress fibers, the rotating motion was maintained (Figure 2B, C). Furthermore, as shown in Figure 2D, we noticed that, while the nuclear rotation speeds of control and SMIFH2-treated cells were comparable in the first 5 hr of the observation window, the nucleus of the SMIFH2-treated cells rotated significantly faster than control cells, on average, in the second 5 hr: the rotating speed of control cells slightly decreased over time, while SMIFH2-treated cells maintained or even slightly accelerated the rotating speed (Figure 2C, D).

![Figure 3.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig3-v2.jpg)

**Figure 3.:** (A) Control cells treated with DMSO show a chiral tilted pattern of F-actin and Myosin II visualized by phalloidin and immunofluorescence with an antibody against Myosin IIA, respectively. (B) SMIFH2 (40 μM) treated cells show a concentric pattern of F-actin and Myosin II. (C) The chiral tilted pattern of F-actin and Myosin II is suppressed in cells treated with blebbistatin (1 μM). The bottom panel shows vertical cross-sections. Scale bars: 20 μm (horizontal) and 5 μm (vertical).

These observations with the formin inhibitor suggested that formins might not be essential for nuclear rotation. To further evaluate this idea, we knocked down formin expression using siRNA. Among the major mammalian formin family members (DIAPHs and DAAMs), DIAPH2 and DAAM1 were identified as being highly expressed in Caco-2 cells by RNA-sequencing (RNA-seq) analysis (Figure 2—figure supplement 2A). However, knockdown of either DIAPH2 or DAAM1 did not disrupt nuclear rotation (Figure 2—figure supplement 2A–D, Figure 2—videos 6 and 7). These findings suggest that formins are not essential for the chiral nuclear rotation in Caco-2 cells, in contrast to previous reports (Tee et al., 2015; Davison et al., 2016; Kuroda et al., 2016; Abe and Kuroda, 2019; Middelkoop et al., 2021; Tee et al., 2023).

In DIAPH2 knockdown cells, the distribution of actin fibers was similar to that in control cells (Figure 2—figure supplement 2E, E’ and Figure 2—video 6). By contrast, a subset of DAAM1-knockdown cells displayed a detached end of the actin bundle, resembling the phenotype observed in SMIFH2-treated cells (Figure 2—figure supplement 2F, F’ and Figure 2—video 7). Although the precise mechanism by which SMIFH2 induces F-actin reorganization while promoting nuclear rotation remains unclear, particularly given its lack of strict specificity for formins (Nishimura et al., 2021b), we employed this inhibitor as a tool to further investigate the mechanism underlying chiral rotational motion.

Previous studies have shown that the chirality in various cell types depends on the activity of Myosin II, proposing that Myosin II with F-actin generates chiral torque on a molecular scale (Naganathan et al., 2014; Fürthauer et al., 2012; Fürthauer et al., 2013; Tjhung et al., 2017). Therefore, we next investigated the role of Myosin II in the chiral rotation by treating Caco-2 cells with a Myosin II inhibitor, blebbistatin. Under this condition, the chiral pattern of peripheral F-actin became less prominent (Figures 2A and 3C and Figure 2—video 8), while the nuclear rotation was mostly suppressed (Figure 2B, C). To confirm the role of Myosin II, we depleted Myosin IIA and/or Myosin IIB heavy chains in Caco-2 cells using siRNAs (Figure 2—figure supplement 3B–D). Their depletion resulted in a significant reduction in the nuclear rotation (Figure 2—figure supplement 3A, Figure 2—video 9). These results suggest that the activity of Myosin II is required for the chiral rotational motion and also for the formation of a chiral pattern of stress fibers. In summary, both the activities of F-actin and Myosin II are important for nuclear and cytoplasmic rotation.

Our results using SMIFH2 showed that nuclear rotation persists even when the chiral stress fibers are lost, which suggests that these structures are not essential for driving rotational motion. To further test this possibility, we disrupted stress fibers by knocking down vinculin using siRNA. Upon vinculin depletion, the chiral arrangement of peripheral actin bundles was lost. Nevertheless, the nucleus continued to rotate clockwise comparable to that observed in control cells (Figure 2—figure supplement 4 and Figure 2—video 10). These results indicate that Myosin II mediates chiral nuclear rotation through subcellular structures other than stress fibers.

### Super-resolution 3D imaging of actin and Myosin II

To further investigate the roles of F-actin and Myosin II in the chiral rotation, we analyzed their distribution and dynamics in more detail, using both control and SMIFH2-treated cells. For this purpose, we employed a 3D super-resolution imaging technique known as expansion microscopy (ExM).

We first examined the distribution of F-actin stained with phalloidin under control conditions (Figure 4A, A’). In the peripheral region of the cell, stress fibers localized on the ventral side exhibited a dextral swirling pattern (yellow in the left panel and bold lines in the right panel of Figure 4A; red in Figure 4A’; dark red lines in Figure 5K, top). These peripheral stress fibers (red in Figure 4A’) likely correspond to the actin bundles associated with focal adhesions, which were shown in Figure 1—figure supplement 2. Adjacent to the inner edge of the peripheral cytoplasmic zone having stress fiber bundles, we detected another population of actin filaments. These filaments, which looked thinner than stress fibers, were oriented parallel to the cell periphery and lacked obvious chirality, seemingly associated with the dorsal cell membranes (green in the left panel and dotted lines in the right panel of Figure 4A; light blue line in Figure 5K, top; green in Figure 4A’). These dorsal actin filaments (green in Figure 4A’) likely correspond to those not anchored to the focal adhesions, which were detectable in the image of Figure 1—figure supplement 2. They also appeared not to associate with any other F-actin populations. Next, we examined the distribution of Myosin IIA using antibodies (Figure 4B). The distribution of Myosin IIA is similar to that of F-actin, except for its striped pattern. Since we could not assess the colocalization of F-actin and Myosin IIA filaments in the same cells in ExM for technical reasons, we investigated their localization using conventional confocal microscopy (Figure 3A and Video 4). The confocal microscopy images indicate that F-actin and Myosin IIA generally colocalize with one another in these specimens.

![Figure 4.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig4-v2.jpg)

**Figure 4.:** Maximum intensity projection (MIP) images of F-actin (A, C) and Myosin IIA (B, D) in DMSO (A, B) and SMIFH2 (C, D) treated cells. The color indicates the height along the $z$-axis, where the height was measured after the samples were swollen (color bar, right). Magnified views of the white boxes are shown in the right top panels, and corresponding outlines of F-actin are shown in the right bottom panels, where the bold and dotted lines indicate stress fibers and dorsal actomyosin fibers, respectively. The vertical cross-sections ($xz$) are shown in the bottom panels, where the bold and dotted lines indicate the peripheral and dorsal inner regions, respectively. Scale bars: 20 µm (horizontal) and 10 µm (vertical). (A’, C’) Composite F-actin images of the ventral (red) and dorsal (green) sides. (A’) In the DMSO-treated cell, the thickness of the ventral and dorsal sides is 2.7 and 6.5 µm, respectively. (C’) In the SMIFH2-treated cells, the thickness of the ventral and dorsal sides is 4.2 and 5.7 µm, respectively.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Maximum intensity projection (MIP) images of F-actin (A) and Myosin IIA (B) in blebbistatin-treated cells. The color indicates the height along the z-axis, where the height was measured after the sample was swollen (colorbar, the most right). Magnified views of the white boxes are shown in the right top panels, and corresponding outlines of F-actin are shown in the right bottom panels, where the bold and dotted lines indicate thick and thin fibers, respectively. The vertical section (xz) images are shown in the bottom panels, where the bold and dotted lines indicate peripheral and dorsal inner region, respectively. Scale bars: 20 µm (horizontal), 10 µm (vertical).

![Figure 5.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig5-v2.jpg)

**Figure 5.:** (A) Maximum intensity projection (MIP) image of Caco-2 treated with DMSO. (B) Snapshot images in the green rectangle in (A), obtained from the $z$-slice at $z=0$ is defined as the plane closest to the substrate. The green line is the same as the green circle in (A). Arrowheads indicate the position of filaments. (C) Snapshot images in the red rectangle in (A) obtained from the $z$-slice at $z=0.5\mum$. The red line is the same as the red circle in (A). Arrowheads indicate the position of filaments. (D) Kymograph along the green circle in (A), obtained from a slice at $z=0$. (E) Kymograph along the yellow line in (A), obtained from the $z$-slice at $z=0$. (F) Kymograph along the red circle in (A), obtained from the $z$-slice at $z=0.5\mum$. inset: schematic diagram of F-actin (black lines) passing through the circle. (G) Kymograph along the yellow line in (A), obtained from the $z$-slice $z=0.5\mum$. (H) MIP image of Caco-2 treated with SMIFH2 ($40\mum$). (I) Kymograph along the red circle in (H), obtained from the MIP image. (J) Kymograph along the yellow line in (H), obtained from the MIP image. (K) Schematic diagram of F-actin structure in control and SMIFH2 treated cells. Stress fibers (dark red) were immobile, while the dorsal actin fibers formed an ‘actomyosin ring’ (light blue), moved in centripetal and clockwise directions. Scale bar: 10 µm.

![Video 4.](https://cdn.elifesciences.org/articles/102296/elife-102296-video4.mp4.jpg)

**Video 4.:** Scale bar: 20 µm.

We next examined the distribution of F-actin and Myosin II in the cells treated with SMIFH2 (Figure 4C, C’, D). As observed by conventional confocal microscopy, the chirally tilted actin stress fibers disappeared at the peripheral region, and instead, F-actin bundles extended radially from the cell edge toward its center (bold line in Figure 4C, right; dark red lines in Figure 5K, bottom). In the interior region, actin filaments were organized into a dense network with a concentric pattern, which was distributed at the dorsal side of cells (green in the left and dotted lines in the right panels of Figure 4C; light blue line in Figure 5K, bottom; green in Figure 4C’). Myosin IIA exhibited a similar reorganization as seen in F-actin (Figure 4D). As observed in control cells, confocal microscopy showed that F-actin and Myosin IIA also colocalize in the SMIFH2-treated cells, particularly in the concentric actin clusters (Figure 3B). Thus, ExM analysis revealed more detailed features of actomyosin distribution, particularly detecting its concentric orientation, located more inside the cell than the peripheral stress fibers.

Additionally, we examined cells treated with blebbistatin by ExM, confirming the results obtained by live imaging and conventional immunostaining (Figures 2A and 3C). The chiral orientation of stress fibers was greatly reduced in the peripheral region after this treatment (Figure 4—figure supplement 1). Furthermore, the dorsally located concentric actin filaments became undetectable in these specimens. These results are consistent with the idea that Myosin II plays a complex role, including in the organization of dorsal actin filaments.

### F-actin ring circulates along the dorsal membrane

To gain further insights into the role of the actomyosin system in the mechanism of intracellular rotation, we examined how F-actin behaves during the rotational process. To this end, we performed live imaging of Caco-2 cells expressing Lifeact-mEmerald, using lattice light-sheet microscopy (LLSM). Since LLSM has a higher spatial resolution, particularly in the z-direction, compared to conventional confocal microscopy, we could identify the dynamics of F-actin in 3D more precisely. We found that stress fibers at the ventral side were almost immobile (Figure 5B), while the actin fibers at the dorsal side moved clockwise as indicated in snapshot images (Figure 5C). Such spatiotemporal dynamics can be systematically seen in the kymographs along different lines, drawn in Figure 5A, at different heights $z$ in control cells. In Figure 5D, E, the kymographs along the green circle and the yellow line, which were analyzed at the ventral side, indicate that F-actin bundles in the peripheral region with the chiral tilted pattern are almost immobile (arrow in Figure 5D, Video 5). Figure 5F, G shows the kymographs along the red circle and the yellow line (drawn in Figure 5A), respectively, at the height where the dorsal cell membrane exists. Rightward descending lines in the kymograph along the red circle indicate that the filaments move in a clockwise direction (Figure 5F, arrow 1). There are also leftward descending lines that appear at the same time as the rightward descending lines appear but with different steepness (Figure 5F, arrow 2). These pairs of lines indicate that the filaments are moving clockwise as well as centripetally (Figure 5F, inset). Furthermore, the kymograph along the yellow line (Figure 5A) also confirms that the filaments are moving centripetally (arrow in Figure 5G). To summarize, along the dorsal cell membrane, the concentric actin filaments move clockwise while also moving in centripetally (see also Video F-actin ring circulates along the dorsal membrane): we hereafter call this concentric structure ‘the actomyosin ring’ (Figure 5K).

![Video 5.](https://cdn.elifesciences.org/articles/102296/elife-102296-video5.mp4.jpg)

We also examined the dynamics of actin fibers in cells treated with SMIFH2, using live image data obtained by LLSM (Figure 5H–J). In Figure 5I, J, the kymographs along the red circle and yellow line (drawn in Figure 5H), respectively, indicate that the actomyosin filaments organizing the ring move clockwise (Figure 5I), and simultaneously flow centripetally (arrow 1 in Figure 5J), similar to the control condition. Additionally, we found that in contrast to the immobile stress fibers with a chiral pattern in control cells (dark red lines in Figure 5K, top), F-actin bundles radially extending from the cell periphery in SMIFH2-treated cells appeared to move passively in a clockwise direction at their proximal ends, although they seem to keep the anchorage of the distal ends to the cell edge (arrow 2 in Figure 5J; Video 6 and dark red lines in Figure 5K, bottom), implying that these radial F-actin bundles do not play active roles in the chiral motion of the actin ring. Thus, the concentric ring of flowing actomyosin filaments was detected also in the SMIFH2-treated cells but showing modified features (Figure 5K). Importantly, the ring developed more extensively after SMIFH2 treatment.

![Video 6.](https://cdn.elifesciences.org/articles/102296/elife-102296-video6.mp4.jpg)

**Video 6.:** Scale bar: 10 µm.

To see if the actomyosin ring is involved in driving the rotating flow, we estimated the spatial distribution of flow speed and orientation (velocity field) from the F-actin time-lapse images using particle image velocimetry (PIV) for both control and SMIFH2-treated cells (Figure 6, Figure 6—figure supplement 1, and Figure 6—video 1). In the cytoplasmic region between the actomyosin ring and the nucleus, we did not detect clear actin filaments, but only found blobs of actin (Figure 5A, H, and green dots in Figure 5K). These blobs also circulated clockwise. From the velocity field inside the cells inferred by PIV, we calculated the angular component of the velocity with respect to the cell center and then converted it into the angular velocity, that is change in the angle per unit time. The spatial profile of the angular velocity (Figure 6A, Figure 6—figure supplement 1A–H) indicates that it is higher in the region where concentric actin filaments are present, rather than the region where the actin blobs are present, indicating that the driving force could be present in the region of the actomyosin ring. The angular velocity averaged over the angular direction shows the peaks in the range from 10 to 20 µm (Figure 6C). Since the size of the actomyosin ring varies from cell to cell, we manually determined the region of the actomyosin ring, and then replotted the angular velocity against the distance scaled by the inner radius of the actomyosin ring (Figure 6D). We found that the peak positions of individual angular velocity profiles, as well as the peak positions of the angular velocity profiles averaged over samples, are located around the scaled distance of one, which suggests that the driving force is present in the region around the actomyosin ring.

![Figure 6.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig6-v2.jpg)

**Figure 6.:** Spatial profile of angular velocity (color code) obtained from the time average of the PIV vector field in a control cell (A: DMSO) or in a cell treated with SMIFH2 (B) superimposed on a snapshot F-actin image. Scale bar: 20 µm. (C) Average angular velocity as a function of the distance from the center. (D) Average angular velocity as a function of a distance scaled by the inner radius of the actomyosin ring of individual cells. Here, positive angular velocity indicates clockwise rotation. Sample averages for two conditions are indicated by the solid lines. Error bars and shaded areas represent standard errors of the means (SEM).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** PIV analysis of cell treated with DMSO and SMIFH2. Spatial distribution of azimuthal velocity (top), radial velocity (middle), and angular velocity (bottom) for cell treated with DMSO (control) (A–D) and with SMIFH2 (E–H). (I) Angular averaged azimuthal velocity plotted against the distance from the cell center. (J) Angular averaged radial velocity plotted against the distance from the cell center. Scale bar: 20 µm. Positive azimuthal and angular velocities indicate clockwise rotation.

We additionally observed another interesting phenomenon to support our idea. In an SMIFH2-treated cell that was imaged by a conventional fluorescence confocal microscope (LSM880, Zeiss), we, by chance, observed that fluorescent debris that seemed to attach to the actomyosin ring persistently circulated approximately three times as fast as the rotating speed of the nucleus: ∼400 and ∼140 degrees/hr for the debris and nucleus, respectively. (Figure 6—video 2, yellow and white lines, respectively). In the other cell observed by LLSM, we observed two fluorescent debris circulating in the area of the actomyosin ring, and in the cytoplasmic region between the actomyosin ring and the nucleus (Figure 6—video 3, yellow and red circles): the angular velocities of the circulating debris were ∼250 and ∼190 degrees/hr, respectively. Although we could not measure the rotating speed of the nucleus in the second cell because the nucleus was barely visible in the LLSM live image, the circulating speeds of the debris are more than two times faster than the typical nuclear angular velocity of SMIFH2-treated cells (Figure 2B–D). These observations support the notion that the actomyosin ring generates a driving force for rotating the nucleus and cytoplasm. Note that, since the angular velocity estimated from the motion of debris was faster than that obtained from the PIV analysis, our PIV analysis for F-actin dynamics may underestimate the flow velocity.

### A theoretical model of chiral cytoplasmic flow induced by the actomyosin ring

Our observations indicate the possibility that the actomyosin ring is a cell-scale structure that drives the chiral cytoplasmic flow. Since the actin filaments of the ring seemed not to have contact with the peripheral stress fibers in control cells, their rotational motion should be driven solely through its own mechanism, without relying on other structures, contrasted with the previous model that the contact between transverse fibers and radial fibers plays a role in establishing the cell chirality in HFF (Tee et al., 2015). Then, how can a concentric pattern without an obvious cell-scale chiral structure generate chiral circulating flow? We here theoretically address this question.

We employ a theoretical framework of active chiral fluid (Fürthauer et al., 2012; Fürthauer et al., 2013; Naganathan et al., 2014), which has been proposed to describe the fluid dynamics driven by active chiral components. We model the actomyosin ring as an active chiral fluid driven by two active elements: (1) a force dipole originating from the contraction force of actomyosin and (2) a torque dipole generated when a bipolar Myosin II filament rotates two antiparallel actin filaments to create a pair of counter-rotating vortex flows (Figure 7A). By representing the orientation of actomyosin fibers as orientational field $p$ and the fluid velocity as $v$, the hydrodynamic equation is described by the Stokes equation with the active contributions:

$$
0=−∇P+η∇^{2}v+ζ^{a}∇⋅pp+\frac{1}{2}ζ^{c}∇\times(∇⋅pp),
$$

where $P$ is the pressure satisfying the incompressibility condition $∇⋅v=0$ and $η$ is the fluid viscosity. Here, the terms with $ζ^{a}$ and $ζ^{c}$ are forces generated by the force dipoles (achiral) and torque dipoles (chiral), respectively. $ζ^{a}$ and $ζ^{c}$ represent the strength of the forces. The signs of $ζ^{a}$ and $ζ^{c}$ would be determined by the nature of force and torque generation at the molecular scale, independently of the cell-scale orientation of actomyosin. Considering that the actomyosin generates contractile force and right-handed torque as shown in Figure 7A; Nishizaka et al., 1993, the signs of the coefficients are $ζ^{a}>0$ and $ζ^{c}>0$. We hereafter assume $ζ^{a}>0$ and $ζ^{c}>0$ constant in space. We also assume the actomyosin filaments have a bipolar structure (Figure 7A) so that Equation 1 is invariant under $p→−p$. We, for convenience, represent the spatial variation of the density and order of the actomyosin by introducing an effective order parameter $S$ as $p=Sn$ (see Equation 11), where $n$ is a unit vector.

![Figure 7.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig7-v2.jpg)

**Figure 7.:** (A) Actomyosin generates a force dipole and a torque dipole. (B–D) Numerical simulation of Equation 1 assuming that the cell shape is axisymmetric around the cell center. (B) Actomyosin is distributed along the dorsal membrane with a concentric orientation. (C) Azimuthal velocity $v_{\phi}$ showing negative values indicating that the flow is generated in a clockwise direction. (D) Velocity in the radial $ρ$- and $z$- directions, ($v_{ρ}$, $v_{z}$), indicated by vectors. Circulating flow is generated in the $ρ$-$z$ plane. (E) Top: A concentric orientational field on a ring generates active torque in the center direction (magenta arrow). Middle: Active torque (magenta clockwise arrow) generated by a concentric orientational field on a ring. Bottom: A side view of a cell from the outside toward the cell center. The concentration of actomyosin increases in $z$ (gray color), leading to a gradient of active torque (magenta clockwise arrow) in the $z$ direction, resulting in a rotational flow clockwise (black arrows). (F) Flow profile along the dorsal side showing an inward sinistral swirling pattern. (G) Flow profile at the ventral side showing an outward dextral swirling pattern. (H) Angular velocity averaged in the $z$ direction plotted along the radial direction, showing a peak at around $ρ/ρ_{a}=1$. Here, $ρ_{a}$ is the leftmost position where $S\geq0.8$.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Cell shape used in the numerical simulation. Here, cell shape is assumed to be axisymmetric with respect to the cell center. $Z_{0}$ is the cell height, $R_{0}$ is the cell radius, and $r_{1}$, $ρ_{2}$ and α are the parameters that determine the cell shape.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** (A–H) Radial and azimuthal velocities shown in Figure 6—figure supplement 1. (I) Radial and azimuthal velocities in the numerical simulation. In the seplots, the radial velocity is positive in the centripetal direction.

We first numerically solved Equation 1, assuming a cell with an axisymmetric geometry shown in Figure 7—figure supplement 1. Based on the experimental observation, we also assumed that actomyosin is distributed on the dorsal side, where the effective order parameter $S$ is set to be positive reflecting the density distribution of actomyosin (Figure 7B). Figure 7C shows the spatial profile of the azimuthal velocity $v_{\phi}$ in the vertical section of the cell. In the entire region, $v_{\phi}$ is negative, indicating that the flow is generated in a clockwise direction viewed from above. Thus, the numerical result shows that the concentric pattern of actomyosin can generate chiral cytoplasmic flow, and the direction is clockwise, consistent with our experimental observation.

How can we understand the underlying mechanism behind the chiral cytoplasmic flow resulting from the concentric pattern of actomyosin? The active chiral term $ζ^{c}∇\times∇⋅pp$ in Equation 1 can be interpreted as follows: the rotation of the axial vector field $ζ^{c}∇⋅pp$, which is an active torque induced by chiral torque dipole, generates a force to induce a flow. For a concentric orientational field on a ring domain, the active torque $ζ^{c}∇⋅pp$ is generated, which is the clockwise direction when viewed from the outside toward the center of the ring, as shown in Figure 7E middle (magenta arrow). The actomyosin ring formed along the dorsal side in Caco-2 cells is regarded as a stack of concentric orientational fields on a ring. In the region where actomyosin is present ($S>0$), the concentration of actomyosin naturally increases with $z$ which leads to an increase of the effective order parameter $S$ with respect to $z$ as indicated in Figure 7B (the gradient of red color in Figure 7E, bottom). For such an orientational field, the strength of the active torque increases as the height $z$ increases (magenta clockwise arrow in Figure 7E, bottom), forming a gradient of the active torque strength in the $z$ direction. Consequently, the gradient generates a force in a clockwise direction as viewed from above (black arrows in Figure 7E bottom, see also the right-hand side of Equation 12).

In the numerical simulation, we also investigated the spatial profile of $ρ$ and $z$ components $(v_{ρ},v_{z})$ of the velocity field. Figure 7D shows that inward flow to the cell center occurs on the dorsal side, while the flow in the opposite direction occurs on the ventral side, resulting in the circulating flow in the $ρ$ and $z$ plane (Figure 7D). This circulating flow is driven by the contractile force of actomyosin on the dorsal side. Due to the circulating flow in the $ρ$-$z$ plane and the azimuthal flow, swirling flows appear on both dorsal and ventral sides (Figure 7F, G, respectively). The sinistral swirling pattern at the dorsal side shown in Figure 7F is driven by both centripetal and clockwise flows, which were indeed observed by LLSM shown in Figure 5. Interestingly, the dextral swirling pattern of the flow on the ventral side is consistent with the chiral pattern of the stress fibers on the ventral side (Figure 1D). When the chiral flow was inhibited with blebbistatin, such a chiral pattern at the ventral side disappeared (Figures 2A and 3C and Figure 4—figure supplement 1), suggesting that the ventral chiral tilted patterns are indeed formed in a flow-dependent manner. This implies that the dextral chiral pattern of the stress fibers is self-organized through alignment with the fluid flow on the ventral side.

Furthermore, we analyzed the radial distribution of the angular velocity and found that it exhibits a peak around the inner edge of the actomyosin ring $ρ∼ρ_{a}$ (Figure 7H) with the peak value of around 80 degree/h, consistent with the PIV analysis of the experimental data (Figure 6C, D). $ρ_{a}$ is the inner radius of the actomyosin ring. This result further supports the idea that the actomyosin ring drives the rotation of the nucleus.

### Depletion of dorsal actin and myosin coincides with the cessation of nuclear rotation

Our experimental observations and theoretical results suggest that the actomyosin ring located at the dorsal side of Caco-2 cells plays a key role in the rotating motion. To further investigate this, we tested whether depletion of actomyosin at the dorsal side affected rotational motion. A previous study showed that the activation of RhoA by Rho Activator II (CN03), a specific RhoA activator, resulted in a decrease in apical stress fibers and an increase in basal stress fibers in vascular smooth muscle cells (Bade et al., 2017). Based on this information, we aimed to decrease the ratio of the actomyosin at the dorsal to ventral sides in Caco-2 cells using Rho Activator II. Remarkably, we observed a substantial increase in the thickness and number of actomyosin bundles at the ventral side, particularly beneath the nucleus, in Caco-2 cells treated with Rho Activator II, while the dorsal actomyosin appeared to decrease significantly (Figure 8A, C). The ratio of dorsal to ventral actomyosin was reduced significantly in the cell treated with Rho Activator II compared with control cells (Figure 8D, E). We then performed live imaging of Caco-2 cells treated with Rho Activator II and found that the rotational motion of the nucleus ceased (Figure 8—video 1), supporting the idea that the dorsal actomyosin is crucial for driving the rotation. We also noticed that in cells treated with Rho Activator II, the bundle of stress fibers was rearranged into a chordal pattern (Figure 8C) and exhibited chiral motion (Figure 8—video 1), the mechanism of which remains to be understood. On the other hand, in cells treated with SMIFH2, the dorsal actomyosin appeared to increase, while the ventral actomyosin decreased (Figure 8A, B). The ratio of dorsal to ventral actomyosin in cells treated with SMIFH2 tended to increase, although the difference was not statistically significant (Figure 8D, E). Taken together, our findings further support the idea that actomyosin at the dorsal side is crucial for driving rotation in Caco-2 cells.

![Figure 8.](https://cdn.elifesciences.org/articles/102296/elife-102296-fig8-v2.jpg)

**Figure 8.:** (A) Actin (magenta) and Myosin II (yellow) showing localization with the dorsal marker Ezrin (cyan) in the DMSO-treated cell. (B) SMIFH2-treated cell showing an increase in dorsal actomyosin and a decrease in ventral actomyosin. (C) Rho Activator II (CN03) treated cell showing a decrease in dorsal actomyosin and an increase in ventral actomyosin. Control (DMSO) and SMIFH2-treated cells showed clockwise (CW) rotation, while CN03-treated cells did show rotation. Scale bars: 20 µm (horizontal) and 5 µm (vertical). Ratio of dorsal F-actin (D) and MyoII (E) to the ventral ones. p values were calculated using the Mann–Whitney U test. $∗p<0.05$, n.s.: $p≧0.05$.

## Discussion

In this study, we investigated the mechanism underlying cell-scale chiral dynamics, which is observed in Caco-2 epithelial cells when cultured as a single cell. We found that Caco-2 cells exhibited nuclear rotation and cytoplasmic circulation clockwise, and these movements require actin and Myosin II activities. High-resolution microscopy has revealed that the concentric actomyosin ring located on the dorsal side of the cells moves in a clockwise direction, leading us to hypothesize that this process may play a critical role in driving cytoplasmic flow. Previous studies using HFF proposed that radial actin fibers produce a force to drive the movement of the concentric actomyosin filaments (transverse fibers) through their connections (Tee et al., 2015). In the case of Caco-2 cells, however, we did not detect such radial fibers crossing the concentric actomyosin ring, and our observations suggested that the actomyosin ring by itself was moving in a clockwise direction through its own mechanism. To test this idea, we employed active chiral fluid theory (Fürthauer et al., 2012; Fürthauer et al., 2013; Naganathan et al., 2014), showing that the actomyosin localized under the dorsal membrane induces an active unidirectional fluid flow of the viscous cytoplasm and in turn nuclear rotation. Since the concentric pattern of actomyosin has no chirality at the cellular scale, our theory indicates that the nuclear rotation and cytoplasmic flow in Caco-2 cells is driven by the molecular-scale chiral mechanics of actomyosin rather than the cell-scale chiral orientation of actomyosin. It is also of note that we did not detect any visible cytoskeletal linkage between the nucleus and other cellular structures, another potential machinery for driving nuclear rotation. The nuclear rotation may be induced directly by the cytoplasmic circulating flow mediated by the friction between the nuclear surface and the cytoplasm. Microtubules and the peripheral stress fibers also exhibited chiral distribution patterns, but we obtained no evidence that they are involved in the chiral motion of the nucleus and cytoplasm. It is, therefore, possible that their chiral distribution was generated as a result of the above-mentioned mechanism.

Our experiments using an inhibitor and RNAi-mediated depletion have revealed that Myosin II is involved in the chirality of Caco-2 cells, which is consistent with previous studies showing the involvement of Myosin II in the chiral behaviors of several types of cells (Kumar et al., 2014). Interestingly, while some of these studies concluded that formins are essential for breaking the chiral symmetry (Tee et al., 2015; Davison et al., 2016; Kuroda et al., 2016; Abe and Kuroda, 2019; Middelkoop et al., 2021; Tee et al., 2023), our results showed that the rotational speed in Caco-2 cells did not decrease but even slightly increased when treated with SMIFH2, a known inhibitor of formins, suggesting that formins are not required for Caco-2 cell chirality. Curiously, a previous study showed that SMIFH2 inhibits the centripetal movement of Myosin II filaments in HFF (Nishimura et al., 2021b), simultaneously demonstrating that this inhibitor also inhibits myosins, which apparently contradicts our observation. However, the same group also reported that SMIFH2 facilitated the centripetal movement of actin and myosin filaments when rat embryo fibroblasts were used (Nishimura et al., 2021a), similar to our present observations as shown in (Figure 6—figure supplement 1J). These reports suggest that how cells respond to SMIFH2 depends on their types. In the case of Caco-2 cells, it is likely that the observed effects of SMIFH2 on actomyosin dynamics were not attributed to its potential inhibition of Myosin II, although how this inhibitor induced the observed reorganization of actin and myosin filaments in Caco-2 cells remains unknown, as SMIFH2 seems to have multiple targets (Nishimura et al., 2021a). Our experiments to deplete DIAPH2 and DAAM1 also support the idea that formins are not essential for breaking the chiral symmetry, at least in the present cell system.

In Caco-2 cells treated with SMIFH2, the actomyosin ring became more visible than in the control cells (Figures 3, 4). Cells treated with SMIFH2 tended to show a trend of actin and myosin shifting from the ventral side to the dorsal side compared to control cells, although not statistically significant (Figure 8D, E). This might be due to a decrease in the formation of stress fibers on the ventral side, followed by a shift of free actin and Myosin II to the dorsal side, which may lead to an increase in the formation of actomyosin ring at the dorsal side. In contrast, treatment by Rho Activator II increased the stress fiber formation at the ventral side, which can induce a shift of actin and Myosin II to the ventral side, leading to a decrease in the formation of actomyosin ring at the dorsal side (Figure 8D, E). These considerations provide support for the model that dorsal actomyosin constitutes the driving force behind the rotational motion, as the rotation tended to increase or decrease in SMIFH2- or Rho Activator II-treated cells, respectively.

In a previous study (Kumar et al., 2014), an achiral active fluid model was proposed to explain the rotation of the nucleus driven by actomyosin. In the theory, the concentric orientational order of actomyosin becomes unstable due to the spontaneous chiral symmetry breaking induced by the contractility of actomyosin, and then a chiral orientational order emerges to drive a unidirectional fluid flow to rotate the nucleus. Since there is no intrinsic chirality in the model, either clockwise or counterclockwise rotation is selected with equal probability. In contrast, in our theoretical model, we considered the intrinsic chirality of the actomyosin gel in order to explain our experiments where the rotational direction is always clockwise. Although our model is consistent with our experimental observations, there is still a limitation. We assumed a concentric orientational order of actomyosin. However, it remains to be elucidated how the concentric order is formed (Tarama and Shibata, 2022; Ni et al., 2022), and how stable the structure is when the actomyosin has intrinsic chirality.

Several types of cells have been reported to exhibit chiral nuclear rotation. Zebrafish melanophores exhibit a counterclockwise nuclear rotation ‘from basement view’ (Yamanaka and Kondo, 2015), which is the same as our observation where the nucleus rotates in a clockwise direction viewed from the dorsal side. The study reported that actin plays a pivotal role in the chiral rotational motion. In the case of singly isolated MDCK cells embedded in a 3D culture, nuclei as well as whole cells exhibited rotations in either direction with a bias to the counterclockwise direction (Chin et al., 2018). Furthermore, a weak inhibition of actin polymerization reversed the bias in the rotational motion, and an actin-binding protein α-actinin-1 regulates the direction of chiral rotation (Chin et al., 2018), similar to the case of HFF (Tee et al., 2015; Tee et al., 2023). In the case of C2C12 myoblasts, whether actin filaments were organized or disorganized was shown to correlate with chirally biased nuclear rotation (Kwong et al., 2019). In contrast to HFF (Tee et al., 2015; Tee et al., 2023), the direction of nuclear rotation of Caco-2 is opposite and the chirality of Caco-2 does not require the activity of Arp2/3 complex (Figure 2) nor physical interactions between the actin ring and other actin structures such as radial fibers. Thus, the mechanism of cell chirality formation seems to differ between cell types, such as HFF and Caco-2 cells. Whether there is a common principle behind the chiral nuclear rotation or whether there are multiple mechanisms remains to be clarified in future studies.

Beads attached externally to the dorsal membrane exhibited both chiral rotation and centripetal movement, as shown in Video 2. This behavior mirrors the movement of actin filaments at the dorsal side, suggesting that the dorsal membrane moves in concert with the underlying actomyosin. In contrast, stress fibers located just above the ventral membrane did not move as shown in the leftmost panel of Video 5, suggesting that the ventral membrane is likely immobile. These observations imply that the dorsal region of the cell undergoes twisting relative to the ventral region. Given the fluid-like properties of the membrane, such twisting is expected to be resolved over the time scale of the rotation of the dorsal side. Similar twisting behavior has been observed in zebrafish melanophores (Yamanaka and Kondo, 2015).

The observation that rotational speed changes with substrate coating (Figure 1—figure supplement 1) may be attributed to several factors, including redistribution of actomyosin that affects the amount of dorsal actomyosin, as exemplified by the effect of Rho Activator II, and substrate-dependent changes in the cell’s internal physical environment, such as variations in effective viscosity at the ventral side.

It has been suggested that the left–right asymmetry at the tissue level originates from chirality at the cellular level. However, it remains unclear how cell chirality coordinates to induce left–right asymmetry in multicellular organisms. Our previous theoretical studies showed that a tissue-scale asymmetry, such as a spatial gradient in the strength of cell-scale torque generation, is necessary for the tissue-scale left–right asymmetry to arise from cell chirality (Yamamoto et al., 2020; Sato et al., 2015b; Sato et al., 2015a). Hence, it will be necessary to investigate how cell chirality and tissue-level asymmetry coordinate to understand left–right asymmetry in organs and the body. Caco-2 is an epithelial line that can form multicellular layers. We thus hope that investigating the coordination between cell chirality and tissue-level chirality using cells, such as Caco-2, which exhibit a clear individual chirality, is a promising approach to reveal the principles of chiral morphogenesis.

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
      <td>Caco-2</td>
      <td>ATCC</td>
      <td></td>
      <td>Ozawa et al., 2020</td>
    </tr>
    <tr>
      <td>Transfected construct (Homo sapiens)</td>
      <td>Lifeact-RFP</td>
      <td>Ozawa et al., 2020</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Homo sapiens)</td>
      <td>EMTB-3XGFP</td>
      <td>Addgene, Miller and Bement, 2009</td>
      <td>Plasmid \# 26741</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (Homo sapiens)</td>
      <td>Lifeact-mEmerald</td>
      <td>Nakamura et al., 2012</td>
      <td>pLVSIN-EF1a-Lifeact-mEmerald-IRES-pur</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>siRNA: Myosin IIA</td>
      <td>Invitrogen</td>
      <td>MYH9HSS106871</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>siRNA: Myosin IIB</td>
      <td>Invitrogen</td>
      <td>MYH10HSS106875</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>siRNA: DAAM1</td>
      <td>Invitrogen</td>
      <td>DAAM1HSS177085</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>siRNA: DIAPH2</td>
      <td>Invitrogen</td>
      <td>DIAPH2HSS102773</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>siRNA: Vinculin</td>
      <td>Invitrogen</td>
      <td>VCL s14764</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Myosin IIA (rabbit monoclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>M8064</td>
      <td>IF (1:1000)WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Myosin IIB (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>8824</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-GAPDH (mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-166574</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HRP-conjugated anti-rabbit IgG (goat monoclonal)</td>
      <td>Invitrogen</td>
      <td>T20926</td>
      <td>WB (1:1000–1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HRP-conjugated anti-mouse IgG (goat monoclonal)</td>
      <td>Invitrogen</td>
      <td>T20912</td>
      <td>WB (1:1000–1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Vinculin (mouse monoclonal)</td>
      <td>Sigma</td>
      <td>V9131</td>
      <td>IF (1:200)WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Ezrin (mouse monoclonal)</td>
      <td>Abcam</td>
      <td>ab4069</td>
      <td>IF (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-DAAM1 (mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-100942</td>
      <td>WB (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Diaph2 (mouse monoclonal)</td>
      <td>Santa Cruz Biotechnology</td>
      <td>sc-55540</td>
      <td>WB (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 488 anti-rabbit IgG (goat monoclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>11034</td>
      <td>IF (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 488 anti-mouse IgG (goat monoclonal)</td>
      <td>Invitrogen</td>
      <td>A11029</td>
      <td>IF (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 647 anti-mouse IgG (donkey monoclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>AP192SA6</td>
      <td>IF (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Alexa Fluor 488 (rabbit monoclonal)</td>
      <td>abcam</td>
      <td>ab150077</td>
      <td>IF (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 488-conjugated anti-rabbit IgG (goat monoclonal)</td>
      <td>Park et al., 2020</td>
      <td>A11034</td>
      <td>IF (1:1000)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Latranculin A</td>
      <td>Sigma</td>
      <td>L5163-100UG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Jasplakinolide</td>
      <td>Toronto Research Chemicals Inc</td>
      <td>J210700</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Nocodazole</td>
      <td>Sigma-Aldrich</td>
      <td>M1404</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CK666</td>
      <td>Sigma-Aldrich</td>
      <td>SML0006-5MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>SMIFH2</td>
      <td>Wako</td>
      <td>4401/10</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Blebbistatin</td>
      <td>Sigma</td>
      <td>B0560-1MG</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Rho Activator II</td>
      <td>Cytoskeleton, Inc</td>
      <td>Cat. #CN03</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Alexa Fluor 568 phalloidin</td>
      <td>Invitrogen</td>
      <td>A12380</td>
      <td>1:400</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Alexa Fluor 488 phalloidin</td>
      <td>Invitrogen</td>
      <td>A12379</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageJ Fiji</td>
      <td>Schindelin et al., 2012</td>
      <td>Version 2.14.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Trim Galore</td>
      <td>Krueger et al., 2023</td>
      <td>Version 0.6.10</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HISAT2</td>
      <td>Kim et al., 2019</td>
      <td>Version 2.2.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Samtools</td>
      <td>Danecek et al., 2021</td>
      <td>Version 1.9</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Stringtie</td>
      <td>Kovaka et al., 2019</td>
      <td>Version 2.2.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PIVlab</td>
      <td>Thielicke and Sonntag, 2021</td>
      <td>Version 2.56</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>Mathworks</td>
      <td>R2024a</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FreeFEM++</td>
      <td>Hecht, 2012</td>
      <td>Version 4.15</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Cell cultures and transfection

Caco-2 (ATCC) cells were cultured in DMEM/Ham’s F-12 (FUJIFILM Wako Pure Chemical Corporation, 048-29785) supplemented with 10% fetal bovine serum (Sigma, F7524, Lot. BCBV 4600) and 1% penicillin/streptomycin (nacalai, 26253-84) at 37°C, 5% CO2 on collagen type I coated Dish (60 mm, IWAKI, 4010-010). For live imaging of actin, we used Lifeact-RFP-transfected Caco-2 cells which were established from Caco-2 (ATCC) in Ozawa et al., 2020. To live-image the microtubule dynamics, we transiently transfected Caco-2 cells with EMTB-3XGFP using Lipofectamine LTX Reagent with PLUS Reagent (Invitrogen, 15338100), according to the manufacturer’s protocol. EMTB-3XGFP was a gift from William Bement (Miller and Bement, 2009) (Addgene plasmid # 26741; http://n2t.net/addgene:26741; RRID:Addgene_26741) For Lifeact-mEmerald (pLVSIN-EF1a-Lifeact-mEmerald-IRES-pur), mEmerald-Lifeact-7 was inserted into pLVSIN-EF1a-IRES-pur at the BamHI and NotI sites by In-Fusion. The construction of pLVSIN-EF1a-IRES-pur has been described previously (Nakamura et al., 2012). mEmerald-Lifeact-7 was a gift from Michael Davidson (Addgene plasmid # 54148; http://n2t.net/addgene:54148; RRID:Addgene_54148).

For protein depletion, cells were transfected with Stealth siRNA or Silencer Select siRNA using Lipofectamine RNAi MAX (Invitrogen). The following Stealth siRNAs were used: MYH9HSS106871 for Myosin IIA; MYH10HSS106875 for Myosin IIB; DAAM1HSS177085 for DAAM1; DIAPH2HSS102773 for DIAPH2; Negative Control Med GC Duplex (#10002823) for negative control. The following Silencer Select siRNA was used: VCL s14764 for vinculin. We examined the effects of RNA interference at 5 days.

### Immunoblotting

Cells were collected in RIPA buffer containing 1× cOmplete EDTA-free protease inhibitor (Roche, 05056489001) and were then mechanically lysed by passage through a 27 G needle on ice. Samples were boiled with 10% 2-mercaptoethanol for 3 min and separated by SuperSep 7.5% SDS–polyacrylamide gel electrophoresis (Fujifilm, 198–14941) at 250 V/30 mA for 70 min, and subsequently transferred to a 0.45-μm pore size PVDF membrane (Cytiva, 1080682) at 250 V/300 mA for 90 min in an ice bath. The PVDF membrane was blocked with Blocking One (Nacalai Tesque, 03953-95) at 4°C overnight and incubated with appropriate primary antibodies for 60 min at room temperature (RT). After washing the membrane with Tris-buffered saline with 0.1% Tween 20 (TBST), it was incubated with appropriate HRP-conjugated secondary antibodies for 60 min at RT. The membrane was then washed with TBST, followed by enhanced chemiluminescence detection (Bio-Rad, 1705060) using LAS-3000 mini (Fujifilm) for image acquisition. Signal intensity was analyzed using the Gel Analysis tool in ImageJ Fiji (Schindelin et al., 2012). The following antibodies were used: rabbit anti-Myosin IIA (Sigma-Aldrich, M8064, dilution 1:1000); rabbit anti-Myosin IIB (Cell Signaling Technology, 8824, dilution 1:1000); mouse anti-GAPDH (Santa Cruz Biotechnology, sc-166574, dilution 1:1000); HRP-conjugated goat anti-rabbit IgG (Invitrogen, T20926, dilution 1:1000); HRP-conjugated goat anti-mouse IgG (Invitrogen, T20912, dilution 1:1000). As a protein ladder marker, Precision Plus Protein Dual Color Standard (Bio-Rad, 1610374) was used.

### Live cell imaging

For live-image data in Figures 1 and 2, Figure 2—figure supplement 1, we used an inverted fluorescence microscope (Olympus, IX-81) equipped with a spinning disk confocal imaging unit (Yokogawa, CSU-X1), a 60×/1.35 oil immersion objective (Olympus, UPLSAPO60XO), and a 561-nm laser (Coherent, Sapphire LP) for RFP excitation or a 488-nm laser (Coherent, Sapphire LP) for GFP excitation. We used a 40×/1.35 oil-immersion objective (Olympus, UApo/340) for the microtubule snapshots in Figure 2—figure supplement 1. The cells were seeded sparsely on a collagen type I coated glass-based dish (IWAKI, 4970-011), and incubated in a stage-top incubator (Tokai Hit) at 37°C with 5% CO2 during live imaging.

We took fluorescence images with multiple z-stacks (number of slices: 7 and $Δz$: 0.5 μm) by EMCCD (Andor Technology, iXon+) every 15 min, and then made maximum intensity Z projections. For the microtubule snapshots in Figure 2—figure supplement 1, we applied a different condition (number of slices: 5 and $Δz$: 1 μm).

For the inhibitor experiments, the following inhibitors were used: latrunculin A (Sigma, L5163-100UG); Jasplakinolide (Toronto Research Chemicals Inc, J210700); Nocodazole (Sigma-Aldrich, M1404); CK666 (Sigma-Aldrich, SML0006-5MG); SMIFH2 (Wako, 4401/10); Blebbistatin (Sigma, B0560-1MG); Rho Activator II (Cytoskeleton, Inc, Cat. #CN03). We started live imaging about 2–3 hr after seeding cells and added the inhibitors about 40 min before the live imaging.

When we observed the dynamics of the beads attached to the dorsal membrane of the cells, we used 2 μm carboxylate-modified beads (Invitrogen, F8887), and live-imaged the dynamics using the DIC channel of the microscope (Olympus, IX-81).

### Analysis of rotation of nucleus

We quantified the rotational behaviors of cells by manually tracking the dynamics of two nucleoli of each cell on DIC images (Segmentation Editor, Fiji). We defined the rotational angle of the cell nucleus by that of the line connecting the two nucleoli and analyzed the rotational dynamics using Python. In Figure 1A, B, we defined the initial time point of the measurement of the nuclear rotation by the time when we started the live imaging. In the inhibitor experiments in Figure 2, we determined the initial time point of the measurement as the time 5 hr after the initiation of live imaging, accounting for the time lag needed for the inhibitors to exert their effects. For each experimental condition, single-cell data were collected from multiple cells in a single culture dish; the number of cells analyzed is given in each figure legend.

### Immunofluorescence antibody staining and microscopy

Cells were seeded on collagen type I coated cover slips (Neuvitro Corporation, NEU-H-12-COLLAGEN-45) and treated with the inhibitors. After 8 hr, the cells were fixed with 2% PFA in PBS(−) for 10 min, permeabilized with 0.25% Triton X-100 in PBS(−) for 10 min, blocked with 3% BSA in PBS(−) for 30 min. Then, we incubated cells with primary antibodies (2 hr), secondary antibodies (1 hr), and phalloidin (30 min) in a blocking buffer (3% BSA in PBS(−)). After washing with PBS(−) three times, the samples were mounted with a mounting medium with DAPI (Vector Laboratories, VECTASHIELD, H-1200). All the processes were performed at RT.

We used rabbit anti-Myosin IIA (Sigma-Aldrich, M8064, 1:1000 for IF), mouse anti-Vinculin (Sigma, V9131, 1:200 for IF), and mouse anti-Ezrin (Abcam, ab4069, 1:1000 for IF) as the primary antibodies and Alexa Fluor 488 goat anti-rabbit IgG (Sigma-Aldrich, 11034, 1:1000 for IF), Alexa Fluor 488 goat anti-mouse IgG (Invitrogen, A11029, 1:1000 for IF), and Alexa Fluor 647 donkey anti-mouse IgG (Sigma-Aldrich, AP192SA6, 1:1000 for IF) as the secondary antibodies, respectively. For actin staining, we used Alexa Fluor 568 phalloidin (Invitrogen, A12380, 1:400).

To analyze the sample, we took fluorescence images with multiple z-stacks ($Δz$: 0.32 μm) using a laser scanning confocal microscope (Zeiss, LSM880) equipped with Plan-Apochromat 63×/1.4 Oil DIC M27. Images were processed with Fiji.

### RNA-seq analysis

RNA was extracted from three independent samples of Caco-2 cells using the RNeasy Kit (QIAGEN). Libraries were sequenced on an Illumina NextSeq 2000 platform with 100 bp single-end reads, supported by the RIKEN BDR DNA Analysis Facility at the Laboratory for Developmental Genome System. Adapter sequences were removed using Trim Galore. Reads were mapped to the reference genome (grch38) using HISAT2, sorted using samtools, and transcript abundances were quantified as transcripts per million using StringTie.

### Expansion microscopy

Protein-retention ExM was carried out as described previously (Zhang et al., 2020). Cells were cultured on collagen type I (Sigma, C8919-20ML) coated cover slips and treated with the inhibitors. Fixation, permeabilization, and blocking were performed as described above. To visualize F-actin, the cells were stained with Alexa Fluor 488 phalloidin (Invitrogen, A12379, 1:400) and next stained for 60 min with a rabbit anti-Alexa Fluor 488 antibody (abcam, ab150077, 1:500) as the primary antibody and Alexa Fluor 488-conjugated goat anti-rabbit IgG (1:1000) as the secondary antibody (Park et al., 2020). After washing, cells were incubated with 100 μg/mL of 6-((Acryloyl)amino)hexanoic acid, succinimidyl ester overnight at RT in the dark. Samples were incubated in gelation solution (8.6% (wt/wt) sodium acrylate, 2.5% (wt/wt) acrylamide, 0.15% (wt/wt) N,N′-methylenebisacrylamide, 2 M NaCl, 1× PBS, 0.1% TEMED, 0.1% ammonium persulfate) for 5 min on ice. Gelation was allowed to proceed at RT for 1 hr. The gel and a cover slip were removed with tweezers and incubated with digestion buffer (0.5% Triton X-100, 1× TE buffer, 1 M NaCl, 8 unit/ml Proteinase K) overnight at RT in the dark. The gels were removed from the digestion buffer and placed in 50 ml of Milli-Q water. Water was exchanged three times every 30 min. Most of the gels expanded to about 4.5 times their original size. Gels were placed on a poly-L-lysine (Sigma-Aldrich, P4707) coated glass bottom dish, and fluorescence images were taken by a laser scanning confocal microscope (Zeiss, LSM880).

### LLSM and image processing

The LLSM was home-built in the Kiyosue laboratory at RIKEN Center for Biosystems Dynamics Research following the design of the Betzig laboratory (Chen et al., 2014) under a research license agreement from Howard Hughes Medical Institute. Electric wiring was performed at RIKEN Advanced Manufacturing Support Team. Metal parts were processed by Maeda Precision Manufacturing Ltd and Zera Development Co. To create a lattice light sheet, a dithered square lattice was used through a spatial light modulator (Fourth Dimension Displays) in combination with an annular mask with 0.55 out and 0.44 inner numerical apertures (Photo-Sciences) and a custom NA 0.65 excitation objective (Special Optics). Images were acquired through a CFI Apo LWD 25XW 1.1-NA detection objective (Nikon) and a scientific sCMOS camera, Orca Flash 4.0 v3 (Hamamatsu Photonics). Caco-2 cells expressing Lifeact-mEmerald were seeded on a collagen-coated coverslip 3 hr before imaging. During imaging, cells were maintained in DMEM/Ham’s F-12 (FUJIFILM Wako Pure Chemical Corporation, 048-29785) supplemented with 10% fetal bovine serum (Sigma, F7524, Lot. BCBV 4600) at 37°C, 5% CO2. For live imaging of Lifeact-mEmerald, a 488-nm laser (MPB Communications) and a long-pass emission filter BLP01-488R-25 (Semrock) were used. Image stacks were collected with a 200-nm step size between planes with 10 ms per plane exposure time and 14.8-s time interval. After the acquisition, images were deskewed and deconvolved using LLSpy. After deskew processing, the voxel pitch was 0.104 × 0.104 × 0.103 μm.

### PIV analysis

PIV analysis was performed using PIVlab (Thielicke and Sonntag, 2021) for the time-lapse images obtained by LLSM. The velocity vector fields were calculated using a multi-grid interrogation (64 × 64, 32 × 32, and 16 × 16 pixel sizes of interrogation windows with 50% overlap each). PIV was performed in the masked area, and the masked area was determined by thresholding the time-integrated image. Using the velocity vector field ($v_{x},v_{y}$), we first calculated azimuthal ($v_{\phi}$) and radial ($v_{ρ}$) velocities as $v_{\phi}=x^v_{y}−y^v_{x}$ and $v_{r}=x^v_{x}+y^v_{y}$, where $x^=x/r$ and $y^=y/r$ with $(x,y)$ being the position from the center of cell and $r=\sqrt{x^{2}+y^{2}}$. Here, the cell center was taken as the $xy$-coordinate of the highest position of the unimodal-shaped cell. From the DIC image, the nucleus always rotates around the center of the nucleus, with the highest position of the cell just above the nucleus center. Then, the angular velocity $\omega$ was obtained as $\omega=v_{\phi}/r$. The temporal averages of $v_{\phi}$ and $\omega$ are shown in Figure 6—figure supplement 1 for all samples analyzed control cells (DMSO) (Figure 6—figure supplement 1A–D) and cells treated with SMIFH2 (Figure 6—figure supplement 1E–H). The angular averages of $v_{\phi}$ (Figure 6—figure supplement 1I), $v_{r}$ (Figure 6—figure supplement 1J), and $\omega$ (Figure 6C) were obtained from their temporal averages at each spatial point. These averages were plotted against the radius scaled by the inner radius of the actomyosin ring in Figure 6D. We here manually identified the inner edge of the actomyosin ring and calculated the inner radius for each cell.

### Theoretical model

We here describe a derivation of our 3D model (Fürthauer et al., 2012). We assume a low Reynolds number limit, a steady state, and incompressibility. In the theory of active chiral fluid, the momentum conservation is represented as:

$$
0=∂_{\beta}(\sigma_{\alpha\beta}^{s}+\sigma_{\alpha\beta}^{e}+\sigma_{\alpha\beta}^{a}),
$$

where $\sigma_{\alpha\beta}^{s}$ and $\sigma_{\alpha\beta}^{a}$ are the symmetric and asymmetric parts of the deviatoric stress, respectively. $\sigma_{\alpha\beta}^{e}$ is Ericksen stress (hydrostatic stress). The indices α, β, and γ denote the three Cartesian coordinates $x,y,$ and $z$. The constitutive equations of the deviatoric stress are given:

$$
\sigma_{\alpha\beta}^{s}=2ηu_{\alpha\beta}+ζ^{a}p_{\alpha}p_{\beta},
$$



$$
\sigma_{\alpha\beta}^{a}=2η^{′}(Ω_{\alpha\beta}−\omega_{\alpha\beta}),
$$

where $u_{\alpha\beta}=(∂_{\alpha}v_{\beta}+∂_{\beta}v_{\alpha})/2$ and $\omega_{\alpha\beta}=(∂_{\alpha}v_{\beta}−∂_{\beta}v_{\alpha})/2$ is the strain rate and the vorticity. $Ω_{\alpha\beta}$ is the spin rotation rate describing the intrinsic rotation rate of local volume elements. $η$ and $η^{′}$ are viscosity coefficients, and $ζ^{a}$ is a coefficient of the achiral active stress. We here only consider anisotropic contributions of active terms allowed in a chiral nematic active fluid for simplicity. Also, in this study, since we assume that the orientational field $p$ is fixed to be a concentric pattern, we omit the terms that derive from the molecular field. We thus define $\sigma_{\alpha\beta}^{e}=−P\delta_{\alpha\beta}$, where $P$ is the pressure serving as a Lagrange multiplier to satisfy the incompressibility.

The angular momentum conservation is given by the following equation:

$$
∂_{\gamma}M_{\alpha\beta\gamma}=2\sigma_{\alpha\beta}^{a},
$$

where $M_{\alpha\beta\gamma}$ is the angular momentum flux. The constitutive equation is written as:

$$
M_{\alpha\beta\gamma}=κ∂_{\gamma}Ω_{\alpha\beta}+ζ^{c}ϵ_{\alpha\beta\delta}p_{\delta}p_{\gamma},
$$

where $κ$ is a dissipative coefficient and $ζ^{c}$ is a coefficient of the active chiral stress which reflects the symmetry of the torque dipole represented in Figure 7, which is called nematic chiral rod motor (Fürthauer et al., 2012). $ϵ_{\alpha\beta\gamma}$ is the Levi-Civita symbol.

We derive the following equation of motion from Equations 2–6,

$$
0=−∂_{\alpha}P+2η∂_{\beta}u_{\alpha\beta}+∂_{\beta}ζ^{a}p_{\alpha}p_{\beta}+\frac{1}{2}∂_{\beta}∂_{\gamma}ζ^{c}ϵ_{\alpha\beta\delta}p_{\delta}p_{\gamma}+\frac{κ}{4η^{′}}∂_{\gamma}^{2}(∂_{\beta}P\delta_{\alpha\beta}−2η∂_{\beta}u_{\alpha\beta}−2∂_{\beta}ζ^{a}p_{\alpha}p_{\beta}+2η^{′}∂_{\beta}\omega_{\alpha\beta}).
$$

In the final term of Equation 7, the length scale $ℓ=\sqrt{κ/η^{′}}$ is a characteristic molecular scale. Since we consider the hydrodynamics at the cell scale, we take the limit of $ℓ→0$ and omit the final term. Finally, applying the incompressibility condition $∂_{\gamma}v_{\gamma}=0$, we obtain the final form:

$$
0=−∂_{\alpha}P+η∂_{\gamma}^{2}v_{\alpha}+∂_{\beta}ζ^{a}p_{\alpha}p_{\beta}+\frac{1}{2}∂_{\beta}∂_{\gamma}ζ^{c}ϵ_{\alpha\beta\delta}p_{\delta}p_{\gamma},
$$

which is equivalent to Equation 1. By introducing non-dimensional velocity, position, and pressure as $v~=\frac{η}{ζ^{a}R_{0}}v$, $(x~,y~,z~)=(x/R_{0},y/R_{0},z/R_{0})$ and $P~=P/ζ^{a}$, where $R_{0}$ is the cell radius, the non-dimensional form of Equation 1 is given by

$$
0=−∇~P~+∇~^{2}v~+∇~⋅pp+\frac{1}{2}ζ∇~\times∇~⋅pp
$$

with the non-dimensional parameter

$$
ζ=\frac{ζ^{c}}{ζ^{a}R_{0}},
$$

which essentially describes the chiral activity relative to the non-chiral active contribution. Hereafter, we omit tilde from the non-dimensional velocity, position, and pressure.

In the numerical simulations, for simplicity, we suppose that the cell is axisymmetric as shown in Figure 7, Figure 7—figure supplement 1. Based on the experimental observations, we consider that the actomyosin bundles align along the circumferential direction: the concentric pattern of the actomyosin ring. We here represent the orientational order $p$ of the actomyosin in the cylindrical coordinate $(ρ,\phi,z)$. Since $p$ is aligned in the circumferential direction, $p(ρ,z)$ is given in the cylindrical coordinate by

$$
p(ρ,z)=S(ρ,z)(0,1,0)^{t},
$$

where $S(ρ,z)$ is the effective strength of the orientation of the actomyosin and takes a finite value in the domain where the actomyosin ring is present. Since we did not see any specific orientational order in the direction of the cell height, at least at our imaging resolution, we considered the orientation of the actomyosin bundle to be parallel to the substrate, and the $z$ component of $p(ρ,z)$ is zero. In the cylindrical coordinate, the equation of motion Equation 1 for the fluid velocity $v=(v_{ρ},v_{\phi},v_{z})^{t}$ and the pressure $P$ read

$$
∂_{ρ}^{2}v_{\phi}+∂_{z}^{2}v_{\phi}+\frac{1}{ρ}∂_{ρ}v_{\phi}−\frac{1}{ρ^{2}}v_{\phi}=\frac{ζ}{ρ}S∂_{z}S,
$$



$$
∂_{ρ}^{2}v_{ρ}+∂_{z}^{2}v_{ρ}+\frac{1}{ρ}∂_{ρ}v_{ρ}−\frac{1}{ρ^{2}}v_{ρ}=∂_{ρ}P+\frac{S^{2}}{ρ},
$$



$$
∂_{ρ}^{2}v_{z}+∂_{z}^{2}v_{z}+\frac{1}{ρ}∂_{ρ}v_{z}=∂_{z}P,
$$



$$
\frac{v_{ρ}}{ρ}+∂_{ρ}v_{ρ}+∂_{z}v_{z}=0.
$$

We numerically solve the equations with the following boundary shape, as shown in Figure 7—figure supplement 1. The dorsal boundary of the cell is well described by the following equations:

$$
{z=Z_{0}−r_{1}+\sqrt{r_{1}^{2}−ρ^{2}}(0\leqρ\leqρ_{1})z=Z_{2}−\sqrt{r_{2}^{2}−(ρ−ρ_{2})^{2}}(ρ_{1}\leqρ\leqρ_{3})z=−(tan⁡\alpha)(ρ−R_{0})(ρ_{3}\leqρ\leqR_{0})
$$

with

$$
{ρ_{1}=\frac{r_{1}ρ_{2}}{r_{1}+r_{2}}ρ_{3}=ρ_{2}−r_{2}sin⁡\alphar_{2}=(sin⁡\alpha)(ρ_{2}−R_{0})+(cos⁡\alpha)Z_{2}Z_{2}=−\frac{r_{1}−Z_{0}−(cos⁡\alpha)(r_{1}+(ρ_{2}−R_{0})sin⁡\alpha)+\sqrt{(−r_{1}+(r_{1}−Z_{0})cos⁡\alpha+R_{0}sin⁡\alpha)(−r_{1}+(r_{1}−Z_{0})cos⁡\alpha+(R_{0}−2ρ_{2})sin⁡\alpha)}}{sin^{2}⁡\alpha}
$$

where $Z_{0}$ is the cell height, $R_{0}$ is the cell radius, $r_{1}$, $ρ_{2}$, and α are the parameters that determine the cell shape. We determined the values of those parameters from the experimental data as $Z_{0}=8.2$ µm, $r_{1}=15.0$ µm, $ρ_{2}=22.0$ µm, $R_{0}=35.0$ µm, and $\alpha=7.0\times2\pi/360.0$. The ventral boundary is specified by $z=0$.

Since the actomyosin ring is located along the dorsal surface, we practically consider that as shown in Figure 7B $S(ρ,z)$ is given by

$$
S=(\frac{1}{2}tanh⁡(\lambda_{1}((sin⁡\beta)ρ+(cos⁡\beta)z−(sin⁡\beta)R_{0}+ξ))+\frac{1}{2})(\frac{1}{2}tanh⁡(−\lambda_{2}((cos⁡\beta)ρ−(sin⁡\beta)z−ξ_{3}))+\frac{1}{2})
$$

in the range $(cos⁡\beta)ρ−(sin⁡\beta)z−\frac{ρ_{3}^{′}}{cos⁡\beta}+(sin⁡\beta)(tan⁡\beta)R_{0}\leq0$, and

$$
S=\frac{1}{2}tanh⁡(\lambda(r_{2}^{′}+ξ−\sqrt{(ρ−ρ_{2})^{2}+(z−Z_{2}^{′})^{2}}))+\frac{1}{2}
$$

in the range $(cos⁡\beta)ρ−(sin⁡\beta)z−\frac{ρ_{3}^{′}}{cos⁡\beta}+(sin⁡\beta)(tan⁡\beta)R_{0}>0$. Here, $ρ_{3}^{′}$, $r_{2}^{′}$ and $Z_{2}^{′}$ are given by

$$
{ρ_{3}^{′}=ρ_{2}−r_{2}^{′}sin⁡\betar_{2}^{′}=(sin⁡\beta)(ρ_{2}−R_{0})+(cos⁡\beta)Z_{2}^{′}Z_{2}^{′}=−\frac{r_{1}−Z_{0}^{′}−(cos⁡\beta)(r_{1}+(ρ_{2}−R_{0})sin⁡\beta)+\sqrt{(−r_{1}+(r_{1}−Z_{0}^{′})cos⁡\beta+R_{0}sin⁡\beta)(−r_{1}+(r_{1}−Z_{0}^{′})cos⁡\beta+(R_{0}−2ρ_{2})sin⁡\beta)}}{sin^{2}⁡\beta}
$$

where $\lambda_{1}$, $\lambda_{2}$, $\beta$, $ξ$, $ξ_{3}$, and $Z_{0}^{′}$ are the parameters that determine the distribution of activity inside the cell. We used the following parameter values, $\lambda_{1}=150.0/R_{0}\mum^{−1}$ , $\lambda_{2}=20.0/R_{0}$ , $\beta=1.7\times\alpha$, $ξ=0.06\timesR_{0}\mum$, $ξ_{3}=0.7\timesR_{0}\mum/s$ and $Z_{0}^{′}=1.5\timesZ_{0}$.

We numerically solved the equations of motion by assuming the no-slip boundary condition for the ventral boundary, the free slip boundary condition for the dorsal surfaces (Kashiwabara et al., 2016), and the vanishing flow velocity for $v_{ρ}$ and $v_{\phi}$ and the continuity for $v_{z}$ at the cell center $ρ=0$. We do not include any organelles such as a nucleus in the model for simplicity. The equations were solved numerically with a finite element method using software FreeFEM++ (Hecht, 2012).

We determined the parameter values to reproduce the experimental observation as follows. As shown in Figure 7—figure supplement 2A–H, the peak values of the radial and azimuthal velocities are comparable. To reproduce this property, we set the parameter value of $ζ$ to be $ζ=0.004$. The simulation also reproduced the shift in the peak positions between two velocities. The peak values of the velocities in the simulation were about $2\times10^{−4}$ (unitless), while those in the experiments were about $5\times10^{−3}∼10^{−2}\mum/s$, giving the velocity scale to be $\frac{ζ^{a}R_{0}}{η}=50\mum/s$ and the time scale to be $\frac{η}{ζ^{a}}=0.7$ s. With this time scale, the peak value of the angular velocity was about 80 degree/hr as shown in Figure 7H, consistent with the experimental observation shown in Figure 6C, D.

### Quantification of dorsal and ventral actomyosin

Fluorescent signals of anti-Myosin IIA and phalloidin were obtained by LSM880 (Zeiss) with Airyscan and processed by ImageJ Fiji. The obtained images were resliced and ten x–z slices containing the cell center were processed with mean intensity projection. The dorsal and ventral surfaces were manually traced with 10-pixel width, and the average signal intensities in the traced regions were quantified. The cell edge regions of overlapping dorsal and ventral traces were annotated as ‘peripheral region’ and excluded from the quantification.
