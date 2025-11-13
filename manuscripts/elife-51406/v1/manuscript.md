# Proteome profile of peripheral myelin in healthy mice and in a neuropathy model

## Authors

- Sophie B Siems<sup>1</sup>
- Olaf Jahn<sup>2</sup> ([ORCID: 0000-0002-3397-8924](https://orcid.org/0000-0002-3397-8924))
- Maria A Eichel<sup>1</sup>
- Nirmal Kannaiyan<sup>3</sup>
- Lai Man N Wu<sup>4</sup>
- Diane L Sherman<sup>4</sup>
- Kathrin Kusch<sup>1</sup> ([ORCID: 0000-0002-5079-502X](https://orcid.org/0000-0002-5079-502X))
- Dörte Hesse<sup>2</sup>
- Ramona B Jung<sup>1</sup>
- Robert Fledrich<sup>1</sup>
- Michael W Sereda<sup>1</sup>
- Moritz J Rossner<sup>3</sup>
- Peter J Brophy<sup>4</sup>
- Hauke B Werner<sup>1</sup> ([ORCID: 0000-0002-7710-5738](https://orcid.org/0000-0002-7710-5738)) †

### Affiliations

1. Department of Neurogenetics, Max Planck Institute of Experimental Medicine Göttingen Germany
2. Proteomics Group, Max Planck Institute of Experimental Medicine Göttingen Germany
3. Department of Psychiatry and Psychotherapy, University Hospital, LMU Munich Munich Germany
4. Centre for Discovery Brain Sciences, University of Edinburgh Edinburgh United Kingdom
5. Institute of Anatomy, University of Leipzig Leipzig Germany
6. Department of Clinical Neurophysiology, University Medical Center Göttingen Germany

† Corresponding author

## Abstract

Proteome and transcriptome analyses aim at comprehending the molecular profiles of the brain, its cell-types and subcellular compartments including myelin. Despite the relevance of the peripheral nervous system for normal sensory and motor capabilities, analogous approaches to peripheral nerves and peripheral myelin have fallen behind evolving technical standards. Here we assess the peripheral myelin proteome by gel-free, label-free mass-spectrometry for deep quantitative coverage. Integration with RNA-Sequencing-based developmental mRNA-abundance profiles and neuropathy disease genes illustrates the utility of this resource. Notably, the periaxin-deficient mouse model of the neuropathy Charcot-Marie-Tooth 4F displays a highly pathological myelin proteome profile, exemplified by the discovery of reduced levels of the monocarboxylate transporter MCT1/SLC16A1 as a novel facet of the neuropathology. This work provides the most comprehensive proteome resource thus far to approach development, function and pathology of peripheral myelin, and a straightforward, accurate and sensitive workflow to address myelin diversity in health and disease.

## Introduction

The ensheathment of axons with myelin enables rapid impulse propagation, a prerequisite for normal motor and sensory capabilities of vertebrates (Weil et al., 2018; Hartline and Colman, 2007). This is illustrated by demyelinating neuropathies of the Charcot-Marie-Tooth (CMT) spectrum, in which mutations affecting myelin genes as MPZ, PMP22, GJB1 and PRX impair myelin integrity and reduce the velocity of nerve conduction in the peripheral nervous system (PNS) (Rossor et al., 2013). Developmentally, myelination by Schwann cells in peripheral nerves is regulated by axonal neuregulin-1 (Michailov et al., 2004; Taveggia et al., 2005) and the basal lamina (Chernousov et al., 2008; Petersen et al., 2015; Ghidinelli et al., 2017) that is molecularly linked to the abaxonal Schwann cell membrane via integrins and the dystroglycan complex (Sherman et al., 2001; Masaki et al., 2002; Nodari et al., 2008; Raasakka et al., 2019). In adulthood, the basal lamina continues to enclose all axon/myelin-units (Hess and Lansing, 1953), probably to maintain myelin. Beyond regulation by extracellular cues, myelination involves multiple proteins mediating radial sorting of axons out of Remak bundles, myelin membrane growth and layer compaction (Sherman and Brophy, 2005; Pereira et al., 2012; Grove and Brophy, 2014; Monk et al., 2015; Feltri et al., 2016). For example, the Ig-domain containing myelin protein zero (MPZ; also termed P0) mediates adhesion between adjacent extracellular membrane surfaces in compact myelin (Giese et al., 1992). At their intracellular surfaces, myelin membranes are compacted by the cytosolic domain of MPZ/P0 together with myelin basic protein (MBP; previously termed P1) (Martini et al., 1995; Nawaz et al., 2013). Not surprisingly, MPZ/P0 and MBP were early identified as the most abundant peripheral myelin proteins (Greenfield et al., 1973; Brostoff et al., 1975).

A system of cytoplasmic channels through the otherwise compacted myelin sheath remains non-compacted throughout life, that is the adaxonal myelin layer, paranodal loops, Schmidt-Lanterman incisures (SLI), and abaxonal longitudinal and transverse bands of cytoplasm termed bands of Cajal (Sherman and Brophy, 2005; Nave and Werner, 2014; Kleopa and Sargiannidou, 2015). Non-compacted myelin comprises cytoplasm, cytoskeletal elements, vesicles and lipid-modifying enzymes, and thus numerous proteins involved in maintaining the myelin sheath. The cytosolic channels probably also represent transport routes toward Schwann cell-dependent metabolic support of myelinated axons (Court et al., 2004; Beirowski et al., 2014; Domènech-Estévez et al., 2015; Kim et al., 2016; Gonçalves et al., 2017; Stassart et al., 2018).

Considering that Schwann cells constitute a major proportion of the cells in the PNS, oligonucleotide microarray analyses have been used for mRNA abundance profiling of total sciatic nerves (Nagarajan et al., 2002; Le et al., 2005). Indeed, these systematic approaches allowed the identification of novel myelin constituents including non-compact myelin-associated protein (NCMAP/MP11) (Ryu et al., 2008). Notwithstanding that the number of known peripheral myelin proteins has grown in recent years, a comprehensive molecular inventory has been difficult to achieve because applications of systematic (‘omics’) approaches specifically to Schwann cells and peripheral myelin remained comparatively scarce, different from studies addressing oligodendrocytes and CNS myelin (Zhang et al., 2014; Patzig et al., 2016b; Sharma et al., 2015; Thakurela et al., 2016; Marques et al., 2016; de Monasterio-Schrader et al., 2012). One main reason may be that the available techniques were not sufficiently straightforward for general application. For example, the protein composition of peripheral myelin was previously assessed by proteome analysis (Patzig et al., 2011). However, at that time the workflow of sample preparation and data acquisition (schematically depicted in Figure 1A) was very labor-intense and required a substantial amount of input material; yet the depth of the resulting datasets remained limited. In particular, differential myelin proteome analysis by 2-dimensional fluorescence intensity gel electrophoresis (2D-DIGE) requires considerable hands-on-time and technical expertise (Patzig et al., 2011; Kangas et al., 2016). While this method is powerful for the separation of proteoforms (Kusch et al., 2017), it typically suffers from under-representation of highly basic and transmembrane proteins. It thus allows comparing the abundance of only few myelin proteins rather than quantitatively covering the entire myelin proteome. Because of these limitations and an only modest sample-to-sample reproducibility, 2D-DIGE analysis of myelin, although unbiased, has not been commonly applied beyond specialized laboratories.

![Figure 1.](https://cdn.elifesciences.org/articles/51406/elife-51406-fig1-v1.jpg)

**Figure 1.:** (A) Schematic illustration of a previous approach to the peripheral myelin proteome (Patzig et al., 2011) compared with the present workflow. Note that the current workflow allows largely automated sample processing and omits labor-intense 2-dimensional differential gel-electrophoresis, thereby considerably reducing hands-on time. Nano LC-MS analysis by data-independent acquisition (DIA) using three different data acquisition modes provides efficient identification and quantification of abundant myelin proteins (MSE; see Figure 2), a comprehensive inventory (UDMSE; see Figures 3–4) and gel-free differential analysis of hundreds of distinct proteins (DRE-UDMSE; see Figure 5). Samples were analyzed in three biological replicates. (B) Immunoblot of myelin biochemically enriched from sciatic nerves of wild-type mice at postnatal day 21 (P21). Equal amounts of corresponding nerve lysate were loaded to compare the abundance of marker proteins for compact myelin (MPZ/P0, MBP, PMP2), non-compact myelin (PRX), the Schwann cell nucleus (KROX20/EGR2), axons (NEFH, KCNA1) and mitochondria (VDAC). Blots show n = 2 biological replicates representative of n = 3 biological replicates. Note that myelin markers are enriched in purified myelin; other cellular markers are reduced. (C) Number and relative abundance of proteins identified in myelin purified from the sciatic nerves of wild-type mice using three different data acquisition modes (MSE, UDMSE, DRE-UDMSE). Note that MSE (orange) provides the best information about the relative abundance of high-abundant myelin proteins (dynamic range of more than four orders of magnitude) but identifies comparatively fewer proteins in purified myelin. UDMSE (blue) identifies the largest number of proteins but provides only a lower dynamic range of about three orders of magnitude. DRE-UDMSE (green) identifies an intermediate number of proteins with an intermediate dynamic range of about four orders of magnitude. Note that MSE with very high dynamic range is required for the quantification of the exceptionally abundant myelin protein zero (MPZ/P0), myelin basic protein (MBP) and periaxin (PRX). ppm, parts per million. (D) Venn diagram comparing the number of proteins identified in PNS myelin by MSE, UDMSE and DRE-UDMSE. Note the high overlap of identified proteins. (E) Venn diagram of the proteins identified in PNS myelin by UDMSE in this study compared with those identified in two previous approaches (Patzig et al., 2011; Kangas et al., 2016).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/51406/elife-51406-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** The heatmap compares the log2 transformed ppm protein abundance values to assess peripheral myelin purified from wild type mice using three data acquisition modes (MSE, UDMSE, DRE-UDMSE). The inset shows the color key and the histogram for the values of the correlation coefficients. Note that the runs cluster with a high overall correlation (>0.75) into three conditions defined by the acquisition mode, in agreement with the experimental design. Among the samples analyzed by different acquisition modes, DRE-UDMSE similarly correlates with both MSE and UDMSE, reflecting its intermediate nature.

The aim of the present study was to establish a straightforward and readily applicable workflow to facilitate both comprehensive knowledge about the protein composition of peripheral myelin and systematic assessment of differences between two states, for example, pathological alterations in a neuropathy model. The major prerequisites were the biochemical purification of myelin, its solubilization with the detergent ASB-14 and the subsequent automated digestion with trypsin during filter-aided sample preparation (FASP). The tryptic peptides were fractionated by liquid chromatography and analyzed by mass spectrometry for gel-free, label-free quantitative proteome analysis. More specifically, we used nano-flow ultra-performance liquid chromatography (nanoUPLC) coupled to an electrospray-ionization quadrupole time-of-flight (ESI-QTOF) mass spectrometer with ion mobility option, providing an orthogonal dimension of peptide separation. The utilized data-independent acquisition (DIA) strategy relies on collecting data in an alternating low and elevated energy mode (MSE); it enables simultaneous sequencing and quantification of all peptides entering the mass spectrometer without prior precursor selection, as reviewed in Neilson et al. (2011) and Distler et al. (2014a). With their high-duty cycle utilized for the acquisition of precursor ions, MSE-type methods are ideally suited to reliably quantify proteins based on peptide intensities. Notably, these methods do not involve the use of spectral libraries in the identification of proteins, different from other DIA strategies. Instead, the achieved high-complexity fragmentation spectra are deconvoluted before submission to dedicated search engines for peptide and protein identification (Geromanos et al., 2009; Li et al., 2009). In the MSE mode, this deconvolution involves precursor-fragment ion alignment solely on the basis of chromatographic elution profiles. On top, drift times of ion mobility-separated precursors are used in the high-definition (HD)MSE mode. An expansion of the latter, referred to as the ultra-definition (UD)MSE mode, additionally implements drift time-dependent collision energy profiles for more effective precursor fragmentation (Distler et al., 2016; Distler et al., 2014b).

Indeed, compared to the previously used manual handling and in-gel digestion, the current workflow (schematically depicted in Figure 1A) is considerably less labor-intense, and automated FASP increases sample-to-sample reproducibility. Moreover, differential analysis by quantitative mass spectrometry (MS) facilitates reproducible quantification of hundreds rather than a few distinct myelin proteins. Together, the present workflow increases the efficacy of assessing the peripheral myelin proteome while shifting the main workload from manual sample preparation and gel-separation to automated acquisition and processing of data. We propose that comprehending the expression profiles of all myelin proteins in the healthy PNS and in myelin-related disorders can contribute to advancing our understanding of the physiology and pathophysiology of peripheral nerves.

## Results

### Purification of peripheral myelin

We biochemically enriched myelin as a light-weight membrane fraction from pools of sciatic nerves dissected from mice at postnatal day 21 (P21) using an established protocol of discontinuous sucrose density gradient centrifugation (Patzig et al., 2011; Larocca and Norton, 2006), in which myelin membranes accumulate at the interface between 0.29 and 0.85 M sucrose. By immunoblotting, proteins specific for both compact (MPZ/P0, MBP, PMP2) and non-compact (PRX) myelin were substantially enriched in the myelin fraction compared to nerve lysates (Figure 1B). Conversely, axonal (NEFH, KCNA1) and mitochondrial (VDAC) proteins and a marker for the Schwann cell nucleus (KROX20/EGR2) were strongly reduced in purified myelin. Together, these results imply that biochemically purified peripheral myelin is suitable for systematic analysis of its protein composition.

### Proteome analysis of peripheral myelin

It has long been difficult to accurately quantify the most abundant myelin proteins both in the CNS (PLP, MBP, CNP; Jahn et al., 2009) and the PNS (MPZ/P0, MBP, PRX; this work), probably owing to their exceptionally high relative abundance. For example, the major CNS myelin constituents PLP, MBP and CNP comprise 17, 8 and 4% of the total myelin protein, respectively (Jahn et al., 2009). We have recently provided proof of principle (Erwig et al., 2019a) that the mass spectrometric quantification of these high-abundant myelin proteins is accurate and precise when data are acquired in the MSE data acquisition mode and proteins are quantified according to the TOP3 method, that is if their abundance values are obtained based on the proven correlation between the average intensity of the three peptides exhibiting the most intense mass spectrometry response and the absolute amount of their source protein (Silva et al., 2006; Ahrné et al., 2013). Using data acquisition by MSE we confirmed that CNP constitutes about 4% of the total CNS myelin proteome and that the abundance of CNP in myelin from mice heterozygous for the Cnp gene (CnpWT/null) compared to wild-type mice is 50.7% (±0.4%), in agreement with the halved gene dosage and gel-based quantification by silver staining or immunoblotting (Erwig et al., 2019a).

When applying the MSE mode to PNS myelin, we quantified 351 proteins with a false discovery rate (FDR) of <1% at peptide and protein level and an average sequence coverage of 35.5% (Figure 1—source data 1). While MSE (labeled in orange in Figure 1C) indeed provided a dynamic range of more than four orders of magnitude and thus quantitatively covered the exceptionally abundant myelin proteins MPZ/P0, MBP and PRX, the number of quantified proteins appeared limited when spectral complexity was deconvoluted solely on the basis of chromatographic elution profiles. Accordingly, by using the UDMSE mode, which comprises ion mobility for additional peptide separation as well as drift time-specific collision energies for peptide fragmentation, proteome coverage was increased about three-fold (1078 proteins quantified; average sequence coverage 34.3%; Figure 1—source data 1). However, the dynamic range of UDMSE (labeled in blue in Figure 1C) was found to be somewhat compressed compared to that of MSE, which can be considered an expectable feature of traveling wave ion mobility devices (Dodds and Baker, 2019), where the analysis of pulsed ion packages leads to a temporal and spatial binning of peptides during ion mobility separation. Indeed, this manifests as a ceiling effect for the detection of exceptionally intense peptide signals, which results in an underestimation of the relative abundance of MPZ/P0, MBP and PRX by UDMSE.

The complementary nature of the MSE and UDMSE data acquisition modes led us to conclude that a comprehensive analysis of the myelin proteome that facilitates both correct quantification of the most abundant proteins and deep quantitative coverage of the proteome would require analyzing the same set of samples with two different instrument settings for MSE and UDMSE, respectively. Considering that instrument time is a bottleneck for the routine differential proteome analysis of myelin from mutant mice, we aimed to combine the strengths of MSE and UDMSE into a single data acquisition mode. Based on a gene ontology enrichment analysis for cellular components of the 200 proteins of highest and lowest abundance from the UDMSE dataset, we realized that the ‘bottom ‘of the quantified proteome is probably largely unrelated to myelin but dominated by contaminants from other subcellular sources including mitochondria. We thus reasoned that for a myelin-directed data acquisition mode, proteome depth may be traded in for a gain in dynamic range and devised a novel method referred to as dynamic range enhancement (DRE)-UDMSE, in which a deflection lens is used to cycle between full and reduced ion transmission during mass spectrometric scanning. Indeed, DRE-UDMSE quantified an intermediate number of proteins in PNS myelin (554 proteins; average sequence coverage 30.6%; Figure 1—source data 1) while providing an intermediate dynamic range (labeled in green in Figure 1C). We thus consider DRE-UDMSE as the data acquisition mode of choice most suitable for routine differential myelin proteome profiling (see below).

Overall, we found a high reproducibility between replicates and even among the different data acquisition modes as indicated by Pearson’s correlation coefficients for protein abundance in the range of 0.765–0.997 (Figure 1—figure supplement 1). When comparing the proteins identified in PNS myelin using the three data acquisition modes, we found a very high overlap (Figure 1D). We also found a high overlap (Figure 1E) between the proteins identified in the present study by UDMSE and those detected in previous proteomic approaches to PNS myelin (Patzig et al., 2011; Kangas et al., 2016), thus allowing a high level of confidence. Together, the three data acquisition modes exhibit distinct strengths in the efficient quantification of exceptionally abundant proteins (MSE), establishing a comprehensive inventory (UDMSE) and gel-free, label-free differential analysis of hundreds of distinct proteins (DRE-UDMSE) in peripheral myelin (see Figure 1A). Yet, analyzing the same set of samples by different modes may not always be feasible in all routine applications when considering required instrument time.

### Relative abundance of peripheral myelin proteins

Considering that MSE provides the high dynamic range required for the quantification of the most abundant myelin proteins, we calculated the relative abundance of the 351 proteins identified in myelin by MSE (Figure 1—source data 1). According to quantitative assessment of this dataset, the most abundant PNS myelin protein, myelin protein zero (MPZ/P0), constitutes 44% (+/- 4% relative standard deviation (RSD)) of the total myelin protein (Figure 2). Myelin basic protein (MBP), periaxin (PRX) and tetraspanin-29 (CD9) constitute 18% (+/- 1% RSD), 15% (+/- 1%) and 1% (+/- 0.2%) of the total myelin protein, respectively (Figure 2). For MPZ/P0 and MBP, our quantification by MSE is in agreement with but specifies prior estimations upon gel-separation and protein labeling by Sudan-Black, Fast-Green or Coomassie-Blue, in which they were judged to constitute 45–70% and 2–26% of the total myelin protein, respectively (Greenfield et al., 1973; Micko and Schlaepfer, 1978; Smith and Curtis, 1979; Whitaker, 1981). However, gel-based estimates of the relative abundance of myelin proteins were not very precise with respect to many other proteins, including those of high molecular weight. Indeed, periaxin was identified as a constituent of peripheral myelin after the advent of gradient SDS-PAGE gels (Gillespie et al., 1994), which allowed improved migration of large proteins into gels. The present MSE-based quantification of myelin proteins also extends beyond and partially adjusts an earlier mass spectrometric approach (Patzig et al., 2011). Indeed, the current approach identified and quantified more myelin proteins, probably owing to improved protein solubilization during sample preparation and higher dynamic range of the used mass spectrometer. By MSE, known myelin proteins (Table 1) collectively constitute over 85% of the total myelin protein (Figure 2) while proteins not yet associated with myelin account for the remaining 15% of the total myelin protein.

![Figure 2.](https://cdn.elifesciences.org/articles/51406/elife-51406-fig2-v1.jpg)

**Figure 2.:** MSE was used to identify and quantify proteins in myelin purified from the sciatic nerves of wild-type mice at P21; their relative abundance is given as percent with relative standard deviation (% +/- RSD). Note that known myelin proteins constitute >80% of the total myelin protein; proteins not previously associated with myelin constitute <20%. Mass spectrometric quantification based on 3 biological replicates per genotype with 4 technical replicates each (see Figure 1—source data 1).

**Table 1.**
 Known myelin proteins in the myelin proteome.Proteins mass-spectrometrically identified in peripheral myelin are compiled according to availability of prior references as myelin proteins. Given are the official gene name, one selected reference, the number of transmembrane domains (TMD) and the mRNA abundance profile cluster (see Figure 3).


<table>
  <thead>
    <tr>
      <th>Protein name</th>
      <th>Gene</th>
      <th>Reference</th>
      <th>TMD</th>
      <th>Cluster</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2-hydroxyacylsphingosine 1-beta-galactosyltransferase</td>
      <td>Ugt8</td>
      <td>Bosio et al., 1996</td>
      <td>2</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Syntrophin α1</td>
      <td>Snta1</td>
      <td>Fuhrmann-Stroissnigg et al., 2012</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Annexin A2</td>
      <td>Anxa2</td>
      <td>Hayashi et al., 2007</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Band 4.1 protein B/4.1B</td>
      <td>Epb41l3</td>
      <td>Ivanovic et al., 2012</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Band 4.1 protein G/4.1G</td>
      <td>Epb41l2</td>
      <td>Ohno et al., 2006</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Breast carcinoma-amplified sequence 1</td>
      <td>Bcas1</td>
      <td>Ishimoto et al., 2017</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Cadherin 1/E-Cadherin</td>
      <td>Cdh1</td>
      <td>Fannon et al., 1995</td>
      <td>1</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Carbonic anhydrase 2</td>
      <td>Ca2</td>
      <td>Cammer and Tansey, 1987</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Catenin α1</td>
      <td>Ctnna1</td>
      <td>Murata et al., 2006</td>
      <td>-</td>
      <td>U-shaped</td>
    </tr>
    <tr>
      <td>Catenin ß1</td>
      <td>Ctnnb1</td>
      <td>Fannon et al., 1995</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Caveolin 1</td>
      <td>Cav1</td>
      <td>Mikol et al., 2002</td>
      <td>1</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>CD9, tetraspanin 29</td>
      <td>Cd9</td>
      <td>Ishibashi et al., 2004</td>
      <td>4</td>
      <td>P18-p</td>
    </tr>
    <tr>
      <td>CD59A</td>
      <td>Cd59a</td>
      <td>Funabashi et al., 1994</td>
      <td>1</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>CD47, integrin-associated signal transducer</td>
      <td>Cd47</td>
      <td>Gitik et al., 2011</td>
      <td>5</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>CD81, tetraspanin 28</td>
      <td>Cd81</td>
      <td>Ishibashi et al., 2004</td>
      <td>4</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>CD82, tetraspanin 27</td>
      <td>Cd82</td>
      <td>Chernousov et al., 2013</td>
      <td>4</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>CD151, tetraspanin 24</td>
      <td>Cd151</td>
      <td>Patzig et al., 2011</td>
      <td>4</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Cell adhesion molecule 4/NECL4</td>
      <td>Cadm4</td>
      <td>Spiegel et al., 2007</td>
      <td>1</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Cell division control protein 42</td>
      <td>Cdc42</td>
      <td>Benninger et al., 2007</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Cell surface glycoprotein MUC18</td>
      <td>Mcam</td>
      <td>Shih et al., 1998</td>
      <td>1</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Ciliary neurotrophic factor</td>
      <td>Cntf</td>
      <td>Rende et al., 1992</td>
      <td>-</td>
      <td>Late-up</td>
    </tr>
    <tr>
      <td>CKLF-like MARVEL TMD-containing 5</td>
      <td>Cmtm5</td>
      <td>Patzig et al., 2011</td>
      <td>4</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Claudin-19</td>
      <td>Cldn19</td>
      <td>Miyamoto et al., 2005</td>
      <td>4</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Cofilin 1</td>
      <td>Cfl1</td>
      <td>Sparrow et al., 2012</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Crystallin α2</td>
      <td>Cryab</td>
      <td>D'Antonio et al., 2006</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Cyclic nucleotide phosphodiesterase</td>
      <td>Cnp</td>
      <td>Matthieu et al., 1980</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Sarcoglycan δ</td>
      <td>Sgcd</td>
      <td>Cai et al., 2007</td>
      <td>1</td>
      <td>Late-up</td>
    </tr>
    <tr>
      <td>Dihydropyrimidinase related protein 1</td>
      <td>Crmp1</td>
      <td>D'Antonio et al., 2006</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Disks large homolog 1</td>
      <td>Dlg1</td>
      <td>Cotter et al., 2010</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Dynein light chain 1</td>
      <td>Dynll1</td>
      <td>Myllykoski et al., 2018</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Dystroglycan</td>
      <td>Dag1</td>
      <td>Yamada et al., 1994</td>
      <td>1</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Dystrophin/DP116</td>
      <td>Dmd</td>
      <td>Cai et al., 2007</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Dystrophin-related protein 2</td>
      <td>Drp2</td>
      <td>Sherman et al., 2001</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>E3 ubiquitin-protein ligase NEDD4</td>
      <td>Nedd4</td>
      <td>Liu et al., 2009</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Ezrin</td>
      <td>Ezr</td>
      <td>Scherer et al., 2001</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Fatty acid synthase</td>
      <td>Fasn</td>
      <td>Salles et al., 2002</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Flotillin 1</td>
      <td>Flot1</td>
      <td>Lee et al., 2014</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Gap junction ß1 protein/Cx32</td>
      <td>Gjb1</td>
      <td>Li et al., 2002</td>
      <td>4</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Gap junction γ3 protein/Cx29</td>
      <td>Gjc3</td>
      <td>Li et al., 2002</td>
      <td>1</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Gelsolin</td>
      <td>Gsn</td>
      <td>Gonçalves et al., 2010</td>
      <td>-</td>
      <td>Late-up</td>
    </tr>
    <tr>
      <td>Glycogen synthase kinase 3ß</td>
      <td>Gsk3b</td>
      <td>Ogata et al., 2004</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Integrin α6</td>
      <td>Itga6</td>
      <td>Nodari et al., 2008</td>
      <td>1</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Integrin αV</td>
      <td>Itgav</td>
      <td>Chernousov and Carey, 2003</td>
      <td>1</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Integrin ß1</td>
      <td>Itgb1</td>
      <td>Feltri et al., 2002</td>
      <td>1</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Integrin ß4</td>
      <td>Itgb4</td>
      <td>Quattrini et al., 1996</td>
      <td>2</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Junctional adhesion molecule C</td>
      <td>Jam3</td>
      <td>Scheiermann et al., 2007</td>
      <td>1</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Laminin α2</td>
      <td>Lama2</td>
      <td>Yang et al., 2005</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Laminin α4</td>
      <td>Lama4</td>
      <td>Yang et al., 2005</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Laminin ß1</td>
      <td>Lamb1</td>
      <td>LeBeau et al., 1994</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Laminin ß2</td>
      <td>Lamb2</td>
      <td>LeBeau et al., 1994</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Laminin γ1</td>
      <td>Lamc1</td>
      <td>Chen and Strickland, 2003</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Membrane Palmitoylated Protein 6</td>
      <td>Mpp6</td>
      <td>Saitoh et al., 2019</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Microtubule-associated protein 1A</td>
      <td>Map1a</td>
      <td>Fuhrmann-Stroissnigg et al., 2012</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Microtubule-associated protein 1B</td>
      <td>Map1b</td>
      <td>Fuhrmann-Stroissnigg et al., 2012</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Mitogen-activated protein kinase 1/ERK2</td>
      <td>Mapk1</td>
      <td>Mantuano et al., 2015</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Mitogen-activated protein kinase 3/ERK1</td>
      <td>Mapk3</td>
      <td>Mantuano et al., 2015</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Moesin</td>
      <td>Msn</td>
      <td>Scherer et al., 2001</td>
      <td>-</td>
      <td>Unchanged</td>
    </tr>
    <tr>
      <td>Monocarboxylate transporter 1</td>
      <td>Slc16a1</td>
      <td>Domènech-Estévez et al., 2015</td>
      <td>11</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Myelin associated glycoprotein</td>
      <td>Mag</td>
      <td>Figlewicz et al., 1981</td>
      <td>1</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Myelin basic protein</td>
      <td>Mbp</td>
      <td>Boggs, 2006</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Myelin protein 2</td>
      <td>Pmp2</td>
      <td>Trapp et al., 1984</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Myelin protein zero/P0</td>
      <td>Mpz</td>
      <td>Giese et al., 1992</td>
      <td>1</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Myelin proteolipid protein</td>
      <td>Plp1</td>
      <td>Garbern et al., 1997</td>
      <td>4</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Myotubularin-related protein 2</td>
      <td>Mtmr2</td>
      <td>Bolino et al., 2004</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Noncompact myelin-associated protein</td>
      <td>Ncmap</td>
      <td>Ryu et al., 2008</td>
      <td>1</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>NDRG1, N-myc downstream regulated</td>
      <td>Ndrg1</td>
      <td>Berger et al., 2004</td>
      <td>-</td>
      <td>P18-uP</td>
    </tr>
    <tr>
      <td>Neurofascin</td>
      <td>Nfasc</td>
      <td>Tait et al., 2000</td>
      <td>2</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Nidogen 1</td>
      <td>Nid1</td>
      <td>Lee et al., 2007</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>P2X purinoceptor 7</td>
      <td>P2r×7</td>
      <td>Faroni et al., 2014</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Paxillin</td>
      <td>Pxn</td>
      <td>Fernandez-Valle et al., 2002</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Periaxin</td>
      <td>Prx</td>
      <td>Gillespie et al., 1994</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Plasmolipin</td>
      <td>Pllp</td>
      <td>Bosse et al., 2003</td>
      <td>4</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Profilin 1</td>
      <td>Pfn1</td>
      <td>Montani et al., 2014</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Lin-7 homolog C</td>
      <td>Lin7c</td>
      <td>Saitoh et al., 2017</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Rac1</td>
      <td>Rac1</td>
      <td>Benninger et al., 2007</td>
      <td>-</td>
      <td>U-Shaped</td>
    </tr>
    <tr>
      <td>Radixin</td>
      <td>Rdx</td>
      <td>Scherer et al., 2001</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>RhoA</td>
      <td>Rhoa</td>
      <td>Brancolini et al., 1999</td>
      <td>-</td>
      <td>U-Shaped</td>
    </tr>
    <tr>
      <td>Septin 2</td>
      <td>Sept2</td>
      <td>Buser et al., 2009</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Septin 7</td>
      <td>Sept7</td>
      <td>Buser et al., 2009</td>
      <td>-</td>
      <td>U-Shaped</td>
    </tr>
    <tr>
      <td>Septin 8</td>
      <td>Sept8</td>
      <td>Patzig et al., 2011</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Septin 9</td>
      <td>Sept9</td>
      <td>Patzig et al., 2011</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Septin 11</td>
      <td>Sept11</td>
      <td>Buser et al., 2009</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
    <tr>
      <td>Sirtuin 2, NAD-dependent deacetylase</td>
      <td>Sirt2</td>
      <td>Werner et al., 2007</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Spectrin alpha chain, non-erythrocytic 1</td>
      <td>Sptan1</td>
      <td>Susuki et al., 2018</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Spectrin beta chain, non-erythrocytic 1</td>
      <td>Sptbn1</td>
      <td>Susuki et al., 2018</td>
      <td>-</td>
      <td>P18-up</td>
    </tr>
    <tr>
      <td>Tight junction protein ZO-1</td>
      <td>Tjp1</td>
      <td>Poliak et al., 2002</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Tight junction protein ZO-2</td>
      <td>Tjp2</td>
      <td>Poliak et al., 2002</td>
      <td>-</td>
      <td>P6-up</td>
    </tr>
    <tr>
      <td>Transferrin</td>
      <td>Tf</td>
      <td>Lin et al., 1990</td>
      <td>2</td>
      <td>Late-up</td>
    </tr>
    <tr>
      <td>Vimentin</td>
      <td>Vim</td>
      <td>Triolo et al., 2012</td>
      <td>-</td>
      <td>Unchanged</td>
    </tr>
    <tr>
      <td>Vinculin</td>
      <td>Vcl</td>
      <td>Beppu et al., 2015</td>
      <td>-</td>
      <td>Descending</td>
    </tr>
  </tbody>
</table>

### Comprehensive compendium and comparison to the transcriptome

To systematically elucidate the developmental abundance profiles of the transcripts that encode peripheral myelin proteins (Figure 3), we used our combined proteome inventory of peripheral myelin (Figure 1—source data 1) to filter mRNA abundance data of all genes expressed in sciatic nerves. By this strategy, Figure 3 displays only those transcripts of which the protein product was identified in peripheral myelin rather than all transcripts in the nerve, thereby discriminating myelin-related mRNAs from other mRNAs such as those present in peripheral axons, fibroblasts, immune cells etc. In this assessment we additionally included PMP22 although it was not detected by MS as well as 45 proteins exclusively identified by LC-MS of myelin separated by SDS-PAGE (Figure 1—source data 1). For mRNA abundance profiles, we exploited a recently established RNA sequencing analysis (RNA-Seq; platform Illumina HiSeq 2000) of sciatic nerves dissected form wild type Sprague Dawley rats at embryonic day 21 (E21), P6, P18 and 6 months (Fledrich et al., 2018). RNA-Seq provides reliable information about the relative abundance of all significantly expressed genes and is thus not limited to those represented on the previously used oligonucleotide microarrays (Patzig et al., 2011). The raw data (accessible under GEO accession number GSE115930) were normalized (Figure 3—source data 1) and standardized. When comparing the proteome and transcriptome datasets, significant mRNA abundance was detected for all 1046 transcripts for which an unambiguous unique gene identifier was found (Figure 3). 126 transcripts displayed developmentally unchanged abundance levels, that is, abundance changes below a threshold of 10% coefficient of variation (Figure 3B; Figure 3—source data 1).

![Figure 3.](https://cdn.elifesciences.org/articles/51406/elife-51406-fig3-v1.jpg)

**Figure 3.:** (A) K-means clustering was performed for the mRNA profiles of those 1046 proteins in our myelin proteome inventory for which significant mRNA expression was found by RNA-Seq in the sciatic nerve of rats dissected at ages E21, P6, P18 and 6 months (M6). Note that this filtering strategy allows to selectively display the developmental abundance profiles of those transcripts that encode myelin-associated proteins rather than of all transcripts present in the nerve. Standardized mRNA abundance profiles are shown (n = 4 biological replicates per age). Known myelin genes are displayed in red. For comparison, Pmp22 mRNA was included although the small tetraspan protein PMP22 was not mass spectrometrically identified due to its unfavorable distribution of tryptic cleavage sites. Normalized counts for all mRNAs including those displaying developmentally unchanged abundance are provided in Figure 3—source data 1. (B) Numbers of mRNAs per cluster.

By fuzzy c-means clustering, those 920 transcripts that showed developmental abundance changes were grouped into 5 clusters (Figure 3A; Figure 3—source data 1). Among those, one cluster corresponds to an mRNA-abundance peak coinciding with an early phase of myelin biogenesis (cluster ‘P6-UP‘), which includes the highest proportion of known myelin proteins (Table 1) such as MPZ/P0, MBP, PRX, cyclic nucleotide phosphodiesterase (CNP), fatty acid synthase (FASN), myelin-associated glycoprotein (MAG), proteolipid protein (PLP/DM20), cell adhesion molecule-4 (CADM4/NECL4), connexin-29 (GJC3), claudin-19 (CLDN19) and CKLF-like MARVEL-transmembrane domain containing protein-5 (CMTM5). However, many known myelin proteins clustered together according to their mRNA-abundance peak coinciding with a later phase of myelination (cluster ‘P18-UP‘), including peripheral myelin protein 2 (PMP2), tetraspanin-29 (CD9), tetraspanin-28 (CD81), connexin-32 (GJB1), plasmolipin (PLLP), junctional adhesion molecule-3 (JAM3), CD59 and dystrophin-related protein-2 (DRP2). The proportion of known myelin proteins was lower in the clusters corresponding to mRNA-abundance peaks in adulthood (clusters ‘late-UP‘, ‘U-shaped‘). Yet, a considerable number of transcripts displayed abundance peaks at the embryonic time-point (cluster ‘Descending‘), including carbonic anhydrase 2 (CA2), cofilin-1 CFL1), tubulin beta-4 (TUBB4b) and band 4.1-protein B (EPB41L3). Generalized, the clusters were roughly similar when comparing previous oligonucleotide microarray analysis of mouse sciatic nerves (Patzig et al., 2011) and the RNA-Seq analysis of rat sciatic nerves (this study); yet, the latter provides information on a larger number of genes and with a higher level of confidence. Together, clustering of mRNA abundance profiles allows categorizing peripheral myelin proteins into developmentally co-regulated groups.

When systematically assessing the proteins identified in myelin by gene ontology (GO)-term analysis, the functional categories over-represented in the entire myelin proteome included cell adhesion, cytoskeleton and extracellular matrix (labeled in turquoise in Figure 4). When analyzing the clusters of developmentally co-expressed transcripts (from Figure 3), proteins associated with the lipid metabolism were particularly enriched in the P6-UP and P18-UP clusters, while those associated with the extracellular matrix (ECM) were over-represented in the U-shaped and Descending clusters (Figure 4). For comparison, known myelin proteins (Table 1) were over-represented in the P6-UP and P18-UP clusters (Figure 4). Together, our proteome dataset provides comprehensive in-depth coverage of the protein constituents of peripheral myelin purified from the sciatic nerves of wild type mice, and comparison to the transcriptome allows identifying developmentally co-regulated and functional groups of myelin proteins. Our data thus supply a solid resource for the molecular characterization of myelin and for discovering functionally relevant myelin proteins.

![Figure 4.](https://cdn.elifesciences.org/articles/51406/elife-51406-fig4-v1.jpg)

**Figure 4.:** All proteins identified in peripheral myelin by UDMSE (turquoise) and the respective developmental expression clusters (Figure 3; shades of red) were analyzed for overrepresented functional annotations using gene ontology (GO) terms. The graph displays the percentage of proteins in each cluster that were annotated with a particular function. For comparison, known myelin proteins were annotated. n.o., not over-represented.

### Neuropathy genes encoding myelin proteins

Heritable neuropathies can be caused by mutations affecting genes preferentially expressed in neurons, Schwann cells or both (Rossor et al., 2013; Pareyson and Marchesi, 2009; Baets et al., 2014; Brennan et al., 2015). To systematically assess which neuropathy-causing genes encode peripheral myelin proteins, we compared our myelin proteome dataset with a current overview about disease genes at the NIH National Library of Medicine at https://ghr.nlm.nih.gov/condition/charcot-marie-tooth-disease#genes. Indeed, 31 myelin proteins were identified to be encoded by a proven neuropathy gene (Table 2), a considerable increase compared to eight disease genes found in a similar previous approach (Patzig et al., 2011). Notably, this increase is owing to both the larger size of the current myelin proteome dataset (Figure 1E) and the recent discovery of numerous neuropathy genes by the widespread application of next generation sequencing.

**Table 2.**
 Peripheral myelin proteins identified in PNS myelin involved in neuropathological diseases.Proteins mass-spectrometically identified in peripheral myelin were analyzed regarding the involvement of the ortholog human gene in neuropathological diseases. PMP22 was added, though it was not identified by MS analyses due to its unfavorable distribution of tryptic cleavage sites. CMT, Charcot-Marie-Tooth disease; DHMN, distal hereditary motor neuropathy; DI-CMTC, dominant intermediate CMTC; DFN, X-linked deafness; HMN, hereditary motor neuropathy; HSAN, hereditary sensory and autonomic neuropathy; HNA, hereditary sensory and autonomic neuropathy; OMIM, Online Mendelian Inheritance in Man; PHARC, polyneuropathy, hearing loss, ataxia, retinitis pigmentosa and cataract; SCA, spinocerebellar ataxia; SPG, spastic paraplegia.


<table>
  <thead>
    <tr>
      <th>Protein name</th>
      <th>Gene name</th>
      <th>OMIM#</th>
      <th>Gene locus</th>
      <th>Neuropathy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Monoacylglycerol lipase ABHD12</td>
      <td>ABHD12</td>
      <td>613599</td>
      <td>20p11.21</td>
      <td>Pharc</td>
    </tr>
    <tr>
      <td>Apoptosis-inducing factor 1</td>
      <td>AIFM1</td>
      <td>300169</td>
      <td>Xq26.1</td>
      <td>CMTX4, DFNX5</td>
    </tr>
    <tr>
      <td>Na+/K+ -transporting ATPase α1</td>
      <td>ATP1A1</td>
      <td>182310</td>
      <td>1p13.1</td>
      <td>CMT2DD</td>
    </tr>
    <tr>
      <td>Cytochrome c oxidase subunit 6A1</td>
      <td>COX6A1</td>
      <td>602072</td>
      <td>12q24.31</td>
      <td>CMTRID</td>
    </tr>
    <tr>
      <td>Dystrophin-related protein 2</td>
      <td>DRP2</td>
      <td>300052</td>
      <td>Xq22.1</td>
      <td>CMTX</td>
    </tr>
    <tr>
      <td>Dynactin subunit 1</td>
      <td>DCTN1</td>
      <td>601143</td>
      <td>2p13.1</td>
      <td>DHMN7B</td>
    </tr>
    <tr>
      <td>Dynamin 2</td>
      <td>DNM2</td>
      <td>602378</td>
      <td>19p13.2</td>
      <td>CMT2M, CMTDIB</td>
    </tr>
    <tr>
      <td>Cytoplasmic dynein 1 heavy chain 1</td>
      <td>DYNC1H1</td>
      <td>600112</td>
      <td>14q32.31</td>
      <td>CMT20, SMALED1</td>
    </tr>
    <tr>
      <td>E3 SUMO-protein ligase</td>
      <td>EGR2</td>
      <td>129010</td>
      <td>10q21.3</td>
      <td>CMT1D, CMT3, CMT4E</td>
    </tr>
    <tr>
      <td>Glycine-tRNA ligase</td>
      <td>GARS (Gart)</td>
      <td>600287</td>
      <td>7p14.3</td>
      <td>CMT2D, HMN5A</td>
    </tr>
    <tr>
      <td>Gap junction ß1 protein/Cx32</td>
      <td>GJB1</td>
      <td>304040</td>
      <td>Xq13.1</td>
      <td>CMTX1</td>
    </tr>
    <tr>
      <td>Guanine nucleotide-binding protein ß4</td>
      <td>GNB4</td>
      <td>610863</td>
      <td>3q26.33</td>
      <td>CMTDIF</td>
    </tr>
    <tr>
      <td>Histidine triad nucleotide-binding protein 1</td>
      <td>HINT1</td>
      <td>601314</td>
      <td>5q23.3</td>
      <td>NMAN</td>
    </tr>
    <tr>
      <td>Hexokinase 1</td>
      <td>HK1</td>
      <td>142600</td>
      <td>10q22.1</td>
      <td>CMT4G</td>
    </tr>
    <tr>
      <td>Heat shock protein ß1</td>
      <td>HSPB1</td>
      <td>602195</td>
      <td>7q11.23</td>
      <td>CMT2F, DHMN2B</td>
    </tr>
    <tr>
      <td>Kinesin heavy chain isoform 5A</td>
      <td>KIF5A</td>
      <td>602821</td>
      <td>12q13.3</td>
      <td>SPG10</td>
    </tr>
    <tr>
      <td>Prelamin A/C</td>
      <td>LMNA</td>
      <td>150330</td>
      <td>1q22</td>
      <td>CMT2B1</td>
    </tr>
    <tr>
      <td>Neprilysin</td>
      <td>MME</td>
      <td>120520</td>
      <td>3q25.2</td>
      <td>CMT2T, SCA43</td>
    </tr>
    <tr>
      <td>Myelin protein zero/P0</td>
      <td>MPZ</td>
      <td>159440</td>
      <td>1q23.3</td>
      <td>CHN2,CMT1B, CMT2I, CMT2J,CMT3, CMTDID, Roussy-Levy syndrome</td>
    </tr>
    <tr>
      <td>Myotubularin-related protein 2</td>
      <td>MTMR2</td>
      <td>603557</td>
      <td>11q21</td>
      <td>CMT4B1</td>
    </tr>
    <tr>
      <td>Alpha-N-acetylglucosaminidase</td>
      <td>NAGLU (NAGA)</td>
      <td>609701</td>
      <td>17q21.2</td>
      <td>CMT2V</td>
    </tr>
    <tr>
      <td>NDRG1, N-myc downstream regulated</td>
      <td>NDRG1</td>
      <td>605262</td>
      <td>8q24.22</td>
      <td>CMT4D</td>
    </tr>
    <tr>
      <td>Neurofilament heavy polypeptide</td>
      <td>NEFH</td>
      <td>162230</td>
      <td>22q12.2</td>
      <td>CMT2CC</td>
    </tr>
    <tr>
      <td>Neurofilament light polypeptide</td>
      <td>NEFL</td>
      <td>162280</td>
      <td>8p21.2</td>
      <td>CMT2E, CMT1F, CMTDIG</td>
    </tr>
    <tr>
      <td>Peripheral myelin protein 2</td>
      <td>PMP2</td>
      <td>170715</td>
      <td>8q21.13</td>
      <td>CMT1G</td>
    </tr>
    <tr>
      <td>Peripheral myelin protein 22</td>
      <td>PMP22</td>
      <td>601907</td>
      <td>17p12</td>
      <td>CMT1A, CMT1E, CMT3, HNPP, Roussy-Levy syndrome</td>
    </tr>
    <tr>
      <td>Ribose-phosphate pyrophosphokinase 1</td>
      <td>PRPS1</td>
      <td>311850</td>
      <td>Xq22.3</td>
      <td>Arts syndrome, CMTX5, DFNX1</td>
    </tr>
    <tr>
      <td>Periaxin</td>
      <td>PRX</td>
      <td>605725</td>
      <td>19q13.2</td>
      <td>CMT4F, CMT3</td>
    </tr>
    <tr>
      <td>Ras-related protein Rab 7a</td>
      <td>RAB7A</td>
      <td>602298</td>
      <td>3q21.3</td>
      <td>CMT2B</td>
    </tr>
    <tr>
      <td>Septin 9</td>
      <td>SEPT9</td>
      <td>604061</td>
      <td>17q25.3</td>
      <td>HNA</td>
    </tr>
    <tr>
      <td>Transitional ER-ATPase</td>
      <td>VCP</td>
      <td>601023</td>
      <td>9p13.3</td>
      <td>CMT2Y</td>
    </tr>
    <tr>
      <td>Tryptophan-tRNA ligase, cytoplasmic</td>
      <td>WARS</td>
      <td>191050</td>
      <td>14q32.32</td>
      <td>HMN9</td>
    </tr>
    <tr>
      <td>Tyrosine-tRNA ligase, cytoplasmic</td>
      <td>YARS</td>
      <td>603623</td>
      <td>1p35.1</td>
      <td>DI-CMTC</td>
    </tr>
  </tbody>
</table>

### Pathological proteomic profile of peripheral myelin in a neuropathy model

The results presented thus far were based on analyzing myelin of healthy wild type mice; yet we also sought to establish a straightforward method to systematically assess myelin diversity, as exemplified by alterations in a pathological situation. As a model we chose mice carrying a homozygous deletion of the periaxin gene (Prx-/-) (Court et al., 2004; Gillespie et al., 2000). Periaxin (PRX) is the third-most abundant peripheral myelin protein (Figure 2) and scaffolds the dystroglycan complex in Schwann cells. Prx-/- mice represent an established model of Charcot-Marie-Tooth disease type 4F (Guilbot et al., 2001; Berger et al., 2006; Marchesi et al., 2010). Aiming to assess the myelin proteome, we purified myelin from pools of sciatic nerves dissected from Prx-/- and control mice at P21. Upon SDS-PAGE separation and silver staining the band patterns appeared roughly similar (Figure 5A), with the most obvious exception of the absence of the high-molecular weight band constituted by periaxin in Prx-/- myelin. Yet, several other bands also displayed genotype-dependent differences in intensity. As expected, PRX was also undetectable by MSE in Prx-/- myelin, in which most of the total myelin protein was constituted by MPZ/P0 and MBP (Figure 5B; Figure 5—source data 1).

![Figure 5.](https://cdn.elifesciences.org/articles/51406/elife-51406-fig5-v1.jpg)

**Figure 5.:** (A) Myelin purified from sciatic nerves dissected from Prx-/- and control mice at P21 was separated by SDS-PAGE (0.5 µg protein load) and proteins were visualized by silver staining. Bands constituted by the most abundant myelin proteins (MPZ/P0, MBP, PRX) are annotated. Note that no band constituted by PRX was detected in Prx-/- myelin and that several other bands also display genotype-dependent differences in intensity. Gel shows n = 2 biological replicates representative of n = 3 biological replicates. (B) The relative abundance of proteins in myelin purified from Prx-/- sciatic nerves as quantified by MSE is given as percent with relative standard deviation (% +/- RSD). Note the increased relative abundance of MPZ/P0 and MBP compared to wild-type myelin (see Figure 2) when PRX is lacking. Mass spectrometric quantification based on 3 biological replicates with 4 technical replicates each (see Figure 5—source data 1). (C,D) Differential proteome analysis by DRE-UDMSE of myelin purified from Prx-/- and wild-type mice. Mass spectrometric quantification based on 3 biological replicates per genotype with 4 technical replicates each (see Figure 5—source data 2). (C) Top 40 proteins of which the abundance is reduced (blue) or increased (red) in peripheral myelin purified from Prx-/- compared to wild-type mice with the highest level of significance according to the -log10 transformed q-value (green). In the heatmaps, each horizontal line corresponds to the fold-change (FC) of a distinct protein compared to its average abundance in wild-type myelin plotted on a log2 color scale. Heatmaps display 12 replicates, that is 3 biological replicates per genotype with 4 technical replicates each. (D-D‘‘‘) Volcano plots representing genotype-dependent quantitative myelin proteome analysis. Data points represent quantified proteins in Prx-/- compared to wild-type myelin and are plotted as the log2-transformed fold-change (FC) on the x-axis against the -log10-transformed q-value on the y-axis. Stippled lines mark a -log10-transformed q-value of 1.301, reflecting a q-value of 0.05 as significance threshold. Highlighted are the datapoints representing the Top 10 proteins displaying highest zdist values (Euclidean distance between the two points (0,0) and (x,y) with x = log2(FC) and y = -log10(q-value) (red circles in D), immune-related proteins (purple circles in D‘), proteins of the extracellular matrix (ECM; yellow circles in D‘‘) and known myelin proteins (blue circles in D‘‘‘). n.d., not detected; n.q., no q-value computable due to protein identification in one genotype only. Also see Figure 5—figure supplement 1. (E) Immunoblot of myelin purified from Prx-/- and control sciatic nerves confirms the reduced abundance of DRP2, SLC16A1/MCT1, BSG and PMP2 in Prx-/- myelin, as found by differential DRE-UDMSE analysis (in C,D). PRX was detected as genotype control; PLP/DM20 and ATP1A1 serve as markers. Blot shows n = 2 biological replicates per genotype. (F) Teased fiber preparations of sciatic nerves dissected from Prx-/- and control mice immunolabelled for MAG (red) and SLC16A1 (green). Note that SLC16A1 co-distributes with MAG in Schmidt-Lanterman incisures (SLI) in control but not in Prx-/- nerves, in accordance with the reduced abundance of SLC16A1 in Prx-/- myelin (C–E). Also note that, in Prx-/- myelin, SLI were largely undetectable by MAG immunolabeling.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/51406/elife-51406-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) The heatmap compares the log2 transformed ppm protein abundance values from the DRE-UDMSE runs to assess peripheral myelin purified from wild type and Prx-/- mice. The inset shows the color key and the histogram for the values of the correlation coefficients. Note that the runs cluster with a high overall correlation (>0.85) into two conditions defined by the genotype, in agreement with the experimental design. (B) Volcano plot representing genotype-dependent quantitative myelin proteome analysis. Data points represent quantified proteins in Prx-/- compared to wild-type myelin plotted as the log2-transformed fold-change (FC) on the x-axis against the -log10-transformed q-value on the y-axis. Note the different axis scale compared to Figure 5D. Stippled line marks a -log10-transformed q-value of 1.301, reflecting a q-value of 0.05 as significance threshold. Highlighted is the datapoint for PRX to illustrate that only trace amounts of PRX were detected when assessing Prx-/- myelin. ATP2A1, ATP1A4 and PLCD1 were not detected in Prx-/- myelin.

Upon differential analysis by DRE-UDMSE (Figure 5—source data 2), multiple proteins displayed genotype-dependent differences as visualized in a heatmap displaying those 40 proteins of which the abundance was reduced or increased with the highest statistical significance in Prx-/- compared to control myelin (Figure 5C). For example, the abundance of the periaxin-associated dystrophin-related protein 2 (DRP2) was strongly reduced in Prx-/- myelin, as previously shown by immunoblotting (Sherman et al., 2001). Notably, the abundance of multiple other proteins was also significantly reduced in Prx-/- myelin, including the extracellular matrix protein laminin C1 (LAMC1; previously termed LAMB2), the laminin-associated protein nidogen (NID1), Ig-like cell adhesion molecules (CADM4, MAG), the desmosomal junction protein desmin (DES), cytoskeletal and cytoskeleton-associated proteins (EPB41L3, MAP1A, CORO1A, SPTBN1, various microtubular and intermediate filament monomers), the monocarboxylate transporter MCT1 (also termed SLC16A1) and the MCT1-associated (Philp et al., 2003) immunoglobulin superfamily protein basigin (BSG, also termed CD147). On the other hand, proteins displaying the strongest abundance increase in Prx-/- myelin included immune-related proteins (LGALS3, LYZ2, CTSD), cytoskeletal and cytoskeleton-associated proteins (CAPG, CORO1C, CNN3, several myosin heavy chain subunits), peroxisomal enzymes (CAT, HSD17B4, MDH1) and known myelin proteins (PLLP/plasmolipin, CRYAB, GJB1/CX32). For comparison, the abundance of the marker proteolipid protein (PLP/DM20) (Patzig et al., 2016a) and the periaxin-associated integrin beta-4 (ITGB4) (Raasakka et al., 2019) in myelin was unaltered in Prx-/- myelin. Together, differential proteome analysis finds considerably more proteins and protein groups to be altered in Prx-/- myelin than previously known (Figure 5C,D–D'''), probably reflecting the complex pathology observed in this model (Court et al., 2004; Gillespie et al., 2000).

The monocarboxylate transporter MCT1/SLC16A1 expressed by myelinating oligodendrocytes (Lee et al., 2012; Fünfschilling et al., 2012) and Schwann cells (Domènech-Estévez et al., 2015; Morrison et al., 2015) has been proposed to supply lactate or other glucose breakdown products to axons, in which they may serve as substrate for the mitochondrial production of ATP (Morrison et al., 2013; Saab et al., 2013; Rinholm and Bergersen, 2014). In this respect it was striking to find the abundance of MCT1 significantly reduced in peripheral myelin when PRX is lacking (Figure 5C), a result that we were able to confirm by immunoblotting (Figure 5E) and immunolabeling of teased fiber preparations of sciatic nerves (Figure 5F). Notably, reduced expression of MCT1 in Slc16a1+/- mice impairs axonal integrity at least in the CNS (Lee et al., 2012; Jha et al., 2020). The reduced abundance of MCT1 thus represents an interesting novel facet of the complex pathology in Prx-/- mice. Considering that the integrity of peripheral axons may be impaired in Prx-/- mice, we assessed their quadriceps nerves. Indeed, Prx-/- mice displayed reduced axonal diameters, a progressively reduced total number of axons and a considerable number of myelin whorls lacking a visible axon (Figure 6), indicative of impaired axonal integrity (Edgar et al., 2009). Yet we note that molecular or neuropathological features other than the reduced abundance of MCT1 probably also contribute to the axonopathy in Prx-/- mice.

![Figure 6.](https://cdn.elifesciences.org/articles/51406/elife-51406-fig6-v1.jpg)

**Figure 6.:** (A–D) Genotype-dependent quantitative assessment of light micrographs of toluidine-stained semi-thin sectioned quadriceps nerves dissected at 2, 4 and 9 months of age reveals progressive loss of peripheral axons in Prx-/- compared to control mice. (A) Representative micrographs. Arrows point at myelinated axons; asterisk denotes an unmyelinated axon; arrowhead points at a myelin whorl lacking a recognizable axon. Scale bars, 10 µm. (B) Total number of axons per nerve that are not associated with a Remak bundle. (C) Total number of myelinated axons per nerve. (D) Total number per nerve of myelin whorls that lack a recognizable axon. Mean +/SD, n = 3–4 mice per genotype and age; *p<0.05, **p<0.01, ***p<0.001 by Student’s unpaired t-test. (E–G) Genotype-dependent assessment of myelinated axons shows a shift toward reduced axonal diameters in quadriceps nerves of Prx-/- compared to control mice at 2 months (E), 4 months (F) and 9 months (G) of age. Data are presented as frequency distribution with 0.5 µm bin width. ***, p<0.001 by two-sided Kolmogorow-Smirnow test. For precise p-values see methods section.

Together, gel-free, label free proteome analysis provides a cost- and time-efficient method that provides an accurate, sensitive tool to gain systematic insight into the protein composition of healthy peripheral myelin and its alterations in pathological situations. Indeed, gel-free proteome analysis is particularly powerful and comprehensive compared to 2D-DIGE; the workflow presented here appears readily applicable to other neuropathy models, thereby promising discovery of relevant novel features of their neuropathology.

## Discussion

We used gel-free, label-free quantitative mass spectrometry to assess the protein composition of myelin biochemically purified from the sciatic nerves of wild-type mice, thereby establishing a straightforward and readily applicable workflow to approach the peripheral myelin proteome. The key to comprehensiveness was to combine the strengths of three data acquisition modes, that is, MSE for correct quantification of high-abundant proteins, UDMSE for deep quantitative proteome coverage including low-abundant proteins and DRE-UDMSE for differential analysis. We suggest that DRE-UDMSE provides a good compromise between dynamic range, identification rate and instrument run time for routine differential myelin proteome profiling as a prerequisite for a molecular understanding of myelin (patho)biology. We have also integrated the resulting compendium with RNA-Seq-based mRNA abundance profiles in peripheral nerves and neuropathy disease loci. Beyond providing the largest peripheral myelin proteome dataset thus far, the workflow is appropriate to serve as starting point for assessing relevant variations of myelin protein composition, for example, in different nerves, ages, species and in pathological conditions. The identification of numerous pathological alterations of myelin protein composition in the Prx-/- neuropathy model indicates that the method is well suited to assess such diversity.

Aiming to understand nervous system function at the molecular level, multiple ‘omics‘-scale projects assess the spatio-temporal expression profiles of all mRNAs and proteins in the CNS including oligodendrocytes and myelin (Zhang et al., 2014; Patzig et al., 2016b; Sharma et al., 2015; Thakurela et al., 2016; Marques et al., 2016). Yet, peripheral nerves are also essential for normal sensory and motor capabilities. Prior approaches to the molecular profiles of Schwann cells and PNS myelin thus far, however, were performed >8 years ago (Nagarajan et al., 2002; Le et al., 2005; Ryu et al., 2008; Patzig et al., 2011; Verheijen et al., 2003; Buchstaller et al., 2004; D'Antonio et al., 2006), and the techniques have considerably advanced since. For example, current gel-free, label-free mass spectrometry can simultaneously identify and quantify the vast majority of proteins in a sample, thereby providing comprehensive in depth-information. Moreover, RNA-Seq technology has overcome limitations of the previously used microarrays for characterizing mRNA abundance profiles with respect to the number of represented genes and the suitability of the oligonucleotide probes. The present compendium thus provides high confidence with respect to the identification of myelin proteins, their relative abundance and their developmental mRNA expression profiles. This view is supported by the finding that over 80% of the total myelin proteome is constituted by approximately 50 previously known myelin proteins. We believe that the majority of the other identified proteins represent low-abundant myelin-associated constituents in line with the high efficiency of biochemical myelin purification. Doubtless, however, the myelin proteome also comprises contaminants from other cellular sources, underscoring the need of independent validation for establishing newly identified constituents as true myelin proteins.

Do myelin proteins exist that escape identification by standard proteomic approaches? Indeed, some proteins display atypically distributed lysine and arginine residues, which represent the cleavage sites of the commonly used protease trypsin. The tryptic digest of these proteins leads to peptides that are not well suited for chromatographic separation and/or mass spectrometric detection/sequencing, as exemplified by the small hydrophobic tetraspan-transmembrane myelin proteins MAL (Schaeren-Wiemers et al., 2004) and PMP22 (Adlkofer et al., 1995). We can thus not exclude that additional proteins with atypical tryptic digest patterns exist in peripheral myelin, which would need to be addressed by the use of alternative proteases. Moreover, potent signaling molecules including erbB receptor tyrosine kinases (Riethmacher et al., 1997; Woldeyesus et al., 1999) and G-protein coupled receptors (GPRs) (Ackerman et al., 2018; Monk et al., 2011; Monk et al., 2009) display exceptionally low abundance. Such proteins may be identified when applying less stringent identification criteria, e.g., by requiring the sequencing of only one peptide per protein. However, lower stringency would also result in identifying false-positive proteins, which we wished to avoid for the purpose of the present compendium. We note that a truly comprehensive spatio-temporally resolved myelin proteome should preferentially also include systematic information about protein isoforms and post-translational modifications, which still poses technical challenges.

Mutations affecting the periaxin (PRX) gene in humans cause CMT type 4F (Guilbot et al., 2001; Kabzinska et al., 2006; Baránková et al., 2008; Tokunaga et al., 2012); the neuropathology resulting from mutations affecting periaxin has been mainly investigated in the Prx-/- mouse model. Indeed, Prx-/- mice display a progressive peripheral neuropathy including axon/myelin-units with abnormal myelin thickness, demyelination, tomaculae, onion bulbs, reduced nerve conduction velocity (Gillespie et al., 2000), reduced abundance and mislocalization of the periaxin-associated DRP2 (Sherman et al., 2001) and reduced internode length (Court et al., 2004). Absence of SLIs (Gillespie et al., 2000) and bands of Cajal (Court et al., 2004) imply that the non-compact myelin compartments are impaired when PRX is lacking. In the differential analysis of myelin purified from Prx-/- and control mice we find that the previously reported reduced abundance of DRP2 (Sherman et al., 2001) represents one of the strongest molecular changes in the myelin proteome when PRX is lacking. Notably, the reported morphological changes in this neuropathy model (Sherman et al., 2001; Court et al., 2004; Gillespie et al., 2000) go along with alterations affecting the abundance of multiple other myelin-associated proteins, including junctional, cytoskeletal, extracellular matrix and immune-related proteins as well as lipid-modifying enzymes. Thus, the neuropathology in Prx-/- mice at the molecular level is more complex than previously anticipated. It is striking that the abundance of the monocarboxylate transporter MCT1/SLC16A1 that may contribute to the metabolic supply of lactate from myelinating cells to axons (Beirowski et al., 2014; Domènech-Estévez et al., 2015; Kim et al., 2016; Gonçalves et al., 2017; Stassart et al., 2018) is strongly reduced in Prx-/- myelin. Considering that MCT1 in Schwann cells mainly localizes to Schmidt Lanterman incisures (SLI) (Domènech-Estévez et al., 2015) and that SLI are largely absent from myelin when PRX is lacking (Gillespie et al., 2000), the reduced abundance of MCT1 in Prx-/- myelin may be a consequence of the impaired myelin ultrastructure. Yet, considering that SLI are part of the cytosolic channels that may represent transport routes toward Schwann cell-dependent metabolic support of myelinated axons, the diminishment of MCT1 may contribute to reduced axonal diameters or axonal loss in Prx-/- mice, probably in conjunction with other molecular or morphological defects. Together, the in depth-analysis of proteins altered in neuropathy models can contribute to an improved understanding of nerve pathophysiology.

Compared to a previous approach (Patzig et al., 2011), the number of proven neuropathy genes of which the encoded protein is mass spectrometrically identified in peripheral myelin has increased four-fold from eight to 32 in the present study. This reflects both that the number of proteins identified in myelin has approximately doubled and that more neuropathy genes are known due to the common use of genome sequencing. We note that our compendium comprises not only myelin-associated proteins causing (when mutated) demyelinating CMT1 (e.g., MPZ/P0, NEFL, PMP2) or intermediate CMT4 (GDAP1, NDRG1, PRX) but also axonal CMT2 (RAB7, GARS, HSPB1). Yet, the expression of genes causative of CMT2 is not necessarily limited to neurons, as exemplified by the classical myelin protein MPZ/P0. Indeed, a subset of MPZ-mutations causes axonal CMT2I or CMT2J (Gallardo et al., 2009; Leal et al., 2014; Tokuda et al., 2015; Duan et al., 2016; Fabrizi et al., 2018), probably reflecting impaired axonal integrity as consequence of a mutation primarily affecting Schwann cells. We also note that the nuclear EGR2/KROX20 causative of demyelinating CMT1D has not been mass spectrometrically identified in myelin, reflecting that Schwann cell nuclei are efficiently removed during myelin purification.

While morphological analysis of peripheral nerves by light and electron microscopy is routine in numerous laboratories, systematic molecular analysis has been less straightforward. Using the sciatic nerve as a model, we show that systematic assessment of the myelin proteome and the total nerve transcriptome are suited to determine comprehensive molecular profiles in healthy nerves and in myelin-related disorders. Myelin proteome analysis can thus complement transcriptome analysis in assessing development, function and pathophysiology of peripheral nerves.

## Materials and methods

### Mouse models

Prx-/- mice (Gillespie et al., 2000) were kept on c57Bl/6 background in the animal facility of the University of Edinburgh (United Kingdom). Genotyping was by PCR on genomic DNA using the forward primers 5‘-CAGATTTGCT CTGCCCAAGT and 5‘-CGCCTTCTAT CGCCTTCTTGAC in combination with reverse primer 5‘-ATGCCCTCAC CCACTAACAG. The PCR yielded a 0.5 kb fragment for the wildtype allele and a 0.75 kb product for the mutant allele. The age of experimental animals is given in the figure legends. All animal work conformed to United Kingdom legislation (Scientific Procedures) Act 1986 and to the University of Edinburgh Ethical Review Committee policy; Home Office project license No. P0F4A25E9.

### Myelin purification

A light-weight membrane fraction enriched for myelin was purified from sciatic nerves of mice by sucrose density centrifugation and osmotic shocks as described (Patzig et al., 2011; Erwig et al., 2019a). Myelin accumulates at the interface between 0.29 and 0.85 M sucrose. Prx-/- and wild type control C57Bl/6 mice were sacrificed by cervical dislocation at postnatal day 21 (P21). For each genotype, myelin was purified as three biological replicates (n = 3); each biological replicate representing a pool of 20 sciatic nerves dissected from 10 mice. Protein concentration was determined using the DC Protein Assay Kit (Bio-Rad).

### Filter-aided sample preparation for proteome analysis

Protein fractions corresponding to 10 μg myelin protein were dissolved and processed according to a filter-aided sample preparation (FASP) protocol essentially as previously described for synaptic protein fractions (Ambrozkiewicz et al., 2018) and as adapted to CNS myelin (Erwig et al., 2019a; Erwig et al., 2019b). Unless stated otherwise, all steps were automated on a liquid-handling workstation equipped with a vacuum manifold (Freedom EVO 150, Tecan) by using an adaptor device constructed in-house. Briefly, myelin protein samples were lysed and reduced in lysis buffer (7 M urea, 2 M thiourea, 10 mM DTT, 0.1 M Tris pH 8.5) containing 1% ASB-14 by shaking for 30 min at 37°C. Subsequently, the sample was diluted with ~10 volumes lysis buffer containing 2% CHAPS to reduce the ASB-14 concentration and loaded on centrifugal filter units (30 kDa MWCO, Merck Millipore). After removal of the detergents by washing twice with wash buffer (8 M urea, 10 mM DTT, 0.1 M Tris pH 8.5), proteins were alkylated with 50 mM iodoacetamide in 8 M urea, 0.1 M Tris pH 8.5 (20 min at RT), followed by two washes with wash buffer to remove excess reagent. Buffer was exchanged by washing three times with 50 mM ammonium bicarbonate (ABC) containing 10% acetonitrile. After three additional washes with 50 mM ABC/10% acetonitrile, which were performed by centrifugation to ensure quantitative removal of liquids potentially remaining underneath the ultrafiltration membrane, proteins were digested overnight at 37°C with 400 ng trypsin in 40 µl of the same buffer. Tryptic peptides were recovered by centrifugation followed by two additional extraction steps with 40 µl of 50 mM ABC and 40 µl of 1% trifluoroacetic acid (TFA), respectively. Aliquots of the combined flow-throughs were spiked with 10 fmol/μl of yeast enolase-1 tryptic digest standard (Waters Corporation) for quantification purposes and directly subjected to analysis by liquid chromatography coupled to electrospray mass spectrometry (LC-MS). A pool of all samples was injected at least before and after any sample set to monitor stability of instrument performance.

### Mass spectrometry

Nanoscale reversed-phase UPLC separation of tryptic peptides was performed with a nanoAcquity UPLC system equipped with a Symmetry C18 5 μm, 180 μm × 20 mm trap column and a HSS T3 C18 1.8 μm, 75 μm × 250 mm analytical column (Waters Corporation) maintained at 45°C. Injected peptides were trapped for 4 min at a flow rate of 8 µl/min 0.1% TFA and then separated over 120 min at a flow rate of 300 nl/min with a gradient comprising two linear steps of 3–35% mobile phase B in 105 min and 35–60% mobile phase B in 15 min, respectively. Mobile phase A was water containing 0.1% formic acid while mobile phase B was acetonitrile containing 0.1% formic acid. Mass spectrometric analysis of tryptic peptides was performed using a Synapt G2-S quadrupole time-of-flight mass spectrometer equipped with ion mobility option (Waters Corporation). Positive ions in the mass range m/z 50 to 2000 were acquired with a typical resolution of at least 20.000 FWHM (full width at half maximum) and data were lock mass corrected post-acquisition. UDMSE and DRE-UDMSE analyses were performed in the ion mobility-enhanced data-independent acquisition mode with drift time-specific collision energies as described in detail by Distler et al. (2016) and Distler et al. (2014b). Specifically, for DRE-UDMSE a deflection device (DRE lens) localized between the quadrupole and the ion mobility cell of the mass spectrometer was cycled between full (100% for 0.4 s) and reduced (5% for 0.4 s) ion transmission during one 0.8 s full scan. Continuum LC-MS data were processed for signal detection, peak picking, and isotope and charge state deconvolution using Waters ProteinLynx Global Server (PLGS) version 3.0.2 (47). For protein identification, a custom database was compiled by adding the sequence information for yeast enolase 1 and porcine trypsin to the UniProtKB/Swiss-Prot mouse proteome and by appending the reversed sequence of each entry to enable the determination of false discovery rate (FDR). Precursor and fragment ion mass tolerances were automatically determined by PLGS 3.0.2 and were typically below 5 ppm for precursor ions and below 10 ppm (root mean square) for fragment ions. Carbamidomethylation of cysteine was specified as fixed and oxidation of methionine as variable modification. One missed trypsin cleavage was allowed. Minimal ion matching requirements were two fragments per peptide, five fragments per protein, and one peptide per protein. The FDR for protein identification was set to 1% threshold.

### Analysis of proteomic data

For each genotype (Prx-/- and wild type control mice sacrificed at P21), biochemical fractions enriched for PNS myelin were analyzed as three biological replicates (n = 3 per condition); each biological replicate representing a pool of 20 sciatic nerves dissected from 10 mice. The samples were processed with replicate digestion and injection, resulting in four technical replicates per biological replicate and thus a total of 12 LC-MS runs per condition to be compared, essentially as previously reported for CNS myelin (Patzig et al., 2016b; Erwig et al., 2019b). The freely available software ISOQuant (www.isoquant.net) was used for post-identification analysis including retention time alignment, exact mass and retention time (EMRT) and ion mobility clustering, peak intensity normalization, isoform/homology filtering and calculation of absolute in-sample amounts for each detected protein (Distler et al., 2016; Distler et al., 2014b; Kuharev et al., 2015) according to the TOP3 quantification approach (Silva et al., 2006; Ahrné et al., 2013). Only peptides with a minimum length of seven amino acids that were identified with scores above or equal to 5.5 in at least two runs were considered. FDR for both peptides and proteins was set to 1% threshold and only proteins reported by at least two peptides (one of which unique) were quantified using the TOP3 method. The parts per million (ppm) abundance values (i.e. the relative amount (w/w) of each protein in respect to the sum over all detected proteins) were log2-transformed and normalized by subtraction of the median derived from all data points for the given protein. Significant changes in protein abundance were detected by moderated t-statistics essentially as described (Ambrozkiewicz et al., 2018; Erwig et al. (2019b) ) across all technical replicates using an empirical Bayes approach and false discovery (FDR)-based correction for multiple comparisons (Kammers et al., 2015). For this purpose, the Bioconductor R packages ‘limma’ (Ritchie et al., 2015) and ‘q-value’ (Storey, 2003) were used in RStudio, an integrated development environment for the open source programming language R. Proteins identified as contaminants (e.g. components of blood or hair cells) were removed from the analysis. Proteins with ppm values below 100 which were not identified in one genotype were considered as just above detection level and also removed from the analysis. The relative abundance of a protein in myelin was accepted as altered if both statistically significant (q-value <0.05). Pie charts, heatmaps and volcano plots were prepared in Microsoft Excel 2013 and GraphPad Prism 7. Pearson’s correlation coefficients derived from log2-transformed ppm abundance values were clustered and visualized with the tool heatmap.2 contained in the R package gplots (CRAN.R-project.org/package = gplots). Only pairwise complete observations were considered to reduce the influence of missing values on clustering behavior. The mass spectrometry proteomics data have been deposited to the ProteomeXchange Consortium (proteomecentral.proteomexchange.org) via the PRIDE partner repository (Vizcaíno et al., 2016) with the dataset identifier PXD015960.

### Gel electrophoresis and silver staining of gels

Protein concentration was determined using the DC Protein Assay kit (BioRad). Samples were separated on a 12% SDS-PAGE for 1 hr at 200 V using the BioRad system, fixated overnight in 10% [v/v] acetic acid and 40% [v/v] ethanol and then washed in 30% ethanol (2 × 20 min) and ddH2O (1 × 20 min). For sensitization, gels were incubated 1 min in 0.012% [v/v] Na2S2O3 and subsequently washed with ddH2O (3 × 20 s). For silver staining, gels were impregnated for 20 min in 0.2% [w/v] AgNO3/0.04% formaldehyde, washed with ddH2O (3 × 20 s) and developed in 3% [w/v] Na2CO3/0.02% [w/v] formaldehyde. The reaction was stopped by exchanging the solution with 5% [v/v] acetic acid.

### Immunoblotting

Immunoblotting was performed as described by Schardt et al. (2009) and de Monasterio-Schrader et al. (2013). Primary antibodies were specific for dystrophin-related-protein 2 (DRP2; Sigma; 1:1000), peripheral myelin protein 2 (PMP2; ProteinTech Group 12717–1-AP; 1:1000), proteolipid protein (PLP/DM20; A431; Jung et al., 1996; 1:5000), Monocarboxylate transporter 1 (MCT1/SLC16A1; Stumpf et al., 2019; 1:1000), periaxin (PRX; Gillespie et al., 1994; 1:1000), sodium/potassium-transporting ATPase subunit alpha-1 (ATP1A1; 1:2000; Abcam #13736–1-AP), myelin protein zero (MPZ/P0; Archelos et al., 1993; kind gift by J Archelos-Garcia; 1:10.000), voltage-dependent anion-selective channel protein (VDAC; Abcam #ab15895; 1:1000), basigin (BSG/CD147; ProteinTech Group #ab64616; 1:1000), neurofilament H (NEFH/NF-H; Covance #SMI-32P; 1:1000), voltage-gated potassium channel subunit A member 1 (KCNA1; Neuromab #73–007; 1:1000), EGR2/KROX20 (Darbas et al., 2004; kind gift by D Meijer, Edinburgh; 1:1000) and myelin basic protein (MBP; 1:2000). To generate the latter antisera, rabbits were immunized (Pineda Antikörper Service, Berlin, Germany) with the KLH-coupled peptide CQDENPVVHFFK corresponding to amino acids 212–222 of mouse MBP isoform 1 (Swisprot/Uniprot-identifier P04370-1). Anti-MBP antisera were purified by affinity chromatography and extensively tested for specificity by immunoblot analysis of homogenate of brains dissected from wild-type mice compared to Mbpshiverer/shiverer mice that lack expression of MBP. Appropriate secondary anti-mouse or -rabbit antibodies conjugated to HRP were from dianova. Immunoblots were developed using the Enhanced Chemiluminescence Detection kit (Western Lightning Plus, Perkin Elmer) and detected with the Intas ChemoCam system (INTAS Science Imaging Instruments GmbH, Göttingen, Germany).

### Immunolabelling of teased fibers

Teased fibers were prepared as previously described by Sherman et al. (2001) and Catenaccio and Court (2018). For each genotype, one male mouse was sacrificed by cervical dislocation at P17. Immunolabelling of teased fibers was performed as described by Patzig et al. (2016b). Briefly, teased fibers were fixed for 5 min in 4% paraformaldehyde, permeabilized 5 min with ice-cold methanol, washed in PBS (3 × 5 min) and blocked for 1 hr at 21°C in blocking buffer (10% horse serum, 0.25% Triton X-100, 1% bovine serum albumin in PBS). Primary antibodies were applied overnight at 4°C in incubation buffer (1.5% horse serum, 0.25% Triton X-100 in PBS). Samples were washed in PBS (3 × 5 min) and secondary antibodies were applied in incubation buffer (1 hr, RT). Samples were again washed in PBS (2 × 5 min), and 4‘,6-diamidino-2-phenylindole (DAPI; 1:50 000 in PBS) was applied for 10 min at RT. Samples were briefly washed 2x with ddH2O and mounted using Aqua-Poly/Mount (Polysciences, Eppelheim, Germany). Antibodies were specific for myelin-associated glycoprotein (MAG clone 513; Chemicon MAB1567; 1:50) and MCT1/SLC16A1 (107). Secondary antibodies were donkey α-rabbit-Alexa488 (Invitrogen A21206; 1:1000) and donkey α-mouse-Alexa555 (Invitrogen A21202; 1:1000). Labeled teased fibers were imaged using the confocal microscope Leica SP5. The signal was collected with the objective HCX PL APO lambda blue 63.0.x1.20. DAPI staining was excited with 405 nm and collected between 417 nm - 480 nm. To excite the Alexa488 fluorophore an Argon laser with the excitation of 488 nm was used and the emission was set to 500 nm - 560 nm. Alexa555 was excited by using the DPSS561 laser at an excitation of 561 nm and the emission was set to 573 nm - 630 nm. To export and process the images LAS AF lite and Adobe Photoshop were used.

### mRNA abundance profiles

Raw data were previously established (Fledrich et al., 2018) from the sciatic nerves of wild type Sprague Dawley rats at the indicated ages (E21, P6, P18; n = 4 per time point). Briefly, sciatic nerves were dissected, the epineurium was removed, total RNA was extracted with the RNeasy Kit (Qiagen), concentration and quality (ratio of absorption at 260/280 nm) of RNA samples were determined using the NanoDrop spectrophotometer (ThermoScientific), integrity of the extracted RNA was determined with the Agilent 2100 Bioanalyser (Agilent Technologies) and RNA-Seq was performed using the Illumina HiSeq2000 platform. RNA-Seq raw data are available under the GEO accession number GSE115930 (Fledrich et al., 2018). For the present analysis, the fastqfiles were mapped to rattus norvegicus rn6 using Tophat Aligner and then quantified based on the Ensemble Transcripts release v96. The raw read counts were then normalized using the R package DESeq2. The normalized gene expression data was then standardized to a mean of zero and a standard deviation of one, therefore genes with similar changes in expression are close in the euclidian space. Clustering was performed on the standardized data using the R package mfuzz. Transcripts displaying abundance differences of less than 10% coefficient of variation were considered developmentally unchanged.

### Venn diagrams

Area-proportional Venn diagrams were prepared using BioVenn (Hulsen et al., 2008) at www.biovenn.nl/.

### GO-term

For functional categorization of the myelin proteome the associated gene ontology terms were systematically analyzed on the mRNA abundance cluster using the Database for Annotation, Visualization and Integrated Discovery (DAVID; https://david.ncifcrf.gov). For comparison known myelin proteins according to literature were added.

### Histological analysis

Prx-/- and control mice were perfused at the indicated ages intravascularly with fixative solution (2.5% glutaraldehyde, 4% paraformaldehyde, 0.1 M sodium cacodylate buffer, pH 7.4). Quadriceps nerves were removed, fixed for 2 hr at room temperature, followed by 18 hr at 4°C in the same fixative, postfixed in OsO4, dehydrated a graded series of ethanol, followed by propylene oxide and embedded in Araldite. All axons not associated with a Remak bundle were counted and categorized as myelinated or non-myelinated. All myelin profiles lacking a recognizable axon were counted. The total number of axons were counted on micrographs of toluidine blue stained Araldite sections (0.5 µm) of quadriceps nerves. Precise p-values for the quantitative comparison between Ctrl and Prx-/- mice were: Total number of axons (Figure 6B; Student’s unpaired t-test): 2 mo p=0.01734; 4 mo p=2.1E-05; 9 mo p=0.007625; Number of myelinated axons (Figure 6C; Student’s unpaired t-test): 2 mo p=0.00444; 4 mo p=2.12E-05; 9 mo p=0.005766; Number of empty myelin profiles (Figure 6D; Student’s unpaired t-test): 2 mo p=0.004445; 4 mo p=0.001461; 9 mo p=0.000695; Axonal diameters (Figure 6E–G; two-sided Kolmogorow-Smirnow test): 2 mo p=2.20E-16; 4 mo p=2.20E-16; 9 mo p=2.20E-16.
