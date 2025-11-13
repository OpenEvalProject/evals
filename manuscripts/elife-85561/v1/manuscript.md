# Tomosyn affects dense core vesicle composition but not exocytosis in mammalian neurons

## Authors

- Aygul Subkhangulova<sup>1</sup> ([ORCID: 0000-0001-8843-0678](https://orcid.org/0000-0001-8843-0678)) †
- Miguel A Gonzalez-Lozano<sup>2</sup> ([ORCID: 0000-0002-7837-151X](https://orcid.org/0000-0002-7837-151X))
- Alexander JA Groffen<sup>3</sup> ([ORCID: 0000-0003-0046-4027](https://orcid.org/0000-0003-0046-4027))
- Jan RT van Weering<sup>3</sup>
- August B Smit<sup>2</sup>
- Ruud F Toonen<sup>1</sup> ([ORCID: 0000-0002-9900-4233](https://orcid.org/0000-0002-9900-4233))
- Matthijs Verhage<sup>1</sup> ([ORCID: 0000-0002-6085-7503](https://orcid.org/0000-0002-6085-7503)) †

### Affiliations

1. Department of Functional Genomics, Center for Neurogenomics and Cognitive Research (CNCR), Vrije Universiteit (VU) Amsterdam Amsterdam Netherlands ([ROR:008xxew50](https://ror.org/008xxew50))
2. Department of Molecular and Cellular Neurobiology, Center for Neurogenomics and Cognitive Research (CNCR), Vrije Universiteit (VU) Amsterdam Amsterdam Netherlands ([ROR:008xxew50](https://ror.org/008xxew50))
3. Department of Human Genetics, Center for Neurogenomics and Cognitive Research (CNCR), Amsterdam University Medical Center (UMC) Amsterdam Netherlands ([ROR:04dkp9463](https://ror.org/04dkp9463))

† Corresponding author

## Abstract

Tomosyn is a large, non-canonical SNARE protein proposed to act as an inhibitor of SNARE complex formation in the exocytosis of secretory vesicles. In the brain, tomosyn inhibits the fusion of synaptic vesicles (SVs), whereas its role in the fusion of neuropeptide-containing dense core vesicles (DCVs) is unknown. Here, we addressed this question using a new mouse model with a conditional deletion of tomosyn (Stxbp5) and its paralogue tomosyn-2 (Stxbp5l). We monitored DCV exocytosis at single vesicle resolution in tomosyn-deficient primary neurons using a validated pHluorin-based assay. Surprisingly, loss of tomosyns did not affect the number of DCV fusion events but resulted in a strong reduction of intracellular levels of DCV cargos, such as neuropeptide Y (NPY) and brain-derived neurotrophic factor (BDNF). BDNF levels were largely restored by re-expression of tomosyn but not by inhibition of lysosomal proteolysis. Tomosyn’s SNARE domain was dispensable for the rescue. The size of the trans-Golgi network and DCVs was decreased, and the speed of DCV cargo flux through Golgi was increased in tomosyn-deficient neurons, suggesting a role for tomosyns in DCV biogenesis. Additionally, tomosyn-deficient neurons showed impaired mRNA expression of some DCV cargos, which was not restored by re-expression of tomosyn and was also observed in Cre-expressing wild-type neurons not carrying loxP sites, suggesting a direct effect of Cre recombinase on neuronal transcription. Taken together, our findings argue against an inhibitory role of tomosyns in neuronal DCV exocytosis and suggests an evolutionary conserved function of tomosyns in the packaging of secretory cargo at the Golgi.

## Introduction

Brain activity relies on the precisely regulated secretion of different chemical messengers, and most neurons co-release multiple neurotransmitters (Nusbaum et al., 2017). Classical small-molecule neurotransmitters (e.g. glutamate, γ-aminobutyric acid) are released from SVs, whereas neuropeptides and neurotrophic factors are packaged in and secreted from DCVs. SV and DCV substantially differ in their morphology and mechanisms of formation (reviewed in De Camilli and Jahn, 1990; Gondré-Lewis et al., 2012). While SVs are loaded with their content directly at synapses, where they subsequently fuse with the presynaptic membrane, DCVs are formed in neuronal somas at the trans-Golgi network (TGN), from where they travel to the release sites that are not confined to synapses. Despite these and many other differences between the two main types of neuronal secretory vesicles, Ca2+-triggered exocytosis of both SV and DCV in most neurons requires an identical basic machinery consisting of SNARE proteins: syntaxin-1 and SNAP25 at the plasma membrane, and VAMP2 on the vesicle (Südhof, 2013; Shimojo et al., 2015; Arora et al., 2017; Hoogstraaten et al., 2020). The SNARE domains of these proteins form a tight complex that brings the two membranes together and drives vesicle fusion. In addition to the basic SNARE machinery, many other proteins participate in the fusion process (reviewed in Südhof, 2013; Rizo and Xu, 2015), of which some are differentially required for SV and DCV exocytosis (Persoon et al., 2019; Moro et al., 2021). The differences in molecular machinery may explain why SV and DCV exocytosis are triggered upon different stimulation paradigms and at different locations within neurons.

Tomosyn (STXBP5) is a large, evolutionary conserved SNARE protein discovered as an interactor of syntaxin-1 in rat brain (Fujita et al., 1998; Masuda et al., 1998). Tomosyn is expressed in a wide range of specialized secretory cell types, such as neurons, platelets, and neuroendocrine cells, suggesting a fundamental role of tomosyn in regulated secretion. Mammals express a second tomosyn gene, STXBP5L, which encodes tomosyn-2 with a nearly 80% amino acid similarity (Groffen et al., 2005). The two genes have a partially overlapping expression pattern in the mouse brain suggesting functional redundancy (Groffen et al., 2005; Barak et al., 2010). Mutations in both genes were found in patients with neurodevelopmental disorders, suggesting a role of tomosyns in human brain function (Matsunami et al., 2013; Cukier et al., 2014; De Rubeis et al., 2014; Kumar et al., 2015).

Tomosyn is comprised of a C-terminal SNARE domain and N-terminal WD40 repeats folded into two seven-bladed β-propellers. The SNARE-domain of tomosyn is homologous to the SNARE domain of VAMP2 and mediates binding to syntaxin-1 and SNAP25. The resulting complex is remarkably similar in structure and stability to the fusogenic complex of syntaxin-1/SNAP25 with VAMP2 (Pobbati et al., 2004). However, in contrast to VAMP2 and most other SNARE proteins, tomosyn does not contain a transmembrane anchor and, therefore, cannot drive membrane fusion. This feature led to a hypothesis that tomosyn functions as an inhibitor of fusion by competing with VAMP2 for binding to syntaxin-1/SNAP25 (Hatsuzawa et al., 2003). In support of this hypothesis, overexpression of tomosyn in neuroendocrine PC12 cells and adrenal chromaffin cells inhibits the fusion of secretory vesicles (Fujita et al., 1998; Hatsuzawa et al., 2003; Yizhar et al., 2004), and, conversely, loss of tomosyn in the nematode, fruit fly and mouse brain increases SV release probability and enhances synaptic transmission (Gracheva et al., 2006; McEwen et al., 2006; Chen et al., 2011; Sauvola et al., 2021; Sakisaka et al., 2008; Ben-Simon et al., 2015). In addition, loss of tomosyn in C. elegans augments neuropeptide secretion, as evidenced by decreased DCV abundance at synapses and increased accumulation of a DCV cargo in scavenger cells (Gracheva et al., 2007; Ch’ng et al., 2008). Together, these studies suggest an evolutionary conserved role of tomosyn as an inhibitor of secretory vesicle exocytosis.

However, several lines of evidence argue against this conclusion. First, rat sympathetic neurons show a decrease in neurotransmitter release from SV upon depletion of tomosyn (Baba et al., 2005). Second, platelets from Stxbp5-null mice show severely reduced exocytosis of all types of secretory granules, which results in excessive bleeding and impaired thrombus formation in vivo (Zhu et al., 2014; Ye et al., 2014). Finally, the loss of SRO7 and SRO77, two yeast orthologs of mammalian tomosyns, causes a strong defect in the exocytosis of post-Golgi vesicles (Lehman et al., 1999). Collectively, these studies suggest a positive role of tomosyn and its yeast orthologs in exocytosis. Thus, despite the clear importance of tomosyn in regulated secretion, its role in this process remains controversial.

In the brain, the role of mammalian tomosyn has been studied with a focus on SV exocytosis, whereas its effect on DCV exocytosis is unknown. In this study, we addressed this question using a mouse model with the inducible loss of all tomosyn and tomosyn-2 isoforms and show that tomosyns do not affect neuronal DCV exocytosis but, paradoxically, regulate intracellular levels of overexpressed and endogenous secretory cargos. Thus, tomosyns differentially modulate two regulated secretory pathways in neurons (secretion from SVs and DCVs) and have an additional role in the regulation of DCV composition.

## Results

To explore the role of tomosyn in neuronal secretion, we generated a new mouse model with a conditional deletion of tomosyn (Stxbp5) and tomosyn-2 (Stxbp5l) (Figure 1—figure supplement 1A). Primary hippocampal neurons isolated from these mice showed a complete loss of tomosyns expression when transduced with a lentivirus encoding Cre-recombinase, as shown by Western blot (WB) and immunocytochemistry (ICC) (Figure 1—figure supplement 1B–C). As a control, we used neurons isolated from the same litter but expressing a defective Cre-recombinase that lacks the catalytic domain (ΔCre). Double knockout (DKO) neurons developed normally in culture and did not show any defects in neurite outgrowth and synapse formation as evidenced by normal dendrite length and density of synaptophysin puncta (Figure 1—figure supplement 1D–G).

To examine DCV fusion, we used a modification of a validated reporter consisting of NPY fused to super-ecliptic pHluorin (Figure 1A, Figure 1—figure supplement 2; Persoon et al., 2018; Nassal et al., 2022). When expressed in primary neurons, this reporter localized almost exclusively to DCVs, as indicated by its co-localization with endogenous DCV markers IA-2 and chromogranins (CHGA, CHGB) (Figure 1—figure supplement 2). Fusion of labeled DCVs with the plasma membrane was stimulated by repetitive bursts of action potentials delivered at 50 Hz to single neurons grown on glial micro-islands. Individual fusion events were detected as transient increases in fluorescence intensity along neurites, as exemplified in Figure 1B. Our stimulation paradigm resulted in a steep accumulation of fusion events that plateaued shortly before the end of the stimulation (Figure 1C). Most of these events (∼80%) were previously shown to be of axonal origin (Persoon et al., 2018). Virtually no fusion events were detected in neurons of both genotypes in the absence of electric stimulation (first 30 s of recordings or in the period after stimulation). Surprisingly, the total number of evoked fusion events was similar between control and DKO neurons, with a tendency (p=0.09) towards a decrease in DKO neurons (Figure 1D). The intracellular pool of the DCV reporter, visualized by a short application of 50 mM NH4Cl to neurons to dequench intravesicular NPY-pHluorin, was decreased by 28% in DKO neurons (Figure 1E). The released fraction, i.e., the number of fusion events normalized to the intracellular pool of vesicles, was nearly identical between the genotypes and comprised approximately 8% of the intracellular content, consistent with the results of our previous studies (Persoon et al., 2018; Moro et al., 2020; Figure 1F). Also, the averaged fluorescence peak of individual fusion events, an estimate of NPY loading per vesicle, was not affected by the loss of tomosyns (Figure 1G). Thus, tomosyns are dispensable for the evoked fusion of neuronal DCVs in hippocampal neurons.

![Figure 1.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig1-v1.jpg)

**Figure 1.:** (A) Experimental strategy for measuring DCV fusion in single isolated neurons. (B) Exemplified fluorescence intensity trace of a neuronal DCV fusion event evoked by electric stimulation (shown as blue bars). Stimulation paradigm consisted of 16 bursts of 50 pulses (‘AP’) delivered at 50 Hz. Transient increase in relative fluorescence intensity (F/F0) indicates a fusion event during the stimulation. At the end of a recording session, neurons were flushed with 50 mM NH4Cl to visualize not fused DCVs. (C) Cumulative count of fusion events detected per single neuron. Data are shown as mean ± SEM and were analyzed by two-way ANOVA. n=34–36 neurons/genotype from three culture preparations. (D) Total count of fusion events detected per single neuron. Data are shown as violin plots with median (dashed line) and quartiles (dotted lines) and analyzed using the Mann-Whitney test. (E) Intracellular pool of pHluorin-labeled DCVs determined by application of 50 mM NH4Cl after the stimulation. Data are shown as violin plots with median (dashed line) and quartiles (dotted lines) and analyzed using a two-tailed unpaired t-test. *p<0.05. (F) Cumulative count of fusion events normalized to the intracellular pool of DCVs (released fraction). Data are shown as mean ± SEM and were analyzed by two-way ANOVA. (G) Peak in fluorescence intensity that results from a single fusion event (averaged per neuron). Data are shown as violin plots with median (dashed line) and quartiles (dotted lines) and analyzed using the Mann-Whitney test. ns: not significant. (H) Levels of syntaxin-1 containing SDS-resistant 80 kDa SNARE complexes are unchanged in Double knockout (DKO) neurons. Boiled and non-boiled lysates were subjected to SDS-PAGE and membranes were probed with an antibody against syntaxin-1 (STX1). Temperature-sensitive complexes were detected at 80 kDa (synaptic SNARE complex) and 200 kDa (possibly complex of syntaxin-1 and SNAP25 with tomosyn). Smear at >80 kDa represents complex multimers. Band intensities in DKO were normalized to the control, plotted as mean ± SD, and analyzed using a one-sample t-test. Dots represent independent culture preparations (n=4). ns: not significant; ***p<0.001.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Schematic depiction of mouse Stxbp5 (encoding tomosyn) and Stxbp5l (encoding tomosyn-2) genes with exons as vertical lines and introns as bridging gaps. To generate conditional double knockout (DKO) of Stxbp5/5 l, exon 2 of Stxbp5, and exon 3 of Stxbp5l were flanked with Lox2272 and LoxP sites, respectively (shown as triangles). Expression of Cre-recombinase results in the excision of the flanked exons in both genes, predicted to cause frameshift mutations and nonsense-mediated mRNA decay of gene transcripts. Proportional gene graphics were made using Exon-Intron Graphic Maker developed by Nikhil Bhatla. (B) Western blot showing loss of tomosyn and tomosyn-2 expression in Cre-expressing primary hippocampal neurons (‘DKO‘). As a control, neurons expressing Cre lacking the DNA-binding domain (ΔCre) were used. Arrow indicates tomosyn, which is flanked by two unspecific bands. Numbers on the left indicate the approximate molecular weight of the bands in kDa. (C) Immunostaining of tomosyn and MAP2 showing loss of tomosyn expression in DKO neurons. Scale bar 20 µm. (D) Example cropped images of control and DKO neurons immunostained for the synaptic marker synaptophysin (‘SYP’) showing normal synapse number and distribution in the DKO neurons (quantified in E-G). Scale bar 20 µm. (E) Total length of MAP2-positive neurites per single neuron. (F) Number of synaptophysin puncta normalized to the length of MAP2-positive neurites. (G) Mean intensity of synaptophysin signal on MAP2-positive neurites. Data in E-G are shown as mean ± SD and were analyzed using a two-tailed unpaired t-test. n=28–30 neurons/genotype. ns: not significant.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) DCV fusion reporter used in this study is based on the human pre-pro-NPY (NPY precursor), which structure is shown in the upper panel with processing sites depicted as scissors. In the DCV fusion reporter, the C-flanking peptide (aa 64–97) was replaced by super-ecliptic pHluorin. (B) DCV fusion reporter localizes to endogenous DCVs in cultured neurons, as shown by co-localization of pre-NPY-pHluorin with the endogenous DCV markers IA-2, chromogranin A (CHGA), and chromogranin B (CHGB). White frames indicate zoomed areas used to generate intensity profiles shown on the right. Scale bar 20 µm.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A) and (B) Results of the SDS-PAGE on boiled and non-boiled lysates of control and DKO cultures. Membranes were probed with antibodies against SNAP25 (A) and VAMP2 (B). Temperature-sensitive complexes were detected at 80 kDa. Additionally, a 200 kDa band was detected in non-boiled lysates of control, but not DKO neurons, with the anti-SNAP25 antibody. Band intensities in DKO were normalized to the control, plotted as mean ± SD, and analyzed using a one-sample t-test. Dots represent independent culture preparations (n=4). ns: not significant; ***p<0.001. (C) Loss of VAMP2 due to overexpression (OE) of tetanus-toxin light chain (TeNT) results in the shift of the 80 kDa band detected with the antibody against syntaxin-1 in non-boiled lysates, indicating that the 80 kDa band represents a complex of syntaxin-1 with VAMP2.

Tomosyn was proposed to act as an inhibitor of vesicle fusion by competing with VAMP2 for the binding to syntaxin-1 and SNAP25. Hence, loss of tomosyns may result in the increased formation of ternary synaptic SNARE complexes consisting of syntaxin-1, SNAP25, and VAMP2. These complexes can be detected based on their resistance to SDS, as was shown for tomosyn-deficient fly brains (Sauvola et al., 2021). We examined levels of the assembled complexes in DKO neurons by SDS-PAGE on non-boiled neuronal lysates, since SDS-resistant complexes disassemble at temperatures higher than 60 °C (Hayashi et al., 1994; Otto et al., 1997; Figure 1H). As expected, a band of approximately 80 kDa that corresponds to the ternary complexes was readily detected with a syntaxin-1 antibody in non-boiled lysates and absent in lysates heated at 95 °C. This band shifted in size upon expression of tetanus toxin light chain (TeNT), which results in cleavage of VAMP2, thus confirming that the detected complexes contain VAMP2 (Figure 1—figure supplement 3C). No difference in the intensity of the 80 kDa band was observed between control and DKO cultures. The same results were obtained when non-boiled lysates were probed with antibodies against SNAP25 and VAMP2 (Figure 1—figure supplement 3A–B). These data suggest that tomosyns do not interfere with the bulk formation of syntaxin-1 containing synaptic SNARE complexes in cultured neurons. Interestingly, in addition to the 80 kDa band, non-boiled WT lysates showed a band of approximately 200 kDa, detected with antibodies against syntaxin-1 and SNAP25. This band was absent in DKO lysates and, therefore, likely represents a complex of tomosyn with syntaxin-1 and SNAP25, suggesting that this complex is resistant to SDS in vivo. This 200 kDa complex was also detected in control neurons with an antibody against tomosyn (Figure 1H).

Despite normal DCV exocytosis, intracellular levels of the DCV reporter were decreased in DKO neurons (Figure 1E). This decrease was also observed in tetrodotoxin (TTX)-silenced network cultures of DKO neurons that were not subjected to electric stimulation (Figure 2A–B). Activity of the synapsin promoter used to drive expression of the DCV reporter was not significantly altered in DKO neurons, as shown by normal expression of enhanced green fluorescent protein (EGFP) from the same promoter (Figure 2—figure supplement 1). Re-expression of the most ubiquitous tomosyn isoform (m-isoform of Stxbp5) restored levels of the overexpressed NPY-pHluorin in DKO neurons (Figure 2A–B). These data suggest that tomosyns affect the amount of the overexpressed DCV cargo and/or the number of DCVs in hippocampal neurons.

![Figure 2.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig2-v1.jpg)

**Figure 2.:** (A) Representative images of the DCV reporter (NPY-pHluorin) in control, double knockout (DKO), and DKO re-expressing tomosyn (Stxbp5 isoform m, ‘Rescue’) neurons. Neurons were grown in mass cultures, silenced with sodium channel blocker tetrodotoxin (TTX, 1 µM) for 48 hr, and fixed on DIV14. White boxes indicate zoomed-in segments of neurites shown under every image. Scale bar 20 µm. (B) Mean intensity of NPY-pHluorin and tomosyn immunostaining in control, DKO, and rescued neurons exemplified in (A). Data were analyzed using one-way ANOVA with Tukey’s multiple comparisons post hoc test. n=29–30 neurons (plotted as dots)/ genotype. ****p<0.0001. (C) Representative images of BDNF immunostaining in control, DKO, and DKO re-expressing tomosyn neurons. Neurons were grown on glial microislands and fixed on DIV16. White boxes indicate zoomed-in segments of neurites shown under every image. Scale bar 20 µm. (D) Quantification of the mean BDNF and tomosyn intensity in control, DKO and rescued neurons exemplified in (C). Data were analyzed using the Kruskal-Wallis test with Dunn’s multiple comparisons post hoc test (BDNF) and one-way ANOVA with Tukey’s multiple comparisons post hoc test (tomosyn). n=20 neurons (plotted as dots)/ genotype. ****p<0.0001. (E) BDNF levels as detected by western blot (WB) in lysates of control and DKO neuronal cultures. Equal loading was verified by immunodetection of GAPDH. (F) Quantification of the BDNF band intensity from WB exemplified in (E). BDNF levels in DKO neurons were normalized to control levels in the corresponding culture. DKO data are plotted as mean ± SD and were analyzed using one-sample t-test. n=8 samples/genotype from four culture preparations. ****p<0.0001. (G) Re-expression of tomosyn (either full length, ‘FL,’ or a truncated mutant lacking the SNARE domain, ‘ΔSNARE’) partially restores BDNF levels in DKO neurons as detected by WB. Same WB shows that an inhibition of lysosomal proteolysis by leupeptin (50 μM for 24 hr) does not equalize BDNF levels between control and DKO neurons. Immunodetection of tomosyn was used to validate the expression and the correct size of the rescue constructs. Equal loading was verified by immunodetection of GAPDH. (H) Quantification of the BDNF band intensity from WB exemplified in (G). BDNF levels in DKO neurons are shown as the mean % of control levels. Data were analyzed using one-sample t-test comparing to 100% (control levels). n=4 samples/genotype from two culture preparations. ***p<0.001. (I) Quantification of the BDNF band intensity in leupeptin-treated samples from WB exemplified in (G). BDNF levels in all groups are shown as % of the averaged vehicle-treated control levels. Bars indicate mean values. Data were analyzed using a two-way repeated measures ANOVA. n=4 samples/genotype from two culture preparations.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Representative images of EGFP expressed under the control of synapsin promoter in fixed control and DKO neurons. Scale bar 20 µm. (B) Quantification of the mean EGFP intensity in control and DKO neurons from confocal microscopy images as exemplified in (A). Data are shown as mean ± SD and were analyzed using a two-tailed unpaired t-test. N=28–30 neurons/genotype. Ns: not significant.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) Representative images of the IA-2 immunostaining in control and DKO neurons. Neurons were grown in mass cultures, silenced with sodium channel blocker tetrodotoxin (TTX, 1 µM) for 48 hr, and fixed on DIV14. White boxes indicate zoomed-in segments of neurites shown under every image. Scale bar 20 µm. (B) Quantification of the mean IA-2 intensity in control and DKO neurons from images exemplified in (A). Data are shown as mean ± SD and were analyzed using a two-tailed unpaired t-test. n=24 neurons/genotype. *p<0.05; ****p<0.0001. (C) Levels of IA-2 as detected by WB in control and DKO neuronal lysates. Proteolytically processed (mature) form of IA-2 was detected at 65 kDa. Equal loading was verified by the detection of total protein stained with trichloroethanol (TCE) and by immunodetection of actin. Amount of mature IA-2 in DKO neurons was normalized to control levels in the corresponding culture. DKO data are presented as mean ± SD and were analyzed using one sample t-test. n=9 samples/genotype from three culture preparations. ****p<0.0001.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (A) Representative images of LAMP1 immunostaining in DIV14 neurons. Scale bar 20 µm. (B) Quantification of the mean LAMP1 intensity in control and double knockout (DKO) neurons from confocal microscopy images as exemplified in (A). Data are shown as mean ± SD and were analyzed using a two-tailed unpaired t-test. n=10 neurons/genotype. ns: not significant. (C) Levels of LAMP1 and LIMP2 as detected by western blot (WB) are normal in DKO neurons. Equal loading was verified by immunodetection of actin. (D) Quantification of LAMP1 and LIMP2 signal from WB images exemplified in (C). Levels of LAMP1 and LIMP2 in DKO were normalized to control levels in the corresponding culture. DKO data are presented as mean ± SD and were analyzed using one sample t-test. n=9 samples/genotype from three culture preparations. ns: not significant.

We next examined if endogenous DCV cargos are also affected by the loss of tomosyns. Levels of BDNF, one of the most common DCV cargos in excitatory hippocampal neurons (Dieni et al., 2012), were decreased by more than half in DKO neurons as shown by ICC and WB analysis (Figure 2C–F). Levels of IA-2 (PTPRN), a transmembrane DCV-resident protein commonly used as a DCV marker, were also lower, by 25%, in DKO neurons as indicated by ICC, and by approximately 50% as evidenced by WB analysis, which allows to distinguish a proteolytically processed (mature) form of IA-2 that runs at approximately 65 kDa (Hermel et al., 1999; Figure 2—figure supplement 2). The cellular distribution of the two DCV markers was similar between the genotypes, with a comparable reduction in somas and neurites of DKO neurons and no re-distribution between the two compartments as detected by ICC. Markers of lysosomes/late endosomes, LAMP1, and LIMP2, were not affected by the loss of tomosyns, as shown by ICC and WB (Figure 2—figure supplement 3). Re-expression of tomosyn (isoform 1 m, NM_001081344) largely restored BDNF levels in DKO neurons (to approximately 80% of WT levels), as shown by ICC and WB (Figure 2C–D and G–H). The SNARE-domain of tomosyn was dispensable for the partial rescue of BDNF levels, since expression of a truncated tomosyn mutant lacking the SNARE-domain (ΔSN) rescued BDNF levels in DKO to the same extent as re-expression of the full-length (FL) tomosyn (Figure 2G–H). Taken together, these data suggest that tomosyns affect intracellular levels of some endogenous DCV cargos in a SNARE-domain independent manner.

Levels of BDNF and other secretory cargos are known to be regulated by lysosomal degradation. We, therefore, tested if an increase in BDNF degradation could account for its decreased levels in the absence of tomosyns. Inhibition of lysosomal proteases by leupeptin for 24 hr resulted in a twofold increase of BDNF levels in neurons of both genotypes but failed to raise BDNF expression in DKO to WT levels (Figure 2G and I), indicating that increased cargo degradation does not explain the decreased BDNF levels in DKO neurons.

We next asked whether levels of any other (secretory) proteins are affected by the loss of tomosyns. To address this question in an unbiased manner, we compared the proteome of cultured control and DKO neurons by mass spectrometry. We detected approximately 8500 proteins, of which around 3% were differentially expressed (log2 fold change threshold 0.3) (Figure 3A). Gene ontology (GO) analysis of proteins decreased in DKO neurons indicating a strong enrichment of proteins related to the cytoskeleton and secretory granules (Figure 3B). As expected, both tomosyns were not detected in DKO neurons (Figure 3C). Interestingly, BDNF was also barely detected in DKO (only in one out of six biological replicates), while readily detected across all replicates in control conditions (Figure 3C), confirming a strong decrease in BDNF levels in DKO neurons. Many common DCV cargos, such as granins VGF and SCG2, cargo processing enzymes PCSK1 and CPE, and transmembrane DCV proteins IA-2 (PTPRN) and PAM were also decreased, albeit to a different extent, in DKO (Figure 3D). Most of the up-regulated proteins were components of the mitochondrial electron transport chain, suggesting that an increase in oxidative phosphorylation is a metabolic feature of DKO neurons (Figure 3B and D, Supplementary file 1). In contrast to the proteins regulating oxidative phosphorylation, most other mitochondrial proteins, for example, proteins responsible for mitochondrial DNA replication and transcription, were unchanged in DKO. A selected number of synaptic proteins were affected in DKO neurons but, in contrast to the DCV-resident proteins, SV proteins did not follow any general trend in DKO neurons: while some proteins (glutamate transporter VGLUT2, glutamate decarboxylase GAD67) were strongly increased in DKO, others (e.g. SYT12 and SV2B) were reduced to a similar extent, and many (e.g. main glutamate transporter VGLUT1, vesicular GABA transporter VGAT) were not significantly altered (Figure 3D). In conclusion, Cre-mediated loss of both tomosyns leads to selective changes in neuronal proteome with a reduction in cytoskeletal and DCV cargo proteins, an increase in mitochondrial proteins driving oxidative respiration, and a re-arrangement of synaptic proteome.

![Figure 3.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig3-v1.jpg)

**Figure 3.:** (A) Volcano plot showing results of the differential expression analysis of control and DKO proteome. Gray lines indicate chosen thresholds for log2 fold change (0.3) and false discovery (FDR) adjusted p-value (0.01). Proteins decreased or increased in DKO are shown in blue and red, respectively. (B) Enriched gene ontology (GO cellular component) terms of the proteins significantly affected in DKO neurons as analyzed by ShinyGO v0.75 (http://bioinformatics.sdstate.edu/go/) with the FDR-adjusted p-value cutoff ≤0.05. (C) List of proteins reliably detected in one of the genotypes only and, therefore, not included in the differential expression analysis shown in (A). Proteins are sorted by the z-score, which reflects the total number of peptides detected per genotype. (D) Examples of proteins that are significantly affected in DKO neurons grouped by subcellular compartment. Heat maps show the degree of down- or upregulation in the DKO.

Next, we examined the ultrastructural morphology of DCVs in DKO and control neurons by electron microscopy (Figure 4). We found DCVs with normal dense cores sparsely distributed among neurites in neurons of both genotypes. Most presynaptic sections did not contain any DCVs, in line with previous reports (Sorra et al., 2006; Persoon et al., 2018). Percent of synaptic sections containing one or several DCVs was decreased in DKO by 30% (12% of all synaptic sections in DKO versus 17% in control), indicating lowered DCV abundancy in DKO. In addition, DCVs in DKO neurons were slightly reduced in diameter (average 65.01±2.08 nm in DKO versus 71.52±1.62 nm in control), with a high proportion of DKO DCVs being only 40–50 nm in diameter (16% of all DCVs in DKO versus 4% in control) (Figure 4A–B). Such a reduction in diameter translates to an approximately 25% decrease in volume. In contrast, the diameter of SV was not affected by the loss of tomosyns (Figure 4D–E). Other parameters of synaptic ultrastructure, such as SV number per synapse, length of the active zone, and length of postsynaptic density, were also unchanged in DKO neurons (Figure 4D and F–H) and DKO somata showed no obvious abnormalities in organelle morphology (Figure 4D). Hence, loss of tomosyns leads to a reduction in DCV size and abundancy, without affecting ultrastructure and the number of SVs.

![Figure 4.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig4-v1.jpg)

**Figure 4.:** (A) Example EM images show the normal appearance of DCVs with a typical dense core in double knockout (DKO) neurons. Scale bar 100 nm. (B) DCV diameter is reduced in DKO neurons, as quantified from EM images exemplified in (A). Data are shown as a SuperPlot, where averages from three independent cultures (biological replicates) are shown as large circles and single observations (DCV profiles) as dots. Data from each culture are shown in a different color. Horizontal bars represent the means of the averages from the three cultures, which were compared using a two-tailed unpaired t-test. Error bars are SD. Number of DCV profiles analyzed: 135 (control) and 64 (DKO). *p<0.05. (C) Frequency distribution of DCVs by diameter is skewed to the left in DKO neurons, indicating a higher proportion of smaller DCVs in DKO neurons than in control. (D) Example EM images show normal ultrastructure of synapses and other cellular organelles in DKO neurons. Golgi cisternae and selected mitochondria are labeled with 'G' and 'M,' respectively. Scale bar 100 nm. (E–H) Quantification of SV diameter, SV number per synapse, length of the active zone, and length of postsynaptic density (PSD) from EM images exemplified in (D). Data are shown as SuperPlots and analyzed as described in (B). Number of individual observations: 617–621 SV profiles (E) and 148–152 synapses (F–H). ns: not significant.

The fact that the abundancy, composition, and size of neuronal DCVs are affected in DKO neurons suggests that tomosyns may regulate DCV biogenesis. DCVs are formed at the TGN in a sequence of membrane fusion/fission events ensuring correct packaging and processing of DCV cargos. We found that tomosyn was enriched at the TGN of cultured hippocampal neurons, as evidenced by the partial colocalization with a TGN marker, TGN38 (Figure 5—figure supplement 1A–B). As reported previously, tomosyn also colocalized with mature DCVs and showed an enrichment at the synapses (Figure 5—figure supplement 1C–F; Geerts et al., 2017), although colocalization of tomosyn with the DCV marker IA-2 was less extensive than with the synaptic marker synaptophysin, possibly due to the fact that IA-2 is also present in endosomes (Solimena et al., 1996). The TGN area, visualized by immunostaining of the TGN marker TMEM87A, was slightly decreased in DKO neurons as compared to controls, suggesting a functional importance of tomosyn at the Golgi (Figure 5A–B).

![Figure 5.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig5-v1.jpg)

**Figure 5.:** (A) Trans-Golgi network (TGN) area is decreased in double knockout (DKO) neurons. Representative images of immunostained TGN marker, TMEM87A (shown in cyan). Nuclei are labeled in red due to the expression of mCherry-tagged Cre or ΔCre. Scale bar 20 µm. (B) Quantification of the area of the TGN and nuclei from confocal microscopy images exemplified in (A). Data are shown as mean ± SD and were analyzed using a two-tailed unpaired t-test. n=39–40 neurons/ genotype. ***p<0.001; ns: not significant. (C) Design of the construct for the Retention Using Selective Hooks (RUSH) assay. As a DCV cargo, human pre-pro-NPY fused to streptavidin-binding peptide (SBP) and enhanced green fluorescent protein (EGFP) was used. The cargo was immobilized at the endoplasmic reticulum (ER) due to interaction with the ER hook, consisting of streptavidin fused to the ER-retention/retrieval signal KDEL. (D) Scheme illustrating synchronized trafficking of a DCV cargo through the secretory pathway upon the addition of biotin in the RUSH assay. (E) Snapshots of time-lapse videos taken after the addition of biotin in the RUSH assay. Time passed after the addition of biotin is shown on top. DCV cargo passes through the Golgi in roughly 45 min after the addition of biotin and gets concentrated in fine puncta that eventually leave cell soma. Scale bar 20 µm. (F) NPY-EGFP intensity in the Golgi area plotted against time after the addition of biotin. Intensity values were normalized to the basal levels (before the addition of biotin). Data are shown as mean ± SEM and were analyzed by two-way ANOVA. n=30–34 neurons/genotype. (G) Time required to reach maximum NPY-EGFP intensity at the Golgi, quantified from (F), is reduced in DKO. Data are shown as mean ± SD and were analyzed by a two-tailed unpaired t-test. *p<0.05. (H) Speed of NPY-EGFP export from the Golgi is increased in DKO neurons. Rate constants were calculated from first-order decay curves fitted to the data shown in (F). Data are shown as mean ± SD and were analyzed by a two-tailed unpaired t-test. *p<0.05. (I) Snapshots of time-lapse videos taken 90 min after the addition of biotin in the RUSH assay with the focus on neurites, where newly made DCVs trafficked after exit from the Golgi. (J) Proportion of newly made DCVs trafficking in anterograde and retrograde directions as quantified from the time-lapse videos exemplified in (I). Majority of vesicles are trafficked anterogradely in neurons of both genotypes. Data are shown as mean ± SD and were analyzed by a two-tailed unpaired t-test. n=12 neurons/genotype. ns: not significant. (K) Speed of anterogradely trafficking vesicles as quantified from the time-lapse videos exemplified in (I). Data are shown as mean ± SD and were analyzed by a two-tailed unpaired t-test. n=12 neurons/genotype. ns: not significant.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) Example confocal microscopy images showing partial co-localization of tomosyn with the TGN marker, TGN38. Scale bar 20 µm. (B) Intensity profile generated from the yellow line indicated in (A) showing partial colocalization of tomosyn and TGN38. (C) Example confocal microscopy images showing partial co-localization of tomosyn with the DCV marker, IA-2. Scale bar 10 µm. (D) Example confocal microscopy images showing partial co-localization of tomosyn with the synapse marker, synaptophysin (SYPH). Scale bar 10 µm. (E) Intensity profile generated from the neurite imaged in (C) showing partial colocalization of tomosyn and IA-2. (F) Intensity profile generated from the neurite imaged in (D) showing partial colocalization of tomosyn and synaptophysin (SYPH).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** Example confocal microscopy images showing co-localization of NPY-EGFP-SBP with CHGA. Scale bar 5 µm.

We next tested whether tomosyn regulates the packaging and export of a neuropeptide cargo from the TGN using a modification of the Retention Using the Selective Hooks (RUSH) method (Boncompain et al., 2012). In this method, streptavidin-binding peptide (SBP)-tagged secretory cargo is retained in the endoplasmic reticulum (ER) until the addition of biotin due to the expression of the ER-localized streptavidin. Biotin disrupts SBP/streptavidin interaction and induces a synchronized transport of the cargo from the ER along the secretory pathway (Figure 5C–D). As a neuropeptide cargo, we used NPY fused to SBP and EGFP, as described previously (Emperador-Melero et al., 2018). In the absence of biotin, NPY-EGFP-SBP was diffusely distributed along cell soma and processes, in agreement with its localization to the ER. Addition of biotin induced a wave of NPY-EGFP-SBP accumulating in the Golgi first, and then leaving the Golgi as discrete puncta (Figure 5E, Figure 5—video 1). These puncta co-localized with an endogenous DCV marker, CHGA, indicating correct packaging of the NPY fusion protein into DCVs during the RUSH assay (Figure 5—figure supplement 2). Formation of such puncta and clearance of NPY-EGFP-SBP from the Golgi was observed in neurons of both genotypes. We next compared the speed of NPY-EGFP-SBP flux through the Golgi by plotting EGFP intensity within the Golgi area over time (Figure 5F). The peak of fluorescence intensity in the Golgi was reached 5.6 min faster in DKO than in control, indicating that the speed of Golgi filling is increased in DKO (Figure 5G). The speed of Golgi clearance – determined by fitting a first order exponential decay curve to the data after the peak – was also increased (by 20%) in DKO neurons (Figure 5H). Thus, loss of tomosyns does not impede export of the overexpressed neuropeptide cargo from Golgi but, conversely, accelerates it.

We also traced the fate of newly made RUSH vesicles 90 min after the addition of biotin. After the exit from Golgi, these vesicles traveled predominantly in one neurite, morphologically identified as the axon (Figure 5I). Most axonal vesicles (67%) traveled in the anterograde direction with a similar speed in neurons of both genotypes (Figure 5J–K), indicating that the transport of newly made DCVs is not affected by the loss of tomosyns.

We then asked if the loss of tomosyns affected mRNA expression of secretory cargos that were significantly decreased in DKO as evidenced by mass spectrometry and WB analysis. We detected a decrease in the expression of various transcript variants of Bdnf (Figure 6A) and other common DCV cargos, most prominently Vgf and Pcsk1, encoding a prohormone convertase (Figure 6B). Interestingly, the decrease in mRNA was less pronounced than the decrease at the protein level, as detected by WB (for BDNF) or mass spectrometry (for VGF and PCSK1) (Figure 6—figure supplement 1). The number of neuropeptides was decreased at the mRNA level in DKO as well (Figure 6C). Grp (gastrin related peptide) and Pnoc (nociceptin, nocistatin) showed the strongest reduction (by 50% and 35%, respectively), while mRNA of genes encoding cholecystokinin, NPY, and tachykinins displayed a reduction by around 30%. It is not clear whether any of these peptides were also decreased at the protein level, since most processed neuropeptides could not be detected in our mass spectrometry-based proteomics analysis due to their small size. Based on single-cell transcriptomics data (Saunders et al., 2018), expression of the affected genes was not confined to a specific neuronal population (e.g. glutamatergic or GABAergic neurons). Strikingly, re-expression of tomosyn (isoform 1 m) from DIV2 onwards did not restore altered transcription of the affected genes, suggesting that tomosyn does not mediate these changes (Figure 6D). Since no annotated genes and functional elements, other than Stxbp5 and Stxbp5l, were predicted to be affected by recombination of the Stxbp5 /Stxbp5 l loci in our mouse model, we tested whether the expression of Cre recombinase per se results in the detected transcriptional defects. Indeed, Cre expression in wild-type neurons not bearing introduced loxP sites led to a decrease in the mRNA expression of Bdnf, Vgf, Pcsk1, and Grp when compared to ΔCre-expressing wild-type neurons, with the size effect comparable to the one observed in Stxbp5/5llox neurons (Figure 6E). Expression of Gapdh, used as housekeeping gene control, was not affected by Cre. Thus, changes in DCV cargos transcription detected in DKO neurons are caused by direct effects of Cre expression, rather than by loss of tomosyns.

![Figure 6.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig6-v1.jpg)

**Figure 6.:** (A) mRNA levels of different Bdnf transcript isoforms as assessed by quantitative RT-PCR and normalized to Gapdh. Data are shown as fold changes (FC) relative to control levels in the corresponding culture preparation. n=8 culture preparations/genotype. Dots represent individual cultures, bar graphs are geometric means, and error bars are geometric SD. Log2FC (ΔΔCt) were analyzed by one-sample t-test. **p<0.01; ***p<0.001; ****p<0.0001. (B) mRNA levels of general DCV cargos as assessed by quantitative RT-PCR and normalized to Gapdh. Data are shown and analyzed as described in (A). *p<0.05; **p<0.01; ***p<0.001. (C) mRNA levels of most abundant hippocampal neuropeptides as assessed by quantitative RT-PCR and normalized to Gapdh. Neuropeptides are sorted by their abundance in hippocampal neurons. Data are shown and analyzed as described in (A). *p<0.05; **p<0.01; ***p<0.001, ns: not significant. (D) Re-expression of tomosyn does not restore mRNA expression of DCV cargos in DKO neurons. mRNA levels of Bdnf, Vgf, Pcsk1, and Grp were normalized to Gapdh and plotted as described in (A). Comparison between DKO and DKO re-expressing tomosyn (DKO +tom) is performed using a two-tailed paired t-test on Log2FC (ΔΔCt). n=3 culture preparations/ genotype. ns: not significant. (E) Expression of Cre-recombinase in wild-type (WT) neurons results in the decreased mRNA expression of DCV cargos. Effects of Cre on Stxbp5/5llox neurons are shown for the direct comparison. mRNA levels of the DCV cargos were normalized to Gapdh and plotted as fold changes (FC) relative to ΔCre. Comparisons between ΔCre and Cre conditions in each genotype were performed using a two-tailed paired t-test. n=8 culture preparations/genotype. *p<0.05; **p<0.01. (F) brain-derived neurotrophic factor (BDNF) and tomosyn levels as detected by western blot (WB) in lysates of ΔCre-mCherry and Cre-mCherry-expressing wild-type neurons. mCherry expression was used as a control. Equal loading was verified by immunodetection of GAPDH. (G) Quantification of BDNF and tomosyn bands intensity from WB exemplified in (F). BDNF and tomosyn levels in (Δ)Cre-expressing wild-type neurons are shown as mean % of control (mCherry-expressing neurons). Error bars represent SD. Data were analyzed using a two-tailed paired t-test. n=3 samples/ genotype. *p<0.05.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Data are shown as mean log2FC. mRNA expression was analyzed by quantitative RT-PCR analysis, as described in Figure 6A–B. Protein levels of BDNF were analyzed by western blot (WB) shown in Figure 2E. Protein levels of VGF and PCSK1 were analyzed by mass spectrometry (Figure 3). Description of the analyses is provided in the corresponding figures.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/85561/elife-85561-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** (A) Representative images of NPY-pHluorin in ΔCre- and Cre-expressing neurons. Neurons were grown in mass cultures, silenced with sodium channel blocker tetrodotoxin (TTX, 1 µM) for 48 hr, and fixed on DIV14. White boxes indicate zoomed-in segments of neurites shown under every image. Scale bar 20 μm. (B) Mean intensity of NPY-pHluorin and tomosyn immunostaining in ΔCre- and Cre-expressing neurons exemplified in (A). Data are shown as mean ± SD and were analyzed using a two-tailed unpaired t-test. n=18 neurons (plotted as dots)/ genotype. ns: not significant.

We next asked whether this effect of Cre expression contributes to the decrease of DCV cargos in DKO at the protein level. Lentivirus-mediated expression of Cre in wild-type neurons resulted in a decrease of BDNF levels by 26% (Figure 6F–G), as compared to >50% reduction in BDNF documented in DKO (Cre-expressing Stxbp5/5llox) neurons (Figure 2E–F). Expression of ΔCre that lacks the catalytic domain did not affect BDNF levels when compared to wild-type neurons expressing mCherry under the same promoter (Figure 6F–G), suggesting that recombinase activity is necessary for the effect of Cre on BDNF levels. Cre expression in wild-type neurons did not affect tomosyn levels. These data indicate that unspecific Cre recombinase activity contributes to the reduction in BDNF protein levels in DKO neurons, but to a lesser extent than the loss of tomosyns. In line with this conclusion, BDNF protein levels in DKO were largely rescued by the re-expression of tomosyn (Figure 2C–D and G–H).

To test if the latter conclusion also applies to a DCV reporter overexpressed under the control of a synapsin promoter, we tested the effects of Cre on the levels of NPY-pHluorin. Cre expression in wild-type neurons did not affect levels of NPY-pHluorin as shown by ICC (Figure 6—figure supplement 1), while the same reporter showed an approximately 20% reduction upon expression of Cre in Stxbp5/5llox neurons that was rescued by re-expression of tomosyn (Figure 2A–B). Thus, while Cre expression impairs transcription of endogenous DCV cargos in both wild-type and Stxbp5/5llox neurons, it affects protein levels of the overexpressed DCV reporter only in Stxbp5/5llox but not in wild-type neurons.

## Discussion

In this study, we examined the role of tomosyns in the exocytosis of neuropeptide-containing DCVs in mammalian neurons. Using a pHluorin-based DCV fusion reporter, we found that the conditional loss of tomosyns does not alter the number of DCV exocytosis events but lowers intracellular levels of the DCV reporter. We corroborated the latter finding by showing that levels of endogenous DCV cargos, such as BDNF, are decreased in tomosyn DKO neurons by three independent approaches (ICC, WB, and mass spectrometry). The effect on the DCV pool and/or composition was accompanied by a smaller DCV size and increased speed of the DCV reporter flux through the TGN. Taken together, these data suggest that tomosyn is dispensable for control of DCV fusion, but, paradoxically, has an impact on the intracellular levels of DCV cargos.

The lack of the effect on neuronal DCV fusion is surprising, given that tomosyn regulates SV release in neurons and secretory granule exocytosis in neuroendocrine cells and platelets. However, phenotypes caused by the loss of tomosyn expression in different cell types are discrepant. While the loss of tomosyn resulted in enhanced SV fusion in the mouse brain and invertebrate nervous system (Sakisaka et al., 2008; Ben-Simon et al., 2015; Gracheva et al., 2006; McEwen et al., 2006; Chen et al., 2011; Sauvola et al., 2021), tomosyn deficiency in platelets, INS-1E cells and rat superior cervical ganglion neurons led to an opposite phenotype – a strong reduction in secretion (Ye et al., 2014; Zhu et al., 2014; Cheviet et al., 2006; Baba et al., 2005). No unifying model explains the discrepant effects of tomosyn on secretory vesicle fusion. Altogether, the discrepant effects of tomosyn on fusion in different cell types suggest that tomosyn does not act solely as an inhibitor of fusogenic SNARE complex formation.

DCVs and SVs differ in release properties, and recent studies shed light on some components of the molecular machinery contributing to these differences (Persoon et al., 2019; Moro et al., 2021). In contrast to SVs, which are released in response to a single electric pulse, neuronal DCVs require prolonged high-frequency stimulation for induction of exocytosis (Hartmann et al., 2001; Xia et al., 2009; Persoon et al., 2018). Several factors can explain the reluctance of DCVs to fuse, among them the loose coupling of DCVs to the sites of calcium entry, requiring an increase in calcium levels reaching beyond an immediate radius of a calcium channel (Mansvelder and Kits, 2000). The difference in calcium sensitivity between SVs and DCVs may facilitate frequency-dependent release of different types of chemical signals from neurons and ensure that neuropeptides are secreted predominantly at high firing rates. Interestingly, the inhibitory effect of tomosyn on DCV fusion in adrenal chromaffin cells is calcium-dependent and could be overridden by an increase in intracellular calcium (Yizhar et al., 2004). Thus, it is possible that high-frequency stimulation and a massive increase in intracellular calcium required for the induction of neuronal DCV exocytosis overrides the regulatory effect of tomosyn.

Despite the lack of effect on DCV exocytosis, loss of tomosyns resulted in the decreased intracellular levels of overexpressed (NPY-pHluorin) and endogenous (BDNF, IA-2) DCV cargos (Figure 2, Figure 2—figure supplement 1). Importantly, this phenotype was reproduced in DKO neurons grown under three different culture conditions that vary in cell density and the ratio of neurons to glia (single neurons grown on glial microislands, sparse network cultures on glial feeder layer, and dense network cultures on coated plastic). This phenotype is consistent with the effect of tomosyn’s loss in platelets, i.e. a strong decrease in many secretory cargos, despite the fact that the release of these cargos was reduced, not enhanced (Ye et al., 2014). Tomosyn-deficient platelets showed more than 50% decrease in the levels of alpha-granules cargos, such as factor V and platelet factor 4 (PF4), although alpha-granule count was not affected. Similarly, loss of tomosyn orthologs SRO7/77 in yeast resulted in the altered composition of secretory vesicles and re-routing of a secretory cargo, sodium pumping ATPase Ena1p, from secretory vesicles into the degradative pathway (vacuole) (Forsmark et al., 2011; Wadskog et al., 2006). Despite the fact that alpha-granules in platelets and secretory vesicles in yeast differ from neuronal DCVs in many aspects, taken together, our published data suggest a general role of tomosyn and its orthologs in sorting cargos into various types of secretory granules. The enrichment of tomosyn at the TGN (Figure 5—figure supplement 1) and decreased DCV and Golgi size in DKO neurons (Figures 4A–C–5A–B) are consistent with such a role.

Importantly, the loss of tomosyns in neurons did not abolish the formation of new secretory granules, as evidenced by the normal budding of NPY-vesicles in the RUSH assay (Figure 5E, Figure 5—video 1). However, NPY flux through the Golgi was slightly accelerated in DKO (Figure 5F–H), supporting the hypothesis that tomosyn regulates the sorting of the soluble cargo at the TGN. The decreased size of DCVs suggests that loading of DCVs with secretory cargo is impaired in DKO, since DCV size is regulated by the amount of loaded cargo, at least in non-neuronal cell types (Clermont et al., 1993; Boquist and Lorentzon, 1979). On the other hand, the peak amplitude of individual NPY-pHluorin fusion events, an estimate of NPY loading per fusing DCV, was not affected in DKO (Figure 1G). This discrepancy suggests that smaller DCVs in DKO may be reluctant to fuse due to the deficiency in specific transmembrane cargos necessary for DCV exocytosis. Another important observation is that interfering with lysosomal activity did not rescue cargo levels in DKO neurons (Figure 2G), indicating that cargo is not mis-sorted to lysosomes in the absence of tomosyns.

Re-expression of tomosyn rescued protein, but not mRNA expression, of DCV cargos in DKO neurons (Figure 6D). We found that the recombinase activity of Cre, irrespective of the presence of the loxP sites, affects the expression of some DCV cargos (Bdnf, Grp, Pcsk1), explaining the inability of tomosyn to rescue transcription of these genes. It has been long acknowledged that Cre expression can have deleterious side effects (Schmidt et al., 2000; Loonstra et al., 2001; Heidmann and Lehner, 2001; Forni et al., 2006; Naiche and Papaioannou, 2007), although, to our knowledge, none were reported for primary neuronal cultures. Cre can catalyze recombination between pseudo (cryptic) loxP sites (Thyagarajan et al., 2000). Our data suggest that Cre expression in postmitotic neurons affects neuronal transcriptome and warrants caution when interpreting data on the proteome DKO neurons.

Notwithstanding this effect, the current study provides robust evidence that the decrease of BDNF at the protein level is caused, to a large extent, specifically by the loss of tomosyns, and not by the effects of Cre on transcription. First, BDNF levels were decreased by more than 50% in DKO neurons (Figure 2C–D and E–F), and only by around 26% in Cre-expressing wild-type neurons (Figure 6F–G). Second, BDNF levels in DKO were restored to approximately 80% of control levels by re-expression of tomosyn (Figure 2C–D). Finally, in support of the specific effects of tomosyn on DCV cargos, levels of the overexpressed NPY-pHluorin levels were decreased in DKO, but not in Cre-expressing wild-type neurons, and this decrease was rescued by the re-expression of tomosyn (Figure 2A–B, Figure 6—figure supplement 1).

Interestingly, the SNARE domain of tomosyn was dispensable for the rescue of BDNF levels in DKO, suggesting that the N-terminal WD40-domain mediates this effect of tomosyn (Figure 2G–H). The main structural feature of the WD40-domain are two bulky beta-propellers comprised of multiple WD40 repeats. This domain constitutes the largest part of tomosyn’s molecule, and it is best conserved among all tomosyn orthologs, including the yeast SRO7/77 that, in fact, lack the canonical SNARE domain. Previous studies showed that WD40-domain alone is not sufficient to rescue synaptic transmission defects caused by the loss of tomosyn orthologs in the fly and nematode (Burdina et al., 2011; Sauvola et al., 2021). On the other hand, overexpression of the WD40 domain alone has an inhibitory effect on secretion from bovine chromaffin and rat pheochromocytoma PC12 cells (Yizhar et al., 2007; Bielopolski et al., 2014). This effect has been attributed to the binding of specific loops in the WD40 propeller region to SNAP25 (Bielopolski et al., 2014). Several other interaction partners of tomosyn were reported to bind to the WD40-propellers, such as Rab3A and synaptotagmin (Yamamoto et al., 2010; Cazares et al., 2016), suggesting that the WD40 domain may serve as a scaffold for the assembly of the dynamic protein complexes. The strength of these interactions can be regulated by posttranslational modifications of the WD40 domain, such as phosphorylation (by PKA, ROCK) and SUMOylation (Baba et al., 2005; Gladycheva et al., 2007; Ferdaoussi et al., 2017). A recent study identified tomosyn as an inhibitor of RhoA in the WD40-domain dependent manner (Shen et al., 2020). RhoA is a small GTPase that regulates, among other processes, membrane trafficking at the Golgi (Quassollo et al., 2015). Remarkably, Sro7 was originally identified in a genome-wide screen as a multicopy suppressor of RHO3, an ortholog of Rho GTPases in yeast, suggesting an evolutionary conserved link between tomosyn and Rho GTPases (Matsui and Toh-E, 1992). Further studies are required to validate the potential regulation of Rho by tomosyn and to assess a role of this hypothetical pathway at the Golgi.

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
      <td>Gene (Mus musculus)</td>
      <td>Stxbp5</td>
      <td>NCBI</td>
      <td>78808</td>
      <td>syntaxin binding protein 5 (tomosyn)</td>
    </tr>
    <tr>
      <td>Gene (Mus musculus)</td>
      <td>Stxbp5l</td>
      <td>NCBI</td>
      <td>207227</td>
      <td>syntaxin binding protein 5-like (tomosyn-2)</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>C57BL/6J-Stxbp5lox/Stxbp5llox</td>
      <td>This paper</td>
      <td>-</td>
      <td>Generation of the mouse model is described in Materials and Methods (Mice)</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>C57BL/6 J</td>
      <td>Charles River</td>
      <td>Strain code 631</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Rattus norvegicus)</td>
      <td>Wistar (Crl:WI)</td>
      <td>Charles River</td>
      <td>Strain code: 003</td>
      <td>Used for preparation of glia feeder layer</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-syntaxin (mouse monoclonal)</td>
      <td>Sigma</td>
      <td>S0664</td>
      <td>1:2000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-SNAP25 (mouse monoclonal)</td>
      <td>Covance</td>
      <td>SMI-81R</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-VAMP2 (mouse monoclonal)</td>
      <td>Synaptic Systems</td>
      <td>104211</td>
      <td>1:2000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-tomosyn (rabbit polyclonal)</td>
      <td>Synaptic Systems</td>
      <td>183103</td>
      <td>1:1000 (WB)1:500 (ICC)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-tomosyn-2 (rabbit polyclonal)</td>
      <td>Synaptic Systems</td>
      <td>183203</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-alpha-tubulin (mouse monoclonal)</td>
      <td>Synaptic Systems</td>
      <td>302211</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-actin (mouse monoclonal)</td>
      <td>Merck</td>
      <td>MAB1501</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-synaptophysin (guinea pig polyclonal)</td>
      <td>Synaptic Systems</td>
      <td>101004</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-MAP2 (chicken polyclonal)</td>
      <td>Abcam</td>
      <td>ab5392</td>
      <td>1:5000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-IA-2 (PTPRN) (mouse monoclonal)</td>
      <td>Merck</td>
      <td>MABS469</td>
      <td>1:100</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-CHGA (rabbit polyclonal)</td>
      <td>Synaptic Systems</td>
      <td>259003</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-CHGB (rabbit polyclonal)</td>
      <td>Synaptic Systems</td>
      <td>259103</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-BDNF (mouse monoclonal)</td>
      <td>DSHB hybridoma product</td>
      <td>BDNF #9 (supernatant)1</td>
      <td>1:4</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-BDNF (mouse monoclonal)</td>
      <td>Biosensis</td>
      <td>BSENM-1736–50 (clone 3C11)</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-LAMP1 (rat monoclonal)</td>
      <td>DSHB hybridoma product</td>
      <td>1D4B (supernatant)2</td>
      <td>1:20 (ICC)1:200 (WB)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-LIMP2 (rabbit polyclonal)</td>
      <td>Novus Biologicals</td>
      <td>NB400-129</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-GAPDH (rabbit polyclonal)</td>
      <td>Elabscience</td>
      <td>E-AB-40337</td>
      <td>1:2000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-TMEM87A (rabbit polyclonal)</td>
      <td>Novus Biologicals</td>
      <td>NBP1-90532</td>
      <td>1:100</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-TGN38 (sheep polyclonal)</td>
      <td>Bio-Rad</td>
      <td>AHP499G</td>
      <td>1:100</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-Syn(pr)-Cre-mCherry</td>
      <td>Wolzak et al., 2022</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-Syn(pr)-ΔCre-mCherry</td>
      <td>Wolzak et al., 2022</td>
      <td>-</td>
      <td>Cre lacking catalytic domain</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-Syn(pr)-pre-NPY-pHluorin</td>
      <td>Nassal et al., 2022</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-mScarlet-T2A-tomosyn</td>
      <td>This paper</td>
      <td>-</td>
      <td>mouse isoform m (NM_001081344). Generation of this reagent is described in Materials and methods (Expression constructs)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-mScarlet-T2A-tomosyn(aa1-1047)</td>
      <td>This paper</td>
      <td>-</td>
      <td>Generation of this reagent is described in Materials and methods (Expression constructs)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLenti-Syn(pr)-mCherry</td>
      <td>This paper</td>
      <td>-</td>
      <td>Generation of this reagent is described in Materials and methods (Expression constructs)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCMV-Streptavidin-KDEL-IRES-EGFP-NPY</td>
      <td>Emperador-Melero et al., 2018</td>
      <td>-</td>
      <td>Construct used for RUSH assay</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>qPCR primers are listed in Table 1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>2.5% trypsin</td>
      <td>gibco</td>
      <td>15090046</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>papain</td>
      <td>Worthington Biochemical Corporation</td>
      <td>LS003127</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>poly-L-ornithine</td>
      <td>Sigma</td>
      <td>P4957</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>laminin</td>
      <td>Sigma</td>
      <td>L2020</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>rat tail collagen</td>
      <td>BD Biosciences</td>
      <td>354236</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>poly-D-lysine</td>
      <td>Sigma</td>
      <td>P6407</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>SensiFast cDNA Synthesis Kit</td>
      <td>Meridian Bioscience</td>
      <td>BIO-65054</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>SensiFast SYBR Lo-ROX Kit</td>
      <td>Meridian Bioscience</td>
      <td>BIO-94020</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>leupeptin</td>
      <td>Hello Bio</td>
      <td>HB3958</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>biotin</td>
      <td>Sigma</td>
      <td>B4501</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>MathWorks</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism</td>
      <td>GraphPad</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji/ImageJ</td>
      <td>NIH</td>
      <td>-</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 1.**
 List of qRT-PCR primers used in this study.


<table>
  <thead>
    <tr>
      <th>Gene</th>
      <th>Forward primer sequence</th>
      <th>Reverse primer sequence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bdnf (all transcripts)</td>
      <td>GGCTGACACTTTTGAGCACGTC</td>
      <td>CTCCAAAGGCACTTGACTGCTG</td>
    </tr>
    <tr>
      <td>Bdnf (transcript 1)</td>
      <td>ACTGAGCAAAGCCGAACTT</td>
      <td>TCTCACCTGGTGGAACATTGTG</td>
    </tr>
    <tr>
      <td>Bdnf (transcript 2)</td>
      <td>TAGGCTGGAATAGACTCTTGG</td>
      <td>CTCACCTGGTGGAACTTCTTTG</td>
    </tr>
    <tr>
      <td>Bdnf (transcript 4)</td>
      <td>CCTCCCCCTTTTAACTGAAG</td>
      <td>CTCACCTGGTGGAACTTTTT</td>
    </tr>
    <tr>
      <td>Bdnf (transcript 6)</td>
      <td>AGGGACCAGAAGCGTGACAA</td>
      <td>CTCACCTGGTGGAACTCAGGGT</td>
    </tr>
    <tr>
      <td>Bdnf (transcript 9)</td>
      <td>TGATTGTGTTTCTGGTGACA</td>
      <td>CGGTTTCTAAGCAAGTGAAC</td>
    </tr>
    <tr>
      <td>Vgf</td>
      <td>CTTTGACACCCTTATCCAAGGCG</td>
      <td>GCTAATCCTTGCTGAAGCAGGC</td>
    </tr>
    <tr>
      <td>Pcsk1</td>
      <td>GGAGAGAATCCTGTAGGCACCT</td>
      <td>GCTCTGGTTGAGAAGATGTCCC</td>
    </tr>
    <tr>
      <td>Pam</td>
      <td>AGTCGGATCGTGCAGTTCTCAC</td>
      <td>ACTGGTTCAGGTGAGGCACAAG</td>
    </tr>
    <tr>
      <td>Ptprn</td>
      <td>TGGCAGGCTATGGAGTAGAGCT</td>
      <td>CTTGACATCGGCTCCTCCAACA</td>
    </tr>
    <tr>
      <td>Scg2</td>
      <td>CAGGAAGAGGTGAGAGACAGCA</td>
      <td>TGGAGGCATCCTCTGAGAGTTG</td>
    </tr>
    <tr>
      <td>Npy</td>
      <td>TACTCCGCTCTGCGACACTACA</td>
      <td>GGCGTTTTCTGTGCTTTCCTTCA</td>
    </tr>
    <tr>
      <td>Cck</td>
      <td>GAGGTGGAATGAGGAAACAA</td>
      <td>CAGATTTCACATTGGGGACT</td>
    </tr>
    <tr>
      <td>Grp</td>
      <td>TTCAAACCGCTAAGTTGGT</td>
      <td>GAAGGGTTTTGTTTTGCTCC</td>
    </tr>
    <tr>
      <td>Sst</td>
      <td>TCTGGAAGACATTCACATCC</td>
      <td>TTCTAATGCAGGGTCAAGTT</td>
    </tr>
    <tr>
      <td>Tac1</td>
      <td>AGATCTCTCACAAAAGGCAT</td>
      <td>CATCGCGCTTCTTTCATAAG</td>
    </tr>
    <tr>
      <td>Pnoc</td>
      <td>TCCTCTTTTGTGACGTTCTG</td>
      <td>GAGGATGCACGTCTTTAAGT</td>
    </tr>
    <tr>
      <td>Vip</td>
      <td>ATGATGTGTCAAGAAATGCC</td>
      <td>ATTCGTTTGCCAATGAGTGA</td>
    </tr>
    <tr>
      <td>Pdyn</td>
      <td>ATCAACCCCCTGATTTGCTC</td>
      <td>ATCTTCCAAGTCATCCTTGC</td>
    </tr>
    <tr>
      <td>Penk</td>
      <td>ACATCAATTTCCTGGCGTGC</td>
      <td>TGTTATCCCAAGGGAACTCG</td>
    </tr>
    <tr>
      <td>Cort</td>
      <td>CTTCTTATGTCAGCTTTGCC</td>
      <td>CTCCAATCCCTTAGTTGACC</td>
    </tr>
    <tr>
      <td>Gapdh</td>
      <td>CATCACTGCCACCCAGAAGACTG</td>
      <td>ATGCCAGTGAGCTTCCCGTTCAG</td>
    </tr>
  </tbody>
</table>

### Mice

Stxbp5lox/lox, Stxbp5llox/lox double conditional null mice were generated by breeding two lines with the individually targeted Stxbp5 and Stxbp5l alleles. To generate Stxbp5lox/+ mice, lox2272 recombination sites flanking exon 2 of Stxbp5 (98 bp in size) were introduced into the genome via homologous recombination in C57Bl/6 embryonic stem (ES) cells (Cyagen Animal Model Services, Santa Clara, USA). Lox2272 recombines efficiently with other lox2272 sites, but not with loxP (Lee and Saito, 1998). Deletion of exon 2 causes a frameshift in all tomosyn reference transcripts (NM_001081344.3, NM_001408063.1, NM_001408064.1, and NM_001408065.1). The targeting vector contained a neomycin resistance marker, flanked by self-deleting anchor sites and placed between exon 2 and the lox2272 site in intron 2. Targeted ES clones were injected into blastocysts to produce germ-line chimeras, which were mated to C57Bl/6 J wild-type mice. Stxbp5 line genotyping was performed using the following primers (5’ ACTTAGCGCGGAGGGTTTTGTC 3’ and 5’ CGTAGGCTTTTAAATCACCGCTGT 3’) to amplify Stxbp5+ or Stxbp5lox specific products of 196 and 236 bp in size, respectively.

The Stxbp5llox/+ line was generated independently as described in Geerts et al., 2015. In these mice, the paralogous exon 3 (also 98 bp in size) is flanked by loxP sites. Cre-mediated excision induces a frameshift in all reference transcripts (NM_172440.3, NM_001114611.1, NM_001114612.1, NM_001114613.1, also named xb-, s-, b- and m-tomosyn-2, respectively). Stxbp5l line genotyping was performed for Stxbp5l as described (Geerts et al., 2015).

After interbreeding the two mouse lines, both backcrossed to an inbred C57Bl/6 J genetic background, newborn pups from homozygous Stxbp5lox/lox, Stxbp5llox/lox matings were used for the preparation of neuronal cultures in all the described experiments. Mice were housed and used for experiments according to institutional guidelines and Dutch laws in accordance with the European Communities Council Directive (2010/63/EU).

### Neuronal cultures

Mouse hippocampal cultures were prepared from newborn pups. Normally, hippocampi from several pups from one nest were pooled in one culture preparation, which was considered as one biological replicate. Hippocampi were dissected in Hanks Balanced Salt Solution (HBSS, Sigma H9394) supplemented with 10 mM HEPES (pH 7.2–7.5, Gibco 15630056) and digested with 0.25% trypsin (Gibco 15090046) at 37 °C for 15 min. After the digestion, tissue pieces were washed in HBSS and triturated using fire-polished Pasteur pipettes in Dulbecco’s modified Eagle medium (DMEM, VWR Life Science VWRC392-0415) supplemented with 10% fetal calf serum (FCS, Gibco 10270), non-essential amino acids (Sigma M7145), and antibiotics (penicillin/streptomycin, Gibco 15140122). For most immunocytochemistry (ICC) experiments, cell suspension was sparsely plated on a feeder layer of rat glia at a density of 20–30×103/well on 15 mm coverslips. For BDNF ICC and pHluorin imaging experiments, neurons were plated on glial micro-islands at a density of 1500/well (to obtain single neuron cultures). For RUSH, rat glia was omitted, and neurons were plated on glass coverslips at a density of approximately 120×103/well on 15 mm coverslips. Prior to plating, glass coverslips were coated with poly-L-ornithine (Sigma P4957) and laminin (Sigma L2020). For western blot, proteomics, electron microscopy, and qPCR experiments, neurons were plated on coated plastic without the glia feeder layer at a density of 400×103/well in a six-well plate. Cultures were maintained in a humified incubator at 37 °C and 5% CO2 in Neurobasal medium (Gibco 21103049) supplemented with B27 (Gibco 17504044), 10 mM HEPES, GlutaMAX (Gibco 35050038) and antibiotics (penicillin/streptomycin, Gibco 15140122). To induce loss of tomosyns, cultures were transduced within 8 hr after plating with a lentivirus encoding Cre-recombinase expressed under the control of synapsin promoter (pSyn-Cre-mCherry). As a control, neurons from the same culture preparation were transduced with Cre-recombinase lacking the catalytic domain (pSyn-ΔCre-mCherry). Experiments were performed, if not otherwise stated, on day in vitro (DIV) 14. For rescue experiments, neurons were transduced on DIV2 with lentivirus encoding either FL tomosyn (isoform 1 m, NM_001081344, aa 1–1116) or truncated tomosyn (aa1-1047) lacking the SNARE domain.

Rat glia were prepared from the cortices of newborn rats. Cortices were digested in papain (Worthington Biochemical Corporation LS003127) at 37 °C for 45 min and triturated in DMEM supplemented with 10% FCS, non-essential amino acids, and antibiotics. Glia were plated and expanded in T175 flasks. For making single neuron cultures, glia were plated on micro-islands of growth permissive substrate (mix of collagen I and poly-D-lysine, Corning 354236 and Sigma P6407, respectively) that were printed on a layer of 0.15% agarose.

### Expression constructs

All transgenes, except for the RUSH reporter, were expressed under the control of the human synapsin promoter in lentiviral backbones. Cre-mCherry and ΔCre-mCherry fusions were described by Wolzak et al., 2022. Generation of the DCV fusion reporter (pre-NPY-pHluorin) was described by Nassal et al., 2022. Constructs encoding FL tomosyn (NM_001081344, aa1-1116) and truncated mutant (aa1-1047) of tomosyn lacking the SNARE domain were generated in this study. Tomosyn-encoding sequences were amplified from the mouse cDNA library and cloned with the N-terminal mScarlet succeeded by the T2A sequence into the lentiviral backbone. Construct encoding constitutively active CREB mutant (Y134F) was described in Moro et al., 2020. RUSH reporter (Streptavidin-KDEL-IRES-SBP-EGFP-NPY) was expressed under the control of the CMV promoter in pIRESneo3 backbone. Generation of this reporter was described in Emperador-Melero et al., 2018.

### Visualization and analysis of DCV fusion

Single neuron cultures were transduced on DIV8 with a lentivirus encoding the N-terminal part of human NPY fused to super-ecliptic pHluorin (Figure 1—figure supplement 2). DIV14-15 neurons were used for live imaging on a Nikon Ti Eclipse inverted microscope equipped with A1R confocal module and Andor DU-897 camera (with 512x512 pixels frame) under 40 x oil objective (numerical aperture, NA 1.3). LU4A laser unit with 488 nm wavelength laser was used as the illumination source. Coverslips were transferred in an imaging chamber in Tyrode’s solution (119 mM NaCl, 2.5 mM KCl, 2 mM CaCl2, 2 mM MgCl2, 25 mM HEPES, and 30 mM Glucose, pH 7.4, 280 mOsmol) and time-lapse videos were recorded at 2 Hz frequency for 2 min at room temperature under constant perfusion with Tyrode’s. After 30 s of baseline recording, neurons were subjected to electric field stimulation (16 trains, each consisting of 50 pulses at 50 Hz and separated by 500 msec intervals) delivered by platinum electrodes. At the end of each recording, 50 mM NH4Cl-containing Tyrode’s solution (with NaCl concentration reduced to 69 mM to maintain osmolarity) was applied to visualize the intracellular pool of DCVs.

Analysis of the time-lapse recordings was performed as described (Persoon et al., 2019). In short, fusion events were detected by a sudden rise in fluorescence intensity. 3 × 3 pixel regions of interest (ROI) were placed on time-lapse recordings using a custom-made script in Fiji (Schindelin et al., 2012). Change in fluorescence intensity (F) within these ROIs was plotted as ΔF/F0, where F0 is an average of the first 10 frames of acquisition. Resulting traces were checked using a custom-made script in MATLAB, and only events with F/F0 ≥2 SD and rise time <1 s were counted. Total number of intracellular vesicles (intracellular pool) was determined as the number of fluorescent puncta after the ammonium pulse corrected to account for overlapping puncta. Released fraction was calculated as the number of fusion events per neuron divided by the intracellular pool of DCVs.

### Immunocytochemistry

Neurons grown on coverslips were fixed by the application of phosphate-buffered saline (PBS) containing 4% paraformaldehyde (PFA, Sigma P6148) and 4% sucrose for 10 min. After fixation, neurons were washed and the residual PFA was quenched by application of 0.1 M glycine for 5 min. Neurons were permeabilized and blocked in PBS containing 0.1% Triton X-100 (Fisher Chemical T/3751/08) and 2% normal goat serum (Gibco 16210–072) (‘blocking buffer’) for 30 min. Primary antibodies diluted in blocking buffer were applied for 1 hr at room temperature. Primary antibodies used in this study and their dilutions are listed in Table 1. After washing with PBS, neurons were incubated with Alexa Fluor-coupled secondary antibodies diluted at 1:500 for 45 min. Stained coverslips were mounted in Mowiol.

### Confocal microscopy of fixed neurons

Imaging of stained neurons was performed on a Nikon Ti Eclipse inverted microscope equipped with A1R confocal module and LU4A laser unit. Images were acquired under 40 x (NA 1.3) or 60 x (NA 1.4) oil objectives in the confocal mode. Acquisition parameters (zoom, image size, scanning speed, laser power, and gain) were set using NIS software to achieve appropriate image resolution and avoid signal saturation. Three to five z-sections with an interval of 0.2 µm were collected per image.

Analysis of staining intensity was performed on maximum intensity projection of z-stacks using a custom-made macro in Fiji, as described (Moro et al., 2020). Masks of the neuronal somata and neurites were obtained based on the MAP2 signal. Puncta of DCV cargos (BDNF, IA-2) were detected within the neurite mask based on their intensity and dimensions.

### SDS-PAGE WB analysis

To analyze protein levels, high-density neuronal cultures (400×103/well in a six-well plate) were lysed in Laemmli sample buffer. Lysates were heated at 95 °C for 5 min, separated by SDS-PAGE using either home-made tris-glycine or commercially available Mini-PROTEAN TGX Stain-Free gels (Bio-Rad 4568096), and transferred to nitrocellulose membrane (Bio-Rad 1620115) using a wet tank transfer method. For BDNF detection, membranes were subjected to crosslinking by 0.5% (v/v) glutaraldehyde directly after the protein transfer according to the published protocol (Karey and Sirbasku, 1989) Membranes were blocked in 5% milk powder dissolved in Tris-buffered saline containing 0.1% TweenⓇ 20 (TBS-T). Membranes were incubated with primary antibodies diluted in TBS-T on a shaking platform overnight at 4 °C. Primary antibodies used in this study and their dilutions are listed in the Key Resources Table. Horseradish peroxidase coupled secondary antibodies were applied at 1:10,000 dilution for 1 hr at room temperature. Chemiluminescence-based detection was performed using SuperSignal West Femto Maximum Sensitivity Substrate (Thermo Scientific 34095) on the Odyssey Fc imaging system (LI-COR Bioscience). Immunosignal of some proteins (IA-2, BDNF) was detected using a more sensitive SuperSignal West Atto Ultimate Sensitivity Substrate (Thermo Scientific A38555). Signal intensities of bands of interest were analyzed using Image Studio Lite Software and normalized to the intensity of a loading control (actin, tubulin, or GAPDH). Actin levels were not affected by the loss of tomosyn, as evidenced by comparing band intensities of actin to total protein stain visualized on Mini-PROTEAN TGX Stain-Free gels.

### Detection of SNARE complexes

Detection of SNARE complexes was performed as described previously (Hayashi et al., 1994; Otto et al., 1997). The protocol is based on the observation that assembled synaptic SNARE complexes (consisting of syntaxin-1, SNAP25, and VAMP2) are preserved in SDS-containing lysis buffer (‘SDS-resistant’) but sensitive to temperatures higher than 60 °C. To detect syntaxin-1 in SNARE complexes, high-density neuronal cultures (400 K/well in a six-well plate) were lysed in 1% SDS-containing Laemmli sample buffer, passed through an insulin syringe and split into two parts. The first part of the lysates was heated at 95 °C for 5 min (for the detection of total syntaxin-1), while the second part was heated at 37 °C for 5 min (for the detection of syntaxin-1 in SNARE complexes). Lysates were separated by SDS-PAGE using 4–20% gradient gels (Mini-PROTEAN TGX Stain-Free gels, Biorad #4568096). Protein transfer and detection were performed as described above.

### Proteome analysis by mass spectrometry

DIV12-13 hippocampal neurons grown in high-density cultures (400×103/well in a six-well plate) were washed once with pre-warmed PBS and lysed in Laemmli sample buffer (50 μl/well). Lysates were passed through an insulin syringe and stored at –80 °C until further processing.

In-gel digestion with Trypsin/Lys-C Mix solution (Promega) was performed as previously described (Li, 2019). Peptides were analyzed by micro LC-MS/MS using a TripleTOF 5600 mass spectrometer (Sciex, Framingham, MA, USA). The peptides were fractionated with a linear gradient of acetonitrile using a 200 mm Alltima C18 column (300 μm i.d., 3 μm particle size) on an Ultimate 3000 LC system (Dionex, Thermo Scientific, Waltham, MA, USA). Data-independent acquisition was used with Sequential Window Acquisition of all THeoretical mass spectra (SWATH) windows of 8 Da, as previously described (Gonzalez-Lozano et al., 2021).

SWATH data was analyzed using DIA-NN (v1.8) (Demichev et al., 2020). A spectral library was generated from the complete mouse proteome with a precursor m/z range of 430–790. Data was searched with 20 ppm mass accuracy, match-between-runs algorithm (MBR) enabled and robust LC as quantification strategy. Propionamide was selected as fixed modification. Downstream analysis was performed using MS-DAP (Koopmans et al., 2023; Koopmans et al., 2022). The experimental replicate with the lowest number of identified peptides was removed from the analysis (for both genotypes). Only peptides identified and quantified in at least four out of five remaining replicates per genotype were included in the analysis. Normalization was achieved using variance stabilization normalization (Vsn) and mode-between protein methods. The Msqrob algorithm was selected for differential expression analysis, using an FDR-adjusted p-value threshold of 0.01 and log2 fold change of 0.3 to discriminate significantly regulated proteins. All data are available in the PRIDE repository with the identifier PXD038442. Gene ontology enrichment analysis of the differentially expressed proteins was performed using ShinyGO application v0.75 with an FDR-adjusted p-value threshold of 0.05 (http://bioinformatics.sdstate.edu/go/) (Ge et al., 2020).

### Electron microscopy

Neurons grown on coated glass coverslips were fixed on DIV14 in 2.5% glutaraldehyde in 0.1 M cacodylate buffer. The cells were postfixed in 1% osmium/1% ruthenium and subsequently dehydrated by increasing ethanol concentrations (30%, 50%, 70%, 90%, 96%, and 100%) before embedding in EPON. After polymerization of the resin for 72 hr at 65 °C, glass coverslips were removed by heating the samples in boiling water. Neuron-rich regions were selected by light microscopy, cut out, and mounted on pre-polymerized EPON cylinders. Ultrathin sections of 70–90 nm were cut on an ultra-microtome (Reichert-Jung, Ultracut E) and collected on formvar-coated single slot grids. Finally, the sections were contrasted with uranyl acetate and lead citrate in an ultra-stainer (Leica EM AC20) and imaged in a JEOL1010 transmission electron microscope (JEOL) at 60 kV while being blinded for the experimental conditions. Synapses, somas, and DCV-rich areas were photographed by a side-mounted Modera camera (EMSIS GmbH). While remaining blinded for experimental conditions, DCV diameters were measured in iTEM software (Olympus), and synapse parameters were quantified in a custom-written software running in Matlab (Mathworks).

### RUSH assay

The protocol is modified from Boncompain et al., 2012. Neurons were grown in standard neuronal medium except Neurobasal without phenol red (Gibco 12348017) was used to minimize an autofluorescent background during live imaging. On DIV7, half of the medium was refreshed with the same medium lacking the B27 supplement (to reduce extracellular biotin levels). On DIV9, neurons were transfected using the calcium phosphate transfection method with a plasmid encoding a DCV reporter and an ER hook (pCMV-Streptavidin-KDEL-IRES-SBP-EGFP-NPY) together with a 'filler' plasmid (pCMV-mCherry). Neurons were imaged live approximately 16 hr after the transfection upon the addition of 40 μM biotin to the conditioned medium. Time-lapse imaging was performed on a Nikon Ti Eclipse inverted microscope equipped with an A1R confocal module under 40 x oil objective (NA 1.3). LU4A laser unit with a 488 nm wavelength laser was used as the illumination source. Neurons were picked for imaging based on the mCherry fluorescence and were imaged at 37°C and 5% CO2 for 2 hr after the addition of biotin, at a frequency of 1 frame/5 min.

Movies were analyzed in Fiji. Possible lateral drift during recordings was corrected using the Image Stabilizer plugin. Mean intensity of NPY-EGFP within the Golgi mask was measured across the frames and plotted against time in GraphPad Prism. The rate constant of Golgi clearance was determined by fitting a one-phase exponential decay curve to the decay phase of the intensity plot.

For imaging of DCV trafficking in neurites, transfected neurons were imaged in 80 min after the addition of biotin with 0.5 Hz frequency (3 min recordings). Kymographs (space/time plots) were generated from time-lapse videos in Fiji using the KymoResliceWide plugin. Kymographs were analyzed using Kymobutler software (Jakobs et al., 2019).

### Quantitative RT-PCR (qRT-PCR)

RNA extraction from neuronal cultures was performed using the ISOLATE II RNA Micro Kit (Meridian Bioscience BIO-52073). cDNA was synthesized from purified RNA using SensiFast cDNA Synthesis Kit (Meridian Bioscience BIO-65054). qRT-PCRs were run on a QuantStudio 5 system (ThermoFisher Scientific) using SensiFast SYBR Lo-ROX Kit (Meridian Bioscience BIO-94020). qRT-PCR primers (listed in Table 1) were validated for the efficiency by running qRT-PCRs on tenfold serial dilutions of cDNA, and for the specificity estimated from melt curves. Only primers with an efficiency of 90–105% were used for experiments. Fold changes (FC) in gene expression were determined using the cycle threshold (CT) comparative method (2−ddCT) using Gapdh as a housekeeping gene. Gapdh CT values were not affected by the genotype or treatment applied. Statistical analysis of the data was performed on log-transformed data (logFC, ddCT).

### Statistical analyses

Sample size was chosen based on the previously published findings from similar experiments using similar measuring techniques. Statistical analyses were performed using GraphPad Prism software. Data distribution was tested for normality using the D'Agostino-Pearson test. Possible outliers were identified using the ROUT method. An F test was used to compare variances between the groups. Statistical tests were chosen based on the distribution of the data sets, as well as on the number of groups being compared. Statistical tests used in individual experiments are specified in the corresponding figure legends. Full statistical information, including exact p-values, is provided in Table 2.

**Table 2.**
 Summary of statistical analyses applied in this study.


<table>
  <thead>
    <tr>
      <th>Figure</th>
      <th>Dataset</th>
      <th>Groups</th>
      <th>n-number*</th>
      <th>Statistical test</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1C</td>
      <td>Cumulative number of DCV fusion events per neuron plotted against time</td>
      <td>controlDKO</td>
      <td>3 (36)3 (34)</td>
      <td>Two-way repeated measures ANOVA</td>
      <td>ptime x genotype = 0.4823ptime &lt;0.0001 (****)pgenotype = 0.3166</td>
    </tr>
    <tr>
      <td>1D</td>
      <td>Total number of DCV fusion events/neuron</td>
      <td>controlDKO</td>
      <td>3 (36)3 (34)</td>
      <td>Mann-Whitney test</td>
      <td>p=0.0970</td>
    </tr>
    <tr>
      <td>1E</td>
      <td>Number of intracellular NPY-pHluorin puncta/neuron</td>
      <td>controlDKO</td>
      <td>3 (36)3 (35)</td>
      <td>Unpaired t test</td>
      <td>p=0.0224 (*)</td>
    </tr>
    <tr>
      <td>1F</td>
      <td>Fraction of released DCVs (% total pool)</td>
      <td>controlDKO</td>
      <td>3 (36)3 (34)</td>
      <td>Two-way repeated measures ANOVA</td>
      <td>ptime x genotype &gt;0.9999ptime &lt;0.0001 (****)pgenotype = 0.9014</td>
    </tr>
    <tr>
      <td>1G</td>
      <td>Fluorescence intensity peaks (averaged per neuron)</td>
      <td>controlDKO</td>
      <td>3 (36)3 (34)</td>
      <td>Mann-Whitney test</td>
      <td>p=0.4509</td>
    </tr>
    <tr>
      <td>1H</td>
      <td>Band intensities of syntaxin-1 complexes (WB)</td>
      <td>DKO(% control)</td>
      <td>4 cultures</td>
      <td>One sample t-test (compare to 100%)</td>
      <td>p37kDa = 0.2858p80 kDa = 0.5714p200 kDa = 0.0002 (***)</td>
    </tr>
    <tr>
      <td>1 suppl 1E</td>
      <td>Dendrite length/ neuron</td>
      <td>controlDKO</td>
      <td>3 (30)3 (28)</td>
      <td>Unpaired t-test</td>
      <td>p=0.5902</td>
    </tr>
    <tr>
      <td>1 suppl 1 F</td>
      <td>Number of synaptophysin puncta/ mm dendrite</td>
      <td>controlDKO</td>
      <td>3 (30)3 (28)</td>
      <td>Unpaired t-test</td>
      <td>p=0.1380</td>
    </tr>
    <tr>
      <td>1 suppl 1 G</td>
      <td>Intensity of synaptophysin signal in neurites</td>
      <td>controlDKO</td>
      <td>3 (30)3 (28)</td>
      <td>Unpaired t-test</td>
      <td>p=0.6561</td>
    </tr>
    <tr>
      <td>1 suppl 3 A</td>
      <td>Band intensities of SNAP25 complexes (WB)</td>
      <td>DKO (% control)</td>
      <td>3 cultures</td>
      <td>One sample t-test (compare to 100%)</td>
      <td>p25kDa = 0.7265p80 kDa = 0.8454p200 kDa = 0.0064 (**)</td>
    </tr>
    <tr>
      <td>1 suppl 3B</td>
      <td>Band intensities of VAMP2 complexes (WB)</td>
      <td>DKO (% control)</td>
      <td>3 cultures</td>
      <td>One sample t-test (compare to 100%)</td>
      <td>p15kDa = 0.0585p80 kDa = 0.4283</td>
    </tr>
    <tr>
      <td rowspan="4">2B</td>
      <td rowspan="2">Intensity of NPY-pHluorin (ICC)</td>
      <td rowspan="2">controlDKO rescue</td>
      <td rowspan="2">3 (30)3 (29)3 (29)</td>
      <td>One-way ANOVA</td>
      <td>p&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>Tukey’s multiple comparisons post hoc test</td>
      <td>pcontrol vs DKO &lt;0.0001 (****)pDKO vs rescue &lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td rowspan="2">Intensity of tomosyn (ICC)</td>
      <td rowspan="2">controlDKO rescue</td>
      <td rowspan="2">3 (30)3 (30)3 (30)</td>
      <td>One-way ANOVA</td>
      <td>p&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>Tukey’s multiple comparisons post hoc test</td>
      <td>pcontrol vs DKO &lt;0.0001 (****)pDKO vs rescue &lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td rowspan="4">2D</td>
      <td rowspan="2">Intensity of BDNF (ICC)</td>
      <td rowspan="2">controlDKO rescue</td>
      <td rowspan="2">3 (20)3 (20)3 (20)</td>
      <td>Kruskal-Wallis test</td>
      <td>p=0.0009 (***)</td>
    </tr>
    <tr>
      <td>Dunn’s multiple comparisons test</td>
      <td>pcontrol vs DKO = 0.0009 (***)pDKO vs rescue &lt;0.0253 (*)</td>
    </tr>
    <tr>
      <td rowspan="2">Intensity of tomosyn (ICC)</td>
      <td rowspan="2">controlDKO rescue</td>
      <td rowspan="2">3 (20)3 (20)3 (20)</td>
      <td>One-way ANOVA</td>
      <td>p&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>Tukey’s multiple comparisons post hoc test</td>
      <td>pcontrol vs DKO = 0.0012 (**)pDKO vs rescue &lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>2F</td>
      <td>Band intensities of BDNF (WB)</td>
      <td>DKO (% control)</td>
      <td>4 (8)</td>
      <td>One sample t-test (compare to 100%)</td>
      <td>p&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>2H</td>
      <td>Band intensities of BDNF (WB rescue)</td>
      <td>DKODKO+FLDKO+ΔSNARE</td>
      <td>2 (4)</td>
      <td>One sample t-test (compare each condition to 100%)</td>
      <td>pDKO = 0.0005 (***) pDKO+FL = 0.1224pDKO+ΔSNARE = 0.0767</td>
    </tr>
    <tr>
      <td>2I</td>
      <td>Band intensities of BDNF (WB leupeptin)</td>
      <td>control±leupeptinDKO±leupeptin</td>
      <td>2 (4)</td>
      <td>Two-way repeated measures ANOVA</td>
      <td>ptreatment = 0.0640pgenotype = 0.0240 (*)</td>
    </tr>
    <tr>
      <td>2 suppl 1B</td>
      <td>Intensity of EGFP expressed under control of synapsin promoter</td>
      <td>controlDKO</td>
      <td>3 (30)3 (28)</td>
      <td>Unpaired t-test</td>
      <td>p=0.0898</td>
    </tr>
    <tr>
      <td rowspan="2">2 suppl 2B</td>
      <td>Intensity of IA-2 (neurites)</td>
      <td>controlDKO</td>
      <td>3 (24)3 (24)</td>
      <td>Unpaired t-test</td>
      <td>p&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>Intensity of IA-2 (soma)</td>
      <td>controlDKO</td>
      <td>3 (24)3 (24)</td>
      <td>Unpaired t-test</td>
      <td>p=0.0472 (*)</td>
    </tr>
    <tr>
      <td>2 suppl 2 C</td>
      <td>Band intensities of IA-2 (WB)</td>
      <td>DKO(% control)</td>
      <td>3 (9)</td>
      <td>One sample t-test (compare to 100%)</td>
      <td>p&lt;0.0001 (****)</td>
    </tr>
    <tr>
      <td>2 suppl 3B</td>
      <td>Intensity of LAMP1</td>
      <td>controlDKO</td>
      <td>2 (10)</td>
      <td>Unpaired t-test</td>
      <td>p=0.9847</td>
    </tr>
    <tr>
      <td rowspan="2">2 suppl 3D</td>
      <td>Band intensities of LAMP1 (WB)</td>
      <td>DKO(% control)</td>
      <td>3 (9)</td>
      <td>One sample t-test (compare to 100%)</td>
      <td>p=0.3716</td>
    </tr>
    <tr>
      <td>Band intensities of LIMP2 (WB)</td>
      <td>DKO(% control)</td>
      <td>3 (9)</td>
      <td>One sample t-test (compare to 100%)</td>
      <td>p=0.7225</td>
    </tr>
    <tr>
      <td>4B</td>
      <td>DCV diameter</td>
      <td>controlDKO</td>
      <td>3 (135 DCVs)3 (64 DCVs)</td>
      <td>Unpaired t-test on means from three independent cultures</td>
      <td>p=0.0129 (*)</td>
    </tr>
    <tr>
      <td>4E</td>
      <td>SV diameter</td>
      <td>controlDKO</td>
      <td>3 (621 SVs)3 (617 SVs)</td>
      <td>Unpaired t-test on means from three independent cultures</td>
      <td>p=0.2234</td>
    </tr>
    <tr>
      <td>4F</td>
      <td>Number of SV/ synapse</td>
      <td>controlDKO</td>
      <td>3 (149 synapses)3 (147 synapses)</td>
      <td>Unpaired t-test on means from three independent cultures</td>
      <td>p=0.4713</td>
    </tr>
    <tr>
      <td>4G</td>
      <td>Length of active zone</td>
      <td>controlDKO</td>
      <td>3 (151 synapses)3 (148 synapses)</td>
      <td>Unpaired t-test on means from three independent cultures</td>
      <td>p=0.4366</td>
    </tr>
    <tr>
      <td>4H</td>
      <td>Length of PSD</td>
      <td>controlDKO</td>
      <td>3 (152 synapses)3 (147 synapses)</td>
      <td>Unpaired t-test on means from three independent cultures</td>
      <td>p=0.3752</td>
    </tr>
    <tr>
      <td rowspan="2">5B</td>
      <td>TGN area</td>
      <td>controlDKO</td>
      <td>3 (40)3 (39)</td>
      <td>Unpaired t-test</td>
      <td>p=0.0001 (***)</td>
    </tr>
    <tr>
      <td>Nucleus area</td>
      <td>controlDKO</td>
      <td>3 (40)3 (39)</td>
      <td>Unpaired t-test</td>
      <td>p=0.1847</td>
    </tr>
    <tr>
      <td>5F</td>
      <td>NPY-EGFP intensity in the Golgi plotted against time</td>
      <td>controlDKO</td>
      <td>3 (33)3 (30)</td>
      <td>Two-way repeated measures ANOVA</td>
      <td>ptime x genotype = 0.0014 (**)ptime &lt;0.0001 (****)pgenotype = 0.3280</td>
    </tr>
    <tr>
      <td>5G</td>
      <td>Time required to reach maximum NPY-EGFP intensity in the Golgi</td>
      <td>controlDKO</td>
      <td>3 (34)3 (28)</td>
      <td>Unpaired t-test</td>
      <td>p=0.0444 (*)</td>
    </tr>
    <tr>
      <td>5H</td>
      <td>Rate constants of NPY-EGFP export from the Golgi</td>
      <td>controlDKO</td>
      <td>3 (34)3 (30)</td>
      <td>Unpaired t-test</td>
      <td>p=0.0276 (*)</td>
    </tr>
    <tr>
      <td rowspan="2">5J</td>
      <td>% anterograde DCVs</td>
      <td>controlDKO</td>
      <td>2 (12)2 (12)</td>
      <td>Unpaired t-test</td>
      <td>p=0.9488</td>
    </tr>
    <tr>
      <td>% retrograde DCVs</td>
      <td>controlDKO</td>
      <td>2 (12)2 (12)</td>
      <td>Unpaired t-test</td>
      <td>p=0.7938</td>
    </tr>
    <tr>
      <td>5K</td>
      <td>Speed of anterogradely trafficking DCVs</td>
      <td>controlDKO</td>
      <td>2 (11)2 (12)</td>
      <td>Unpaired t-test</td>
      <td>p=0.8107</td>
    </tr>
    <tr>
      <td>6A</td>
      <td>mRNA expression of Bdnf transcript isoforms</td>
      <td>DKO (logFC relative to control)</td>
      <td>8 cultures</td>
      <td>One sample t-test (compare to log2FC = 0)</td>
      <td>ptotal = 0.0003 (***)ptr1=0.0006 (***)ptr2=0.0032 (**)ptr4 &lt;0.0001 (****)ptr6=0.1183ptr9=0.0012 (**)</td>
    </tr>
    <tr>
      <td>6B</td>
      <td>mRNA expression of general DCV cargos</td>
      <td>DKO (logFC relative to control)</td>
      <td>8 cultures</td>
      <td>One sample t-test (compare to log2FC = 0)</td>
      <td>p VgfVgf 0.0006 (***)p Pcsk1Pcsk10.0006 (***)p PamPam 0.0032 (**)p PtprnPtprn 0.0187 (*)p Scg2Scg20.0177 (*)</td>
    </tr>
    <tr>
      <td>6C</td>
      <td>mRNA expression of general DCV cargos</td>
      <td>DKO (logFC relative to control)</td>
      <td>8 cultures</td>
      <td>One sample t-test (compare to log2FC = 0)</td>
      <td>p NpyNpy 0.0002 (***)p CckCck 0.0016 (**)p GrpGrp 0.0003 (***)p SstSst 0.6986p Tac1Tac10.0201 (*)p PnocPnoc 0.0023 (**)p VipVip 0.7972p PdynPdyn 0.8905p PenkPenk 0.4408p CortCort 0.0267 (*)</td>
    </tr>
    <tr>
      <td>6D</td>
      <td>mRNA expression of DCV cargos upon tomosyn re-expression</td>
      <td>DKODKO +tom</td>
      <td>3 cultures</td>
      <td>Paired t-test on log2FC</td>
      <td>p Bdnf-tr1Bdnf-tr10.5453p Bdnf-tr4Bdnf-tr40.4470pVgf = 0.6284p Pcsk1Pcsk10.4625p GrpGrp 0.2974</td>
    </tr>
    <tr>
      <td rowspan="2">6E</td>
      <td rowspan="2">Effect of Cre on DCV cargo mRNA expression in Stxbp5/5llox and WT neurons</td>
      <td>ΔCre - Stxbp5/5lloxCre - Stxbp5/5llox</td>
      <td>3 cultures</td>
      <td>Paired t-test on log2FC</td>
      <td>p Bdnf-tr1Bdnf-tr10.0274 (*)pVgf = 0.0115 (*)p Pcsk1Pcsk10.0039 (**)p GrpGrp 0.0062 (**)p GapdhGapdh 0.2759</td>
    </tr>
    <tr>
      <td>ΔCre - WTCre - WT</td>
      <td>3 cultures</td>
      <td>Paired t-test on log2FC</td>
      <td>p Bdnf-tr1Bdnf-tr10.0160 (*)pVgf = 0.0057 (**)p Pcsk1Pcsk10.0040 (**)p GrpGrp 0.0041 (**)p GapdhGapdh 0.3046</td>
    </tr>
    <tr>
      <td rowspan="2">6G</td>
      <td>Band intensities of BDNF (WB)</td>
      <td>ΔCreCre</td>
      <td>3 (3)</td>
      <td>Paired t-test</td>
      <td>p=0.0476 (*)</td>
    </tr>
    <tr>
      <td>Band intensities of tomosyn (WB)</td>
      <td>ΔCreCre</td>
      <td>3 (3)</td>
      <td>Paired t-test</td>
      <td>p=0.7470</td>
    </tr>
    <tr>
      <td>6 suppl 2B</td>
      <td>Intensity of NPY-pHluorin (ICC)</td>
      <td>ΔCreCre</td>
      <td>3 (18)</td>
      <td>Unpaired t-test</td>
      <td>p=0.8022</td>
    </tr>
    <tr>
      <td></td>
      <td>Intensity of tomosyn (ICC)</td>
      <td>ΔCreCre</td>
      <td>3 (18)</td>
      <td>Unpaired t-test</td>
      <td>p=0.7105</td>
    </tr>
  </tbody>
</table>

_*n-number is the number of independent culture preparations. The number of individual observations (e.g. neurons or lanes) is provided in brackets._

### Materials availability

All DNA constructs and mouse models used in this study are available upon request. Requests should be directed to the lead contact, Matthijs Verhage (m.verhage@vu.nl).
