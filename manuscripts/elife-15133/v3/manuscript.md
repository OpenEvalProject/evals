# Physical determinants of vesicle mobility and supply at a central synapse

## Authors

- Jason Seth Rothman<sup>1</sup> ([ORCID: 0000-0003-3036-2291](https://orcid.org/0000-0003-3036-2291))
- Laszlo Kocsis<sup>2</sup>
- Etienne Herzog<sup>3</sup> ([ORCID: 0000-0002-0058-6959](https://orcid.org/0000-0002-0058-6959))
- Zoltan Nusser<sup>2</sup> ([ORCID: 0000-0001-7004-4111](https://orcid.org/0000-0001-7004-4111)) †
- Robin Angus Silver<sup>1</sup> ([ORCID: 0000-0002-5480-6638](https://orcid.org/0000-0002-5480-6638)) †

### Affiliations

1. Department of Neuroscience, Physiology and Pharmacology University College London London United Kingdom
2. Laboratory of Cellular Neurophysiology, Institute of Experimental Medicine Hungarian Academy of Sciences Budapest Hungary
3. Department of Molecular Neurobiology Max Planck Institute of Experimental Medicine Göttingen Germany
4. Team Synapse in Cognition, Interdisciplinary Institute for Neuroscience Université de Bordeaux, UMR 5297, F-33000 Bordeaux France

† Corresponding author

## Abstract

Encoding continuous sensory variables requires sustained synaptic signalling. At several sensory synapses, rapid vesicle supply is achieved via highly mobile vesicles and specialized ribbon structures, but how this is achieved at central synapses without ribbons is unclear. Here we examine vesicle mobility at excitatory cerebellar mossy fibre synapses which sustain transmission over a broad frequency bandwidth. Fluorescent recovery after photobleaching in slices from VGLUT1Venus knock-in mice reveal 75% of VGLUT1-containing vesicles have a high mobility, comparable to that at ribbon synapses. Experimentally constrained models establish hydrodynamic interactions and vesicle collisions are major determinants of vesicle mobility in crowded presynaptic terminals. Moreover, models incorporating 3D reconstructions of vesicle clouds near active zones (AZs) predict the measured releasable pool size and replenishment rate from the reserve pool. They also show that while vesicle reloading at AZs is not diffusion-limited at the onset of release, diffusion limits vesicle reloading during sustained high-frequency signalling.

## Introduction

At the early stages of auditory, vestibular and visual pathways, information is transmitted at high rates across specialized ribbon synapses (de Ruyter van Steveninck and Laughlin, 1996; Matthews and Fuchs, 2010). At these synapses, vesicular release is sustained by a large number of highly mobile vesicles (Holt et al., 2004; Rea et al., 2004) and a ribbon-like scaffold that is thought to rapidly capture and deliver vesicles to the release sites (Griesinger et al., 2005; Khimich et al., 2005; LoGiudice et al., 2008; Graydon et al., 2014). Downstream of ribbon synapses, sensory information is transmitted by conventional synapses formed by afferent and sensory nuclei neurons that sustain rate-coded signalling over a broad frequency bandwidth (Taschenberger and von Gersdorff, 2000; Saviane and Silver, 2006; Bagnall et al., 2008; Hallermann et al., 2010). Some of these conventional synapses, such as those formed by cerebellar mossy fibre terminals (MFTs) or vestibular nerve fibres, have a readily releasable pool (RRP) of only 1–2 vesicles per AZ, which are docked and primed and ready for release. A much larger releasable pool (RP) containing 200–300 vesicles resides nearby and these vesicles can be supplied to the AZ, docked and primed at a combined rate of 40–80 s−1 (with all three steps referred together as reloading) to refill the RRP (Saviane and Silver, 2006; Hallermann et al., 2010; McElvain et al., 2015). Even when the large RP is depleted by sustained high-frequency stimulation, release rates of 7–8 s−1 can be sustained by replenishment from a large vesicle reserve pool (R) at these synapses (Saviane and Silver, 2006; McElvain et al., 2015). Because these conventional synapses lack ribbons, and central synapses are thought to contain mostly immobile vesicles (Jordan et al., 2005; Lemke and Klingauf, 2005; Shtrahman et al., 2005; Lee et al., 2012), it is unclear how vesicles are supplied to AZs during sustained high-frequency signalling.

Vesicles are actively transported within axons at ~1–5 µm/s (Brown, 2003), but passive diffusion is thought to dominate vesicle translocation within the presynaptic terminals of both ribbon (Holt et al., 2004; Rea et al., 2004; LoGiudice et al., 2008; Graydon et al., 2014) and conventional central synapses (Tokuoka and Goda, 2006). Presynaptic terminals are packed with macromolecules and cytoskeletal elements, as well as vesicles and mitochondria (Harris and Weinberg, 2012; Wilhelm et al., 2014). The rate of vesicle diffusion will therefore be determined not only by the cytoplasmic viscosity, but by the cytoskeletal matrix (Luby-Phelps et al., 1987) and organelles including vesicles (Gaffield et al., 2006), as well as binding to these elements (Shtrahman et al., 2005) via fine protein connectors (Siksou et al., 2007; Fernández-Busnadiego et al., 2013). These factors, together with the tortuous paths required to diffuse around large organelles, are thought to explain why vesicle mobility in crowded presynaptic terminals is substantially lower than that of vesicle-sized beads in cytoplasm (Luby-Phelps et al., 1987; Gaffield et al., 2006). Hydrodynamic interactions between vesicles are another potentially important determinant of their mobility. Hydrodynamic forces arise from the displacement of fluid as nanoscale objects move through solution. Studies of protein diffusion in red blood cells and bacteria (Doster and Longeville, 2007; Ando and Skolnick, 2010) show hydrodynamic interactions reduce the mobility of macromolecules. Moreover, studies of colloidal suspensions of vesicle-sized beads demonstrate hydrodynamic interactions are particularly strong in crowded environments, when the volume fraction of the diffusing objects is high (van Blaaderen et al., 1992; Tokuyama and Oppenheim, 1994; Segrè et al., 1995). However, nothing is known about how hydrodynamic interactions affect vesicle mobility within axon terminals. Quantifying the physical determinants of vesicle mobility within crowded presynaptic terminals could therefore provide new insights into vesicle supply at central synapses.

We have investigated the physical determinants of vesicle mobility in cerebellar MFTs, large central glutamatergic synapses that sustain broad-bandwidth rate-coded sensory signalling (Saviane and Silver, 2006; Hallermann et al., 2010). To do this, we combined fluorescent recovery after photobleaching (FRAP) in Venus-tagged VGLUT1 (VGLUT1Venus) knock-in mice (Herzog et al., 2011) with serial-section electron microscopy (EM), electron tomography and 3D reaction-diffusion modelling of the presynaptic environment. Our results establish that most vesicles within MFTs are highly mobile and hydrodynamic interactions and vesicle collisions are major determinants of their mobility. Moreover, simulations of vesicle diffusion at 14 reconstructed AZs indicate that, while vesicle diffusion does not limit vesicle reloading at the onset of sustained high-frequency signalling, it does limit vesicle reloading at late times due to significant vesicle depletion near the AZ. The simulations also predict both the size of the functional RP and the vesicle replenishment rate from the reserve pool.

## Results

### FRAP of VGLUT1Venus labelled vesicles in cerebellar MFTs

We investigated vesicle mobility within cerebellar MFTs using FRAP (Figure 1) at near-physiological temperature (35°C) in acute slices obtained from young-adult (P22-33) VGLUT1Venus knock-in mice (Herzog et al., 2011). In the cerebellar input layer, VGLUT1 is expressed in MFTs arising from several pre-cerebellar nuclei (Gebre et al., 2012; Hisano et al., 2002). Whole-cell patch-clamp recordings from postsynaptic granule cells (GCs) confirmed EPSC amplitudes, kinetics and short-term plasticity of cerebellar MFT-GC synapses in VGLUT1Venus mice were similar compared to wild-type mice (Figure 1—figure supplement 1). Moreover, previous work showed the expression and subcellular distribution of VGLUT1Venus is indistinguishable from that of native VGLUT1 in wild-type mice (Herzog et al., 2011). The advantages of studying vesicle mobility using VGLUT1Venus knock-in mice rather than lipophilic dyes such as FM1-43 include the ability to use acute slices rather than primary cultures, and the capacity to monitor fluorescence of both mobile and immobile vesicles.

![Figure 1.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig1-v3.jpg)

**Figure 1.:** (A) A VGLUT1Venus-labelled MFT near the surface of a cerebellar slice. Blue ellipse denotes xz dimensions of iPSF. Inset, lower magnification. Scale bars: 5 µm. (B) Fluorescence recovery after photobleaching (FRAP) measurements from 15 locations within a single MFT (bottom, gray lines; note logarithmic timescale) using 2-ms low-intensity laser probe pulses before and after a single 0.5-ms high-intensity laser bleaching pulse (top; note logarithmic y-scale). Fluorescence measured without the bleaching pulse in the same MFT from 14 random locations (red lines; interleaved with recordings with bleaching). Data were normalized to the average fluorescence of the first 3 probe pulses (f0) before bleaching. Filled black and red circles are means ± SEM. Black and gray horizontal lines denote measurement windows for f1s and f5s reported in C. (C) Average fluorescence recovery for 62 MFTs at 1 s (black; f1s, average 0.4–1.7 s) and 5 s (gray; f5s, average 2.7–6.9 s) after bleaching, normalized between f0 and fb, where fb is the fluorescence just after bleaching (average 0.02–0.08 s). (D) Same as B but gray lines are averaged FRAP curves from 62 MFTs (3–24 recordings per MFT) and black circles are the weighted population average, computed by Equation (1).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** (A) EPSCs recorded from a GC (average of 8 recordings) in response to stimulation of a single MFT at 40, 100 and 300 Hz (100, 100 and 25 stimuli, respectively) in a VGLUT1Venus mouse. Phasic refers to the fast rising EPSC peak and is measured relative to the tonic baseline current (see 300 Hz, red lines), and is related to the direct vesicle release of glutamate at the recorded MFT-GC connection. Tonic refers to the slow component of the EPSC, which is mediated by glutamate spillover from neighbouring MFT-GC connections (DiGregorio et al., 2002). (B) Average phasic EPSC amplitude (blue) of single MFT-GC connections (gray; n = 5) for 40, 100 and 300 Hz MFT stimulation, as shown in A. EPSC peak values were normalized to that of first EPSC. (C) Average steady-state EPSC amplitude of phasic (blue) and tonic (green) components for data in B. There were no statistical differences between VGLUT1Venus mice (v; n = 5) and WT mice (n = 13): p=0.6 and 0.3 at 100 Hz, p=0.4 and 0.2 at 300 Hz for phasic and tonic components respectively. Data for WT mice at 40 Hz is not available (NA). (D) Average basal EPSC recorded from a GC in response to stimulation of a single MFT (average of 5 EPSCs separated by more than 1 s). Red line is a double-exponential fit to the decay component (11 ms window starting 0.1 ms after the peak). (E) Average basal peak EPSC amplitude and 20–80% rise time (top graphs) from 29 GCs (capacitance = 2.8 ± 0.2 pF, series resistance = 27.9 ± 1.7 MΩ; 36°C; n = 12 VGLUT1Venus mice). The relative percent amplitude of the fast decay component (a1), the time constant of the fast and slow decay components (τ1 and τ2) and the weighted decay (τw = [a1τ1 + a2τ2]/[a1 + a2]) for double-exponential fits to EPSCs as shown in D (bottom graphs). There were no statistical differences between VGLUT1Venus mice (v; n = 29) and WT mice (n = 14) for any of the measures: p=0.6, 0.6, 0.3, 0.5 (unequal variance), 0.6 and 0.3, respectively. These analyses show that MFT-GC synapses in VGLUT1Venus knock-in mice have a normal glutamatergic synaptic physiology. EPSCs were recorded via an Axopatch 200B amplifier (10 kHz filter) and InstruTech ITC-18 board (40 kHz sampling) at −76.3 mV (corrected for +6.3 mV liquid junction potential) using fire-polished borosilicate micropipettes containing (in mM) 110 KmeSO3, 4 NaCl, 1.78 CaCl2, 0.3 Na-GTP, 4 Mg-ATP, 40 HEPES and 5 EGTA (pH 7.3). The ACSF contained 10 µM AP5, 20 µM 7-chlorokynurenic acid, 10 µM SR 95531 and 0.3 µM strychnine. Stimulus artefacts were removed as previously described (Saviane and Silver, 2006). Data for WT mice is from Hallermann et al. (2010) with permission.

MFTs expressing VGLUT1Venus were visualized with conventional fluorescence microscopy (Figure 1A). To assay vesicle mobility, we positioned a diffraction-limited laser focal spot within a MFT and recorded fluorescence using the confocal spot detection method. The intensity of a brief bleaching pulse was set to produce a modest reduction in fluorescence (~35%) to ensure the bleached volume did not extend significantly beyond the core of the illumination point-spread function of our microscope (iPSF; FWHM xy = 0.30 µm, z = 1.32 µm; e−2 volume = 0.31 µm3). Fluorescence was monitored before and after the bleaching pulse using brief low-intensity probe pulses that produced little cumulative bleaching (Figure 1B, red circles). Since the iPSF was considerably smaller than the MFTs (Figure 1A, blue spot), which are typically 7 × 10 µm, we made multiple FRAP recordings from several locations within the same MFT (Figure 1B). While the individual FRAP measurements were variable, fluorescence almost always exhibited a strong recovery within 10 s (grey lines) indicating unbleached and bleached vesicles were free to move in and out of the confocal volume. The mean fluorescence recovery was determined for each MFT by averaging the individual FRAP measurements (black circles). To determine whether fluorescence recovery varied between MFTs, we calculated the fluorescence at two times, 1 s (f1s) and 5 s (f5s), during the recovery. Distributions of f1s and f5s across 62 MFTs were unimodal with mean 35 ± 2 and 63 ± 2%, respectively (Figure 1C). We therefore calculated a population mean FRAP curve by performing a weighted mean across all 62 MFTs (Figure 1D). The time of half recovery (t1/2) of the average FRAP curve was 0.8 s and 77% of the bleached fluorescence recovered within 10 s. These results indicate the majority of vesicles within MFTs are highly mobile.

### Modulation of vesicle mobility

To test whether our FRAP measurements reflected the movement of vesicles within MFTs, we performed several manipulations known to slow or speed vesicle mobility. Reducing the temperature from 35° to 21°C slowed the fluorescence recovery (Figure 2A; f1s = 35 ± 2 vs. 25 ± 3%, respectively, p<0.01; n = 62 vs. 36 MFTs). Moreover, the Q10 of the t1/2 was 1.5, which is closer to that expected for passive diffusion (Q10 ~ 1.3) than for active transport in axons (Q10 ~ 3; Forman et al., 1977). Disruption of the actin cytoskeleton with 10 μM cytochalasin-D and 10 μM latrunculin-B (n = 60 MFTs) sped the fluorescence recovery compared to control conditions (f1s = 45 ± 2 vs. 35 ± 2%, respectively, p<0.001). In contrast, 5 μM jasplakinolide (n = 44 MFTs), a peptide that stabilizes actin filaments in vitro (Bubb et al., 2000), slowed fluorescence recovery compared to control conditions (f1s = 27 ± 2 vs. 35 ± 2%, p<0.01). These results suggest actin filaments within MFTs (Hirokawa and Yorifuji, 1989) have a modest effect on vesicle mobility.

![Figure 2.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig2-v3.jpg)

**Figure 2.:** (A) Weighted average FRAP curve for control conditions (black circles; 35°C; 62 MFTs, 619 locations, 6 mice; from Figure 1D), 21°C (green circles; 36 MFTs, 414 locations, 2 mice), 10 µM cytochalasin-D and 10 µM latrunculin-B (blue circles; 60 MFTs, 458 locations, 3 mice) and 5 µM jasplakinolide (yellow circles; 44 MFTs, 492 locations, 2 mice). Lines show double-exponential fits. Diamonds indicate t1/2. Data were normalized between f0 and fb, where fb was estimated from the fits at t = 0. (B) Same as A but for 2 µM okadaic acid (purple circles; 42 MFTs, 388 locations, 2 mice), 50 µM roscovitine (red circles; 45 MFTs, 374 locations, 3 mice) and fixed slices (brown circles; 17 MFTs, 168 locations, 1 mouse). (C) Fit of the analytical solution of Axelrod et al. (Ax; Axelrod et al., 1976) for passive diffusion (Dlong = 0.025 ± 0.003 µm2/s; red line) and directed flow (Vo = 0.344 ± 0.012 µm/s; yellow line) to normalized drift-corrected control FRAP data (open black circles; Figure 2—figure supplement 1D). Blue line shows the best-match finite-difference (FD) simulation using iPSF and cPSF of our microscope, a 0.5 ms bleaching pulse, 2 ms probe pulses and Dlong = 0.028 µm2/s. (D) Dlong for MFTs (black), goldfish retina bipolar cells (orange; Holt et al., 2004), lizard retina cone cells (yellow; Rea et al., 2004) and mouse NMJ (brown; Gaffield and Betz, 2007). Dlong for rat hippocampal boutons at room temperature computed from fluorescence correlation spectroscopy (FCS) assuming a pure diffusion (pink circle), stick and diffuse model (diamond), a caged diffusion model (filled triangle; Yeung et al., 2007), a caged diffusion model using different FCS data (square, Jordan et al., 2005), and for single-vesicle tracking measurements (open triangle, Lee et al., 2012). Mobile fractions are given in parentheses if known (MFT value is from Figure 4)

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** (A) Absolute rates of tissue drift in x, y and z directions (n = 29, 29 and 32, respectively; 35°C). Drift rates were measured by fluorescence CCD imaging of small spherical objects for 2–10 min. While x and y drift directions were random between locations, drift in z was consistently positive (i.e. upward). (B) Estimating the error due to drift using Monte Carlo FRAP simulations computed for conditions where (1) all vesicles and mitochondria were immobile (yellow) and (2) all vesicles and mitochondria moved in the same direction with average drift rates in A (brown). The difference between the two FRAP curves gave the error due to drift (green). The experimental FRAP data from fixed tissue (brown circles; Figure 2B) had similar behaviour to the simulation with added drift, but with slightly larger fluorescence recovery. (C) Time dependence of predicted error induced by tissue drift (green). Black dashed line shows fit (slope = 1.01% F/s, Pearson’s r = 1.00) to the error due to drift in B, plotted with normal x-axis. (D) The control experimental FRAP curve at 35°C (Figure 2A) before and after correction for the error due to drift computed in C (closed and open circles, respectively). Solid and dashed black lines are normalized fits (Table 1).

Application of okadaic acid (OA; n = 42 MFTs), a nonspecific phosphatase inhibitor, dramatically sped the fluorescence recovery (Figure 2B; f1s = 64 ± 5 vs. 35 ± 2%, p<0.001, unequal-variance t-test), consistent with other studies (see Table 1, legend; Jordan et al., 2005; Shtrahman et al., 2005; Gaffield et al., 2006). Moreover, OA decreased the immobile fraction from 25% to 10–15%, indicating the immobile fraction can be attributed to immobile vesicles rather than large immobile organelles.

**Table 1.**
 Estimates of Dlong under various experimental conditions.Table 1—source data 1.Fits of Axelrod equation to FRAP curves.


<table>
  <thead>
    <tr>
      <th>Solution</th>
      <th>°C</th>
      <th>t1/2 (s)</th>
      <th>Dlong (µm2/s)</th>
      <th>% Recovered</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>STRD (-drift)</td>
      <td>35</td>
      <td>0.58 ± 0.08</td>
      <td>0.025 ± 0.003</td>
      <td>67</td>
    </tr>
    <tr>
      <td>STRD</td>
      <td>35</td>
      <td>0.81 ± 0.10</td>
      <td>0.018 ± 0.005</td>
      <td>77</td>
    </tr>
    <tr>
      <td>STRD</td>
      <td>21</td>
      <td>1.39 ± 0.24</td>
      <td>0.010 ± 0.002</td>
      <td>73</td>
    </tr>
    <tr>
      <td>CD + LB (10 µM)</td>
      <td>35</td>
      <td>0.46 ± 0.05</td>
      <td>0.032 ± 0.003</td>
      <td>80</td>
    </tr>
    <tr>
      <td>Jaspla (2 µM)</td>
      <td>35</td>
      <td>0.96 ± 0.13</td>
      <td>0.015 ± 0.002</td>
      <td>76</td>
    </tr>
    <tr>
      <td>Jaspla (5 µM)</td>
      <td>35</td>
      <td>1.41 ± 0.15</td>
      <td>0.010 ± 0.001</td>
      <td>84</td>
    </tr>
    <tr>
      <td>OA (2 µM)</td>
      <td>35</td>
      <td>0.12 ± 0.02</td>
      <td>0.120 ± 0.018</td>
      <td>85</td>
    </tr>
    <tr>
      <td>Rosco (50 µM)</td>
      <td>35</td>
      <td>0.72 ± 0.11</td>
      <td>0.020 ± 0.003</td>
      <td>77</td>
    </tr>
  </tbody>
</table>

_STRD: Standard ACSF. -drift: data corrected for tissue drift (Figure 2—figure supplement 1); all other measurements are not drift corrected. CD + LB: 10 µM cytochalasin-D plus 10 µM latrunculin-B. Jaspla: jasplakinolide. OA: okadaic acid. Rosco: roscovitine. Values for Dlong and t1/2 (± STDV) were computed by fitting experimental FRAP curves (Figure 2A,B) to Equation (2).The effect of OA on vesicle mobility in the MFT is in close agreement with that reported by Shtrahman et al. (2005) who report Dlong = 0.10 µm2/s for hippocampal boutons in OA. While our results do show a reduction in the immobile vesicle fraction, this reduction is not enough to account for the large increase in Dlong. Instead, the increase in Dlong is more likely due to a reduction in protein interactions between the vesicles and cytoskeleton, as suggested by Shtrahman et al., in which case the effects of OA will be reflected in a change in Dcyto. Using data from Figure 5, we estimate Dcyto = 0.515 µm2/s in OA, a four-fold increase from control conditions (0.127 µm2/s)._

To examine the potential role of synapsin in MFTs (Hirokawa and Yorifuji, 1989) we applied the Cdk5 inhibitor roscovitine (n = 45 MFTs), which has been shown to increase vesicle mobility in hippocampal synapses from wild-type but not synapsin-knockout mice (Orenbuch et al., 2012). We found 50 µM roscovitine had no detectable effect on the rate of fluorescence recovery (Figure 2B; f1s = 38 ± 3 vs. 35 ± 2%, p=0.3) suggesting that, as for ribbon synapses (Mandell et al., 1990), there is little synapsin-based vesicle clustering at the centre of MFTs.

Finally, we repeated our FRAP experiments using paraformaldehyde-fixed slices (n = 17 MFTs), where subcellular components, including vesicles, were immobilized by cross-linking, and found fluorescence recovery was nearly absent (Figure 2B). However, there was a small but consistent increase in fluorescence after 2 s due to slow tissue drift (Figure 2—figure supplement 1A–C). A simple linear correction for the drift allowed a more accurate estimate of the control FRAP curve (Figure 2—figure supplement 1D). Together, these results confirm our FRAP measurements reflect the diffusion of vesicles within MFTs, suggest vesicle mobility is reduced by the presence of a network of actin filaments in the cytoplasm, and indicate synapsin has little impact on vesicle mobility within the interior of MFTs.

### The long-time self-diffusion coefficient of vesicles in MFTs

Vesicle mobility is often quantified by calculating the ‘effective’ diffusion coefficient, also known as the long-time self-diffusion coefficient (Dlong), which reflects the mobility of a diffusant on long time scales (van Blaaderen et al., 1992). We quantified Dlong of vesicles in MFTs by fitting our average control FRAP curve to an analytical solution of the diffusion equation (Axelrod et al., 1976). This gave Dlong = 0.018 ± 0.005 µm2/s for the raw control FRAP curve and 0.025 ± 0.003 µm2/s after correcting for tissue drift (Figure 2C, red line; Figure 2—figure supplement 1D; Table 1). In contrast to the diffusion model, which matched our data closely, the fit of a model of directed flow (Axelrod et al., 1976) was poor (Figure 2C, yellow line). Moreover, the fit of the weighted sum of the diffusion and flow models converged on diffusion (98%), suggesting diffusion underlies vesicle mobility in MFTs. Because some of the assumptions underlying the analytical diffusion model only approximated our experimental conditions, we also used 3D finite-difference reaction-diffusion simulations that explicitly modelled these conditions (Materials and methods). The FRAP simulation that best matched the drift-corrected data had a Dlong similar to that obtained with the analytical solution (p=0.84, F-test; Figure 2C, blue line). A comparison of our best estimate for Dlong in MFTs (0.025 µm2/s) with that estimated at other synapses (Figure 2D) indicates vesicle mobility is higher in MFTs than at other conventional central synapses and the neuromuscular junction (NMJ), but comparable to that measured at ribbon synapses.

### Quantification of organelle crowding within MFTs

Densely packed organelles within presynaptic terminals are expected to lead to crowding effects (Wilhelm et al., 2014) that could affect vesicle mobility (Gaffield et al., 2006). To quantify vesicle and mitochondrial densities within the central region of MFTs, where our FRAP measurements were predominantly made, we performed serial-section EM (Figure 3A). Quantitative analysis of 3D volumes (0.2–0.4 µm3, n = 3) revealed a vesicle density of 3930 ± 262 per µm3 (or 118 ± 8 per µm2 in 2D) in regions not occupied by mitochondria, consistent with previous measurements from MFTs (Palay and Chan-Palay, 1974). To convert this density into a volume fraction, we estimated the mean volume occupied by a vesicle by performing high-resolution 3D electron tomography on MFTs. Vesicle diameters exhibited an approximately normal distribution with a mean of 41.1 ± 0.2 nm (256 vesicles around 3 AZs; Figure 3—figure supplement 1), again consistent with previous measurements (Palay and Chan-Palay, 1974). Taking into account vesicle membrane proteins (Takamori et al., 2006), and the cubic relationship between vesicle radius and volume, indicates the mean volume occupied by a vesicle is equivalent to a sphere with 44 nm diameter. Using this diameter, we computed a vesicle volume fraction of 0.17 ± 0.01 of the non-mitochondrial volume (Figure 3B). The average volume fraction occupied by mitochondria was 0.28 ± 0.04. Hence, this analysis shows the central region of the MFT is a highly crowded environment with 40% of the volume occupied by vesicles and mitochondria.

![Figure 3.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig3-v3.jpg)

**Figure 3.:** (A) Electron micrograph of a cerebellar MFT from adult mouse showing vesicles and mitochondria (m). Scale bar: 0.5 µm. (B) Mean density of vesicles and mitochondria (black lines) computed from electron micrographs from 3 MFTs (gray circles), where the vesicle density is computed for the non-mitochondrial volume. Vesicle volume fraction was computed assuming a diameter of 44 nm in fixed tissue (Figure 3—figure supplement 1E). (C) Left: xz cross section (3 × 3 µm) through the 3D Monte Carlo model of the MFT simulating live tissue conditions, showing randomly placed 49 nm vesicles (0.17 volume fraction) that are mobile (green) or immobile (light gray, 25%), and clusters of mitochondria (dark gray, 0.28 volume fraction). Differences in vesicle diameters reflect their different cross sections in a single plane. Blue shading denotes iPSF. Right: xy (top, 3 × 3 µm) and xz (bottom: 3 × 7 µm) cross sections of iPSF and cPSF (Figure 3—figure supplement 2). Scale bars: 0.5 µm. (D) FRAP simulations for model in C with (black) and without (red) the bleaching pulse, showing individual trials (lines) and averages (filled circles). Top: bleaching rate (k) of Equation (4) used for probe and bleaching pulses.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** (A,B) Low (A) and high (B) magnification EM images of the cerebellar GC layer showing a VGLUT1Venus-immunopositive MFT. The higher magnification in B shows asymmetrical synapses (arrowheads) made by the MFT with GC dendrites (d). The MFT contains a cluster of mitochondria (m) in the middle and high density of synaptic vesicles. Scale bars: 400 nm (A) and 100 nm (B). (C,D) EM tomographic subvolumes (0.6 nm thick, 6 nm apart) of a MFT making an asymmetrical synapse with a GC dendrite. Arrows denote a docked synaptic vesicle. Such segmentation views were used to find the largest diameter of each vesicle. Scale bar: 100 nm. (E) Distribution of synaptic vesicle diameters (n = 256; 1 nm bins) has a mean of 41.1 ± 0.2 nm (calculated from 3 tomographic subvolumes). Taking into account the proteins that extend ~1.2 nm from the vesicle membrane (Takamori et al., 2006), and the cubic relationship between vesicle radius and volume, the mean volume occupied by a vesicle is equivalent to a sphere with 44 nm diameter.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** (A) The emission point spread function (ePSF) measured from fluorescence emitted from an imaged bead as previously described (DiGregorio et al., 2007). Left: xz plane (y = 0; 4.0 × 9.6 µm) of a 3D wide-field ePSF created from axial images (xy plane; 1 pixel = 0.05 µm) of a 110 nm fluorescent bead (Molecular Probes yellow-green FluoSpheres: 505 nm excitation, 515 nm emission) taken in multiple planes in 0.4 µm steps (dz). The resolution in the axial plane was increased by a factor of 8 (i.e. dz = 0.05 µm) by cubic spline interpolation. Vertical symmetry along x-axis was created by averaging. Values were normalized between 0 and 1, displayed with a colour scale from blue to yellow. Middle: 2D fit of ePSF to a diffraction integral representation of a high-NA objective (Sheppard and Torok, 1997) that includes a sin2θ series function to account for spherical aberrations (DiGregorio et al., 2007). Right: difference between ePSF and the 2D fit displayed with a colour scale from green (−0.14) to red (+0.14). (B) 1D profiles of ePSF and the fit in A along x-axis (left; y = 0, z = 0) and z-axis (right; x = 0, z = 0). (C) Left: 1D profile of the average confocal PSF (cPSF) in the x-axis (black line; FWHMxy = 255 nm) and range (gray; FWHMxy = 218–336 nm) computed from fluorescence measured from 110 nm beads as a focused laser spot (488 nm) was stepped across their lateral dimensions. Plots of average fluorescence versus spot location were fit with a Gaussian function and the resulting Gaussian widths were corrected for bead size using deconvolution (Chaigneau et al., 2011): FWHMactual = [(FWHMmeasured)2 – (FWHMbead)2]1/2. Red line is derived from a theoretical cPSF (Wilson and Carlini, 1987). Green dashed line is a Gaussian fit to the theoretical cPSF (FWHMxy = 238 nm). Right: 1D profile of the average cPSF in the z-axis (black line; FWHMz = 916 nm, range 780–1047 nm), with theoretical cPSF (red line) and its Gaussian fit (green dashed line; FWHMz = 975 nm).

### Effects of organelle crowding on vesicle mobility

To investigate the impact of organelle crowding on vesicle mobility in MFTs, we modelled vesicle diffusion in 3D using a hard-sphere Monte Carlo algorithm (Cichocki and Hinsen, 1990) that explicitly simulated the movement of individual vesicles and their collisions (Figure 3C). In these simulations, vesicle movement on each time step was determined by the short-time vesicle diffusion coefficient (Dshort) which defines the rate of diffusion before collisions occur. Vesicles were not allowed to overlap with themselves or mitochondria. Since simulations mimicked conditions of live tissue, we corrected our measured vesicle diameter for the 11% tissue shrinkage in fixed tissue (Korogod et al., 2015) giving an equivalent diameter of 49 nm. The spatial extent of the bleaching reaction was set by the iPSF, and the average fluorescence during the probe pulses was computed by spatially weighting the fluorescence according to the measured confocal PSF (cPSF) of our microscope (Figure 3C, right; Figure 3—figure supplement 2). Approximately 300 vesicles were located within the cPSF (Figure 3C, left). When the timing and intensity of the bleaching reaction were set to match the bleaching and probe pulses used in our FRAP experiments, FRAP curves from the Monte Carlo simulations (Figure 3D) exhibited remarkably similar behaviour to our experimental FRAP curves (Figure 1B).

Only two parameters were varied in these experimentally constrained simulations: Dshort and the fraction of immobile vesicles. To find the values of these two parameters that produced a FRAP curve that best matched our experimental FRAP curve, we used a parameter search and chi-square (χ2) criterion (Figure 4A,B). The log of the χ2 calculated from the simulated and experimental FRAP curves had a minimum at Dshort = 0.060 µm2/s and a 25% immobile fraction (68.3% confidence intervals 0.055–0.070 µm2/s and 24–25%, respectively). To better understand how vesicle collisions reduce vesicle mobility, we examined how vesicle diffusion, computed from the mean square displacement (MSD) of the mobile vesicles, changed as a function of time (D(t) = MSD/6t; Figure 4C). At short times, before any vesicle collisions, D(t) ≈ Dshort (0.060 µm2/s). At longer times, however, as vesicles collided with themselves and mitochondria, D(t) fell to a steady-state value of 0.025 µm2/s. Hence, over the 10 s period of our FRAP experiment, D(t) reached a similar Dlong estimated from our analytical and finite-difference approaches (Figure 2C). Indeed, comparison of the FRAP curve computed from our best-match Monte Carlo simulation with that computed from our best-match finite-difference simulation showed a close match (Figure 4D). These results indicate steric interactions introduce a pronounced time dependence to vesicle diffusion and over long timescales vesicle collisions reduce vesicle mobility by a factor of 2.4 (i.e. Dlong/Dshort = 0.42).

![Figure 4.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig4-v3.jpg)

**Figure 4.:** (A) Parameter search for the best match between the average drift-corrected control FRAP data (Figure 2C) and Monte Carlo (MC) simulations (Figure 3C,D) across a range of Dshort and % immobile vesicles, expressed as log($χ^{2}$). Black star denotes smallest $χ^{2}$ (Dshort = 0.060 µm2/s, 25% immobile vesicles). Ellipse denotes 68.3% confidence region for two degrees of freedom ($χ^{2}$ < 2.30). The vesicle step size (dr = 2 nm) was sufficiently small to avoid discretization error and the simulation space (a 2 µm cube) was sufficiently large to avoid boundary effects (Figure 4—figure supplement 1). (B) Best-match simulation (red) compared to control FRAP data (open circles). Gray denotes 68.3% confidence. (C) D(t) for best-match conditions in A with steady-state value (Dlong = 0.025 µm2/s; black dashed line) computed from a double-exponential fit for t > 10 ms. Inset, D(t) on a logarithmic timescale with average time to first collision (gray dashed line, 0.46 ms) when steric interactions start to reduce vesicle mobility. (D) Same as B but with added best-match finite-difference (FD) simulation with Dlong = 0.028 µm2/s (blue). Log($χ^{2}$) = 0.8 (MC) and 0.5 (FD).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** (A) Average FRAP curves for vesicle step size dr = 1 and 2 nm (blue and red; see Equation 3) for best-match conditions in Figure 4B (2 µm cube geometries) showing a close overlap and therefore little discretization error for the simulation with dr = 2 nm. (B) The simulation in A for dr = 2 nm inside a 2 µm cube (red) was repeated inside a 3 µm cube (green), with both FRAP curves also showing a close overlap. Hence, a 2 µm cube is sufficiently large to avoid boundary effects and simulate the large interior of a MFT.

To understand how steric interactions affect vesicle mobility under different conditions, we explored the effect of different vesicle volume fractions, immobile vesicle fractions and mitochondria volume fractions on vesicle mobility. In the absence of immobile vesicles and mitochondria, increasing the vesicle volume fraction from 0 to 0.5 reduced vesicle mobility (measured as Dlong/Dshort) in a near-linear manner (Figure 5A, red circles) as previously reported (black squares; Cichocki and Hinsen, 1990). Adding immobile vesicles further reduced the diffusion coefficient of the mobile vesicles (Gaffield et al., 2006) and as the fraction of immobile vesicles increased, this effect became increasingly nonlinear. Finally, adding mitochondria reduced vesicle mobility to a similar extent across all vesicle densities (blue open circles). For conditions within MFTs, the reduction in vesicle mobility due to collisions between mobile vesicles was 30%, while that due to collisions with immobile vesicles and mitochondria was 13% and 32%, respectively. These results show vesicle collisions are a major determinant of vesicle mobility at a central synaptic terminal.

![Figure 5.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig5-v3.jpg)

**Figure 5.:** (A) Effect of steric interactions on Dlong, normalized to Dshort, as a function of the vesicle volume fraction and % immobile vesicles. In the absence of immobile vesicles, the results matched those of Cichocki and Hinsen (black squares; 1990). Also shown is Dlong/Dshort for a 0.28 mitochondria volume fraction and 25% immobile vesicle fraction (blue open circles), with dashed blue line denoting average conditions at the centre of MFTs (0.17 vesicle volume fraction in the non-mitochondrial volume). Dlong was computed for an infinitely small vesicle step size (dr = 0) via linear extrapolation (Figure 5—figure supplement 1). Lines are polynomial fits. Error bars are smaller than symbols. (B) The effect of hydrodynamic interactions on Dshort, normalized to Dcyto, as a function of the vesicle volume fraction for conditions when all vesicles are mobile (red line; Equation 5; Tokuyama and Oppenheim, 1994) or when 25% are immobile (blue line; Equations 6,7). (C) D(t) for MFT conditions in A showing initial value (Dcyto), the reduction due to hydrodynamic interactions (Dshort) and to both hydrodynamic and steric interactions (Dlong). Inset, schematic diagram of hydrodynamic interactions between vesicles (top) and a combination of hydrodynamic and steric interactions (bottom). (D) Combined effect of steric and hydrodynamic interactions on Dlong/Dcyto as a function of vesicle volume fraction when all vesicles are mobile (red circles; computed via multiplication of data in A with data in B) compared to the theoretical prediction of Tokuyama and Oppenheim (black line; Equation 8). Blue circles denote the same MFT conditions as in A. Red and blue lines are polynomial fits.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** (A) Time course of the diffusion coefficient, D(t), for dr = 0.5, 1.0 and 2.0 nm, normalized to Dshort (gray lines; see Equation 3). Steady-state values (Dlong/Dshort; open black circles) were estimated from double-exponential fits for t > 10 ms. Inset: estimate of Dlong/Dshort for dr = 0 (red circle) computed via linear back extrapolation (black line). Black square denotes solution from (Cichocki and Hinsen, 1990) for comparison. Each line is the average of 15 simulations for a 1 µm cube, no mitochondria, 0.20 vesicle volume fraction, no immobile vesicles. Periodic boundary conditions were used to simulate infinite space. Error bars are smaller than symbols. (B) The same analysis as A except parameters were the same as those for the best-match simulation in Figure 4B.

### Effect of hydrodynamic interactions on vesicle mobility

Hydrodynamic interactions have long been known to be a major determinant of the self-diffusion of nanoscale beads in crowded colloidal suspensions (van Blaaderen et al., 1992; Segrè et al., 1995). Unlike steric interactions, hydrodynamic interactions occur on a very fast timescale, so their effect on vesicle diffusion can essentially be considered instantaneous. To estimate the effect of hydrodynamic interactions on vesicle diffusion in MFTs, we used an analytical approach that is accurate across a wide range of volume fractions (Tokuyama and Oppenheim, 1994). We quantified the effect of hydrodynamic interactions by calculating the ratio of Dshort to the ‘free’ unhindered diffusion coefficient of a single vesicle in cytoplasm (Dcyto). As shown in Figure 5B, Dshort/Dcyto shows an approximately linear relationship with vesicle volume fraction (red line). However, introduction of randomly dispersed immobile vesicles at 25% produced a nonlinear dependence between Dshort/Dcyto and the total vesicle volume fraction (blue line; Freed and Muthukumar, 1978; Michailidou et al., 2009). For the vesicle volume fraction found at the centre of MFTs, Dshort/Dcyto = 0.47 (dashed blue line) suggesting hydrodynamic interactions reduce vesicle mobility by two-fold within MFTs.

### Combined effects of steric and hydrodynamic interactions on vesicle mobility

As hydrodynamic interactions act on a microsecond timescale, the vesicle diffusion coefficient D(t) is expected to decrease from Dcyto to Dshort almost instantaneously (Figure 5C). On the other hand, vesicle collisions take longer to occur, so their effect on D(t) is expected to occur on a millisecond to second timescale. At these longer timescales, both hydrodynamic and steric interactions are therefore present. The different timescales of hydrodynamic and steric interactions suggest they can be treated as independent processes, allowing their combined effect to be calculated via a simple multiplication: Dlong/Dcyto = Dshort/Dcyto × Dlong/Dshort (Figure 5D; red circles and black line; Medina-Noyola, 1988; van Blaaderen et al., 1992). For the conditions at the centre of MFTs, the combined effect of hydrodynamic interactions and vesicle collisions resulted in an 80% reduction in vesicle mobility (Dlong/Dcyto = 0.19; dashed blue line). This suggests the diffusion coefficient of dilute vesicles in cytoplasm, in the absence of crowding effects, is 0.127 µm2/s, which is only a factor of 3.5 lower than that of dilute 50 nm beads in the cytoplasm of 3T3 cells at 37°C (0.45 µm2/s; Luby-Phelps et al., 1987). A likely explanation of the lower value of Dcyto for vesicles than beads is that vesicle protein interactions with the cytomatrix slow vesicle mobility.

### Quantification of the morphology around the AZ

To understand how hydrodynamic and steric interactions could influence vesicle supply at AZs, we quantified the morphological properties of 14 AZs using 3D reconstructions from high-resolution serial-section EM (Figure 6A,B). The AZ area, closely opposed to the postsynaptic density, varied across synaptic contacts (0.009–0.039 µm2) with a mean of 0.017 ± 0.002 µm2 (n = 14). This is smaller than most other central synapses which can have 10-fold larger areas (Xu-Friedman and Regehr, 2004; Harris and Weinberg, 2012; Holderith et al., 2012). When expressed as the diameter of a circular disk, our AZ measurements correspond to a range of 108–222 nm, with mean 145 ± 8 nm.

![Figure 6.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig6-v3.jpg)

**Figure 6.:** (A) Serial-section electron micrographs containing a cerebellar MFT-GC synaptic junction (EM series #3). Scale bar: 100 nm. (B) 3D reconstruction of the synapse in A showing an AZ (red), synaptic vesicles (yellow) and postsynaptic GC dendrite (blue). (C) Vesicle count (top) as a function of distance from the AZ computed from 3D reconstructions as in B (n = 14; 22 nm bins). Counts of 0 for first bin are not shown (n = 3). Vesicle density (bottom; left axis; count per volume) for the total volume surrounding the AZ (black) or restricted volume within the vesicle cloud (red circles), and the vesicle volume fraction within the vesicle cloud computed using 4.4 nm voxels (blue line; right axis). Dashed line denotes vesicle density measured at the centre of the MFT (Figure 3B).

To determine the spatial extent of vesicles near the AZ, we designated those regions in the 3D reconstructions that contained vesicles as freely diffusible space, and all other regions as non-diffusible space (Materials and methods). We refer to the region of diffusible space extending from each AZ face as the vesicle ‘cloud’. Vesicle density within the vesicle cloud was calculated either by counting the number of vesicle centre points falling within its boundaries, or by computing the volume fraction occupied by the vesicles (Figure 6C, bottom; red circles and blue line respectively). The vesicle density reached 5652 ± 377 per µm3 at 30 nm from the AZ. This corresponds to a volume fraction of 0.25, assuming a vesicle diameter of 44 nm in fixed tissue, which is 50% higher than the volume fraction at the center of MFTs (0.17). Vesicle density declined with distance from the AZ, converging to the density estimated at the centre of the MFT for distances >100 nm. These results suggest an accumulation of vesicles extends ~2 vesicle diameters from the AZ. The total number of vesicles increased monotonically with distance from the AZ, from 2 ± 1 within 22 nm, to 48 ± 6 within 100 nm and 252 ± 34 within 300 nm (Figure 6C, top). These results show that, while there are few docked vesicles at the AZ, hundreds of vesicles reside nearby.

The similarity in vesicle density within the cloud and in the MFT interior (Figure 6C, bottom; red circles and dashed horizontal line, respectively), plus the irregular shape of the vesicle clouds, suggests diffusional barriers imposed by intracellular organelles and/or the plasma membrane are present in the AZ region. To examine this, we quantified the spatial dependence of the vesicle density assuming all of the space surrounding the AZ is diffusible (Figure 6C, bottom; black circles). This approach gave a similar estimate of the vesicle density close to the AZ, but beyond 150 nm from the AZ the density rapidly declined, reaching 15% of the peak value by 400 nm from the AZ. This suggests that, beyond 150 nm, intracellular organelles, cytoskeletal barriers and/or curvature of the plasma membrane create a significant amount of non-diffusible space (Figure 3A). Indeed, quantification of the mean distance from the AZ to the nearest mitochondrial membrane revealed mitochondria are located within 270 ± 20 nm (n = 29) of the AZ. These results suggest that the diffusible space available to vesicles is restricted near the AZ of MFTs and that vesicle density only increases above that found in the MFT interior within 100 nm of the AZ release face.

### Models of diffusion-limited vesicle supply to the AZ during sustained release

To examine the effectiveness of diffusion in supplying vesicles to AZs, we modelled vesicle diffusion in the vicinity of the 14 reconstructed AZs using our measured 3D geometries (Figure 7A). We assumed Dcyto was identical to that measured in the centre of the MFT and regions outside the vesicle cloud consisted of non-diffusible space since these regions contained no vesicles in the EM reconstructions. The most distal regions of the vesicle cloud were coupled to a large reserve of vesicles to mimic replenishment from the centre of the MFT. Hydrodynamic interactions were simulated using analytical expressions that accounted for local variations in vesicle density and the effect of the plasma membrane, which reduced vesicle mobility as vesicles approached the AZ (Figure 7—figure supplement 1). In our initial simulations, vesicles that collided with the AZ were instantaneously ‘released’ without any delay. Under these conditions the vesicle release rate equals the rate at which vesicles are supplied to the AZ via diffusion, which we here simply call the vesicle supply rate.

![Figure 7.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig7-v3.jpg)

**Figure 7.:** (A) xy cross sections through a Monte Carlo simulation of a 3D AZ reconstruction (Figure 6B; EM series #3) showing non-diffusible space (gray) surrounding the vesicle cloud and AZ (red), and reserve vesicles surrounding the cloud with restricted access. The immobile vesicle fraction was 25% (gray circles). For mobile vesicles within the cloud (green circles) Dshort was computed via a local density measurement, and hydrodynamic interactions arising from the plasma membrane (Equations 9 and 10) reduced Dshort as vesicles approached the AZ (Figure 7—figure supplement 1B). Vesicles that touched the AZ were instantaneously released. Only the central part of the simulation is shown. Scale bar: 0.5 µm. (B) Vesicle supply rate to the AZ for 14 AZ reconstructions (Figure 6) and their average (blue line). Black line denotes AZ in A. (C) Average control in B compared to the same simulations repeated for: vesicle-to-vesicle connectors and vesicle-to-AZ tethers with 100-ms lifetime for vesicles <150 nm of the AZ (orange; C-100 ms), no hydrodynamic interactions (No HI; yellow), no hydrodynamic or steric interactions between vesicles (No HI or SI; green; vesicles were simulated as dimensionless points; Dlong = Dcyto = 0.127 µm2/s) and an ‘open’ geometry where the vesicle cloud is continuous with the reserve (red). See Figure 7—figure supplement 2. (D,E) Average supply rate between 0–2 ms and at 100 ms computed for conditions in C and for connectors and tethers with 1 ms lifetime (C-1 ms). (F) Cumulative number of vesicles supplied to the AZ for simulations in C. (G) Same as F but for 100 s. Line fit to the control (black dashed line; 50–100 s) illustrates back extrapolation used to compute the RP size and the vesicle supply rate from the slope. (H,I) Supply rate between 50–100 s and pool size (as illustrated in G) for conditions in C. Estimates for an infinitely small vesicle step (dr = 0) for control conditions are similar to those shown here for dr = 5 nm (Figure 7—figure supplement 3). Gray shaded regions denote range of experimentally measured values.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig7-figsupp1-v3.jpg)

**Figure 7—figure supplement 1.:** (A) Average vesicle density near the AZ (computed in 50 nm bins for 14 AZs) at various times during the simulations of sustained release in Figure 7B for control (left), in the presence of connectors and tethers (middle; 100 ms lifetime) and for open-geometry conditions (without connectors and tethers; right). Gray region denotes the immobile vesicle volume fraction. Dashed black line denotes vesicle density measured at the centre of the MFT. Dotted black line denotes vesicle density computed with the original vesicle positions from our EM reconstructions in Figure 6, which is only slightly different to the vesicle density at the start of the simulations (solid black line) due to the algorithm that removes vesicle overlaps. (B) Estimated vesicle diffusion constant near the AZ (D90ms; computed as for Dlong in Figure 5C, but using an average of D(t) between 80–100 ms, where D(t) is computed from the MSD starting at times specified by the line colours in legend A) for different times during sustained release, across different conditions. Dashed black line denotes measured Dlong at the centre of the MFT. The vesicle step size used in the simulations was the same as that in Figure 7 (dr = 5 nm; solid lines). However, the dashed-dotted black line denotes D90ms at t = 0 estimated for an infinitely small vesicle step (dr = 0) computed via linear extrapolation using simulations for dr = 1, 2 and 5 nm (see Figure 7—figure supplement 3). Note, vesicle mobility in the open-geometry simulations is higher than Dlong at the centre of the MFT because the reserve pool in these simulations does not contain mitochondria.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig7-figsupp2-v3.jpg)

**Figure 7—figure supplement 2.:** The control xy cross section (left) is from Figure 7A. For simulations with connectors (middle) vesicles <150 nm from the AZ are connected to each other if they are <10 nm from each other (orange), and tethered to the AZ if they are <8 nm from the AZ (blue). For the open geometry (right) non-diffusible space (gray) away from the AZ was converted to diffusible space and populated with vesicles at a 0.17 volume fraction; this effectively combines the RP with the reserve pool.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig7-figsupp3-v3.jpg)

**Figure 7—figure supplement 3.:** (A) Average rate of vesicle supply to the AZ for dr = 5 nm (blue; from Figure 7B; n = 14 AZs) and dr = 0 nm (black) computed via linear extrapolation using simulations for dr = 2, 3 and 5 nm (see Equation 3). At early times (0–2 ms) the vesicle supply rate was higher for dr = 0 nm than for dr = 5 nm (2097 ± 346 vs. 1052 ± 294 s−1) but was comparable at intermediate times (100 ms; 94 ± 10 vs. 73 ± 13 s−1). (B) Cumulative number of vesicles supplied to the AZ for data in A with linear fits over 50–100 s (dashed lines). The RP sizes estimated via back extrapolation are similar (245 ± 40 vs. 237 ± 40 vesicles for dr = 0 and 5 nm, respectively) as are the steady-state vesicle supply rates (8 ± 1 vs. 7 ± 1 s−1).

At the earliest simulation times (0–2 ms) the vesicle supply rate varied between 25–4000 s−1, with a mean of ~1000 s−1 (Figure 7B–D). The average vesicle supply rate declined to ~200 s−1 by 10 ms when ~5 vesicles had been released (Figure 7F). These values are well above the experimental vesicle reloading rates of 40–80 s−1 per functional release site estimated at MFT-GC synapses during brief bursts of high-frequency stimulation (Saviane and Silver, 2006; Hallermann et al., 2010) and obtained during continuous depolarization of the presynaptic terminal (Ritzau-Jost et al., 2014). Even when vesicles were accumulated close to the AZ by simulating the effects of vesicle-vesicle binding due to fine protein connectors (Figure 7—figure supplement 2; Siksou et al., 2007; Fernández-Busnadiego et al., 2013), which reduced vesicle mobility by five-fold close to the AZ (Figure 7—figure supplement 1), the maximal vesicle supply rates remained higher than the experimental vesicle reloading rates (Figure 7D). These results suggest that at early times vesicle diffusion does not limit vesicle reloading at the AZ.

At intermediate times (~100 ms), when ~15 vesicles had been released, vesicle supply rates to the AZ approached the experimental vesicle reloading rates (Figure 7C,E,F), raising the possibility vesicle reloading could be limited by diffusion during sustained release. To investigate this, we focussed on later times (50–100 s) when the cumulative number of vesicles supplied to the AZ increased linearly with time, indicating the supply rate was constant (Figure 7G, blue line). The slope of the linear portion of the cumulative supply functions gave a mean vesicle supply rate of 7 ± 1 s−1 (Figure 7G,H) which is remarkably similar to the vesicle release rates per release site measured at MFTs (8 s−1; Saviane and Silver, 2006) and vestibular nerve synapses (7 s−1; McElvain et al., 2015) during long trains of stimuli. Moreover, the back-extrapolation method for estimating the size of the pool of vesicles that can be depleted during the train (i.e. RRP+RP) gave an average of 237 ± 40 vesicles (Figure 7I), similar to values obtained for EPSC trains at MFTs (300; Saviane and Silver, 2006) and vestibular nerve synapses (200; McElvain et al., 2015). The close agreement between our experimentally constrained models of vesicle diffusion at AZs and experimental measurements suggests vesicular release is diffusion-limited during sustained high-frequency signalling once the RRP and RP are depleted. Examination of vesicle density close to the AZ during sustained release revealed that it falls dramatically, reaching a steady state after ~20 s (Figure 7—figure supplement 1, control conditions). However, vesicle mobility increased substantially during vesicle depletion due to reduced hydrodynamic and steric interactions, resulting in a shallow concentration gradient and a constant vesicle supply rate at late times.

To better understand the role of physical factors in vesicle supply to MFT AZs, we first removed hydrodynamic interactions from our simulations. This increased the vesicle supply rate at early, intermediate and late times (Figure 7C–E,H), indicating fast hydrodynamic interactions between vesicles play a key role in slowing vesicle supply to the AZ. Interestingly, removing steric interactions (by shrinking vesicles to points) had little additional effect to removing hydrodynamic interactions at early and intermediate times (Figure 7C–E). However, at late times, removing vesicle collisions increased vesicle supply to the AZ by a factor of 2 (Figure 7C,G,H) consistent with their effect on vesicle mobility over long time scales (Figure 5D). These results show the physical interactions arising from vesicle crowding limit the maximal vesicle supply rate to the AZ.

Next, we examined how the restricted diffusible space in the vicinity of the AZ affected vesicle supply. To do this we ‘opened up’ the 14 AZ geometries by removing the non-diffusible space surrounding each AZ and filled it with vesicles at the density measured at the centre of MFTs, thereby combining the RP and reserve pools (Figure 7—figure supplement 2). For open geometries, the average vesicle supply rate at early times was the same as that for the control geometries (Figure 7C). However, after ~1 s, the average vesicle supply rate for the open geometries levelled off to 55 s−1, resulting in a seven-fold higher supply rate than the control (Figure 7G,H). Back extrapolation produced a pool size estimate of only 16 ± 3 vesicles (Figure 7I). These results suggest the presence of diffusion boundaries arising from membrane invaginations, intracellular organelles and possibly the actin cytomatrix (Sankaranarayanan et al., 2003; Guillet et al., 2016) limit diffusion-mediated vesicle supply to the AZ. Moreover, by determining the limiting vesicle supply rate during sustained release and thus the size of the pool of vesicles that can be depleted before release and supply rates equalize (excluding those replenished during that time), the geometry of the diffusible space close to the AZ determines the size of the functionally defined RP.

To examine how vesicle docking and priming (molecular and positional) and release probability affect our conclusions, we simulated 100 Hz MFT spike trains (Figure 8) assuming 1 or 2 release sites per AZ and a release probability of 0.5 (Saviane and Silver, 2006; Hallermann et al., 2010). To examine the limiting case, we assumed the total time for docking and priming (τd+p) was equal to the measured RP→RRP vesicle reloading time at these AZs (16.7 ms; Figure 8—figure supplement 1). As expected, the initial release rate was lower than that for conditions of instantaneous release and, after the RRP was released, the vesicle release rate became limited by τd+p and the release probability (Figure 8A–C). However, at later times during the train (>1 s), the release rate converged with that for instantaneous release, indicating that it had become limited by the diffusion-mediated vesicle supply (Figure 8A). Back extrapolation analysis of cumulative release at late times during the 100 Hz train gave estimates for the limiting vesicle release rate and RP size that were similar to that obtained with instantaneous release, irrespective of whether 1 or 2 release sites were present (Figure 8D,F,G). These more realistic simulations of release during 100 Hz trains therefore support our finding that vesicle release becomes diffusion-limited during sustained high-frequency signalling. Furthermore, back extrapolation analysis of the open-geometry condition revealed that the release rate rapidly becomes limited to ~30 s−1, resulting in a RP pool of only 2 ± 1 vesicles (i.e. close to the RRP; Figure 8E–G). While the exact values of the functional pool estimated from back extrapolation of the open-geometry condition may be prone to some error, because of its small size and the fact that the replenishment rate is higher than the release rate (Neher 2015), the more than 100-fold reduction in the RP estimate compared to that for measured vesicle clouds shows that the diffusible space around the AZ is a major determinant of the RP pool size.

![Figure 8.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig8-v3.jpg)

**Figure 8.:** (A) Average vesicle release rate during simulations of a 100 Hz stimulus train across 14 AZs (control geometries) each with an RRP of 1 (dark blue line) or 2 (light blue line) vesicles (i.e. 1 or 2 release sites) and a release probability of 0.5. Reloading of the RRP was mediated by diffusion followed by a delay of 16.7 ms to account for docking/priming (τd+p; Figure 8—figure supplement 1). Diffusion-limited vesicle supply rate to the AZ is shown for comparison (dashed blue line; instantaneous release condition from Figure 7C). Dark gray lines denote the maximal steady-state release rates (after the initial release of the RRP) for 1 or 2 release sites (30 and 60 s−1, respectively); rates falling below these lines indicate vesicle diffusion is limiting vesicle release. Red line shows release from an AZ with an RRP of 1 and the same τd+p for open geometry conditions during a 100 Hz train. Diffusion-limited vesicle supply rate to the open geometry AZ is shown for comparison (dashed red line; instantaneous release condition from Figure 7C). (B) Average release rate between 0–10 ms computed for conditions in A (note difference in window length of early release compared to Figure 7D due to 10 ms inter-stimulus intervals). Open symbols denote instantaneous release conditions (INST). RS: release site. (C) Average release rate at 100 ms computed for conditions in A. At these times the release rates are limited by τd+p and the release probability (horizontal dark gray lines for 1 and 2 release sites), not by vesicle diffusion. (D) Cumulative number of vesicles released during 100 Hz train for control conditions (solid blue lines). At late times the simulations of stochastic release during the train overlap with those for instantaneous release (dashed blue line) and have similar slopes (dashed and solid black linear fits, respectively). (E) Cumulative number of vesicles released for open-geometry conditions. Release during the 100 Hz train simulation with one release site (solid red line) is approximately half the diffusion-mediated AZ supply rate for the open-geometry configuration (dashed red line, and solid back line fit). (F,G) Supply rate between 50–100 s and pool size computed from linear fits to data in D and E. Dark gray lines in F as for A. Light gray shaded regions denote range of experimentally measured values.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/15133/elife-15133-fig8-figsupp1-v3.jpg)

**Figure 8—figure supplement 1.:** Vesicles docked and primed at the AZ (red) are defined as the readily releasable pool (RRP = 1 or 2 vesicles for MFT AZs). Vesicles in the RRP are reloaded from a large releasable pool (RP), where the reloading rate (kreload) is determined by the time for vesicles to be supplied to the AZ (τs), plus the time for docking (τd) and priming (τp): kreload = (τs + τd + τp)−1. Vesicles in the RP are replenished from an even larger reserve (R) pool, but at a much slower rate.

## Discussion

We have investigated the physical determinants of vesicle mobility and supply within a large central mammalian axon terminal. Our results show 75% of vesicles within cerebellar MFTs are highly mobile, and hydrodynamic interactions and vesicle collisions arising from organelle crowding are major determinants of vesicle mobility. 3D reconstructions of 14 AZs from high-resolution serial-section EM revealed ‘clouds’ of vesicles near the AZ exhibiting variable shapes and sizes. Simulations of vesicle diffusion at these reconstructed AZs suggest that, at early times during high-frequency presynaptic activity, diffusion-mediated vesicle supply is substantially faster than the experimentally measured vesicle reloading rates. However, at later times, during prolonged presynaptic activity, when the RP becomes depleted, the rate of vesicular release becomes limited by diffusion-mediated supply to the AZ. These AZ simulations predict the size of the experimentally measured RP and the vesicle replenishment rate from the reserve pool. Hence, our results identify the major physical determinants of vesicle diffusion within the crowded environment of presynaptic terminals, show vesicle mobility at an excitatory central synapse is comparable to that at ribbon synapses and suggest passive diffusion limits vesicle supply to AZs during sustained high-frequency release. Moreover, our results provide a structural basis for the functionally defined ~300 vesicle RP at MFT AZs.

### Physical determinants of vesicle mobility within MFTs

Our results show that crowding within presynaptic terminals gives rise to two types of physical interaction that slow vesicle mobility. Fast hydrodynamic interactions arising from fluid displacement influence vesicle mobility on both short (microsecond) and long (millisecond to second) timescales. In contrast, effects of vesicle collisions (Gaffield et al., 2006) are only felt on long time scales. The combined effects of these interactions result in a vesicle diffusion coefficient that evolves with a characteristic time course that depends on the vesicle density (Figure 5C). Given the strength of hydrodynamic interactions in crowded environments, it is surprising their effects have only recently been investigated in biological systems in the context of protein diffusion (Doster and Longeville, 2007; Ando and Skolnick, 2010). Our results extend these studies by showing hydrodynamic interactions are likely to be a major determinant of vesicle diffusion in synaptic terminals. Indeed, taking account of hydrodynamic and steric interactions arising from vesicle crowding explains much of the discrepancy between Dlong of vesicles and 50 nm beads in cytoplasm (Luby-Phelps et al., 1987). Hence, our results identify the main physical determinants of vesicle mobility in a central axon terminal and highlight the need to consider hydrodynamic interactions within crowded intracellular environments.

### Comparison of vesicle mobility across synapses

By quantifying how hydrodynamic and steric interactions vary with vesicle volume fraction and the fraction of immobile vesicles, it is possible to predict the vesicle mobility near the AZ and across different types of synapses (Table 2). At MFTs our quantitative model of vesicle mobility predicts that vesicle diffusion slows down from 0.025 μm2/s within the MFT interior to 0.012 μm2/s in the vicinity of the AZ. Thus, physical interactions slow vesicle mobility even in the absence of binding to tethers and connectors (which could slow diffusion further to 0.002 μm2/s). For ribbon-type bipolar cells, which have a vesicle density comparable to MFTs, our model of vesicle mobility predicts Dlong = 0.014 μm2/s, which matches well to the value measured in goldfish (0.015 μm2/s; Holt et al., 2004), but cannot account for the exceptionally high mobility found in lizard (Rea et al., 2004). Nevertheless, our framework does predict the low vesicle mobility at the NMJ (predicted 0.006 μm2/s vs. measured 0.005 μm2/s; Gaffield and Betz, 2007), where vesicle density is more than double that within the MFT (0.33 vs. 0.17 volume fraction). Measurements of vesicle mobility in small central synapses are more numerous but highly variable. Our modelling predicts that Dlong is low within the middle of the vesicle cluster in small boutons (0.002 μm2/s). This is similar to some FRAP-based estimates (Shtrahman et al., 2005) and recent single-vesicle tracking measurements (0.003 μm2/s; Lee et al. 2012). Moreover, our predicted Dlong falls within the wide range of estimates of vesicle mobility using fluorescence correlation spectroscopy (Figure 2D, pink symbols; Yeung et al., 2007; Jordan et al., 2005), but these estimates depend on the diffusion/binding model applied (Jordan et al., 2005; Shtrahman et al., 2005; Yeung et al., 2007). Synapsin-based immobilization of vesicles appears prevalent in small boutons (Orenbuch et al., 2012), consistent with reports that most vesicles are immobile (Shtrahman et al., 2005; Lee et al., 2012). Moreover, there is a rapid vesicle exchange with the axon (Staras et al., 2010; Herzog et al., 2011) where mobility is high (Lee et al., 2012). Our simulations suggest that the low mobility of vesicles in small central synapses is largely due to strong steric and hydrodynamic interactions arising from the high vesicle density. Moreover, although the presence of tethers/connectors will restrict vesicle mobility further, their effects will only be strong if they have long lifetimes (i.e. slow unbinding). While the properties of vesicle mobility within small synapses is still uncertain, our results show that to understand the variations in vesicle mobility across synapses, it is necessary to account for the physical interactions arising from organelle crowding.

**Table 2.**
 Predictions of vesicle mobility for different types of synaptic terminals.


<table>
  <thead>
    <tr>
      <th></th>
      <th>MFT</th>
      <th>MFT</th>
      <th>MFT</th>
      <th>NMJ</th>
      <th>Boutons</th>
      <th>Ribbon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Centre</td>
      <td>Cloud</td>
      <td>AZ face</td>
      <td>AZ cluster</td>
      <td>AZ cluster</td>
      <td>Centre</td>
    </tr>
    <tr>
      <td>Ves. density (per µm2)</td>
      <td>118</td>
      <td>103</td>
      <td>170</td>
      <td>224</td>
      <td>200</td>
      <td></td>
    </tr>
    <tr>
      <td>Ves. density (per µm3)</td>
      <td>3930</td>
      <td>3444</td>
      <td>5652</td>
      <td></td>
      <td></td>
      <td>4421</td>
    </tr>
    <tr>
      <td>Total ves. volume %</td>
      <td>17</td>
      <td>17</td>
      <td>25</td>
      <td>33</td>
      <td>29</td>
      <td>29</td>
    </tr>
    <tr>
      <td>Immobile vesicle %</td>
      <td>25</td>
      <td>25</td>
      <td>17</td>
      <td>40</td>
      <td>73</td>
      <td>13</td>
    </tr>
    <tr>
      <td>Imm. ves. volume %</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>13</td>
      <td>20</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Non-diffusible vol. %</td>
      <td>28</td>
      <td>36</td>
      <td>29</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Dcyto / D0</td>
      <td>0.01</td>
      <td>0.01</td>
      <td>0.01</td>
      <td>0.01</td>
      <td>0.01</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>Dshort / Dcyto</td>
      <td>0.47</td>
      <td>0.47</td>
      <td>0.39</td>
      <td>0.24</td>
      <td>0.19</td>
      <td>0.37</td>
    </tr>
    <tr>
      <td>Dlong / Dshort</td>
      <td>0.41</td>
      <td>0.30</td>
      <td>0.29</td>
      <td>0.20</td>
      <td>0.09</td>
      <td>0.43</td>
    </tr>
    <tr>
      <td>Dlong / Dcyto</td>
      <td>0.19</td>
      <td>0.14</td>
      <td>0.11</td>
      <td>0.05</td>
      <td>0.02</td>
      <td>0.16</td>
    </tr>
    <tr>
      <td>D0 (µm2/s)</td>
      <td>12.682</td>
      <td>12.682</td>
      <td>12.682</td>
      <td>12.764</td>
      <td>12.764</td>
      <td>9.055</td>
    </tr>
    <tr>
      <td>Dcyto</td>
      <td>0.127</td>
      <td>0.127</td>
      <td>0.127</td>
      <td>0.128</td>
      <td>0.128</td>
      <td>0.091</td>
    </tr>
    <tr>
      <td>Dshort</td>
      <td>0.060</td>
      <td>0.060</td>
      <td>0.050</td>
      <td>0.031</td>
      <td>0.025</td>
      <td>0.033</td>
    </tr>
    <tr>
      <td>AZ wall hydro. (β)</td>
      <td></td>
      <td></td>
      <td>0.84</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Dlong</td>
      <td>0.025</td>
      <td>0.018</td>
      <td>0.012</td>
      <td>0.006</td>
      <td>0.002</td>
      <td>0.014</td>
    </tr>
    <tr>
      <td>Dlong measured</td>
      <td>0.025</td>
      <td>NA</td>
      <td>NA</td>
      <td>0.005</td>
      <td>0.004</td>
      <td>0.110 (0.015)</td>
    </tr>
  </tbody>
</table>

_For the MFT, 3D vesicle (ves) densities were computed from 2D densities by diving by the slice thickness (0.03 µm). The total vesicle volume % was computed assuming a 44 nm vesicle diameter in fixed tissue. It was assumed the immobile vesicle volume fraction near the AZ was the same as in the MFT centre (4%). For the MFT centre computation, the non-diffusible volume (vol) is the mitochondria volume fraction; for the cloud and AZ face computations, the non-diffusible volume is the non-diffusible space within the vesicle clouds computed from the 14 AZ reconstructions. D0 was computed via the Stokes-Einstein equation assuming a 49 nm vesicle diameter for in vitro conditions at 35°C. Diffusion constants and ratios are from Results (see Figure 5). Hydrodynamic (hydro) effects from the membrane wall near the AZ were computed via Equations (9) and (10), and are average β between 50 and 100 nm from the wall, where β = (2β||+β⊥)/3. Measured Dlong near the AZ face is not available (NA): vesicles close to AZs are too small to be detected by our FRAP measurements.For the NMJ, the 2D vesicle density is the average of those reported in Mantilla et al. (2004) and Coleman et al. (2008). The total vesicle volume % was computed assuming a proportional relationship with the MFT vesicle density and volume fraction. The immobile vesicle % and measured Dlong is from Gaffield and Betz (2007). D0 was computed assuming a 49 nm vesicle diameter and 37°C.Data for the ribbon synapse is from Rea et al. (2004). The 3D vesicle density was computed assuming 250,000 vesicles with 50 nm diameter inside a hemisphere with 6 µm diameter. The non-diffusible volume was set to zero since Figure 3A of Rea et al. shows few mitochondria. D0 was computed assuming a 50 nm vesicle diameter and 22°C. Note, our estimate of Dlong is 10-fold smaller than the measured Dlong of Rea et al., but is comparable to the measured Dlong of another study of ribbon-type synapses in bipolar cells (value shown in brackets; 0.015 µm2/s; Holt et al., 2004).For the hippocampal boutons, the 2D vesicle density is from Li et al. (1995) and Schikorski and Stevens (2001). The total vesicle volume % was computed assuming a proportional relationship with the MFT vesicle density and volume fraction. The immobile vesicle % is from Shtrahman et al. (2005). D0 was computed assuming a 49 nm vesicle diameter and 37°C. Values for measured Dlong derived from fluorescence correlation spectroscopy (FCS) vary widely, depending on the model used to fit to the data (5 × 10−5 to 0.054 µm2/s; Figure 2D, pink symbols), but our predicted Dlong most closely matches that of a fit to pure diffusion (0.0043 µm2/s; Shtrahman et al., 2005) and the measured Dlong of Lee et al. (0.003 µm2/s; 2012) who tracked single vesicles using quantum dots.For all terminals, Dcyto/D0 was assumed to equal that in the MFT centre (0.01). Dshort/Dcyto was computed as the blue line in Figure 5B. Dlong/Dshort was computed using data in Figure 5A._

### Supply of vesicles to the AZ and structural correlates of the releasable pool

Our 3D EM reconstructions revealed the AZs of MFTs are small and surrounded by a cloud of vesicles that is highly variable in shape and size. Our analysis shows that on average there are only 2 vesicles at the AZ face, suggesting few vesicles are docked and release ready at each AZ. This potentially explains why multi-vesicular release (Wadiche and Jahr, 2001) is not a dominant form of release at MFTs (Sargent et al., 2005). Away from the AZ face, the vesicle density falls to a level comparable to the density measured at the centre of the MFT. The accumulation of vesicles at the AZ face has a similar spatial extent as the AZ cytomatix protein Bassoon (~100 nm), which speeds vesicle reloading at MFTs (Hallermann et al., 2010) possibly via vesicle clustering (Mukherjee et al., 2010). Our experimentally constrained simulations suggest diffusion can supply vesicles to the AZ at the onset of high-frequency signalling (<100 ms) faster than the measured vesicle reloading rates of 40–80 s−1 (Figure 7C), even in the presence of protein filament connectors and tethers (Siksou et al., 2007; Fernández-Busnadiego et al., 2013). This suggests factors other than diffusion, such as docking and priming, limit vesicle reloading at the onset of sustained release. Ca2+-dependent mechanisms that speed docking and priming (Neher and Sakaba, 2008) would therefore be most effective at accelerating vesicle reloading at the early stages of high-frequency signalling, but increasing vesicle mobility or reducing the immobile fraction would be effective later, once vesicle depletion occurs.

Previous studies of vesicular release at cerebellar MFTs (Saviane and Silver, 2006; Hallermann et al., 2010; Sargent et al., 2005) and vestibular nerve synapses (McElvain et al., 2015) suggest that each AZ has an RRP of 1–2 vesicles and a RP of ~200–300 vesicles (Figure 8—figure supplement 1). Remarkably, 3D AZ reconstructions predict the size of the RRP and our simulations predict the RP from the spatial positions of the vesicles, the diffusible space surrounding the AZ and our model of vesicle mobility. Furthermore, once the RP is depleted, our simulations predict a vesicle supply rate of 7 s−1, which matches the release rates of 7–8 s−1 recorded at these synapses (Saviane and Silver, 2006; McElvain et al., 2015). Because glutamate refilling is 100-fold slower than these rates (Hori and Takahashi, 2012), rapid local endocytosis (Watanabe et al., 2013) is unlikely to be responsible for these limiting rates. Our results therefore suggest that, during sustained high-frequency release, vesicle supply from the reserve pool to the AZ is limited by vesicle diffusion from the interior of the MFT. Thus, diffusion rather than docking and priming potentially limits the rate at which continuous sensory variables, such as head velocity (Arenz et al., 2008) and joint angle (van Kan et al., 1993), are transmitted. Moreover, the fact that increasing diffusional access to the AZ effectively eliminates the functionally defined RP indicates the shape and extent of the vesicle cloud associated with an AZ is a major determinant of the RP, because it sets the rate of supply from the reserve pool. This structural property could therefore contribute to the heterogeneous functional properties of MFTs (Sargent et al., 2005) originating from different precerebellar nuclei (Chabrol et al., 2015). Thus, our results provide the structural basis for a functionally defined vesicle pool and show diffusion ultimately limits vesicle supply during sustained high-frequency signalling at a central synapse.

## Materials and methods

### Animals

The generation and general characterization of the VGLUT1Venus (Slc17A7ct(venus)Nbr) knock-in mouse line was published previously (Herzog et al., 2011); all experiments using this line were performed with littermates derived from crossing homozygous VGLUT1v/v mice (F2 SV129/ola x C57BL/6 genetic background). All animal experiments were conducted in strict accordance with the United Kingdom Home Office Animals Scientific Procedures Act of 1986, and approved by the UCL ethics review board. All mice were anaesthetized with ketamine or isoflurane during surgical procedures.

### Electron microscopy and 3D reconstructions

Two C57Bl6 mice (P28 and P30) were anaesthetized with ketamine (35 mg) and transcardially perfused with 0.9% saline, then with 2% paraformaldehyde and 1% glutaraldehyde in 0.1 M Na-acetate buffer (pH = 6) for 2 min, then with 2% paraformaldehyde and 1% glutaraldehyde in 0.1 M Na-borate buffer (pH = 8) for one hour. Four VGLUT1Venus mice (all P28) were anaesthetized with ketamine (35 mg) and transcardially perfused with 0.9% saline, then with 4% paraformaldehyde and 0.1% or 0.05% glutaraldehyde in 0.1 M Na-phosphate buffer for 25 min. After perfusion, brains were dissected and 60 µm sections were cut from the cerebellar vermis. Sections from VGLUT1Venus mice were immunoreacted for either VGLUT1 or GFP using anti-VGLUT1 (1:500 dilution; Synaptic Systems Cat# 135 302, RRID:AB_887877; Goettingen, Germany) or anti-GFP (1:1000 dilution; Millipore Cat# AB3080P, RRID:AB_91338; Billerica, Massachusetts) primary antibodies, respectively. Sections were then washed, incubated with biotinylated or 0.8 nm gold-coupled (Aurion, Wageningen, The Netherlands) secondary antibodies. Reactions were visualized with either silver enhancement (Aurion SE-EM kit) or a DAB reaction. Following reactions, sections from the C57Bl6 mice were washed in 0.1 M PB then treated with 1% OsO4 and 1% uranyl acetate before dehydration and embedding in Epoxy resin. Small blocks from the sections were re-embedded and 30 nm serial ultrathin sections were cut for 3D reconstruction (Holderith et al., 2012). Images were taken with a Jeol JEM1011 electron microscope equipped with a bottom-mounted CCD camera (Cantega; Olympus Soft Imaging Solutions, Münster, Germany). 3D reconstructions and measurements were performed using Synapse Web Reconstruct (RRID:SCR_002716; http://synapses.clm.utexas.edu/tools/reconstruct/reconstruct.stm). MFTs from VGLUT1Venus mice were qualitatively analysed at low and high magnification and compared to those obtained from C57Bl6 mice. All GFP- and VGLUT1-immunopositive MFTs were large, contained clusters of mitochondria and had vesicle densities similar to those found in C57Bl6 mice. The cloud of vesicles surrounding the AZs were also apparent with variable size. The proximity of mitochondria to AZs was also highly variable, similar to that found in C57Bl6 mice (data not shown).

### Electron tomography

Serial sections (200 nm) from C57Bl6 mice were cut and collected onto copper slot grids. Fiducial markers were introduced at both sides of the grids (Imig et al., 2014). Single-axis tilt series were acquired in FEI Tecnai G2 Spirit BioTWIN transmission EM operating at 120 kV and equipped with an Eagle 4K HS digital camera (FEI, Eindhoven, The Netherlands). Tomographic volumes were reconstructed using IMOD (Kremer et al., 1996; RRID:SCR_003297) and exported as z-stacks for analysis. Vesicle diameters were measured using Reconstruct, defined as the distance between the outer parts of the membrane bilayers at the plane where the diameter was largest.

### Quantification of vesicle count and density surrounding the AZ

Vesicle count was computed as a function of distance from the AZ face for 14 3D reconstructions. To do this, the distance from a vesicle’s centre to the nearest point of the AZ face was measured for each vesicle and a histogram of the distances constructed using 22 nm bins. In order to compute the vesicle density as a function of distance to the AZ, we limited the diffusible space to the outermost extremity of the vesicle ‘cloud’. To do this, we divided the space surrounding the AZ into 44 nm voxels and defined voxels as diffusible only if they contained any part of a vesicle (Figure 7A). The vesicle density was computed within the cloud as a function of distance from the AZ by sorting the diffusible voxels as a function of their distance to the AZ and counting the number of vesicle centre points that fell within each bin and dividing by the sum of the voxel volumes. The vesicle density was also calculated by subdividing the 44 nm voxels into 4.4 nm voxels and computing the volume of voxels that fell within the vesicles and dividing by the total volume of the diffusible voxels. To calculate the vesicle density when assuming all space surrounding the AZ is diffusible, we divided the vesicle count as a function of distance from the AZ (22 nm bins, as described above) by the space surrounding the AZ in 22 nm thick bands.

### FRAP recordings

Parasagittal slices of the cerebellar vermis were prepared (Nielsen et al., 2004) from VGLUT1Venus knock-in mice (P22–33, n = 19). FRAP in the cerebellar slices was performed on a custom spot confocal system (Prairie Technologies, Middleton, Wisconsin; DiGregorio et al., 2007) at 35°C unless stated otherwise. Data was acquired and analyzed using NeuroMatic (RRID:SCR_004186; http://www.neuromatic.thinkrandom.com) that runs within the IGOR Pro environment (RRID:SCR_000325; WaveMetrics, Portland, Oregon). Laser light (488 nm) was focussed to a diffraction-limited spot with 100x objective lens (1.0 NA, Olympus). The bleaching pulse was 28.5 µW (after the objective) of 0.5 ms duration and probe pulses were 0.04 µW of 2 ms duration. The ACSF contained (in mM) 125 NaCl, 2.5 KCl, 2 CaCl2, 1 MgCl2, 1.25 NaH2PO4, 26 NaHCO3 and 25 glucose. Okadaic acid (2 μM), cytochalasin-D (10 μM) plus latrunculin-B (10 μM), jasplakinolide (2 or 5 μM) and roscovitine (50 µM) were added to the ACSF where specified. FRAP recordings were discarded if they had an unstable baseline fluorescence or large jumps in fluorescence. MFTs were discarded if they had less than 3 FRAP recordings.

To test for potential phototoxicity, we repeated our measurements using half the laser power during the bleaching pulse (16 MFTs, 156 total locations, 1 mouse), which produced ~13% bleaching from baseline fluorescence, rather than ~35% under control conditions, and computed f1s and f5s values. However, no significant differences were found for half-power conditions compared to control conditions for f1s (40 ± 5 vs. 35 ± 2%, respectively, p=0.4, unequal-variance t-test) and f5s values (59 ± 7 vs. 63 ± 2%, p=0.6, unequal-variance t-test), consistent with results of finite-difference FRAP simulations for full- and half-power bleaching (not shown). We also tested for time-dependent changes in the FRAP recordings within single MFTs by comparing f1s and f5s distributions computed from the first 4–10 and last 4–10 recordings taken from a single MFT. Restricting the analysis to those MFTs with at least 8 recordings (n = 47, 6 mice), we found no difference between f1s values of the first and last recordings (38 ± 2 and 37 ± 2%, respectively, p=0.8, paired t-test) and f5s values of the first and last recordings (63 ± 3 and 63 ± 3%, p=0.8, paired t-test) indicating the laser was not inducing time-dependent changes in vesicle mobility within single MFTs.

To test for photoactivation of bleached Venus (McAnaney et al., 2005), we compared FRAP recordings with 21 probe pulses after the large bleaching pulse (n = 82; Figure 1B, top) to recordings with 11 probe pulses (n = 79; recorded within the same MFTs from a P45 and P51 mouse) and found no significant difference (f1s = 33 ± 5 vs. 41 ± 4%, respectively, p=0.17, unequal-variance t-test). Since photoactivation of bleached Venus should result in a faster fluorescence recovery with a larger number of probe pulses, these results demonstrate the small brief probe pulses used in our FRAP experiments did not cause photoactivation of bleached Venus.

For each population of FRAP recordings from multiple MFTs, a final weighted average (Xi) and variance (σi2) for a given probe pulse i was computed across MFTs (e.g. Figure 1D; black circles) using the following equations:

$$
X¯_{i}=\sumjn_{j}x¯_{ji}/N_{1}\sigma_{i}^{2}=\sumjn_{j}(x¯_{ji}−X¯_{i})^{2} N_{1}/(N_{1}^{2}−N_{2})N_{1}=\sumjn_{j}N_{2}=\sumjn_{j}^{2}
$$

where j is the MFT index number, nj the number of recordings for a given MFT, and xji the average of these nj recordings.

### Estimation of Dlong from FRAP

A theoretical fluorescence recovery curve for pure diffusion can be described as follows (Axelrod et al., 1976):

$$
F_{K}(t)=f_{0}\sumn[\frac{−K^{n}}{n!}][1+n(1+\frac{2t}{\tau_{D}})]^{−1}
$$

where f0 is the fluorescence before bleaching, K is the bleaching parameter that determines the level of fluorescence immediately after bleaching (fb = (1−exp(−K))/K), and τD is the characteristic diffusion time defined as τD = ω2/4Dlong. Parameter ω is the half-width of the illumination beam at e−2 of the peak height which we estimated to be 0.23 µm from our iPSF. We computed the FK summation for n = 0–19, which was sufficient to approximate the infinite series. To determine Dlong, Equation (2) was fitted to our normalized control data by letting parameters K and Dlong vary while fixing f0 = 1 and ω = 0.23 µm. To allow a variable steady-state fluorescence (finf) during the fit, FK was transformed as follows: fK = fb + (finf − fb)(FK − fb)/(1 − fb). Results of the fit were: Dlong = 0.018 ± 0.005 µm2/s, K = 0.94 ± 0.05, finf = 0.917 ± 0.011. After drift correction, results of the fit were: Dlong = 0.025 ± 0.003 µm2/s, K = 0.97 ± 0.03, finf = 0.883 ± 0.004.

One caveat of using Equation (2) to estimate Dlong is that its accuracy relies on the following assumptions about our experimental paradigm: (1) the bleaching pulse is brief compared to the rate of diffusion, (2) bleaching is a simple irreversible first-order reaction, (3) the bleaching volume is small compared to the total volume of the synaptic terminal (4) iPSF and cPSF have the same Gaussian intensity profile in the xy direction and are infinite in the z direction (i.e. both are the same Gaussian beam), (5) fluorescence detection causes no additional bleaching during the fluorescence recovery phase, (6) there is a homogeneous concentration of diffusant and (7) diffusion is isotropic. While assumptions (1), (2) and (3) are reasonable for our experimental paradigm, assumptions (4–7) may not be strictly correct. To test assumptions (4) and (5), we used a 3D finite-difference reaction-diffusion simulation approach (see below) that explicitly modelled the bleaching and probe pulses and the spatial properties of the iPSF and cPSF of our microscope (Figure 3—figure supplement 2). Comparison of the fit to our drift-corrected control data (where Dlong = 0.025 µm2/s) to a finite-difference simulation with Dlong = 0.025 µm2/s showed a close agreement, with only a slightly slower rate of recovery for the finite-difference simulation (not shown; t1/2 = 0.58 vs. 0.66 s). Only a small increase in Dlong to 0.028 µm2/s of the finite-difference simulation was necessary to produce matching FRAP curves (Figure 2C). Similarly, to test assumptions (4–7), we used a 3D Monte Carlo simulation approach (see below) that included long cylindrical mitochondria, which form non-diffusible regions and are therefore likely to introduce anisotropic diffusion. Nevertheless, we found a close agreement to the finite-difference simulation that simulates a homogeneous concentration with isotropic diffusion (Figure 4D). These results suggest that the assumptions required to apply Equation (2) are reasonable for our experimental paradigm and it should therefore produce a reasonable estimate of Dlong.

### Finite-difference simulations

FRAP experiments were simulated in 3D space using an extended version of D3D, an in-house finite-difference reaction-diffusion simulator (Nielsen et al., 2004; DiGregorio et al., 2007; Nakamura et al., 2015). The voxel size was 50 nm and the time step (dt) was set by a stability restriction parameter (Crank, 1975) which was tested to be sufficiently small. The expression for iPSF was the same as that derived for the measured emission PSF of our microscope (Figure 3—figure supplement 2A,B), but using a light wavelength of 488 nm instead of 515 nm. The expression of cPSF (a Gaussian function with FWHMxy = 255 nm and FWHMz = 916 nm) was derived from fluorescence measured from 110 nm beads (Figure 3—figure supplement 2C). Both iPSF and cPSF were positioned so their peaks were aligned at the centre of the simulation geometry (Figure 3C). Values of iPSF and cPSF were computed at the centre of each voxel, and these values were used for bleaching and fluorescence detection. The e−2 volume of iPSF (0.31 µm3) was computed by summing the volume of voxels with an iPSF value > e−2. The e−2 volume of the cPSF was 0.15 µm3, which is small compared to the volume of the MFTs (30–60 µm3; Jakab and Hámori, 1988; Kim et al., 2013). To take advantage of xy symmetry and reduce simulation time, we simulated one-quarter of the entire space.

### Monte Carlo simulations

Brownian motion of vesicles, including steric interactions, was simulated using a 3D Monte Carlo algorithm for non-overlapping hard spheres (Cichocki and Hinsen, 1990). At the start of the simulation, mobile vesicles were given the same Dshort, the mean vesicle step size (dr) was set to a small fraction (0.5–5.0 nm) of the vesicle diameter (49 nm), and dt was computed via Einstein’s relation in 3D space:

$$
dt=dr^{2}/6D_{short}
$$

If a displaced vesicle resulted in overlap with another vesicle, or a non-diffusible voxel, the vesicle stayed at the same location; otherwise the vesicle was moved to the new location. Vesicles were not allowed to overlap with the simulation borders, except when computing D(t), in which case periodic boundary conditions were used.

For FRAP simulations, mitochondria were simulated as cylindrical regions of non-diffusible voxels with 0.28 µm diameter and 2.25 µm length, randomly placed throughout the cubic simulation space in clusters of 2–3 (Figure 3C). Vesicles were given an initial fluorescence (f) of unitary and this was then scaled by the following reaction during the bleaching and probe pulses:

$$
f_{t+dt}=f_{t}[1.0 − iPSF(x,y,z)⋅k⋅dt]
$$

where t is time, dt is the time step and k is the bleaching rate that is scaled by a normalized 3D spatial weighting function defined by iPSF described above. Average fluorescence of all vesicles was computed according to a normalized 3D spatial weighting defined by cPSF described above. The vesicle step size dr was set to 2 nm which was small enough to avoid discretization error (Figure 4—figure supplement 1A). We compared simulated FRAP curves for cubic geometries in the range 1.5–3.0 µm and found a 2 µm cube produced negligible border effects for simulations with Dshort < 0.080 µm2/s and was therefore sufficiently large to simulate the centre of a large MFT (Figure 4—figure supplement 1B).

For FRAP simulations with added drift (Figure 2—figure supplement 1B), mitochondria were simulated as non-diffusible volumes specified by x, y and z coordinates, rather than non-diffusible voxels as shown in Figure 3C, so that drift could be applied to the mitochondria’s x, y and z coordinates. If a vesicle moved outside the geometry it was returned to the opposite side of the geometry (i.e. periodic boundary conditions) with a fluorescence value of 1.0 to simulate unbleached vesicles moving into the simulation space.

One potential caveat to our quantification of vesicle mobility is the possibility our measured FRAP represents the movement of small clumps of vesicles rather than individual vesicles. However, this should not unduly affect our results since the vesicle volume fraction, rather than the vesicle size, primarily determines the hydrodynamic and steric contributions to Dlong (Medina-Noyola, 1988). Moreover, inspection of EMs of the interior of the MFT suggests vesicles are dispersed. Interestingly, vesicles exhibit a negative potential, which generates an electrostatic repulsive force, which could explain why vesicles do not tend to aggregate in clumps (Ohsawa et al., 1981).

For AZ simulations, we used the 3D reconstructions from our EM data. The diffusible space was determined by the outer surface of the vesicle cloud as described above. In one of the 14 AZ reconstructions, a low vesicle density resulted in space close to the AZ being ‘filled in’ by our algorithm. As the presence of non-diffusible space so close to the AZ seemed unlikely, we expanded the diffusible space surrounding this AZ by two vesicle diameters (the dimensions of the high-vesicle-density zone; Figure 6C). To remove the effects of fixation shrinkage in our EM data, the geometries, including AZs, were scaled up by 11% (Korogod et al., 2015). After scaling, vesicle diameters and voxel widths were 49 nm.

Because we used a uniform vesicle diameter of 49 nm, rather than a distribution, small overlaps between vesicles occurred. To alleviate this problem we used an algorithm (Lubachevsky and Stillinger, 1990) that first shrank vesicles until there were no overlaps and then allowed them to randomly move, slowly expanding until they reached a diameter of 49 nm. To maintain high vesicle densities close to the AZ (Figure 6C) vesicles <200 nm from the AZ were not allowed to move more than 24.5 nm from their original location; all other vesicles were not allowed to move more than 49 nm. We verified the average vesicle density near the AZ was similar before and after removing vesicle overlaps (Figure 7—figure supplement 1A). To create a vesicle reserve surrounding the reconstruction geometries, the geometries were expanded and populated with vesicles at a 17% volume fraction of which 25% were immobile (Figure 7A). Final simulations had ~13,000 mobile vesicles. To create ‘open’ geometries, non-diffusible voxels surrounding the AZ were converted to diffusible space and populated with vesicles as for the reserve. The final simulations had ~17,000 mobile vesicles. For all AZ simulations, dr = 5 nm, which was sufficiently small to avoid significant discretization error (Figure 7—figure supplement 3A,B). Simulations were repeated 20 times for each AZ and averaged.

To investigate how filament connectors might influence vesicle properties near the AZ, we performed simulations whereby vesicles <150 nm from the AZ rapidly formed connectors with neighbouring vesicles (average 1.5 connectors per vesicle; Siksou et al., 2007; Fernández-Busnadiego et al., 2013) if they were <10 nm of one another. Once connected, vesicles were not allowed to diffuse more than 10 nm from each other, thereby simulating flexible protein filaments (Graydon et al., 2014). A connector on rate of 10,000 s-1 was used and each bound connector had a lifetime that was randomly sampled from an exponential distribution with mean equal to the inverse of the connector unbinding rate (1000 or 10 s-1). Filament tethers to the AZ (Fernández-Busnadiego et al., 2013) were simulated in a similar fashion. In this case, vesicles became ‘tethered’ to the AZ if they were <8 nm from it. The same on and off rates of the connectors were used and no more than 2 vesicles could be tethered to the AZ at one time.

Because the vesicle density increases close to the AZ (Figure 6C) the effects of vesicle-vesicle hydrodynamic interactions are expected to be larger near the AZ. Hence, for those vesicles within the vesicle cloud, we used the local vesicle volume fraction surrounding each vesicle to compute the vesicle’s Dshort and dr on every time step of the AZ simulations. The local vesicle density was computed within a distance of 4 vesicle radii from the vesicle’s centre (Urbina-Villalba et al., 2003). Dshort was computed from the ratio Dshort/Dcyto (Figure 5B) assuming our estimate of Dcyto = 0.127 µm2/s and 0.04 immobile vesicle volume fraction.

To compute the vesicle supply rates in Figure 7, release events were counted within the following windows: 0-10 ms in 2 ms bins, 10-100 ms in 10 ms bins, 100-1000 ms in 100 ms bins, 1-10 s in 1 s bins, 10-100 s in 10 s bins. Release counts were converted to rates by dividing the bin count by the bin duration and the number of simulation repetitions (20). The cumulative vesicle counts were computed within the same windows. The vesicle release rates and cumulative vesicle counts in Figure 8 were computed in the same manner, except for using a single 10 ms bin within the first window as this corresponds to the stimulus interval of the 100 Hz train. Final release rates and counts were displayed as continuous functions by drawing lines between the midpoint of each consecutive bin.

### Calculation of hydrodynamic interactions

Effects of hydrodynamic interactions on vesicle mobility from vesicle-vesicle interactions were determined with analytical expressions for Dshort/Dcyto as a function of the vesicle volume fraction (Φ). For conditions of all mobile vesicles, Dshort/Dcyto (here denoted as Γm) was computed using the analytical expression of Tokuyama and Oppenheim (1994) (Figure 5B; red line):

$$
\frac{D_{short}}{D_{cyto}}=Γ_{m}=\frac{1}{1+H(ϕ_{m})}H(ϕ_{m})=\frac{2b^{2}}{1−b}−\frac{c}{1+2c}−\frac{bc(2+c)}{(1+c)(1−b+c)}b(ϕ_{m})=\sqrt{9ϕ_{m}/8}c(ϕ_{m})=11ϕ_{m}/16
$$

where Dcyto is equivalent to D0 of Tokuyama and Oppenheim and Φm is the mobile vesicle volume fraction. For a mixture of mobile and immobile vesicles, Dshort/Dcyto (here denoted as Γmix) was computed using the self-consistent equation of Freed and Muthukumar (1978) up to the squared term:

$$
ζ_{short}=ζ_{cyto}(1+κr+\frac{(κr)^{2}}{3})ζ_{cyto}=6\piηrκ=\sqrt{c_{im}ζ_{short}/η}\frac{D_{short}}{D_{cyto}}=Γ_{mix}=\frac{ζ_{cyto}}{ζ_{short}}
$$

where ζ is the drag coefficient (related to Stokes-Einstein equation D = kBT/ζ, kB being the Boltzmann's constant and T absolute temperature), η is viscosity, r is the vesicle radius and cim is the density of immobile vesicles (count per µm3) which was converted to the immobile vesicle volume fraction (Φim). However, Equation (6) describes conditions for small Φm. For conditions with large Φm, hydrodynamic interactions from the immobile vesicles are expected to be less due to ‘screening’ effects from the mobile vesicles. To account for this, we applied the analytical model of Michailidou et al. (2009) to compute Γmix in the presence of a large Φm (Figure 5B; blue solid line) denoted as $Γ_{mix}^{′}$:

$$
Γ_{mix}^{′}=\frac{Γ_{m}}{1+\frac{Γ_{m}}{Γ_{ff}}(\frac{1}{Γ_{mix}}−1)}Γ_{ff}=1−1.5ϕ_{m}+0.75ϕ_{m}^{2}
$$

where Γff is the far-field-only Dshort, i.e. the short-time self-diffusion coefficient in the absence of near-field hydrodynamic interactions, derived from previously published computer simulations (Banchio and Brady, 2003). Note that when Γff ≈ Γm (e.g. with a low Φm) then Equation (7) reduces to $Γ_{mix}^{′}≈Γ_{m}Γ_{mix}$.

The combined long-time effects of steric and hydrodynamic interactions, expressed as Dlong/Dcyto, was computed for conditions of all mobile vesicles using the analytical expression of Tokuyama and Oppenheim (1994):

$$
\frac{D_{long}}{D_{cyto}}=\frac{1−9ϕ_{m}/32}{1+H(ϕ_{m})+(ϕ_{m}/ϕ_{0})/(1−ϕ_{m}/ϕ_{0})^{2}}ϕ_{0}=\frac{(4/3)^{3}}{7ln(3)−8ln(2)+2}≈0.5718
$$

where Φm is the mobile vesicle volume fraction and H(Φm) is defined in Equation (5). This equation was used only for comparison purposes in Figure 5D.

For AZ simulations, the effects of hydrodynamic interactions from a membrane wall (denoted as β) were computed via analytical expressions for diffusion toward a wall (β⊥; Brenner, 1961) and parallel to a wall (β||; Goldman et al., 1967):

$$
\beta_{⊥}=\frac{6Δ_{z}^{2}+2rΔ_{z}}{6Δ_{z}^{2}+9rΔ_{z}+2r^{2}}\beta_{∥}=1− \frac{9}{16}ρ+\frac{1}{8}ρ^{3}−\frac{45}{256}ρ^{4}−\frac{1}{16}ρ^{5}ρ=r/Δ_{z+r}
$$

where △z is the shortest distance between the wall (i.e. AZ) and edge of the vesicle and △z+r is the distance between the wall (i.e. AZ) and the centre of the vesicle (i.e. △z+r = △z + r). To account for diminished hydrodynamic interactions from the wall due to a high Φm, we again used the analytical model of Michailidou et al. (2009) to apply a correction factor to β, denoted as β':

$$
\beta_{⊥}^{′}=\frac{1}{1+\frac{Γ_{mix}^{′}}{Γ_{ff}}(\frac{1}{\beta_{⊥}}−1)}\beta_{∥}^{′}=\frac{1}{1+\frac{Γ_{mix}^{′}}{Γ_{ff}}(\frac{1}{\beta_{∥}}−1)}
$$

Values for β' were then used to appropriately scale the vesicle steps in the x, y and z directions computed during each time step.

### Statistics

Data are presented as mean ± standard error of the mean (SEM) and fit parameters as ± standard deviation (STDV). Experimental and simulation results were compared with a chi-square criterion and experimental means were compared using the Student’s t-test (unpaired two-tailed equal-variance unless stated otherwise) where p<0.05 was considered significant. Model comparisons were computed via an F-test. No statistical method was used to predetermine sample sizes.

### Code

Java code to reproduce the finite-difference and Monte Carlo reaction-diffusion simulations is available at https://github.com/SilverLabUCL/D3D_eLife.
