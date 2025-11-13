# Advances in X-ray free electron laser (XFEL) diffraction data processing applied to the crystal structure of the synaptotagmin-1 / SNARE complex

## Authors

- Artem Y Lyubimov<sup>1</sup>
- Monarin Uervirojnangkoorn<sup>1</sup>
- Oliver B Zeldin<sup>1</sup>
- Qiangjun Zhou<sup>1</sup>
- Minglei Zhao<sup>1</sup>
- Aaron S Brewster<sup>6</sup>
- Tara Michels-Clark<sup>6</sup>
- James M Holton<sup>6</sup>
- Nicholas K Sauter<sup>6</sup>
- William I Weis<sup>1</sup> †
- Axel T Brunger<sup>1</sup> ([ORCID: 0000-0001-5121-2036](https://orcid.org/0000-0001-5121-2036)) †

### Affiliations

1. Department of Molecular and Cellular Physiology Stanford University Stanford United States
2. Neurology and Neurological Science Stanford University Stanford United States
3. Structural Biology Stanford University Stanford United States
4. Photon Science Stanford University Stanford United States
5. Howard Hughes Medical Institute Stanford University Stanford United States
6. Molecular Biophysics and Integrated Bioimaging Division Lawrence Berkeley National Laboratory Berkeley United States
7. Stanford Synchrotron Radiation Lightsource SLAC National Accelerator Laboratory Menlo Park United States
8. Department of Biochemistry and Biophysics University of California, San Francisco San Francisco United States

† Corresponding author

## Abstract

X-ray free electron lasers (XFELs) reduce the effects of radiation damage on macromolecular diffraction data and thereby extend the limiting resolution. Previously, we adapted classical post-refinement techniques to XFEL diffraction data to produce accurate diffraction data sets from a limited number of diffraction images (Uervirojnangkoorn et al., 2015), and went on to use these techniques to obtain a complete data set from crystals of the synaptotagmin-1 / SNARE complex and to determine the structure at 3.5 Å resolution (Zhou et al., 2015). Here, we describe new advances in our methods and present a reprocessed XFEL data set of the synaptotagmin-1 / SNARE complex. The reprocessing produced small improvements in electron density maps and the refined atomic model. The maps also contained more information than those of a lower resolution (4.1 Å) synchrotron data set. Processing a set of simulated XFEL diffraction images revealed that our methods yield accurate data and atomic models.

## Introduction

X-ray free electron laser (XFEL) crystallography is an emerging technique for obtaining high-resolution diffraction data from macromolecular crystals (Schlichting, 2015). Diffraction data from an XFEL pulse lasting only tens of femtoseconds are largely free from X-ray induced radiation damage that might otherwise affect the success of crystallographic phasing and atomic model refinement. However, the crystal is effectively stationary during the XFEL pulse, which complicates determination of the crystal lattice model from the resulting zero-rotation or 'still' diffraction images. Furthermore, the XFEL pulse destroys or damages the illuminated crystal volume and thus allows only a single diffraction image to be collected. This effect is exacerbated by the variation in intensity and spectrum of the incident XFEL beam produced by the self-amplified spontaneous emission (SASE) process (Bonifacio et al., 1994; Emma et al., 2010). Together, these features cause significant image-to-image variability in the diffraction data (Hattne et al., 2014; Kern et al., 2012; Lyubimov et al., 2016; Sauter, 2015) and therefore pose challenges for data processing. Early XFEL diffraction data sets were processed exclusively using 'Monte Carlo' summation methods (Kirian et al., 2010), which required large numbers of diffraction images.

Previously, we described a program, PRIME, that uses post-refinement techniques to improve the scaling and merging of XFEL data sets obtained from relatively small numbers (100–2000) of diffraction patterns (Uervirojnangkoorn et al., 2015). This method, and similar methods described by others (Kabsch, 2014; Kroon-Batenburg et al., 2015; White, 2014; Ginn et al., 2015a) were applied to diffraction data of crystals of known structure (White, 2014; Kabsch, 2014; Lyubimov et al., 2015; Murray et al., 2015; Ginn et al., 2015b). We subsequently successfully applied our methods to the previously unknown crystal structure of the complex between synaptotagmin-1 (Syt1) and the neuronal SNARE complex, which mediates the fusion of synaptic vesicles with the synaptic membrane and is essential for Ca2+-dependent neurotransmitter release (Zhou et al., 2015). We had only a limited number of relatively large, plate-like crystals available that were not suitable for liquid jet experiments, so the XFEL diffraction data were collected on the goniometer setup implemented at the X-ray Pump Probe (XPP) endstation of the Linac Coherent Lightsource (LCLS) at SLAC National Accelerator Laboratory (Cohen et al., 2014).

To date, several structures have been determined using relatively small numbers of diffraction images obtained from crystals of known structure that diffracted to high resolutions (Cohen et al., 2014; Lyubimov et al., 2015; Uervirojnangkoorn et al., 2015; Hirata et al., 2014; Suga et al., 2015). Although valuable as test cases for methods development, they were not challenging enough to test the limits of XFEL data processing methods. In contrast, the Syt1–SNARE XFEL diffraction data set contained two crystal forms indistinguishable by visual inspection and had a limiting resolution of ~3.5 Å. These diffraction data required us to improve our data processing methods.

Here we describe improvements to PRIME (Uervirojnangkoorn et al., 2015) and other parts of the data processing system. We reprocessed the XFEL diffraction data of the Syt1–SNARE complex, which resulted in small improvements to the data and the atomic model refined against these data. We verified the accuracy of these improved methods by processing a simulated a XFEL diffraction data set that mimicked the Syt1–SNARE XFEL experiment. We also compared the reprocessed XFEL diffraction data set to a synchrotron diffraction data set collected from a similar Syt1–SNARE crystal. The synchrotron data extended to lower resolution (4.1 Å) and consequently provided less detailed electron density maps. Nonetheless, comparison with XFEL-derived maps calculated to 4.1 Å resolution showed that the XFEL maps were slightly more interpretable. We conclude that our methods have general applicability to XFEL diffraction data processing.

## Results and discussion

### Reprocessing the 3.5 Å XFEL diffraction data of the Syt1–SNARE complex

As previously described (Zhou et al., 2015), we used the program cctbx.xfel (Hattne et al., 2014) to index and integrate the observed XFEL diffraction images of crystals of the Syt1-SNARE complex. We performed a grid search of spot-finding parameters on an image-to-image basis to maximize the success of indexing and integration (Lyubimov et al., 2016). We divided the diffraction images into individual clusters based on their crystal symmetry and unit cell parameters using hierarchical clustering (Andrews and Bernstein, 2014; Zeldin et al., 2015). Using the largest cluster, we employed post-refinement as implemented in the program PRIME (Uervirojnangkoorn et al., 2015) to generate a merged diffraction data set from the relatively limited number of diffraction images. Two previously unpublished features were necessary to obtain the best results possible at the time, and are described in detail in the methods. First, the crystal lattice model refinement algorithm in cctbx.xfel was enhanced in order to minimize instances of mis-indexing. Second, an improved scaling procedure was implemented in PRIME.

Subsequent to the original publication (Zhou et al., 2015), we further enhanced the data processing methods. We combined the IOTA grid search method (Lyubimov et al., 2016) with new features including automatic rejection of images that had no discernible diffraction, the ability to use information about the Bravais lattice and unit cell dimensions from other data, and detection of mis-indexed images. We also implemented a graphical user interface for the processing of XFEL diffraction images. As described in the Materials and methods, the cctbx.xfel algorithms were also modified to allow refinement of parameters such as detector position and tilt. Finally, we introduced a feature to include reflections with negative intensity measurements in merging and post-refinement with PRIME.

We reprocessed the XFEL diffraction data of the Syt1–SNARE complex at 3.5 Å resolution to take advantage of all improvements implemented since the original publication (Zhou et al., 2015). Of the 789 diffraction images collected from 148 crystals, 362 images were indexed in the 'long unit cell' crystal form (see Materials and methods); this was the largest of the unit cell 'clusters' determined by the Andrews-Bernstein algorithm (Andrews and Bernstein, 2014 ; Zeldin et al., 2015). Of these, 328 images could be successfully integrated. Of the 328 integrated images, 15 were rejected during post-refinement, and the remaining 313 were merged into the final scaled data set (Table 1A).

**Table 1.**
 Data processing and refinement statistics for the synchrotron, XFEL, and simulated XFEL diffraction data.


<table>
  <thead>
    <tr>
      <th></th>
      <th>A. XFEL (SLAC-LCLS)</th>
      <th>B. Synchroton (APS-NECAT)</th>
      <th>C. Simulated XFEL (nanoBragg)</th>
      <th>D. XFEL - Exclusion of negative intensities</th>
      <th>E. XFEL - Exclusion of high resolution reflections</th>
      <th>F. XFEL - Exclusion of low resolution reflections</th>
      <th>G. Simulated XFEL – Exclusion of negative intensities</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>No. images</td>
      <td>313</td>
      <td>450</td>
      <td>432</td>
      <td>297</td>
      <td>316</td>
      <td>304</td>
      <td>432</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
      <td>P212121</td>
    </tr>
    <tr>
      <td>Cell dimensions* a, b, c (Å)</td>
      <td>69.5, 171.0, 291.3</td>
      <td>68.8, 169.7, 286.8</td>
      <td>69.4, 170.4, 291.0</td>
      <td>69.4, 170.4, 291.0</td>
      <td>69.5, 171, 291.4</td>
      <td>69.6, 171, 291.4</td>
      <td>69.4, 170.4, 291.0</td>
    </tr>
    <tr>
      <td>Resolution† (Å)</td>
      <td>20.0–3.5 (3.56–3.50)</td>
      <td>50.0–4.1 (4.21–4.10)</td>
      <td>20.0–3.5 (3.56–3.50)</td>
      <td>20.0–3.5 (3.56–3.50)</td>
      <td>20.0 – 4.1 (4.17–4.10)</td>
      <td>10.0 – 3.5 (3.56–3.50)</td>
      <td>20.0–3.5 (3.56–3.50)</td>
    </tr>
    <tr>
      <td>Data cutoff [I / σ(I)]</td>
      <td>−3</td>
      <td>−3</td>
      <td>−3</td>
      <td>.5</td>
      <td>−3</td>
      <td>−3</td>
      <td>.5</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>97.8 (89.2)</td>
      <td>98.1 (99.1)</td>
      <td>99.8 (99.1)</td>
      <td>87.8 (58.4)</td>
      <td>95.8 (84.2)</td>
      <td>88.3 (58.0)</td>
      <td>99.1 (95.5)</td>
    </tr>
    <tr>
      <td>Multiplicity (rotation) ‡</td>
      <td>--</td>
      <td>3.3 (3.4)</td>
      <td>--</td>
      <td>--</td>
      <td>--</td>
      <td>--</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Multiplicity (still) ‡</td>
      <td>6.1 (2.9)</td>
      <td>--</td>
      <td>9.5 (6.7)</td>
      <td>4.4 (1.67)</td>
      <td>5.8 (3.1)</td>
      <td>4.3 (1.7)</td>
      <td>8.4 (4.8)</td>
    </tr>
    <tr>
      <td colspan="8">Post-refinement parameters</td>
    </tr>
    <tr>
      <td>Linear scale factor G0</td>
      <td>2.8</td>
      <td>--</td>
      <td>1.9</td>
      <td>2.9</td>
      <td>3.9</td>
      <td>2</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td>B</td>
      <td>66.8</td>
      <td>--</td>
      <td>39.3</td>
      <td>73.1</td>
      <td>71.3</td>
      <td>59.9</td>
      <td>30.1</td>
    </tr>
    <tr>
      <td>γ0 (Å−1)</td>
      <td>0.00024</td>
      <td>--</td>
      <td>0.00027</td>
      <td>0.00016</td>
      <td>0.00015</td>
      <td>0.0014</td>
      <td>0.00032</td>
    </tr>
    <tr>
      <td>γe (Å−1)</td>
      <td>0.00627</td>
      <td>--</td>
      <td>0.00270</td>
      <td>0.00483</td>
      <td>0.00498</td>
      <td>0.0639</td>
      <td>0.00225</td>
    </tr>
    <tr>
      <td>Average Tpr</td>
      <td>169.8</td>
      <td>--</td>
      <td>90.7</td>
      <td>157.22</td>
      <td>119.8</td>
      <td>125.6</td>
      <td>74.8</td>
    </tr>
    <tr>
      <td>Average Txy (mm2)</td>
      <td>7.3</td>
      <td>--</td>
      <td>1.5</td>
      <td>13.74</td>
      <td>4.1</td>
      <td>5.8</td>
      <td>1.35</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>94.3 (34.2)</td>
      <td>99.9 (63.8)</td>
      <td>99.1 (82.0)</td>
      <td>93.6 (43.4)</td>
      <td>94.3 (71.0)</td>
      <td>94.9 (41.7)</td>
      <td>99.4 (80.2)</td>
    </tr>
    <tr>
      <td>Rmerge(%) (rotation) †</td>
      <td>--</td>
      <td>12.1 (78.8)</td>
      <td>--</td>
      <td>--</td>
      <td>--</td>
      <td>--</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Rmerge(%) (still) †</td>
      <td>49.4 (79.5)</td>
      <td>--</td>
      <td>17.3 (53.0)</td>
      <td>36.8 (33.5)</td>
      <td>38.3 (37.1)</td>
      <td>37.1 (32.8)</td>
      <td>13.0 (31.5)</td>
    </tr>
    <tr>
      <td>I / σ(I)</td>
      <td>3.6 (0.2)</td>
      <td>7.6 (1.8)</td>
      <td>8.1 (1.6)</td>
      <td>4.7 (1.3)</td>
      <td>6.2 (1.8)</td>
      <td>3.5 (1.3)</td>
      <td>8.4 (2.4)</td>
    </tr>
    <tr>
      <td colspan="8">Structure-refinement parameters</td>
    </tr>
    <tr>
      <td>Rwork / Rfree (%)</td>
      <td>29.2/32.9</td>
      <td>28.8/ 29.5</td>
      <td>9.6/11.1</td>
      <td>30.0/33.2</td>
      <td>28.9/33.5</td>
      <td>31.5/34.6</td>
      <td>10.7/12.5</td>
    </tr>
    <tr>
      <td>R.m.s. deviations</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.002</td>
      <td>0.004</td>
      <td>0.002</td>
      <td>0.002</td>
      <td>0.003</td>
      <td>0.002</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>Bond angles (° )</td>
      <td>0.5</td>
      <td>0.7</td>
      <td>0.4</td>
      <td>0.5</td>
      <td>0.6</td>
      <td>0.5</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>No. atoms</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>10578</td>
      <td>10889</td>
      <td>10578</td>
      <td>10578</td>
      <td>10903</td>
      <td>10578</td>
      <td>10578</td>
    </tr>
    <tr>
      <td>Ca2+</td>
      <td>21</td>
      <td>15</td>
      <td>21</td>
      <td>21</td>
      <td>21</td>
      <td>15</td>
      <td>21</td>
    </tr>
    <tr>
      <td>B-factors</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>106</td>
      <td>155</td>
      <td>40</td>
      <td>52</td>
      <td>103</td>
      <td>64</td>
      <td>43</td>
    </tr>
    <tr>
      <td>Ca2+</td>
      <td>88</td>
      <td>149</td>
      <td>27</td>
      <td>33</td>
      <td>77</td>
      <td>43</td>
      <td>28</td>
    </tr>
  </tbody>
</table>

_*The unit cell parameters displayed for XFEL data sets are the mean values of these parameters after post-refinement.† Values in parentheses are for the highest resolution shell.‡ '(rotation)' refers to rotation diffraction data collected at the synchrotron and '(still)'refers to XFEL diffraction data._

As in the originally published Syt1–SNARE structure, we observed strong electron density for many side chains (Figure 1A,B). Our modified data processing methods resulted in small improvements in the refinement statistics of the Syt1–SNARE structure (Table 1A) vs. the originally published structure (Zhou et al., 2015). Moreover, the reprocessed XFEL diffraction data produced slightly more interpretable electron density maps, which in a few cases allowed better modeling of side chain rotamers that were previously difficult to interpret (Figure 1—figure supplement 1). Simulated annealing composite omit maps (Figure 1—figure supplement 2) indicated that the electron densities observed in the XFEL-data derived maps are not likely affected by potential model bias.

![Figure 1.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig1-v2.jpg)

**Figure 1.:** The maps were obtained using (A) the XFEL diffraction data at 3.5 Å resolution; (B) same as (A) but truncated to 4.1 Å resolution in order to match the limiting resolution of the synchrotron data; (C) the simulated XFEL diffraction data set; (D) the synchrotron data set (at 4.1 Å resolution), (E) same as (D) but with the synchrotron data sharpened with Bsharp = −23 Å2 in order to account for the differences in overall B-factors of the corresponding diffraction data sets. All maps were rendered at a contour level of 2.0 σ.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** The maps were obtained using (A) the 3.5 Å XFEL diffraction data as originally published in (Zhou et al., 2015), (B) the reprocessed 3.5 Å XFEL diffraction data and (C) the 4.1 Å synchrotron data. Note that in (C) the salt bridge between R233 and E346 could not be accurately modeled due to poor density. The map in (B) was sharpened with Bsharp = −33 Å2, and the map in (C) was sharpened with Bsharp = −23 Å2 in order to account for the differences in overall B-factors of the corresponding diffraction data sets. All maps were rendered at a contour level of 1.5 σ.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** The maps were obtained using (A) the 3.5 Å XFEL diffraction data; (B) same as (C) but truncated to 4.1 Å resolution in order to match the limiting resolution of (A); (C) the 4.1 Å synchrotron data set and (D) same as (C) but with the synchrotron data set sharpened with Bsharp = −23 Å2 in order to account for the differences in overall B-factors of the corresponding diffraction data sets. All maps were rendered at a contour level of 1.5 σ.

As a further assessment of the Syt1–SNARE XFEL diffraction data reprocessing, we re-refined the most current atomic model against the original XFEL diffraction data, resulting in Rwork = 31.1% and Rfree = 33.6%. Since the original XFEL diffraction data did not include negative intensity measurements, we also re-refined the current model against the reprocessed data set including only reflections with positive measurements. Rwork and Rfree were 1.1% and 0.4% lower, respectively, than those for the original XFEL diffraction data (Table 1D), indicating that the reprocessed data are more accurate than the original data. Inclusion of negative intensity measurements further lowered Rwork and Rfree by 0.8% and 0.3%, respectively, for the reprocessed data (Table 1A), indicating that the inclusion of negative intensities results in a somewhat more accurate model, which could be due to improved data completeness, accuracy, or both.

### Accuracy of data processing with simulated XFEL diffraction images

In order to assess if our improved data processing system could accurately process XFEL still data, we generated a simulated XFEL diffraction data set from the atomic coordinates of the Syt1–SNARE complex (Materials and methods) and processed it with the same methods used for the observed XFEL data. This produced a merged dataset with excellent CC1/2, Rmerge and I / σ(I) values (Table 1C) and good agreement with structure factors calculated from the Syt1–SNARE structure that were used to generate the simulated XFEL data set [CC = 97.5% (88.4% in the high resolution bin), R = 11.8% (35.1% in the high resolution bin)]. The atomic model of the Syt1–SNARE complex was then re-refined against the simulated XFEL dataset, resulting in low R-values (Table 1C) and good agreement with the structure that was used to generate the simulated data set (root-mean-square-difference = 0.11 Å). Moreover, electron density maps computed from the simulated XFEL dataset showed strong features for most side chains (Figure 1C). Thus, our data processing system can produce a reasonably accurate merged diffraction data set from simulated XFEL still images. However, the CC1/2 of the observed XFEL diffraction data and the R values of the corresponding refined atomic model are inferior to those obtained from the simulated XFEL data set (Table 1A). Although this difference might arise from experimental noise, it may also indicate that the simulation does not fully account for certain features of the observed XFEL data.

### Comparison to 4.1 Å synchrotron diffraction data of the Syt1-SNARE complex

We previously reported diffraction data sets from crystals of the Syt1-SNARE complex collected at a microfocus synchrotron beam line using rotation data collection (Zhou et al., 2015). These synchrotron data sets, however, were obtained from a different (short unit cell') crystal form than that for the XFEL-data derived Syt1–SNARE crystal structure (Zhou et al., 2015). Here we have measured a synchrotron data set from a similar crystal in the same long unit cell' crystal form used for the XFEL-data derived structure (Table 1B).

A key difference between the XFEL and synchrotron data is the higher limiting resolution of the XFEL diffraction data (3.5 Å vs. 4.1 Å, Table 1A, B). The synchrotron diffraction data were obtained from a single crystal judged to be the best from a pool screened for optimal diffraction, and 4.1 Å was determined to be the maximum achievable limiting resolution with this particular data set. In contrast, the XFEL diffraction data were obtained from 148 crystals of widely varying quality with limiting resolutions ranging from ~5 Å to 2.9 Å (in 92 cases). Even though only 313 XFEL diffraction images were used in the final merged data set, it had high completeness (97.8%) and good multiplicity (6.1), along with reasonable merging statistics to 3.5 Å resolution (Table 1A). Notably, more diffraction images (450) were used in the synchrotron data set.

For more precise comparison, we re-scaled the synchrotron data to the same isotropic temperature factor (B) value as that of the XFEL data by applying a (sharpening) B factor of −23 Å2. Subsequent re-refinement of the atomic model produced only a slight improvement in the electron density map (Figures 1D,E). We also tested the effect of the different resolution limits of the XFEL and synchrotron data sets by reprocessing the XFEL data truncated to 4.1 Å resolution, followed by atomic model refinement (Table 1E). Although the synchrotron data-derived model refined to a lower Rfree value than the XFEL data-derived model (29.5% vs. 32.9%), the electron density maps calculated from the XFEL data set (Figures 1A,B) generally contained more information than the synchrotron data-derived maps (Figure 1D), even when the latter were sharpened (Figure 1E). The same effect was found using simulated annealing composite omit maps (Figure 1—figure supplement 2), suggesting that the side chain density features of the XFEL data-derived maps are not the result of model bias.

The electron density maps were quantitatively assessed by the real-space correlation coefficient (CC) calculated for each amino acid type (Figure 2). The real-space CCs were calculated using phenix.get_cc_mtz_pdb (Adams et al., 2010) by comparing a likelihood-weighted 2mFo-DFc electron density map with a map calculated from the model. All amino acid types correlate better with the XFEL data-derived map than with the corresponding synchrotron data-derived map (Figure 2A). Additionally, more Ca2+ were visible in the XFEL-data derived maps (21 Ca2+) than in synchrotron-data derived maps (15 Ca2+). The 13 Ca2+ that were in matching positions in both maps had higher real-space CCs in the XFEL-data derived structure (Figure 2C). Similar, but somewhat less pronounced results were obtained when calculating the real-space correlation coefficients from the simulated annealing composite omit maps (Figure 2—figure supplement 1).

![Figure 2.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig2-v2.jpg)

**Figure 2.:** (A) Real-space correlation coefficients for atomic models of the Syt1–SNARE complex refined against the XFEL (XFEL 3.5 Å, XFEL 4.1 Å) and synchrotron [Synchrotron 4.1 Å, Synchrotron 4.1 Å (sharpened)] diffraction data and analyzed by amino acid residue type; (B) differences between real-space correlation coefficients of the atomic models (ΔCC) refined against the XFEL and synchrotron diffraction data of Syt1–SNARE complex, both processed and refined at 4.1 Å resolution; (C) real-space correlation coefficients for the Ca2+ sites that were visible in the XFEL- and synchrotron-data derived Syt1–SNARE crystal structures (due to the different numbering of calcium ions in XFEL- and synchrotron-derived structures, two chain and atom labels are given for each, e.g. “F502 / L1”; the first label refers to the XFEL-derived structure, while the second label refers to the synchrotron-derived structure). To facilitate the comparison, the XFEL-based correlation coefficients were calculated at a limiting resolution of 4.1 Å (matching the limiting resolution of the synchrotron data set) as well as at the actual limiting resolution of the XFEL diffraction data set (3.5 Å). Furthermore, the electron density maps obtained from the synchrotron data were sharpened with Bsharp = −23 Å2 in order to account for the difference in overall B-factors of the diffraction data sets.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Real-space correlation coefficients for atomic models of the Syt1–SNARE complex refined against the XFEL (XFEL 3.5 Å, XFEL 4.1 Å) and synchrotron [Synchrotron 4.1 Å, Synchrotron 4.1 Å (sharpened)] diffraction data and analyzed by amino acid residue type; (B) differences between real-space correlation coefficients of the atomic models (ΔCC) refined against the XFEL and synchrotron diffraction data of Syt1–SNARE complex, both processed and refined at 4.1 Å resolution; (C) real-space correlation coefficients for the Ca2+ sites that were visible in the XFEL- and synchrotron-data derived Syt1–SNARE crystal structures. To facilitate the comparison, the XFEL-based correlation coefficients were calculated at a limiting resolution of 4.1 Å (matching the limiting resolution of the synchrotron data set) as well as at the actual limiting resolution of the XFEL diffraction data set (3.5 Å). Furthermore, the electron density maps obtained from the synchrotron data were sharpened with Bsharp = −23 Å2 in order to account for the difference in overall B-factors of the diffraction data sets.

Although the differences between XFEL and synchrotron data sets may be due to differences in radiation damage sustained by the crystals during X-ray exposure, they may have arisen from batch-to-batch differences in crystal quality, individual crystal-to-crystal variability, differences in data collection strategy, or a combination of all these factors. Further studies will be required to determine whether XFELs can improve upon the diffraction data obtained from synchrotrons.

### Conclusions

Advances to our XFEL diffraction data processing system resulted in somewhat better statistics of a diffraction data set and refined atomic model for the crystal structure of the Syt1–SNARE complex than that previously reported (Zhou et al., 2015). Compared with a lower resolution synchrotron diffraction data set obtained from similar crystals in the same crystal form, the electron density maps calculated from the XFEL data contained more information, especially for many side chains. However, the statistics of the XFEL diffraction data (CC1/2) and refined atomic model (Rwork and Rfree) are still inferior to those obtained from synchrotron data (Table 1). The accuracy of a merged data set obtained from simulated XFEL diffraction images (Table 1) and the accuracy of an atomic model that was refined against it indicate that the differences in refinement statistics cannot be explained by an inability to adequately recover partiality and scaling information from a 'perfect' XFEL diffraction data set. We expect that further improvements in modeling the properties of XFEL diffraction data (Hattne et al., 2014; Lyubimov et al., 2016; Sauter, 2015), such as pulse-to-pulse variation in the SASE spectrum (Emma et al., 2010; Bonifacio et al., 1994), along with different modes of XFEL beam generation (Amann et al., 2012), should further improve the statistics of the XFEL diffraction data and ultimately approach those of synchrotron crystallography.

## Materials and methods

### Crystallization of the Syt1–SNARE complex

Construct design, cloning, expression, purification and crystallization of the Syt1–SNARE complex have been previously described (Zhou et al., 2015), and are briefly summarized here. Crystallization took 1–3 months, making the optimization of the crystals a difficult and time-consuming process. All crystals appeared as single plates approximately 25 × 250 × 500 μm3 and were mounted using 0.4–0.7 mm cryo-loops. Due to surface tension, the mounted crystals rested in the same plane as the cryo-loops. The mounted crystals were flash-cooled in a cryo-protecting solution containing the same constituents as the crystallization condition (20 mM Tris-HCl pH 8.0, 300 mM NaCl, 100 mM MgCl2, 1 mM CaCl2, and 0.5 mM TCEP in the protein buffer and 100 mM HEPES-Na pH 7.5 and 1% PEG 8000 in the reservoir buffer) supplemented with 35% (v/v) sucrose. The Syt1–SNARE complex crystallizes in two distinct crystal forms with morphologies that were indistinguishable by inspection of the crystals. As one of these crystal forms arose by the doubling of a single axis of the other crystal form, we term these 'long unit cell' and 'short unit cell' crystal forms, respectively (Zhou et al., 2015; Zeldin et al., 2015; Lyubimov et al., 2016).

### XFEL data collection

Collection of the Syt1–SNARE XFEL diffraction data has been described (Zhou et al., 2015) and is briefly summarized here. The XFEL data were collected at the X-ray Pump Probe (XPP) endstation of the Linac Coherent Light Source (LCLS) at the SLAC National Accelerator Laboratory, using a goniometer-based fixed target sample delivery station and an automatic sample loading system similar to the setup used for conventional synchrotron data collection at SSRL (Cohen et al., 2002, 2014). We used a 30 μm XFEL beam with a pulse duration of 40 fs in SASE mode. We calculated the centroid of the SASE energy spectrum and used this value for the wavelength input to post-refinement of each diffraction image. Each 40 fs XFEL pulse at the XPP endstation at LCLS delivers approximately 1012 photons, depositing a dose of 0.5 MGy. A total of 148 crystals were screened, yielding 789 images with usable diffraction.

### Simulated XFEL data

To better understand some of the persistent problems found when integrating the intensities of XFEL data, we simulated XFEL diffraction images (Table 2, Figure 3) from the previously deposited structure of the Syt1–SNARE complex (PDB ID 5CCG). We calculated structure factors from these coordinates to 3.0 Å resolution with bulk solvent model parameters k_sol = 0.3 e/Å3 and B_sol = 50 Å2 using CNS (Brunger et al., 1998). XFEL still diffraction images were simulated using the program nanoBragg (http://bl831.als.lbl.gov/~jamesh/nanoBragg/) with parameters shown in Table 2. These parameters were optimized using a brute-force grid search scored by the Pearson correlation coefficient between the simulated image and a single observed XFEL diffraction image with a high number of strong, well-resolved Bragg peaks, hand-selected from the Syt1–SNARE complex XFEL data set. To expedite the comparisons, pixels far from observed spots were excluded using a mask derived from blurring the background-subtracted real image. The point-spread function of the fiber-coupled CCD detector was implemented as described previously (Holton et al., 2012), and the conventional mosaic spread (Helliwell et al., 1982) was represented by 675 discrete mosaic domains distributed isotropically and randomly over a spherical cap with diameter 0.2 deg. Beam divergence and dispersion were simulated using four discrete source points, separated by the desired divergence, each emitting six discrete wavelengths evenly spaced across the desired spectral width (Table 2). The experimentally observed X-ray background was extracted with the fastBragg companion program nonBragg using a median-filtered azimuthal average for constant-resolution rings of pixels. This radial profile was subsequently used to simulate the X-ray background level. Finally, a hand-drawn beam stop shadow was applied to the simulated images. Apart from the random number seed used to generate noise, the final 432 simulated XFEL diffraction images varied from each other only in crystal orientation and the beam intensity, which were randomized shot-to-shot.

**Table 2.**
 Diffraction parameters for generation of the simulated XFEL diffraction data.


<table>
  <thead>
    <tr>
      <th>Parameters</th>
      <th>Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Beam size (μm)</td>
      <td>30</td>
    </tr>
    <tr>
      <td>Spectral dispersion (Δλ/λ,%)</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>Wavelength jitter (%)</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>Intensity jitter* (%)</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Beam center X, Y (mm)</td>
      <td>160.53, 182.31</td>
    </tr>
    <tr>
      <td>Misset angles (°)</td>
      <td>96.95, −52.09, −32.52</td>
    </tr>
    <tr>
      <td>Detector distance (mm)</td>
      <td>299.82</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>1.304735</td>
    </tr>
    <tr>
      <td>Mosaicity (°)</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>Divergence (mrad)</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>Dispersion (%)</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>Unit cell dimensions (a, b, c) (Å)</td>
      <td>69.6 171.1 291.9</td>
    </tr>
    <tr>
      <td>Mosaic domain size (μm)</td>
      <td>0.96 × 1.0 × 1.1</td>
    </tr>
  </tbody>
</table>

_* Intensities were modeled using a Gaussian distribution with mean of 2 × 1012 photons/pulse and FWHM of 2 × 1012 photons/pulse._

![Figure 3.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig3-v2.jpg)

**Figure 3.:** The insets show close-up views of the indicated regions.

### XFEL diffraction data reprocessing

The experimental and the simulated XFEL diffraction images were indexed and integrated using identical procedures (Figure 4). We used cctbx.xfel (Hattne et al., 2014) with the improvements outlined below, along with the latest version of IOTA (Lyubimov et al., 2016), which enabled proper processing of a few additional diffraction images that had been previously mis-indexed. A hierarchical clustering algorithm (Andrews and Bernstein, 2014; Zeldin et al., 2015) was used to separate the two crystal forms found in the experimental XFEL diffraction images. Integrated diffraction images were scaled, merged and post-refined using PRIME (Uervirojnangkoorn et al., 2015) with improvements in scaling as outlined below.

![Figure 4.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig4-v2.jpg)

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Section of an XFEL diffraction image shown with overlaid integration prediction obtained with the LABELIT method implemented in cctbx.xfel (Hattne et al., 2014) and B) DIALS methods (Waterman et al., 2016) recently implemented in cctbx.xfel. A single reflection with incorrect (A, inset) and correct (B, inset) corresponding integration prediction was selected to illustrate how the new crystal lattice refinement approach implemented in DIALS results in a significant improvement of the integrated intensities. Initial spot-finding results are marked as clusters of red squares, integration masks as clusters of teal squares, and pixels used for background calculation as clusters of yellow squares.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** The L-tests were performed using phenix.xtriage (Zwart et al., 2005) for the (A) synchrotron data set, (B) observed XFEL data set with $I/\sigma(I)>0.5$, (C) observed XFEL data set with $I/\sigma(I)>−3.0$, (D) simulated XFEL data set with $I/\sigma(I)>0.5$ and (E) simulated XFEL data set with $I/\sigma(I)>−3.0$. All L-tests are shown for the data sets at their respective limiting resolutions (corresponding to Table 1).

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Each diffraction image was indexed and integrated using every possible combination of the two spot-finding parameters; only the selected optimal integration results (one per each image) were used to construct the heat map. The color of each square represents the number of optimally integrated diffraction images (shown inside each square) for this combination of spot-finding parameters. Parameter distributions for A) experimental XFEL and B) simulated XFEL diffraction data are shown (corresponding to Table 1, columns A, C). Note the much wider distribution in experimental vs. simulated XFEL diffraction data, illustrating the image-to-image variability of serial XFEL diffraction data sets, which necessitated the grid search approach.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Direct beam coordinates obtained from (A) diffraction images integrated using default direct beam coordinate refinement radius (4.0 mm) and (B) diffraction images integrated using a restricted default direct beam coordinate search area (0.5 mm). Note the bimodal distribution of direct beam coordinate sets (filled grey circles) clustered around the median (filled yellow circle) and outlier (filled red circles) clustered within a distance (~1.4 mm) approximately corresponding to the length of the c-axis (~292 Å, open blue circle), which indicates incorrect assignment of Miller indices (mis-indexing).

### Improvements to indexing, integration, and scaling

Several previously unpublished improvements to the core modules of the cctbx.xfel suite of software were required in order to successfully index and integrate diffraction images obtained from the Syt1–SNARE crystals using XFEL radiation:

### Indexing and integration of the XFEL diffraction images

Typically, when processing XFEL diffraction data of a known system using cctbx.xfel, one would supply the known crystal symmetry and unit cell data as target parameters in order to better guide the lattice model refinement. However, this approach is not suitable for a system such as Syt1–SNARE complex, where a batch typically contains crystals in two related, but distinct orthorhombic unit cells (Zhou et al., 2015). In this case, using a single target unit cell to process diffraction data from two similar crystal forms would be inappropriate, as incorrect unit cell parameters could be forced upon images. Furthermore, since the Syt1–SNARE complex structure was unknown at the time, and the only information about the unit cell parameters was from lower-resolution synchrotron diffraction data, we were not confident that the available unit cell information would apply to the XFEL diffraction data set. To circumvent these difficulties, we utilized a multi-step data processing strategy (Figure 4).

We began by pooling all 789 XFEL diffraction images regardless of which crystal form they were from (Figure 4A), and indexed them without supplying any target unit cell parameters (Figure 4B). At this stage, we employed a spot-finding parameter grid search using the program IOTA (Lyubimov et al., 2016), which was specially developed for the purpose of optimizing the processing of XFEL diffraction stills. We used the unit cell information obtained from these indexed diffraction images (Figure 4C) and performed a hierarchical cluster analysis of these unit cells (Andrews and Bernstein, 2014; Zeldin et al., 2015). We then correlated each indexed image with the crystal it was obtained from, and identified 72 crystals that belonged to the 'long unit cell' (a = 69.4 Å, b = 170.8 Å, c = 291.2 Å, α = β = γ = 90°) crystal form (Figure 4D). The 362 diffraction images obtained from these 72 crystals comprised the 'long unit cell' cluster (Figure 4E). Only this crystal form yielded a sufficient number of diffraction images for a complete data set. The remaining 427 images that were either assigned to the 'short unit cell' cluster, could not be indexed, or contained no interpretable diffraction, were excluded from further analysis.

The clustering algorithm produced a set of consensus unit cell parameters that are assigned to the 'long unit cell' cluster. We used these unit cell parameters as a target for the indexing and integration of the 362 'long unit cell'diffraction images. At this stage, we performed an extensive spot-finding parameter grid search (minimum spot area = 2–22 pixels, minimum spot height = 2–15 σ, Figure 4F). Interestingly, this produced a wide range of spot-finding parameters that would yield optimal integration results (Figure 4—figure supplement 3A). An identical grid search carried out for the set of simulated XFEL diffraction images (described below) yielded a much narrower distribution (Figure 4—figure supplement 3B), illustrating the high degree of shot-to-shot variability inherent in XFEL diffraction data.

Of the 362 'long unit cell' diffraction images, 328 images were successfully integrated using the wide grid search parameters, while 34 images could not be integrated for a variety of reasons (insufficient number of Bragg reflections, poor diffraction quality, or un-resolvable multiple lattices). The 328 successfully integrated diffraction images were used as input for scaling, post-refinement and merging using the program PRIME. Of those 328 integrated diffraction images, 15 were rejected during post-processing due to large deviations from refined mean values for unit cell and scaling parameters. The remaining 313 integrated diffraction images were included in the final merged XFEL data set (Figure 4G–I, Table 1A).

### Analysis of refined direct beam coordinates identifies mis-indexed XFEL images

Processing of the simulated XFEL diffraction data set with cctbx.xfel revealed occasional incidents of mis-indexing by a shift of a Miller index by ± 1. Since even a few mis-indexed frames can adversely affect the statistics of a merged diffraction data set, a diagnostic tool to detect them early would be desirable. We found that a plot of the refined direct beam coordinates can identify mis-indexed diffraction images in the experimental XFEL data set (Figure 4—figure supplement 4).

We have shown previously that probable position(s) for the direct beam position on the detector can be deduced from the periodic repeat of bright spots (Sauter et al., 2004), given an initial estimate of the beam position derived from the refined detector metrology (Hattne et al., 2014). Probability maps for the direct beam position have been useful for data collected at synchrotron beamlines, in cases where the beam position is not correctly recorded with the image metadata. Searching for probable beam positions up to a radius of 4 mm around the initial position allows the indexing program LABELIT to estimate the true position. However, we found it counterproductive to apply such a wide beam search to XFEL data. Firstly, at the XPP endstation the beam position with respect to the detector is known within ± 100 μm. Secondly, allowing a large search radius can potentially identify an incorrect beam position. In the case of the Syt1–SNARE complex XFEL diffraction data, eight mis-indexed frames exhibited a shift of ~1.5 mm in beam position, corresponding to a shift of one lattice spacing along the long c-axis (291 Å, Figure 4—figure supplement 4A). We therefore limited the beam search scope to a radius of 0.5 mm. Under this condition only two XFEL diffraction images remained mis-indexed (Figure 4—figure supplement 4B), and were therefore omitted from the merged diffraction data set.

### Scaling, post-refinement, and merging of the XFEL data sets

Integrated XFEL images in the long unit cell cluster were scaled, post-refined and merged with PRIME, which corrects partially recorded intensities to their full intensity values using a partiality model (Uervirojnangkoorn et al., 2015). This step begins with the generation of the initial reference set, which is in turn used to determine the initial linear scale factor (G0) and the initial temperature factor (B0) for each image. In the original version of PRIME, the initial reference set was obtained by merging the integrated images and scaling them to the mean intensity of these images (referred to as mean-intensity scaling') (Uervirojnangkoorn et al., 2015). Our new approach scales each diffraction image to the intensity distribution calculated assuming a random distribution of atoms in the unit cell, i.e., a Wilson plot, generated using the scattering factors of atoms with the temperature (B) factor equal to zero and the contents of the asymmetric unit. For each diffraction image, the full intensity of each reflection is calculated using the initial parameters (crystal orientation, unit cell, mosaicity, spectral dispersion; see [Uervirojnangkoorn et al., 2015]). The average of these full intensity estimates is computed for selected reflections (I/σ(I) > 0.5) in equivolume resolution shells to generate an 'observed' Wilson plot, which is fitted to the calculated Wilson plot over the entire resolution range using a linear scale and B factor. Specifically, using the relation

$$
ln\frac{⟨I_{full}(hkl)⟩}{\sumif_{i}(s)}=lnG_{0}−\frac{B_{0}s^{2}}{2}
$$

where $ s$ is $2\frac{sin\theta}{\lambda}$, $I_{full}(hkl)$ is the partiality-corrected observed intensity of Miller index $hkl$, and $f_{i}(s)$ is the scattering factor of atom in each resolution bin, we obtain the initial scale factors ($G_{0}$ and $B_{0}$, i.e., the intercept and slope) that optimally fit $ln\frac{⟨I_{full}(hkl)⟩}{\sum_{i}f_{i}(s) }$ vs. $s.$ All integrated diffraction images were brought to the same scale using these initial scale factors, with all reflections included in the merging step. We note that the non-ideal Wilson behavior of macromolecular diffraction data leads to non-zero values for the B factor of the merged and scaled data set. We refer to this scaling method as 'pseudo-Wilson' scaling.

The next step starts with the pseudo-Wilson scaled and merged data set described earlier as an initial reference and is used to refine crystal orientation, reflection width, and unit-cell parameters. The resolution cutoff was placed where CC1/2 fell below 0.25, yielding a merged data set that was 97.4% complete to 3.5 Å resolution. Post-refinement was performed in ten cycles, and at the end of each cycle a new reference set was generated by applying the new scale factors and diffraction parameters to each diffraction image and re-merging the data set. Completeness and average number of observations of the final merged data set and improvement in terms of CC1/2 from the starting reference set to the final merged data set are illustrated in Figure 5. Wilson plots of the observed intensities before and after mean-intensity scaling and pseudo-Wilson scaling are shown in Figure 5—figure supplement 1A. The convergence behavior of post-refinement parameters (scale factors G and B, reflecting range γ0 and γe, crystal orientation, and unit cell dimensions) and of the refinement target functions (post-refinement target Tpr and spot-position target Txy) are shown in Figure 5—figure supplements 1B–C. Although some parameters continued to change after three cycles, little change occurred in CC1/2 (Figure 5—figure supplement 1B). After scaling each diffraction image using the idealized Wilson model, the B-factor of the initial reference was 29 Å2; the B-factor value changed over the next few cycles until stabilizing at 36 Å2 (Figure 5—figure supplement 1B). As mentioned above, we generalized PRIME in order to include negative intensity measurements in post-refinement.

![Figure 5.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig5-v2.jpg)

**Figure 5.:** (A) Completeness, (B) Average number of partial observations per Miller index, (C) CC1/2, comparing the initial reference set and post-refined data set, (D) I / σ(I).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/18740/elife-18740-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Changes in each parameter and target function are plotted relative to the previous cycles, while the CC1/2 metric and the B-factor are shown as absolute values for each merged data set per cycle starting from the initial reference set. The convergence of the post-refinement parameters and the refinement target functions are shown as box plots. These box plots show the first (Q1) and the third (Q3) quartiles (bottom and top of the blue box), the second quartile (Q2; red line), and the range at a 1.5 interquartile (Q3–Q1; black horizontal lines) for the particular quantity. The plus signs show any data points beyond this range. (A) Overlay of Wilson plots (on a logarithmic scale) for the observed intensities for all diffraction images (top), after mean-intensity scaling, as defined in (Uervirojnangkoorn et al., 2015) (middle), and after pseudo-Wilson scaling (bottom). (B) Convergence of post-refinement and spot-location target functions, the CC1/2 metric, and the overall B-factor of the merged data. (C) Convergence behavior of the all post-refined parameters. In all plots in (B) and (C), the horizontal axis is the post-refinement cycle number.

Taken together, the improvements in XFEL processing methods resulted in better statistics for the XFEL diffraction data set of the Syt1–SNARE complex (Table 1) than previously published (Zhou et al., 2015). In particular, the reprocessed data set was is more complete (97.8% vs. 87.6%, respectively) than the previously published XFEL data set, has a higher multiplicity (6.1 vs. 5.0) and a better CC1/2 (94.3% vs. 92.7%).

### Effects of resolution and signal-to-noise cutoffs

We investigated the effects of applying different filters to the observed XFEL diffraction data prior to post-refinement and merging on the statistics of the merged data set: (a) merging with negative measurements (including all reflections with $I/\sigma(I)>−3$); (b) merging using all reflections with $I/\sigma(I)>0.5$ and omitting reflections higher than 4.1 Å Bragg spacings; and (c) merging using all reflections with $I/\sigma(I)>0.5$ and omitting reflections lower than 10 Å Bragg spacings. Inclusion of the negative intensities slightly improved the merging and refinement statistics (Table 1), improved the L-test (Figure 4—figure supplement 2), and lowered the overall atomic model R values (Table 1). Omitting high- or low-resolution data has a small deleterious effect on the merging statistics (Rmerge and CC1/2) and the corresponding refined atomic models (Table 1), suggesting that the intensity measurements are of roughly the same quality throughout different resolutions. The electron density map generated from the XFEL data set that included negative intensities yielded higher average B-factor than that generated from the reflection set without negative intensities (~100 Å2 vs. ~50 Å2 respectively), but this had no substantial effect on the interpretability of the electron density maps, so the data set with negative intensities included was used for the final refinement of the Syt1–SNARE complex (Table 1).

In contrast to the substantial effect of excluding negative intensities on the L-test statistics of the observed XFEL data, the effect was very small for the simulated XFEL data (Figure 4—figure supplement 2). The effect on merging statistics and R-values of refined atomic models for the simulated XFEL data was similarly small (Table 1), likely due to the much smaller fraction of negative intensities in the simulated XFEL data (4.1%) than in the observed XFEL data (15.8%).

### Synchrotron data collection and processing

Synchrotron data were collected using the shutterless, continuous rotation method at the Northeastern Collaborative Access Team (NE-CAT) beamline at the Advanced Photon Source at Argonne National Lab on a Pilatus 6M detector (Dectris). 80 cryo-cooled crystals were screened and the best diffraction data (in the long unit cell form) were merged from three data sets collected at three different positions on a single crystal using consecutive spindle angles. A 30 μm beam was used throughout the experiment. Each of the three data sets contained 150 diffraction images in 0.2° frames and an exposure time of 0.2 s. The diffraction images were indexed and integrated using XDS (Kabsch, 2010) and scaled and merged using Scala (Evans, 2006).

### Atomic model refinements

The structure of the Syt1–SNARE complex was refined against the merged XFEL diffraction data set to 3.5 Å resolution (Table 1) in a manner similar to that previously described (Zhou et al., 2015). Briefly, the phases for the XFEL crystal structure of Syt1-SNARE complex were determined by molecular replacement with Phaser (McCoy, 2007) using the rat SNARE complex (PDB ID: 1N7S), the rat Syt1 C2A domain (PDB ID: 3F04), and the rat Syt1 C2B domain (PDB ID: 1UOW) as search models. The structure was iteratively rebuilt and initially refined using CNS v1.3 (Brunger et al., 1998), with deformable elastic network (DEN) restraints (Schroder et al., 2014), restrained grouped atomic displacement parameters (ADP) and non-crystallographic symmetry (NCS) restraints, then further refined with phenix.refine (Adams et al., 2010) using NCS restraints, secondary structure restraints, and individual ADP refinement. The unit cell dimensions for refinement were set to the mean values obtained by post-refinement with PRIME. Re-refinement of the Syt1 – SNARE structure against the reprocessed XFEL data resulted in better atomic model Rwork / Rfree values (29.2% / 32.9% vs. 32.2% / 35.3%) than the originally published structure. The final refinement cycle was replicated for the resolution- or intensity-truncated XFEL data sets (Table 1) in order to obtain comparable refinement statistics.

The phases for the synchrotron diffraction data were determined using molecular replacement and refined in the same manner as above. We transferred the test set of reflections for cross-validation that was used for the refinement against the XFEL data. Refined independently from the XFEL-data derived structure, the synchrotron data-derived structure yielded slightly better Rwork / Rfree values than the structure refined against the XFEL diffraction data truncated to the same resolution (4.1 Å) (Table 1).

### Generation of simulated annealing composite omit maps

Composite omit maps were generated in order to reduce the potential effect of model bias (Figure 1—figure supplement 2). The maps were generated using phenix.composite_omit_map (Terwilliger et al., 2008) via the Phenix GUI (Echols et al., 2012), employing a single cycle of Cartesian simulated annealing (starting at 5000 K) to reduce model bias, followed by minimization. We chose to exclude bulk solvent from the omitted regions, as that option appeared to result in stronger omit map features.

### Additional files

The merged XFEL diffraction data (Table 1A) and the merged synchrotron diffraction data (Table 1B) for the Syt1–SNARE complex, along with the corresponding atomic model coordinates have been deposited in the Protein Data Bank (PDB IDs 5KJ7 and 5KJ8, respectively). The merged simulated XFEL diffraction data (Table 1C) and corresponding atomic model coordinates are available as Source Data files. The complete set of raw XFEL diffraction images for the Syt1–SNARE complex will be deposited in the SBGrid data repository.
