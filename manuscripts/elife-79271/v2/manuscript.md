# Mechanosensitive pore opening of a prokaryotic voltage-gated sodium channel

## Authors

- Peter R Strege<sup>1</sup> ([ORCID: 0000-0003-4571-2207](https://orcid.org/0000-0003-4571-2207))
- Luke M Cowan<sup>1</sup> ([ORCID: 0000-0002-5512-1227](https://orcid.org/0000-0002-5512-1227))
- Constanza Alcaino<sup>1</sup>
- Amelia Mazzone<sup>1</sup>
- Christopher A Ahern<sup>2</sup> ([ORCID: 0000-0002-7975-2744](https://orcid.org/0000-0002-7975-2744))
- Lorin S Milescu<sup>3</sup> †
- Gianrico Farrugia<sup>1</sup> ([ORCID: 0000-0003-3473-5235](https://orcid.org/0000-0003-3473-5235)) †
- Arthur Beyder<sup>1</sup> †

### Affiliations

1. Enteric Neuroscience Program (ENSP), Division of Gastroenterology & Hepatology, Department of Medicine, Mayo Clinic Rochester United States ([ROR:02qp3tb03](https://ror.org/02qp3tb03))
2. Department of Molecular Physiology and Biophysics, University of Iowa Iowa City United States ([ROR:036jqmy94](https://ror.org/036jqmy94))
3. Department of Biology, University of Maryland, College Park College Park United States ([ROR:047s2c258](https://ror.org/047s2c258))
4. Department of Physiology and Biomedical Engineering, Mayo Clinic Rochester United States ([ROR:02qp3tb03](https://ror.org/02qp3tb03))

† Corresponding author

## Abstract

Voltage-gated ion channels (VGICs) orchestrate electrical activities that drive mechanical functions in contractile tissues such as the heart and gut. In turn, contractions change membrane tension and impact ion channels. VGICs are mechanosensitive, but the mechanisms of mechanosensitivity remain poorly understood. Here, we leverage the relative simplicity of NaChBac, a prokaryotic voltage-gated sodium channel from Bacillus halodurans, to investigate mechanosensitivity. In whole-cell experiments on heterologously transfected HEK293 cells, shear stress reversibly altered the kinetic properties of NaChBac and increased its maximum current, comparably to the mechanosensitive eukaryotic sodium channel NaV1.5. In single-channel experiments, patch suction reversibly increased the open probability of a NaChBac mutant with inactivation removed. A simple kinetic mechanism featuring a mechanosensitive pore opening transition explained the overall response to force, whereas an alternative model with mechanosensitive voltage sensor activation diverged from the data. Structural analysis of NaChBac identified a large displacement of the hinged intracellular gate, and mutagenesis near the hinge diminished NaChBac mechanosensitivity, further supporting the proposed mechanism. Our results suggest that NaChBac is overall mechanosensitive due to the mechanosensitivity of a voltage-insensitive gating step associated with the pore opening. This mechanism may apply to eukaryotic VGICs, including NaV1.5.

## Introduction

Electrically excitable tissues with mechanical functions like the heart and gut using VGICs to generate electrical activity, which drives mechanical activity via electro-mechanical coupling (Hille, 2001). Conversely, mechanical movements change membrane tension and impact electrical function in a process called mechano-electrical feedback (Kohl et al., 2005), which relies on specialized mechanically-gated ion channels, such as TREK (Brohawn et al., 2014) and Piezo (Ranade et al., 2015). However, studies dating back nearly 40 years suggest that VGICs are also mechanosensitive and thus may directly contribute to mechano-electrical feedback (Conti et al., 1982; Conti et al., 1984; Hao et al., 2013; Strege et al., 2003; Terakawa, 1983). Indeed, most VGIC families display mechanosensitivity, including sodium (NaV) (Morris and Juranka, 2007), potassium (KV) (Gu et al., 2001; Schmidt et al., 2012), calcium (CaV) (Farrugia et al., 1999), proton (HV) (Pathak et al., 2016), and cyclic nucleotide-gated (HCN) (Lin et al., 2007) channels. An important mechanistic advance was made in a recent study that showed that Kv channels are exquisitely mechanosensitive in their opening transition (Schmidt et al., 2012).

Mechano-electrical feedback via VGICs can play a distinct physiological role. Unlike the specialized mechano-gated channels whose activation is generally voltage-insensitive, mechanosensitive VGICs create a ‘voltage-informed’ mechano-electrical feedback (Gaub et al., 2020; Hao et al., 2013). Perhaps the best example is the voltage-gated sodium channel NaV1.5, responsible for the upstroke of cardiac action potentials (Gellens et al., 1992). Given the heart’s role as a pump, NaV1.5 is a natural target for mechanosensitivity investigations, and several studies showed that macroscopic NaV1.5 currents are mechanosensitive (Beyder et al., 2010; Morris and Juranka, 2007). Interestingly, disease-associated NaV1.5 mutations (channelopathies) can affect mechanosensitivity (Banderali et al., 2010; Beyder et al., 2014; Strege et al., 2018). Furthermore, lipid-permeable anesthetics and amphipathic drugs such as ranolazine that target NaV1.5 inhibit its mechanosensitivity, often with little effect on its voltage-dependent gating (Beyder et al., 2012a; Beyder et al., 2012b). Despite this abundant phenomenological evidence, it is unclear whether mechanosensitivity is intrinsic to the channel or emerges through interactions with other factors, and the mechanism of mechanosensitivity in NaV channels remains unknown.

NaV channels operate through a complex gating mechanism, where the voltage-dependent movement of the four voltage sensors can trigger a voltage-independent physical opening of the intracellular gate in the pore, immediately followed by a fast and thorough inactivation (Patlak, 1991). Whether applied by fluid shear stress or membrane stretch, mechanical force alters the overall voltage sensitivity of macroscopic NaV currents (Beyder et al., 2010; Morris and Juranka, 2007; Strege et al., 2003), but we do not know how each gating transition is influenced by force. In principle, this information could be extracted by analyzing the response of single-channel events or macroscopic currents to mechanical stimuli, as recently shown for KV channels (Schmidt et al., 2012). However, the complexities of the eukaryotic NaV channel structure, together with its fast activation and inactivation kinetics, would make this mechanistic analysis more challenging.

An alternative strategy is to use bacterial voltage-gated sodium channels, which have emerged as powerful models for eukaryotic NaVs (Bagnéris et al., 2014). Like their eukaryotic counterparts, prokaryotic NaVs are strongly voltage-sensitive (Ren et al., 2001), have similar pharmacological sensitivities (Lee et al., 2012a; Lee et al., 2012b), and share some structural elements despite being homotetramers (Bagnéris et al., 2014; Catterall and Zheng, 2015; Lee et al., 2012b). NaChBac from B. halodurans is the first prokaryotic NaV channel discovered (Ren et al., 2001) and presents significant advantages for mechanistic studies: at one-fourth the coding sequence length of eukaryotic NaVs, NaChBac has simpler mutagenesis, structural symmetry, and thus potentially simpler gating, slower kinetics, and removable inactivation, which altogether facilitate detailed mechanistic investigations (Lee et al., 2012a; Lee et al., 2012b). In this study, we examined the mechanism of NaChBac mechanosensitivity through a combination of macroscopic and single-channel recordings, kinetic modeling, structural analysis, and mutagenesis, and found that mechanosensitivity is intrinsic and likely resides with the channel pore.

## Results

### Mechanical stimulation of bacterial voltage-gated sodium channels

We first tested if prokaryotic sodium channels are mechanically sensitive, as previously shown for eukaryotic NaVs (Beyder et al., 2010; Morris and Juranka, 2007; Strege et al., 2003; Figure 1). In a side-by-side comparison with the eukaryotic NaV1.5, we examined two prokaryotic channels: the wild-type (WT) NaChBac and a mutant (T220A) NaChBac with inactivation removed (Lee et al., 2012a; Lee et al., 2012b; Figure 1A). We expressed each channel in HEK293 cells and assayed its mechanosensitivity via whole-cell electrophysiology, with fluid shear stress (~1.1 dyn/cm2) applied as mechanical stimulation. Under control conditions, the wild-type NaChBac responded to depolarizing voltage pulses with steep activation followed by complete inactivation, like NaV1.5 but with slower kinetics (Figure 1B, Figure 1—figure supplement 1A-D). The T220A mutant activated and stayed open with minimal inactivation (Figure 1B; Figure 1—figure supplement 1B).

![Figure 1.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig1-v2.jpg)

**Figure 1.:** (A) Topologies of eukaryotic NaV channel NaV1.5 (black) and prokaryotic NaV channel NaChBac, without (WT, blue) or with (T220A, red) point mutation T220A, which makes NaChBac devoid of inactivation. (B) Representative Na+ currents were elicited by a depolarization from –120 mV to –40 mV of NaV1.5 (black), WT NaChBac (blue), or T220A NaChBac (red), before (—) or during (▬) shear stress. (C) Difference currents were obtained by subtracting the control trace from the shear trace in (B). (D) Voltage-dependent conductance normalized to the maximum conductance of controls (G/GMax,Control) for NaV1.5 (black), WT NaChBac (blue) or T220A NaChBac (red), before (—) or during (▬) shear stress (n=7–10 cells; p<0.05 by a paired two-tailed t-test when comparing shear to control at voltages >−70 mV for NaV1.5, >−60 mV for WT and >−80 mV for T220A).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A–B) Voltage protocols (A) elicited currents (B) from NaV1.5 and WT or T220A NaChBac channels transiently expressed in HEK293 cells. Currents were recorded before (control) or during (shear) flow of bath (extracellular) solution through the recording chamber at a rate of 10 mL/min. (C–D) Time constants of activation (C, τa) or inactivation (D, τi) versus step voltage, before (●) or during (○) shear stress. (E) Current density-voltage relationship of peak Na+ currents before (●) or during (○) shear stress. (F–G) Half-point of steady-state activation (F) and availability (G), recorded before (●) or during (○) shear stress. Far-right column, mean parameters for the time constants of activation (C, τa) or inactivation (D, τi) at –30 mV, the maximum peak Na+ current (E, IPeak), the half-point of steady-state activation (F, V1/2a), and the half-point of steady-state availability (G, V1/2i), recorded from paired controls (Control) or with shear stress (Shear). Voltage clamp data were recorded from n=7–10 cells each; *p<0.05 to control or †p<0.05 to NaV1.5 by two-way ANOVAs with Dunnett’s post-test.

Shear stress increased the whole-cell currents of both prokaryotic channels, comparably to NaV1.5 (Figure 1B, ‘control’ vs. ‘shear’; Figure 1—figure supplement 1B, E; IPeak in Table 1). Both activation and inactivation responded to shear stress, as demonstrated by the difference currents (IShear – IControl) from both wild-type NaChBac and NaV1.5 (Figure 1C). Removal of inactivation in NaChBac T220A allowed us to separate these responses and focus on activation. Shear forces also increased T220A NaChBac currents, albeit slightly less than for wild-type (Figure 1C), suggesting that mechanical forces act predominantly on the mechanistic steps associated with the channel’s activation and/or opening. Overall, shear stress increased maximum conductance (GMax) by 47% for WT NaChBac and 34% for T220A NaChBac, compared to 26% for NaV1.5 (Figure 1D, GMax in Table 1).

**Table 1.**
 Effect of shear stress on parameters of wild-type and T220A NaChBac.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="3">NaV1.5</th>
      <th colspan="3">WT NaChBac</th>
      <th colspan="3">T220A NaChBac</th>
    </tr>
    <tr>
      <th>Control</th>
      <th>Shear</th>
      <th>Change</th>
      <th>Control</th>
      <th>Shear</th>
      <th>Change</th>
      <th>Control</th>
      <th>Shear</th>
      <th>Change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IPEAK (pA/pF)</td>
      <td>‑134.3±16.4</td>
      <td>‑164.0±18.5*</td>
      <td>+23.6 ± 3.5%</td>
      <td>‑37.0±9.1</td>
      <td>‑59.2±15.5*</td>
      <td>+58.7 ± 10.1%</td>
      <td>‑214.6±60.4</td>
      <td>‑281.8±73.7*</td>
      <td>+39.0 ± 6.8%</td>
    </tr>
    <tr>
      <td>GMAX (nS)</td>
      <td>2.21±0.28</td>
      <td>2.75±0.32*</td>
      <td>+26.2 ± 3.2%</td>
      <td>0.48±0.09</td>
      <td>0.71±0.15*</td>
      <td>+47.0 ± 10.9%</td>
      <td>2.96±0.81</td>
      <td>3.72±0.95*</td>
      <td>+31.7 ± 8.3%</td>
    </tr>
    <tr>
      <td>EREV (mV)</td>
      <td>+23.9 ± 2.3</td>
      <td>+20.1 ± 2.2*</td>
      <td>‑3.8±0.4</td>
      <td>+55.6 ± 5.9</td>
      <td>+55.2 ± 5.3</td>
      <td>‑0.3±2.4</td>
      <td>+21.9 ± 2.4</td>
      <td>+18.8 ± 2.5</td>
      <td>‑3.1±1.7</td>
    </tr>
    <tr>
      <td>V1/2A (mV)</td>
      <td>‑59.1±0.8</td>
      <td>‑60.5±1.0</td>
      <td>‑1.4±0.6</td>
      <td>‑45.1±2.5</td>
      <td>‑49.6±2.1*</td>
      <td>‑4.4±0.6</td>
      <td>‑70.8±2.3</td>
      <td>‑74.5±2.2*</td>
      <td>‑3.7±0.9</td>
    </tr>
    <tr>
      <td>V1/2I (mV)</td>
      <td>‑93.0±2.1</td>
      <td>‑95.5±2.4*</td>
      <td>‑2.4±0.4</td>
      <td>‑56.9±2.8</td>
      <td>‑60.7±2.0*</td>
      <td>‑3.7±1.1</td>
      <td>‑44.1±5.4</td>
      <td>‑56.4±3.5*</td>
      <td>‑12.2±3.1</td>
    </tr>
    <tr>
      <td>δVA</td>
      <td>6.1±0.3</td>
      <td>5.7±0.3*</td>
      <td>‑0.4±0.1</td>
      <td>8.1±0.6</td>
      <td>6.8±0.3*</td>
      <td>‑1.3±0.4</td>
      <td>5.1±0.6</td>
      <td>3.2±0.6</td>
      <td>‑1.9±0.8</td>
    </tr>
    <tr>
      <td>δVI</td>
      <td>‑6.9±0.1</td>
      <td>‑6.7±0.1*</td>
      <td>0.2±0.1</td>
      <td>‑6.0±0.2</td>
      <td>‑5.8±0.3</td>
      <td>0.2±0.3</td>
      <td>‑14.3±1.9</td>
      <td>‑13.2±2.3</td>
      <td>0.4±2.2</td>
    </tr>
    <tr>
      <td>τA (ms)</td>
      <td>0.49±0.04</td>
      <td>0.43±0.03*</td>
      <td>‑10.5 ± 6.0%</td>
      <td>18.6±3.4</td>
      <td>11.6±2.5*</td>
      <td>‑39.3 ± 3.8%</td>
      <td>8.4±1.8</td>
      <td>4.5±0.7*</td>
      <td>‑42.1 ± 5.6%</td>
    </tr>
    <tr>
      <td>τI (ms)</td>
      <td>0.77±0.07</td>
      <td>0.53±0.04*</td>
      <td>‑29.8 ± 3.4%</td>
      <td>213.0±37.8</td>
      <td>162.4±31.6*</td>
      <td>‑23.3 ± 4.3%</td>
      <td>—</td>
      <td>—</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

_Shear, the flow of extracellular solution; IPeak, maximum peak current density; GMax, maximum peak conductance; ERev, reversal potential; V1/2a, half-point of steady-state activation; δVa, slope of steady-state activation; V1/2i, half-point of steady-state inactivation; δVi, slope of steady-state inactivation; τa, time constant of activation at -30 mV; τi, time constant of inactivation at -30 mV. The background of NaV1.5 was H558/Q1077del. Number of cells: NaV1.5, 10; wild-type (WT) NaChBac, 7; T220A NaChBac, 7.*p<0.05 shear vs. control by a two-tailed paired Student’s t-test._

Although the steady-state conductance curves obtained under shear stress mostly appear as vertically stretched versions of the control curves, accounting for the higher maximum current, they exhibit a slight negative shift of the half-activation voltage (Figure 1D; V1/2a in Table 1). This effect is more easily visualized when each conductance curve is normalized to its maximum (Figure 1—figure supplement 1F). Shear stress also increased the conductance slope (δVa in Table 1). Interestingly, the half-inactivation voltage also exhibits a negative shift (Figure 1—figure supplement 1G ; V1/2i in Table 1). Kinetically, shear stress accelerates the time course of both activation (Figure 1—figure supplement 1C ; τa in Table 1) and inactivation (Figure 1—figure supplement 1D ; τi in Table 1).

### Interactions between electrical and mechanical stimuli

The whole-cell shear stress experiments demonstrate that mechanical forces affect NaChBac macroscopic currents. These results are likely to have mechanistic implications, but ambiguities inherent to macroscopic currents limit the information that can be extracted from data about individual state transitions. We addressed these ambiguities via single-channel recordings, followed by a mechanistic analysis to determine how force interacts with voltage to gate the channel. To simplify experiments and interpretations, we focused on NaChBac T220A, which lacks inactivation (Lee et al., 2012a; Lee et al., 2012b). We expressed NaChBac T220A in Piezo1-knockout (P1KO) HEK293 cells, free of mechanosensitive channel activity (Dubin et al., 2017; Figure 2A, Figure 2—figure supplement 1A-F). We assayed mechanosensitivity via cell-attached patch-clamp electrophysiology, using a high-speed pressure clamp (Besch et al., 2002) to apply controlled suction to patches.

![Figure 2.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig2-v2.jpg)

**Figure 2.:** (A) Representative traces of single T220A NaChBac channels at −80, –60, –40, or –20 mV and with 0 (unshaded) or –10 mmHg (shaded region) applied to the patch. (B) All-point histograms constructed from the traces shown in (A) at −80, –60, or –20 mV and 0 (black) or –10 mmHg (red) binned every 0.2 pA. Bins were normalized to an area of 1 and fit with a sum of two Gaussians, in which open events at –60 mV were 0.77 pA and 0.17 PO without pressure and 0.75 pA and 0.72 PO (330% increase) with pressure; open events at –20 mV were 0.43 pA and 0.90 PO without pressure and 0.42 pA and 0.90 PO (0% increase) with pressure. (C) Mean open probabilities (PO) at voltage steps from –100 to –20 mV with 0 (black) or –10 to –50 mmHg (red gradient) pressure (n=7–21 cells per voltage; *p<0.05, control vs. pressure by a paired two-tailed t-test). (D) PO per voltage from (C), re-plotted vs. pressure (0 to –50 mmHg).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Single channel activity from an untransfected P1KO cell before or during (shaded area) application of pressure by high-speed pressure clamp (HSPC). (B) All-sample distribution curves generated from all traces recorded from the cell represented in (A), at +60 mV and with 0 (black) or –30 mmHg pressure stimulus (red). (C) Voltage- and pressure-clamp protocols to test the pressure sensitivity of single channel currents to –30 mmHg at voltage steps from –60 through +100 mV. (D) Single channel currents averaged from 60 sweeps of the protocol shown in (C) —a holding voltage of –100 mV to steps from –50 to +100 mV with 0 (control) or –30 mmHg (pressure) applied to the patch. (E) Difference current obtained by subtracting pressure from control currents in (D) (IDifference = IControl – IPressure). (F) Current-voltage (I–V) relationship from control (black symbols), pressure (red), or difference (white) currents at the plateau, as shown in (D–E). (Inset) Enlargement of currents from –60 to 0 mV. (G) Noise spectrum averaged from 25 ten-second traces without (black) or with (red) the high-speed pressure clamp (HSPC) connected to the patch-clamp head stage. Vertical gray lines indicate multiples of 60 Hz. Noise exclusive to HSPC ≈ 1.7 kHz.

The single-channel amplitude of voltage-gated sodium channels is tiny (~1 pA at –80 mV and ~0.5 pA at –20 mV), and pressure-clamping introduces additional noise and transient artifacts. Together with rapid channel kinetics, these limitations have traditionally prevented single-channel studies on mechanosensitivity in VGICs. After careful mechanical and electrical optimization, despite the low signal-to-noise ratio typical for sodium channels (Vandenberg and Bezanilla, 1991), and the noise introduced by the pressure clamp (Figure 2—figure supplement 1G), we were able to resolve single-channel events across a physiologically relevant voltage range, and with enough bandwidth (~1 kHz) to capture sufficiently fast kinetics (Figure 2A).

Suction on the membrane patch exerts a mechanical force on the channel (Coste et al., 2010). Because patches have non-zero resting tension (Suchyna et al., 2009), we designed stimulation protocols to test voltage- and mechano-sensitivity in a pairwise fashion (Figure 2A), enabling us to assess mechanosensitivity from the difference between the suction-induced currents and the no-suction baseline, for all channels and traces. Under these conditions, a non-zero patch tension is expected to slightly bias the kinetic properties at rest but not obscure the magnitude and location of mechanosensitive steps within the gating mechanism. Within each 400ms voltage step from –100 to –20 mV, the suction pressure alternated between 0 and −10, –30, or –50 mmHg. Thus, we could obtain and compare control and pressure data in the same cell, using test pressures relevant to mechanosensitive channel function (Coste et al., 2010; Gottlieb et al., 2012). As indicated by the current amplitude histograms (Figure 2B), the single-channel current is less than 0.5 pA at –20 mV, but we could still separate the closed and open levels. Above –20 mV, the unitary current became too small for reliable analysis. Using a half-amplitude threshold method, we measured open-state occupancy between –100 and –20 mV (Figure 2C). We cross-checked this approach against fitting all-point amplitude histograms with sums of two Gaussian distributions, one for each current level (Figure 2B), where the relative weight of the open-level Gaussian indicates the open-state occupancy probability (PO). The two methods produced similar results.

Under control conditions (zero applied patch pressure), PO was strongly voltage-dependent (Figure 2A–C), as predicted by the whole-cell activation curve (Figure 1D). PO was nominally zero at –80 mV and below, and PO increased as the voltage became more positive, reaching 0.525 at –20 mV. Relative to whole-cell activation, the PO curve is shallower and ~20 mV more positive. This discrepancy is likely an artifact of a scattered and non-zero resting potential, unmeasurable in cell-attached recordings (averaging sigmoid curves with a scattered and shifted midpoint results in a shallower and shifted sigmoid).

Patch suction altered the voltage-dependent PO (Figure 2A–C; Table 2). At extremely negative voltages (–100 and –80 mV), where the channel is closed under control conditions, PO remained zero under suction. However, pressure significantly increased PO at more positive voltages. Responses were dependent on suction strength (Figure 2C and D), but even at high negative pressures (–30 and –50 mmHg), the induced changes were confined to the voltage activation range (−80 to –20 mV) (Figure 2C and D). These results agree with the whole-cell experiments, where shear stress stretched the curve vertically. As single-channel data yield the actual PO values under different pressures and voltages, we could establish that the increase in whole-cell conductance results from an increase in PO and not in single-channel conductance, which remained constant under pressure (Figure 2A and B).

**Table 2.**
 Effect of pressure on the open probability of mutants D93A and I228G in the T220A NaChBac background.


<table>
  <thead>
    <tr>
      <th>Voltage</th>
      <th colspan="3">T220A background</th>
      <th colspan="3">D93A</th>
      <th colspan="3">I228G</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>(mV)</td>
      <td>Control</td>
      <td>Pressure</td>
      <td>Difference</td>
      <td>Control</td>
      <td>Pressure</td>
      <td>Difference</td>
      <td>Control</td>
      <td>Pressure</td>
      <td>Difference</td>
    </tr>
    <tr>
      <td>–100</td>
      <td>0.023±0.013</td>
      <td>0.028±0.014</td>
      <td>0.004±0.002</td>
      <td>0.079±0.022</td>
      <td>0.109±0.062</td>
      <td>0.030±0.043</td>
      <td>0.021±0.009</td>
      <td>0.019±0.008</td>
      <td>–0.002±0.001</td>
    </tr>
    <tr>
      <td>–80</td>
      <td>0.019±0.005</td>
      <td>0.024±0.009</td>
      <td>0.005±0.005</td>
      <td>0.135±0.023</td>
      <td>0.237±0.048*</td>
      <td>0.103±0.037†</td>
      <td>0.028±0.020</td>
      <td>0.032±0.019</td>
      <td>0.003±0.002</td>
    </tr>
    <tr>
      <td>–60</td>
      <td>0.176±0.044</td>
      <td>0.271±0.069</td>
      <td>0.096±0.043</td>
      <td>0.471±0.082</td>
      <td>0.554±0.080*</td>
      <td>0.082±0.014</td>
      <td>0.100±0.033</td>
      <td>0.114±0.036</td>
      <td>0.014±0.011†</td>
    </tr>
    <tr>
      <td>–40</td>
      <td>0.353±0.071</td>
      <td>0.443±0.070*</td>
      <td>0.090±0.025</td>
      <td>0.657±0.051</td>
      <td>0.665±0.045</td>
      <td>0.008±0.023†</td>
      <td>0.379±0.062</td>
      <td>0.391±0.066</td>
      <td>0.012±0.011†</td>
    </tr>
    <tr>
      <td>–20</td>
      <td>0.525±0.067</td>
      <td>0.551±0.070*</td>
      <td>0.026±0.010</td>
      <td>0.638±0.011</td>
      <td>0.611±0.015</td>
      <td>–0.027±0.016†</td>
      <td>0.537±0.069</td>
      <td>0.524±0.067</td>
      <td>–0.012±0.010</td>
    </tr>
  </tbody>
</table>

_Open probability; n = 6-12 cells.*p<0.05, -10 vs. 0 mmHg pressure, by a two-tailed paired t-test.†p<0.05, D93A or I228G vs. T220A background by a two-tailed unpaired t-test._

Because some previous studies have shown that shear stress and patch pressure can create irreversible changes (Beyder et al., 2010; Schmidt et al., 2012; Wang et al., 2009), we tested specifically for reversibility in our preparations. In whole-cell experiments, we found that the increase in peak NaV1.5 and NaChBac T220A current density induced by shear stress are fully reversible (Figure 3A–B, Figure 3—figure supplement 2), although in some cells the acceleration in NaV1.5 kinetics or shift in half-activation voltage was not reversible and led to a non-zero difference current (Strege et al., 2003; Figure 3—figure supplement 2B). With single channels, to test the reversibility of PO increase by patch pressure, we lengthened the time before pressure application to 2 s, applied –30 mmHg pressure for 500ms, and compared the pre- and post-pressure PO values (Figure 3C, Figure 3—figure supplement 1A). Pressure increased PO throughout the –80 to –20 mV activation range (Figure 3—figure supplement 1B), with 20 out of 21 cells responding at –60 mV (Figure 3D–E). Once pressure returned to 0 mmHg, PO returned to its baseline value (Figure 3F, Figure 3—figure supplement 1C-D). As expected, this change was not instantaneous, because the channel must transition back into a different set of state occupancies, which takes time (Figure 3—figure supplement 1B).

![Figure 3.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig3-v2.jpg)

**Figure 3.:** (A) Representative whole-cell currents from HEK cells expressing T220A NaChBac were elicited by a voltage protocol (Figure 1—figure supplement 1A) before (black), during (red), or after (blue) shear stress. (B) Peak current densities before (black), during (red), or after (blue) shear stress (n=5 cells, *p<0.05 to pre-control by a one-way ANOVA with Dunnett’s post-test). (C) Representative single channel activity at –60 mV from Piezo1-knockout HEK cells transfected with T220A NaChBac, before (unshaded), during (shaded region), or after application of –30 mmHg to the patch for 500 ms. (D) All-sample distributions of single channel activity from the cell shown in (C), binned every 0.05 pA with peaks at 0 pA (closed) and ~0.9 pA (open). (E) Mean open channel probability (PO) per cell (gray circles) before (black), during (red), or after (blue) application of –30 mmHg pressure. (F) Differences in post-pressure PO (∆PO) from pre-pressure controls.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Protocols to test the reversibility of pressure-dependent increases in PO. (B) Current traces averaged from idealized single channel events in 4–17 cells at voltage steps from –100 to –20 mV, before (black), during (red), or after (blue) the pressure step to –30 mmHg. Shaded areas represent the difference in average PO with pressure versus each pre-control baseline. (C) Single channel open probability versus voltage. (D) Differences in open probability (∆PO), subtracting the open probability before pressure from either pressure (red) or post-control (blue).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Representative whole-cell Na+ current traces elicited by a voltage step from –120 to –30 mV before (black, pre-control), during (red, shear), or 2–5 min after shear stress (1.1 dyn/cm2). (B) Difference currents were obtained by subtracting the pre-control recording from either the shear (left, red traces) or the post-control recordings (right, blue traces). Na+ currents were elicited by voltage steps from –120 to –100 through 0 mV. (C) Voltage-dependent conductance of post-control currents, normalized to the maximum conductance of pre-controls (G/GMax,Control) (n=24 cells). Lower or upper boundaries of the shaded area represent the G/GMax of pre-control currents or currents during shear, respectively. (D) Maximum conductance (GMax) of Na+ currents before (black), during (red), or 2–5 min after shear stress (n=24 cells; *p<0.01, shear vs. pre-control and p>0.05, post-control vs. pre-control by paired two-tailed t-tests). (E) Difference in maximum conductance (∆GMax) of post-control Na+ currents, normalized to pre-controls.

### Mechanical force mainly affects pore opening

An intuitive interpretation of the whole-cell and single-channel results is that force alone does not open the channel. If it did, we would see openings at voltages where the channel is typically closed, provided that we applied enough membrane tension. Instead, we see that force enhances openings (increases PO) that are already driven by membrane depolarization. A simple interpretation is that force does not create additional conformational states but modifies the energetics of the existing transitions. If this is true, then force will interact with at least one mechanistic component: (1) voltage sensor activation, (2) pore opening, or (3) inactivation. It seems to us that inactivation is unlikely to play a significant role. First, NaChBac T220A responds to patch pressure like the wild type does, even though the mutant virtually lacks inactivation (Figure 1B and C). Second, eukaryotic NaV and wild-type NaChBac have similar responses to shear stress (Figure 1B and C), even though they inactivate via different mechanisms (Gamal El-Din et al., 2019). Thus, the effects of force on inactivation could simply be due to the coupling of inactivation to activation (Aldrich et al., 1983). For these reasons, we focus here on the NaChBac T220A channels, which show minimal inactivation.

The remaining possibilities are that force interacts with (1) the voltage sensors or (2) the pore. While not necessarily mutually exclusive, the two extreme models corresponding to these interactions are easier to formulate and discriminate than mixed models. Hence, we examined the specific changes in kinetic properties driven by force and compared them against model predictions. We first formulated a kinetic model (Figure 4A) that encapsulates the homo-tetrameric nature of NaChBac T220A, its voltage-dependent activation, and its lack of inactivation. We made the rates along the activation pathway (closed states C1 to C5) strongly voltage-dependent to agree with the whole-cell and single-channel activation curves (Figures 1D and 2C). In contrast, we made the concerted opening transition (C5 to open state O6) voltage-independent, as previously shown for eukaryotic NaVs (Kuo and Bean, 1994) and based on our observation that the whole-cell activation curve reaches a steady maximum (Figure 1D), which, according to the single-channel data, corresponds to a maximum PO of ~0.6 (Figure 2C). If the concerted opening were significantly voltage-dependent, the maximum PO would approach unity at strongly depolarizing voltages. The model parameters were manually adjusted to match the experimental data under control conditions (see Methods).

![Figure 4.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig4-v2.jpg)

**Figure 4.:** (A) Mechanosensitive activation (MSA) depicts a model in which the C1 to C5 closed state transitions are both voltage- and pressure-dependent (blue and red); mechanosensitive opening (MSO) depicts a model in which the C1 to C5 closed state transitions are voltage-dependent (blue), and the C5 closed to O6 open state transition is pressure-dependent (red). The predictions of these two models to voltage and pressure stimuli are shown in (B–D), with kinetic parameters as described in Materials and Methods. (B) MSA (left) and MSO (right) model predictions of open probability (PO) across voltages from –110 to –30 mV with 0 (black) or –28 mmHg applied pressure (dark red), compared to G/GMax whole-cell data (Figure 1D) with 0 (●) or 10 mL/min (○) fluid shear stress. (C–D) MSA (left) and MSO (right) model predictions of single channel PO (●) plotted versus voltage (C) at pressures from 0 to –50 mmHg (red gradient) or versus pressure (D) at voltages from –100 to –20 mV (blue gradient). (E) MSO model adapted fit to a single pressure-sensitive C5 to O6 transition with pressure-dependent kinetic constants assigned for opening (kO) and closing (kC). Insets: top, open (left), and closed (right) dwell time histograms of single channel data (black) vs. the MSO model PDF curves (blue), under 0 mmHg (top row) or –50 mmHg pressure (bottom row), with vertical dotted lines indicating the inverse of the time constants; middle, bar graphs depicting the change in the time constants kC (left) or kO (right) with –10 or –50 mmHg pressure; bottom, single channel trace recorded at –20 mV (black) and idealization (blue) with –10 mmHg applied to the region shaded (gray), compared to a trace simulated with the MSO model. *p<0.05 to 0 mmHg by unpaired two-tailed t-tests using the raw values of the time constants. (F) MSA (dotted blue line) and MSO (solid blue line) model prediction of single channel PO at –60 mV before, during, and after pressure, compared to the average current from single channel data (black).

### Mechanosensitive activation

The first scenario, where mechanical force interacts only with the voltage sensors, is captured by a mechanosensitive activation (MSA) model (Figure 4A). In this case, we expect to see force-induced changes in the mechanosensitive rate constants along the C1 to C5 pathway. Experimentally, we observed increased whole-cell current by shear stress (Figure 4B), matched by an increase in PO when membrane tension is raised via patch suction (Figure 4C). With the MSA model, we can explain this result by ascribing positive tension sensitivity (i.e. negative pressure sensitivity) to the activation (forward) rates and/or negative tension sensitivity to the deactivation (backward) rates. A situation where both activation and deactivation rates have positive or negative tension sensitivities is also acceptable, as long as the forward sensitivities are more positive than the backward ones.

The MSA model predicts that the activation curve shifts toward more negative voltages when tension increases, but its slope and maximum value remain precisely the same (Figure 4B, MSA). The activation midpoint would change because tension shifts the equilibrium of each activation step (C1 to C5) toward C5 at any given voltage. In contrast, the slope and maximum PO would be unchanged by tension because they are determined by the voltage sensitivity of activation and by the voltage- and force-independent opening transition (C5 to O6), respectively. In other words, extreme tension would push the channel to reside in the C5 and O6 states, but the equilibrium between these two states – and hence maximum PO – would remain the same. However, we did not observe this behavior experimentally. Instead, when membrane tension increased, both the whole-cell activation curve (Figure 4B) and the PO curve (Figure 4C) exhibited increased steepness and greater maximum value. The experimental activation data are thus in stark contrast with the predictions of the MSA model.

### Mechanosensitive opening

The alternative scenario, where mechanical force interacts only with the channel pore, is captured by a mechanosensitive opening (MSO) model (Figure 4A). In this case, we expect to see force-induced changes in the mechanosensitive C5 to O6 rate constants. With the MSO model, the observed increase in PO by tension can be explained by ascribing positive tension sensitivity to the opening (forward) rate, and/or negative tension sensitivity to the closing (backward) rate, or any combination where the forward sensitivity is more positive than the backward one.

The MSO model predicts that the activation curve reaches a larger value and becomes steeper when tension increases and shifts slightly toward more negative voltages (Figure 4B, MSO). The maximum PO would change because it is determined by the tension-dependent pore opening rates, but why would the voltage activation curve shift and steepen under tension, when the tension-dependent rates are voltage-insensitive? The reason is that voltage acts through the voltage-dependent activation/deactivation rates to increase the joint occupancy of the final two states, C5 and O6, while tension acts through the tension-dependent opening rates to increase the occupancy of the open state O6. Thus, under tension, an increase in voltage will lead to a proportionately larger increase in PO, compared to zero-tension conditions, and cause a shift in the activation curve, increased steepness, and a greater maximum value. Indeed, the MSO model supports the mechanically-induced changes in the whole-cell and single-channel activation curves (Figure 4B and C, MSO).

Having examined the changes in PO vs. voltage under different pressure values, we conversely examined PO vs. tension under different voltages (Figure 4D). Reversing voltage and tension as independent variables does not create new information, as we are using the same data points as in Figure 4C, but it makes it easier to judge the fitness of each model. Thus, the MSA model predicts a significant shift in the PO vs. tension curve when the voltage increases but no change in the maximum value and the slope of the curve (Figure 4D, MSA). In contrast, the MSO model predicts a significant change in the maximum value and the slope but only a small shift in the curve (Figure 4D, MSO). The experimental PO data points align well with either the MSA or the MSO model at zero pressure. However, the MSO model becomes a significantly better match to the data as the pressure increases (Figure 4C).

### Mechanical force destabilizes the NaChBac closed state

The analysis so far clearly favors the MSO model. However, we used only the steady-state information in the data, and we do not know if the MSO model can also explain the observed kinetics. The MSO model assumes tension-dependent opening and closing rates (at least one, if not both), whereas the MSA model assumes these rates to be tension-independent. If the pore opening transition were tension-dependent, then the pore opening (C5 to O6) and/or the closing (O6 to C5) rate would be affected by force, which would be reflected in the single-channel closed and open lifetimes. In our simple NaChBac kinetic model, the open state lifetime distribution has only one component, with the time constant equal to the inverse of the closing rate constant (O6 to C5). In contrast, the closed-state lifetime distribution has five components, without an easy way to isolate the opening rate constant. However, the deactivation rates are likely so small at extremely depolarizing voltages (e.g. ≥–20 mV) that the channel essentially flickers between the last two states (C5 and O6). Hence, as an approximation, the closed lifetime distribution has only one component at these extreme voltages, with a time constant that approaches the inverse of the opening rate constant (C5 to O6). Consequently, a truncated model with only the final two states would approximate the channel at –20 mV (Figure 4E).

Because NaChBac T220A has some residual inactivation (Figure 1—figure supplement 1E, J), we used relatively short (200–500 ms) voltage/pressure stimulation episodes, so many recorded traces contained no events. To fit the single-channel data with the MIL algorithm (Qin et al., 1996), we had to discard the first and last dwells in each trace because they are by necessity truncated and cannot be used for analysis, which means that all the eventless traces were also discarded. Under these conditions, the remaining traces that are suitable for analysis would slightly bias the estimated rates because of the inherently higher PO. Nevertheless, the mechanosensitivity of the opening and closing rates should emerge clearly from this analysis. As a verification, we also performed the analysis with the model parameters constrained (Navarro et al., 2018; Salari et al., 2018) to enforce a ratio between the opening and closing rate constants corresponding to the PO measured under control (zero added tension) conditions, and also to enforce the total pressure sensitivity, which can be reliably estimated from the PO data. The results obtained with these parameter constraints were similar to those obtained in the constraint-free analysis.

The closed state lifetime distribution shifts toward shorter dwell times by 15% under –10 mmHg pressure (kO: 124.9 ± 5.7 s–1 at 0 mmHg to 144.4 ± 6.6 s–1 at –10 mmHg; n=124 traces from 10 patches) and by 21% under –50 mmHg pressure (kO: 178.2 ± 11.9 s–1 at 0 mmHg to 217.0 ± 14.7 s–1 at –50 mmHg; n=23 traces from three patches) (Figure 4E). The average closed lifetime approaches the bandwidth limit (~1 ms) and, even though the fitting algorithm partially compensates for the missed events, it’s possible that the increase in the opening rate with pressure is underestimated. In contrast, the open state distribution remained virtually unchanged by tension under –10 mmHg pressure (kC: 48.1 ± 2.2 s–1 to –48.2 ± 2.3 s–1), although it shifts toward longer dwell times under –50 mmHg (kC: 101.4 ± 6.8 s–1 to –87.5 ± 6.1 s–1).

The observed shift in the closed state lifetimes further confirms that the channel is better represented by the MSO model, as the competing MSA model would exhibit no such shift at saturating voltages. Moreover, it suggests that force destabilizes the closed state, as the opening rate changes the most with tension. As we now have an idea about the magnitude of opening and closing dwell times, we can also examine activation kinetics. In principle, we can extract this information by fitting the single-channel data recorded at intermediate voltages (e.g. –60 mV), where the channel visits all states. However, the changes in voltage and pressure stimuli make these data non-stationary, and a more straightforward approach is to examine the macroscopic data created by averaging the single-channel recordings. As shown in Figure 4F, the MSO model captures well the time course of the average current and gives us an idea about the magnitude of the activation rates. In all, our modeling of the whole-cell and single channel results suggest that the MSO model, which assigns tension sensitivity to the voltage-insensitive pore opening step, best fits the experimental data and associates the NaChBac mechanosensor with the pore structure.

### Pressure may affect the stability of the intracellular gate

According to the ‘force-from-lipid’ model (Martinac et al., 1990), ion channels gain mechanosensitivity when their cross-section expands or shrinks upon a conformational change (Perozo et al., 2002a; Sachs and Morris, 1998). Based on our kinetic analysis, the site of mechanosensitivity in NaChBac is most likely the pore opening, the final gating transition (C5 to O6 in the MSO model in Figure 4A). Interestingly, previous structural modeling studies have predicted that when voltage sensors are suitably activated, mechanical energy is required to open the gate (Fowler and Sansom, 2013), which implies that negative membrane tension (i.e. patch suction) would facilitate opening. If our hypothesis were true, we would predict a change in the cross-section between the final two states in the MSO model: the activated but still closed C5 and the open O6. To test this hypothesis, we examined the two existing prokaryotic voltage-gated sodium channel structural models: NaVAb, capturing the channel in the closed conformation (Boiteux et al., 2014), and NaVMs, representing the open state (McCusker et al., 2012).

By contrasting closed and open models, we searched for the channel substructures undergoing the largest movements within the membrane plane and found that the intracellular portion of the pore-forming S6 segment is displaced laterally around a ‘gating hinge’ (Figure 5A and B). Interestingly, this type of movement has been previously proposed in functional studies (Beyder and Sachs, 2009; Webster et al., 2004; Zhao et al., 2004) and confirmed by structural experiments (Lenaeus et al., 2017), including an example where the intracellular side of a VGIC pore was found to expand the area of the bilayer’s inner leaflet upon S6 lateral movement (Beyder and Sachs, 2009; Iwasa et al., 1980).

![Figure 5.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig5-v2.jpg)

**Figure 5.:** (A) Conformational change of prokaryotic Na+ channels from the closed (cyan, NaVAb, 2017) to open state (magenta, NaVMs, 2017), illustrating the movement of the voltage sensor, S4-S5 linker, S6 segment, and C-terminal tail in relation to the lipid bilayer. (B) Location of key residues T220A and I228 in the S6 pore segment and D93 in the voltage sensor. (C–D) Voltage-dependent open probabilities ((D), PO) of single channel activities (C) recorded at the indicated voltages with 0 or –10 mmHg pressure from P1KO cells expressing the T220A NaChBac background (red or gray shading) or with additional mutations D93A (blue) or I228G (indigo). (*p<0.05, –10 mmHg vs. 0 mmHg by paired two-tailed t-tests, n=338–636 traces per voltage from 6 to 12 cells). Half-points of open probability (0 to –10 mmHg): T220A, –45.6 to –58.1 mV; D93A, –65.1 to –72.3 mV; I228G, –46.2 to –48.0 mV. (E) Difference in open probability induced by –10 mmHg pressure (PO(–10)–PO(0)) as a function of voltage in the control background (red or gray shading) or with D93A (blue) or I228G (indigo) (*p<0.05, D93A or I228G to T220A background by unpaired two-tailed t-tests).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Voltage stimulus protocol to elicit whole-cell Na+ currents by holding the cell at –170 (D93A) or –120 mV (I228G), then stepping to a voltage ladder from –120 through –60 (D93A) or through 0 mV (I228G) for 1 s, then to a single voltage at –80 mV for 200 ms (D93A) or –50 mV for 400 ms (I228G). (B) Whole-cell Na+ currents elicited by the voltage protocols shown in (A). (C) Steady-state activation curves versus the voltage of step one for the T220A background (red) or the mutants D93A (blue) or I228G (indigo). (C) Steady-state availability (inactivation) currents at step two vs. the conditioning voltage of step one for background (red) or mutant D93A (blue) or I228G (indigo) channels (n=8 (T220A), 3 (D93A), or 11 (I228G) transfected P1KO cells).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Differences in open probability (∆PO) of the T220A background (left) or I228G (right), were calculated by subtracting the open probability (PO) at 0 mmHg from the PO with −10, –30, or –50 mmHg pressure. (B) Macroscopic current traces of T220A (red) and I228G (blue) elicited by voltage steps to −70, –60, and –50 mV and with –30 mmHg, compared to currents at 0 mmHg pressure (gray). (C) Current-voltage plots of T220A (red) and I228G (blue) at –30 mmHg vs. 0 mmHg controls (gray) (T220A, n=10 cells, *p<0.05, 0 to –30 mmHg; I228G, n=7 cells, p>0.05, 0 to –30 mmHg by paired two-tailed t-tests).

According to our structural analysis, the ‘force-from-lipid’ model applies to NaChBac. Because S6 helices move and open the pore only after voltage sensors activate, it follows that mechanosensitivity, which is associated with S6 movement, resides with the pore opening (C5 to O6 in the MSO model) and not with the voltage sensor activation (C1 to C5 in the MSA model). This interpretation agrees with the MSO model, with one potential caveat being that NaVAb as a closed channel could represent other closed states along the activation pathway, rather than the fully activated closed conformation (C5 in the MSO model). As a result, a mechanosensitive transition could still occur before the pore opening. In other words, although the pore opening is likely mechanosensitive, it might not be the only mechanosensitive transition, based solely on these structural models.

If mechanosensitivity were built into the pore opening, altering S6 lateral movement via mutagenesis would alter the effects of patch suction on PO. However, if voltage sensor activation were additionally mechanosensitive, then voltage sensor mutagenesis would only change the response to suction but not eliminate it. We tested these ideas via site-directed mutagenesis within the S6 hinge and the voltage sensor, using NaChBac T220A as background. Most mutations we tried within the pore resulted in non-expressing or non-functional channels, but we eventually settled on I228G in the S6 hinge region (Figure 5B). Within the voltage sensor, we chose D93A to stabilize the sensor in the resting position (DeCaen et al., 2009; Figure 5B). We applied the same single-channel experimental paradigms to directly compare the double mutants (NaChBac T220A plus I228G or D93A) with the T220A results described above (Figure 5C).

The voltage sensor NaChBac T220A+D93A double mutant shifted its voltage sensitivity relative to T220A (Figure 5D; Figure 5—figure supplement 1C). However, its mechanosensitivity remained intact and followed the negative shift of voltage-dependent gating (Figure 5D and E). The pore NaChBac T220A+I228G double mutant channel exhibits some interesting properties. First, the channel could gate normally with voltage, like the single mutant controls (Figure 5D). Second, the effect of membrane tension on PO was nearly eliminated at all pressures (Figure 5E). Thus, at –60 mV, membrane tension increased PO by 0.096 for the NaChBac T220A mutant but only by 0.014 for NaChBac T220A+I228G, corresponding to an approximate sevenfold difference in effects between the two mutants. At –40 mV, the difference was similar (~sevenfold): 0.090 with NaChBac T220A and only 0.012 with NaChBac T220A+I228G. We could explain the small remaining effect of tension on PO in the double mutant in two ways: either there is a partial displacement of S6 during pore opening and a resulting (smaller) cross-section expansion, or there is another (weakly) mechanosensitive transition in the gating mechanism. The first possibility seems more plausible, because some degree of S6 displacement is probably necessary for channel opening, and also because NaChBac T220A+D93A maintained a tension sensitivity similar to NaChBac T220A, even though its voltage sensitivity shifted by more than –30 mV (Figure 5D). Overall, these mutagenesis results provide experimental evidence that strengthens our conclusion that mechanical forces interact primarily with the pore opening transition.

## Discussion

Electrically excitable cells depend on concerted efforts by VGICs to detect small changes in transmembrane voltage and amplify them to produce a wide range of action potentials (Hodgkin and Huxley, 1952). Some electrical organs, such as the heart, bladder, and gut, function primarily as mechanical pumps, using excitation-contraction coupling to drive muscle contractions. Cells in these pumps experience significant recurrent changes in membrane tension that can potentially affect the activity of membrane proteins, which, in turn, can affect organ function by a process called mechano-electrical feedback (Gaub et al., 2020; Hao et al., 2013; Otway et al., 2007; Strege et al., 2003). In these mechanical environments, VGICs mechanosensitivity may serve to integrate electrical (Navarro et al., 2020) and mechanical signals into a single control loop (Hao et al., 2013).

VGICs are undoubtedly mechanosensitive (Beyder et al., 2010; Laitko et al., 2006; Morris, 2011; Morris and Juranka, 2007; Schmidt et al., 2012; Tabarean et al., 1999), but the underlying mechanosensitivity mechanisms remain poorly understood, due to intrinsic structural and functional limitations. Here, we used the relatively simple bacterial voltage-gated sodium channel NaChBac as a model, because it shares crucial structural and functional elements (Bagnéris et al., 2014; Ren et al., 2001) with the more complex eukaryotic voltage-gated sodium channels (NaVs). We found that NaChBac (Ren et al., 2001) is mechanosensitive, and, impressively, the mechanosensitive responses of NaChBac closely resemble those of NaV1.5 (Figure 1), with force increasing the peak currents and accelerating the kinetics. These effects are consistent with previous studies using macroscopic currents to examine mechanosensitivity in eukaryotic NaVs (Beyder et al., 2010; Morris and Juranka, 2007) and other VGICs (Calabrese et al., 2002; Gu et al., 2001; Schmidt et al., 2012), which further strengthens NaChBac as a model for studying eukaryotic VGICs. In response to physiological levels of mechanical stimuli traditionally used to stimulate a mechano-gated ion channel (Kefauver et al., 2020), NaChBac channels substantially increased their activity in a voltage-dependent manner, in both macroscopic and single-channel preparations (Figures 1 and 2). Force produced a rise in the peak current evoked by depolarizing the membrane to activate the channels. However, without membrane depolarization, force alone could not open NaChBac (Figure 1 and Figure 2), suggesting that mechanical force does not create new conformational states but rather impacts a single transition along the gating pathway. While whole-cell experiments proved informative, single-channel studies were required to more directly test our hypotheses.

We removed NaChBac inactivation (NaChBac T220A) (Lee et al., 2012a; Lee et al., 2012b), which allowed us to zoom in on the mechanosensitivity of voltage-dependent activation. Using the NaChBac T220A mutant, along with technical optimizations and a paired-stimulus configuration that controlled for the known resting elevated mechanical tension in patch bilayers (Opsahl and Webb, 1994; Suchyna et al., 2009), we were able to resolve sub-pA NaChBac events with mechanical stimulation (Figures 2—5). Patch suction modified NaChBac voltage-gating, reversibly increasing NaChBac voltage-dependent open probability (PO) in a dose-dependent fashion. This effect was indeed state-dependent, suggesting that applied forces have a state-specific effect on the NaV channel, where the added mechanical energy appears to modify the energy landscape of gating but does not overcome voltage-gating (Fowler and Sansom, 2013; Sigg and Bezanilla, 2003).

To explain NaChBac mechanosensitivity, we favor a ‘mechanosensitive opening’ mechanism (the MSO model), rather than a ‘mechanosensitive activation’ (the MSA model). The MSO model features pore opening as one strongly mechanosensitive transition (Figure 4) and is consistent with the previous findings in KV channels, where mechanosensitivity was examined in macroscopic currents (Schmidt et al., 2012). Considering the simplicity of our MSO model, it is remarkable how well it could fit both whole-cell and single-channel data, under a fairly broad range of voltage and pressure values. The critical discriminator between the two competing models is the force-induced change in the macroscopic and single-channel voltage-dependent activation curves, i.e., increased maximum response and slope. The observed effects are by far better explained by the MSO model. The MSO model also accounts for the pressure-induced changes in pore opening kinetics, projecting that at maximally activating voltages, patch suction may shorten the closed state lifetimes and may destabilize the closed state. At higher pressure, patch suction may additionally lengthen the open-state lifetimes. While the structures responsible for voltage and force sensitivity may be distinct and function independently, from a kinetic mechanism standpoint, voltage and force sensitivities are state-dependent and intertwined: voltage acts on states C1 through C5, whereas tension acts on states C5 and O6. Consequently, channels must first activate by voltage before responding to tension. While simplified, this model captures the essence of the VGIC function and can apply to both prokaryotic and eukaryotic sodium channels.

By comparing the closed and open bacterial NaV crystal structures, we identified the intracellular gate as the site where the most extensive cross-section area changes occur during the transition from closed to open (Lenaeus et al., 2017; McCusker et al., 2012). The bottom halves of S6 form the intracellular gate, working like hinges on a door latched by non-covalent interactions. Functional and modeling studies support the swinging door model: targeting S6 residues around the pore’s hinge impedes gating (Webster et al., 2004; Woolfson et al., 1991; Zhao et al., 2004), and pore opening leads to a physical expansion of the inner leaflet, suggesting a significant area expansion (Beyder and Sachs, 2009). Consistent with these studies, electrophysiology and modeling show that S6 in the pore stores the mechanical energy of gating (Fowler and Sansom, 2013; Long et al., 2005). We targeted sites separately to differentiate between the effects of force on voltage sensors from those on the pore. The S4 positively charged residues that sense voltage are stabilized in the resting state within the lipid bilayer by counterbalancing acidic (negatively charged) residues (DeCaen et al., 2009). By mutating one of these acidic residues (D93), the half-activation and half-inactivation voltages shifted negative, but the channel maintained its responsiveness to patch pressure, confirming that voltage sensors do not significantly contribute to mechanosensitivity (Figure 5). Our functional data suggested that S6, forming a highly conserved component of the intracellular gate, might influence NaChBac mechanosensitivity. After many mutants turned out to be non-functional, we eventually identified and mutated a conserved hydrophobic residue, I228, located in the S6 lining the channel pore. I228G eliminated the response to pressure (Figure 5). The dramatic loss of I228G NaChBac mechanosensitivity suggests a loss of pressure sensitivity in the final opening step. However, it is also possible that the overall gating scheme for I228G NaChBac changed compared to its T220A background, leading to a loss of apparent dependence on the pressure-sensitive opening step. Thus, these results agree with structural and functional data showing significant in-plane area expansion during channel gating, support the swinging door model of VGIC pore gating, and suggest that force and voltage cooperate to gate NaChBac.

Since broad structural aspects of the intracellular gate appear conserved across VGICs, from prokaryotes to eukaryotes (Bagnéris et al., 2014; Shaya et al., 2014), we surmise that VGIC mechanosensitivity may be a generalizable, ubiquitous property, that can be observed across many families of VGICs (Morris, 2011; Schmidt et al., 2012) and across each phylum, including unicellular to complex multicellular organisms. Future studies may answer the fascinating questions of how archaic prokaryotic ion channels, including sodium channels, have developed mechanosensitivity, potentially as their earliest sense (Anishkin et al., 2014), and what role has selective pressure played in maintaining, developing, or losing this property.

How does membrane tension reach the NaChBac pore? In the force-from-lipid model, bilayers transduce mechanical energy directly into channel gating (Kung, 2005; Martinac et al., 1990; Zheng et al., 2011). For the tensed bilayer to perform work (F⋅d) on the channel, conformational transitions leading to the open state must associate with in-plane area expansion during the opening, and with area contraction during closing (Sachs and Morris, 1998). Bilayers self-assemble to minimize contact between lipid tails and water molecules. However, despite the minimization of free energy in assembled bilayers, the physical and energetic differences between phospholipid headgroups and lipid tails produce substantial intrinsic lateral forces (Cantor, 1997), reaching 1000 atm (Gullingsrud and Schulten, 2004). These lateral forces act upon the protein-lipid interface of ion channels (Kefauver et al., 2020; Perozo et al., 2002b) and have non-homogeneous effects on resident proteins through the bilayer thickness: the hydrophobic lipid core applies compression while phospholipid head groups apply tension (Figure 6). Specialized mechano-gated ion channels are logical candidates to take advantage of this physical arrangement, and indeed they leverage forces developed at the protein-lipid interface for their force-from-lipid gating (Cox et al., 2019; Kefauver et al., 2020; Martinac et al., 1990; Perozo et al., 2002b). For VGICs, both voltage sensors (Schmidt et al., 2006) and pore-forming structures are bathed in phospholipids (Shaya et al., 2011). Therefore, it is reasonable to conclude that lipids could contribute to force sensing (Fowler and Sansom, 2013; Schmidt et al., 2012), given that lipids are crucial for voltage-dependent gating (Milescu et al., 2009; Schmidt et al., 2006) and pore opening (Fowler and Sansom, 2013; Morris and Juranka, 2007; Shaya et al., 2011; Zheng et al., 2011), and lipid-permeable compounds frequently alter VGIC mechanosensitivity (Beyder et al., 2012a; Cowan et al., 2022). Further work is required to determine the energetics of intracellular pore dilation, lipid-protein interactions in VGIC mechanosensitivity, and to translate these results to eukaryotic VGICs will require technical and molecular modifications to slow down and resolve kinetics and remove inactivation.

![Figure 6.](https://cdn.elifesciences.org/articles/79271/elife-79271-fig6-v2.jpg)

**Figure 6.:** (A) VGIC pore is embedded in the lipid bilayer, which has an intrinsic distribution of mechanical forces even with no tension added to the system. (B) Mechanical stress applied to the bilayer alters the profile of bilayer forces, which destabilizes the intracellular gate and leads to intracellular pore expansion.

VGIC’s PO-dependent mechanosensitivity has important physiologic implications, allowing NaV channels to serve as voltage-sensitive mechanosensors. Force can adjust the voltage set point for NaV channel activation and affect action potential upstroke, regulating excitability (Conti et al., 1982; Conti et al., 1984). Meanwhile, mechanosensitivity in voltage-gated potassium (KV) channels (Schmidt et al., 2012) may serve as a mechanical brake on neuronal hyperexcitability, in a voltage-sensitive fashion (Hao et al., 2013). Beyond roles for VGIC mechanosensitivity in physiology, studies have uncovered patient VGIC mutations with functional disruptions in mechanosensitivity associated with diseases such as long-QT syndrome (Banderali et al., 2010) and irritable bowel syndrome (IBS) (Saito et al., 2009; Strege et al., 2018).

VGIC mechanosensitivity could be pharmacologically targeted in mechano-pathologies. Although specific VGIC mechanosensing inhibitors remain undeveloped, recent studies show that some amphipathic compounds that target NaV channels are effective blockers of NaV mechanosensitivity, separately from their local anesthetic mechanism (Beyder et al., 2012a; Beyder et al., 2012b; Cowan et al., 2022). Interestingly, the compounds’ amphipathic nature is critical for function (Beyder et al., 2012a; Cowan et al., 2022), implying the channel pore’s lipid-protein interface is crucial for VGIC mechanosensitivity and suggesting the intracellular gate’s interaction with lipids may provide a novel pharmacologic target.

To summarize, we show here that the prokaryotic VGIC NaChBac is intrinsically mechanosensitive, and its mechanosensitivity may depend on the channel pore intracellular gate. These results offer opportunities for future studies to determine roles for NaV channel mechanosensitivity in physiology and pathophysiology and target NaV mechanosensitivity in disease.

## Materials and methods

### Cell culture

Human embryonic kidney cells (HEK293; American Type Culture Collection, Manassas, VA) were cultured in minimum essential medium (MEM, 11095–080) supplemented with 10% fetal bovine serum (FBS, 10082147) and 1% penicillin-streptomycin (15140–122, Life Technologies, Co., Grand Island, NY). Regular or Piezo1 knockout (P1KO) HEK293 cells (a kind gift from Dr. Ardem Patapoutian, Scripps Research Institute Dubin et al., 2017) were transfected with DNA plasmids encoding wild-type NaV1.5 (variant H558/Q1077del) or wild-type or T220A NaChBac, along with GFP as a reporter, by Lipofectamine 3000 reagent (L3000-008) in OPTI-MEM medium (31985–070; Life Technologies, Co., Grand Island, NY). P1KO cells submitted to American Type Culture Collection (ATCC, Manassas, VA) for STR profiling were an exact match (eight core loci plus Amelogenin) for the Piezo1 knockout HEK293T cell line, CRL-3519. PCR testing on P1KO cells was negative for mycoplasma. Transfected cells were incubated at 37 °C for 24 hr (NaV1.5) or 32 °C for 24–48 hr (WT or T220A NaChBac). Then, cells were lifted by trypsin and resuspended in NaCl Ringer’s extracellular solution (composition below) before electrophysiology.

Site-directed mutagenesis was performed in the T220A NaChBac background to introduce an additional mutation, I228G or D93A, by using the QuikChange Lightning Site-Directed Mutagenesis Kit (Agilent Technologies, Santa Clara, CA). Upon verification of construct integrity and successful mutagenesis by DNA sequencing, either plasmid was transfected into P1KO cells for electrophysiology (Table 3, Figure 5).

**Table 3.**
 Primers for mutagenesis of I228G or D93A into the T220A NaChBac background.


<table>
  <thead>
    <tr>
      <th>Mutation</th>
      <th>Forward primer</th>
      <th>Reverse primer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>I228G</td>
      <td>TCATCTTTAACTTGTTTATCGGTGTAGGCGTCAATAACGTTGAAAAAGCAGA</td>
      <td>TCTGCTTTTTCAACGTTATTGACGCCTACACCGATAAACAAGTTAAAGATGA</td>
    </tr>
    <tr>
      <td>D93A</td>
      <td>TGGTTTGCTTTCTTAATTGTAGCCGCAGGT</td>
      <td>ACCTGCGGCTACAATTAAGAAAGCAAACCA</td>
    </tr>
  </tbody>
</table>

### Electrophysiology

#### Pipette fabrication and data acquisition

Pipettes were pulled from KG-12 or 8250 glass (King Precision Glass, Claremont, CA) for whole-cell or cell-attached patches, respectively, on a P-97 puller (Sutter Instruments, Novato, CA) and coated with HIPEC R-6101 (Dow Corning, Midland, MI). Membrane tension depends on resting pressure, applied pressure, and membrane area (Lewis and Grandl, 2015; Slavchov et al., 2014; Suchyna et al., 2009). The membrane area is defined by dome shape and membrane creep, factors influenced by the unique diameter and angle of each pipette tip. We kept 8250 glass pipettes within a narrow 1.2–1.5 MΩ range optimal for assessing the pressure response of channels (~4.2 µm in diameter and ~14° from wall to wall). Between pipette pairs, the heating parameter was reduced by 1–3 units in each stage of the four-stage pull to ensure that the break time fell within 2 s of the previous pair. Data were acquired with an Axopatch 200B amplifier, Digidata 1440A or 1550, and pClamp 10.6–11.2.1 software (Molecular Devices, Sunnyvale, CA).

#### Recording solutions

For whole-cell electrophysiology of WT or T220A NaChBac, the extracellular solution was NaCl Ringer’s, containing (in mM): 150 Na+, 5 K+, 2.5 Ca2+, 160 Cl-, 10 HEPES, 5.5 glucose, pH 7.35, 300 mmol/kg. The intracellular solution contained (in mM): 145 Cs+, 5 Na+, 5 Mg2+, 125 CH3SO3-, 35 Cl-, 10 HEPES, 2 EGTA, pH 7.0, 300 mmol/kg. For whole-cell electrophysiology of NaV1.5 and cell-attached patch-clamp of T220A NaChBac, the bath (extracellular) solution contained (in mM): 135 Cs+, 15 Na+, 5 K+, 2.5 Ca2+, 160 Cl-, 10 HEPES, 5.5 glucose, pH 7.35, 300 mmol/kg. The pipette solution for cell-attached patches was NaCl Ringer’s, supplemented with 0.03 mM Gd3+ to inhibit leak currents.

#### Whole-cell voltage clamp

Whole-cell Na+ currents from HEK293 cells heterologously expressing NaV1.5 (variant H558/Q1077del) or WT or T220A NaChBac were recorded with a two-pulse protocol that tests channel activation during the first step and channel availability (steady-state inactivation) during the second step. Cells expressing NaV1.5 were pulsed every 1 s from the –130 mV holding potential through –10 mV in 5 mV intervals during step 1, then immediately pulsed to –40 mV for 50 ms during step 2. NaV1.5 data were sampled at 20 kHz and filtered at 5 kHz. Cells expressing NaChBac were pulsed every 4.75 s from the –120 mV holding potential through 0 mV in 10 mV intervals during step 1, then immediately pulsed to 0 mV for 50 ms (WT) or –50 mV for 400 ms (T220A) during step 2 (Figure 1—figure supplement 1A). NaChBac data were sampled at 2 kHz and filtered at 1 kHz.

#### Cell-attached patch-clamp

P1KO cells heterologously expressing T220A NaChBac channels were held at –120 mV. To obtain single-channel events, we recorded thousands of sweeps in response to a voltage ladder protocol containing five 400 ms-long steps, from –100 mV to –20 mV in 20 mV increments, with a 3 s inter-sweep interval. Each voltage step was divided into two 200 ms-long pressure steps, from 0 mmHg to −10, –30, or –50 mmHg. Because the D93A mutant had open and closed times approximately 2–5 times longer than T220A, D93A experiments were performed with 4 s-long voltage steps and 2 s-long pressure steps. To test reversibility following pressure, the duration of each of the five voltage steps was 1 s with a 7.5 s inter-sweep interval, and pressure was applied for 500 ms (Figure 3—figure supplement 1A). Capacitance and passive currents were subtracted with a 1-sweep blank record, averaged from several to dozens of traces from the same or a subsequent recording in which no channel openings were observed (Benndorf, 1994).

#### Mechanical stimulation

Mechanical stimuli were applied by shear stress to the entire cell, and by pressure clamp to membrane patches, as previously described (Beyder et al., 2012a; Beyder et al., 2012b). For whole-cell electrophysiology, shear stress was applied as the flow of extracellular solution through the 700 µL elliptical bath chamber, for 60–90 s at 10 mL/min (Beyder et al., 2012a; Strege et al., 2018). Shear stress (1.1 dyn/cm2) was estimated by the equation $\tau=\frac{6ηQ}{h^{2}w}$ , in which τ is shear stress, η is viscosity (~1.02 cP), Q is flow rate (10 mL/min), h is solution depth (1 mm), and w is chamber width (9 mm). For cell-attached patch-clamp experiments, a negative pressure of –10 or –30 mmHg was applied by high-speed pressure clamp (HSPC-1, ALA Scientific Instruments, Farmingdale, NY) (Besch et al., 2002). The single-channel data were sampled at 20 kHz and low-pass filtered online at 5 kHz but for analysis were further filtered at 0.5 kHz, due to a bandwidth limitation imposed by the HSPC (Figure 2—figure supplement 1G). Patches are known to have non-zero resting tension (Suchyna et al., 2009), so we took great care to minimize the negative pressure while forming seals. The pressure clamp was set to +10 mmHg prior to the pipette entering the bath, and seals were acquired spontaneously by stepping to 0 mmHg momentarily after the pipette tip made contact with the cell membrane. Initial pipette resistance was 1–2 MΩ, and seal resistance was >10 GΩ.

### Data analysis

Data were analyzed in pClamp version 10.6 or 11.0.3 (Molecular Devices, Sunnyvale, CA), Excel 2010 (Microsoft, Redmond, WA), and SigmaPlot 12.5 (Systat Software, San Jose, CA). To estimate whole-cell conductance and the voltage of half-activation, the peak current evoked by voltage step 1 in the protocol described above was fit with a Boltzmann equation, $I_{V}=V-E_{Rev}\timesG_{Max}/1+e^{V-V_{1/2a}/\deltaV_{a}}$ , where IV is the peak current (pA/pF) at the test voltage V (mV), ERev is the reversal potential (mV), GMax is maximum conductance (nS), V1/2a is the half-activation voltage (mV), and δVa is the voltage sensitivity of activation (mV). To estimate the voltage of half-inactivation, the peak current IV evoked by voltage step 2 in the protocol was first normalized as a percentage to its maximum across all sweeps and then was fit with a Boltzmann equation, $I_{V}=1/1+e^{V-V_{1/2i}/\deltaV_{i}}$ , where V1/2i is the half-inactivation voltage and δVi is the voltage sensitivity of inactivation. For kinetic analysis, whole-cell currents were fit to an exponential equation, $I_{t}=A_{1}\timese^{-t/\tau_{a}}+A_{2}\timese^{-t/\tau_{i}}+C$, where τa and τi are activation and inactivation time constants (ms), respectively, and A1, A2, and C are constants.

To characterize single-channel conductance properties, all-point histograms of T220A NaChBac single-channel activity were fit with a sum of two Gaussian functions, $fx=A_{1}\timese^{-0.5\timesx-\mu_{1}^{2}/\sigma_{1}^{2}}/\sigma_{1}\times\sqrt{2\pi}+A_{2}\timese^{-0.5\timesx-\mu_{2}^{2}/\sigma_{2}^{2}}/\sigma_{2}\times\sqrt{2\pi}+C$, where x is current (pA), µ and σ represent the mean and standard deviation of the closed and open state current (pA), A1 and A2 are the weights of the closed and open state Gaussian components, respectively, and C is baseline current. Open probability was calculated as PO = A2/(A2 +A1). The response to pressure, PO(x)–PO(0), where x stands for –10 or –30 mmHg, was obtained as the difference in PO values within the same trace. The single-channel closed and open times were calculated in QuB. Single channel time constants are expressed as means ± standard deviation (SD). Change from shear stress or pressure was considered statistically significant when p<0.05 for mechano-stimulus vs. control, as determined by a two-way ANOVA with Dunnett’s post-test.

### Single-channel data analysis and simulations

The analysis and simulations were done with the QuB program, the MLab edition (http://milesculabs.org/QuB.html). QuB was used to digitally low-pass filter the data at 0.5 kHz to eliminate a periodic artifact induced by the pressure clamp system (Figure 2—figure supplement 1G) and to extract (‘idealize’) the signal from the noisy data. QuB was further used to simulate the behavior of the tested NaChBac model and to calculate its properties: the voltage-activation curve at different pressures, the pressure-activation curve at different voltages, and the probability density function for closed and open dwell times, and to extract rate constants from single channel data, using the MIL algorithm that features a first-order approximation to correct for missed events (Qin et al., 1996).

### NaV channel model

To capture the basic properties of the NaChBac channel (homotetramer, inactivation removed), we used the simple linear kinetic scheme C1-C2-C3-C4-C5-O6. Each rate constant had the general expression k = k0 × exp(kv ×V+ kp×P), where V is membrane potential, P is patch pressure, k0 is a pre-exponential factor representing the value of the rate constant at zero voltage and pressure, and kv and kp are sensitivity factors for voltage and pressure, respectively. Lack of voltage or pressure dependence was encoded by setting kv or kp to zero. The rates along the activation pathway were in the expected 4:3:2:1 ratio (e.g. k23=2 × k45). The parameters of the model were tweaked by hand to match the macroscopic and single-channel data, collected within our unique experimental configuration defined above by the pipette geometry. First, we chose a set of k0 preexponential parameters for the C5-O6 transition, to match the observed PO at saturating voltages (at –20 mV). Then, we adjusted the kv exponential parameters that describe the voltage sensitivity of the C1 through C5 transitions, to match the normalized macroscopic activation curve under no-shear conditions. Next, we determined the statistical distribution (average and standard deviation) of the resting potential of the single-channel patched cells—to match the voltage-dependent PO curve—which is voltage-shifted and shallower relative to the macroscopic activation curve. To generate a PO curve that takes into account the scattered and non-zero resting potential, the PO value at each voltage point was obtained by numerically integrating over the Gaussian distribution describing the resting potential. Next, we adjusted the k0 preexponential parameters for the C1 through C5 transitions to approximately match the observed single-channel lifetimes. Finally, for the MSO model, we adjusted the kp exponential parameters describing the pressure sensitivity of the C5 to C6 transition, to match the PO curve under negative patch pressure. The same kp values were also used for the MSA model. The kinetic parameters used for the simulations shown in Figure 4B–D were the following: k0,activation = 800 s–1, k0,deactivation = 0.1 s–1, k0,opening = 70 s–1, k0,closing = 55 s–1, kv,activation = 0.055 V–1, kv,deactivation = -0.055 V–1, kp,activation/opening = -0.05 mmHg–1, and kp,deactivation/closing = -0.005 mmHg–1.
