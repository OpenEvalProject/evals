# Calcium transients trigger switch-like discharge of prostaglandin E2 in an extracellular signal-regulated kinase-dependent manner

## Authors

- Tetsuya Watabe<sup>1</sup>
- Shinya Yamahira<sup>1</sup>
- Kanako Takakura<sup>1</sup>
- Dean Thumkeo<sup>3</sup>
- Shuh Narumiya<sup>3</sup>
- Michiyuki Matsuda<sup>1</sup> ([ORCID: 0000-0002-5876-9969](https://orcid.org/0000-0002-5876-9969))
- Kenta Terai<sup>2</sup> ([ORCID: 0000-0001-7638-3720](https://orcid.org/0000-0001-7638-3720)) †

### Affiliations

1. https://ror.org/02kpeqv85 Research Center for Dynamic Living Systems, Graduate School of Biostudies, Kyoto University Kyoto Japan
2. https://ror.org/02kpeqv85 Department of Pathology and Biology of Diseases, Graduate School of Medicine, Kyoto University Kyoto Japan
3. https://ror.org/02kpeqv85 Department of Drug Discovery Medicine, Graduate School of Medicine, Kyoto University Kyoto Japan
4. https://ror.org/02kpeqv85 Institute for Integrated Cell-Material Sciences, Kyoto University Kyoto Japan

† Corresponding author

## Abstract

Prostaglandin E 2 (PGE 2 ) is a key player in a plethora of physiological and pathological events. Nevertheless, little is known about the dynamics of PGE 2 secretion from a single cell and its effect on the neighboring cells. Here, by observing confluent Madin–Darby canine kidney (MDCK) epithelial cells expressing fluorescent biosensors, we demonstrate that calcium transients in a single cell cause PGE 2 -mediated radial spread of PKA activation (RSPA) in neighboring cells. By in vivo imaging, RSPA was also observed in the basal layer of the mouse epidermis. Experiments with an optogenetic tool revealed a switch-like PGE 2 discharge in response to the increasing cytoplasmic Ca 2+ concentrations. The cell density of MDCK cells correlated with the frequencies of calcium transients and the following RSPA. The extracellular signal-regulated kinase (ERK) activation also enhanced the frequency of RSPA in MDCK and in vivo. Thus, the PGE 2 discharge is regulated temporally by calcium transients and ERK activity.

## Introduction

Prostaglandin E2 (PGE2) is an eicosanoid lipid mediator that regulates a plethora of homeostatic functions, including vascular permeability, immune response, and mucosal integrity (Narumiya, 2007). The metabolic pathway of PGE2 production, which is a major branch of the arachidonic acid cascade, was extensively studied in the mid to late 20th century. This cascade starts from the activation of cytosolic phospholipase A2 (cPLA2) (Park et al., 2006). Increased intracellular calcium induces the translocation and activation of cPLA2 from the cytosol to the Golgi, endoplasmic reticulum, and perinuclear membrane, where cPLA2 cleaves arachidonic acid out of the membrane phospholipids (Clark et al., 1995; Hirabayashi et al., 1999; Evans et al., 2001). The arachidonic acid is then presented to cyclooxygenases, COX1 and COX2, to yield PGH2, which is further converted to PGE2 by prostaglandin E synthases (Smith and Langenbach, 2001). PGE2 synthesized de novo is secreted to the extracellular space either by passive diffusion or by active transport by multidrug resistance protein 4 (MRP4) (Reid et al., 2003). The secreted PGE2 exerts its actions by acting on four G protein-coupled receptors (GPCRs), EP1 to EP4, expressed in neighboring cells (Narumiya, 2007; Regan, 2003).

Although it is largely believed that the PGE2 action is primarily regulated by the expression and activation of COX (Kalinski, 2012), cPLA2 appears to play a more important role in the short-term regulation of PGE2 production and secretion (Leslie, 2015). It was shown that the secretion of arachidonic acid is induced within a few minutes after the calcium-dependent translocation of cPLA2 to endo-membranes (Hirabayashi et al., 1999; Evans et al., 2001). Moreover, ERK and p38 MAP kinases also contribute to the activation of cPLA2 (Lin et al., 1993), which may be calcium-independent (Gijón et al., 2000). Importantly, these earlier biochemical studies did not elucidate the dynamics of the production and secretion of PGE2 at the single-cell level, leaving many questions unanswered. For example, do all cells contribute to the production of PGE2? Does each cell keep secreting PGE2 upon stimulation?

Genetically encoded biosensors based on the principle of Förster resonance energy transfer (FRET) allow us to visualize the dynamics of intracellular signaling molecules at the single-cell resolution (Miyawaki and Niino, 2015; Greenwald et al., 2018). The development of transgenic mice expressing FRET biosensors has opened a window to the visualization of signaling molecule activity in live tissues (Terai et al., 2019). Furthermore, by using the activation of protein kinase A (PKA) and ERK MAP kinase as surrogate markers, we can also visualize the intercellular communications mediated by Gs-coupled receptors and tyrosine kinase receptors in live tissues (Konishi et al., 2021; Hino et al., 2020). In this study, we show that PGE2 discharged from a single cell causes radial spread of PKA activation (RSPA) in neighboring cells in tissue culture and the mouse epidermis. By combining a chemical biology approach, optogenetic stimulation, and a simulation model, we quantitatively analyzed the PGE2 secretion and found that the PGE2 discharge is regulated temporally by calcium transients and quantitatively by growth factor signaling and cell density.

## Results

## PGE2 mediates RSPA

In an attempt to understand intercellular communication under physiological conditions, we observed the PKA activity of Madin–Darby canine kidney (MDCK) epithelial cells by using the FRET biosensor Booster-PKA (Zhang et al., 2001; Watabe et al., 2020; Figure 1A). We noticed that PKA activation propagates from a single cell to neighboring cells under a confluent condition. We named this phenomenon radial spread of PKA activation (RSPA) and pursued underlying mechanisms (Figure 1B, Figure 1—video 1). In a typical example, approximately 100 neighboring cells located within a 100 µm distance exhibit firework-like spread of PKA activation, which decays within several minutes. To characterize this phenomenon without preoccupations, we developed a program to identify and characterize RSPA under various conditions (Figure 1C). The frequency, but not the radius, of RSPA depended on the cell density; that is, RSPA was observed only when cells were maintained at more than 6 × 104 cells/cm2 (Figure 1D and E). The probability of RSPA in each cell was also increased in a cell density-dependent manner (Figure 1—figure supplement 1A). To examine whether the PKA activation correlates with increased intracellular cAMP concentration, we employed another FRET biosensor for cAMP, hyBRET-Epac, and performed a similar experiment (Watabe et al., 2020; Ponsioen et al., 2004; Figure 1—figure supplement 1B and C). Although the increment of the FRET ratio was not so remarkable as that of Booster-PKA (Figure 1—figure supplement 1D), we found that the pattern of cAMP concentration change is very similar to the activity change of PKA, indicating that a Gs protein-coupled receptor (GsPCR) mediates RSPA (Figure 1—figure supplement 1E). This discrepancy between hyBRET-Epac and Booster-PKA may be partially explained by the difference in the dynamic ranges for cAMP signaling in each FRET biosensor (Watabe et al., 2020). Previous transcriptome analysis of MDCK cells showed that ATP receptor and PGE2 receptor EP2 are the most abundant GsPCRs (Shukla et al., 2015). Thus, we examined the contribution of the ATP receptor and PGE2 receptors EP2 and EP4 by using specific inhibitors (Figure 1F). Inhibitors against EP2, EP4, and COX, but not the ATPase apyrase, abolished RSPA, indicating that PGE2 mediates RSPA.

## RSPA is also observed in the epidermis of the PKAchu mice

To clarify the physiological relevance of RSPA, we used PKAchu mice, which are transgenic mice expressing a FRET biosensor for PKA, AKAR3EV (Kamioka et al., 2012; Sato et al., 2020; Figure 2A). We previously observed that ERK MAP kinase activation is propagated radially among the basal layer cells of the mouse epidermis (Hiratsuka et al., 2015), but we failed to observe a similar propagation of PKA activation. We reasoned that this failure was due to the low frequency and short duration of this phenomenon. When we observed a region of over 1 mm square at 1 min intervals, we successfully observed RSPA in the basal layer of the mouse auricular epidermis (Figure 2B, Figure 2—video 1). Upon i.p. injection of a COX inhibitor, RSPA almost completely disappeared within 10 min (Figure 2C), indicating that RSPA in the epidermis is mediated by prostaglandins, presumably PGE2. The cell density in the basal layer is approximately 2 × 106 cells cm-2, which is markedly higher than that in MDCK cells (Figure 2D and E). It is not clear whether this may be related to the lower frequency (~300 cm–2 hr-1) and smaller radius of RSPA in the basal layer cells compared to MDCK cells (Figure 2E).

## RSPA is triggered by calcium transients

What causes RSPA? In agreement with the principal role of calcium in cPLA2 activation, dual imaging of calcium and PKA showed that an intracellular calcium transient precedes RSPA (Figure 3A). As anticipated, the frequency of RSPA was suppressed by the calcium chelator BAPTA-AM (Figure 3B). Note that not all of the calcium transients induced RSPA (Figure 3C, arrowheads). Approximately only one-tenth of calcium transients evoke RSPA (compare Figures 1E and 3D). Moreover, the frequency of calcium transients was also cell density-dependent (Figure 3D). To further pursue the relationship between calcium transient and RSPA, we employed the Gq-DREADD system (Armbruster et al., 2007). The Gq-DREADD-expressing producer cells were plated with the reporter cells expressing Booster-PKA at a 1:1200 ratio (Figure 3E). Upon activation of the Gq protein-coupled receptor by the DREADD ligand CNO, we observed RSPA with almost the same size and time course as observed under the non-stimulated condition (Figure 3F). Among cells with the calcium transient, 76% exhibited RSPA, significantly higher than that in the unstimulated state. Because the average calcium signal intensity was higher in RSPA (+) cells than in RSPA (-) cells (Figure 3G), the peak value of calcium transients appears to be important for the following induction of RSPA.

## RSPA is a switch-like response to cytoplasmic calcium concentration

To further explore the relationship between the peak value of the calcium transient and RSPA, we employed OptoSTIM1, an optogenetic tool to activate the calcium influx (Kyung et al., 2015; Figure 4A). As anticipated, a blue light flash caused a calcium transient, followed by RSPA (Figure 4B). In a preliminary experiment, a 30 min interval was sufficient to restore the calcium response; therefore, we repeated the blue light flash every 30 min to 1 hr with increasing light intensity. As the light intensity was increased, the amplitude of calcium transients represented by the R-GECO signal also increased linearly (Figure 4C). In stark contrast, RSPA occurred in an all-or-nothing manner. We repeated this experiment for 13 cells to find any correlations between the calcium concentration and the size of RSPA (Figure 4D). The R-GECO signal intensity ratio (F/F0) that evoked RSPA ranged from 1.5 to 2.1 among the different cells (Figure 4D, left), but the size of RSAP did not show a clear correlation with the R-GECO signal intensity ratio (Figure 4D, right). This observation indicates that there is a threshold of the cytoplasmic calcium concentration for the triggered PGE2 secretion.

![Figure 4.](https://cdn.elifesciences.org/articles/86727/elife-86727-fig4-v1.jpg)

**Figure 4.:** (A) Schematic representation of RSPA induction using OptoSTIM1. Madin–Darby canine kidney (MDCK) cells expressing OptoSTIM1 and R-GECO1 were employed as the producer cells. The Booster-PKA-expressing MDCK cells, deficient in COX-1 and COX-2 (COX-DKO), were employed as the reporter cells. (B) The producer cells were stimulated by a flashlight during imaging. Blue circled cells in the mKOκ image are the producer cells. The FRET ratio, the value of mKate2/mKOκ, in each pixel is shown in pseudocolor as indicated. The time 0 was set as just before blue light irradiation. The detection limit for the RSPA radius was 26 µm, as shown in the shaded area. (C) Flashlight illumination was repeated with increasing LED power. (D) Vertically aligned dots (left) are the results from an individual producer cell. The right panel shows the relationship between R-GECO fluorescence intensity and the radius of RSPA.

## High cell density increases the sensitivity to PGE2

We next explored the mechanism that determines the size of RSPA. First, taking advantage of the reproducibility of DREADD system, we examined the involvement of EP2/EP4, cPLA2, and COX1/2 in the calcium-induced RSPA by CRISPR/Cas9-mediated gene knockout (Figure 5A). As anticipated, we did not observe any RSPA by using the reporter MDCK cells deficient from EP2 and EP4. Knockout of COX2 and cPLA2, but not COX1, in the producer cells almost completely abolished CNO-induced RSPA. These results support the idea that RSPA is mediated by PGE2 via the Ca2+-cPLA2-COX2-EP2/4-cAMP-PKA pathway (Figure 5B).

Next, because the size of RSPA depends on the cell density (Figure 1E), we reasoned that the sensitivity of MDCK cells to PGE2 may also be regulated by cell density. To avoid the effect of PGE2 produced by the cells, the COX1/2-deficient MDCK cells were challenged by the bath application of PGE2. We found an approximately tenfold difference in the EC50 between the high and low cell densities (Figure 5C), suggesting that increased sensitivity to PGE2 underlies the increased RSPA size under the confluent condition. Transcriptome analysis showed a twofold increase in guanine nucleotide-binding protein G(s) subunit alpha (GNAS) (Figure 5D), but it is not clear whether this difference is sufficient to explain the difference in RSPA frequency. We did not observe any cell density dependence in the transcription of EP2, EP4 (Figure 5D), phosphodiesterases, or adenylyl cyclases (Figure 5—figure supplement 1). Thus, the cell density appears to increase the sensitivity to PGE2 mostly in a transcription-independent manner.

## ERK activity is required for RSPA

Previously, we reported that ERK activation is propagated among confluent MDCK cells in a wave-like fashion (Aoki et al., 2013). To examine whether ERK activity also regulates RSPA, we simultaneously observed ERK and PKA activities by using EKAREV-NLS and Booser-PKA, respectively (Figure 6A). It appeared that the center of RSPA was localized primarily in areas of high ERK activity. Further quantitative analysis has shown that the ERK activity of the cells locating in the center of RSPA was significantly higher than that of the randomly chosen cells (Figure 6B, left). However, the size of RSPA did not correlate with the ERK activity (Figure 6B, right). We next examined the timing of RSPA and the passage of ERK activation waves by aligning the events at the highest PKA activity. It appears that RSPA was evoked when the cells exhibited the highest ERK activity (Figure 6C and D, Figure 6—figure supplement 1). Cross-correlation analysis of PKA activity and ERK activity revealed that ERK activation preceded PKA activation by approximately 3 min (Figure 6E). The ERK activation wave is known to be mediated by EGFR and EGFR ligands (Lin et al., 2022). Accordingly, the addition of EGF faintly increased the frequency of RSPA in our experiments, while the MEK and EGFR inhibitors almost completely abrogated RSPA (Figure 6F), representing that ERK activation or basal ERK activity is essential for RSPA. Collectively, these results obtained with MDCK cells showed that RSPA is triggered by calcium transient in cells with high ERK activity.

The results in MDCK cells motivated us to validate our model in vivo. Thus, we tested RSPA in the basal layer of the mouse auricular epidermis could be canceled by the administration of MEKi (Figure 6G and H). As anticipated, RSPA in the basal layer was significantly attenuated 30 min after the administration, representing that ERK activity is required for RSPA in vivo.

## Discussion

## PGE2 discharge causes radial spread of PKA activation in neighboring cells

To the best of our knowledge, only one study has visualized PGE2 secretion from a single cell (Zonta et al., 2003). In this study, HEK cells expressing the Gq-coupled PGE2 receptor EP1 and a calcium indicator were used to monitor PGE2 release from agonist-stimulated astrocytes. However, the spontaneous release of PGE2 has never been visualized in either tissue culture cells or live animals. Here we have shown that PGE2 is discharged after calcium transients in MDCK cells at high cell densities (Figure 1). This PGE2 discharge leads to the radial spread of PKA activation, which we named RSPA, in the neighboring EP2-expressing cells. By using transgenic mice expressing the PKA biosensor, RSPA was also observed in the mouse auricular epidermis (Figure 2). RSPA in the epidermis is almost completely shut off by COXi, strongly suggesting that prostaglandin(s), most likely PGE2, mediates RSPA in the skin. Notably, we failed to observe RSPA in melanoma tissues in which calcium transients were frequently observed (Konishi et al., 2021). We reasoned that repetitive PGE2 secretion from tumor cells maintains a high PGE2 concentration in the tumor microenvironment, which prevented us from observing pulsatile PKA activation. In fact, the PGE2 concentration in melanoma tissue is known to reach as high as 10 µM (Konishi et al., 2021). Thus, RSPA in the skin may function as an alert signal in an early phase of cellular stress.

## PGE2 is discharged in a switch-like manner in response to Ca2+ transients

Soon after the identification of a Ca2+-dependent translocation domain within cPLA2 (Clark et al., 1991), Ca2+-dependent cPLA2 arachidonic acid release from cells has been reported (Hirabayashi et al., 1999; Gijón et al., 2000); therefore, it is not surprising to find that the PGE2 discharge in our present experiments was due to Ca2+-dependent cPLA2 activation (Figure 3). However, visualization of PGE2 secretion at the single-cell resolution revealed a switch-like response of PGE2 discharge to the increasing Ca2+ concentration (Figure 4). Recruitment of cPLA2 to the ER and perinuclear membrane requires a higher Ca2+ concentration than that to Golgi (Evans et al., 2001). If so, cPLA2 may be sequestered at Golgi at low intracellular Ca2+ concentration, and only when the intracellular Ca2+ concentration exceeds the threshold that cPLA2 may reach the ER to liberate arachidonic acids.

What does regulate the frequency of Ca2+ transients? Since the frequency is cell density-dependent in MDCK cells (Figure 3D), one candidate might be mechanical stress. 293 and HeLa cells demonstrate that cells show an increment in their frequency (Morita et al., 2015). However, a clear mechano receptor has not been identified.

## ERK also regulates the probability of RSPA

In the cell density-dependent RSPA of MDCK cells, ERK activity regulates the probability, but not the size, of RSPA. Of note, the MEK inhibitor did not significantly decrease the frequency of calcium transients (Figure 6—figure supplement 2), suggesting that ERK had a direct effect on the production of PGE2. Because ERK positively regulates cPLA2 by phosphorylating Ser505 (Cook and McCormick, 1993; Qiu et al., 1993), it is reasonable that the RSPA is regulated by ERK activity.

The ERK activation wave is operated by a positive feedforward mechanism in which ERK promotes EGFR ligand shedding and the following EGFR activation increases ERK activity in the neighboring cells (Hino et al., 2020; Aoki et al., 2017). Here we found that the ERK activation functions as the ‘AND gate’ for PGE2 production together with the calcium transients (Figure 7). Notably, the propagation of PKA activation, ~100 µm/min (Figure 1B), is markedly faster than that of ERK activation, 2–4 µm/min (Hiratsuka et al., 2015). Because PKA antagonizes Ras-dependent ERK activation (Cook and McCormick, 1993; Burgering et al., 1993; Wu et al., 1993), the EGFR ligand-ERK and PGE2-PKA pathways fit the Turing diffusion reaction model consisting of slow positive and fast negative signaling cascades.

![Figure 7.](https://cdn.elifesciences.org/articles/86727/elife-86727-fig7-v1.jpg)

**Figure 7.:** 2 (PGE2) secretion.The frequency of calcium transients is cell density-dependent manner. The ERK activation wave is there in both conditions. Because both calcium transient and ERK activation are required for radial spread of PKA activation (RSPA), the probability for PGE2 secretion is regulated as ‘AND gate’.

## RSPA may not directly affect cell competition

Recently, PGE2 was shown to regulate cell competition among MDCK cells. Interestingly, extrusion of Ras-transformed MDCK cells has been shown to be suppressed by PGE2 (Sato et al., 2020), whereas extrusion of MDCK cells expressing constitutively active YAP was dependent on PGE2 (Ishihara et al., 2020). Therefore, the effect of PGE2 in cell competition could be markedly different according to the signaling cascades that cause the oncogenic changes of MDCK cells. Importantly, PGE2 promotes the extrusion of MDCK cells expressing the constitutively active YAP by internalization of E-cadherin (Ishihara et al., 2020), which is a relatively slow process. Since RSPA causes PKA activation for only several minutes in each cell, multiple RSPA events may be needed to reach the concentration required for the induction of extrusion.

## The radius of RSPA might represent the amount of PGE2 discharge

The radius of RSPA, in MDCK cells, might partially represent the amount of PGE2 discharge from the single cell. However, because of the cell-to-cell junction of the confluent MDCK cells, we failed to quantify the PGE2. In HeLa cells, we quantitated PGE2 secreted from a single cell by combining fluorescence microscopy and a simulation model (Watabe et al., 2023).

## Limitations of this study

It would be clear that the physiological relevance of RSPA remains. In MDCK cells, the treatment of NSAIDs, which perturb RSPA, did not show a detectable change in cell growth, ERK wave propagation during collective migration, migration velocity, cell survival, or apoptosis. In mice epidermis, the frequency of RSPA was not remarkably changed by inflammation or corrective migration, evoked by TPA treatment or wound, respectively.

## Conclusions

We have shown that the PGE2 discharge from a single cell is a stochastic and switch-like event in the confluent MDCK cells and mouse epidermis. The secreted PGE2 can transiently activate PKA in cells within a few hundred micrometers from the producer cell. The question of why cells adopt this pulsatile rather than continuous secretion of PGE2 awaits the future.

## Materials and methods

## Reagents

ONO-AE3-208, PF-04418948, clozapine N-oxide, and PGE2 were purchased from Cayman Chemical. BAPTA-AM was obtained from Enzo Life Sciences. PD0325901, mitomycin C, and indomethacin were purchased from FUJIFILM Wako Pure Chemical Corp. AG1478 was purchased from BioVision Inc. Apyrase and EGF were obtained from Sigma-Aldrich. H-89 was purchased from Seikagaku Corp. The DREADD ligand, clozapine N-oxide, was purchased from Cayman Chemical. Flurbiprofen axetil was purchased from KAKEN Pharmaceutical.

## Cell culture

MDCK cells were purchased from the RIKEN BioResource Center (no. RCB0995). Lenti-X 293T cells were obtained from Invitrogen. MDCK and Lenti-X 293T cells were maintained in Dulbecco’s modiﬁed Eagle medium (FUJIFILM Wako Pure Chemical Corp.) containing 10% fetal bovine serum (Sigma-Aldrich) and 1% v/v penicillin−streptomycin (Nacalai Tesque). Cell line identity were validated.

## Plasmids and primers

Plasmids and primers are described in Supplementary files 1 and 2.

## Cell lines

For the generation of MDCK cells stably expressing Booster-PKA or the other ectopic proteins, a lentiviral or piggyBac transposon system was employed. To prepare the lentivirus, a lentiCRISPRv2-derived expression plasmid, psPAX2 (plasmid no. 12260; Addgene), and pCMV-VSV-G-RSV-Rev (RIKEN BioResource Center) were co-transfected into Lenti-X 293T cells using polyethyleneimine (Polyscience). Virus-containing media were collected at 48 or 72 hr after transfection, filtered, and applied to target cells with 10 μg/mL polybrene (Nacalai Tesque). To introduce ectopic genes using a PiggyBac system, pPB plasmids and pCMV-mPBase(neo-) encoding piggyBac transposase were co-transfected into MDCK cells by electroporation with an Amaxa nucleofector (Lonza). Cells were selected with the medium containing the following antibiotics: 10 μg/mL blasticidin S (FUJIFILM Wako Pure Chemical Corp.), 100 μg/mL zeocin (InvivoGen), 2.0 μg/mL puromycin (InvivoGen), or 200 μg/mL hygromycin (FUJIFILM Wako Pure Chemical Corp.).

MDCK cells expressing EKAREV-NLS were previously described (Kawabata and Matsuda, 2016). The established cell lines are described in Supplementary file 3.

The identity of cell lines was validated by partial genome sequence during knockout cell development. Mycoplasma contamination was tested with PlasmoTest (InvivoGen) when it was suspicious.

## CRISPR/Cas9-mediated KO cell lines

For CRISPR/Cas9-mediated single or multiple knockouts of genes, sgRNAs targeting the exons were designed using CRISPRdirect (Naito et al., 2015). Oligo DNAs for the sgRNA were cloned into the lentiCRISPRv2 (plasmid no. 52961; Addgene) vector or pX459 (plasmid no. 62988; Addgene) vector. The expression plasmids for sgRNA and Cas9 were introduced into MDCK cells by lentiviral infection or electroporation. For electroporation, pX459-derived plasmids were transfected into MDCK cells using an Amaxa Nucleofector II. Cells were selected with the medium containing the antibiotics depending on the drug-resistance genes. After the selection, genomic DNAs were isolated with SimplePrep reagent (TaKaRa Bio). PCR was performed using KOD FX neo (Toyobo) for amplification with the designed primers, followed by DNA sequencing.

## Wide-field fluorescence microscopy

Cells were imaged with an ECLIPSE Ti2 inverted microscope (Nikon) or an IX83 inverted microscope (Olympus). The ECLIPSE Ti2 inverted microscope was equipped with a Plan Fluor ×10 or ×4 objective, an ORCA Fusion Digital CMOS camera (HAMAMATSU PHOTONICS K.K.), an X-Cite TURBO LED light source (Excelitas Technologies), a Perfect Focus System (Nikon), a TI2-S-SE-E motorized stage (Nikon), and a stage top incubator (Tokai Hit). The IX83 inverted microscope was equipped with a UPlanAPO ×10/0.40 NA objective lens (Olympus), a Prime sCMOS camera (Photometrics), a CoolLED precisExcite LED illumination system (Molecular Devices), an IX2-ZDC laser-based autofocusing system (Olympus), and an MD-XY30100T-Meta automatically programmable XY stage.

The following ﬁlters were used for the multiplexed imaging: for CFP and YFP imaging, a 434/32 excitation ﬁlter (Nikon), a dichroic mirror 455 (Nikon), and 480/40 and 535-30 emission filters (Nikon) for CFP and YFP, respectively; for GCaMP6s imaging, a 480/40 (Nikon) excitation ﬁlter, a dichroic mirror 455 (Nikon), and a 535/50 emission filter (Nikon); for mKOκ and mKate2 imaging, a 555BP10 excitation ﬁlter (Omega Optical), an FF562Di03 dichroic mirror (Semrock), and XF3024 (590DF35) (Omega Optical) and BLP01-633R-25 (Semrock) emission filters for mKOκ and mKate2, respectively; for iRFP670 imaging, an FF01-640/14 excitation filter (Semrock), a dichroic mirror 660 (Nikon), and a 700/75 emission filter (Nikon); for R-GECO1, a 555BP10 excitation ﬁlter (Omega Optical), an FF562Di03 dichroic mirror (Semrock), and an XF3024 emission filter (590DF35) (Omega Optical).

## In vivo two-photon imaging of the mouse epidermis

The establishment of transgenic mice expressing AKAR3EV (PKAchu mice) was described previously (Kamioka et al., 2012). Briefly, 8- to 13-week-old female mice were used for the in vivo imaging. The ear hair was removed with a razor 1 d before the experiments. Mice were anesthetized with 1.5% isoﬂurane (FUJIFILM Wako Pure Chemical Corp.) inhalation and placed in a side-lying position on an electric heater maintained at 37°C. The ear skin was placed on the cover glass. Two-photon excitation microscopy was performed with an FV1200MPE-IX83 inverted microscope (Olympus) equipped with a ×30/1.05 silicon oil-immersion objective lens (XLPLN 25XWMP; Olympus), an InSight DeepSee Ultrafast laser (Spectra Physics), an IR-cut ﬁlter (BA685RIF-3), two dichroic mirrors DM505 (Olympus), and two emission ﬁlters (BA460-500 for CFP and BA520-560 for YFP) (Olympus). The excitation wavelength was 840 nm.

The animal protocols were approved by the Animal Care and Use Committee of Kyoto University Graduate School of Medicine (approval no. 22063).

## Spontaneous RSPA

MDCK cells expressing Booster-PKA or hyBRET-Epac were seeded on collagen-coated glass-bottom 96-well plates (Matsunami Glass Ind.) at a density of 1.2–2.4 × 105 cells/cm2. Before imaging, the culture media were replaced with phenol red-free M199 (Thermo Fisher Scientific) supplemented with 10% fetal bovine serum. Cells were imaged by wide-ﬁeld ﬂuorescence microscopy, as described above.

## Analysis of calcium concentrations

Intracellular Ca2+ concentrations in MDCK cells were visualized with a genetically encoded calcium indicator, GCaMP6s or R-GECO1. For GCaMP6s analysis, calcium signals were expressed as F/F0, where F is the fluorescence at each time point, and F0 represents baseline fluorescence. To analyze the peak F/F0 value of GCaMP6s, F0 was calculated as the minimum projection of fluorescence intensity over the 5 min before each frame. Each cell showing calcium transient was visually checked to exclude the F/F0 elevation caused by flowing debris and misregistration of cells. If two or more adjacent cells showed calcium transients simultaneously, it was counted as a calcium transient. If two or more calcium transients were detected at intervals of more than 1 min, they were counted separately. In the Gq-DREADD experiment, F0 was calculated as the mean intensity before the stimulation.

For R-GECO1 analysis, F/F0 calcium signals were calculated by assigning the reference F0 using the fluorescence intensity before each blue light flash.

## Gq-DREADD-induced calcium transients and RSPA

MDCK cells expressing both Gq-DREADD-P2A-mCherry-NLS (Evans et al., 2001) and GCaMP6s (Evans et al., 2001) were utilized as PGE2 producer cells. MDCK cells expressing Booster-PKA served as PGE2 reporter cells. The producer and reporter cells were mixed at a ratio of 1:400 to 1:200 and plated on collagen-coated glass-bottom 96-well plates (Matsunami Glass Ind. or AGC Inc) at a density of 1.2–2.4 × 105 cells/cm2. Before imaging, the culture media were replaced with phenol red-free M199 (Thermo Fisher Scientific) supplemented with 10% fetal bovine serum. Gq-DREADD was activated by the addition of 1 µM of clozapine N-oxide (CNO). Cells were imaged by wide-ﬁeld ﬂuorescence microscopy, as described above.

## Light-induced calcium transients and RSPA

MDCK cells expressing both R-GECO1-P2A-iRFP670 and OptoSTIM1 (CRY2clust) (Lee et al., 2014) were used as PGE2 producer cells. COX1 and COX2-deficient MDCK cells expressing Booster-PKA were used as PGE2 reporter cells. The producer and reporter cells were mixed at a ratio of 1:400 to 1:1200 and plated on collagen-coated glass-bottom 96-well plates (Matsunami Glass Ind.) or 24-well plates (AGC Inc). After 16–32 hr of incubation, the culture media were replaced with phenol red-free M199 (Thermo Fisher Scientific) supplemented with 10% fetal bovine serum or M199 supplemented with 0.1% w/v bovine serum albumin (Sigma-Aldrich). Cells were imaged by wide-ﬁeld ﬂuorescence microscopy, as described above. During the observation, OptoSTIM1 was activated with 475 nm LED for 200 ms to trigger calcium influx into the cell. To control the calcium influx from small to large, the excitation light was modulated from 0.8 to 67 μW mm–2. To prevent cell division, MDCK cells with 3 µg/mL of mitomycin C for 1 hr 1 d before passage.

## Titration of PGE2 sensitivity

COX-1 and COX-2 depleted (COX-DKO) MDCK cells expressing Booster-PKA were seeded on a 96-well glass-base plate at the indicated densities. Before imaging, the culture media were replaced with phenol red-free M199 (Thermo Fisher Scientific) supplemented with 10% fetal bovine serum for MDCK. The 96-well plate was imaged by an inverted microscope as described earlier. mKate2 and mKOκ images were obtained in one position for every well at around 5 min intervals. Cells were stimulated with PGE2 at the indicated concentrations. The mKate2/mKOκ ratio was quantified from the average intensity of the whole field of view at around 20–30 min after the addition of PGE2.

## Quantification of RSPA

The program code for image analysis is available via GitHub at https://github.com/TetsuyaWatabe-1991/RSPAanalysis (copy archived at Watabe, 2023).

Ratio images of MDCK cells expressing Booster-PKA were created after background subtraction. A median filter and a Gaussian 2D filter were applied to each image for noise reduction. The ratio image was normalized by a minimum intensity projection along the time axis. The processed images were binarized with a predetermined threshold and processed by morphological opening and closing to refine the RSPA area. Center coordinates and equivalent circle radii were obtained from each RSPA area. If the distance between the center coordinates of RSPA between successive frames was less than 100 μm, they were considered to be the same RSPA. For MDCK cells expressing hyBRET-Epac and mouse ear skin expressing AKAR3EV, the center coordinates of each RSPA were manually determined due to the low signal-to-noise ratio.

To obtain the time course of the RSPA radius, concentric regions were defined at the center of each RSPA. The median FRET ratio in each concentric ROI was calculated. The radius of the outermost concentric region where the median ratio value exceeds a predetermined threshold was defined as the radius of the RSPA.

## Cross-correlation analysis of ERK and PKA activity

Cross-correlation analysis was performed with Python using the scientific library SciPy (http://www.scipy.org). The centers of each spontaneous RSPA in MDCK cells expressing both EKAREV and Booster-PKA were detected automatically as described above. The regions of interest were defined at the center of each RSPA with a radius of 10 µm, and the average ERK and PKA activity from 2 to 5 cells was quantified. The program code for this analysis is available via GitHub as described above.

## RNA-seq

COX1 and COX2-deficient MDCK cells expressing Booster-PKA were seeded in collagen-coated glass-bottom 96-well plates (AGC Inc) at a density of 1.5 × 104 or 6.0 × 104 or 2.4 × 105 cells/cm2. After 24 hr of incubation, the culture media were replaced with phenol red-free M199 (Thermo Fisher Scientific) supplemented with 10% fetal bovine serum. Then, 3 hr after medium replacement, RNA was extracted from each sample using an RNeasy Mini Kit (QIAGEN). Libraries for RNA-seq were prepared using an NEBNext Ultra II Directional RNA Library Prep Kit for Illumina (New England Biolabs) and sequenced on the NextSeq500 (Illumina) as 75 bp single-end reads. RNA-seq data were trimmed using Trim Galore version 0.6.6 (Krueger, 2015Krueger, 2015) and Cutadapt version 2.8 (Martin, 2011). The quality of reads was checked and filtered using FastQC version 0.11.9 (; Andrews, 2010). The reads were mapped to a reference genome canFam3.1 (Lindblad-Toh et al., 2005, Hoeppner et al., 2014) using HISAT2 version 2.2.1 (Kim et al., 2019), and the resulting aligned reads were sorted and indexed using SAMtools version 1.7 (Li et al., 2009). Relative abundances of genes were measured in FPKM using StringTie version 2.1.4 (Kovaka et al., 2019, Pertea et al., 2015). Plots were created in Python using the pandas, matplotlib, NumPy, and seaborn libraries.

Sequence data are available in the DNA Data Bank of Japan Sequence Read Archive under accession numbers DRR014156 to DRR014161.

## Statistical analysis

All statistical analyses and visualizations were performed in Python using the libraries NumPy, pandas, SciPy, pingouin, matplotlib, and seaborn. No statistical analysis was used to predetermine the sample size. Welch’s t-test was used to evaluate statistically signiﬁcant diﬀerences. p-Values <0.05 were considered statistically signiﬁcant.
