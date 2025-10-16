# Direct assessment of substrate binding to the Neurotransmitter:Sodium Symporter LeuT by solid state NMR

## Authors

- Simon Erlendsson<sup>1</sup> ([ORCID: 0000-0002-6378-870X](https://orcid.org/0000-0002-6378-870X))
- Kamil Gotfryd<sup>3</sup>
- Flemming Hofmann Larsen<sup>6</sup>
- Jonas Sigurd Mortensen<sup>3</sup> ([ORCID: 0000-0002-6743-276X](https://orcid.org/0000-0002-6743-276X))
- Michel-Andreas Geiger<sup>7</sup>
- Barth-Jan van Rossum<sup>7</sup>
- Hartmut Oschkinat<sup>7</sup>
- Ulrik Gether<sup>3</sup>
- Kaare Teilum<sup>1</sup> †
- Claus J Loland<sup>3</sup> ([ORCID: 0000-0002-1773-1446](https://orcid.org/0000-0002-1773-1446)) †

### Affiliations

1. Structural Biology and NMR Laboratory, Department of Biology University of Copenhagen Copenhagen Denmark
2. Linderstrøm-Lang Centre for Protein Science, Department of Biology University of Copenhagen Copenhagen Denmark
3. Molecular Neuropharmacology Laboratory, Department of Neuroscience and Pharmacology University of Copenhagen Copenhagen Denmark
4. Lundbeck Foundation Center for Biomembranes in Nanomedicine University of Copenhagen Copenhagen Denmark
5. Faculty of Health and Medical Sciences University of Copenhagen Copenhagen Denmark
6. Quality and Technology, Department of Food Science, Faculty of Life Sciences University of Copenhagen Copenhagen Denmark
7. Leibniz-Institut für Molekulare Pharmakologie FMP Berlin Germany

† Corresponding author

## Abstract

10.7554/eLife.19314.001 The Neurotransmitter:Sodium Symporters (NSSs) represent an important class of proteins mediating sodium-dependent uptake of neurotransmitters from the extracellular space. The substrate binding stoichiometry of the bacterial NSS protein, LeuT, and thus the principal transport mechanism, has been heavily debated. Here we used solid state NMR to specifically characterize the bound leucine ligand and probe the number of binding sites in LeuT. We were able to produce high-quality NMR spectra of substrate bound to microcrystalline LeuT samples and identify one set of sodium-dependent substrate-specific chemical shifts. Furthermore, our data show that the binding site mutants F253A and L400S, which probe the major S1 binding site and the proposed S2 binding site, respectively, retain sodium-dependent substrate binding in the S1 site similar to the wild-type protein. We conclude that under our experimental conditions there is only one detectable leucine molecule bound to LeuT. DOI: http://dx.doi.org/10.7554/eLife.19314.001

## Introduction

The Neurotransmitter:Sodium Symporters (NSSs) are responsible for clearing neurotransmitters, such as dopamine, serotonin, norepinephrine, glycine and GABA from the synaptic cleft. The transporters are thereby crucial for the regulation of synaptic transmission in the CNS and alterations in their function have been linked to several psychiatric and neurological disorders such as depression, bipolar disorders, attention deficit hyperactive disorder (ADHD), epilepsy, and Parkinson’s disease (Broer, 2013; Kristensen et al., 2011). The understanding of the molecular mechanisms and structural (re)arrangements underlying NSS function has advanced significantly in recent years. The most detailed insight into structure-function relationships of NSSs comes from studies of the amino acid transporter, LeuT, from Aquifex aeolicus (Kantcheva et al., 2013; Kazmier et al., 2014; Malinauskaite et al., 2014, 2016; Piscitelli et al., 2010; Quick et al., 2012; Shi et al., 2008; Singh et al., 2007; Wang et al., 2012a, 2012b; Yamashita et al., 2005). Recent structures of the drosophila dopamine transporter (dDAT) (Penmatsa et al., 2013) and the human serotonin transporter (Coleman et al., 2016), which are eukaryotic members of the NSS family, confirm that LeuT is a reliable model protein and proves its value in understanding the molecular function of this class of transporters.

Functional studies of LeuT have suggested the existence of a secondary substrate binding site (S2) located in the extracellular vestibule of LeuT approximately 10 Å from the primary substrate binding site (S1) (Khelashvili et al., 2013; Quick et al., 2009; Shi et al., 2008). The S2 site is suggested to be an allosteric trigger, essential for coupling the energy from the electrochemical gradient to the transport of the solute. The binding of leucine to the S2 site has been measured to have the same affinity (in nM range) as binding to the S1 but does not, as the S1 bound substrate, directly coordinate sodium (Quick et al., 2012). However, attempts to crystallize LeuT with substrate bound to the S2 site have so far been unsuccessful, and therefore the existence of the S2 site is supported primarily by radioligand binding assays and guided MD simulations (Quick et al., 2012; Zhao et al., 2011). Due to the lack of structural evidence, the existence of a high-affinity S2 site has been questioned (Piscitelli et al., 2010), supporting the need for employing new techniques for investigating ligand binding in NSS proteins.

Here we investigate the leucine binding properties of LeuT by magic angle spinning (MAS) NMR, aiming at a characterization of the proposed S2 binding site. Our approach offers several advantages: (i) We use microcrystalline samples of LeuT prepared under experimental conditions allowing for conformations capable of ligand binding to both S1 and S2 (Quick et al., 2012). (ii) NMR offers information on the full structural ensemble which is unlikely not to include conformers (even lowly populated) prone to bind leucine in S2. (iii) Leucine binding to S1 and S2 may be distinguished by characteristic chemical shifts that are expected to be different due to different chemical environments, i.e. interacting residues (Reyes et al., 2011).

## Results and discussion

Prior to crystallization and NMR experiments we verified the functionality of the produced LeuT wild-type (WT) samples. We initially performed [3H]leucine saturation binding experiments and subsequently assessed Na+-dependency of [3H]leucine binding. All experiments were done at a DDM concentration commonly used in in vitro assays (i.e., 0.05% corresponding to 5.7x CMC). At this detergent concentration, LeuT was reported to retain binding to both S1 and the putative S2 site (Quick et al., 2012). In scintillation proximity binding assays LeuT WT bound [3H]leucine with a dissociation constant (Kd) of 12 ± 1 nM in the presence of 200 mM sodium. The EC50 value calculated for the Na+-dependent binding was 47 ± 4 mM (Figure 1—figure supplement 1A–B). These values are in agreement with those previously reported for LeuT (Shi et al., 2008; Singh et al., 2008).

As we were primarily interested in a simple readout reporting solely on substrate binding, we purified and kept LeuT in the presence of 1 mM

![Figure 1.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig1-v1.jpg)

**Figure 1.:** (A) Cartoon illustration of experimental approach. 15N enriched L-leucine substrate is added to detergent reconstituted LeuT, which is subsequently crystallized using large scale sitting drop vapour diffusion. Rod-shaped microcrystals form within 24 hr and can be readily harvested. (PDB ID: 3F3E) (B) LeuT WT purified in NaCl (red) and LeuT purified in KCl (black). 15N L-Leucine specific peak is indicated by an asterix with a chemical shift of 38.2 ppm. Spectra are tentatively intensity normalized to the 15N natural abundance signal from the LeuT backbone amides. Signal-to-noise is calculated to be 21. (C) 23Na-NMR of LeuT WT (red) and LeuT WT in KCl (black) in presence of leucine. Minor peak at −8.9 ppm represents the shape of one or two structural sodium molecules. Despite inequivalent location of the two sodium sites in the LeuT, the coordination mechanism is almost identical which might account for the observation of a single peak in the 23Na-NMR spectrum instead of two distinct peaks.DOI: http://dx.doi.org/10.7554/eLife.19314.003

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** LeuT WT was purified in KCl and eluted in 0.05% DDM (pH 8.0). Scintillation proximity assay-based measurements of (A) [3H]leucine saturation binding to 100 ng LeuT in the presence of 200 mM NaCl and (B) Na+-dependent [3H]leucine binding (100 nM) by 100 ng LeuT. Ionic strength was compensated with KCl. Data are displayed as means ± s.e.m., performed in triplicates, n = 3.DOI: http://dx.doi.org/10.7554/eLife.19314.004

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** LeuT microcrystals are needle-shaped and have a length of 1–10 μm. The microscopic image was solely used to assess the quality of the microcrystalline material.DOI: http://dx.doi.org/10.7554/eLife.19314.005

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A) Protein concentration: 2 mg/ml, leucine concentration: 1 mM. The spectrum is dominated by the signal arising from the free unbound leucine, at ~42 ppm. Spectrum was recorded on a 400 MHz Bruker shielded wide bore magnet equipped with a 3.2 mm MAS HCN operating at ~100 K. Spinning rate: 8000 kHz. CP contact time: 1000 us, recycling delay: 3 s. 24 k scans were required to record presented spectrum. (B) 15N CP/MAS spectra from dry L-leucine powder (top panel) and from lyophilized leuT samples (bottom panel). Free 15N L-Leucine has a distinct chemical shift at 118 ppm. For the LeuT WT NaCl preparation (red) several additional peaks appear around the dominating free state peak. Though these peaks vary slightly in intensity when compared to LeuT WT KCl (dark). These peaks do not originate from structural leucine. Spectra were recorded on a 700 MHz Bruker shielded wide bore magnet equipped with a 4 mm MAS HCN probe operating at 298 K. Spinning rate: 12500 KHz, CP contact time: 1500 us, recycling delay: 2.5 s. 65 K scans were required to record presented spectra.DOI: http://dx.doi.org/10.7554/eLife.19314.006

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** (A) Line broadening for window function 1 Hz, Signal-to-noise in calculated to be 21, Full width half height (FWHH) of the substrate peak is 31 Hz. (B) Line broadening for window function 10 Hz.DOI: http://dx.doi.org/10.7554/eLife.19314.007

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** 15N spectra of free 98% 15N L-leucine at different pH.(A) pH titration of the L-leucine amine. The 1D 15N spectra are recorded for 1024 scans at 25°C. (B) 15N chemical shift of the L-leucine amine as a function of pH. From the sigmoidal curve fit the pI is estimated to be 9.72 ± 0.06.DOI: http://dx.doi.org/10.7554/eLife.19314.008

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig1-figsupp6-v1.jpg)

**Figure 1—figure supplement 6.:** Spectra for samples prepared in NaCl or KCl are colored in red and black, respectively. Resonances originating from labelled leucine are indicated by their chemical shifts and their respective assignments. These results are in good agreement with the 15N 1D spectra, and only one set of chemical shifts from the ligand can be observed.DOI: http://dx.doi.org/10.7554/eLife.19314.009

To achieve sufficiently narrow line widths of the NMR signals and to avoid any signal from unbound leucine, we produced microcrystalline samples of LeuT (Figure 1—figure supplement 2), and performed cross polarization (CP)-based NMR experiments at temperatures above the freezing point. In all other preparations tested (frozen, lyophilized and proteoliposomes) the signal from the unspecific or unbound leucine completely dominated the spectra (Figure 1—figure supplement 3A–B). Using the microcrystalline preparations, we were able to produce the high quality CP-based 15N detected spectra showing one significant (above 2σ – Figure 1—figure supplement 4) peak at 38.2 ppm that could be assigned to the amine of protein bound leucine (Figure 1B). In addition to the sharp signal from leucine, much broader signals between 110 and 130 ppm were also observed, which originate from the 15N natural abundance of the LeuT amides (Figure 1B). To further assess whether the intense signal at 38.2 ppm reflects sodium specific leucine binding to LeuT, we performed a parallel experiment substituting Na+ with K+. Sodium is required for leucine binding (Zhao et al., 2011). By the use of 23Na-NMR we confirmed the presence of only a negligible amount of residual NaCl (at 7.1 ppm), and that no detectable Na+ was coordinated in the protein (Figure 1C). In the absence of Na+, the signal at 38.2 ppm in the 15N 1D spectrum disappeared as expected for a signal originating from 15N-leucine bound to LeuT (Figure 1B). Worth of note, the amine NH3+ group of free leucine has a chemical shift of approximately 41 ppm at pH 8 (Figure 1—figure supplement 5A–B), demonstrating that the bound substrate resides in a not fully solvent accessible environment. Importantly, we were unable to detect any signal from any additionally bound leucine. Similarly, the 13C CP/MAS spectra from the same samples clearly displayed only one single set of sodium dependent leucine signals (Figure 1—figure supplement 6).

To investigate whether the origin of the substrate peak at 38.2 ppm was due to leucine binding either to the S1 or the S2 site, we recorded solid state NMR spectra of two variants with compromised leucine binding, F253A (S1) and L400S (S2) (

![Figure 2.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig2-v1.jpg)

**Figure 2.:** (A–B) Cartoon representation displaying the location of F253 in the S1 site and L400 in the proposed S2 site based on PDB: 3USG (Wang et al., 2012a). (C) 15N 1D NMR spectrum of LeuT WT (red), F253A (green) and L400S (blue). Inset: Close-up of L-leucine specific peak. Spectra are tentatively intensity normalized to the 15N natural abundance signal from the LeuT amides.DOI: http://dx.doi.org/10.7554/eLife.19314.010

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Spectra are tentatively normalized to the LeuT natural abundance amide signal. As expected the substrate peak relates to LeuT concentration and not to the added free leucine concentration.DOI: http://dx.doi.org/10.7554/eLife.19314.011

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** To rule out that wrong phasing would cause the chemical shift difference observed for the substrate peak of the spectra presented in Figure 2C, we present the them also as power spectra (which is ultimately a squared magnitude spectra) where phase signs are not preserved. We have intensified the F253A signal to only demonstrate the chemical shift difference.DOI: http://dx.doi.org/10.7554/eLife.19314.012

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (A) Full spectrum displayed with a line broadening of the windows function of 100 Hz. Tentatively intensity normalized using natural abundance signals. (B and C) Close up of the substrate peak region showing preserved chemical shift difference between the substrate bound in LeuT WT (black dashed line) and LeuT F253A (blue dashed line) in two different free substrate concentrations.DOI: http://dx.doi.org/10.7554/eLife.19314.013

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/19314/elife-19314-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** Sodium ions are depicted in blue. Measured chemical shift values in red (in ppm) and measured distances in black (in Å). Image is made from PDB file: 3F3E.DOI: http://dx.doi.org/10.7554/eLife.19314.014

In conclusion, although all LeuT samples used in the present study were prepared in DDM at low concentration to exclude previously reported detrimental effects on the S2 binding site, we were only able to identify one single substrate signal at 38.2 ppm in the 15N spectra and one set of signals in the 13C spectrum (Figure 2—figure supplement 2). We note, however, that at our current signal-to-noise ratio (~20), we would not be able to detect species populated less than 5% of the structural ensemble. Based on the minor change in chemical shift in the F253A (S1) mutant, and the completely unaltered signal for the L400S (S2) mutant we reason that the observable bound leucine is located at the S1 binding site, thus supporting the idea that LeuT exhibit one single central binding site. We cannot exclude that the detection of S2 binding may only be possible upon the complete transition of the transporter towards a specific (yet unknown) conformation or that unfavourable crystal contacts might complicate S2 binding. However, several crystal structures have shown the binding of antidepressants, which overlaps with the putative S2 site, using these exact conditions (Singh et al., 2007; Zhou et al., 2009). As previously proposed for LeuT (Piscitelli et al., 2010) we speculate that the S2 substrate binding site, if present, is rather a transient site, responsible for optimal functionality of the transporter.

## Materials and methods

## Protein expression and purification

Expression of LeuT WT from Aquifex aeolicus was performed according to the protocol described previously (Billesbølle et al., 2015). LeuT WT was expressed in E. coli C41(DE3) transformed with pET16b encoding C-terminally 8xHis-tagged transporter (expression plasmid was kindly provided by Dr E. Gouaux, Vollum Institute, Portland, Oregon, USA). Briefly, isolated bacterial membranes were solubilized in 1% DDM (Anatrace, USA) in the presence of 1 mM 98% 15N-L-Leucine (Cambridge isotopes, Tewksbury, MA) and the protein was bound to nickel-charged affinity resin (Life Technologies, Carlsbad, CA). Subsequently, protein was eluted in 20 mM Tris-HCl (pH 8.0), 200 mM KCl, 0.05% DDM, 1 mM 15N-L-Leucine and 300 mM imidazole (KCl sample) or in the same buffer containing NaCl instead of KCl (NaCl sample). LeuT F253A and L400S variants were generated from the leuT gene using a QuikChange kit (Agilent Technologies, Santa Clara, CA) and purified similarly to the LeuT WT protein with the difference that 5 µM of 13C-15N-L-Leucine (Cambridge Isotopes) was used for co-purification, and the salt content in all buffers consisted of 50 mM NaCl and 150 KCl. The LeuT F253A variant in the presence of 1 mM substrate was prepared similar to the NaCl sample. Subsequently, all LeuT samples were dialyzed for approx. 36 hr at 4°C in the respective elution buffer without imidazole.

## Functional characterization of LeuT WT

Functional characterization of the LeuT WT purified in KCl was performed using a scintillation proximity assay (SPA) (Quick and Javitch, 2007). Saturation binding of [3H]leucine (50.2 Ci/mmol; PerkinElmer, Waltham, MA) to purified LeuT WT was performed with 100 ng/well (1.66 pmol) of protein in buffer composed of 20 mM Tris-HCl (pH 8.0), 200 mM NaCl, 0.05% DDM, 20% glycerol in the presence of 1.25 mg/ml copper chelate (His-Tag) YSi beads (PerkinElmer). Sodium-dependency was measured at fixed [3H]leucine concentration of 100 nM with increasing concentrations of NaCl (NaCl was substituted with KCl for equal ionic strength) again using 100 ng/well LeuT WT. [3H]Leucine binding was monitored using MicroBeta liquid scintillation counter (PerkinElmer) and data were fitted to a one-site saturation or dose-response function, respectively, using Prism 7 software (GraphPad, San Diego, CA).

## Preparation of microcrystals

Microcrystalline samples were produced by large scale sitting drop vapour diffusion method. 1 mL of the protein sample solutions were mixed 1:1 with the crystallization buffer composed of 100 mM NaCl (or KCl), 120 mM MgCl2, 28% PEG400, 100 mM MES or HEPES pH 6.5. The crystallization was carried out at 18°C. After approximately 20 hr a white precipitate could be harvested by centrifugation and transferred directly to the rotor. All samples were freshly prepared immediately before use. Microcrystals where visualized using a Leica M125 microscope with a 1.0x PlanApo objective.

## Lyophilized protein preparation

Protein for lyophilisation was depleted of glycerol during dialysis, snap-freezed in liquid nitrogen and added to a freeze drier. The remaining powder could be transferred directly to the rotor.

## Solution NMR

15N-L-Leucine was dissolved to a final concentration of 1 mM in the following buffer: 20 mM Tris-HCl (pH 8.0), 200 mM KCl, 0.05% DDM and added to an Economy WG5 NMR tube. The Experiment was run on a Bruker Avance III 500 MHz operating at a Larmor frequency of 50.667 MHz for 15N. The directly detected 15N spectra were recorded using a recovery delay of 2 s and an acquisition time of 500 ms. The total number of 1024 scans were used.

## Solid sate NMR

Microcrystalline LeuT nitrogen spectra were recorded on Bruker Avance III 800 MHz wide bore (89 mm) spectrometer equipped with a 4 mm MAS HCN efree probe. Spectra were obtained at 275 K (measured temperature), at 12500 Hz magic-angle-spinning. 15N CP/MAS experiments were run for 60 K scans in blocks of 10 K scans and the magnet was fine-tuned between each block. Cross-polarization contact time was set to 1750 us. Initial recovery delay was set to 3 s. Protons were decoupled at 86 kHz during acquisition. 13C CP/MAS experiments were run for 2 K scans. Cross-polarization contact time was set to 2000 us. The initial recovery delay was set to 3 s. Spectra were displayed using a 1, 10 or 100 Hz line broadening for EM window function in topspin.

Sodium MAS NMR spectra were recorded on a Bruker Avance NMR spectrometer operating at a Larmor frequency of 105.8 MHz for 23Na using a double resonance probe equipped for 4 mm (o.d.) rotors. All spectra were recorded at room temperature employing a central transition selective 90 degree pulse (1.8 μs), a recycle delay of 2 s, an acquisition time of 40.9 ms, a spectral width of 75.19 kHz and a spin rate of either 9 or 10 kHz. The spectra are referenced to crystalline NaCl at 7.1 ppm.
