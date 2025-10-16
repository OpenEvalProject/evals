# Mitochondrial Ca2+ uptake by the voltage-dependent anion channel 2 regulates cardiac rhythmicity

## Authors

- Hirohito Shimizu<sup>1</sup>
- Johann Schredelseker<sup>1</sup>
- Jie Huang<sup>1</sup>
- Kui Lu<sup>2</sup>
- Shamim Naghdi<sup>3</sup>
- Fei Lu<sup>1</sup>
- Sarah Franklin<sup>4</sup>
- Hannah DG Fiji<sup>2</sup>
- Kevin Wang<sup>1</sup>
- Huanqi Zhu<sup>2</sup>
- Cheng Tian<sup>1</sup>
- Billy Lin<sup>1</sup>
- Haruko Nakano<sup>1</sup>
- Amy Ehrlich<sup>3</sup>
- Junichi Nakai<sup>6</sup>
- Adam Z Stieg<sup>7</sup> ([ORCID: 0000-0001-7312-9364](https://orcid.org/0000-0001-7312-9364))
- James K Gimzewski<sup>2</sup>
- Atsushi Nakano<sup>1</sup>
- Joshua I Goldhaber<sup>10</sup>
- Thomas M Vondriska<sup>4</sup>
- György Hajnóczky<sup>3</sup>
- Ohyun Kwon<sup>2</sup>
- Jau-Nian Chen<sup>1</sup> †

### Affiliations

1. Department of Molecular, Cell and Developmental Biology University of California, Los Angeles Los Angeles United States
2. Department of Chemistry and Biochemistry University of California, Los Angeles Los Angeles United States
3. MitoCare Center, Department of Pathology, Anatomy and Cell Biology Thomas Jefferson University Philadelphia United States
4. Department of Anesthesiology University of California, Los Angeles Los Angeles United States
5. Broad Center of Regenerative Medicine and Stem Cell Research University of California, Los Angeles Los Angeles United States
6. Brain Science Institute Saitama University Saitama Japan
7. California NanoSystems Institute University of California, Los Angeles Los Angeles United States
8. WPI Center for Materials Nanoarchitectonics National Institute for Materials Science Tsukuba Japan
9. School of Physics, Centre for Nanoscience and Quantum Information University of Bristol Bristol UK
10. Cedars-Sinai Heart Institute Los Angeles United States

† Corresponding author

## Abstract

10.7554/eLife.04801.001 Tightly regulated Ca 2+ homeostasis is a prerequisite for proper cardiac function. To dissect the regulatory network of cardiac Ca 2+ handling, we performed a chemical suppressor screen on zebrafish tremblor embryos, which suffer from Ca 2+ extrusion defects. Efsevin was identified based on its potent activity to restore coordinated contractions in tremblor . We show that efsevin binds to VDAC2, potentiates mitochondrial Ca 2+ uptake and accelerates the transfer of Ca 2+ from intracellular stores into mitochondria. In cardiomyocytes, efsevin restricts the temporal and spatial boundaries of Ca 2+ sparks and thereby inhibits Ca 2+ overload-induced erratic Ca 2+ waves and irregular contractions. We further show that overexpression of VDAC2 recapitulates the suppressive effect of efsevin on tremblor embryos whereas VDAC2 deficiency attenuates efsevin's rescue effect and that VDAC2 functions synergistically with MCU to suppress cardiac fibrillation in tremblor . Together, these findings demonstrate a critical modulatory role for VDAC2-dependent mitochondrial Ca 2+ uptake in the regulation of cardiac rhythmicity. DOI: http://dx.doi.org/10.7554/eLife.04801.001

## Introduction

During development, well-orchestrated cellular processes guide cells from diverse lineages to integrate into the primitive heart tube and establish rhythmic and coordinated contractions. While many genes and pathways important for cardiac morphogenesis have been identified, molecular mechanisms governing embryonic cardiac rhythmicity are poorly understood. The findings that Ca2+ waves traveling across the heart soon after the formation of the primitive heart tube (Chi et al., 2008) and that loss of function of key Ca2+ regulatory proteins, such as the L-type Ca2+ channel, Na/K−ATPase and sodium-calcium exchanger 1 (NCX1), severely impairs normal cardiac function (Rottbauer et al., 2001; Shu et al., 2003; Ebert et al., 2005; Langenbacher et al., 2005), indicate an essential role for Ca2+ handling in the regulation of embryonic cardiac function.

Ca2+ homoeostasis in cardiac muscle cells is tightly regulated at the temporal and spatial level by a subcellular network involving multiple proteins, pathways, and organelles. The release and reuptake of Ca2+ by the sarcoplasmic reticulum (SR), the largest Ca2+ store in cardiomyocytes, constitutes the primary mechanism governing the contraction and relaxation of the heart. Ca2+ influx after activation of the L-type Ca2+ channel in the plasma membrane induces the release of Ca2+ from the SR via ryanodine receptor (RyR) channels, which leads to an increase of the intracellular Ca2+ concentration and cardiac contraction. During diastolic relaxation, Ca2+ is transferred back into the SR by the SR Ca2+ pump or extruded from the cell through NCX1. Defects in cardiac Ca2+ handling and Ca2+ overload, for example during cardiac ischemia/reperfusion or in long QT syndrome, are well known causes of contractile dysfunction and many types of arrhythmias including early and delayed afterdepolarizations and Torsade des pointes (Bers, 2002; Choi et al., 2002; Yano et al., 2008; Greiser et al., 2011).

Ca2+ crosstalk between mitochondria and ER/SR has been noted in many cell types and the voltage-dependent anion channel (VDAC) and the mitochondrial Ca2+ uniporter (MCU) serve as primary routes for Ca2+ entry through the outer and inner mitochondrial membranes, respectively (Rapizzi et al., 2002; Bathori et al., 2006; Shoshan-Barmatz et al., 2010; Baughman et al., 2011; De Stefani et al., 2011). In the heart, mitochondria are tethered to the SR and are located in close proximity to Ca2+ release sites (García-Pérez et al., 2008; Boncompagni et al., 2009; Hayashi et al., 2009). This subcellular architecture exposes the mitochondria near the Ca2+ release sites to a high local Ca2+ concentration that is sufficient to overcome the low Ca2+ affinity of MCU and facilitates Ca2+ crosstalk between SR and mitochondria (García-Pérez et al., 2008; Dorn and Scorrano, 2010; Kohlhaas and Maack, 2013). Increase of the mitochondrial Ca2+ concentration enhances energy production during higher workload and dysregulation of SR-mitochondrial Ca2+ signaling results in energetic deficits and oxidative stress in the heart and may trigger programmed cell death (Brandes and Bers, 1997; Maack et al., 2006; Kohlhaas and Maack, 2013). However, whether SR-mitochondrial Ca2+ crosstalk also contributes significantly to cardiac Ca2+ signaling during excitation-contraction coupling requires further investigation.

In zebrafish, the tremblor (tre) locus encodes a cardiac-specific isoform of the Na+/Ca2+ exchanger 1, NCX1h (also known as slc8a1a) (Ebert et al., 2005; Langenbacher et al., 2005). The tre mutant hearts lack rhythmic Ca2+ transients and display chaotic Ca2+ signals in the myocardium leading to unsynchronized contractions resembling cardiac fibrillation (Langenbacher et al., 2005). In this study, we used tre as an animal model for aberrant Ca2+ handling-induced cardiac dysfunction and took a chemical genetic approach to dissect the Ca2+ regulatory network important for maintaining cardiac rhythmicity. A synthetic compound named efsevin was identified from a suppressor screen due to its potent ability to restore coordinated contractions in tre. Using biochemical and genetic approaches we show that efsevin interacts with VDAC2 and potentiates its mitochondrial Ca2+ transporting activity and spatially and temporally modulates cytosolic Ca2+ signals in cardiomyocytes. The important role of mitochondrial Ca2+ uptake in regulating cardiac rhythmicity is further supported by the suppressive effect of VDAC2 and MCU overexpression on cardiac fibrillation in tre.

## Results and discussion

## Identification of a chemical suppressor of tre cardiac dysfunction

Homozygous

![Figure 1.](https://cdn.elifesciences.org/articles/04801/elife-04801-fig1-v1.jpg)

**Figure 1.:** (A) Line scans across the atria of Tg(myl7:GFP) embryonic hearts at 48 hpf. Rhythmically alternating systoles and diastoles are recorded from vehicle- (upper left) or efsevin- treated wild type (upper right) and efsevin-treated tre (lower right) embryos, while only sporadic unsynchronized contractions are recorded from vehicle-treated tre embryos (lower left). (B, C) Fractional shortening (FS) deduced from the line-scan traces. While cardiac contraction was not observed in tre, efsevin-treated wild type and tre hearts have similar levels of FS to those observed in control hearts. Ventricular FS of wild type v.s. wild type + efsevin vs tre + efsevin: 39 ± 0.6%, n = 8 vs 39 ± 1%, n = 10 vs 35 ± 3%, n = 6; and Atrial FS: 37 ± 1%, n = 11 vs 35 ± 2%, n = 11 vs 33 ± 2%, n = 15. (D) While efsevin restored a heart rate of 46 ± 2 beats per minute (bpm) in tre embryos, same treatment does not affect the heart rate in wild type embryos (126 ± 2 bpm in vehicle-treated embryos vs 123 ± 3 bpm in efsevin-treated wild-type embryos). ***, p < 0.001 by one-way ANOVA. (E) Dose-dependence curve for efsevin. The tre embryos were treated with various concentrations of efsevin from 24 hpf and cardiac contractions were analyzed at 48 hpf. (F–H) Representative time traces of local field potentials for wild type (F), tre (G) and efsevin-treated tre (H) embryos clearly display periods of regular, irregular, and restored periodic electrical activity. (I) In vivo optical maps of Ca2+ activation represented by isochronal lines every 33 ms recorded from 36 hpf wild type (left), tre (center) and efsevin-treated tre (right) embryos.DOI: http://dx.doi.org/10.7554/eLife.04801.003

## Efsevin suppresses Ca2+ overload-induced irregular contraction

We next examined whether efsevin could suppress aberrant Ca

![Figure 2.](https://cdn.elifesciences.org/articles/04801/elife-04801-fig2-v1.jpg)

**Figure 2.:** (A) Line-scan analysis of Ca2+ transients in mESC-CMs after 10 days of differentiation. (B–D) Representative graph of Ca2+ transients detected in mESC-CMs (B). After treatment with 10 mM Ca2+ for 10 min, the EB showed an irregular pattern of Ca2+ transients (C). Efsevin treatment restores regular Ca2+ transients under Ca2+ overload conditions in mESC-CMs (D). (E) Plotted intervals between peaks of Ca2+ signals detected in mESC-CMs prior to treatment (control), in 10 mM Ca2+ext (Ca2+) and in 10 mM Ca2+ext+10 μM efsevin (Ca2++efsevin). (F, G) Plotted intervals of contractions detected in EBs prior to treatment (control), in 10 mM Ca2+ext (Ca2+) and in 10 mM Ca2+ext + 10 μM efsevin (Ca2+ + efsevin) for mouse ESC-CMs (F) and 5 mM Ca2+ext (Ca2+) and in 5 mM Ca2+ext + 5 μM efsevin (Ca2+ + efsevin) for human ESC-CMs (G). ***, p < 0.001 by F-test.DOI: http://dx.doi.org/10.7554/eLife.04801.011

## VDAC2 mediates the suppressive effect of efsevin on tre

To identify the protein target of efsevin, we generated a N-Boc-protected 2-aminoethoxyethoxyethylamine linker-attached efsevin (efsevin

![Figure 3.](https://cdn.elifesciences.org/articles/04801/elife-04801-fig3-v1.jpg)

**Figure 3.:** (A) Structures of efsevin and two derivatives, OK-C125 and OK-C19. (B) Efsevin and OK-C125 restored rhythmic contractions in the majority of tremblor embryos, whereas OK-C19 failed to rescue the tremblor phenotype. (C) Structures of linker-attached compounds (indicated by superscript L). (D) Compounds efsevinL and OK-C125L retained their ability to restore rhythmic contractions in NCX1hMO injected embryos, while the inactive derivative OK-C19L was still unable to induce rhythmic contraction. (E) Affinity agarose beads covalently linked with efsevin (efsevinLB) or OK-C125 (OK-C125LB) pulled down 2 protein species from zebrafish embryonic lysate, whereof one, the 32 kD upper band, was sensitive to competition with a 100-fold excess free efsevinL. The 32 kD band was not detected in proteins eluted from beads capped with ethanolamine alone (beadsC) or beads linked to OK-C19 (OK-C19LB). Arrowheads point to the 32kD bands. (F) Mass Spectrometry identifies the 32kD band as VDAC2. Peptides identified by mass spectrometry (underlined) account for 30% of the total sequence.DOI: http://dx.doi.org/10.7554/eLife.04801.012

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/04801/elife-04801-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Image shows an example of the identification of VDAC2 peptide. Diagnostic b- and y-series ions are shown in red and blue, respectively.DOI: http://dx.doi.org/10.7554/eLife.04801.013

VDAC2 is expressed in the developing zebrafish heart (

![Figure 4.](https://cdn.elifesciences.org/articles/04801/elife-04801-fig4-v1.jpg)

**Figure 4.:** tre.(A) In situ hybridization analysis showed that VDAC2 is expressed in embryonic hearts at 36 hpf (upper image) and 48 hpf (lower image). (B) Injection of 25 pg in vitro synthesized VDAC2 mRNA restored cardiac contractions in 52.9 ± 12.1% (n = 78) of 1-day-old tre embryos, compared to 21.8 ± 5.1% in uninjected siblings (n = 111). (C) Schematic diagram of myl7:VDAC2 construct (top). In situ hybridization analysis showed that TBF treatment induces VDAC2 expression in the heart (lower panel). (D) While only ∼20% of myl7:VDAC2;NCX1hMO embryos have coordinated contractions (n = 116), 52.3 ± 2.4% of these embryos established persistent, rhythmic contractions after TBF induction of VDAC2 (n = 154). (E) On average, 71.2 ± 8.8% efsevin treated embryos have coordinated cardiac contractions (n = 131). Morpholino antisense oligonucleotide knockdown of VDAC2 (MOVDAC2) attenuates the ability of efsevin to suppress cardiac fibrillation in tre embryos (45.3 ± 7.4% embryos with coordinated contractions, n = 94). (F) Efsevin treatment restores coordinated cardiac contractions in 76.2 ± 8.7% NCX1MO embryos, only 54.1 ± 3.6% VDAC2zfn/zfn;NCX1MO embryos have coordinated contractions (n = 250). (G) Diagram of Zinc finger target sites. VDAC2 carries a 34 bp deletion in exon 3 which results in a premature stop codon (red asterisk). In situ hybridization analysis showing loss of VDAC2 transcripts in zfn/zfnVDAC2 embryos. White arrowheads point to the developing heart.zfn/zfnDOI: http://dx.doi.org/10.7554/eLife.04801.014

## VDAC2-dependent effect of efsevin on mitochondrial Ca2+ uptake

VDAC is an abundant channel located on the outer mitochondrial membrane serving as a primary passageway for metabolites and ions (

![Figure 5.](https://cdn.elifesciences.org/articles/04801/elife-04801-fig5-v1.jpg)

**Figure 5.:** 2+ uptake.(A) HeLa cells were transfected with a flag-tagged zebrafish VDAC2 (VDAC2flag), immunostained against the flag epitope and counterstained for mitochondria with MitoTracker Orange and for nuclei with DAPI. (B) Representative traces of mitochondrial matrix [Ca2+] ([Ca2+]m) detected by Rhod2. Arrows denote the addition of Ca2+. Mitochondrial Ca2+ uptake was assessed when VDAC2 was overexpressed (left), cells were treated with 1 µM efsevin (middle) and combination of both at suboptimal doses (right). Control-traces with ruthenium red (RuRed) show mitochondrial specificity of the signal. (C) Representative traces of cytosolic [Ca2+] ([Ca2+]c) changes upon the application of 7.5 µM IP3 in the presence (+) or absence (−) of RuRed. Mitochondrial Ca2+ uptake was assessed by the difference of the – and + RuRed conditions normalized to the total release (n = 4; mean ± SE). (D) MEFs overexpressing zebrafish VDAC2 (polycistronic with mCherry) were stimulated with 1 μM ATP in a nominally Ca2+ free buffer. Changes in [Ca2+]c and [Ca2+]m were imaged using fura2 and mitochondria-targeted inverse pericam, respectively. Black and gray traces show the [Ca2+]c (in nM) and [Ca2+]m (F0/F mtpericam) time courses in the absence (left) or present (right) of efsevin. (E) Bar charts: Cell population averages for the peak [Ca2+]c (left), the corresponding [Ca2+]m (middle), and the coupling time (time interval between the maximal [Ca2+]c and [Ca2+]m responses) in the presence (black, n = 24) or absence (gray, n = 28) of efsevin.DOI: http://dx.doi.org/10.7554/eLife.04801.024

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/04801/elife-04801-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** 2+ delivery between IP3 receptors and VDAC2.V1V3DKO MEFs were stimulated with 100 μM ATP (left) or 2 μM thapsigargan (Tg) (right). Changes in [Ca2+]c and [Ca2+]m were imaged using fura2 and mitochondria targeted inverse pericam, respectively. Representative traces obtained in three cells are shown.DOI: http://dx.doi.org/10.7554/eLife.04801.025

Mitochondria are located in close proximity to Ca2+ release sites of the ER/SR and an extensive crosstalk between the two organelles exists (García-Pérez et al., 2008; Hayashi et al., 2009; Brown and O'Rourke, 2010; Dorn and Scorrano, 2010; Kohlhaas and Maack, 2013). We examined whether Ca2+ released from intracellular stores could be locally transported into mitochondria through VDAC2 in VDAC1/VDAC3 double knockout (V1/V3DKO) MEFs where VDAC2 is the only VDAC isoform being expressed (Roy et al., 2009a). While treatments with ATP, an IP3-linked agonist, and thapsigargin, a SERCA inhibitor, stimulated similar global cytoplasmic [Ca2+] elevation in intact cells, only ATP induced a rapid mitochondrial matrix [Ca2+] rise (Figure 5—figure supplement 1). This finding is consistent with observations obtained in other cell types (Rizzuto et al., 1994; Hajnóczky et al., 1995) and suggests that Ca2+ was locally transferred from IP3 receptors to mitochondria through VDAC2 at the close ER-mitochondrial associations. We next investigated whether this process could be modulated by efsevin. In permeabilized V1/V3DKO MEFs, treatment with efsevin increased the amount of Ca2+ transferred into mitochondria during IP3-induced Ca2+ release (Figure 5C). Also, in intact V1/V3 DKO MEFs, efsevin accelerated the transfer of Ca2+ released from intracellular stores into mitochondria during stimulation with ATP (Figure 5D,E).

## Efsevin modulates Ca2+ sparks and suppresses erratic Ca2+ waves in cardiomyocytes

We next examined the effect of efsevin on cytosolic Ca

![Figure 6.](https://cdn.elifesciences.org/articles/04801/elife-04801-fig6-v1.jpg)

**Figure 6.:** (A) Electrically paced Ca2+ transients at 0.5 Hz (top). Normalized quantification of Ca2+ transient parameters reveals no difference for transient amplitude (efsevin-treated at 98.6 ± 4.5% of vehicle-treated) and time to peak (95 ± 3.9%), but a significant decrease for the rate of decay (82.8 ± 4% of vehicle- for efsevin-treated) (lower panel). (B) Representation of typical Ca2+ sparks of vehicle- and efsevin treated cardiomyocytes (top). No differences were observed for spark frequency (101.1 ± 7.7% for efsevin- compared to vehicle-treated), maximum spark amplitude (101.6 ± 2.5%) and Ca2+ release flux (98.7 ± 2.8%). In contrast, the decay phase of the single spark was significantly faster in efsevin treated cells (82.5 ± 2.1% of vehicle-treated). Consequently, total duration of the spark was reduced to 85.7 ± 2% and the total width was reduced to 89.5 ± 1.4% of vehicle-treated cells. *, p < 0.05; ***, p < 0.001. (C) Increasing concentrations of extracellular Ca2+ induced a higher frequency of spontaneous propagating Ca2+ waves in isolated adult murine ventricular cardiomyocytes. Efsevin treatment reduced Ca2+ waves in a dose-dependent manner. (D) Quantitative analysis of spontaneous Ca2+ waves spanning more than half of the entire cell. Addition of 1 µM efsevin reduced Ca2+ waves to approximately half. Increasing the concentration of efsevin to 10 µM further reduced the number of spontaneous Ca2+ waves and 25 µM efsevin almost entirely blocked the formation of Ca2+ waves.DOI: http://dx.doi.org/10.7554/eLife.04801.026

## Mitochondrial Ca2+ uptake modulates embryonic cardiac rhythmicity

We hypothesize that efsevin treatment/VDAC2 overexpression suppresses aberrant Ca

![Figure 7.](https://cdn.elifesciences.org/articles/04801/elife-04801-fig7-v1.jpg)

**Figure 7.:** (A) MCU and MICU1 are expressed in the developing zebrafish hearts (arrowhead). (B) Overexpression of MCU is sufficient to restore coordinated cardiac contractions in tre embryos (47.1 ± 1.6% embryos, n = 112 as opposed to 18.3 ± 5.3% of uninjected siblings, n = 64) while this effect is significantly attenuated when co-injected with morpholino antisense oligonucleotide targeted to VDAC2 (27.1 ± 1.9% embryos, n = 135). (C) Suboptimal overexpression of MCU (MCUS) and VDAC2 (VDAC2S) in combination is able to suppress cardiac fibrillation in tre embryos (42.9 ± 2.6% embryos, n = 129). (D) The ability of VDAC2 to restore rhythmic contractions in tre embryos (48.5 ± 3.5% embryos, n = 111) is significantly attenuated when MCU is knocked down by antisense oligonucleotide (MOMCU) (25.6 ± 2.4% embryos, n = 115). (E) Overexpression of MICU1 is sufficient to restore rhythmic cardiac contractions in tre embryos (49.3 ± 3.4% embryos, n = 127 compared to 16.8 ± 1.4% of uninjected siblings, n = 150). This effect is abrogated by VDAC2 knockdown (MOVDAC2, 25.3 ± 5.5% embryos, n = 97). (F) Suboptimal overexpression of MICU1 (MICU1S) and VDAC2 (VDAC2S) in combination is able to restore rhythmic cardiac contractions in tre embryos (48.6 ± 6.0%, n = 106). Error bars represent s.d.; *p < 0.05; ***p < 0.001.DOI: http://dx.doi.org/10.7554/eLife.04801.027

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/04801/elife-04801-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** In situ hybridization analysis shows that the expression levels of MCU, MICU1 and VDAC2 are comparable between wild type and tre embryos with and without efsevin treatment.DOI: http://dx.doi.org/10.7554/eLife.04801.028

## Conclusion

In summary, we conducted a chemical suppressor screen in zebrafish to dissect the regulatory network critical for maintaining rhythmic cardiac contractions and to identify mechanisms underlying aberrant Ca2+ handling-induced cardiac dysfunction. We show that activation of VDAC2 through overexpression or efsevin treatment potently restores rhythmic contractions in NCX1h deficient zebrafish hearts and effectively suppresses Ca2+ overload-induced arrhythmogenic Ca2+ events and irregular contractions in mouse and human cardiomyocytes. We provide evidence that potentiating VDAC2 activity enhances mitochondrial Ca2+ uptake, accelerates Ca2+ transfer from intracellular stores into mitochondria and spatially and temporally restricts single Ca2+ sparks in cardiomyocytes. The crucial role of mitochondria in the regulation of cardiac rhythmicity is further supported by the findings that VDAC2 functions in concert with MCU; these genes have a strong synergistic effect on suppressing cardiac fibrillation and loss of function of either gene abrogates the rescue effect of the other in tre.

The regulatory roles of mitochondrial Ca2+ in cardiac metabolism, cell survival and fate have been studied extensively (Brown and O'Rourke, 2010; Dorn and Scorrano, 2010; Doenst et al., 2013; Kasahara et al., 2013; Kohlhaas and Maack, 2013; Luo and Anderson, 2013). Our study provides genetic and physiologic evidence supporting an additional role for mitochondria in regulating cardiac rhythmicity and reveals VDAC2 as a modulator of Ca2+ handling in cardiomyocytes. Our findings, together with recent reports of the physical interaction between VDAC2 and RyR2 (Min et al., 2012) and the close proximity of outer and inner mitochondrial membranes at the contact sites between the mitochondria and the SR (García-Pérez et al., 2011), suggest an intriguing model. We propose that mitochondria facilitate an efficient clearance mechanism in the Ca2+ microdomain, which modulates Ca2+ handling without affecting global Ca2+ signals in cardiomyocytes. In this model, VDAC facilitates mitochondrial Ca2+ uptake via MCU complex and thereby controls the duration and the diffusion of cytosolic Ca2+ near the Ca2+ release sites to ensure rhythmic cardiac contractions. This model is consistent with our observation that efsevin treatment induces faster inactivation kinetics of cytosolic Ca2+ transients without affecting the amplitude or the time to peak in cardiomyocytes and the reports that blocking mitochondrial Ca2+ uptake has little impact on cytosolic Ca2+ transients (Maack et al., 2006; Kohlhaas et al., 2010). Further support for this model comes from the observation of the Ca2+ peaks on the OMM (Drago et al., 2012) and the finding that downregulating VDAC2 extends Ca2+ sparks (Subedi et al., 2011; Min et al., 2012) and that blocking mitochondrial Ca2+ uptake by Ru360 leads to an increased number of spontaneous propagating Ca2+ waves (Seguchi et al., 2005). Future studies on the kinetics of VDAC2-dependent mitochondrial Ca2+ uptake and exploring potential regulatory molecules for VDAC2 activity will provide insights into how the crosstalk between SR and mitochondria contributes to Ca2+ handling and cardiac rhythmicity.

Aberrant Ca2+ handling is associated with many cardiac dysfunctions including arrhythmia. Establishing animal models to study molecular mechanisms and develop new therapeutic strategies are therefore major preclinical needs. Our chemical suppressor screen identified a potent effect of efsevin and its biological target VDAC2 on manipulating cardiac Ca2+ handling and restoring regular cardiac contractions in fish and mouse and human cardiomyocytes. This success indicates that fundamental mechanisms regulating cardiac function are conserved among vertebrates despite the existence of species-specific features and suggests a new paradigm of using zebrafish cardiac disease models for the dissection of critical genetic pathways and the discovery of new therapeutic approaches. Future studies examining the effects of efsevin on other arrhythmia models would further elucidate the potential for efsevin as a pharmacological tool to treat cardiac arrhythmia associated with aberrant Ca2+ handling.

## Materials and methods

## Zebrafish husbandry and transgenic lines

Zebrafish of the mutant line tremblor (tretc318) were maintained and bred as described previously (Langenbacher et al., 2005). Transgenic lines, myl7:gCaMP4.1LA2124 and myl7:VDAC2LA2309 were created using the Tol2kit (Esengil et al., 2007; Kwan et al., 2007; Shindo et al., 2010). The VDAC2LA2256 was created using the zinc finger array OZ523 and OZ524 generated by the zebrafish Zinc Finger Consortium (Foley et al., 2009a, 2009b).

## Molecular Biology

Full length VDAC2 cDNA was purchased from Open Biosystems (Huntsville, AL) and cloned into pCS2+ or pCS2+3XFLAG. Full length cDNA fragments of zebrafish MCU (Accession number: JX424822) and MICU1 (JX42823) were amplified from 2 dpf embryos and cloned into pCS2+. For mRNA synthesis, plasmids were linearized and mRNA was synthesized using the SP6 mMESSAGE mMachine kit according to the manufacturers manual (Ambion, Austin, TX.).

## Zebrafish injections

VDAC2 mRNA and morpholino antisense oligos (5′-GGGAACGGCCATTTTATCTGTTAAA-3′) (Genetools, Philomath, OR) were injected into one-cell stage embryos collected from crosses of tretc318 heterozygotes. Cardiac performance was analyzed by visual inspection on 1 dpf. The tre mutant embryos were identified either by observing the fibrillation phenotype at 2–3 dpf or by genotyping as previously described (Langenbacher et al., 2005).

## Chemical screen

Chemicals from a synthetic library (Castellano et al., 2007; Choi et al., 2011; Cruz et al., 2011) and from Biomol International LP (Farmingdale, NY) were screened for their ability to partially or completely restore persistent heartbeat in tre embryos. 12 embryos collected from crosses of tretc318 heterozygotes were raised in the presence of individual compounds at a concentration of 10 µM from 4 hpf (Choi et al., 2011). Cardiac function was analyzed by visual inspection at 1 and 2 dpf. The hearts of tretc318 embryos manifest a chaotic movement resembling cardiac fibrillation with intermittent contractions in rare occasion (Ebert et al., 2005; Langenbacher et al., 2005). Compounds that elicit persistent coordinated cardiac contractions were validated on large number of tre mutant embryos and NCX1h morphants (>500 embryos).

## Zebrafish cardiac imaging

Videos of GFP-labelled myl7:GFP hearts were taken at 30 frames per second. Line-scan analysis was performed along a line through the atria or the ventricles of these hearts (Nguyen et al., 2009). Fraction of shortening was deduced from the ratio of diastolic and systolic width and heart rate was determined by beats per minute. Cardiac parameters were analyzed in tremblortc318 and VDAC2LA2256 at 2 dpf.

## Zebrafish optical mapping

36 hpf myl7:gCaMP4.1 embryos were imaged at a frame rate of 30 ms/frame. Electromechanical isolation was achieved by tnnt2MO (Milan et al., 2006). The fluorescence intensity of each pixel in a 2D map was normalize to generate heat maps and isochronal lines at 33 ms intervals were obtained by identifying the maximal spatial gradient for a given time point (Chi et al., 2008).

## Mouse and human embryonic stem cells

The mouse E14Tg2a ESC and human H9 ESC line were cultured and differentiated as previously described (Blin et al., 2010; Arshi et al., 2013). At day 10 of differentiation, beating mouse EBs were exposed to external solution containing 10 mM CaCl2 for 10 min before DMSO or efsevin (10 μM) treatment. Human EBs were differentiated for 15 days and treated with 5 mM CaCl2 for 10 min before DMSO or efsevin (5 μM) treatment. Images of beating EBs were acquired at a rate of 30 frames/s and analyzed by motion-detection software. For calcium recording, the EBs were loaded with 10 μM fluo-4 AM in culture media for 30 min at 37°C. Line-scan analysis was performed and fluorescent signals were acquired by a Zeiss LSM510 confocal microscope.

## Microelectrode array measurements

2-day-old wild type, tre, and efsevin-treated tre embryos were placed on uncoated, microelectrode arrays (MEAs) containing 120 integrated TiN electrodes (30 μm diameter, 200 μm interelectrode spacing). Local field potentials (LFPs) at each electrode were collected for three trials per embryo type over a period of three minutes at a sampling rate of 1 kHz using the MEA2100-HS120 system (Multichannel Systems, Reutiligen, Germany). Raw data was low-pass filtered at a cutoff frequency of 10 Hz using a third-order Butterworth filter. Data analysis was carried out using the MC_DataTool (Multichannel Systems) and Matlab (MathWorks).

## Ca2+ imaging

Murine ventricular cardiomyocytes were isolated as previously described (Reuter et al., 2004). Cells were loaded with 5 µM fluo-4 AM in external solution containing: 138.2 mM NaCl, 4.6 mM KCl, 1.2 mM MgCl, 15 mM glucose, 20 mM HEPES for 1 hr and imaged in external solution supplemented with 2, 5 or 10 mM CaCl2. For the recording of Ca2+ sparks and transients, the external solution contained 2 mM CaCl2. For Ca2+ transients, cells were field stimulated at 0.5 Hz with a 5 ms pulse at a voltage of 20% above contraction threshold. For all measurements, efsevin was added 2 hr prior to the actual experiment. Images were recorded on a Zeiss LSM 5 Pascal confocal microscope. Data analysis was carried out using the Zeiss LSM Image Browser and ImageJ with the SparkMaster plugin (Picht et al., 2007). Cells were visually inspected prior to and after each recording. Only those recordings from healthy looking cells with distinct borders, uniform striations and no membrane blebs or granularity were included in the analysis.

## Biochemistry

For pull down assays mono-N-Boc protected 2,2'-(ethylenedioxy)bis(ethylamine) was attached to the carboxylic ester of efsevin and its derivatives through the amide bond. After removal of the Boc group using TFA, the primary amine was coupled to the carboxylic acid of Affi-Gel 10 Gel (Biorad, Hercules, CA). 2-day-old zebrafish embryos were deyolked by centrifugation before being lysed with Rubinfeld's lysis buffer (Rubinfeld et al., 1993). The lysate was precleaned by incubation with Affi-Gel 10 Gel to eliminate non-specific binding. Precleaned lysate was incubated with affinity beads overnight. Proteins were eluted from the affinity beads and separated on SDS-PAGE. Protein bands of interest were excised. Gel plugs were dehydrated in acetonitrile (ACN) and dried completely in a Speedvac. Samples were reduced and alkylated with 10 mM dithiotreitol and 10 mM TCEP solution in 50 mM NH4HCO3 (30 min at 56°C) and 100 mM iodoacetamide (45 min in dark), respectively. Gel plugs were washed with 50 mM NH4HCO3, dehydrated with ACN, and dried down in a Speedvac. Gel pieces were then swollen in digestion buffer containing 50 mM NH4HCO3, and 20.0 ng/μl of chymotrypsin (25°C, overnight). Peptides were extracted with 0.1% TFA in 50% ACN solution, dried down and resuspended in LC buffer A (0.1% formic acid, 2% ACN).

## Mass spectrometry analyses and database searching

Extracted peptides were analyzed by nano-flow LC/MS/MS on a Thermo Orbitrap with dedicated Eksigent nanopump using a reversed phase column (New Objective, Woburn, MA). The flow rate was 200 nl/min for separation: mobile phase A contained 0.1% formic acid, 2% ACN in water, and mobile phase B contained 0.1% formic acid, 20% water in ACN. The gradient used for analyses was linear from 5% B to 50% B over 60 min, then to 95% B over 15 min, and finally keeping constant 95% B for 10 min. Spectra were acquired in data-dependent mode with dynamic exclusion where the instrument selects the top six most abundant ions in the parent spectra for fragmentation. Data were searched against the Danio rerio IPI database v3.45 using the SEQUEST algorithm in the BioWorks software program version 3.3.1 SP1. All spectra used for identification had deltaCN>0.1 and met the following Xcorr criteria: >2 (+1), >3 (+2), >4 (+3), and >5 (+4). Searches required full cleavage with the enzyme, <4 missed cleavages and were performed with the differential modifications of carbamidomethylation on cysteine and methionine oxidation.

## In situ hybridization

In situ hybridization was performed as previously described (Chen and Fishman, 1996). DIG-labeled RNA probe was synthesized using the DIG RNA labeling kit (Roche, Indianapolis, IN).

## Immunostaining

HeLa cells were transfected with a C-terminally flag-tagged zebrafish VDAC1 or VDAC2 in plasmid pCS2+ using Lipofectamine 2000 (Invitrogen). After staining with MitoTracker Orange (Invitrogen) cells were fixed in 3.7% formaldehyde and permeabilized with acetone. Immunostaining was performed using primary antibody ANTI-FLAG M2 (Sigma Aldrich, St. Luis, MO) at 1:100 and secondary antibody Anti-Mouse IgG1-FITC (Southern Biotechnology Associates, Birmingham, AL) at 1:200. Cells were mounted and counterstained using Vectashield Hard Set with DAPI (Vector Laboratories, UK).

## Mitochondria Ca2+ uptake assay in HeLa cells

HeLa cells were transfected with zebrafish VDAC2 using Lipofectamine 2000 (Invitrogen, Carlsbad, CA). 36 hrs after transfection, cells were loaded with 5 µM Rhod2-AM (Invitrogen), a Ca2+ indicator preferentially localized in mitochondria, for 1 hr at 15°C followed by a 30 min de-esterification period at 37°C. Subsequently, cells were permeabilized with 100 µM digitonin for 1 min at room temperature. Fluorescence changes in Rhod2 (ex: 544 nm, em: 590 nm) immediately after the addition of Ca2+ (final free Ca2+ concentration is calculated to be approximately 10 µM using WEBMAXC at http://web.stanford.edu/∼cpatton/webmaxcS.htm) were monitored in internal buffer (5 mM K-EGTA, 20 mM HEPES, 100 mM K-aspartate, 40 mM KCl, 1 mM MgCl2, 2 mM maleic acid, 2 mM glutamic acid, 5 mM pyruvic acid, 0.5 mM KH2PO4, 5 mM MgATP, pH adjusted to 7.2 with Trizma base) using a FLUOSTAR plate reader (BMG Labtech, Germany).

## Mitochondria Ca2+ uptake assay in VDAC1/VDAC3 double knockout (V1/V3 DKO) MEFs

V1/V3 DKO MEFs were cultured as previously described (Roy et al., 2009a). Efsevin-treated (15 μM for 30 min) or mock-treated MEFs were used for measurements of [Ca2+]c in suspensions of permeabilized cells or imaging of [Ca2+]m simultaneously with [Ca2+]c in intact single cells. Permeabilization of the plasma membrane was performed by digitonin (40 μM/ml). Changes in [Ca2+] in the cytoplasmic buffer upon IP3 (7.5 μM) addition in the presence or absence of ruthenium red (3 μM) was measured by fura2 in a fluorometer (Csordás et al., 2006; Roy et al., 2009b). To avoid endoplasmic reticulum Ca2+ uptake 2 μM thapsigargin was added before IP3. For imaging of [Ca2+]m and [Ca2+]c, MEFs were co-transfected with plasmids encoding polycistronic zebrafish VDAC2 with mCherry and mitochondria-targeted inverse pericam for 40 hr. Cells were sorted to enrich the transfected cells and attached to glass coverslips. In the final 10 min, of the efsevin or mock-treatment, the cells were also loaded with fura2AM (2.5 μM) and subsequently transferred to the microscope stage. Stimulation with 1 μM ATP was carried out in a norminally Ca2+ free buffer. Changes in [Ca2+]c and [Ca2+]m were imaged using fura2 (ratio of ex:340 nm–380 nm) and mitochondria-targeted inverse pericam (ex: 495 nm), respectively (Csordas et al., 2010).

## Statistics

All values are expressed as mean ± SEM, unless otherwise specified. Significance values are calculated by unpaired student's t-test unless noted otherwise.
