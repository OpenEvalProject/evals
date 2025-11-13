# Measuring ligand-cell surface receptor affinities with axial line-scanning fluorescence correlation spectroscopy

## Authors

- Antonia Franziska Eckert<sup>1</sup>
- Peng Gao<sup>1</sup> ([ORCID: 0000-0002-5354-3944](https://orcid.org/0000-0002-5354-3944))
- Janine Wesslowski<sup>3</sup>
- Xianxian Wang<sup>3</sup>
- Jasmijn Rath<sup>1</sup>
- Karin Nienhaus<sup>1</sup> ([ORCID: 0000-0002-8357-846X](https://orcid.org/0000-0002-8357-846X))
- Gary Davidson<sup>3</sup> ([ORCID: 0000-0002-2264-5518](https://orcid.org/0000-0002-2264-5518)) †
- Gerd Ulrich Nienhaus<sup>1</sup> ([ORCID: 0000-0002-5027-3192](https://orcid.org/0000-0002-5027-3192)) †

### Affiliations

1. Institute of Applied Physics, Karlsruhe Institute of Technology Karlsruhe Germany
2. Institute of Nanotechnology, Karlsruhe Institute of Technology Karlsruhe Germany
3. Institute of Biological and Chemical Systems, Karlsruhe Institute of Technology Karlsruhe Germany
4. Department of Physics, University of Illinois at Urbana-Champaign Urbana United States

† Corresponding author

## Abstract

Development and homeostasis of multicellular organisms is largely controlled by complex cell-cell signaling networks that rely on specific binding of secreted ligands to cell surface receptors. The Wnt signaling network, as an example, involves multiple ligands and receptors to elicit specific cellular responses. To understand the mechanisms of such a network, ligand-receptor interactions should be characterized quantitatively, ideally in live cells or tissues. Such measurements are possible using fluorescence microscopy yet challenging due to sample movement, low signal-to-background ratio and photobleaching. Here, we present a robust approach based on fluorescence correlation spectroscopy with ultra-high speed axial line scanning, yielding precise equilibrium dissociation coefficients of interactions in the Wnt signaling pathway. Using CRISPR/Cas9 editing to endogenously tag receptors with fluorescent proteins, we demonstrate that the method delivers precise results even with low, near-native amounts of receptors.

## Introduction

In multicellular organisms, cell-cell communication is mediated to a large extent by cell surface receptors in the plasma membrane. They bind their cognate ligands from the extracellular space, which triggers a cascade of intracellular processes. Major signaling pathways form tightly regulated networks comprised of multiple receptors and protein ligands. Among these, Wnt signaling is an ancient and evolutionarily conserved, complex network that controls a variety of physiological processes essential for embryonic development and tissue homeostasis (Clevers and Nusse, 2012; Niehrs, 2012). There are 10 different Frizzled G-protein-coupled receptors binding 19 different Wnt glycolipoprotein ligands (in humans), and additional co-receptors and effector proteins are also crucially involved in the modulation of signal transduction (Niehrs, 2012). Knowledge about the strengths of the various biomolecular interactions is a prerequisite to understanding the function of such a complex network. Accordingly, the equilibrium dissociation coefficient, KD, which determines the fraction of ligand-bound receptors at a particular ligand concentration, should be measured for all relevant interactions in the network. To this end, a multitude of biochemical and biophysical in vitro assays have been devised. Those assays, however, may not completely emulate the complex environment of living cells and tissues; consequently, researchers are striving to measure biomolecular interactions as closely as possible to the real-life situation (Ries et al., 2009b; Ng et al., 2016).

Fluorescence correlation spectroscopy (FCS) is a powerful method for measuring ligand-receptor interactions within the plasma membrane of live cells (Bacia et al., 2006; Ries et al., 2009b; Dörlich et al., 2015). The technique requires that ligands and receptors are specifically labeled with different fluorescent markers so that their emission can be detected separately in two color channels. A confocal microscope allows a tiny observation volume (~1 fL) to be positioned within the sample, and the emitted fluorescence light is captured as a function of time (Zemanová et al., 2003). Fluctuations of the fluorescence intensity due to molecular diffusion into and out of the observation volume are analyzed by calculating intensity pair correlation functions, from which diffusion coefficients, related to the size of the diffusing entities, as well as local concentrations can be extracted. Importantly, dual-color cross-correlation analysis provides a means of selectively measuring the concentration of ligand-receptor complexes. Finally, KD values can be calculated from the local concentrations of free ligand as well as ligand-bound and ligand-free receptors.

The intrinsic dynamics of live cells and tissues poses considerable challenges to FCS measurements. Movement of the cell membrane within the observation volume gives rise to strong intensity fluctuations obscuring those resulting from molecular diffusion in the plane of the membrane. Line-scanning FCS (lsFCS) solves this problem by quickly scanning the observation volume perpendicularly through the membrane (Ries et al., 2009a). Another difficulty comes from the labeling procedure usually employed for live samples, that is the expression of fusion constructs of the proteins of interest with genetically encoded marker proteins of the GFP family (Nienhaus and Nienhaus, 2014). These markers are not as bright as synthetic dyes, and the signal-to-background ratio (SBR) is often small in the presence of the unavoidable cellular autofluorescence and especially at low expression levels, which are, however, desirable to avoid overexpression artifacts. The poor photostability of GFP-like proteins poses yet another challenge because the focused laser spot causes local photobleaching. Labels cannot be replenished efficiently from neighboring regions of the plasma membrane due to the low diffusivity of integral membrane proteins within biological membranes. Therefore, careful corrections are necessary to account for the loss of fluorescent labels.

Here, we present a novel framework for FCS-based measurement of ligand-receptor interactions featuring high sensitivity, precision and robustness. In contrast to earlier approaches (Ries et al., 2009a; Ries et al., 2009b; Dörlich et al., 2015), we employ axial (i.e. along the optical axis) line scanning at ultra-high speed by using a tunable acoustic gradient index of refraction (TAG) lens (Duocastella et al., 2014). This device allows us to sweep the observation volume through the membrane within a few microseconds and thus more than two orders of magnitude faster than with lateral line scanning by means of galvanometric scanners. With axial lsFCS, the correlation decay is significantly faster than with lateral lsFCS, resulting in shorter overall measurement times to reach comparable precision. Thus, changes in cellular morphology that may compromise the data are less likely to occur. Moreover, the much higher scanning frequency of TAG lens-based axial lsFCS results in an enhanced time resolution of the correlation functions. In dual-color cross-correlation experiments, optimal overlap of the observation volumes is much easier to achieve with axial lsFCS. It is also worth mentioning that, in a typical sample consisting of a layer of cells on a coverslip surface, axial scanning offers abundant spots for lsFCS measurements, greatly facilitating data collection. A new and powerful data analysis pipeline that includes background and photobleaching corrections allows us to extract precise equilibrium dissociation coefficients.

We have evaluated the method by measuring the binding of the Wnt signaling inhibitors human Dickkopf1 (DKK1) and Dickkopf2 (DKK2) to the Wnt co-receptor lipoprotein-receptor related protein 6 (LRP6) in human lung cancer (NCI-H1703) and human embryonic kidney (HEK293T) cells (Mao et al., 2001; Cruciat and Niehrs, 2013). For these interactions, KD values in the range of 0.3–0.5 nM (without error analysis) were determined by in vitro studies (Bafico et al., 2001; Mao et al., 2001; Semënov et al., 2001); a more recent paper reported 3 ± 1 nM (Bourhis et al., 2010).

As many biological studies involve overexpression of receptors far above the natural level, the effect of receptor density on the binding affinity is an issue of broad interest. To explore this issue, we varied the receptor density in the plasma membrane in the range 20–1000 µm–2 by using three different ways to express LRP6 receptors fused to fluorescent proteins in the cells. The respective gene was (1) introduced via transient transfection, or (2) stably integrated into the genome of cells by stable transfection, or (3) integrated into a cell line at the endogenous LRP6 gene locus by CRISPR/Cas9 editing. We have observed an impressive consistency in the KD determinations using LRP6 fused to mCherry and tdTomato markers, which differ considerably in size, brightness and emission spectrum (Shaner et al., 2005), attesting to the accuracy of the results. As another example, we have studied the binding of DKK1 to Kremen2, a receptor modulating the canonical Wnt signaling pathway, and the impact of LRP6 on this interaction (Davidson et al., 2002; Mao et al., 2002).

## Results

### 3D confocal microscope with fast axial scanning

Our home-built microscope is shown schematically in Figure 1a; details of the design are provided in Materials and methods and Figure 1—figure supplement 1. For dual-color excitation, we select two out of three available lasers (blue (470 nm), green (561 nm) and red (640 nm)), pulsing every 25 ns with a mutual delay of 12.5 ns. This pulsed interleaved excitation scheme (Müller et al., 2005) yields two time-separated intervals of 12.5 ns during which photons are collected in two color channels; channel crosstalk is thus strongly reduced. Photons are registered by a time-correlated single photon counting (TCSPC) unit. For each photon, we record the absolute time from the start of data acquisition, that is the macro time, tM, and the time elapsed since the previous laser pulse, that is the micro time, tµ. The observation volume, formed by tight focusing of the laser beam with a high-NA objective and a confocal detection pinhole, is scanned laterally (within the focal plane) by galvanometric mirrors. In addition, we use a TAG lens driven in resonance (147 kHz) to move the observation volume up and down along the optical axis by several micrometer in an oscillatory manner with a period of ~6.8 µs (Figure 1—figure supplement 2). In addition to tM and tµ, the TCSPC card stores the lateral positions, x and y, of the galvanometer mirrors for each photon counting event as well as the timing pulse, tTAG, at the beginning of each TAG lens oscillation cycle. From tTAG, the z position is determined by a mapping procedure accounting for the nonlinear axial displacement with time (Figure 1—figure supplement 3). As a consequence, the pixel dwell times vary with the displacement, so that the collected photon events need to be rescaled. Finally, dual-color 3D images can be reconstructed from the arrival times and locations of origin of all photons registered (Figure 1). Because axial scanning is fast, the voxel dwell times are short but can be effectively increased by multiple axial scans in succession at a chosen x-y position.

![Figure 1.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig1-v2.jpg)

**Figure 1.:** Shown are a schematic depiction of the microscope and (upper left) the excitation pulse sequence and the ensuing fluorescence emission. The sample cell (shown as a 3D image) is cut open to visualize axial scanning across the top membrane. The 3D image has been merged from four image slices (80 × 80 µm2, 256 × 256 pixels, three scans, each with pixel dwell time 60 µs). APD, avalanche photodiode.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** APD1 and APD2, avalanche photodiodes (τ-SPAD Single Photon Counting Module, PicoQuant, Berlin, Germany); BPF1 and BPF2, bandpass filters. For laser excitation at 470 nm: Brightline HC 525/50 or HC 520/35 with mCherry or tdTomato as receptor markers, respectively, for 561 nm: HC 600/37, for 640 nm: HC 676/37 (all Semrock, Rochester, NY); L1 – L3, picosecond pulsed lasers (L1: 561 nm (PDL 561, Abberior, Göttingen, Germany), L2: 470 nm (LDH-P-C-470B, Picoquant), L3: 640 nm (LDH-P-C-640B; PicoQuant)); LP1 – LP5, longpass dichroic mirrors (LP1: 532 nm longpass (AHF, Tübingen, Germany), LP2: 605 nm longpass (Thorlabs, Munich, Germany), LP3: 532 nm longpass (AHF), LP4: 575 nm longpass (Edmund Optics, Mainz, Germany), LP5: 555 nm longpass (FF555-Di02, Semrock); M, dichroic mirror; MMF, multimode fiber ((MMF-IRVIS-62.5/125–0.245 L, OZ Optics, Ottawa, Canada); MO, microscope objective (HCX PL APO W CORR CS 63x/1.2, Leica Microsystems, Wetzlar, Germany); Scanner, galvanometric laser scanner (Yanus V, Till Photonics, Gräfelfing, Germany); SMF, single mode fiber; SL, scan lens (AC254-040-A-ML, Thorlabs); TL, tube lens; TAG lens, tunable acoustic gradient index of refraction lens (model 2.0, TAG Optics, Princeton, NJ); QB, quad-band dichroic mirror (zt 405/473/561/640 RPC, AHF); QWP, quarter-wave plate (AQWP05M-600, Thorlabs); SMF, single-mode fiber; WDM, wavelength division multiplexer (RGB26HA, Thorlabs); WFC, wideband fiber coupler (TW630R5A1, Thorlabs).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Shown are x-z sections of the image of an 80 nm gold bead (EM.GC80, BBI solutions, Cardiff, UK) immobilized in an agarose hydrogel (3%, w/w) 30 µm above the cover glass, taken with 640 nm laser irradiation (a) without and (b) with the TAG lens oscillating in resonance. The scanned volume was 3 × 3 × 12 µm3. Scale bar, 1 µm. (c) Intensity profiles along lines 1–9 in panel b, which cross the focus laterally at different axial positions. The intensity profile without oscillating TAG lens is included for comparison (shaded in grey). (d) Full widths at half maximum (FWHM) of the lateral intensity distribution as a function of the axial position. The FWHM averaged over all axial positions is 0.53 ± 0.05 µm (mean ± SD). With the TAG lens switched off, the FWHM of the focus is 0.32 ± 0.01 µm laterally and 0.89 ± 0.02 µm axially. (e) Intensity within the x-y plane integrated within a circle of radius 0.25 µm around the center at various axial positions. Black curve: TAG lens turned off, blue curve: TAG lens turned on.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (a) Nonlinear axial scan performed by the TAG lens resonantly driven at 147 kHz. The curve was acquired by scanning a cover glass at 300 equally spaced axial positions (displacement 50 nm each) by using the piezo transducer of the microscope (total scan range 15 µm, 8 µm selected for the analysis, 0.12 s/position), with the TAG lens turned on. The photons reflected from the bottom surface of the cover glass were registered by the TCSPC card. The data were rearranged into an image to establish a relation between the time elapsed since the preceding TAG lens timing pulse, t, and the axial position, z. The data points (shifted along the y-axis to represent the focus displacement with respect to the cover glass) are shown as yellow spheres, the blue line is a fit with a Fourier sum,$zt=z_{0}+z_{1}sin⁡(2\pit/T+\phi_{1})+z_{2}sin⁡(4\pit/T+\phi_{2})+z_{3}sin⁡(6\pit/T+\phi_{3})$, yielding z0 = 2.41 µm, z1 = –2.58 µm, z2 = 0.33 µm, z3 = –0.08 µm; $\phi_{1}$ = 1.25 rad, $\phi_{2}$ = 0.90 rad, $\phi_{3}$ = 0.56 rad, T = 6.8 µs. (b) The fit function was then used to reassign all registered photons to specific axial positions of the TAG lens, covering a complete TAG lens scanning period. (b) Symbols: Intensities of the brightest pixel in each column for 50 TAG lens positions equally spaced along the axial direction, normalized to a scale between 0 and 1. Red line: fit with a polynomial, $I(z)=\sumi=0i=7a_{i}z^{i}$, with a0 = 1.27, a1 = ‒12.53, a2 = 63.53, a3 = ‒87.72, a4 = ‒163.38, a5 = 616.21, a6 = ‒649.88, a7 = 233.49. We took the brightest pixel for correcting the intensities and not the integrated intensity shown in grey because, in the axial lsFCS data analysis, the membrane positions, zMEM1(t) and zMEM2(t), are also determined from the pixels with the highest photon counts.

### Comparison of axial and lateral lsFCS

We compared the two scanning modes with Atto647N-labeled giant unilamellar vesicles (GUVs) as a simple model system offering excellent SBR (Figure 2a). We took axial lsFCS data by continuously scanning through the top of a GUV for 60 s in an oscillatory fashion (Figure 2b). These data can be visualized as kymographs, displaying the intensity during the axial sweeps along the x-axis and multiple sweeps in succession along the y-axis (Figure 2c). We determine the intensity as a function of time by integrating over the emission signal during each membrane crossing event. From the intensity time trace, we calculate an autocorrelation function, which can be fitted very well with a model function based on a circular observation area in the x-y plane and 2D diffusion within the membrane (Figure 2d),

$$
G(\tau)=N^{−1}(1+\tau/\tau_{D})^{−1}.
$$

![Figure 2.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig2-v2.jpg)

**Figure 2.:** (a) 3D image of a GUV (diameter 60 µm), showing the scanning directions of the focus across the membrane in lateral and axial lsFCS; scale bar, 10 µm. (b) Axial focus position during a single oscillation cycle of 6.8 µs. (c) Kymograph, horizontal axis: intensity during axial focus oscillations (averaged over 500 ms), vertical axis: sequence of 500 ms periods during 60 s of axial scanning. Lines mark the membrane positions. (d) Autocorrelation curves for axial (blue) and lateral (black) scanning; points: experimental data; lines: fits with Equations (1) and (2), yielding τD = 36 ± 1 ms with axial scanning and τD = 46 ± 2 ms, S = 4.0 ± 0.3 with lateral scanning, respectively. The lateral lsFCS autocorrelation data have also been scaled to the axial ones (grey) for better comparison. Observation areas on the plasma membrane are depicted schematically in the corresponding colors, possible dye trajectories are shown in red. (e) Standard deviation (SD), calculated for two groups of seven normalized lateral (black) and axial (blue) lsFCS curves, plotted as a function of the overall time of data acquisition. For details, see Materials and methods.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Confocal images of multi-color spheres excited at (a) 470 nm and (b) 561 nm. (c, d) Symbols: intensity distribution along the dashed lines in panels a and b, respectively. Lines: Gaussian fits, yielding FWHM values of 258 ± 8 nm and 300 ± 10 nm for 470 and 561 nm excitation. Confocal width parameter, ω0 (corresponding to a 1/e2 intensity drop), measured on ten multi-color beads with excitation at (e) 470 nm and (f) 561 nm. Boxes mark the SE. The median is indicated by the central line, the mean as a black circle. Whiskers mark the full range.

Here, τ is the lag time and $\tau_{D}$ is the diffusional correlation time. The amplitude of the autocorrelation function, $G0$, equals the inverse of the average number of fluorescently labeled molecules in the observation area, N, which is the product of the average concentration (i.e. area density), C, and focal area, A, so that $N=C∙A=C∙\pi\omega_{0}^{2}$. Here, ω0 is the radial distance over which the intensity in the focal plane decays by a factor of e–2 (for details, see Figure 2—figure supplement 1 and Materials and methods). For lateral line scanning of the focus along the x direction, the resulting $G\tau$ has a much lower time resolution (millisecond scale, Figure 2d) due to the lower speed of galvanometer scanning. Moreover, $G\tau$ decays more slowly than with axial scanning because the observation area in the y-z plane, $A=\pi\omega_{0}z_{0}$, is significantly larger and elongated (Figure 2d, insets) because the axial extension, z0, of a confocal spot is about five times greater than the lateral one. Thus, there are more fluorophores in the observation area on average, resulting in a smaller amplitude, $G0$, of the autocorrelation function (Figure 2d). Fluorophores reside longer in the observation area and are thus more prone to photobleaching. The corresponding diffusional autocorrelation function,

$$
G(\tau)=N^{−1}(1+\tau/\tau_{D})^{−1/2}(1+S^{2}\tau/\tau_{D})^{−1/2},
$$

contains an extra anisotropy parameter, S = ω0/z0, which makes fitting more ambiguous. To conclude, axial lsFCS has several advantages over lateral scanning, resulting in a markedly reduced data acquisition time for comparable data quality (Figure 2e). Notably, an overall shorter measurement is less likely to be spoiled by sample movement, which is unavoidable in experiments on live specimens.

### Analysis of fast axial lsFCS on live cells

In live-cell experiments, we survey cultured cells by collecting 3D image stacks to select suitable locations for axial lsFCS (Figure 3a, b). Subsequently, fluorescence intensity time traces are recorded from these spots for typically 60 s in two color channels. Notably, the unavoidable intrinsic background fluorescence of live samples and photobleaching of the markers during the experiment can severely compromise the analysis of FCS data. To cope with these adverse effects, we apply appropriate corrections to the data, which we illustrate with an axial lsFCS experiment on a stably transfected cell expressing LRP6-mCherry, exposed to conditioned medium (CM) containing DKK1-eGFP. The axial lsFCS data are visualized as kymographs, 2D plots of the intensity along the scan line versus time (Figure 4a). From these data, we determine the membrane positions, zMEM1(t) and zMEM2(t) based on the pixels with the highest photon counts (Figure 4a, thick white lines) and compute intensity time traces, IMEM1(t) and IMEM2(t), by integrating each scan over the pixel with the highest photon count and the neighboring two pixels on either side. Finally, the two membrane signals are joined into one raw intensity time trace for each color channel, $I_{raw}t$. For background determination, we add the intensities of four regions of one pixel each, ~2 µm (10 pixels) to the left and right of zMEM1(t) and zMEM2(t) (Figure 4a, thin white lines). After scaling the background trace to the respective signal trace according to the pixel numbers, we subtract the background from the raw signal trace, $I't=I_{raw}t-I_{bg}(t)$. In Figure 4b, we have plotted the raw signal intensities, IG,raw(t) and IR,raw(t), and the scaled background intensities, IG,bg(t) and IR,bg(t), in the green and red channels, respectively, during a typical 60-s experiment.

![Figure 3.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig3-v2.jpg)

**Figure 3.:** Confocal images of cells were selected from image stacks taken sequentially (to avoid crosstalk) with 561 (3 µW) and 470 nm (5 µW) laser excitation to visualize (a) LRP6-mCherry and (b) DKK1-eGFP. A volume of 65 × 65 × 25 µm3 was scanned with 256 × 256 × 64 pixels (pixel dwell time, 40 µs). Shown are a lateral slice near the glass coverslip and cross-sections along the lines marked in the lateral view. Scale bars, 10 µm.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (a) Time dependence of the DKK1-eGFP emission from the cell membrane of transfected HEK293T cells expressing LRP6-mCherry after adding conditioned medium (CM) containing the ligand at different concentrations. Time-lapse spinning disk confocal images (200 ms frames every 100 s) were recorded for 1 hr, λexc = 488 nm, λdet = 525 ± 25 nm. Symbols, data; lines, exponential fits. Inset: concentration dependence of the apparent association rate coefficients obtained by exponential fits of the kinetic traces. Linear regression yields kon = (5.0 ± 0.2)×10‒4 nM‒1 s‒1, koff = (1.3 ± 0.1)×10‒3 s‒1, resulting in Kd = 2.6 ± 0.1 nM. We note that such measurements on individual cells are highly unreliable due to large systematic errors. (b) DKK1-eGFP emission decrease after removing unbound DKK1-eGFP ligands by two successive washing steps. 200 ms frames were recorded every 300 s for up to 3 hr. Symbols, data; lines, exponential fits. For an ensemble of 50 cells, koff = (2.6 ± 0.2)×10‒4 s‒1 was obtained as an average. Fixing this koff intercept in a linear regression of two apparent rate coefficients (at 3.5 and 7 nM, averages over 50 cells) yielded kon = (6.7 ± 0.2)×10‒4 nM‒1 s‒1 and Kd = 0.4 ± 0.1 nM. We note that the Kd value obtained by these extremely tedious experiments agrees within the error with the one measured by axial lsFCS (Table 1). (c) Confocal images of LRP6-mCherry (top) before (0 s) and after (300, 600, 900 and 1200 s) adding CM with 5.1 nM DKK1-eGFP (bottom).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (a) Confocal laser scanning microscopy images showing cell surface localization and relative expression levels of LRP6-mCherry in live cells. Non-specific autofluorescence is seen only adjacent to the nucleus (top panel with wt cells). (b) SDS-PAGE/western blot analysis showing relative expression levels of LRP6 receptor proteins in lysates from CRISPR/Cas9 and stable cell lines, compared to endogenous LRP6 from wt NCI-H1703 cells. Prior to harvest of cell lysates, cells were treated overnight with either control (con) CM or mWnt3a CM as indicated. Note the expected size increase of the LRP6 fusion protein upon tagging as well as the characteristic upshift of the LRP6 receptor protein upon Wnt stimulation, confirming Wnt-dependent receptor modification. The latter effect is less obvious in the stably expressing LRP6-mCherry cell line. Transferrin receptor (TfR) was used as a protein loading control. Transiently transfected cells were not included on the western blot as NCI-H1703 cell transfection efficiency is too low to allow comparison of average expression levels and instead requires analysis of single cells by microscopy. (c) TOPFLASH Wnt/β-catenin reporter assay showing the relative responsiveness of the LRP6-mCherry cell lines to both Wnt stimulation and DKK1-eGFP inhibition. Cells in 96-well plates were transfected with 20/5 ng of TOPFLASH/Renilla reporters, 8 ng mouse Wnt3a and 25 ng human DKK1-eGFP as indicated. 48 hr post transfection, cell lysates were harvested for luciferase assays. Note that both the CRISPR/Cas9 edited cell line and the cells stably expressing LRP6-mCherry respond to Wnt3a and DKK1 in the expected manner.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (a) SDS-PAGE/Western blot analysis showing relative expression levels of LRP6-mCherry and LRP6-tdTomato from lysates of the corresponding CRISPR/Cas9 cell lines. Note the presence of lower molecular weight wt LRP6 bands in both endogenously-tagged cell lines, in line with heterozygous tagging of the endogenous LRP6 locus in NCI-H1703 cells. Note also the higher apparent expression of the endogenously tagged LRP6 allele compared to the unedited allele in lysates from both CRISPR/Cas9 cell lines. (b) Confocal laser scanning microscopy images of CRISPR/Cas9 edited cells showing a direct comparison of cell surface localization and fluorescence intensity of the two endogenously tagged LRP6 receptor proteins.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** (a) TOPFLASH Wnt/β-catenin reporter assay. HEK293T cells in 96-wells were transfected with 25/5 ng TOPFLASH/Renilla reporters, 8 ng mWnt1, 1 ng mFrizzled8, 1 ng hDKK1-eGFP, 1 ng V5-xKremen2, 1 ng V5-xKremen2-mCherry and 1 ng V5-xKremen2-eGFP as indicated. 24 hr post transfection, cell lysates were harvested for luciferase reporter assay. Note that, in the absence of DKK1-eGFP, the fluorescently tagged Kremen2 receptors show marginally greater inhibition of Wnt signaling compared to non-fluorescently tagged Kremen2 (compare lanes 4, 5 and 6). In the presence of DKK1, however, all Kremen2 constructs show a strong reduction (compare lane 3 with lanes 7, 8 and 9), confirming that they retain their ability to synergize with DKK1 in Wnt inhibition. (b) Western blot analysis to visualize the integrity of both V5-xKremen2-mCherry and V5-xKremen2-eGFP.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** Schematic depiction of the LRP6 tagged locus at exon 23. The gene sequence of LRP6, the sequence and position of the guide RNA (gRNA) and the PAM site as well as the integration site are shown. The donor DNA includes the left and right homology arms (LHA, RHA) of indicated length, the FP gene and the resistance cassette.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** Sequences of individual strands.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig3-figsupp7-v2.jpg)

**Figure 3—figure supplement 7.:** (a) Wnt/β-catenin signaling response of different cell lines and their corresponding LRP6 receptor proteins to Wnt3a ligand stimulation. Upper graph: TOPFLASH Wnt reporter assay under both control and Wnt3a stimulated conditions. Wt and CRISPR/Cas9 edited NCI-H1703 cells harboring LRP6 tagged with either mCherry or tdTomato were transfected with TOPFLASH reporter and treated overnight with either control CM (con CM) or Wnt3a CM as indicated. Lower panels: Western blots showing either wt LRP6, LRP6-mCherry or LRP6-tdTomato proteins expressed by the different cell lines. Note the expected size increase of the LRP6 fusion protein upon endogenous tagging with either mCherry (25 kDa, compare lanes 1 and 3) or tdTomato (50 kDa, compare lanes 1 and 5). The fainter, lower molecular weight LRP6 bands visible in CRISPR/Cas9 edited cells correspond to wt LRP6 expressed from the unedited LRP6 allele of the heterozygous edited cells, which are not visible in the anti-mCherry Western blot. Note also the Wnt-induced upshifts of bands for wt LRP6 (compare lanes 1 and 2) as well as the LRP6-mCherry (compare lanes 3 and 4) and LRP6-tdTomato (compare lanes 5 and 6) fusion proteins, confirming that correct covalent modification of LRP6 occurs upon Wnt pathway stimulation. Wnt-dependent activation of endogenously fluorescently tagged LRP6 was further confirmed by analysis of LRP6 phosphorylation, using a phospho-specific LRP6 antibody (Sp1490). As can be seen in the pLRP6 western blot panel, an increase in phosphorylation levels accompanies the upshifted LRP6 bands (compare lane 2 with 1, 4 with 3 and 6 with 5). Total LRP6 protein levels were assessed using LRP6 specific antibodies, a mCherry antibody was used to specifically detect LRP6 fused to either mCherry or tdTomato and an antibody specific for the TfR was used as a loading control. (b) Cell surface biotinylation assay and western blot analysis to detect LRP6 located specifically on the plasma membrane and the effects of Wnt and DKK1 CM on membrane localization. Wt (upper panels) as well as CRISPR/Cas9 edited NCI-H1703 cells harboring tagged LRP6-mCherry (lower panels) were treated with con CM, DKK1-eGFP CM or mWnt3a CM for 2 hr. Cell surface proteins were biotinylated and purified by affinity pull-down using NeutrAvidin-agarose beads, LRP6 was specifically detected by immunoblotting. Note that slightly greater amounts of cell surface LRP6-mCherry were obtained from CRISPR/Cas9 edited cells compared to wt cells (compare lanes 1 and 4), in line with our observations that endogenously tagged LRP6 is expressed at somewhat higher levels. Note also the Wnt-dependent upshift of cell surface localized LRP6 (compare lanes 1 and 3) and LRP6-mCherry (compare lanes 4 and 6) from wt and CRISPR edited cells, respectively. Incubation with DKK1-eGFP resulted in a small reduction of cell surface LRP6 levels as well as LRP6 size. I: input; CS: cell surface (biotinylated proteins); FT: flow through. The TfR was used as a loading control. The sample loading ratio for I:CS:FT was 2:20:1.

![Figure 3—figure supplement 8.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig3-figsupp8-v2.jpg)

**Figure 3—figure supplement 8.:** (a, b) TOPFLASH Wnt reporter assays showing the effect of siRNA-mediated silencing of all LRP6 receptors (siLRP6) or only the endogenously tagged LRP6 receptors (siCherry/siTomato). CRISPR/Cas9 edited NCI-H1703 cells expressing endogenously-tagged LRP6-mCherry (a) and LRP6-tdTomato (b) as well as wt cells (a and b) were co-transfected in 96-well format with 3.3 pmol siRNA (targeting either LRP6, mCherry or tdTomato) and 25/5 ng TOPFLASH/Renilla reporters. 18 hr post-transfection, cells were treated overnight with control or Wnt3a CM before harvesting cell lysates for luciferase assays. For each treatment, luciferase values were set to one for the control samples in order to compare Wnt responsiveness between cell lines. As expected, knockdown of all LRP6 receptors with siLRP6 resulted in a strong reduction of the Wnt-induced TOPFLASH signal, although the LRP6-tdTomato CRISPR cell line displayed a somewhat weaker reduction. For specific knockdown of the endogenously tagged LRP6-mCherry species using siCherry, the degree of Wnt activation was significantly reduced when compared to the effect of siCherry on the corresponding wt cells. This partial reduction confirms that LRP6-mCherry contributes to Wnt signaling activity seen in these cells but that siRNA resistant, non-tagged LRP6 remains. Similarly, for LRP6-tdTomato silencing using siTomato, a significantly reduced Wnt activation was observed when compared to the effect of siTomato on wt cells. These results confirm that LRP6-mCherry and LRP6-tdTomato are active in Wnt reception, and, in agreement with our sequencing results of the CRISPR/Cas9 cell lines, that both cell lines are heterozygous, such that only one of the LRP6 alleles has been endogenously tagged. (c) Western blot analysis of LRP6, LRP6-mCherry and LRP6-tdTomato from wt and CRISPR/Cas9 edited NCI-H1703 cell lines after the indicated siRNA transfections. Cells were transfected with 39.6 pmol siRNA in 24-well format and cell lysates were harvested after 48 hr for Western blot analysis. Note that knockdown using siLRP6 leads to complete loss of all LRP6 receptor proteins (lanes 2, 6 and 9), whereas knockdown using siCherry (lane 7) or LRP6-tdTomato (lane 10) results in specific loss of the endogenously tagged LRP6 bands with higher molecular weight, and not the lower molecular weight wt LRP6 bands. These results further confirm that the CRISPR/Cas9 edited cell lines are heterozygous with respect to targeted endogenous tagging of LRP6. The band intensities also confirm that the endogenously tagged LRP6 receptors are expressed at higher levels than their corresponding wt receptors. Vinculin was used as a loading control.

![Figure 3—figure supplement 9.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig3-figsupp9-v2.jpg)

**Figure 3—figure supplement 9.:** (a) NCI-H1703 cells in 96-well format were transfected with 20/2 ng TOPFLASH/Renilla reporters. 16 hr post transfection, mWnt3a CM was added for 6 hr, followed by a 12 hr treatment with either DKK1-eGFP or DKK2-eGFP CM, as indicated, before cell lysates were harvested for the luciferase assay. (b) Western blot analysis to visualize the integrity of the DKK1-eGFP and DKK2-eGFP fusion proteins present in the CM. The DKK1 and DKK2 fusion proteins show major bands at ~68 and~58 kDa, respectively. The expected molecular weights are 56 kDa for DKK1-eGFP and 55 kDa for DKK2-eGFP, suggesting that DKK1-eGFP has more post-translational modification(s), which is consistent with the appearance of additional bands for DKK1-eGFP. The amounts of original CM loaded were 0.33 µl for DKK1-eGFP and 10 µl for DKK2-eGFP.

![Figure 4.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig4-v2.jpg)

**Figure 4.:** (a) Kymograph of the membrane scan recorded in the green (ligand, left) and red (receptor, right) color channels, showing the fluorescence from the membrane during 60 s of axial scanning (500 ms binning time). Thick white lines trace the membrane positions. (b) Time traces of the raw ligand (IG,raw) and receptor (IR,raw) intensities from the membrane and the corresponding background, IG,bg and IR,bg, determined ±10 pixels away from the membrane (thin white lines in panel a). Lines through, IG,bg and IR,bg are sums of six sine functions fitted to the data for noise filtering. (c) Autocorrelation (cyan, DKK1-eGFP; magenta, LRP6-mCherry) and cross-correlation (blue) functions after background and photobleaching corrections.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (a) Correlation curves at various different receptor densities due to different cell types and receptor expression techniques, all at 0.1 nM DKK1-eGFP. (b) Correlation curves measured on transiently transfected NCI-H1703 cells at various DKK1-eGFP concentrations indicated in the individual panels.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Symbols (cyan and magenta, autocorrelations; blue, cross-correlation) represent averaged data (mean ± SEM) over at least nine axial lsFCS measurements of 60 s each; lines are fits with Equation 1 (a) Correlation functions from cells expressing LRP6-mCherry (magenta) and Mem-eGFP (cyan). Mem is a membrane marker peptide consisting of the 20 N-terminal residues of neuromodulin, which contains a palmitoylation sequence. As expected, the cross-correlation amplitude is zero because both labeled moieties diffuse independently in the plasma membrane. (b) Correlation curves of LRP6 fused to both mCherry and eGFP. The autocorrelation amplitudes are different and reflect the greatly different maturation yields of the two fluoresscent proteins. The cross-correlation amplitude is significant, revealing a sizeable fration of constructs carrying both fluorophores. Notably, the function Γ (Equation 5) equals 0.14 ± 0.02 and is thus identical to the value obtained for HEK293T cells transiently transfected with LRP6-mCherry and exposed to saturating concentrations of DKK1-eGFP (see Figure 6—figure supplement 1, Table 1), as we should expect. (c) Correlation curves of LRP6-tdTomato, with tdTomato excited with 470 nm (4–5 µW) and 561 nm (<1 µW) laser light; emission was detected in the red channel with a bandpass filter 600/37 nm (center/width). Using the same fluorophore for dual-color excitation (PIE), photobleaching is identical for both color channels and perfect cross-correlation is ensured. The cross-correlation amplitude is expected to be (GG(0) + GR(0))/2 for complete overlap of the green and red foci, as we observe in the data.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (a) The flow chart lists the individual steps of the data analysis procedure. Tasks in light gray boxes are performed using Matlab. Tasks in dark gray boxes are processed in Origin Pro. (b) Source data files illustrate the individual steps. (c) To obtain reliable and reproducible results, data selection occurs according to the stringent criteria given here.

A significant loss of signal is apparent in the intensity time traces, indicating that photobleaching continually removes fluorescent markers from the observation area. We compensate the intensity decrease by calculating $I'(0)/I'(t)$ and fitting this ratio with a smooth function, $\gammat$, which we heuristically model as a sum of six sine functions (Dörlich et al., 2015). Then, we multiply the intensity time trace by this function, $It=I't∙\gamma(t)$. Finally, we calculate intensity autocorrelation functions of the green and red color channels, $G_{C}\tau$ (color index C = G, R, respectively), and the cross-correlation function, $G_{\times}\tau$

$$
G_{C}(\tau)=\frac{1}{⟨\gamma(t)⟩}⋅(\frac{⟨I_{C}(t)⋅I_{C}(t+\tau)⟩}{⟨I_{C}(t)⟩^{2}}−1),
$$



$$
G_{\times}(\tau)=\frac{⟨I_{G}(t)⋅I_{R}(t+\tau)⟩}{⟨I_{G}(t)⟩⟨I_{R}(t)⟩}−1.
$$

The angular brackets denote time averages over the total duration of the experiment. Importantly, the amplitudes of the autocorrelation functions have to be rescaled by $\gammat^{-1}$ to correct for the loss of fluorophores due to photobleaching. G×(τ), however, does not require rescaling because photobleaching decreases the numerator and denominator in Equation 4 to equal extents so that the effect cancels. The correlation functions resulting from the single 60-s axial scanning data in Figure 4a, b are plotted in Figure 4c together with fits using the diffusional model correlation function, Equation 1. For illustration purposes, more correlation functions are presented in Figure 4—figure supplement 1. These data were measured under systematic variation of receptor density and ligand concentration. We have also included correlation curves of three sets of control experiments on live HEK293T cells as Figure 4—figure supplement 2. As a negative control, we have co-expressed our LRP6-mCherry receptor with the membrane marker Mem-eGFP. Both molecules diffuse within the plasma membrane but do not interact. Accordingly, the resulting cross-correlation has zero amplitude (Figure 4—figure supplement 2a). As a positive control, we have chosen LRP6-mCherry-eGFP, so that each receptor carries a green and a red fluorescent (or non-fluorescent) protein (Figure 4—figure supplement 2b). As another positive control, we have used LRP6-tdTomato, which can be excited at 470 and 561 nm. This experiment is expected to yield complete cross-correlation of the signals from the two color channels, so that the correlation amplitudes differ only due to the wavelength-dependent observation areas (Figure 4—figure supplement 2c). Experimental details have been included in the figure caption and Materials and methods section.

To achieve a high precision in KD determination, the ligand concentration in the CM has to be carefully measured, for example by solution FCS or spectrometrically (for details, see Materials and methods). We dilute the stock solution with cell culture medium, incubate the cells and perform axial lsFCS experiments for several logarithmically spaced ligand concentrations covering the region around KD. This range can easily be identified in confocal images of cultured cells by determining the ligand concentration above which membrane staining by ligands is clearly visible. If KD values are in the nanomolar range and below, even lower ligand concentrations are required in the CM. Consequently, the kinetics of ligand-receptor formation are slow and sufficient time must be allowed to ensure equilibration before the measurement (Figure 3—figure supplement 1).

Fits of the experimental correlation functions $G_{G}(\tau)$, $G_{R}\tau$ and $G_{\times}(\tau)$ with Equation 1 yield the amplitudes, $G_{G}0$, $G_{R}(0)$ and $G_{\times}(0)$, for each ligand concentration. We then compute the expression,

$$
Γ(C_{L})=\frac{G_{\times}(0)^{2}}{G_{G}(0)G_{R}(0)}(C_{L})=A\beta⋅\frac{1}{1+\frac{K_{D}}{C_{L}}}.
$$

$Γ(C_{L})$ is the key function in our quantitative analysis and represents simply a scaled equilibrium binding isotherm, $FC_{L}=1+K_{D}/C_{L}^{-1}$. $FC_{L}$ represents the fraction of ligand-bound receptors, which depends on the ratio between the KD of the ligand-receptor pair and the ligand concentration, CL. The prefactor A depends on the detection areas and is a few percent shy of one for our excitation wavelengths (470 and 561 nm); the ratio between receptors carrying a functional fluorescent domain and all (exogenous or endogenous) receptors capable of specific binding is given by the parameter β. We note that, in Equation 5, we make the (optimistic) assumption that all receptors fused to fluorescent markers are expressed in their functional form, that is that they are competent of binding to their cognate ligand. Likewise, all ligand proteins dispersed in the CM are assumed to be able to recognize the receptor. A derivation and detailed discussion of the validity, assumptions and limitations of Equation 5 are given in Materials and methods. The parameters β and KD are determined by non-linear least-squares fits of Equation 5 to the data. Exemplary data on DKK1-eGFP binding to LRP6-mCherry measured on stably transfected NCI-H1703 cells are shown in Figure 5. In addition to data and fits of $Γ(C_{L})$ (Figure 5a), we have plotted $FC_{L}$ together with the scaled experimental data (Figure 5c). Figure 5e displays, for all individual 60-s experiments, the photobleaching parameters $\gammat$ used to correct the autocorrelation functions (Equation 3). In our analyses, we have observed that the function $Γ(C_{L})$ is very robust against background due to cancellation effects (see Materials and methods). To illustrate this point, we have plotted results for the same experimental data as in Figure 5a but calculated without prior background correction of the intensity time traces (Figure 5b, d, f). Indeed, there is only a small and insignificant change of the resulting KD parameter from 0.08 ± 0.01 nM to 0.10 ± 0.02 nM, with and without background correction, respectively. The entire sequence of data analysis steps including data quality management is summarized in Figure 4—figure supplement 3.

![Figure 5.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig5-v2.jpg)

**Figure 5.:** Panels on the left and right show the data with and without background correction, respectively. (a, b) Ligand concentration dependence of the function $Γ(C_{L})$ defined in Equation 5. (c, d) Fractional occupancies, F(CL), of receptors with DKK1 ligands. Symbols: experimental data (mean ± SEM) from five axial scans of 60 s each; lines: fits with Equation 5, yielding the parameters KD = 0.08 ± 0.01 nM and β = 0.44 ± 0.02 with background correction and KD = 0.10 ± 0.02 nM and β = 0.31 ± 0.01 without. (e, f) Parameter ⟨γ(t)⟩ used for photobleaching correction of the autocorrelation functions. Each point represents an individual 60 s scan. Boxes mark the 25–75% range. The median is indicated by the central line, the mean as a black square; whiskers indicate the SD.

### DKK1 and DKK2 binding to LRP6-mCherry

To examine the reliability of our axial lsFCS-based analysis for the determination of KD values of ligand-receptor interactions, we studied DKK1-eGFP binding to NCI-H1703 lung cancer cells expressing LRP6-mCherry in widely differing amounts. To this end, we transiently transfected cells with LRP6-mCherry. Moreover, we used a cell line harboring stably integrated LRP6-mCherry and a CRISPR/Cas9 edited cell line expressing endogenously tagged LRP6-mCherry. A detailed characterization of both cell lines is provided in Figure 3—figure supplement 2. HEK293T cells transiently expressing LRP6-mCherry were also included in this comparison. We calculated receptor densities from $G_{R}0$ and the size of the observation area (Figure 6a). Note that these figures include only receptors carrying a functional (i.e. fluorescent) mCherry tag; the real numbers are roughly a factor of two greater, assuming a chromophore maturation yield of around 0.5 for mCherry (Maeder et al., 2007; Yasuda et al., 2006). In any case, it is evident that the different types of gene insertion yield widely different LRP6-mCherry receptor densities at the cell membrane, ranging from 18 µm–2 for the CRISPR/Cas9 edited cells to ~1000 µm–2 for strongly overexpressing HEK293T cells. As one might expect, the relative scatter of receptor densities is greater for transiently transfected cells than for CRISPR/Cas9 edited and stably transfected cells. The ligand concentration dependencies of the fractional occupancies, $FC_{L}$, are plotted in Figure 6b; the corresponding $Γ(C_{L})$ data (Equation 5) are included as Figure 6—figure supplement 1. These data reveal a systematic effect of the expression level on the affinity. We find KD values of 0.08 ± 0.01 and 0.09 ± 0.01 nM for cell lines harboring stably integrated LRP6-mCherry and CRISPR/Cas9 edited cells, whereas three- to fourfold lower affinities are observed for transiently transfected cells. KD values and other parameters from the analysis are compiled in Table 1. For NCI-H1703 cells, the fraction of fluorescent receptors, β, varies widely, from 14% in the CRISPR/Cas9 cells to 47% in the overexpressing cells. On the one hand, β depends on the fraction of endogenously produced (unlabeled) receptors, which are present also in the (haploid) gene edited cells; on the other hand, β depends on the ability of the gene construct and the cell line to produce fully mature, fluorescent fusion proteins. For strongly overexpressing cells, this latter effect is predominant because their endogenous receptor production can be neglected. Accordingly, the β parameter is highest for the transiently overexpressing NCI-H1703 cells. However, a word of caution is in order here. As we discuss in Materials and methods, the amplitude of $Γ(C_{L})$, which is controlled by β in our model, Equation 5, in fact also decreases with the maturation yield of the ligand marker and in the presence of non-functional receptors carrying a fluorescent label (see Materials and methods). We believe that this latter issue explains the relatively small amplitudes found for HEK293T cells. The diffusion coefficients (DG, DR) calculated from the correlation decay times of $G_{G}\tau$ and $G_{R}\tau$ (Table 1) are around 0.3 – 0.4 µm2 s–1. However, their uncertainties are comparatively large, perhaps due to the intrinsic structural heterogeneity of the plasma membrane.

![Figure 6.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig6-v2.jpg)

**Figure 6.:** (a) Densities of fluorescently labeled receptors, determined from the autocorrelation amplitudes, GR(0), using ω0 = 0.25 µm. Each data point corresponds to an individual 60-s experiment. Boxes mark the 25 – 75% range; the median is shown as the central line and the mean as a black square. Whiskers indicate the SD. (b) Fractional occupancies, $FC_{L}$, of receptors with Dkk1-eGFP as a function of the ligand concentration in the CM. Symbols (shapes/colors as in panel a), experimental data (mean ± SEM from at least three axial scans of 60 s each); lines, fits with Equation 5.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Г(CL) is plotted as a function of the DKK1-eGFP concentration CL. (a) Transiently transfected HEK293T cells. Data taken with DKK1-eGFP-SNAP as a ligand are included in cyan. (b) Transiently transfected NCI-H1703 cells. (c) Stably transfected NCI-H1703 cells. (d) NCI-H1703 cells expressing endogenously tagged LRP6-mCherry after CRISPR/Cas9 genome editing. Symbols, data; lines, fits with Equation 5.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** (a) Г(CL) as a function of DKK1-eGFP (magenta) and DKK2-eGFP (orange) ligand concentrations CL. Symbols represent data (mean ± SEM) from five axial scans of 60 s each; lines are fits with Equation 5, yielding the parameters KD = 0.08 ± 0.01 nM and β = 0.44 ± 0.02 for DKK1-eGFP and KD = 0.26 ± 0.04 nM and β = 0.43 ± 0.02 for DKK2-eGFP. (b) Corresponding binding isotherm F(CL) as a function of DKK1-eGFP and DKK2-eGFP ligand concentrations.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** (a) Receptor densities, each data point represents an individual cell, boxes mark the 25–75% range. The median is indicated by the central line, the mean as a small black square. Whiskers mark the SD. (b) Г(CL) and (c) corresponding binding isotherms F(CL) as functions of DKK1-eGFP ligand concentration CL. Symbols represent data obtained from five axial scans of 60 s each (mean ± SD); lines are fits with Equation 5.

**Table 1.**
 Parameters obtained from the analysis of axial lsFCS data of DKK1 binding to LRP6-mCherry.Table 1—source data 1.Source Data to Table 1.


<table>
  <thead>
    <tr>
      <th>Cell line</th>
      <th colspan="2">HEK293T</th>
      <th colspan="3">NCI-H1703</th>
    </tr>
    <tr>
      <th>Receptor gene insertion</th>
      <th colspan="2">Transient transfection</th>
      <th>Transient transfection</th>
      <th>Stable transfection</th>
      <th>CRISPR/Cas9 genome editing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ligand</td>
      <td>DKK1-eGFP</td>
      <td>DKK1-eGFP-SNAP</td>
      <td colspan="3">DKK1-eGFP</td>
    </tr>
    <tr>
      <td>Receptor density (µm‒2) *</td>
      <td>370 ± 150</td>
      <td>1080 ± 470</td>
      <td>140 ± 80</td>
      <td>45 ± 23</td>
      <td>18 ± 9</td>
    </tr>
    <tr>
      <td>KD (nM)</td>
      <td>0.49 ± 0.09</td>
      <td>0.46 ± 0.09</td>
      <td>0.22 ± 0.02</td>
      <td>0.08 ± 0.01</td>
      <td>0.09 ± 0.01</td>
    </tr>
    <tr>
      <td>β</td>
      <td>0.13 ± 0.01</td>
      <td>0.15 ± 0.01</td>
      <td>0.47 ± 0.01</td>
      <td>0.44 ± 0.02</td>
      <td>0.14 ± 0.01</td>
    </tr>
    <tr>
      <td>DG (µm2 s‒1) †</td>
      <td>0.44 ± 0.08</td>
      <td>0.40 ± 0.07</td>
      <td>0.45 ± 0.11</td>
      <td>0.29 ± 0.06</td>
      <td>0.33 ± 0.15</td>
    </tr>
    <tr>
      <td>DR (µm2 s‒1) †</td>
      <td>0.46 ± 0.09</td>
      <td>0.45 ± 0.11</td>
      <td>0.42 ± 0.13</td>
      <td>0.27 ± 0.05</td>
      <td>0.33 ± 0.06</td>
    </tr>
    <tr>
      <td>⟨γG⟩‡</td>
      <td>1.32 ± 0.11</td>
      <td>1.25 ± 0.24</td>
      <td>1.36 ± 0.21</td>
      <td>1.62 ± 0.25</td>
      <td>1.54 ± 0.23</td>
    </tr>
    <tr>
      <td>⟨γR⟩‡</td>
      <td>1.21 ± 0.08</td>
      <td>1.26 ± 0.13</td>
      <td>1.33 ± 0.16</td>
      <td>1.54 ± 0.25</td>
      <td>1.42 ± 0.29</td>
    </tr>
  </tbody>
</table>

_* Receptor densities are given as median ± half the range covered by the second and third quartile of the distribution. Individual data points were calculated from receptor autocorrelation amplitudes, GR(0), and the observation area (0.20 µm2).† Diffusion coefficients of receptor-bound ligands and receptors were calculated from the translational diffusion times by using D = ω02/4τ.‡ The photobleaching parameters ⟨γ⟩ are given as the median value ± half the range covered by the second and third quartile of the distribution compiled from all scans._

In addition, we have examined possible effects of the bulky fluorescent moiety (eGFP) fused to the DKK1 ligand on the strength of the receptor-ligand interaction. To this end, we have attached an additional SNAP-tag domain (19.4 kDa) to the C-terminus of eGFP, which further increases the bulk of the construct but does not change its fluorescence properties. Axial lsFCS experiments were carried out using HEK293T cells transiently overexpressing LRP6-mCherry. Binding of DKK1-eGFP and DKK1-eGFP-SNAP to the receptors yielded essentially identical results (Figure 6 and Table 1), with KD = 0.49 ± 0.09 and 0.46 ± 0.09 nM, respectively, suggesting that the fusion tag perturbs the interaction only in a very minor way.

We have further measured the binding of DKK2-eGFP to LRP6-mCherry in the plasma membrane of stably transfected NCI-H1703 cells (Figure 6—figure supplement 2 and Table 2). DKK2 has been reported to have a lower affinity toward LRP6 than DKK1 (Mao et al., 2001). Indeed, our result, KD = 0.26 ± 0.04 nM, for DKK2 indicates a significantly reduced affinity with respect to DKK1 binding to stably transfected NCI-H1703 cells (KD = 0.08 ± 0.01 nM, Table 1).

**Table 2.**
 Parameters obtained from the analysis of axial lsFCS data on NCI-1703 cells.Table 2—source data 1.Source Data to Table 2.


<table>
  <thead>
    <tr>
      <th>Receptor</th>
      <th>LRP6-mCherry</th>
      <th>LRP6-tdTomato</th>
      <th>LRP6-tdTomato</th>
      <th>xKremen2-mCherry</th>
      <th>xKremen2-mCherry, LRP6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Receptor gene insertion</td>
      <td>Stable transfection</td>
      <td>Transient transfection</td>
      <td>CRISPR/Cas9 genome editing</td>
      <td>Transient transfection</td>
      <td>Transient transfection</td>
    </tr>
    <tr>
      <td>Ligand</td>
      <td>DKK2-eGFP</td>
      <td>DKK1-eGFP</td>
      <td>DKK1-eGFP</td>
      <td>DKK1-eGFP</td>
      <td>DKK1-eGFP</td>
    </tr>
    <tr>
      <td>Receptor density (µm‒2) *</td>
      <td>32 ± 16</td>
      <td>106 ± 52</td>
      <td>21 ± 15</td>
      <td>44 ± 33</td>
      <td>41 ± 30</td>
    </tr>
    <tr>
      <td>KD (nM)</td>
      <td>0.26 ± 0.04</td>
      <td>0.22 ± 0.03</td>
      <td>0.10 ± 0.02</td>
      <td>10.3 ± 2.1</td>
      <td>0.54 ± 0.06</td>
    </tr>
    <tr>
      <td>β</td>
      <td>0.43 ± 0.02</td>
      <td>0.51 ± 0.02</td>
      <td>0.26 ± 0.01</td>
      <td>0.45 ± 0.02</td>
      <td>0.66 ± 0.03</td>
    </tr>
    <tr>
      <td>DG (µm2 s‒1) †</td>
      <td>0.27 ± 0.08</td>
      <td>0.35 ± 0.19</td>
      <td>0.27 ± 0.19</td>
      <td>0.25 ± 0.15</td>
      <td>0.32 ± 0.18</td>
    </tr>
    <tr>
      <td>DR (µm2 s‒1) †</td>
      <td>0.30 ± 0.07</td>
      <td>0.44 ± 0.34</td>
      <td>0.39 ± 0.19</td>
      <td>0.19 ± 0.08</td>
      <td>0.27 ± 0.09</td>
    </tr>
    <tr>
      <td>⟨γG⟩‡</td>
      <td>1.22 ± 0.17</td>
      <td>1.31 ± 0.15</td>
      <td>1.47 ± 0.25</td>
      <td>1.36 ± 0.22</td>
      <td>1.30 ± 0.22</td>
    </tr>
    <tr>
      <td>⟨γR⟩‡</td>
      <td>1.41 ± 0.19</td>
      <td>1.41 ± 0.16</td>
      <td>1.66 ± 0.39</td>
      <td>1.42 ± 0.29</td>
      <td>1.35 ± 0.16</td>
    </tr>
  </tbody>
</table>

_*Receptor densities were calculated from the amplitudes of the receptor autocorrelation functions, GR(0), and the observation area (0.20 µm2).† Diffusion coefficients of receptor-bound ligands and receptors were calculated from the translational diffusion times by using D = ω02/4τ.‡ The photobleaching parameters ⟨γ⟩ are given as the median of the distribution from all scans; the errors denote half the width of the second and third quartile of the distribution._

### DKK1 binding to LRP6-tdTomato

To test the robustness of our analysis, we have further studied the binding of DKK1 to a fusion protein of LRP6 with a distinctly different fluorescent protein marker, tdTomato, emitting at 581 nm. Unlike monomeric mCherry, tdTomato is a tandem dimeric marker protein and thus twice as large as mCherry. It is 5- to 6-fold brighter than mCherry and, therefore, promises a significantly higher SBR in the red channel. We transiently transfected cells with LRP6-tdTomato and we also developed a CRISPR/Cas9 edited cell line expressing endogenously tagged LRP6-tdTomato. A comparison of endogenously tagged LRP6-mCherry and LRP6-tdTomato expressed in CRISPR/Cas9 edited cells is given in Figure 3—figure supplement 3. As expected, the calculated density of LRP6-tdTomato in CRISPR/Cas9 edited NCI-H1703 cells was much lower than in transiently transfected cells, with medians at 21 ± 15 and 106 ± 52 µm–2, respectively (Figure 6—figure supplement 3a). The ligand concentration dependencies of the $Γ(C_{L})$ data (Equation 5) and the corresponding fractional occupancies, $FC_{L}$, are included as Figure 6—figure supplement 3b, c; fit parameters are compiled in Table 2. For LRP6-tdTomato fusion constructs, we obtained KD values of 0.10 ± 0.02 and 0.22 ± 0.03 nM for DKK1 binding to CRISPR/Cas9 gene edited and transiently transfected cells, respectively. These values are identical within the error to those obtained for LRP6-mCherry. We also note that, as in the experiments with the mCherry label, the β parameter is lower for CRISPR/Cas9 edited than for transiently transfected NCI-H1703 cells, in line with the expectation that the fraction of non-fluorescent receptors in the plasma membranes of CRISPR/Cas9 edited cells is larger. Taken together, our results suggest that (i) the larger size of the tdTomato label does not adversely affect DKK1 binding and (ii) we can reliably measure affinities in the subnanomolar range in live cells even with less bright fluorescent protein tags such as mCherry.

### Interactions between xKremen2-mCherry, DKK1 and LRP6

Kremen proteins (Kremen1 and 2) are type I transmembrane receptors known to modulate Wnt signaling in two distinctly different ways. They were originally identified as negative regulators of Wnt signaling (Mao et al., 2002; Ellwanger et al., 2008), amplifying DKK-mediated inhibition of Wnt signaling. Formation of a ternary complex of DKK, LRP6 and Kremen was proposed, which is rapidly endocytosed and thereby depletes the Wnt co-receptor LRP6 from the plasma membrane (Mao et al., 2002). In the absence of DKK, however, Kremen proteins have also been reported to enhance Wnt signaling by stabilizing the LRP6 receptor at the plasma membrane via Kremen-LRP6 heterodimer formation (Hassler et al., 2007). We generated (Xenopus laevis) xKremen2-mCherry and xKremen2-eGFP fusion proteins to study Kremen interactions using axial lsFCS. Activity tests confirmed that the presence of mCherry or eGFP appended to the intracellular domain of xKremen2 does not alter its ability to interact with DKK1-eGFP to inhibit Wnt signaling (Mao et al., 2002; Figure 3—figure supplement 4).

We measured the strength of the Kremen-DKK1 interaction by incubating NCI-H1703 cells transiently expressing xKremen2-mCherry with CM containing DKK1-eGFP in varying concentrations (Figure 7). A series of dual-color confocal images showed weak staining of the plasma membrane by DKK1-eGFP binding from the CM at 4 nM but bright staining at 15 nM (Figure 7—figure supplement 1a). Consistent with this observation, axial lsFCS yielded a KD value of 10.3 ± 2.1 nM (Figure 7, Figure 7—figure supplement 2, Table 2), which is considerably higher than the previously reported in vitro values of <3 nM for DKK1 binding to mKremen2 (Mao et al., 2002). However, when unlabeled LRP6 was co-expressed together with xKremen2-mCherry, there was pronounced green staining of the plasma membrane by DKK1-eGFP already at ligand concentrations below 1 nM (Figure 7—figure supplement 1b). This effect was not a result of a markedly higher xKremen2-mCherry concentration in the membrane because axial lsFCS revealed an xKremen2-mCherry density of 68 ± 10 µm–2 with and 79 ± 11 µm–2 without LRP6 co-expression, respectively (Figure 7a). Instead, the apparent affinity of DKK1-eGFP toward xKremen2-mCherry was found to increase roughly 20-fold (KD = 0.54 ± 0.06 nM) in the presence of co-expressed, unlabeled LRP6 (Figure 7b). This finding suggests that LRP6, xKremen2 and DKK1 indeed engage in a ternary complex, with DKK1 binding mediated mainly by the receptor with higher affinity, that is LRP6. DKK1 binding within the LRP6-DKK1-xKremen2 complex is not as strong as to LRP6 alone (KD = 0.22 ± 0.02 nM, see Table 1), presumably because the presence of Kremen interferes with the optimal formation of DKK1-LRP6 binding interfaces. We also note that the β parameter, which is normally 0.4–0.5 for transiently transfected NCI-H1703 cells (Tables 1 and 2), is exceptionally high (0.66) in this experiment. We would actually have expected a smaller β, considering that we co-express non-labeled LRP, which can also bind DKK1 and thereby increase the amount of molecules contributing to the intensity of the green channel. We believe that the large β value indicates a fraction of complexes that are not simple ternary complexes but larger ones containing two or more xKremen2-mCherry molecules.

![Figure 7.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig7-v2.jpg)

**Figure 7.:** (a) Densities of fluorescently labeled receptors, determined from the autocorrelation amplitudes, GR(0), with ω0 = 0.25 µm. Data on the left and right show results without and with LRP6 cotransfection. Each symbol represents data from an individual 60-s experiment. Boxes mark the 25 – 75% range. The median is shown as the central line and the mean as a black square; whiskers indicate the SD. (b) Fractional occupancies, $FC_{L}$, of receptors with DKK1-eGFP as a function of the ligand concentration in the CM. Open and closed symbols, experimental data (mean ± SEM from at least three axial scans of 60 s each) from cells with and without LRP6 co-transfection, respectively; solid lines, binding isotherms from fits with Equation 5; dotted line, DKK1-eGFP binding curve upon transfection with LRP6 only (for comparison).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Red, xKremen2-mCherry; green, DKK1-eGFP. (a) Transiently transfected cells expressing xKremen2-mCherry. (b) Cells additionally co-transfected to express unlabeled LRP6. With LRP6 cotransfection, DKK1-eGFP staining is already pronounced at 0.4 nM, whereas it is only well visible at 15 nM without, suggesting that the presence of LRP6 strongly enhances the binding affinity of DKK1 toward xKremen2. Within each data set, images are shown with the same intensity and contrast settings. Scale bar, 20 µm.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** Dependence of Г(CL) on the DKK1-eGFP ligand concentration CL. Open symbols: with LRP6 cotransfection; closed symbols: without LRP6 cotransfection; symbols represent data (mean ± SD) obtained from five axial scans of 60 s each. Lines are fits with Equation 5; fit parameters are given in Table 2.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/55286/elife-55286-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** Each symbol represents a data point from an axial lsFCS measurement on a single cell. Only data with correlation amplitudes GG > 0.02 and F’<1 have been included to remove statistical outliers. Box indicates the 25–75% range; the median is shown as the central line and the mean as a black square. Whiskers mark the SD.

The engagement of unlabeled (and thus not visible) LRP6 in the ternary complex was only indirectly inferred from the large change of the apparent binding affinity of DKK1 to xKremen2 upon LRP6 coexpression. Thus, we next aimed to directly observe a LRP6-xKremen2 interaction in the plasma membrane, as earlier suggested (Hassler et al., 2007). To this end, we performed axial lsFCS on a large number of NCI-H1703 cells stably expressing LRP6-mCherry and, in addition, xKremen2-eGFP using transient transfection. The FCS data showed almost exclusively that LRP6 was the less abundant of the two receptor species, in accord with a report by Li et al., 2010 that LRP6 expression is markedly suppressed upon co-transfection of the two receptors. We found that 25 ± 14% of LRP6 receptors co-diffused with the more abundant xKremen2 receptor, that is they were part of a dual-labeled receptor heterodimer; 15 ± 6% of the xKremen2 receptors co-diffused with LRP6 (Figure 7—figure supplement 3).

## Discussion

We have developed a fluorescence microscopy-based methodology for the precise quantification of the strength of receptor-ligand interactions on live samples and applied it to the study of receptor-ligand interactions in the Wnt signaling network. In the investigations presented here, we have measured KD values between 0.08 and 10 nM and we estimate that it will be possible to extend this range by about one more order of magnitude, making the method broadly applicable to a wide range of ligand-receptor interactions. Notably, we are not limited to cultured cells but can also study tissue samples or model organisms.

We have equipped our confocal microscope with a TAG lens that allows ultrafast axial scanning of the observation spot. Here we have exploited this capability for dual-color lsFCS experiments to measure local concentrations of ligand-free and ligand-bound receptors residing in the plasma membrane. Axial scanning offers clear advantages over lateral scanning; most importantly, it features a smaller observation area of circular shape on the plasma membrane of cells. As a consequence, the overall data acquisition time can be reduced by about five-fold with respect to lateral scanning for comparable data precision, and the unavoidable changes in cell position and morphology are less likely to compromise the measurements. For the calculation of autocorrelation and cross-correlation functions, we have implemented a data analysis pipeline that corrects for background and photobleaching effects, which is especially important when using fusion constructs with GFP-like proteins for fluorescence labeling. KD values are determined by fitting the ligand concentration dependence of the ratios of cross- and autocorrelation functions according to Equation 5.

Our studies of ligand binding to membrane-bound receptors on living cells have demonstrated that dual-color axial lsFCS in conjunction with our new data analysis is a robust tool to precisely quantify the strengths of ligand-receptor interactions. Data could be collected at receptor densities as low as ca. 20 µm‒2, using, CRISPR/Cas9-edited NCI-H1703 cells expressing endogenously tagged receptors. Wild-type (wt) cells appear to express even lower levels of LRP6 than the endogenously tagged CRISPR/Cas9 edited cells, as judged from comparative western blot analysis. The CRISPR/Cas9 edited cells express the single (heterozygous) targeted allele of LRP6 at higher levels than both LRP6 alleles in wt cells. The endogenously tagged allele of CRISPR/Cas9 edited cells is also expressed at higher levels than the corresponding untagged allele. Possibly, the increased expression of endogenously tagged LRP6 may result from removal and/or displacement of micro-RNA binding sites present in the 3’ untranslated region, which function as negative regulatory elements for LRP6 expression (Zhang et al., 2018; Yang et al., 2019). In accord with a lower expression from the wild-type LRP6 gene locus, we were unable to detect plasma membrane fluorescence on wt cells upon immersion into DKK-eGFP containing CM at saturating DKK concentrations.

In agreement with earlier in-vitro studies (Bafico et al., 2001; Mao et al., 2001; Semënov et al., 2001; Bourhis et al., 2010), we determined subnanomolar equilibrium binding coefficients of eGFP labeled DKK1 and DKK2 ligands binding to LRP6 receptors tagged with mCherry and tdTomato at the C-terminus. The KD values of DKK1-LRP6 binding were found to increase noticeably with increasing apparent receptor density, from 0.08 nM at 20–50 µm‒2 to 0.5 nM at ~1000 µm‒2. Such an affinity modulation could result from receptor-receptor interactions, which become more prevalent at higher density. One may argue, though, that statistical dispersion of LRP6 receptors in the plasma membrane would lead to an average separation between LRP6 receptors of more than 30 nm at a density of 1000 µm–2, which appears too large for direct interactions. However, local LRP6 densities can be much higher if the receptors segregate into nanodomains embedded within our observation area of 0.2 µm2. Unfortunately, direct visualization of LRP6 clustering is precluded by the diffraction-limited resolution of our confocal microscope, but there is ample evidence for such clustering from a range of studies. In canonical Wnt signaling, LRP6 not only binds Wnt in a ternary complex with Frizzled receptors but also triggers formation of multi-protein complexes, signalosomes, as part of Wnt pathway activation. Interestingly, a LRP6 variant lacking the entire ectodomain composed of four 300-residue long, concatenated modules (PE1–4), each containing a YWTD β-propeller and an epidermal growth factor (EGF)-like domain, followed by three LDLR type A modules (LA1–3) of 40 residues each, is constitutively active in the absence of Wnt ligands (Mao et al., 2001; Liu et al., 2003; Brennan et al., 2004; Chen et al., 2014; Ren et al., 2015). Moreover, for a variety of engineered ectodomain variants, the level of signaling activity was found to scale inversely with the size of the ectodomain (Chen et al., 2014). Matoba et al., 2017 argued that there is an intrinsic tendency of the LRP6 transmembrane (TM) domain to oligomerize, leading to spontaneous signaling upon LRP6 overexpression. The curved shape of the bulky ectodomain on the cell surface, which they visualized by negative stain electron microscopy, presumably keeps the TM domains apart and thus counteracts oligomerization and spontaneous signaling. This repulsive effect may be relieved by conformational rearrangements straightening the ectodomain upon formation of LRP6-Wnt-Frizzled complexes (Matoba et al., 2017). By contrast, DKK binding would stabilize the bent form of the ectodomain. Thus, in our experiments, a higher LRP6 expression level could presumably lead to denser packing of the bulky LRP6 ectodomain, giving it less freedom to adopt the curved shape favorable for DKK binding, which then may causes the reduced affinity toward DKK antagonists at higher LRP6 expression levels.

We further quantified the interaction of DKK1 with another transmembrane receptor, xKremen2, known to regulate Wnt signaling (Mao et al., 2002). With NCI-H1703 cells overexpressing xKremen2, the measured KD of ~10 nM was much greater than the one previously reported from in-vitro experiments (Mao et al., 2002). Notably, upon coexpression of unlabeled LRP6, we observed an affinity increase of roughly 20-fold, implying formation of a complex comprising DKK1, LRP6, and xKremen2, with a much higher DKK1 binding strength. The resultant KD of 0.54 ± 0.06 nM is closer to but still not equal to the one measured for DKK1-LRP6 binding alone (KD = 0.22 ± 0.02 nM). These data suggest that the complex is stabilized by DKK1-LRP6 interactions which are reduced if xKremen2 is present, possibly due to steric interference. Notably, strong, synergistic binding of DKK1 to both receptors should lead to a lower KD than for DKK1-LRP6 binding alone. Thus, the DKK1-LRP6-xKremen complex appears to be mainly stabilized by interactions between DKK1-LRP6 and Kremen-LRP6, but not significantly by the weaker DKK1-xKremen2 interaction (KD = 10.3 ± 2.1 nM). This scenario implies a mutual interaction between the two receptors, which was confirmed by axial lsFCS experiments on cells expressing both receptors labeled in different colors, showing a high degree of heterodimer formation.

In conclusion, we have introduced a biophysical method based on lsFCS with fast axial scanning. In combination with a sophisticated correlation analysis pipeline, highly precise KD values can be obtained. Our investigations show that even small changes in KD values can be measured, attesting to the robustness and reliability of the method. However, besides statistical errors, there are always systematic errors that may deteriorate the accuracy of the results. Two sources of such errors, namely (1) incomplete fluorophore maturation in the fluorescent protein tag, and (2) lack of binding competence of a fraction of ligands or receptors, and their effects on the data have been discussed in the Materials and methods section. To achieve a high accuracy, it is of utmost importance to choose a fluorescent protein tag with optimal maturation yield for the ligands. Moreover, the production of CM should be optimized so as to ensure a large fraction of ligand molecules competent of binding to their cognate receptor. Finally, we note that the accuracy hinges on the precise knowledge of the ligand concentration in the CM. This is not at a trivial issue when dealing with highly dilute solutions in the (sub-)nanomolar range. These and other errors can be minimized by careful experimentation and analysis. Consequently, we feel greatly encouraged to investigate further ligand receptor binding reactions in the Wnt signaling pathway using axial lsFCS.

## Materials and methods

### Microscope setup

Our home-built microscope (see Figure 1—figure supplement 1 for a schematic) has three picosecond pulsed lasers (L1 – L3) for fluorescence excitation, emitting at 470, 561 nm and 640 nm. They are externally triggered by 40 MHz transistor–transistor logic (TTL) signals. A delay generator introduces a mutual delay of 12.5 ns between two of the three lasers chosen for dual-channel experiments to enable pulsed interleaved excitation (Müller et al., 2005), so that the fluorescence excited by the two lasers can be detected in two separate time windows of 12.5 ns width. The laser beams are coupled into a wideband fiber coupler (WFC) by a mirror (M) and two dichroic mirrors LP1 and LP2. To minimize axial misalignment of the foci, the combined beam is split into three paths via a wavelength division multiplexer (WDM), and further combined using a mirror M and dichroic beamsplitters LP3 and LP4. In each path, the axial focus position of the beam is carefully adjusted by changing the distance between the fiber end and the coupling lens. After reflection by quad-band mirror QB, the excitation light passes through a TAG lens enabling fast axial scanning of the excitation focus, the laser scanner, scan lens (SL), and enters a Leica DMi8 microscope frame (Leica Microsystems, Wetzlar, Germany), in which the beam is collimated by a tube lens (TL) and reflected by a mirror (M) into the vertical direction. A quarter-wave plate generates circular polarization to avoid polarized excitation. The laser beam is finally focused into the sample by a 63×/1.2 NA water immersion objective. For additional, slow scanning in the axial direction, the objective can be moved by a motorized linear actuator with an accuracy of 0.5 nm (M-122, Physik Instrumente, Karlsruhe, Germany) and a piezo actuator (P-720, Physik Instrumente).

The fluorescence emitted by the sample propagates back through QB and is coupled into a multi-mode fiber serving as a pinhole of 1 AU (for 640 nm light). Subsequently, it is separated into two color channels by a 555 nm longpass dichroic mirror LP5, passed through bandpass filters BPF1 and BPF2 and are finally detected by two avalanche photodiodes APD1 and APD2. A TCPSC card (SPC-150, Becker and Hickl GmbH, Berlin, Germany) records, for each photon, its absolute arrival time and its delay time with respect to the 40-MHz laser trigger and, furthermore, the lateral (x, y) positions of the galvanometer scanner as well as the timing signal, tTAG, issued by the TAG lens control unit for z coordinate determination.

### Focus size calibration

Multi-color beads (TetraSpeck microspheres, diameter d = 0.1 µm, Thermo Fisher Scientific, Karlsruhe, Germany) were sparsely immobilized on a chambered glass plate and scanned with the focused 470 nm and 561 nm laser beams (both 5 µW). The emitted light was passed through Brightline bandpass filters (HC 525/50 for green emission, HC 600/37 for red emission, Semrock, Rochester, NY) before detection. In each color channel, ten beads were selected for focus size determination. By analyzing the intensity distributions across their centers and correcting the measured full widths at half maximum (FWHMm) values for the actual size of the beads according to FWHM = (FWHMm2 – d2)1/2, we obtained FWHM470nm = 242 ± 4 nm (mean ± standard error of the mean (SEM)) and FWHM561nm = 295 ± 9 nm (mean ± SEM). The focus parameter, ω0, which corresponds to the distance over which the intensity decays by a factor of 1/e2, was calculated by using the relation ω0 = (2 ln(2))1/2 FWHM, yielding ω0 = 207 ± 3 nm and 251 ± 8 nm for 470 nm and 561 nm laser excitation (see Figure 2—figure supplement 1).

### Dependence of the precision of axial and lateral lsFCS on the duration of the measurement

The overall data acquisition time needed to obtain a FCS curve with sufficient quality is an important parameter, especially when studying live samples which unavoidably move during the experiment. To address this issue, we have performed 14 axial and lateral line scanning FCS experiments on Atto647N-labeled GUVs, each with a duration of 400 s. From the intensity time traces, 40 individual $G_{i}(\tau)$ curves were calculated, normalized to amplitude 1 and averaged to yield a single $G¯(\tau)$. The scatter of an individual curve around the average was quantified by the standard deviation (SD),

$$
SD_{i}=\sqrt{\frac{1}{\tau}\sum\tau(G_{i}(\tau)−G¯(\tau))^{2}}.
$$

This calculation was carried out for all 40 curves, and the average and SD were calculated for this ensemble. Subsequently, the procedure was repeated with the same but artificially shortened intensity time traces to generate the data presented in Figure 2e. This graph shows that SD ≈ 0.1 can be reached with axial lsFCS in one-fifth of the time needed with lateral lsFCS.

### FCS data acquisition and analysis

Axial lsFCS data were collected on live cells for 60 s with 470 nm excitation of eGFP at 5 µW (2.8 kW/cm2) and 561 nm excitation of mCherry/tdTomato at 3 µW (1.5 kW/cm2). Cells were kept at 37°C and 5% CO2. Before data collection, the cell culture medium was replaced by 500 µl CM with DKK1-eGFP or DKK2-eGFP concentrations, CL, in the range of 0.01 nM ‒ 220 nM. To ensure that binding equilibrium was reached prior to the axial lsFCS experiment, at CL = 3.5 nM, the cells were incubated for 5 min (see Figure 3—figure supplement 1). For all other ligand concentrations, the incubation times were adjusted by the ratio 3.5 nM/CL, as expected for a bimolecular reaction. At concentrations below 1 nM, the CM was replaced by fresh medium in the middle of the incubation period to compensate for ligand depletion from the CM due to receptor binding or endocytosis.

At each CL, six cells were selected on average for axial lsFCS on both the basal and the top membranes (~50% each). With the TAG lens turned off, the focal volume was centered on the membrane under study. Then, the TAG lens was turned on (at 75% of its maximum amplitude) to scan the focus across the membrane, spanning roughly 5.3 μm in axial direction. Photons were registered by the TCSPC unit and sorted according to their macroscopic and microscopic arrival times to generate intensity time traces in the two color channels used for correlation analysis.

These data were plotted as kymographs, that is 2D plots of the intensity along the scan line (on the x-axis) line by line for the entire scan sequence and, thus, as a function of time (on the –y-axis). Data sets showing pronounced bright features near the membrane (fluorescent clusters) or strongly fluctuating membrane positions were discarded. Furthermore, kymographs were inspected for correct focusing, and if the plasma membrane was not near to the middle of the axial oscillation range, data were also discarded. After correcting the remaining intensity time traces for background and photobleaching, autocorrelation and cross-correlation curves were calculated with Equations 3 and 4, respectively, and fitted with the diffusional model correlation function, Equation 1. Those data sets for which the fit returned markedly deviant correlation times, τD, or different ones for the twocolor channels were discarded. From the amplitudes, $G_{G}0$, $G_{R}0$ and $G_{\times}0$, the function $Γ(C_{L})$ was computed (Equation 5). At least three independent $Γ(C_{L})$ values were determined and averaged for each particular ligand concentration, CL, plotted as a function of ligand concentration and fitted with Equation 5 by variation of two parameters, KD and β (see below). The entire sequence of data analysis steps including data quality management is shown diagrammatically in Figure 4—figure supplement 3.

To ensure proper functioning of the axial lsFCS apparatus and the analysis, we frequently performed control experiments with samples designed to give a sizeable (or complete) cross-correlation or none at all. Examples are shown in Figure 4—figure supplement 2.

### Determination of KD from ligand concentration-dependent dual-color axial lsFCS

To measure the equilibrium dissociation coefficient of a ligand-receptor pair, we take axial lsFCS data over a wide range of free ligand concentrations on cells expressing the receptor. In the following, we assume that all receptors on the cell surface are capable of binding their cognate ligand, and that the ligands in turn are all competent of binding to their cognate receptor. We further assume that the ligands are labeled with fluorescent proteins emitting in the green channel and have a fluorophore maturation yield, $η=C_{L}/(C_{L}+C_{l})=1$, with $C_{L},C_{l}$ denoting ligands carrying a functional (fluorescent) and non-functional (dark) marker protein, respectively. The extension to $η<1$ is straightforward and will be discussed below. By using regular solution FCS, we can precisely determine CL of the CM stock solution, from which a dilution series with a range of ligand concentrations is generated. Ligands in the medium bind to receptors on the cell membrane to form ligand-receptor complexes, which are present at concentrations (area densities) CRL (receptor fluorescent) and CrL (receptor nonfluorescent). Note that receptors may be nonfluorescent because the cells endogeneously produce (non-fluorescent) receptors, or the fluorescent moeity of the fusion protein did not mature to its functional form. Furthermore, depending on the ratio of KD and CL, there will be a smaller or larger fraction of fluorescently labeled receptors at a concentration, CR, that do not have a ligand bound.

For the analysis, it is important that fast 3D diffusion of the ligand in the medium and much slower 2D diffusion of the ligand in ligand-receptor complexes in the membrane are well separated in time. Thus, only slow 2D diffusion with characteristic times of milliseconds needs to be considered. Two autocorrelation functions, $G_{G}\tau$ and $G_{R}\tau$, and one cross-correlation function, $G_{\times}\tau$, can be calculated from our dual-color axial lsFCS data and modeled as

$$
G_{G}(\tau)=\frac{1}{A_{G}(C_{rL}+C_{RL})^{2}}⋅(C_{rL}+C_{RL})(1+\frac{4D_{RL}\tau}{\omega_{G}^{2}})^{−1},
$$



$$
G_{R}(\tau)=\frac{1}{A_{R}(C_{R}+C_{RL})^{2}}⋅(C_{R}(1+\frac{4D_{R}\tau}{\omega_{R}^{2}})^{−1} +C_{RL}(1+\frac{4D_{RL}\tau}{\omega_{R}^{2}})^{−1}),
$$



$$
G_{\times}(\tau)=\frac{1}{A_{eff}(C_{R}+C_{RL})⋅(C_{rL}+C_{RL})}⋅C_{RL}(1+\frac{4D_{RL}\tau}{\omega_{eff}^{2}})^{−1}.
$$

Here, $A_{G}=\pi\omega_{G}^{2}$ and $A_{R}=\pi\omega_{R}^{2}$ are the confocal observation areas of the green and red color channels, respectively; $A_{eff}=\pi\omega_{eff}^{2}$ is the effective area in the dual-color experiment, with $\omega_{eff}^{2}=\omega_{G}^{2}+\omega_{R}^{2}/2$. The diffusional correlation times of the different species are introduced as $\tau_{D}=\omega_{G/R}^{2}/4D$.

For KD determination, we are only interested in the concentrations of the different species and, thus, the amplitudes of the correlation functions at τ = 0. We calculate the ratios

$$
\frac{G_{\times}(0)}{G_{G}(0)}=\frac{A_{G}}{A_{eff}}⋅\frac{C_{RL}}{(C_{R}+C_{RL})},
$$



$$
\frac{G_{\times}(0)}{G_{R}(0)}=\frac{A_{R}}{A_{eff}}⋅\frac{C_{RL}}{(C_{rL}+C_{RL})},
$$

and multiply both equations to obtain

$$
\frac{G_{\times}(0)^{2}}{G_{G}(0)G_{R}(0)}=\frac{A_{G}A_{R}}{A_{eff}^{2}}⋅\frac{C_{RL}}{(C_{R}+C_{RL})}⋅\frac{C_{RL}}{(C_{rL}+C_{RL})}.
$$

In Equation 12, the observation areas appear in the form of the squared ratio of the geometric and arithmetic means, $A=(A_{G}A_{R})/A_{eff}^{2}$, which equals 0.967 for the observation areas of our dual-color FCS experiments with 470 and 561 nm laser excitation. In general, this parameter is just a few percent shy of one for realistic observation areas in a dual-color experiment. Thus, the geometric differences between the two color channels almost cancel if we ensure perfect overlap between the observation areas for the two colors. Notably, in lateral lsFCS and 3D FCS dual-color cross-correlation measurements, optimal overlap of the observation areas and volumes, respectively, is more difficult to achieve because of mutual displacements along the axial direction. This problem is completely absent in axial line-scanning FCS due to its intrinsic axial self-alignment.

We introduce the equilibrium dissociation coefficient, $K_{D}=C_{R}C_{L}/C_{RL}$, and rearrange Equation 12 to read

$$
Γ(C_{L})=\frac{G_{\times}(0)^{2}}{G_{G}(0)G_{R}(0)}(C_{L})=A\beta⋅\frac{1}{1+\frac{K_{D}}{C_{L}}}.
$$

$Γ(C_{L})$ takes the form of a binding isotherm, multiplied by a scaling factor which includes, apart from the geometric parameter A, the maturation yield of the red fluorophores marking the receptor, $\beta=C_{RL}/C_{rL}+C_{RL}$. Thus, the amplitude of $Γ(C_{L})$ for $C_{L}→∞$ yields an estimate of this value. Notably, incomplete fluorophore maturation of the receptor tag affects only the amplitude of the binding isotherm but not the KD value.

Up to this point, we have assumed that the maturation yield of the fluorescent protein marking the ligand is one. How does Equation 5 change upon generalization to $η<1$? In this case, the autocorrelation amplitude of the red channel, $G_{R}(0)$, is not only governed by ligand-free receptors but also those having a dark ligand bound. Then, $K_{D}$ in Equation 5 is not equal to $C_{R}C_{L}/C_{RL}$ but rather

$$
\frac{(C_{R}+C_{Rl})C_{L}}{C_{RL}}=K_{D}+\frac{C_{Rl}}{C_{RL}}C_{L}=K_{D}+\frac{(1−η)}{η}C_{L}.
$$

Substituting $K_{D}$ in Equation 5 by the right-hand side of Equation 13 yields

$$
Γ(C_{L})=A\betaη⋅\frac{1}{1+\frac{ηK_{D}}{C_{L}}}.
$$

Equation 14 reveals that incomplete maturation of the ligand marker affects the binding curve in two ways: $η$ becomes part of the overall scaling factor of the binding curve (y-axis) and decreases its amplitude. More importantly, in contrast to fluorophore maturation effects of the receptor tags, $η$ also affects the location of the binding step along the $C_{L}$ coordinate (x-axis); the midpoint of the binding isotherm is at $C_{L}=ηK_{D}$ and not at $K_{D}$. Alternatively, one can view this modification as a redefinition of the x-axis to represent the total ligand concentration, $C_{L}+C_{l}=C_{L}/η$. Thus, the presence of dark ligand markers affects the $K_{D}$ values. We note that maturation yields are difficult to determine, and are by no means characteristic parameters of the chosen fluorescent marker proteins. They generally vary with the conditions of the experiment including the nature of the expression system, expression temperature and yield, and details of the design of the fusion construct carrying the marker. To minimize this source of systematic error, we have chosen eGFP, a protein for which high maturation yields (80 – 100%) have been reported (Foo et al., 2012b; Komatsubara et al., 2019; Sniegowski et al., 2005; Ulbrich and Isacoff, 2007).

In addition to incomplete fluorescence marker maturation, there is another source of systematic error relevant to most methods of affinity measurement (with the exception of single molecule-based experiments, for example by Manz et al., 2017). A fraction of receptors on the plasma membrane as well as a fraction of ligands in the CM may be incompetent of binding, for example due to improper folding. Unlike the degree of fluorophore maturation, which can at least be estimated, quantification of the functional fraction is a formidable task. How does this problem affect the results of our axial lsFCS experiments? Let us start with the effect of non-binding ligands present in the CM. In this case, their concentration will be less than the one anticipated from the FCS amplitudes or from any spectroscopic method capable of concentration determination. Accordingly, we have to rescale the CL axis of our binding curves to represent only the functional ligand fraction, which leads to real KD values that are smaller than the apparent ones, that is when assuming 100% binding-competent ligands. The effect of binding-incompetent receptors being present is a little more involved and we only sketch the consequences here. We have to include an additional species, non-functional receptors, CR†, in $G_{R}\tau$ in Equation 8. If we then calculate $Γ(C_{L})$, yet another scaling factor appears in the amplitude of the binding isotherm, which represents the fraction of functional receptors, $ρ=(C_{R}+C_{RL})/(C_{R†}+C_{R}+C_{RL})$. Importantly, in analogy to the case of incomplete fluorophore maturation of the receptor tag, the presence of receptors incapable of ligand binding only modifies the amplitude of the binding curve but has no effect on KD.

Throughout this work, we have used Equation 5 for our data analysis. The parameters β and $K_{D}$ were determined by non-linear least-squares fits of $Γ(C_{L})$ to the experimental data. If the maturation yield of the ligand marker is known, one may choose Equation 14 or simply replace $K_{D}$ obtained from fitting with Equation 5 with $K_{D}/η$ to correct for incomplete maturation of the ligand tag. Likewise, if the functional fractions are known, one can take them into acount as described above.

Finally, without going into detail, we note that the combination of correlation functions through which $Γ(C_{L})$ is defined not only leads to rather simple expressions for the analysis of $K_{D}$ but also has the beneficial property that background contributions are largely cancelled even if explicit background correction of the intensity time traces is omitted (Figure 5). We refer interested readers to papers that discuss correction factors for pair correlation function amplitudes due to uncorrelated background (Weidemann et al., 2002; Foo, 2012a). From the equations presented in these papers, it can be easily verified that the correction factors indeed cancel in the calculation of $Γ(C_{L})$.

### Analysis of LRP6-xKremen2 heterodimer formation using dual-color axial lsFCS

To estimate the fraction of LRP6 molecules bound to xKremen2, we took axial lsFCS data on stably LRP6-mCherry expressing NCI-H1703 cells that were co-transfected with the xKremen2-eGFP plasmid. Importantly, background expression of endogenous (unlabeled) Kremen and LRP6 is negligible in NCI-H1703 cells. In the following analysis, we refer to xKremen2-eGFP as receptor G (emissive green form) or g (non-emissive green form) and, accordingly, to LRP6-mCherry as receptor R (emissive red form) or r (non-emissive red form). These species may be present in the plasma membrane either as monomers or as four different heterodimer species, GR, gr, gR and Gr. The amplitudes of the relevant pair correlation functions are given by

$$
G_{G}(0)=\frac{1}{A_{G}(C_{GR}+C_{G}+C_{Gr})}=\frac{1}{A_{G}(η_{R}^{−1}C_{GR}+C_{G})},
$$



$$
G_{R}(0)=\frac{1}{A_{R}(C_{GR}+C_{R}+C_{gR})}=\frac{1}{A_{R}(η_{G}^{−1}C_{GR}+C_{R})},
$$



$$
G_{\times}(0)=\frac{C_{GR}}{A_{eff}(C_{GR}+C_{R}+C_{gR})⋅(C_{GR}+C_{G}+C_{Gr})}=\frac{C_{GR}}{A_{eff}(η_{G}^{−1}C_{GR}+C_{R})⋅(η_{R}^{−1}C_{GR}+C_{G})}.
$$

Here we have introduced the maturation yields, $η_{G}=C_{G}/(C_{G}+C_{g})$ and $η_{R}=C_{R}/(C_{R}+C_{r})$, that is the fractions of eGFP and mCherry proteins, respectively, carrying a functional fluorophore. The observation area-weighted ratios of cross- and autocorrelation functions, $F_{R}^{'}$ and $F_{G}^{'}$, are given by the following expressions,

$$
F_{R}^{′}=\frac{A_{eff}}{A_{G}}⋅\frac{G_{\times}(0)}{G_{G}(0)}=\frac{C_{GR}}{η_{G}^{−1}C_{GR}+C_{R}} ⟹ F_{R}=\frac{C_{GR}}{C_{GR}+C_{R}}=\frac{1}{F_{R}^{′ −1}+(1−η_{G}^{−1})},
$$



$$
F_{G}^{′}=\frac{A_{eff}}{A_{R}}⋅\frac{G_{\times}(0)}{G_{R}(0)}=\frac{C_{GR}}{η_{R}^{−1}C_{GR}+C_{G}} ⟹ F_{G}=\frac{C_{GR}}{C_{GR}+C_{G}}=\frac{1}{F_{G}^{′ −1}+(1−η_{R}^{−1})},
$$

with $A_{eff}$/$A_{G}$ = 1.23 and $A_{eff}$/$A_{R}$ = 0.84 under our experimental conditions. $F_{R}^{'}$ and $F_{G}^{'}$ correspond to bound fractions only for 100% fluorophore maturation but, as shown above, allow one to calculate the true bound fractions, $F_{R}$ and $F_{G}$, provided that the maturation yields are known. According to Equations 18 and 19, the experimentally determined average $F_{R}^{'}=0.25$ (Figure 7—figure supplement 3) corresponds to a bound fraction of LRP6 receptors, $F_{R}=0.26$, assuming $η_{G}=0.9$ for eGFP. Lower maturation yields result in larger relative corrections. Thus, the experimentally determined average $F_{G}^{'}=0.15$ yields $F_{G}=0.18$, assuming $η_{R}=0.5$ for mCherry.

### Giant unilamellar vesicles

GUVs were prepared according to the protocol by García-Sáez et al., 2010 using a lipid mixture consisting of 50 mol% sphingomyelin (SM, Sigma-Aldrich, Darmstadt, Germany), 49.999 mol% cholesterol (Sigma-Aldrich) and 0.001 mol% 1,2-dipalmitoyl-sn-glycero-3-phosphoethanolamine (DPPE) labeled with Atto 647N (Sigma-Aldrich).

### Plasmids

pCS2+hLRP6-tdTomato was generated by replacing the mCherry open reading frame (ORF) of pCS2+hLRP6-mCherry (Dörlich et al., 2015) with the ORF of tdTomato, using the XbaI and SnaBI restriction sites. For the cell line stably expressing LRP6-mCherry, the ORF of the hLRP6-mCherry fusion was inserted between the NheI/NotI restriction sites of the pEF1a-IRES-Neo plasmid (a gift from Thomas Zwaka, Addgene plasmid # 28019) to create pEF1a-hLRP6-mCherry-IRES-Neo. pCS2+V5-xKremen2-mCherry was generated by replacing the hLRP6 ORF of pCS2+hLRP6-mCherry with the ORF of xKremen2 using NEBuilderHiFi DNA Assembly (New England Biolabs E2621S). pCS2+hDKK1-eGFP and pCS2+hDKK2-eGFP were described previously (Krupnik et al., 1999; Brott and Sokol, 2002; Dörlich et al., 2015). pCS2+hDKK1-eGFP-SNAP was generated from pCS2+hDKK1-eGFP by adding 36 bases (GGTTCAGCAGGTTCTGCAGCAGGTTCTGGAGAGTTC) coding for a 12-amino acid linker (GSAGSAAGSGEF) and the gene of the SNAP-tag domain (a kind gift from Professor Nils Johnsson, University of Ulm, Germany) using the NEBuilderHiFi DNA Assembly kit (New England Biolabs). The pCS2+hLRP6-mCherry-eGFP construct was built in an analogous fashion, using the eGFP instead of the SNAP-tag gene.

### Generation of cell lines stably expressing fluorescently tagged LRP6

NCI-H1703 cells were transfected with 2 µg pEF1a-hLRP6-mCherry-IRES-Neo in six-well plates using ScreenFectA (ScreenFect GmbH, Eggenstein, Germany) according to the manufacturer’s one-step protocol. 24 hr post-transfection, the medium was exchanged, and 48 hr post-transfection one tenth of the cells were transferred to 10 cm2 dishes and cultured in RPMI 1640 supplemented with 700 µg/ml G418 (Sigma-Aldrich). Selection was performed for 12 d. Clonal lines were obtained by limited dilutions in 96-well plates.

### Generation of CRISPR/Cas9 cell lines expressing fluorescently tagged LRP6

The human LRP6 locus was targeted within exon 23 for C-terminal endogenous tagging with a fluorescent protein (see Figure 3—figure supplement 5). Using the E-CRISP online tool (Heigwer et al., 2014), we identified a 20 bp protospacer (5’-ACGTTGGAGGCAGTCAGAGG-3’) followed on the 3’ end by a NGG PAM (protospacer adjacent motif) downstream of the LRP6 stop codon, in exon 23. DNA oligonucleotides were designed and annealed to generate the following short double-stranded DNA fragment containing the 20 bp protospacer, an additional guanine nucleotide at the 5’end that increases targeting efficiency (Cong et al., 2013) and 4 bp overhangs suitable for ligation into a BbsI restiction site (Figure 3—figure supplement 6). This short double-stranded DNA fragment was ligated into the BbsI restriction site of the pX330-U6-Chimeric_BB-CBh-hSpCas9 (D10) vector (Cong et al., 2013), generating a plasmid encoding a single guide RNA (sgRNA) harboring the LRP6 specific 20 bp protospacer under the control of a U6 RNA Polymerase III promotor.

The PCR2.1-PITX-eGFP-PGK-Puro vector (Hockemeyer et al., 2011) was used as a template to create the PCR2.1-hLRP6-mCherry-PGK-Puro and PCR2.1-hLRP6-tdTomato-PGK-Puro donor vectors. DNA sequences of ~700 bp for the left and the right homology arms (LHA, RHA) of LRP6 were PCR-amplified from genomic DNA using the primer pairs:

The homology arm PCR products were cloned into the PCR2.1 donor vector using the SBfI/NheI (LHA) or AscI/FseI (RHA) restriction sites. The PCR amplified mCherry and tdTomato ORFs were cloned into the PCR2.1 donor vector using the NheI/EcoRI restriction sites. For the LRP6-mCherry donor vector, complementary single strand oligonucleotides bearing a 12-amino acid linker (ASTLEASLERAS) were annealed and cloned into the NheI digested vector between LHA and mCherry. For the LRP6-tdTomato donor, the NheI restiction site (AS) served as a linker between LRP6 and tdTomato. In order to protect the donor vector from cleavage by the Cas9 nuclease, a silent mutation within the PAM site of the right homology arm of LRP6 was introduced using the QuickChange Lightning Site-directed Mutagenesis Kit (Agilent Technologies, Waldbronn, Germany).

To establish a cell line expressing endogenously tagged LRP6, NCI-H1703 cells cultured in 6-well plates were transfected with 1 µg donor plasmid and 1 µg CRIPSPR/Cas9 plasmid using ScreenFectA (ScreenFect GmbH) according to the manufacturer’s 1-step protocol. 24 hr post-transfection the medium was exchanged. 48 hr post-transfection, one tenth of the cells were transferred to 10 cm2 dishes and cultured in medium supplemented with 2 µg/ml puromycin (Sigma-Aldrich). After 5 days of selection, single cells were transferred to 96-well plates using limited dilutions to amplify the clonal lines. Initial screening of these cell lines for edited LRP6 using SDS-PAGE and western blot indicated a CRISPR/Cas9 targeting efficiency of 57%. Genomic DNA from promising candidate cell lines was sent for sequencing (Microsynth AG, Balgach, Switzerland). The results indicated that only heterozygous clones were obtained. siRNA gene knock-down experiments confirmed the heterozygous nature of the cells (Figure 3—figure supplement 7). For the CRISPR/Cas9 edited cells used in this work, we confirmed that the fluorescently tagged LRP6 receptors were properly localized at the cell surface (Figure 3—figure supplement 3b and Figure 3—figure supplement 8b) and underwent Wnt-dependent post-translational modification similar to wt receptors (Figure 3—figure supplement 8a). The CRISPR/Cas9 edited cells were also tested for their ability to activate and inhibit Wnt/β-catenin pathway signaling in response to Wnt and Dkk ligand stimulation, respectively (Figure 3—figure supplement 2c and Figure 3—figure supplement 8a).

### Cell culture and transient transfection

An 8-well Nunc Lab-Tek chambered cover glass (Thermo Fisher Scientific, Waltham, USA) was coated with fibronectin (Sigma-Aldrich, St. Louis, MO) to ensure efficient adhesion of the cells. To this end, each well was incubated with 200 µl fibronectin (50 µg/ml, diluted in Dulbecco’s phosphate buffered saline (DPBS, no calcium, no magnesium, Sigma Aldrich)) for at least 1 hr at room temperature. Afterwards, the solution was removed by aspiration, and the chamber was allowed to dry. Fibronectin coated chambers were either used directly or stored for a maximum of 1 ‒ 2 weeks at 4°C. Before use, the fibronectin-coated wells were washed with DPBS. Stably transfected or CRISPR/Cas9 gene-edited cells were seeded in the pretreated wells; cell experiments were performed on the next day. Wt cells were allowed to attach for at least 1 hr before transient transfection. They were investigated 23 ‒ 36 hr after transfection to ensure comparable results.

Human embryonic kidney 293T (HEK293T) cells (DSMZ ACC-635) were cultured in Dulbecco's Modified Eagle Medium (DMEM, Thermo Fisher, Waltham, MA) supplemented with 10% fetal bovine serum (FBS, Thermo Fisher) and 1% penicillin/streptomycin (P/S; Thermo Fisher). NCI-H1703 human lung carcinoma cells (ATCC CRL-5889) were cultured in RPMI 1640 medium (Thermo Fisher) supplemented with 10% FBS and 1 mM sodium pyruvate (Thermo Fisher). Both cell lines were maintained at 37°C and 5% CO2. Expi293F suspension cells (Thermo Fisher A14527) were cultured in Expi293 Expression Medium (Thermo Fisher) at 37°C and 8% CO2 with 125 rpm orbital shaking. All cell lines tested negative for mycoplasma.

HEK293T wt and NCI-H1703 wt cells were transfected with 1 ‒ 2 µg DNA per well at a 1:6 ratio of MesD:hLRP6-Fluorophore using Xfect (TaKaRa Clontech, Mountain View, CA) according to the manufacturer's protocol. Six hours after transfection, the medium was exchanged with fresh cell culture medium supplemented with 10% FBS and 1 mM sodium pyruvate. For co-expression of LRP6 and xKremen2-eGFP in NCI-H1703 cells, transfections were performed sequentially. First, cells were transfected with 1500 ng LRP6 plasmid and 5 hr later, the same cells were transfected with 400–500 ng xKremen2 plasmid. After 2.5 hr, the medium was completely exchanged and the cells were cultured overnight.

### Preparation of Conditioned Medium (CM)

HEK 293F suspension cells in Expi293 Expression Medium (30 ml, 2.5 × 106 cells/ml) were transfected with 30 µg pCS2+human-DKK1/2-eGFP plasmid using ScreenFectUP-293 + Booster (ScreenFect GmbH) according to the manufacturer's instruction. DKK1-eGFP CM was collected 96 hr post-transfection. TOPFLASH Wnt reporter assays and western blot analysis confirmed both the integrity and activity of the DKK-eGFP fusion proteins produced from suspension cell cultures (Figure 3—figure supplement 9). For experiments using NCI-H1703 cells, the harvested cell culture medium was concentrated 30-fold using Amicon 10 kDa ultra filters (Merck KGaA, Darmstadt, Germany) and reconstituted to the same volume with fresh RPMI containing 10% FBS. For experiments with HEK293T cells, the same procedure was followed using DMEM instead of RPMI medium. The CM was sterilized using a 0.22 µm filter and stored at 4°C. DKK2-eGFP CM was prepared using the same protocol but reconstituted to only half the original volume. Mouse Wnt3a CM was prepared from mouse L cells stably transfected with mouse Wnt3a (ATCC CRL-2647). Control CM was prepared from non-transfected L cells (ATCC CRL-2648). Cells were maintained at 37°C and 5% CO2.

### DKK1-eGFP concentration in the CM

The ligand concentration in the CM needs to be measured as precisely as possible because it determines the scaling of the x-axis of the binding curves. Thus, any error in this quantity will directly affect the measured KD values. In this work, we have routinely measured the ligand concentration in CM with solution FCS using PEG-coated sample chambers to minimize errors due to protein adsorption. To examine the reliability of these concentration determinations by independent means, we developed a protocol based on optical absorption and fluorescence spectrometry. A solution of purified eGFP was prepared to serve as a reference; its concentration was determined with an absorption spectrometer (Cary 100, Agilent Technologies, Santa Clara, CA). Next, the eGFP stock solution was diluted in three steps, each time roughly by a factor of ten, to a final concentration of a few ten nanomolar, similar to the ligand concentration of the CM. To measure the dilution factors as precisely as possible, emission spectra were taken with a Fluorolog-3 spectrofluorometer (HORIBA Jobin Yvon, Edison, NJ) before and after each dilution step (with identical spectrometer settings) to account for pipetting errors and protein loss due to adsorption onto the quartz cuvette surfaces. Then, emission spectra of DKK1-eGFP CM and control CM (without DKK1-eGFP) were taken. Finally, the emission spectrum of DKK1-eGFP CM was quantitatively decomposed into eGFP and background fluorescence spectra by using the spectra of purified eGFP and control CM. This procedure yielded results identical to those from solution FCS.

### siRNA transfection

siRNAs targeting the fluorescently tagged LRP6 mRNA were designed using the Dharmacon ‘siDesign’ center. They were obtained from Dharmacon (Horizon Discovery group, Cambridge, UK) and have the following sequences: mCherry, CCUACAACGUCAACAUCAAUU; tdTomato, UCAAAGAGUUCAUGCGCUUUU (MQ-003845–03, siGENOME LRP6 siRNA set of 4 and D-001210–03, siGENOME Non-Targeting siRNA #3). siRNA transfection was performed by using ScreenFectA (ScreenFect GmbH, Eggenstein, Germany) according to the manufacturer’s protocol.

### Western blot analysis

Expression of fluorescently tagged proteins was verified by SDS-PAGE/western blot analysis (see Figure 3—figure supplement 2, Figure 3—figure supplement 3, Figure 3—figure supplement 4, Figure 3—figure supplement 7, Figure 3—figure supplement 8, Figure 3—figure supplement 9). For western blot analysis of LRP6 expressed in CRISPR/Cas9 edited, stably transfected and corresponding wt cells, 60 μl control or Wnt3a CM was added to the cells cultured in 96-well plates. After overnight incubation, cells were lysed in 1% Triton lysis buffer (1% Triton X-100, 50 mM Tris-HCl (pH 7.0), 150 mM NaCl, 25 mM NaF, 5 mM Na3VO4, 0,1% NP-40, 1 mM EDTA) containing Complete protease inhibitor cocktail (Roche, Basel, Switzerland). After 15 min incubation on ice, cell lysates were centrifuged at 10,000 × g at 4°C for 10 min and supernatants were taken.

For membrane protein extraction, adherent cells from confluent 10 cm2 dishes were detached with 2 ml low-salt buffer (5 mM HEPES (pH 7.0), 1 mM MgCl2, 10 mM NaF, 5 mM Na3VO4) containing Complete protease inhibitor cocktail (Roche, Basel, Switzerland). Detached cells were transferred to a pre-cooled dounce tissue grinder and cell membranes were disrupted using 50 rapid strokes on ice. Lysates were centrifuged at 20,000 × g for 30 min at 4°C to pellet the membranes, which were dissolved in 200 µl 1% Triton lysis buffer.

For western blot analysis of DKK1/2-eGFP, 10 µl of the original, serum-free DKK2-eGFP CM and 0.33 µl of the DKK1-eGFP CM were heat-denatured in Laemmli sample buffer and separated by SDS-PAGE before transfer to a PVDF membrane using a Bio-Rad Transblot-Turbo system (Bio-Rad, Hercules, CA). Membranes were blocked at room temperature for 1 hr in 5% BSA – TBST blocking buffer (5% BSA, 137 mM NaCl, 2,7 mM KCl, 19 mM Tris base (pH 7.4), 0.1% Tween-20) and transferred to a BioLane HTI automated western blot processor for antibody incubation and washing steps. The following antibodies were used: anti-total-LRP6 ([1C10], 1:1000, Abcam, Cambridge, UK), anti-phospho-LRP6 (Sp1490, 1:1000, Cell Signaling, Frankfurt am Main, Germany), anti-mCherry (ab183628, 1:2500, Abcam), anti-GFP (Ab1828,1:2000, Abcam), anti-Vinculin (E1E9V, 1:1000, Cell Signaling), anti-Transferrin receptor (#136800, 1:10,000, Thermo Fisher) and HRP-conjugated anti-rabbit or anti-mouse secondary antibodies (Dako Denmark A/S, Glostrup, Denmark). For semi-quantitative detection of protein bands, the membranes were incubated with ECL Prime (GE-Healthcare, Freiburg, Germany) and imaged using a ChemiDoc Touch Imaging System (Bio-Rad).

### Cell surface biotinylation

To compare the levels of LRP6 localized on the plasma membrane of wt and CRISPR/Cas9 edited NCI-H1703 cells, cell surface biotinylation assays were performed. 1.2 × 106 cells were seeded in a 6-well plate and, after 24 hr, treated with control CM, DKK1-eGFP CM, or mWnt3a CM for 2 hr. After washing the cells three times with ice-cold PBS (pH 8.0), 1 ml of a freshly prepared biotin solution (EZ-Link Sulfo-NHS-SS-biotin 5 (Thermo Fisher, Cat. No.21328), 5 mg/ml stock solution in ultrapure water, diluted in PBS to a final concentration of 0.5 mg/ml) was added to each well. The 6-well plate was gently shaken for 1.5 hr on ice. Cells were washed with quenching buffer (35 mM Tris buffer, pH 8.0) to remove un-reacted biotin and washed twice with ice-cold PBS (pH 8.0). Cells were lysed in 300 µl 1% Triton lysis buffer and centrifuged at 10,000 × g at 4°C for 5 min. 30 µl of the resulting supernatant was removed for ‘input’ analysis. The remaining 250 µl of supernatant was mixed with 50 µl of a 50% NeutrAvidin agarose slurry (Pierce, Cat. No. 29200) and gently shaken overnight at 4°C. Samples were then centrifuged at 500 × g for 1 min and the supernatants collected as ‘flow through’. The pelleted beads were washed four times with TBST buffer (Tris-buffered saline with Tween20), then heated to 98°C in Laemmli buffer for 5 min before centrifugation at 10,600 × g for 5 min. Supernatants were collected as’ biotin labeled protein’ samples. All samples were processed for western blot analysis as described below.

### Luciferase reporter assays

To test the biological activity of the fluorescently tagged LRP6 fusion proteins, 5.5 × 104 cells cultured in 96-well plates were transfected with 20 ng TCF firefly luciferase (TOPFLASH) and 2 ng CMV Renilla luciferase (Korinek, 1997) using ScreenFectA according to the manufacturer’s 1-step protocol (ScreenFect GmbH). 12 hr post-transfection, 60 μl of control or Wnt3a CM was carefully added to the cells, which were then incubated for another 6 hr before harvesting cell lysates.

To test the biological activity of the DKK1/2-eGFP fusion proteins, NCI-H1703 lung cancer cells cultured in 96-well plates were transfected with TOPFLASH/Renilla reporter plasmids (20/2 ng). The next day, 80 µl medium was exchanged by either control CM or Wnt3a CM. After 6 hr, 120 µl DKK1/2-eGFP CM was added. The cells were incubated for another 12 hr before harvesting cell lysates.

To determine the biological activity of V5-xKremen2-mCherry/eGFP in HEK293T cells, cells cultivated in 96-well plates were transfected (per well) with 20/2 ng TOPFLASH/Renilla reporter plasmids, 8 ng mWnt1, 1 ng mFrizzled8, 1 ng DKK1-eGFP, and 1 ng V5-xKremen2-mCherry/eGFP. Cell lysates were harvested for luciferase reporter assay 24 hr post-transfection.

To compare the responsiveness of CRISPR/Cas9 endogenously tagged cell lines, stably transfected NCI-H1703 cell lines and wt parental cells to mWnt3a and DKK1, cells cultured in 96-well plates were transfected with TOPFLASH/Renilla reporter plasmids (20/2 ng) and, as indicated, 8 ng of mWnt3a and 25 ng of DKK1-eGFP. Cell lysates were harvested 48 hr post transfection.

For the luciferase assays, cells from 96-well plates were harvested in 35 µl passive lysis buffer (Promega, Mannheim, Germany) and processed according to the manufacturer’s protocol. TOPFLASH luciferase values were normalized to control Renilla luciferase values. All error bars shown in the TOPFLASH data (Figure 3—figure supplement 4, Figure 3—figure supplement 7, Figure 3—figure supplement 9) are standard deviations from the mean of 4 samples; experiments were performed at least three times.
