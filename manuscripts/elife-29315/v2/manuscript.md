# Computer assisted detection of axonal bouton structural plasticity in in vivo time-lapse images

## Authors

- Rohan Gala<sup>1</sup> ([ORCID: 0000-0003-1872-0957](https://orcid.org/0000-0003-1872-0957))
- Daniel Lebrecht<sup>2</sup>
- Daniela A Sahlender<sup>4</sup> ([ORCID: 0000-0002-0510-9529](https://orcid.org/0000-0002-0510-9529))
- Anne Jorstad<sup>4</sup> ([ORCID: 0000-0002-6438-1979](https://orcid.org/0000-0002-6438-1979))
- Graham Knott<sup>4</sup> ([ORCID: 0000-0002-2956-9052](https://orcid.org/0000-0002-2956-9052))
- Anthony Holtmaat<sup>2</sup> ([ORCID: 0000-0002-7577-0769](https://orcid.org/0000-0002-7577-0769))
- Armen Stepanyants<sup>1</sup> ([ORCID: 0000-0002-9387-2320](https://orcid.org/0000-0002-9387-2320)) †

### Affiliations

1. Department of Physics and Center for Interdisciplinary Research on Complex Systems Northeastern University Boston United States
2. Department of Basic Neurosciences, Faculty of Medicine University of Geneva Geneva Switzerland
3. Lemanic Neuroscience Doctoral School Switzerland
4. Biological Electron Microscopy Facility, Centre of Electron Microscopy École Polytechnique Fédérale de Lausanne Lausanne Switzerland

† Corresponding author

## Abstract

The ability to measure minute structural changes in neural circuits is essential for long-term in vivo imaging studies. Here, we propose a methodology for detection and measurement of structural changes in axonal boutons imaged with time-lapse two-photon laser scanning microscopy (2PLSM). Correlative 2PLSM and 3D electron microscopy (EM) analysis, performed in mouse barrel cortex, showed that the proposed method has low fractions of false positive/negative bouton detections (2/0 out of 18), and that 2PLSM-based bouton weights are correlated with their volumes measured in EM (r = 0.93). Next, the method was applied to a set of axons imaged in quick succession to characterize measurement uncertainty. The results were used to construct a statistical model in which bouton addition, elimination, and size changes are described probabilistically, rather than being treated as deterministic events. Finally, we demonstrate that the model can be used to quantify significant structural changes in boutons in long-term imaging experiments.

## Introduction

The repertoire of synaptic connectivity within neuronal networks is immensely increased through the continuous formation and elimination of synapses (Chklovskii et al., 2004; Stepanyants et al., 2002). Indeed, in vivo imaging studies over the last 15 years have shown that synaptic structures remain dynamic throughout adulthood (Holtmaat and Svoboda, 2009; Trachtenberg et al., 2002). This structural plasticity, i.e. the appearance, disappearance, and the morphological modifications of synapses in the adult brain has been established as a fundamental underpinning of learning and experience-dependent changes in neuronal circuits (Holtmaat and Caroni, 2016; Holtmaat and Svoboda, 2009; Stepanyants and Chklovskii, 2005).

Synapses in the central nervous system are morphologically distinct structures, visible only in electron microscopy (EM). In light microscopy (LM) a synapse can be detected based on the presence of a swelling on the axon, referred to as bouton, or a protrusion from the dendrite, known as spine. In the cerebral cortex, the majority of excitatory synapses and a minority of inhibitory synapses occur on dendritic spines (Gray, 1959). Spines can easily be detected, hence most studies of structural plasticity have used manual or semi-automated tracking of these structures in time-lapse images to infer circuit changes (Holtmaat and Svoboda, 2009). Yet, studies relying on tracking of dendritic spines may not reveal the full extent of synaptic plasticity because synapses can also occur on dendritic shafts. On the other hand, a dendrite’s presynaptic apposition can be detected as an irregularity or swelling on the axon. Similar to dendritic spines, such axonal boutons have long since been recognized as sites of functional connections between neurons (Van Gehuchten, 1904). Therefore, the detection of these structures would provide a powerful means to analyze synaptic connectivity (Markram et al., 2015; Meyer et al., 2010)

Many EM studies have revealed a variety of presynaptic morphologies and the arrangements of vesicles, endoplasmic reticulum, and mitochondria therein (Harris and Weinberg, 2012). This is the only method capable of verifying that LM observations of axonal boutons do indeed correspond to synaptic contacts, but applying such a method every time is difficult across large volumes and impossible at more than one time point. The few real-time imaging studies of presynaptic plasticity in vivo used semi-automatic detection methods to track individual axonal boutons in LM time-lapse images (Chen et al., 2015; De Paola et al., 2006; Grillo et al., 2013; Holtmaat et al., 2009; Johnson et al., 2016; Keck et al., 2011; Majewska et al., 2006; Mostany et al., 2013; Qiao et al., 2016; Stettler et al., 2006; Yang et al., 2016). Visually isolated axons were segmented, and axonal boutons, as presumed synaptic contacts, were scored by virtue of their integrated fluorescence (De Paola et al., 2006; Grillo et al., 2013). Based on arbitrarily defined thresholds, boutons are usually scored in a binary fashion, i.e. present or absent. However, due to jitter in fluorescence caused by fluctuations in imaging conditions, binary scoring of boutons may lead to high false positive/negative rates.

Several computer-assisted methods aid axon segmentation (Acciai et al., 2016; Parekh and Ascoli, 2013) and bouton detection (Song et al., 2016) in sparsely labeled tissue, but many challenges remain. The most difficult challenges to overcome are due to the limited resolution of two-photon microscopy (mainly along the optical axis, z). For example, due to the high density of boutons on cortical axons, boutons often lie in close proximity to one another and can appear fused in microscopy images (Figure 1). In densely labeled tissue bouton detection is further confounded by the fact that axons can also appear fused to one another which locally increases the integrated fluorescence. Furthermore, spatially and temporally non-uniform expression levels and the variability in axon caliber complicate the tracking of boutons over time. Such complications lead to inconsistencies and bias in LM-based bouton detection methods. The bias will affect bouton density estimates, while the inconsistencies, combined with binary scoring of boutons, will lead to an apparent increase in the bouton turnover rate.

![Figure 1.](https://cdn.elifesciences.org/articles/29315/elife-29315-fig1-v2.jpg)

**Figure 1.:** (A) Maximum intensity xy projection of an image stack showing axons of fluorescently labeled neurons in superficial layers of mouse barrel cortex. High density of labeled axons makes it difficult to automatically detect boutons and track their structural changes over time. Scale bar is 20 μm. (B) A subset of labeled axons from the region outlined in (A). To improve visibility, image intensity beyond five voxels from the axon centerlines was set to zero. Bouton detection and bouton size measurement are confounded by large variations in fluorescence levels across axons. (C) Axons from (B) shown on the zx maximum intensity projection. Horizontal scale bars in (B) and (C) are 5 μm. Vertical scale bar in (C) is 15 μm. Lower resolution in z compared to xy is yet another challenge in bouton analyses. (D–F) Magnified views of the highlighted boutons from (B). Close proximity of boutons on an axon (D), large range of bouton sizes (E), and large range of bouton fluorescence levels (D–F), present additional obstacles to accurate bouton detection and measurement. Scale bar in (D–F) is 1.25 μm.

Here, we describe semi-automated methodology for bouton detection and tracking in images acquired by 2-photon laser scanning microscopy (2PLSM) in vivo. We validate the results of the method with correlative 3D EM of in vivo imaged axons, and by applying the detection method to images acquired under various conditions that mimic the variability in time-lapse imaging. We quantify variability in bouton detection and propose a statistical model to deal with the inherent uncertainties of this LM-based detection method.

## Results

### LM-based bouton detection and measurement of structural changes

Here, we describe and evaluate a heuristic strategy that utilizes axon traces to detect and quantify boutons in 2PLSM images taken through a cranial window in vivo. This procedure consists of the following major steps: (1) tracing axons in 3D, (2) optimization of traces, (3) generation of axon intensity profiles, (4) detection of putative boutons based on the profiles, (5) normalization of intensity profiles and calculation of bouton weights, and (6) matching putative boutons across time-lapse images.

Axons can be traced automatically or manually with various tools (Acciai et al., 2016; Parekh and Ascoli, 2013). In this study, high density of labeled axons (Figure 1A) precluded the possibility of automated tracing. Therefore, axons were traced manually by using NCTracer software (Chothani et al., 2011; Gala et al., 2014), and traces were optimized as described in Materials and methods. Following optimization, two intensity profiles were generated for each axon by convolving specifically designed filters with the image at all trace node positions and scaling the results to unit means. While various filters can be used to generate axon intensity profiles, in this study, we settled on the following two: (1) a modified, multi-scale Laplacian of Gaussian filter (LoGxy) to detect putative boutons and (2) a fixed size Gaussian filter (G) to provide an estimate of axon intensity in the regions devoid of boutons (see Materials and methods for details). In the following we will refer to such inter-bouton regions as axon shaft.

$$
LoG_{xy}(x,y,z|R_{xy},R_{z})=\frac{4e^{−(x^{2}+y^{2})/R_{xy}^{2}}}{\piR_{xy}^{4}}(1−\frac{x^{2}+y^{2}}{R_{xy}^{2}})\times\frac{e^{−z^{2}/R_{z}^{2}}}{\sqrt{\pi}R_{z}}G(x,y,z|R)=\frac{e^{−(x^{2}+y^{2}+z^{2})/R^{2}}}{(\pi)^{3/2}R^{3}}
$$

Figure 2A and B show that distinct putative boutons can be identified as peaks in the LoGxy profile plotted against node positions along the trace, $I^{LoG_{xy}}(s_{i})$. This is because the LoGxy filter is designed to sharpen boundaries between boutons by suppressing intensity in the regions immediately adjacent to boutons. In contrast, the G filter yields a smoother profile, $I^{G}(s_{i})$, which is not very useful for resolving putative boutons that are in close proximity (arrows in Figure 2C), but is well suited for estimating shaft intensity. For these reasons, LoGxy profiles were used to identify putative boutons, while G profiles were used to determine intensities of axon shafts.

![Figure 2.](https://cdn.elifesciences.org/articles/29315/elife-29315-fig2-v2.jpg)

**Figure 2.:** (A) Maximum intensity xy projection of an axon segment showing multiple putative boutons. Yellow line is the optimized trace of this axon. (B) Putative boutons visible in (A) correspond to peaks on the LoGxy intensity profile (black line). Foreground peaks (cyan lines) and local background (red line) are fitted to the intensity profile as described in the text. The overall fit (thick yellow line), which is the sum of foreground peaks and background, closely matches the intensity profile. (C) G intensity profile is obtained by sliding a fixed size Gaussian filter along the optimized trace. Small or closely positioned peaks cannot be resolved on the G profile (arrows). Peak amplitudes from the LoGxy profile and background from the G profile are used to define bouton weights.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/29315/elife-29315-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Five users traced the same set of 16 axon segments using manual tracing module of NCTracer software. Manual traces (colored lines) are shown superimposed on zx (top), yz (left), and xy (center) maximum intensity projection images of an axon segment. To improve visibility, image intensity beyond five voxels from the axon centerline was set to zero. While on the xy projection, manual traces closely match the underlying axon intensity, variability between traces becomes apparent by viewing the zx and yz projections. (B) User traces after optimization are virtually indistinguishable on all projections. (C) Axon intensity profiles can be obtained by sliding various filters along manual traces. Here, we show LoGxy intensity profiles for the five manual user traces. Note that slight tracing inaccuracies may lead to large variability in axon intensity profiles, e.g. absent peak in the User four trace profile (dashed line). (D) Inter-user variability in axon intensity profiles is virtually eliminated after trace optimization.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/29315/elife-29315-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Putative boutons were automatically detected based on manual traces of 5 users. Differences in user traces lead to variability in putative bouton detection. The fraction of inter-user conflicts is particularly high for low weight boutons. (B) Trace optimization reduces the fraction of inter-user conflicts. (C) Trace optimization also reduces inter-user bias and variability in bouton weight measurements. (D) Root mean square (RMS) weight difference, calculated for putative boutons detected on manual (red points) and optimized traces (blue points), shows that optimization reduces variability in the entire range of bouton weights.

To automatically detect putative boutons in an LoGxy profile we used an algorithm that is similar to the Backward-Stepwise Subset Selection method (Hastie et al., 2009). Here, a varying number of foreground peaks, $N_{f}$, and a constant number of background peaks, $N_{b}$, was fitted to $I^{LoG_{xy}}(s_{i})$ by minimizing the following objective function of peak positions, $\mu_{j}^{f}$and $\mu_{k}^{b}$, amplitudes, $a_{j}^{f}$and $a_{k}^{b}$, and widths, $\sigma_{j}^{f}$and $\sigma_{k}^{b}$ (see Materials and methods for details):

$$
min\frac{a_{j}^{f},\mu_{j}^{f},\sigma_{j}^{f}}{a_{k}^{b},\mu_{k}^{b},\sigma_{k}^{b}}⁡(\sumi(I^{LoG_{xy}}(s_{i})−\sumj=1N_{f}a_{j}^{f}e^{−\frac{(s_{i}−\mu_{j}^{f})^{2}}{2(\sigma_{j}^{f})^{2}}}−\sumk=1N_{b}a_{k}^{b}e^{−\frac{(s_{i}−\mu_{k}^{b})^{2}}{2(\sigma_{k}^{b})^{2}}})^{2})a_{j}^{f}\geq0;0.5\mum\leq\sigma_{j}^{f}\leq2.0\muma_{k}^{b}\geq0;\sigma_{k}^{b}\geq20\mum
$$

We note that, though profile background was fit with a sum of spatially distributed peak functions, constraints imposed on their widths ($\sigma_{k}^{b}\geq$ 20 μm) ensure that the fit varies slowly along the axon (red line in Figure 2B).

Following the detection of putative boutons, intensity of bouton $j$ was defined as the sum of the $j$-th foreground peak amplitude and background intensity at the peak location:

$$
I_{j}^{Bouton}=a_{j}^{f}+\sumk=1N_{b}a_{k}^{b}e^{−\frac{(\mu_{j}^{f}−\mu_{k}^{b})^{2}}{2(\sigma_{k}^{b})^{2}}}
$$

Shaft intensity was estimated from the G profile by incorporating information about the positions of detected putative boutons, Figure 2C. To that end, we initialized the above described peak detection algorithm with the foreground and background peaks detected on the LoGxy profile, but ran the algorithm on the G intensity profile. Shaft intensity for a given axon was defined as the fitted background intensity on the G profile, averaged over trace nodes,

$$
I_{i}^{Background}=\sumk=1N_{b}a_{k}^{b,G}e^{−\frac{(s_{i}−\mu_{k}^{b,G})^{2}}{2(\sigma_{k}^{b,G})^{2}}}I^{Shaft}=⟨I_{i}^{Background}⟩_{i}
$$

In this expression, index G in the superscripts of peak amplitudes, $a$, positions, μ, and widths, σ, was added to emphasize that these quantities are calculated based on the G intensity profile. We note that background intensity, $I_{i}^{Background}$, is designed to vary smoothly along the axon (red line in Figure 2C) and be independent of bouton density, providing a robust estimate of axon shaft intensity.

Our goal is to use intensity profiles to extract structural information related to the physical sizes of boutons. This task is hindered by the facts that axon intensity depends strongly on expression levels of fluorescent molecules (Figure 1A) and microscopy conditions. Therefore, to measure unbiased structural information, intensity profiles must be properly normalized. One may consider using median (or mean) profile intensity or local shaft intensity for normalization. However, these types of normalizations can lead to errors. For example, if density of boutons varies across axons, normalization with the median (or mean) may bias boutons on higher bouton density axons towards lower intensity values. Also, if density of boutons is sufficiently large, normalization with local shaft intensity can lead to variability as the latter cannot be measured reliably between closely positioned boutons.

Our heuristic normalization approach is based on the idea that by convolving the LoGxy or G filter with the image at a trace node position $s_{i}$ along axon $a$ in imaging session $t$, we obtain a quantity that is proportional to three factors: $M_{t}$, a factor related to imaging conditions [e.g. laser power, photomultiplier tube (PMT) voltage, and cranial window quality], $ρ_{a,t}$, volume density of fluorescent molecules, and $A_{a,t}(s_{i})$, a structural factor which has been linked to axon cross-section area (drawn perpendicular to the xy projection of the axon centerline) convolved with the microscope point-spread function (Song et al., 2016) and profile filter:

$$
I~_{a,t}^{LoG_{xy},G}(s_{i})=M_{t}ρ_{a,t}A_{a,t}^{LoG_{xy},G}(s_{i})
$$

In creating the LoGxy and G profiles (Figure 2) we rescale $I~_{a,t}^{LoG_{xy}}(s_{i})$ and $I~_{a,t}^{G}(s_{i})$ to unit means in order to minimize effects related to imaging conditions and expression levels, thus isolating structural information:

$$
I_{a,t}^{LoG_{xy},G}(s_{i})=\frac{I~_{a,t}^{LoG_{xy},G}(s_{i})}{⟨I~_{a,t}^{LoG_{xy},G}(s_{i})⟩_{i}}=\frac{A_{a,t}^{LoG_{xy},G}(s_{i})}{⟨A_{a,t}^{LoG_{xy},G}(s_{i})⟩_{i}}
$$

It may be tempting to use putative bouton intensity, $I_{j}^{Bouton}$ in Equation (3), which is detected based on $I_{a,t}^{LoG_{xy}}(s_{i})$ as proxy for bouton size. However, this may lead to bias as the denominators in Equation (6) depend strongly on bouton density. To address this issue, we use axon shaft intensity detected from G intensity profiles, $I^{Shaft}$ in Equation (4), for normalization. The resulting quantity, referred to as bouton weight, $w_{j}^{Bouton}$, conveys structural information, which is effectively independent of the above-mentioned bias,

$$
w_{j}^{Bouton}=\frac{I_{j}^{Bouton}}{I^{Shaft}}
$$

### Validation of LM-based bouton detection methodology with EM

Correlative light and electron microscopy (CLEM) was used to validate the described bouton detection procedure (Figure 3 and Figure 3—video 1). Four axon segments were selected for this analysis (Figure 3A). The axon segments were imaged in vivo with 2PLSM, the brain tissue was fixed shortly after, and subsequently imaged with EM (see Materials and methods for details). Putative boutons in the 2PLSM stack of images were detected and quantified as described above (Figure 3B). Axons in EM images were reconstructed in 3D (Figure 3C) and rendered in Blender software for further analysis.

![Figure 3.](https://cdn.elifesciences.org/articles/29315/elife-29315-fig3-v2.jpg)

**Figure 3.:** (A) Maximum intensity xy projection of an image stack used for CLEM analysis. White box demarcates the region imaged with EM. Colored lines are traces of four axon segments chosen for EM reconstruction. Scale bar is 10 μm. (B) Region outlined in (A) is shown at 4x magnification with background removed. (C) 3D EM reconstruction of the four axon segments shown in (B). Red areas mark PSDs, and blue volumes outline mitochondria. Most varicosities identified in EM are clearly visible in 2PLSM images (B). (D) Higher magnifications and different orientations of a subset of reconstructed varicosities shows that structural swellings on axons may or may not be associated with PSDs and/or contain mitochondria. Numbers in (B–D) enumerate distinct varicosities identified in EM.

Putative boutons detected in 2PLSM images could be unambiguously matched with varicosities identified in EM (Figure 3—video 1, asterisks in Figure 4A–D, and Table 1). We used positions of the centers of matched boutons to register LM traces and EM centerlines with an optimal linear transformation (Hastie et al., 2009). Average distance between the registered traces (Gala et al., 2014) was small, 0.34 ± 0.17 μm (mean ± s.d.), confirming that the same set of axons was reconstructed in LM and EM. A small discrepancy between registered traces may be attributed to non-linear distortion of tissue in the EM experiment and the relatively low z-resolution of LM. Overall, 16 boutons en passant and one bouton terminaux could be identified in EM. The bouton terminaux was detected with our method, but was excluded from further analysis because it is not located on the axon centerline. With the omission of this bouton, the LM-based procedure detected 18 putative boutons with 0 false negatives and two false positives, both of which were small (1.1 and 2.2 in weight, #18 and #19 in Table 1).

![Figure 4.](https://cdn.elifesciences.org/articles/29315/elife-29315-fig4-v2.jpg)

**Figure 4.:** (A–D) Top row: EM reconstructions of axons are shown next to the corresponding 2PLSM maximum intensity projections. Varicosities identified in EM are marked with grey asterisks, and putative boutons automatically detected based on the intensity profiles are marked with green asterisks. Second row: Normalized intensity profiles of the same axons plotted as functions of position along axon centerlines obtained in EM. Third row: z cross-section areas of axons, including (black) and excluding (blue) mitochondria, are well correlated with intensity profiles. These cross-sections are drawn perpendicular to the 2PLSM xy projections of the axon centerlines. Fourth row: Normal cross-section areas showing the extents of boutons (green) based on criteria described in Materials and methods. (E) Demarcated boutons shown in 3D (green). Bouton weights are highly correlated with their EM-based volumes that include (F) or exclude (G) mitochondrial volumes. Grey regions in (B) highlight two spurious peaks in the normalized intensity profile, one resulting from a close apposition of two axons and another caused by the presence of a terminal bouton. Such regions were annotated in 2PLSM images and were excluded from all analyses. In addition, bouton #7 (red box in B, F, and G) was excluded from the correlation analysis because it is directly adjacent to a branch point, which biases weight calculation.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/29315/elife-29315-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A–D) Comparison of axon intensity profiles obtained with different filters. Each profile is plotted as a function of position on axon trace obtained in LM. Top row: EM reconstructions and 2PLSM maximum intensity projections for the four axons included in CLEM analyses (same as shown in Figure 4). Rows 2–8 show intensity profiles of these axons generated by using raw voxel intensities along the trace, mean filters of box sizes 3 × 3 × 3 and 5 × 5 × 5, Gaussian filters [see Equation (1)] of sizes R = 1 and R = 2, and median filters of box sizes 3 × 3 × 3 and 5 × 5 × 5. Each profile was normalized by its median profile intensity. Row 9 shows multi-scale LoGxy profiles normalized by shaft intensities. In the absence of filtering, profiles appear jagged, which may lead to false positives in peak detection (arrows). On the other hand, large filters (5 × 5 × 5 and R = 2) may not resolve small boutons or closely positioned boutons (arrows). When the filter size is carefully tuned (3 × 3 × 3 and R = 1 in this case) profiles generated by various filters may appear similar to those obtained with the multi-scale LoGxy. (E) Bouton measurements based on these profiles were compared to bouton volumes measured in EM. LoGxy filter profile normalized with shaft intensity leads to both accurate bouton detection and highest degree of correlation between peak amplitudes on the profiles and bouton volumes.

**Table 1.**
 Comparison of LM-based and EM measurements.Bouton IDs match those in Figures 3 and 4. The probability that a putative bouton belongs to the category of LM boutons, $P(bouton|w)$ was calculated according to Equation (9) with $w_{threshold}$ = 2.0. Bouton #8 (grey) was excluded from the analyses as it is a terminal bouton. Hyphens indicate that boutons, mitochondria, or PSDs were not detected in EM.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2">2PLSM measurements</th>
      <th colspan="3">EM measurements</th>
    </tr>
    <tr>
      <th></th>
      <th>Bouton ID</th>
      <th>Putative bouton weight, w</th>
      <th>P(bouton | w)</th>
      <th>Bouton volume [μm3]</th>
      <th>Mitochondria volume [μm3]</th>
      <th>PSD surface area [μm2]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">Axon 1</td>
      <td>1</td>
      <td>13.5</td>
      <td>1.00</td>
      <td>0.919</td>
      <td>0.189</td>
      <td>0.666</td>
    </tr>
    <tr>
      <td>2</td>
      <td>10.8</td>
      <td>1.00</td>
      <td>0.779</td>
      <td>0.170</td>
      <td>0.595</td>
    </tr>
    <tr>
      <td>3</td>
      <td>1.98</td>
      <td>0.48</td>
      <td>0.093</td>
      <td>-</td>
      <td>0.371</td>
    </tr>
    <tr>
      <td>4</td>
      <td>10.1</td>
      <td>1.00</td>
      <td>0.998</td>
      <td>0.225</td>
      <td>1.92</td>
    </tr>
    <tr>
      <td>5</td>
      <td>8.65</td>
      <td>1.00</td>
      <td>0.669</td>
      <td>0.139</td>
      <td>1.83</td>
    </tr>
    <tr>
      <td>6</td>
      <td>6.25</td>
      <td>1.00</td>
      <td>0.219</td>
      <td>0.043</td>
      <td>0.138</td>
    </tr>
    <tr>
      <td rowspan="3">Axon 2</td>
      <td>7</td>
      <td>3.63</td>
      <td>0.93</td>
      <td>0.483</td>
      <td>0.111</td>
      <td>0.612</td>
    </tr>
    <tr>
      <td>8</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>0.574</td>
      <td>-</td>
      <td>2.75</td>
    </tr>
    <tr>
      <td>9</td>
      <td>5.57</td>
      <td>1.00</td>
      <td>0.372</td>
      <td>0.027</td>
      <td>1.28</td>
    </tr>
    <tr>
      <td rowspan="4">Axon 3</td>
      <td>10</td>
      <td>9.54</td>
      <td>1.00</td>
      <td>0.632</td>
      <td>0.182</td>
      <td>0.645</td>
    </tr>
    <tr>
      <td>11</td>
      <td>1.99</td>
      <td>0.49</td>
      <td>0.102</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>12</td>
      <td>8.51</td>
      <td>1.00</td>
      <td>0.456</td>
      <td>-</td>
      <td>1.23</td>
    </tr>
    <tr>
      <td>13</td>
      <td>10.8</td>
      <td>1.00</td>
      <td>0.704</td>
      <td>0.161</td>
      <td>1.49</td>
    </tr>
    <tr>
      <td rowspan="6">Axon 4</td>
      <td>14</td>
      <td>5.80</td>
      <td>1.00</td>
      <td>0.308</td>
      <td>-</td>
      <td>0.867</td>
    </tr>
    <tr>
      <td>15</td>
      <td>4.23</td>
      <td>1.00</td>
      <td>0.198</td>
      <td>-</td>
      <td>0.686</td>
    </tr>
    <tr>
      <td>16</td>
      <td>5.96</td>
      <td>1.00</td>
      <td>0.229</td>
      <td>0.027</td>
      <td>0.402</td>
    </tr>
    <tr>
      <td>17</td>
      <td>2.85</td>
      <td>0.93</td>
      <td>0.140</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>18</td>
      <td>1.14</td>
      <td>0.01</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>19</td>
      <td>2.19</td>
      <td>0.65</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

We tested the idea that 2PLSM intensity is correlated to the area of axon cross-section drawn perpendicular to the xy projection of axon centerline (Song et al., 2016). We refer to such cross-sections as z cross-sections (third row in Figure 4A–D) to distinguish them from normal cross-sections, which are drawn perpendicular to the axon centerline. For this, we calculated the normalized axon intensity profile, $I_{a,t}^{LoG_{xy}}(s_{i})/I^{Shaft}$, and compared it to EM z cross-section areas including and excluding mitochondrial z cross-section areas. Both z cross-section areas appear to be well correlated with normalized intensity profiles. However, it is clear from visual inspection that the normalized intensity profiles do not resolve small changes in axon cross-section, which is the result of limited resolution of 2PLSM.

To examine the extent to which LM-based measurements provide information about bouton size, we plotted bouton weight against bouton volumes including (Figure 4F) and excluding (Figure 4G) mitochondrial volume. Normal axon cross-sections were used to identify bouton boundaries and calculate bouton volume as described in Materials and methods (fourth row in Figure 4A–D and Figure 4E). Bouton #7 (red box in Figure 4B) was excluded from these analyses, because it is bounded on one side by the terminal bouton branch which biases weight measurement. The results show high degree of correlation in both cases (Pearson’s r = 0.93), supporting the idea that LM-based measurements can be used to quantify volumes of even very small varicosities (#3, 0.093 μm3). The results also provide support for the choice of filters, Equation (1), and the normalization procedure, Equation (7), showing that the proposed method could overcome axon-specific differences in the expression levels and bouton density, capturing meaningful fine-scale structural information.

It is important to emphasize that we did not attempt to find the best procedure for fitting the EM data. It is possible that some other combinations of filter types, normalizations, and parameters would lead to marginally better correlations. However, due to the small sample size, this would likely be a case of over-fitting. The described procedure was designed based on theoretical considerations, and the parameters were chosen based on the observed range of bouton sizes (see Materials and methods). Nonetheless, we explored alternative filtering and normalization strategies. Figure 4—figure supplement 1 shows profiles derived from raw voxel intensities, and profiles obtained with mean, Gaussian, and median filters of different but fixed sizes. Each of these profiles was normalized by its median value. The figure makes it clear that some amount of filtering benefits bouton detection, as jagged unfiltered profiles can lead to false positives. Similarly, relatively large filters of fixed size (e.g. 5 × 5 × 5 and R = 2) are not well suited for bouton detection as they often suppress intensities of small boutons and merge closely positioned boutons. When the filter size is carefully tuned (3 × 3 × 3 and R = 1), resulting profiles can look similar to those of multi-scale LoGxy, although higher baselines in these profiles can make peak detection more challenging. Furthermore, we examined the combined effect of filtering and normalization on bouton measurement by comparing the amplitudes of profile peaks to corresponding bouton volumes. Multi-scale LoGxy profile normalized with shaft intensity as described above leads to the highest correlation compared to the best considered alternatives (Figure 4—figure supplement 1E).

### Effects of imaging conditions on bouton analysis

Next, we sought to evaluate the effects of various imaging conditions on bouton detection and measurement. To that end, a set of fluorescently labeled axons was imaged seven times in a span of 80 min with different laser power (LP) and PMT voltage (see inset in Figure 5A). In addition, in condition E, a thin layer of agarose was applied to the cranial window to mimic deterioration of window quality which often accompanies long-term imaging experiments. In the following, we assume that there is negligible structural plasticity of boutons throughout the duration of this short-term imaging experiment, and therefore differences in bouton measurements can be attributed to the effects of imaging conditions and measurement uncertainties. The inset in Figure 5B shows the maximum intensity projections of an axon segment imaged in all seven conditions. This inset illustrates that increasing (decreasing) LP and/or PMT voltage results in an overall increase (decrease) in intensity, and therefore proper normalization procedure must be used to minimize the effects of such changes on bouton measurements.

![Figure 5.](https://cdn.elifesciences.org/articles/29315/elife-29315-fig5-v2.jpg)

**Figure 5.:** The same set of axons was imaged 7 times within 80 min with various microscope settings and cranial window conditions (inset in A). Putative boutons detected based on the first imaging session (condition A) were chosen to be the gold standard. Precision (A) and recall (B) in bouton detection were measured under the remaining conditions, B-G. Both precision and recall increase with bouton weight. While for very small boutons ($w$ < 2.0, dashed line) detection is unreliable, agreement with the gold standard is achieved across all imaging conditions in 95% of boutons with weights greater than 2.0. Numbers of boutons in the gold standard are indicated next to the data points in (A). Inset in (B) shows an example of one axon segment imaged in conditions A-G. (C) Bouton weights under different imaging conditions are plotted against the gold standard weight. Best fit lines show no significant bias for conditions B and C, however small, but significant reduction in mean bouton weight was observed in the remaining four conditions (all p < 0.03, two-sample t-test). Abbreviations used in the inset of A: LP is laser power in mW, PMT denotes photomultiplier tube voltage in Volts, and WC is cranial window condition, where ‘n’ stands for normal and ‘a’ indicates presence of a thin layer of agarose. Color code used in (A–C) is defined by the inset table in (A). (D) CDFs for differences in bouton weights across imaging conditions. Data from all conditions were pooled. Different lines show CDFs for various intervals of mean bouton weight. (E) Variance in bouton weight difference increases linearly with mean bouton weight (χ2 linear regression with $var(Δw)=\alpha⟨w⟩$, p = 0.33, α = 0.24 ± 0.01, mean ± s.d.). Error-bars indicate standard deviations obtained with bootstrap sampling with replacement. (F) Red line shows the distribution of true bouton weight for a putative bouton of measured weight $w$ = 1.5. Area under the curve to the right of $w_{threshold}$ = 2.0 gives $P(bouton|w)$ = 0.12. Large putative boutons (e.g. blue curve, $w$ = 3.0) have high probability of being LM boutons.

Putative boutons on 16 axon segments were detected in all conditions independently (400 putative boutons per condition on average). Custom software was used to match the same putative boutons across conditions. Putative boutons detected in condition A were chosen to be the gold standard, and precision/recall in bouton detection in the remaining conditions B-G were evaluated as functions of bouton weight (Figure 5A and B). The results show that for 95% of putative boutons of weight $w$ > 2.0 both precision and recall equal one in all conditions. This number of unambiguously detected putative boutons goes up to 99% for $w$ > 2.5 and 100% for $w$ > 3.1. For reference, $w$ = 2.0 corresponds to the weights of the two smallest varicosities identified in EM (#3 and #11 in Table 1), and the weight of the next smallest bouton (#17) is $w$ = 2.8. Therefore, all but very small boutons can be detected with our method with high confidence.

To examine the effects of imaging conditions on bouton weight, we tested a subset of 290 putative boutons that were detected and matched across all seven experiments. Figure 5C shows bouton weights in conditions B-G plotted against the corresponding weights in condition A. Although axon intensities in conditions B and C are drastically different from A (see inset in Figure 5B), the normalization procedure could correct for these differences (blue and red lines in Figure 5C). However, small (≈ 7%) but significant bias was present in conditions D-G, which may have been caused by bleaching due to prolonged imaging. Figure 5C also reveals a considerable amount of variability in weight measurements. This variability, reflected in the R2 coefficients, was similar across all comparisons, including the imaging experiments performed under the same conditions (e.g. A and G, cyan points). Therefore, bouton weight measurements are accompanied with uncertainty which is inherent to the LM-based methodology. This uncertainty cannot be eliminated entirely, and hence, it must be explicitly incorporated into models that derive biological information from bouton measurements.

### Statistical framework for the analysis of structural plasticity of boutons

To model the variability observed in Figure 5C, we examined bouton weight differences for all pairs of imaging conditions, $Δw=w_{1}−w_{2}$. Because such changes clearly depend on bouton size, we looked at the statistics of $Δw$ in various intervals of average bouton weight, $⟨w⟩=(w_{1}+w_{2})/2$. Figure 5D shows the cumulative distribution functions (CDFs) of bouton weight differences in eight intervals of $⟨w⟩$. These distributions are not significantly different from Gaussian distributions, and their variances are roughly proportional to the mean bouton weights, $var(Δw)=\alpha⟨w⟩$, Figure 5E. Therefore, all CDFs shown in Figure 5D could be standardized by rescaling the weight differences as $Δw/\sqrt{\alpha⟨w⟩}$, leading to distributions that are statistically indistinguishable from the Standard Normal CDF (all p > 0.05, one-sample KS test).

Based on this result, we propose a statistical model in which measured bouton weight, $w$, is the sum of the true weight, $w_{0}$, and a noise term, δ. The latter is randomly drawn from a Gaussian distribution with variance proportional to the measured weight, $var(\delta)=\frac{1}{2}\alphaw$:

$$
w=w_{0}+\delta;P(\delta)=\frac{e^{−\delta^{2}/\delta^{2}\alphaw\alphaw}}{\sqrt{\pi\alphaw}}
$$

Equation (8) quantifies uncertainties in bouton weight measurements, making it possible to define bouton presence probabilistically. To that end, we impose a threshold on true bouton weight, $w_{threshold}$, and refer to putative boutons with $w_{0}$ > $w_{threshold}$, as LM (light microscopy) boutons. In the following we set $w_{threshold}$ = 2.0, which is motivated by several considerations. First, this value equals twice the average normalized axon shaft intensity. Therefore, by using $w_{threshold}$ = 2.0 we are only including peaks that are substantially larger than the axon shaft intensity. Second, $w$ = 2.0 corresponds to the weights of the two smallest varicosities detected in EM (#3 and #11 in Table 1). Finally, detection of putative boutons becomes unreliable for $w$ < 2.0 (Figure 5A and B). We note that as an alternative to choosing a single threshold value to define LM boutons, one could vary the threshold in a certain range (e.g. 1–3) and report results as functions of this parameter.

The probability that a putative bouton of measured weight $w$ belongs to the category of LM boutons, $P(bouton|w)$, can be calculated based on the noise model of Equation (8):

$$
P(bouton|w)=\frac{1}{2}(1+erf(\frac{w−w_{threshold}}{\sqrt{\alphaw}}))
$$

In this expression, $erf$ denotes the error function. Shaded regions in Figure 5F illustrate these probabilities for two putative boutons of measured weights $w$ = 1.5 and $w$ = 3.0. Note that even when $w$ is less than $w_{threshold}$, there is a non-zero probability that the detected peak is an LM bouton. For large $w$ (e.g. greater than 3), this probability approaches unity, and the LM bouton definition becomes virtually deterministic.

LM bouton definition can be used to calculate the probabilities of bouton addition, elimination, potentiation, and depression based on the measured weights in two imaging sessions (initial and final), $w_{i}$ and $w_{f}$:

$$
P(added|w_{i}→w_{f})=(1−P(bouton|w_{i}))\timesP(bouton|w_{f})P(eliminated|w_{i}→w_{f})=P(bouton|w_{i})\times(1−P(bouton|w_{f}))P(potentiated|w_{i}→w_{f})=P(bouton|w_{i})\timesP(bouton|w_{f})\times\frac{1}{2}(1+erf(\frac{w_{f}−w_{i}}{\sqrt{\alpha(w_{i}+w_{f})}}))P(depressed|w_{i}→w_{f})=P(bouton|w_{i})\timesP(bouton|w_{f})\times\frac{1}{2}(1+erf(\frac{w_{i}−w_{f}}{\sqrt{\alpha(w_{i}+w_{f})}}))
$$

We would like to clarify that LM boutons may or may not correspond to varicosities seen in EM (Table 1), and the latter may not always be associated with postsynaptic densities (PSDs) and, thus, functional synapses (Shepherd and Harris, 1998). Therefore, the relationship between an LM bouton and a synapse is not deterministic and is likely to contain false-positives and false-negatives. However, the number of such errors is expected to decrease with increasing $w$. For example, Table 1 shows that all LM boutons of $w$ > 2.2 correspond to EM varicosities, and all LM boutons of $w$ > 2.9 are varicosities associated with PSDs.

### Bouton changes can be resolved despite the uncertainty in measurements

Next, we set out to determine if the above described bouton detection procedure can be used to identify significant structural changes in long-term, in vivo imaging experiments. To that end, axons of GFP labeled neurons were imaged in superficial layers of barrel cortex in five mice. Imaging was performed at 4 day intervals over a 24 day period (seven imaging sessions). On average, 968 bouton sites were detected on 20 axon segments in each animal and imaging session. These sites were tracked over the duration of the experiment (Figure 6—figure supplement 1) to quantify bouton addition, elimination, and weight changes as compared to the initial state of the circuit. The short-term imaging experiment of Figure 5 was used as control. Here, conditions B-G were compared to condition A, and the results were pooled.

Figure 6A shows the fraction of added LM boutons over time, as compared to the first imaging session. Specifically, we only consider significant bouton addition events, i.e. those for which the probability of addition according to Equation (10) is greater than 0.95. Analogous plots for the fractions of significant bouton eliminations and significant bouton weight changes (potentiation and depression combined) are shown in Figure 6B and C respectively. As was expected, the fractions of significant changes in the short-term imaging experiment (red points in Figure 6) are at the chance levels (dashed red lines). The latter was obtained with a bootstrap procedure in which the weights of individual boutons were independently shuffled across conditions. In contrast, in the long-term imaging experiment, the fractions of significant bouton additions, eliminations, and weight changes are significantly larger than chance already by the second imaging session (after 4 days), and these fractions continue to increase with time, consistent with the idea of gradual modification of the circuit. These results illustrate that the described methodology can be used to quantify circuit changes, despite the numerous challenges associated with long-term, in vivo imaging experiments.

![Figure 6.](https://cdn.elifesciences.org/articles/29315/elife-29315-fig6-v2.jpg)

**Figure 6.:** (A) Fraction of boutons that are absent on day 0 and are present at a later time with joint probability of 0.95 or greater (significant bouton addition). Red point (error-bars are too small to be visible) shows this fraction in images acquired within 80 min (conditions A-G). Black points show the results for a long-term imaging experiment. Statistically significant fraction of added boutons is detected after 4 days (interval between imaging sessions), and this fraction grows with time, consistent with the idea of gradual modification of the initial circuit. Similar trends were observed for the fractions of significant bouton eliminations (B) and significant bouton weight changes. Dashed red lines in (A–C) indicate baseline circuit changes expected from the statistical model. Error-bars indicate standard deviations based on Poisson statistics.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/29315/elife-29315-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A). xy projection of an axon segment that was imaged at 4 day intervals over a period of 68 days. Image intensity in each session is normalized independently as described for intensity profiles. Colored lines link corresponding putative boutons. These lines do not always run in parallel due to small rotations of the brain, nonlinear tissue distortions, and movements of boutons. (B). Normalized and aligned intensity profiles of the axon from A (see Materials and methods for details). Arrows indicate two locations on the axon where a bouton present on day 0 was eliminated after few imaging sessions.

## Discussion

Detection of structural changes in boutons is hindered by various technical challenges and fundamental limitations of light microscopy. Unfortunately, any uncertainty that enters the analysis of long-term in vivo imaging data manifests itself as spurious structural plasticity. Therefore, it is important to account for all sources of errors, minimize their effect, and incorporate the residual uncertainty into the interpretation of results. Below, we describe various sources of errors affecting bouton measurements.

First, fluorescence based measurements provide only indirect evidence of bouton size. Therefore, such measurements need to be validated by showing that they are informative of bouton structures. In this study, we used CLEM to show that bouton weight, defined based on 2PLSM data, is well correlated with bouton volume (Figure 4F and G). Second, variability in expression levels of fluorescent proteins across axons and within axons over time makes it difficult to compare boutons on different axons and to identify true structural changes. Here, these problems were mitigated by a specifically designed normalization procedure (Figure 2), which was verified with CLEM (Figure 4) and was tested in the short-term imaging experiment (Figure 5A–C). Third, because the resolution of 2PLSM (≈ 0.3 µm in xy) is not much smaller than bouton size (≈ 1 µm for small boutons in Figure 3), there are inherent uncertainties in detection of small boutons, differentiation of closely positioned boutons, and measurement of bouton size changes. These uncertainties of the imaging method cannot be eliminated, and, therefore, they must be modeled to ensure that bouton measurements are interpreted correctly (Figure 5D–F).

Many other technical issues can add to the uncertainty and introduce bias in bouton measurements. For example, deterioration of cranial window quality with time, deformation of brain tissue, small changes in brain orientation relative to the microscope, and slight movement of boutons along axons can lead to the perception of increased plasticity. In contrast, limited temporal resolution of long-term imaging experiments, typically few days between imaging sessions, can lead to an underestimate of plasticity, as changes that occur between imaging sessions remain unaccounted. Finally, uncertainty can arise from the computational method used to detect boutons. Figure 2—figure supplement 2D shows that computational uncertainty of the method described in this study is small and can be ignored considering contributions from other sources (Figure 5C).

It is important to emphasize that not every putative bouton detected in LM will correspond to a varicosity if imaged with EM. This is particularly so for very small putative boutons ($w$ < 2.0, bouton volume < 0.1 μm3) which can result from noise in fluorescence or inhomogeneity in labeling. In the absence of a reliable synaptic marker, the only reasonable way to eliminate such functionally irrelevant putative boutons is by imposing a threshold on bouton weight. In this study, we refer to putative boutons whose true weight exceeds the threshold as LM boutons and suggest setting this threshold at 2.0 based on CLEM and short-term imaging experiments. In practice, one may vary the threshold in a small range to ensure that specific conclusions are robust to the choice of this parameter.

Using a threshold to define an LM bouton as an all-or-none entity may impose a bias since the true bouton weight is unknown due to measurement uncertainty. The problem is exacerbated by the unimodal shape of bouton weight distributions (see Figure 2—figure supplement 2B), because of which a large fraction of weights will lie within the range of uncertainty around the threshold, regardless of its value. Such ambiguous boutons can either be discarded, which may bias biological interpretation, or, otherwise, they must be treated probabilistically. For example, probabilistic description is essential for calculation of the expected number of LM boutons. Simply counting the number of above threshold weights would result in an underestimate as bouton weight distribution is monotonically decreasing. Similar considerations apply to calculations of expected numbers of added, eliminated, potentiated, and depressed boutons. As most bouton structures are stable and do not change substantially over days-to-weeks, their weight changes often lie within the range of measurement uncertainty and must also be described probabilistically. Furthermore, probabilistic description is necessary for calculation of error-bars and for establishing statistical significance of results. To illustrate the feasibility of this approach, we applied it to a dataset of 4840 bouton sites tracked over 24 days. Figure 6 shows that statistically significant changes in LM boutons can be detected in long-term imaging experiments. It remains to be seen if the detected changes are informative of circuit alterations that subserve the many functions of the brain.

## Materials and methods

### In vivo imaging

All experiments were performed according to the guidelines of the Swiss Federal Act on Animal Protection and Swiss Animal Protection Ordinance. The ethics committee of the University of Geneva and the Cantonal Veterinary Office of Geneva, Switzerland (approval code GE/61/17) approved all experiments.

For development of the detection methodology we used data from mice that had been repeatedly imaged as part of a larger optical micro-stimulation and behavioral study (not yet published). Only the methodology that is relevant for the present study will be mentioned. Adeno-associated viral (AAV) vectors encoding floxed GFP (AAV2/9.CAG.flex.eGFP.WPRE.bGH2 [Upen]) were co-injected with an AAV vector encoding Cre (AAV2/9.hSynapsin.hGHintron.GFP-Cre.WPRE.SV40 [Upen]) at a ratio of 0.15 × 109: 1 (genome copies: genome copies). This produced an average of about 150 GFP-expressing cells per animal, mostly in L2/3 and L5 of the barrel cortex. We exclusively imaged the processes of these neurons in the upper layers of the cortex. Hence, the source of the fluorescent signal in the green channel is dominated by cytosolic GFP.

Following the AAV injection, we implanted a 3 mm diameter glass window over the barrel cortex as previously described (Holtmaat et al., 2009). Imaging experiments were started 6 weeks after the virus injection. Imaging was performed under anaesthesia (0.5–1.5% isoflurane). A custom-built alignment system was used to ensure identical positioning of the mouse’s cranial window at different time points, and to avoid rotations relative to the axial dimension of the objective. The system was based on aligning a beam reflected by the cranial window through two apertures, which uniquely determines a line in three spatial dimensions. The apertures and the laser position were constant, and the only free variables were the cranial window position and rotation (i.e., the x, y, and z-positions, as well as the row and pitch needed to be identical between sessions to satisfy the passage of light through the two apertures). We used a custom built 2PLSM (Janelia Research Campus, model Non-MIMMS in vivo microscope) to acquire in vivo anatomical images of the anesthetized animals through the cranial window. We used the ScanImage software (Janelia Research Campus, Vidrio Technologies) (Pologruto et al., 2003) to record the 2PLSM images, and additional custom software to align anatomical structures present on the central image stack by using a red-green overlay between current and past images.

For imaging we used a 20x water immersion objective (NA 0.95, XLUMPlanFI, Olympus, Japan). Images were acquired at a voxel volume of ≈ 0.13 × 0.26 × 0.8 μm3 (x × y × z). We binned the data in the x dimension to generate isometric voxels in x and y for all analyses. The voxel dwell time was 0.8 μs for the full resolution images (and thus twice as high after 2x binning of the x dimension). Each ROI comprised an image stack of ≈ 270 × 270 × 250 μm3. As the imaging light source we used a Ti:sapphire femtosecond pulsed laser (Chameleon ultra II, Coherent) that was lasing at 1010 nm. Emitted fluorescence light was split into two channels using a dichroic mirror (Semrock, FF735-Di01−35.5 × 49.0) and two bandpass filters (red channel, Semrock FF01-607/70; green channel, Semrock FF01-530/70). Each channel was equipped with a PMT (red channel, Hamamatsu R3896; green channel, Hamamatsu H10770PA-40SEL). Images were analyzed only in the green channel.

### Correlative 3D EM

Electron microscopy was carried out on the region outlined in Figure 3A using a previously described method (Maco et al., 2014; Maco et al., 2013). An image of the blood vessel pattern below the cranial window was taken immediately after the last 2PLSM imaging session. The anesthetized animal was then chemically fixed by perfusing, via the heart, 10 ml of isotonic PBS immediately followed by 200 ml of 2.5% glutaraldehyde and 2% paraformaldehyde in phosphate buffer (0.1 M, pH 7.4). Two hours later, the brain was removed and 60-μm-vibratome sections cut from the imaged region, tangential to the cortical surface. The region containing the imaged axons was located in these sections by matching the pattern of blood vessels seen in the first 2–3 sections with the image of the brain’s surface taken prior to the perfusion. The 2-photon laser was then used to burn lines into the fixed section around the region of interest. The laser was tuned to λ = 850 nm with a power of ~300 mW at the back focal plane of the objective. A rectangle of ~25 μm x 25 μm was burnt around the ROI using the line scan mode (2 ms/line). This shape acts as a fiducial mark that can be seen after the tissue has been stained, and resin embedded, ready for election microscopy. This section was then washed in sodium cacodylate buffer (0.1 M, pH 7.4) 5 × 3 min, postfixed and stained in reduced osmium (1.5% potassium ferrocyanide with 1% osmium tetroxide in 0.1 M sodium cacodylate buffer) for 40 min, followed by another 40 min incubation with 1% osmium tetroxide in the same buffer, and finally for 40 min with 1% aqueous uranyl acetate. Next, the section was dehydrated in a series of increasing concentrations of alcohol, then infiltrated in 100% Durcupan resin, and flat embedded between two glass slides and placed in a 60°C oven for 24 hr.

A small piece of the section (2 mm x 2 mm), containing the laser marked region, was trimmed from the rest of the section and glued onto a slab of blank resin, keeping the region of interest closest to the surface. This block was then trimmed in the ultramicrotome, using glass knives, so that the laser marks were within 5 μm of its surface, and less than 2 μm from one edge. The block was then mounted on a 45° aluminum stub, using conductive carbon paint, so that this edge was uppermost. It was then sputter coated with a 30 nm thick layer of gold. The sample was then placed in the focused ion beam scanning electron microscope chamber (FIBSEM; Zeiss NVision 40, Zeiss SMT, Germany) and orientated so that the ion beam could mill parallel to the laser marks, and therefore parallel to the 2PLSM plane of focus. The sample was imaged with an electron beam of 1.7 kV and a probe current of 1.1 nA using the back-scattered electron detector (ESB). Images with a pixel size of 6 nm were collected with a dwell time of 12 μs per pixel. The ion beam removed 12 nm of resin after each image, using a current of 700 pA, with an energy of 30 kV.

The serial electron micrographs were aligned in FIJI (http://fiji.sc; Schindelin et al., 2012) and the structures of interest segmented in the TrakEM2 part of the software (Cardona et al., 2012). Models were then exported to the Blender software (Blender Foundation, Amsterdam; http://www.blender.org), and the NeuroMorph toolset (http://neuromorph.epfl.ch; Jorstad et al., 2015) was used to measure axon cross-section areas, bouton and mitochondrial volumes, and PSD surface areas. The beginning and end of each bouton were defined, using the centerline processing tool, as the points along the axon where its normal cross-section area changed by more than 30% within a distance of 0.2 μm. The boutons were then delineated and their volumes calculated in the measurement tool (fourth row in Figure 4A–D and Figure 4E).

### Trace optimization

Figure 2—figure supplement 1A shows three maximum intensity projection views of an axon segment, which was traced independently by five users. Inter-user trace variability, which is usually more pronounced along the z-dimension (optical axis), can hinder bouton detection and measurement. Therefore, it is essential to optimize the layout of manual traces, ensuring that they accurately follow axon centerlines in the underlying image.

In this study, we used the optimization algorithm described in (Chothani et al., 2011). In this version of the algorithm, positions of trace nodes $r_{k}=(x_{k},y_{k},z_{k})^{T}$ are updated to optimize a fitness function, which includes intensity integrated along the trace and a regularizing constraint on the positions of neighboring trace nodes:

$$
ℱ({r_{k}})=\sumk(\frac{1}{\lambda}\summI(l_{m})\frac{e^{\frac{−‖r_{k}−l_{m}‖^{2}}{2R^{2}}}}{(2\pi)^{3/2}R^{3}}(1−\frac{2}{3}\frac{‖r_{k}‖^{2}}{R^{2}})−\frac{\alpha\lambda}{2}\sumk^{′}‖r_{k}−r_{k^{′}}‖^{2})
$$

Here, vectors $l_{m}$ denote the positions of voxel centers in the image stack, index $k^{′}$ enumerates the neighbors of node $k$, parameter λ denotes the average density of nodes in the trace (number of nodes per voxel), and Lagrange multiplier α > 0 controls the stiffness of the trace. The first term in this expression represents convolution of the image with the Laplacian of Gaussian filter of size R, and due to the fast decay of the Gaussian factor, summation in this term can be restricted to a small number of voxels in the vicinity of the trace. The following parameter values were used to produce the results of this study. R was set to three voxels (roughly equal to axon diameter in the images), λ was set to 0.5, and α equaled 0.001. The fitness function was maximized with Newton’s method as previously described (Gala et al., 2014). Trace node positions were synchronously updated at every iteration step, and optimization terminated when the relative change in $ℱ$ fell below 10−6.

Results of this optimization procedure (Figure 2—figure supplement 1B) show marked improvement over manual traces. The optimized traces are smoother, closer to one another in z, and follow the underlying axon intensity in the image more accurately. Following optimization, all traces were subdivided to a higher density of nodes, λ = 4.

### Generation of axon intensity profiles

Parameters of filters used to generate the axon intensity profiles, Equation (1), were chosen in the following way. The xy size of the multi-scale LoGxy filter was chosen to span bouton sizes observed in 2PLSM images, Rxy ∈ [1.5, 3.0] voxels (0.39 μm to 0.78 μm). Since the observed bouton size in the z dimension is dominated by the point spread function of the microscope, a single size was chosen for the z component of the filter, Rz = 2 voxels (1.6 μm). Upon convolution with the image, this multi-scale filter returns the maximum intensity calculated over the specified range of sizes. The Gaussian filter, G, was chosen to have a fixed size of R = 2 voxels in all three dimensions. This size was selected to be roughly equal to the typical axon shaft radius observed in the images (Figure 2—figure supplement 1A).

Figure 2—figure supplement 1C shows LoGxy profiles for the five manual traces from Figure 2—figure supplement 1A. Small differences in the layout of manual traces can lead to significant variability in intensity profiles, which is undesirable. Trace optimization reduces this variability to an extent undetectable by visual inspection, Figure 2—figure supplement 1D.

### Detection of putative boutons

Peak detection algorithm, Equation (2), was initialized with a number of foreground peaks, $N_{f}=⌈L/0.5\mum⌉$, which is much larger than the expected number of putative boutons. In this expression, $⌈⌉$ denotes the ceiling function and $L$ is the trace length in micrometers. The number of background peaks, $N_{b}=⌈L/25\mum⌉$, was determined based on the observed spatial scale of background variability. The peaks were initially distributed uniformly along the entire length of the trace. Both, Gaussian and Lorentzian peak functions were tested, but only the former was used in this study as it provided a better fit to intensity profiles as judged by the value of the objective function.

The objective function was minimized with the gradient descent method. Gradient steps were taken simultaneously along the $\mu_{j}^{f}$, $\mu_{k}^{b}$, $a_{j}^{f}$, $a_{k}^{b}$, $\sigma_{j}^{f}$, and $\sigma_{k}^{b}$ dimensions. At every gradient step, parameters that moved outside the bounds specified in Equation (2) were set to these bounds. Upon convergence, that is, when the relative change in the value of the objective function became less than 10−6, one small foreground peak was eliminated or a pair of closely positioned foreground peaks was merged, and the resulting set of peaks was re-optimized. This procedure was continued until there were no peaks left that passed the following heuristic criteria: (1) a single foreground peak is marked for elimination if the peak amplitude is less than 0.3, and (2) a pair of overlapping foreground peaks is marked for merger if distance between the peaks is less than 1.0 μm or overlap area of the peaks exceeds 50% of either area. Here, the threshold of 0.3 was set to exclude small profile peaks that result from fluctuations of intensity along the axon. This threshold was chosen to be significantly lower than the mean profile intensity, which is one according to Equation (6). Distance threshold of 1.0 μm (size of a small bouton, see e.g. Figure 3) and threshold on inter-peak overlap were introduced to merge peaks corresponding to the same varicosity.

### Matching putative boutons across imaging sessions

Custom software was used to match putative boutons over time. Because most large boutons remains stable over weeks to months, they can serve as fiducial points to match the remaining boutons. Here, piecewise linear registration of normalized intensity profiles was performed based on few fiducial boutons marked by users across imaging sessions (Figure 6—figure supplement 1). This was followed by matching the remaining putative boutons with a greedy, distance-based algorithm. All results were then validated with visual inspection. For putative boutons detected in some, but not all imaging sessions the missing bouton weights were filled in with the normalized intensity profile values at the corresponding registered positions. This procedure was performed for axons traced by different users (Figure 2—figure supplement 2), axons repeatedly imaged under different conditions (Figure 5), and axons monitored in the long-term imaging experiment (Figure 6).

### Quantifying precision of bouton detection methodology

Small inaccuracies in layout of axon traces can introduce errors in bouton detection. Therefore, it is essential to verify that trace optimization can guarantee sufficiently high precision in bouton detection. For this test, putative boutons were detected automatically, both with and without trace optimization, on the same set of 16 axon segment traced manually by five users. In the absence of trace optimization, a total of 578 candidate bouton sites were identified and matched across all five user traces (Figure 2—figure supplement 2A). A candidate bouton site here is defined as a position on an axon where a putative bouton was detected based on at least one user trace. For the majority of candidate bouton sites, 348 (60%), a putative bouton was present in all five user traces, and thus, there was a full consensus in bouton detection. However, 141 (24%) candidate bouton sites had one conflict and 89 (16%) had two. A conflict is defined as a dissent from the majority, and given five traces, the maximum number of conflicts is two. In contrast, after trace optimization, 474 candidate bouton sites were detected, of which 409 (86%) had full consensus, 39 (8%) had one conflict, and 26 (6%) had two (Figure 2—figure supplement 2B). With trace optimization, it was possible to obtain complete agreement in all putative boutons of weights greater than 2.5. This is a marked improvement over bouton detection with no trace optimization where 17 putative boutons of weights greater than 2.5 had one or more conflicts.

Tracing inaccuracies also affect the weights of detected putative boutons. Figure 2—figure supplement 2C, shows that inaccurate manual traces can contribute to bias (slope difference from 1) and variance (deviation from the best fit line) in bouton weight, and that trace optimization significantly reduces such errors. To quantify the uncertainty in bouton weight we calculated root mean square (RMS) weight difference for putative boutons detected with no conflicts (Figure 2—figure supplement 2D). As was expected, trace optimization dramatically reduces this uncertainty in the entire range of bouton weights.

We would like to point out that some amount of uncertainty in bouton detection (Figure 2—figure supplement 2B) and measurement (Figure 2—figure supplement 2D) remains even after trace optimization. However, as shown in Figure 5A–C this uncertainty of the method is much smaller than variability originating from the experimental sources, and therefore, it is not a limiting factor in structural plasticity measurements.

### Implementation

Axons of fluorescently labeled neurons were traced by using the manual tracing module of NCTracer software (http://www.neurogeometry.org). Custom software written in MATLAB, BoutonAnalyzer (Gala et al., 2017; copy archived at https://github.com/elifesciences-publications/BoutonAnalyzer), was used to optimize the traces, generate intensity profiles, detect putative boutons, and match these boutons across multiple user traces and imaging sessions. BoutonAnalyzer enables the user to visually inspect the results of bouton detection and matching and edit them if necessary. The NeuroMorph Centerline Processing and NeuroMorph Measurement tools were used to measure axon cross-section areas, bouton and mitochondrial volumes, and PSD surface areas (Jorstad and Knott, 2017). A copy is archived at https://github.com/elifesciences-publications/NeuroMorph.

### Data availability

Data used in the CLEM experiment are available in the Dryad Digital Repository (https://dx.doi.org/10.5061/dryad.3q50t). This dataset includes a 2PLSM image stack in TIFF format (Figure 3A), optimized traces of four axon segments in SWC format (Figure 3A), and 3D EM reconstructions of these axons in Blender format (Figure 3C).
